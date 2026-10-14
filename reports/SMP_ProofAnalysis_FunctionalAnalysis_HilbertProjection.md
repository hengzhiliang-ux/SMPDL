# SMPDL 单体审计：Hilbert 空间视角下的正交投影定理

> **审计对象**：Hilbert 空间中闭凸集上的正交投影与 Riesz 表示  
> **审计日期**：2026-10-14  
> **审计框架**：Göttingen S/M/P × D/L v1.5  
> **历史编号**：H23-PreFix  
> **总体评价**：⚪ 已确认正确（在内积结构语义内）。

---

## 1. 声明与版本

**主声明**（正交投影定理 + Riesz 表示）：设 `H` 为 Hilbert 空间（完备内积空间），`C ⊆ H` 非空闭凸，则对任意 `x ∈ H`：

1. **存在唯一** `P_C(x) ∈ C` 使 `‖x - P_C(x)‖ = dist(x, C)`；
2. 投影由**变分不等式**刻画：`⟨x - P_C x, c - P_C x⟩ ≤ 0 ∀c ∈ C`；
3. 特例 `C = M`（闭子空间）：`H = M ⊕ M^⊥`，正交分解；
4. **Riesz 表示**：每个连续线性泛函 `f ∈ H*` 可写为 `f(x) = ⟨x, y⟩`，且 `‖f‖ = ‖y‖`——**对偶空间自同构** `H* ≅ H`。

**版本信息**：
- **形式化基础**：Hilbert 空间理论（Hilbert 1900s；Riesz 1907）
- **依赖前提**：内积、完备性、平行四边形恒等式
- **AxiomaticBase**：`HilbertSpace` + `InnerProduct`
- **历史定位**：几何直觉（垂直、投影）在无穷维的完整保留——内积是"几何性"的全部来源。

---

## 2. S/M/P × D/L 六格审计

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| 内积 | 线性 + 共轭对称 + 正定 | ✅ |
| 完备性 | Cauchy 列收敛 | ✅ |
| 平行四边形恒等式 | 投影存在性证明核心 | ✅ |
| 变分不等式 | 投影的刻画 | ✅ |
| Riesz 表示 | 对偶同构 | ✅ |

### 2.2 S*L — 语义逻辑结构

- Hilbert 语义：**角度与长度共存**（内积诱导范数），"垂直"可定义——欧氏几何的直觉得以延续。
- 闭凸集投影的存在性证明本质用平行四边形恒等式 + 完备性——两者都是内积结构的礼物。
- ⚠️ 风险：把"投影存在"归功于完备性而忽视内积——Banach 空间（完备但无内积）投影即失效（见 PostFix）。

### 2.3 M*D — 数学依存

```text
HilbertProjection
    │
    ├── Inner product → norm + angles
    │
    ├── Parallelogram identity
    │
    ├── Completeness → minimizing sequence converges
    │
    ├── Projection theorem + variational inequality
    │
    └── Riesz representation: H* ≅ H (self-dual)
```

### 2.4 M*L — 数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| 投影存在唯一 | ✅ | 闭凸集。 |
| 正交分解 | ✅ | 闭子空间。 |
| Riesz 同构 | ✅ | 共轭线性同构。 |
| 平行四边形必要性 | ✅ | 范数满足它 ⇔ 来自内积（Jordan–von Neumann）。 |

### 2.5 P*D / P*L — 编程层

- Mathlib：`InnerProductSpace` 与投影、Riesz 均有形式化。

---

## 3. 判定

| 维度 | 状态 |
|---|---|
| 声明真实性 | ⚪ 真 |
| 证明正确性 | ⚪ 正确 |
| 形式化验证 | 🟢 Mathlib 成熟 |
| 兼容性 | ✅ 泛函分析标准 |

**SMPDL 判定**：⚪ **低风险 / 已确认正确**。

---

## 4. 人类科学家可执行的验证动作

1. 用平行四边形恒等式完成极小化序列收敛证明。
2. 验证闭子空间分解 `H = M ⊕ M^⊥`。
3. 用 Jordan–von Neumann 定理验证 `ℓ¹` 范数不满足平行四边形恒等式（预告 Banach 侧失效）。

---

## 5. 署名与许可

**Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0**
