## 1. 准备与基线 grep

- [x] 1.1 在仓库根执行一次基线 grep,收集所有需要替换的旧路径命中点,落盘到本 change 目录下的临时文件 `migration-grep-baseline.txt`(完成 1.x 后删除):覆盖 `references/figma-source.md`、`references/components.md`、`references/tokens.md`、`references/page-matrix.md`、`references/contract-screens.md`、`references/icons.md`、`references/qa.md`、`references/golden-examples.md`、`references/data-format.md`、`references/prompt-evals.md`、`references/implementation-patterns.md`、`docs/btcc/btcc-design-system`、`docs/btcc/btcc-prompt-pack`、`docs/btcc/btcc-generation-governance`
- [x] 1.2 检查仓库根 `README.md`(若存在)是否引用了 `docs/btcc/*` 或旧 references 路径,记入待改清单
- [x] 1.3 检查 `skills/btcc-style-generator/agents/openai.yaml` 的全部路径引用,记入待改清单
- [x] 1.4 通读 `docs/btcc/btcc-design-system.md`、`docs/btcc/btcc-prompt-pack.md`、`docs/btcc/btcc-generation-governance.md`,确认其内容已被现有 11 份 references 完全覆盖,无独有信息;若发现独有内容,把要保留的段落记入待改清单(将吸纳进对应角色文件)

## 2. 抽取 SSOT 规则文件 references/rules.md

- [x] 2.1 新建 `skills/btcc-style-generator/references/rules.md`,顶部加一段"归属判定原则"(D2 中"谁是主要写入触发者"的判定标准)
- [x] 2.2 从 `SKILL.md` Core Rules、`tokens.md` Usage Rules、`components.md` Trading Form Rules、`page-matrix.md` 的 Open Long/Short 段落抽出方向规则,合并去重,只保留一份
- [x] 2.3 收录"dark-first"、"compact spacing / tabular numbers / 不要营销 hero"、"红绿只用于状态与数值"等全局视觉规则
- [x] 2.4 收录命名约定(组件 / token / 文件命名)
- [x] 2.5 收录"未验证范围声明"的占位符与角标格式
- [x] 2.6 在 `rules.md` 中明确声明:本文件是 SSOT,其他 references 文件 MUST 仅以引用形式提及这些规则,不得重复声明
- [x] 2.7 校对 `rules.md` 必须包含 spec R2 列出的所有最低规则项;校对完成后用 Read 自检

## 3. 创建 for-figma-inspect/ 子目录

- [x] 3.1 把 `references/figma-source.md` 内容迁移到 `references/for-figma-inspect/source-anchors.md`,只保留 Figma anchor 信息(file key / page name / 组件集名);移除任何方向规则或 token 数值
- [x] 3.2 把 `references/contract-screens.md` 整体迁移到 `references/for-figma-inspect/contract-screens.md`,内容保持(它本就是 `合约pro` 子屏 node 索引)
- [x] 3.3 把 `references/icons.md` 迁移到 `references/for-figma-inspect/icons.md`,只保留 icon 角色与 Figma 线索;移除任何重复的颜色规则
- [x] 3.4 三份新文件顶部统一加一行 "See `references/rules.md` for global rules.",不在文件内重复声明 SSOT 规则
- [x] 3.5 删除三份对应的旧文件:`figma-source.md`、`contract-screens.md`、`icons.md`(仅指 references 根下的旧文件)

## 4. 创建 for-code-generation/ 子目录 — components 拆三

- [x] 4.1 新建 `references/for-code-generation/components-trading.md`,从旧 `components.md` 抽取 Trading Form / Order Book / TP-SL Bottom Sheet / Market Pair Header 四个段落
- [x] 4.2 新建 `references/for-code-generation/components-account.md`,从旧 `components.md` 抽取 Orders/Positions/Assets Panel / Market Table / Wallet Asset Table 三个段落
- [x] 4.3 新建 `references/for-code-generation/components-global.md`,从旧 `components.md` 抽取 Secondary Button / Bottom TabBar / Product Navigation 三个段落
- [x] 4.4 三份 components-* 文件统一去掉文件内对方向颜色规则的"规定式"声明,只在引用 token 时注明"按 rules.md 与 tokens-colors.md"
- [x] 4.5 校对每份 components-* 文件不超过 ~120 行(spec R4 软约束);超出时在文件顶部加一行说明
- [x] 4.6 删除旧 `references/components.md`

## 5. 创建 for-code-generation/ 子目录 — tokens 拆二

- [x] 5.1 新建 `references/for-code-generation/tokens-colors.md`,从旧 `tokens.md` 抽取 Collections 表、Semantic Tokens 表、Primitive Gray Ramp 表、与颜色相关的 Usage Rules
- [x] 5.2 新建 `references/for-code-generation/tokens-size-typography.md`,从旧 `tokens.md` 抽取 Size Tokens(Radius / Control Heights / Spacing)、Typography Tokens、与尺寸/排印相关的 Usage Rules
- [x] 5.3 两份 tokens-* 文件去掉重复声明的方向规则,改为"颜色方向规则见 `rules.md`"
- [x] 5.4 删除旧 `references/tokens.md`

## 6. 创建 for-code-generation/ 子目录 — pages 拆二

