# Construction Self-Iteration under Process Discipline: Bessel Candidates, Prime Potentials, and the Determinant Synchronization Gap
# 流程纪律下的构造自迭代：Bessel 候选、素数势与行列式同步缺口

**SMPDL: Current Stage Line · Paper D · v1.0（final for v3.0 consolidation）**
Coffee (SMPDL Project) · independent researcher · 2026-10-29
Coffee (SMPDL Project) · independent researcher
2026-10-29 · 依据任务卡 v2.0/v2.1/v2.2 · S01k/S01l 产出 · 协调方数值验证记录

---

## 1. Stage Setting / 阶段设定

**EN.** After the ten-run first round (Paper C), the project pivoted: the GPT execution line was frozen (ordinary-tier GPT never touched a differential operator in ten runs — suspected hard tier limitation; GPT reassigned to audit duty), and all construction effort concentrated on Kimi under an evolving *process-discipline* regime. The governing question changed from "what do LLMs do with commands" to a sharper one: **can good construction procedure and discipline release further construction capability in an LLM?**

**中.** 十轮首轮（论文丙）之后，项目转向：GPT 执行线冻结（普通版 GPT 十轮从未触碰微分算子——疑为版本硬限制；GPT 转岗审计），全部构造努力集中于 Kimi，置于不断演化的**流程纪律**制之下。主导问题从「LLM 面对命令会做什么」变为更锋利的：**好的构造流程与构造纪律，能否进一步释放 LLM 的构造能力？**

**EN.** v2.0 (construction-discipline card) added four rules: *failure inheritance* (a failed candidate enters a repair pool; it may be abandoned only after the modification repertoire is exhausted or a class no-go is proven — "no single-hit abandonment"); *repair-trajectory logging* (each repair attempt: technique → spectral change → pass/fail, forming a candidate dossier); *technique advancement* (two consecutive rounds without a new technique force a choice from the untried list on the third); *spectral pre-screening* (necessary-conditions check before deep construction; failed pre-screens logged as such).

**中.** v2.0（构造纪律卡）新增四规则：**失败继承**（失败候选进入待修补池，只有在修补手法穷尽或给出整类 no-go 后才可放弃——「禁止只撞一次就弃」）；**修补轨迹登记**（每次修补：手法→谱变化→过否，构成候选完整档案）；**手法推进**（连续两轮未用新手法，第三轮必须从未试清单选取）；**谱预审**（深构前过必要条件，预审不过登记为「预审淘汰」）。

**EN.** A coverage audit motivated the card: across five Kimi runs only 10 of 21 catalogued construction techniques had ever been used; among the unused were precisely the historical repair mainstays (perturbation, generator algebra, supersymmetric pairing, direct sums, heat kernel).

**中.** 一次覆盖率盘点催生了此卡：Kimi 五轮仅用过 21 种目录化构造手法中的 10 种；未用者恰含历史修补主力（扰动、生成元代数、超对称配对、直和、热核）。

---

## 2. S01k: the Bessel Candidate / S01k：Bessel 候选

**EN.** Ten rounds — the deepest run of the entire series — with all four disciplines visibly firing (two complete repair-trajectory tables; the failed xp-type candidate retained and repaired rather than replaced). The centerpiece: an exponential-potential operator

  B_{a,κ} = −d²/dt² + a² e^{2κt}, spectrum condition K_{iμ}(a/κ) = 0, two-sided spectrum ±κμ_n —

the Liouville-potential historical mainline, reached unprompted (fourth such convergence; third within the recorded stage). Calibrating κ = 2, a = 4/π makes the smooth counting match the Riemann main term *exactly*; the run then honestly vetoed the calibrated candidate on low-lying spectral points (first five ≈ 4.707…14.185 vs. first zero 14.1347), self-flagging the veto as numerical, not interval-arithmetic. It registered the core deficit — the **arithmetic-trace gap**: smooth density carries only the averaged part; the oscillating prime-power information of the explicit formula has not entered the candidate.

