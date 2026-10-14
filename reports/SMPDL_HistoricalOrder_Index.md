# SMPDL 已生成案例：数学史顺序索引

**版本**：v2.5  
**日期**：2026-10-14  
**范围**：本索引按数学史发展脉络，排列当前已生成的 43 组（126 份）"同构证明、异基础" SMPDL 审计报告（H1–H43，候选池清零收官）。每组给出历史定位、核心命题、基础差异、建议同构标签与对应文件名，便于教学、审校、历史研究与网页案例库导航。

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
| 11 | 拓扑学 | Weierstrass, Heine, Borel | 19 世纪–20 世纪初 | 紧致空间 ↔ 非紧致空间 | 连续函数的最值定理 | `S-ISO / M-BISIM / P-BISIM` |
| 12 | 范畴论与代数拓扑 | Eilenberg, Mac Lane, Grothendieck, Hurewicz, Whitehead | 1945–1960s | 同构 ↔ 范畴等价 ↔ 同伦等价 | “相同”概念的三种强度 | `S-BISIM / M-BISIM / P-BISIM` |
| 13 | 概率论 | Bayes, Laplace, Fisher, Neyman-Pearson, Jeffreys | 1763–20 世纪 | 频率主义 ↔ 贝叶斯 | 二项比例估计与区间解释 | `S-BISIM / M-ISO / P-BISIM` |
| 14 | 代数几何 | Hilbert, Grothendieck | 1890s–1960s | 经典代数簇 ↔ 概形 | 仿射 Nullstellensatz | `S-BISIM / M-BISIM / P-BISIM` |
| 15 | 数论 | Dirichlet, Dedekind, Artin, Chebotarev | 1837–20 世纪 | 解析数论 ↔ 代数数论 | 算术级数中的素数 | `S-ISO / M-BISIM / P-BISIM` |
| 16 | 古典几何/非欧几何 | Euclid, Gauss, Lobachevsky, Bolyai, Riemann | ~300 BCE – 1850s | 欧氏 ↔ 球面 ↔ 双曲 | 三角形内角和与曲率 | `S-ISO / M-ISO / P-BISIM` |
| 17 | 实分析/测度论 | Riemann, Lebesgue | 1854–1902 | Riemann ↔ Lebesgue 积分 | 极限-积分交换（DCT） | `S-BISIM / M-BISIM / P-BISIM` |
| 18 | 偏微分方程 | Green, Sobolev, Lax–Milgram | 19 世纪–1954 | 经典解 ↔ 弱解 | Laplace 方程存在性与正则性 | `S-BISIM / M-BISIM / P-BISIM` |
| 19 | 复分析 | Cauchy, Hartogs | 19 世纪–1906 | 单复变 ↔ 多复变 | Hartogs 现象与全纯域 | `S-ISO / M-BISIM / P-BISIM` |
| 20 | 组合/Ramsey 理论 | Ramsey, Erdős–Szekeres | 1930–1935 | 有限 ↔ 无限 Ramsey | 单色集存在性 | `S-ISO / M-BISIM / P-BISIM` |
| 21 | 模型论 | Löwenheim, Skolem, Gödel, Henkin | 1915–1950 | 一阶 ↔ 二阶逻辑 | 紧致性与 LS 定理 | `S-BISIM / M-BISIM / P-BISIM` |
| 22 | 证明论 | Hilbert, Gentzen, Prawitz | 1917–1965 | Hilbert ↔ 自然演绎 | 切消去与规范化 | `S-BISIM / M-BISIM / P-BISIM` |
| 23 | 泛函分析 | Hilbert, Riesz, Banach | 1900s–1932 | Hilbert ↔ Banach 空间 | 投影与对偶 | `S-BISIM / M-BISIM / P-BISIM` |
| 24 | 表示论 | Frobenius, Burnside, Pólya | 1896–1937 | 线性 ↔ 置换表示 | 特征标与不变量 | `S-BISIM / M-BISIM / P-BISIM` |
| 25 | 动力系统 | Poincaré, Sharkovsky, Li–Yorke | 1880s–1975 | 连续流 ↔ 离散映射 | P–B 定理与混沌 | `S-BISIM / M-BISIM / P-BISIM` |
| 26 | 自动机理论 | Kleene, Chomsky | 1956 | 正则 ↔ 上下文无关 | 封闭性与判定性 | `S-BISIM / M-BISIM / P-BISIM` |
| 27 | 逻辑/量子基础 | Boole, Stone, Birkhoff–von Neumann, Gleason, Kochen–Specker | 1847–1967 | 布尔逻辑 ↔ 量子逻辑 | 分配律与真值语义 | `S-BISIM / M-BISIM / P-BISIM` |
| 28 | 代数（律减法第二辑） | Graves, Cayley, Frobenius, Hurwitz, Lie, Artin | 1843–1950s | 结合代数 ↔ 非结合代数 | 结合律与括号语义 | `S-BISIM / M-BISIM / P-BISIM` |
| 29 | 分析基础（上游律） | 毕达哥拉斯, Dedekind, Cantor, Hilbert | ~500 BCE–1872 | ℚ ↔ ℝ | Dedekind 完备律与定理群生根 | `S-BISIM / M-BISIM / P-BISIM` |
| 30 | 测度论（交换律定价） | Cauchi, Riemann, Fubini, Tonelli | 1821–1909 | 条件收敛 ↔ 绝对可积 | 积分次序交换律 | `S-BISIM / M-BISIM / P-BISIM` |
| 31 | 重写理论/λ 演算 | Church, Rosser, Tait, Knuth–Bendix | 1936–1970 | 非汇合重写 ↔ λ 演算 | Church–Rosser 汇合律 | `S-BISIM / M-BISIM / P-BISIM` |
| 32 | 序理论/非线性分析（均衡） | Knaster, Tarski, Kakutani, Nash, Minty | 1928–1964 | 单调 ↔ 非单调集值 | 单调律与均衡理论 | `S-BISIM / M-BISIM / P-BISIM` |
| 33 | 数学物理（守恒） | Noether, Lorenz, Ward | 1918–1963 | 耗散系统 ↔ 变分对称系统 | 守恒律与对称对偶 | `S-BISIM / M-BISIM / P-BISIM` |
| 34 | 代数/非阿分析 | Eudoxus, Stolz, Levi-Civita, Ostrowski, Robinson | 前4世纪–1960s | 阿氏域 ↔ 非阿域 | Archimedes 律与无穷小 | `S-BISIM / M-BISIM / P-BISIM` |
| 35 | 动力系统（几何力学） | Liouville, Poincaré, Lorenz, Smale, Ruelle | 1838–1976 | 保守流 ↔ 耗散流 | Liouville 禁闭与吸引子 | `S-BISIM / M-BISIM / P-BISIM` |
| 36 | 证明论（资源敏感） | Gentzen, Girard, Wadler | 1935–1990 | 经典结构 ↔ 线性逻辑 | 收缩/弱化律与 bang | `S-BISIM / M-BISIM / P-BISIM` |
| 37 | 射影几何 | Desargues, Hilbert, Hall, Moufang | 1648–1951 | Desarguesian ↔ 非 Desargues | Desargues 律与三元环 | `S-BISIM / M-BISIM / P-BISIM` |
| 38 | 交换代数 | Gauss, Kummer, Dedekind | 1801–1871 | 整环 ↔ 含零因子环 | 零因子律与理想论 | `S-BISIM / M-BISIM / P-BISIM` |
| 39 | tropical 代数 | Cuninghame-Green, Maslov, Viro | 1960s–2000s | 经典半环 ↔ tropical 半环 | 幂等律与优化代数化 | `S-BISIM / M-BISIM / P-BISIM` |
| 40 | 半群理论 | Burnside, Wagner, Novikov–Adian | 1902–1968 | 可消 ↔ 非可消半群 | 消去律与逆半群 | `S-BISIM / M-BISIM / P-BISIM` |
| 41 | 点集拓扑/谱理论 | Hausdorff, Zariski, Stone, Hochster, Scott | 1914–1970s | Hausdorff ↔ 非 Hausdorff | T2 分离律与谱拓扑 | `S-BISIM / M-BISIM / P-BISIM` |
| 42 | 拓扑相变/数学物理 | Brouwer, Hopf, BKT, Atiyah–Singer | 1911–1973 | 拓扑荷禁闭 ↔ 解绑相变 | 同伦不变律与指标定理 | `S-BISIM / M-BISIM / P-BISIM` |
| 43 | 拟度量几何 | Fréchet, Wilson, Lawvere, Künzi | 1906–1990s | 对称度量 ↔ 拟度量 | 距离对称律与富集范畴 | `S-BISIM / M-BISIM / P-BISIM` |

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

