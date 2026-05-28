# Shared Rules

These rules apply to all BTCC UI surfaces.

## 1. Operational first

BTCC is a trading product, not a marketing site. The first screen should show actionable state: market data, orders, balances, positions, forms, or controls.

## 2. Color is state

- Green = positive, success, buy
- Red = negative, danger, sell
- Amber = warning
- Gold = reward or highlight
- Blue = primary CTA or selected state

Do not use colors as decoration.

## 3. Unverified means explicit

Anything not verified against current Figma source must be labeled `Unverified`.

## 4. Token naming

Use existing BTCC semantic token names only. Do not invent `--primary`, `--accent`, or other generic names.

## 5. Numeric display

Prices, balances, ratios, and countdowns must use tabular numerals.

## 6. Icon language

Use BTCC-native iconography for trading and account surfaces. Do not swap in generic icon sets unless the skill explicitly allows it.

## 7. Single source of truth

Prefer the smallest verified rule set that matches the target surface. Platform rules override shared rules when they conflict.