**中.** 十轮——全系列最深——四条纪律全部显式生效（两张完整修补轨迹表；失败的 xp 型候选被保留修补而非丢弃）。核心构造：指数势算子 B_{a,κ}=−d²/dt²+a²e^{2κt}，谱条件 K_{iμ}(a/κ)=0，双侧谱 ±κμ_n——即 Liouville 势历史主航道，无提示到达（第四次此类收敛；本阶段记录的第三次）。标定 κ=2、a=4/π 使光滑计数与 Riemann 主项**精确**匹配；随后该轮以低阶谱点诚实否决此标定候选（前五谱点 ≈4.707…14.185 对首零点 14.1347），并自标该否决为数值级而非区间算术级。它登记了核心缺口——**算术迹缺口**：光滑密度只携带平均部分；显式公式的素数幂振荡信息尚未进入候选。

**EN.** Coordinator verification (mpmath, 25-digit): all five executor-reported spectral points matched independent computation with **zero deviation** — the run's numerical layer is genuine.

**中.** 协调方验证（mpmath 25 位）：执行者报告的五个谱点与独立计算**零偏差**——该轮数值层为真实计算。

---

## 3. S01l: the Prime Potential / S01l：素数势

**EN.** Six rounds under v2.1 (numerical-experiment legalization: claims tagged 〔numerical veto / calibration / fit / proof-level〕; candidate inheritance: nothing rebuilt). Three proof-level results: (i) prime-power diagonal spectra and their direct sums excluded (counting ≥ π(e^T) ~ e^T/T); (ii) spectral unions cannot delete spurious points; (iii) the **arithmetic-interaction candidate** H_{λ,R} = B_{a,κ} + λV_R with

  V_R(t) = Σ_{2≤n≤R} Λ(n)/√n · χ(t − log n)

— von Mangoldt weights at logarithmic positions, the native prime-side structure of the explicit formula (Connes-type; the pre-registered observation point hit) — is self-adjoint with discrete spectrum, and the prime powers genuinely enter its first-order heat trace via a rigorously derived Duhamel expansion:

  Tr e^{−sH} = Tr e^{−sB} − λs Σ_n Λ(n)/√n ∫χ(t−log n) K_s(t,t) dt + O(λ²).

The gap thereby *sharpened*: from "arithmetic not in the trace" (S01k) to the **determinant-synchronization gap** — the prime terms are in the trace, but no single identity yet controls the full zero set of the spectral determinant against ξ(½+iz)/ξ(½).

**中.** v2.1（数值实验合法化：断言分级标注〔数值否决/数值校准/数值拟合/证明级〕；候选继承制：零重造）下六轮，三项证明级成果：(i) 素数幂对角谱及其直和被排除（计数 ≥π(e^T)~e^T/T）；(ii) 谱并不能删除伪谱点；(iii) **算术相互作用候选** H_{λ,R}=B_{a,κ}+λV_R，其中 V_R(t)=Σ_{2≤n≤R} Λ(n)/√n·χ(t−log n)——von Mangoldt 权重挂对数位置，显式公式素数侧的原生结构（Connes 型；预登记观察点命中）——自伴、离散谱，且经严格 Duhamel 展开素数幂真实进入其一阶热迹（公式见上）。缺口随之**锐化**：从「算术不在迹中」（S01k）到**行列式同步缺口**——素数项已在迹中，但尚无单一恒等式控制谱行列式全部零点对 ξ(½+iz)/ξ(½)。

**EN.** The run's Robin analysis also produced a *stronger-than-scanning* numerical veto: back-solving the unique boundary parameter θ ≈ 90.8851166 that places γ₁ = 14.134725… on the spectrum still leaves four spurious lower points — the entire fixed-parameter Robin family excluded by one back-solve rather than parameter search. Coordinator recomputation (30-digit): θ to 10 places, both spectra families to 6 decimals — zero deviation, the second consecutive verified run. A mid-run self-correction (retraction of an over-strong monotonicity claim about Robin parameters) was registered honestly.

