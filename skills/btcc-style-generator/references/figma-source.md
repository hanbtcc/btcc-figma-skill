# BTCC Figma Source Reference

Use this file when the user provides the BTCC Figma file or asks to preserve the original Figma rules.

## File

- Figma file: `新BTCC APP`
- File key: `GW9kMfpf0Nib5DG4TjoWBp`
- Extracted on: 2026-05-27

## Page Aliases

Use ASCII aliases in generated docs/code. Keep original names only when calling Figma tools or explaining source provenance.

| Alias | Original Figma Page | Role |
| --- | --- | --- |
| `design-spec` | `设计规范` | Token table, icon examples, repeated component usage. |
| `global-components` | `全局组件` | Global reusable components. |
| `icons` | `图标` | Icon page; currently empty in the extraction pass. |
| `theme-swap` | `换色` | Color/theme exploration. |
| `home` | `首页` | Home patterns. |
| `assets` | `资产` | Wallet/assets patterns. |
| `markets` | `行情` | Market list patterns. |
| `legacy-contract` | `老合约` | Legacy contract patterns. |
| `tradfi` | `TradFi` | TradFi feature patterns. |
| `contract-pro` | `合约pro` | Main contract trading reference. |
| `spot` | `现货` | Spot trading patterns. |
| `copy-trading` | `跟单` | Copy trading patterns. |
| `auth` | `登录注册` | Login and registration patterns. |
| `profile-settings` | `我的、设置` | Profile and settings patterns. |
| `coupon-trial-fund` | `卡券/体验金` | Coupon and trial-fund patterns. |
| `payments-nft-withdrawal` | `支付通道、NFT、提现` | Payment, NFT, withdrawal patterns. |
| `c2c` | `C2C` | C2C patterns. |
| `insights` | `观点` | Content/opinion patterns. |
| `h5` | `h5` | Mobile web patterns. |

## Component Sets Found

| Alias | Original Name | Page | Variants |
| --- | --- | --- | --- |
| `secondary-button` | `次级button` | `全局组件` | `normal` and `pressed`; sizes `extra small`, `small`, `Medium`, `large`. |
| `bottom-tabbar` | `TabBar 底部标签栏` | `合约pro` | `home`, `discover`, `copy`, `assets`, `trade`. |

## Primary Source Nodes

| Node / Frame | Original Cue | Use |
| --- | --- | --- |
| `contract-pro-dark` | `合约pro-dark` | 375 x 812 contract trading mobile reference. |
| product nav | `USDT-M`, `Coin-M`, `Spot`, `USDT-M Pro`, `beta` | Top product navigation. |
| pair header | `BTCUSDT`, `Perp`, `-2.14%` | Market context. |
| order form | `cross`, `100x`, `Open`, `Close`, `limit`, `BBO`, `Amount`, `TP/SL` | Trading form anatomy. |
| order book | `Funding / Countdown`, `Price (USDT)`, `Size (BTC)`, `B 39%`, `61% S` | Order book anatomy. |
| account panel | `orders(0)`, `positions(0)`, `assets`, `Available: 0.0000 USDT`, `Deposit`, `transfer` | Lower operational panel. |

## Figma Plugin Rules

- Use `get_metadata` for page structure when a node id is unknown.
- Use `use_figma` for variable, component, and icon inspection.
- Before creating new Figma UI, inspect `design-spec`, `global-components`, and the target page.
- Do not infer that a page has no useful patterns just because it has no top-level children in a metadata listing; use Figma inspection when the page matters.

