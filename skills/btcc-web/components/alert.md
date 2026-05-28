# Alert（横条提示）

> Figma 锚点：`770:8645 Alert`（296×* master）；变体 `128343:195716 Alert`（552×48）。

## 用途

页面顶部 / 表单顶部 / 弹窗内的**持久状态提示**——告诉用户当前状态（KYC 未完成、API 已禁用、邮箱已过期）。区别于 [`toast.md`](toast.md)（瞬时通知）、[`tips.md`](tips.md)（hover 气泡）。

## 几何

| 属性 | 值 |
| --- | --- |
| 圆角 | **4px** |
| Padding | 6px 12px 6px 16px（左 16 右 12，垂直 6） |
| 高度 | 自适应内容（最小 36，常见 48） |
| 图标尺寸 | 16px，左对齐 |
| icon ↔ text 间距 | 8px |
| 关闭按钮 | 16px，右对齐，可选 |

## 4 种状态色

每种状态背景使用 `*-alert` 同色族，文字使用同色族的"主色"。

| 状态 | 背景 | 文字 / icon | 用途 |
| --- | --- | --- | --- |
| Info | `var(--fill-info-alert)` `#11375d` | `var(--fill-brand-button-normal)` `#0c73ed` | 一般信息、提示 |
| Success | `var(--fill-success-alert)` `#14513c` | `var(--fill-success)` `#2ca85d` | 操作成功、状态正常 |
| Danger | `var(--fill-danger-alert)` `#5c2329` | `var(--fill-error)` `#eb464f` | 错误、风险 |
| Warning | `var(--fill-warning-alert)` `#5b3415` | `var(--fill-warning)` `#e0601f` | 警告、需注意 |

> 反模式：把 Alert 背景做成 `var(--fill-error)` 纯红 → 不对，Alert 是**淡色背景 + 高对比文字**，用 `*-alert` 系列。

## CSS

```css
.btcc-alert {
  display: flex;
  align-items: flex-start;
  gap: var(--space-8);
  padding: 6px var(--space-12) 6px var(--space-16);
  border-radius: var(--radius-alert);
  font-family: var(--font-family-base);
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  line-height: 20px;
}
.btcc-alert__icon { width: 16px; height: 16px; flex-shrink: 0; }
.btcc-alert__body { flex: 1; min-width: 0; }
.btcc-alert__close {
  width: 16px; height: 16px;
  background: none; border: none; cursor: pointer;
  color: inherit; opacity: 0.7;
}
.btcc-alert__close:hover { opacity: 1; }

.btcc-alert--info    { background: var(--fill-info-alert);    color: var(--fill-brand-button-normal); }
.btcc-alert--success { background: var(--fill-success-alert); color: var(--fill-success); }
.btcc-alert--danger  { background: var(--fill-danger-alert);  color: var(--fill-error); }
.btcc-alert--warning { background: var(--fill-warning-alert); color: var(--fill-warning); }
```

## 反模式

- ❌ 把 alert 圆角做 8 / 12 / 100（实际 4）
- ❌ 用纯色背景（实际 `*-alert` 暗调） + 浅色文字（应反过来）
- ❌ 把 Toast 当 Alert 用（Toast 浮在页面右上 / 顶部，Alert 嵌在内容流中）
