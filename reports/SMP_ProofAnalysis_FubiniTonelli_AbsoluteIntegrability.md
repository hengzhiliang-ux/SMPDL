# SMPDL 单体审计：Fubini/Tonelli 定理视角下的交换条件刻画

> **审计对象**：乘积测度与 σ-可积性框架下逐次积分交换的充要条件  
> **审计日期**：2026-10-14  
> **审计框架**：Göttingen S/M/P × D/L v1.5  
> **历史编号**：H30-PostFix  
> **总体评价**：⚪ 已确认正确——Fubini + Tonelli 分工完成律的"定价表"。

---

## 1. 声明与版本

**主声明**（Fubini–Tonelli 双定理群）：设 `(X,μ)`、`(Y,ν)` 为 σ-有限测度空间，`f` 可测：

1. **Tonelli（非负侧，1909）**：`f ≥ 0` 时，**无需任何可积性假设**：

```text
∫∫ f d(μ×ν) = ∫ [∫ f dν] dμ = ∫ [∫ f dμ] dν   （三者同 ±∞）
```

——非负世界**免费享有交换律**；
2. **Fubini（可积侧，1907）**：`f ∈ L¹(μ×ν)`（绝对可积）时，三个积分均有限且相等——**交换的充分条件**；且逐次内层 a.e. 有定义；
3. **组合用法（教科书标准流程）**：先对 `|f|` 用 Tonelli 判断可积性，再对 `f` 用 Fubini 交换——"Tonelli 试金，Fubini 结账"；
4. **结构根源**：交换律失效的精确原因是**乘积测度的定义依赖截面一致性**——σ-有限性保证截面测度唯一，条件收敛破坏 a.e. 截面结构；
5. **推论**：σ-有限性不可去（非 σ-有限测度上有真反例）；一维对应 = 绝对收敛级数可任意重排（Levi/Lebesgue）。

**版本信息**：
- **形式化基础**：Fubini 1907 / Tonelli 1909（Lebesgue 测度论框架的产物——H17 引擎的直接下游）
- **依赖前提**：乘积测度、σ-有限性、单调收敛（MCT）
- **AxiomaticBase**：`ProductMeasure` + `SigmaFinite` + `FubiniTonelli`
- **历史定位**：L6 裁决完成——Cauchy 时代的疑问在测度论中获得充要定价。

---

## 2. S/M/P × D/L 六格审计

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| 乘积测度 μ×ν | 截面一致性 | ✅ |
| σ-有限性 | 可数覆盖 | ✅ |
| Tonelli（f≥0 免费交换） | MCT | ✅ |
| Fubini（L¹ ⇒ 交换） | 截面 a.e. 可积 | ✅ |
| 试金-结账流程 | 教科书标准 | ✅ |

### 2.2 S*L — 语义逻辑结构

- PostFix 语义：**交换律获得精确定价**——非负 = 免费；绝对可积 = 标准价；条件收敛 = 禁区（±π/4 反例驻守）；
- "积分"从"一个数"升格为"一个带条件的三元等式群"；
- ⚠️ 风险：忽略 σ-有限性（反例存在）；把 Tonelli 的"允许 ∞"误用于符号函数（f≥0 是前提不是技术性假设）。

### 2.3 M*D — 数学依存

```text
FubiniTonelli
    │
    ├── product measure (via π-λ / Carathéodory)
    │
    ├── σ-finiteness → unique section measures
    │
    ├── Tonelli: f ≥ 0 ⇒ free interchange (three values agree in [0,∞])
    │
    ├── Fubini: f ∈ L¹ ⇒ interchange valid, finite
    │
    └── Combined workflow: Tonelli on |f| → integrability check → Fubini on f
```

### 2.4 M*L — 数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| Tonelli 无条件性 | ✅ | MCT 直推。 |
| Fubini 充分性 | ✅ | 截面定理。 |
| 反例纳入 | ✅ | ±π/4 恰因 ∫∫\|f\|=∞ 而落界外。 |
| σ-有限必要性 | ✅ | 已知反例。 |

### 2.5 P*D / P*L — 编程层

- Mathlib：`MeasureTheory.Product` 层级完整（`Measure.prod`、Fubini 定理族已形式化）；σ-有限作为类型类假设出现——**库级"律定价"的可视化**。

---

## 3. 判定

| 维度 | 状态 |
|---|---|
| 声明真实性 | ⚪ 真 |
| 证明正确性 | ⚪ 正确（Fubini/Tonelli） |
| 形式化验证 | 🟢 Mathlib 完整 |
| 兼容性 | ✅ 现代测度论标准 |

**SMPDL 判定**：⚪ **低风险 / 已确认正确**。

---

## 4. 人类科学家可执行的验证动作

1. 用 Tonelli 对 PreFix 反例的 |f| 判出 ∞（确认落界外）。
2. 完整走一遍"试金-结账"流程于一个正例（如 `e^{-xy}` 于 (0,∞)×(0,1)）。
3. 检查 Mathlib 中 Fubini 定理的 σ-有限类型类约束。

---

## 5. 署名与许可

**Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0**
