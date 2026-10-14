# SMPDL 单体审计：Laplace 方程弱解视角下的变分存在性

> **审计对象**：弱解（Sobolev 空间）框架下 Dirichlet 问题的存在性与正则性层级  
> **审计日期**：2026-10-14  
> **审计框架**：Göttingen S/M/P × D/L v1.5  
> **历史编号**：H18-PostFix  
> **总体评价**：⚪ 已确认正确（在 H¹ 弱框架内）。

---

## 1. 声明与版本

**主声明**（弱解存在 + 正则性层级）：设 `Ω` 有界、`f ∈ L²(Ω)`、`g ∈ H^{1/2}(∂Ω)`，求 `u ∈ H¹(Ω)` 使

```text
∫_Ω ∇u·∇v dx = ∫_Ω f v dx   ∀v ∈ H₀¹(Ω)   （弱形式）
```

由 Lax–Milgram 定理，弱解存在唯一；且满足 **正则性层级**：域光滑 ⇒ `u ∈ H²`（甚至 `C^∞` 内部，Weyl 引理）；域有角点 ⇒ `u ∉ H²`（正则性失效）。

**Weyl 引理**：弱调和（`∫∇u·∇v = 0 ∀v∈C_c^∞`）⇒ `u` 内部光滑——弱解自动恢复经典性（对 Laplace 方程）。

**版本信息**：
- **形式化基础**：Sobolev 空间 + 变分方法（Sobolev, 1930s；Lax–Milgram, 1954）
- **依赖前提**：H¹ 空间、分部积分（弱导数）、Lax–Milgram、椭圆正则性
- **AxiomaticBase**：`WeakSolution` + `SobolevSpaces`
- **历史定位**：把"解"的定义从逐点满足放宽为"对测试函数积分恒等式"，用存在性换正则性。

---

## 2. S/M/P × D/L 六格审计

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| 弱导数 | 分部积分意义下的导数 | ✅ |
| 测试函数 v ∈ H₀¹ | 变分语义 | ✅ |
| 双线性形式 coercivity | Lax–Milgram 条件 | ✅ |
| Weyl 引理 | 弱 ⇒ 内部光滑 | ✅ |
| 椭圆正则性 | 域几何决定 H² | ✅ |

### 2.2 S*L — 语义逻辑结构

- 弱语义：**"解"只需对一切测试函数满足积分恒等式**——方程不必逐点成立，甚至不必逐点可微。
- ⚠️ 风险："解"同名异义（经典解 ⊆ 弱解；反向依赖方程与域）。Weyl 引理是 Laplace 特有的"弱→强"恢复，不能推广到一般方程。

### 2.3 M*D — 数学依存

```text
WeakSolutionFramework
    │
    ├── Sobolev space H¹, H₀¹
    │
    ├── Bilinear form a(u,v) = ∫∇u·∇v
    │       └── coercive (Poincaré)
    │
    ├── Lax–Milgram ⇒ ∃! u ∈ H¹
    │
    ├── Weyl lemma ⇒ u smooth interior
    │
    └── Corner domain ⇒ u ∉ H² (regularity breaks)
```

### 2.4 M*L — 数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| Lax–Milgram 应用 | ✅ | coercivity 由 Poincaré 不等式。 |
| 唯一性 | ✅ | 能量方法。 |
| Weyl 引理 | ✅ | Laplace 特有的正则性恢复。 |
| 角点反例 | ✅ | L 形域角点处梯度奇异。 |

### 2.5 P*D / P*L — 编程层

- FEniCS / FreeFEM：弱形式直接可编码——P 层与弱框架高度协同。
- Mathlib：Sobolev 空间形式化发展中。

---

## 3. 判定

| 维度 | 状态 |
|---|---|
| 声明真实性 | ⚪ 真 |
| 证明正确性 | ⚪ 正确 |
| 形式化验证 | 🟡 发展中（CAS/FEM 工程支持强） |
| 兼容性 | ✅ 现代偏微分方程理论 |

**SMPDL 判定**：⚪ **低风险 / 已确认正确**。

---

## 4. 人类科学家可执行的验证动作

1. 验证 Poincaré 不等式给出 coercivity，从而 Lax–Milgram 适用。
2. 证明弱解的唯一性（能量估计）。
3. 构造 L 形域角点奇异解 `u = r^{2/3} sin(2θ/3)`，验证 `u ∉ H²`。

---

## 5. 署名与许可

**Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0**
