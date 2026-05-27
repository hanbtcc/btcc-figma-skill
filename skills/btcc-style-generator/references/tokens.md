# BTCC Original Token Reference

Use this file when implementing BTCC theme variables, mapping Figma tokens to code, or reviewing whether generated UI uses the original design rules.

## Collections

| Collection Alias | Original Figma Name | Modes | Role |
| --- | --- | --- | --- |
| `semantic` | `变量合集` | `dark`, `light` | Semantic UI colors for text, surfaces, dividers, fills, alerts, buttons. |
| `gray-ramp` | `梯度色板` | `Mode 1` | Primitive dark/light gray ramps. |
| `size` | (not exposed as Figma variables) | n/a | Radius / control height / spacing observed from `合约pro-dark`. |
| `typography` | (not exposed as Figma variables) | n/a | Font family, weight, size, line-height observed from `合约pro-dark`. |

## Semantic Tokens

| Original Figma Token | Code Token | Dark | Light |
| --- | --- | --- | --- |
| `text | icon/primary` | `--btcc-text-primary` | `#F1F3F5` | `#13161C` |
| `text | icon/secondary` | `--btcc-text-secondary` | `#878F99` | `#717C95` |
| `text | icon/tertiary` | `--btcc-text-tertiary` | `#444D59` | `#A6AEC1` |
| `text | icon/white` | `--btcc-text-white` | `#FFFFFF` | `#FFFFFF` |
| `text | icon/black` | `--btcc-text-black` | `#000000` | `#000000` |
| `text | icon/disable` | `--btcc-text-disabled` | `#3E4A59` | `#959DAD` |
| `text | icon/on base button` | `--btcc-text-on-base-button` | `#000000` | `#F1F2F5` |
| `text | icon/anti` | `--btcc-text-anti` | `#FFFFFF` | `#000000` |
| `text | icon/tips` | `--btcc-text-tips` | `#13161C` | `#F1F3F5` |
| `bg/primary` | `--btcc-bg-primary` | `#0C0F12` | `#FFFFFF` |
| `bg/secondary` | `--btcc-bg-secondary` | `#000000` | `#F1F2F5` |
| `bg/other` | `--btcc-bg-other` | `#2C3642` | `#FFFFFF` |
| `bg/model` | `--btcc-bg-modal` | `#13171B` | `#FFFFFF` |
| `bg/card` | `--btcc-bg-card` | `#13171B` | `#F1F2F5` |
| `bg/mask` | `--btcc-bg-mask` | `#000000 60%` | `#000000 60%` |
| `bg/tips` | `--btcc-bg-tips` | `#F1F3F5` | `#13161C` |
| `bg/toast` | `--btcc-bg-toast` | `#212830` | `#40485B` |
| `Divider/primary` | `--btcc-divider-primary` | `#212830` | `#F1F2F5` |
| `Divider/container Divider` | `--btcc-divider-container` | `#2C3642` | `#DBDEE6` |
| `border/Primary` | `--btcc-border-primary` | `#3E4A59` | `#DBDEE6` |
| `fill/other` | `--btcc-fill-other` | `#2C3642` | `#FFFFFF` |
| `fill/Primary Container` | `--btcc-fill-primary-container` | `#1A1F24` | `#F1F2F5` |
| `fill/Secondary Container` | `--btcc-fill-secondary-container` | `#444D59` | `#DBDEE6` |
| `fill/Page Input` | `--btcc-fill-input` | `#1A1F24` | `#F1F2F5` |
| `fill/Page Input disable` | `--btcc-fill-input-disabled` | `#212830` | `#E4E6EB` |
| `fill/tag` | `--btcc-fill-tag` | `#1A1F24` | `#F1F2F5` |
| `fill/Switch` | `--btcc-fill-switch` | `#1A1F24` | `#DBDEE6` |
| `fill/Brand` | `--btcc-brand` | `#0C73ED` | `#195EFF` |
| `fill/Secondary Colors` | `--btcc-secondary-accent` | `#84DC1F` | `#84DC1F` |
| `fill/Brand Alert` | `--btcc-brand-alert` | `#0C73ED 20%` | `#195EFF 20%` |
| `fill/Success` | `--btcc-success` | `#2CA85D` | `#2CA85D` |
| `fill/Green Button Pressed` | `--btcc-success-pressed` | `#1B8248` | `#299C56` |
| `fill/Success Alert` | `--btcc-success-alert` | `#2CA85D 20%` | `#2CA85D 20%` |
| `fill/Error` | `--btcc-error` | `#EB464F` | `#EB464F` |
| `fill/Red Button Pressed` | `--btcc-error-pressed` | `#C4313D` | `#E0434B` |
| `fill/Error Alert` | `--btcc-error-alert` | `#EB464F 20%` | `#EB464F 20%` |
| `fill/Warning` | `--btcc-warning` | `#E0601F` | `#E0601F` |
| `fill/Warning Alert` | `--btcc-warning-alert` | `#E0601F 20%` | `#E0601F 20%` |
| `fill/check` | `--btcc-check` | `#F0B848` | `#F0B848` |
| `fill/check Alert` | `--btcc-check-alert` | `#F0B848 20%` | `#F0B848 20%` |
| `fill/normal Alert` | `--btcc-normal-alert` | `#1A1F24` | `#F1F2F5` |
| `fill/Brand Button/Normal` | `--btcc-button-brand-bg` | `#0C73ED` | `#195EFF` |
| `fill/Brand Button/Pressed` | `--btcc-button-brand-bg-pressed` | `#0B6ADB` | `#1858F0` |
| `fill/Brand Button/Disable` | `--btcc-button-brand-bg-disabled` | `#202738` | `#E1E6F1` |
| `fill/Secondary Button/Normal` | `--btcc-button-secondary-bg` | `#212830` | `#E4E6EB` |
| `fill/Secondary Button/Pressed` | `--btcc-button-secondary-bg-pressed` | `#1A1F24` | `#F1F2F5` |

