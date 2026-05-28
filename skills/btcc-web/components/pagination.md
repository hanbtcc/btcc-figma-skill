# 分页（Pagination）

> Figma 锚点：`5568:196480 分页`（352×32）。

## 几何

| Cell | 尺寸 | 圆角 | 字体 |
| --- | --- | --- | --- |
| Prev / Next 按钮 | 32 × 32 | **25px** | — |
| 当前页（current） | 32 × 32 | **19px** | **PingFang SC Regular 14px** |
| 普通页码 | 32 × 32 | **19px** | PingFang SC Regular 14px |

注：Web 分页使用 **PingFang SC Regular**（不是 Lato），与多语言市场习惯保持一致。

## 颜色

| 状态 | 背景 | 文字 / icon |
| --- | --- | --- |
| Prev/Next normal | `var(--fill-primary-container)` | `var(--text-icon-primary)` |
| Prev/Next disabled | `var(--fill-primary-container)` | `var(--text-icon-disable)` |
| Current page | `var(--text-icon-anti)` `#fff` | `var(--bg-primary)` `#0c0f12`（黑） |
| Normal page | transparent + 1px border `var(--divider-primary)` | `var(--text-icon-primary)` |
| Page hover | `var(--fill-secondary-button-hover)` | `var(--text-icon-primary)` |

## CSS

```css
.btcc-pagination {
  display: inline-flex;
  align-items: center;
  gap: var(--space-8);
}
.btcc-pagination__nav,
.btcc-pagination__page {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: var(--h-page);
  height: var(--h-page);
  font-family: "PingFang SC", var(--font-family-base);
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-regular);
  font-variant-numeric: tabular-nums;
  cursor: pointer;
  user-select: none;
}
.btcc-pagination__nav {
  border-radius: var(--radius-page-nav);  /* 25 */
  background: var(--fill-primary-container);
  color: var(--text-icon-primary);
  border: none;
}
.btcc-pagination__nav:disabled {
  color: var(--text-icon-disable);
  cursor: not-allowed;
}
.btcc-pagination__page {
  border-radius: var(--radius-page-page); /* 19 */
  border: 1px solid var(--divider-primary);
  background: transparent;
  color: var(--text-icon-primary);
}
.btcc-pagination__page:hover {
  background: var(--fill-secondary-button-hover);
}
.btcc-pagination__page[aria-current="page"] {
  background: var(--text-icon-anti);
  color: var(--bg-primary);
  border-color: var(--text-icon-anti);
}
.btcc-pagination__ellipsis {
  display: inline-flex;
  align-items: center; justify-content: center;
  width: var(--h-page); height: var(--h-page);
  color: var(--text-icon-secondary);
}
```

## 反模式

- ❌ Prev/Next 与页码用同一圆角（实际 25 vs 19，差 6）
- ❌ 当前页用品牌蓝填充（实际是反白：`#fff` bg + `#0c0f12` text）
- ❌ 字体写 Lato（实际 PingFang SC Regular）
- ❌ 数字不加 `font-variant-numeric: tabular-nums`
