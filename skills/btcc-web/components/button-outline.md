# 描边 button（Outline / Secondary CTA）

> Figma 锚点：`741:4616`（component master，757×88 设计稿尺寸；实际渲染按 48h）。

## 用途

辅助操作 / 取消 / 次要 CTA。和 [`button-primary.md`](button-primary.md) 同形态、同尺寸，仅边框 + 文字色，无填充。

一个页面 / 弹窗里允许多个描边按钮（不像一级 button 限 1 个）。

## 几何

| 属性 | 值 |
| --- | --- |
| 高度 | **48px** |
| 圆角 | **100px**（pill） |
| 边框 | 1px solid `var(--border-primary)` 或 `var(--fill-brand-button-normal)`（强调时） |
| Padding | 0 24px |
| 文字 | Lato Medium 14px / 20px |

## 颜色变体

### 中性描边（默认）
| 状态 | 边框 | 文字 |
| --- | --- | --- |
| Normal | `var(--border-primary)` | `var(--text-icon-primary)` |
| Hover | `var(--text-icon-primary)` | `var(--text-icon-primary)` |
| Disabled | `var(--text-icon-disable)` | `var(--text-icon-disable)` |

### 品牌描边（强调，与一级 CTA 并列）
| 状态 | 边框 | 文字 |
| --- | --- | --- |
| Normal | `var(--fill-brand-button-normal)` | `var(--fill-brand-button-normal)` |
| Hover | `var(--fill-brand-button-hover)` | `var(--fill-brand-button-hover)` |

## CSS

```css
.btcc-btn-outline {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-8);
  height: var(--h-button);
  padding: 0 var(--space-24);
  min-width: 168px;
  border: 1px solid var(--border-primary);
  border-radius: var(--radius-pill);
  background: transparent;
  color: var(--text-icon-primary);
  font-family: var(--font-family-base);
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  cursor: pointer;
}
.btcc-btn-outline:hover { border-color: var(--text-icon-primary); }
.btcc-btn-outline.btcc-btn-outline--brand {
  border-color: var(--fill-brand-button-normal);
  color: var(--fill-brand-button-normal);
}
.btcc-btn-outline.btcc-btn-outline--brand:hover {
  border-color: var(--fill-brand-button-hover);
  color: var(--fill-brand-button-hover);
}
.btcc-btn-outline:disabled {
  border-color: var(--text-icon-disable);
  color: var(--text-icon-disable);
  cursor: not-allowed;
}
```

## 反模式

- ❌ 边框 2px（应该 1px）
- ❌ 圆角小于 100（应该 pill）
- ❌ 用绿色 / 红色描边做装饰（绿/红只承载语义，违反 R-SHARED-2）
