---
name: BTCC 世界杯活动 LP（Web 桌面版）
date: 2026-05-28
platform: web
status: design-approved
unverified-marker: true   # 按 rules.md R-SCOPE-1，营销 LP 不在已验证 Figma 范围
target-figma:
  team: Metaverse HK (organization::1544657499809167084)
  file: 待 use_figma 创建
---

# BTCC 世界杯活动 LP（Web 桌面版）— 设计文档

## 1. 目标与约束

- **场景**：世界杯期间的拉新 + 入金活动落地页，主 CTA「立即注册领奖」。
- **平台**：Web 桌面（断点 1024 / 1440 / 1556 / 1920，主响应宽度 1200px 内容区）。
- **机制**：100,000 USDT 平分奖池，新用户按"注册 / 入金 / 交易"累计份额瓜分。
- **风格**：BTCC 主站延续，dark-first，操作型语言替代营销型 hero。

### 与 BTCC 规则的边界

| 规则 | LP 内的处理 |
| --- | --- |
| `R-LAYOUT-1`（不要 marketing hero on operational surfaces） | 本页**是**营销 LP，hero 允许，但视觉语言用"奖池行情卡"代替全屏球场图 |
| `R-LAYOUT-2`（密排、tabular-nums、克制卡片） | 严格遵守 |
| `R-COLOR-1`（多/空方向色） | 不涉及（无交易控件） |
| `R-COLOR-2`（颜色即状态） | 严格遵守，绿色仅用于"已完成 / 状态为成功"，不做装饰 |
| `R-NAME-1`（`--btcc-*` token） | 全部 token 使用 `--btcc-*`，不引入 `--accent` 或裸 hex |
| `R-SCOPE-1`（未验证标记） | 页面顶部加 `Unverified / 未验证 — Source: BTCC-style convention; not in verified Figma metadata pass.` |

## 2. 整体框架

- 容器：1200px 居中，左右各 24px gutter
- 背景：`--btcc-bg-primary` (`#0C0F12`)
- 模块间距：80px（活动页可比交易页松一档）
- 字体：`--btcc-font-family-sans`
- 数字列：`font-variant-numeric: tabular-nums`，右对齐

## 3. 模块清单（按从上到下顺序）

```
[Hero — 两栏：左标题/CTA + 右奖池行情卡]
  ↓
[三步领奖 — 三个 step 卡片横排]
  ↓
[实时参与名单 + 奖池分配预览 — 双栏，模拟交易页 RecentTrades+OrderBook]
  ↓
[活动规则 — 双栏 list]
  ↓
[底部 CTA — 倒计时 + 主按钮]
```

## 4. Hero 区

**整体：** 两栏 grid，左 720px / 右 440px，列间距 40px，纵向居中对齐，整段高度约 480px。

**左栏：**
- 顶部 chip：`WORLD CUP × BTCC`
  - 12px / `--btcc-font-weight-medium` / `--btcc-brand`
  - 背景 `--btcc-brand-alert`，padding `4px 10px`，圆角 `--btcc-radius-tag` (4px)
- 主标题（两行）：
  - 第一行：`瓜分 100,000 USDT` — 56px / 700 / 行高 64px
    - "100,000 USDT" 子串使用 `--btcc-brand` 蓝；其余 `--btcc-text-primary`
  - 第二行：`世界杯狂欢奖池` — 56px / 700 / `--btcc-text-primary`
- 副文案：`注册并入金即按比例瓜分，无需抽签` — 14px / `--btcc-text-secondary`
- 主 CTA：`立即注册领奖`
  - 高 48px、左右内边距 32px、圆角 `--btcc-radius-control` (6px)
  - 背景 `--btcc-brand`，press 态 `--btcc-brand-pressed`
  - 文字 `--btcc-text-anti` (`#FFFFFF`)，14px / 500
- 次 CTA：`查看活动规则 →`
  - 14px / `--btcc-text-secondary`，hover `--btcc-text-primary`，无背景

**右栏（奖池行情卡）：**

视觉语言模仿交易页右侧 `Order Book` 卡，但内容是奖池数据。

- 卡片：宽 440px、高约 320px、padding 24px
- 背景 `--btcc-bg-card` (`#13171B`)
- 边框 1px `--btcc-divider-container` (`#2C3642`)
- 圆角 `--btcc-radius-card` (12px)

卡内 4 行 row（行高 56px，行间 1px `--btcc-divider-primary` 分隔），每行结构 `label ······ value`，label 左对齐 12-14px secondary，value 右对齐 tabular-nums：

