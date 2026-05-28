#!/usr/bin/env python3
"""Heuristic QA lint for BTCC-style generated web files."""

from __future__ import annotations

import argparse
import re
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


ALLOWED_HEX = {
    "#0C0F12",
    "#13171B",
    "#FFFFFF",
    "#F1F3F5",
    "#878F99",
    "#717C95",
    "#0C73ED",
    "#195EFF",
    "#2CA85D",
    "#EB464F",
    "#E0601F",
    "#F0B848",
    "#8994A3",
    "#84DC1F",
}

TEXT_EXTENSIONS = {
    ".css",
    ".html",
    ".htm",
    ".js",
    ".jsx",
    ".mdx",
    ".svelte",
    ".ts",
    ".tsx",
    ".vue",
}

CONTRACT_HINTS = ("perp", "leverage", "open long", "open short", "order book", "positions")
CONTRACT_REQUIRED = ("order book", "open long", "open short")


@dataclass
class Finding:
    path: Path
    line: int
    code: str
    message: str

    def format(self, root: Path) -> str:
        try:
            display = self.path.relative_to(root)
        except ValueError:
            display = self.path
        return f"{display}:{self.line}: {self.code}: {self.message}"


def iter_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS:
            files.append(path)
        elif path.is_dir():
            for child in path.rglob("*"):
                if child.is_file() and child.suffix.lower() in TEXT_EXTENSIONS:
                    files.append(child)
    return sorted(set(files))


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def lint_file(path: Path) -> list[Finding]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    lowered = text.lower()
    findings: list[Finding] = []

    for match in re.finditer(r"#[0-9a-fA-F]{3,8}\b", text):
        value = match.group(0)
        if value.upper() not in ALLOWED_HEX and not re.fullmatch(r"#[0-9a-fA-F]{3,4}", value):
            findings.append(
                Finding(path, line_number(text, match.start()), "BTCC001", f"arbitrary hex color {value}; map to BTCC semantic tokens")
            )

    for pattern, code, message in (
        ("linear-gradient", "BTCC002", "avoid decorative gradients on operational BTCC surfaces"),
        ("radial-gradient", "BTCC002", "avoid decorative gradients on operational BTCC surfaces"),
    ):
        for match in re.finditer(pattern, lowered):
            findings.append(Finding(path, line_number(text, match.start()), code, message))

    if path.suffix.lower() in {".css", ".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte"}:
        if "--btcc-" not in lowered and "var(--btcc-" not in lowered:
            findings.append(Finding(path, 1, "BTCC003", "no BTCC token usage detected"))
        if "tabular-nums" not in lowered and "font-variant-numeric" not in lowered:
            findings.append(Finding(path, 1, "BTCC004", "numeric surfaces should use tabular numbers"))

    icon_button_patterns = [
        r"<button(?=[^>]*(?:icon|aria-hidden))(?!(?=[^>]*aria-label=))(?!(?=[^>]*title=))[^>]*>",
        r"<button(?!(?=[^>]*aria-label=))(?!(?=[^>]*title=))[^>]*>[\s\S]{0,120}<svg\b",
        r"<Button(?=[^>]*(?:icon|aria-hidden|Icon))(?!(?=[^>]*aria-label=))(?!(?=[^>]*title=))[^>]*>",
        r"<Button(?!(?=[^>]*aria-label=))(?!(?=[^>]*title=))[^>]*>[\s\S]{0,120}<svg\b",
    ]
    for pattern in icon_button_patterns:
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            findings.append(Finding(path, line_number(text, match.start()), "BTCC005", "icon-only buttons need aria-label or title"))

    if any(hint in lowered for hint in CONTRACT_HINTS):
        missing = [term for term in CONTRACT_REQUIRED if term not in lowered]
        if missing:
            findings.append(Finding(path, 1, "BTCC006", f"contract surface missing required terms: {', '.join(missing)}"))
        if "open long" in lowered and "open short" in lowered:
            long_match = re.search(r"<(?:button|Button)[^>]*>[^<]*open long", lowered)
            short_match = re.search(r"<(?:button|Button)[^>]*>[^<]*open short", lowered)
            long_context = long_match.group(0) if long_match else lowered
            short_context = short_match.group(0) if short_match else lowered
            if not re.search(r"(brand|--btcc-brand|--btcc-button-brand|fill/brand|#0c73ed|#195eff)", long_context):
                findings.append(Finding(path, 1, "BTCC007", "Open Long uses fill/Brand (brand blue) in 合约pro; do not switch it to success/green"))
            if not re.search(r"(error|red|--btcc-[\w-]*error|--btcc-[\w-]*short|fill/error|#eb464f)", short_context):
                findings.append(Finding(path, 1, "BTCC008", "Open Short needs error/red semantic styling"))

    marketing_terms = ("hero", "inspirational", "beautiful gradient", "floating card")
    if any(term in lowered for term in marketing_terms) and any(term in lowered for term in CONTRACT_HINTS):
        findings.append(Finding(path, 1, "BTCC009", "contract/trading pages should not use marketing hero structure"))

    return findings


