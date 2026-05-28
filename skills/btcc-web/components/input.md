# Input（输入框）

> Figma 锚点：
> - `126691:93620 订单类型`（1134×738，包含订单输入栏 anatomy）—— 主样本，48h / radius 4
> - `554:5273 输入框`（368×380，含数量 + 步进）—— 数量输入，带左右按钮

## 用途

订单数量、价格、金额、API 名称、备注、地址等数据录入。Web 输入是**方角小圆**（4px 圆角），**不是 pill**——这与按钮风格相反。

## 几何（R-SHAPE-WEB）

| 属性 | 值 |
| --- | --- |
| 高度 | **48px** |
| 圆角 | **4px** |
| Padding | 0 12px |
| 背景 | `var(--fill-page-input)` `#1d232a`（dark）/ `#f5f7fa`（light） |
| 边框 | 默认无；focus 时 1px solid `var(--fill-brand-button-normal)` |
| 文字 | Lato Medium 14px |
| 文字色 | `var(--text-icon-primary)` |
| Placeholder 色 | `var(--text-icon-secondary)` |
| label（顶部） | Lato Regular 12px，`var(--text-icon-secondary)`，与 input 间距 8px |
| 后缀 / 单位 | Lato Medium 14px `var(--text-icon-secondary)`，右内边距 12 |

## CSS

```css
.btcc-field {
  display: flex;
  flex-direction: column;
  gap: var(--space-8);
}
.btcc-field__label {
  font-size: var(--font-size-xs);
  color: var(--text-icon-secondary);
}
.btcc-input {
  height: var(--h-input);
  padding: 0 var(--space-12);
  background: var(--fill-page-input);
  border: 1px solid transparent;
  border-radius: var(--radius-input);
  color: var(--text-icon-primary);
  font-family: var(--font-family-base);
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  font-variant-numeric: tabular-nums;
}
.btcc-input::placeholder { color: var(--text-icon-secondary); }
.btcc-input:focus { border-color: var(--fill-brand-button-normal); outline: none; }
.btcc-input:disabled { color: var(--text-icon-disable); cursor: not-allowed; }
.btcc-input--error { border-color: var(--fill-error); }

/* 数量输入：左右步进 + 中间 input */
.btcc-input-stepper {
  display: flex;
  height: var(--h-input);
  background: var(--fill-page-input);
  border-radius: var(--radius-input);
  align-items: center;
}
.btcc-input-stepper__btn {
  width: 32px;
  height: 100%;
  border: none;
  background: transparent;
  color: var(--text-icon-secondary);
  cursor: pointer;
}
.btcc-input-stepper__btn:hover { color: var(--text-icon-primary); }
.btcc-input-stepper input {
  flex: 1; min-width: 0; height: 100%;
  background: transparent; border: none;
  text-align: center;
  font-family: var(--font-family-base);
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  color: var(--text-icon-primary);
  font-variant-numeric: tabular-nums;
}
.btcc-input-stepper input:focus { outline: none; }
```

## 反模式

- ❌ Input 圆角 100 / 24 / 12（实际 4）
- ❌ Input 高 32 / 36 / 40（实际 48）
- ❌ Input 背景透明（实际是 `var(--fill-page-input)`）
- ❌ 数字 input 不加 `font-variant-numeric: tabular-nums`（违反 R-SHARED-5）