### H11. 拓扑学：紧致 ↔ 非紧致（19 世纪–20 世纪初）

- **历史定位**：Weierstrass 在 19 世纪证明闭区间上连续函数的有界性与最值定理；20 世纪拓扑学将关键前提抽象为“紧致性”，Heine-Borel 定理在 `ℝ^n` 中建立紧致与“闭且界”的等价。
- **核心命题**：连续函数是否一定有界、是否能取到最大/最小值。
- **基础差异**：定义域是否具有紧致性；紧致空间任意开覆盖有有限子覆盖，非紧致空间则否。
- **结论变化**：紧致 + 连续 ⇒ 有界且取最值；非紧致 + 连续 ⇏ 有界或取最值。
- **SMPDL 标签**：`S-ISO / M-BISIM / P-BISIM`。
- **对应文件**：
  - `SMPDL_Compare_CompactVsNoncompact_ExtremeValue_PrePostFix.md`

---

### H12. 范畴论与代数拓扑：同构 ↔ 范畴等价 ↔ 同伦等价（1945–1960s）

- **历史定位**：Eilenberg 与 Mac Lane 1945 年创立范畴论，将“同构”形式化为对象间的可逆态射；随后发现许多数学场景只需“范畴等价”或“同伦等价”即可保留关键不变量。Grothendieck 在代数几何中广泛使用范畴等价；Hurewicz 与 Whitehead 在代数拓扑中建立同伦等价。
- **核心命题**：“两个对象/范畴/空间相同”的三种强度。
- **基础差异**：逆映射的严格性——严格相等（同构）vs 自然同构（范畴等价）vs 同伦（同伦等价）。
- **结论变化**：同构最强；范畴等价保留全部范畴性质 up to isomorphism；同伦等价保留代数拓扑不变量但允许点集不同。
- **SMPDL 标签**：`S-BISIM / M-BISIM / P-BISIM`（同构↔范畴等价）；`S-BISIM / M-BISIM / P-BISIM`（同胚↔同伦等价）。
- **对应文件**：
  - `SMP_ProofAnalysis_Category_Isomorphism.md`
  - `SMP_ProofAnalysis_Category_Equivalence.md`
  - `SMP_ProofAnalysis_Category_HomotopyEquivalence.md`
  - `SMPDL_Compare_IsomorphismVsEquivalenceVsHomotopy_PrePostFix.md`

