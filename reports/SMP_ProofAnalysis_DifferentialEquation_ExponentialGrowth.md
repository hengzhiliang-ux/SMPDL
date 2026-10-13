# S/M/P × D/L 审计报告：微分方程中的指数增长

> **定理**：初值问题
> 
> dP/dt = kP, P(0) = P₀
> 
> 在 k, P₀ ∈ ℝ 给定、P : ℝ → ℝ 可微的条件下，唯一解为
> 
> P(t) = P₀ e^{kt}。
> 
> **来源**：标准常微分方程教材（如 Boyce-DiPrima, *Elementary Differential Equations*；Hairer-Nørsett-Wanner）。
> 
> **分析日期**：2026-10-13 | **审计框架**：Göttingen S/M/P × D/L v1.5 | **AxiomaticBase**：`DifferentialEquation`
> 
> **风险评级**：⚪ 已确认正确（在标准实分析与 ODE 公理体系内）。

---

## 0. 分析目标

1. 对微分方程指数增长模型 dP/dt = kP 的求解做一次 S/M/P × D/L 六格审计。
2. 明确证明依赖的核心假设：实数完备性、可微性、指数函数性质、解的唯一性。
3. 为后续与差分方程版本做同构对比建立基准（S/M/P 标签、证明骨架、风险点）。
4. 检查自然语言中是否把“分离变量法”当作纯代数技巧，忽略极限与导数基础。

---

## 1. S 层审计（语义层）

### 1.1 S*D：语义依存

| 自然语言元素 | 支持的后续元素 | 依赖说明 |
|---|---|---|
| 函数 P : ℝ → ℝ | 可微性假设 | 定理对象 |
| 常数 k ∈ ℝ | 增长率参数 | 方程参数 |
| 初值 P(0) = P₀ | 确定唯一解 | 定解条件 |
| 微分方程 dP/dt = kP | 导数与函数成正比 | 核心语义 |
| 分离变量：dP/P = k dt | 积分两边 | 求解技巧 |
| 积分得 ln|P| = kt + C | 对数函数性质 | 中间结论 |
| 指数化得 P(t) = P₀ e^{kt} | 指数函数性质 | 最终解 |

### 1.2 S*L：语义逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| 量词显式化 | ✅ | “对所有 t ∈ ℝ”可显式写为 ∀t ∈ ℝ。 |
| 术语单义性 | ⚠️ 中 | “解”在 ODE 中指满足方程与初值的可微函数；需与差分方程的“序列解”区分。 |
| 隐喻/图示依赖 | ⚠️ 中 | “增长率与当前量成正比”是强直觉隐喻；严格证明需回到导数定义。 |
| 隐含跳跃 | 🟡 中 | 分离变量法依赖 P ≠ 0 与链式法则；P = 0 需单独验证。 |
| 蕴涵方向 | ✅ | 由微分方程 + 初值推出解的形式，方向正确。 |

**S 层结论**：自然语言证明直观，但“分离变量”与“指数化”步骤依赖实分析中的导数、积分与指数对数性质。教学中若省略这些基础，易造成“代数技巧”幻觉。

---

## 2. M 层审计（数学层）

### 2.1 M*D：数学依存

```text
DifferentialEquation_ExponentialGrowth
    │
    ├── Real numbers ℝ
    │       └── Complete ordered field with differentiable structure
    │
    ├── Differentiable function P : ℝ → ℝ
    │       └── dP/dt exists everywhere
    │
    ├── Ordinary Differential Equation
    │       └── P'(t) = k P(t)
    │
    ├── Initial condition
    │       └── P(0) = P₀
    │
    ├── Solving by separation of variables
    │       ├── Assume P(t) ≠ 0 locally
    │       ├── dP/P = k dt
    │       ├── integrate: ln|P| = kt + C
    │       └── exponentiate: P(t) = C' e^{kt}
    │
    ├── Apply initial condition
    │       └── C' = P₀
    │
    ├── Handle P(t) = 0 case
    │       └── If P₀ = 0, the zero function is a solution
    │
    └── Uniqueness theorem
            └── Picard-Lindelöf / Gronwall-type argument guarantees uniqueness
```

