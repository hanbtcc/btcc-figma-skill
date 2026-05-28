# Tab（一级 / 二级 Tab 栏）

> Figma 锚点：
> - `554:5228 一级tab栏`（264×80）—— 主导航 Tab，带选中底线
> - `554:5221 二级tab栏`（172×64）—— 面板内分类 Tab
> - `554:5210 自选`（437×66）—— Tab 之一的"自选"特殊 cell

## 用途

页面顶部 / 面板顶部分类导航。**不是单选按钮，不是 chip**。

- 一级：合约 pro / 现货 / 资产 / 钱包 / 充币 / 提现 等顶层切换。
- 二级：合约下"持仓 / 委托 / 历史委托 / 资产"，资产下"现货 / 合约 / 法币" 等。

## 一级 Tab 几何

| 属性 | 值 |
| --- | --- |
| 高度 | 40px（一行 cell），完整栏 80px（含 padding） |
| Cell padding | 0 16px |
| 选中态 | **底部 2px solid `var(--text-icon-anti)`**（白），不是圆角填充 |
| 字号 | Lato **Bold 14px**（选中），Lato Medium 14px（未选） |
| 字色（选中） | `var(--text-icon-primary)` |
| 字色（未选） | `var(--text-icon-secondary)` |
| Cell 间距 | 24px |

## 二级 Tab 几何

| 属性 | 值 |
| --- | --- |
| 高度 | 32px |
| 选中态 | 底部 2px solid `var(--fill-brand-button-normal)`（品牌蓝） |
| 字号 | Lato Medium 14px |
| 字色 | 选中 `var(--text-icon-primary)`，未选 `var(--text-icon-secondary)` |
| Cell 间距 | 16px |

## CSS

```css
.btcc-tabs {
  display: flex;
  gap: var(--space-24);
  border-bottom: 1px solid var(--divider-primary);
}
.btcc-tab {
  position: relative;
  height: 40px;
  padding: 0 var(--space-16);
  display: inline-flex;
  align-items: center;
  font-family: var(--font-family-base);
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  color: var(--text-icon-secondary);
  cursor: pointer;
  user-select: none;
}
.btcc-tab[aria-selected="true"] {
  color: var(--text-icon-primary);
  font-weight: var(--font-weight-bold);
}
.btcc-tab[aria-selected="true"]::after {
  content: "";
  position: absolute;
  left: 16px; right: 16px; bottom: -1px;
  height: 2px;
  background: var(--text-icon-anti);
}

/* 二级 tab：缩小高度、选中色换品牌蓝 */
.btcc-tabs--sub .btcc-tab { height: 32px; gap: var(--space-16); }
.btcc-tabs--sub .btcc-tab[aria-selected="true"]::after {
  background: var(--fill-brand-button-normal);
}
```

## 反模式

- ❌ Tab 选中态用整段背景填充（实际只是底部 2px 线）
- ❌ Tab 用 pill 圆角 chip 替代（不是 chip 风格）
- ❌ Tab 字号 16 / 12（实际 14）
- ❌ 一级 Tab 选中色用品牌蓝（一级用白 anti，二级才用品牌蓝）
