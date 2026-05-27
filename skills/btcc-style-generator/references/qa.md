# BTCC Generation QA

Use this file before claiming a generated BTCC-style page is complete.

## Hard Failures

These require revision:

- First viewport has no market, account, product, or trading state.
- Contract/trading page lacks order form or order book.
- `Open Long` does not use `fill/Brand` (brand blue) or `Open Short` does not use `fill/Error` (red). BTCC's `合约pro` reverses the common Western "long=green / short=red" convention; the long button is brand blue and only the short button is red. Profit/loss numbers, bid/ask depth, and pnl text still use green for positive and red for negative.
- Large decorative gradient hero appears in an operational page.
- Text overlaps, clips, or wraps incoherently inside compact controls.
- Numeric columns are not aligned or not tabular.
- Icon-only controls have no accessible label in code.
- Arbitrary hex colors are used where BTCC semantic tokens exist.
- Mobile layout has touch targets below 40px for primary controls.

## Automated Heuristic Check

For generated web files, run:

```bash
python skills/btcc-style-generator/scripts/btcc_qa_lint.py <file-or-directory>
```

The script is intentionally heuristic. It checks common drift:

- arbitrary hex colors outside the extracted BTCC allowlist
- decorative `linear-gradient` or `radial-gradient`
- missing `--btcc-*` token usage
- missing tabular number styling
- icon-only buttons without `aria-label` or `title`
- contract pages missing order book / long / short terms
- Open Long not using brand blue, or Open Short not using error red
- marketing hero language mixed into trading pages

Run the script as a supplement to visual and Figma checks, not a replacement.

## Token Checks

- Uses `--btcc-*` custom properties or local equivalent mappings.
- Dark mode values match original Figma tokens.
- Light mode mappings are preserved when themeable.
- Component states use component/semantic tokens.
- No generic `--primary`, `--accent`, or unscoped token names inside BTCC surfaces.

## Visual Checks

- Dense but readable.
- Thin neutral dividers.
- Primary surface hierarchy is clear.
- Cards are used only for repeated items or contained tools.
- Order book depth bars stay behind text and low contrast.
- Selected states use more than color alone.
- Icons match BTCC compact line style.

## Content Checks

- Uses stable BTCC trading terms: `Perp`, `TP/SL`, `Available`, `Open Long`, `Open Short`.
- `Open Long` uses `fill/Brand` (brand blue), `Open Short` uses `fill/Error` (red). Do not invert this even when stylistic instinct suggests green/red.
- Empty states are short and action-oriented.
- Risk/error copy is concise.
- No long educational prose inside trading panels.
- Casing is consistent inside each surface.

## Responsive Checks

Mobile:

- 16px side gutters.
- 40-44px touch targets.
- Bottom sheet for focused modal tasks.
- Dense tables become readable stacked rows or horizontally scrollable tables.

Desktop:

- Trading pages use multi-column workspace.
- Chart/market area is the largest region.
- Form and order book remain visible.
- Mobile bottom navigation is not copied directly.

## Figma-Assisted Checks

When Figma plugin is available:

- Original tokens were inspected or loaded.
- Existing icon roles were checked before fallback icons were chosen.
- Existing component sets were considered: `次级button`, `TabBar 底部标签栏`.
- If creating in Figma, generated nodes should use token/component bindings where practical.

## Reporting

In the final response, report:

- Which BTCC page pattern was used.
- Whether Figma source was inspected.
- Any fallback icons or missing source assets.
- Any verification that was not possible.
