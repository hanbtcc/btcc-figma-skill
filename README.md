# BTCC Style Generator

This repository packages the BTCC app design language extracted from the Figma file `新BTCC APP` into reusable Markdown specs, prompt references, assets, and a Codex skill.

It is intended for generating BTCC-style crypto exchange web pages, especially trading, contract, market, wallet, auth, account, copy trading, and app-like operational screens.

## Source

- Figma file: `新BTCC APP`
- Figma file key: `GW9kMfpf0Nib5DG4TjoWBp`
- Verified pages (current `get_metadata` pass):
  - `设计规范` — primary token source (`0:1`)
  - `合约pro` — main contract trading reference (`1262:304`)
  - `合约pro-dark` — verified dark trading layout (`3112:1423`)
- Component instance names referenced as anatomy hints (not guaranteed component-set pages):
  - `次级button`
  - `TabBar 底部标签栏`
- Other page aliases (`全局组件`, `图标`, `首页`, `资产`, `行情`, `现货`, `跟单`, `登录注册`, `C2C`, `h5`, etc.) appear in older notes but were NOT returned by the current Figma metadata pass. See `skills/btcc-style-generator/references/for-figma-inspect/source-anchors.md` and `rules.md` R-SCOPE-1 for the verified-vs-unverified split.

When the Figma plugin is available, inspect the source file before inventing tokens, icons, components, or layout rules. Do not assume an unverified page alias maps to a real Figma page in the current file.

## What Is Included

```text
skills/
  btcc-style-generator/
    SKILL.md
    agents/
      openai.yaml
    assets/
      btcc-tokens.css
      btcc-tokens.json
      icons/*.svg
    references/
      rules.md                    ← single source of truth
      for-figma-inspect/
        source-anchors.md
        contract-screens.md
        icons.md
      for-code-generation/
        components-trading.md
        components-account.md
        components-global.md
        tokens-colors.md
        tokens-size-typography.md
        pages-contract.md
        pages-other.md
      for-review-and-qa/
        qa.md
        golden-examples.md
        data-format.md
      for-prompt-design/
        prompt-evals.md
        implementation-patterns.md
    scripts/
      btcc_qa_lint.py
```

## Quick Start

1. Read the golden rules first:

   ```text
   skills/btcc-style-generator/references/rules.md
   ```

2. Use the Codex skill entrypoint for routing:

   ```text
   skills/btcc-style-generator/SKILL.md
   ```

   The SKILL.md "Task → Files" index maps an invocation class (e.g. "generate a contract page", "change the order button") to the minimum file set to load.

3. If generating web code, import the token CSS or map the JSON tokens into the target project:

   ```css
   @import "./skills/btcc-style-generator/assets/btcc-tokens.css";
   ```

4. Before claiming output is ready, run the QA linter:

   ```bash
   python skills/btcc-style-generator/scripts/btcc_qa_lint.py <file-or-directory>
   ```

## Core BTCC Rules

The authoritative rules live in `skills/btcc-style-generator/references/rules.md`. Highlights below are pointers, not the source of truth — when in doubt, read the file.

- Direction buttons in `合约pro` are inverted from the western convention: `Open Long` uses brand blue, `Open Short` uses error red. Numeric direction (positive/negative) still follows green/red. (`rules.md` R-COLOR-1)
- Color is status, not decoration. Reserve red and green for state and numeric semantics. (`rules.md` R-COLOR-2)
- Operational state in the first viewport. No marketing hero on trading or wallet surfaces. (`rules.md` R-LAYOUT-1)
- Dark-first, compact spacing, dense rows, tabular numbers, restrained borders. (`rules.md` R-LAYOUT-2)
- Figma-exported BTCC SVG icons before generic icon libraries; line stroke around 1.5–2 px at 24 px. (`rules.md` R-ICON-1)
- Use `--btcc-*` semantic tokens. Do not introduce arbitrary hex or `--primary` / `--accent`. (`rules.md` R-NAME-1)
- Surfaces outside the verified Figma pass MUST carry an "Unverified / 未验证" marker. (`rules.md` R-SCOPE-1)

