# BTCC Prompt Pack

## Purpose

Use this prompt pack to generate BTCC-style webpages and app-like web views. It pairs with `docs/btcc/btcc-design-system.md`, which is the source of truth for design tokens and component rules.

For repeatable generation, also follow `docs/btcc/btcc-generation-governance.md`. That file defines token naming, component-level fixed rules, icon registry, content terminology, responsive behavior, accessibility, motion, and QA gates.

The prompts below are designed for AI coding agents, UI generators, and design assistants. They should produce dense, operational exchange interfaces rather than generic crypto landing pages.

## Master System Prompt

```text
You generate BTCC-style web product interfaces for a crypto exchange.

The output must feel like a compact trading workspace: precise, technical, stateful, and operational. Prioritize market data, account state, trading controls, risk signals, and task completion over decoration.

Use the BTCC design system:
- Default to dark mode using BTCC semantic tokens.
- Preserve light-mode token mappings when a theme is requested.
- Use neutral surfaces, thin dividers, compact spacing, and tabular numbers.
- Use compact line icons that match the BTCC Figma source: 24px toolbar icons, 16px inline icons, and 10-14px selector/status icons.
- Use BTCC token governance: primitive tokens, semantic tokens, then component tokens. Do not hardcode component colors when a token exists.
- Use brand blue for primary neutral actions and selected states.
- Use green for positive, bid, profit, buy, and long states.
- Use red for negative, ask, loss, sell, short, error, and destructive states.
- Use warning orange and check gold only for their specific semantic states.
- Use tabs for major operational states and segmented controls for mode switches.
- Use tables, order-book rows, compact panels, and dense form controls for data-heavy areas.

Do not create a generic SaaS landing page, oversized marketing hero, decorative gradient page, soft editorial layout, or card-heavy brochure. Cards are allowed only for repeated modules or genuinely contained tools. Keep key product state visible in the first viewport.

If exact implementation details are missing, make conservative BTCC-style assumptions and explain only the necessary assumptions in code comments or final notes, not in visible app copy.
```

## Token Prompt Insert

Use this when the generator needs explicit colors:

```text
Use these BTCC semantic tokens as CSS custom properties:

Dark:
--btcc-bg-primary: #0c0f12;
--btcc-bg-secondary: #000000;
--btcc-bg-card: #13171b;
--btcc-bg-modal: #13171b;
--btcc-bg-toast: #212830;
--btcc-text-primary: #f1f3f5;
--btcc-text-secondary: #878f99;
--btcc-text-tertiary: #444d59;
--btcc-text-disabled: #3e4a59;
--btcc-divider-primary: #212830;
--btcc-divider-container: #2c3642;
--btcc-border-primary: #3e4a59;
--btcc-fill-container: #1a1f24;
--btcc-fill-input: #1a1f24;
--btcc-brand: #0c73ed;
--btcc-brand-pressed: #0b6adb;
--btcc-success: #2ca85d;
--btcc-success-pressed: #1b8248;
--btcc-error: #eb464f;
--btcc-error-pressed: #c4313d;
--btcc-warning: #e0601f;
--btcc-check: #f0b848;

Light:
--btcc-bg-primary: #ffffff;
--btcc-bg-secondary: #f1f2f5;
--btcc-bg-card: #f1f2f5;
--btcc-bg-modal: #ffffff;
--btcc-bg-toast: #40485b;
--btcc-text-primary: #13161c;
--btcc-text-secondary: #717c95;
--btcc-text-tertiary: #a6aec1;
--btcc-text-disabled: #959dad;
--btcc-divider-primary: #f1f2f5;
--btcc-divider-container: #dbdee6;
--btcc-border-primary: #dbdee6;
--btcc-fill-container: #f1f2f5;
--btcc-fill-input: #f1f2f5;
--btcc-brand: #195eff;
--btcc-brand-pressed: #1858f0;
--btcc-success: #2ca85d;
--btcc-success-pressed: #299c56;
--btcc-error: #eb464f;
--btcc-error-pressed: #e0434b;
--btcc-warning: #e0601f;
--btcc-check: #f0b848;
```

## General Page Prompt Template

