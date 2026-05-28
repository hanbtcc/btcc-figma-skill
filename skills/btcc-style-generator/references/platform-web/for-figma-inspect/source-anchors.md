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
| `7628:74717` | `LP活动` | Verified (2026-05-28) — campaign landing-page reference; see "LP activity reference" below |

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

## LP activity reference (`7628:74717`)

Verified canvas containing BTCC's production campaign landing pages. Use as **reference for ANY new BTCC campaign LP** rather than inventing layout from scratch. The canonical desktop sample is `7752:73942 jjj交易赛` (1920 × 6873).

### Top-level LP frames inside `7628:74717`

| Node ID | Name | Size | Role |
| --- | --- | --- | --- |
| `7752:73942` | `jjj交易赛` | 1920 × 6873 | Desktop campaign LP — canonical layout |
| `7872:82203` | `jjj交易赛-h5` | 375 × 8315 | H5 mobile campaign LP variant |

### Verified anatomy of `7752:73942` (desktop campaign)

Module sequence top → bottom inside the 1920-wide frame, content area is 1200 wide centered (left margin 360):

| Module | Node ID | Size | Notes |
| --- | --- | --- | --- |
| Hero (full-bleed) | `7752:84855` | 1920 × 903 | Full-bleed image (`sdfs 1`) + 194-tall lower overlay (`Rectangle 893`) — this is the BTCC-approved exception to "no marketing hero" because the content below stays operational |
| Hero copy + CTA | `7752:84791` | 768 × 336 | Title 768×112 + subtitle 521×56 + CTA group 234×56 (Register Now 168×56 + share 76×56), positioned 312/283 inside the hero |
| Content column | `7801:96583` | 1200 × 5238 | Holds every operational module below |
| Pool progress | `7801:96426` | 1200 × 686 | **Prize pool accrual timeline** — 13 ticks @ 44×68 + 987×4 progress bar; this is the BTCC pattern for "pool grows with volume" |
| My status | `7801:96560` | 1200 × 236 | Two 584×156 cards: "My Volume" + "Estimated Reward", numbers @ 48px, decorative side art 175-192 wide |
| Leaderboard | `7801:96584` | 1200 × 980 | Top-3 hero cards 378.6×325 (with 146×300 background numerals) + table for ranks 4-10 |
| Reward distribution rules | `7833:14693` | 1200 × 514 | **Rules as a 4-column data table** (Rank / Share / Min Volume / —), not paragraphs |
| Profit-rate rules table | `7833:14947` | 1200 × 514 | Mirror of the trading-volume rules table |
| Jersey & badge requirements | `7833:14402` | 1200 × 740 | Two 1200×314 strips, each with 414×314 prize art + copy block |
| Terms & conditions | `7833:15006` | 1200 × 824 | Section title 40px centered + 1200 × 744 long-form text |

> Note: `7752:84858` (the "Win your share of 300,000 USDT" educational paragraph) is `hidden=true` in the source — the BTCC team deliberately removed marketing copy from the live layout.

### Pattern hints for new LP work

These are observed conventions in the verified `jjj交易赛` LP. Mirror them rather than invent:

- **Section title**: 40px, centered, 80px gap to its content body.
- **Pool visualization**: progress-bar-with-ticks beats abstract "pool number" cards. The bar reads operationally.
- **"My status" lives as its own block**, not buried inside other modules. Numbers @ 48px.
- **Rules use tabular data** (Rank | Share | Threshold). Long prose rules go to a final terms block.
- **Decorative imagery is allowed in dedicated prize blocks** (jersey, badge, top-3 background numerals). Keep it out of the operational modules.
- **Hidden educational paragraph**: BTCC frequently authors but hides verbose hero subtitles — when in doubt, drop the paragraph.

## Token / Icon caveat

Per `platform-web/rules-web.md` R-ASSETS-WEB, `assets/btcc-tokens.{json,css}` and `assets/icons/*.svg` are APP-derived. Web code generation must reconcile them against the Web Figma local-variables collection, or carry an Unverified marker.
