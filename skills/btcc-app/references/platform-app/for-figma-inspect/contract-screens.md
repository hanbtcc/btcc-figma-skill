> See `references/rules.md` for global rules.

# BTCC 合约pro Sub-Screen Index

Lookup table for the `合约pro` page (`1262:304`) in Figma file `GW9kMfpf0Nib5DG4TjoWBp`.

The page exposes ~200 frames across two swimlanes (the dark spec on the left, a paired set on the right) plus light-mode and historical revisions. This file groups them by purpose and keeps a single canonical node ID per name. Pull from the Figma plugin with `get_design_context` / `get_metadata` on the listed node IDs.

> Treat this as a routing index, not a spec. Component anatomy lives in `for-code-generation/components-*.md`; page layout specs live in `for-code-generation/pages-*.md`; golden rules live in `rules.md`. When generating UI, locate the right frame here, then inspect it in Figma before producing code.

## How To Use

1. Identify the user's request (e.g. "leverage picker", "history orders detail").
2. Find the matching row below; copy the canonical node ID.
3. Call `get_design_context` on that node ID for layout, and `get_metadata` if you need to drill into nested frames.
4. Cross-check direction-button color (see `rules.md` R-COLOR-1), token values (see `for-code-generation/tokens-colors.md`), and component anatomy (see `for-code-generation/components-trading.md`).

All frames listed are mobile (`375` wide) unless noted otherwise.

## Main Workspace

| Surface | Canonical node ID | Size | Notes |
| --- | --- | --- | --- |
| `合约pro-dark` (verified anchor) | `3112:1423` | 375×812 | Main mobile contract workspace; primary anchor for tokens, order form, order book, direction buttons (rule basis: `rules.md` R-COLOR-1). |
| `合约pro-light` | `3598:1740` | 375×812 | Light-mode counterpart of the main workspace. |

## Empty States

| Screen | Canonical node ID | Size |
| --- | --- | --- |
| 无委托单 (no pending orders) | `15251:59149` | 375×1061 |
| 限价-无订单 (limit, no order) | `15251:59432` | 375×1061 |
| 市价-无资产 (market, no assets) | `15251:59714` | 375×1061 |
| 止盈止损设置-无数据 (TP/SL empty) | `20151:53593` | 375×812 |

## Anomaly / Risk Surfaces

| Screen | Canonical node ID | Size |
| --- | --- | --- |
| 有持仓-异常 (with position, anomaly) | `5516:56911` | 375×994 |
| 无持仓-异常 (no position, anomaly) | `5516:57180` | 375×916 |
| 风险提示弹窗 (risk popup) | `16599:11456` | 375×812 |
| 全部平仓二次弹窗 (close-all confirmation) | `5516:57446` | 375×812 |
| 杠杆风险提示-3d文件-dark | `16585:27092` | 512×512 |
| 杠杆风险提示-3d文件-light | `16601:16713` | 512×512 |

## Order Entry & Modals

| Screen | Canonical node ID | Size | Notes |
| --- | --- | --- | --- |
| 下单弹窗 (order confirm modal) | `3742:9574` | 375×812 | |
| 计划委托 (planned order) | `3754:5599` | 375×812 | |

## Bottom-Sheet Pickers

| Picker | Canonical node ID | Size |
| --- | --- | --- |
| 仓位模式选择 (position mode picker) | `3748:1837` | 375×812 |
| 杠杆调整 (leverage picker) | `3748:1448` | 375×812 |
| 下单单位 (order size unit) | `3750:1465` | 375×812 |
| 订单类型 (order type) | `5370:65323` | 375×812 |
| 订单薄深度 (order book depth) | `3812:5658` | 375×812 |
| 选中币对 (pair selector) | `5516:35309` | 375×812 |
| 资金费率 (funding rate detail) | `3763:8721` | 375×812 |
| 止盈止损介绍 (TP/SL intro) | `3767:3500` | 375×812 |
| 订单类型介绍 (order type intro) | `3754:3333` | 375×812 |
| 分享 (share) | `3767:4007` | 375×812 |
| 持仓量 (open interest detail) | `16215:60980` | 375×812 |
| 交易单位 (trading unit) | `3852:5364` | 375×812 |
| 仓位模式 (position mode info) | `3852:5388` | 375×812 |

## TP/SL Flows

| Screen | Canonical node ID | Size |
| --- | --- | --- |
| 止盈止损 (TP/SL) | `3754:5124` | 375×812 |
| 止盈止损设置-固定仓位 (per-position) | `3768:5234` | 375×812 |
| 止盈止损设置-全部仓位 (whole position) | `3770:5277` | 375×812 |
| 有委托单-止盈止损 (pending + TP/SL) | `3785:4574` | 375×1256 |

