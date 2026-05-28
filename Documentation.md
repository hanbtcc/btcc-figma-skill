# Documentation - BTCC Skills Repository

## 当前状态（2026-05-28）
仓库内部保留三 skill：`btcc-shared`、`btcc-web`、`btcc-app`。
另外新增对外分发 skill：`skills/btcc-ui-design/`，用于 GitHub 安装到 Codex 后直接调用。

## 关键决策
### D1：H5 镜像归属 Web，不属于 App
BTCC 有两套独立 Figma：
- BTCC WEB（含浏览器内 375w 移动响应版） -> `btcc-web/`
- BTCC APP（iOS / Android 原生） -> `btcc-app/`

影响：用户提到 BTCC H5 / 移动 H5 时进 `btcc-web`，不进 `btcc-app`。两者规则不一致。

### D2：APP 全部规则在新 Figma 落地前视为 Unverified
`btcc-app/references/` 与 `btcc-app/assets/btcc-tokens.{css,json}` 属于旧推断数据。新 Figma 未到之前，不要直接把 APP token 或几何当作真值引用。

### D3：合约 pro 蓝 / 红方向规则只适用于合约 pro
Open Long = 品牌蓝，Open Short = 错误红，与西方惯例相反，仅适用于合约 pro。
现货 / 闪兑 / 资产仍是绿买 / 红卖。

### D4：根 README 是两条入口
README 现在只负责说明两条路径：
- 仓库内协作入口
- 对外分发的 Codex skill `skills/btcc-ui-design/`

## 最近变更
- **2026-05-28** — Web + Shared 完整性收官 commit。补 components/table.md + components/upload.md + components/README.md，修 5 处死链，根 README 列全 17 份组件，新增 `.tmp/` 到 .gitignore。三 skill 拆分作为同次 commit 提交（94 files, +5499/-546）。
- **2026-05-28** — 新增 Codex 可见入口 `~/.codex/skills/btcc-skills/`。它只负责把 BTCC/Figma 任务路由回仓库内的 `btcc-shared` / `btcc-web` / `btcc-app`。
- **2026-05-28** — 新增对外分发 skill `skills/btcc-ui-design/`。它是自包含包，面向 GitHub 安装到 Codex，提供 shared / web / app / Figma pitfalls 的最小路由与规则集。

## Skill activation gate
- Project rule file: `AGENTS.md`
- Manual slash command: `.claude/commands/btcc/skills.md`
- Command forms: `/btcc:skills auto <task>`, `/btcc:skills web <task>`, `/btcc:skills app <task>`, `/btcc:skills shared <task>`
- For distributed Codex usage, install `skills/btcc-ui-design/` from GitHub and restart Codex.
