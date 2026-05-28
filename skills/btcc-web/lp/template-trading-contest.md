# LP 模板族 · 交易赛 / 排行榜（Trading Contest）

> 主锚点：`7752:73942 jjj交易赛`（Web 1920 × 长高度）
> 关联：[`../../specs/2026-05-28-worldcup-lp/`](../../../openspec/) 世界杯 LP v2 已采用此模板。

## 用途

按交易量 / 盈亏 / 累计奖池等维度组织的**比赛活动**：
- 报名 → 交易期 → 排名结算 → 发奖
- 适合：世界杯、季度赛、新币挑战、合约 / 现货分赛道

## 模块清单（自上而下）

```
1. Hero 1920 × 760
   - 活动名（大字，2D 或 3D，可矢量化）
   - 副标 / Tagline
   - 倒计时（活动开始 / 进行中 / 已结束）
   - 主 CTA "立即报名 / 立即参赛"
   - 装饰：奖杯、奖金堆、品牌光效

2. 我的状态卡 1200 × 160-200
   - 已报名状态：徽章 + 当前排名 + 距上一名差额 + "继续交易"按钮
   - 未报名：CTA "立即报名"
   - 已结束：奖金到账状态 + "查看历史成绩"

3. 奖池 / 奖金分布 1200 × N
   - 渐进解锁的奖池：随交易量门槛累积奖金
   - 奖金分布表：1-10 名奖金（金 / 银 / 铜 + 后续）

4. 任务 / 进度 1200 × N
   - 当前周期任务（每日交易量 / 每周累计 / 邀请好友）
   - 进度条 + 已领奖品
   - 链接：components/alert.md / progress

5. 排行榜 1200 × N（核心）
   - 顶部 3 名特殊视觉（金 / 银 / 铜领奖台）
   - 4-100 名表格：排名 / 用户（脱敏）/ 交易量 / 奖金
   - 我的排名条置顶（即使不在前 100）
   - Tab 切换：合约 / 现货 / 综合
   - 分页 32×32 r19/r25

6. 规则 long-form 1200
   - 活动时间、参赛资格、计算口径、奖金发放、风险声明

7. Footer 1920
```

## 几何 / 颜色

| 区域 | 高 | 关键 |
| --- | --- | --- |
| Hero | 760 | 主标 Lato Black 64-96 / 副标 24 |
| 倒计时 | 内嵌 hero | 4 段 dd / hh / mm / ss，每段卡 80×80 r4，**tabular-nums** |
| 我的状态卡 | 160-200 | r4 / bg-card / 内嵌 chip 排名 |
| 奖池卡 | 240-360 | 大数字 `$XXX,XXX`，Lato Black 48 + tabular-nums |
| 排行榜表 | 行 56 | 头像 32 + 用户名脱敏 + 数字 tabular-nums |
| 排行榜顶 3 | 280 高领奖台 | 金 / 银 / 铜带渐变光效，带奖金数 |

## 关键模块 → 组件

| 模块 | 组件文件 | 备注 |
| --- | --- | --- |
| 主 CTA | [`../components/button-primary.md`](../components/button-primary.md) | pill 100 / h48 / 或 hero 内大尺寸 h64 |
| 倒计时 | inline | tabular-nums 必加 |
| 排名 chip | [`../components/button-secondary-sm.md`](../components/button-secondary-sm.md) 选中变体 | h28 r29 |
| 排行榜表 | [`../components/table.md`](../components/table.md) | 行高 56，含 32 头像 + 用户名脱敏，sticky 我的排名行 |
| Tab（合约/现货/综合） | [`../components/tab.md`](../components/tab.md) 一级 | h40 |
| 分页 | [`../components/pagination.md`](../components/pagination.md) | PingFang SC Reg 14 |
| 报名成功反馈 | [`../components/dialog.md`](../components/dialog.md) 480 | success 绿 icon |
| 状态 alert | [`../components/alert.md`](../components/alert.md) | 活动状态 |

## 状态机（必备）

| 状态 | 主 CTA | 我的状态卡 |
| --- | --- | --- |
| 未开始 | "敬请期待" disabled + 倒计时 | 提前预告 |
| 报名期 | "立即报名" 一级 brand | "报名后开始累计" |
| 报名期 + 已报名 | "立即交易" 一级 brand | "已报名 #XXXX" |
| 进行中 | "继续交易" 一级 brand | 当前排名 + 差额 |
| 进行中 + 未报名 | "立即报名" 一级 brand | "尚有 N 天可报名" |
| 已结束 | "查看历史" outline | 最终排名 + 奖金到账 |

## H5 差异

- Hero 缩到 375 × 480-600。
- 排行榜变成卡片列表，每张卡 343 × 96，含排名 / 用户 / 数字。
- 顶 3 领奖台横排压缩为 343 × 200。
- 主 CTA 底部 sticky 满宽 pill 100 / h48。

## 反模式

- ❌ 排行榜不做"我的排名置顶"（用户必须能立刻看到自己的位置）。
- ❌ 倒计时不加 tabular-nums（数字会跳）。
- ❌ 奖池数字不加 tabular-nums。
- ❌ 状态机不全（最少 6 种状态都要有）。
- ❌ 报名成功用 toast（应是 dialog 480 + 礼花 success）。
- ❌ Hero 大字图片化但不做矢量化（多语种切换时排版崩溃）。