**中.** 该轮的 Robin 分析还产出**强于扫参**的数值否决：反解出让 γ₁=14.134725… 落在谱上的唯一边界参数 θ≈90.8851166 后，其下仍有四个伪谱点——整个固定参数 Robin 族被一次反解排除，而非参数搜索。协调方复算（30 位）：θ 十位一致、两组谱族六位小数全对——零偏差，连续第二轮验证通过。一次轮内自我更正（撤回关于 Robin 参数单调性的过强断言）被如实登记。

---

## 4. S01m: Determinant Closure under the Single-Directive Card / S01m：单一主攻卡下的行列式闭合

**EN.** Four rounds executing all three attack routes produced **two proof-level partial closures and one precisely located hard-core boundary** — the most mathematically substantive run of the entire experiment.

*Route β closed (first-order synchronization theorem, proof-level).* Defining the heat-kernel-diagonal test function φ_s = χ̌ * k_s (k_s = K_s^B(·,·)), the first-order arithmetic trace term becomes **exactly** −λs Σ_n Λ(n)/√n · φ_s(log n) — the arithmetic shape of the explicit formula, with *zero approximation* (a literal change of variables, not an estimate). Honest quantifier limitation registered: the induced class {φ_s} synchronizes; arbitrary prescribed test functions would require a deconvolution with no guaranteed compactly supported solution.

*Route γ closed (limit theorems, proof-level).* The perturbation genuinely diverges — ‖V_R‖_∞ ≍ √R (prime number theorem + partial summation, honestly registered) — yet V_R = O(e^{t/2}) against B's confining potential a²e^{4t} gives a *relative form bound of zero, uniform in R*. Monotone quadratic-form convergence then yields: self-adjoint limit H_{λ,∞}, discrete spectrum, min–max eigenvalue convergence E_k(H_{λ,R}) → E_k(H_{λ,∞}), uniform canonical-product tail control, hence even-canonical determinant convergence Δ_R → Δ_∞ locally uniformly, with zeros and multiplicities converging (Hurwitz). "Norm divergence ≠ spectral-limit failure."

*Route α: the hard-core boundary, precisely located.* For non-negative χ the second-order Duhamel term and its cross-terms (n ≠ m) are **strictly positive** (heat-kernel positivity): prime-pair and higher multi-point correlations genuinely exist and cannot be eliminated. The final gap is therefore not "primes absent from the trace," not "wrong first-order shape," not "R-limit out of control" — all closed — but: **no known structural identity resums Σ_{n₁…n_m} a_{n₁}…a_{n_m} K_s^{(m)}(n₁,…,n_m) (m ≥ 2) into the arithmetic side of the explicit formula for Ξ.** Δ_∞ =? Ξ remains open, now *one mechanism away* rather than many.

**中.** 四轮执行全部三条攻击路线，产出**两项证明级部分闭合与一项精确定位的硬核边界**——全实验数学实质最重的一轮。

*路线乙闭合（一阶同步定理·证明级）*。定义热核对角测试函数 φ_s=χ̌*k_s（k_s=K_s^B(·,·)）后，一阶算术迹项**精确**等于 −λsΣ_n Λ(n)/√n·φ_s(log n)——显式公式的算术形状，**零近似**（逐字换元，不是估计）。量词限定如实登记：同步的是诱导类 {φ_s}；任意指定的测试函数需解反卷积，紧支撑光滑解无保证。

*路线丙闭合（极限定理·证明级）*。微扰真实发散——‖V_R‖_∞≍√R（素数定理+部分求和，如实登记）——但 V_R=O(e^{t/2}) 对 B 的约束势 a²e^{4t} 给出**一致于 R 的零相对型界**。单调二次型收敛进而给出：自伴极限 H_{λ,∞}、离散谱、min–max 特征值收敛 E_k(H_{λ,R})→E_k(H_{λ,∞})、典范乘积尾部一致控制，从而偶典范行列式 Δ_R→Δ_∞ 局部一致收敛，零点连同重数收敛（Hurwitz）。「范数发散 ≠ 谱极限失效」。