## Primitive Gray Ramp

### Dark

| Token | Value |
| --- | --- |
| `dark/gray1` | `#FFFFFF` |
| `dark/gray2` | `#F1F3F5` |
| `dark/gray3` | `#EAEDF0` |
| `dark/gray4` | `#DADFE5` |
| `dark/gray5` | `#A5B1C0` |
| `dark/gray6` | `#878F99` |
| `dark/gray7` | `#697E95` |
| `dark/gray8` | `#3E4A59` |
| `dark/gray9` | `#444D59` |
| `dark/gray10` | `#212830` |
| `dark/gray11` | `#1A1F24` |
| `dark/gray12` | `#13171B` |
| `dark/gray13` | `#0C0F12` |
| `dark/gray14` | `#000000` |
| `dark/gray15` | `#2C3642` |

### Light

| Token | Value |
| --- | --- |
| `light/gray1` | `#FFFFFF` |
| `light/gray2` | `#F1F2F5` |
| `light/gray3` | `#E4E6EB` |
| `light/gray4` | `#DBDEE6` |
| `light/gray5` | `#A6AEC1` |
| `light/gray6` | `#959DAD` |
| `light/gray7` | `#717C95` |
| `light/gray8` | `#40485B` |
| `light/gray9` | `#2D3341` |
| `light/gray10` | `#222731` |
| `light/gray11` | `#212429` |
| `light/gray12` | `#13161C` |
| `light/gray13` | `#0D0E12` |
| `light/gray14` | `#000000` |

## Usage Rules

- Use semantic tokens in components. Use primitive ramp tokens only when defining or debugging semantic tokens.
- Light mode is dark-derived, not authored separately. Brand / state / accent hues are mostly 1:1 across modes (`success` `#2CA85D`, `error` `#EB464F`, `warning` `#E0601F`, `check` `#F0B848`, `secondaryAccent` `#84DC1F`); only `brand` shifts (`#0C73ED` → `#195EFF`). Bg / text / divider / border / fill / button surfaces invert across the gray ramp. Do not synthesize new light hexes per component.
- BTCC `合约pro` direction-button rule (overrides the common "long=green / short=red" convention on the action button only):
  - `Open Long` button → `--btcc-brand`, pressed → `--btcc-brand-pressed`.
  - `Open Short` button → `--btcc-error`, pressed → `--btcc-error-pressed`.
  - Numeric direction in the same page (bid rows, percent change, pnl text) still uses success/green for positive and error/red for negative.
