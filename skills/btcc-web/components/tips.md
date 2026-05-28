# Tips（hover 气泡 / Tooltip）

> Figma 锚点：`112251:212465 tips`（292×96 master）。

## 用途

hover 在 icon、字段名、表头上，揭示**额外说明**。和 [`alert.md`](alert.md)（持久状态条）、[`toast.md`](toast.md)（瞬时通知）有别——tips 必须由用户**主动 hover** 触发，离开即消失。

## 几何

| 属性 | 值 |
| --- | --- |
| 圆角 | **4px** |
| Padding | 8px 12px |
| 最大宽度 | 292px（自适应内容） |
| 背景 | `var(--bg-tips)` `#1d232a` |
| 阴影 | `var(--shadow-tips)` `0 4px 8px rgba(0,0,0,0.16)` |
| 字体 | Lato Regular 12px / 16px |
| 字色 | `var(--text-icon-primary)` |
| 箭头（指向触发元素） | **8 × 16 多边形**，颜色与 tip 背景一致 |

## CSS

```css
.btcc-tip {
  position: relative;
  max-width: 292px;
  padding: var(--space-8) var(--space-12);
  background: var(--bg-tips);
  border-radius: var(--radius-alert);
  box-shadow: var(--shadow-tips);
  color: var(--text-icon-primary);
  font-family: var(--font-family-base);
  font-size: var(--font-size-xs);
  font-weight: var(--font-weight-regular);
  line-height: 16px;
  z-index: 1000;
}
.btcc-tip__arrow {
  position: absolute;
  width: 16px; height: 8px;
  background: var(--bg-tips);
  clip-path: polygon(50% 100%, 0 0, 100% 0);
}
.btcc-tip[data-placement="top"] .btcc-tip__arrow {
  bottom: -8px; left: 50%; transform: translateX(-50%);
}
.btcc-tip[data-placement="bottom"] .btcc-tip__arrow {
  top: -8px; left: 50%; transform: translateX(-50%) rotate(180deg);
}
```

## 反模式

- ❌ Tip 圆角 8 / 12（实际 4）
- ❌ Tip 字号 14（实际 12 Regular）
- ❌ 把 Tip 做成持久 panel（应是 hover 触发，离开消失；持久状态用 Alert）
- ❌ 箭头用 4×8（实际 8×16）