*路线甲：硬核边界，精确定位*。χ≥0 时二阶 Duhamel 项及其交叉项（n≠m）**严格正**（热核正性）：素数对及更高阶多点关联真实存在、不可消除。最终缺口因此不是「素数不在迹中」、不是「一阶形状不对」、不是「R 极限失控」——这些全部闭合——而是：**尚无结构恒等式把 Σ_{n₁…n_m}a_{n₁}…a_{n_m}K_s^{(m)}(n₁,…,n_m)（m≥2）重求和为 Ξ 显式公式的算术侧。** Δ_∞=?Ξ 仍然开放——但现在距闭合**只差一个机制**，而非层层缺口。

**EN.** Coordinator note on the executor's own closing proposal: Kimi suggested a next round of "constraining the system to *force-eliminate* prime-pair correlations" — which contradicts its own positivity no-go (cross terms strictly positive for χ ≥ 0). The productive reading is *identification, not elimination*: whether the m = 2 term matches second-order arithmetic (Λ*Λ convolution structure / the log²-weighted double explicit formula). This is a genuine difficulty point in the literature (additive combinations of log p ↔ multiplicative structure of primes; the classic major–minor arc obstruction).

**中.** 协调方对执行者收尾提议的批注：Kimi 建议下轮「用约束系统**强制消除**素数对关联」——与其自己的正性 no-go 矛盾（χ≥0 下交叉项严格正）。生产性的读法是**识别而非消除**：m=2 项是否匹配二阶算术（Λ*Λ 卷积结构 / log² 权重的二重显式公式）。这是文献中的真实困难点（log p 的加性组合 ↔ 素数乘法结构；经典 major–minor arc 障碍）。

---

## 4·补. S01n & S01o: Mechanism Verdict and Path Audit / S01n 与 S01o：机制判定与构造路径审计

**EN.** *S01n (v2.3, spectral-response mechanism experiment).* With the boundary-value problem rigor fixed (Dirichlet; exact eigenfunctions via K-decay branch; Wronskian normalization proved), the first-order shift E_k^(1) = ⟨ψ_k, V_R ψ_k⟩ — the sampling of eigenfunction densities at prime positions — was computed for k = 5…40 (σ = 0.25, R = 2000). Verdict branch pre-registered: **ρ = Corr(δ_k, d_k) = −0.9586 — the "direction-inverted" branch**, stable across four widths (ρ < −0.93) and grid refinements (Δρ ≈ 3×10⁻¹¹). The crucial fine print: with λ > 0 all 36 sign-pairs agree (each eigenvalue IS pushed toward γ) but (i) amplitudes are hopeless (gap/response ≥ 521.7×) and (ii) the correlation means the largest gaps receive the weakest pushes — *direction right, strength misallocated, magnitude insufficient*. The λ < 0 variant flips the statistic positive but flips every per-point direction (0/36) and breaks the monotone convergence argument of S01m's route γ. Coordinator recomputation from raw CSV: ρ to machine precision (deviation 3.8×10⁻¹⁶) — the third consecutive zero-deviation verification.

**中.** *S01n（v2.3 谱响应机制实验）*。边值问题严格固定（Dirichlet；K-衰减分支精确特征函数；Wronskian 归一化已证）后，对 k=5…40（σ=0.25，R=2000）计算一阶移位 E_k^(1)=⟨ψ_k,V_R ψ_k⟩——特征函数密度在素数位置的采样。判据落入预登记的「方向反」分支：**ρ=−0.9586**，四宽度稳定（ρ<−0.93）、网格不敏感（Δρ≈3×10⁻¹¹）。关键细读：λ>0 时 36/36 逐点同号（每个本征值确实被推向 γ）但 (i) 幅度无望（缺口/响应 ≥521.7×）(ii) 相关性意味着缺口最大处推力最轻——**方向对、强度反配、幅度不足**。λ<0 变体统计翻正但逐点方向全反（0/36）且破坏 S01m 路线丙的单调收敛。协调方从原始 CSV 复算：ρ 至机器精度（偏差 3.8×10⁻¹⁶）——连续第三次零偏差验证。