---

### H13. 概率论：频率主义 ↔ 贝叶斯（预留）

- **状态**：预留待补。
- **预期核心命题**：大数定律 / 条件概率解释 / 参数估计的哲学差异。
- **预期 SMPDL 标签**：`S-BISIM / M-BISIM / P-BISIM`。

---

### H14. 代数几何：经典代数簇 ↔ 概形（1890s–1960s）

- **历史定位**：Hilbert 在 1890s 建立经典 Nullstellensatz，将代数理想与几何点集对应起来；Grothendieck 在 1960s 用概形理论将几何对象从“点集”升级为“局部环化空间”，保留幂零信息并推广到任意交换环。
- **核心命题**：仿射 Nullstellensatz 在经典簇与概形框架下的表述差异。
- **基础差异**：经典框架使用代数闭域上的点集 + 根理想；概形框架使用任意交换环的素谱 + 结构层 + 任意理想。
- **结论变化**：经典框架下 `I(V(I)) = √I`（信息丢失幂零）；概形框架下理想 `I` 与闭子概形 `Spec(R/I)` 一一对应（保留幂零）。
- **SMPDL 标签**：`S-BISIM / M-BISIM / P-BISIM`。
- **对应文件**：
  - `SMP_ProofAnalysis_AlgebraicGeometry_ClassicalVariety.md`
  - `SMP_ProofAnalysis_AlgebraicGeometry_Scheme.md`
  - `SMPDL_Compare_VarietyVsScheme_AffineNullstellensatz_PrePostFix.md`

---

### H13. 概率论：频率主义 ↔ 贝叶斯（1763–20 世纪）

- **历史定位**：Bayes 1763 年提出逆概率问题，将概率解释为主观信念度；Fisher 与 Neyman-Pearson 在 20 世纪建立频率主义框架，将概率定义为长期相对频率。两种解释长期竞争，至今仍是统计学哲学的核心张力。
- **核心命题**：二项比例 `p` 的估计与区间解释。
- **基础差异**：频率主义把 `p` 视为固定未知常数，区间是抽样覆盖频率；贝叶斯把 `p` 视为随机变量，区间是后验概率。
- **结论变化**：同一数据下，MLE `p̂ = k/n` 与后验均值可能数值相近，但置信区间与可信区间的语义截然不同。
- **SMPDL 标签**：`S-BISIM / M-ISO / P-BISIM`。
- **对应文件**：
  - `SMP_ProofAnalysis_Frequentist_BinomialProportion.md`
  - `SMP_ProofAnalysis_Bayesian_BinomialProportion.md`
  - `SMPDL_Compare_FrequentistVsBayesian_BinomialProportion_PrePostFix.md`

---

### H15. 数论：解析数论 ↔ 代数数论（1837–20 世纪）

- **历史定位**：Dirichlet 1837 年用 L-函数证明算术级数中有无穷多素数，开创解析数论；Dedekind、Weber、Hilbert、Artin、Chebotarev 在 19–20 世纪建立代数数论与类域论，发现分圆域的 Galois 结构可直接编码素数在算术级数中的分布。
- **核心命题**：Dirichlet 算术级数素数定理。
- **基础差异**：解析方法用复分析 L-函数与特征标正交关系；代数方法用分圆域、Frobenius 元素与 Chebotarev 密度定理。
- **结论变化**：结论相同，但代数方法同时给出密度 `1/φ(q)`，并适用于更一般的 Galois 扩张。
- **SMPDL 标签**：`S-ISO / M-BISIM / P-BISIM`。
- **对应文件**：
  - `SMP_ProofAnalysis_NumberTheory_Analytic_DirichletAP.md`
  - `SMP_ProofAnalysis_NumberTheory_Algebraic_DirichletAP.md`
  - `SMPDL_Compare_AnalyticVsAlgebraic_DirichletAP_PrePostFix.md`

