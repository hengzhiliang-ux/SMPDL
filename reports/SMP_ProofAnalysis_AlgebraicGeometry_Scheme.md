# SMPDL 单体审计：概形视角下的仿射 Nullstellensatz

> **审计对象**：现代代数几何中“多项式方程零点集”的概形表述  
> **审计日期**：2026-10-14  
> **审计框架**：Göttingen S/M/P × D/L v1.5  
> **历史编号**：H14-PostFix  
> **总体评价**：⚪ 已确认正确（在概形论语义内）。

---

## 1. 声明与版本

**主声明**（仿射概形的 Nullstellensatz 对应）：设 `R` 为交换环，`Spec(R)` 为其素谱，配备 Zariski 拓扑与结构层 `𝒪_{Spec(R)}`，则

```text
R 的理想 I  ↔  Spec(R) 的闭子概形 Y = Spec(R/I)
```

并且 `I(Y) = ker(R → Γ(Y, 𝒪_Y)) = I`，即概形框架下理想与闭子概形一一对应，无需取根。

**版本信息**：
- **形式化基础**：概形理论（Grothendieck, EGA, 1960s）
- **依赖前提**：交换环、素谱、层论、局部环、局部化、概形
- **典型实例**：`Spec(ℂ[x,y]/(x²))` 是比 `Spec(ℂ[x,y]/(x))` 更“厚”的闭子概形，携带幂零信息
- **AxiomaticBase**：`SchemeTheory` + `SheafTheory`

---

## 2. S/M/P × D/L 六格审计

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| 交换环 `R` | 加法群 + 乘法幺半群 + 分配律 | ✅ |
| 素谱 `Spec(R)` | 环的所有素理想集合 | ✅ |
| Zariski 拓扑 | 闭集由理想定义 | ✅ |
| 结构层 `𝒪_{Spec(R)}` | 在每个素理想处取局部化 `R_p` | ✅ |
| 闭子概形 `Spec(R/I)` | 商环的谱，携带 nilpotent 信息 | ✅ |

### 2.2 S*L — 语义逻辑结构

- 概形视角下，几何对象不再是“点集”，而是 **局部环化空间** `(X, 𝒪_X)`。
- Nullstellensatz 的经典等式 `I(V(I)) = √I` 被重新解释为：**经典簇丢失了幂零信息，而概形保留了它**。
- ⚠️ 风险：学生容易把 `Spec(R)` 误当作 `MaxSpec(R)` 或 `k^n` 中的点集，忽略结构层与幂零方向。

### 2.3 M*D — 数学依存

```text
AffineSchemeNullstellensatz(R, I)
    │
    ├── Commutative ring R
    │
    ├── Prime spectrum Spec(R)
    │
    ├── Structure sheaf 𝒪_{Spec(R)}
    │
    ├── Closed subscheme Y = Spec(R/I)
    │
    ├── Ideal sheaf ℐ_Y ⊆ 𝒪_{Spec(R)}
    │
    └── Global sections ker(R → Γ(Y, 𝒪_Y)) = I
```

- 依赖关系闭合：核心依赖交换代数、层论、局部化。

### 2.4 M*L — 数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| 定义量词 | ✅ | `Spec(R)` 是环上所有素理想，非仅极大理想。 |
| 幂零信息保留 | ✅ | `R/I` 与 `R/√I` 可定义不同子概形但相同经典簇。 |
| 无需代数闭域 | ✅ | 概形理论对任意交换环有效。 |
| 退化情形 | ✅ | `I = R` 对应空概形；`I = (0)` 对应全空间。 |

### 2.5 P*D / P*L — 编程层

- Lean 4 / Mathlib：`AlgebraicGeometry.PrimeSpectrum` 与 `Scheme` 形式化正在推进。
- Coq：无主流概形形式化库。
- 风险：结构层与层上同调的形式化复杂度高，远难于经典簇计算。

---

## 3. 判定

| 维度 | 状态 |
|---|---|
| 自然语言声明真实性 | ⚪ 真 |
| 证明正确性 | ⚪ 正确（Grothendieck 标准理论） |
| 形式化验证 | 🟡 部分支持（Mathlib 发展中） |
| 与已知数学兼容性 | ✅ 与现代代数几何一致 |

**SMPDL 判定**：⚪ **低风险 / 已确认正确**（形式化实现难度高）。

---

## 4. 人类科学家可执行的验证动作

1. 对比 `Spec(ℂ[x]/(x²))` 与 `Spec(ℂ[x]/(x))`：前者是“双重点”，后者是单点；经典簇视角无法区分。
2. 验证 `Γ(Spec(R/I), 𝒪_{Spec(R/I)}) = R/I`，从而说明理想 `I` 与闭子概形一一对应。
3. 检查结构层在素理想 `p` 处的茎是否为局部环 `R_p`。

---

## 5. 署名与许可

**Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0**
