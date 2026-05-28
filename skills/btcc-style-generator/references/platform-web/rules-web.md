# BTCC Web Platform Rules

This file extends `references/rules.md` with platform-specific concretization for BTCC desktop / web surfaces. Rules below MUST cite a parent rule from `rules.md`. Do NOT introduce new rules here; if a new rule is genuinely cross-platform, add it to `rules.md` first.

## R-LAYOUT-2-WEB: Desktop Breakpoints and Density

Per rules.md R-LAYOUT-2 (web profile):

- Primary breakpoints supported by the BTCC WEB Figma source: 1024 / 1440 / 1556 / 1920 (per the rulers on canvas `0:1 设计规范`, fileKey `VrE25c6IAuIieWngebNnwx`).
- Layout MUST stay legible at 1440 minimum; ≥1920 is the canonical workspace width for `合约pro` desktop.
- Hover states MUST be defined for all interactive controls; focus rings MUST use a token bound to brand or border-active, not arbitrary colors.
- Side-by-side trading layout (order book + 下单 + right panel) MUST stay above the fold at 1440; do not stack vertically before the smallest desktop breakpoint.
- Cursor states: pointer for actionable, text for inputs, not-allowed for disabled.

## R-SCOPE-1-WEB: Verified Web Sources

Per rules.md R-SCOPE-1, the BTCC WEB-side verified scope is:

- File: `新BTCC WEB`, key `VrE25c6IAuIieWngebNnwx`.
- Verified canvas: `设计规范` (`0:1`).
- Unverified canvas: `其他-马甲包官网/桌面图标` (`3089:7459`).
- The BTCC WEB Figma file does NOT contain top-level `合约pro` / `合约pro-dark` canvases; desktop trading anatomy lives as sub-frames inside `0:1`. See `for-figma-inspect/source-anchors.md` for the per-element node index.

When generating UI for an unverified Web surface, follow `rules.md` R-SCOPE-1 marker requirements verbatim.

## R-ASSETS-WEB: Token and Icon Provenance

Per rules.md R-NAME-1 and R-ICON-1:

- `assets/btcc-tokens.{json,css}` and `assets/icons/*.svg` are currently derived from the BTCC APP file. They have NOT been cross-checked against the BTCC WEB local-variables collection.
- Web code generation MUST mark token usage as Unverified until tokens are reconciled with Web Figma local variables, OR ask the user to provide a Web token export.
- When a Web design references an icon role for which no APP-derived asset is suitable, fall back per `rules.md` R-ICON-1 ordering rather than introducing arbitrary illustrations.
