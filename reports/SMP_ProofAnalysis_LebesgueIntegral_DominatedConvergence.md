# SMPDL 单体审计：Lebesgue 积分视角下的控制收敛定理

> **审计对象**：Lebesgue 积分框架下的控制收敛定理（Dominated Convergence Theorem, DCT）  
> **审计日期**：2026-10-14  
> **审计框架**：Göttingen S/M/P × D/L v1.5  
> **历史编号**：H17-PostFix  
> **总体评价**：⚪ 定理成立——Lebesgue 框架恢复并强化了极限-积分交换。

---

## 1. 声明与版本

**主声明**（Lebesgue 控制收敛定理）：设 `{f_n}` 为测度空间 `(X, Σ, μ)` 上的可测函数列，`f_n → f` a.e.，且存在可积控制函数 `g`（`|f_n| ≤ g` a.e.，`∫g dμ < ∞`），则 `f` 可积且

```text
lim_{n→∞} ∫ |f_n - f| dμ = 0
⇒ lim ∫ f_n dμ = ∫ f dμ
```

**版本信息**：
- **形式化基础**：Lebesgue 积分理论（Lebesgue, 1902）
- **依赖前提**：σ-代数、可测函数、单调收敛定理、Fatou 引理
- **AxiomaticBase**：`LebesgueIntegration` + `MeasureTheory`
- **历史定位**：DCT 是现代分析的发动机——测度论把"按值域分划"替代"按定义域分划"，使积分算子对 a.e. 极限封闭

---

## 2. S/M/P × D/L 六格审计

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| σ-代数与测度 | 可测结构 | ✅ |
| 可测函数列 | a.e. 收敛 | ✅ |
| 控制函数 g | 可积上界 | ✅ |
| Fatou 引理 | DCT 证明核心 | ✅ |
| 单调收敛定理 | Fatou 的前提 | ✅ |

### 2.2 S*L — 语义逻辑结构

- Lebesgue 积分语义是"**按 y 轴（值域水平集）分划求和**"，可积性只依赖可测性，与连续性无关。
- Dirichlet 函数在 Lebesgue 框架下**可测且可积**（积分仍为 0），H17-PreFix 的断裂点被直接修复。
- ⚠️ S*L 风险："可积"一词在两个框架下同名异义（Riemann 可积 ⊂ Lebesgue 可积，反向不成立——如 `sin(x)/x` 条件收敛情形）。

### 2.3 M*D — 数学依存

```text
LebesgueDCT
    │
    ├── Monotone Convergence Theorem (MCT)
    │
    ├── Fatou's Lemma: ∫liminf ≤ liminf ∫
    │
    ├── |f_n| ≤ g, g integrable
    │
    ├── Apply Fatou to g + f_n and g - f_n
    │
    └── ∫f_n → ∫f
```

### 2.4 M*L — 数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| MCT 成立 | ✅ | 非负可测递增列可交换。 |
| Fatou 引理 | ✅ | MCT 的推论。 |
| DCT 结论 | ✅ | Fatou 双向夹逼。 |
| 反例修复 | ✅ | Dirichlet 型列在 Lebesgue 下 `∫f_n = 0 = ∫f`，交换恢复。 |

### 2.5 P*D / P*L — 编程层

- Mathlib：`MeasureTheory.Integral` 层级完整（`lintegral` → `Integral` → DCT 全链形式化）。
- 这也是 H17 中 P 层差异最大的点：Riemann 层形式化薄，Lebesgue 层极厚。

---

## 3. 判定

| 维度 | 状态 |
|---|---|
| 自然语言声明真实性 | ⚪ 真 |
| 证明正确性 | ⚪ 正确 |
| 形式化验证 | 🟢 Mathlib 完整支持 |
| 与已知数学兼容性 | ✅ 现代实分析标准 |

**SMPDL 判定**：⚪ **低风险 / 已确认正确**。

---

## 4. 人类科学家可执行的验证动作

1. 用 Fatou 引理写出 DCT 的完整双向夹逼证明。
2. 验证 Dirichlet 型 `f_n` 列在 Lebesgue 下满足 DCT 全部条件且交换成立。
3. 对比 `∫ sin(x)/x`（条件收敛）：Riemann 瑕积分存在，但非 Lebesgue 可积——语义非对称的反向例子。

---

## 5. 署名与许可

**Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0**
