# BTCC Trading Components

> See `references/rules.md` for global rules.

Anatomy guidance for BTCC trading-surface components: market pair header, trading form, order book, TP/SL bottom sheet. Token names cite Figma labels in backticks; map to the code tokens in `tokens-colors.md` and `tokens-size-typography.md`. Direction-color and tabular-number rules live in `rules.md`; this file does not redeclare them.

## Market Pair Header

Observed anatomy:

- Pair: `BTCUSDT`
- Contract tag: `Perp`
- Change: `-2.14%`
- Actions: market stats, chart/K-line, more

Layout guidance:

- Surface the active pair or market context as the first row.
- Pair name reads larger and stronger than secondary metadata.
- Apply numeric direction color per `rules.md` R-COLOR-2; use `fill/Success` / `fill/Error` from `tokens-colors.md` for change values.
- Pair selector chevron is compact, around 16px (see `tokens-size-typography.md`).

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

Layout guidance:

- Keep controls dense and vertically stable.
- Input/button height follows `--btcc-size-input` / `--btcc-size-button` (see `tokens-size-typography.md`).
- Available balance sits above price/amount inputs.
- `Open Long` / `Open Short` buttons inject token fills per `rules.md` R-COLOR-1; pressed states map to the corresponding `*-pressed` tokens in `tokens-colors.md`.
- Numeric direction cues inside the form (bid rows in adjacent panels, percent change, pnl text) follow `rules.md` R-COLOR-2.
- Unit selectors sit inside or adjacent to inputs.
- `TP/SL` is a compact control, not an explanation block.

## Order Book

Observed anatomy:

1. Funding/countdown summary: `Funding / Countdown`, `+0.0100% / 05:49:18`.
2. Header: `Price (USDT)`, `Size (BTC)`.
3. Ask rows with error-token price logic and low-contrast depth bars.
4. Mid price block: emphasized price and secondary reference price.
5. Bid rows with success-token price logic and low-contrast depth bars.
6. Ratio strip: `B 39%`, `61% S`.
7. Optional precision selector such as `0.01`.

Layout guidance:

- Ask/bid color assignments follow `rules.md` R-COLOR-2; pull `fill/Error` and `fill/Success` from `tokens-colors.md`.
- Numeric columns follow `rules.md` R-LAYOUT-2 (tabular-nums, right-aligned).
- Rows stay compact, typically 24px rhythm (`--btcc-size-row`).
- Depth bars sit behind values and never reduce text readability.
- Mid price reads as visually distinct but not oversized.
- Ratio strip is compact and anchored near the order book bottom.

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

Layout guidance:

- Scrim uses `bg/mask`; sheet surface uses `bg/model` (see `tokens-colors.md`).
- Mobile sheet top corners may be rounded via `--btcc-radius-card`.
- State summary precedes controls.
- Primary action position stays stable when content changes (re-affirms `rules.md` R-LAYOUT-1).
- The `Open long` / `Open short` summary chip in the order summary row is descriptive text; its color follows `rules.md` R-COLOR-1 only when rendered as an action button, not as an inline label.
