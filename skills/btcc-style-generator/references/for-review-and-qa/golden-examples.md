# BTCC Golden Examples

> See `references/rules.md` for global rules. Examples below show the minimum shape of each surface; their "why" links back to rules.md.

These are structural benchmarks, not pixel specs.

> **Source-verification note.** Only the contract-trading examples are backed by a verified Figma source page (`合约pro`, node `1262:304`; main mobile frame `合约pro-dark` `3112:1423`, per rules.md R-SCOPE-1). Market table, wallet/assets, and auth/login examples below are general BTCC-style conventions consistent with the verified contract surface; their Figma source pages were not returned in the current `get_metadata` pass. If han points at a specific Figma node for one of these surfaces, re-verify before treating the shapes below as canonical.

## Contract Trading Desktop

Purpose: dense pro trading workspace.

Required first viewport:

- Top product bar with pair selector, market price, 24h stats, and compact utility icons.
- Main chart region as the largest area.
- Right or side order book with bid / ask rows and depth bars.
- Order form with `Limit`, `Market`, leverage / margin controls, `Available`, `TP/SL`, `Open Long`, and `Open Short`.
- Bottom tabbed table: `Positions(0)`, `Open Orders(0)`, `Order History`, `Trade History`, `Assets`.

BTCC traits:

- Selected neutral controls and the `Open Long` button share brand blue (rationale: rules.md R-COLOR-1).
- `Open Short` button is error red (rationale: rules.md R-COLOR-1).
- Bid rows, percent change, and pnl text remain green / red as numeric direction cues (rationale: rules.md R-COLOR-2).
- Numeric columns are tabular and tightly aligned (rationale: rules.md R-LAYOUT-2).
- Local icons: `market-stats.svg`, `kline.svg`, `more.svg`, `dropdown.svg`, `warning-circle.svg` (per rules.md R-ICON-1 source order).

Forbidden drift:

- Marketing hero, large promotional banner, empty chart-only page, or form hidden below the fold (violates rules.md R-LAYOUT-1).

## Contract Trading Mobile

Purpose: compact app-like trading screen.

Required first viewport:

- Status / app header if mocking an app shell.
- Pair selector row with price, change, K-line / stat / more icons.
- Compact chart or tabbed market module.
- Order book and order form reachable without leaving the screen pattern (rationale: rules.md R-LAYOUT-1).
- Bottom nav when representing full app context.

BTCC traits:

- Side gutters and touch targets follow rules.md R-LAYOUT-2.
- Dense controls but no clipped labels.
- Bottom actions remain visible and stateful.

Forbidden drift:

- Desktop table squeezed unreadably into mobile, tiny touch targets, or decorative app-store-style hero (violates rules.md R-LAYOUT-1, R-LAYOUT-2).

## Market Table

Purpose: scan and compare pairs.

Required modules:

- Segmented tabs for watchlist / category / sort state.
- Pair rows with symbol, secondary metadata, last price, and percent change.
- Optional sparkline or compact mini chart.
- Filters / search remain compact.

BTCC traits:

- Positive / negative movement uses green / red as numeric semantics (rationale: rules.md R-COLOR-2).
- Price and percent are right-aligned (rationale: rules.md R-LAYOUT-2).
- Rows are dense, separated by thin dividers or subtle surface changes (rationale: rules.md R-LAYOUT-2).

Forbidden drift:

- Card grid of coins, large logos, or educational descriptions per asset (violates rules.md R-LAYOUT-2).

## Wallet / Assets

Purpose: account balances and fund movement.

Required modules:

- Total assets summary with hidden / show toggle.
- Shortcut actions: `Deposit`, `Withdraw`, `Transfer` (vocabulary per rules.md R-NAME-2).
- Asset list with coin, available, frozen / in-order, approximate value.
- Records or history tab when space allows.

BTCC traits:

- Use `plus-circle.svg`, `transfer.svg`, `orders-file.svg` where appropriate (per rules.md R-ICON-1 source order).
- Balances use fixed decimals and asset units (per rules.md R-NAME-2 placeholders).
- Empty balances use `0.0000` or `--`, not vague placeholders (per rules.md R-NAME-2).

Forbidden drift:

- Fintech lifestyle landing page, large cards nested inside cards, or promotional rewards as the main hierarchy (violates rules.md R-LAYOUT-1, R-LAYOUT-2).

## Auth / Login

Purpose: fast account entry.

Required modules:

- Login / register switch.
- Email / phone account input.
- Password or verification code input.
- Primary CTA, secondary account recovery, and risk / security note.

BTCC traits:

- Restrained visual weight (rationale: rules.md R-LAYOUT-2).
- Brand blue for primary CTA (rationale: rules.md R-COLOR-2 — brand blue is the primary neutral action).
- Concise risk / security copy.
- Decorative illustration only if the original page pattern requires it.

Forbidden drift:

- Long marketing value proposition before the form, oversized gradient hero, or social-app-style onboarding (violates rules.md R-LAYOUT-1).