def run(paths: list[Path]) -> tuple[int, list[Finding]]:
    files = iter_files(paths)
    findings: list[Finding] = []
    for file_path in files:
        findings.extend(lint_file(file_path))
    return (1 if findings else 0, findings)


def self_test() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        bad = root / "bad.tsx"
        bad.write_text(
            """
export function Bad() {
  return <main style={{ background: '#7c3aed' }}>
    <section className="hero" style={{ background: 'linear-gradient(red, blue)' }}>
      <button><svg /></button>
      <button>Open Long</button><button>Open Short</button>
      <p>BTCUSDT Perp leverage positions</p>
    </section>
  </main>
}
""",
            encoding="utf-8",
        )
        good = root / "good.tsx"
        good.write_text(
            """
import './btcc-tokens.css'
export function Good() {
  return <main className="btcc tabular-nums" style={{ background: 'var(--btcc-bg-primary)' }}>
    <button aria-label="More"><svg /></button>
    <section>
      <h1>BTCUSDT Perp</h1>
      <p>Order Book</p>
      <button className="bg-[var(--btcc-brand)]">Open Long</button>
      <button className="bg-[var(--btcc-fill-error)]">Open Short</button>
      <p>Positions(0)</p>
    </section>
  </main>
}
""",
            encoding="utf-8",
        )
        bad_findings = lint_file(bad)
        good_findings = lint_file(good)
        expected_codes = {"BTCC001", "BTCC002", "BTCC003", "BTCC004", "BTCC005", "BTCC006", "BTCC007", "BTCC008", "BTCC009"}
        actual_codes = {finding.code for finding in bad_findings}
        missing = expected_codes - actual_codes
        if missing:
            print(f"self-test failed: bad fixture missing {sorted(missing)}", file=sys.stderr)
            for finding in bad_findings:
                print(finding.format(root), file=sys.stderr)
            return 1
        if good_findings:
            print("self-test failed: good fixture produced findings", file=sys.stderr)
            for finding in good_findings:
                print(finding.format(root), file=sys.stderr)
            return 1
    print("self-test passed")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lint generated BTCC-style web files.")
    parser.add_argument("paths", nargs="*", type=Path, help="Files or directories to lint.")
    parser.add_argument("--self-test", action="store_true", help="Run built-in fixtures.")
    args = parser.parse_args(argv)

    if args.self_test:
        return self_test()

    if not args.paths:
        parser.error("provide at least one file/directory or --self-test")

    root = Path.cwd()
    status, findings = run(args.paths)
    for finding in findings:
        print(finding.format(root))
    if findings:
        print(f"{len(findings)} BTCC QA finding(s)", file=sys.stderr)
    return status


if __name__ == "__main__":
    raise SystemExit(main())
