# API 管理（API Management）

> Figma 锚点（1558:14723 内）：
> - **Web 交易设定**：`9305:147186` 交易设定
> - **Web API 管理**：`9307:18488` API管理
> - **创建 API 密钥 弹窗**：`10406:150679`

## 用途

用户创建 / 管理 API Key（用于程序化交易、第三方平台对接）。

## 布局（Web 1200 容器）

```
API 管理
─────────────────────────────────────────────
顶部信息：
  当前已创建 N / 上限 5
  [ + 创建新 API ] pill 100 / h48 / 一级 button
─────────────────────────────────────────────
表格：
  名称        │ 权限              │ IP 白名单 │ 创建时间    │ 操作
  trade-bot   │ 读 / 交易         │ 12.34...  │ 2026-05-28 │ [编辑][删除]
  read-only   │ 读                │ 任意      │ 2026-05-20 │ [编辑][删除]
  ...
```

## 创建 API 弹窗（`10406:150679`，宽 480 / 600）

| 字段 | 控件 | 备注 |
| --- | --- | --- |
| 名称 | input h48 r4 | 字符限制 |
| 权限 | checkbox 组 | 读取 / 交易 / 提现（提现风险高，默认禁用） |
| IP 白名单 | textarea | 多个 IP 换行，警示 |
| 通行密码 | 6 位分段 input | 资金密码 |
| 2FA OTP | 6 位分段 input | |
| 阅读条款 | checkbox + 链接 | |
| 主 CTA | "创建" 一级 button | pill 100 / h48 / 宽满 |
| 副 CTA | "取消" outline | |

## 关键模块 → 组件

| 模块 | 组件文件 | 备注 |
| --- | --- | --- |
| 创建按钮 | [`components/button-primary.md`](../components/button-primary.md) | pill 100 |
| API 表格 | [`components/table.md`](../components/table.md) | 行高 56 |
| 编辑 / 删除 | [`components/button-secondary-sm.md`](../components/button-secondary-sm.md) | h28 r29 |
| 创建弹窗 | [`components/dialog.md`](../components/dialog.md) 480 / 600 | |
| 权限警示 | [`components/alert.md`](../components/alert.md) danger | "提现权限风险高" |
| Key 生成展示 | （inline）| 一次性显示 + 复制按钮，提示用户保存 |

## 安全要点

- API Secret **仅在创建时显示一次**，关闭弹窗后不可再查看（必须配 alert warning：请立即保存）。
- 删除 API 必须经过安全验证（见 `pages/account-security.md` 安全验证流程）。

## 反模式

- ❌ 提现权限默认勾选（必须默认禁用）。
- ❌ Secret 在表格里展示（实际仅创建时弹窗一次）。
- ❌ IP 白名单用 input 单行（实际 textarea 多行）。
- ❌ 创建 API 不需要 2FA（必须 + 资金密码 + 2FA 双验证）。
