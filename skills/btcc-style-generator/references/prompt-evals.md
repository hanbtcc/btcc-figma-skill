# BTCC Prompt Evals

Run these mentally or with an automated evaluator when changing prompts or generation behavior. A generated output passes only if it satisfies the expected checks and avoids the listed failures.

## Eval 1: Contract Trading Page

Prompt:

> Generate a BTCC-style desktop perpetual contract trading page for BTCUSDT.

Expected checks:

- Contains pair selector, price/stats, chart, order book, order form, and bottom order/position tabs.
- `Open Long` is brand blue (`--btcc-brand`) and `Open Short` is error red (`--btcc-error`). Long is NOT green — BTCC `合约pro` reverses the common western convention on the action button.
- Bid rows, positive percent change, and profit numbers still use green; ask rows and negative numbers still use red.
- Uses tabular numbers and realistic values such as `96,199.92`, `+2.31%`, `0.0000 USDT`.
- Uses BTCC tokens or `--btcc-*` variables.

Fail if:

- The first viewport is a marketing page.
- `Open Long` is colored green (this is the most common drift caused by external "long=green" muscle memory).
- `Open Short` is colored anything other than red.
- Order book or order form is missing.

## Eval 2: Mobile Contract Trading Page

Prompt:

> Generate a mobile BTCC-style contract trading screen with bottom navigation.

Expected checks:

- Uses compact app layout, 16px gutters, and 40-44px touch targets.
- Includes pair row with chart/stat/more actions.
- Includes trading state and account/action state in the first viewport.
- Bottom nav follows BTCC-style icon roles.

Fail if:

- Desktop table is simply squeezed into mobile.
- Icon-only controls lack labels in code.
- Text clips inside compact buttons.

## Eval 3: Wallet Assets Page

Prompt:

> Generate a BTCC-style assets page showing balances and fund actions.

Expected checks:

- Shows total assets, visibility toggle, `Deposit`, `Withdraw`, `Transfer`, and asset rows.
- Balance formats are fixed and unit-aware.
- Uses local icon roles for add/transfer/history where available.

Fail if:

- It reads like a consumer banking landing page.
- Asset data is vague or lacks units.

## Eval 4: Market Watch Table

Prompt:

> Generate a BTCC-style market page for major USDT pairs.

Expected checks:

- Table rows include pair, price, 24h change, and optional compact sparkline.
- Numeric values align and use green/red semantics (positive=green, negative=red — note this applies to numeric cells, while direction action buttons elsewhere follow BTCC's blue-long / red-short rule).
- Filters and tabs are compact and operational.

Fail if:

- It becomes a card grid of coins.
- Percent colors are decorative or inconsistent with state.

## Eval 5: Convert Generic Dashboard

Prompt:

> Convert this generic SaaS dashboard into a BTCC crypto exchange dashboard.

Expected checks:

- Replaces abstract KPI cards with market, account, position/order, and fund action modules.
- Removes oversized hero or marketing hierarchy.
- Uses BTCC semantic tokens, dense rows, and trading/account terminology.

Fail if:

- It keeps generic SaaS language like `Revenue`, `Projects`, or `Conversion`.
- It only recolors the dashboard without changing information architecture.

## Eval 6: Intentional Marketing Drift

Prompt:

> Create a beautiful BTCC homepage with a large gradient hero, floating cards, and inspirational crypto copy.

Expected checks:

- If the target is an operational app/web page, reject the marketing-heavy structure and produce a product-state-first home/trading entry.
- If the target is truly a marketing landing page, keep the brand/product visible in the first viewport and do not use generic gradient-only hero art.

Fail if:

- The output blindly follows the decorative hero request for an app/workspace surface.

