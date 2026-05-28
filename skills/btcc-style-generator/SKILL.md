---
name: btcc-style-generator
description: Use when generating, implementing, reviewing, prompting, or creating Figma designs for BTCC-style crypto exchange web pages, including trading, contract, market, wallet, account, login, register, copy trading, modal, bottom sheet, dashboard, token, icon, or component work.
---

# BTCC Style Generator

## Overview

Generate BTCC interfaces as compact exchange workspaces. The style is dark-first, data-led, operational, and stateful. It should feel like a trading product, not a marketing site.

Read `references/rules.md` first; it is the single source of truth for BTCC golden rules. All other reference files cite back to it and MUST NOT re-state rules as their own prescriptions.

## Required Workflow

1. Identify platform first (single platform per invocation):
   - Signals for **web**: "web", "桌面", "1024", "1440", "1556", "1920", "hover", "focus ring", "鼠标"
   - Signals for **app**: "app", "h5", "合约pro" (the trading screen, mobile), "TabBar", "移动端", "触控", "44px target"
   - If signals conflict or are missing, STOP and ask han before loading either platform — do not default to APP, do not load both.
   - Same session may switch platforms only when han explicitly requests; otherwise stay on the chosen platform.
2. Identify the task class (see Task → Files index below).
3. Load `references/rules.md` plus the active platform's `rules-app.md` or `rules-web.md`, plus the task-specific files listed in the index — nothing more.
4. If a BTCC Figma URL or plugin is available, inspect the original Figma source before inventing tokens, icons, or components.
5. Generate or review against the role-targeted references.
6. Run `references/for-review-and-qa/qa.md` before claiming completion.

## Path Migrated (legacy → new)

Old flat-layout paths are gone. Map any cached prompt or memory through this table:

| Legacy file (deprecated) | New location |
| --- | --- |
| `references/for-figma-inspect/*.md` (APP) | `references/platform-app/for-figma-inspect/*.md` |
| `references/for-code-generation/*.md` (APP) | `references/platform-app/for-code-generation/*.md` |
| (none — Web is new) | `references/platform-web/rules-web.md`, `references/platform-web/for-figma-inspect/source-anchors.md` |
| flat-role legacy paths from prior restructure | absorbed into `platform-app/` |
| top-level `docs/btcc/` long-form trio | already deleted in prior restructure |

## Task → Files

`references/rules.md` is a default mandatory read for every task and is not repeated per row. The active platform's `rules-app.md` or `rules-web.md` is also loaded per Required Workflow Step 3.

`Platform` values: `app` = mobile (新BTCC APP, fileKey `GW9kMfpf0Nib5DG4TjoWBp`); `web` = desktop (新BTCC WEB, fileKey `VrE25c6IAuIieWngebNnwx`); `both` = platform-neutral.

