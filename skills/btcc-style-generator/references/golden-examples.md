# BTCC Golden Examples

Use these as structural benchmarks. They are not pixel specs; they describe the minimum shape a generated BTCC-style page should preserve.

## Contract Trading Desktop

Purpose: dense pro trading workspace.

Required first viewport:

- Top product bar with pair selector, market price, 24h stats, and compact utility icons.
- Main chart region as the largest area.
- Right or side order book with bid/ask rows and depth bars.
- Order form with `Limit`, `Market`, leverage/margin controls, `Available`, `TP/SL`, `Open Long`, and `Open Short`.
- Bottom tabbed table: `Positions(0)`, `Open Orders(0)`, `Order History`, `Trade History`, `Assets`.

BTCC traits:

- Brand blue only for selected neutral controls.
- Long button is green; short button is red.
- Numeric columns are tabular and tightly aligned.
- Use local icons: `market-stats.svg`, `kline.svg`, `more.svg`, `dropdown.svg`, `warning-circle.svg`.

Forbidden drift:

- Marketing hero, large promotional banner, empty chart-only page, or form hidden below the fold.

## Contract Trading Mobile

Purpose: compact app-like trading screen.

Required first viewport:

- Status/app header if mocking an app shell.
- Pair selector row with price, change, K-line/stat/more icons.
- Compact chart or tabbed market module.
- Order book and order form reachable without leaving the screen pattern.
- Bottom nav when representing full app context.

BTCC traits:

- 16px side gutters.
- 40-44px touch targets.
- Dense controls but no clipped labels.
- Bottom actions remain visible and stateful.

Forbidden drift:

- Desktop table squeezed unreadably into mobile, tiny touch targets, or decorative app-store-style hero.

## Market Table

Purpose: scan and compare pairs.

Required modules:

- Segmented tabs for watchlist/category/sort state.
- Pair rows with symbol, secondary metadata, last price, and percent change.
- Optional sparkline or compact mini chart.
- Filters/search remain compact.

BTCC traits:

- Positive/negative movement is green/red.
- Price and percent are right-aligned.
- Rows are dense, separated by thin dividers or subtle surface changes.

Forbidden drift:

- Card grid of coins, large logos, or educational descriptions per asset.

## Wallet / Assets

Purpose: account balances and fund movement.

Required modules:

- Total assets summary with hidden/show toggle.
- Shortcut actions: `Deposit`, `Withdraw`, `Transfer`.
- Asset list with coin, available, frozen/in-order, approximate value.
- Records or history tab when space allows.

BTCC traits:

- Use `plus-circle.svg`, `transfer.svg`, `orders-file.svg` where appropriate.
- Balances use fixed decimals and asset units.
- Empty balances use `0.0000` or `--`, not vague placeholders.

Forbidden drift:

- Fintech lifestyle landing page, large cards nested inside cards, or promotional rewards as the main hierarchy.

## Auth / Login

Purpose: fast account entry.

Required modules:

- Login/register switch.
- Email/phone account input.
- Password or verification code input.
- Primary CTA, secondary account recovery, and risk/security note.

BTCC traits:

- Keep visual weight restrained.
- Use brand blue for primary CTA.
- Use concise risk/security copy.
- Do not distract with large decorative illustration unless the original page pattern requires it.

Forbidden drift:

- Long marketing value proposition before the form, oversized gradient hero, or social-app-style onboarding.

