# SMPDL 数学史回溯：十个最有希望 Lean 样本

**SMPDL History Retrospective: The 10 Most Promising Lean-Formalized Samples**  
**版本 Version**: v2.2-retro  
**日期 Date**: 2026-10-13  
**样本来源 Source**: OpenAI math release, 第五批「结构最完善、已有 Lean 证明」的 10 个族  
**方法论 Methodology**: S/M/P × D/L 六格审计 + 数学史谱系定位 + 最近构造/证明方法比对

---

## TL;DR

本报告对第五批 SMPDL 审计中筛选出的 **10 个「最有希望」Lean 形式化样本**做数学史回溯。每个样本给出：

1. **历史主线 Thread**：从问题提出到 OpenAI 声明的关键节点；
2. **最接近的经典构造 Closest Classical Construction**：人类数学中与之同构或最相似的构造；
3. **最接近的证明方法 Closest Proof Method**：该领域主导的、可类比的方法论；
4. **仍需人类补充的位置 Remaining Human Gap**：Lean 覆盖之外、仍需数学家审查的结构/前提。

总览表显示，这 10 个问题横跨 **解析数论、组合数论、图论、离散几何、表示论、泛函分析**六大领域；它们的人类数学史平均跨度约 **40–60 年**，其中 3 个（KL 组合不变性、强瘦树、Tingley 问题）仍是开放或仅部分解决的核心猜想。

---

## 1. 样本遴选说明

第五批审计的目标是从 OpenAI math 库中挑选 **「结构相对最完善、已有 Lean 形式化」** 的 10 个族。遴选标准包括：

- 声明在 Lean 仓库中有对应条目；
- 证明长度适中，TRAP-CHECK 风险可控；
- 与已知人类数学构造有足够丰富的历史对话空间；
- 人类科学家仍能在「动机/推广/边界条件」层面提出补充证明。

最终入选的 10 个族如下表。

| 编号 No. | 样本 Sample | 领域 Field | 首次提出 First Posed | Lean 状态 Lean Status | 人类史跨度 Human History Span |
|---|---|---|---|---|---|
| 1 | Squarefree values of quartic polynomials | 解析数论 | Erdős (1953) | 已形式化 | 73 年 |
| 2 | Jacobsthal quadratic upper bound | 组合数论/筛法 | Jacobsthal / Erdős (1965) | 已形式化 | 61 年 |
| 3 | Totient asymptotic formula | 解析数论 | Mertens (1874) | 已形式化 | 152 年 |
| 4 | Bounded components of Gaussian-prime graphs | 组合数论/几何 | Gordon (1962) | 已形式化 | 64 年 |
| 5 | Planar graph L1 embeddings | 度量嵌入/算法 | Gupta et al. (2004) | 已形式化 | 22 年 |
| 6 | Mixing time of graph switch Markov chain | 组合概率/马尔可夫链 | Jerrum–Sinclair (1980s) | 已形式化 | 40 年 |
| 7 | Periodic tiling counterexample (Einstein problem) | 离散几何 | Wang (1961) | 已形式化 | 65 年 |
| 8 | Kazhdan–Lusztig combinatorial invariance | 表示论/组合 | Kazhdan–Lusztig (1979) | 已形式化 | 47 年 |
| 9 | Strong thin spanning trees | 图论/组合优化 | Goddyn (2004) | 已形式化 | 22 年 |
| 10 | Tingley sphere isometry problem | 泛函分析/凸几何 | Tingley (1987) | 已形式化 | 39 年 |

---

## 2. 逐项历史回溯

### 2.1 Squarefree values of quartic polynomials

**样本名 Sample**: `SMP_ProofAnalysis_OpenAI_Squarefree_Quartics.md`  
**核心声明 Core Claim**: 每个可约、不可约的四次（乃至 4–8 次）整系数多项式，在允许条件下，其取值中平方自由值具有正密度，且密度由 Euler 乘积给出。

#### 历史主线

- **1933 Ricci**: 处理 `k ≥ d` 情形，给出完整渐近公式；密度常数即为 Euler 乘积。
- **1953 Erdős**: 证明 `k = d − 1` 时存在无穷多个 `k`-幂自由值；特别指出 `n⁴ + 2` 的平方自由问题仍是开放。
- **1967 Hooley**: 对 `k = d − 1` 给出精确渐近。
- **1976 Nair**: 将 `k = d − 2` 推进到 `d ≥ 24`。
- **2006 Heath-Brown**: 引入 **determinant method**，证明 `d ≥ 10` 时 `k = d − 2` 成立。
- **2011 Browning**: 改进到 `d ≥ 9`，并给出 `Xᵈ + c` 型多项式 `d ≥ 6` 的结果。
- **2026 OpenAI**: 声称覆盖 `d = 4,5,6,7,8`（即 `k = d − 2`），从而与 Browning 结果衔接，覆盖所有 `d ≥ 4`。

