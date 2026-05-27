---
name: btcc-style-generator
description: Use when generating, implementing, reviewing, prompting, or creating Figma designs for BTCC-style crypto exchange web pages, including trading, contract, market, wallet, account, login, register, copy trading, modal, bottom sheet, dashboard, token, icon, or component work.
---

# BTCC Style Generator

## Overview

Generate BTCC interfaces as compact exchange workspaces. The style is dark-first, data-led, operational, and stateful. It should feel like a trading product, not a marketing site.

## Required Workflow

1. Identify the page or asset type.
2. Load the smallest needed reference files.
3. If a BTCC Figma URL or plugin is available, inspect the original Figma source before inventing tokens, icons, or components.
4. Generate or review using original BTCC tokens, component anatomy, icon roles, and page matrix rules.
5. Run `references/qa.md` before claiming completion.

## Reference Router

Load these on demand:

| Need | Read |
| --- | --- |
| Original Figma page names, aliases, component sets, source nodes | `references/figma-source.md` |
| Dark/light tokens, original Figma token names, CSS variable mapping | `references/tokens.md` |
| Trading form, order book, tab bar, buttons, modals, tables anatomy | `references/components.md` |
| Icon roles, sizes, Figma cues, fallback icon names | `references/icons.md` |
| Page-specific structure for contract, home, markets, wallet, auth, copy, spot, C2C, H5 | `references/page-matrix.md` |
| Number formats, trading labels, mock data, positive/negative semantics | `references/data-format.md` |
| Page-level gold standards for contract, mobile, market, wallet, auth | `references/golden-examples.md` |
| Prompt regression tests and pass/fail expectations | `references/prompt-evals.md` |
| Code packaging, icon tiers, fidelity labels, AI prompt hygiene | `references/implementation-patterns.md` |
| Completion checks and hard failures | `references/qa.md` |

The broader project docs are also available:

- `docs/btcc/btcc-design-system.md`
- `docs/btcc/btcc-generation-governance.md`
- `docs/btcc/btcc-prompt-pack.md`

Use the skill-local `references/` files first when you need concise operational guidance.

Reusable assets:

| Asset | Use |
| --- | --- |
| `assets/btcc-tokens.json` | Machine-readable dark/light BTCC token values. |
| `assets/btcc-tokens.css` | Drop-in CSS custom properties for web implementations. |
| `assets/icons/*.svg` | Figma-exported core BTCC utility icons. |
| `scripts/btcc_qa_lint.py` | Heuristic web-output QA checker. |

## Core Rules

- Default to dark mode.
- Use original BTCC semantic tokens instead of arbitrary colors.
- Use `assets/btcc-tokens.css` or `assets/btcc-tokens.json` when creating web code if no project token system already exists.
- Preserve light-mode mappings when creating themeable code.
- Use brand blue for neutral primary actions and selected states.
- Use green for buy, long, bid, profit, positive, and success states.
- Use red for sell, short, ask, loss, negative, error, and destructive states.
- Use compact spacing, dense rows, thin dividers, restrained borders, and tabular numbers.
- Keep product state, market state, account state, or trading actions visible in the first viewport.
- Use tabs for major operational states and segmented controls for mode switches.
- Use BTCC/Figma-matched compact line icons before generic icon packs.
- Prefer `assets/icons/*.svg` for known BTCC utility roles before fallback icon libraries.
- Use cards only for repeated modules or genuinely contained tools.

## Figma Plugin Workflow

When the Figma plugin is available:

1. Load `references/figma-source.md`.
2. Inspect `设计规范`, `全局组件`, and the target page with Figma tools.
3. Read local variables before defining or mapping tokens.
4. Search source screens for icon roles before choosing fallbacks.
5. Prefer existing Figma component sets:
   - `次级button`
   - `TabBar 底部标签栏`
6. If creating/updating Figma nodes, keep generated nodes linked to tokens/components where practical.

## Original Figma Anchors

Known source anchors:

- File: `新BTCC APP`
- File key: `GW9kMfpf0Nib5DG4TjoWBp`
- Token page: `设计规范`
- Global components: `全局组件`
- Main trading reference: `合约pro`
- Component set: `次级button`
- Component set: `TabBar 底部标签栏`

## Common Mistakes

- Turning the UI into a generic crypto marketing landing page.
- Using a large gradient hero as the first screen of an operational page.
- Making every section a floating card.
- Using green/red as decoration instead of market or transaction state.
- Using brand blue for long/short trading actions.
- Hiding trading/account actions below the fold.
- Making table rows too tall or sparse.
- Forgetting tabular numbers for prices and balances.
- Replacing BTCC utility icons with colorful decorative icons.
- Using vague copy where operational labels are clearer.
- Leaving selected states dependent on color alone.
- Shipping clipped text, overlapping controls, or misaligned numeric columns.

## Completion Gate

Before finishing:

1. Read `references/qa.md`.
2. For generated web files, run `python skills/btcc-style-generator/scripts/btcc_qa_lint.py <file-or-directory>` when the files are available locally.
3. Check for hard failures.
4. State whether Figma source was inspected.
5. Mention any fallback icons, missing assets, or unverified assumptions.
