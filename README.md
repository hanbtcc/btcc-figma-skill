# BTCC Skills

> BTCC 设计语言 → Codex skill 仓库。从 Figma 源文件提取规则、token、组件解剖、页面索引、LP 模板族，按平台拆成三个独立 skill。

## 三 skill 结构

| Skill | 范围 | Figma 文件 | 状态 |
| --- | --- | --- | --- |
| [`skills/btcc-shared/`](skills/btcc-shared/) | 跨平台共享规则（操作优先 / 颜色即状态 / Unverified 标记 / 数据呈现 / 图标语言） | — | ✅ 已就绪 |
| [`skills/btcc-web/`](skills/btcc-web/) | Web 桌面（含 H5 响应式镜像）：Lato + PingFang SC、pill 100 / h48、9 个 LP 模板族 | `新BTCC WEB` `VrE25c6IAuIieWngebNnwx` | ✅ 已就绪 |
| [`skills/btcc-app/`](skills/btcc-app/) | iOS / Android 原生 APP | `新BTCC APP` `GW9kMfpf0Nib5DG4TjoWBp` | ⚠️ 等待 han 提供新一轮 Figma，全部规则视为 Unverified |

**重要**：Web 移动 H5（浏览器内 375w 视图）属于 **btcc-web/**，不属于 btcc-app/。原生 APP 是单独的 Figma 文件，规则与 Web H5 不一致。详见 [`skills/btcc-web/pages/h5-mirror.md`](skills/btcc-web/pages/h5-mirror.md)。

## 用法

### 1. 任务路由

按目标平台先选 skill：

```text
要做 BTCC Web 桌面 / H5  → skills/btcc-web/SKILL.md
要做 BTCC iOS / Android  → skills/btcc-app/SKILL.md（待重做）
跨平台规则                → skills/btcc-shared/rules-shared.md
```

### 2. 必读顺序

1. [`skills/btcc-shared/rules-shared.md`](skills/btcc-shared/rules-shared.md) — 所有任务的共同基线
2. 对应平台 SKILL.md 的「Task → Files」索引 — 把任务类型映射到最小文件集
3. 任务相关的 page / component / lp 解剖文档

### 3. QA

Web 输出在交付前跑：

```bash
python skills/btcc-web/qa-lint.py <file-or-dir>
```

规则覆盖：禁用 Helvetica/Inter 字体、禁用 `--btcc-*`/`--accent` token 名、CTA button 圆角必须 pill 100、input 圆角必须 r4、价格 / 余额必须 tabular-nums、合约方向蓝（Open Long 蓝 / Open Short 红）不得出现在现货 / 闪兑 / 资产语境。

## btcc-web 内容索引

```text
skills/btcc-web/
  SKILL.md                       入口 + Task → Files 索引
  rules.md                       Web 9 条规则（R-FONT-WEB / R-SHAPE-WEB / R-COLOR-WEB-1 等）
  figma-plugin-pitfalls.md       use_figma 插件常见坑
  qa-lint.py                     正则静态扫描器
  tokens/                        web 真实 Figma 变量（fill/brand-button/normal 等）
  components/                    17 份组件解剖：
    button-primary.md  button-outline.md  button-secondary-sm.md
    input.md  selector.md  switch.md  upload.md
    dialog.md  tab.md  topnav.md
    table.md  orderbook.md  trading-form.md  pagination.md
    alert.md  toast.md  tips.md
  pages/                         17 份页面索引：
    contract.md spot.md swap.md         交易类
    assets.md deposit.md withdraw.md transfer.md payment-fiat.md
    funding-history.md coupons.md       资产类
    bank-address.md account-security.md api-management.md
    identity-kyc.md vip.md              用户中心类
    dialog-library.md h5-mirror.md      通用 + H5
  lp/                            10 份 LP 模板族 + 中奖弹窗 + 3D 奖品资产 + i18n：
    rules-lp.md
    template-trading-contest.md  template-spinner.md  template-grid-9.md
    template-blindbox.md         template-slot.md     template-scratchcard.md
    template-generic-lp.md       modals-reward.md
    assets-3d-prizes.md          i18n-assets.md
```

## btcc-app 内容索引（旧版，待重做）

```text
skills/btcc-app/
  SKILL.md                       入口（已重写为 APP 专属，标注 Unverified）
  references/                    旧版 SSOT + APP 专属文件
  assets/                        APP 推断的 token CSS / JSON、icon SVG（待 Figma 校验）
  scripts/btcc_qa_lint.py        旧 lint 脚本，等 APP 重做
```

等 han 提供新 APP Figma 后，会按 btcc-web 的同种范式重做 btcc-app（rules → tokens → components → pages → qa-lint）。

## 核心规则（btcc-shared 摘要）

完整版见 [`skills/btcc-shared/rules-shared.md`](skills/btcc-shared/rules-shared.md)。要点：

- **R-SHARED-1 操作优先**：合约 / 现货 / 资产 / 闪兑首屏直接给操作组件，不放营销 hero。LP 是唯一例外。
- **R-SHARED-2 颜色即状态**：绿涨 / 红跌、绿成功 / 红失败 / 黄警告 / 蓝主操作。颜色不做装饰。
- **R-COLOR-1（合约 pro 专属，Web/APP 同向）**：Open Long 用品牌蓝、Open Short 用错误红，与西方规范相反。仅适用于 **合约 pro**——现货 / 闪兑 / 资产仍是绿买 / 红卖。
- **R-SHARED-3 Unverified 标记**：未在 Figma 验证的页面 / token / 组件，必须显式标 `Unverified` 并指出未验证之处。
- **R-SHARED-5 数据呈现**：价格 / 余额 / 倒计时 / 排行榜 / 分页全部 `font-variant-numeric: tabular-nums`。
- **R-NAME-1 真实 Figma 变量名**：禁用 `--primary` / `--accent` / 任意十六进制；用 `--fill-brand-button-normal`、`--text-icon-primary` 等真实命名空间。

## Figma 源文件

| 文件 | fileKey | 状态 |
| --- | --- | --- |
| 新BTCC WEB | `VrE25c6IAuIieWngebNnwx` | btcc-web/ 全部内容来自这份文件，已采样 1558:14723（415 frames）+ 7628:74717 LP（339 frames） |
| 新BTCC APP | `GW9kMfpf0Nib5DG4TjoWBp` | 等 han 提供新一轮文件，旧版数据保留在 btcc-app/references/ |

## 历史

仓库前身是单一的 `skills/btcc-style-generator/`（APP 与 Web 混在一起）。2026-05-28 拆成三 skill：

1. 抽出跨平台规则 → `btcc-shared/`
2. 按 `新BTCC WEB` Figma 重做 Web 全部内容 → `btcc-web/`
3. 老 `btcc-style-generator/` 改名为 `btcc-app/`，删掉 `platform-web/`，等待新 APP Figma 重做

git 历史完整保留（`git mv`）。
