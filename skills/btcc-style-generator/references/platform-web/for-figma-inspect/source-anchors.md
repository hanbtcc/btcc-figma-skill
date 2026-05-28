# BTCC Web — Figma Source Anchors

> See `references/rules.md` for global rules and `references/platform-web/rules-web.md` for web-specific extensions.

Verified on 2026-05-28 via Figma `get_metadata`. Re-verify if older than ~30 days.

## File

| Field | Value |
| --- | --- |
| Name | `新BTCC WEB` |
| File key | `VrE25c6IAuIieWngebNnwx` |

## Top-level canvases

| Node ID | Name | Status |
| --- | --- | --- |
| `0:1` | `设计规范` | Verified — primary source for tokens, components, desktop trading anatomy |
| `3089:7459` | `其他-马甲包官网/桌面图标` | Unverified |

## Verified sub-frames inside `0:1 设计规范`

Anchors below are directly observed in Figma metadata. Names retain Chinese labels exactly as authored.

| Node ID | Name | Role |
| --- | --- | --- |
| `651:14846` | `合约pro下单框` | Desktop order form (1214 × 698) |
| `647:13104` | `盘口` | Order book (695 × 684) |
| `647:12465` | `顶部导航条` | Top global nav (1961 × 185) |
| `663:2867` | `右侧选项` | Right-side panel (540 × 1134) |
| `651:13295` | `已选列表` | Selected pair list (1556 × 32) |
| `647:12512` | `右顶信息` | Top-right info bar (1556 × 56) |
| `554:5210` | `已选` | Selected tab cell (437 × 66) |
| `554:5221` | `二级tab组` | Secondary tab group (172 × 64) |
| `554:5228` | `一级tab组` | Primary tab group (264 × 80) |
| `554:5235` | `下单组` | Order action group (329 × 102) |
| `554:5252` | `次级button` | Secondary button (274 × 68) |
| `554:5259` | `开多下单button` | Open Long button (389 × 80) — must use `--btcc-brand`, see rules.md R-COLOR-1 |
| `554:5266` | `开空下单button` | Open Short button (395 × 80) — must use `--btcc-error`, see rules.md R-COLOR-1 |
| `554:5273` | `计算器` | Calculator (368 × 380) |
| `554:5318` | `止盈止损` | TP/SL panel (625 × 285) |
| `770:8645` | `Alert` | Alert dialog (336 × 211) |
| `4558:37495` | `toast` | Toast (584 × 98) |
| `734:14906` | `switch` | Switch (106 × 56) |
| `741:4552` | `一级button` | Primary button (757 × 88) |
| `741:4616` | `次级button (large)` | Secondary button large (757 × 88) |
| `1109:4825` | `单选框` | Radio (173 × 56) |
| `5568:196480` | `分页` | Pagination (352 × 32) |
| `1088:6704` | `主题色阶梯度` | Brand color ramp (448 × 753) |
| `8367:106176` | `dark-辅助色阶梯度` | Dark aux color ramp (448 × 753) |
| `8367:106219` | `light-辅助色阶梯度` | Light aux color ramp (448 × 753) |

## Unverified frames inside `0:1`

The remaining frames in this canvas are color-swatch scratch areas or cross-platform mobile mockups, e.g. `red` / `green` / `orange` test swatches at `1088:5613` / `5647` / `5681` and a 360 × 737 mobile mockup `合约pro下单 128817:91276`. Treat as Unverified per `rules.md` R-SCOPE-1; mark any derived doc with `> Source: BTCC-style convention; not in verified Figma metadata pass.`

## Token / Icon caveat

Per `platform-web/rules-web.md` R-ASSETS-WEB, `assets/btcc-tokens.{json,css}` and `assets/icons/*.svg` are APP-derived. Web code generation must reconcile them against the Web Figma local-variables collection, or carry an Unverified marker.