| Label | Value | 数字色 |
| --- | --- | --- |
| 奖池总额 | `100,000 USDT` | `--btcc-brand` 24px |
| 已参与人数 | `12,486` | `--btcc-text-primary` 20px |
| 剩余时间 | `42d 17:23:08` | `--btcc-text-primary` 20px tabular-nums |
| 当前预估个人收益 | `≈ 8.0 USDT` | `--btcc-success` 20px |

> 设计意图：用户第一眼看到的不是"装饰图"，而是"奖池作为可被精确计算的数字"，与 BTCC 主站的数据感统一。

## 5. 三步领奖

**整体：** 标题 `三步领奖` 一行（16px / `--btcc-text-secondary`，左对齐），下接 3 张卡横排。

**卡片：** 380px × 220px，间距 20px。

```
背景：--btcc-bg-card
边框：1px --btcc-divider-container
圆角：--btcc-radius-card (12px)
padding：24px
```

**卡内布局：**
- 左上 watermark 数字：`01` `02` `03`
  - 48px / 700 / `--btcc-text-disabled` (`#3E4A59`)（淡化，不抢戏）
  - 绝对定位，距左 24px、距上 16px
- 右上状态徽章：
  - 待完成：`待完成` — 12px / `--btcc-text-secondary`，背景 `--btcc-fill-tag`，4px 圆角，padding `2px 8px`
  - 已完成：`✓ 已完成` — 12px / `--btcc-success`，背景 `--btcc-success-alert`，同尺寸
- 主标题（18px / `--btcc-text-primary` / 500）
- 副说明（12px / `--btcc-text-secondary`）
- 分隔线 1px `--btcc-divider-primary`，上下 margin 12px
- 权益小标 `解锁权益` — 12px / `--btcc-text-secondary`
- 权益值 — 14px / `--btcc-brand` / 500
- CTA 按钮 — 36px 高、宽度 fit-content、内边距 20px
  - 主按钮（Step 01）：`--btcc-brand` 填充 + `--btcc-text-anti`
  - 次按钮（Step 02/03 在 Step 01 未完成时）：`--btcc-button-secondary-bg` + `--btcc-text-primary`

**三张卡内容：**

| | 标题 | 说明 | 解锁 | CTA |
| --- | --- | --- | --- | --- |
| 01 | 注册 BTCC | 完成手机或邮箱注册 | +1 份基础奖池资格 | 立即注册 |
| 02 | 完成首次入金 | 入金 ≥ 100 USDT | +3 份奖池资格 | 去入金 |
| 03 | 完成首笔合约交易 | 名义价值 ≥ 50 USDT | +6 份奖池资格 | 去交易 |

## 6. 实时参与名单 + 奖池分配预览

**整体：** 两栏并排，各 580px 宽，列间距 40px。视觉对应交易页 `Recent Trades + Order Book` 双栏。

**通用规则：**
- 不使用整块卡片背景，仅用 1px `--btcc-divider-primary` 分行
- 标题区高 36px，左对齐 16px / `--btcc-text-primary` / 500，右侧附状态徽标
- 表格 row 高 32px（密排）

### 6.1 左栏：实时参与（Live Feed）

- 标题：`实时参与` + 右上小绿点 + `Live` 文字（`--btcc-success` 12px）
- 列头：`用户` `状态` `贡献份额` `时间`
  - 12px / `--btcc-text-secondary`，列头与正文之间 1px `--btcc-divider-container`
- 数据 8 行（mock 数据，前端用伪流式：每 3-5 秒从顶部插入 1 行下推）
- 列对齐：用户左 / 状态左 / 份额右 / 时间右
- 状态色：
  - `已注册` → `--btcc-text-secondary`
  - `已入金` → `--btcc-brand`
  - `已交易` → `--btcc-success`
- 用户名脱敏：`u***982`
- 时间相对：`12s ago` / `1m ago`

### 6.2 右栏：奖池分配预览

```
当前预估人均收益                   ≈ 8.01 USDT      ← 28px / brand / tabular-nums
─────────────────────────────────────
若额外 1,000 人加入                ≈ 7.42 USDT      ← 14px / text-primary
若额外 5,000 人加入                ≈ 5.72 USDT
若额外 10,000 人加入               ≈ 4.45 USDT
─────────────────────────────────────
我已贡献的份额                      0 份
我的预估收益                       — USDT     [ 加入 ]
```

