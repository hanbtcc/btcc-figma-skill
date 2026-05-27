# BTCC Design System

## Source And Scope

This document freezes the reusable BTCC app design rules extracted from the Figma file `新BTCC APP` on 2026-05-27.

Use it for BTCC-style web pages, mobile-inspired responsive pages, trading terminals, account pages, wallet pages, login/register flows, and future Codex skills. The source design is app-first, especially the `合约pro` page, so web output should adapt the same density, token logic, and component grammar rather than copying mobile dimensions literally.

## Design Thesis

BTCC UI should feel like a crypto exchange workspace: compact, operational, precise, and stateful. Data, risk, order actions, balance state, and navigation must be visible before decorative content. The default personality is technical and calm, with strong emphasis on price movement, order state, and account actions.

Do not turn BTCC pages into marketing landing pages unless the user explicitly asks for marketing. Even then, the first viewport should still signal exchange utility through market data, trading entry points, wallet/account actions, or product modules.

## Figma Structure

The source file contains these relevant pages:

| Page | Purpose |
| --- | --- |
| `设计规范` | Primary token and color specification page. |
| `全局组件` | Global component holding area. |
| `图标` | Icon inventory page. |
| `换色` | Theme/color-change exploration. |
| `首页` | Home patterns. |
| `资产` | Assets and wallet patterns. |
| `行情` | Market patterns. |
| `老合约` | Legacy contract patterns. |
| `TradFi` | TradFi feature patterns. |
| `合约pro` | Main contract trading reference. |
| `现货` | Spot trading patterns. |
| `跟单` | Copy trading patterns. |
| `登录注册` | Auth patterns. |
| `我的、设置` | Profile and settings patterns. |
| `卡券/体验金` | Coupons and trial-fund patterns. |
| `支付通道、NFT、提现` | Payments, NFT, withdrawal patterns. |
| `C2C` | C2C patterns. |
| `观点` | Content/opinion patterns. |
| `h5` | Mobile web patterns. |

## Token Philosophy

Use semantic tokens first. Do not start from arbitrary hex values when a BTCC token exists.

The Figma file has two local variable collections:

| Collection | Role |
| --- | --- |
| `变量合集` | Semantic dark/light tokens for text, backgrounds, dividers, borders, fills, alerts, and buttons. |
| `梯度色板` | Primitive gray ramps used by semantic tokens. |

When implementing web CSS, preserve semantic names as custom properties where possible, for example `--btcc-bg-primary`, `--btcc-text-primary`, `--btcc-fill-brand`.

## Semantic Color Tokens

### Text And Icon

| Token | Dark | Light | Usage |
| --- | --- | --- | --- |
| `text-icon-primary` | `#F1F3F5` | `#13161C` | Primary labels, prices, major icons. |
| `text-icon-secondary` | `#878F99` | `#717C95` | Secondary labels, metadata, supporting values. |
| `text-icon-tertiary` | `#444D59` | `#A6AEC1` | Placeholder text, weakest captions, inactive helper copy. |
| `text-icon-white` | `#FFFFFF` | `#FFFFFF` | Pure white text/icons on dark or colored fills. |
| `text-icon-black` | `#000000` | `#000000` | Pure black text/icons where required. |
| `text-icon-disable` | `#3E4A59` | `#959DAD` | Disabled or unavailable controls. |
| `text-icon-on-base-button` | `#000000` | `#F1F2F5` | Text on base/filled button surfaces. |
| `text-icon-anti` | `#FFFFFF` | `#000000` | Inverted text/icon use. |
| `text-icon-tips` | `#13161C` | `#F1F3F5` | Text on tip surfaces. |

### Background

