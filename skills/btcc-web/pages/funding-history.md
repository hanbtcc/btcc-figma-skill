# 资金记录（Funding History）

> Figma 锚点（1558:14723 内）：
> - **Web**：`9590:15462`、`9884:11688` 资金记录
> - **H5**：`9884:12021`、`10054:10701`、`10090:10905`、`100582:133289` h5-资金记录
> - **资金证明报告**：`10003:10639`

## 用途

所有资金类型的统一历史记录：充币 / 提币 / 划转 / 法币入金 / 闪兑 / 卡券到账 / 体验金到账 / 手续费返还 / 资金费率结算 等。

## 布局（Web 1556 内容宽）

```
资金记录                                    [资金证明报告 ↓]
─────────────────────────────────────────────────────────────
[ 充币 / 提币 / 划转 / 闪兑 / 法币 / 全部 ] h40 一级 Tab
─────────────────────────────────────────────────────────────
筛选行 56h：
  [▼ 币种] [▼ 状态] [日期 from] [日期 to]   [搜索] [重置]
─────────────────────────────────────────────────────────────
表格：
  时间        │ 类型 │ 币种 │ 数量      │ 状态   │ 备注/TXID
  2026-05-28  │ 充币 │ USDT │ +100.00   │ 成功 ✓ │ TXxx...
  2026-05-27  │ 提币 │ BTC  │ -0.0123   │ 处理中 │ 1A1z...
  ...
─────────────────────────────────────────────────────────────
分页 32 × 32 r19 / r25
```

## 关键模块 → 组件

| 模块 | 组件文件 | 备注 |
| --- | --- | --- |
| 类型 Tab | [`components/tab.md`](../components/tab.md) 一级 | h40 |
| 筛选 dropdown | [`components/selector.md`](../components/selector.md) A | 580 |
| 日期范围 picker | [`components/input.md`](../components/input.md) | h48 r4 |
| 搜索 / 重置 | [`components/button-primary.md`](../components/button-primary.md) / outline | h48 |
| 资金证明报告 | [`components/button-secondary-sm.md`](../components/button-secondary-sm.md) | h28 r29 链接到 `10003:10639` |
| 表格 | [`components/table.md`](../components/table.md) | 行高 56，时间列 tabular-nums |
| 状态标签 | inline pill 12px | 成功 success / 处理中 warning / 失败 error |
| 分页 | [`components/pagination.md`](../components/pagination.md) | 32×32，PingFang SC Reg 14 |

## 数据规则

- 时间列、数量列必须 `font-variant-numeric: tabular-nums`（R-SHARED-5）。
- 数量正负：+ 用 `var(--fill-success)`、- 用 `var(--text-icon-primary)`（不是红——R-SHARED-2 数字方向规则；金额减少不等于 PnL 跌）。
- TXID / 地址 hash：等宽显示，超长截断 `0x1A2B…3F4D`，hover 显示完整 + 复制按钮。

## 反模式

- ❌ 把"-100 USDT"涂红（金额变化不等于 PnL，不适用绿涨红跌）。
- ❌ 类型筛选做成 dropdown（实际是 h40 Tab 横向）。
- ❌ TXID 完整显示（应截断 + hover 完整 + 复制）。
- ❌ 不加 tabular-nums（数字会跳）。