---

### H16. 古典几何/非欧几何：欧氏 ↔ 球面 ↔ 双曲（~300 BCE – 1850s）

- **历史定位**：Euclid ~300 BCE 建立欧氏几何；19 世纪 Gauss、Lobachevsky、Bolyai、Riemann 发现平行公设可被替换，从而发展出球面与双曲几何；Gauss-Bonnet 定理最终把三种几何统一为常曲率 `K` 取不同值。
- **核心命题**：三角形内角和与面积的关系。
- **基础差异**：欧氏 `K=0`、球面 `K>0`、双曲 `K<0`；平行公设分别为"唯一平行线""无平行线""无穷多平行线"。
- **结论变化**：统一公式 `α+β+γ = π + K·Area`，分别退化为 `= π`、`= π + Area/R²`、`= π - Area`。
- **SMPDL 标签**：`S-ISO / M-ISO / P-BISIM`。
- **对应文件**：
  - `SMP_ProofAnalysis_Euclidean_TriangleAngleSum.md`
  - `SMP_ProofAnalysis_Spherical_TriangleAngleSum.md`
  - `SMP_ProofAnalysis_Hyperbolic_TriangleAngleSum.md`
  - `SMPDL_Compare_EuclideanVsSphericalVsHyperbolic_TriangleAngleSum_PrePostFix.md`

---

### H17. 实分析/测度论：Riemann ↔ Lebesgue 积分（1854–1902）

- **历史定位**：Riemann 1854 年定义按定义域分划的积分；Lebesgue 1902 年翻转分划方向（按值域水平集），使积分算子对 a.e. 极限封闭——控制收敛定理（DCT）成为现代分析发动机。
- **核心命题**：极限与积分的交换（DCT）。
- **基础差异**：分划方向（x 轴 vs y 轴）；可积判据（不连续点测度零 vs 可测 + 绝对积分有限）。
- **结论变化**：Riemann 下 DCT 反例成立（Dirichlet 型列极限不可积，🔴）；Lebesgue 下 DCT 定理成立（⚪）——两侧结论方向相反。
- **SMPDL 标签**：`S-BISIM / M-BISIM / P-BISIM`。
- **对应文件**：
  - `SMP_ProofAnalysis_RiemannIntegral_LimitInterchange.md`
  - `SMP_ProofAnalysis_LebesgueIntegral_DominatedConvergence.md`
  - `SMPDL_Compare_RiemannVsLebesgue_DominatedConvergence_PrePostFix.md`

---

### H18. 偏微分方程：经典解 ↔ 弱解（19 世纪–1954）

- **历史定位**：Green/Gauss 19 世纪建立经典位势理论（解 = C² 逐点满足）；Sobolev 1930s 引入弱导数与 Sobolev 空间，Lax–Milgram 1954 给出普遍存在性；Weyl 引理提供"弱→内部光滑"的桥。
- **核心命题**：Laplace 方程 Dirichlet 问题的存在性与正则性。
- **基础差异**："解"的定义强度（逐点 C² vs H¹ 变分恒等式）。
- **结论变化**：存在性↔正则性双向交换——经典解正则性前置但存在性稀缺；弱解存在性普遍但正则性分层（角点域 ∉ H²）。
- **SMPDL 标签**：`S-BISIM / M-BISIM / P-BISIM`。
- **对应文件**：
  - `SMP_ProofAnalysis_PDE_ClassicalSolution_Laplace.md`
  - `SMP_ProofAnalysis_PDE_WeakSolution_Laplace.md`
  - `SMPDL_Compare_ClassicalVsWeak_LaplaceEquation_PrePostFix.md`

---

### H19. 复分析：单复变 ↔ 多复变（19 世纪–1906）

- **历史定位**：Cauchy/Riemann/Weierstrass 建立单复变；Hartogs 1906 发现多复变特有现象——"被迫延拓"，多复变学科由此诞生；Cartan–Thullen 全纯凸刻画、Oka 解决 Levi 问题。
- **核心命题**：Hartogs 现象与全纯域。
- **基础差异**：复维数 n（1 vs ≥2）。
- **结论变化**：域的自由性消失（任意域可为自然域 → 存在非全纯域）；孤立奇点消失（可去/极点/本性分类 → 自动可去）——维度阈值相变，结论反转。
- **SMPDL 标签**：`S-ISO / M-BISIM / P-BISIM`。
- **对应文件**：
  - `SMP_ProofAnalysis_ComplexAnalysis_OneVariable.md`
  - `SMP_ProofAnalysis_ComplexAnalysis_SeveralVariables.md`
  - `SMPDL_Compare_OneVsSeveralComplexVariables_Hartogs_PrePostFix.md`