| Token | Dark | Light | Usage |
| --- | --- | --- | --- |
| `bg-primary` | `#0C0F12` | `#FFFFFF` | Primary page canvas. |
| `bg-secondary` | `#000000` | `#F1F2F5` | Secondary page background or deep section base. |
| `bg-other` | `#2C3642` | `#FFFFFF` | Alternate background. |
| `bg-model` | `#13171B` | `#FFFFFF` | Modal and bottom-sheet surface. |
| `bg-card` | `#13171B` | `#F1F2F5` | Card and contained panel surface. |
| `bg-mask` | `#000000 60%` | `#000000 60%` | Modal mask and overlay scrim. |
| `bg-tips` | `#F1F3F5` | `#13161C` | Tip background, usually inverse. |
| `bg-toast` | `#212830` | `#40485B` | Toast and transient notification surface. |

### Dividers, Borders, And Containers

| Token | Dark | Light | Usage |
| --- | --- | --- | --- |
| `divider-primary` | `#212830` | `#F1F2F5` | Fine dividers inside panels and rows. |
| `divider-container` | `#2C3642` | `#DBDEE6` | Stronger container separation. |
| `border-primary` | `#3E4A59` | `#DBDEE6` | Input borders, panel edges, selected outlines. |
| `fill-primary-container` | `#1A1F24` | `#F1F2F5` | Primary neutral container fill. |
| `fill-secondary-container` | `#444D59` | `#DBDEE6` | Secondary neutral container fill. |
| `fill-page-input` | `#1A1F24` | `#F1F2F5` | Input and select field fill. |
| `fill-page-input-disable` | `#212830` | `#E4E6EB` | Disabled input fill. |
| `fill-tag` | `#1A1F24` | `#F1F2F5` | Tags, pills, compact labels. |
| `fill-switch` | `#1A1F24` | `#DBDEE6` | Switch backgrounds. |
| `fill-other` | `#2C3642` | `#FFFFFF` | Miscellaneous neutral fill. |
| `fill-normal-alert` | `#1A1F24` | `#F1F2F5` | Neutral alert fill. |

### Brand, State, And Alerts

| Token | Dark | Light | Usage |
| --- | --- | --- | --- |
| `fill-brand` | `#0C73ED` | `#195EFF` | Brand color, selected states, primary CTA. |
| `fill-brand-alert` | `#0C73ED 20%` | `#195EFF 20%` | Low-emphasis brand alert or selected background. |
| `fill-secondary-colors` | `#84DC1F` | `#84DC1F` | Secondary accent; use sparingly. |
| `fill-success` | `#2CA85D` | `#2CA85D` | Positive states, profit, long/buy confirmation. |
| `fill-success-alert` | `#2CA85D 20%` | `#2CA85D 20%` | Low-emphasis success background. |
| `fill-error` | `#EB464F` | `#EB464F` | Negative states, loss, errors, short/sell emphasis. |
| `fill-error-alert` | `#EB464F 20%` | `#EB464F 20%` | Low-emphasis error background. |
| `fill-warning` | `#E0601F` | `#E0601F` | Warning and risk notices. |
| `fill-warning-alert` | `#E0601F 20%` | `#E0601F 20%` | Low-emphasis warning background. |
| `fill-check` | `#F0B848` | `#F0B848` | Check, highlighted verification, gold status. |
| `fill-check-alert` | `#F0B848 20%` | `#F0B848 20%` | Low-emphasis check/gold background. |

### Button Tokens

| Token | Dark | Light | Usage |
| --- | --- | --- | --- |
| `fill-brand-button-normal` | `#0C73ED` | `#195EFF` | Primary button default. |
| `fill-brand-button-pressed` | `#0B6ADB` | `#1858F0` | Primary button pressed/active. |
| `fill-brand-button-disable` | `#202738` | `#E1E6F1` | Disabled primary button. |
| `fill-green-button-pressed` | `#1B8248` | `#299C56` | Pressed buy/long button. |
| `fill-red-button-pressed` | `#C4313D` | `#E0434B` | Pressed sell/short button. |
| `fill-secondary-button-normal` | `#212830` | `#E4E6EB` | Secondary button default. |
| `fill-secondary-button-pressed` | `#1A1F24` | `#F1F2F5` | Secondary button pressed. |

