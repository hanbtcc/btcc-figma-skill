# Dialog（弹窗 / Modal）

> Figma 锚点：BTCC Web 的弹窗**没有单一 master**，但有大量同构样本，宽度极有规律。

## 弹窗宽度规律（基于 1558:14723 全站合集）

| 宽度 | 出现频次 | 用途 |
| --- | --- | --- |
| **480px** | 130+ 个 | 表单类弹窗（充值、提现、绑定邮箱、修改密码、添加银行账户、KYC、安全验证、Alert Dialog） |
| 600px | ~20 个 | 提现反馈、内容多于表单的复杂确认（如 `2981:5538 提币-反馈`） |
| **680px** | ~8 个 | 大尺寸数据弹窗（如 `130478:45854 Alert Dialog对话框`、`130479:87577 支付结果-弹窗最高`） |
| 432–434px | 少量 | 如 `128343:195522`，特殊紧凑变体 |
| 552px | 1 个 | `128343:195716 Alert`（横条变体） |

## 几何（480px 表单弹窗为例）

| 属性 | 值 |
| --- | --- |
| 宽度 | **480 / 600 / 680** 三档（不响应式） |
| 圆角 | **8px**（card 外圆角） |
| 阴影 | `var(--shadow-dialog)` `0 12px 24px rgba(0,0,0,0.32)` |
| 背景 | `var(--bg-card)` `#13171b` |
| 内 padding | 24px 上 + 24px 左右 + 24px 下 |
| 标题字号 | Lato Bold 16-20px |
| 标题字色 | `var(--text-icon-primary)` |
| body 字号 | Lato Medium 14px / 20px |
| 关闭 X | 16px，右上角，距上 24、距右 24 |
| 底部按钮区 | 距 body 24px；button 用 `--h-button` 48px pill 100；2 个按钮时间距 12px |

## 标准结构

```html
<div class="btcc-dialog-mask" role="presentation"></div>
<div class="btcc-dialog" role="dialog" aria-modal="true" aria-labelledby="dlg-title">
  <button class="btcc-dialog__close" aria-label="Close">×</button>
  <h2 class="btcc-dialog__title" id="dlg-title">绑定邮箱</h2>
  <div class="btcc-dialog__body">
    <!-- 表单 / 内容 -->
  </div>
  <div class="btcc-dialog__footer">
    <button class="btcc-btn-outline">取消</button>
    <button class="btcc-btn-primary">确认</button>
  </div>
</div>
```

## CSS

```css
.btcc-dialog-mask {
  position: fixed; inset: 0;
  background: rgba(0, 0, 0, 0.6);
  z-index: 1000;
}
.btcc-dialog {
  position: fixed;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  width: 480px;
  background: var(--bg-card);
  border-radius: var(--radius-dialog);  /* 8 */
  box-shadow: var(--shadow-dialog);
  padding: var(--space-24);
  color: var(--text-icon-primary);
  z-index: 1001;
}
.btcc-dialog--md { width: 600px; }
.btcc-dialog--lg { width: 680px; }
.btcc-dialog__close {
  position: absolute;
  top: var(--space-24); right: var(--space-24);
  width: 16px; height: 16px;
  border: none; background: transparent;
  color: var(--text-icon-secondary);
  cursor: pointer;
}
.btcc-dialog__close:hover { color: var(--text-icon-primary); }
.btcc-dialog__title {
  margin: 0 0 var(--space-16) 0;
  font-family: var(--font-family-base);
  font-size: var(--font-size-md);
  font-weight: var(--font-weight-bold);
  color: var(--text-icon-primary);
}
.btcc-dialog__body {
  font-family: var(--font-family-base);
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  line-height: 20px;
  color: var(--text-icon-primary);
}
.btcc-dialog__footer {
  display: flex; gap: var(--space-12);
  margin-top: var(--space-24);
  justify-content: flex-end;
}
```

## 弹窗类型清单（来自 1558:14723，告诉你"应该用什么"）

| 类型 | 样本 nodeId | 宽 | 备注 |
| --- | --- | --- | --- |
| 表单弹窗（输入信息） | `9252:29042 修改密码`、`10271:154427 绑定手机`、`10271:154672 国家` | 480 | 标题 + form + 主/副 button |
| 安全验证弹窗 | `123438:151547 / 125938:192533` | 480 | 标题 + 验证码输入 + 倒计时 |
| 选择列表弹窗 | `6332:9326 / 8559:113581 选择支付方式`、`6339:8220 推荐银行` | 400-480 | 标题 + 卡列表 + 取消 |
| 提示确认（Alert Dialog） | `129661:304594 / 130534:113350 / 130615:116845` | 480 | 标题 + 一段说明 + 主/副 button |
| 提交反馈 | `4683:35561 提现成功`、`110432:32673 兑换成功` | 480 / 375（h5） | 图标 + 文字 + 单 button |
| 失败反馈 | `110338:201920 / 129275:224645 身分資料驗證失敗` | 480 | 红色 icon + 文字 + 重试 |
| 充值到账 | `107643:38636 充值到账弹窗` | 480 | 金额突出 + button |
| 卡券奖励 | `108783:53109 / 111333:101659 体验金` | 480 | 卡券图 + 描述 + 领取 button |
| 升级 / 引导 | `111333:101719 升级说明`、`126734:136611` | 480 | 图 + bullet 列表 + 立即升级 |
| 复杂表单 | `4683:35663 文件上传`、`10406:55318 银行卡` | 480-600 | 多 step 或 多分组 |
| 支付结果（最高） | `130479:87577 支付结果-弹窗最高` | 680 | 复杂结果展示 |

## 反模式

- ❌ 弹窗用响应式百分比宽（实际固定 480/600/680）
- ❌ 弹窗圆角 16 / 24 / 32（实际 8）
- ❌ 弹窗内 button 不用 pill 100（实际同主 CTA：48 / 100）
- ❌ 关闭 X 用大尺寸（实际 16px，右上 24/24）
- ❌ 多个一级 button（弹窗只允许一个，副操作用 outline）
