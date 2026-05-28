# BTCC APP Platform Rules

This file extends `references/rules.md` with platform-specific concretization for BTCC mobile / H5 / APP surfaces. Rules below MUST cite a parent rule from `rules.md`. Do NOT introduce new rules here; if a new rule is genuinely cross-platform, add it to `rules.md` first.

## R-LAYOUT-2-APP: Mobile Density and Touch

Per rules.md R-LAYOUT-2 (mobile profile):

- Page gutters MUST be 16px on phone widths.
- Touch targets MUST be 40-44px on primary controls (`Open Long`, `Open Short`, `Confirm`, `Buy/Sell` tabs).
- Bottom action bar height MUST be ≥ 56px to clear the iOS home indicator on `合约pro` order surfaces.
- TabBar item taps MUST hit at least 44×44 (`次级button`, `TabBar 底部标签栏` component sets).

## R-SCOPE-1-APP: Verified APP Sources

Per rules.md R-SCOPE-1, the BTCC APP-side verified scope is:

- File: `新BTCC APP`, key `GW9kMfpf0Nib5DG4TjoWBp`.
- Verified pages: `设计规范` (`0:1`), `合约pro` (`1262:304`), `合约pro-dark` (`3112:1423`).
- Component sets in scope: `次级button`, `TabBar 底部标签栏`.
- Unverified surfaces (BTCC-style convention; re-verify before relying on them): `home`, `markets`, `wallet/assets`, `auth`, `copy-trading`, `spot`, `c2c`, `h5`, `全局组件`, `图标`, `换色`, `老合约`, `TradFi`, `我的、设置`, `卡券/体验金`, `支付通道、NFT、提现`, `观点`.

When generating UI for an unverified APP surface, follow `rules.md` R-SCOPE-1 marker requirements verbatim.