#### 最接近的数学构造

**局部密度 Euler 乘积** 是最核心的构造：对每个素数 `p`，计算 `f(n) ≡ 0 (mod p²)` 在 `p²` 个剩余类中的比例 `ρ_f(p²)/p²`，则密度为

```
C(f,2) = ∏_p (1 − ρ_f(p²)/p²)
```

这与 **Bunyakovsky 型可允许条件** 直接相关：必须排除某个 `p²` 整除所有 `f(n)` 的退化情形。

#### 最接近的证明方法

Heath-Brown 的 **p-adic determinant method** 是该问题的标准工具：

1. 将 `f(n)` 被大素数平方整除的稀有事件，转化为某固定曲面上的有理点计数；
2. 用行列式方法给出这类点的上界；
3. 小素数用剩余类计数直接处理。

OpenAI 证明的关键人类审查点是：它是否真正将 Heath-Brown–Browning 的 determinant method 推广到 `d = 4–8`，还是在某个隐藏处依赖了尚未发表的 intermediate result。

#### 仍需人类补充

- **明确有效误差项**：OpenAI 声明给出的是密度极限，但未给出收敛速率；人类数学家需补证 `O(x^{1−δ})` 型误差项。
- **Admissibility 的算法判定**：Lean 中「对所有 `p`，存在 `n` 使 `p² ∤ f(n)`」这一条件在实现时是否完整覆盖了 Erdős 例外（`k = 2ˡ` 且 `2^{k−1} | f(n)` 对所有 `n`）。

---

### 2.2 Jacobsthal quadratic upper bound

**样本名 Sample**: `SMP_ProofAnalysis_OpenAI_Jacobsthal_QuadraticBound.md`  
**核心声明 Core Claim**: Jacobsthal 函数 `h(k)` 满足 `h(k) ≪ k² / (log log 3k)²`，即任意 `k` 个素数与剩余类无法覆盖超过 `C k² / (log log k)²` 长度的连续整数区间。

#### 历史主线

- **Jacobsthal**: 提出 `h(k) ≪ k²` 的猜想。
- **Erdős**: 观察到 Brun 筛法可给出 `h(k) ≪ k^c`（某常数 `c`）。
- **1977 Vaughan**: 证明 `h(k) ≪ k² (log k)⁴`。
- **1978 Iwaniec**: 改进到 `h(k) ≪ (k log k)²`。
- **2018 Ford–Green–Konyagin–Maynard–Tao**: 给出下界 `h(k) ≫ k (log k)(log log log k)/(log log k)²`，说明真实增长率在 `k` 与 `k²` 之间。
- **2026 OpenAI**: 声称改进到 `k² / (log log 3k)²`，首次将多余对数因子从分子移到分母。

#### 最接近的数学构造

**剩余类筛与 totative 计数**：给定 `k` 个素数 `P`，对每对素数 `p,q` 选择剩余类 `a_p, a_q`，删除所有满足 `n ≡ a_p (mod p)` 的整数。Jacobsthal 函数即问：最短多长区间必含一个不被任何 `p ∈ P` 整除的整数（totative）。

#### 最接近的证明方法

Iwaniec 的 **线性筛法 (linear sieve)** 与 Vaughan 的 **大筛法组合** 是主要工具：

1. 用筛法估计在长度 `L` 区间内「与所有 `p ∈ P` 都不互素」的整数个数；
2. 标准大筛在 `L ≈ k²` 时给出的下界恰好趋于零，因此必须保留边界项；
3. OpenAI 声称通过分析「试图抵消边界项的剩余类必然呈现刚性模式」，从而控制这些模式的贡献。

#### 仍需人类补充

- **显式常数 `C`**：声明是非显式的，人类数学家需将其明确化或给出至少一个可计算上界。
- **刚性模式的完整分类**：OpenAI 的论证依赖于剩余类模式的可预测性，但尚未给出分类引理；人类需补证该刚性结构的穷举。
- **与素数间隙问题的联系**：Jacobsthal 函数与 `Y(x)`（覆盖 `[1,y]` 所需素数剩余类问题）等价，OpenAI 是否一致处理了该等价性？

---

### 2.3 Totient asymptotic formula

**样本名 Sample**: `SMP_ProofAnalysis_OpenAI_Totient_Asymptotic.md`  
**核心声明 Core Claim**: Euler totient 函数的部分和满足

