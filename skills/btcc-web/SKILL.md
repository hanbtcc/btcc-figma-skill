---
name: btcc-web
description: 生成、实现、审查、写 prompt、用 Figma 制作 BTCC Web（桌面）crypto 交易所页面。覆盖合约（合约pro）、现货、闪兑、资产、充提币、划转、法币入金、卡券、安全账户、KYC、API管理、个人中心、VIP、LP 活动（交易赛/转盘/九宫格/盲盒/老虎机/刮刮卡）等所有 Web 业务域。来自新BTCC WEB Figma file (VrE25c6IAuIieWngebNnwx)。
---

# BTCC Web Generator

## 何时进入

- "做一个 BTCC 的合约页 / 现货页 / 充币页 / 提现弹窗"
- "用 BTCC 风格做一个落地页 / 转盘 / 盲盒 / 交易赛"
- "把这段代码改成 BTCC Web 风格"
- "BTCC Web 的按钮 / 输入框 / 表格 / Tab / 弹窗长什么样"
- 用户给出 BTCC Web Figma URL（fileKey `VrE25c6IAuIieWngebNnwx`）

## 何时不进入

- 原生 APP（iOS / Android）→ 进 `btcc-app`。**H5 镜像页（375w 浏览器移动版）属于 Web，不属于 APP**——见 `pages/h5-mirror.md`。
- 仅修跨平台的 R-SHARED-* 规则 → 进 `btcc-shared`。

## 必读顺序

1. [`../btcc-shared/rules-shared.md`](../btcc-shared/rules-shared.md) —— R-SHARED-1 ~ R-SHARED-7
2. [`rules.md`](rules.md) —— Web 专属（R-FONT-WEB / R-SHAPE-WEB / R-COLOR-WEB-1 / R-LAYOUT-WEB / R-TOKEN-WEB / R-LP-WEB / R-PAGE-WEB / R-SCOPE-WEB）
3. 任务索引下方的对应文件
4. 调 `use_figma` 之前 → [`figma-plugin-pitfalls.md`](figma-plugin-pitfalls.md)

## 任务 → 文件索引

不重复列必读项。每行只列**额外**要读的文件。

| 任务 | 必读 |
| --- | --- |
| 做合约 pro（期货下单页） | `pages/contract.md`、`components/trading-form.md`、`components/orderbook.md`、`components/topnav.md`、`components/selector.md`、`tokens/web-tokens.css` |
| 做现货 / 闪兑 | `pages/spot.md` 或 `pages/swap.md`、`components/trading-form.md`、`tokens/web-tokens.css` |
| 做资产总览 / 钱包 | `pages/assets.md`、`tokens/web-tokens.css` |
| 做充币 / 提币 / 划转 | `pages/deposit.md`、`pages/withdraw.md`、`pages/transfer.md`、`components/dialog.md` |
| 做法币入金 | `pages/payment-fiat.md`、`components/dialog.md` |
| 做卡券 / VIP / 个人中心 | `pages/coupons.md` 或 `pages/vip.md` |
| 做安全账户 / KYC | `pages/account-security.md`、`pages/identity-kyc.md`、`components/dialog.md`、`components/upload.md` |
| 做 API 管理 | `pages/api-management.md`、`components/dialog.md` |
| 改一个按钮 / Tab / Input / 上传 | `components/<component>.md`、`tokens/web-tokens.css` |
| 改一个弹窗 / 提示 | `components/dialog.md` 或 `components/alert.md` 或 `components/toast.md` 或 `components/tips.md` |
| 改资金记录 / 报表 / 表格类 | `pages/funding-history.md`、`pages/vip.md`（交易报表）、`components/table.md` |
| 做 LP 活动 / 落地页 | `lp/rules-lp.md` 然后选模板：`template-trading-contest.md` / `template-spinner.md` / `template-grid-9.md` / `template-blindbox.md` / `template-slot.md` / `template-scratchcard.md` / `template-generic-lp.md`，加 `lp/modals-reward.md`、`lp/i18n-assets.md` |
| 用 Figma 插件直接搭 | `figma-plugin-pitfalls.md` |
| 复查输出 | `qa-lint.py` 跑一遍，再核 `rules.md` 的反模式速查 |

## Figma 抓取流程

1. 文件：`新BTCC WEB`，fileKey `VrE25c6IAuIieWngebNnwx`。
2. 先用 `get_metadata`（无 nodeId）确认 canvas 仍是 `0:1 / 1558:14723 / 7628:74717 / 3089:7459`。
3. 想做组件 → 进 `0:1`，看 `tokens/web-tokens.css` 的 nodeId 行。
4. 想做页面 → 进 `1558:14723`，按 `pages/<topic>.md` 中给出的 nodeId 跳转。
5. 想做 LP → 进 `7628:74717`，按 `lp/template-*.md` 中给出的样本 nodeId 跳转。
6. 调用 `use_figma` 前，**先读** `figma-plugin-pitfalls.md` 的 7 条 P-PLUGIN-* 与预飞行清单。

## 完成检查（Completion Gate）

1. 已读 `../btcc-shared/rules-shared.md` 与 `rules.md`，反模式速查无命中。
2. 跑 `python skills/btcc-web/qa-lint.py <文件或目录>`（如有本地代码输出）。
3. Token 全部走 `var(--*)`，命名空间在 `tokens/web-tokens.css` 内，没有自造 `--btcc-*`。
4. 字体走 Lato + PingFang SC，不写 Helvetica Neue / Inter。
5. CTA 是 48px / pill 100；Input 是 48px / 4。
6. 合约方向按钮 long = 蓝、short = 红；现货买卖仍按绿/红。
7. 所有提到的页面 / 组件 nodeId 可在 Figma 中查到；查不到的标 Unverified。
8. 调 Figma 插件前已过 figma-plugin-pitfalls.md 的预飞行清单。

## 资产清单

| 资产 | 用途 |
| --- | --- |
| `tokens/web-tokens.css` | Web 真实 Figma 变量名转写的 CSS 自定义属性，dark + light |
| `tokens/web-tokens.json` | 同上的 JSON 版本，给工具链用 |
| `qa-lint.py` | 启发式 lint：检查 Web 真实 token、48/100、Lato 等 |
| `figma-plugin-pitfalls.md` | 调 `use_figma` 前的 7 条 P-PLUGIN-* 与预飞行清单 |
