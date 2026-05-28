# 一级 button（CTA / Primary Button）

> Figma 锚点：`741:4552`（component master），`741:4616`（描边变体 → 见 [`button-outline.md`](button-outline.md)）。
> 文件：新BTCC WEB（`VrE25c6IAuIieWngebNnwx`）/ canvas `0:1 设计规范`。

## 用途

Web 操作页 / LP 活动 / 弹窗的**主操作 CTA**：Register Now、Confirm、Buy、Sell、Open Long、领取奖励。

每个页面 / 弹窗中**最多一个一级 button**。其余操作降级为描边或次级 button。

## 几何（R-SHAPE-WEB）

| 属性 | 值 | 说明 |
| --- | --- | --- |
| 高度 | **48px** | 不变 |
| 宽度 | hug content（最小 168px，建议 168 / 210 / 234 三档） | LP hero CTA 234，弹窗 168，操作页面 210 |
| 圆角 | **100px**（pill） | 不是 6 / 8 / 12 |
| Padding | 10px 上下 + 24px 左右 | 文字/图标居中 |
| 文字间距 | 图标 + 文字之间 8px | 仅当带图标时 |

## 颜色（R-TOKEN-WEB）

### Dark
| 状态 | 背景 | 文字 |
| --- | --- | --- |
| Normal | `var(--fill-brand-button-normal)` `#0c73ed` | `var(--text-icon-anti)` `#fff` |
| Hover | `var(--fill-brand-button-hover)` `#0b6adb` | `#fff` |
| Pressed | `var(--fill-brand-button-pressed)` `#0a5fc4` | `#fff` |
| Disabled | `var(--fill-brand-button-disable)` `#202738` | `var(--text-icon-disable)` `#3d4655` |

### Light
| 状态 | 背景 | 文字 |
| --- | --- | --- |
| Normal | `#195eff` | `#fff` |
| Hover | `#1450e6` | `#fff` |
| Pressed | `#0f44cc` | `#fff` |
| Disabled | `#e6edf7` | `#b6bcc9` |

## 字体（R-FONT-WEB）

- Family: **Lato**（拉丁/数字优先，中文兜底 PingFang SC）
- Weight: **Medium (500)**
- Size: **14px**
- Line-height: 20px

## HTML / CSS 结构

```html
<button class="btcc-btn-primary">Register Now</button>
<button class="btcc-btn-primary" disabled>Disabled</button>
<button class="btcc-btn-primary">
  <span class="icon"><!-- 24px svg --></span>
  Buy with Card
</button>
```

```css
@import "../tokens/web-tokens.css";

.btcc-btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-8);
  height: var(--h-button);
  padding: 0 var(--space-24);
  min-width: 168px;
  border: none;
  border-radius: var(--radius-pill);
  background: var(--fill-brand-button-normal);
  color: var(--text-icon-anti);
  font-family: var(--font-family-base);
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  line-height: 20px;
  cursor: pointer;
  transition: background 0.15s ease;
}
.btcc-btn-primary:hover    { background: var(--fill-brand-button-hover); }
.btcc-btn-primary:active   { background: var(--fill-brand-button-pressed); }
.btcc-btn-primary:disabled {
  background: var(--fill-brand-button-disable);
  color: var(--text-icon-disable);
  cursor: not-allowed;
}
```

## Figma 中创建（use_figma 片段）

```js
const btn = figma.createFrame();
btn.layoutMode = 'HORIZONTAL';
btn.primaryAxisAlignItems = 'CENTER';
btn.counterAxisAlignItems = 'CENTER';
btn.primaryAxisSizingMode = 'AUTO';   // hug width，先按文字撑
btn.counterAxisSizingMode = 'FIXED';
btn.resize(210, 48);
btn.cornerRadius = 100;
btn.paddingLeft = 24; btn.paddingRight = 24;
btn.paddingTop = 10;  btn.paddingBottom = 10;
btn.fills = [{ type: 'SOLID', color: { r: 0x0c/255, g: 0x73/255, b: 0xed/255 } }];

const t = figma.createText();
await figma.loadFontAsync({ family: 'Lato', style: 'Medium' });
t.fontName = { family: 'Lato', style: 'Medium' };
t.fontSize = 14;
t.characters = 'Register Now';
t.fills = [{ type: 'SOLID', color: { r: 1, g: 1, b: 1 } }];
btn.appendChild(t);
```

参见 `figma-plugin-pitfalls.md`：
- P-PLUGIN-3 hug-content：button 是 hug，不要让父级把它拉宽。
- P-PLUGIN-5 字体名 `Medium`，不是 `medium` / `MEDIUM`。
- P-PLUGIN-7 hex 必须 0–1 浮点，不要 0–255 int。

## 在合约 pro 的特例（R-COLOR-WEB-1）

- **Open Long**（开多）按钮：用此组件 + 文字 `开多 / Open Long`，**保持品牌蓝**。Figma anchor `554:5259 开多下单button`（389×80，**LP 不复用此尺寸；下单区按 80 高、本组件按 48 高**）。
- **Open Short**（开空）按钮：同结构但背景换为 `var(--fill-error)` `#eb464f`，文字仍 `var(--text-icon-anti)`。Figma anchor `554:5266 开空下单button`（395×80）。

详见 [`trading-form.md`](trading-form.md)。

## 反模式

- ❌ 圆角写 6 / 8 / 12 / 16 → 用 100（pill）
- ❌ 字体写 Helvetica Neue / Inter → 用 Lato Medium
- ❌ 同页面出现两个一级 button → 第二个降级到 outline 或 secondary
- ❌ Open Long 涂绿 → 永远是品牌蓝
- ❌ disabled 用 `opacity: 0.4` → 用 `--fill-brand-button-disable` token