---

### H20. 组合/Ramsey 理论：有限 ↔ 无限 Ramsey（1930–1935）

- **历史定位**：Ramsey 1930 原始论文含无限版；Erdős–Szekeres 1935 重述有限版并给出递归界；无限版证明需依赖选择（DC），与有限版经紧致性衔接。
- **核心命题**：单色集存在性（有限尺寸 vs 无限集）。
- **基础差异**：论域基数（有限 vs 可数无限）；公理依赖（ZF vs ZF+DC）。
- **结论变化**：方向一致的强度加深（无限版更强且蕴含有限版）；"任意大有限"≠"无限"的语义鸿沟。
- **SMPDL 标签**：`S-ISO / M-BISIM / P-BISIM`。
- **对应文件**：
  - `SMP_ProofAnalysis_Ramsey_Finite.md`
  - `SMP_ProofAnalysis_Ramsey_Infinite.md`
  - `SMPDL_Compare_FiniteVsInfinite_Ramsey_PrePostFix.md`

---

### H21. 模型论：一阶 ↔ 二阶逻辑（1915–1950）

- **历史定位**：Löwenheim 1915/Skolem 1920/Gödel 1930 建立一阶元定理群；Dedekind 1888 的二阶归纳早已蕴含范畴性；Henkin 1950 的广义语义揭示"语义档位"隐藏第三档。
- **核心命题**：紧致性与 Löwenheim–Skolem 定理的成立性。
- **基础差异**：量词域（仅元素 vs 全部子集）；语义档位（全语义 vs Henkin 语义）。
- **结论变化**：紧致性/LS/完备性全部反转（✅→❌）；范畴性反向反转（❌→✅）——"没有免费午餐"权衡。
- **SMPDL 标签**：`S-BISIM / M-BISIM / P-BISIM`。
- **对应文件**：
  - `SMP_ProofAnalysis_FirstOrderLogic_Compactness.md`
  - `SMP_ProofAnalysis_SecondOrderLogic_FailureOfCompactness.md`
  - `SMPDL_Compare_FirstVsSecondOrder_Compactness_PrePostFix.md`

---

### H22. 证明论：Hilbert 系统 ↔ 自然演绎（1917–1965）

- **历史定位**：Hilbert 1917–28 极简公理化；Gentzen 1935 创立自然演绎/相继式演算并证 Hauptsatz；Prawitz 1965 完成规范化理论——"证明本身成为数学对象"。
- **核心命题**：切消去/规范化与子公式性质。
- **基础差异**：公理化风格（多公理+单规则 vs 规则对偶+近零公理）。
- **结论变化**：证明能力等价，但结构元定理从无到有（切消去/子公式/witness 提取/Curry–Howard）——分析力反转。
- **SMPDL 标签**：`S-BISIM / M-BISIM / P-BISIM`。
- **对应文件**：
  - `SMP_ProofAnalysis_ProofTheory_HilbertSystem.md`
  - `SMP_ProofAnalysis_ProofTheory_NaturalDeduction.md`
  - `SMPDL_Compare_HilbertVsNaturalDeduction_CutElimination_PrePostFix.md`

---

### H23. 泛函分析：Hilbert ↔ Banach 空间（1900s–1932）

- **历史定位**：Hilbert 1900s/Riesz 1907 建立内积空间几何；Banach 1932 系统化仅范数空间；Jordan–von Neumann 1935 给出"范数⇔内积"判定。
- **核心命题**：闭凸投影与对偶表示。
- **基础差异**：结构（内积+完备 vs 仅范数完备）。
- **结论变化**：投影存在唯一性反转（✅→c₀ 失效/C[0,1] 多解）；自对偶反转（Riesz ✅ → L^∞*⊋L¹）——单结构移除引发定理群坍塌。
- **SMPDL 标签**：`S-BISIM / M-BISIM / P-BISIM`。
- **对应文件**：
  - `SMP_ProofAnalysis_FunctionalAnalysis_HilbertProjection.md`
  - `SMP_ProofAnalysis_FunctionalAnalysis_BanachProjection.md`
  - `SMPDL_Compare_HilbertVsBanach_OrthogonalProjection_PrePostFix.md`

---

### H24. 表示论：线性 ↔ 置换表示（1896–1937）