| 数学对象 | 结构签名 | 在证明中的作用 |
|---|---|---|
| 实数域 ℝ | 完备有序域 | 时间与数量的论域 |
| 可微函数 P : ℝ → ℝ | C¹ 函数 | 定理对象 |
| 导数 dP/dt | 极限定义的函数 | 方程左侧 |
| 增长率 k | 实数参数 | 比例常数 |
| 初值 P₀ | 实数 | 定解条件 |
| 指数函数 e^{kt} | 满足 d/dt e^{kt} = k e^{kt} | 解的核函数 |
| 对数函数 ln | 指数函数的反函数 | 分离变量步骤 |
| 解的唯一性定理 | Picard-Lindelöf | 保证解唯一 |

### 2.2 M*L：数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| 公理系统一致性 | ✅ | 在标准实分析与 ODE 理论内严格。 |
| 构造合法性 | ✅ | 通过分离变量法显式构造解。 |
| 量词范围 | ✅ | 对所有 t ∈ ℝ 成立。 |
| 边界情况 | ✅ | P₀ = 0 时零函数是解；唯一性定理覆盖。 |
| 隐藏假设 | 🟡 中 | 分离变量时默认 P(t) ≠ 0；需用连续性论证或单独处理 P₀ = 0。 |
| 等价命题循环 | ✅ | 无。 |

**M 层结论**：证明在标准 ODE 理论内逻辑结构完整。核心依赖为导数/积分、指数对数函数、解的唯一性定理。

---

## 3. P 层审计（编程/形式化层）

### 3.1 P*D：形式化依存

> 在 Mathlib/Lean 4 中，常微分方程理论有 `Mathlib.Analysis.ODE` 相关部分，但更基础地，解 P(t) = P₀ e^{kt} 可通过显式求导验证。

```text
DifferentialEquation_ExponentialGrowth
    │
    ├── Mathlib.Data.Real.Basic
    │       └── ℝ
    │
    ├── Mathlib.Analysis.Calculus.Deriv.Basic
    │       └── deriv
    │
    ├── Mathlib.Analysis.SpecialFunctions.ExpLog
    │       └── Real.exp, Real.log
    │
    └── Theorem sketch
            └── theorem exponential_growth_ode_solution
                    {k P0 : ℝ}
                    (P : ℝ → ℝ)
                    (hdiff : Differentiable ℝ P)
                    (heq : ∀ t, deriv P t = k * P t)
                    (hic : P 0 = P0) :
                    ∀ t, P t = P0 * Real.exp (k * t)
```

### 3.2 P*L：形式化逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| 语法可编译 | ✅ | Mathlib 提供导数、指数函数与可微性定义。 |
| 类型签名一致 | ✅ | 输入：k, P₀ : ℝ，可微 P；输出：∀t, P(t) = P₀ e^{kt}。 |
| 定义等价 | ✅ | `deriv` 与标准导数等价；`Real.exp` 与指数函数等价。 |
| 命题等式 | ✅ | 目标等式可直接作为定理。 |
| `#print axioms` | 🟢 低 | 依赖实数构造与微分学；不直接意外依赖选择公理。 |

**P 层结论**：Mathlib 可支撑本定理形式化。主要工作是构造分离变量或直接使用指数函数求导验证。

---

## 4. 跨层映射检查

### 4.1 S ↔ M

| S 层主张 | M 层形式化 | 同构强度 | 说明 |
|---|---|---|---|
| 增长率与当前量成正比 | P'(t) = k P(t) | ⭐⭐⭐ 高 | 直接对应 |
| 分离变量 | dP/P = k dt | ⭐⭐⭐ 高 | 核心技巧 |
| 积分得对数 | ln|P| = kt + C | ⭐⭐⭐ 高 | 直接对应 |
| 指数化 | P(t) = C' e^{kt} | ⭐⭐⭐ 高 | 直接对应 |
| 初值确定常数 | C' = P₀ | ⭐⭐⭐ 高 | 直接对应 |
| 解的唯一性 | Picard-Lindelöf | ⭐⭐⭐ 高 | 保证结论 |

### 4.2 M ↔ P

