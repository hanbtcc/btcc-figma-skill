# 合约 Pro（Contract Pro / Futures）

> Figma 锚点（1558:14723 内）：
> - **桌面 Web 1920**：
>   - `5896:9053 合约pro`（旗舰，最完整版式）
>   - `2609:24065 合约pro`（旧资产视角）
>   - `5603:29612 合约pro`
>   - `111388:116518 合约pro`
>   - `2609:24063 老合约`、`111388:116083 老合约`（保留兼容样式，新页面不复用）
> - **H5 镜像 375**：
>   - `2142:17221 h5-合约pro`
>   - `2142:16070 / 2142:16449 h5-合约`
>   - `3401:20087 h5-合约`

## 用途

加密货币合约交易（永续 / 交割）pro 模式。整页**铺满 viewport**，无 1200 容器约束，但内部按列分区。

## 三栏布局（Web）

```
┌─顶部 nav 64h─────────────────────────────────────────────────┐
│ Logo │ 合约 现货 资产 … │           通知 钱包 头像 下载 语言 │
├──────────────────────────────────────────────────────────────┤
│ 已选交易对：BTC/USDT  $27,449.00  +0.45%   24h H/L/Vol  │深度│  ← 子级 nav 32-56h
├──────────┬───────────────────────────┬───────────────────────┤
│  左栏    │       中栏（K线 + 图表）  │  右栏（盘口 + 表单）  │
│ 240-280  │     flex-1（最大）        │   400-460             │
│ 选币列表 │  ──── 1080 ────           │  ┌─盘口 380-420──────┐│
│ + 板块   │                           │  │ 价/量/累计 24h     ││
│ + 热门   │                           │  │  Lato Med 12 num   ││
│          │                           │  └────────────────────┘│
│          │                           │  ┌─下单表单 380──────┐│
│          │                           │  │ Buy/Sell 风险率    ││
│          │                           │  │ 价格 / 数量 / 杠杆 ││
│          │                           │  │ TP/SL │ 计算器     ││
│          │                           │  │ Open Long  品牌蓝  ││
│          │                           │  │ Open Short 错误红  ││
│          │                           │  └────────────────────┘│
├──────────┴───────────────────────────┴───────────────────────┤
│  下方：当前委托 / 历史委托 / 持仓 / 资金费率（h40 一级 Tab） │
└──────────────────────────────────────────────────────────────┘
```

## 关键模块 → 组件清单

| 模块 | 组件文件 | 备注 |
| --- | --- | --- |
| 顶部 nav | [`components/topnav.md`](../components/topnav.md) | h64 |
| 已选 pair 行 | topnav.md 子节 | h32-56，数字 tabular-nums |
| 选币左栏 | [`components/selector.md`](../components/selector.md) 模式 B | 540 → Web 内嵌窄 240-280 时把右滑改为常驻 |
| K 线 / 图表 | TradingView iframe（外部） | 不在 Figma 还原范围 |
| 盘口 | [`components/orderbook.md`](../components/orderbook.md) | 380-420w / 24h / tabular-nums |
| 下单表单 | [`components/trading-form.md`](../components/trading-form.md) | 380w / Open Long 蓝 Open Short 红（**R-COLOR-WEB-1**） |
| 当前/历史委托 / 持仓 Tab | [`components/tab.md`](../components/tab.md) 一级 | h40 |
| 委托表格 | [`components/table.md`](../components/table.md) | 行高 40，价格列 tabular-nums |
| 计算器弹窗 | [`components/dialog.md`](../components/dialog.md) 480 | 触发自工具栏 |
| 杠杆调整 | [`components/dialog.md`](../components/dialog.md) 480 | 含 slider |
| TP / SL | trading-form.md 内嵌 | switch + 输入 |
| 选币右栏（合约 pro 切币） | [`components/selector.md`](../components/selector.md) 模式 B | 540 |

## 颜色 / 数据规则

- **Open Long / Open Short**：R-COLOR-WEB-1。
- **盘口价格**：sell 红 `#EB464F`、buy 绿 `#2CA85D`（数字方向，仍是绿涨红跌）。
- **PnL / 24h 涨跌**：绿涨红跌（R-SHARED-2）。
- **风险率**：低绿、中黄 `#E0601F`、高红 `#EB464F`。
- 所有数字必须 `font-variant-numeric: tabular-nums`（R-SHARED-5）。

## 反模式

- ❌ 把合约 pro 主体限在 1200 容器（实际全宽，仅内部子模块固定宽）。
- ❌ Open Long 涂绿（R-COLOR-WEB-1）。
- ❌ 盘口行高 32 / 40（实际 24）。
- ❌ 下单表单和盘口塞进同一卡片（实际是右栏两个独立卡）。
- ❌ K 线区域用静态图占位（实际是 TradingView iframe 整合）。
- ❌ 委托 Tab 用 pill（应是 h40 底部 2px 线）。
