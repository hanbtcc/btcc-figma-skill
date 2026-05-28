---
name: btcc-shared
description: BTCC 设计语言跨平台规则。被 btcc-app 与 btcc-web 引用。不直接生成代码。
---

# btcc-shared

跨平台 SSOT。一个文件：[`rules-shared.md`](rules-shared.md)。

## 何时进入

- 修改 R-SHARED-* 规则。
- 在 btcc-app 或 btcc-web 引用 shared 规则前，先读这里。

## 何时不进入

- 生成具体页面/组件 → 进 btcc-app 或 btcc-web。
- 调 token 值 → 进对应平台的 `tokens/`。

## 规则索引

- R-SHARED-1 操作优先
- R-SHARED-2 颜色即状态
- R-SHARED-3 未验证标记
- R-SHARED-4 Token 命名空间
- R-SHARED-5 数据呈现
- R-SHARED-6 图标语言
- R-SHARED-7 SSOT

详见 [rules-shared.md](rules-shared.md)。
