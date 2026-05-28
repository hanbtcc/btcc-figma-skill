# 顶部导航（Top Nav）

> Figma 锚点：`647:12465 顶部导航栏`（1961×185 master，常见渲染高 ~64-72）。

## 用途

每个登录态页面顶部一根。包含：左 logo、中产品 / 业务 tab、右账户 / 下载 / 通知 / 设置入口。

## 几何

| 属性 | 值 |
| --- | --- |
| 高度 | 64-72px（操作页 64，LP/营销页 72） |
| 容器宽 | 1920（全宽，不限制内容容器） |
| Padding | 0 24px（左右） |
| 背景 | `var(--bg-primary)`（暗）/`var(--bg-card)`（亮） |
| 底边 | 1px solid `var(--divider-primary)` |
| logo 高 | 24-28px |

## 内容分区

```
[ Logo |  产品 Tab（合约 / 现货 / 资产 / 行情 / 跟单 / C2C）  ] · · · [ 通知 | 钱包 | 头像 | 下载 | 语言 ]
```

- **左**：logo + 一级产品 Tab（用 [`tab.md`](tab.md) 一级 Tab 样式）。
- **中（少见）**：搜索框（合约页才有；用 [`input.md`](input.md) 但高度 36-40，加 search icon）。
- **右**：图标按钮组，每个图标 24px，间距 16；带数字角标的通知/购物车在右上角加小红点 8×8。

## 顶部 nav 之上的"selected pair"行

> Figma 锚点：`651:13295 已选列表`（1556×32），`647:12512 右顶信息`（1556×56）。

合约 / 现货 / 闪兑页面的**子级 nav** 信息行：

| 区域 | 内容 |
| --- | --- |
| 左 | 已选交易对（如 BTC/USDT），价格，24h 涨跌 |
| 中 | 24h 高 / 低 / 量 |
| 右 | "更多" / "K 线" / "深度图" 切换按钮 |

字号统一 Lato Medium 12-14px。数字 tabular-nums。

## CSS

```css
.btcc-topnav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 64px;
  padding: 0 var(--space-24);
  background: var(--bg-primary);
  border-bottom: 1px solid var(--divider-primary);
}
.btcc-topnav__left  { display: flex; align-items: center; gap: var(--space-32); }
.btcc-topnav__right { display: flex; align-items: center; gap: var(--space-16); }
.btcc-topnav__logo  { height: 24px; }
.btcc-topnav__icon  {
  width: 24px; height: 24px;
  background: none; border: none;
  color: var(--text-icon-primary);
  cursor: pointer;
}
.btcc-topnav__icon:hover { color: var(--fill-brand-button-normal); }
```

## 反模式

- ❌ 顶部 nav 高 80 / 96（实际 64-72）
- ❌ 用品牌蓝当 nav 背景（背景应是 `bg-primary`，仅 Logo / hover 用蓝）
- ❌ 顶部 nav 加阴影（不用，仅一根 1px 底边）
- ❌ 把次级 button / pill 形状塞进 nav（产品 Tab 用底部 2px 线，不用 pill）
