# BTCC Figma Source Reference

Use this file when the user provides the BTCC Figma file or asks to preserve the original Figma rules.

## File

- Figma file: `新BTCC APP`
- File key: `GW9kMfpf0Nib5DG4TjoWBp`
- Last verified via Figma MCP: 2026-05-27

## Verified Pages

`get_metadata` against the file root returned only the pages below at the time of verification. Treat these as the only source of truth for token/component extraction:

| Alias | Original Figma Page | Node ID | Role |
| --- | --- | --- | --- |
| `design-spec` | `设计规范` | `0:1` | Token table, icon examples, repeated component usage. |
| `contract-pro` | `合约pro` | `1262:304` | Main contract trading reference. Hosts `合约pro-dark` (`3112:1423`) plus 200+ subscreens (limit/market entry, close-position, TP/SL sheets, full-screen orders, etc.). For a node-ID lookup table grouped by purpose see `contract-screens.md`. |

## Unverified / Missing Page Aliases

Earlier docs referenced page aliases that the current Figma metadata pass did NOT return as top-level pages. Do not generate UI on the assumption that these pages exist in the source file; if you need a pattern from one of them, ask han to point at a Figma URL/node, then re-verify.

| Alias | Cited Original Page | Status |
| --- | --- | --- |
| `global-components` | `全局组件` | Not present in current `get_metadata`. Patterns previously attributed to it (e.g. `次级button`) are now treated as instance-pattern references, not as a known component-set page. |
| `icons` | `图标` | Not present in current `get_metadata`. Icon assets currently come from `设计规范` and `合约pro` exports. |
| `theme-swap` | `换色` | Not present. |
| `home` | `首页` | Not present. |
| `assets` | `资产` | Not present. |
| `markets` | `行情` | Not present. |
| `legacy-contract` | `老合约` | Not present. |
| `tradfi` | `TradFi` | Not present. |
| `spot` | `现货` | Not present. |
| `copy-trading` | `跟单` | Not present. |
| `auth` | `登录注册` | Not present. |
| `profile-settings` | `我的、设置` | Not present. |
| `coupon-trial-fund` | `卡券/体验金` | Not present. |
| `payments-nft-withdrawal` | `支付通道、NFT、提现` | Not present. |
| `c2c` | `C2C` | Not present. |
| `insights` | `观点` | Not present. |
| `h5` | `h5` | Not present. |

When generating output for one of the unverified aliases, prefer general BTCC token/icon rules and label the result clearly (e.g. "no Figma source reference for this page; followed BTCC primitives only").

## Component-Set References

The following names appeared in earlier extraction notes. They are kept here as instance-pattern anchors — names you may see inside `合约pro` and `设计规范` — not as guaranteed published library components in the current file:

| Alias | Cited Name | Source |
| --- | --- | --- |
| `secondary-button` | `次级button` | Variants observed: `normal`/`pressed` × `extra small`/`small`/`Medium`/`large`. Treat as anatomy reference until re-verified as a component set. |
| `bottom-tabbar` | `TabBar 底部标签栏` | Variants observed: `home`, `discover`, `copy`, `assets`, `trade`. 375 × 78. Treat as instance pattern from `合约pro`. |

## Primary Source Nodes

| Node / Frame | Original Cue | Use |
| --- | --- | --- |
| `合约pro-dark` (`3112:1423`) | 375 × 812 | Mobile contract trading reference. Verified via `get_design_context`: `Open Long` button uses `fill/brand`, `Open Short` uses `fill/error`. |
| product nav | `USDT-M`, `Coin-M`, `Spot`, `USDT-M Pro`, `beta` | Top product navigation. |
| pair header | `BTCUSDT`, `Perp`, `-2.14%` | Market context. |
| order form | `cross`, `100x`, `Open`, `Close`, `limit`, `BBO`, `Amount`, `TP/SL` | Trading form anatomy. |
| order book | `Funding / Countdown`, `Price (USDT)`, `Size (BTC)`, `B 39%`, `61% S` | Order book anatomy. |
| account panel | `orders(0)`, `positions(0)`, `assets`, `Available: 0.0000 USDT`, `Deposit`, `transfer` | Lower operational panel. |

## Figma Plugin Rules

- Use `get_metadata` (no nodeId) to list verified top-level pages before assuming any page exists.
- Use `get_design_context` against a specific node to inspect tokens / Tailwind classes / Code Connect bindings.
- Use `search_design_system` for token names instead of dumping the entire `设计规范` page (it is too large to inline).
- Before creating new Figma UI, inspect `design-spec` (设计规范) and the target node in `合约pro`.
- Do not infer that a page has no useful patterns just because it has no top-level children in a metadata listing; use Figma inspection when the page matters.
- Do not invent new aliases for pages that have not been verified in `get_metadata`.