- **历史定位**：Frobenius 1896 创立特征标理论；Burnside 1897/1911 轨道计数；Pólya 1937 计数理论——线性化单向桥（置换→线性）在两个传统间架设。
- **核心命题**：特征标正交与不变量完备性。
- **基础差异**：表示载体（向量空间 vs 集合作用）。
- **结论变化**：不变量完备性降档（特征标完备决定线性同构 vs 特征标不决定置换同构，需 Burnside 环）——信息压缩的单向性。
- **SMPDL 标签**：`S-BISIM / M-BISIM / P-BISIM`。
- **对应文件**：
  - `SMP_ProofAnalysis_RepresentationTheory_Linear.md`
  - `SMP_ProofAnalysis_RepresentationTheory_Permutation.md`
  - `SMPDL_Compare_LinearVsPermutationRepresentation_CharacterTheory_PrePostFix.md`

---

### H25. 动力系统：连续流 ↔ 离散映射（1880s–1975）

- **历史定位**：Poincaré 1880s/Bendixson 1901 平面二分定理；Sharkovsky 1964 周期全序、Li–Yorke 1975"周期三即混沌"、May 1976 logistic 流行化——两世界由 Poincaré 截面单向连接。
- **核心命题**：极限集结构（P–B 二分 vs Sharkovsky/混沌谱）。
- **基础差异**：时间结构（ℝ 流 vs ℕ 迭代）。
- **结论变化**：P–B/Dulac 定理群失效（平面二分 → 一维即混沌）；不变量更换（Hamiltonian → 拓扑熵）——定理群整体替换。
- **SMPDL 标签**：`S-BISIM / M-BISIM / P-BISIM`。
- **对应文件**：
  - `SMP_ProofAnalysis_DynamicalSystems_ContinuousFlow.md`
  - `SMP_ProofAnalysis_DynamicalSystems_DiscreteMap.md`
  - `SMPDL_Compare_ContinuousVsDiscreteDynamics_PoincareMap_PrePostFix.md`

---

### H26. 自动机理论：正则 ↔ 上下文无关（1956）

- **历史定位**：Kleene 1956 正则语言；Chomsky 1956 上下文无关文法、Chomsky–Schützenberger 1963 深化——Chomsky 层级的第一道"表达力换元性质"。
- **核心命题**：封闭性与判定性。
- **基础差异**：机器资源（有限状态 vs +无界栈）。
- **结论变化**：交/补封闭性反转（✅→❌）；等价判定从可判定跌至不可判定（元级反转）；隐藏 DCFL 层（确定性子类补封闭）。
- **SMPDL 标签**：`S-BISIM / M-BISIM / P-BISIM`。
- **对应文件**：
  - `SMP_ProofAnalysis_Automata_RegularLanguages.md`
  - `SMP_ProofAnalysis_Automata_ContextFreeLanguages.md`
  - `SMPDL_Compare_RegularVsContextFree_ClosureProperties_PrePostFix.md`

---

### H27. 逻辑/量子基础：布尔 ↔ 量子逻辑（1847–1967）

- **历史定位**：Boole 1847/1854 建立布尔代数，Stone 1936 证明集合表示；Birkhoff–von Neumann 1936 识别投影格为量子命题结构，Gleason 1957 推导 Born 规则，Kochen–Specker 1967 证明非语境真值指派不可能——分配律被确认为"经典性的结构指纹"。
- **核心命题**：分配律与真值/概率语义。
- **基础差异**：命题载体（集合 vs Hilbert 闭子空间）；律层级（分配律全局成立 vs dim≥3 失效、正交模律残存）。
- **结论变化**：分配律失效 + KS 全局真值指派不可能 + Stone 表示丧失——真值语义降为语境内（兼容块布尔拼图）；Gleason 把概率收窄为密度算子；dim=2 为模格中间档。
- **SMPDL 标签**：`S-BISIM / M-BISIM / P-BISIM`。
- **律登记**：甲级律（分配律），见 `SMPDL_LawStructure_MigrationScreening.md`。
- **对应文件**：
  - `SMP_ProofAnalysis_QuantumLogic_BooleanAlgebra.md`
  - `SMP_ProofAnalysis_QuantumLogic_OrthomodularLattice.md`
  - `SMPDL_Compare_BooleanVsQuantumLogic_DistributiveLaw_PrePostFix.md`

---

### H28. 代数：结合代数 ↔ 非结合代数（1843–1950s）

- **历史定位**：Hamilton 1843.10 打破交换律仅两个月后，Graves 1843.12（Cayley 1845 独立发表）打破结合律得八元数；Frobenius 1877 封顶结合可除代数（ℝ,ℂ,ℍ），Hurwitz 1898 以交错律换价封顶 8 维；Lie 1870s–80s 建立以雅可比恒等式替代结合的李理论；Artin 定理（1950s）给出两生成元局域桥。
- **核心命题**：结合律与括号语义（幂的良定义性）。
- **基础差异**：括号可否压扁（树→串 vs 树即语义）；幂 `aⁿ` 良定义 vs 失义。
- **结论变化**：记号合法性坍塌（aⁿ 失义）+ 数系封顶换价（Frobenius 4 维 → Hurwitz 8 维）+ 例外结构涌现（G₂、例外李代数）；残存律 = 交错律（Artin 桥）+ 雅可比恒等式（派生通道）。
- **SMPDL 标签**：`S-BISIM / M-BISIM / P-BISIM`。
- **律登记**：甲级律（结合律）· F1 族 · D 档 · 模式一+二（E′ = 交错律/雅可比），见 `SMPDL_LawStructure_MigrationScreening.md`。
- **对应文件**：
  - `SMP_ProofAnalysis_AssociativeAlgebra_PowerLaws.md`
  - `SMP_ProofAnalysis_NonAssociativeAlgebra_OctonionsLie.md`
  - `SMPDL_Compare_AssociativeVsNonAssociative_BracketLaws_PrePostFix.md`