- [x] 6.1 新建 `references/for-code-generation/pages-contract.md`,从旧 `page-matrix.md` 抽取 `合约pro` 已验证页面规范
- [x] 6.2 新建 `references/for-code-generation/pages-other.md`,从旧 `page-matrix.md` 抽取其余 7 类未验证页面规范,文件顶部和每个 section 顶部都加显著"未验证 / Unverified"角标
- [x] 6.3 `pages-other.md` 内按"风险等级"用 section 区分(完全未见 vs 部分见过 vs Figma 有节点但未对齐组件),沿用 design Open Question 3 的暂行分组方式
- [x] 6.4 删除旧 `references/page-matrix.md`

## 7. 创建 for-review-and-qa/ 子目录

- [x] 7.1 把 `references/qa.md` 迁移到 `references/for-review-and-qa/qa.md`;凡是 qa checklist 涉及方向颜色 / dark-first / tabular 等规则的条目,改写为"参照 `rules.md` 第 X 条"形式,不再独立声明
- [x] 7.2 把 `references/golden-examples.md` 迁移到 `references/for-review-and-qa/golden-examples.md`,同样去除自有"规定式"语句
- [x] 7.3 把 `references/data-format.md` 迁移到 `references/for-review-and-qa/data-format.md`
- [x] 7.4 删除三份对应的旧文件

## 8. 创建 for-prompt-design/ 子目录

- [x] 8.1 把 `references/prompt-evals.md` 迁移到 `references/for-prompt-design/prompt-evals.md`,删除其中可能存在的颜色规则列表或 components 复制片段
- [x] 8.2 把 `references/implementation-patterns.md` 迁移到 `references/for-prompt-design/implementation-patterns.md`
- [x] 8.3 删除两份对应的旧文件

## 9. 重写 SKILL.md

- [x] 9.1 删除 SKILL.md 现有 Core Rules 整段(规则全部下沉到 `rules.md`),替换为单行 "Read `references/rules.md` first; it is the single source of truth for BTCC golden rules."
- [x] 9.2 删除现有 Reference Router 11 行平铺映射
- [x] 9.3 在 Overview 之后(或与 Required Workflow 相邻位置)新增 "Task → Files" 反向索引表,至少覆盖 spec R7 与 design D3 列出的 8 类调用,使用 design D3 的精确文件清单
- [x] 9.4 在反向索引表上方加一行 "Path Migrated" 提示,列出 5 条最高频旧→新路径映射(components / tokens / page-matrix / figma-source / docs/btcc)
- [x] 9.5 删除 SKILL.md 中对 `docs/btcc/btcc-design-system.md` / `btcc-generation-governance.md` / `btcc-prompt-pack.md` 的引用段落
- [x] 9.6 保留并更新 Figma Plugin Workflow / Original Figma Anchors / Common Mistakes / Completion Gate 段落,把其中对旧 `references/*` 路径的引用替换为新路径
- [x] 9.7 用 Read 自检 SKILL.md;反向索引表必须能让"改下单按钮颜色"映射到 `rules.md` + `for-code-generation/components-trading.md` 且不指向 `page-matrix.md`(spec R7 第一个 scenario)

## 10. 删除冗余长文档

- [x] 10.1 删除 `docs/btcc/btcc-design-system.md`
- [x] 10.2 删除 `docs/btcc/btcc-prompt-pack.md`
- [x] 10.3 删除 `docs/btcc/btcc-generation-governance.md`
- [x] 10.4 若 `docs/btcc/` 目录变空,一并删除该目录
- [x] 10.5 若仓库根 `README.md` 引用了上述路径,改写或移除链接

## 11. 同步外围引用

- [x] 11.1 更新 `skills/btcc-style-generator/agents/openai.yaml` 中所有旧 references 路径为新路径
- [x] 11.2 检查 `scripts/btcc_qa_lint.py` 中是否含有路径引用(只改路径,不动硬编码规则字符串,见 D6)
- [x] 11.3 检查 `assets/` 下文件是否含有路径引用(预期无,确认即可)
- [x] 11.4 检查 openspec 其他文件(`openspec/changes/restructure-btcc-skill-by-role/` 自身除外)是否引用旧路径,若有则修正

## 12. 验证

- [x] 12.1 重跑 1.1 中的 grep,要求所有命中数为 0(`scripts/btcc_qa_lint.py` 中硬编码的规则字符串若被命中,确认仅为规则字面量而非路径引用,可豁免)
- [x] 12.2 执行 `openspec validate restructure-btcc-skill-by-role --strict`,要求通过
- [x] 12.3 执行一次 `python skills/btcc-style-generator/scripts/btcc_qa_lint.py skills/btcc-style-generator/`(或现成的演示输出)作为回归冒烟,确认无新增 false positive
- [x] 12.4 用反向索引表对 8 类任务做 dry-run:对每一类调用,人工或 LLM 按 SKILL.md 单跳跳转,验证文件清单可命中且无遗漏
- [x] 12.5 列出最终 `references/` 树,确认刚好 5 个直接子项(`rules.md` + 4 个角色目录),无散落 .md(spec R1)
- [x] 12.6 抽样核对:在 `for-review-and-qa/qa.md` 中搜索字面量 "Open Long",应为引用形式而非"规定式"语句(spec R5 第二个 scenario)
- [x] 12.7 删除 1.1 中产生的临时基线文件 `migration-grep-baseline.txt`

## 13. 提交

- [x] 13.1 单次 commit 完成全部移动 / 拆分 / 删除 / 引用更新(D5 约束),commit message 显式列出 BREAKING 路径变更摘要
- [x] 13.2 在 commit message body 中粘贴 12.1 grep 结果(0 hits)与 12.2 validate 结果作为证据
