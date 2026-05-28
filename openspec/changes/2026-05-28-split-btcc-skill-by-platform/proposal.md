## Why

`skills/btcc-style-generator/` 现行结构（`rules.md` SSOT + 四个角色目录）只服务一份 Figma 源 —— BTCC APP，文件名 `新BTCC APP`、fileKey `GW9kMfpf0Nib5DG4TjoWBp`。verified anchor 全部落在 `合约pro` / `合约pro-dark` 两份 mobile canvas 上。han 提供的 BTCC Web 端 Figma 文件 `新BTCC WEB` (fileKey `VrE25c6IAuIieWngebNnwx`) 经 `get_metadata` 查证，是完全独立的另一份源：仅 2 个 canvas (`0:1 设计规范`、`3089:7459 其他-马甲包官网/桌面图标`)，断点矩阵 1024 / 1440 / 1556 / 1920，所有按钮、输入、弹窗、下单组件作为子 frame 挂在 `0:1` 之下，APP 的 `合约pro` / `合约pro-dark` 顶层 canvas 在 Web 文件里**不存在**。

更严重的是，顶层 `rules.md` R-LAYOUT-2 当前混入了 mobile 专属字句 (`mobile gutters MUST be 16px`、`touch targets MUST be 40-44px`)，这些规则既无法套到 Web，又因为住在 SSOT 里反过来污染了 Web 输出。继续在同一目录结构里硬塞两个平台的内容，会让 LLM 在调用时无法判断该读 mobile 还是 desktop，要么默认 APP、要么把两端规则一起注入。

按平台再切一刀，把 APP / Web 各自的 Figma anchor、平台衍生规则隔离到 `platform-app/` 与 `platform-web/`，同时把跨平台共享的资产 (`rules.md` SSOT、`for-prompt-design/`、`for-review-and-qa/`) 留在原位，可以让一个 skill 同时服务两条产品线而不互相污染，并保留 SSOT 单点纪律。

## What Changes

- **BREAKING**: `skills/btcc-style-generator/references/for-figma-inspect/{source-anchors,contract-screens,icons}.md` → `references/platform-app/for-figma-inspect/`（已由主线 `git mv` 完成）。
- **BREAKING**: `skills/btcc-style-generator/references/for-code-generation/{components-trading,components-account,components-global,tokens-colors,tokens-size-typography,pages-contract,pages-other}.md` → `references/platform-app/for-code-generation/`（已由主线 `git mv` 完成）。
- **BREAKING**: `references/rules.md` R-LAYOUT-2 拆分 —— 通用部分 (`tabular-nums`、右对齐数值、卡片节制、dark-derived light) 留顶层；mobile 专属 (`16px gutter`、`40-44px touch target`、bottom action bar 高度) 下沉到新文件 `platform-app/rules-app.md` 内编号 `R-LAYOUT-2-APP`。
- **BREAKING**: SKILL.md `Required Workflow` 第 1 步改为「先确认单一平台」(信号冲突或缺失时停下询问 han，禁止默认 APP，禁止并行加载两侧)。
- **BREAKING**: SKILL.md `Task → Files` 反向索引表新增 `Platform` 列，每行标 `app` / `web` / `both`，APP 行的文件路径全部加 `platform-app/` 前缀；Web 行只指向 `platform-web/for-figma-inspect/source-anchors.md` + `rules-web.md`，并标注「Web code-generation 内容尚未填充」。
- 新增 `platform-app/rules-app.md`：以 `Per rules.md R-LAYOUT-2`、`Per rules.md R-SCOPE-1` 起首格式展开 APP 平台衍生（mobile gutters、touch targets、APP verified 列表 = `设计规范` / `合约pro` / `合约pro-dark`）。
- 新增 `platform-web/rules-web.md`：以 `Per rules.md R-LAYOUT-2`、`Per rules.md R-SCOPE-1`、`Per rules.md R-NAME-1 / R-ICON-1` 起首格式展开 Web 平台衍生（断点 1024/1440/1556/1920、hover/focus、桌面密度、Web verified 列表 = canvas `0:1`、`assets/btcc-tokens.*` 与 `assets/icons/*` 暂为 APP 派生需 Unverified 标注）。
- 新增 `platform-web/for-figma-inspect/source-anchors.md`：仅 fileKey + canvas 表 + canvas `0:1` 内 verified 子 frame 节点表（下单框 `651:14846`、盘口 `647:13104`、顶部导航条 `647:12465` 等）；**不**新建 `platform-web/for-code-generation/` 目录（验证素材尚不充分）。
- 修改 `references/for-prompt-design/implementation-patterns.md`：APP 相关路径前缀加 `platform-app/`；纯 SSOT 引用与 `for-prompt-design/` 同目录引用不变。
- 修改仓库根 `README.md`：14 处对 `references/for-figma-inspect/*` 与 `references/for-code-generation/*` 的引用改写为新前缀；References table 末尾追加 `platform-web/rules-web.md`、`platform-web/for-figma-inspect/source-anchors.md`、`platform-app/rules-app.md` 三行说明。
- `references/for-prompt-design/`、`references/for-review-and-qa/` 保留在 references 顶层不下沉（两端共用 prompt 评测与 QA 流程，避免双向同步漂移）。