---

### H29. 分析基础：ℚ ↔ ℝ 的 Dedekind 完备律（~500 BCE–1872）

- **历史定位**：毕达哥拉斯 √2 不可通约开启两千年 L1 潜默；Dedekind/Cantor 1872 双构造（分割/Cauchy 列）完成裁决；Hilbert 唯一性表征（完备序域 ≅ ℝ）定型"对象由律定义"。
- **核心命题**：完备律与 IVT/单调收敛/Heine–Borel 定理群的生根。
- **基础差异**：有序域公理相同；完备律（sup 存在）一有一无。
- **结论变化**：定理群整体反转（ℚ ❌ IVT/单调收敛/区间套 → ℝ ✅ 全恢复 + HB(ℝ) 新生）；全库唯一"加法断裂"（加律看生根，与减法族镜像）；**上游律**——回溯串联 H10（IVT 可计算化）、H11（紧致性 = 完备律下游）、H17（测度引擎地基）、H6（完备性另一档拆解：*ℝ 弃阿基米德）。
- **SMPDL 标签**：`S-BISIM / M-BISIM / P-BISIM`。
- **律登记**：乙级律（完备律）· F5 族 · D+E 双档 · 模式一+二（E′ = 定理群满仓），见 `SMPDL_LawStructure_MigrationScreening.md`。
- **对应文件**：
  - `SMP_ProofAnalysis_RationalsQ_SupremumGap.md`
  - `SMP_ProofAnalysis_CompleteOrderedField_TheoremGroup.md`
  - `SMPDL_Compare_QvsR_DedekindCompleteness_PrePostFix.md`（含 §5 上游回溯串联总图）

---

### H30. 测度论：条件收敛 ↔ 绝对可积（1821–1909）

- **历史定位**：Cauchy 1821 误判连续性足以交换逐次积分；一维 Riemann 重排定理（1854/1867）率先示警；19 世纪反例积累（L3 摩擦 80 年）；Fubini 1907 / Tonelli 1909 在测度论框架完成裁决（L6）。
- **核心命题**：积分次序交换律（∫∫ = ∫∫）。
- **基础差异**：可积性档位（条件收敛 vs 绝对可积 L¹ / 非负）+ σ-有限性。
- **结论变化**：交换律三档定价——非负免费（Tonelli）/ L¹ 标准（Fubini）/ 条件收敛禁区（±π/4 反例守门）；与 H17 构成 F5 姊妹篇（极限-积分 / 积分-积分交换的定价手册）；一维同构 = Riemann 重排定理。
- **SMPDL 标签**：`S-BISIM / M-BISIM / P-BISIM`。
- **律登记**：乙级律（Fubini 交换律）· F5 族 · E 档 · 模式一+二；**移除-涌现首轮回验组**（α 主 + γ 辅，触发修订案 A），见 `SMPDL_LawStructure_MigrationScreening.md` 与 `SMPDL_RemovalEmergence_Synthesis.md`。
- **对应文件**：
  - `SMP_ProofAnalysis_IteratedIntegrals_ConditionalConvergence.md`
  - `SMP_ProofAnalysis_FubiniTonelli_AbsoluteIntegrability.md`
  - `SMPDL_Compare_ConditionalVsAbsolute_IteratedIntegral_PrePostFix.md`（含 §7 移除-涌现回验）

---

### H31. 重写理论/λ 演算：非汇合 ↔ Church–Rosser（1936–1970）

- **历史定位**：Church–Rosser 1936 与 Gentzen 切消去 1935 同期同工具（C3 集群双响）；Tait/Martin-Löf 并行归约定型证明；Knuth–Bendix 1970 把汇合检查算法化。
- **核心命题**：汇合律（范式唯一性）。
- **结论变化**：一般 TRS 汇合失效（a→b,a→c 双范式）；λβ 恢复（斜条带法）；范式唯一/一致性/策略自由三后果；工具群（KB/Newman/正交）。
- **律登记**：乙级（Church–Rosser 汇合律）· F6 族 · E 档；回验 α 主 + β 辅（元层涌现，修订案 B）。
- **对应文件**：`SMP_ProofAnalysis_Rewriting_NonConfluent.md` / `SMP_ProofAnalysis_LambdaCalculus_ChurchRosser.md` / `SMPDL_Compare_NonConfluentVsLambda_ChurchRosser_PrePostFix.md`

