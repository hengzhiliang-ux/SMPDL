# SMPDL 单体审计：Riemann 积分视角下的极限与积分交换

> **审计对象**：Riemann 积分框架下"逐点收敛 + 一致有界"能否交换极限与积分  
> **审计日期**：2026-10-14  
> **审计框架**：Göttingen S/M/P × D/L v1.5  
> **历史编号**：H17-PreFix  
> **总体评价**：🔴 反例成立——Riemann 框架下控制收敛定理不成立（结论反转）。

---

## 1. 声明与版本

**主声明**（Riemann 框架的反例）：存在函数列 `{f_n}` 满足：每项 Riemann 可积、逐点收敛于 `f`、且被可积函数 `g` 一致控制（`|f_n| ≤ g`），但

```text
lim ∫ f_n dx  ≠  ∫ lim f_n dx
```

**标准反例（Dirichlet 型函数列）**：在 `[0,1]` 上，令 `{q_k}` 为有理数枚举，定义

```text
f_n(x) = 1 若 x ∈ {q_1,...,q_n}；否则 0
```

每个 `f_n` 有限点不连续、Riemann 可积且积分为 0；逐点极限是 Dirichlet 函数（有理处 1、无理处 0），**处处不连续、Riemann 不可积**。

**版本信息**：
- **形式化基础**：古典分析（Riemann, 1854）
- **依赖前提**：分划-达布和定义、有界性、不连续点集勒贝格测度零准则
- **AxiomaticBase**：`RiemannIntegration` + `BoundedConvergence`
- **历史定位**：Riemann 积分对"极限运算"封闭性差，是 19 世纪分析的主要痛点，直接催生 Lebesgue 理论

---

## 2. S/M/P × D/L 六格审计

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| 分划 + 达布上/下和 | Riemann 可积性定义 | ✅ |
| 不连续点集测度零 | Riemann 可积判据（Lebesgue 准则） | ✅ |
| 极限函数处处不连续 | Dirichlet 函数 | ✅ |
| 反例结论 | 积分算子在逐点极限下不封闭 | ✅ |

### 2.2 S*L — 语义逻辑结构

- Riemann 积分的语义是"**按 x 轴分划求和**"，可积性依赖函数的逐点连续性，而逐点极限会灾难性地破坏连续性。
- ⚠️ 主要 S*L 风险：把"每个 f_n 可积"误推"极限必可积"——这正是 Riemann 框架的语义陷阱。

### 2.3 M*D — 数学依存

```text
RiemannCounterexample
    │
    ├── f_n = 1 on {q_1..q_n}, 0 elsewhere
    │
    ├── Each f_n: Riemann integrable, ∫f_n = 0
    │
    ├── f_n → 1_ℚ pointwise (Dirichlet function)
    │
    └── 1_ℚ not Riemann integrable (discontinuous everywhere)
```

### 2.4 M*L — 数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| 每项可积 | ✅ | 有限不连续点 ⇒ 测度零 ⇒ Riemann 可积。 |
| 一致控制 | ✅ | `|f_n| ≤ 1 = g`，`g` 可积。 |
| 极限可积性 | ❌ | 极限处处不连续，不可积。 |
| 结论 | 🔴 | 交换失败：`∫ lim f_n` 无意义。 |

### 2.5 P*D / P*L — 编程层

- Lean/Mathlib：`RiemannIntegrable` 有形式化；反例可构造。
- 数值陷阱：任何离散采样都会把 `1_ℚ` 积成 0，掩盖断裂——**数值验证在此失效**，必须符号推理。

---

## 3. 判定

| 维度 | 状态 |
|---|---|
| 自然语言声明真实性 | ⚪ 真（反例成立） |
| 证明正确性 | ⚪ 正确 |
| 形式化验证 | 🟢 Mathlib 支持 |
| 与已知数学兼容性 | ✅ 古典分析标准结论 |

**SMPDL 判定**：⚪ **反例正确**——但这本身标记了 Riemann 框架的🔴级缺陷。

---

## 4. 人类科学家可执行的验证动作

1. 验证每个 `f_n` 的不连续点集为 `n` 个点（测度零）。
2. 验证 Dirichlet 函数达布上和恒 1、下和恒 0，不可积。
3. 反思：为何数值积分实验无法发现此断裂。

---

## 5. 署名与许可

**Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0**