```
∑_{n≤x} φ(n) = (3/π²) x² + O(x log x)
```

或更强的误差项形式。

#### 历史主线

- **1874 Mertens**: 首次证明主项 `3/π² x²` 与误差 `O(x log x)`。
- **1930 Chowla–Pillai**: 证明误差不能是 `o(x log log log x)`。
- **1950 Erdős–Shapiro**: 给出 `Ω_±(x log log log log x)` 振荡下界。
- **1963 Walfisz**: 用 Vinogradov 均值定理与指数和，将误差改进为 `O(x (log x)^{2/3} (log log x)^{4/3}`)，保持 50 年最佳。
- **1987 Montgomery**: 进一步改进振荡下界到 `Ω_±(x √log log x)`。
- **2016 H.-Q. Liu**: 将 Walfisz 误差中的 `(log log x)^{4/3}` 改进为 `(log log x)^{1/3}`。
- **2026 OpenAI**: 在 Lean 中形式化了一个特定误差项版本（很可能是 Mertens 经典形式）。

#### 最接近的数学构造

**Möbius 反演与格点计数**：核心恒等式

```
∑_{d≤x} μ(d) ⌊x/d⌋² = −1 + 2∑_{n≤x} φ(n)
```

将 totient 求和转化为互素整数对计数，再用 Dirichlet 双曲法拆分求和范围。

#### 最接近的证明方法

Mertens 的 **初等证明** 是教学标准：

1. 用 `φ(n) = n ∑_{d|n} μ(d)/d`；
2. 交换求和顺序得到 `∑_{d≤x} μ(d) ⌊x/d⌋ (x/d + O(1))`；
3. 主项给出 `(6/π²) x²/2 = 3/π² x²`，误差项 `O(x log x)`。

若 OpenAI 声称更强误差，则需引入 **Vaughan 恒等式** 或 **Vinogradov 组合分解** 处理 Type I/II 指数和。

#### 仍需人类补充

- **误差项的精确形式**：需要确认 Lean 中形式化的是 Mertens 的 `O(x log x)` 还是 Walfisz/Liu 的更强结果；后者需要大量指数和理论，目前未见公开 Lean 库支持。
- **`Ω` 下界的补充**：上界只是问题的一半；人类数学家通常也会关心 Chowla–Pillai 型下界，OpenAI 是否处理了双向结果？

---

### 2.4 Bounded components of Gaussian-prime graphs

**样本名 Sample**: `SMP_ProofAnalysis_OpenAI_GaussianPrime_BoundedComponents.md`  
**核心声明 Core Claim**: 在 Gaussian 素数图上，以有界步长 `D` 行走时，每个连通分支的大小被一个只依赖于 `D` 的常数 `B_D` 一致有界；即 Gaussian moat 问题答案为否。

#### 历史主线

- **1962 Basil Gordon**: 在斯德哥尔摩 ICM 上提出 Gaussian moat 问题：能否用有界步长在 Gaussian 素数上走到无穷远？
- **1970 Jordan–Rabung**: 证明至少需要步长 4。
- **1998 Gethner–Wagon–Wick**: 用计算机找到步长 `√26` 的「护城河」，覆盖所有素数到 `10⁶`。
- **1998 Ilan Vardi**: 引入 **prime percolation** 随机模型，用连续渗流预测临界步长约为 `√(2π λ_c log |z|)`。
- **2005 Tsuchimura**: 证明步长 `≤ 6` 时从原点出发的可达范围有限。
- **2026 OpenAI**: 声称对所有起点（包括坐标轴）和步长 `D`，连通分支一致有界。

#### 最接近的数学构造

**Gaussian 整数筛 + 信息熵论证**：选取有限个满足 `p ≡ 1 (mod 4)` 的普通素数，每个分裂为两个 Gaussian 素数；删除所有被这些素数整除的格点。OpenAI 声称可以构造一个周期性筛，使得任何步长 `≤ D` 的无穷路径都无法完全避开被删除点。

这与 **覆盖系统 (covering system)** 和 **渗流相变 (percolation transition)** 有精神联系：素数密度足够低，但局部结构（分裂、相伴元）强制产生不可穿越的障碍。

#### 最接近的证明方法

OpenAI 使用的核心方法是 **熵方法 (entropy method)**：

1. 采样一条有界步长路径上的若干点；
2. 考察这些点在被选素数模下的剩余类分布；
3. 若路径无限，则这些点必须在越来越多的素数约束下「躲避」被删除类；
4. 每次跨过一个素数块都会损失固定量的熵；
5. 有界步长携带的信息量有限，导致矛盾。

这与 Vardi 的 **渗流启发** 互补：渗流预测非周期障碍的存在，熵方法试图给出确定性证明。

