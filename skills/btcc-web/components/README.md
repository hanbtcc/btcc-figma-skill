# Components（组件解剖）索引

> 17 份 BTCC Web 组件解剖。每份含：Figma 锚点、几何（高度 / 圆角 / padding）、token 引用、HTML / CSS 骨架、反模式。
> 全部基于新BTCC WEB Figma file `VrE25c6IAuIieWngebNnwx`，token 命名空间见 [`../tokens/web-tokens.css`](../tokens/web-tokens.css)。

## 文件清单

### Buttons（按钮族）

| 文件 | 用途 | 几何 |
| --- | --- | --- |
| [button-primary.md](button-primary.md) | 一级 CTA（提交 / 主操作） | h48 / pill 100 |
| [button-outline.md](button-outline.md) | 描边二级 CTA | h48 / pill 100 |
| [button-secondary-sm.md](button-secondary-sm.md) | 行内小按钮（编辑 / 删除 / 链接化操作） | h28 / r29 |

### Inputs（录入族）

| 文件 | 用途 | 几何 |
| --- | --- | --- |
| [input.md](input.md) | 文本 / 数量 / 价格输入 | h48 / r4 |
| [selector.md](selector.md) | dropdown / 选币 / 国家 等 4 种模式 | A 580 / B 540 |
| [switch.md](switch.md) | 开关（隐藏小数额、TP/SL） | 30×16 |
| [upload.md](upload.md) | KYC / 凭证 / 头像 上传 | dropzone 160h r4 |

### Containers（容器族）

| 文件 | 用途 | 几何 |
| --- | --- | --- |
| [dialog.md](dialog.md) | 弹窗 / Modal | 480 / 600 / 680 / r8 |
| [tab.md](tab.md) | 一级 / 二级 Tab | h40 / h32 |
| [topnav.md](topnav.md) | 顶部导航 | h64 |

### Data（数据族）

| 文件 | 用途 | 几何 |
| --- | --- | --- |
| [table.md](table.md) | 表格（订单 / 资金 / 卡券 / 排行榜） | 行高 40 / 56 |
| [orderbook.md](orderbook.md) | 盘口 | 380-420w / 24h 行 |
| [trading-form.md](trading-form.md) | 下单表单 | 380w / Open Long 蓝 Open Short 红 |
| [pagination.md](pagination.md) | 分页 | 32×32 |

### Feedback（反馈族）

| 文件 | 用途 | 几何 |
| --- | --- | --- |
| [alert.md](alert.md) | 行内 Alert（info / success / warning / danger） | 高度自适应 / r4 |
| [toast.md](toast.md) | 浮层 Toast | 顶部 56-64 |
| [tips.md](tips.md) | tooltip / 微提示 | 自适应 / r4 |

## 使用顺序

1. **先读** [`../rules.md`](../rules.md) → R-FONT-WEB / R-SHAPE-WEB / R-COLOR-WEB-1 / R-TOKEN-WEB。
2. **再读** [`../../btcc-shared/rules-shared.md`](../../btcc-shared/rules-shared.md) → R-SHARED-1 ~ R-SHARED-7。
3. **找组件** → 按上面分组进入对应 md。
4. **token 反查** → [`../tokens/web-tokens.css`](../tokens/web-tokens.css)（dark + light）/ [`../tokens/web-tokens.json`](../tokens/web-tokens.json)。

## 几何速查（高优先级，记不住就回这里）

| 元件 | 高度 | 圆角 |
| --- | --- | --- |
| 一级 / 描边 button | 48 | **100** pill |
| 行内小 button | 28 | 29 |
| input / selector / upload | 48 / 56 / 160 | **4**（不是 pill） |
| dialog | — | 8（外圆角） |
| card / table 容器 | — | 4 |
| Tab 一级 / 二级 | 40 / 32 | — |
| 表格行 | **40** 或 **56**（不插值 32/48/64） | — |
| 盘口行 | 24 | — |

## 反模式（组件级共性）

- ❌ button 圆角 6 / 8 / 12（这是 APP 风格；Web 必须 pill 100）
- ❌ input 圆角 100 / 24 / 12（实际 r4）
- ❌ dialog 圆角 4 或 16（实际 r8）
- ❌ 表格行高 32 / 48 / 64（实际 40 或 56，不插值）
- ❌ 数字列不加 `font-variant-numeric: tabular-nums`（违反 R-SHARED-5）
- ❌ Open Long 涂绿（合约 pro 必须蓝；R-COLOR-WEB-1）
- ❌ 用 `--btcc-*` / `--accent` / `--primary`（必须真实 Figma 命名空间，见 R-TOKEN-WEB）
