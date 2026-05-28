# Switch（开关）

> Figma 锚点：`734:14906 switch`（106×56 master，渲染 30×16）。

## 几何

| 属性 | 值 |
| --- | --- |
| 总尺寸 | 30 × 16 |
| 滑球 | 12 × 12（圆） |
| 滑球初始 left | 2px |
| 滑球开启 left | 16px |
| 圆角 | 8px（轨道）/ round-full（滑球） |

## 颜色

| 状态 | 轨道 | 滑球 |
| --- | --- | --- |
| Off | `var(--fill-switch-off)` `#444d59` | `#fff` |
| On | `var(--fill-switch-on)` = `var(--fill-brand-button-normal)` `#0c73ed` | `#fff` |
| Disabled | 加 0.4 opacity | — |

## CSS

```css
.btcc-switch {
  --w: var(--switch-w);     /* 30 */
  --h: var(--h-switch);     /* 16 */
  --b: var(--switch-ball);  /* 12 */
  position: relative;
  display: inline-block;
  width: var(--w); height: var(--h);
  border-radius: 8px;
  background: var(--fill-switch-off);
  cursor: pointer;
  transition: background 0.18s ease;
}
.btcc-switch::after {
  content: "";
  position: absolute;
  top: 2px; left: 2px;
  width: var(--b); height: var(--b);
  border-radius: 50%;
  background: #fff;
  transition: left 0.18s ease;
}
.btcc-switch[aria-checked="true"] {
  background: var(--fill-switch-on);
}
.btcc-switch[aria-checked="true"]::after { left: 16px; }
.btcc-switch[aria-disabled="true"] { opacity: 0.4; cursor: not-allowed; }
```

```html
<div role="switch" aria-checked="true" tabindex="0" class="btcc-switch"></div>
```

## 反模式

- ❌ 用 iOS 原生大尺寸 switch（48 / 56 宽，BTCC 是 30）
- ❌ 用绿/红做 on/off 状态色（绿是 success 不是 on，违反 R-SHARED-2；on 必须用品牌蓝）
- ❌ 滑球做成方角（应是圆）
