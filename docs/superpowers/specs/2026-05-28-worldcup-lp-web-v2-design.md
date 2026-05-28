---
name: BTCC 世界杯 LP v2（累进解锁版，路径 C）
date: 2026-05-28
platform: web
status: design-pending-review
unverified-marker: true
target-figma:
  team: Metaverse HK (organization::1544657499809167084)
  file: BTCC × World Cup 2026 — 世界杯拉新累进 LP（待 use_figma 创建新文件）
references:
  - skills/btcc-style-generator/references/rules.md
  - skills/btcc-style-generator/references/platform-web/rules-web.md
  - skills/btcc-style-generator/references/platform-web/for-figma-inspect/source-anchors.md  # LP activity reference: 7752:73942 jjj交易赛
  - skills/btcc-style-generator/references/for-prompt-design/figma-plugin-pitfalls.md
supersedes: 2026-05-28-worldcup-lp-web-design.md
---

# BTCC 世界杯 LP v2 — 累进解锁版（路径 C）设计文档

## 0. 与 v1 的差异（重读历史用）

| 维度 | v1（平分版） | v2（累进版，本文档） |
| --- | --- | --- |
| 奖池机制 | 100,000 USDT 平分 | 0 → 100,000 USDT 累进解锁，新用户加入推动奖池上涨 |
| Hero | 两栏：左标题 + 右奖池行情卡 | 全幅头图 + 左对齐标题/CTA（对齐公司 jjj交易赛） |
| 段标题 | 16px 左对齐 | 40px 居中（对齐公司范式） |
| 「我的」模块 | 嵌入奖池预览右下 | 独立 1200×236 双卡块，数字 48px |
| 奖池可视化 | 4 行行情卡 | progress-bar-with-ticks 时间线（直接复用公司范式） |
| 排行榜 | 实时参与流（伪流式 8 行） | 邀请人排行：Top3 大卡 + 4-10 名表格 |
| 规则 | 文字双栏 list | 4 列数据表 + 末尾 terms 长文 |
| 装饰图 | 0 张 | 允许少量（hero、Top3 背景大数字、邀请图标） |

**v2 仍然保留 v1 的核心定位**：拉新落地页，主 CTA "立即注册领奖"。机制改成累进，目的是复用公司的 progress-bar 视觉语言而不发明新的。

## 1. 目标与约束

- **场景**：世界杯期间的新用户注册落地页，机制为「人越多，奖池越大」。
- **平台**：Web 桌面，主 frame 1920×~5800，内容区 1200 居中（与公司 jjj交易赛 一致）。
- **机制**：每 1,000 个新用户注册并完成入金，奖池累进 +5,000 USDT，封顶 100,000 USDT。最终所有合格用户按邀请份额瓜分奖池（不再是无差别平分）。
- **主 CTA**：`立即注册领奖`，hero 与 footer 各出现一次（保持 v1 的克制）。
- **风格**：BTCC 主站延续，dark-first，密排，操作型语言。

### R-rule 边界

| 规则 | 处理 |
| --- | --- |
| `R-LAYOUT-1` | LP 是公司唯一允许的「带 hero 装饰图」例外 surface。第一屏内容区下方仍要有可被即时操作的奖池 progress（与公司一致） |
| `R-LAYOUT-2` | 严格保留：tabular-nums、密排表、克制卡片 |
| `R-COLOR-1` | 不涉及（无交易控件） |
| `R-COLOR-2` | 严格保留：绿色仅用于「已完成 / 已解锁」与正向数字 |
| `R-NAME-1` | 全部 `--btcc-*`，不引入 `--accent` 或裸 hex |
| `R-SCOPE-1` | 顶部加 `Unverified / 未验证` chip |

## 2. 整体框架

- 主 frame：1920 × ~5800，背景 `--btcc-bg-primary` (`#0C0F12`)
- 内容列：1200 居中，左 360 / 右 360
- 模块间距：80px（公司稿用 80–120px，本稿统一 80）
- 字体：`--btcc-font-family-sans`
- 数字列：`font-variant-numeric: tabular-nums`，右对齐

## 3. 模块清单（top → bottom）

