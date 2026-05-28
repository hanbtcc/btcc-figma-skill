## Context

当前 `skills/btcc-style-generator/` 在调用层面表现为"路由信息分散、规则多源、单文件混合多场景"三类问题。SKILL.md 的 Reference Router 只列出 11 个平铺文件名,LLM 无法在 prompt 时间内判断最小读取集合;同一条规则(以 `Open Long`/`Open Short` 颜色绑定为典型,grep 命中 14 处)在 references 与 `docs/btcc/*` 中重复出现,任何单点修订都需要跨文件同步,极易产生静默不一致。`components.md` (193) / `tokens.md` (168) / `page-matrix.md` (185) 内部按"组件大类 / token 大类 / 页面合集"切分,但调用方的真实意图通常落在角色而非分类上,导致 LLM 倾向于全量加载或漏读。

`assets/` 与 `scripts/btcc_qa_lint.py` 路径稳定,本次重构不涉及。`openspec/specs/` 当前为空,无既有 capability 需要迁移,因此本次主要是 skill 自身的结构契约从无到有。

## Goals

- 让 LLM 调用 skill 时,从"任务意图 → 需要读哪些文件"在 SKILL.md 单跳即可解决,不再需要 grep references。
- 让黄金规则(颜色语义、命名、未验证范围声明等)只在一份文件里维护,其他文件最多引用、不复制。
- 让单文件长度与角色边界对齐,避免"为了改一个表格要打开 200 行不相关内容"。

## Non-Goals

- 不重写规则本身,只搬运与去重;若发现规则冲突,本次只标注,不在 design 阶段裁决。
- 不调整 `assets/` 与 `scripts/` 的路径与内容。
- 不引入新的 capability spec,`openspec/specs/btcc-skill-structure/` 的 spec.md 由后续 tasks 承担,design 只约束骨架。
- 不为旧路径保留 stub,接受一次性 BREAKING(详见 D4 / D5)。

## Decisions

### D1 按"角色"而非"组件类型"或"页面类型"分目录

选用 `for-figma-inspect / for-code-generation / for-review-and-qa / for-prompt-design`。

- 备选 A(被否决):按组件类型分(`components/ tokens/ pages/ icons/ qa/ prompts/`)。这是当前实质结构的微调,无法解决"同一份 `tokens.md` 既给 figma-inspect 用又给 code-generation 用"的复用歧义,LLM 仍需读全文判断哪段适用。
- 备选 B(被否决):按页面类型分(`contract/ account/ global/`)。颗粒度太细,`qa.md`、`prompt-evals.md`、`figma-source.md` 这类横切文件无处安放,要么强行重复要么塞进 `global/`,反而恶化。
- 选定理由:角色直接对应 LLM 的 prompt 入口意图,SKILL.md 的反向索引只需要"任务 → 角色 → 文件"两跳,且每个角色目录下的文件数控制在 3 个左右,接近一次性可加载。

### D2 SSOT `references/rules.md` 的边界

`rules.md` 内必须且只能包含:

- 颜色语义绑定(`Open Long` = brand / `Open Short` = error;盈利绿 / 亏损红的语义方向)
- 命名约定(组件命名、token 命名、文件命名)
- 全局禁止项(禁止生成的视觉样式、禁止杜撰未验证页面)
- 未验证范围声明的写法约定(占位符格式、必须出现的角标)
- 规则之间的优先级与冲突解法

不属于 SSOT、必须留在角色目录的:

- 具体 token 数值(放 `for-code-generation/tokens-colors.md` 与 `tokens-size-typography.md`)
- 组件解剖(各 anatomy 表、props 表、状态表)
- 页面布局/截图引用(`pages-contract.md` 等)
- Figma 节点 anchor(`for-figma-inspect/source-anchors.md`)
- QA 检查项的具体清单(放 `for-review-and-qa/qa.md`,但其断言依据必须 link 回 `rules.md`)

判断规则:如果一条内容被改一次就需要在 ≥2 个角色文件里同步,它属于 SSOT;如果它只服务于某一个角色的产出动作,就留在角色目录。

### D3 SKILL.md "任务 → 文件清单" 反向索引最少覆盖

确认覆盖 proposal 列出的 8 类调用,并显式约束每行的格式 `任务 → 角色目录 → 文件 1, 文件 2, ...(rules.md 默认必读不重复列出)`:

1. 生成合约 pro 页面 → for-code-generation → pages-contract, components-trading, components-global, tokens-colors, tokens-size-typography
2. 改下单按钮 / 表单 → for-code-generation → components-trading, tokens-colors
3. 加杠杆 picker → for-code-generation → components-trading, tokens-size-typography
4. 审查模型输出 → for-review-and-qa → qa, golden-examples, data-format
5. 写 / 改 prompt → for-prompt-design → prompt-evals, implementation-patterns
6. 看 Figma 节点定位 → for-figma-inspect → source-anchors, contract-screens, icons
7. 改 token 值 → for-code-generation → tokens-colors 或 tokens-size-typography(二选一)
8. 加新页面(未验证) → for-code-generation → pages-other(必须带"未验证"角标)+ for-figma-inspect → source-anchors

`rules.md` 在每条调用中默认必读,以"前置必读"形式在表头声明一次,行内不再重复占位,降低 LLM 噪声。

### D4 `docs/btcc/*` 三份长文档处置:直接删除,不留 stub

- 备选(被否决):保留为 1-2 行的 stub redirect。问题在于 stub 仍是规则的"看似存在的入口",grep 时会被 LLM 当成可读源,反而延长收敛周期;且 stub 维护成本与彻底删除相当。
- 选定:直接删除三份文件。仓库历史可通过 git log / git show 追溯,真正需要"散文版背景"的人可以回溯到删除前的 commit。
- 影响面:仓库根 `README.md` 若引用这三份文件,在 tasks 阶段一并改写或移除链接,落入 R1 的检查范围。

### D5 旧路径迁移:Write 新 + Delete 旧,而非 `git mv`

- 这次大部分文件不是单纯 rename,而是同时拆分(`components.md` 一拆三、`tokens.md` 一拆二、`page-matrix.md` 一拆二)与重命名(`figma-source.md` → `source-anchors.md`)。`git mv` 在拆分场景下不能保留 blame 关联,价值不大。
- 统一用 Write 新文件 + Delete 旧文件,在同一 commit 内完成,保证 HEAD 任意时刻仓库一致。
- 引用更新顺序:先扫一遍仓库内所有出现旧路径的位置(SKILL.md / agents/openai.yaml / 仓库根 README / scripts 注释 / 本次 design 之外的 openspec 文档),用新路径替换;然后在同一 commit 删旧文件。
- 单次 commit 完成,不做中间态;commit message 显式列出 BREAKING 路径变更,便于外部使用者从 git log 一眼看到。

### D6 `scripts/btcc_qa_lint.py` 中硬编码规则的处理:保留

脚本内的 "Open Long=brand / Open Short=error" 不是文档冗余,而是规则的运行时执行体。SSOT 的边界是"人和 LLM 读的源",可执行代码是 SSOT 的下游消费者,允许其再次声明同一约束(否则就要在脚本里反向解析 markdown,得不偿失)。

约束:`rules.md` 与 `btcc_qa_lint.py` 必须保持语义一致;若未来扩展规则,先改 `rules.md`,再同步脚本。该约束写入 `Implement.md` 而不是 design,本设计只声明立场。

## Risks / Trade-offs

- **R1 [Risk] 断链风险**:`SKILL.md` 自身、`agents/openai.yaml`、仓库根 `README.md`、`scripts/` 注释、其他 openspec 文档、外部用户的 prompt 模板可能硬编码旧 references 路径。  
  Mitigation:tasks 阶段第一步在仓库根做一次 `grep -R "references/components.md\|references/tokens.md\|references/page-matrix.md\|references/figma-source.md\|references/contract-screens.md\|references/icons.md\|references/qa.md\|references/golden-examples.md\|references/data-format.md\|references/prompt-evals.md\|references/implementation-patterns.md\|docs/btcc/btcc-design-system\|docs/btcc/btcc-prompt-pack\|docs/btcc/btcc-generation-governance"`,把命中点全部列入待改清单;迁移完成后再跑同一 grep,要求零命中作为收尾门槛。外部模板的断链不在仓库可控范围,接受一次性 BREAKING 并在 proposal 已声明。

- **R2 [Risk] LLM 调用者短期内仍记得旧路径**:已经在使用本 skill 的 prompt / agent 链路可能继续按旧名读文件,首跳必失败。  
  Mitigation:SKILL.md 顶部新增"Task → Files"索引表本身就是新入口的强信号;在该表上方加一条简短"Path Migrated"提示行,列出 5 条最高频旧→新路径映射(components / tokens / page-matrix / figma-source / docs/btcc),让 LLM 在第一次读 SKILL.md 时就能拿到映射。该提示行设为临时,后续阶段可清理(在 Open Questions 中跟踪)。