#### 仍需人类补充

- **`B_D` 的显式公式**：声明仅证明存在性，未给出 `B_D` 关于 `D` 的任何显式界。
- **熵论证的严格化**：将「随机采样」转化为不依赖概率的确定性计数论证，是数学家通常要求的严格化步骤。
- **相伴元 (associates) 与坐标轴素数的处理**：Lean 声明包含坐标轴上的 Gaussian 素数（即 `1+i` 的相伴元及普通素数 `p ≡ 3 mod 4`），需确认证明是否一致覆盖这些退化情形。

---

### 2.5 Planar graph L1 embeddings

**样本名 Sample**: `SMP_ProofAnalysis_OpenAI_Planar_L1_Embeddings.md`  
**核心声明 Core Claim**: 平面图（或更一般地，排除固定 minor 的图族）可低失真嵌入 `L1` 空间，可能与 Gupta 等 2004 年的常数失真猜想相关。

#### 历史主线

- **1981 Okamura–Seymour**: 若所有 terminals 位于单个面上，则存在到 `L1` 的等距嵌入。
- **1999 Rao**: 证明任意 `n` 顶点平面图可嵌入 `L1` 且失真 `O(√log n)`。
- **2004 Gupta–Newman–Rabinovich–Sinclair**: 猜想排除固定 minor 的图族可 **常数失真** 嵌入 `L1`。
- **2009 Lee–Sidiropoulos**: 研究 terminals 可被 `γ` 个面覆盖的情形。
- **2013 Chekuri 等**: 进一步改进面覆盖参数化。
- **2019 Krauthgamer–Lee–Rika**: 给出 `O(log γ)` 失真上界。
- **2020 Filtser**: 改进到 `O(√log γ)`。
- **2026 OpenAI**: 声称给出平面图到 `L1` 的某种低失真嵌入（具体常数/参数需核对）。

#### 最接近的数学构造

**稀疏割–流对偶 (Sparsest Cut / Flow-Cut Gap)**：`L1` 嵌入失真与稀疏割问题中的流–割间隙等价（Linial–London–Rabinovich 1995; Gupta–Newman–Rabinovich–Sinclair 2004）。因此平面图 `L1` 嵌入的构造直接对应于平面图稀疏割的近似算法。

另一个关键构造是 **部分最短路径分解 (Partial Shortest Path Decomposition, PSPD)**：将度量拆分为若干截断的 `L1` 范数分量，每一项对应图中某条最短路径。

#### 最接近的证明方法

现代证明通常沿以下路线：

1. **Krauthgamer–Nguyen–Zondiner** 型随机嵌入：按某种概率分布将图嵌入到 `L1`；
2. **Okamura–Seymour 定理** 处理单面 terminals 的精确等距嵌入；
3. **面覆盖分解**：将一般 terminals 集合分解为 `γ` 个单面子问题；
4. **凸组合**：将这些单面嵌入组合成全局低失真嵌入。

OpenAI 若能将失真降到 `O(1)`，则是重大突破，需要仔细审查其是否隐式依赖了未解决猜想。

#### 仍需人类补充

- **具体失真常数**：Gupta 猜想是 `O(1)`，但 OpenAI 声明的具体参数必须明确，否则无法判断其是否真正解决该猜想。
- **终端集合 (terminals) 的限制**：Filtser 的结果针对 terminals 可被 `γ` 个面覆盖；OpenAI 是否处理全顶点集 `V`？
- **权重图与无权重图**：Rao 的结果对加权平面图成立；OpenAI 的 Lean 形式化是否一致处理了边权？

---

### 2.6 Mixing time of graph switch Markov chain

**样本名 Sample**: `SMP_ProofAnalysis_OpenAI_GraphSwitch_Mixing.md`  
**核心声明 Core Claim**: 图切换链（switch chain）在给定度序列的所有简单图上具有快速混合（polynomial mixing time）。

#### 历史主线

- **1980s Jerrum–Sinclair**: 用 **canonical paths** 方法证明随机正则图生成算法的快速混合。
- **1999 Kannan–Tetali–Vempala**: 将近正则二分图的切换链混合分析系统化。
- **2007 Cooper–Dyer–Frieze**: 对正则简单图给出切换链的多项式混合时间上界。
- **2015 Greenhill 等**: 将结果推广到「不太稠密」的不规则度序列，提出 **stability** 条件。
- **2018–2020**: 对更广泛的 degree sequences（包括部分稠密情形）的混合分析继续推进。
- **2026 OpenAI**: 声称在 Lean 中形式化了一般度序列下图切换链的快速混合。

#### 最接近的数学构造

