# BTCC Icon Registry

Use this file when choosing icons for BTCC-style UI, especially when the Figma plugin is available.

## Source Strategy

1. Search the BTCC Figma file first.
2. Prefer in-file icon nodes, component instances, or copied vectors.
3. If implementing in code, prefer the local SVG assets in `assets/icons/`.
4. If the project already has a strict icon component system, wrap the local SVG path data or map source icons to the nearest project icon component.
5. Use line-icon fallbacks only when no source asset is available.

## Local SVG Assets

These assets were exported from the original Figma `设计规范` page:

| Asset | Original Figma Cue | Use |
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

## Sizing

| Use | Size |
| --- | --- |
| Toolbar and product nav icons | 24px |
| Bottom navigation icons | 20-24px |
| Inline pair/unit icons | 16px |
| Dropdown chevrons and dense selectors | 10-14px |
| Warning/add mini icons | 12-14px |
| Mobile touch container | 40-44px |
| Desktop icon button container | 32-40px |

## Role Mapping

| Role | Original Figma Cue | Source Page | Size | Fallback |
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
| System status | mobile signal, Wi-Fi, battery | `设计规范` | iOS-like native sizes | Do not use in web content except app frame mockups. |

## Style Rules

- Prefer stroke icons with restrained weight, visually around 1.5-2px at 24px.
- Keep icon color bound to text/icon tokens.
- Active nav icons use brand/primary emphasis.
- Disabled icons use `text | icon/disable`.
- Do not mix colorful illustrative icons into trading controls.
- Do not use emoji or filled playful icons.
- Keep icon-only buttons accessible with labels.

## Figma Notes

- The `图标` page was empty in the extraction pass; rely on `设计规范` and `合约pro` observed icon nodes.
- Some icons are nested vectors with generic names like `Vector`, `Subtract`, or `Rectangle`. Use the parent frame name as the semantic source cue.
- When reading via Figma tools, collect parent names and sizes, not only leaf vector names.
