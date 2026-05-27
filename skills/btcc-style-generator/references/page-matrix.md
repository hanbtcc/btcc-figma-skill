# BTCC Page Matrix

Use this file when choosing structure for a requested BTCC page.

> **Source-verification note.** Only `合约pro` (and `设计规范` for tokens) is currently verified in the Figma file root via `get_metadata`. Sections below for `home`, `markets`, `wallet`, `auth`, `copy-trading`, `spot`, `c2c`, `h5`, and modal/sheet patterns are general BTCC anatomy guidance — they do NOT have a confirmed source page in the current pass. Treat them as conventions consistent with the verified `合约pro` style; if han points at a specific Figma node for one of these surfaces, re-verify via `get_design_context` before relying on the rules below.

## Contract Pro

Source page: `合约pro` (verified, node `1262:304`; main mobile frame `合约pro-dark` `3112:1423`).

First viewport must include:

- Product nav: `USDT-M`, `Coin-M`, `Spot`, `USDT-M Pro`, `beta`.
- Pair header: pair, contract tag, movement, chart/action icons.
- Trading form.
- Order book.
- Orders/positions/assets panel.

Desktop adaptation:

- Chart/market area should become the largest central region.
- Order form and order book become persistent side columns.
- Orders/positions/assets panel sits below chart or in a secondary region.

Do not:

- Make a marketing hero.
- Hide order form below the fold.
- Color the `Open Long` button green; in BTCC `合约pro` the long button is brand blue and the short button is red.

## Exchange Home

Source page alias: `home` *(not verified in current Figma metadata pass; treat as BTCC-style convention only)*

First viewport should include:

- Compact product navigation.
- Market snapshot or top movers.
- Entry modules for Contract, Spot, Copy Trading, Wallet/Assets.
- Account action such as Login, Deposit, or Trade.

Do not:

- Lead with a decorative crypto slogan.
- Use oversized hero type without market/product utility.

## Markets

Source page alias: `markets` *(not verified in current Figma metadata pass; convention only)*

Must include:

- Category tabs.
- Search/filter.
- Dense market table.
- Pair, last price, change, volume/high-low, trade action.

Do not:

- Turn market data into large loose cards unless on mobile and still scannable.
- Use green/red outside movement state.

## Wallet / Assets

Source page aliases: `assets`, `profile-settings` *(not verified in current Figma metadata pass; convention only)*

Must include:

- Balance summary.
- Deposit, withdraw, transfer actions.
- Asset table.
- History tabs or recent transactions.
- Hidden-balance state when relevant.

Do not:

- Use directional red/green for neutral account actions.
- Make empty state illustration-first.

## Auth

Source page alias: `auth` *(not verified in current Figma metadata pass; convention only)*

Must include:

- Login/register switch.
- Email/phone and password or verification fields.
- Submit action.
- Security cues.
- Product context through compact market/account modules.

Do not:

- Create a generic illustration-led auth hero.
- Use long marketing copy inside the form area.

## Copy Trading

Source page alias: `copy-trading` *(not verified in current Figma metadata pass; convention only)*

Must include:

- Trader leaderboard.
- ROI/PnL/win-rate/risk/follower metrics.
- Filters.
- Copy action.
- Strategy detail or preview.

Do not:

- Make it feel like social media.
- Use performance colors as decoration.

## Spot

Source page alias: `spot` *(not verified in current Figma metadata pass; convention only)*

Must include:

- Pair selector.
- Market/chart area.
- Order form with buy/sell.
- Order book or recent trades.
- Open orders/history.

Do not:

- Reuse contract-only terminology such as leverage unless the page includes margin features.

## C2C

Source page alias: `c2c` *(not verified in current Figma metadata pass; convention only)*

Must include:

- Buy/sell mode.
- Currency/payment filters.
- Offer list with price, limit, payment method, merchant state.
- Action button.

Do not:

- Use order-book layout if the flow is an offer marketplace.

## H5 / Mobile Web

Source page alias: `h5` *(not verified in current Figma metadata pass; convention only)*

Must include:

- Mobile-first density.
- 16px side gutters.
- 40-44px touch targets.
- Bottom sheets for focused tasks.
- Bottom navigation only for app-like pages.

Do not:

- Directly shrink desktop tables until text is unreadable.

## Modal / Bottom Sheet

Use for:

- TP/SL setup.
- Pair selector.
- Order confirmation.
- Transfer/deposit flows.
- Risk warning.

Must include:

- Scrim if modal.
- State summary.
- Controls.
- Stable primary action.

Mobile:

- Bottom sheet with drag handle.

Desktop:

- Center modal or side panel, depending workflow complexity.