## Capabilities

### Modified Capabilities

- `btcc-skill-structure`：原"四个角色目录"骨架契约、`rules.md` SSOT 契约、SKILL.md 反向索引表契约全部需要适配「2 共享目录 + 2 平台目录」与「先识别平台再加载」的新协议；下文 spec delta 给出具体的 MODIFIED / ADDED Requirement。

## Impact

- **受影响的 skill 文件**：
  - `skills/btcc-style-generator/references/rules.md`（R-LAYOUT-2 拆分、R-SCOPE-1 末尾追加平台脚注）。
  - `skills/btcc-style-generator/references/platform-app/{for-figma-inspect,for-code-generation}/`（10 份文件由主线预先 `git mv` 落位）。
  - 新建 `skills/btcc-style-generator/references/platform-app/rules-app.md`、`platform-web/rules-web.md`、`platform-web/for-figma-inspect/source-anchors.md`。
  - `skills/btcc-style-generator/SKILL.md`（Required Workflow + Task → Files + Path Migrated + Original Figma Anchors + Figma Plugin Workflow / Common Mistakes / Completion Gate 路径替换）。
  - `skills/btcc-style-generator/references/for-prompt-design/implementation-patterns.md`（APP 路径前缀更新）。
- **受影响的项目文档**：仓库根 `README.md`（14 处路径替换 + 3 行追加）。
- **不受影响**：
  - `skills/btcc-style-generator/agents/openai.yaml`（grep 已确认无 `references/for-...` 路径硬编码）。
  - `skills/btcc-style-generator/assets/btcc-tokens.{json,css}`、`assets/icons/*.svg`（保留为 APP 派生值，Web 端使用时按 R-ASSETS-WEB 标 Unverified）。
  - `skills/btcc-style-generator/scripts/btcc_qa_lint.py`（不引用 references 路径；其内部硬编码的规则字符串在本次范围外）。
  - `references/for-prompt-design/prompt-evals.md`、`references/for-review-and-qa/{qa,golden-examples,data-format}.md`。
- **协作风险**：
  - 任何外部仓库或文档对旧路径 `references/for-figma-inspect/*`、`references/for-code-generation/*` 的硬编码引用都会断裂 —— 通过仓库根 grep 校验零命中（`docs/superpowers/specs/`、`openspec/changes/archive/` 历史叙述允许保留旧字面量）来兜底。
  - SKILL.md 步骤 1 若被忽略，LLM 可能默认 APP 而对 Web 任务产出错误规范 —— 通过 Required Workflow 显式停下询问 + Task → Files 表 `Platform` 列双重提示来缓解。
  - `rules-app.md` / `rules-web.md` 一旦绕过 `Per rules.md R-` 前缀私自立法，会破坏 R-SSOT-1 —— 通过 spec ADDED Requirement「Platform Rules Files Reference SSOT」与 scenario 兜底。
