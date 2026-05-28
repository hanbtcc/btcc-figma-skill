# 现货（Spot）

> Figma 锚点（1558:14723 内）：
> - **Web**：`2103:16421 现货`、`5163:20111 现货`、`5172:21798 现货`
> - **H5**：`2149:17615 h5-现货`、`5172:21659 / 5849:28709 兑换成功`

## 用途

币币交易（spot trading）。逻辑近似合约 pro，但：
- **没有杠杆 / TP-SL / 风险率**。
- **方向按钮颜色按 R-SHARED-2**：买 = 绿 `#2CA85D`，卖 = 红 `#EB464F`。**不沿用合约的"蓝/红"反惯例**。

## 布局

同合约 pro 三栏（左选币 / 中 K 线 / 右盘口 + 下单表单）。差别：

| 区域 | 合约 pro | 现货 |
| --- | --- | --- |
| 方向按钮 | Open Long 蓝 / Open Short 红 | **Buy 绿 / Sell 红** |
| 杠杆区 | 0.5×–100× | **不显示** |
| TP / SL | 折叠开关 | **不显示** |
| 风险率 | 顶部行展示 | **不显示** |
| 数量步进 | BTC | BTC |
| 计算器 | 有（合约盈亏） | 无 |
| 委托表格 | 当前 / 历史 / 持仓 / 资金费率 | 当前 / 历史 / 成交（无持仓） |

## 关键模块 → 组件

| 模块 | 组件文件 | 备注 |
| --- | --- | --- |
| 顶部 nav | [`components/topnav.md`](../components/topnav.md) | h64 |
| 选币左栏 | [`components/selector.md`](../components/selector.md) | 240-280 常驻 |
| 盘口 | [`components/orderbook.md`](../components/orderbook.md) | sell 红 / buy 绿 |
| 下单表单 | [`components/trading-form.md`](../components/trading-form.md) | **覆写**：CTA 改 Buy 绿 / Sell 红 |
| 委托 Tab | [`components/tab.md`](../components/tab.md) 一级 | h40 |

## 反模式

- ❌ 现货 Buy 按钮用蓝（**只有合约 pro 是反惯例**，现货遵循 R-SHARED-2 绿/红）。
- ❌ 把合约 pro 的杠杆/TP-SL/风险率行复制到现货。
- ❌ 现货盘口和合约盘口用不同样式（盘口配色一致：sell 红 / buy 绿）。
