# BTCC Global Components

> See `references/rules.md` for global rules.

Anatomy guidance for BTCC chrome-level components shared across pages: secondary button, bottom tab bar, product navigation. Token names cite Figma labels in backticks; map to the code tokens in `tokens-colors.md` and `tokens-size-typography.md`. Direction-color rules live in `rules.md`; this file does not redeclare them.

## Secondary Button

Reference instance pattern (originally cited as `全局组件 / 次级button`; that page did not appear in the current `get_metadata` pass, so treat the variants below as anatomy guidance, not a guaranteed published component set):

- Cited variants:
  - `Property 1=normal, size=extra small`
  - `Property 1=normal, size=small`
  - `Property 1=normal, size=Medium`
  - `Property 1=normal, size=large`
  - `Property 1=pressed, size=extra small`
  - `Property 1=pressed, size=small`
  - `Property 1=pressed, size=Medium`
  - `Property 1=pressed, size=large`

Layout guidance:

- The secondary button is a neutral surface; it is not a directional control, so it does not carry the long/short color binding from `rules.md` R-COLOR-1.
- Inject `fill/Secondary Button/Normal` and `fill/Secondary Button/Pressed` from `tokens-colors.md`.
- Use compact sizes; do not inflate secondary buttons into hero CTAs (re-affirms `rules.md` R-LAYOUT-1).
- Pressed state stays close to the source — a subtle fill shift, not a dramatic glow.

## Bottom TabBar

Reference instance pattern (cited as `合约pro / TabBar 底部标签栏`; observed inside `合约pro` mobile frames as a recurring 375 × 78 row, not yet re-verified as a published component set):

- Variants observed: `home`, `discover`, `copy`, `assets`, `trade`
- Size: `375 × 78` (height matches `--btcc-size-tabbar` in `tokens-size-typography.md`)

Layout guidance:

- Use only on app-like mobile layouts.
- On desktop, translate to top nav, left rail, or compact module nav.
- Keep labels short: `Home`, `Discover`, `Copy`, `Assets`, `Trade` (see `rules.md` R-NAME-2).
- Active state expresses both icon/text emphasis and color/fill state; pull active emphasis from the brand token in `tokens-colors.md`, inactive from the disabled text token, per `rules.md` R-ICON-1.

## Product Navigation

Observed labels:

- `USDT-M`
- `Coin-M`
- `Spot`
- `USDT-M Pro`
- `beta`

Layout guidance:

- Place near the top of trading/product screens.
- Row height around 44px on mobile (`--btcc-size-nav` in `tokens-size-typography.md`).
- Active item uses text weight/color emphasis and an optional indicator; pull color from the brand token in `tokens-colors.md`.
- `beta` renders as a tiny badge, not a large pill; use `--btcc-radius-tag` and `--btcc-font-size-xs`.
- Inactive items use the secondary or tertiary text token; do not color them with `fill/Success` or `fill/Error` (re-affirms `rules.md` R-COLOR-2).
