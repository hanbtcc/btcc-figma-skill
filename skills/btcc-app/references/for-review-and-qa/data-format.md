# BTCC Data Format

> See `references/rules.md` for global rules. This file defines concrete data format conventions; rule rationale links back to rules.md.

Use this when generating exchange UI copy, mock data, tables, order forms, charts, wallet balances, and empty states.

## Number Rules

| Data | Format | Example |
| --- | --- | --- |
| Pair | uppercase base/quote without slash in compact labels | `BTCUSDT` |
| Pair with product | pair plus product tag | `BTCUSDT Perp` |
| Price | comma thousands, 2 decimals by default | `96,199.92` |
| Index/mark price | same precision as market price unless source differs | `96,184.10` |
| Quantity | compact suffix for large values | `31.121K` |
| Balance | fixed 4 decimals plus asset | `0.0000 USDT` |
| Percent | signed, 2-4 decimals by context | `+0.0100%` |
| Leverage | compact multiplier | `100x` |
| Countdown | `HH:MM:SS` | `05:49:18` |
| Empty value | double dash | `--` |
| Position/order count | label plus count | `Positions(0)` |

These format conventions align with rules.md R-NAME-2 placeholders.

## Semantic Color Mapping

Color binds to market / account state, not decoration (see rules.md R-COLOR-2 — color is status, not decoration).

| Meaning | Token intent |
| --- | --- |
| Bid row, positive change, profit number, success toast | success / green |
| Ask row, negative change, loss number, error / destructive | error / red |
| Primary neutral action, selected tab, brand affordance, `Open Long` button | brand blue |
| `Open Short` button | error / red |
| Warning, liquidation risk, abnormal status | warning / orange |
| Funding / check / limited reward highlight | check / yellow |
| Disabled, unavailable, placeholder | text / icon disabled and low-contrast fill |

Direction-button mapping (the row "Open Long button = brand blue / Open Short button = error red") is a concrete instantiation of rules.md R-COLOR-1; do not re-derive it locally.

## Labels

Preferred terms (per rules.md R-NAME-2):

- `Open Long`
- `Open Short`
- `Limit`
- `Market`
- `TP/SL`
- `Available`
- `Margin`
- `Order Book`
- `Recent Trades`
- `Positions(0)`
- `Open Orders(0)`
- `Assets`
- `Deposit`
- `Transfer`
- `Withdraw`
- `Demo`
- `Perp`

Use short labels and compact helper text; avoid verbose educational text in trading panels (see rules.md R-LAYOUT-1).

## Table Alignment

Numeric and label alignment follows rules.md R-LAYOUT-2:

- Right-align numeric columns.
- Left-align pair, asset, status, and action labels.
- Numeric columns use `font-variant-numeric: tabular-nums`.
- Keep signs visible for deltas: `+2.31%`, `-0.48%`.
- Preserve precision consistency down a column.

## Mock Data Defaults

Use realistic but clearly mock exchange values:

| Surface | Safe defaults |
| --- | --- |
| Header pair | `BTCUSDT Perp`, `96,199.92`, `+2.31%` |
| Funding | `+0.0100% / 05:49:18` |
| Available balance | `0.0000 USDT` |
| Order input | `Price`, `Amount`, `TP/SL` |
| Wallet asset | `USDT`, `BTC`, `ETH` |
| Empty states | `No open orders`, `No positions`, `No records` |