```
[Hero — 1920×720 全幅头图 + 左 768 内嵌标题/CTA]
  ↓ 80
[Pool Progress — 累进时间线（核心）]
  ↓ 80
[My Status — 双卡：我邀请的人 / 我的预估奖金]
  ↓ 80
[Three Steps — 三步领奖（v1 内容保留，视觉降级辅助说明）]
  ↓ 80
[Inviter Leaderboard — Top3 大卡 + 4-10 名表格]
  ↓ 80
[Pool Distribution Rules — 4 列数据表]
  ↓ 80
[Terms — 长文段]
  ↓ 80
[Footer CTA — 倒计时 + 主按钮]
```

## 4. Hero 区（1920×720）

**结构：** 全幅 hero frame，含装饰图 + 底部 194px overlay（与公司 `7752:84855` 同构），内嵌左对齐 768 内容块定位在 `(312, 200)`。

### 装饰图层

- 背景 1920×720 渐变 + 装饰元素（**Unverified**：本稿无对应素材，先用 BTCC 蓝紫渐变 `--btcc-brand` → `--btcc-bg-primary` 占位，后续替换为世界杯主题素材）
- 底部 194px overlay：`--btcc-bg-primary` α=0.85，作为标题与下方内容的过渡

### 内容块（768×336，左对齐）

```
[chip] WORLD CUP × BTCC                           ← 12px / brand / brand-alert 背景
[h1] Win Your Share of                             ← 56/64, primary
     100,000 USDT World Cup Pool                   ← 56/64, "100,000 USDT" 用 brand 蓝
[sub] Pool grows as more traders register.         ← 14/22, secondary
      Bigger community, bigger pool.
[cta-row]                                          ← 56 高
  [Register Now (168×56)]   [Learn More (76×56)]
```

- chip：`padding: 4px 10px`，背景 `--btcc-brand-alert`，圆角 `--btcc-radius-tag` (4px)
- h1：`Helvetica Neue` 700 / 56px / 行高 64
  - 「100,000 USDT」用 `setRangeFills` 着色为 `--btcc-brand`（按 P-PLUGIN-2，按字符索引）
- sub：14px / `--btcc-text-secondary` / 22px 行高
- 主 CTA：168×56，`--btcc-brand` 填充，`--btcc-text-anti` 文字 / 14px / 500
- 次 CTA：76×56，`--btcc-button-secondary-bg`，文字 `--btcc-text-primary`

## 5. Pool Progress（累进时间线，核心）

公司稿同位模块：`7801:96426`（1200×686）。完整复用 progress-bar + ticks 范式。

**整体：** 1200 宽，内边距 32 / 32，标题 40px 居中，下方累进时间线。

### 5.1 段标题

`Prize Pool — Unlocked by Community` — 40px / `--btcc-text-primary` / 700，居中

### 5.2 引导文案（一行）

`Initial pool: 5,000 USDT. For every 1,000 new users completing deposit, the pool unlocks +5,000 USDT. Maximum: 100,000 USDT.`

- 14px / `--btcc-text-secondary`，居中，距标题 24

### 5.3 主累进卡（1136×322）

横向两列，分隔线居中：

| 列 | 内容 |
| --- | --- |
| 左 535×322 | 装饰图 320×198（蓝色奖杯/球类占位）+ 「Unlocked Prize Pool (USDT)」label + 数字 `45,000` 48px brand 蓝 |
| 中分 | 2×171 px 竖线 `--btcc-divider-container` |
| 右 535×322 | 装饰图 320×198（社区/人头占位）+ 「Total Participants」label + 数字 `12,486` 48px primary |

数字字号：48px / 700 / tabular-nums

### 5.4 累进时间线（1136×68）

公司稿对应 `7801:96427`。结构：左 153 宽 label 列 + 右 1017 宽 ticks 列。

**Label 列（153×68）**：
- 上：`New Users` / 14px / secondary
- 下：`Pool Amount` / 14px / secondary
- 行间距同公司稿，纵向距 31px 是中线

**Ticks 列（1017×68）**：13 个 tick @ 44×68，间距按公司稿留白（每段 84px 中心距）。每个 tick：

```
50,000        ← 上数字 14/22 primary
   ●          ← 中心小圆点 6×6，已解锁的填 brand 蓝、未解锁的填 text-tertiary
5,000         ← 下数字 14/22，已解锁 primary，未解锁 text-secondary
```

