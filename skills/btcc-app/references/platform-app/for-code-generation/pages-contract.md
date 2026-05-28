# BTCC Contract Pro Page (verified)

> See `references/rules.md` for global rules.

Verified page spec for `合约pro` (Contract Pro). This is the only BTCC page-level spec backed by the current Figma metadata pass. Other surfaces live in `pages-other.md` and carry an `Unverified` marker.

## Contract Pro

Source page: `合约pro` (verified, node `1262:304`; main mobile frame `合约pro-dark` `3112:1423`).

First viewport must include:

- Product nav: `USDT-M`, `Coin-M`, `Spot`, `USDT-M Pro`, `beta`.
- Pair header: pair, contract tag, movement, chart/action icons.
- Trading form.
- Order book.
- Orders/positions/assets panel.

Desktop adaptation:

- Chart/market area becomes the largest central region.
- Order form and order book become persistent side columns.
- Orders/positions/assets panel sits below chart or in a secondary region.

Anti-patterns (each violates an R- rule in `rules.md`):

- Marketing hero on this surface (violates `rules.md` R-LAYOUT-1).
- Order form hidden below the fold (violates `rules.md` R-LAYOUT-1).
- `Open Long` painted with anything other than `fill/Brand`, or `Open Short` with anything other than `fill/Error` (violates `rules.md` R-COLOR-1; tokens live in `tokens-colors.md`).
- Numeric direction cues (bid rows, percent change, pnl) recolored away from success / error semantics (violates `rules.md` R-COLOR-2).

Component composition for this page:

- Pair header, trading form, order book, TP/SL bottom sheet — see `components-trading.md`.
- Orders/positions/assets panel — see `components-account.md`.
- Product navigation, bottom tab bar (mobile) — see `components-global.md`.