## Close / Flip / Cancel

| Action | Canonical node ID | Size |
| --- | --- | --- |
| 平仓-限价 (close, limit) | `5516:40093` | 375×812 |
| 平仓-市价 (close, market) | `5516:41020` | 375×812 |
| 全部平仓 (close all) | `3775:2954` | 375×812 |
| 反手 (flip side) | `3774:4215` | 375×812 |
| 撤销 (cancel) | `3775:3374` | 375×812 |
| 修改保证金 (adjust margin) | `15193:29814` | 375×812 |

## Order / Position Panel States

| State | Canonical node ID | Size |
| --- | --- | --- |
| 有订单 (with active orders) | `3735:6200` | 375×1256 |
| 有委托单 (with pending orders) | `3737:7425` | 375×1256 |
| 条件委托单 (conditional pending) | `3785:3317` | 375×1256 |
| 有资产 (with assets) | `3742:8736` | 375×1256 |

## Order Detail

| Screen | Canonical node ID | Size |
| --- | --- | --- |
| 委托订单详情 (order detail) | `3775:5205` | 375×812 |

## Orders Archive (全部订单-*)

| Tab / Detail | Canonical node ID | Size |
| --- | --- | --- |
| 委托单 (open orders list) | `3785:5030` | 375×812 |
| 历史委托单 (history orders) | `3785:5339` | 375×812 |
| 历史委托单-限价/市价 | `5516:42111` | 375×812 |
| 历史委托单-条件委托 | `12103:64091` | 375×812 |
| 历史仓位 (history positions) | `3802:3410` | 375×812 |
| 交易账单 (trading bill) | `3809:4453` | 375×812 |
| 交易明细 (trading detail) | `11840:54704` | 375×812 |
| 体验金记录 (bonus record) | `12021:61150` | 375×812 |
| 委托单-委托详情-市价/限价 | `5516:42405` | 375×812 |
| 委托单-委托详情-止盈止损 | `11872:71252` | 375×812 |
| 历史委托单-委托详情-限价/市价 | `5516:42461` | 375×812 |
| 历史委托单-委托详情-市价/限价 | `11872:71562` | 375×964 |
| 历史委托单-委托详情-条件委托 | `11872:71688` | 375×812 |
| 历史仓位-仓位详情 | `11872:71830` | 375×1201 |

## Calculator (计算器-*)

| Screen | Canonical node ID | Size |
| --- | --- | --- |
| 盈亏计算 (PnL calc) | `3884:28471` | 375×812 |
| 模拟计算 (simulation) | `3884:29065` | 375×899 |
| 模拟计算(无当前仓位) | `3884:28683` | 375×812 |
| 模拟计算-结果 | `3884:29266` | 375×843 |
| 模拟计算-下单确认 | `7926:47417` | 375×843 |
| 强平价格 (liq price) | `3930:30818` | 375×812 |
| 目标价格 (target price) | `3930:30985` | 375×812 |
| 币对选择 (pair pick) | `5140:17624` | 375×812 |

## Risk / Fees Tables

| Screen | Canonical node ID | Size |
| --- | --- | --- |
| 仓位档位 (position tier) | `3930:31092` | 375×812 |
| 费率 (fee tier) | `3956:5208` | 375×812 |
| 风险准备金 (risk fund) | `3930:32466` | 375×812 |

## Settings & Utilities

| Screen | Canonical node ID | Size |
| --- | --- | --- |
| 交易设置 (trading settings) | `3844:4709` | 375×903 |
| 交易通知 (trading notifications) | `3844:9368` | 375×812 |
| 时间筛选 (time filter) | `3789:3459` | 375×812 |
| 二次确认 (confirmation) | `3844:11259` | 375×812 |
| 更多 (more menu) | `3834:5638` | 375×812 |

## Toasts & Component Anchors

| Surface | Canonical node ID | Size | Notes |
| --- | --- | --- | --- |
| toast | `3812:3753` | 375×812 | Toast surface variants. |
| TabBar 底部标签栏 | `3194:1296` | 415×510 | Bottom tab bar component set. |
| bar-chart-square-down (icon) | `1359:316` | 24×24 | Market stats icon source. |
| bar-chart-square-up (icon) | `1359:318` | 24×24 | Market stats icon source. |

## Notes

- Frames named `Frame 17xxxxxxxx` / `Frame 21xxxxxxxx` are nested layout helpers; they are skipped from this index. Drill in via `get_metadata` on the parent if needed.
- Many screens have 2-4 historical duplicates with different node IDs (different swimlanes or older revisions). The canonical node ID picked here favors the dark, current-swimlane copy.
- Re-verify any row before relying on it for production work — the index reflects the `get_metadata` pass on 2026-05-27.
