# SMPDL 单体审计：代数数论视角下的 Dirichlet 算术级数素数定理

> **审计对象**：代数数论中利用分圆域与类域论证明“算术级数中有无穷多素数”  
> **审计日期**：2026-10-14  
> **审计框架**：Göttingen S/M/P × D/L v1.5  
> **历史编号**：H15-PostFix  
> **总体评价**：⚪ 已确认正确（在代数数论语义内）。

---

## 1. 声明与版本

**主声明**（Dirichlet 算术级数定理，代数版本）：设整数 `q ≥ 2`，`a` 与 `q` 互素，则算术级数 `a mod q` 中包含无穷多个素数。代数证明通过考察分圆域 `ℚ(ζ_q)` 及其理想分解行为，利用类域论中的**分裂定律**来刻画素数在算术级数中的分布。

核心步骤：

1. 素数 `p`（`p ∤ q`）在 `ℚ(ζ_q)` 中完全分裂当且仅当 `p ≡ 1 (mod q)`；
2. 更一般地，`p` 在 `ℚ(ζ_q)` 中的 Frobenius 元素对应于 `p mod q ∈ (ℤ/qℤ)^×`；
3. 由 Chebotarev 密度定理，Frobenius 元素在 Galois 群 `Gal(ℚ(ζ_q)/ℚ) ≅ (ℤ/qℤ)^×` 中均匀分布；
4. 因此每个与 `q` 互素的剩余类 `a mod q` 都包含无穷多个素数，且密度为 `1/φ(q)`。

**版本信息**：
- **形式化基础**：代数数论 / 类域论（Dedekind, Weber, Hilbert, Takagi, Artin, Chebotarev；19–20 世纪）
- **依赖前提**：代数数域、分圆域、Galois 扩张、理想分解、Frobenius 元素、Chebotarev 密度定理
- **典型实例**：`q=4` 时，`ℚ(i) = ℚ(ζ_4)`；素数 `p ≡ 1 (mod 4)` 在 `ℤ[i]` 中分裂为两个素理想
- **AxiomaticBase**：`AlgebraicNumberTheory` + `ClassFieldTheory`

---

## 2. S/M/P × D/L 六格审计

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| 分圆域 `ℚ(ζ_q)` | 本原 `q` 次单位根 | ✅ |
| Galois 群 `Gal(ℚ(ζ_q)/ℚ)` | 与 `(ℤ/qℤ)^×` 同构 | ✅ |
| 理想分解 | 素数在数域中的素理想分解 | ✅ |
| Frobenius 元素 | 与 `p mod q` 对应 | ✅ |
| Chebotarev 密度定理 | Frobenius 在 Galois 群中均匀分布 | ✅ |

### 2.2 S*L — 语义逻辑结构

- 代数数论的核心策略：把“素数在算术级数中的分布”转化为“素数在代数数域中的分解行为”，再转化为 Galois 群中 Frobenius 元素的分布问题。
- 关键洞察：分圆域的 Galois 群正好编码了模 `q` 的乘法结构，因此素数的 Frobenius 元素直接对应其模 `q` 剩余类。
- ⚠️ 风险：学生容易把“完全分裂”与“剩余类为 1”的对应关系推广到任意分圆域扩张，忽略 Artin 互反律的前提。

### 2.3 M*D — 数学依存

```text
Dirichlet_AP_Algebraic(q, a)
    │
    ├── Cyclotomic field K = ℚ(ζ_q)
    │
    ├── Galois group G = Gal(K/ℚ) ≅ (ℤ/qℤ)^×
    │
    ├── Prime p ∤ q decomposes in O_K
    │
    ├── Frobenius σ_p ∈ G corresponds to p mod q
    │
    ├── Chebotarev: Frobenius elements equidistributed in G
    │
    └── For every class a mod q, infinitely many p with σ_p = a
```

- 依赖关系闭合：核心依赖代数数域、Galois 理论、Chebotarev 密度定理。

### 2.4 M*L — 数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| 分裂定律 | ✅ | `p ≡ 1 (mod q)` ⇔ `p` 在 `ℚ(ζ_q)` 中完全分裂。 |
| Frobenius 对应 | ✅ | `σ_p` 在 `G` 中对应 `p mod q`。 |
| Chebotarev 密度 | ✅ | 每个共轭类（此处每个元素）有密度 `1/|G| = 1/φ(q)`。 |
| 退化情形 | ✅ | `q=1` 退化为素数无穷；`q=4` 对应 `ℚ(i)`。 |

### 2.5 P*D / P*L — 编程层

- SageMath / PARI-GP：可计算分圆域中的素理想分解与 Frobenius 元素。
- Mathlib：代数数域、分圆域、Galois 理论的形式化正在推进；Chebotarev 密度定理形式化极具挑战。
- 风险：代数数论形式化复杂度高，远高于解析证明中的复分析步骤。

---

## 3. 判定

| 维度 | 状态 |
|---|---|
| 自然语言声明真实性 | ⚪ 真 |
| 证明正确性 | ⚪ 正确（类域论标准应用） |
| 形式化验证 | 🟡 部分支持（Mathlib 发展中；Chebotarev 定理形式化困难） |
| 与已知数学兼容性 | ✅ 与标准代数数论一致 |

**SMPDL 判定**：⚪ **低风险 / 已确认正确**（形式化实现难度高）。

---

## 4. 人类科学家可执行的验证动作

1. 对 `q=4`，验证 `ℚ(i) = ℚ(ζ_4)`，并验证素数 `p ≡ 1 (mod 4)` 在 `ℤ[i]` 中分裂（如 `5 = (2+i)(2-i)`），而 `p ≡ 3 (mod 4)` 保持惰性（如 `3` 在 `ℤ[i]` 中仍素）。
2. 用 SageMath 计算若干素数在 `ℚ(ζ_7)` 中的 Frobenius 元素，确认其与 `p mod 7` 的对应。
3. 验证 Chebotarev 密度定理在 `ℚ(ζ_q)` 中的具体实例：统计小素数按模 `q` 剩余类的分布频率。

---

## 5. 署名与许可

**Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0**
