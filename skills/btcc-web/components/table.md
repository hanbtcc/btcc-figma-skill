# Table（数据表格）

> Figma 锚点：BTCC Web 的表格**没有单一 master 组件**，但在 1558:14723 中有大量同构样本：
> - `2613:24075 盈亏分析`、`2609:24071 我的卡券`、`9590:15462 资金记录`、`5896:9053 合约pro` 委托区、`9307:18488 API管理`、`5896:8500 资产总览`、`100586:121640 交易报表`、`7752:73942 jjj交易赛` 排行榜

## 用途

所有以**行 × 列**结构呈现的数据：委托记录、持仓、资金记录、资产明细、API 列表、卡券列表、排行榜、交易报表、盈亏分析、银行卡 / 提币地址列表。

**不是表格的场景**：
- 单条数据 → 用卡片（resp `bg-card` r4）。
- 配对的 key/value 列表 → 用 `definition list`，不要硬塞表格。
- 盘口 → 走 [`orderbook.md`](orderbook.md)（行高 24，专用样式）。

## 行高规约

| 业务 | 行高 | 备注 |
| --- | --- | --- |
| 委托 / 持仓 / 资金费率 | **40px** | 紧凑、密度高，价格列 tabular-nums |
| 资金记录 / 卡券 / 银行卡 / API / 资产 | **56px** | 含 24 logo / icon + 双行文字 |
| 排行榜 | **56px** | 含 32 头像 + 用户名脱敏 |
| 列头 | **24px** 或 **40px** | 列头与首行差 16-32 间距 |

行高从来不是 32 / 48；不要插值。

## 几何（56h 行为例）

| 属性 | 值 |
| --- | --- |
| 容器宽 | 内容容器 1200 / 1556（按页面） |
| 容器圆角 | 4px（外圆角） |
| 容器背景 | `var(--bg-card)` 或透明（嵌入卡片内） |
| 列头背景 | `var(--bg-primary)` 或 `transparent` |
| 列头分隔 | 底部 1px `var(--divider-primary)` |
| 行分隔 | 底部 1px `var(--divider-primary)` |
| 行 hover | `var(--fill-secondary-button-hover)` |
| 行 padding | 0 16 |
| 列对齐 | 文字左、数字右、操作右 |

## 字体

- 列头：Lato Medium 12px `var(--text-icon-secondary)`。
- 单元格：Lato Medium 14px `var(--text-icon-primary)`。
- 数字 / 价格 / 时间：**`font-variant-numeric: tabular-nums` 必加**（R-SHARED-5）。
- 中文环境（如分页 / 排行榜中文用户名）：PingFang SC Regular 14px。

## 状态标签（行内 pill）

成功 / 处理中 / 失败 / 已过期 等状态用**行内小 pill**：

| 状态 | 文字色 | 背景 | 边框 |
| --- | --- | --- | --- |
| 成功 | `var(--text-icon-success)` | rgba(44,168,93,0.12) | none |
| 处理中 | `var(--text-icon-warning)` | rgba(224,96,31,0.12) | none |
| 失败 | `var(--text-icon-error)` | rgba(235,70,79,0.12) | none |
| 已过期 / 中性 | `var(--text-icon-secondary)` | rgba(135,143,153,0.12) | none |

pill 高 20-22，padding 0 8，圆角 100，字号 12，不带描边。

## HTML / CSS 骨架

```html
<table class="btcc-table btcc-table--56">
  <thead>
    <tr>
      <th>时间</th>
      <th>类型</th>
      <th>币种</th>
      <th class="num">数量</th>
      <th>状态</th>
      <th>备注 / TXID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="num">2026-05-28 14:23</td>
      <td>充币</td>
      <td>USDT</td>
      <td class="num pos">+100.00</td>
      <td><span class="btcc-pill btcc-pill--success">成功</span></td>
      <td><span class="btcc-mono-trunc">0x1A2B…3F4D</span></td>
    </tr>
    <!-- ... -->
  </tbody>
</table>
```

```css
.btcc-table {
  width: 100%;
  border-collapse: collapse;
  font-family: var(--font-family-base);
  color: var(--text-icon-primary);
}
.btcc-table thead th {
  height: 40px;
  padding: 0 var(--space-16);
  text-align: left;
  font-size: var(--font-size-xs);
  font-weight: var(--font-weight-medium);
  color: var(--text-icon-secondary);
  border-bottom: 1px solid var(--divider-primary);
}
.btcc-table tbody td {
  padding: 0 var(--space-16);
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  border-bottom: 1px solid var(--divider-primary);
  vertical-align: middle;
}
.btcc-table--40 tbody tr { height: 40px; }
.btcc-table--56 tbody tr { height: 56px; }
.btcc-table tbody tr:hover { background: var(--fill-secondary-button-hover); }

.btcc-table th.num,
.btcc-table td.num {
  text-align: right;
  font-variant-numeric: tabular-nums;
}
.btcc-table td.pos { color: var(--text-icon-success); }
.btcc-table td.neg { color: var(--text-icon-error); }

/* 行内状态 pill */
.btcc-pill {
  display: inline-flex;
  align-items: center;
  height: 22px;
  padding: 0 var(--space-8);
  border-radius: 100px;
  font-size: var(--font-size-xs);
  font-weight: var(--font-weight-medium);
}
.btcc-pill--success { color: var(--text-icon-success); background: rgba(44, 168, 93, 0.12); }
.btcc-pill--warning { color: var(--text-icon-warning); background: rgba(224, 96, 31, 0.12); }
.btcc-pill--error   { color: var(--text-icon-error);   background: rgba(235, 70, 79, 0.12); }
.btcc-pill--muted   { color: var(--text-icon-secondary); background: rgba(135, 143, 153, 0.12); }

/* hash / TXID 截断 */
.btcc-mono-trunc {
  font-family: var(--font-family-num);
  font-variant-numeric: tabular-nums;
  color: var(--text-icon-secondary);
  cursor: pointer;
}
```

## 排行榜行（顶 3 + 普通 4-100）

排行榜表格行高 56，但**顶 3** 单独走 `template-trading-contest.md` 的 280h 领奖台，不进表格。表格从第 4 名开始，列：

```
名次 │ 用户        │ 交易量(USDT) │ 奖金(USDT) │
4    │ 0x12***34  │ 12,345.67    │ 50.00      │
```

我的排名行：sticky 置顶 56h，背景 `rgba(12,115,237,0.08)`（暗）/ `rgba(25,94,255,0.06)`（亮），边框 1px solid `var(--fill-brand-button-normal)`。

## 空态 / 加载态

| 态 | 处理 |
| --- | --- |
| 空 | 表格高度退化为 ~280，居中插画 + "暂无数据" 14px secondary |
| 加载中 | tbody 用 6-10 行骨架（背景 `var(--fill-secondary-button-normal)`，闪烁） |
| 错误 | 占位 + "重试" outline button |

## 反模式

- ❌ 行高 32 / 48 / 64（实际 40 或 56，不插值）。
- ❌ 数字列左对齐或居中（数字必须右对齐 + tabular-nums）。
- ❌ 状态用文字色着色而无背景 pill（行内状态用 pill，纯文字色读起来太弱）。
- ❌ 列头加粗 700（实际 Medium 500，secondary 灰）。
- ❌ 行 hover 背景用 brand 蓝（hover 用 `--fill-secondary-button-hover` 中性灰）。
- ❌ TXID / 地址 完整显示（必须截断 + hover 完整 + 复制）。
- ❌ 把表格塞进卡片再加自己的圆角 8（应外层用 r4，避免双层圆角）。
