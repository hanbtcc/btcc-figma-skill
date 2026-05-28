## 1. 准备与基线 grep

- [x] 1.1 在仓库根执行基线 grep，列出所有命中点：`grep -rn -E "references/(for-figma-inspect|for-code-generation)/" --include="*.md" --include="*.yaml" --include="*.py" --exclude-dir="archive" --exclude-dir=".git"`，落盘到本 change 目录下的临时文件 `migration-grep-baseline.txt`（任务 9 完成后删除）
- [x] 1.2 核对基线命中范围与 plan File Structure 中"修改"清单一致：`README.md`、`skills/btcc-style-generator/SKILL.md`、`skills/btcc-style-generator/references/for-prompt-design/implementation-patterns.md`；`docs/superpowers/specs/`、`docs/superpowers/plans/`、`openspec/changes/archive/` 下的历史叙述允许保留旧字面量
- [x] 1.3 用 `git status` 确认主线已完成的 `git mv` 落位：`references/platform-app/for-figma-inspect/{source-anchors,contract-screens,icons}.md` 与 `references/platform-app/for-code-generation/{components-trading,components-account,components-global,tokens-colors,tokens-size-typography,pages-contract,pages-other}.md` 全部存在
- [x] 1.4 在已平移文件内部搜 `references/for-figma-inspect|references/for-code-generation`，确认平移文件之间相互引用是同目录裸文件名，无需改写；如有绝对前缀命中则记入待改清单

## 2. 拆分 rules.md R-LAYOUT-2

- [x] 2.1 Read `skills/btcc-style-generator/references/rules.md`，定位 R-LAYOUT-2 当前 6 条混杂段
- [x] 2.2 把 R-LAYOUT-2 内 mobile 专属字句 (`mobile gutters MUST be 16px`、`touch targets MUST be 40-44px`、bottom action bar 高度) 整段删除，替换为脚注："Platform-specific extensions of this rule (mobile gutters / touch targets / web breakpoints / hover) live in `platform-app/rules-app.md` and `platform-web/rules-web.md`."
- [x] 2.3 在 R-SCOPE-1 末尾追加：「Verified anchors are tracked per platform: see `platform-app/for-figma-inspect/source-anchors.md` for the BTCC APP file and `platform-web/for-figma-inspect/source-anchors.md` for the BTCC WEB file.」
- [x] 2.4 自检：`grep -nE "Mobile gutters|touch targets|40-44px|16px gutter" skills/btcc-style-generator/references/rules.md` 应零命中

## 3. 平移 APP 文件【主线预先完成】

- [x] 3.1 主线预先完成：`git mv references/for-figma-inspect/{source-anchors,contract-screens,icons}.md references/platform-app/for-figma-inspect/`
- [x] 3.2 主线预先完成：`git mv references/for-code-generation/*.md references/platform-app/for-code-generation/`（共 7 份）
- [x] 3.3 主线预先完成：删除空目录 `references/for-figma-inspect/`、`references/for-code-generation/`
- [x] 3.4 主线预先完成：`references/for-prompt-design/`、`references/for-review-and-qa/` 保留在 references 顶层不动

## 4. 创建 platform-app/rules-app.md

- [x] 4.1 新建 `skills/btcc-style-generator/references/platform-app/rules-app.md`，顶部写一段约束声明："This file extends `references/rules.md` with platform-specific concretization for BTCC mobile/H5/APP surfaces. Rules below MUST cite a parent rule from `rules.md`. Do NOT introduce new rules here."
- [x] 4.2 写 `## R-LAYOUT-2-APP: Mobile Density and Touch`，每条以 `Per rules.md R-LAYOUT-2 (mobile profile):` 起首，覆盖：page gutters 16px、primary 控件触控目标 40-44px、bottom action bar ≥56px、TabBar 命中 ≥44×44
- [x] 4.3 写 `## R-SCOPE-1-APP: Verified APP Sources`，以 `Per rules.md R-SCOPE-1` 起首，列：File `新BTCC APP`、key `GW9kMfpf0Nib5DG4TjoWBp`、Verified pages `设计规范` (`0:1`) / `合约pro` (`1262:304`) / `合约pro-dark` (`3112:1423`)、未验证页面列表
- [x] 4.4 自检：每条规则首句必须能溯源到顶层 R-* 编号，禁止出现独立发明的新 R-XXX 编号

