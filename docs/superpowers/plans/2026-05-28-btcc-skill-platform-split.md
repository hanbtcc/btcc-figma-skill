# BTCC Skill Platform Split — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在 `skills/btcc-style-generator/` 下引入 `references/platform-app/` 与 `references/platform-web/` 子目录，把现有 references 平移到 APP 子目录、为 Web 建最小骨架（rules-web + figma source-anchors），并把 `rules.md` 中混杂的 mobile 专属规则下沉到 `platform-app/rules-app.md`。

**Architecture:** 单一 skill 内部按平台分子目录。`rules.md` 顶层留平台无关的 SSOT（颜色 / 命名 / scope 机制 / SSOT 纪律 / R-LAYOUT-2 通用部分），`platform-{app,web}/rules-{app,web}.md` 仅以 `Per rules.md R-XXX:` 形式展开平台衍生（mobile gutters / 触控目标 vs Web 断点 / hover）。`for-prompt-design/` 与 `for-review-and-qa/` 不下沉，两端共享。

**Tech Stack:** Markdown + OpenSpec change（`openspec/changes/2026-05-28-split-btcc-skill-by-platform/`）+ git。

---

## File Structure

新增 / 改动 / 移动文件清单（路径相对仓库根）：

**新建**
- `openspec/changes/2026-05-28-split-btcc-skill-by-platform/proposal.md`
- `openspec/changes/2026-05-28-split-btcc-skill-by-platform/tasks.md`
- `openspec/changes/2026-05-28-split-btcc-skill-by-platform/specs/btcc-skill-structure/spec.md`（delta：MODIFIED Requirements）
- `skills/btcc-style-generator/references/platform-app/rules-app.md`
- `skills/btcc-style-generator/references/platform-web/rules-web.md`
- `skills/btcc-style-generator/references/platform-web/for-figma-inspect/source-anchors.md`

**移动（`git mv`）**
- `references/for-figma-inspect/{source-anchors,contract-screens,icons}.md` → `references/platform-app/for-figma-inspect/`
- `references/for-code-generation/{components-trading,components-account,components-global,tokens-colors,tokens-size-typography,pages-contract,pages-other}.md` → `references/platform-app/for-code-generation/`

**修改**
- `skills/btcc-style-generator/references/rules.md`：删除 R-LAYOUT-2 中 mobile 专属字句、加平台脚注
- `skills/btcc-style-generator/SKILL.md`：Required Workflow 加平台识别步骤、Task→Files 表加 Platform 列、所有路径前缀加 `platform-app/`
- `skills/btcc-style-generator/references/for-prompt-design/implementation-patterns.md`：路径前缀更新
- `README.md`：14 条路径引用更新
- `openspec/specs/btcc-skill-structure/spec.md`：通过 OpenSpec archive 流程同步

**不动**
- `skills/btcc-style-generator/agents/openai.yaml`（grep 确认无路径引用）
- `skills/btcc-style-generator/assets/`、`scripts/btcc_qa_lint.py`
- `references/for-prompt-design/`、`references/for-review-and-qa/`

---

### Task 1: 起草 OpenSpec 变更骨架

**Files:**
- Create: `openspec/changes/2026-05-28-split-btcc-skill-by-platform/proposal.md`
- Create: `openspec/changes/2026-05-28-split-btcc-skill-by-platform/tasks.md`
- Create: `openspec/changes/2026-05-28-split-btcc-skill-by-platform/specs/btcc-skill-structure/spec.md`

- [ ] **Step 1.1：写 proposal.md**

内容（按上次 archive 的格式）：
- `## Why`：现行 skill 的 references 仅覆盖 APP 端 Figma `新BTCC APP`（fileKey `GW9kMfpf0Nib5DG4TjoWBp`），新 Web 文件 `新BTCC WEB`（fileKey `VrE25c6IAuIieWngebNnwx`）属独立来源；`rules.md` R-LAYOUT-2 混入 mobile 专属规则（16px gutter / 40-44px 触控）无法套用 Web。
- `## What Changes`（每条以 BREAKING 标注路径变更）：新增两个平台子目录、APP 内容平移、Web 建最小骨架、R-LAYOUT-2 拆分、SKILL.md 路由加平台识别、README 14 条引用更新。
- `## Capabilities`：`### Modified Capabilities` 列出 `btcc-skill-structure`（重写要求集以反映平台分目录）。
- `## Impact`：列出受影响文件 + 协作风险（旧路径硬编码失效）+ 缓解（grep 校验）。