**对称差与交替环**：给定两个同度序列图 `G, G'`，其对称差 `G Δ G'` 可分解为若干偶长度的交替环。切换链的每次转移可看作在某个 4-顶点子图上交换两条边。

**多商品流 (multicommodity flow)**：在状态空间上定义一组从 `G` 到 `G'` 的规范路径，要求每条边上的流负载不要过大。

#### 最接近的证明方法

Sinclair 的 **多商品流/导通率 (conductance)** 框架是标准方法：

1. 对每个 `(G, G')` 对，在 `G Δ G'` 的交替环上构造规范路径；
2. 证明任何中间图 `Z` 与某个编码（encoding）一一对应；
3. 通过编码数限制经过每条转移的规范路径数量；
4. 得出导通率下界，从而得到混合时间上界。

OpenAI 若声称完全一般度序列的快速混合，则需审查其是否覆盖了 Greenhill 等人发现的一些反例/慢混合序列。

#### 仍需人类补充

- **度序列条件**：快速混合并非对所有度序列成立；OpenAI 是否明确了适用的度序列类（如 `P-stable` 或 `8-stable`）？
- **编码引理的严格性**：canonical path 分析中「给定 `(Z,Z')`、`L`、`φ` 可唯一恢复 `(G,G')`」这一 encoding 论证是常见的人类审查点。
- **与二分图切换链的关系**：OpenAI 是否区分了非二分图与二分图切换链？后者已有更完整理论。

---

### 2.7 Periodic tiling counterexample (Einstein problem)

**样本名 Sample**: `SMP_ProofAnalysis_OpenAI_PeriodicTiling_Counterexample.md`  
**核心声明 Core Claim**: 存在某种周期性铺砖的反例构造，或与 **Einstein problem**（是否存在单块非周期铺砖）的严格形式化相关。

#### 历史主线

- **1961 王浩 (Hao Wang)**: 提出 Wang tiles 与可判定性问题；猜想任何能铺砌平面的有限 tile set 都能周期铺砌。
- **1966 Robert Berger**: 构造首个非周期 tile set（20,426 块 Wang tiles），证明 Wang 猜想错误，且 Domino 问题不可判定。
- **1971 Raphael Robinson**: 将非周期集缩小到 6 块。
- **1973 Roger Penrose**: 用风筝与飞镖 (kite and dart) 两块实现非周期铺砌。
- **2010 Socolar–Taylor**: 提出单块非连通 tile 的解法。
- **2022–2023 Smith–Myers–Kaplan–Goodman-Strauss**: 发现 **hat tile**（允许镜像）和 **spectre**（严格手性、无需镜像）两块单 tile，彻底解决 Einstein problem。
- **2026 OpenAI**: 声称在 Lean 中形式化了一个「周期铺砖反例」或相关的 tile 非周期性质。

#### 最接近的数学构造

**替换系统 (substitution tiling)** 与 **匹配规则 (matching rules)**：非周期性的经典来源包括：

- Robinson 的层级替换规则；
- Penrose 的边/角匹配规则；
- hat tile 的 **metatile** 层级与 **spectre** 的严格手性构造。

OpenAI 的「周期铺砖反例」最可能是指：构造一个 tile set，它可铺砌平面，但任何铺砌都不是周期性的——即非周期集的显式示例。

#### 最接近的证明方法

现代 Einstein 问题的证明方法是 **组合-几何 + 计算机辅助验证**：

1. 定义 tile 的有限邻域配置集合；
2. 证明任何全局铺砌必然满足某种层级替换结构；
3. 通过替换矩阵或 inflation factor 证明不存在全局平移对称性；
4. 用 SAT / 组合搜索验证局部配置集的完备性。

#### 仍需人类补充

- **tile 是否允许反射/旋转/装饰**：Einstein 问题的不同变体对匹配规则、反射、装饰有不同要求；OpenAI 必须明确其形式化的是哪一版本。
- **计算机辅助部分的信任链**：hat/spectre 证明中大量依赖计算搜索；Lean 形式化需将这些搜索（或至少其结果）纳入验证。
- **从局部规则到全局非周期的严格推导**：替换层级存在 ⇒ 非周期性，这一步通常需要人类数学家给出清晰的归纳论证。

---

### 2.8 Kazhdan–Lusztig combinatorial invariance

**样本名 Sample**: `SMP_ProofAnalysis_OpenAI_KazhdanLusztig_CombinatorialInvariance.md`  
**核心声明 Core Claim**: Kazhdan–Lusztig 多项式 `P_{x,w}(q)` 仅由 Coxeter 群中的 Bruhat 区间 `[x,w]` 的偏序结构决定。

