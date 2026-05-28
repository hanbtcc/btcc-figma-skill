---
title: BTCC skill 平台分子目录设计 (App + Web)
date: 2026-05-28
owner: han
status: draft (pending han approval)
---

# 设计：BTCC skill 按平台分子目录

## 背景

`skills/btcc-style-generator/` 现有结构（角色四分 + `rules.md` SSOT）针对的是 Figma 文件 `新BTCC APP`（fileKey `GW9kMfpf0Nib5DG4TjoWBp`）的 mobile 规范。verified anchor 仅覆盖 APP 的 `合约pro` / `合约pro-dark`。

han 提供了 Web 端 Figma 文件 `新BTCC WEB`（fileKey `VrE25c6IAuIieWngebNnwx`）。元数据查证后该文件为完全独立的另一份源：仅 2 个 canvas（`0:1 设计规范`、`3089:7459 其他-马甲包官网/桌面图标`），断点矩阵 1024 / 1440 / 1556 / 1920 / 1930，所有按钮、输入、弹窗、下单组件挂在 `0:1` 之下。APP 文件中 `合约pro`、`合约pro-dark` 在该文件内**不存在**。

现有 `rules.md` 中的 R-LAYOUT-2 混入 mobile 专属规则（`mobile gutters MUST be 16px`、`touch targets MUST be 40-44px`），无法直接套用到 Web。其余规则（颜色语义、术语、scope 标记、SSOT 纪律、图标顺序）在两端通用。

## 目标

让一个 skill 能同时服务 BTCC APP 与 BTCC Web 两条产品线，平台间共享**规则 SSOT** 与**审查/术语/prompt 资产**，但 Figma 源锚点、组件细节、断点矩阵、触控目标等平台专属内容互不污染。

## 非目标

- 不拆为两个独立 skill（已与 han 确认，trigger 描述会模糊冲突，且会复制 SSOT）。
- 不在本次扩展 Web 的 `for-code-generation/` 内容（验证素材尚不充分）。
- 不动 `assets/btcc-tokens.*` 与 `assets/icons/*`，本次保留为 APP 派生值，留出 Web 接口点。
- 不动 `scripts/btcc_qa_lint.py` 的规则编码（仅在 lint 触及平台差异时再处理）。

## 决策

### D1. 目录骨架

```
skills/btcc-style-generator/
├── SKILL.md
├── references/
│   ├── rules.md                         # 平台无关 SSOT
│   ├── for-prompt-design/               # 平台无关
│   │   ├── prompt-evals.md
│   │   └── implementation-patterns.md
│   ├── for-review-and-qa/               # 平台无关
│   │   ├── qa.md
│   │   ├── golden-examples.md
│   │   └── data-format.md
│   ├── platform-app/
│   │   ├── rules-app.md                 # APP 专属规则（引用回 rules.md）
│   │   ├── for-figma-inspect/
│   │   │   ├── source-anchors.md
│   │   │   ├── contract-screens.md
│   │   │   └── icons.md
│   │   └── for-code-generation/
│   │       ├── components-trading.md
│   │       ├── components-account.md
│   │       ├── components-global.md
│   │       ├── tokens-colors.md
│   │       ├── tokens-size-typography.md
│   │       ├── pages-contract.md
│   │       └── pages-other.md
│   └── platform-web/
│       ├── rules-web.md                 # WEB 专属规则（引用回 rules.md）
│       └── for-figma-inspect/
│           └── source-anchors.md        # 仅 fileKey + canvas 0:1 verified anchor
├── agents/openai.yaml
├── assets/                              # 不动
└── scripts/                             # 不动
```

`for-prompt-design/` 与 `for-review-and-qa/` **不下沉**：两端共用 prompt 评测和 QA 流程，避免双向同步漂移。

### D2. SSOT 拆分