- [ ] **Step 1.2：写 tasks.md（与本计划任务序号 2-12 对齐的扁平 checkbox 列表）**

格式参考 `openspec/changes/archive/2026-05-28-restructure-btcc-skill-by-role/tasks.md`，章节：
1. 准备与基线 grep
2. 拆分 rules.md（R-LAYOUT-2）
3. 平移 APP 文件
4. 创建 platform-app/rules-app.md
5. 创建 platform-web/rules-web.md
6. 创建 platform-web/for-figma-inspect/source-anchors.md
7. 重写 SKILL.md
8. 更新外围引用（README、implementation-patterns.md）
9. 验证
10. 提交

- [ ] **Step 1.3：写 spec delta**

文件 `specs/btcc-skill-structure/spec.md` 用 OpenSpec delta 语法：
```
## MODIFIED Requirements
### Requirement: Directory Skeleton Under references/
The `references/` directory SHALL contain exactly five direct children: `rules.md`, `for-prompt-design/`, `for-review-and-qa/`, `platform-app/`, `platform-web/`.
（保留原 scenario 风格，把"四个角色目录"改为"两个共享目录 + 两个平台目录"）

### Requirement: Platform Subdirectory Layout
`references/platform-app/` SHALL contain `rules-app.md`, `for-figma-inspect/`, `for-code-generation/`.
`references/platform-web/` SHALL contain `rules-web.md` and `for-figma-inspect/source-anchors.md`.
[scenarios: 缺 rules-app.md / Web 凭空出现 for-code-generation 文件]

### Requirement: Platform Rules Files Reference SSOT
`rules-app.md` 与 `rules-web.md` 中每条规则首行 SHALL 以 `Per rules.md R-` 开头，禁止独立发明与 SSOT 冲突的新规则。
[scenario: 平台规则文件出现非引用形式的"规定式"语句]

### Requirement: SKILL.md Platform Identification Step
SKILL.md Required Workflow 第 1 步 SHALL 要求在加载任务文件前确定单一平台（app 或 web），冲突或缺失时停下询问用户。
[scenario: Required Workflow 缺平台识别]

### Requirement: SKILL.md Task Index Has Platform Column
SKILL.md Task→Files 表 SHALL 包含 `Platform` 列，每行有值（`app` / `web` / `both`）。
[scenario: 表无 Platform 列]
```

- [ ] **Step 1.4：commit**

```bash
git add openspec/changes/2026-05-28-split-btcc-skill-by-platform/
git commit -m "docs(openspec): propose splitting BTCC skill by platform"
```

---

### Task 2: 基线 grep

**Files:**
- Create (临时): `openspec/changes/2026-05-28-split-btcc-skill-by-platform/migration-grep-baseline.txt`

- [ ] **Step 2.1：grep 旧路径并落盘**

```bash
cd C:/Users/gtshkadmin/Desktop/figma
grep -rn -E "references/(for-figma-inspect|for-code-generation)/" \
  --include="*.md" --include="*.yaml" --include="*.py" \
  --exclude-dir="archive" --exclude-dir="docs/superpowers" \
  > openspec/changes/2026-05-28-split-btcc-skill-by-platform/migration-grep-baseline.txt
```
预期命中文件：`README.md`、`SKILL.md`、`references/for-prompt-design/implementation-patterns.md`、`openspec/specs/btcc-skill-structure/spec.md`。

- [ ] **Step 2.2：人工核对**

确认基线列表与本计划 File Structure 中"修改"清单一致（README + SKILL + implementation-patterns）。`openspec/specs/btcc-skill-structure/spec.md` 由 archive 阶段自动同步，不在本次手改清单。

---

### Task 3: 拆分 rules.md（R-LAYOUT-2）

**Files:**
- Modify: `skills/btcc-style-generator/references/rules.md`

- [ ] **Step 3.1：定位现有 R-LAYOUT-2**

Read `skills/btcc-style-generator/references/rules.md` lines 44-50。当前 6 条混杂；需要拆为：
- 通用部分留顶层（第 1-5 条：dark-first、tabular-nums、右对齐数值、卡片节制、…）
- mobile 专属下沉（第 6 条：`Mobile gutters MUST be 16px; touch targets MUST be 40-44px on primary controls.`）

