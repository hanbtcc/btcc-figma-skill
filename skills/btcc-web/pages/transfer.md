# 划转（Transfer）

> Figma 锚点（1558:14723 内）：
> - **Web**：`101930:12213`、`108208:21377` 划转
> - **H5 / 弹窗**：`9949:70622`、`103707:58432` 划转

## 用途

账户内部资金划转：合约 ↔ 现货 ↔ 法币 ↔ 跟单 等账户间的币种转移，不出链不收费。常以**弹窗形式**触发（从资产总览页或下单区"余额不足"提示）。

## 形态

| 触发位置 | 形态 | 锚点 |
| --- | --- | --- |
| 资产总览操作按钮 | 全屏弹窗 480 | `9949:70622` |
| 合约 pro 下单"余额不足"提示 | 浮层 580（dropdown 模式） | inline |
| H5 总览 | 整页（375 宽） | `103707:58432` |

## 表单结构（弹窗 480）

```
划转                                       ✕
─────────────────────────────────────────────
从     [▼ 现货账户          ]
       余额：1,234.56 USDT
   ↕ 切换方向（圆形 36 secondary）
到     [▼ 合约账户          ]

币种   [▼ USDT              ]

数量   [-][_____  100  ][+]  [全部]
        余额 1,234.56 USDT

ⓘ 划转免手续费 / 即时到账

[      确认划转      ] pill 100 / h48 / 宽满
```

## 关键模块 → 组件

| 模块 | 组件文件 | 备注 |
| --- | --- | --- |
| 弹窗容器 | [`components/dialog.md`](../components/dialog.md) | 480 r8 |
| 账户 dropdown | [`components/selector.md`](../components/selector.md) | A 模式 |
| 切换方向圆形按钮 | [`components/button-secondary-sm.md`](../components/button-secondary-sm.md) | 36 r-full（圆形变体） |
| 数量 input + 步进 + 全部 | [`components/input.md`](../components/input.md) 步进版 | h48 r4 |
| 提示 alert | [`components/alert.md`](../components/alert.md) | info 蓝 |
| 确认 CTA | [`components/button-primary.md`](../components/button-primary.md) | 宽满 432 / pill 100 |

## 反模式

- ❌ 划转单独成页（实际主要是弹窗形态，整页只在 H5 出现）。
- ❌ 切换方向用文字 button（应是圆形 36 secondary）。
- ❌ 划转有手续费提示（实际免费，alert info 表达即可）。
- ❌ "从 / 到"用单选 radio（实际是两个 dropdown，可任意组合）。
