# Order Book（盘口）

> Figma 锚点：`647:13104 盘口`（695×684）。

## 用途

合约 pro / 现货 / 闪兑页面**右栏**或下单区**左侧**的实时买卖盘。

## 结构

```
盘口
─────────────────────────────────────────
价格(USDT) ｜ 数量(BTC) ｜ 累计(BTC)        ← 列头 行高 24
─────────────────────────────────────────
27,450.50  ｜  0.0123    ｜  0.0123       ← 卖单（asks），从下到上
27,450.00  ｜  0.0250    ｜  0.0373         价格降序到 mid
27,449.50  ｜  0.0500    ｜  0.0873
─────────────────────────────────────────
27,449.00  ↓  -0.50  ↓  USD 27,449.00     ← Mid 价格栏：高对比，行高 40
─────────────────────────────────────────
27,448.50  ｜  0.0100    ｜  0.0100       ← 买单（bids），从上到下
27,448.00  ｜  0.0300    ｜  0.0400         价格降序
─────────────────────────────────────────
[ 买单累计 ▰▰▰▰▱▱ 60% ｜ ▱▱▰▰▰▰ 40% 卖单累计 ]    ← 底部比例条，可选
```

## 几何

| 属性 | 值 |
| --- | --- |
| 总宽 | 380-420px（合约 pro 默认右栏） |
| 行高 | **24px**（紧凑） |
| 字体 | Lato **Medium 12px**，**`font-variant-numeric: tabular-nums`** 必加 |
| 列对齐 | 价格 → 左对齐，数量 → 右对齐，累计 → 右对齐 |
| 列头字色 | `var(--text-icon-secondary)` |
| 价格列字色 | sell `var(--pnl-down)` `#eb464f`，buy `var(--pnl-up)` `#2ca85d` |
| 数量 / 累计字色 | `var(--text-icon-primary)` |
| 累计深度条（行内背景） | sell `rgba(235,70,79,0.12)` 自右向左铺，buy `rgba(44,168,93,0.12)` 自右向左铺 |
| Mid 价格行 | 高 40，加 1px 上下分隔线，价格字号 16，加箭头 ↑/↓ |

## CSS（节选）

```css
.btcc-orderbook {
  width: 400px;
  font-family: var(--font-family-base);
  font-size: var(--font-size-xs);
  font-weight: var(--font-weight-medium);
  font-variant-numeric: tabular-nums;
  color: var(--text-icon-primary);
}
.btcc-orderbook__head,
.btcc-orderbook__row {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  align-items: center;
  height: 24px;
  padding: 0 var(--space-12);
  font-size: 12px;
}
.btcc-orderbook__head { color: var(--text-icon-secondary); }
.btcc-orderbook__row { position: relative; }
.btcc-orderbook__row > * { position: relative; z-index: 1; }
.btcc-orderbook__row .price-sell { color: var(--pnl-down); }
.btcc-orderbook__row .price-buy  { color: var(--pnl-up); }
.btcc-orderbook__row .qty,
.btcc-orderbook__row .cum { text-align: right; }

.btcc-orderbook__row::before {
  content: "";
  position: absolute;
  top: 0; right: 0; bottom: 0;
  background: rgba(235, 70, 79, 0.12);
  width: var(--depth, 0%);
  z-index: 0;
}
.btcc-orderbook__row.is-buy::before { background: rgba(44, 168, 93, 0.12); }

.btcc-orderbook__mid {
  display: flex; align-items: center; justify-content: space-between;
  height: 40px; padding: 0 var(--space-12);
  border-top: 1px solid var(--divider-primary);
  border-bottom: 1px solid var(--divider-primary);
  font-size: var(--font-size-md);
  font-weight: var(--font-weight-bold);
}
```

## 反模式

- ❌ 行高 32 / 40（实际 24，密集！）
- ❌ 不加 tabular-nums（数字会跳动，违反 R-SHARED-5）
- ❌ 把买单涂蓝、卖单涂红（卖盘是 R-COLOR-WEB-1 例外区域**之外**——盘口数字方向仍按绿/红，不是按钮反向规则）
- ❌ 累计深度条加在整行外面盖住（应是行内伪元素，不影响文字 z-index）