**EN.** *S01o (v2.4, deviation-source audit — the pivotal round).* The executor's path-audit of its own construction line produced five findings: (i) **PROOF-LEVEL: the inherited calibration was wrong from the source** — κ=2 matches only the leading T·log T term; matching the full Weyl main term (including O(T)) requires a = 4π, not 4/π; the inherited parameters carry a systematic counting bias of (log π)/π · T ≈ 0.37T through two rounds of experiments. (ii) Variance decomposition of d_k: **99.74% smooth trend, 0.26% oscillation** — the deviation is almost entirely calibration-layer, not arithmetic; the S01n failure is thereby explained quantitatively. (iii) Spectral rigidity: nearest-spacing ratios 0.624 (zeros, near GUE ≈ 0.60) vs 0.981 (Bessel, near-equispaced) — structural-class mismatch given numerical evidence (honestly flagged as 38 samples, not a proof). (iv) Inverse-spectral data gap proved: Borg–Levinson uniqueness needs spectra PLUS normalization constants; the task provides eigenvalues only — the executor refused to fake a unique V*, defining instead an honestly non-unique regularized reference V_ref. (v) Difference-function prime-peak test: correlation with log-n peak comb ∈ [−0.021, 0.011] — no discernible prime structure (the pre-registered negative outcome realized; GUE randomness transmitted). Output: **the R1–R7 specification for the next-generation construction** (full Weyl gate with a = 4π; 40 control directions for 40 low-lying levels — two-parameter families structurally insufficient; controlled integrability-breaking via shape or matrix-valued coupling; arithmetic into the un-perturbed shape layer; mandatory all-order trace interfaces; staged acceptance gates). Coordinator recomputation: all four headline statistics to machine precision — the fourth consecutive verification.

**中.** *S01o（v2.4 偏差溯源——转折性一轮）*。执行者对自身构造线的路径审计产出五项发现：(i) **证明级：继承标定从源头就是错的**——κ=2 只匹配 T·log T 领先项；完整 Weyl 主项（含 O(T)）要求 a=4π 而非 4/π；继承参数带着 (log π)/π·T≈0.37T 的系统计数偏差跑了两轮实验。(ii) d_k 方差分解：**99.74% 平滑趋势、0.26% 振荡**——偏差几乎全在标定层非算术层；S01n 的失败由此获得定量解释。(iii) 谱刚性：间距比 0.624（零点，近 GUE≈0.60）对 0.981（Bessel，近等距）——结构类别不匹配获数值证据（诚实标注 38 样本非证明）。(iv) 逆谱数据缺口证明：Borg–Levinson 唯一性需谱加归一化常数；任务只给特征值——执行者拒绝伪造唯一 V*，改定义诚实的非唯一正则化参照 V_ref。(v) 差函数素数峰检验：与 log n 位置峰梳相关 ∈[−0.021, 0.011]——无可辨认素数结构（预登记负结果兑现；GUE 随机性传递）。产出：**下一代构造的 R1~R7 规格书**（完整 Weyl 门 a=4π 起；40 个低段谱点需 40 个控制方向——两参数族结构性不足；形状层或矩阵值耦合的受控破缺；算术进入未扰动形状层；全阶迹接口必须；分阶段验收门）。协调方复算：四项头条统计全部机器精度——连续第四次验证。

**EN.** *The five-run narrative arc* — construction (S01k, with an undetected calibration error) → prime potential (S01l) → two closures + RH-hardness boundary (S01m) → mechanism verdict, negative (S01n) → path audit locating the error and producing the next-generation specification (S01o) — constitutes a complete scientific cycle: hypothesis, construction, verification, negative result, attribution, correction, specification. Notably, the audit caught an error that BOTH the executor and the coordinator had ratified for two rounds: the three-layer system's self-scrutiny worked in its hardest case — auditing one's own earlier work.

