# BTCC Data Format

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

## Semantic Color

Use color for market/account state, not decoration.

| Meaning | Token intent |
| --- | --- |
| Buy, bid, long, positive, profit, success | success/green |
| Sell, ask, short, negative, loss, error | error/red |
| Primary neutral action, selected tab, brand affordance | brand blue |
| Warning, liquidation risk, abnormal status | warning/orange |
| Funding/check/limited reward highlight | check/yellow |
| Disabled, unavailable, placeholder | text/icon disabled and low-contrast fill |

Do not use brand blue for `Open Long` or `Open Short`. Use success and error.

## Labels

Preferred terms:

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

Avoid verbose educational text in trading panels. Use short labels and compact helper text.

## Table Alignment

- Right-align numeric columns.
- Left-align pair, asset, status, and action labels.
- Use `font-variant-numeric: tabular-nums`.
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

