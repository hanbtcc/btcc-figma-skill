# Upload（文件上传）

> Figma 锚点：
> - `4683:35663 文件上传`、`5886:228674`、`5009:49310 文件上传` —— KYC / 提现反馈复杂表单中的上传区
> - `2981:5538 提币-反馈` 内嵌截图凭证上传
> - 头像上传：`pages/vip.md` 编辑资料弹窗（dialog 480 内嵌）

## 用途

KYC 证件正反面、提币凭证截图、头像、地址证明等。**支持拖拽 + 点击两种触发**，必须显示上传进度条与缩略图。Web 上传**不是**简单的 `<input type="file">`，而是带视觉态的拖放区。

## 形态

| 形态 | 用途 | 几何 |
| --- | --- | --- |
| **大拖放区**（dropzone） | KYC 证件 / 地址证明 | 宽度跟父容器（dialog 内 432 / 552），高度 **160px** |
| **缩略图区**（preview） | 上传成功后展示，可删除 / 重传 | 96×96 或 120×120 r4 |
| **头像圆形** | 个人中心 | 96×96 r9999 + 右下相机 icon 28×28 |
| **行内按钮触发** | 提币凭证 / 反馈截图 | h32-h40 outline button + 旁边小字提示 |

KYC 流程默认用**大拖放区**，状态切换为缩略图。

## 几何（大拖放区，dropzone 模式）

| 属性 | 值 |
| --- | --- |
| 高度 | **160px**（拖放区主态） |
| 圆角 | **4px**（与 input 一致，不是 pill） |
| 背景 | `var(--fill-page-input)` |
| 边框 | 1px **dashed** `var(--divider-primary)`（默认） |
| Hover 边框 | 1px dashed `var(--fill-brand-button-normal)` + 背景 `var(--fill-secondary-button-hover)` |
| Active / dragover | 1px **solid** `var(--fill-brand-button-normal)` + 背景 `rgba(12,115,237,0.08)`（暗）/ `rgba(25,94,255,0.06)`（亮） |
| 错误 | 1px solid `var(--fill-error)` + 文字 `var(--text-icon-error)` |
| 内 padding | 24px 上下 + 16px 左右 |
| 主图标 | 32×32 上传 icon `var(--text-icon-secondary)`，dragover 时 → `--fill-brand-button-normal` |
| 主文案 | Lato Medium 14px `var(--text-icon-primary)`，"拖拽文件到此处或点击上传" |
| 副文案 | Lato Regular 12px `var(--text-icon-secondary)`，"支持 JPG / PNG / PDF，最大 5MB" |

## 几何（缩略图区）

| 属性 | 值 |
| --- | --- |
| 尺寸 | 96×96 或 120×120 |
| 圆角 | 4px |
| 背景 | `var(--bg-card)` |
| 图片 fit | cover，居中 |
| 删除 X | 右上角 -8/-8 偏出，圆形 24×24，背景 `rgba(0,0,0,0.6)`，icon 12 白 |
| 重传 hover | 整块覆盖 50% 黑遮罩 + "重新上传" 12px 白居中 |
| 进度遮罩 | 上传中底部 4px 进度条，brand 蓝填充，背景 `rgba(0,0,0,0.4)` 半透 |

## 状态机

```
idle ─drag enter→ dragover ─drop file→ uploading ─success→ preview
  │ ─click→ filepicker → uploading                     │
  │                                                      ▼
  │                                                    error / 删除
  ▼                                                      │
 idle  ←──────────────────────────────────────────────  ┘
```

每个状态边界都要有视觉反馈：

- **idle**：dashed 灰边 + 主文案 + 副文案。
- **dragover**：solid 蓝边 + 蓝背景 + icon 染蓝（**不要**改文案，避免抖动）。
- **uploading**：替换主图标为 spinner 24×24，主文案 → "上传中…"，下方进度条 4px 高 brand 蓝填充，百分比 12 secondary 跟随。
- **preview**：替换为缩略图（多个则排列 12px gap），左下角文件名 12 secondary 截断，右上角 X。
- **error**：边框 → error 红，主文案 → "上传失败，点击重试" red，副文案保留格式提示。

## HTML / CSS 骨架

```html
<div class="btcc-upload" data-state="idle">
  <input type="file" hidden accept="image/*,.pdf">

  <!-- idle / dragover / uploading 用同一容器，data-state 切换 -->
  <div class="btcc-upload__dropzone">
    <svg class="btcc-upload__icon" width="32" height="32"><!-- upload-cloud --></svg>
    <div class="btcc-upload__title">拖拽文件到此处或点击上传</div>
    <div class="btcc-upload__hint">支持 JPG / PNG / PDF，最大 5MB</div>
    <div class="btcc-upload__progress" hidden>
      <div class="btcc-upload__progress-bar" style="width: 0%"></div>
    </div>
  </div>

  <!-- preview 模式 -->
  <ul class="btcc-upload__preview-list" hidden>
    <li class="btcc-upload__thumb">
      <img src="…" alt="">
      <button class="btcc-upload__remove" aria-label="删除">×</button>
      <span class="btcc-upload__filename">id-front.jpg</span>
    </li>
  </ul>
</div>
```