---

### H32. 序理论/非线性分析：单调 ↔ 非单调集值（1928–1964）

- **历史定位**：Knaster 1928/Tarski 1955 单调免费午餐；Kakutani 1941 凸性接棒；Nash 1950 一页证明；Minty 1962 单调几何表征；VI（Lions–Stampacchia 1967）。
- **核心命题**：单调律与不动点/均衡存在性。
- **结论变化**：免费午餐终止（递减跳跃反例）；凸值+USCO 接棒（Kakutani）；单调降档为唯一性可购条件；Minty E′ 表征。
- **律登记**：乙级（单调律）· F5 族 · E 档+E′；回验**学科级 α 兑现**（Nash/VI 双产业）+ 跨组元涌现（凸性接盘侠规律，修订案 C）。
- **对应文件**：`SMP_ProofAnalysis_Tarski_MonotoneFixpoint.md` / `SMP_ProofAnalysis_SetValued_KakutaniVI.md` / `SMPDL_Compare_MonotoneVsSetValued_EquilibriumTheory_PrePostFix.md`

---

### H33. 数学物理：耗散 ↔ 变分对称（1918–1963）

- **历史定位**：Noether 1918《不变变分问题》（Göttingen，与本项目谱系同源）；Lorenz 1963 耗散混沌；Ward–Takahashi 量子延伸。
- **核心命题**：守恒律与对称性对偶。
- **结论变化**：一般系统守恒缺席（零首次积分常态，混沌前提）；变分+对称 ⇒ 守恒定价且**双向**（逆定理）；规范（无限维）⇒ 恒等式分档；Ward E′。
- **律登记**：乙级（守恒律）· F7 表征律族（物理界代表）· E 档 + Ward E′；回验 γ 兑现 + 双向涌现（修订案 D）。
- **对应文件**：`SMP_ProofAnalysis_DissipativeSystem_NoConservation.md` / `SMP_ProofAnalysis_Noether_SymmetryConservation.md` / `SMPDL_Compare_DissipativeVsVariational_Noether_PrePostFix.md`

---

## 三、阅读与使用建议

### 3.1 教学顺序

建议按本索引的 H1→H26 顺序引导学生：

1. 从**几何直觉**（H1、H16）入手，理解曲率、平行公设如何改变三角形内角和；
2. 进入**分析与离散**（H2、H3），体会连续/离散与有限/无限的差异；
3. 进入**代数**（H4、H5），理解单条公理或域特征如何改变恒等式；
4. 进入**分析基础**（H6、H10、H11、H17），比较 ε-δ、无穷小、可计算性、紧致性与测度论五种严格化/抽象化路径；
5. 进入**逻辑与基础**（H7–H9、H21、H22），讨论 20 世纪数学基础危机、逻辑强度权衡与证明结构分析；
6. 进入**现代结构观**（H12、H14、H23、H24），理解"相同"概念强度分层、几何对象的层化升级、空间结构与不变量分辨率；
7. 进入**概率与数论的多元方法**（H13、H15），体会同一结论在不同解释框架或数学分支中的并存；
8. 进入**方程与动力学**（H18、H25），理解解的定义强度与时间结构如何重塑定理群；
9. 进入**维数与层级**（H19、H20、H26），理解维度阈值、基数层级与计算层级引发的定性断裂。

### 3.2 审校顺序

对于 AI 生成证明审校，建议**反向**从 H26→H1 扫描：

- 先检查**层级与阈值**（H26：语言类/机器资源、H20：论域基数、H19：复维数）是否声明；
- 再检查**方程与动力系统框架**（H25：时间结构、H18：解的强弱层级）是否声明；
- 再检查**概率解释与方法框架**（H13：频率主义/贝叶斯、H15：解析/代数数论）是否声明；
- 再检查**现代结构观**（H14：簇/概形框架、H12：同构/等价/同伦等价强度、H23：空间结构、H24：不变量分辨率）是否声明；
- 再检查**可计算性与紧致性需求**（H11：紧致性假设、H10：可计算性需求、H17：积分框架）与**基础框架**（H9：集合论/类型论、H8：ZFC/ZF、H7：经典/直觉主义、H21：逻辑阶数、H22：证明系统风格）是否声明；
- 再检查**分析/代数**基础是否匹配结论；
- 最后检查**几何**前提（H1、H16：欧氏/球面/双曲、曲率 `K`）是否被默认。

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
- `SMPDL_Audit_SampleSuite.md`：将这 43 组 126 份报告按 H1–H43 编号入库。

---

## 五、署名与许可

本索引由 Göttingen SMPDL 项目维护，采用项目统一的署名与许可条款。新增索引版本号 `v1.0`，后续随样本库扩展升级。
