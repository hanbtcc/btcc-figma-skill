# BTCC Golden Rules (SSOT)

This file is the **single source of truth** for the BTCC style-generator skill's golden rules. Every other file under `skills/btcc-style-generator/references/` MAY reference these rules, but MUST NOT re-state them as prescriptive declarations. If a rule needs to change, change it here first, then propagate references.

## Ownership Principle

When deciding which file owns a piece of content, ask: **"who is the primary writer that triggers an update?"**

- A change to direction-color, dark-first, naming, or scope-disclosure rules should originate here, in `rules.md`. Multiple downstream files consume these rules → SSOT.
- A change to a token's hex value originates from a code-generation or design-source-sync action → owned by `for-code-generation/tokens-*.md`.
- A change to a `合约pro` sub-screen node ID originates from re-running Figma metadata → owned by `for-figma-inspect/contract-screens.md`.
- A change to a QA checklist item's wording originates from a review-process tweak → owned by `for-review-and-qa/qa.md`, but its rule basis MUST link back here.

If a rule, once edited, would need synchronous edits in ≥2 role files, it belongs here.

## R-COLOR-1: Direction Buttons (BTCC overrides the western convention)

In BTCC `合约pro` the action button colors are reversed from the common "long=green / short=red" convention. Numeric semantics still follow the convention; only the button surface differs.

- `Open Long` button MUST use `fill/Brand` (`--btcc-brand`, blue). Pressed state MUST use `fill/Brand Button/Pressed` (`--btcc-button-brand-bg-pressed`).
- `Open Short` button MUST use `fill/Error` (`--btcc-error`, red). Pressed state MUST use `fill/Red Button Pressed` (`--btcc-error-pressed`).
- Numeric direction cues — bid rows, percent change, pnl text, profit/loss numbers — MUST keep `fill/Success` for positive and `fill/Error` for negative.
- Do NOT switch the long button to green to "match" surrounding green pnl text. The verified Figma source `合约pro-dark` (`3112:1423`) paints long blue.

## R-COLOR-2: Color is Status, Not Decoration

Reserve red and green for state and numeric semantics. Do not use them for decorative emphasis.

- Brand blue: primary neutral actions, selected states, the long-direction button.
- Red (`fill/Error`): sell, short, ask, loss, negative, error, destructive, the short-direction button.
- Green (`fill/Success`): profit, bid depth, positive change, success toasts. NOT for the long button.
- Warning orange (`fill/Warning`): liquidation risk, abnormal status.
- Yellow (`fill/check`): funding / check / limited reward highlight.

## R-LAYOUT-1: Operational State First

Generated BTCC pages MUST surface product / market / account / trading state in the first viewport.

- No marketing hero, gradient banner, or inspirational crypto copy on operational surfaces.
- Trading pages MUST keep order form and order book reachable without leaving the first pattern.
- Wallet / account pages MUST show balance summary and primary fund actions on first paint.

## R-LAYOUT-2: Density and Type

- Default to dark mode. Light mode is dark-derived; do not author per-component light hexes.
- Compact spacing, dense rows, thin neutral dividers, restrained borders.
- Numeric columns MUST use `font-variant-numeric: tabular-nums`.
- Right-align numeric columns; left-align pair / asset / status / action labels.
- Card surfaces only for repeated modules or genuinely contained tools — not for every section.
- Platform-specific extensions of this rule (mobile gutters / touch targets / web breakpoints / hover) live in `platform-app/rules-app.md` and `platform-web/rules-web.md`.

## R-ICON-1: Icon Source Order

1. Search the BTCC Figma file first.
2. Prefer in-file icon nodes / component instances / copied vectors.
3. In code, prefer the local SVGs in `skills/btcc-style-generator/assets/icons/` for known BTCC utility roles.
4. Wrap into the project's icon component when one exists.
5. Use a generic line-icon fallback only when no source asset is available.

Style:

- Stroke icons with restrained weight, visually around 1.5-2px at 24px.
- Bind color to text/icon tokens; active nav uses brand emphasis; disabled uses `text | icon/disable`.
- Do not mix colorful illustrative icons or emoji into trading controls.
- Icon-only buttons MUST carry an accessible label in code (`aria-label` / `title`).

## R-NAME-1: Naming Conventions