```text
Create a BTCC-style {page_type} page for {audience_or_use_case}.

Functional requirements:
- {requirement_1}
- {requirement_2}
- {requirement_3}

Design requirements:
- Use the BTCC design system and semantic color tokens.
- Default to dark trading UI.
- Keep the first viewport operational: show product state, market/account data, and primary actions immediately.
- Use compact panels, tabs, segmented controls, dense tables, and clear action hierarchy.
- Use green/red only for directional market or transaction states.
- Use brand blue for primary neutral actions, selected states, and product emphasis.
- Use tabular numbers for prices, balances, percentages, quantities, and timestamps.
- Keep cards limited to repeated modules or true contained tools.
- Avoid decorative gradients, oversized hero typography, generic stock imagery, and marketing-first composition.

Interaction requirements:
- Include hover, active, selected, disabled, empty, and loading states where relevant.
- Ensure selected states do not rely on color alone.
- Ensure mobile and desktop layouts are both usable without clipped text.
```

## Contract Trading Page Prompt

```text
Create a BTCC-style contract trading page.

The first viewport must include:
- Top product navigation with USDT-M, Coin-M, Spot, and USDT-M Pro beta.
- Pair header for BTCUSDT Perp with price movement and chart/more actions.
- Main trading grid with chart or market area, order book, order entry form, and positions/orders/assets panel.
- Order entry controls: cross/isolated margin mode, leverage, Open/Close segmented control, Available balance, order type selector, price input, amount input, unit selector, percent slider, TP/SL control, risk estimate rows, Open Long and Open Short buttons.
- Order book with Price (USDT), Size (BTC), red ask rows, green bid rows, low-contrast depth bars, mid price, funding/countdown, and buy/sell ratio.
- Bottom or lower panel tabs for orders, positions, and assets.

Style:
- Use BTCC dark tokens.
- Use compact 24-32px data rows.
- Use 38-44px primary form buttons.
- Use green for long/buy and red for short/sell.
- Keep explanatory copy minimal and operational.
```

## Exchange Home Prompt

```text
Create a BTCC-style exchange home page.

The first viewport must communicate trading utility, not marketing brochure.

Include:
- Compact top navigation with product areas and account actions.
- Market snapshot strip with BTC, ETH, and top movers.
- Fast entry modules for Contract, Spot, Copy Trading, Wallet, and Deposit.
- Watchlist or market table with price, 24h change, volume, and action.
- Account state module for logged-out or low-balance users.

Style:
- Use dark BTCC workspace styling.
- Use compact cards only as repeated product modules.
- Keep the H1 practical if used; avoid a giant decorative slogan.
- Use market data as the primary visual signal.
```

## Market Page Prompt

```text
Create a BTCC-style market page.

Include:
- Category tabs for Favorites, Spot, USDT-M, Coin-M, and Top Movers.
- Search and filter controls.
- Dense market table with Pair, Last Price, 24h Change, High/Low, Volume, and Trade action.
- Positive and negative movement states using BTCC green/red.
- Optional compact sparkline column.

Style:
- Prioritize scanability and column alignment.
- Use tabular numbers.
- Keep rows dense and readable.
- Avoid large chart decorations unless tied to selected market detail.
```

## Wallet And Assets Prompt

```text
Create a BTCC-style wallet/assets page.

Include:
- Total balance summary with hidden-balance toggle.
- Deposit, Withdraw, Transfer, and History actions.
- Asset table with coin, available, frozen, total value, and row actions.
- Account/security or verification notice if useful.
- Transaction history tabs.

Style:
- Use neutral panels and compact tables.
- Use brand blue for neutral account actions.
- Use warning only for risk or incomplete verification states.
- Keep empty states actionable.
```

## Login And Register Prompt

```text
Create a BTCC-style login/register page.

Include:
- Compact auth form with email/phone, password, verification code if needed, and primary submit.
- Login/register switch.
- Security cues such as passkey, 2FA, or device trust when relevant.
- Product context through a small market/account panel, not a decorative hero.

Style:
- Calm, technical, and compact.
- Use brand blue for submit.
- Avoid oversized illustration-led auth pages.
- Keep copy short and functional.
```

## Copy Trading Prompt

```text
Create a BTCC-style copy trading page.

Include:
- Trader leaderboard with ROI, PnL, win rate, followers, risk level, and copy action.
- Filters for market, timeframe, risk, and strategy type.
- Strategy detail panel with performance chart and risk metrics.
- Copy setup control with amount, stop loss, and confirmation.

Style:
- Treat it as a financial operations page, not social media.
- Use dense ranking tables and compact metric panels.
- Use green/red for performance only.
```

## Modal And Bottom Sheet Prompt

