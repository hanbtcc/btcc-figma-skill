---
name: btcc-ui-design
description: Use when designing, reviewing, or prompting BTCC company UI in Codex, including Web, H5, LP, and native app surfaces.
---

# BTCC UI Design

This is the distributable Codex skill for BTCC UI work.
It is self-contained and intended to be installed from GitHub.

## When to use

- BTCC web desktop or browser H5 UI
- BTCC LP campaign layouts
- BTCC native iOS / Android UI
- BTCC UI review, prompt writing, or Figma work

## Routing

1. Read `references/shared-rules.md`.
2. If the task is Web, H5, or LP, also read `references/web.md`.
3. If the task is native app, also read `references/app.md`.
4. Before any `use_figma` call, read `references/figma-pitfalls.md`.

## Operating rules

- Treat shared rules as the baseline and platform rules as overrides.
- Keep BTCC UI operational, dense, and transactional.
- Do not invent token names or color semantics.
- Mark anything not yet verified against current Figma source as `Unverified`.
- Browser H5 belongs to Web, not native app.

## Output expectations

- Follow the smallest relevant rule set.
- Prefer exact, existing BTCC naming over generic UI language.
- For app surfaces, assume unverified until the current source proves otherwise.
