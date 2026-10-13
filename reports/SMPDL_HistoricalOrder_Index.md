# SMPDL 已生成案例：数学史顺序索引

**版本**：v1.0  
**日期**：2026-10-13  
**范围**：本索引按数学史发展脉络，排列当前已生成的 10 组（30 份）“同构证明、异基础” SMPDL 审计报告。每组给出历史定位、核心命题、基础差异、建议同构标签与对应文件名，便于教学、审校、历史研究与网页案例库导航。

---

## 一、时间轴总览

| 历史编号 | 时期 | 关键人物 | 年代 | 对比组 | 核心命题 | SMPDL 标签建议 |
|---|---|---|---|---|---|---|
| 1 | 古典几何 | Euclid, Gauss, Riemann, Lobachevsky | ~300 BCE – 1850s | 欧氏几何 ↔ 球面几何 | 三角形内角和 | `S-ISO / M-ISO / P-BISIM` |
| 2 | 古典分析 | Newton, Leibniz, Euler | 17–18 世纪 | 微分方程 ↔ 差分方程 | 指数增长模型 | `S-ISO / M-BISIM / P-BISIM` |
| 3 | 组合数学 | Euler, König, Erdős | 1736–20 世纪 | 有限图 ↔ 无限图 | 最小度 ≥ 2 是否保证有环 | `S-ISO / M-BISIM / P-BISIM` |
| 4 | 抽象代数 | Hamilton, Cayley, Noether | 19 世纪 | 交换环 ↔ 非交换环 | (ab)ⁿ 的展开 | `S-BISIM / M-BISIM / P-BISIM` |
| 5 | 域论与特征 | Galois, Dedekind, Steinitz | 19 世纪末–20 世纪初 | 特征 0 ↔ 特征 p | (a+b)ᵖ 的展开 | `S-ISO / M-ISO / P-BISIM` |
| 6 | 分析严格化 | Weierstrass, Robinson | 19 世纪–1961 | 标准分析 ↔ 非标准分析 | 导数定义 | `S-ISO / M-ISO / P-BISIM` |
| 7 | 数理逻辑 | Brouwer, Heyting | 1907 起 | 经典逻辑 ↔ 直觉主义逻辑 | 存在性证明 | `S-BISIM / M-ISO / P-ISO` |
| 8 | 公理化集合论 | Zermelo, Fraenkel, von Neumann | 1908–1920s | ZFC ↔ ZF | 任意向量空间有基 | `S-BISIM / M-BISIM / P-BISIM` |
| 9 | 基础多元竞争 | Russell, Church, Martin-Löf | 1908–1980s | 集合论 ↔ 类型论 | n + 0 = n | `S-ISO / M-BISIM / P-BISIM` |
| 10 | 可计算数学 | Turing, Weihrauch, Bishop | 1936–1980s | 经典分析 ↔ 可计算分析 | 中间值定理 | `S-ISO / M-BISIM / P-BISIM` |

---

## 二、详细条目

### H1. 古典几何：欧氏 ↔ 球面（~300 BCE – 1850s）

- **历史定位**：欧氏几何源于古希腊公理化传统；球面/非欧几何在 19 世纪因平行公设研究而成熟（Gauss、Riemann、Lobachevsky）。
- **核心命题**：三角形内角和。
- **基础差异**：欧氏假设平行公设（曲率 K=0）；球面几何无平行线、具有常正曲率。
- **结论变化**：欧氏 = 180°；球面 = π + Area/R²。
- **SMPDL 标签**：`S-ISO / M-ISO / P-BISIM`。
- **对应文件**：
  - `SMP_ProofAnalysis_Euclidean_TriangleAngleSum.md`
  - `SMP_ProofAnalysis_Spherical_TriangleAngleSum.md`
  - `SMPDL_Compare_EuclideanVsSpherical_TriangleAngleSum_PrePostFix.md`

---

### H2. 古典分析：微分方程 ↔ 差分方程（17–18 世纪）

- **历史定位**：Newton、Leibniz 建立微积分；Euler 将差分法与微分法并置研究，形成连续与离散两条路径。
- **核心命题**：指数增长/衰减模型。
- **基础差异**：连续流（导数）vs 离散迭代（递推）。
- **结论变化**：微分方程解为 `P(t)=P₀e^{kt}`；差分方程解为 `P_n=P₀(1+hk)^n`。
- **联系**：Euler 离散化 `(1+kt/n)^n → e^{kt}` 在 `h→0` 时收敛。
- **SMPDL 标签**：`S-ISO / M-BISIM / P-BISIM`。
- **对应文件**：
  - `SMP_ProofAnalysis_DifferentialEquation_ExponentialGrowth.md`
  - `SMP_ProofAnalysis_DifferenceEquation_ExponentialGrowth.md`
  - `SMPDL_Compare_DifferentialVsDifference_ExponentialGrowth_PrePostFix.md`