- [ ] **Step 3.2：改写 R-LAYOUT-2**

把 R-LAYOUT-2 最后一条 mobile 行替换为脚注：

```
## R-LAYOUT-2: Density and Type

- Default to dark mode. Light mode is dark-derived; do not author per-component light hexes.
- Compact spacing, dense rows, thin neutral dividers, restrained borders.
- Numeric columns MUST use `font-variant-numeric: tabular-nums`.
- Right-align numeric columns; left-align pair / asset / status / action labels.
- Card surfaces only for repeated modules or genuinely contained tools — not for every section.
- Platform-specific extensions of this rule (mobile gutters / touch targets / web breakpoints / hover) live in `platform-app/rules-app.md` and `platform-web/rules-web.md`.
```

- [ ] **Step 3.3：在 R-SCOPE-1 中加平台脚注**

在 `R-SCOPE-1` 末尾追加：

```
Verified anchors are tracked per platform: see `platform-app/for-figma-inspect/source-anchors.md` for the BTCC APP file and `platform-web/for-figma-inspect/source-anchors.md` for the BTCC WEB file.
```

- [ ] **Step 3.4：自检**

```bash
grep -n "Mobile gutters\|touch targets\|40-44px\|16px" skills/btcc-style-generator/references/rules.md
```
预期：0 行命中（mobile 专属字串已下沉）。

---

### Task 4: 平移 APP references 文件

**Files:**
- Move (`git mv`):
  - `skills/btcc-style-generator/references/for-figma-inspect/{source-anchors,contract-screens,icons}.md`
    → `.../platform-app/for-figma-inspect/`
  - `skills/btcc-style-generator/references/for-code-generation/*.md`（7 个）
    → `.../platform-app/for-code-generation/`

- [ ] **Step 4.1：创建空目录**

```bash
mkdir -p skills/btcc-style-generator/references/platform-app/for-figma-inspect
mkdir -p skills/btcc-style-generator/references/platform-app/for-code-generation
```

- [ ] **Step 4.2：git mv 所有文件**

```bash
cd skills/btcc-style-generator/references
git mv for-figma-inspect/source-anchors.md   platform-app/for-figma-inspect/
git mv for-figma-inspect/contract-screens.md platform-app/for-figma-inspect/
git mv for-figma-inspect/icons.md            platform-app/for-figma-inspect/
git mv for-code-generation/components-trading.md       platform-app/for-code-generation/
git mv for-code-generation/components-account.md       platform-app/for-code-generation/
git mv for-code-generation/components-global.md        platform-app/for-code-generation/
git mv for-code-generation/tokens-colors.md            platform-app/for-code-generation/
git mv for-code-generation/tokens-size-typography.md   platform-app/for-code-generation/
git mv for-code-generation/pages-contract.md           platform-app/for-code-generation/
git mv for-code-generation/pages-other.md              platform-app/for-code-generation/
rmdir for-figma-inspect for-code-generation
```

- [ ] **Step 4.3：被移动文件的内部交叉引用更新**

部分文件相互引用（`source-anchors.md` 引 `contract-screens.md`、components 引 tokens）。这些是**同目录相对引用**，平移后路径不变，无需改。但检查任一文件是否含 `references/for-figma-inspect/` 形式的绝对前缀，如有改为 `platform-app/for-figma-inspect/`：

```bash
grep -rn "references/for-figma-inspect\|references/for-code-generation" \
  skills/btcc-style-generator/references/platform-app/
```
预期：0 行（相对引用应当只写 `contract-screens.md`、`tokens-colors.md` 等裸文件名）。如有命中，逐处改为新前缀。

---

### Task 5: 创建 platform-app/rules-app.md

**Files:**
- Create: `skills/btcc-style-generator/references/platform-app/rules-app.md`

- [ ] **Step 5.1：写 rules-app.md**

内容（每条以 `Per rules.md R-XXX:` 开头）：

