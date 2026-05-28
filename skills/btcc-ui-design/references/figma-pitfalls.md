# Figma Plugin Pitfalls

Read this before any `use_figma` call.

## Checklist

1. Load fonts with exact Figma family/style names.
2. Use `setCurrentPageAsync`, not `figma.currentPage = ...`.
3. Treat `setRangeFills` offsets as character indices, not bytes.
4. Do not rely on `fontFeatures` in the Plugin API.
5. Build colors with normalized 0-1 channel values.
6. Do not use `getPluginData` / `setPluginData` through `use_figma`.
7. Make hug-content frames explicit with AUTO sizing and inheritance.

## Rule

If any item above is not satisfied, fix the call before sending it.
