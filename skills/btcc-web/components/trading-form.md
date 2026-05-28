# Trading Form（合约下单区）

> Figma 锚点：
> - `651:14846 合约pro下单框`（1214×698）—— 桌面老版下单区 master
> - `554:5235 下单组`（329×102）—— 下单 action group
> - `554:5259 开多下单button`（389×80）—— Open Long
> - `554:5266 开空下单button`（395×80）—— Open Short
> - `554:5252 次级button`（274×68）—— 工具行 button
> - `554:5273 输入框`（368×380）—— 数量 input + 步进
> - `554:5318 止盈止损`（625×285）—— TP/SL 面板

## 用途

合约 pro / 现货 / 闪兑页面的**右栏下单表单**。整个表单宽度 360-400px，铺满 viewport 高度（vmin-content）。

## 结构

```
[ 限价 / 市价 / 跟踪 / 计划委托 ]    ← 二级 Tab（同 components/tab.md 二级样式）
─────────────────────────────────
[ Buy / Sell ] 风险率：12.34%      ← 方向 toggle + 当前账户健康
─────────────────────────────────
价格   [_____________ USDT]        ← input 48h radius 4
数量   [-] [_____________] [+]     ← stepper 48h（components/input.md 步进版）
       BTC 余额: 0.1234
─────────────────────────────────
保证金       0.5x  1x  ··· 100x    ← 杠杆滑块或步进
止盈止损     ☐ 启用                ← switch + 子表单（554:5318）
─────────────────────────────────
[ 计算器 ]                         ← 触发 554:5273 计算器弹窗
─────────────────────────────────
[ 开多 / Open Long  $0.123 ]       ← 一级 button 但宽满，48h pill 100，蓝
[ 开空 / Open Short $0.123 ]       ← 一级 button 宽满，48h pill 100，红
                                     间距 8
─────────────────────────────────
可用    0.1234 USDT
最大可买 0.0567 BTC
```

## 关键尺寸

| 区域 | 高 | 备注 |
| --- | --- | --- |
| 一级 Tab 行 | 40 | components/tab.md |
| Buy/Sell + 风险行 | 32 | 文字行 |
| Input 行（label 8 + input 48） | 56 | 每行 |
| 杠杆 / TP/SL 行 | 48 | 含开关 |
| 工具按钮（计算器） | 28 | 次级 button |
| 主 CTA（Open Long / Open Short） | **48 + 48 + 8 间距 = 104** | 一级 button × 2 |
| 信息行（可用 / 最大可买） | 24 × 2 = 48 | 12px 字号 |

## 颜色（R-COLOR-WEB-1）

- **Open Long button**：`bg = var(--fill-brand-button-normal)` `#0c73ed`，文字 `#fff`。**永远不绿**。
- **Open Short button**：`bg = var(--fill-error)` `#eb464f`，文字 `#fff`。
- 上方 Buy / Sell **文本切换**（如果存在 toggle）：选中颜色仍按"绿涨红跌"规则——这里是**数字方向**，不是 CTA 按钮，遵循 R-SHARED-2。
- 风险率：低 `var(--fill-success)`，中 `var(--fill-warning)`，高 `var(--fill-error)`。

## CSS 骨架

```css
.btcc-trading-form {
  width: 380px;
  display: flex;
  flex-direction: column;
  gap: var(--space-16);
  padding: var(--space-16);
  background: var(--bg-card);
  border-left: 1px solid var(--divider-primary);
  font-family: var(--font-family-base);
  color: var(--text-icon-primary);
}
.btcc-trading-form__cta {
  display: grid; gap: var(--space-8);
}
.btcc-trading-form__cta .btcc-btn-primary { width: 100%; }
.btcc-trading-form__cta--short {
  background: var(--fill-error);
}
.btcc-trading-form__cta--short:hover {
  background: #d63b43;     /* error hover：加 8% 黑叠层 */
}
.btcc-trading-form__info {
  display: flex; justify-content: space-between;
  font-size: var(--font-size-xs);
  color: var(--text-icon-secondary);
  font-variant-numeric: tabular-nums;
}
```

## 反模式

- ❌ Open Long 涂绿（**永远是品牌蓝**——R-COLOR-WEB-1）
- ❌ Open Long / Short 不铺满表单宽（实际是表单宽，48h pill 100）
- ❌ 输入框圆角 100（实际 4，与按钮风格相反）
- ❌ 杠杆 picker 用大尺寸 chip（用 28h 次级 button 或 slider）
- ❌ TP/SL 永远展开（默认折叠，由 switch 控制）
- ❌ 用 css `text-transform: uppercase` 强行做"OPEN LONG"（按钮文字按 Figma 原文，中英两种本地化）
