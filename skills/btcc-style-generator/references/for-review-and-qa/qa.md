# BTCC Generation QA

> See `references/rules.md` for global rules. This checklist cites rules by ID; it does not re-state them.

Use this file before claiming a generated BTCC-style page is complete.

## Hard Failures

A generated page MUST be revised when any of the following are true.

- [ ] First viewport surfaces market / account / product / trading state (per rules.md R-LAYOUT-1).
- [ ] Contract / trading page exposes order form and order book in the first pattern (per rules.md R-LAYOUT-1).
- [ ] Long / short button colors follow rules.md R-COLOR-1 (Open Long = brand blue, Open Short = error red; numeric pnl/depth follows R-COLOR-2).
- [ ] No large decorative gradient hero in operational surfaces (per rules.md R-LAYOUT-1).
- [ ] Text does not overlap, clip, or wrap incoherently inside compact controls.
- [ ] Numeric columns follow rules.md R-LAYOUT-2 (right-aligned, tabular-nums, consistent precision).
- [ ] Icon-only controls carry an accessible label in code (per rules.md R-ICON-1).
- [ ] No arbitrary hex colors where BTCC semantic tokens exist (per rules.md R-NAME-1, R-COLOR-2).
- [ ] Mobile primary touch targets are within the range required by rules.md R-LAYOUT-2.

## Automated Heuristic Check

For generated web files, run the lint script. It MUST be run before sign-off; it does not replace visual or Figma review.

```bash
python skills/btcc-style-generator/scripts/btcc_qa_lint.py <file-or-directory>
```

The script is intentionally heuristic and re-encodes rules.md in code form (per rules.md R-SSOT-1). It checks common drift:

- arbitrary hex colors outside the extracted BTCC allowlist (rules.md R-COLOR-2, R-NAME-1)
- decorative `linear-gradient` / `radial-gradient` (rules.md R-LAYOUT-1, R-COLOR-2)
- missing `--btcc-*` token usage (rules.md R-NAME-1)
- missing tabular number styling (rules.md R-LAYOUT-2)
- icon-only buttons without `aria-label` / `title` (rules.md R-ICON-1)
- contract pages missing order book / long / short terms (rules.md R-LAYOUT-1, R-NAME-2)
- direction-button color mismatch (rules.md R-COLOR-1)
- marketing hero language mixed into trading pages (rules.md R-LAYOUT-1)

## Token Checks

- [ ] CSS custom properties follow rules.md R-NAME-1 (`--btcc-<group>-<role>`).
- [ ] Dark-mode values come straight from extracted Figma tokens (per rules.md R-LAYOUT-2 dark-first default).
- [ ] Light-mode mappings are derived from dark, not authored ad hoc (per rules.md R-LAYOUT-2).
- [ ] Component states bind to component / semantic tokens, not generic `--primary` / `--accent` (per rules.md R-NAME-1).

## Visual Checks

- [ ] Density and dividers follow rules.md R-LAYOUT-2 (compact rows, thin neutral dividers, restrained borders).
- [ ] Surface hierarchy is clear without over-using cards (per rules.md R-LAYOUT-2 — cards only for repeated modules or genuinely contained tools).
- [ ] Order-book depth bars stay behind text and remain low contrast.
- [ ] Selected state uses more than color alone (supports rules.md R-COLOR-2 — color is status, not decoration).
- [ ] Icon style follows rules.md R-ICON-1 (compact stroke, restrained weight, token-bound color).

## Content Checks

- [ ] Vocabulary follows rules.md R-NAME-2 (`Perp`, `TP/SL`, `Available`, `Open Long`, `Open Short`, etc.).
- [ ] Direction-button colors follow rules.md R-COLOR-1 (do not invert based on stylistic instinct).
- [ ] Empty states are short and action-oriented; numeric placeholders follow rules.md R-NAME-2 (`--`, `0.0000 USDT`, `+0.0100%`, `100x`, `HH:MM:SS`).
- [ ] Risk / error copy is concise; no long educational prose inside trading panels.
- [ ] Casing is consistent inside each surface.

## Responsive Checks

Mobile:

- [ ] Side gutters and touch targets follow rules.md R-LAYOUT-2.
- [ ] Bottom sheets are used for focused modal tasks.
- [ ] Dense tables become readable stacked rows or horizontally scrollable tables.

Desktop:

- [ ] Trading pages use a multi-column workspace.
- [ ] Chart / market area is the largest region.
- [ ] Order form and order book remain visible (per rules.md R-LAYOUT-1).
- [ ] Mobile bottom navigation is not copied directly to desktop.

## Figma-Assisted Checks

When the Figma plugin is available:

- [ ] Original tokens were inspected or loaded.
- [ ] Existing icon roles were checked before any fallback icon was chosen (per rules.md R-ICON-1).
- [ ] Existing component sets (`次级button`, `TabBar 底部标签栏`, etc.) were considered.
- [ ] Generated nodes use token / component bindings where practical.

## Scope Disclosure

- [ ] Any generated surface outside the verified scope listed in rules.md R-SCOPE-1 carries the unverified marker and convention disclaimer.

## Reporting

In the final response, report:

- Which BTCC page pattern was used.
- Whether Figma source was inspected (and which anchors, per rules.md R-SCOPE-1).
- Any fallback icons or missing source assets.
- Any verification that was not possible, including which rules.md R-IDs could not be confirmed.