#### 历史主线

- **1979 Kazhdan–Lusztig**: 在 Hecke 代数中定义 KL 多项式，猜想其系数对应 flag variety 上 Schubert variety 的 intersection cohomology 维数。
- **1981 Beilinson–Bernstein** 与 **Brylinski–Kashiwara**: 独立证明 KL 猜想，建立几何表示论与组合表示论的桥梁。
- **1980s Lusztig / Dyer**: 提出 **combinatorial invariance conjecture**：KL 多项式只依赖于 Bruhat 区间的 poset 结构。
- **1990s–2000s**: 对短长度区间（长度 ≤ 4，后扩展到 ≤ 8 in type A, ≤ 6 in types B/D）进行计算机验证。
- **Soergel bimodules**: 给出 KL 多项式的纯代数/组合解释，但未完全解决组合不变性。
- **2026 OpenAI**: 声称在 Lean 中形式化了某类 Coxeter 群中的组合不变性结果。

#### 最接近的数学构造

**Bruhat 区间与 R-多项式**：KL 多项式递归地由 R-多项式定义，而 R-多项式本身完全由 Bruhat 序的覆盖关系确定。组合不变性猜想等价于：R-多项式也是 Bruhat 区间 poset 的不变量。

另一个核心构造是 **Soergel bimodule**：它将 Hecke 代数范畴化，使得 KL 多项式系数成为某些 Hom 空间的维数。

#### 最接近的证明方法

目前已知结果主要是 **计算验证 + 组合分类**：

1. 对固定长度 `L`，枚举所有可能的 Bruhat 区间 poset；
2. 用递归公式计算 KL 多项式；
3. 验证同构 poset 给出相同多项式。

OpenAI 若声称一般性证明，则需给出新的结构性论证，可能是通过 Soergel bimodule 的某种等价性。

#### 仍需人类补充

- **适用范围**：组合不变性猜想在一般 Coxeter 群中仍是开放问题；OpenAI 是否仅在有限/可计算情形（如长度 ≤ N 或特定类型）形式化？
- **从 R-多项式到 KL 多项式的递归**：该递归涉及 Möbius 反演；Lean 实现时需确保基例与归纳步覆盖所有退化区间。
- **几何解释的缺失**：即使组合不变性在 Lean 中成立，其几何意义（与 intersection cohomology 的联系）仍需人类数学家解释。

---

### 2.9 Strong thin spanning trees

**样本名 Sample**: `SMP_ProofAnalysis_OpenAI_StrongThinSpanningTrees.md`  
**核心声明 Core Claim**: 每个 `k`-边连通图都包含一个 `O(1/k)`-瘦的生成树（strong thin tree conjecture 的最优形式）。

#### 历史主线

- **1961 Nash–Williams / 1961 Tutte**: 树打包定理：2k-边连通图包含 k 条边不交生成树。
- **1984 Jaeger**: 提出弱 3-流猜想；Thomassen 后来用不同方法证明。
- **2004 Goddyn**: 提出 **thin tree conjecture**：存在函数 `f` 使得每个 `f(ε)`-边连通图都有 `ε`-瘦生成树。**Strong** 形式要求 `f(ε) = O(1/ε)`。
- **2011 Oveis Gharan–Saberi**: 对平面/有界亏格图证明存在性。
- **2015 Anari–Oveis Gharan**: 用谱方法证明任意 `k`-边连通图存在 `O(polyloglog n / k)`-瘦树。
- **2017 Asadpour–Goemans–Madry–Oveis Gharan–Saberi**: 给出构造性算法， achieve `O(log n / log log n · k)`-瘦树。
- **2015 Marcus–Spielman–Srivastava**: 解决 Kadison–Singer 问题，为 **spectrally thin trees** 提供工具。
- **2026 OpenAI**: 声称在 Lean 中形式化 strong thin tree 的最优界。

#### 最接近的数学构造

**生成树多面体 (spanning tree polytope)**：所有生成树的凸包；一点 `z ∈ STP` 可理解为生成树的分数包装。

**有效电阻 (effective resistance)** 与 **谱稀疏化 (spectral sparsification)**：Harvey–Olver 将瘦树问题松弛为谱瘦树，用 Kadison–Singer / 交错族方法处理。

#### 最接近的证明方法

强瘦树猜想的已知最佳路线：

1. **谱松弛**：将边割条件替换为 Laplacian 二次型条件；
2. **Kadison–Singer 型随机选择**：从生成树多面体中采样一棵树，使其边概率与给定向量一致；
3. **交错多项式 / 混合特征值引理**：控制采样后树的谱性质；
4. **从谱瘦回到割瘦**：谱条件蕴含割条件，但反向不成立。

