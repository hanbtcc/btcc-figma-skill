## Why

`skills/btcc-style-generator/` 目前把 11 份 references 文件、3 份 `docs/btcc/*` 长文档以及 `SKILL.md` 自身的 Core Rules 揉在同一层级,职责重叠严重。仅"`Open Long`=brand / `Open Short`=error"这一条规则就分散在 14 个文件中,任何一次修订都要跨文件同步,且 `components.md` (193 行)、`tokens.md` (168 行)、`page-matrix.md` (185 行) 把多种调用场景塞在单文件里,LLM 调用时无法判断"我现在该读哪几个文件",倾向于全量加载或漏读。

调用者(LLM 或人)进入这个 skill 时,意图通常落在四个角色之一:**从 Figma 看设计 / 写代码 / 审查输出 / 设计 prompt**。把 references 按角色重新组织,并让规则在唯一来源(SSOT)里出现一次,可以让"任务 → 文件清单"的反向映射明确,显著降低读错文件、漏读、读冗余的概率。

## What Changes

- **BREAKING**: 重排 `skills/btcc-style-generator/references/` 目录,改为 `for-figma-inspect/`、`for-code-generation/`、`for-review-and-qa/`、`for-prompt-design/` 四个角色子目录,加一份 `rules.md` 作为黄金规则 SSOT。
- **BREAKING**: `SKILL.md` 的 Reference Router 改为"任务 → 角色目录 → 具体文件"的两层路由表,删除 11 行平铺映射;Core Rules 改成单条 "见 `references/rules.md`",不在 SKILL.md 重复。
- **BREAKING**: 拆分 `components.md` → `for-code-generation/components-trading.md` (form / order book / TP-SL sheet) + `components-account.md` (wallet / market table / orders panel) + `components-global.md` (button / nav / tab bar / pair header)。
- **BREAKING**: 拆分 `tokens.md` → `for-code-generation/tokens-colors.md` + `tokens-size-typography.md`。
- **BREAKING**: 拆分 `page-matrix.md` → `for-code-generation/pages-contract.md` (已验证 `合约pro`) + `pages-other.md` (其余未验证页面,加显著 "未验证" 标识)。
- 重新归位现有文件:
  - `figma-source.md` → `for-figma-inspect/source-anchors.md`
  - `contract-screens.md` → `for-figma-inspect/contract-screens.md`
  - `icons.md` → `for-figma-inspect/icons.md`
  - `qa.md` → `for-review-and-qa/qa.md`
  - `golden-examples.md` → `for-review-and-qa/golden-examples.md`
  - `data-format.md` → `for-review-and-qa/data-format.md`
  - `prompt-evals.md` → `for-prompt-design/prompt-evals.md`
  - `implementation-patterns.md` → `for-prompt-design/implementation-patterns.md`
- **删除**: `docs/btcc/btcc-design-system.md`、`docs/btcc/btcc-prompt-pack.md`、`docs/btcc/btcc-generation-governance.md`。这三份长文档(共 1279 行)是 references 的散文版且无更新信息,信息全部由新结构承担。
- 在 `SKILL.md` 顶部新增"Task → Files"反向索引表,覆盖至少 8 类典型调用(生成合约页 / 改下单按钮 / 加杠杆 picker / 审查输出 / 写 prompt / 看 Figma 节点 / 改 token / 加新页面)。
- `assets/` 与 `scripts/` 路径不变,保持向后兼容(它们被 SKILL.md 和 README 引用,内容稳定无重叠问题)。
- `agents/openai.yaml` 与 `README.md` (若存在) 同步更新到新路径。

## Capabilities

### New Capabilities

- `btcc-skill-structure`: BTCC style-generator skill 的目录骨架、SSOT 规则文件、SKILL.md 路由协议,以及"任务 → 文件清单"反向索引表的内容契约。

### Modified Capabilities

- 仓库 `openspec/specs/` 当前为空,无既有 capability 需要变更。

## Impact

- **受影响的 skill**: `skills/btcc-style-generator/` 下全部 11 份 references、`SKILL.md` 自身、`agents/openai.yaml`(若引用旧路径)。
- **受影响的项目文档**: `docs/btcc/` 三份长文档全部删除;若仓库根 `README.md` 引用了它们,需要改写或移除链接。
- **受影响的脚本**: `scripts/btcc_qa_lint.py` 当前不读 references 文件,不受路径迁移影响,但其中重复的"Open Long=brand"硬编码规则需保留(脚本是规则的运行时执行者,不视为文档冗余)。
- **不受影响**: `assets/btcc-tokens.css`、`assets/btcc-tokens.json`、`assets/icons/*.svg` 路径全部保留。
- **协作风险**: 重命名后,任何外部对 `skills/btcc-style-generator/references/components.md` 等旧路径的硬编码引用都会断裂。需要在 tasks 中扫一遍仓库内所有出现旧路径的位置(grep 结果显示 14 处),并在 design.md 里说明迁移策略。
