# LP（落地页 / 活动页）索引

> 10 份 LP 模板族 + 规则文件，覆盖 BTCC LP 全部 9 个已沉淀模板族 + 中奖弹窗 + 奖品 3D 资产 + i18n。
> Figma canvas：`7628:74717 LP活动`（339 顶层节点）。

## 文件清单

| 文件 | 角色 | 主锚点 |
| --- | --- | --- |
| [rules-lp.md](rules-lp.md) | LP 规则（必先选模板 / 共享版式 / 多语种 / H5 / hero 例外 / 抽奖 CTA / 中奖统一 / 文件命名） | — |
| [template-trading-contest.md](template-trading-contest.md) | 交易赛 / 排行榜 | `7752:73942` |
| [template-spinner.md](template-spinner.md) | 转盘抽奖（4-10 等分） | `118680:273993/274021/274052` |
| [template-grid-9.md](template-grid-9.md) | 九宫格抽奖 | `130471:7587` |
| [template-blindbox.md](template-blindbox.md) | 盲盒抽奖（三态：未开 / 开盒中 / 已开） | `123281:58352`、`123412:159584/157328` |
| [template-slot.md](template-slot.md) | 老虎机抽奖 | `128326:3798` |
| [template-scratchcard.md](template-scratchcard.md) | 刮刮卡抽奖 | `130722:132548`、`130846:107320` |
| [template-generic-lp.md](template-generic-lp.md) | 通用 LP（入金任务 / 交易任务 / 奖池） | `120454:274073`、`128160:3792` |
| [modals-reward.md](modals-reward.md) | 中奖 / 未中奖弹窗（统一） | `120960:276861/276865/276899` |
| [assets-3d-prizes.md](assets-3d-prizes.md) | 奖品 3D 资产库 | `118680:274206...274716` |
| [i18n-assets.md](i18n-assets.md) | 多语种 i18n 资产规则（EN/TW/KR/JR） | — |

## 使用顺序

1. **先读** [rules-lp.md](rules-lp.md) → 弄清 8 条 LP 规则。
2. **选模板** → 按 `template-*.md` 选 1-2 个组合。
3. **统一弹窗** → 抽奖结果用 [modals-reward.md](modals-reward.md)。
4. **奖品资产** → 从 [assets-3d-prizes.md](assets-3d-prizes.md) 选取，不自创。
5. **多语种** → 按 [i18n-assets.md](i18n-assets.md) 准备 EN/TW/KR/JR 四语版本。
6. **回到 Web 规则** → [`../rules.md`](../rules.md) R-LP-WEB / R-FONT-WEB。

## 模板组合常见配方

| 业务场景 | 模板组合 |
| --- | --- |
| 世界杯 / 季度赛 | trading-contest（旗舰）+ generic-lp（任务底座）+ modals-reward |
| 节日大促抽奖 | spinner / blindbox（任选 1）+ generic-lp 任务条 + modals-reward |
| 新用户注册礼 | generic-lp（仅入金任务）+ modals-reward 单一中奖 |
| 高奖金老虎机日 | slot 主体 + generic-lp 累积奖池 + modals-reward |
| 周末轻量活动 | scratchcard + 引导卡 + modals-reward |

## 反模式（LP 体系级）

- ❌ 自创 LP 版式（必走 9 个模板族之一）
- ❌ 自创奖品图（必从 assets-3d-prizes.md 取）
- ❌ 自创中奖弹窗（必用 modals-reward.md）
- ❌ 只做单语版（EN/TW/KR/JR 必齐）
- ❌ 不做 H5 镜像
- ❌ Hero 整页都是装饰（hero 之下必须有可操作模块）
