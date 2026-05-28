> See `references/rules.md` for global rules.

# BTCC Icon Anchor Registry

Icon role names paired with Figma clues — where to find each icon in the BTCC Figma file and what naming hints to look for. Style/color rules are not declared here; see `rules.md` R-ICON-1 (icon source order, stroke style, accessibility) and R-COLOR-2 (color-as-status binding).

## Source Strategy

Follow `rules.md` R-ICON-1 for the source-order policy. The list below is the role-to-anchor lookup itself, not a re-statement of that rule.

## Local SVG Asset Anchors

These assets were exported from the original Figma `设计规范` page. Use them as the in-code anchor when the project does not already have an icon component for the role.

| Asset | Original Figma Cue | Role |
| --- | --- | --- |
| `assets/icons/market-stats.svg` | `bar-chart-square-down` | Market stats / analytics shortcut |
| `assets/icons/kline.svg` | `k线` | Candlestick / K-line chart |
| `assets/icons/more.svg` | `更多` | Overflow menu |
| `assets/icons/plus-circle.svg` | `plus-circle 1` | Add funds / add action |
| `assets/icons/warning-circle.svg` | `warning-circle` | Warning / info |
| `assets/icons/orders-file.svg` | `file-minus-01` | Orders, history, records, empty utility |
| `assets/icons/dropdown.svg` | `icon 2` | Dropdown / selector |
| `assets/icons/transfer.svg` | `顶部导航栏icon` | Transfer shortcut |
| `assets/icons/demo-trading.svg` | `模拟` | Demo trading |
| `assets/icons/discover.svg` | `line-chart-up-03` | Discover / market trend |

## Sizing Hints

These are the observed Figma frame/vector sizes per usage context — record only, not a rule. Layout/sizing rules belong in `for-code-generation/tokens-size-typography.md` and `rules.md` R-LAYOUT-2.

| Use | Observed size |
| --- | --- |
| Toolbar and product nav icons | 24px |
| Bottom navigation icons | 20-24px |
| Inline pair/unit icons | 16px |
| Dropdown chevrons and dense selectors | 10-14px |
| Warning/add mini icons | 12-14px |
| Mobile touch container | 40-44px |
| Desktop icon button container | 32-40px |

## Role Mapping (Figma anchor → role)

| Role | Original Figma Cue | Source Page | Observed size | Generic-icon fallback name |
| --- | --- | --- | --- | --- |
| Market stats | `bar-chart-square-down` | `设计规范` | 24px frame, 16px vector | `BarChart` |
| K-line / chart | `k线` | `设计规范` | 24px frame | `ChartCandlestick` |
| Overflow menu | `更多` | `设计规范` | 24px frame | `MoreHorizontal` |
| Pair/dropdown selector | `icon 2` | `设计规范` | 16px or 10px | `ChevronDown` |
| Add funds | `plus-circle 1` | `设计规范` | 14px frame | `PlusCircle` |
| Warning / info | `warning-circle` | `设计规范` | 12px frame | `AlertCircle` |
| Orders / history / empty utility | `file-minus-01` | `设计规范` | 24px frame | `FileMinus` |
| Deposit shortcut | deposit icon inside `Frame 1707481376` | `设计规范` | 24px in 40-44px container | `Wallet` or `Download` |
| Transfer shortcut | `顶部导航栏icon` | `设计规范` | 24px frame | `ArrowLeftRight` or `Repeat2` |
| Demo trading | `模拟` | `设计规范` | 24px frame | `BadgePlay` or equivalent |
| Bottom nav home | home tab graphic | `合约pro` | 18-24px | `Home` |
| Bottom nav discover | `line-chart-up-03` | `设计规范`, `合约pro` | 24px frame | `TrendingUp` |
| Bottom nav copy | copy tab graphic | `合约pro` | 18-24px | `Copy` |
| Bottom nav assets | `BTCCtp` / assets cue | `设计规范`, `合约pro` | 20px vector | `Wallet` |
| Bottom nav trade | trade tab graphic | `合约pro` | 18-24px | `ChartCandlestick` |
| System status | mobile signal, Wi-Fi, battery | `设计规范` | iOS-like native sizes | App-frame mockups only. |

For active-state coloring, disabled-state coloring, stroke style, and accessibility on icon-only buttons, see `rules.md` R-ICON-1 and R-COLOR-2 — do not re-declare those here.

## Figma Anchor Notes

- The `图标` page was empty in the extraction pass; rely on `设计规范` and `合约pro` observed icon nodes. (The empty-page status is also recorded in `source-anchors.md`.)
- Some icons are nested vectors with generic names like `Vector`, `Subtract`, or `Rectangle`. Use the parent frame name as the semantic source cue.
- When reading via Figma tools, collect parent names and sizes, not only leaf vector names.