| 顶层 `rules.md` 保留                                 | `platform-app/rules-app.md` 引用并补充                       | `platform-web/rules-web.md` 引用并补充                                  |
| ---------------------------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------- |
| R-COLOR-1 / R-COLOR-2 颜色语义                       | —                                                            | —                                                                       |
| R-LAYOUT-1 首屏运营态                                | —                                                            | —                                                                       |
| R-NAME-1 / R-NAME-2 命名/术语                        | —                                                            | —                                                                       |
| R-ICON-1 图标来源顺序                                | —                                                            | —                                                                       |
| R-SCOPE-1 verified vs unverified（机制）             | APP verified 列表（`合约pro` / `合约pro-dark`）              | WEB verified 列表（canvas `0:1 设计规范`）+ 其它皆 Unverified           |
| R-SSOT-1 SSOT 纪律                                   | —                                                            | —                                                                       |
| R-SSOT-2 反模式列表                                  | —                                                            | —                                                                       |
| R-LAYOUT-2 数据密度与排版**通用部分**（tabular-nums、右对齐数值列、暗色优先派生亮色、最小化卡片化）| **R-LAYOUT-2-APP**：mobile gutters 16px、触控目标 40-44px | **R-LAYOUT-2-WEB**：断点 1024/1440/1556/1920、桌面密度、hover/focus、键鼠交互、滚动条策略 |

**约束**：`rules-app.md` 和 `rules-web.md` 中每条规则必须以 `Per rules.md R-XXX:` 格式开头，禁止独立发明与顶层冲突的新规则。新发明的平台规则需先写回顶层（如未来 R-A11Y-1 全局适用），不得在平台文件里创立 SSOT 之外的规则。

### D3. SKILL.md 路由

Required Workflow 第 1 步加平台识别：

```
1. Identify platform first (single platform per invocation):
   - "web" / "桌面" / "1920" / "1440" / "hover" → platform-web
   - "app" / "h5" / "合约pro" / "TabBar" / "移动端" → platform-app
   - 信号冲突或缺失时停下询问 han，不默认任一平台、不并行加载两侧。
2. Identify task class.
3. Load: rules.md + platform-<chosen>/rules-<chosen>.md + 任务对应 references。
4. 同一会话只允许在用户显式切换平台时才重新加载另一侧的 platform-* 文件。
```

Task→Files 表新增 `Platform` 列。每行至少给出一个平台值（`app` / `web` / `both`）。当前 `web` 行仅指向 `platform-web/for-figma-inspect/source-anchors.md` 与 `rules-web.md`，并显式标注：「Web code-generation 内容尚未填充；如需生成 Web 代码请先与 han 确认或在 Unverified 标记下生成」。

### D4. Web verified anchor 内容

`platform-web/for-figma-inspect/source-anchors.md` 在本次落盘以下事实（来自实际 Figma 元数据查询，验证日期 2026-05-28）：

- File: `新BTCC WEB`
- File key: `VrE25c6IAuIieWngebNnwx`
- Canvas `0:1 设计规范`（混合：按钮、输入、弹窗、下单、`合约pro` 桌面版下单组件 `651:14846 合约pro下单框`、`647:13104 盘口`、`647:12465 顶部导航条`、`663:2867 右侧选项` 等）
- Canvas `3089:7459 其他-马甲包官网/桌面图标`（unverified，标 `> Source: BTCC-style convention`）

WEB 文件无独立的 `合约pro` / `合约pro-dark` 顶层 canvas；按钮、Tab、下单等元素是 canvas `0:1` 内的子 frame。后续若需要细化为页面级 anchor，需 han 在 Figma 中标注页面边界。

### D5. 迁移映射

