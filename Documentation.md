# Documentation —— BTCC Skills 仓库

> 跨任务复用的状态、决策、边界。git 历史能恢复的内容不写在这里。

## 当前状态（2026-05-28）

仓库已从单一 `skills/btcc-style-generator/` 拆为三 skill。Web + Shared 已完整，APP 等新 Figma。

```
skills/
  btcc-shared/   ✅ 跨平台 SSOT（R-SHARED-1 ~ R-SHARED-7）
  btcc-web/      ✅ 全量基于 新BTCC WEB Figma (VrE25c6IAuIieWngebNnwx)
  btcc-app/      ⚠️ Unverified，等 han 提供新 APP Figma (GW9kMfpf0Nib5DG4TjoWBp)
```

## 关键决策（不可从 git 自动恢复）

### D1：H5 镜像归属 Web，不属于 APP

BTCC 有两套独立 Figma：
- 新BTCC WEB（含浏览器内 375w 移动响应版） → `btcc-web/pages/h5-mirror.md`
- 新BTCC APP（iOS / Android 原生）→ `btcc-app/`

**影响**：用户提到"BTCC H5 / 移动 H5"时进 `btcc-web`，不进 `btcc-app`。两者规则不一致——Web H5 仍是 Lato + pill 100，APP 是系统字 + r6（待新 Figma 重新校验）。

### D2：APP 全部规则在新 Figma 落地前视为 Unverified（R-SHARED-3）

`btcc-app/references/` 与 `btcc-app/assets/btcc-tokens.{css,json}` 是从老 APP Figma 推断的早期数据。新 Figma 没到之前**不要**：
- 直接基于旧 APP token 生成代码
- 把 APP 的几何（38h / r6）当真实值引用
- 修正旧 APP 文件的内容（避免与未来重做冲突）

只读 / 只参考；引用时显式标 `Unverified`。

### D3：合约 pro 蓝/红方向规则（R-COLOR-WEB-1 / R-COLOR-1）只适用于"合约 pro"

Open Long = 品牌蓝、Open Short = 错误红，与西方惯例（绿涨红跌）相反。**仅** 合约 pro 下单按钮；现货 / 闪兑 / 资产 仍是绿买 / 红卖。qa-lint.py 已检测此跨域复用（RULE_LONG_BLUE_OUTSIDE_FUTURES）。

### D4：根 README 是三 skill 入口，不是单 skill 描述

历史上 README.md 描述单一 `btcc-style-generator/`。现已重写为三 skill 索引 + 任务路由表。改 README 时同步改 skill 内 SKILL.md，避免双层失同步。

## 仓库导航最小入口

| 目的 | 第一站 |
| --- | --- |
| 任何 BTCC 任务（共同基线） | `skills/btcc-shared/rules-shared.md` |
| Web 桌面 / H5 任务 | `skills/btcc-web/SKILL.md` 任务索引 |
| APP 原生任务 | `skills/btcc-app/SKILL.md`（先认 Unverified） |
| 跑 lint | `python skills/btcc-web/qa-lint.py <file-or-dir>` |
| 调 Figma 插件前预飞行 | `skills/btcc-web/figma-plugin-pitfalls.md` |

## 已知边界 / 未完成

- `btcc-app/` 整套（rules-app.md / tokens / components / pages）等新 Figma 重做。重做时按 btcc-web/ 同种范式：rules → tokens → components → pages → qa-lint。
- `btcc-app/scripts/btcc_qa_lint.py` 是旧脚本，APP 重做时改写或并入 btcc-web 版的扫描器。
- `btcc-shared/` 暂时只有 SKILL + rules-shared，后续若提炼出更多跨平台组件契约（如安全验证流、tabular-nums 实现示例），加 components-shared/ 子目录。

## Git 提交风格

- 拆 skill / 改架构 → `refactor(skills): ...`
- 加 Figma 锚点 / 文档新增 → `feat(<skill>): ...` 或 `docs(specs): ...`
- 归档 / 重命名 → `chore(...): ...`
- 提交信息中文为主，英文 type prefix。

## 最近变更

- **2026-05-28** — Web + Shared 完整性收官 commit。补 components/table.md + components/upload.md + components/README.md，修 5 处死链，根 README 列全 17 份组件，新增 `.tmp/` 到 .gitignore。三 skill 拆分作为同次 commit 提交（94 files, +5499/-546）。
