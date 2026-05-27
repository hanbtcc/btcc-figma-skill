# BTCC Component Anatomy

Use this file when generating implementation details, reviewing page structure, or translating BTCC Figma patterns into web components.

## Secondary Button

Original Figma component set:

- Page: `全局组件`
- Name: `次级button`
- Variants:
  - `Property 1=normal, size=extra small`
  - `Property 1=normal, size=small`
  - `Property 1=normal, size=Medium`
  - `Property 1=normal, size=large`
  - `Property 1=pressed, size=extra small`
  - `Property 1=pressed, size=small`
  - `Property 1=pressed, size=Medium`
  - `Property 1=pressed, size=large`

Rules:

- Use for neutral secondary actions, not long/short trading direction.
- Use `fill/Secondary Button/Normal` and `fill/Secondary Button/Pressed`.
- Use compact sizes. Do not inflate secondary buttons into hero CTAs.
- Keep pressed state visually close to source: subtle fill shift, not a dramatic glow.

## Bottom TabBar

Original Figma component set:

- Page: `合约pro`
- Name: `TabBar 底部标签栏`
- Variants: `home`, `discover`, `copy`, `assets`, `trade`
- Size: `375 x 78`

Rules:

- Use only on app-like mobile layouts.
- On desktop, translate to top nav, left rail, or compact module nav.
- Keep labels short: `Home`, `Discover`, `Copy`, `Assets`, `Trade`.
- Active state should use both icon/text emphasis and color/fill state.

## Product Navigation

Observed labels:

- `USDT-M`
- `Coin-M`
- `Spot`
- `USDT-M Pro`
- `beta`

Rules:

- Place near the top of trading/product screens.
- Keep row height around 44px on mobile.
- Use active text weight/color and optional indicator.
- `beta` is a tiny badge, not a large pill.

## Market Pair Header

Observed anatomy:

- Pair: `BTCUSDT`
- Contract tag: `Perp`
- Change: `-2.14%`
- Actions: market stats, chart/K-line, more

Rules:

- Always show the active pair or market context.
- Keep the pair name larger/stronger than secondary metadata.
- Use red/green for change values.
- Pair selector chevron should be compact, around 16px.

## Trading Form

Observed anatomy:

1. Margin/leverage row: `cross`, `100x`.
2. Mode segmented control: `Open`, `Close`.
3. Available balance row: `Available`, `00.000 USDT`, add icon.
4. Order type selector: `limit`.
5. Price input: label `price(USDT)` or `price`, value, optional `BBO`.
6. Amount input: label `Amount`, unit selector such as `BTC`.
7. Percentage slider with tick marks.
8. `TP/SL` control.
9. Estimate rows: `max long`, `cost` or `Margin`, `liq.price`.
10. Directional actions: `Open Long`, `Open Short`, or `Buy/Long`, `Sell/Short`.

Rules:

- Keep controls dense and vertically stable.
- Use 38-44px input/button height.
- Keep available balance above price/amount inputs.
- Long/buy uses success; short/sell uses error.
- Do not use brand blue for long/short buttons.
- Unit selectors sit inside or adjacent to inputs.
- `TP/SL` is a compact control, not a full explanation block.

## Order Book

Observed anatomy:

1. Funding/countdown summary: `Funding / Countdown`, `+0.0100% / 05:49:18`.
2. Header: `Price (USDT)`, `Size (BTC)`.
3. Ask rows with red/error price logic and low-contrast depth bars.
4. Mid price block: emphasized price and secondary reference price.
5. Bid rows with green/success price logic and low-contrast depth bars.
6. Ratio strip: `B 39%`, `61% S`.
7. Optional precision selector such as `0.01`.

Rules:

- Use tabular numbers.
- Keep rows compact, typically 24px rhythm.
- Depth bars must sit behind values and never reduce text readability.
- Mid price should be visually distinct but not oversized.
- Ratio strip is compact and anchored near the order book bottom.

## Orders / Positions / Assets Panel

Observed anatomy:

- Tabs: `orders(0)`, `positions(0)`, `assets`.
- Right utility icon: `file-minus-01`.
- Context row: `Current Trading Pair`.
- Empty balance state: `Available: 0.0000 USDT`.
- Empty prompt: deposit/transfer/demo trading actions depending the context.

Rules:

- Counts stay in tab labels.
- Empty states remain compact and action-oriented.
- Do not use large decorative illustrations.
- Keep account actions visible when balance or data is empty.

## TP/SL Bottom Sheet

Observed anatomy:

1. Mask/scrim.
2. Bottom sheet surface with drag handle.
3. Title: `TP/SL`.
4. Pair/order summary: `BTCUSDT`, `Perp`, `limit`, `Open long`, leverage.
5. Summary rows: `Entry Price`, `Last Price`, `Est.Liq.Price`.
6. Tabs: `fixed position(0)`, `all position`.
7. Primary action area.
8. Compact empty state.
9. Home indicator.

Rules:

- Use `bg/mask` for scrim and `bg/model` for sheet.
- Mobile sheet top corners may be rounded.
- State summary comes before controls.
- Primary action must not jump when content changes.

## Market Table

Recommended anatomy for web:

- Pair column.
- Last price.
- 24h change.
- High/low or volume.
- Optional sparkline.
- Trade action.

Rules:

- Pair and price columns should be scannable.
- Use positive/negative semantic colors only for movement.
- Keep row height dense.
- Use a compact action button, not a large CTA in every row.

## Wallet / Asset Table

Recommended anatomy:

- Coin/asset.
- Available.
- Frozen/in order.
- Total value.
- Actions: deposit, withdraw, transfer.

Rules:

- Balance values use tabular numbers.
- Hidden-balance state should preserve layout width.
- Account actions use brand or secondary button tokens, not direction colors.

