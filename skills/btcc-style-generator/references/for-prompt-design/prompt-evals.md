# BTCC Prompt Evals

> See `references/rules.md` for global rules.

Run these mentally or with an automated evaluator when changing prompts or generation behavior. A generated output passes only if it satisfies the expected checks and avoids the listed failures. Any rule cited below (direction colors, numeric semantics, dark-first layout, marketing-hero ban, naming, unverified-marker) is owned by `rules.md`; this file MUST NOT re-declare those rules.

## Eval 1: Contract Trading Page

Prompt:

> Generate a BTCC-style desktop perpetual contract trading page for BTCUSDT.

Expected checks:

- Contains pair selector, price/stats, chart, order book, order form, and bottom order/position tabs.
- Action-button colors comply with `rules.md` R-COLOR-1; numeric direction cues comply with R-COLOR-2.
- Uses tabular numbers (R-LAYOUT-2) and realistic values such as `96,199.92`, `+2.31%`, `0.0000 USDT`.
- Uses BTCC tokens (`--btcc-*`) instead of arbitrary hex (R-NAME-1).

Fail if:

- The first viewport is a marketing page (violates R-LAYOUT-1).
- The action-button direction colors deviate from R-COLOR-1 (most common drift: `Open Long` rendered green from western muscle memory).
- Order book or order form is missing.

## Eval 2: Mobile Contract Trading Page

Prompt:

> Generate a mobile BTCC-style contract trading screen with bottom navigation.

Expected checks:

- Compact app layout, gutters and touch targets per R-LAYOUT-2.
- Includes pair row with chart/stat/more actions.
- Trading state and account/action state both visible in the first viewport (R-LAYOUT-1).
- Bottom nav follows BTCC-style icon roles (R-ICON-1).

Fail if:

- Desktop table is simply squeezed into mobile.
- Icon-only controls lack accessible labels in code (R-ICON-1).
- Text clips inside compact buttons.

## Eval 3: Wallet Assets Page

Prompt:

> Generate a BTCC-style assets page showing balances and fund actions.

Expected checks:

- Shows total assets, visibility toggle, primary fund actions, and asset rows in the first viewport (R-LAYOUT-1).
- Balance formats follow BTCC trading vocabulary (R-NAME-2).
- Uses local icon roles for add/transfer/history where available (R-ICON-1).
- Page is treated as unverified surface and carries the marker per R-SCOPE-1.

Fail if:

- It reads like a consumer banking landing page (violates R-LAYOUT-1).
- Asset data is vague or lacks units.
- Unverified marker is missing (violates R-SCOPE-1).

## Eval 4: Market Watch Table

Prompt:

> Generate a BTCC-style market page for major USDT pairs.

Expected checks:

- Table rows include pair, price, 24h change, and optional compact sparkline.
- Numeric values right-align and use the numeric semantics defined in `rules.md` R-COLOR-2.
- Filters and tabs are compact and operational (R-LAYOUT-1, R-LAYOUT-2).
- Surface carries the unverified marker per R-SCOPE-1.

Fail if:

- It becomes a card grid of coins (violates R-LAYOUT-2).
- Percent colors are decorative or inconsistent with state (violates R-COLOR-2).

## Eval 5: Convert Generic Dashboard

Prompt:

> Convert this generic SaaS dashboard into a BTCC crypto exchange dashboard.

Expected checks:

- Replaces abstract KPI cards with market, account, position/order, and fund action modules.
- Removes oversized hero or marketing hierarchy (R-LAYOUT-1).
- Uses BTCC semantic tokens (R-NAME-1), dense rows (R-LAYOUT-2), and trading/account terminology (R-NAME-2).

Fail if:

- It keeps generic SaaS language like `Revenue`, `Projects`, or `Conversion` (violates R-NAME-2).
- It only recolors the dashboard without changing information architecture.

## Eval 6: Intentional Marketing Drift

Prompt:

> Create a beautiful BTCC homepage with a large gradient hero, floating cards, and inspirational crypto copy.

Expected checks:

- If the target is an operational app/web page, reject the marketing-heavy structure and produce a product-state-first home/trading entry per R-LAYOUT-1.
- If the target is truly a marketing landing page, keep the brand/product visible in the first viewport and avoid generic gradient-only hero art.

Fail if:

- The output blindly follows the decorative hero request for an app/workspace surface (violates R-LAYOUT-1).