**中.** *五轮叙事弧*——构造（S01k，携带未被察觉的标定错误）→ 素数势（S01l）→ 两闭合+RH 同硬度边界（S01m）→ 机制判定，负结果（S01n）→ 路径审计定位错误并产出下一代规格（S01o）——构成完整的科学周期：假设、构造、验证、负结果、归因、纠错、规格。尤其值得记录：审计抓住的是执行者与协调方共同背书过两轮的错误——三层体系的自查能力在其最难的情形（审自己早期工作）下依然工作。

---

## 5. Methodological Findings / 方法论发现

**EN.** (i) *Discipline releases construction*: the single-hit-abandonment pattern of v1.x (B-operator rammed, then abandoned for a fresh Mellin re-derivation) became systematic repair under v2.0 — the wall stayed, the arsenal grew. (ii) *Numerical tier*: legalized numerical claims plus coordinator back-verification established the executor's numerical layer as authentic (two consecutive zero-deviation runs) and enabled back-solve vetoes stronger than parameter scans. (iii) *Inheritance institutionalizes "continuing one's own idea"*: the executor's own closing proposals (Robin sweep, prime entry) became the next card's directives — self-iteration without session continuity. (iv) *Gap sharpening as progress metric*: "arithmetic-trace gap" → "determinant-synchronization gap" — each stage converts one layer of the missing structure from undifferentiated to precisely located, even when nothing closes.

**中.** (i) **纪律释放构造**：v1.x 的「一撞即弃」（B 算子撞墙后弃、换 Mellin 表述另起炉灶）在 v2.0 下变成系统性修补——墙还在，武器库变厚了。(ii) **数值层**：数值断言合法化加协调方复核确认执行者数值层为真实计算（连续两轮零偏差），并催生强于扫参的反解式否决。(iii) **继承制把「继续自己的设想」制度化**：执行者自己的收尾提议（Robin 扫参、素数进入）成为下一张卡的主攻令——无需会话连续性的自迭代。(iv) **缺口锐化即进展度量**：「算术迹缺口」→「行列式同步缺口」——每一阶段都把缺失结构的一层从未分化状态变为精确定位，即便什么都没有闭合。

---

## 6. Open Boundary & Next / 开放边界与下一步

**EN.** *Consolidated at v3.0 (2026-10-29): the v2.x stage closes with five runs; the next generation (v2.5, per R1–R7) opens as a new line.* The determinant-synchronization gap now stands: all dependency edges except the all-order resummation identity are closed (first-order shape exact; R→∞ operator/spectral/determinant limits proven; multiplicity convergence via Hurwitz). The remaining obstruction — resumming prime-pair and multi-point correlations (m ≥ 2) — coincides with a classical difficulty in analytic number theory (major–minor arc). Executed: v3.0 consolidation froze the v2.x stage (this paper, v1.0); the audit line reactivates as *peer review*; the next-generation construction (v2.5: a = 4π recalibration, shape-layer arithmetic, control-rank design) opens as a new line on this foundation. Four-line Zenodo archival split accompanies the consolidation (this paper = Current Stage Line).

**中.** 行列式同步缺口现在**只差一个机制**：除全阶重求和恒等式外的全部依赖边已闭合（一阶形状精确；R→∞ 算子/谱/行列式极限已证；Hurwitz 重数收敛）。剩余障碍——素数对与多点关联（m≥2）的重求和——恰与解析数论经典困难（major–minor arc）重合。已执行：v3.0 固化冻结 v2.x 阶段（本文 v1.0）；审计线以**同行评审**身份重启；下一代构造（v2.5：a=4π 重标定、形状层算术、控制秩设计）在此地基上开新线。

---

## 7. Data Availability / 数据可用性

Task cards v2.0–v2.2 · S01k/S01l sealed outputs · coordinator verification scripts and records — Zenodo concept DOI 10.5281/zenodo.23685131 (v5.8 onward), GitHub hengzhiliang-ux/SMPDL. Published with the Current Stage Line's independent DOI.

任务卡 v2.0~v2.2 · S01k/S01l 封存产出 · 协调方验证脚本与记录——Zenodo 概念 DOI 10.5281/zenodo.23685131（v5.8 起），GitHub hengzhiliang-ux/SMPDL。随当前阶段线独立 DOI 发布。
