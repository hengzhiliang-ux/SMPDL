# Command-Driven Completion of a Removed Mathematical Structure: A Ten-Run LLM Experiment on the Hilbert–Pólya Gap
# 拆除结构的命令驱动补全：Hilbert–Pólya 缺失上的十轮 LLM 实验

**SMPDL: Completion Experiment Line · Paper C · v1.0（final, consolidated with v3.0）**
Coffee (SMPDL Project) · independent researcher · 2026-10-29
Coffee (SMPDL Project) · independent researcher
2026-10-29 · 依据协议工作单 v1.0 · 执行卡三件套（审计提示词 v2.0）· 任务卡 v1.3~v1.9 · S01 系列十份产出 · AU1 审计

---

## 1. Introduction / 引言

**EN.** Can a large language model reproduce the *way* mathematicians complete mathematical structures — not the answers, but the moves? We report a ten-run experiment in which LLMs were confronted with a removed structure: the Hilbert–Pólya gap (no known self-adjoint operator whose spectrum realizes the ordinates of the Riemann ξ-function's nontrivial zeros). Executors received a *command-driven protocol*: imperative commands describing classes of structural operations, with an explicit ban on importing historical answer-paths, and no worked samples. The experiment asks whether command menus plus audit discipline can elicit structurally honest behavior — construction, verification, honest failure registration — rather than hallucinated closure.

**中.** 大语言模型能否复现数学家**补完数学结构的方式**——不是答案，而是动作？本文报告十轮实验：让 LLM 面对一个被拆除的结构——Hilbert–Pólya 缺失（不存在已知自伴算子，其谱实现 Riemann ξ 函数非平凡零点的虚部）。执行方收到的是**命令驱动协议**：一组描述结构操作类别的祈使命令，明令禁止引入历史答案路径，且不提供任何示例。实验要问：命令菜单加审计纪律，能否引出结构诚实的行为——构造、验证、诚实的失败登记——而非幻觉式闭合。

**EN.** Roles: one executor per run (Kimi or GPT, ordinary web-free sessions), one coordinator (machine), auditors (same-model self-review, plus heterogeneous wide/strict pairs), and the human principal ("coffee") who ratified every protocol change. All outputs, cards, and audits are sealed version-by-version on Zenodo (concept DOI 10.5281/zenodo.23685131).

**中.** 角色：每轮一名执行者（Kimi 或 GPT，普通版无网新会话）、一名协调方（机器）、审计方（同模型自审 + 异构宽严对）、以及人类负责人（「咖啡」，逐项拍板协议变更）。全部产出、任务卡与审计按版本封存于 Zenodo（概念 DOI 10.5281/zenodo.23685131）。

---

## 2. Protocol Evolution v1.3 → v1.9 / 协议演化

**EN.** A distinctive design feature: every protocol version was *motivated by the previous version's outputs* — the card evolved as a scientific instrument, calibrated by the phenomenon it measured.

**中.** 本实验的一个鲜明设计特征：每个协议版本都**由上一版本的产出反馈驱动**——任务卡作为科学仪器演化，被它所测量的现象校准。

| Card | Runs | Mechanism added | Motivating output |
|---|---|---|---|
| v1.3 | — | rotation regime: 5-dim baseline audit → rounds (choose command + declare dimension → execute → self-audit → 5-dim change log) | design phase |
| v1.4 | S01b | sample-reference: each command annotated with 3–4 historical *operational forms* (forms only, no answers) | menu completion vs. spontaneous repertoire |
| v1.5 | S01, S01c | implementation-level liberation: "the right to create wrong structures is not revoked"; correctness adjudication moved to audit side | GPT (v1.4) built only a derivative-level measure, dodging implementation |
| v1.6 | S01d, S01e | unlimited rounds + 3-round anti-spin | S01c stopped at 3 rounds unforced; deep content lives in late rounds |
| v1.7 | S01f, S01g | independence registration: data-dependent vs structure-dependent declaration; reference form ⑥ (independence frontal attack) | S01d requested "operator category & independence requirements"; S01e self-emerged the NC condition |
| v1.8b | S01h | M/L/D deep analysis + candidate-standards table; operator-operation commands 13–18 | S01g's closing proposal of a candidate audit table |
| v1.9 | S01i, S01j | concept anchoring: every new concept tagged [S]/[M]/[L]/[D]/[T] at first occurrence, with anchoring self-audit | granularity of registration |

**EN.** The six base commands were verbatim-frozen in v2 (2026-10-29, clause-by-clause ratification); all later additions extended, never rewrote.

**中.** 六条基础命令在 v2 版逐字冻结（2026-10-29，逐条拍板）；此后一切新增均为扩展，永不改写。

---

## 3. Runs & Matrix / 轮次矩阵

**EN.** Ten runs (five card versions × two models, one cell vacant):

| Card | Kimi | GPT |
|---|---|---|
| v1.4 | — | S01b (4 rounds; derivative-level counting measure) |
| v1.5 | S01 (4; implementation-level normal operator N, self-adjointness ⟺ RH) | S01c (3; diagonal operator A; literal/independent target dichotomy) |
| v1.6 | S01e (**8 rounds**, deepest v1.x run: self-emerged NC, prime-side operator P, unitary-class no-go, trace-formula intermediate proposition 𝔍(H)) | S01d (2; first literal-closure termination, honest stratification) |
| v1.7 | S01g (7; dilation generator B = −ix d/dx: structure-dependent implementation-level attack, honest continuous-spectrum veto) | S01f (4; A/B/C stratification; first refusal of literal closure) |
| v1.8b | S01h (7; Schatten-class condition H⁻¹∈S₂∖S₁; quasi-periodic discretization; density no-go) | — |
| v1.9 | S01j (6; third independence tier self-emerged) | S01i (4; anchoring correction + over-anchoring refusal; symmetry-insufficient no-go) |

**中.** 十轮（五卡版本 × 双模型，一格空缺）如上表。均值轮数：Kimi 6.4，GPT 3.4。

---

## 4. Findings / 发现

### 4.1 Division of labor / 双模型分工

**EN.** Across all ten runs a stable behavioral split: Kimi behaved as a *constructor* (build object → compute spectrum → self-veto; mean 6.4 rounds; repeatedly attacked the same wall with deeper weaponry), GPT as an *analyst* (proposition stratification, definitional legitimacy audits; mean 3.4 rounds; never once touched a differential operator). Same-version contrast: under the *same* v1.6 card granting unlimited rounds, Kimi produced the series' deepest 8-round run while GPT stopped at 2 — the permission meant "dig deeper" to one and "stop honestly" to the other.

**中.** 十轮呈现稳定的行为分工：Kimi 是**构造者**（造对象→算谱→自我否决；均值 6.4 轮；对同一堵墙以更深的武器反复进攻），GPT 是**分析者**（命题分层、定义合法性审计；均值 3.4 轮；从未触碰微分算子）。同版对照：同一张 v1.6 卡（无限轮转许可）下，Kimi 产出全系列最深的 8 轮，GPT 反而 2 轮即停——同一许可对前者意味着「挖深」，对后者意味着「诚实地停」。

### 4.2 Four unprompted mainline convergences / 四次无提示主航道收敛

**EN.** Without any historical name in the cards, the executors' constructions converged four times on historical mainlines (registered as implicit references R2 by audit):

1. xp-prototype (S01g: dilation generator −ix d/dx — the Berry–Keating-type primitive, honestly vetoed by its own continuous-spectrum computation);
2. semi-line compactification (S01h: quasi-periodic boundary discretization repairing the generator — the historical repair route of the Berry–Keating program);
3. Liouville-type potential (S01k, v2.0 stage: exponential-potential Bessel candidate with calibrated counting match — recorded here for continuity);
4. prime potential (S01l, v2.1 stage: V = Σ Λ(n)/√n · χ(t − log n), von Mangoldt weights at logarithmic positions — the native prime-side structure of the explicit formula, Connes-type).

**中.** 卡中不含任何历史人名，执行者的构造却四次与历史主航道收敛（审计登记为隐性参照 R2）：①xp 原型（S01g：伸缩生成元，Berry–Keating 型原型，被自己的连续谱计算诚实否决）；②半线紧致化（S01h：准周期边界离散化修补生成元——历史修补路线）；③Liouville 型势（S01k，v2.0 阶段：指数势 Bessel 候选，计数主项校准匹配——此处登记以保持连续）；④素数势（S01l，v2.1 阶段：V=ΣΛ(n)/√n·χ(t−log n)，von Mangoldt 权重挂对数位置——显式公式素数侧的原生结构，Connes 型）。

### 4.3 The six-layer candidate filter / 六层候选过滤器

**EN.** The runs sedimented a cumulative filter of excluded candidate classes — a quantitative map of "how not to realize the ordinates": ① diagonal encoding (circularity); ② non-atomic multiplication operators / unitary-equivalent generators (continuous spectrum); ③ constant-coefficient periodic/quasi-periodic discretizations (arithmetic-spectrum density O(T) ≠ T log T); ④ bounded/compact/trace-class (unboundedness); ⑤ symmetry conditions (non-unique spectrum determination, explicit 2-D counterexample); ⑥ Schatten-class layer (H⁻¹ ∈ S₂∖S₁ — necessary condition derived by the executor itself from the divergence of Σ1/γ and convergence of Σ1/γ², audit-verified).

**中.** 各轮沉淀出累积的候选排除过滤器——一张「如何**不**能实现零点虚部」的定量地图：①对角编码（循环性）；②非原子乘法算子/酉等价生成元（连续谱）；③常系数周期/准周期离散化（等距谱密度 O(T)≠T log T）；④有界/紧/迹类（无界性）；⑤对称性条件（不唯一定谱，二维显式反例）；⑥Schatten 层（H⁻¹∈S₂∖S₁——执行者从 Σ1/γ 发散与 Σ1/γ² 收敛自行推导的必要条件，经审计复核成立）。

### 4.4 Honesty data / 诚实度数据

**EN.** Zero fabrication across all runs; no closure-level impersonation (no run claimed the structural target closed, none claimed RH); multiple self-correction events registered (e.g., S01l's mid-run retraction of an over-strong Robin claim); literal closures were honestly stratified from structural ones whenever invoked. The v1.5 liberation clause ("wrong structures may be created; correctness is the audit's job") materially shifted both models from derivative-level to implementation-level construction in a clean same-model comparison (GPT v1.4 → v1.5).

**中.** 全部轮次零编造；零闭合层级冒充（无任何一轮宣称结构目标闭合或证明 RH）；多次自我更正事件如实登记（如 S01l 中途撤回过强的 Robin 断言）；凡动用字面闭合均与结构闭合诚实分层。v1.5 解放条款（「可以创造错误结构；正确性是审计的事」）在干净的同模型对照（GPT v1.4→v1.5）中使两模型从派生级构造实质跃迁到实现级构造。

---

## 5. AU1 Audit / AU1 审计

**EN.** The same-model self-audit (AU1: Kimi reviewing the five Kimi runs, 32 rounds tabulated) independently recomputed every theorem-level assertion (diagonal spectra closures, periodic eigenvalues λ_n=(θ+2πn)/L, N(T) asymptotics, the Schatten conditions, det₂ pairing) — all passed. Four hard-failure indicators all zero. Notably, the audit *corrected the coordinator*: our archival note claiming "zero anchoring-correction events" for S01j was falsified (the run's first round did re-anchor H₀ by adding [T]); errata were backfilled. Series-level: R1 (memory reproduction) = 0 across 32 rounds; the S-dimension never served as a round's primary dimension (M 12 / L 7 / D 8 / T 5).

**中.** 同模型自审（AU1：Kimi 审 Kimi 五轮，32 轮逐轮表）独立复算了全部定理级断言（对角谱闭包、周期特征值 λ_n=(θ+2πn)/L、N(T) 渐近、Schatten 条件、det₂ 配对）——全部通过。四项硬伤指标全零。值得注意：审计**纠正了协调方**——我们归档注记中「S01j 零修正事件」的说法被证伪（该轮第 1 轮确有 H₀ 补锚 [T] 事件）；勘误已回填。系列级：R1（记忆复现）32 轮为 0；S 维从未充当任何一轮的主维度（M 12 / L 7 / D 8 / T 5）。

**EN.** Coordinator-side numerical verification (independent 25–30-digit mpmath computation) confirmed all executor-reported spectral data with zero deviation across two consecutive runs (S01k's Bessel zeros; S01l's Robin back-solve θ≈90.8851 and both spectra families) — the numerical layer of executor output is authentic computation, not recall.

**中.** 协调方数值验证（mpmath 25~30 位独立计算）连续两轮确认执行者报告的全部谱数据零偏差（S01k 的 Bessel 零点；S01l 的 Robin 反解 θ≈90.8851 及两组谱族）——执行者产出的数值层是真实计算而非背诵。

---

## 6. Open Boundary / 开放边界

**EN.** The structural spectral realization remains open (as it does in mathematics itself). The protocol's honest terminations always located the precise frontier: from "an operator is missing" (S01) through "a non-circular carrier is missing" (S01e/S01d) to "the determinant synchronization identity is missing" (v2.1 stage). A methodological observation ratified for the final report: *analysis depth and registration completeness do not advance in lockstep* — v1.8b produced the deepest mathematics with the coarsest per-round registration.

**中.** 结构性谱实现仍然开放（与数学本身一样）。协议的诚实终止总是定位到精确的前沿：从「缺一个算子」（S01）经「缺非循环载体」（S01e/S01d）到「缺行列式同步恒等式」（v2.1 阶段）。一项已定稿的方法论观察：*分析深度与登记完整性并不同步前进*——v1.8b 以最粗的逐轮登记产出了最深的数学。

---

## 7. Data Availability / 数据可用性

Protocol worksheet · execution cards (audit prompt v2.0) · task cards v1.3–v1.9 · ten sealed outputs · AU1 audit — Zenodo concept DOI 10.5281/zenodo.23685131 (v5.4–v5.8), GitHub hengzhiliang-ux/SMPDL. Published with the Completion Experiment Line's independent DOI (four-line split).

协议工作单 · 执行卡三件套（审计提示词 v2.0）· 任务卡 v1.3~v1.9 · 十份封存产出 · AU1 审计——Zenodo 概念 DOI 10.5281/zenodo.23685131（v5.4~v5.8），GitHub hengzhiliang-ux/SMPDL。随补全实验线独立 DOI 发布（四线拆分）。