- **R3 [Risk] 角色边界存在交叉地带**:典型如 `tokens-colors.md` 既被 code-generation 消费(直接生成 CSS 变量)又被 figma-inspect 消费(对照 Figma variables 命名);`qa.md` 也间接读 tokens 做颜色比对。  
  Mitigation:**消费者多 ≠ 归属多**。归属判定标准为"谁是该文件的主要写入触发者":token 值的修改起点几乎一定来自代码生成或设计源同步,主写入方是 code-generation,故归 `for-code-generation/`。`for-figma-inspect/` 与 `for-review-and-qa/` 的相关文件以"link 到 tokens-colors"方式引用,不复制内容。这一判定标准在 `rules.md` 顶部以一段"归属判定原则"显式写出,让后续新增文件有章可循。

## Migration Plan

### 文件级映射(原 → 新)

旧路径全部相对仓库根。

- `skills/btcc-style-generator/references/figma-source.md` → `skills/btcc-style-generator/references/for-figma-inspect/source-anchors.md`
- `skills/btcc-style-generator/references/contract-screens.md` → `skills/btcc-style-generator/references/for-figma-inspect/contract-screens.md`
- `skills/btcc-style-generator/references/icons.md` → `skills/btcc-style-generator/references/for-figma-inspect/icons.md`
- `skills/btcc-style-generator/references/components.md` → 拆分为:
  - `skills/btcc-style-generator/references/for-code-generation/components-trading.md`(form / order book / TP-SL sheet)
  - `skills/btcc-style-generator/references/for-code-generation/components-account.md`(wallet / market table / orders panel)
  - `skills/btcc-style-generator/references/for-code-generation/components-global.md`(button / nav / tab bar / pair header)
- `skills/btcc-style-generator/references/tokens.md` → 拆分为:
  - `skills/btcc-style-generator/references/for-code-generation/tokens-colors.md`
  - `skills/btcc-style-generator/references/for-code-generation/tokens-size-typography.md`
- `skills/btcc-style-generator/references/page-matrix.md` → 拆分为:
  - `skills/btcc-style-generator/references/for-code-generation/pages-contract.md`(已验证 `合约pro`)
  - `skills/btcc-style-generator/references/for-code-generation/pages-other.md`(其余未验证页面,带"未验证"角标)
- `skills/btcc-style-generator/references/qa.md` → `skills/btcc-style-generator/references/for-review-and-qa/qa.md`
- `skills/btcc-style-generator/references/golden-examples.md` → `skills/btcc-style-generator/references/for-review-and-qa/golden-examples.md`
- `skills/btcc-style-generator/references/data-format.md` → `skills/btcc-style-generator/references/for-review-and-qa/data-format.md`
- `skills/btcc-style-generator/references/prompt-evals.md` → `skills/btcc-style-generator/references/for-prompt-design/prompt-evals.md`
- `skills/btcc-style-generator/references/implementation-patterns.md` → `skills/btcc-style-generator/references/for-prompt-design/implementation-patterns.md`
- 新建:`skills/btcc-style-generator/references/rules.md`(从原 SKILL.md Core Rules 与各 references 中抽取去重的 SSOT)
- 删除:`docs/btcc/btcc-design-system.md`、`docs/btcc/btcc-prompt-pack.md`、`docs/btcc/btcc-generation-governance.md`

### 执行约束

1. **单次 commit 完成移动**:Write 新 + Delete 旧 + SKILL.md / agents/openai.yaml / 仓库根 README 路径替换在同一 commit 内,不留中间态。
2. **旧路径零残留 grep 验证**:迁移完成后跑 R1 中列出的 grep 表达式,要求命中数为 0(命中 `git log` 或 commit message 内的历史路径不算回归,但建议命中点放在 quoted block 中明确标注为历史)。
3. **`openspec validate --strict`**:验证 change 自身结构合法。
4. **`scripts/btcc_qa_lint.py` 回归运行**:跑一次 lint,确认硬编码规则与新 `rules.md` 语义一致,无新增 false positive。
5. **SKILL.md 自检**:用反向索引表里 8 类任务的第一类(生成合约 pro 页面)做一次 dry-run,确认 LLM 能从 SKILL.md 单跳跳到正确的 5 个文件。

## Open Questions

1. `rules.md` 是否需要进一步拆为"颜色 SSOT"与"布局/命名 SSOT"两份?当前文件预估 < 150 行,暂判定不拆,留作后续 change。
2. SKILL.md 顶部为缓解 R2 加的"Path Migrated"提示行保留多久?暂不定,等 1-2 轮调用反馈后再决定是否删除。
3. `pages-other.md` 内的未验证页面是否应该按"风险等级"再分(完全未见 vs 部分见过 vs Figma 有节点但未对齐组件)?当前先在文件内用 section 区分,不切多文件。