## 5. 创建 platform-web/rules-web.md

- [x] 5.1 `mkdir -p skills/btcc-style-generator/references/platform-web` 后新建 `rules-web.md`，顶部写约束声明，与 rules-app.md 同款（不许立法、必须引用顶层）
- [x] 5.2 写 `## R-LAYOUT-2-WEB: Desktop Breakpoints and Density`，每条以 `Per rules.md R-LAYOUT-2 (web profile):` 起首：断点 1024 / 1440 / 1556 / 1920、1440 最小可读、hover / focus 必须用 brand 或 border-active token、`合约pro` 桌面三栏在 1440 不许垂直堆叠、cursor 状态规则
- [x] 5.3 写 `## R-SCOPE-1-WEB: Verified Web Sources`，以 `Per rules.md R-SCOPE-1` 起首，列：File `新BTCC WEB`、key `VrE25c6IAuIieWngebNnwx`、Verified canvas `设计规范` (`0:1`)、Unverified canvas `其他-马甲包官网/桌面图标` (`3089:7459`)；明确说明 Web 文件不含顶层 `合约pro` / `合约pro-dark` canvas，desktop 下单结构作为 `0:1` 的子 frame 存在，详见 source-anchors.md
- [x] 5.4 写 `## R-ASSETS-WEB: Token and Icon Provenance`，以 `Per rules.md R-NAME-1 and R-ICON-1` 起首：`assets/btcc-tokens.{json,css}` 与 `assets/icons/*.svg` 当前为 APP 派生、未与 Web Figma local variables 校对；Web 代码生成应将 token 标 Unverified 或要求 han 提供 Web token 抽取
- [x] 5.5 自检：`grep -nE "^- " skills/btcc-style-generator/references/platform-web/rules-web.md` 输出每条规则首句应以 `Per rules.md` 起始或为事实陈述（fileKey、canvas 编号）

## 6. 创建 platform-web/for-figma-inspect/source-anchors.md

- [x] 6.1 `mkdir -p skills/btcc-style-generator/references/platform-web/for-figma-inspect`
- [x] 6.2 新建 `source-anchors.md`，顶部加引用行 "See `references/rules.md` for global rules and `references/platform-web/rules-web.md` for web-specific extensions." 与验证日期 (`Verified on 2026-05-28 via Figma get_metadata`)
- [x] 6.3 写 `## File` 表：Name `新BTCC WEB`、File key `VrE25c6IAuIieWngebNnwx`
- [x] 6.4 写 `## Top-level canvases` 表：`0:1 设计规范` (Verified)、`3089:7459 其他-马甲包官网/桌面图标` (Unverified)
- [x] 6.5 写 `## Verified sub-frames inside 0:1 设计规范` 表：包含 `651:14846 合约pro下单框`、`647:13104 盘口`、`647:12465 顶部导航条`、`663:2867 右侧选项`、`651:13295 已选列表`、`647:12512 右顶信息`、`554:5210 已选`、`554:5221 二级tab组`、`554:5228 一级tab组`、`554:5235 下单组`、`554:5252 次级button`、`554:5259 开多下单button`（标 must use `--btcc-brand`，引 R-COLOR-1）、`554:5266 开空下单button`（标 must use `--btcc-error`，引 R-COLOR-1）、`554:5273 计算器`、`554:5318 止盈止损`、`770:8645 Alert`、`4558:37495 toast`、`734:14906 switch`
- [x] 6.6 写 `## Unverified frames` 段说明 `1088:5613 / 5647 / 5681` 颜色样本、`128817:91276 合约pro下单 (mobile mockup)` 等是 BTCC-style convention，需在派生文档里加 `> Source: BTCC-style convention; not in verified Figma metadata pass.`
- [x] 6.7 写 `## Token / Icon caveat` 段引 `platform-web/rules-web.md` R-ASSETS-WEB

## 7. 重写 SKILL.md