```text
Create a BTCC-style {modal_or_sheet_name}.

Structure:
- Scrim using BTCC mask behavior.
- Surface using modal/sheet background token.
- Header with concise title and close action.
- State summary first.
- Controls second.
- Explanation or helper copy last.
- Primary action fixed or visually stable.

For mobile bottom sheets:
- Use top drag handle.
- Use rounded top corners.
- Keep content dense and thumb-friendly.

Avoid:
- Long paragraphs.
- Decorative empty illustrations unless explicitly requested.
- Actions that move when validation messages appear.
```

## Component-Level Prompt Snippets

### Icons And Assets

```text
Use BTCC-style utility icons. Prefer existing Figma assets when the Figma plugin is available. Match the source icon language: compact stroke-based icons, 24px for toolbar/navigation actions, 16px for inline pair or unit controls, and 10-14px for chevrons/warnings/status markers.

Use these observed icon roles where relevant:
- bar-chart-square-down for market stats.
- k-line/candlestick icon for chart access.
- more icon for overflow actions.
- plus-circle for adding funds or quick balance actions.
- warning-circle for risk and information prompts.
- file/order icon for orders, history, or empty operational state.
- deposit, transfer, and demo-trading icons for account shortcuts.
- home, discover, copy, assets, trade icons for app navigation.

Do not invent colorful decorative icon sets. If source icons are unavailable in code, use a visually similar line icon library and keep stroke, size, and color restrained.
```

### Tabs

```text
Use tabs for major operational states. Active tabs must use text weight plus brand/underline/fill state, not color alone. Keep tab labels short and include counts when useful, such as orders(0), positions(0), assets.
```

### Segmented Controls

```text
Use segmented controls for mutually exclusive modes such as Open/Close, Limit/Market/Trigger, Cross/Isolated, or time range. Keep them compact and visually attached.
```

### Order Book

```text
Use a dense order book with ask rows above, bid rows below, mid price between them, low-contrast depth bars behind quantities, and tabular numeric alignment. Ask is red/error; bid is green/success.
```

### Trading Form

```text
Use a compact trading form with available balance, order type, price, amount, slider, TP/SL, risk rows, and directional actions. Long/buy actions use green; short/sell actions use red; neutral submit actions use brand blue.
```

### Empty State

```text
Use compact empty states. Show the state, then the next useful action. Avoid large illustrations. For account or trading empties, offer Deposit, Transfer, Demo trading, or Select pair as appropriate.
```

## Negative Prompt

```text
Do not make this look like:
- A generic crypto marketing landing page.
- A SaaS dashboard with soft pastel cards.
- A purple/blue gradient hero page.
- A beige editorial finance site.
- A playful gamified app.
- A sparse website with oversized headings and little data.
- A card stack where every page section is a floating card.
- A page where the main trading/account action is below the fold.
- A page where color is decorative rather than semantic.
- A page where text overlaps, table numbers misalign, or dense controls wrap awkwardly.
```

## Self-Review Prompt

Use this after generating a BTCC-style page:

```text
Review the generated page against the BTCC design system.

Check:
1. Does the first viewport show product, market, account, or trading state immediately?
2. Are BTCC semantic tokens used instead of arbitrary colors?
3. Is dark mode the default, and is light mode token-ready if requested?
4. Are blue, green, red, warning, and check colors used only for their semantic roles?
5. Are trading controls compact and close to the data they affect?
6. Are tabs used for major states and segmented controls for modes?
7. Are tables/order-book rows dense, aligned, and numeric with tabular figures?
8. Are cards limited to repeated modules or true contained tools?
9. Are empty, disabled, selected, hover, active, and loading states handled?
10. Is there any marketing hero, decorative gradient, oversized type, clipped text, overlap, or generic dashboard styling that violates BTCC?

Return only actionable fixes, ordered by severity.
```

## Implementation Guardrails For Coding Agents

When using this prompt pack in a codebase:

- Read the existing project structure and component system first.
- If the Figma plugin is available, inspect the BTCC file for existing icons, components, variables, and styles before recreating assets.
- Follow `btcc-generation-governance.md` for token naming, icon fallback mapping, content terms, responsive behavior, motion, and QA.
- Reuse existing components and tokens when present.
- Add BTCC tokens in one theme file or CSS layer, not scattered across components.
- Prefer project/Figma-matched icons over unrelated icon packs; use line-icon fallbacks only when needed.
- Prefer CSS custom properties for theme switching.
- Use responsive grids with stable min/max widths for trading panels.
- Verify with desktop and mobile screenshots.
- Check that table text, buttons, tabs, and compact controls do not overlap.
- Do not add visible instructions explaining how to use the page unless the product flow requires it.
