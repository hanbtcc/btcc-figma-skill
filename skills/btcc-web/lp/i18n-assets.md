# LP · 多语种 i18n 资产规则（i18n Assets）

> BTCC LP 必须支持 **EN / TW / KR / JR (JP)** 四语言变体，活动稳定后才会扩展到更多语种。

## 命名约定（基于 7628:74717 canvas 真实命名）

| 前缀 | 语言 | 备注 |
| --- | --- | --- |
| `EN-` | English | 国际版默认 |
| `TW-` | 繁體中文 | 台灣 / 香港 / 海外华人 |
| `KR-` | 한국어 | 韩国 |
| `JR-` 或 `JP-` | 日本語 | 日本（命名混用，需对照锚点） |
| `CN-` 或 不带前缀 | 简体中文 | 中国大陆 / 默认（少见，BTCC 主市场不在国内） |

## 多语种范式

**规则**：每个 LP 整页 frame 复制四份，分别替换：
1. **Hero 头图大字**：通常矢量化或图层化，避免点阵字模糊。
2. **倒计时单位**：天 → Day / 日 / 일 / 天。
3. **CTA 文案**：立即抽奖 / Spin Now / 立即抽獎 / 즉시 추첨 / 今すぐ抽選。
4. **任务文案**：交易满 100 USDT / Trade $100 USDT 等。
5. **奖品名称**：体验金券 / Experience Voucher / 體驗金券 / 체험권 / 体験金券。
6. **规则 long-form**：整段法律文本本地化。

**不变项**（保持四语一致）：
- 整页几何与版式
- token / 颜色
- 抽奖控件交互
- 奖品 3D 资产（[`assets-3d-prizes.md`](assets-3d-prizes.md)）
- 数字格式（仍是阿拉伯数字 + tabular-nums）

## i18n 资产清单（每个 LP 必备）

| 资产类型 | 数量 | 路径示例 |
| --- | --- | --- |
| Hero 头图（含大字） | 4 (×语种) | `lp/<theme>/hero-en.png` |
| Hero 副标 / Tagline | 4 | 通常是 SVG / 文本图层 |
| CTA 文案 | 4 | i18n 字典 |
| 倒计时标签 | 4 | i18n 字典（DD/HH/MM/SS）|
| 任务表文案 | 4 | i18n 字典 |
| 奖品名 | 4 | i18n 字典 |
| 规则 long-form | 4 | i18n 字典 |

## 字体与本地化排版

| 语种 | 主字体 | 兜底 | 注意 |
| --- | --- | --- | --- |
| EN | **Lato** | system-ui | 数字 tabular-nums，段距更宽 |
| TW | **PingFang TC** | Microsoft JhengHei, 思源黑體 | 行距比英文加 4-8px |
| KR | **Noto Sans KR** | Malgun Gothic | 韩文长度通常比英文长 1.2x |
| JR / JP | **Noto Sans JP** | Hiragino Sans, Yu Gothic | 段落标点用全角 |
| CN（如有） | **PingFang SC** | Microsoft YaHei, 思源黑体 | 同 TC 段距规则 |

**关键**：**Lato 不渲染中日韩字符**——CSS 必须 fallback 到 PingFang / Noto。
- Web 默认 stack：`"Lato", "PingFang SC", "PingFang TC", "Noto Sans KR", "Noto Sans JP", -apple-system, sans-serif`
- 见 `tokens/web-tokens.css` `--font-family-base`

## 多语种渲染常见坑

| 坑 | 影响 | 规避 |
| --- | --- | --- |
| 韩文 / 日文比英文长 | CTA / 任务文案换行 | 预留 1.2x 宽度 + 设计可换行 |
| 大字 hero 用图片 | 多语种切换时整张换图，文件巨大 | 矢量化 SVG / 分层 PNG（背景 + 文字层分离） |
| 倒计时单位本地化漏改 | "Days / 일 / 日" 错混 | i18n 字典统一管理 |
| 数字格式本地化 | 千分位 1,000 / 1.000 | 保持 1,000（业内通用），不本地化 |
| 字体 fallback 缺失 | 韩 / 日字符渲染成 ☐ ☐ ☐ | font stack 必须含 Noto |
| 规则段落直接机翻 | 法律风险 | 必须人工校对 |

## 文件命名（仓库）

```
lp/<theme>/
  README.md                链接到本 LP 选用的模板族
  hero-en.png              四语种 Hero 头图
  hero-tw.png
  hero-kr.png
  hero-jr.png
  hero-en@2x.png ...
  notes-en.md              英文 long-form 规则
  notes-tw.md
  notes-kr.md
  notes-jr.md
  i18n.json                文案字典（cta / countdown / tasks / prizes）
```

## i18n.json 结构示例

```json
{
  "en": {
    "hero_title": "Trading Carnival",
    "hero_sub": "Win up to $10,000",
    "cta_primary": "Spin Now",
    "countdown": { "d": "D", "h": "H", "m": "M", "s": "S" },
    "tasks": {
      "deposit_100": "Deposit 100 USDT",
      "trade_1000": "Trade 1,000 USDT"
    },
    "prizes": {
      "voucher_50": "50 USDT Experience Voucher"
    }
  },
  "tw": { "hero_title": "交易嘉年華", "...": "..." },
  "kr": { "hero_title": "트레이딩 카니발", "...": "..." },
  "jr": { "hero_title": "トレーディングカーニバル", "...": "..." }
}
```

## 反模式

- ❌ 只做英文一份铺到全部市场（BTCC 主市场是 TW / JP / KR，必须覆盖）。
- ❌ Hero 大字用 PNG 整张图（多语种切换文件巨大，应矢量或分层）。
- ❌ 字体 fallback 链漏 Noto Sans KR / JP（韩 / 日字符渲染成 ☐）。
- ❌ 韩 / 日 CTA 强制单行（长度比英文长，必须允许换行）。
- ❌ 规则机翻不校对（法律风险）。
- ❌ 倒计时单位"Day"在 KR / JR 模板里没本地化（漏改）。
