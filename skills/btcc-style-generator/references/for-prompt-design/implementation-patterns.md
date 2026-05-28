# BTCC Implementation Patterns

> See `references/rules.md` for global rules.

Use this when turning the BTCC design spec into reusable code, Figma plugin workflows, prompts, or repository instructions. Process and packaging guidance only — token values, component anatomy, and color/layout/naming rules are owned elsewhere (see `rules.md` for global rules; for APP tokens and components see `platform-app/for-code-generation/`, for Web see `platform-web/`).

## What Mature Design Systems Usually Fix

These patterns keep AI/code generation from drifting after the first version.

| Pattern | BTCC application |
| --- | --- |
| Multi-format tokens | Keep `assets/btcc-tokens.json` for tools and `assets/btcc-tokens.css` for web output. |
| Themeable icons | Prefer local SVGs for exact Figma shape; convert color to `currentColor` only when the target component system needs theme inheritance. |
| Figma as source of truth | Re-inspect verified anchors in `platform-app/for-figma-inspect/source-anchors.md` (APP) or `platform-web/for-figma-inspect/source-anchors.md` (Web) before inventing new tokens/components. |
| Agent-readable docs | Keep `SKILL.md` as a router and put heavy details in role directories under `references/`. |
| Regression prompts | Run `references/for-prompt-design/prompt-evals.md` before changing the prompt pack. |
| Static checks | Run `scripts/btcc_qa_lint.py` on generated code to catch common drift. |
| Component status | Track which BTCC components are Figma-exact, approximated, or missing. |

## Asset Packaging

Recommended repository shape:

```text
btcc-style-generator/
  SKILL.md
  assets/
    btcc-tokens.css
    btcc-tokens.json
    icons/*.svg
  references/
    rules.md
    for-review-and-qa/
    for-prompt-design/
    platform-app/
    platform-web/
  scripts/
    btcc_qa_lint.py
```

Keep generated app implementations outside the skill unless they are short, stable gold examples. The skill should teach future agents how to produce BTCC-like output, not become a sample app archive.

## Icon Handling

Icon source order and styling are defined in `rules.md` R-ICON-1. When converting exact Figma SVGs to themeable icons, preserve `viewBox`, path geometry, stroke width, linecap, and linejoin; only replace fixed stroke/fill values with `currentColor` or a token-bound CSS variable.

## Component Fidelity Levels

Use these labels in reviews:

| Level | Meaning |
| --- | --- |
| `figma-exact` | Uses original token names, sizes, states, and copied vector/component structure. |
| `token-exact` | Uses original tokens but rebuilt component anatomy for the target stack. |
| `role-exact` | Preserves information architecture and semantic color/icon roles, but implementation details differ. |
| `fallback` | Uses a generic component/icon because the original source was unavailable. |

Generated work should state the lowest fidelity level used for visible core components.

## AI Prompt Hygiene

When changing prompts:

- Keep hard constraints short and testable; let `rules.md` carry the canonical rule statements and reference them by R- ID rather than restating.
- Put page-specific requirements in examples/evals (`prompt-evals.md`), not only prose.
- Include negative examples for common drift listed in `rules.md` R-SSOT-2 (marketing hero, arbitrary colors, oversized cards, missing order book, wrong long/short button colors).
- Keep Figma inspection an explicit step when the plugin is available; point at `platform-app/for-figma-inspect/` or `platform-web/for-figma-inspect/` rather than reciting anchors inline.
- Prefer "use the BTCC token/icon registry" over pasting long token lists into every prompt.

## External References

Public design-system projects that informed these process patterns:

- [OpenTable design tokens](https://github.com/opentable/design-tokens): multi-format tokens and themeable icons.
- [Equinor Design System](https://github.com/equinor/design-system): Figma as source of truth, tokens extracted into code, icons as installable assets.
- [Figma Simple Design System](https://github.com/figma/sds): variables, styles, components, Code Connect, React code, and icon scripts in one reference implementation.
- [Figma Dev Mode best practices](https://www.figma.com/best-practices/how-figma-uses-dev-mode/): variables and code references surfaced in developer workflows.
