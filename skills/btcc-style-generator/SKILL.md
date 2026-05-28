---
name: btcc-style-generator
description: Use when generating, implementing, reviewing, prompting, or creating Figma designs for BTCC-style crypto exchange web pages, including trading, contract, market, wallet, account, login, register, copy trading, modal, bottom sheet, dashboard, token, icon, or component work.
---

# BTCC Style Generator

## Overview

Generate BTCC interfaces as compact exchange workspaces. The style is dark-first, data-led, operational, and stateful. It should feel like a trading product, not a marketing site.

Read `references/rules.md` first; it is the single source of truth for BTCC golden rules. All other reference files cite back to it and MUST NOT re-state rules as their own prescriptions.

## Required Workflow

1. Identify the task class (see Task → Files index below).
2. Load `references/rules.md` plus the task-specific files listed in the index — nothing more.
3. If a BTCC Figma URL or plugin is available, inspect the original Figma source before inventing tokens, icons, or components.
4. Generate or review against the role-targeted references.
5. Run `references/for-review-and-qa/qa.md` before claiming completion.

## Path Migrated (legacy → new)

Old flat-layout paths are gone. Map any cached prompt or memory through this table:

| Legacy file (deprecated) | New location |
| --- | --- |
| flat `components` doc | `references/for-code-generation/components-{trading,account,global}.md` |
| flat `tokens` doc | `references/for-code-generation/tokens-{colors,size-typography}.md` |
| flat `page-matrix` doc | `references/for-code-generation/pages-{contract,other}.md` |
| flat `figma-source` doc | `references/for-figma-inspect/source-anchors.md` |
| top-level `docs/btcc/` long-form trio | deleted; content absorbed into `references/` role directories |

## Task → Files

`references/rules.md` is a default mandatory read for every task and is not repeated per row.

| Task | Role | Files |
| --- | --- | --- |
| Generate a `合约pro` contract page | for-code-generation | `pages-contract.md`, `components-trading.md`, `components-global.md`, `tokens-colors.md`, `tokens-size-typography.md` |
| Change the order button / trading form | for-code-generation | `components-trading.md`, `tokens-colors.md` |
| Add a leverage picker | for-code-generation | `components-trading.md`, `tokens-size-typography.md` |
| Review AI / model output | for-review-and-qa | `qa.md`, `golden-examples.md`, `data-format.md` |
| Write or edit a prompt | for-prompt-design | `prompt-evals.md`, `implementation-patterns.md` |
| Inspect a Figma node / anchor | for-figma-inspect | `source-anchors.md`, `contract-screens.md`, `icons.md` |
| Modify a token value | for-code-generation | `tokens-colors.md` (color) or `tokens-size-typography.md` (size / type) |
| Add a new page (unverified surface) | for-code-generation + for-figma-inspect | `pages-other.md` (carry the Unverified marker per `rules.md` R-SCOPE-1), `source-anchors.md` |

## Reusable Assets

| Asset | Use |
| --- | --- |
| `assets/btcc-tokens.json` | Machine-readable dark/light BTCC token values. |
| `assets/btcc-tokens.css` | Drop-in CSS custom properties for web implementations. |
| `assets/icons/*.svg` | Figma-exported core BTCC utility icons. |
| `scripts/btcc_qa_lint.py` | Heuristic web-output QA checker (runtime enforcer of `rules.md`). |

## Figma Plugin Workflow

When the Figma plugin is available:

1. Load `references/for-figma-inspect/source-anchors.md`.
2. Inspect `设计规范`, `全局组件`, and the target page with Figma tools.
3. Read local variables before defining or mapping tokens.
4. Search source screens for icon roles before choosing fallbacks (`references/for-figma-inspect/icons.md`).
5. Prefer existing Figma component sets:
   - `次级button`
   - `TabBar 底部标签栏`
6. If creating or updating Figma nodes, keep generated nodes linked to tokens/components where practical.

## Original Figma Anchors

- File: `新BTCC APP`
- File key: `GW9kMfpf0Nib5DG4TjoWBp`
- Token page: `设计规范`
- Global components: `全局组件`
- Main trading reference: `合约pro`
- Component sets: `次级button`, `TabBar 底部标签栏`

For the full anchor list and verified vs unverified scope, see `references/for-figma-inspect/source-anchors.md` and `rules.md` R-SCOPE-1.

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

## Completion Gate

Before finishing:

1. Read `references/for-review-and-qa/qa.md`.
2. For generated web files, run `python skills/btcc-style-generator/scripts/btcc_qa_lint.py <file-or-directory>` when the files are available locally.
3. Check for hard failures.
4. State whether Figma source was inspected.
5. Mention any fallback icons, missing assets, or unverified assumptions per `rules.md` R-SCOPE-1.