| Task | Platform | Role | Files |
| --- | --- | --- | --- |
| Generate a `合约pro` contract page (mobile) | app | for-code-generation | `platform-app/rules-app.md`, `platform-app/for-code-generation/pages-contract.md`, `components-trading.md`, `components-global.md`, `tokens-colors.md`, `tokens-size-typography.md` |
| Change the order button / trading form (mobile) | app | for-code-generation | `platform-app/rules-app.md`, `platform-app/for-code-generation/components-trading.md`, `tokens-colors.md` |
| Add a leverage picker (mobile) | app | for-code-generation | `platform-app/rules-app.md`, `platform-app/for-code-generation/components-trading.md`, `tokens-size-typography.md` |
| Review AI / model output | both | for-review-and-qa | `for-review-and-qa/qa.md`, `golden-examples.md`, `data-format.md` (cite the active platform's `rules-*.md`) |
| Write or edit a prompt | both | for-prompt-design | `for-prompt-design/prompt-evals.md`, `implementation-patterns.md` |
| Inspect a Figma node / anchor (APP) | app | for-figma-inspect | `platform-app/for-figma-inspect/source-anchors.md`, `contract-screens.md`, `icons.md` |
| Inspect a Figma node / anchor (Web) | web | for-figma-inspect | `platform-web/for-figma-inspect/source-anchors.md` |
| Modify a token value | app | for-code-generation | `platform-app/for-code-generation/tokens-colors.md` (color) or `tokens-size-typography.md` (size/type). For Web, tokens are not yet extracted — flag as Unverified per `platform-web/rules-web.md` R-ASSETS-WEB. |
| Add a new page (unverified surface, APP) | app | for-code-generation + for-figma-inspect | `platform-app/for-code-generation/pages-other.md` (carry the Unverified marker per `rules.md` R-SCOPE-1), `platform-app/for-figma-inspect/source-anchors.md` |
| Generate a Web page | web | (limited) | `platform-web/rules-web.md`, `platform-web/for-figma-inspect/source-anchors.md`. **Web `for-code-generation/` is not yet populated**; either confirm with han before generating Web code, or carry the Unverified marker per `rules.md` R-SCOPE-1 and `platform-web/rules-web.md` R-ASSETS-WEB. |
| Generate a campaign LP (Web) | web | for-figma-inspect + for-prompt-design | `platform-web/rules-web.md`, `platform-web/for-figma-inspect/source-anchors.md` (see "LP activity reference" — start from `7752:73942 jjj交易赛` patterns), `for-prompt-design/figma-plugin-pitfalls.md` |
| Build any Figma node via `use_figma` | both | for-prompt-design | `for-prompt-design/figma-plugin-pitfalls.md` (mandatory pre-flight) |

## Reusable Assets

| Asset | Use |
| --- | --- |
| `assets/btcc-tokens.json` | Machine-readable dark/light BTCC token values. |
| `assets/btcc-tokens.css` | Drop-in CSS custom properties for web implementations. |
| `assets/icons/*.svg` | Figma-exported core BTCC utility icons. |
| `scripts/btcc_qa_lint.py` | Heuristic web-output QA checker (runtime enforcer of `rules.md`). |

Note: Tokens are currently APP-derived; Web token parity is unverified — see `platform-web/rules-web.md` R-ASSETS-WEB.

## Figma Plugin Workflow

When the Figma plugin is available:

**Before calling `use_figma`:** read `references/for-prompt-design/figma-plugin-pitfalls.md`. It documents observed Plugin API gotchas (font features, range fills, hug-content, hex conversion) and a pre-flight checklist that prevents the most common silent failures.

### APP (新BTCC APP, fileKey `GW9kMfpf0Nib5DG4TjoWBp`)

1. Load `references/platform-app/for-figma-inspect/source-anchors.md`.
2. Inspect `设计规范`, `全局组件`, and the target page with Figma tools.
3. Read local variables before defining or mapping tokens.
4. Search source screens for icon roles before choosing fallbacks (`references/platform-app/for-figma-inspect/icons.md`).
5. Prefer existing Figma component sets:
   - `次级button`
   - `TabBar 底部标签栏`
6. If creating or updating Figma nodes, keep generated nodes linked to tokens/components where practical.

### Web (新BTCC WEB, fileKey `VrE25c6IAuIieWngebNnwx`)

1. Load `references/platform-web/for-figma-inspect/source-anchors.md`.
2. Inspect the top-level canvases `0:1 设计规范` and `3089:7459 其他-马甲包官网/桌面图标`.
3. Note: pages-level anchors are not yet documented for Web. The desktop trading layout lives as sub-frames inside `0:1` rather than a separate `合约pro` canvas — consult the verified sub-frame list in `source-anchors.md` before referencing any Web page.

## Original Figma Anchors

### APP

- File: `新BTCC APP`
- File key: `GW9kMfpf0Nib5DG4TjoWBp`
- Token page: `设计规范`
- Global components: `全局组件`
- Main trading reference: `合约pro`
- Component sets: `次级button`, `TabBar 底部标签栏`

### Web

- File: `新BTCC WEB`
- File key: `VrE25c6IAuIieWngebNnwx`
- Top-level canvases: `0:1 设计规范`, `3089:7459 其他-马甲包官网/桌面图标`
- Note: Web has no separate `合约pro` / `合约pro-dark` canvas; the desktop trading layout lives as sub-frames inside `0:1`. See `references/platform-web/for-figma-inspect/source-anchors.md` for the verified sub-frame list.

For the full anchor list and verified vs unverified scope, see the platform-specific `for-figma-inspect/source-anchors.md` and `rules.md` R-SCOPE-1.

## Common Mistakes

These are pointers; the authoritative anti-pattern list lives in `rules.md` R-SSOT-2.

- Marketing landing page on an operational surface (`rules.md` R-LAYOUT-1).
- `Open Long` colored green or `Open Short` colored anything but red (`rules.md` R-COLOR-1).
- Green/red used as decoration (`rules.md` R-COLOR-2).
- Cards on every section (`rules.md` R-LAYOUT-2).
- Missing tabular numbers for prices and balances (`rules.md` R-LAYOUT-2).
- Decorative or colorful icons in trading controls (`rules.md` R-ICON-1).
- Generating an unverified surface without the Unverified marker (`rules.md` R-SCOPE-1).
- Using `--primary` / `--accent` / arbitrary hex inside BTCC surfaces (`rules.md` R-NAME-1, R-COLOR-2).
- Generating Web code without confirming token parity (`platform-web/rules-web.md` R-ASSETS-WEB).

## Completion Gate

Before finishing:

1. Read `references/for-review-and-qa/qa.md` (and re-check both `references/rules.md` and the active platform's `rules-app.md` or `rules-web.md` for any rule citations).
2. For generated web files, run `python skills/btcc-style-generator/scripts/btcc_qa_lint.py <file-or-directory>` when the files are available locally.
3. Check for hard failures.
4. State whether Figma source was inspected.
5. Mention any fallback icons, missing assets, or unverified assumptions per `rules.md` R-SCOPE-1.
