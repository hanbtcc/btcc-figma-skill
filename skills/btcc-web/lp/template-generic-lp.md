# LP 模板族 · 通用 LP（Generic）

> 主锚点：
> - `120454:274073 LP通用模版`
> - `120858:302678 LP模版-通用模版`
> - `128160:3792 LP通用模版`
> - `127864:236015 LP通用模版1`

## 用途

**不带抽奖**的 LP 活动，专注于：
- **入金任务 / 交易任务**：完成阶梯任务领奖
- **奖池累积**：随累计交易量 / 入金额涨奖池
- **空投 / 注册礼**：完成简单任务领固定奖励

是 LP 的"基础底座"，其他抽奖模板（spinner / blindbox / slot 等）也常常**叠加在通用 LP 上**当作奖励出口。

## 模块清单

```
1. Hero 1920 × 760
   - 活动名 + 副标 + 倒计时
   - 主 CTA（"立即参与" / "去入金" / "去交易"）

2. 我的状态卡 1200 × 200
   - 当前进度：已入金 / 已交易 / 已邀请人数
   - 已领奖品 / 累计奖金
   - "查看奖励历史" outline

3. 任务区 1200 × N（核心）
   3.1 入金任务
       - 表格：金额阈值 / 奖励 / 状态（未达 / 进行中 / 已领）
       - 每行尾："去入金" 一级 button h28 / 或"领取" / 或 "已领"
   3.2 交易任务
       - 表格：交易量阈值 / 奖励 / 状态
       - 每行尾："去交易" / "领取" / "已领"
   3.3 邀请任务（可选）
       - 邀请链接 + 复制按钮
       - 已邀请数 / 阶段奖励
   
4. 奖池卡 1200 × 360（如有累积奖池）
   - 大数字 jumbo 48 + tabular-nums
   - 解锁条件 progress
   - 当前阶段 / 下一阶段奖励

5. 规则 long-form
6. Footer
```

## 任务表格结构

| 列 | 内容 | 样式 |
| --- | --- | --- |
| 阶段 | T1 / T2 / T3 | chip 28h |
| 阈值 | "入金 100 USDT" | 14px primary |
| 奖励 | "10 USDT 体验金" | 14px brand color |
| 进度 | "78 / 100" + 进度条 | tabular-nums + 高 4px progress |
| 状态 | 未达 / 进行中 / 已领 | secondary / brand / success |
| 操作 | 按钮 | h28 r29 |

行高 64-80（含进度条）。

## 关键模块 → 组件

| 模块 | 组件文件 | 备注 |
| --- | --- | --- |
| 主 CTA | [`../components/button-primary.md`](../components/button-primary.md) | pill 100 / h48 |
| 行内"去入金" / "领取" | [`../components/button-secondary-sm.md`](../components/button-secondary-sm.md) | h28 r29，brand 配色 |
| "已领" 状态 | [`../components/button-secondary-sm.md`](../components/button-secondary-sm.md) disabled | h28 灰 |
| 任务进度 | （inline progress 4h r2 + tabular-nums） | |
| 奖池数字 | （inline Lato Black 48 + tabular-nums） | |
| 已领奖励反馈 | [`modals-reward.md`](modals-reward.md) | |
| 规则展开 | [`../components/alert.md`](../components/alert.md) info | 折叠展开 |
| 邀请链接 input | [`../components/input.md`](../components/input.md) readonly + 复制 | |

## 任务状态机（每条任务）

| 状态 | 操作按钮 | 进度条 |
| --- | --- | --- |
| 未达成 | "去入金 / 去交易" h28 brand | 显示当前进度 |
| 已达成未领 | "领取" h28 brand | 100% / brand |
| 已领取 | "已领" h28 disabled | 100% / success |
| 已过期 | "已过期" h28 disabled 灰 | 灰 |

## H5 差异

- 任务表格变堆叠卡：每张任务卡 343 × 160 r4。
- 状态、进度、按钮垂直堆叠。
- Hero 缩到 375 × 480-600。
- 主 CTA 底部 sticky。

## 反模式

- ❌ 任务表格不显示进度条（用户无法判断离下一阶段差多远）。
- ❌ "去入金"和"领取"用同一个文案（不同状态文案必须区分）。
- ❌ 已领状态不灰化（用户会重复点）。
- ❌ 奖池数字不加 tabular-nums。
- ❌ 邀请链接不带复制按钮（用户复制麻烦）。
- ❌ 把通用 LP 当成"什么都装"的容器（应只装入金 / 交易 / 邀请三大任务，抽奖另起 spinner / blindbox 模板）。