- 顶部"当前预估"行高 64px，单独显示
- 阶梯三行高 32px 密排
- 底部"我已贡献"两行 + 一个 36px 高 brand 小按钮 `加入`
- 不画曲线图、不放金币 3D 图

## 7. 活动规则

**整体：** 标题 `活动规则`（16px / `--btcc-text-primary` / 500，左对齐），下方两栏 list。

**左栏 — 份额规则：**
```
· 注册并完成手机/邮箱验证                          +1 份
· 累计入金 ≥ 100 USDT                            +3 份
· 完成首笔合约交易（≥ 50 USDT 名义价值）             +6 份
· 单用户最高累计 10 份
```

**右栏 — 奖励发放：**
```
· 奖池总额 100,000 USDT，按总份额平分
· 活动结束后 7 个工作日内发放至现货账户
· 每用户实际收益 = (个人份额 / 全网总份额) × 100,000
· 反作弊：同 IP / 同设备 / 同 KYC 视为单账号
```

- 文字 14px / `--btcc-text-secondary`，行高 1.7
- 数字（`100,000 USDT`、`+6 份` 等）用 `--btcc-text-primary` 加粗
- 项目符号统一用 `·` 中点（避免装饰性 emoji 或彩色点）
- 底部小字一行：`活动最终解释权归 BTCC 所有 · 详见用户协议 →`
  - 12px / `--btcc-text-disabled`

## 8. 底部 CTA

```
                  距活动结束还剩
                42d 17:23:08
                ─────────────
            [    立即注册领奖    ]
                  已有 12,486 人参与
```

- 整段居中，纵向间距：标题 → 倒计时 16px → 分隔线 → CTA 24px → 参与人数 16px
- 标题 `距活动结束还剩` — 14px / `--btcc-text-secondary`
- 倒计时 — 32px / `--btcc-brand` / 500 / tabular-nums
- 分隔线 80px 长，1px `--btcc-divider-container`
- CTA 按钮 — 64px 高、240px 宽、`--btcc-brand` 填充、14px / `--btcc-text-anti` / 500
- 参与人数 — 12px / `--btcc-text-secondary`，`12,486` 子串用 `--btcc-text-primary`

**不重复奖池数字。** 奖池金额仅出现在 hero 一次，避免视觉权重稀释。

## 9. Token 速查（仅本 LP 用到的）

- **背景**：`--btcc-bg-primary` / `--btcc-bg-card`
- **文字**：`--btcc-text-primary` / `--btcc-text-secondary` / `--btcc-text-disabled` / `--btcc-text-anti`
- **品牌色**：`--btcc-brand` / `--btcc-brand-pressed` / `--btcc-brand-alert`
- **状态色**：`--btcc-success` / `--btcc-success-alert`
- **分隔/边框**：`--btcc-divider-primary` / `--btcc-divider-container`
- **圆角**：`--btcc-radius-tag` (4px) / `--btcc-radius-control` (6px) / `--btcc-radius-card` (12px)
- **填充**：`--btcc-fill-tag` / `--btcc-button-brand-bg` / `--btcc-button-secondary-bg`

## 10. Figma 文件交付

- 目标 team/org：`Metaverse HK` (`organization::1544657499809167084`)
- 文件名（建议）：`BTCC × World Cup 2026 — 拉新瓜分奖池 LP`
- 单页面（Page 名 `LP - Desktop 1440`），主 frame 1440 × 实际高度（约 2200px）
- frame 内由上至下排列 5 个分组（`Hero` / `Steps` / `Live + PoolPreview` / `Rules` / `Footer CTA`）
- 顶部加一个 `Unverified` 红色 chip 文本节点（per R-SCOPE-1）

## 11. QA 验收点

1. 整页只有 hero 区出现一次 `100,000 USDT`（避免视觉重复）
2. 所有数字栏 `font-variant-numeric: tabular-nums` 命中
3. 无任何裸 hex / `--accent` / `--primary`
4. 绿色仅用于"已完成 / 已交易 / 实时点亮 / 预估收益"四种合法状态
5. 无球场/奖杯渐变背景图（违反 BTCC 视觉一致性）
6. 顶部 Unverified 标记存在
7. CTA 按钮只在 hero 与 footer 出现两次（避免按钮泛滥）

## 12. 后续步骤（不属于本设计文档）

1. 在 Metaverse HK 团队下用 `create_new_file` 新建文件
2. 用 `use_figma` 按本文档逐模块构建节点
3. 用 `get_screenshot` 取回 frame 截图，对照本文档第 11 节验收
4. 必要时迭代视觉，迭代后再次截图复盘
