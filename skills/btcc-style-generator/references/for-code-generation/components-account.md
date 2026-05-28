# BTCC Account & Market Components

> See `references/rules.md` for global rules.

Anatomy guidance for BTCC account-side and market-listing components: orders/positions/assets panel, market table, wallet asset table. Token names cite Figma labels in backticks; map to the code tokens in `tokens-colors.md` and `tokens-size-typography.md`. Direction-color and tabular-number rules live in `rules.md`; this file does not redeclare them.

## Orders / Positions / Assets Panel

Observed anatomy:

- Tabs: `orders(0)`, `positions(0)`, `assets`.
- Right utility icon: `file-minus-01`.
- Context row: `Current Trading Pair`.
- Empty balance state: `Available: 0.0000 USDT`.
- Empty prompt: deposit/transfer/demo trading actions depending the context.

Layout guidance:

- Counts stay inside tab labels (e.g. `Positions(0)`); do not promote them into separate badges.
- Empty states stay compact and action-oriented; account actions remain visible when balance or data is empty (re-affirms `rules.md` R-LAYOUT-1).
- Avoid large decorative illustrations; the panel is operational, not promotional.
- Action affordances such as `Deposit`, `Transfer`, `Demo` use the brand or secondary button tokens in `tokens-colors.md`. They are neutral account actions, not directional; do not paint them with `fill/Success` or `fill/Error` (see `rules.md` R-COLOR-2).

## Market Table

Recommended anatomy for web:

- Pair column.
- Last price.
- 24h change.
- High/low or volume.
- Optional sparkline.
- Trade action.

Layout guidance:

- Pair and price columns stay scannable; numeric columns follow `rules.md` R-LAYOUT-2 (tabular-nums, right-aligned).
- 24h change cells follow `rules.md` R-COLOR-2 — `fill/Success` for positive, `fill/Error` for negative; do not use semantic colors as decoration.
- Row height stays dense; on mobile the trade-action button stays compact, not a hero CTA in every row.
- Sparkline color tracks the same direction semantics as the change cell.

## Wallet / Asset Table

Recommended anatomy:

- Coin/asset.
- Available.
- Frozen/in order.
- Total value.
- Actions: deposit, withdraw, transfer.

Layout guidance:

- Balance values follow `rules.md` R-LAYOUT-2 (tabular-nums); use `--btcc-font-size-sm` from `tokens-size-typography.md` for table cells.
- Hidden-balance state preserves layout width; do not collapse the row.
- Account actions use brand or secondary button tokens from `tokens-colors.md`; they are not directional, so do not assign them direction colors (see `rules.md` R-COLOR-2).
- Empty / zero rows render `--` per the trading-vocabulary convention in `rules.md` R-NAME-2; do not render `0` for missing values.
