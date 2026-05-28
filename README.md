# BTCC Figma Skill Repo

这个仓库有两条线：

1. **内部协作**：仓库内拆成 `btcc-shared`、`btcc-web`、`btcc-app`
2. **对外分发**：`skills/btcc-ui-design/`，可通过 GitHub 安装到 Codex

## 内部协作

本 checkout 里，BTCC / Figma 任务仍按仓库规则走：

- `AGENTS.md`
- `.claude/commands/btcc/skills.md`
- `skills/btcc-shared/`
- `skills/btcc-web/`
- `skills/btcc-app/`

Web / H5 属于 `btcc-web`，不是 `btcc-app`。
APP 规则在新 Figma 重新校验前，仍视为 `Unverified`。

## 对外分发

给别人安装到 Codex 时，使用：

- `skills/btcc-ui-design/`

它是一个自包含 skill 包，提供 BTCC UI 的最小路由和规则集。

### 安装方式

从 GitHub 安装这个 skill 后，重启 Codex。
安装完成后，在 Codex 里直接通过 `btcc-ui-design` 使用。

## 仓库结构

```text
skills/
  btcc-shared/      跨平台共享规则
  btcc-web/         Web / H5 / LP
  btcc-app/         Native App
  btcc-ui-design/    对外分发的 Codex skill
```

## 约定

- 共享规则优先，平台规则覆盖共享规则
- 未经当前 Figma 验证的内容要标 `Unverified`
- 不要自己发明 token 名称或颜色语义
- `use_figma` 前先看 Figma pitfalls