| 当前路径                                                                        | 新路径                                                                                              |
| ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `references/rules.md`                                                           | 保留位置；删除 R-LAYOUT-2 中 mobile 专属字句，标注其下沉到 `platform-app/rules-app.md`              |
| `references/for-figma-inspect/{source-anchors,contract-screens,icons}.md`       | `references/platform-app/for-figma-inspect/{同名}`                                                  |
| `references/for-code-generation/*.md`                                           | `references/platform-app/for-code-generation/*.md`                                                  |
| `references/for-review-and-qa/*.md`                                             | 不动（平台无关）                                                                                    |
| `references/for-prompt-design/*.md`                                             | 不动（平台无关）                                                                                    |
| —                                                                               | 新建 `references/platform-app/rules-app.md`                                                         |
| —                                                                               | 新建 `references/platform-web/rules-web.md`                                                         |
| —                                                                               | 新建 `references/platform-web/for-figma-inspect/source-anchors.md`                                  |

### D6. 路径引用同步范围

迁移后须 grep 仓库内所有引用并改写：

- `SKILL.md`
- `agents/openai.yaml`
- `README.md`（如有指向 `references/for-...` 的链接）
- `openspec/specs/btcc-skill-structure/spec.md`（更新 capability 契约）
- `scripts/btcc_qa_lint.py` 不引用 references 路径，但若涉及 R-LAYOUT-2 mobile 数值的硬编码需评估

### D7. assets 与 scripts 处理

- `assets/btcc-tokens.{json,css}`、`assets/icons/`、`scripts/btcc_qa_lint.py` **本次不动**。
- `platform-web/rules-web.md` 中加显式注释：「`assets/btcc-tokens.*` 当前为 APP 派生值，未与 Web Figma local variables 校对；Web 代码生成在确认 token 一致性之前应将 token 标为 Unverified 或要求 han 提供 Web token 抽取。」

## 失效风险与缓解

- **风险 1**：路径迁移漏改，旧引用断链。缓解：tasks 中加一条全仓 grep 校验，零命中（`scripts/btcc_qa_lint.py` 内的硬编码规则字符串例外）。
- **风险 2**：`rules-app.md` / `rules-web.md` 新增独立规则，破坏 R-SSOT-1。缓解：在两文件顶部写约束「本文件仅展开 rules.md 中的 R-* 规则在该平台的具体数值/约束，不得创立新规则」。
- **风险 3**：用户不指定平台时被 Claude 默认为 APP。缓解：SKILL.md Required Workflow 步骤 1 显式要求先确认平台。
- **风险 4**：现有 `openspec/specs/btcc-skill-structure/spec.md` 的 Requirements 与新结构冲突。缓解：本变更通过 OpenSpec delta 同步修改 capability spec（MODIFIED Requirements）。

## 验收标准

1. `references/` 直接子项恰为：`rules.md`、`for-prompt-design/`、`for-review-and-qa/`、`platform-app/`、`platform-web/`。
2. `platform-app/` 下含 `rules-app.md` + `for-figma-inspect/` + `for-code-generation/`，文件名/数量与现有 APP 内容一致。
3. `platform-web/` 下含 `rules-web.md` + `for-figma-inspect/source-anchors.md`，且 `for-code-generation/` 不存在。
4. `rules.md` R-LAYOUT-2 中不再出现 `16px gutter` / `40-44px` / `mobile` 字串。
5. `rules-app.md` / `rules-web.md` 中每条规则首行匹配 `Per rules.md R-`。
6. SKILL.md Task→Files 表含 `Platform` 列且每行有值。
7. Required Workflow 第 1 步包含平台识别提示。
8. 仓库 grep `references/for-figma-inspect/` 直连旧路径零命中（`docs/superpowers/specs/`、`openspec/changes/archive/` 历史文档可保留）。
9. OpenSpec `openspec validate` 对新 change 通过。

## 后续（不在本次范围）

- 拉取 Web Figma local variables，决定 token 是否复用 APP `btcc-tokens.{json,css}`。
- 填充 `platform-web/for-code-generation/` 下的 components / tokens / pages（需要 han 提供更细的 Web 验证页面或允许 Unverified 草稿）。
- 评估 `btcc_qa_lint.py` 是否需要 platform 维度，例如对 web 输出不应触发"触控目标 40-44px"的硬性检查。
- 评估是否需要把 R-COLOR / R-NAME 分离到 SSOT 子文件以便引用粒度更细。
