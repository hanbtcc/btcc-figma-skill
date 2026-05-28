## MODIFIED Requirements

### Requirement: Directory Skeleton Under references/
The `skills/btcc-style-generator/references/` directory SHALL contain exactly five direct children: the file `rules.md`, the two cross-platform role subdirectories `for-prompt-design/` and `for-review-and-qa/`, and the two platform subdirectories `platform-app/` and `platform-web/`. Any sibling entry that is not a member of this set is non-conformant. Loose `.md` files placed directly under `references/` (other than `rules.md`) MUST NOT exist. The legacy top-level role directories `for-figma-inspect/` and `for-code-generation/` MUST NOT continue to exist directly under `references/`; their content lives under `platform-app/` after the platform split.

#### Scenario: Sixth top-level entry appears
- **WHEN** a reviewer lists `references/` and finds a sixth direct child such as `references/notes/` or `references/legacy.md`
- **THEN** the structure is non-conformant and SHALL be rejected

#### Scenario: Legacy role directory survives at top level
- **WHEN** `references/for-figma-inspect/` or `references/for-code-generation/` still exists directly under `references/` after the platform split
- **THEN** the structure is non-conformant and the directory MUST be removed; its content MUST live under `platform-app/`

#### Scenario: Stray markdown file under references/
- **WHEN** any `.md` file other than `rules.md` is found directly under `references/` (for example `references/components.md`)
- **THEN** the structure is non-conformant and the file MUST be moved into one of the four subdirectories or deleted

### Requirement: Single Source of Truth Rules File
`references/rules.md` SHALL be the single authoritative source of the BTCC golden rules and SHALL hold only platform-agnostic rules. It MUST cover at minimum: the `Open Long` uses `--btcc-brand` and `Open Short` uses `--btcc-error` direction rule, dark-first defaults, tabular numbers for numeric data, the prohibition on large hero marketing blocks, and the constraint that red and green are reserved for state and numeric semantics rather than decoration. It MUST NOT contain mobile-specific or web-specific concretizations such as `mobile gutters`, `40-44px touch target`, breakpoint pixel widths, or hover-state language; those concretizations live in `platform-app/rules-app.md` and `platform-web/rules-web.md` respectively. No other file under `references/` SHALL re-state the platform-agnostic rules as prescriptive declarations; they MAY only reference `rules.md`.

#### Scenario: Mobile gutter clause survives in rules.md
- **WHEN** `references/rules.md` still contains the literal string `Mobile gutters MUST be 16px` or `touch targets MUST be 40-44px`
- **THEN** the structure is non-conformant and the clause MUST be moved into `platform-app/rules-app.md` under `R-LAYOUT-2-APP`

#### Scenario: Rule duplicated in a sibling file
- **WHEN** a sibling such as `for-review-and-qa/qa.md` re-states "Open Long uses brand color" as its own rule rather than citing `rules.md`
- **THEN** the structure is non-conformant and the duplicated declaration MUST be replaced by a reference to `rules.md`

#### Scenario: Direction rule missing from rules.md
- **WHEN** `references/rules.md` is absent, or its content omits the `Open Long` / `Open Short` color direction rule
- **THEN** the structure is non-conformant

### Requirement: SKILL.md Reverse Index Table
`SKILL.md` SHALL provide a "task to files" mapping table at a prominent location either immediately after the Overview section or adjacent to the Required Workflow section. The table SHALL cover at least eight invocation classes: generating a contract page, changing the order button color, adding a leverage picker, reviewing AI output, designing a prompt, inspecting a Figma node, modifying a token, and adding a new page. The table SHALL include a `Platform` column whose value for every row is one of `app`, `web`, or `both`. Rows whose Role column resolves to `for-code-generation` or `for-figma-inspect` MUST cite a `platform-app/...` or `platform-web/...` path for that role's files; cross-platform rows (Role `for-review-and-qa` / `for-prompt-design`) MAY cite the unprefixed `references/for-...` paths.

#### Scenario: User looks up "change order button color" on mobile
- **WHEN** a user reads the SKILL.md index for the task "change order button color" with platform `app`
- **THEN** the table SHALL direct them to `references/rules.md`, `references/platform-app/rules-app.md`, and `references/platform-app/for-code-generation/components-trading.md`, and SHALL NOT direct them to the deprecated top-level `for-code-generation/components-trading.md`

#### Scenario: Index covers fewer than eight task classes
- **WHEN** the reverse index table covers seven or fewer invocation classes
- **THEN** the table is non-conformant and MUST be expanded to cover at least the eight required classes

### Requirement: Zero Tolerance for Broken Path References
After the platform split, every repository-wide reference to legacy `references/for-figma-inspect/*` and `references/for-code-generation/*` paths SHALL be migrated to the corresponding `references/platform-app/...` location (or, where applicable, `references/platform-web/...`). A repository-root grep for these legacy top-level paths MUST return zero hits, with the following exemptions: hardcoded rule strings inside `scripts/btcc_qa_lint.py`; archived OpenSpec changes under `openspec/changes/archive/`; and historical narrative documents under `docs/superpowers/specs/` and `docs/superpowers/plans/`.

#### Scenario: Grep for legacy for-figma-inspect path
- **WHEN** `grep -rn "references/for-figma-inspect/" .` is executed from the repository root with the exemptions above excluded
- **THEN** it SHALL return zero hits

#### Scenario: README retains a legacy path
- **WHEN** the repository root `README.md` still contains `references/for-code-generation/components-trading.md`
- **THEN** the structure is non-conformant and the path MUST be updated to `references/platform-app/for-code-generation/components-trading.md`

## ADDED Requirements