## Design Tokens

Machine-readable token files:

- `skills/btcc-style-generator/assets/btcc-tokens.json`
- `skills/btcc-style-generator/assets/btcc-tokens.css`

Key semantic values:

| Token intent | Dark | Light |
| --- | --- | --- |
| Background primary | `#0C0F12` | `#FFFFFF` |
| Modal/card background | `#13171B` | `#FFFFFF` |
| Text/icon primary | `#F1F3F5` | `#13161C` |
| Text/icon secondary | `#878F99` | `#717C95` |
| Brand | `#0C73ED` | `#195EFF` |
| Secondary accent | `#84DC1F` | `#84DC1F` |
| Success | `#2CA85D` | `#2CA85D` |
| Error | `#EB464F` | `#EB464F` |
| Warning | `#E0601F` | `#E0601F` |
| Check/reward | `#F0B848` | `#F0B848` |

Full token tables and semantic mappings live in `skills/btcc-style-generator/references/for-code-generation/tokens-colors.md` and `tokens-size-typography.md`.

## Icons

Core SVG icons were exported from the original Figma `设计规范` page and stored in:

```text
skills/btcc-style-generator/assets/icons/
```

Available icon assets:

- `market-stats.svg`
- `kline.svg`
- `more.svg`
- `plus-circle.svg`
- `warning-circle.svg`
- `orders-file.svg`
- `dropdown.svg`
- `transfer.svg`
- `demo-trading.svg`
- `discover.svg`

Icon selection order is defined in `rules.md` R-ICON-1; role mapping and Figma cues live in `references/for-figma-inspect/icons.md`.

## Figma Plugin Workflow

When the Figma plugin is available:

1. Open or target the Figma file `GW9kMfpf0Nib5DG4TjoWBp`.
2. Run `get_metadata` (no nodeId) to confirm which pages currently exist before assuming any alias maps to a real page.
3. Inspect `设计规范` (`0:1`) for variables, colors, and source icons.
4. Inspect `合约pro` (`1262:304`), especially `合约pro-dark` (`3112:1423`), for verified trading layouts and direction-button colors.
5. For tokens, prefer `search_design_system` over a full-page metadata dump (the `设计规范` page is too large to inline).
6. Reuse existing Figma variables/instances when creating or updating Figma nodes.
7. Only create new tokens/components when the verified source does not cover the need.

Do not rely on memory alone for Figma-specific values when the plugin can inspect the file. Do not generate UI on the basis of an unverified page alias.

## Recommended Generation Workflow

1. Identify the task class and consult the SKILL.md "Task → Files" index for the minimum file set to read.
2. Always read `references/rules.md` first.
3. For contract trading work, load `for-code-generation/pages-contract.md`, `components-trading.md`, `components-global.md`, `tokens-colors.md`, `tokens-size-typography.md`.
4. For unverified surfaces (home, wallet/assets, auth, copy trading, spot, c2c, h5, etc.), load `for-code-generation/pages-other.md` and carry the Unverified marker.
5. Generate using BTCC tokens, icon roles, compact spacing, and operational hierarchy.
6. Run QA:

   ```bash
   python skills/btcc-style-generator/scripts/btcc_qa_lint.py <file-or-directory>
   ```

7. Compare against `for-review-and-qa/qa.md`, `golden-examples.md`, `data-format.md`, and `for-prompt-design/prompt-evals.md`.

## Prompt Evaluation

Use `skills/btcc-style-generator/references/for-prompt-design/prompt-evals.md` before changing prompt behavior.

The eval set covers:

- desktop contract trading page
- mobile contract trading page
- wallet/assets page
- market table page
- generic dashboard to BTCC conversion
- marketing-drift resistance

The most important failures to catch are:

- turning an operational screen into a marketing hero page
- missing order book or order form on trading pages
- coloring the `Open Long` button green
- using arbitrary colors instead of BTCC tokens
- losing tabular numeric alignment
- replacing BTCC utility icons with decorative icons

These map back to `rules.md` R-LAYOUT-1, R-COLOR-1, R-COLOR-2, R-LAYOUT-2, and R-ICON-1.