底部 progress bar 987×4，圆角 2，已解锁段 `--btcc-brand`，未解锁段 `--btcc-divider-container`。当前奖池 45,000 → 9 个 tick 已解锁。

> 这是 BTCC LP 的核心可视化范式。务必复用，不发明新的奖池图。

## 6. My Status（1200×236）

公司稿同位模块：`7801:96560`。两张 584×156 卡横排，间距 32。

### 卡 1（584×156）

```
[内容区 32 padding]
  My Invites                                      ← 24/24 secondary
  127                                             ← 48/48 primary tabular-nums
[右侧装饰 175×154 — 邀请图标占位]
```

### 卡 2（584×156）

```
[内容区 32 padding]
  Estimated Reward (USDT)                         ← 24/24 secondary
  358.42                                          ← 48/48 success（绿，per R-COLOR-2）tabular-nums
[右侧装饰 192×154 — 奖金图标占位]
```

- 卡背景 `--btcc-bg-card`
- 卡内边框 1px `--btcc-divider-container`
- 圆角 `--btcc-radius-card` (12)

## 7. Three Steps（v1 保留，视觉降级）

由「主区」降为「侧支说明」。三个 380×220 卡横排（与 v1 同），但去掉 watermark 大数字（v1 踩坑：watermark 抢戏），改为左上小 step 数字 chip：

| 卡 | 标题 | 说明 | 解锁 | CTA |
| --- | --- | --- | --- | --- |
| Step 1 | Register | Phone or email | Eligible to invite | Register Now |
| Step 2 | Deposit ≥ 100 USDT | Activate your account | Counts toward pool | Deposit |
| Step 3 | Invite a Friend | Share your code | +1 share for you | Get Invite Code |

**关键改动**：
- 去掉左上 48px watermark 数字
- 改为左上 24×24 chip：`#1` `#2` `#3`，背景 `--btcc-fill-tag`，文字 `--btcc-text-primary` 14px
- 状态徽章保留（待完成 / ✓已完成）
- CTA 按钮规格保留

段标题 `How to Earn Shares` 40px 居中。

## 8. Inviter Leaderboard（1200×~980）

公司稿同位模块：`7801:96584`。

### 8.1 段标题

`Top Inviters` — 40px / primary / 居中

### 8.2 Top 3 大卡（1200×325，三列各 378.6×325）

每张大卡上半 220 高，下半 103 高分隔线划开。

**上半 220：**
- 左侧 32/32 起 80×80 头像位（占位 `--btcc-fill-secondary-container`）
- 头像下方 32/128 起 60 高文字块：用户名（24/24 primary）+ `no.1`（24/24 secondary）
- 右侧绝对定位大数字 `1` / `2` / `3`：146×300，字号 ~220 / 700 / `--btcc-text-disabled`（淡化背景）

**下半 103（双列）：**
- 左 138×55：`123` 邀请人数（24px primary tabular-nums）+ label `My Invites`（14px secondary）
- 右 93×55：`580` 预估奖金（24px success tabular-nums）+ label `Reward (USDT)`（14px secondary）

中间 2px 分隔线 328 宽。

### 8.3 第 4-10 名表格（1200×472）

7 行 × 64 高密排表，每行 4 列：

| 列 | 宽 | 对齐 | 字号 |
| --- | --- | --- | --- |
| Rank | 219.6 | 左 | 17/17 primary |
| UID | 219.6 | 左 | 17/17 primary |
| My Invites | 381 | 右 | 17/17 primary tabular-nums |
| Reward (USDT) | 219.6 | 右 | 17/17 success tabular-nums |

行间分隔 1px `--btcc-divider-primary`。

底部一行小字 208×17：`Updates every hour · Top 50 shown` / 14/14 / `--btcc-text-disabled`

## 9. Pool Distribution Rules（1200×514）

公司稿同位模块：`7833:14693`。规则即数据表。

### 段标题

`Reward Distribution Rules` — 40px / primary / 居中

### 表格（1200×434，3 列 × 6 行）

