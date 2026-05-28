# Figma Plugin API Pitfalls (when calling `use_figma`)

> 调 `use_figma` 前必读。本文件记录在 BTCC Figma 文件中实际踩过的 Plugin API 坑。平台中立（APP / Web 都生效）。新坑加在这里，别在各平台 rules 里复述。

These are concrete failures observed while building BTCC LP / page nodes via the Figma MCP `use_figma` tool. Each entry says **what failed**, **why**, and **the corrected pattern**.

## P-PLUGIN-1: `fontFeatures` is not a TextNode property

**Failure**

```javascript
const t = figma.createText();
t.characters = '42d 17:23:08';
t.fontFeatures = { TNUM: true };   // TypeError: Cannot set property fontFeatures
```

**Why**

The Figma Plugin API's `TextNode` does not expose a `fontFeatures` setter. OpenType features like `tnum` are not directly toggleable from the plugin API. They become live only when:

- The chosen font family already ships tabular figures by default, OR
- The receiving environment (CSS, exported HTML/React) sets `font-variant-numeric: tabular-nums`.

**Corrected pattern**

- In the Figma node, just pick the right font and don't touch features.
- In generated code (`rules.md` R-LAYOUT-2 mandates this anyway), apply `font-variant-numeric: tabular-nums` on numeric columns at the CSS layer.
- If a font without TNUM is mandatory, switch the font; do not try to force the feature from the plugin.

## P-PLUGIN-2: `setRangeFills(start, end, ...)` indexes characters, not bytes

**Failure**

A title like `瓜分 100,000 USDT` was supposed to brand-color the substring `100,000 USDT`. Calling:

```javascript
title.setRangeFills(3, 15, [hex('#0C73ED')]);
```

…ended up coloring the wrong substring because the author counted bytes (UTF-8 made each CJK char 3 bytes) instead of characters.

**Why**

Figma's `setRangeFills(start, end, fills)` takes **character offsets** in the user-perceived string. CJK characters count as 1 each. Mixed CJK + ASCII strings still index uniformly by character.

The string `瓜分 100,000 USDT` indexed by character:

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|
| 瓜 | 分 | (space) | 1 | 0 | 0 | , | 0 | 0 | 0 | (space) | U | S | D | T | (end) |

`setRangeFills(3, 15, ...)` colors `100,000 USDT` (correct).

**Corrected pattern**

- Reset the entire string's fill first, then apply the highlight range. This protects against earlier `setRangeFills` calls leaking partial state.
- Verify offsets by using `Array.from(text).slice(start, end).join('')` mentally before calling.
- Prefer building the string and indices together:

```javascript
const head = '瓜分 ';
const num  = '100,000 USDT';
const all  = head + num;
node.characters = all;
node.fills = [hex('#F1F3F5')];                         // primary for whole string
node.setRangeFills(head.length, head.length + num.length, [hex('#0C73ED')]);
```

This makes the brand-colored substring computed, not hand-counted.

## P-PLUGIN-3: HORIZONTAL auto-layout children stretch on the cross axis by default

**Failure**

A row containing a status pill rendered as a full-width bar instead of hugging its label:

```javascript
const row = flex({ layoutMode: 'HORIZONTAL' });
const badge = flex({ layoutMode: 'HORIZONTAL', padding: 8 });   // inner badge
row.appendChild(badge);
// badge stretched to row width
```

**Why**

When a frame has `layoutMode: 'HORIZONTAL'`, child frames inherit `layoutAlign = 'STRETCH'` on the cross (vertical) axis by default, AND child frames whose own `layoutMode` is also `HORIZONTAL` start with `primaryAxisSizingMode: 'FIXED'` if their width was previously set or implied. The combination causes pills/chips to grow wider than their content.

The "hug content" intent must be made explicit on **both** the wrapping container and the child:

```javascript
badge.layoutMode = 'HORIZONTAL';
badge.primaryAxisSizingMode = 'AUTO';     // hug width
badge.counterAxisSizingMode = 'AUTO';     // hug height
badge.layoutAlign = 'INHERIT';            // do not stretch in parent
```

If the badge sits inside a wrapping `flex` row whose `counterAxisAlignItems` is `'CENTER'`, also set the row's children to not stretch:

```javascript
row.counterAxisAlignItems = 'CENTER';
// each child:
child.layoutAlign = 'INHERIT';
```

**Corrected pattern**

A reusable hug-content frame helper:

```javascript
function hug(opts = {}) {
  const f = figma.createFrame();
  f.layoutMode = opts.layoutMode || 'HORIZONTAL';
  f.primaryAxisSizingMode = 'AUTO';
  f.counterAxisSizingMode = 'AUTO';
  f.layoutAlign = 'INHERIT';
  f.fills = opts.fills || [];
  return f;
}
```

Use `hug()` for chips, badges, pill buttons; use a separate `flex()` factory (with explicit FIXED width) only when a frame is genuinely meant to fill its parent.

## P-PLUGIN-4: `figma.currentPage` is read-only; use `setCurrentPageAsync`

**Failure**

```javascript
figma.currentPage = newPage;   // throws
```

**Corrected pattern**

```javascript
await figma.setCurrentPageAsync(newPage);
```

This is documented in the `use_figma` tool description but easy to miss when porting older plugin code.

## P-PLUGIN-5: Font names with spaces are literal; case and spacing matter

**Failure**

Loading `Inter SemiBold` or `InterSemiBold` throws "font not found".

**Why**

Figma resolves font style strings exactly as they appear in the font's metadata. For `Inter` the styles are `Regular`, `Medium`, `Semi Bold`, `Bold`, `Extra Bold`. Same convention applies to `Roboto`, `Source Code Pro`, etc.

**Corrected pattern**

```javascript
await figma.loadFontAsync({ family: 'Inter', style: 'Semi Bold' });
text.fontName = { family: 'Inter', style: 'Semi Bold' };
```

When in doubt, paste the exact string Figma shows in the type panel.

## P-PLUGIN-6: `getPluginData` / `setPluginData` are not supported through `use_figma`

The plugin sandbox exposed by `use_figma` does NOT include the plugin-data API. Do not write code that depends on storing per-node metadata via `setPluginData` — it will silently fail or throw. Use node names with structured prefixes (e.g. `btcc-pool-row-1`) for any tagging the agent itself needs to recognize on later passes.

## P-PLUGIN-7: Hex → SOLID conversion expects 0–1 floats, not 0–255

**Failure**

```javascript
node.fills = [{ type: 'SOLID', color: { r: 12, g: 115, b: 237 } }];  // pure white-blue blowout
```

**Corrected pattern**

```javascript
const hex = (h, a = 1) => ({
  type: 'SOLID',
  color: {
    r: parseInt(h.slice(1, 3), 16) / 255,
    g: parseInt(h.slice(3, 5), 16) / 255,
    b: parseInt(h.slice(5, 7), 16) / 255,
  },
  opacity: a,
});
```

Bind hex inputs through this helper exactly once and never inline raw 0–255 ints into a `SOLID` fill.

## Quick pre-flight checklist before each `use_figma` call

1. Are all referenced fonts pre-loaded with `loadFontAsync`?
2. Are hug-content frames marked `primaryAxisSizingMode: 'AUTO'` AND `layoutAlign: 'INHERIT'`?
3. Are character ranges for `setRangeFills` counted as user-perceived characters, not bytes?
4. Are colors built via the `hex()` helper (0–1 floats), not raw 0–255 ints?
5. Tabular numerals delegated to CSS / font choice, not a `fontFeatures` setter?
6. Page switch uses `setCurrentPageAsync`, not `figma.currentPage = ...`?

If any answer is "no", fix the call before sending.