## QA Linter

Run:

```bash
python skills/btcc-style-generator/scripts/btcc_qa_lint.py <file-or-directory>
```

Self-test:

```bash
python skills/btcc-style-generator/scripts/btcc_qa_lint.py --self-test
```

The linter is the runtime enforcer of `rules.md`. It checks common generation drift:

- arbitrary hex colors outside the BTCC allowlist
- decorative gradients on operational pages
- missing `--btcc-*` token usage
- missing tabular number styling
- icon-only buttons without `aria-label` or `title`
- contract pages missing `Order Book`, `Open Long`, or `Open Short`
- `Open Long` not styled with `fill/Brand` (blue) or `Open Short` not styled with `fill/Error` (red)
- marketing hero language mixed into trading pages

The linter is heuristic. Use it together with visual review and Figma inspection.

## Skill Installation

To use this as a Codex skill, copy or symlink:

```text
skills/btcc-style-generator/
```

into the Codex skills directory for the target environment, then invoke it when generating or reviewing BTCC-style UI.

The skill entrypoint is:

```text
skills/btcc-style-generator/SKILL.md
```

## File Guide

| File | Purpose |
| --- | --- |
| `skills/btcc-style-generator/SKILL.md` | Codex skill router and Task → Files index |
| `skills/btcc-style-generator/references/rules.md` | Single source of truth for BTCC golden rules |
| `references/for-figma-inspect/source-anchors.md` | Figma file key, page names, component-set anchors |
| `references/for-figma-inspect/contract-screens.md` | `合约pro` sub-screen index (node IDs by purpose) |
| `references/for-figma-inspect/icons.md` | Icon roles, Figma cues, local SVG hints |
| `references/for-code-generation/components-trading.md` | Trading form, order book, TP/SL sheet, market pair header |
| `references/for-code-generation/components-account.md` | Orders / positions / assets panel, market table, wallet table |
| `references/for-code-generation/components-global.md` | Secondary button, bottom tab bar, product navigation |
| `references/for-code-generation/tokens-colors.md` | Color collections, semantic tokens, gray ramp |
| `references/for-code-generation/tokens-size-typography.md` | Radius, control heights, spacing, type scale |
| `references/for-code-generation/pages-contract.md` | Verified `合约pro` page structure |
| `references/for-code-generation/pages-other.md` | Unverified pages (home, wallet, auth, copy, spot, c2c, h5) with Unverified marker |
| `references/for-review-and-qa/qa.md` | QA checklist, all rule citations link back to `rules.md` |
| `references/for-review-and-qa/golden-examples.md` | Gold-standard structures for verified surfaces |
| `references/for-review-and-qa/data-format.md` | Number formats, labels, mock data, semantics |
| `references/for-prompt-design/prompt-evals.md` | Regression prompts and pass/fail checks |
| `references/for-prompt-design/implementation-patterns.md` | Packaging, fidelity levels, prompt hygiene |
| `assets/btcc-tokens.json` | Token data for tools and transformations |
| `assets/btcc-tokens.css` | CSS variables for generated web code |
| `assets/icons/*.svg` | Figma-exported core BTCC icons |
| `scripts/btcc_qa_lint.py` | Heuristic QA linter (runtime enforcer of `rules.md`) |

## Current Status

Completed:

- Figma source anchors documented.
- Core dark/light tokens extracted.
- Core icon roles documented.
- 10 original Figma SVG icons exported.
- Codex skill created and restructured by role (rules.md SSOT + 4 role directories).
- Golden examples added.
- Data formatting rules added.
- Prompt eval set added.
- QA linter added and self-tested.

Known limitations:

- The `图标` Figma page appeared empty during extraction, so icon assets currently come from `设计规范` and `合约pro`.
- Some complex components are specified by anatomy and behavior rather than fully exported as Figma component code.
- The QA linter is heuristic and should not replace visual QA or Figma source inspection.
- Surfaces other than `合约pro` / `合约pro-dark` / `设计规范` remain unverified per `rules.md` R-SCOPE-1.
