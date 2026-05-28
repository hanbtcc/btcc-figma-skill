# 闪兑（Swap）

> Figma 锚点（1558:14723 内）：
> - **Web**：`9764:153702 闪兑`、`9822:165386 闪兑`
> - **H5**：（同名 H5 镜像 Unverified，未在 415 名单中识别到独立 H5 frame）

## 用途

不挂盘口的快速兑换（即时报价）。形态接近钱包内的"换币"按钮，但单独成页。

## 布局

```
┌──── 顶部 nav 64h ────────────────────────────────────┐
│                                                       │
│           ┌──────── 闪兑卡 480-520w ──────┐          │
│           │ 闪兑                            │          │
│           │  ─────────────                  │          │
│           │  支付   [▼ USDT] [_____ 100  ]  │← 余额行  │
│           │     ↕ 切换                      │          │
│           │  收到   [▼ BTC ] [_____ ≈0.0036]│ (估算)   │
│           │  ─────────────                  │          │
│           │  汇率：1 BTC = 27,449.50 USDT   │← 12px    │
│           │  滑点：0.5% / 手续费：免        │          │
│           │  ─────────────                  │          │
│           │ [ 立即兑换 ]  pill 100 / h48    │← 一级    │
│           └─────────────────────────────────┘          │
│                                                       │
│   下方：闪兑历史记录（h40 一级 Tab + 表格）          │
└───────────────────────────────────────────────────────┘
```

## 关键模块 → 组件

| 模块 | 组件文件 | 备注 |
| --- | --- | --- |
| 闪兑卡（容器） | [`components/dialog.md`](../components/dialog.md) 风格 | 但不是弹窗，r8、bg-card |
| 币种选择 | [`components/selector.md`](../components/selector.md) 模式 A | dropdown 580 |
| 数量输入 | [`components/input.md`](../components/input.md) | h48 r4 |
| 兑换 CTA | [`components/button-primary.md`](../components/button-primary.md) | 宽满 480 / pill 100 |
| 切换方向按钮 | [`components/button-secondary-sm.md`](../components/button-secondary-sm.md) | 圆形 36 r-full |
| 历史 Tab | [`components/tab.md`](../components/tab.md) 一级 | h40 |
| 兑换成功弹窗 | [`components/dialog.md`](../components/dialog.md) 480 | 见 5172:21659 / 5849:28709 |

## 颜色

- 立即兑换 CTA：`var(--fill-brand-button-normal)` 品牌蓝 —— **不是合约的反惯例**，闪兑是普通 CTA。
- 估算金额（≈ 前缀）：`var(--text-icon-secondary)` 二级文字。
- 滑点超阈值警告：`var(--fill-warning)` `#E0601F`。

## 反模式

- ❌ 把闪兑做成左右两栏（实际是居中单卡）。
- ❌ 收到金额用主色显示（应是估算颜色——secondary）。
- ❌ 切换方向按钮做成大尺寸（应是 36 圆形 secondary）。
- ❌ 没有显示汇率 / 滑点 / 手续费三件套（实际样本都有）。