```markdown
# BTCC APP Platform Rules

This file extends `references/rules.md` with platform-specific concretization for BTCC mobile/H5/APP surfaces. Rules below MUST cite a parent rule from `rules.md`. Do NOT introduce new rules here.

## R-LAYOUT-2-APP: Mobile Density and Touch

Per rules.md R-LAYOUT-2 (mobile profile):

- Page gutters MUST be 16px on phone widths.
- Touch targets MUST be 40-44px on primary controls (`Open Long`, `Open Short`, `Confirm`, `Buy/Sell` tabs).
- Bottom action bar height MUST be ≥ 56px to clear iOS home indicator on `合约pro` order surface.
- TabBar item taps MUST hit at least 44x44 (`次级button`, `TabBar 底部标签栏` component sets).

## R-SCOPE-1-APP: Verified APP Sources

Per rules.md R-SCOPE-1, the BTCC APP-side verified scope is:

- File: `新BTCC APP`, key `GW9kMfpf0Nib5DG4TjoWBp`.
- Verified pages: `设计规范` (`0:1`), `合约pro` (`1262:304`), `合约pro-dark` (`3112:1423`).
- Unverified surfaces: `home`, `markets`, `wallet/assets`, `auth`, `copy-trading`, `spot`, `c2c`, `h5`, `全局组件`, `图标`, `换色`, `老合约`, `TradFi`, `我的、设置`, `卡券/体验金`, `支付通道、NFT、提现`, `观点`.
```

- [ ] **Step 5.2：自检**

```bash
grep -n "^- " skills/btcc-style-generator/references/platform-app/rules-app.md | grep -v "Per rules.md\|MUST\|File:\|Verified\|Unverified"
```
逐条人工检查命中行：每条规则首句应能溯源到顶层 R-* 编号。

---

### Task 6: 创建 platform-web/rules-web.md

**Files:**
- Create: `skills/btcc-style-generator/references/platform-web/rules-web.md`

- [ ] **Step 6.1：写 rules-web.md**