### Requirement: Platform Subdirectory Layout
`references/platform-app/` SHALL contain exactly three direct children: the file `rules-app.md`, the subdirectory `for-figma-inspect/` (with `source-anchors.md`, `contract-screens.md`, `icons.md`), and the subdirectory `for-code-generation/` (with the seven files `components-trading.md`, `components-account.md`, `components-global.md`, `tokens-colors.md`, `tokens-size-typography.md`, `pages-contract.md`, `pages-other.md`). `references/platform-web/` SHALL contain exactly two direct children: the file `rules-web.md` and the subdirectory `for-figma-inspect/` containing at least `source-anchors.md`. `references/platform-web/for-code-generation/` MUST NOT exist until web-side verification material is added under a future change; its absence is conformant.

#### Scenario: platform-app missing rules-app.md
- **WHEN** `references/platform-app/` does not contain `rules-app.md`
- **THEN** the structure is non-conformant

#### Scenario: platform-web prematurely contains code-generation files
- **WHEN** `references/platform-web/for-code-generation/` exists with any `.md` file before a future change formally introduces it
- **THEN** the structure is non-conformant and the directory MUST be removed

#### Scenario: platform-web missing source-anchors.md
- **WHEN** `references/platform-web/for-figma-inspect/source-anchors.md` is absent
- **THEN** the structure is non-conformant

### Requirement: Platform Rules Files Reference SSOT
Every prescriptive bullet inside `references/platform-app/rules-app.md` and `references/platform-web/rules-web.md` SHALL begin with the literal prefix `Per rules.md R-` followed by the parent rule identifier from `references/rules.md`, optionally with a profile qualifier (e.g. `Per rules.md R-LAYOUT-2 (mobile profile):`). These files MUST NOT introduce a brand-new rule identifier that does not exist in `rules.md`; new globally-applicable rules MUST first be added to `rules.md` before being referenced here. Section headings of the form `## R-XXX-APP:` or `## R-XXX-WEB:` are permitted as platform-scoped extensions of an existing parent `R-XXX` rule, but MUST NOT introduce semantics absent from the parent rule.

#### Scenario: Platform rule file invents a new rule
- **WHEN** `platform-app/rules-app.md` declares `## R-MOBILE-NEW-1: ...` whose identifier does not appear anywhere in `rules.md`
- **THEN** the structure is non-conformant and the rule MUST either be promoted into `rules.md` first, or removed

#### Scenario: Platform rule bullet missing SSOT citation
- **WHEN** a bullet in `rules-web.md` reads `Hover states MUST be defined for all interactive controls.` without the `Per rules.md R-` prefix
- **THEN** the structure is non-conformant and the bullet MUST be rewritten with an explicit `Per rules.md R-LAYOUT-2 (web profile):`-style prefix

#### Scenario: Platform-scoped extension heading bound to parent rule
- **WHEN** `platform-app/rules-app.md` contains `## R-LAYOUT-2-APP: Mobile Density and Touch` whose bullets all cite `Per rules.md R-LAYOUT-2 (mobile profile):`
- **THEN** the file is conformant for that section

### Requirement: SKILL.md Platform Identification Step
The first step of `skills/btcc-style-generator/SKILL.md` `Required Workflow` SHALL require the agent to identify a single target platform (one of `app` or `web`) before loading any task-specific reference file. The step SHALL list at least two disambiguation cues per platform (for example `web` / `桌面` / `1920` / `1440` / `hover` for web; `app` / `h5` / `合约pro` / `TabBar` / `移动端` for app). The step SHALL explicitly require that, when platform signals are missing or conflicting, the agent stops and asks the user, MUST NOT default to either platform, and MUST NOT load both `platform-app/` and `platform-web/` reference files in parallel within a single task. Subsequent workflow steps SHALL load `references/rules.md` together with `references/platform-<chosen>/rules-<chosen>.md` and only the task-specific files for the chosen platform.

#### Scenario: Required Workflow lacks platform identification
- **WHEN** the first step of `Required Workflow` jumps directly to identifying the task class without naming a platform identification step
- **THEN** the structure is non-conformant and a platform-first step MUST be added

#### Scenario: Workflow allows defaulting to APP on ambiguity
- **WHEN** the platform identification step contains language permitting "default to app" on missing signals
- **THEN** the structure is non-conformant; the step MUST require stopping to ask the user

#### Scenario: Workflow allows parallel loading of both platforms
- **WHEN** any workflow step instructs the agent to load `platform-app/` and `platform-web/` reference files together within one task
- **THEN** the structure is non-conformant; loading SHALL be platform-scoped

### Requirement: SKILL.md Task Index Has Platform Column
The `Task → Files` reverse-index table in `skills/btcc-style-generator/SKILL.md` SHALL include a column literally named `Platform`. Every data row of the table SHALL populate that column with one of the values `app`, `web`, or `both`. Rows annotated `web` MUST cite at least `references/platform-web/rules-web.md` and `references/platform-web/for-figma-inspect/source-anchors.md`. Rows annotated `app` whose Role column resolves to `for-code-generation` or `for-figma-inspect` MUST cite paths under `references/platform-app/...`. At least one row in the table SHALL be annotated `web` and SHALL carry a notice that web `for-code-generation` content is not yet filled.

#### Scenario: Task table missing Platform column
- **WHEN** the table header omits a column named `Platform`
- **THEN** the structure is non-conformant; the column MUST be added and every row populated

#### Scenario: Web row points to APP files
- **WHEN** a row annotated `web` cites `references/platform-app/for-code-generation/...` as a primary file
- **THEN** the structure is non-conformant and the row MUST cite `platform-web/...` files instead, or be re-annotated

#### Scenario: No web row exists
- **WHEN** the table contains only `app` and `both` rows with zero `web` rows
- **THEN** the structure is non-conformant; at least one `web` row MUST exist