| Rank | Share of Pool | Min Invites Required |
| --- | --- | --- |
| 1 | 22% | 100 |
| 2-5 | 34% | 50 |
| 6-10 | 15% | 20 |
| 11-50 | 24% | 10 |
| 51-100 | 5% | 5 |
| 101-200 | 5% | 1 |

- 列宽：357.3 / 357.3 / 357.3（左侧 32 padding）
- 行高 64
- 表头 14px / secondary
- 表格内容 17px / primary（数字列右对齐 + tabular-nums）
- 行分隔 1px `--btcc-divider-primary`

## 10. Terms（1200×~600）

公司稿同位模块：`7833:15006`。

- 段标题 `Campaign Rules & Terms` 40px 居中
- 长文 1200 宽，14/22 secondary，约 11 条编号条款，覆盖：
  1. 注册资格（必须点击 Register Now）
  2. 入金阈值（≥ 100 USDT 才计入）
  3. 邀请有效性（被邀请人需完成入金）
  4. 排行榜计算（按邀请的合格新用户数）
  5. 反作弊（同 IP / 同设备 / 同 KYC 视为单账号）
  6. 奖励发放（活动结束后 5 个工作日）
  7. 奖励性质（trading funds，可作保证金，不可提现）
  8. 解释权归 BTCC

## 11. Footer CTA

```
              距活动结束还剩
            42d 17:23:08                    ← 32/32 brand tabular-nums
            ─────────────                   ← 80×1 divider-container
        [    立即注册领奖    ]              ← 240×64 brand fill
              已有 12,486 人参与            ← 14/14 secondary
```

居中布局，纵向 16/24/16 间距。**整页只在 hero 与此处出现 CTA 按钮，保持克制。**

## 12. Token 速查（仅本 LP 用到）

- 背景：`--btcc-bg-primary` / `--btcc-bg-card`
- 文字：`--btcc-text-primary` / `--btcc-text-secondary` / `--btcc-text-disabled` / `--btcc-text-anti`
- 品牌：`--btcc-brand` / `--btcc-brand-pressed` / `--btcc-brand-alert`
- 状态：`--btcc-success` / `--btcc-success-alert`
- 分隔/边框：`--btcc-divider-primary` / `--btcc-divider-container`
- 填充：`--btcc-fill-tag` / `--btcc-fill-secondary-container`
- 圆角：`--btcc-radius-tag` (4) / `--btcc-radius-control` (6) / `--btcc-radius-card` (12)

## 13. QA 验收点

1. 整页只有 hero 与 footer 各出现一次 `100,000 USDT` 与主 CTA 按钮
2. 所有数字栏 tabular-nums 命中
3. 无任何裸 hex / `--accent` / `--primary`
4. 绿色仅用于「已解锁」「我的预估奖金」「正向数字」三种合法状态
5. 顶部 Unverified 标记存在
6. 累进时间线 13 ticks + progress bar 结构存在（不要变成阶梯卡片或饼图）
7. 段标题统一 40px 居中
8. My Status 双卡数字字号 48px
9. Leaderboard Top3 大卡的背景大数字（1/2/3）字色为 `--btcc-text-disabled`，不抢戏

## 14. 实现踩坑前置（per figma-plugin-pitfalls.md）

构建前完成 P-PLUGIN-1..7 预检：
- 字体 `Helvetica Neue` 全 weight 预加载（含 700）
- hero 大标题用 `setRangeFills(headLen, headLen+numLen, brand)` 着色 100,000 USDT 子串
- chip / badge / step chip 用 `hug()` helper（AUTO 双轴 + INHERIT）
- 颜色全部走 `hex()` helper，0–1 浮点
- 不调用 `fontFeatures` 或 `setPluginData`

## 15. Figma 文件交付

- 团队：Metaverse HK (`organization::1544657499809167084`)
- 文件名建议：`BTCC × World Cup 2026 — 累进奖池 LP v2`
- 单页面（Page `LP - Desktop 1920`），主 frame 1920 × ~5800
- 顶部加 Unverified 红色 chip（per R-SCOPE-1）

## 16. 后续步骤

1. han 通过后，新建 Figma 文件
2. 按本文档逐模块构建（`use_figma`）
3. 用 `get_screenshot` 取主 frame 全图，对照第 13 节验收
4. 更新 v1 spec 状态为 `superseded-by: v2`（保留历史）
