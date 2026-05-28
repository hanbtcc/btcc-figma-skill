# 账户安全（Account Security）

> Figma 锚点（1558:14723 内）：
> - **Web 安全账户**：`4715:37123`、`9234:13257`、`102650:53766`、`102678:57225`、`100935:110603`、`107617:189221`、`123570:147049`
> - **Web 绑定邮箱**：`123438:47248`
> - **2FA / 验证弹窗**（130+ 个）：
>   - 建议完善 2FA：`123570:146855`、`123644:35373`、`128495:28516/28451`
>   - 移除谷歌：`123704:35795`
>   - 2FA = 邮箱：`123438:152063`、`128343:195615`
>   - 2FA = 身份验证器：`125938:192289`、`125938:193204`
>   - 安全验证要求：`130555:114569`、`130615:116695` 等系列

## 用途

账户安全设置中心。包含：登录密码、资金密码、邮箱、手机、2FA（Google Authenticator / 邮箱验证 / 短信）、API 设备 / 登录历史。

## 布局（Web 1200 容器）

```
账户安全
─────────────────────────────────────────────
左 280w 侧栏 nav         │  右 880w 内容区
[ 安全设置 ]             │
[ 登录密码 ]             │  当前模块标题
[ 资金密码 ]             │  ─────────────
[ 邮箱     ✓ ]           │  邮箱：u***@gmail.com
[ 手机     - ]           │  最近修改 ...
[ Google 2FA ✓ ]         │  [修改] secondary h28
[ 设备登录历史 ]          │
[ KYC      ✓ ]           │
                        │
（侧栏每行 56h，含状态  │
 icon ✓ / -）           │
```

## 关键模块 → 组件

| 模块 | 组件文件 | 备注 |
| --- | --- | --- |
| 侧栏 nav | （inline 56h list） | 状态 icon 16px |
| 修改 / 绑定按钮 | [`components/button-secondary-sm.md`](../components/button-secondary-sm.md) | h28 r29 |
| 修改密码 弹窗 | [`components/dialog.md`](../components/dialog.md) 480 | 含 3 个 input |
| 绑定邮箱 弹窗 | [`components/dialog.md`](../components/dialog.md) 480 | `123438:47248` |
| 绑定 2FA 弹窗 | [`components/dialog.md`](../components/dialog.md) 480 | 含 QR + 验证码 |
| 验证码 input | [`components/input.md`](../components/input.md) | h48 r4，6 位分段 |
| 安全验证（高敏操作前置） | [`components/dialog.md`](../components/dialog.md) 480 | 见 `130555:114569` 系列 |
| 风险提示 alert | [`components/alert.md`](../components/alert.md) | warning / danger |
| 完善 2FA 引导 | [`components/dialog.md`](../components/dialog.md) 480 | 含插画 + bullet |

## 安全验证（Security Verification）

> 高敏操作（修改密码 / 绑定 2FA / 提币 / 关闭 2FA / 修改邮箱）前必须出现的二次验证弹窗。锚点系列：`130555:114569 / 130615:116695 ...`。

| 子类型 | 输入项 |
| --- | --- |
| 邮箱验证 | 6 位 OTP，60s 倒计时 |
| 谷歌验证 | 6 位 TOTP |
| 手机验证 | 6 位 SMS OTP |
| 资金密码 | 6 位数字密码 |

**多 2FA 已启用**：弹窗内顶部 Tab 切换"邮箱 / Google / 手机"。

## 反模式

- ❌ 把高敏操作直接执行而不弹"安全验证"弹窗。
- ❌ 验证码 input 不分段（实际是 6 位分段，每位 48×48 r4）。
- ❌ "已绑定"状态用文字"绑定"显示（应是 ✓ icon + 隐码）。
- ❌ 2FA 二维码与密钥不可同框（弹窗内必须同时给 QR 和 base32 文本，方便用户备份）。
- ❌ 用 alert 显示"未绑定"（应是侧栏状态 - icon，加跳转 CTA）。