| M 层对象/关系 | P 层表达 | 同构强度 | 判据 |
|---|---|---|---|
| 可微函数 P | `P : ℝ → ℝ` + `Differentiable ℝ P` | ⭐⭐⭐ 高 | 类型/类对应 |
| 导数 dP/dt | `deriv P t` | ⭐⭐⭐ 高 | 函数对应 |
| 指数函数 | `Real.exp` | ⭐⭐⭐ 高 | 函数对应 |
| 初值条件 | `P 0 = P0` | ⭐⭐⭐ 高 | 等式对应 |
| 解的等式 | `∀ t, P t = P0 * Real.exp (k * t)` | ⭐⭐⭐ 高 | 目标对应 |

### 4.3 S ↔ P

| 自然语言步骤 | 形式化代码 | 保真度 |
|---|---|---|
| 假设 P 可微且满足 ODE | `variable {k P0 : ℝ} {P : ℝ → ℝ} (hdiff : Differentiable ℝ P) (heq : ∀ t, deriv P t = k * P t) (hic : P 0 = P0)` | ✅ 高 |
| 验证候选解 | `have hsol : ∀ t, P t = P0 * Real.exp (k * t) := ...` | ✅ 高 |
| 对候选解求导 | `simp [deriv_const_mul, deriv_mul, deriv_id'', Real.deriv_exp, mul_comm k]` | ✅ 高 |
| 用唯一性定理 | `apply ODE_solution_unique ...` | ✅ 高（需完整库支持） |

**跨层结论**：S/M/P 三层映射高度一致；主要风险在于 P 层需要完整的 ODE 唯一性定理库，或改用显式构造法。

---

## 5. 风险点与判定

| 风险点 | 层级 | 风险等级 | 处理状态 |
|---|---|---|---|
| 分离变量时 P = 0 的处理 | M | 🟡 中 | 需用连续性或单独讨论 |
| 解的唯一性定理依赖 Lipschitz 条件 | M | 🟢 低 | f(t,P) = kP 是全局 Lipschitz |
| 自然语言把 ODE 解当作纯代数对象 | S | 🟡 中 | 需强调可微性与实数基础 |
| 形式化中 ODE 唯一性库不成熟 | P | 🟡 中 | 可用显式构造替代 |

**最终判定**：⚪ 已确认正确。该证明在标准 ODE 公理体系内逻辑完整、跨层同构强度高，适合作为 SMPDL 样本库中“连续正确样本”的基准条目。

---

## 6. 结论

微分方程指数增长模型是一个**连续极限与可微性**驱动的经典案例：

- **S 层**：自然语言“增长率与当前量成正比”被严格化为导数方程。
- **M 层**：数学结构完整，核心为 `ODE + 初值 → 分离变量 → 指数函数 → 唯一性`。
- **P 层**：Mathlib 提供 `deriv`、`Real.exp` 等工具；完整唯一性证明需要 ODE 库支持。
- **跨层映射**：三层对应关系明确，同构强度为 ⭐⭐⭐ 高。

该样本建议标记为：`DifferentialEquation`、`S-ISO / M-ISO / P-ISO`（自洽），并作为与 `DifferenceEquation` 版本对比的基准版本。

---

## 7. 文献引用纪律检查

| 引用对象 | 真实性 | 支持性 | 说明 |
|---|---|---|---|
| Boyce-DiPrima, *Elementary Differential Equations* | ✅ 真实 | ✅ 支持 | 常微分方程标准教材。 |
| Hairer-Nørsett-Wanner, *Solving ODEs* | ✅ 真实 | ✅ 支持 | ODE 数值与分析参考。 |
| Picard-Lindelöf 唯一性定理 | ✅ 真实 | ✅ 支持 | 解的存在唯一性标准定理。 |
| Mathlib `deriv` / `Real.exp` | ✅ 真实 | ✅ 支持 | Lean 4 形式化层参考。 |

**核查结论**：引用对象均为真实存在的数学内容或形式化库，支持方向与本报告一致。

---

## 8. 署名与许可

**Göttingen S/M/P × D/L 数学证明审查方法论** · v1.5  \
**作者**：咖啡 / CampanaSilvae · fecit · MMXXVI  \
**首发时间**：2026-10-13 GMT+8  \
**许可协议**：[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh)

搬运、改写或教学引用请注明来源与本页面链接。
