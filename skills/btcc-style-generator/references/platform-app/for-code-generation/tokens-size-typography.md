# BTCC Size & Typography Tokens

> See `references/rules.md` for global rules.

Authoritative source for BTCC size, radius, spacing, and typography tokens. Values are observed from `合约pro-dark` (`3112:1423`) sub-frames and codified for reuse — they are conventions backed by the verified contract page, not first-class published Figma variables. Color tokens live in `tokens-colors.md`. Color direction rules live in `rules.md` (see R-COLOR-1, R-COLOR-2); this file does not redeclare them.

The Figma source file does not expose radius / size / spacing / typography as named variables. Treat the values below as conventions and flag any deviation explicitly when shipping.

## Radius

| Token | Value | Observed at | Use |
| --- | --- | --- | --- |
| `--btcc-radius-tag` | `4px` | `Frame 431` (`Perp` tag) | small tags, chips |
| `--btcc-radius-control` | `6px` | order form inputs (`3112:1481`, `3112:1490`, `3112:1495`), Open/Close segment (`3112:1468`) | inputs, segmented controls, secondary surfaces |
| `--btcc-radius-card` | `12px` | bottom sheets, large cards | cards, modals, sheets |
| `--btcc-radius-pill` | `100px` | direction buttons (`Frame 1707481005` long/short) | full-pill direction buttons, tab indicators |

## Control Heights

| Token | Value | Observed at | Use |
| --- | --- | --- | --- |
| `--btcc-size-control-sm` | `28px` | mode segmented control, leverage row, `limit` selector | compact controls inside a panel |
| `--btcc-size-button` | `38px` | `Open Long` / `Open Short` buttons | primary direction action |
| `--btcc-size-input` | `42px` | price/amount input, BBO sidecar | price/amount input fields |
| `--btcc-size-row-sm` | `22px` | product nav row text height | dense text rows |
| `--btcc-size-row` | `24px` | order book rows | order book / dense table rows |
| `--btcc-size-nav` | `44px` | product nav, status bar, bottom orders bar | top/bottom nav rows |
| `--btcc-size-tabbar` | `78px` | bottom `TabBar 底部标签栏` | mobile bottom tab bar |

## Spacing

| Token | Value | Use |
| --- | --- | --- |
| `--btcc-space-1` | `4px` | tight inline gaps inside controls |
| `--btcc-space-2` | `8px` | gap between stacked rows in trading form |
| `--btcc-space-3` | `12px` | input internal horizontal padding |
| `--btcc-space-4` | `16px` | screen side gutter |
| `--btcc-space-6` | `24px` | section break inside a panel |

## Typography

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

## Usage Rules (size & typography only)

- For non-color values (radius / control height / spacing / typography), prefer `--btcc-radius-*`, `--btcc-size-*`, `--btcc-space-*`, `--btcc-font-*` over arbitrary numbers.
- Tabular-numeric, dark-first, compact-density, and gutter rules are SSOT — see `rules.md` R-LAYOUT-2. Apply the typography tokens above; do not redeclare the rule here.
- These values are observed conventions, not first-class Figma variables; flag deviations explicitly when shipping.