```markdown
# BTCC Web Platform Rules

This file extends `references/rules.md` with platform-specific concretization for BTCC desktop/web surfaces. Rules below MUST cite a parent rule from `rules.md`. Do NOT introduce new rules here.

## R-LAYOUT-2-WEB: Desktop Breakpoints and Density

Per rules.md R-LAYOUT-2 (web profile):

- Primary breakpoints supported by the BTCC WEB Figma source: 1024 / 1440 / 1556 / 1920 (per the rulers on canvas `0:1 设计规范`, fileKey `VrE25c6IAuIieWngebNnwx`).
- Layout MUST stay legible at 1440 minimum; ≥1920 is the canonical workspace width for `合约pro` desktop.
- Hover states MUST be defined for all interactive controls; focus rings MUST use a token bound to brand or border-active, not arbitrary colors.
- Side-by-side trading layout (`order book` + `下单` + `right panel 合约信息/账户资产`) MUST stay above the fold at 1440; do not stack vertically before the smallest desktop breakpoint.
- Cursor states: pointer for actionable, text for inputs, not-allowed for disabled.

## R-SCOPE-1-WEB: Verified Web Sources

Per rules.md R-SCOPE-1, the BTCC WEB-side verified scope is:

- File: `新BTCC WEB`, key `VrE25c6IAuIieWngebNnwx`.
- Verified canvas: `设计规范` (`0:1`).
- Unverified canvas: `其他-马甲包官网/桌面图标` (`3089:7459`).
- The BTCC WEB Figma file does NOT contain top-level `合约pro` / `合约pro-dark` canvases; desktop trading anatomy lives as sub-frames inside `0:1`. See `for-figma-inspect/source-anchors.md` for the per-element node index.

## R-ASSETS-WEB: Token and Icon Provenance

Per rules.md R-NAME-1 and R-ICON-1:

- `assets/btcc-tokens.{json,css}` and `assets/icons/*.svg` are currently derived from the BTCC APP file. They have NOT been cross-checked against the BTCC WEB local variables collection.
- Web code generation MUST mark token usage as Unverified until tokens are reconciled, OR ask the user to export Web Figma local variables.
```

- [ ] **Step 6.2：自检**

```bash
grep -nE "^##|^- " skills/btcc-style-generator/references/platform-web/rules-web.md | head -20
```
人工核对每条规则首句以 `Per rules.md` 起始或为事实陈述（fileKey、canvas 编号）。

---

### Task 7: 创建 platform-web/for-figma-inspect/source-anchors.md

**Files:**
- Create: `skills/btcc-style-generator/references/platform-web/for-figma-inspect/source-anchors.md`

- [ ] **Step 7.1：建目录并写文件**

```bash
mkdir -p skills/btcc-style-generator/references/platform-web/for-figma-inspect
```

文件内容：

```markdown
# BTCC Web — Figma Source Anchors

> See `references/rules.md` for global rules and `references/platform-web/rules-web.md` for web-specific extensions.

Verified on 2026-05-28 via Figma `get_metadata`. Re-verify if older than ~30 days.

## File

| Field | Value |
| --- | --- |
| Name | `新BTCC WEB` |
| File key | `VrE25c6IAuIieWngebNnwx` |

## Top-level canvases

| Node ID | Name | Status |
| --- | --- | --- |
| `0:1` | `设计规范` | Verified — primary source for tokens, components, desktop trading anatomy |
| `3089:7459` | `其他-马甲包官网/桌面图标` | Unverified |

## Verified sub-frames inside `0:1 设计规范`

Anchors below are directly observed in Figma metadata. Names retain Chinese labels exactly as authored.

| Node ID | Name | Role |
| --- | --- | --- |
| `651:14846` | `合约pro下单框` | Desktop order form (1214 × 698) |
| `647:13104` | `盘口` | Order book (695 × 684) |
| `647:12465` | `顶部导航条` | Top global nav (1961 × 185) |
| `663:2867` | `右侧选项` | Right-side panel (540 × 1134) |
| `651:13295` | `已选列表` | Selected pair list (1556 × 32) |
| `647:12512` | `右顶信息` | Top-right info bar (1556 × 56) |
| `554:5210` | `已选` | Selected tab cell (437 × 66) |
| `554:5221` | `二级tab组` | Secondary tab group (172 × 64) |
| `554:5228` | `一级tab组` | Primary tab group (264 × 80) |
| `554:5235` | `下单组` | Order action group (329 × 102) |
| `554:5252` | `次级button` | Secondary button (274 × 68) |
| `554:5259` | `开多下单button` | Open Long button (389 × 80) — must use `--btcc-brand`, see rules.md R-COLOR-1 |
| `554:5266` | `开空下单button` | Open Short button (395 × 80) — must use `--btcc-error`, see rules.md R-COLOR-1 |
| `554:5273` | `计算器` | Calculator (368 × 380) |
| `554:5318` | `止盈止损` | TP/SL panel (625 × 285) |
| `651:14846` | `合约pro下单框` | (duplicate, see above) |
| `770:8645` | `Alert` | Alert dialog (336 × 211) |
| `4558:37495` | `toast` | Toast (584 × 98) |
| `734:14906` | `switch` | Switch (106 × 56) |

## Unverified frames (BTCC-style convention)

The remaining frames inside canvas `0:1` (e.g. `red`, `green`, `orange` color swatches at `1088:5613` / `5647` / `5681`, `dark-brand` / `light-brand` collections, mobile-shaped mockups such as `合约pro下单` `128817:91276` 360×737) are color/spec scratch areas or cross-platform mockups. Treat as Unverified per rules.md R-SCOPE-1; mark with `> Source: BTCC-style convention; not in verified Figma metadata pass.` in any derived doc.

## Token / Icon caveat

Per `platform-web/rules-web.md` R-ASSETS-WEB, `assets/btcc-tokens.{json,css}` and `assets/icons/*.svg` are APP-derived. Web code generation must reconcile or mark Unverified.
```

- [ ] **Step 7.2：自检**

```bash
grep -c "^|" skills/btcc-style-generator/references/platform-web/for-figma-inspect/source-anchors.md
```
预期 ≥ 25（节点表行数）。检查每个 fileKey/nodeID 字面量是否与 Task 1 中 Web 元数据查询结果一致（fileKey `VrE25c6IAuIieWngebNnwx`、canvas `0:1` 与 `3089:7459`）。

---

### Task 8: 重写 SKILL.md

**Files:**
- Modify: `skills/btcc-style-generator/SKILL.md`

- [ ] **Step 8.1：替换 Required Workflow 段**

把当前 5 步替换为：

```markdown
## Required Workflow

1. Identify platform first (single platform per invocation):
   - "web" / "桌面" / "1920" / "1440" / "hover" / "鼠标" → `platform-web`
   - "app" / "h5" / "合约pro" / "TabBar" / "移动端" → `platform-app`
   - 信号冲突或缺失时停下询问用户，不默认任一平台、不并行加载两侧。
2. Identify the task class (see Task → Files index below).
3. Load `references/rules.md` + `references/platform-<chosen>/rules-<chosen>.md` + the task-specific files listed in the index — nothing more.
4. If a BTCC Figma URL or plugin is available, inspect the original Figma source before inventing tokens, icons, or components. Use the platform's `for-figma-inspect/source-anchors.md`.
5. Generate or review against the role-targeted references.
6. Run `references/for-review-and-qa/qa.md` before claiming completion.
```

- [ ] **Step 8.2：替换 Path Migrated 表**

```markdown
## Path Migrated (legacy → new)

| Legacy path (deprecated)                              | New location                                                                  |
| ----------------------------------------------------- | ----------------------------------------------------------------------------- |
| `references/for-figma-inspect/*.md` (APP)             | `references/platform-app/for-figma-inspect/*.md`                              |
| `references/for-code-generation/*.md` (APP)           | `references/platform-app/for-code-generation/*.md`                            |
| (none — Web previously absent)                        | `references/platform-web/rules-web.md` + `for-figma-inspect/source-anchors.md` |
| `rules.md` mobile gutters / 40-44px / touch targets   | `platform-app/rules-app.md` R-LAYOUT-2-APP                                    |
```

- [ ] **Step 8.3：替换 Task → Files 表**

把现有表替换为加 `Platform` 列：

```markdown
## Task → Files

`references/rules.md` is a default mandatory read for every task and is not repeated per row. After identifying the platform, also load `references/platform-<platform>/rules-<platform>.md`.

| Task | Platform | Role | Files |
| --- | --- | --- | --- |
| Generate a `合约pro` contract page (mobile) | app | for-code-generation | `platform-app/for-code-generation/{pages-contract,components-trading,components-global,tokens-colors,tokens-size-typography}.md` |
| Generate a desktop `合约pro` workspace | web | for-figma-inspect | `platform-web/for-figma-inspect/source-anchors.md` (code-generation content not yet filled — see note below) |
| Change the order button / trading form | app | for-code-generation | `platform-app/for-code-generation/{components-trading,tokens-colors}.md` |
| Add a leverage picker | app | for-code-generation | `platform-app/for-code-generation/{components-trading,tokens-size-typography}.md` |
| Review AI / model output | both | for-review-and-qa | `for-review-and-qa/{qa,golden-examples,data-format}.md` |
| Write or edit a prompt | both | for-prompt-design | `for-prompt-design/{prompt-evals,implementation-patterns}.md` |
| Inspect a Figma node / anchor (mobile) | app | for-figma-inspect | `platform-app/for-figma-inspect/{source-anchors,contract-screens,icons}.md` |
| Inspect a Figma node / anchor (desktop) | web | for-figma-inspect | `platform-web/for-figma-inspect/source-anchors.md` |
| Modify a token value | app | for-code-generation | `platform-app/for-code-generation/{tokens-colors,tokens-size-typography}.md` |
| Add a new page (unverified surface) | app | for-code-generation + for-figma-inspect | `platform-app/for-code-generation/pages-other.md` (carry the Unverified marker per `rules.md` R-SCOPE-1), `platform-app/for-figma-inspect/source-anchors.md` |

> Web code-generation content (components / tokens / pages) is not yet filled. Generating Web code requires either user-provided Web Figma reconciliation or explicit Unverified markers per `rules.md` R-SCOPE-1.
```

- [ ] **Step 8.4：更新 Original Figma Anchors 段**

替换为：

```markdown
## Original Figma Anchors

Two independent Figma sources, one per platform.

- BTCC APP — file `新BTCC APP`, key `GW9kMfpf0Nib5DG4TjoWBp`. Verified pages `设计规范` (`0:1`), `合约pro` (`1262:304`), `合约pro-dark` (`3112:1423`). Component sets `次级button`, `TabBar 底部标签栏`. Full anchor list: `platform-app/for-figma-inspect/source-anchors.md`.
- BTCC WEB — file `新BTCC WEB`, key `VrE25c6IAuIieWngebNnwx`. Verified canvas `设计规范` (`0:1`). Full anchor list: `platform-web/for-figma-inspect/source-anchors.md`.

For verified-vs-unverified scope per platform, see `rules.md` R-SCOPE-1 plus `platform-app/rules-app.md` R-SCOPE-1-APP and `platform-web/rules-web.md` R-SCOPE-1-WEB.
```

- [ ] **Step 8.5：更新 Figma Plugin Workflow / Common Mistakes / Completion Gate**

逐处 `references/for-figma-inspect/` → `references/platform-<platform>/for-figma-inspect/`，`references/for-code-generation/` 同理。Common Mistakes 段保留对 `rules.md` 的引用，无需平台前缀。Completion Gate `references/for-review-and-qa/qa.md` 路径不变。

- [ ] **Step 8.6：自检**

```bash
grep -nE "references/(for-figma-inspect|for-code-generation)/" skills/btcc-style-generator/SKILL.md
```
预期：0 行命中。

```bash
grep -n "Platform" skills/btcc-style-generator/SKILL.md
```
预期：Task → Files 表头含 `| Platform |`。

---

### Task 9: 同步外围引用（README 与 implementation-patterns）

**Files:**
- Modify: `README.md`
- Modify: `skills/btcc-style-generator/references/for-prompt-design/implementation-patterns.md`

- [ ] **Step 9.1：README.md 路径替换**

逐处替换（共约 14 处）：

| Old | New |
| --- | --- |
| `references/for-figma-inspect/source-anchors.md` | `references/platform-app/for-figma-inspect/source-anchors.md` |
| `references/for-figma-inspect/contract-screens.md` | `references/platform-app/for-figma-inspect/contract-screens.md` |
| `references/for-figma-inspect/icons.md` | `references/platform-app/for-figma-inspect/icons.md` |
| `references/for-code-generation/components-trading.md` | `references/platform-app/for-code-generation/components-trading.md` |
| `references/for-code-generation/components-account.md` | `references/platform-app/for-code-generation/components-account.md` |
| `references/for-code-generation/components-global.md` | `references/platform-app/for-code-generation/components-global.md` |
| `references/for-code-generation/tokens-colors.md` | `references/platform-app/for-code-generation/tokens-colors.md` |
| `references/for-code-generation/tokens-size-typography.md` | `references/platform-app/for-code-generation/tokens-size-typography.md` |
| `references/for-code-generation/pages-contract.md` | `references/platform-app/for-code-generation/pages-contract.md` |
| `references/for-code-generation/pages-other.md` | `references/platform-app/for-code-generation/pages-other.md` |

`references/for-review-and-qa/*` 与 `references/for-prompt-design/*` 不变。

在 README 的"References table"段末尾追加 3 行 Web 条目：

```markdown
| `references/platform-web/rules-web.md` | Web-specific extensions of rules.md (breakpoints, hover, desktop density) |
| `references/platform-web/for-figma-inspect/source-anchors.md` | Figma anchors for `新BTCC WEB` (fileKey VrE25c6IAuIieWngebNnwx) |
| `references/platform-app/rules-app.md` | APP-specific extensions of rules.md (mobile gutters, touch targets) |
```

- [ ] **Step 9.2：implementation-patterns.md 路径替换**

```bash
grep -n "references/" skills/btcc-style-generator/references/for-prompt-design/implementation-patterns.md
```
对每条命中：APP-相关路径加 `platform-app/` 前缀；纯 `references/rules.md` 与 `references/for-prompt-design/...` 不变。`references/` 出现在树状示意图（fenced code block）中的，参考新结构重画一棵小树即可（保留 1 级 + 2 级目录足矣）。

- [ ] **Step 9.3：自检**

```bash
grep -rn -E "references/(for-figma-inspect|for-code-generation)/" \
  README.md skills/btcc-style-generator/
```
预期：0 行命中。

---

### Task 10: 验证

- [ ] **Step 10.1：全仓 grep 旧路径**

```bash
cd C:/Users/gtshkadmin/Desktop/figma
grep -rn -E "references/(for-figma-inspect|for-code-generation)/" \
  --include="*.md" --include="*.yaml" --include="*.py" \
  --exclude-dir="archive" \
  --exclude-dir=".git" \
  | grep -v "openspec/changes/2026-05-28-split-btcc-skill-by-platform/migration-grep-baseline.txt"
```
预期：0 行命中（除基线文件本身外）。`docs/superpowers/specs/` 下的设计文档与 `docs/superpowers/plans/` 下的本计划本身允许保留旧路径字面量（它们是历史叙述）。

- [ ] **Step 10.2：openspec validate**

```bash
openspec validate 2026-05-28-split-btcc-skill-by-platform --strict
```
预期：通过。

- [ ] **Step 10.3：lint 烟测**

```bash
python skills/btcc-style-generator/scripts/btcc_qa_lint.py skills/btcc-style-generator/
```
预期：无新增 false positive。

- [ ] **Step 10.4：结构校验**

```bash
ls skills/btcc-style-generator/references/
```
预期 5 项：`rules.md  for-prompt-design  for-review-and-qa  platform-app  platform-web`。

```bash
ls skills/btcc-style-generator/references/platform-app/
ls skills/btcc-style-generator/references/platform-web/
```
预期：app 含 `rules-app.md  for-figma-inspect  for-code-generation`；web 含 `rules-web.md  for-figma-inspect`。

- [ ] **Step 10.5：dry-run Task → Files 表**

对 SKILL.md 表中 10 行任务，每行人工跳转对应文件，确认每个路径存在。任一失败回到 Task 8/9 修正。

- [ ] **Step 10.6：删除临时基线**

```bash
rm openspec/changes/2026-05-28-split-btcc-skill-by-platform/migration-grep-baseline.txt
```

---

### Task 11: 单次提交

- [ ] **Step 11.1：commit**

```bash
git add skills/btcc-style-generator/ README.md openspec/changes/2026-05-28-split-btcc-skill-by-platform/
git status --short
```
检查 status：应看到大量 R（rename）、若干 M（modify）、几个新建文件、无意外文件。

```bash
git commit -m "$(cat <<'EOF'
refactor(btcc-skill): split references by platform (app + web)

BREAKING:
- references/for-figma-inspect/*       → references/platform-app/for-figma-inspect/*
- references/for-code-generation/*     → references/platform-app/for-code-generation/*
- rules.md R-LAYOUT-2 mobile clauses   → platform-app/rules-app.md (R-LAYOUT-2-APP)

NEW:
- platform-web/rules-web.md (R-LAYOUT-2-WEB, R-SCOPE-1-WEB, R-ASSETS-WEB)
- platform-web/for-figma-inspect/source-anchors.md (新BTCC WEB, fileKey VrE25c6IAuIieWngebNnwx, canvas 0:1)

Verified after change:
- repo-wide grep for legacy `references/for-{figma-inspect,code-generation}/` → 0 hits
- openspec validate 2026-05-28-split-btcc-skill-by-platform --strict → pass
- btcc_qa_lint.py smoke run → no new false positives
EOF
)"
```

注：proposal/tasks/spec delta 在 Task 1 已 commit；本 commit 是结构调整 + 引用同步。

---

## Self-Review

1. **Spec coverage**：spec 9 条验收 → Task 4（结构）/3（R-LAYOUT-2 拆分）/5+6（rules-app/web 引用 R-）/8（SKILL.md Platform 列与平台识别步骤）/10.1（grep 零命中）/10.2（openspec validate）。Web `for-code-generation/` 不存在 → Task 10.4 校验。每条均有任务覆盖。
2. **Placeholder 扫描**：无 TBD / TODO；每个 Step 给出具体命令、文件内容、预期结果。
3. **Type/命名一致性**：`rules-app.md` / `rules-web.md` 文件名、R-LAYOUT-2-APP / R-LAYOUT-2-WEB 编号、`platform-app/` / `platform-web/` 前缀在 Task 4-10 中保持一致。Web fileKey `VrE25c6IAuIieWngebNnwx` 在 Task 6 / 7 / 11 commit message 中字面量一致。

---

## Execution Handoff

Plan saved to `docs/superpowers/plans/2026-05-28-btcc-skill-platform-split.md`.

han 已要求"用 agent 加速"。下一步：用 `superpowers:dispatching-parallel-agents` 把 Task 4-7（彼此独立的目录创建/平移/写作）并行分派，主线串行执行 Task 1（OpenSpec 骨架）、Task 2-3（rules.md 改动）、Task 8-11（依赖前面产物的 SKILL.md / README / 验证 / commit）。