- File naming: kebab-case (`components-trading.md`, `tokens-colors.md`).
- Role directories: `for-figma-inspect/`, `for-code-generation/`, `for-review-and-qa/`, `for-prompt-design/`.
- CSS custom properties: `--btcc-<group>-<role>` (`--btcc-text-primary`, `--btcc-button-brand-bg-pressed`).
- Token aliases in docs: keep the original Figma label in backticks (`fill/Brand`, `text | icon/secondary`) when mapping to code tokens.
- Component anatomy headings: lowercase trading vocabulary (`Trading Form`, `Order Book`, `TP/SL Bottom Sheet`), not generic UI labels.

## R-NAME-2: Trading Vocabulary

Use BTCC's stable trading terms. Avoid verbose educational text in trading panels.

- Preferred labels: `Open Long`, `Open Short`, `Limit`, `Market`, `TP/SL`, `Available`, `Margin`, `Order Book`, `Recent Trades`, `Positions(0)`, `Open Orders(0)`, `Assets`, `Deposit`, `Transfer`, `Withdraw`, `Demo`, `Perp`.
- Empty values: `--`, balances `0.0000 USDT`, percent `+0.0100%`, countdown `HH:MM:SS`, leverage `100x`.

## R-SCOPE-1: Verified vs Unverified Content

The skill MUST visibly distinguish content backed by verified Figma source from content offered as BTCC-style convention.

Verified anchors are tracked per platform: see `platform-app/for-figma-inspect/source-anchors.md` for the BTCC APP file and `platform-web/for-figma-inspect/source-anchors.md` for the BTCC WEB file. The anchor lists below remain as historical record for the APP file specifically.

Verified anchors (re-verify if older than ~30 days):

- Figma file `新BTCC APP`, key `GW9kMfpf0Nib5DG4TjoWBp`.
- Verified pages: `设计规范` (`0:1`), `合约pro` (`1262:304`), `合约pro-dark` (`3112:1423`).

Unverified surfaces (treat as convention; re-verify before relying on them in production): `home`, `markets`, `wallet/assets`, `auth`, `copy-trading`, `spot`, `c2c`, `h5`, `全局组件`, `图标`, `换色`, `老合约`, `TradFi`, `我的、设置`, `卡券/体验金`, `支付通道、NFT、提现`, `观点`.

When generating UI for an unverified surface, files MUST:

1. Carry an "Unverified / 未验证" marker at the top of the page-level section.
2. Use the placeholder line: `> Source: BTCC-style convention; not in verified Figma metadata pass.`
3. Mention this fact in the agent's final report (per `for-review-and-qa/qa.md`).

## R-SSOT-1: SSOT Discipline

- This file (`rules.md`) is the only place where the rules above appear as prescriptions.
- Other reference files MAY paraphrase context but MUST cite back here when stating a rule, e.g. `(see rules.md R-COLOR-1)`.
- Token numeric tables, component anatomy, page layout specs, Figma anchor tables, QA checklists, and prompt evals are NOT golden rules — they are role-owned content and MUST live in their respective role directories.
- Generated implementations downstream of this skill (e.g. `scripts/btcc_qa_lint.py`) are runtime enforcers of these rules; they may re-encode the rules as code, but MUST keep semantic parity with this file. When changing a rule, edit `rules.md` first, then the script.

## R-SSOT-2: Common Mistakes (anti-patterns the rules above prevent)

These exist as a quick negative-checklist. They are not new rules; each one is a violation of an R- rule above.

- Turning the UI into a generic crypto marketing landing page → violates R-LAYOUT-1.
- Coloring `Open Long` green by default → violates R-COLOR-1.
- Coloring `Open Short` anything other than red → violates R-COLOR-1.
- Using green/red as decoration → violates R-COLOR-2.
- Hiding trading/account actions below the fold → violates R-LAYOUT-1.
- Making every section a floating card → violates R-LAYOUT-2.
- Forgetting tabular numbers for prices and balances → violates R-LAYOUT-2.
- Replacing BTCC utility icons with colorful decorative icons → violates R-ICON-1.
- Generating an "unverified" page without the unverified marker → violates R-SCOPE-1.
- Using `--primary` / `--accent` / arbitrary hex inside BTCC surfaces → violates R-NAME-1 and R-COLOR-2.
