# BTCC Style Generator

This repository packages the BTCC app design language extracted from the Figma file `新BTCC APP` into reusable Markdown specs, prompt references, assets, and a Codex skill.

It is intended for generating BTCC-style crypto exchange web pages, especially trading, contract, market, wallet, auth, account, copy trading, and app-like operational screens.

## Source

- Figma file: `新BTCC APP`
- Figma file key: `GW9kMfpf0Nib5DG4TjoWBp`
- Primary token source page: `设计规范`
- Global component source page: `全局组件`
- Main contract trading reference page: `合约pro`
- Known component sets:
  - `次级button`
  - `TabBar 底部标签栏`

When the Figma plugin is available, inspect the source file before inventing tokens, icons, components, or layout rules.

## What Is Included

```text
docs/
  btcc/
    btcc-design-system.md
    btcc-generation-governance.md
    btcc-prompt-pack.md

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
      components.md
      data-format.md
      figma-source.md
      golden-examples.md
      icons.md
      implementation-patterns.md
      page-matrix.md
      prompt-evals.md
      qa.md
      tokens.md
    scripts/
      btcc_qa_lint.py
```

## Quick Start

1. Read the high-level design system:

   ```text
   docs/btcc/btcc-design-system.md
   ```

2. Read the prompt pack:

   ```text
   docs/btcc/btcc-prompt-pack.md
   ```

3. Use the Codex skill for actual generation work:

   ```text
   skills/btcc-style-generator/SKILL.md
   ```

4. If generating web code, import the token CSS or map the JSON tokens into the target project:

   ```css
   @import "./skills/btcc-style-generator/assets/btcc-tokens.css";
   ```

5. Before claiming output is ready, run the QA linter:

   ```bash
   python skills/btcc-style-generator/scripts/btcc_qa_lint.py <file-or-directory>
   ```

## Core BTCC Rules

- Default to dark mode.
- Treat BTCC as an operational exchange UI, not a marketing landing page.
- Put market, account, product, or trading state in the first viewport.
- Use original BTCC semantic tokens instead of arbitrary colors.
- Use brand blue for neutral primary actions and selected states.
- Use green for buy, long, bid, positive, profit, and success states.
- Use red for sell, short, ask, negative, loss, and error states.
- Keep trading/workspace screens compact, dense, and data-led.
- Use thin dividers, tabular numbers, aligned numeric columns, and restrained borders.
- Use tabs for major operational states and segmented controls for mode switches.
- Prefer the Figma-exported BTCC SVG icons before generic icon libraries.

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
| Success | `#2CA85D` | `#2CA85D` |
| Error | `#EB464F` | `#EB464F` |
| Warning | `#E0601F` | `#E0601F` |
| Check/reward | `#F0B848` | `#F0B848` |

Use `references/tokens.md` for full token names and mappings.

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

Icon selection order:

1. Inspect the original Figma icon/source node.
2. Use the local SVG asset if the role is covered.
3. Wrap the SVG in the target project icon component if needed.
4. Use a fallback icon library only when no BTCC source asset exists.

Use `references/icons.md` for role mapping, sizes, and fallback names.

## Figma Plugin Workflow

When the Figma plugin is available:

1. Open or target the Figma file `GW9kMfpf0Nib5DG4TjoWBp`.
2. Inspect `设计规范` for variables, colors, and source icons.
3. Inspect `全局组件` for component sets such as `次级button`.
4. Inspect the target page, especially `合约pro` for trading layouts.
5. Reuse existing Figma variables/components when creating or updating Figma nodes.
6. Only create new tokens/components when the original source does not cover the need.

Do not rely on memory alone for Figma-specific values when the plugin can inspect the file.

## Recommended Generation Workflow

1. Identify the page type:
   - contract trading
   - market/watchlist
   - wallet/assets
   - auth/login/register
   - copy trading
   - account/settings
   - H5/mobile app-like surface

2. Load the smallest relevant references:
   - `references/page-matrix.md`
   - `references/components.md`
   - `references/tokens.md`
   - `references/icons.md`
   - `references/data-format.md`

3. Use the gold examples:
   - `references/golden-examples.md`

4. Generate using BTCC tokens, icon roles, compact spacing, and operational hierarchy.

5. Run QA:

   ```bash
   python skills/btcc-style-generator/scripts/btcc_qa_lint.py <file-or-directory>
   ```

6. Compare against:
   - `references/qa.md`
   - `references/prompt-evals.md`

## Prompt Evaluation

Use `skills/btcc-style-generator/references/prompt-evals.md` before changing prompt behavior.

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
- using brand blue for long/short actions
- using arbitrary colors instead of BTCC tokens
- losing tabular numeric alignment
- replacing BTCC utility icons with decorative icons

## QA Linter

Run:

```bash
python skills/btcc-style-generator/scripts/btcc_qa_lint.py <file-or-directory>
```

Self-test:

```bash
python skills/btcc-style-generator/scripts/btcc_qa_lint.py --self-test
```

The linter checks common generation drift:

- arbitrary hex colors outside the BTCC allowlist
- decorative gradients on operational pages
- missing `--btcc-*` token usage
- missing tabular number styling
- icon-only buttons without `aria-label` or `title`
- contract pages missing `Order Book`, `Open Long`, or `Open Short`
- long/short actions without success/error styling cues
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
| `docs/btcc/btcc-design-system.md` | Human-readable full design system summary |
| `docs/btcc/btcc-generation-governance.md` | Governance, review, and generation discipline |
| `docs/btcc/btcc-prompt-pack.md` | Prompt templates for BTCC-style generation |
| `skills/btcc-style-generator/SKILL.md` | Codex skill router and usage rules |
| `references/figma-source.md` | Figma pages, components, source anchors |
| `references/tokens.md` | Original token names and mappings |
| `references/components.md` | Trading forms, buttons, tabs, tables, modals |
| `references/icons.md` | Icon roles, sizes, Figma cues, local SVGs |
| `references/page-matrix.md` | Page-by-page structure rules |
| `references/data-format.md` | Number formats, labels, mock data, semantics |
| `references/golden-examples.md` | Gold-standard page structures |
| `references/prompt-evals.md` | Regression prompts and pass/fail checks |
| `references/implementation-patterns.md` | Packaging, fidelity levels, prompt hygiene |
| `references/qa.md` | Manual and automated QA checklist |
| `assets/btcc-tokens.json` | Token data for tools and transformations |
| `assets/btcc-tokens.css` | CSS variables for generated web code |
| `assets/icons/*.svg` | Figma-exported core BTCC icons |
| `scripts/btcc_qa_lint.py` | Heuristic QA linter |

## Current Status

Completed:

- Figma source anchors documented.
- Core dark/light tokens extracted.
- Core icon roles documented.
- 10 original Figma SVG icons exported.
- Prompt pack and generation governance written.
- Codex skill created.
- Golden examples added.
- Data formatting rules added.
- Prompt eval set added.
- QA linter added and self-tested.

Known limitations:

- The `图标` Figma page appeared empty during extraction, so icon assets currently come from `设计规范` and `合约pro`.
- Some complex components are specified by anatomy and behavior rather than fully exported as Figma component code.
- The QA linter is heuristic and should not replace visual QA or Figma source inspection.