---

### H3. 组合数学：有限图 ↔ 无限图（1736–20 世纪）

- **历史定位**：Euler 1736 年解决柯尼斯堡七桥问题奠定图论基础；20 世纪图论形式化后，有限与无限情形的方法论分野逐渐清晰。
- **核心命题**：最小度 ≥ 2 是否保证存在环。
- **基础差异**：有限性保证“最长路径存在”；无限性不保证。
- **结论变化**：有限图 ⇒ 必有环；无限图 ⇏ 必有环（双向无限路径为反例）。
- **SMPDL 标签**：`S-ISO / M-BISIM / P-BISIM`。
- **对应文件**：
  - `SMP_ProofAnalysis_FiniteGraph_CycleByMinDegree.md`
  - `SMP_ProofAnalysis_InfiniteGraph_CycleByMinDegree.md`
  - `SMPDL_Compare_FiniteVsInfinite_GraphCycle_PrePostFix.md`

---

### H4. 抽象代数：交换环 ↔ 非交换环（19 世纪）

- **历史定位**：Hamilton 1843 年发现四元数，打破乘法交换律的默认假设，催生非交换代数。
- **核心命题**：二项式幂 `(ab)ⁿ` 的展开。
- **基础差异**：乘法交换律的有无。
- **结论变化**：交换环中 `(ab)ⁿ = aⁿbⁿ`；非交换环中 `(ab)ⁿ = a(ba)ⁿ⁻¹b`。
- **SMPDL 标签**：`S-BISIM / M-BISIM / P-BISIM`。
- **对应文件**：
  - `SMP_ProofAnalysis_CommutativeRing_BinomialPower.md`
  - `SMP_ProofAnalysis_NonCommutativeRing_BinomialPower.md`
  - `SMPDL_Compare_CommutativeVsNonCommutative_BinomialPower_PrePostFix.md`

---

### H5. 域论与特征：特征 0 ↔ 特征 p（19 世纪末–20 世纪初）

- **历史定位**：Galois 引入有限域思想；Dedekind、Steinitz（1910）系统建立域的抽象理论，特征成为区分域结构的关键不变量。
- **核心命题**：二项式展开 `(a+b)ᵖ`。
- **基础差异**：域的特征（char 0 vs char p）。
- **结论变化**：特征 0 下完整展开；特征 p 下出现 Freshman's Dream `(a+b)ᵖ = aᵖ + bᵖ`。
- **SMPDL 标签**：`S-ISO / M-ISO / P-BISIM`。
- **对应文件**：
  - `SMP_ProofAnalysis_Characteristic0_FreshmanDream.md`
  - `SMP_ProofAnalysis_CharacteristicP_FreshmanDream.md`
  - `SMPDL_Compare_Char0vsCharP_FreshmanDream_PrePostFix.md`

---

### H6. 分析严格化：标准分析 ↔ 非标准分析（19 世纪–1961）

- **历史定位**：Weierstrass 在 19 世纪用 ε-δ 极限严格化分析；Robinson 1961 年用模型论恢复 Leibniz 的无穷小方法，证明两者等价。
- **核心命题**：导数定义。
- **基础差异**：实数 ℝ 上的 ε-δ 极限 vs 超实数 *ℝ 上的无穷小量。
- **结论变化**：导数值一致，但表述与证明工具不同。
- **SMPDL 标签**：`S-ISO / M-ISO / P-BISIM`。
- **对应文件**：
  - `SMP_ProofAnalysis_StandardAnalysis_DerivativeLimit.md`
  - `SMP_ProofAnalysis_NonstandardAnalysis_DerivativeInfinitesimal.md`
  - `SMPDL_Compare_StandardVsNonstandard_Derivative_PrePostFix.md`

---

### H7. 数理逻辑：经典逻辑 ↔ 直觉主义逻辑（1907 起）

- **历史定位**：Brouwer 1907 年提出直觉主义，反对无限制使用排中律（LEM）；Heyting 建立形式化演算。
- **核心命题**：存在无理数 a, b 使 aᵇ 为有理数。
- **基础差异**：经典逻辑允许 LEM 与非构造性存在证明；直觉主义要求构造性见证。
- **结论变化**：经典版本不能提取 witness；直觉主义版本给出显式 `a=√2, b=log₂9`。
- **SMPDL 标签**：`S-BISIM / M-ISO / P-ISO`。
- **对应文件**：
  - `SMP_ProofAnalysis_ClassicalLogic_ExistenceWitness.md`
  - `SMP_ProofAnalysis_IntuitionisticLogic_ExistenceWitness.md`
  - `SMPDL_Compare_ClassicalVsIntuitionistic_ExistenceWitness_PrePostFix.md`

---

### H8. 公理化集合论：ZFC ↔ ZF（1908–1920s）

