---
name: btcc-app
description: BTCC 移动 APP（iOS / Android）专属 skill。用于生成、实现、审查 BTCC APP 页面、组件、token。Web 走 ../btcc-web/，跨平台共享规则走 ../btcc-shared/。
---

# BTCC APP Skill（移动端）

> 三 skill 体系：
> - [`../btcc-shared/`](../btcc-shared/) ← 跨平台共享规则（操作优先 / 颜色即状态 / Unverified 标记 / 数据呈现 / 图标语言）
> - [`../btcc-web/`](../btcc-web/) ← Web 桌面（pill 100 / h48 / Lato + PingFang SC / 9 个 LP 模板族）
> - [`../btcc-app/`](.) ← 本目录：移动 APP（fileKey `GW9kMfpf0Nib5DG4TjoWBp`，待新 Figma 验证）

## 范围

本 skill **仅适用于 BTCC iOS / Android 原生 APP**，不含：
- Web 桌面版 → 走 [`../btcc-web/`](../btcc-web/)
- Web 移动 H5（浏览器内） → 走 [`../btcc-web/pages/h5-mirror.md`](../btcc-web/pages/h5-mirror.md)（H5 是 Web 响应式，规则与 Web 一致）

## ⚠️ 当前状态：等待新 APP Figma 文件

**2026-05-28 状态**：APP Figma `GW9kMfpf0Nib5DG4TjoWBp` 旧版数据保留在 `references/platform-app/`、`assets/`、`scripts/btcc_qa_lint.py` 中。等 han 提供新一轮 APP Figma 后，将整体重做。

在新 Figma 验证完成前，本 skill **所有规则、token、组件几何**均按 R-SHARED-3 视为 **Unverified**：
- 旧文档中的 38px / r6 / 系统字体等 APP 风格参数，**未在 Web 文件中验证**。
- 旧 token `assets/btcc-tokens.css` 是从 APP 推断的早期版本，可能与最新 Figma 不一致。

## 必读顺序

1. [`../btcc-shared/rules-shared.md`](../btcc-shared/rules-shared.md) → 跨平台规则
2. [`references/rules.md`](references/rules.md) → 旧版 SSOT，含 R-COLOR-1（合约方向按钮蓝/红）、R-LAYOUT-1/2、R-NAME-1 等。**注意：当前所有 APP 规则视为 Unverified，等新 Figma 验证。**
3. [`references/platform-app/rules-app.md`](references/platform-app/rules-app.md) → APP 专属规则（旧版本，待重做）
4. 任务相关文件（见下表）

## Task → Files 索引

| 任务 | 必读 |
| --- | --- |
| 生成合约 pro 页面（APP） | `references/rules.md`、`references/platform-app/rules-app.md`、`references/platform-app/for-code-generation/pages-contract.md`、`components-trading.md`、`components-global.md`、`tokens-colors.md`、`tokens-size-typography.md` |
| 修改下单按钮 / 表单 | `references/platform-app/rules-app.md`、`references/platform-app/for-code-generation/components-trading.md`、`tokens-colors.md` |
| 添加杠杆调整器 | `references/platform-app/rules-app.md`、`references/platform-app/for-code-generation/components-trading.md`、`tokens-size-typography.md` |
| 检查 Figma 节点（APP） | `references/platform-app/for-figma-inspect/source-anchors.md`、`contract-screens.md`、`icons.md` |
| 修改 token 值 | `references/platform-app/for-code-generation/tokens-colors.md` 或 `tokens-size-typography.md` |
| 添加未验证页面 | `references/platform-app/for-code-generation/pages-other.md` + Unverified 标记 |
| 写或编辑 prompt | `references/for-prompt-design/prompt-evals.md`、`implementation-patterns.md` |
| 审核 AI 输出 | `references/for-review-and-qa/qa.md`、`golden-examples.md`、`data-format.md` |
| 调 use_figma | `references/for-prompt-design/figma-plugin-pitfalls.md`（必读） |

## 资源

| 资源 | 说明 |
| --- | --- |
| `assets/btcc-tokens.json` | APP 推断的 token JSON（待新 Figma 验证） |
| `assets/btcc-tokens.css` | APP 推断的 token CSS（待新 Figma 验证） |
| `assets/icons/*.svg` | APP 核心 utility icon |
| `scripts/btcc_qa_lint.py` | 旧版 QA lint 脚本（可作为参考，等 APP 重做） |

## Figma 锚点

- File: `新BTCC APP`
- fileKey: `GW9kMfpf0Nib5DG4TjoWBp`
- Token page: `设计规范`
- Global components: `全局组件`
- 主交易参考: `合约pro`
- Component sets: `次级button`、`TabBar 底部标签栏`

## 常见反模式（旧版，待重做）

- ❌ 操作页用营销 LP 版式（违反 R-LAYOUT-1）
- ❌ Open Long 涂绿 / Open Short 不红（违反 R-COLOR-1，**注意：APP / Web 的 R-COLOR-1 是同向规则——蓝/红**）
- ❌ 绿/红用作装饰（违反 R-COLOR-2）
- ❌ 每个 section 都加卡片（违反 R-LAYOUT-2）
- ❌ 价格 / 余额不加 tabular-nums
- ❌ 交易控件用彩色装饰图标
- ❌ 未验证页面不带 Unverified 标记（违反 R-SCOPE-1）
- ❌ 用 `--primary` / `--accent` / 任意十六进制（违反 R-NAME-1）

## 完成检查

完成前：
1. 读 `references/for-review-and-qa/qa.md`、再核对 `references/rules.md` 和 `rules-app.md` 的任何引用规则。
2. 对生成的 web 文件运行 `python skills/btcc-app/scripts/btcc_qa_lint.py <file-or-dir>`（如本地可用）。
3. 检查硬失败项。
4. 说明是否查看了 Figma 源文件。
5. 提及任何 fallback icon、缺失资产、未验证假设（R-SCOPE-1）。