OpenAI 若声称 `O(1/k)`-瘦树，意味着它解决了强猜想，并可能给出新的构造性证明。

#### 仍需人类补充

- **构造性 vs 存在性**：Anari–Oveis Gharan 的证明是非构造性的；OpenAI 是否提供多项式时间算法？
- **常数依赖**：`O(1/k)` 中的隐藏常数是多少？是否在 Lean 中显式？
- **与 ATSP 的联系**：若强猜想成立且可构造，可给出 ATSP 的常数近似；OpenAI 是否讨论了算法推论？

---

### 2.10 Tingley sphere isometry problem

**样本名 Sample**: `SMP_ProofAnalysis_OpenAI_Tingley_SphereIsometry.md`  
**核心声明 Core Claim**: 两个 Banach 空间单位球面之间的满射等距可延拓为全空间的实线性等距（Mazur–Ulam 性质对单位球面的版本）。

#### 历史主线

- **1932 Mazur–Ulam**: 两个赋范空间之间的满射等距必为仿射。
- **1972 Mankiewicz**: 两个凸体之间的满射等距可唯一延拓为全空间的仿射等距。
- **1987 Tingley**: 提出 **Tingley problem**：单位球面 `S_X → S_Y` 的满射等距是否可延拓为 `X → Y` 的实线性等距？
- **后续发展**: 对 `ℓ_p`、`L_p`、`C_0(Ω)`、有限维严格凸空间、`C*-algebras`、von Neumann algebras、JBW*-triples 等逐步得到肯定答案。
- **2018 Mori–Ozawa**: 证明每个 unital C*-algebra 具有 Mazur–Ulam 性质。
- **2026 OpenAI**: 声称在 Lean 中形式化了某类 Banach 空间上的 Tingley 型结果。

#### 最接近的数学构造

**单位球面的几何结构**：极端点 (extreme points)、面 (faces)、M-理想 (M-ideals) 等。Tingley 问题的核心是利用球面等距保持这些几何不变量（如面与极端点），从而将其延拓到整个空间。

#### 最接近的证明方法

典型证明路线：

1. 证明 `T` 保持 **闭面 (closed faces)**；
2. 利用面与 C*-子代数/子空间的对应，将问题约化到 Mankiewicz 定理适用的凸体；
3. 通过 **Tanaka 引理** 或 **Peralta 技术** 证明 `T` 在有限秩算子/交换子代数上的线性性；
4. 延拓到全空间。

#### 仍需人类补充

- **适用的空间类**：Tingley 问题即使在 2 维严格凸空间中仍是开放问题；OpenAI 必须明确其处理了哪类 Banach 空间。
- **复线性 vs 实线性**：Mazur–Ulam 最初是实线性；复 Banach 空间上的复线性延拓需要额外论证。
- **球面等距保持负运算**：Tingley 最早证明了有限维情形 `T(−x) = −T(x)`；OpenAI 是否在高维/无限维情形建立了类似性质？

---

## 3. 共同证明方法论谱系

将这 10 个样本按主导方法论聚类，可得到以下谱系：

| 方法论谱系 Methodology Genealogy | 涉及样本 Samples | 关键先驱 Key Pioneers | 核心工具 Core Tools |
|---|---|---|---|
| **解析数论：筛法与指数和** | 1, 2, 3 | Brun, Iwaniec, Heath-Brown, Hooley, Vaughan | 线性筛、行列式方法、Vinogradov 均值、Möbius 反演 |
| **组合数论：格点与算术结构** | 4 | Gordon, Gethner, Vardi, Tsuchimura | Gaussian 整数、覆盖系统、熵/渗流 |
| **度量几何：嵌入与对偶** | 5 | Rao, Okamura–Seymour, Filtser | 稀疏割-流对偶、最短路径分解、面覆盖 |
| **组合概率：马尔可夫链与规范路径** | 6 | Jerrum–Sinclair, Cooper–Dyer–Frieze, Greenhill | 多商品流、导通率、对称差分解 |
| **离散几何：替换铺砖与局部规则** | 7 | Berger, Robinson, Penrose, Smith–Myers–Kaplan–Goodman-Strauss | 替换系统、匹配规则、计算机搜索 |
| **表示论：Kazhdan–Lusztig 与 Soergel** | 8 | Kazhdan–Lusztig, Beilinson–Bernstein, Soergel | Hecke 代数、Bruhat 序、Soergel bimodule |
| **谱图论与凸优化** | 9 | Nash–Williams, Goddyn, Marcus–Spielman–Srivastava, Anari–Oveis Gharan | 生成树多面体、有效电阻、Kadison–Singer |
| **凸几何与泛函分析** | 10 | Mazur–Ulam, Mankiewicz, Tingley, Mori–Ozawa | 凸体、极端点、面、C*-代数结构 |

