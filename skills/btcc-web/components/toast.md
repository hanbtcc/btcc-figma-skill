# Toast（瞬时通知）

> Figma 锚点：`4558:37495 toast`（584×98 master，渲染常见 168 宽 / 多行）。

## 用途

操作完成后的**瞬时反馈**：复制成功、订单已提交、网络断开、登录失效。3-5 秒后自动消失。

## 几何

| 属性 | 值 |
| --- | --- |
| 圆角 | **4px** |
| Padding | **20px 16px**（垂直 20，水平 16） |
| 最小宽度 | **168px** |
| 阴影 | `var(--shadow-toast)` `0 8px 10.4px rgba(0,0,0,0.12)` |
| 边框 | 1px solid `var(--border-primary)` |
| 背景 | `var(--bg-toast)` `#212830` |
| 字体 | Lato Medium 14px / 20px |
| 字色 | `var(--text-icon-primary)` |
| 图标 | 20px，左对齐，icon ↔ text 间距 12 |

## 浮动定位

| 上下文 | 位置 |
| --- | --- |
| 全局 toast | 页面**顶部居中**（top: 80px，distance from top nav）或**右上**（top: 80px, right: 24px） |
| 弹窗内 toast | 弹窗顶部 - 16px |

## CSS

```css
.btcc-toast {
  display: inline-flex;
  align-items: center;
  gap: var(--space-12);
  min-width: 168px;
  padding: var(--space-20) var(--space-16);
  background: var(--bg-toast);
  border: 1px solid var(--border-primary);
  border-radius: var(--radius-alert);
  box-shadow: var(--shadow-toast);
  color: var(--text-icon-primary);
  font-family: var(--font-family-base);
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  line-height: 20px;
}
.btcc-toast__icon { width: 20px; height: 20px; flex-shrink: 0; }
.btcc-toast--success .btcc-toast__icon { color: var(--fill-success); }
.btcc-toast--error   .btcc-toast__icon { color: var(--fill-error); }
.btcc-toast--warning .btcc-toast__icon { color: var(--fill-warning); }
.btcc-toast--info    .btcc-toast__icon { color: var(--fill-brand-button-normal); }

.btcc-toast-host {
  position: fixed;
  top: 80px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1100;
  display: flex; flex-direction: column; gap: var(--space-8);
  pointer-events: none;
}
.btcc-toast-host > * { pointer-events: auto; }
```

## 反模式

- ❌ Toast 圆角 12 / 24 / pill（实际 4）
- ❌ Toast 背景用 `*-alert` 系列（那是 Alert；Toast 用 `var(--bg-toast)` `#212830`）
- ❌ Toast 不带阴影（实际有 8/10.4px 阴影）
- ❌ Toast 持久不消失（默认 3000ms 后 fade）
