# App Rules

These rules apply to BTCC native iOS / Android surfaces.

## Scope

- Native app surfaces only
- Treat browser H5 as Web, not App
- Treat any unclear APP reference as `Unverified` unless the current source proves it

## Density

- Use compact mobile layouts with 16px page gutters
- Primary controls should feel touch-friendly and dense, not oversized
- Bottom action bars should leave room for system safe areas

## Controls

- Prefer 40-44px touch targets for primary actions
- Keep action bars, tabs, and form rows clear and direct
- Do not import Web sizing assumptions into App layouts

## Verification

- If a screen, component, or token is not re-verified against the current APP source, label it `Unverified`
- When App and shared rules conflict, App-specific rules win

