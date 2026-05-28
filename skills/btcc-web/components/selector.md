# Selector（选币 / 选项下拉 / 选择器）

> Figma 锚点：
> - `663:2867 右侧选项`（540×1134）—— 合约 pro 右侧的选币 / 切换面板
> - `647:13107 选择币种`（580×180）—— dropdown 缩略型
> - `554:5210 自选`（437×66）—— "自选"列表 cell
> - `1109:4825 单选框`（173×56）—— Radio
> - `112251:211871 单选框`（145×48）—— Radio 紧凑版

## 用途

- 选币 / 选合约 / 选支付方式 / 选语言 / 选时区。
- 触发后用**右滑面板**（合约 pro 右栏）或**dropdown 浮层**。
- 不要用 native `<select>`——视觉差距太大。

## 模式 A：dropdown（行内 580×N）

| 属性 | 值 |
| --- | --- |
| 触发器（trigger） | input 形态：48h radius 4，右侧带 dropdown 箭头 16px |
| 浮层 | 580 宽 / 自适应高（最高 ~480，超出滚动） |
| 浮层圆角 | 4px |
| 浮层阴影 | `var(--shadow-tips)` |
| 浮层背景 | `var(--bg-card)` `#13171b` |
| 列表行高 | 40 |
| 列表行 padding | 0 16 |
| 行 hover | `var(--fill-secondary-button-hover)` |
| 选中行 | 文字 `var(--fill-brand-button-normal)`，右侧 ✓ 16px |

## 模式 B：右滑面板（合约 pro 右栏）

| 属性 | 值 |
| --- | --- |
| 宽 | **540px** |
| 高 | 屏高（vh） |
| 顶部 | 标题 + 搜索框 + 关闭 X |
| 内容 | 自选 Tab（554:5210）+ 合约列表 + 板块过滤 |
| 列表行高 | 56（包含币图标 24 + 双行文本） |

## CSS（dropdown 模式）

```css
.btcc-selector { position: relative; }
.btcc-selector__trigger {
  width: 100%;
  height: var(--h-input);
  padding: 0 var(--space-12);
  display: inline-flex;
  align-items: center; justify-content: space-between;
  background: var(--fill-page-input);
  border-radius: var(--radius-input);
  color: var(--text-icon-primary);
  font-family: var(--font-family-base);
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  cursor: pointer;
}
.btcc-selector__menu {
  position: absolute;
  top: calc(100% + 4px); left: 0; min-width: 100%;
  max-height: 480px; overflow: auto;
  background: var(--bg-card);
  border-radius: var(--radius-input);
  box-shadow: var(--shadow-tips);
  z-index: 1000;
}
.btcc-selector__option {
  display: flex; align-items: center; justify-content: space-between;
  height: 40px;
  padding: 0 var(--space-16);
  color: var(--text-icon-primary);
  font-family: var(--font-family-base);
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  cursor: pointer;
}
.btcc-selector__option:hover { background: var(--fill-secondary-button-hover); }
.btcc-selector__option[aria-selected="true"] { color: var(--fill-brand-button-normal); }
```

## Radio（单选）

```css
.btcc-radio {
  display: inline-flex;
  align-items: center;
  gap: var(--space-8);
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  color: var(--text-icon-primary);
  cursor: pointer;
}
.btcc-radio__mark {
  width: 16px; height: 16px;
  border-radius: 50%;
  border: 1px solid var(--text-icon-secondary);
  position: relative;
  flex-shrink: 0;
}
.btcc-radio[aria-checked="true"] .btcc-radio__mark {
  border-color: var(--fill-brand-button-normal);
}
.btcc-radio[aria-checked="true"] .btcc-radio__mark::after {
  content: "";
  position: absolute; inset: 3px;
  border-radius: 50%;
  background: var(--fill-brand-button-normal);
}
```

## 反模式

- ❌ 用 native `<select>`（视觉断层）
- ❌ Dropdown 圆角 100 / 24（实际 4）
- ❌ Radio 选中点用绿/红（用品牌蓝；绿/红是数字方向，不是控件状态）
- ❌ 选币面板宽 320 / 480（实际 540）
