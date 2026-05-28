#!/usr/bin/env python3
"""BTCC Web qa-lint：扫描 HTML / CSS / JSX / TSX / Vue 文件，
检查是否违反 BTCC Web 设计规则（rules.md / rules-shared.md）。

用法：
    python skills/btcc-web/qa-lint.py [path]   # 扫描指定路径，默认当前目录

退出码：
    0  无违规
    1  有违规

规则覆盖：
    R-FONT-WEB    禁用 Helvetica Neue / Inter / SF Pro，必须 Lato + PingFang SC
    R-SHAPE-WEB   一级 button 必须 pill 100 / h48；input 必须 r4 不是 pill
    R-COLOR-WEB-1 现货 / 闪兑 / 资产 不得复用合约 pro 蓝/红方向按钮
    R-TOKEN-WEB   禁用 --btcc-* / --accent / --primary 等非真实 Figma 变量
    R-SHARED-5    数字 / 价格 / 倒计时 / 分页 / 排行榜 应有 tabular-nums
    R-LP-WEB      LP 不得自创版式（仅文档级提示，扫描不到）

仅做静态文本扫描，依赖关键字匹配，不解析 AST。
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Iterable

# 可扫描的源文件后缀
SOURCE_SUFFIXES = {
    ".html", ".htm",
    ".css", ".scss", ".less",
    ".js", ".jsx", ".ts", ".tsx",
    ".vue", ".svelte", ".astro",
}

# 跳过目录（性能 + 噪声）
SKIP_DIRS = {
    "node_modules", ".git", "dist", "build", ".next", ".nuxt",
    "out", "coverage", ".turbo", ".cache", ".pnpm-store",
    "skills",   # 我们自己的 skills 目录里有大量"反模式"示例，不扫
}

# ────────────────────── 规则定义 ──────────────────────

# R-FONT-WEB：禁用字体
RULE_FONT_FORBIDDEN = re.compile(
    r"font-family\s*:\s*[^;]*?\b(Helvetica\s+Neue|Helvetica|Inter|SF\s+Pro|Roboto|Arial)\b",
    re.IGNORECASE,
)

# R-TOKEN-WEB：禁用 token 名
RULE_TOKEN_FORBIDDEN = re.compile(
    r"--(?:btcc-(?:primary|brand|accent|main)|accent|primary-color|brand-color)\b"
)

# R-SHAPE-WEB：CTA button 圆角错误（圆角 6 / 8 / 12 是 APP 风格，Web 是 100 pill）
RULE_BUTTON_RADIUS_BAD = re.compile(
    r"\.(?:btcc-)?btn(?:-primary|-cta)?\s*\{[^}]*?border-radius\s*:\s*(?:6|8|10|12|16)px",
    re.IGNORECASE | re.DOTALL,
)

# R-SHAPE-WEB：input 圆角不能是 pill 100
RULE_INPUT_RADIUS_PILL = re.compile(
    r"\.(?:btcc-)?input\s*\{[^}]*?border-radius\s*:\s*(?:100|9999|999)px",
    re.IGNORECASE | re.DOTALL,
)

# R-SHARED-5：可能需要 tabular-nums 的关键字
RULE_NUMERIC_HINTS = re.compile(
    r"\b(price|amount|balance|countdown|leaderboard|pagination|orderbook|tabular)\b",
    re.IGNORECASE,
)
RULE_HAS_TABULAR_NUMS = re.compile(r"font-variant-numeric\s*:\s*tabular-nums", re.IGNORECASE)

# R-COLOR-WEB-1：合约方向按钮蓝（不应在现货 / 闪兑 / 资产 文件里出现）
RULE_LONG_BLUE_OUTSIDE_FUTURES = re.compile(
    r"open[-_]?long.*(?:#0c73ed|--fill-brand-button-normal)",
    re.IGNORECASE | re.DOTALL,
)


# ────────────────────── 扫描 ──────────────────────

def iter_files(root: Path) -> Iterable[Path]:
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if p.suffix.lower() not in SOURCE_SUFFIXES:
            continue
        # 跳过 SKIP_DIRS
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        yield p


def scan_file(path: Path) -> list[tuple[int, str, str]]:
    """返回 [(line_no, rule_id, message), ...]"""
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return []
    findings: list[tuple[int, str, str]] = []

    # R-FONT-WEB
    for m in RULE_FONT_FORBIDDEN.finditer(text):
        line_no = text.count("\n", 0, m.start()) + 1
        findings.append((line_no, "R-FONT-WEB",
                         f"禁用字体 '{m.group(1)}'：BTCC Web 必须用 Lato + PingFang SC"))

    # R-TOKEN-WEB
    for m in RULE_TOKEN_FORBIDDEN.finditer(text):
        line_no = text.count("\n", 0, m.start()) + 1
        findings.append((line_no, "R-TOKEN-WEB",
                         f"禁用 token 名 '{m.group(0)}'：必须用 --fill-brand-button-normal / --text-icon-primary 等真实 Figma 变量"))

    # R-SHAPE-WEB（button radius）
    for m in RULE_BUTTON_RADIUS_BAD.finditer(text):
        line_no = text.count("\n", 0, m.start()) + 1
        findings.append((line_no, "R-SHAPE-WEB",
                         "一级 button 圆角不应是 6/8/10/12/16px（这是 APP 风格）；Web 必须 pill 100"))

    # R-SHAPE-WEB（input radius pill）
    for m in RULE_INPUT_RADIUS_PILL.finditer(text):
        line_no = text.count("\n", 0, m.start()) + 1
        findings.append((line_no, "R-SHAPE-WEB",
                         "input 圆角不应是 pill 100；Web 必须 r4（方角小圆）"))

    # R-SHARED-5
    if RULE_NUMERIC_HINTS.search(text) and not RULE_HAS_TABULAR_NUMS.search(text):
        # 仅在 css 类文件提示
        if path.suffix.lower() in {".css", ".scss", ".less"}:
            findings.append((1, "R-SHARED-5",
                             "文件含 price/amount/balance/countdown/leaderboard/pagination/orderbook 关键字但未声明 tabular-nums"))

    # R-COLOR-WEB-1
    name_lower = path.name.lower()
    is_futures_context = any(kw in name_lower for kw in ("contract", "futures", "futures-pro", "trading-form"))
    if not is_futures_context:
        for m in RULE_LONG_BLUE_OUTSIDE_FUTURES.finditer(text):
            line_no = text.count("\n", 0, m.start()) + 1
            findings.append((line_no, "R-COLOR-WEB-1",
                             "Open Long 蓝色仅适用于合约 pro；现货 / 资产 / 闪兑 等其它语境应用 success 绿"))

    return findings


def main(argv: list[str]) -> int:
    root = Path(argv[1]) if len(argv) > 1 else Path.cwd()
    if not root.exists():
        print(f"[btcc-web qa-lint] 目录不存在：{root}", file=sys.stderr)
        return 2

    print(f"[btcc-web qa-lint] 扫描根目录：{root}")
    total_files = 0
    total_findings = 0
    for f in iter_files(root):
        total_files += 1
        findings = scan_file(f)
        if not findings:
            continue
        rel = f.relative_to(root) if str(f).startswith(str(root)) else f
        for line_no, rule_id, msg in findings:
            print(f"{rel}:{line_no}  [{rule_id}]  {msg}")
            total_findings += 1

    print(f"\n[btcc-web qa-lint] 共扫描 {total_files} 个文件，发现 {total_findings} 处违规。")
    return 1 if total_findings > 0 else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
