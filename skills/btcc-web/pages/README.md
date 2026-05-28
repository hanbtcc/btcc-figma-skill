# Pages（页面索引）

> 17 份业务页面，按 BTCC Web 业务域分类。每份含：Figma 锚点（基于 1558:14723 全站合集）、布局结构、关键模块 → 组件映射、反模式。

## 交易类

| 文件 | 业务域 | 主锚点 |
| --- | --- | --- |
| [contract.md](contract.md) | 合约 Pro / 永续 | `5896:9053` |
| [spot.md](spot.md) | 现货 | `2103:16421`、`5163:20111`、`5172:21798` |
| [swap.md](swap.md) | 闪兑 | `9764:153702`、`9822:165386` |

## 资产类

| 文件 | 业务域 | 主锚点 |
| --- | --- | --- |
| [assets.md](assets.md) | 资产总览 | `122196:298806` |
| [deposit.md](deposit.md) | 加密充币 | `122196:299464`、`130487:87820` |
| [withdraw.md](withdraw.md) | 加密提币 / 提现 | `110288:202540`、`110138:200547` |
| [transfer.md](transfer.md) | 账户内划转 | `108208:21377` |
| [payment-fiat.md](payment-fiat.md) | 法币入金 | `8539:112094`、`104678:71613` |
| [funding-history.md](funding-history.md) | 资金记录 | `9884:11688` |

## 用户中心类

| 文件 | 业务域 | 主锚点 |
| --- | --- | --- |
| [coupons.md](coupons.md) | 卡券（体验金 / 抵扣金 / 交易券 / 积分） | `129837:140311`、`126725:132716` |
| [bank-address.md](bank-address.md) | 银行卡 / 提币地址 / 收货地址 | `10345:45045`、`10370:52858`、`10382:53435` |
| [account-security.md](account-security.md) | 账户安全 / 2FA / 安全验证 | `123570:147049`、`123438:47248` |
| [identity-kyc.md](identity-kyc.md) | 身份认证 / KYC | `126947:39043` |
| [api-management.md](api-management.md) | API 管理 | `9307:18488`、`10406:150679` |
| [vip.md](vip.md) | 个人中心 / VIP / 报表 / 盈亏 / 分享 | `129823:139018`、`100586:121640`、`2613:24075` |

## 通用类

| 文件 | 业务域 | 主锚点 |
| --- | --- | --- |
| [dialog-library.md](dialog-library.md) | 通用弹窗（Alert / 反馈 / 引导 / 安全验证） | `129661:304594`、`130479:87577`、`130555:114569` |
| [h5-mirror.md](h5-mirror.md) | H5 镜像（375 宽，浏览器移动版） | 各业务 h5 节点 |

## 使用顺序

1. **先读** [`../rules.md`](../rules.md) → 弄清字体 / 几何 / token / 颜色规则。
2. **再读** [`../../btcc-shared/rules-shared.md`](../../btcc-shared/rules-shared.md) → 跨平台规则（操作优先 / 颜色即状态 / Unverified 标记 / 数据呈现）。
3. **按页面族进入** → 找到对应业务域 md，读 Figma 锚点、布局、组件清单。
4. **拆解到组件** → 跟着"模块 → 组件"链接读 [`../components/*.md`](../components/)。
5. **调 Figma 前** → 必读 [`../figma-plugin-pitfalls.md`](../figma-plugin-pitfalls.md)。

## 反模式（页面级共性）

- ❌ 不查 1558:14723 直接推测页面（违反 R-SHARED-3 Unverified）。
- ❌ 把 H5 当 APP 来做（H5 是 Web 响应式，规则与 Web 一致）。
- ❌ 跨域复用：合约 pro 的反惯例蓝/红被复制到现货 / 资产 / 闪兑（仅合约 pro 例外）。
- ❌ 数据表格不加 tabular-nums（违反 R-SHARED-5）。
- ❌ 高敏操作（提币 / API / 修改密码 / 关闭 2FA）跳过"安全验证"弹窗。