- **历史定位**：Zermelo 1908 年提出集合论公理；Fraenkel、von Neumann 在 1920 年代完善为 ZF/ZFC，选择公理（AC）成为独立且关键的公理。
- **核心命题**：任意向量空间都有基。
- **基础差异**：ZFC 包含选择公理；ZF 不包含。
- **结论变化**：ZFC 下可证（Zorn 引理）；ZF 下不可证（Cohen 独立性 + Blass 反向结果）。
- **SMPDL 标签**：`S-BISIM / M-BISIM / P-BISIM`。
- **对应文件**：
  - `SMP_ProofAnalysis_ZFC_VectorSpaceBasis.md`
  - `SMP_ProofAnalysis_ZF_VectorSpaceBasis.md`
  - `SMPDL_Compare_ZFCvsZF_VectorSpaceBasis_PrePostFix.md`

---

### H9. 基础多元竞争：集合论 ↔ 类型论（1908–1980s）

- **历史定位**：Russell 1908 年为解决悖论提出类型论；Church 1940 年建立简单类型论 λ 演算；Martin-Löf 在 1970–80 年代发展依赖类型论，成为现代证明助手（Lean/Coq/Agda）的基础。
- **核心命题**：n + 0 = n。
- **基础差异**：集合论外延基础（递归定义 + 外延相等）vs 类型论归纳基础（归纳类型 + identity type）。
- **结论变化**：等式符号相同，但证明结构与可提取信息不同。
- **SMPDL 标签**：`S-ISO / M-BISIM / P-BISIM`。
- **对应文件**：
  - `SMP_ProofAnalysis_SetTheory_NatPlusZero.md`
  - `SMP_ProofAnalysis_TypeTheory_NatPlusZero.md`
  - `SMPDL_Compare_SetTheoryVsTypeTheory_NatPlusZero_PrePostFix.md`

---

### H10. 可计算数学：经典分析 ↔ 可计算分析（1936–1980s）

- **历史定位**：Turing 1936 年建立可计算性理论；Bishop 1967 年发展构造性分析；Weihrauch 2000 年系统建立 Type-2 可计算分析，将“存在性”升级为“可计算存在性”。
- **核心命题**：中间值定理（IVT）。
- **基础差异**：经典分析依赖 ℝ 完备性与上确界公理；可计算分析要求函数可计算且有效一致连续，并给出求根算法。
- **结论变化**：经典版本只保证根存在；可计算版本保证根可计算并附带二分法近似算法。
- **SMPDL 标签**：`S-ISO / M-BISIM / P-BISIM`。
- **对应文件**：
  - `SMP_ProofAnalysis_ClassicalAnalysis_IntermediateValue.md`
  - `SMP_ProofAnalysis_ComputableAnalysis_IntermediateValue.md`
  - `SMPDL_Compare_ClassicalVsComputable_IntermediateValue_PrePostFix.md`

---

## 三、阅读与使用建议

### 3.1 教学顺序

建议按本索引的 H1→H10 顺序引导学生：

1. 从**几何直觉**（H1）入手，理解“基础假设改变结论”的最直观案例；
2. 进入**分析与离散**（H2、H3），体会连续/离散与有限/无限的差异；
3. 进入**代数**（H4、H5），理解单条公理或域特征如何改变恒等式；
4. 进入**分析基础**（H6、H10），比较 ε-δ、无穷小与可计算性三种严格化路径；
5. 最后进入**逻辑与基础**（H7–H9），讨论 20 世纪数学基础危机与多元基础。

### 3.2 审校顺序

对于 AI 生成证明审校，建议**反向**从 H10→H1 扫描：

- 先检查**可计算性需求**（H10）与**基础框架**（H9：集合论/类型论、H8：ZFC/ZF、H7：经典/直觉主义）是否声明；
- 再检查**分析/代数**基础是否匹配结论；
- 最后检查**几何**前提（H1：欧氏/球面/双曲）是否被默认。

### 3.3 历史研究用途

研究者可用本索引：

- 追踪“同一证明骨架”在不同历史时期的合法性变化；
- 比较 19 世纪代数革命、20 世纪逻辑革命与 17 世纪分析革命的异同；
- 为 `riemann-lecturer/index.html` 的动画时间线提供内容骨架。

---

## 四、同步位置

本索引应在以下位置同步：

- `Göttingen_SMPDL_README.md`：第七节新增“7.8 数学史顺序索引”；
- `SMPDL_Framework.md`：在“同构分析章节”增加“历史脉络”维度；
- `riemann-lecturer/index.html`：案例库按历史时间线排序，并增加“历史时期”筛选器；
- `SMPDL_Audit_SampleSuite.md`：将这 10 组 30 份报告按 H1–H10 编号入库。

---

## 五、署名与许可

本索引由 Göttingen SMPDL 项目维护，采用项目统一的署名与许可条款。新增索引版本号 `v1.0`，后续随样本库扩展升级。