- [x] 7.1 替换 `## Required Workflow` 段，把当前步骤改成 6 步，第 1 步显式要求平台识别（"web/桌面/1920/1440/hover" → web；"app/h5/合约pro/TabBar/移动端" → app；冲突或缺失停下询问 han）
- [x] 7.2 第 3 步明确 "Load `references/rules.md` + `references/platform-<chosen>/rules-<chosen>.md` + 任务对应 references"，禁止跨平台并行加载
- [x] 7.3 替换 `## Path Migrated` 表，列 4 条最高频映射：`for-figma-inspect/* → platform-app/for-figma-inspect/*`、`for-code-generation/* → platform-app/for-code-generation/*`、新建 `platform-web/`、`rules.md mobile clauses → platform-app/rules-app.md`
- [x] 7.4 替换 `## Task → Files` 表，新增 `Platform` 列；至少 10 行覆盖：生成 `合约pro` mobile 页 (app)、生成 desktop `合约pro` workspace (web)、改下单按钮/交易表单 (app)、加杠杆 picker (app)、审查输出 (both)、写 prompt (both)、看 Figma 节点 mobile (app)、看 Figma 节点 desktop (web)、改 token (app)、加新页 (app)；表格末尾加注 "Web code-generation content (components / tokens / pages) is not yet filled."
- [x] 7.5 替换 `## Original Figma Anchors`：列两份独立 Figma 源（APP / Web），分别给 fileKey 与 verified 范围，并指向各自 platform 下的 source-anchors.md
- [x] 7.6 逐处替换 `## Figma Plugin Workflow`、`## Common Mistakes`、`## Completion Gate` 中的旧 `references/for-figma-inspect/`、`references/for-code-generation/` 路径前缀为 `references/platform-<platform>/...`；`rules.md` 与 `for-review-and-qa/qa.md`、`for-prompt-design/*.md` 路径不变
- [x] 7.7 自检：`grep -nE "references/(for-figma-inspect|for-code-generation)/" skills/btcc-style-generator/SKILL.md` 应零命中；`grep -n "Platform" skills/btcc-style-generator/SKILL.md` 应在 Task → Files 表头看到 `| Platform |`

## 8. 同步 README 与 implementation-patterns 路径

- [x] 8.1 README.md：逐处替换 `references/for-figma-inspect/{source-anchors,contract-screens,icons}.md` → `references/platform-app/for-figma-inspect/...`，共 3 类
- [x] 8.2 README.md：逐处替换 `references/for-code-generation/{components-trading,components-account,components-global,tokens-colors,tokens-size-typography,pages-contract,pages-other}.md` → `references/platform-app/for-code-generation/...`，共 7 类
- [x] 8.3 README.md：在 References table 末尾追加 3 行 —— `platform-app/rules-app.md`、`platform-web/rules-web.md`、`platform-web/for-figma-inspect/source-anchors.md` 各一行说明
- [x] 8.4 `references/for-prompt-design/implementation-patterns.md`：grep `references/` 命中行，APP 相关路径加 `platform-app/` 前缀；纯 `references/rules.md` 与 `references/for-prompt-design/...` 不变；如内含目录树示意图则按新结构重画
- [x] 8.5 自检：`grep -rn -E "references/(for-figma-inspect|for-code-generation)/" README.md skills/btcc-style-generator/` 应零命中

## 9. 验证 + commit

- [x] 9.1 全仓 grep：`grep -rn -E "references/(for-figma-inspect|for-code-generation)/" --include="*.md" --include="*.yaml" --include="*.py" --exclude-dir="archive" --exclude-dir=".git"`，排除 `docs/superpowers/`、本 change 目录基线文件后应零命中
- [x] 9.2 执行 `openspec validate 2026-05-28-split-btcc-skill-by-platform --strict`，要求通过
- [x] 9.3 执行 `python skills/btcc-style-generator/scripts/btcc_qa_lint.py skills/btcc-style-generator/` 烟测，确认无新增 false positive
- [x] 9.4 结构校验：`ls skills/btcc-style-generator/references/` 恰为 5 项 (`rules.md` + `for-prompt-design` + `for-review-and-qa` + `platform-app` + `platform-web`)；`ls platform-app/` 含 `rules-app.md` + 两子目录；`ls platform-web/` 含 `rules-web.md` + `for-figma-inspect/`，**无** `for-code-generation/`
- [x] 9.5 对 SKILL.md Task → Files 表 10 行任务做 dry-run，每条路径 ls 存在
- [x] 9.6 删除临时基线文件 `openspec/changes/2026-05-28-split-btcc-skill-by-platform/migration-grep-baseline.txt`
- [x] 9.7 单次 commit 全部改动（含主线预先 mv 后的位置）；commit message 列出 BREAKING 路径变更摘要、9.1 grep 结果、9.2 validate 结果作为证据
