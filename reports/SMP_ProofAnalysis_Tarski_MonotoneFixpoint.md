# SMPDL 单体审计：Tarski 单调不动点定理

> **审计对象**：完全格上单调映射的不动点理论——单调律在位时的免费午餐  
> **审计日期**：2026-10-14  
> **审计框架**：Göttingen S/M/P × D/L v1.5  
> **历史编号**：H32-PreFix  
> **总体评价**：⚪ 已确认正确（在单调语义内）。

---

## 1. 声明与版本

**主声明**（Tarski 不动点定理，1955）：设 `L` 为**完全格**（任意子集有上确界与下确界），`f: L → L` **单调**（`x ≤ y ⇒ f(x) ≤ f(y)`），则：

1. `f` 的不动点集合 `Fix(f)` 非空且本身构成**完全格**（有最小不动点 `⊥* = ∧{x : f(x) ≤ x}` 与最大不动点）；
2. 最小不动点由**超限迭代**达到：`f^α(⊥)`（α 历经序数）稳定于 `lfp(f)`；
3. **不需要任何连续性/压缩性**——纯单调即得不动点存在——与 Banach 压缩映射（1922）的"度量 + 压缩"条件形成**双路线分工**。

**伴生定理群（单调世界全家福）**：
- **Knaster–Tarski**（最小不动点刻画）：`lfp(f) = ∧{x : f(x) ≤ x}`；
- **Kleene 不动点定理**（ω-链版本）：`f` 连续（Scott 连续）时 `lfp = ⊔ fⁿ(⊥)`——程序设计语言的指称语义基础；
- **Cousot–Cousot（1979）**：把 Tarski 精化到收缩算子（abstract interpretation 产业的理论核）。

**版本信息**：
- **形式化基础**：Tarski 1955（A. Tarski, "A lattice-theoretical fixpoint theorem and its applications"）；前驱 Knaster 1928
- **依赖前提**：完全格、单调性
- **AxiomaticBase**：`CompleteLattice` + `MonotoneMap`
- **历史定位**：L1 远古（不等式推理隐用单调两千年）→ L6（Tarski 1955 表征 + Cousot 产业）。

---

## 2. S/M/P × D/L 六格审计

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| 完全格 | ∧/∨ 全存在 | ✅ |
| 单调性 | 保序 | ✅ |
| 前不动点集 {x : f(x) ≤ x} | lfp 刻画 | ✅ |
| 超限迭代 | 序数爬升 | ✅ |
| Kleene/CC 精化 | 连续版/收缩版 | ✅ |

### 2.2 S*L — 语义逻辑结构

- 单调语义核心：**"序的保持 ⇒ 平衡点的存在"**——无需度量、无需压缩，纯序结构免费送不动点；
- 最小不动点是"从底向上爬"的构造终点——序直觉完整保留。
- ⚠️ 风险：把 Tarski 用于非完全格/非单调映射——两个前提缺一即崩（见 PostFix）。

### 2.3 M*D — 数学依存

```text
MonotoneWorld
    │
    ├── complete lattice L
    │
    ├── f monotone
    │
    ├── Knaster–Tarski: lfp = ∧ pre-fixed points
    │
    ├── Fix(f) is itself a complete lattice
    │
    └── refinements: Kleene (ω-chain, continuity) / Cousot–Cousot (industry)
```

### 2.4 M*L — 数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| Tarski 定理 | ✅ | 纯序证明。 |
| 不动点集合格结构 | ✅ | 完全格。 |
| 与 Banach 分工 | ✅ | 序 vs 度量两路线。 |

### 2.5 P*D / P*L — 编程层

- Mathlib：`CompleteLattice`/`order.lfp` 完整（`lfp_le` 等定理族）；Kleene 版亦有——**静态分析产业（Cousot）的库级依托**。

---

## 3. 判定

| 维度 | 状态 |
|---|---|
| 声明真实性 | ⚪ 真 |
| 证明正确性 | ⚪ 正确（Tarski） |
| 形式化验证 | 🟢 Mathlib 完整 |
| 兼容性 | ✅ 序理论标准 |

**SMPDL 判定**：⚪ **低风险 / 已确认正确**。

---

## 4. 人类科学家可执行的验证动作

1. 证明 `∧{x : f(x) ≤ x}` 是不动点（Tarski 核心两行）。
2. 验证 Kleene 版在 Scott 连续下的 ω-链到达。
3. 对比 Banach（度量+压缩）与 Tarski（格+单调）条件集的交集为空。

---

## 5. 署名与许可

**Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0**