## Primitive Gray Ramp

### Dark Ramp

| Token | Value |
| --- | --- |
| `dark-gray-1` | `#FFFFFF` |
| `dark-gray-2` | `#F1F3F5` |
| `dark-gray-3` | `#EAEDF0` |
| `dark-gray-4` | `#DADFE5` |
| `dark-gray-5` | `#A5B1C0` |
| `dark-gray-6` | `#878F99` |
| `dark-gray-7` | `#697E95` |
| `dark-gray-8` | `#3E4A59` |
| `dark-gray-9` | `#444D59` |
| `dark-gray-10` | `#212830` |
| `dark-gray-11` | `#1A1F24` |
| `dark-gray-12` | `#13171B` |
| `dark-gray-13` | `#0C0F12` |
| `dark-gray-14` | `#000000` |
| `dark-gray-15` | `#2C3642` |

### Light Ramp

| Token | Value |
| --- | --- |
| `light-gray-1` | `#FFFFFF` |
| `light-gray-2` | `#F1F2F5` |
| `light-gray-3` | `#E4E6EB` |
| `light-gray-4` | `#DBDEE6` |
| `light-gray-5` | `#A6AEC1` |
| `light-gray-6` | `#959DAD` |
| `light-gray-7` | `#717C95` |
| `light-gray-8` | `#40485B` |
| `light-gray-9` | `#2D3341` |
| `light-gray-10` | `#222731` |
| `light-gray-11` | `#212429` |
| `light-gray-12` | `#13161C` |
| `light-gray-13` | `#0D0E12` |
| `light-gray-14` | `#000000` |

## CSS Token Mapping

Use this as a starting point for web implementation:

```css
:root,
[data-theme="dark"] {
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
}

[data-theme="light"] {
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
}
```

## Typography

The Figma file exposes local text styles under `SF Pro/14/*`, all with 14px size, automatic line height, and 0% letter spacing. Treat this as an app-origin baseline, not a complete web type scale.

Use a compact trading scale:

| Role | Size | Weight | Usage |
| --- | --- | --- | --- |
| `display-price` | 20-24px | 600-700 | Main price, account total, modal title. |
| `section-title` | 16-18px | 600 | Panel title, major table title, page area label. |
| `body` | 14px | 400-500 | Default labels and row text. |
| `body-strong` | 14px | 600 | Active tabs, important row values. |
| `caption` | 12px | 400-500 | Order book labels, metadata, compact badges. |
| `micro` | 10-11px | 500 | Beta tags, tiny status tags, chart labels. |

Rules:

- Prefer SF Pro, Inter, or system UI stacks.
- Use tabular numbers for prices, balances, order book rows, percentages, and timestamps.
- Keep letter spacing at 0.
- Avoid oversized hero typography for product UI.
- Align numeric columns consistently; prices and balances should scan vertically.

Suggested CSS:

```css
body {
  font-family: "SF Pro", Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  letter-spacing: 0;
}

.btcc-number {
  font-variant-numeric: tabular-nums;
}
```

## Spacing And Density

BTCC spacing is compact. The `合约pro` reference uses a 375px mobile width with 16px side gutters, 44px navigation rows, 56px pair header, compact 28px controls, 38-42px inputs/buttons, and 24px order book rows.

Recommended web scale:

| Token | Value | Usage |
| --- | --- | --- |
| `space-2` | 2px | Micro dividers, slider bars. |
| `space-4` | 4px | Tight icon/text gaps. |
| `space-8` | 8px | Compact internal gaps. |
| `space-12` | 12px | Dense panel padding. |
| `space-16` | 16px | Page gutters, major panel padding. |
| `space-20` | 20px | Wider tab gaps or form sections. |
| `space-24` | 24px | Large section separation. |

Rules:

