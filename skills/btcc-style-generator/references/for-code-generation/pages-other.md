# BTCC Other Pages

> # ⚠ Unverified / 未验证
> Source: BTCC-style convention; not in verified Figma metadata pass.

> See `references/rules.md` for global rules.

This file holds page-level specs for surfaces other than `合约pro`. None of these are confirmed by the current `get_metadata` pass on the BTCC Figma file. Treat all anatomy below as conventions consistent with the verified `合约pro` style; if han points at a specific Figma node for one of these surfaces, re-verify via `get_design_context` before relying on the rules below. The verified contract spec lives in `pages-contract.md`. Each section below MUST keep its `> Unverified` marker. Section grouping below uses the risk tiers from the change design (Open Question 3): Tier A is "completely unseen in the metadata pass", Tier B is "partially observed but not aligned to a published component set", Tier C is "shared cross-cutting modal/sheet patterns".

Sections in this file MUST also follow `rules.md` R-COLOR-1, R-COLOR-2, R-LAYOUT-1, R-LAYOUT-2 even though the underlying Figma source is unverified — defaults inherit from the verified contract spec.

## Tier A — Completely Unseen Surfaces

### Exchange Home

> Unverified — not in the current `get_metadata` pass; treat as BTCC-style convention only.

Source page alias: `home`.

First viewport should include:

- Compact product navigation.
- Market snapshot or top movers.
- Entry modules for Contract, Spot, Copy Trading, Wallet/Assets.
- Account action such as Login, Deposit, or Trade.

Anti-patterns:

- Lead with a decorative crypto slogan (violates `rules.md` R-LAYOUT-1).
- Oversized hero type without market/product utility (violates `rules.md` R-LAYOUT-1).

### Auth

> Unverified — not in the current `get_metadata` pass; treat as BTCC-style convention only.

Source page alias: `auth`.

Must include:

- Login/register switch.
- Email/phone and password or verification fields.
- Submit action.
- Security cues.
- Product context through compact market/account modules.

Anti-patterns:

- Generic illustration-led auth hero (violates `rules.md` R-LAYOUT-1).
- Long marketing copy inside the form area (violates `rules.md` R-LAYOUT-1).

### Copy Trading

> Unverified — not in the current `get_metadata` pass; treat as BTCC-style convention only.

Source page alias: `copy-trading`.

Must include:

- Trader leaderboard.
- ROI/PnL/win-rate/risk/follower metrics.
- Filters.
- Copy action.
- Strategy detail or preview.

Anti-patterns:

- Social-media feel that buries operational data (violates `rules.md` R-LAYOUT-1).
- Performance colors used as decoration (violates `rules.md` R-COLOR-2).

### C2C

> Unverified — not in the current `get_metadata` pass; treat as BTCC-style convention only.

Source page alias: `c2c`.

Must include:

- Buy/sell mode.
- Currency/payment filters.
- Offer list with price, limit, payment method, merchant state.
- Action button.

Anti-patterns:

- Reusing order-book layout when the flow is an offer marketplace.

## Tier B — Partially Observed Surfaces

### Markets

> Unverified — not in the current `get_metadata` pass; treat as BTCC-style convention only.

Source page alias: `markets`.

Must include:

- Category tabs.
- Search/filter.
- Dense market table (see `components-account.md` for the table anatomy).
- Pair, last price, change, volume/high-low, trade action.

Anti-patterns:

- Market data rendered as large loose cards on desktop (violates `rules.md` R-LAYOUT-2).
- Green/red used outside movement state (violates `rules.md` R-COLOR-2).

### Wallet / Assets

> Unverified — not in the current `get_metadata` pass; treat as BTCC-style convention only.

Source page aliases: `assets`, `profile-settings`.

Must include:

- Balance summary.
- Deposit, withdraw, transfer actions.
- Asset table (see `components-account.md`).
- History tabs or recent transactions.
- Hidden-balance state when relevant.

Anti-patterns:

- Directional red/green on neutral account actions (violates `rules.md` R-COLOR-2).
- Empty state that leads with illustration instead of next action (violates `rules.md` R-LAYOUT-1).

### Spot

> Unverified — not in the current `get_metadata` pass; treat as BTCC-style convention only.

Source page alias: `spot`.

Must include:

- Pair selector.
- Market/chart area.
- Order form with buy/sell.
- Order book or recent trades.
- Open orders/history.

Anti-patterns:

- Reusing contract-only terminology such as leverage when the page has no margin features (violates `rules.md` R-NAME-2).

### H5 / Mobile Web

> Unverified — not in the current `get_metadata` pass; treat as BTCC-style convention only.

Source page alias: `h5`.

Must include:

- Mobile-first density.
- 16px side gutters and 40-44px touch targets, per `rules.md` R-LAYOUT-2.
- Bottom sheets for focused tasks.
- Bottom navigation only for app-like pages.

Anti-patterns:

- Directly shrinking desktop tables until text is unreadable (violates `rules.md` R-LAYOUT-2).

## Tier C — Cross-Cutting Patterns

### Modal / Bottom Sheet

> Unverified — Figma has component-level modal/sheet nodes but no aligned page spec; treat as BTCC-style convention.

Use for:

- TP/SL setup (see `components-trading.md`).
- Pair selector.
- Order confirmation.
- Transfer/deposit flows.
- Risk warning.

Must include:

- Scrim if modal (`bg/mask` from `tokens-colors.md`).
- State summary.
- Controls.
- Stable primary action.

Mobile:

- Bottom sheet with drag handle; corners use `--btcc-radius-card` from `tokens-size-typography.md`.

Desktop:

- Center modal or side panel, depending on workflow complexity.
