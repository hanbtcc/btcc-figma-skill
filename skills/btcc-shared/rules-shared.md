---
name: btcc-shared-rules
description: 跨平台 BTCC 设计原则。APP 与 Web 共用的硬规则。被 btcc-app 与 btcc-web 各自的 rules.md 引用，不重复表述。
---

# BTCC Shared Rules（SSOT，跨平台）

> 这是 BTCC 设计语言中**与平台无关**的硬规则。APP 与 Web 各自的 `rules.md` 必须引用此处条目，不得自行复述。
>
> 平台差异（断点、触控目标、字体、控件高、半径、状态色映射的细节）一律放到 platform 层。

## R-SHARED-1 操作优先（Operational-first）

**规则**：BTCC 是交易产品，不是营销站点。**首屏必须呈现可操作状态**：行情、订单、持仓、资产、表单。

**反模式**：
- 满屏 hero、品牌口号、价值主张段落作为首屏。
- 在交易/钱包/账户/订单页放营销轮播。
- 用插画装饰核心数据区。

**例外**：仅 `LP活动` canvas（运营活动落地页）允许 hero 全屏图，且 hero 之下所有模块仍必须是操作型（进度、排行、规则表、领奖按钮）。

**判定**：首屏 1080px（Web）或 1 屏（APP）内若超过 30% 像素是装饰性内容（图、口号、空 padding），即违反。

---

## R-SHARED-2 颜色即状态（Color = State）

**规则**：红/绿/橙/金只承载语义，不做装饰。
- **绿** = 正向数值、Success 状态、买入方向（spot 现货）。
- **红** = 负向数值、Error/Danger 状态、卖出方向（spot 现货）、Open Short 按钮（合约）。
- **橙** = Warning 状态。
- **金** = 提醒/奖励/勋章/check-in。
- **品牌蓝** = 主操作（CTA、Open Long 合约按钮、链接、tab 选中条）。

**反模式**：
- 用绿/红当背景色装饰非语义模块（例如绿色 banner、红色卡片标题）。
- 同一页面有两种以上 CTA 主蓝色。
- 用金色当文字色装饰非奖励内容。

**注意**：合约（futures）方向按钮颜色与现货（spot）不同。**详见各平台 rules.md 的 R-COLOR-1**——这是平台层规则，不在 shared。

---

## R-SHARED-3 未验证必须标记（Unverified）

**规则**：任何未在最近一次 Figma `get_metadata` pass 中确认存在的页面/组件/token，输出时必须显式标注 `> Unverified / 未验证：本节基于 BTCC 通用约定推导，不在已验证 Figma 节点中。`

**反模式**：
- 把"我猜 BTCC 应该有这个"当作事实写进 spec。
- 复用旧 skill 留下来的页面别名却不核对当前 Figma 是否还存在。
- 把 APP 的 token 直接套到 Web 不做核对。

**判定**：spec 中出现的每个 nodeId 必须可以在对应 Figma 文件中查到；查不到就标 Unverified。

---

## R-SHARED-4 Token 命名空间（Naming）

**规则**：所有颜色/字号/半径/间距引用必须走**已存在的 Figma 本地变量名**或其 CSS 等价物。

**Web 与 APP 共享同一组语义颜色变量**（Web 文件中通过 import APP 文件的变量库实现）。具体命名见各平台 `tokens/`。

**反模式**：
- 写死十六进制颜色（除非是 token fallback 同行）。
- 自造 `--primary` / `--accent` / `--btcc-*` 这种不在 Figma 变量集合里的命名空间。
- 用同一份 token 文件假装 APP 与 Web 完全一致——尺寸/半径/字体差异要走平台 tokens。

---

## R-SHARED-5 数据呈现（Tabular Data）

**规则**：所有数字（价格、量、余额、收益、倒计时）必须使用**等宽数字**（tabular-nums）渲染。表格行高紧凑，列对齐严格（数字右对齐或小数点对齐）。

**实现层**：
- Web 端 CSS：`font-variant-numeric: tabular-nums`（在 BTCC 字体 Lato/PingFang 上仍生效）。
- APP 端按平台 rules-app.md 处理。
- Figma 中不要试图通过 `fontFeatures` API 强行打开 TNUM——见 `figma-plugin-pitfalls.md` P-PLUGIN-1。

**反模式**：
- 用变宽数字渲染价格表（视觉上数字会跳动）。
- 表格行 padding 超过 16px（密度变低，操作信息减少）。
- 数字列左对齐或居中对齐。

---

## R-SHARED-6 图标语言（Icon Language）

**规则**：使用 BTCC Figma `设计规范` 与 `图标` 页面导出的图标。线性风格、stroke 1.5–2px、24px 网格。

**反模式**：
- 用 Material/FontAwesome/Heroicons 等通用库图标替代 BTCC 原生图标。
- 在交易控件区用彩色填充图标（操作区图标必须单色）。
- 图标尺寸不在 16/20/24/32 系列内。

---

## R-SHARED-7 Single-Source Truth（SSOT）

**规则**：本文件是跨平台规则的唯一来源。

- `btcc-app/rules.md` 与 `btcc-web/rules.md` 引用本文件条目时，**只写 R-SHARED-N 的引用**，不复述规则文本。
- 平台特有规则（断点、触控、平台字体、控件高/半径、合约方向按钮颜色、LP 模板）写在各自 rules.md。
- 当 shared 与 platform 冲突时，以 platform 为准（因为 platform 更具体）。

---

## 反模式速查（Anti-pattern Cheatsheet）

| 现象 | 违反 |
| --- | --- |
| 交易页首屏放品牌 hero | R-SHARED-1 |
| 用绿色 banner 装饰 | R-SHARED-2 |
| 用金色当链接色 | R-SHARED-2 |
| 自造 `--btcc-primary` | R-SHARED-4 |
| 价格表数字会跳 | R-SHARED-5 |
| Heroicons 替代原生图标 | R-SHARED-6 |
| 把 APP token 直接搬给 Web 不核对 | R-SHARED-4 |
| 推测 BTCC 应该有的页面写成事实 | R-SHARED-3 |