- Use `16px` outer gutters on mobile and `16-24px` gutters on desktop trading workspaces.
- Use dense rows for trading data: `24-32px` row height for order book/table rows.
- Use `38-44px` for primary action buttons and core inputs.
- Keep controls close to the data they affect.

## Radius And Shape

Use restrained radii:

| Element | Radius |
| --- | --- |
| Panels/cards | 4-8px |
| Inputs/selects | 4-6px |
| Buttons | 4-8px |
| Tags/pills | 4px or fully pill only for tiny badges |
| Bottom sheets | 16px top radius on mobile only |

Avoid overly soft rounded rectangles. BTCC should feel precise, not plush.

## Elevation And Effects

The Figma file has two local effect styles:

| Style | Effect |
| --- | --- |
| `渐隐遮罩-亮色` | Progressive layer blur, radius about 10.1. |
| `渐隐遮罩-暗色` | Progressive layer blur, radius about 10.1. |

Use effects sparingly. Prefer borders, dividers, and surface shifts over heavy shadows. Use scrims and blur only for modals, sheets, progressive masks, and content fade edges.

## Core Component Grammar

### Icons And Shared Assets

The source file uses compact vector icons embedded in `设计规范` and `合约pro`. The `图标` page exists but did not expose a complete standalone icon library through the current read pass, so treat actual in-page usage as the source of truth.

Core icon pattern:

| Category | Observed Names | Size | Usage |
| --- | --- | --- | --- |
| Product nav | `line-chart-up-03`, `BTCCtp`, home/discover/copy/assets/trade tab graphics | 20-24px | Bottom tab bar and major product navigation. |
| Market actions | `bar-chart-square-down`, `k线`, `更多` | 24px | Pair header actions: stats, candlestick/chart, more menu. |
| Selectors | `icon 2`, chevron-like vectors | 10-16px | Pair selector, leverage selector, unit selector, dropdown controls. |
| Account actions | deposit icon, `顶部导航栏icon`, `模拟` | 24px inside 40-44px touch containers | Deposit, transfer, demo trading, wallet shortcuts. |
| Utility/status | `plus-circle 1`, `warning-circle`, `file-minus-01` | 12-24px | Add funds, warnings, orders/history/empty utility. |
| System chrome | mobile signal, Wi-Fi, battery, home indicator | Native iOS-like sizes | Mobile app frame context only. Avoid using as decorative web content. |

Icon rules:

- Prefer real Figma assets when working with the Figma plugin. Search/import existing nodes or components before drawing replacements.
- Use stroke-based icons for most controls. Keep stroke weight visually close to `1.5-2px` at 24px.
- Use `24px` for primary toolbar/navigation icons.
- Use `16px` for inline icons next to pair names, compact buttons, and tags.
- Use `10-14px` for dropdown chevrons, warning markers, and dense form controls.
- Place 24px icons inside `40-44px` touch targets on mobile and `32-40px` targets on desktop.
- Bind icon color to text/icon semantic tokens: primary for active, secondary for normal utility, tertiary/disabled for unavailable states, brand for selected states.
- Do not use multicolor decorative icons in trading controls unless the icon itself communicates asset identity or product category.
- Do not invent a new icon style for one page. Match the source file's linear, compact, utility-first icon language.

When translating to web code:

- Use project icons if they visually match the BTCC source.
- Use Lucide-style line icons only as fallback approximations.
- Name icon components semantically, for example `ChartActionIcon`, `CandlestickIcon`, `MoreIcon`, `WarningCircleIcon`, `PlusCircleIcon`, `OrdersIcon`, `DepositIcon`, `TransferIcon`.
- Keep icon-only buttons accessible with `aria-label` or equivalent.

### Navigation

Use tab-like top navigation for product areas:

- `USDT-M`
- `Coin-M`
- `Spot`
- `USDT-M Pro` with a compact `beta` tag

For mobile/web-app bottom navigation, the Figma component set is `TabBar 底部标签栏` with variants:

