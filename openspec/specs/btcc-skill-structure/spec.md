# btcc-skill-structure Specification

## Purpose
TBD - created by archiving change restructure-btcc-skill-by-role. Update Purpose after archive.
## Requirements
### Requirement: Directory Skeleton Under references/
The `skills/btcc-style-generator/references/` directory SHALL contain exactly five direct children: the file `rules.md`, and the four role subdirectories `for-figma-inspect/`, `for-code-generation/`, `for-review-and-qa/`, and `for-prompt-design/`. Any sibling entry that is not a member of this set is non-conformant. Loose `.md` files placed directly under `references/` (other than `rules.md`) MUST NOT exist.

#### Scenario: Sixth top-level entry appears
- **WHEN** a reviewer lists `references/` and finds a sixth direct child such as `references/notes/` or `references/legacy.md`
- **THEN** the structure is non-conformant and SHALL be rejected

#### Scenario: Stray markdown file under references/
- **WHEN** any `.md` file other than `rules.md` is found directly under `references/` (for example `references/components.md`)
- **THEN** the structure is non-conformant and the file MUST be moved into one of the four role subdirectories or deleted

### Requirement: Single Source of Truth Rules File
`references/rules.md` SHALL be the single authoritative source of the BTCC golden rules. It MUST cover at minimum: the `Open Long` uses `--btcc-brand` and `Open Short` uses `--btcc-error` direction rule, dark-first defaults, tabular numbers for numeric data, the prohibition on large hero marketing blocks, and the constraint that red and green are reserved for state and numeric semantics rather than decoration. No other file under `references/` SHALL re-state these rules as prescriptive declarations; they MAY only reference `rules.md`.

#### Scenario: Rule duplicated in a sibling file
- **WHEN** a sibling such as `for-review-and-qa/qa.md` re-states "Open Long uses brand color" as its own rule rather than citing `rules.md`
- **THEN** the structure is non-conformant and the duplicated declaration MUST be replaced by a reference to `rules.md`

#### Scenario: Direction rule missing from rules.md
- **WHEN** `references/rules.md` is absent, or its content omits the `Open Long` / `Open Short` color direction rule
- **THEN** the structure is non-conformant

### Requirement: for-figma-inspect Directory Contents
`references/for-figma-inspect/` SHALL contain exactly three files whose responsibilities are bounded as follows: `source-anchors.md` SHALL hold raw Figma anchors (file key, page name, component-set name); `contract-screens.md` SHALL hold the `合约pro` sub-screen node index; `icons.md` SHALL hold icon roles paired with Figma clues. Token numeric tables, component layout specs, and code-generation guidance MUST NOT appear in this directory.

#### Scenario: All three files aligned with their responsibilities
- **WHEN** the directory contains `source-anchors.md`, `contract-screens.md`, and `icons.md`, each scoped to its declared responsibility
- **THEN** the directory is conformant

#### Scenario: Token tables placed under for-figma-inspect/
- **WHEN** a token numeric table appears in any file under `for-figma-inspect/`
- **THEN** the structure is non-conformant and the table MUST be relocated into `for-code-generation/`

### Requirement: for-code-generation Directory Splits
`references/for-code-generation/` SHALL split components, tokens, and pages into multiple subtopic files rather than monolithic single files. The required file set is: `components-trading.md`, `components-account.md`, `components-global.md`, `tokens-colors.md`, `tokens-size-typography.md`, `pages-contract.md`, `pages-other.md`. Each component file SHALL stay within approximately 120 lines as a soft cap; any component file exceeding 120 lines MUST carry an explicit justification at the top.

#### Scenario: Monolithic components file present
- **WHEN** a single `components.md` simultaneously documents trading form, wallet, and global navigation components
- **THEN** the structure is non-conformant and MUST be split into `components-trading.md`, `components-account.md`, and `components-global.md`

#### Scenario: Mixed token concerns in one file
- **WHEN** `tokens-colors.md` also contains size scales or typography rules
- **THEN** the structure is non-conformant and the size and typography content MUST live in `tokens-size-typography.md`

### Requirement: for-review-and-qa Directory Contents
`references/for-review-and-qa/` SHALL contain three review-focused files: `qa.md`, `golden-examples.md`, and `data-format.md`. These files SHALL cite `rules.md` when checking against golden rules and MUST NOT re-declare those rules as their own.