```css
.btcc-upload__dropzone {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: var(--space-8);
  height: 160px;
  padding: var(--space-24) var(--space-16);
  background: var(--fill-page-input);
  border: 1px dashed var(--divider-primary);
  border-radius: var(--radius-input);
  cursor: pointer;
  transition: border-color .12s, background .12s;
}
.btcc-upload__dropzone:hover {
  border-color: var(--fill-brand-button-normal);
  background: var(--fill-secondary-button-hover);
}
.btcc-upload[data-state="dragover"] .btcc-upload__dropzone {
  border-style: solid;
  border-color: var(--fill-brand-button-normal);
  background: rgba(12, 115, 237, 0.08);
}
.btcc-upload[data-state="error"] .btcc-upload__dropzone {
  border-color: var(--fill-error);
}

.btcc-upload__title {
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  color: var(--text-icon-primary);
}
.btcc-upload__hint {
  font-size: var(--font-size-xs);
  color: var(--text-icon-secondary);
}

/* 进度条 */
.btcc-upload__progress {
  width: 100%;
  height: 4px;
  margin-top: var(--space-8);
  background: var(--fill-secondary-button-normal);
  border-radius: 2px;
  overflow: hidden;
}
.btcc-upload__progress-bar {
  height: 100%;
  background: var(--fill-brand-button-normal);
  transition: width .2s linear;
}

/* 缩略图 */
.btcc-upload__preview-list {
  display: flex;
  gap: var(--space-12);
  padding: 0;
  margin: 0;
  list-style: none;
}
.btcc-upload__thumb {
  position: relative;
  width: 96px;
  height: 96px;
  border-radius: var(--radius-input);
  background: var(--bg-card);
  overflow: hidden;
}
.btcc-upload__thumb img {
  width: 100%; height: 100%;
  object-fit: cover;
}
.btcc-upload__remove {
  position: absolute;
  top: -8px; right: -8px;
  width: 24px; height: 24px;
  border: none; border-radius: 100px;
  background: rgba(0, 0, 0, 0.6);
  color: #fff;
  cursor: pointer;
}
.btcc-upload__filename {
  position: absolute;
  left: 0; right: 0; bottom: 0;
  padding: 0 var(--space-8);
  height: 20px;
  line-height: 20px;
  font-size: var(--font-size-xs);
  color: #fff;
  background: rgba(0, 0, 0, 0.5);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* 头像圆形变体 */
.btcc-upload--avatar .btcc-upload__dropzone {
  width: 96px;
  height: 96px;
  padding: 0;
  border-radius: 9999px;
}
.btcc-upload--avatar .btcc-upload__title,
.btcc-upload--avatar .btcc-upload__hint { display: none; }
```

## 多文件 / 批量

KYC 证件正反面通常 2 个独立 dropzone（左 / 右排列，每个 160h），**不要**用一个 dropzone 接受多文件——避免用户混淆正反面顺序。

提现反馈 / 申诉截图允许 1 个 dropzone 接多张，已上传的缩略图横排在 dropzone 下方 gap 12，最多 3-5 张。

## 校验 / 错误

- 类型不匹配：`accept` 之外，错误态 + 文案 "格式不支持，请上传 JPG / PNG / PDF"。
- 体积超限：error 态 + "文件超过 5MB，请压缩或更换"。
- 网络失败：error 态 + "上传失败，点击重试"，主图标变 retry。
- 后端校验失败（如证件不清晰）：跳出 `dialog.md` 480 失败弹窗，**不**在 dropzone 内显示——失败弹窗能给重拍指引。

## 与 dialog 的关系

KYC 上传通常嵌在 dialog 480 / 600 内（见 `components/dialog.md`）。dropzone 宽度 = dialog 内 padding 后剩余宽度（480 - 48 = 432）。**不要**让 dropzone 自带圆角 8 与 dialog 的 8 形成双层圆角；dropzone 永远 r4。

## 反模式

- ❌ 用裸 `<input type="file">` 不包视觉态（必须有拖放区与状态切换）。
- ❌ 边框用 solid 1px（idle 必须是 dashed，dragover 才切 solid）。
- ❌ dragover 时改文案 / 改尺寸（仅改边框 + 背景 + icon 颜色，避免布局抖动）。
- ❌ dropzone 圆角 100 / 8（必须 4，与 input 一致）。
- ❌ 上传中无进度反馈（必须 spinner + 进度条 + 百分比）。
- ❌ 缩略图直接用原图（必须 cover crop 96×96 或 120×120，文件大时显示 fade-in）。
- ❌ 错误用 toast（dropzone 内错误**就在原地**显示，toast 留给跨页通知）。
- ❌ 头像上传仍用 160h dashed 拖放区（头像走 96×96 圆形变体）。
