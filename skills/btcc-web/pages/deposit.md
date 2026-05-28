# 充币（Deposit）

> Figma 锚点（1558:14723 内）：
> - **Web**：`4060:6303`、`4328:8453`、`122157:281595`、`122196:299464`、`130487:87820` 充币
> - **H5**：`4184:20027`、`122193:297784` H5 充币

## 用途

加密货币充值入金。**不是法币入金**（法币 → `pages/payment-fiat.md`）。

## 流程

```
1. 选币（USDT / BTC / ETH / TRX …）          → selector.md A 模式 dropdown 580
2. 选网络（ERC20 / TRC20 / BEP20 / BTC …）   → selector.md A 模式 dropdown 580
3. 显示充值地址 + 二维码 + 一键复制         → 自定义卡片
4. 风险提示 alert（最少充值 / 到账区块数）  → alert.md info
5. 历史充值记录（可选展开）                 → 表格
```

## 布局（Web 1200 容器）

```
充币
─────────────────────────────────────────────
左 600w                  │   右 560w
┌─选币 / 选网络 卡──────┐ │ ┌─地址 + 二维码 卡──────┐
│ 币种  [▼ USDT      ]  │ │ │  ┌────┐                 │
│ 网络  [▼ TRC20     ]  │ │ │  │QR  │  TXxxxxxxxxxxxxx│
│                       │ │ │  └────┘  [复制] [下载]  │
│ ⓘ 最低充值 1 USDT     │ │ │  ─────────────          │
│ ⓘ 1 个区块到账        │ │ │  备注（如 XRP）         │
└───────────────────────┘ │ │  到账时间预估           │
                          │ └─────────────────────────┘
                          │
                          │ ⚠️ 风险 alert（warning）
─────────────────────────────────────────────
最近充币记录（h40 一级 Tab + 表格）
```

## 关键模块 → 组件

| 模块 | 组件文件 | 备注 |
| --- | --- | --- |
| 币种 / 网络选择 | [`components/selector.md`](../components/selector.md) 模式 A | dropdown 580 |
| 充值地址 + 二维码 | （自定义） | QR 200×200，bg-card r4 |
| 复制 / 下载 | [`components/button-secondary-sm.md`](../components/button-secondary-sm.md) | h28 r29 |
| 备注 input（XRP / EOS）| [`components/input.md`](../components/input.md) | h48 r4 readonly |
| 风险 alert | [`components/alert.md`](../components/alert.md) | warning 黄 |
| 充值记录 | [`components/tab.md`](../components/tab.md) + 表格 | h40 |

## 反模式

- ❌ 把"最低充值"和"区块到账"用 toast 显示（应是常驻 inline alert）。
- ❌ 充值地址用纯文本（实际有专用容器：bg-card r4 + 复制按钮 + QR）。
- ❌ 网络选项做成 radio 横排（应是 dropdown 580）。
- ❌ XRP / EOS 缺备注 input（这两个币没有备注无法到账，必须有警示）。
- ❌ 把法币入金的"选支付方式"流程套在加密充币上（两条线完全不同）。