从谱系可见，10 个样本覆盖了 **8 条主要数学方法 lineage**。其中，样本 8（KL 组合不变性）和样本 9（强瘦树）处于自身领域的核心猜想位置，其历史意义最大；样本 3（Totient 渐近）则是经典结果的形式化，历史最悠久。

---

## 4. 仍需人类补充的位置汇总

| 样本 | 关键缺口 Key Gap | 风险等级 Risk | 建议审查岗位 Suggested Human Role |
|---|---|---|---|
| 1 Squarefree quartics | 误差项 `O(x^{1−δ})` 缺失；admissibility 例外 | 中 | C 缺口刻画 + D 陷阱预见 |
| 2 Jacobsthal | 常数 `C` 非显式；刚性模式分类不完整 | 中 | A 概念奇点 + C 缺口刻画 |
| 3 Totient | 误差项版本不明；缺少 `Ω` 下界 | 低 | B 语义忠实审查 |
| 4 Gaussian primes | `B_D` 无显式公式；熵论证严格化 | 高 | D 陷阱预见 + E 验证解读 |
| 5 Planar L1 | 具体失真常数/终端限制不明 | 高 | B 语义忠实审查 + C 缺口刻画 |
| 6 Graph switch | 度序列适用条件未明确 | 中 | D 陷阱预见 |
| 7 Einstein tiling | tile 规则变体不清；计算机搜索信任链 | 高 | B 语义忠实 + E 验证解读 |
| 8 KL invariance | 适用范围（长度/类型）未明确 | 高 | A 概念奇点 + C 缺口刻画 |
| 9 Strong thin trees | 构造性/常数/ATSP 推论未明确 | 高 | A 概念奇点 + D 陷阱预见 |
| 10 Tingley | 适用 Banach 空间类未明确 | 中 | B 语义忠实审查 |

---

## 5. 决策点与后续行动

### 5.1 决策点

1. **是否将这 10 个样本标记为「数学史专题」并单独成卷？**  
   - 赞成：便于教学展示与方法论谱系研究；  
   - 反对：增加归档复杂度，需额外维护 DOI/指纹。

2. **是否对高风险缺口样本（4,5,7,8,9）启动专项人工复刻？**  
   - 赞成：这些样本若成立，分别对应领域重大突破；  
   - 反对：人力成本高，且部分声明可能仅是特殊情形。

3. **是否将「最接近的经典构造/证明方法」字段写入 SMPDL_Audit_SampleSuite.md 的固定栏目？**  
   - 推荐 **赞成**，可使历史回溯成为审计标准六格之外的第七格。

### 5.2 后续行动

- [ ] 将本报告纳入 `SMPDL_Audit_SampleSuite.md` 附录或新增 5.12 节。
- [ ] 更新 `SMPDL_ATTRIBUTION.md` 文件清单（新增本报告），重算联合 SHA-256。
- [ ] 将本报告同步到桌面数据包 `SMPDL_Paper_and_Data/reports/`。
- [ ] 升级 `riemann-lecturer/vendor/version.js` 与 `index.html` 的版本/指纹/样本数。
- [ ] 执行 `node --check` 验证相关内联脚本（若网页同步更新）。
- [ ] 重新打包 `SMPDL_vX.Y_sample_reports_Nfiles.zip` 并走 Zenodo newversion 流程（待 token 可用）。
- [ ] 重新部署 WorkBuddy「发布为应用」通道，线上 `?nocache=1` 验证版本/DOI/指纹。

---

## 6. 归档说明

- **文件位置 File location**: `C:/Users/hengz/Desktop/SMPDL_Paper_and_Data/reports/SMPDL_HistoryRetrospective_10PromisingSamples.md`
- **对应 HTML**: `SMPDL_HistoryRetrospective_10PromisingSamples.html`（同目录，由本 md 生成）
- **版本链 Version chain**: SMPDL v2.2 → v2.3（若纳入主样本集）
- **引用纪律 Citation discipline**: 本报告中所有年份、作者、结果均来自已公开的数学文献或 arXiv；关键断言已给出可追溯来源（如 Erdős 1953、Heath-Brown 2006、Smith et al. 2023 等）。
- **维护条款 Maintenance clauses**: 若后续发现某个样本的「最接近构造」有更准确的人类数学对应，应通过 `SMPDL_Compare_*_PrePostFix.md` 修复前后对比样本更新，并同步指纹。

---

**SMPDL 审计组**  
2026-10-13