#### Scenario: QA checklist cites rules.md correctly
- **WHEN** `qa.md` references the direction rule by linking to `rules.md` rather than restating it
- **THEN** the file is conformant

#### Scenario: QA file re-declares a golden rule
- **WHEN** `qa.md` contains a prescriptive line such as "Open Long must use --btcc-brand" without referencing `rules.md`
- **THEN** the structure is non-conformant

### Requirement: for-prompt-design Directory Contents
`references/for-prompt-design/` SHALL contain exactly `prompt-evals.md` and `implementation-patterns.md`. These files MUST serve only prompt-design and AI-output-wrapping concerns, and MUST NOT duplicate component specs or token tables that belong in `for-code-generation/`.

#### Scenario: Color rule list placed inside prompt-evals.md
- **WHEN** `prompt-evals.md` contains a list of color tokens or restates the long/short direction rule
- **THEN** the structure is non-conformant and the content MUST be removed in favor of a reference to `rules.md`

### Requirement: SKILL.md Reverse Index Table
`SKILL.md` SHALL provide a "task to files" mapping table at a prominent location either immediately after the Overview section or adjacent to the Required Workflow section. The table SHALL cover at least eight invocation classes: generating a contract page, changing the order button color, adding a leverage picker, reviewing AI output, designing a prompt, inspecting a Figma node, modifying a token, and adding a new page.

#### Scenario: User looks up "change order button color"
- **WHEN** a user reads the SKILL.md index for the task "change order button color"
- **THEN** the table SHALL direct them to `references/rules.md` and `references/for-code-generation/components-trading.md`, and SHALL NOT direct them to the deprecated `page-matrix.md`

#### Scenario: Index covers fewer than eight task classes
- **WHEN** the reverse index table covers seven or fewer invocation classes
- **THEN** the table is non-conformant and MUST be expanded to cover at least the eight required classes

### Requirement: Removal of Redundant Long-form Documents
The files `docs/btcc/btcc-design-system.md`, `docs/btcc/btcc-prompt-pack.md`, and `docs/btcc/btcc-generation-governance.md` SHALL NOT exist in the repository after the restructure. The skill MUST NOT contain any link or path reference targeting `docs/btcc/*`.

#### Scenario: Legacy long-form doc still present
- **WHEN** `docs/btcc/btcc-design-system.md` continues to exist on disk
- **THEN** the structure is non-conformant and the file MUST be deleted

#### Scenario: SKILL.md links to docs/btcc/*
- **WHEN** `SKILL.md` retains a link such as `docs/btcc/btcc-prompt-pack.md`
- **THEN** the structure is non-conformant and the link MUST be removed or repointed into the new role-based structure

### Requirement: Zero Tolerance for Broken Path References
After the restructure, every repository-wide reference to legacy `references/` paths (including `references/components.md`, `references/tokens.md`, and `references/page-matrix.md`) SHALL be migrated to the new role-based paths. A repository-root grep for these legacy paths MUST return zero hits, with the sole exception of hardcoded rule strings inside `scripts/btcc_qa_lint.py`, which acts as the runtime enforcer of the rules and is not a path reference.

#### Scenario: Grep for legacy references path
- **WHEN** `grep -r "references/components.md" .` is executed from the repository root
- **THEN** it SHALL return zero hits

#### Scenario: agents/openai.yaml retains a legacy path
- **WHEN** `agents/openai.yaml` still contains `references/components.md`
- **THEN** the structure is non-conformant and the path MUST be updated to the corresponding new file under `for-code-generation/`

### Requirement: Figma and Token Assets Stay In Place
The paths `assets/btcc-tokens.css`, `assets/btcc-tokens.json`, `assets/icons/`, and `scripts/btcc_qa_lint.py` SHALL remain unchanged by this restructure to preserve external consumer compatibility. Token assets MUST NOT be relocated under `references/`.

#### Scenario: Token CSS path preserved
- **WHEN** `assets/btcc-tokens.css` continues to live at its original path after the restructure
- **THEN** the structure is conformant for that asset

#### Scenario: Tokens moved into references/
- **WHEN** `assets/btcc-tokens.json` is relocated to `references/for-code-generation/btcc-tokens.json`
- **THEN** the structure is non-conformant and the asset MUST be moved back to `assets/`