- `home`
- `discover`
- `copy`
- `assets`
- `trade`

On desktop, translate bottom tabs into a left rail, top nav, or compact module nav instead of copying mobile bottom navigation literally.

### Market Pair Header

The `合约pro` page uses:

- Pair title: `BTCUSDT`
- Contract tag: `Perp`
- Change indicator: e.g. `-2.14%`
- Icon actions: market stats, candlestick/chart, more

For generated pages, always show the current pair or market context near the top. Do not hide it inside a dropdown without visible state.

### Trading Form

Reference structure:

- Margin mode row: `cross`, leverage such as `100x`
- Open/Close segmented control
- Available balance row with add/deposit icon
- Order type selector such as `limit`
- Price input, optional `BBO` shortcut
- Amount input with unit selector
- Percent slider with tick marks
- `TP/SL` checkbox/control
- Risk/account estimate rows: `max long`, `cost`, `liq.price`
- Buy/Long and Sell/Short actions

Web adaptation:

- Keep Open/Close and order type above price/amount fields.
- Put available balance above the form inputs.
- Use success green for buy/long and error red for sell/short when actions are directional.
- Primary brand blue is for neutral product actions, selected states, and non-directional CTAs.

### Order Book

Reference structure:

- Funding/countdown summary above order book.
- Column headers: `Price (USDT)` and `Size (BTC)`.
- Ask and bid rows with compact 24px rhythm.
- Depth bars behind size cells.
- Mid price emphasized between ask and bid blocks.
- Buy/sell ratio strip at the bottom, e.g. `B 39%` / `61% S`.

Rules:

- Use tabular numbers.
- Depth bars must sit behind text and remain low-contrast.
- Ask rows use error/red logic; bid rows use success/green logic.
- Keep order book width efficient. On desktop, it can live right of chart or form.

### Positions, Orders, Assets

Reference bottom panel:

- Tabs: `orders(0)`, `positions(0)`, `assets`
- Utility icon on the right
- Empty state tied to current trading pair
- Account prompts such as deposit/transfer actions

Rules:

- Use tabs for mutually exclusive operational states.
- Empty states should be compact and actionable, not illustrative-first.
- Keep deposit/transfer actions visible when balance is empty.

### Bottom Sheets And Modals

Reference modal/sheet pattern:

- Scrim uses `bg-mask`.
- Sheet surface uses `bg-model`.
- Mobile bottom sheet has drag handle and rounded top corners.
- Example TP/SL sheet shows title, pair tags, order metadata, entry/last/liquidation rows, nested tabs, a primary button, and a compact empty state.

Rules:

- Use bottom sheets for mobile task flows.
- Use centered or side modals for desktop.
- Keep modal content operational: state summary first, controls second, explanation last.

### Buttons

Use three intent families:

- Brand button: primary neutral action, selected CTA, submit.
- Success button: buy/long/positive trading direction.
- Error button: sell/short/destructive or negative direction.

Rules:

- Use button heights around `38-44px` for primary actions.
- Keep labels concise: `Open Long`, `Open Short`, `Deposit`, `Transfer`.
- Disabled buttons use `fill-brand-button-disable` and disabled text logic.
- Icon-only buttons need clear hover/focus affordance and accessible labels.

### Inputs And Selectors

Inputs are compact, filled, and stateful:

- Fill: `fill-page-input`.
- Disabled fill: `fill-page-input-disable`.
- Border: `border-primary` only when needed for focus/selection/separation.
- Unit selectors should sit inside or adjacent to inputs, not far away.
- Placeholder text uses tertiary text.

### Tags And Badges

Use small tags for:

- `Perp`
- `beta`
- order type such as `limit`
- direction such as `Open long`
- leverage such as `10x`

Tags should be compact, not decorative chips. Use neutral fills for informational tags and semantic fills for state tags.

## Layout Patterns

### Mobile Contract Page

The source `合约pro-dark` frame is `375 x 812`. Main structure:

1. Status bar, 44px.
2. Product nav, 44px.
3. Pair header, 56px.
4. Trading workspace, 514px: form left, order book right.
5. Orders/positions/assets panel.
6. Bottom tab bar.

When generating mobile screens, preserve this priority: pair context, trade controls, order book, account/order state.

### Desktop Trading Page

Recommended desktop adaptation:

1. Top product nav and account actions.
2. Pair header and market summary strip.
3. Main grid:
   - Chart or market depth as the widest center area.
   - Order book in a narrow right or left column.
   - Trading form in the opposite side column.
4. Positions/orders/assets panel pinned below chart.
5. Optional watchlist or market list as a side rail.

Avoid a marketing hero as the first screen for contract trading.

### Home Or Product Entry Page

Use an exchange-utility layout:

- Market snapshot strip.
- Contract/spot/copy entry modules.
- Account entry or onboarding action.
- Watchlist or top movers.
- Compact product cards only for repeated product modules.

The first viewport must make BTCC feel tradable, not brochure-like.

### Auth Page

Use a calm, product-focused auth layout:

- Compact login/register form.
- Brand/product context.
- Security/account cues.
- Minimal copy.
- No oversized illustration-driven hero unless requested.

### Wallet Or Account Page

Use dense account state:

- Balance summary.
- Asset table.
- Deposit, withdraw, transfer actions.
- History tabs.
- Risk/security notices.

## Interaction States

| State | Rule |
| --- | --- |
| Default | Neutral surfaces, low-contrast dividers, compact typography. |
| Hover | Slight surface lift or border change; avoid dramatic color shifts. |
| Active/selected | Brand fill or brand alert background plus text weight change. |
| Focus | Visible but restrained outline using brand or border token. |
| Disabled | Disabled text and disabled fill; no ambiguous half-active states. |
| Error | Error token plus concise message near the affected field. |
| Success | Success token for confirmations and positive trading direction. |
| Loading | Neutral skeleton/shimmer; no decorative loading animation. |

Selected states should not rely on color alone. Combine color with weight, underline, border, icon, or filled container.

## Data Visualization

For charts, order books, and market modules:

- Green means positive, bid, profit, buy, or long.
- Red means negative, ask, loss, sell, short, or error.
- Brand blue means product selection or primary neutral action, not price direction.
- Use subdued gridlines and low-contrast backgrounds.
- Use compact legends and labels.
- Keep chart controls close to the chart.

## Content Voice

BTCC copy should be short, functional, and state-aware.

Good:

- `Available`
- `Deposit`
- `Transfer`
- `Open Long`
- `Open Short`
- `Funding / Countdown`
- `Current Trading Pair`
- `No available data`

Avoid:

- Long marketing paragraphs in operational surfaces.
- Vague motivational copy.
- Decorative feature explanations inside trading workspaces.

## Accessibility And Responsiveness

- Keep text contrast readable in both dark and light modes.
- Do not use color alone for profit/loss or selected states.
- Provide accessible labels for icon-only controls.
- Ensure numeric tables remain readable on mobile.
- Avoid horizontal overflow unless it is a deliberate data table with clear scroll behavior.
- Preserve tap targets around `40-44px` on touch layouts.
- On desktop, avoid stretching compact controls into huge empty cards.

## Implementation Checklist

Before considering a BTCC-style page complete:

- Uses semantic BTCC tokens instead of arbitrary colors.
- Supports dark mode by default; light mode if requested or themeable.
- Shows product/market/account state in the first viewport.
- Uses compact spacing and dense information hierarchy.
- Uses tabs for major operational states.
- Uses segmented controls for mode switches.
- Uses tables/order-book rows for dense market data.
- Uses green/red only for directional state and blue for product action/selection.
- Avoids oversized marketing hero composition unless explicitly required.
- Keeps cards only for repeated units or true contained modules.
- Has no overlapping text or clipped numeric values.
- Has empty states that point to actions where appropriate.