- Primary neutral actions also use brand button tokens.
- Inputs, tags, switches, cards, modals, and dividers must use their original Figma semantic tokens.
- Preserve dark and light values even if the current task only asks for dark mode.
- For non-color values (radius / control height / spacing / typography), prefer `--btcc-radius-*`, `--btcc-size-*`, `--btcc-space-*`, `--btcc-font-*` over arbitrary numbers; these are observed from `合约pro-dark` and not yet first-class Figma variables, so flag any deviation explicitly when shipping.

## Size Tokens (observed)

The Figma source file does not expose radius / size / spacing as named variables. The values below are observed from `合约pro-dark` (`3112:1423`) sub-frames and codified for reuse. Treat them as conventions backed by the verified contract page, not as canonical published variables.

### Radius

| Token | Value | Observed at | Use |
| --- | --- | --- | --- |
| `--btcc-radius-tag` | `4px` | `Frame 431` (`Perp` tag) | small tags, chips |
| `--btcc-radius-control` | `6px` | order form inputs (`3112:1481`, `3112:1490`, `3112:1495`), Open/Close segment (`3112:1468`) | inputs, segmented controls, secondary surfaces |
| `--btcc-radius-card` | `12px` | bottom sheets, large cards | cards, modals, sheets |
| `--btcc-radius-pill` | `100px` | direction buttons (`Frame 1707481005` long/short) | full-pill direction buttons, tab indicators |

### Control Heights

| Token | Value | Observed at | Use |
| --- | --- | --- | --- |
| `--btcc-size-control-sm` | `28px` | mode segmented control, leverage row, `limit` selector | compact controls inside a panel |
| `--btcc-size-button` | `38px` | `Open Long` / `Open Short` buttons | primary direction action |
| `--btcc-size-input` | `42px` | price/amount input, BBO sidecar | price/amount input fields |
| `--btcc-size-row-sm` | `22px` | product nav row text height | dense text rows |
| `--btcc-size-row` | `24px` | order book rows | order book / dense table rows |
| `--btcc-size-nav` | `44px` | product nav, status bar, bottom orders bar | top/bottom nav rows |
| `--btcc-size-tabbar` | `78px` | bottom `TabBar 底部标签栏` | mobile bottom tab bar |

### Spacing

| Token | Value | Use |
| --- | --- | --- |
| `--btcc-space-1` | `4px` | tight inline gaps inside controls |
| `--btcc-space-2` | `8px` | gap between stacked rows in trading form |
| `--btcc-space-3` | `12px` | input internal horizontal padding |
| `--btcc-space-4` | `16px` | screen side gutter |
| `--btcc-space-6` | `24px` | section break inside a panel |

## Typography Tokens (observed)

Helvetica Neue Regular / Medium observed across `合约pro-dark` (price input, direction button, leverage row, order book). The source file uses these as raw text styles, not named typography variables.

| Token | Value | Use |
| --- | --- | --- |
| `--btcc-font-family-sans` | `"Helvetica Neue", "PingFang SC", "Helvetica", system-ui, -apple-system, sans-serif` | default UI font |
| `--btcc-font-weight-regular` | `400` | labels, table cells, secondary text |
| `--btcc-font-weight-medium` | `500` | direction button, price emphasis, segmented control active text |
| `--btcc-font-size-xs` | `10px` | secondary labels (`price(USDT)`, mode segment text) |
| `--btcc-font-size-sm` | `12px` | leverage values, pair tag, table headers, ratio strip |
| `--btcc-font-size-md` | `14px` | direction button label, price value |
| `--btcc-line-height-tight` | `18px` | dense rows |
| `--btcc-line-height-base` | `20px` | default body lines |

