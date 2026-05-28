# 次级 button（Small Inline Button）

> Figma 锚点：`554:5252 次级button`（master 274×68 但实际渲染高度 28）。

## 用途

工具栏、面板内行内操作、tab 旁边的 "More"、表格行内 "Cancel"。**永远不是 CTA**——CTA 用一级 button。

## 几何

| 属性 | 值 |
| --- | --- |
| 高度 | **28px**（不是 32 / 36 / 40） |
| 圆角 | **29px**（接近 pill） |
| Padding | 0 12px |
| 文字 | Lato **Regular 12px** |
| 内置图标尺寸 | 16px |
| icon + text 间距 | 4px |

## 颜色

### Dark
| 状态 | 背景 | 文字 |
| --- | --- | --- |
| Normal | `var(--fill-secondary-button-normal)` `#212830` | `var(--text-icon-primary)` |
| Hover | `var(--fill-secondary-button-hover)` `#2b333d` | `var(--text-icon-primary)` |
| Pressed | `var(--fill-secondary-button-pressed)` `#353d48` | `var(--text-icon-primary)` |
| Disabled | `var(--fill-secondary-button-normal)` | `var(--text-icon-disable)` |

### Light
| 状态 | 背景 | 文字 |
| --- | --- | --- |
| Normal | `#f5f7fa` | `var(--text-icon-primary)` |
| Hover | `#ebeef3` | `var(--text-icon-primary)` |

## CSS

```css
.btcc-btn-secondary {
  display: inline-flex;
  align-items: center;
  gap: var(--space-4);
  height: var(--h-button-sm);    /* 28 */
  padding: 0 var(--space-12);
  border: none;
  border-radius: var(--radius-pill-sm);  /* 29 */
  background: var(--fill-secondary-button-normal);
  color: var(--text-icon-primary);
  font-family: var(--font-family-base);
  font-size: var(--font-size-xs);  /* 12 */
  font-weight: var(--font-weight-regular);
  cursor: pointer;
}
.btcc-btn-secondary:hover  { background: var(--fill-secondary-button-hover); }
.btcc-btn-secondary:active { background: var(--fill-secondary-button-pressed); }
.btcc-btn-secondary:disabled {
  color: var(--text-icon-disable);
  cursor: not-allowed;
}
```

## 反模式

- ❌ 高 32 / 36（实际 28）
- ❌ 字号 14（实际 12 Regular）
- ❌ 用此组件作 CTA（CTA 必须是一级 button 48h pill 100）
- ❌ 圆角 4 / 8 / 16（实际 29）
