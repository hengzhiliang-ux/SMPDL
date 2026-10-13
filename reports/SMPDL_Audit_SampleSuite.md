# SMPDL 结构审查样本总览

> 基于 Göttingen S/M/P × D/L v2.1  
> 日期：2026-10-13

---

## 总览表

| 案例 | 类型 | 审计结果 | 关键通过/失败层 | 备注 |
|---|---|---|---|---|
| 欧几里得素数无限 | 正确证明 | ✅ 通过 | 全绿 | 构造法，依赖图无反向边 |
| 所有三角形都是等腰 | 经典谬误 | ❌ 失败 | S*L, M*D, M*L, P*D, P*L | 隐藏 betweenness 假设 |
| Kempe 四色定理 | 研究级谬误 | ❌ 失败 | M*D, M*L, P*D, P*L | 两次 Kempe 互换独立性未证 |
| √2 无理性 | 正确证明 | ✅ 通过 | 全绿 | 反证法 + 奇偶性 |
| 调和级数发散 | 正确证明 | ✅ 通过 | 全绿 | 分组下界估计 |
| Ramsey 数 R(3,3)=6 | 正确证明 | ✅ 通过 | 全绿 | 鸽巢 + 案例分析 + 显式下界 |
| Cantor 对角线论证 | 正确证明 | ✅ 通过 | 全绿 | 显式构造反枚举 |
| 前 n 个奇数之和 = n² | 正确证明 | ✅ 通过 | 全绿 | 数学归纳法 |
| 二元 AM-GM 不等式 | 正确证明 | ✅ 通过 | 全绿 | 从平方非负出发 |
| 鸽巢原理（基本形式） | 正确证明 | ✅ 通过 | 全绿 | 反证 + 计数 |
| Fermat「所有 Fermat 数都素数」 | 证伪猜想 | ✅ 反驳成立 | 全绿 | Euler 对 F₅ 的因子分解 |
| Euler 幂和猜想 | 证伪猜想 | ✅ 反驳成立 | 全绿 | Lander–Parkin–Selfridge 反例 |
| Basel 问题 ζ(2)=π²/6 | 已证猜想 | ✅ 通过 | 全绿 | Fourier 级数法 |
| Wilson 定理 | 已证猜想 | ✅ 通过 | 全绿 | 双向刻画 |
| Fermat 小定理 | 已证猜想 | ✅ 通过 | 全绿 | 乘法重排 |
| Appel–Haken 四色定理 | 研究级计算机辅助证明 | ⚠️ 部分通过 | P*D, P*L, 跨层映射有风险 | 数学正确但形式化/可理解性有缺口 |
| Navier–Stokes「Lost in Translation」 | AI 自动形式化误译事件 | ❌ S 层失败 | S*D, S*L, 跨层 S→P | Lean 通过但 NL 证明未被验证；m+4→m+5 误译 |
| Riemann 假设 | 开放问题 | ⚠️ 诊断 | M*L 失败 | 局部/统计→全称推广缺口 |
| Andrews-Curtis 猜想 | 开放问题 | ⚠️ 诊断 | M*L 显著缺口 | 缺乏统一结构性理由 + 无非平凡 AC 不变量 |
| OpenAI Kaplansky 特征 2 反例 | AI 生成研究级声明 | ⚠️ 待验证 | M*L + S→P 翻译 | 概率存在性未显式化；P 通过 ≠ S/M 已验证 |
| OpenAI 一般图完美匹配 FPRAS | AI 生成研究级声明 | 🔴 高风险 | M*L 冲突 | 与已知近似计数差分障碍直接冲突风险 |
| OpenAI 最优 Max-Cut NP-hardness | AI 生成研究级声明 | 🔴 高风险 | M*L 张力 | 显著超越当前无条件 NP-hardness 界限；依赖同族 UGC 证明 |
| OpenAI Weil 类代数性（分裂阿贝尔八维簇） | AI 生成声明，已被数学家/社区审查并撤回 | 🔴 已证伪 | M*D/M*L 失败 | 符号错误导致 Eliashberg–Murphy 消去定理前提不满足 |
| OpenAI K3 曲面 Kuga–Satake 对应代数性 | AI 生成声明，已被数学家/社区审查并撤回 | 🔴 已证伪 | M*D 失败 | 依赖已被撤回的 Weil 类构造 |
| OpenAI K3 曲面乘积上的有理 Hodge 猜想 | AI 生成声明，已被数学家/社区审查并撤回 | 🔴 已证伪 | M*D 多重失败 | 依赖两篇已被撤回的同族手稿 |
| OpenAI Selmer 逆命题（椭圆曲线每个素数） | AI 生成研究级声明 | 🟡 高风险 | S*L 量词范围 + M*D | 声明强度接近 BSD/Tate–Shafarevich 量级 |
| OpenAI Kähler 四维 log canonical flip 终止性 | AI 生成研究级声明 | 🟡 高风险 | M*D 多重依赖 | 依赖刚修订的 Kähler MMP 同族输入 |
| OpenAI GFF/Lipschitz 两弧边界极限 | AI 生成研究级声明 | 🟢/🟡 中低风险 | S*D 清晰 + M*D 外部依赖 | 依赖链已明确化，前版已被修复 |
| OpenAI taming ⇒ compatibility（09-23 版） | AI 生成声明，已被修复 | 🔴 错误 | M*L/S*L | cone-equality claim 被 10-06 版修正 |
| OpenAI Ashkin–Teller 联合 scaling limit（09-25 版） | AI 生成声明，已被修复 | 🔴 错误 | M*D/M*L 多节点 | crossing/boundary-attachment/conditioning/convergence 修复 |
| OpenAI 有限普通 Kähler MMP（09-24 版） | AI 生成声明，已被修复 | 🔴 错误 | M*D 输入模糊 | positivity/contraction 论证在 10-07 版扩展 |
| OpenAI taming ⇒ compatibility（修复前后对比） | 修复前后对比 | 🟢/🟡 中低风险 | S*L/M*L 已修复 | 声明收窄 + 反例显式 |
| OpenAI Ashkin–Teller 联合 scaling limit（修复前后对比） | 修复前后对比 | 🟡 中风险 | M*D/M*L 已声明修复 | 核心论证重写，新工具待验证 |
| OpenAI 有限普通 Kähler MMP（修复前后对比） | 修复前后对比 | 🟡 中风险 | M*D 已声明修复 | 输入显式化 + 核心论证补强 |
| OpenAI 低 Selmer 秩完整 BSD | AI 生成研究级声明 | 🔴 高风险 | M*D/M*L 千禧年级依赖 | 历史依赖断裂 |
| OpenAI 准 Riemann 假设 | AI 生成研究级声明 | 🔴 高风险 | S*L/M*L 声明强度远超已知 | 形式化范围待查 |
| OpenAI CM 阿贝尔簇 Hodge | AI 生成研究级声明 | 🔴 高风险 | M*D 同族依赖多米诺 | 受撤回事件波及 |
| OpenAI 有理数域 Hilbert 第十问题 | AI 生成研究级声明 | 🔴 高风险 | M*D 核心编码障碍未披露 | 长期开放问题 |
| OpenAI 自由群因子同构 | AI 生成研究级声明 | 🔴 高风险 | S*L/M*L 跨结论放大 | 形式化范围待查 |
| OpenAI Catalan 常数无理 | AI 生成研究级声明 | 🔴 高风险 | M*D 核心构造未披露 | 长期开放问题 |
| OpenAI Goldfeld 密度猜想 | AI 生成研究级声明 | 🔴 高风险 | M*D/M*L 依赖网络密集 | 与 BSD/Tate–Shafarevich 相关 |
| OpenAI Chowla/Elliott 两点相关 | AI 生成研究级声明 | 🔴 高风险 | S*L/M*L 声明远超已知 | log 幂节省待查 |
| OpenAI Fontaine–Mazur p=2 | AI 生成研究级声明 | 🔴 高风险 | M*D 形变理论障碍 | 模性 lifting 核心未披露 |
| OpenAI 正特征受限几何 Langlands | AI 生成研究级声明 | 🔴 高风险 | M*D 多重依赖 | 推出 Ramanujan/Arthur 待查 |
| OpenAI 阿贝尔簇 Zilber–Pink | AI 生成研究级声明 | 🔴 高风险 | M*D/M*L 高维障碍 | 推广 Manin–Mumford/Mordell–Lang |
| OpenAI π 的无理性指数为 2 | AI 生成研究级声明 | 🔴 高风险 | M*D 逼近构造未披露 | Flint–Hills 推论依赖前者 |
| OpenAI p-adic section 猜想 | AI 生成研究级声明 | 🔴 高风险 | M*D/M*L anabelian 障碍 | 局部→全局提升待查 |
| OpenAI 弱非齐次 Duffin–Schaeffer | AI 生成研究级声明 | 🔴 高风险 | S*L/M*L 非齐次重叠估计 | 任意平移 γ 待查 |
| OpenAI 虚二次域椭圆曲线模性 | AI 生成研究级声明 | 🔴 高风险 | M*D 非全实域障碍 | local-global 兼容待查 |
| OpenAI 对数空间精确去随机化 L=RL=BPL | AI 生成研究级声明，已完成 Lean 形式化 | 🔴 高风险 | S*L/M*L 声明强度远超已知 | PRG/Extractor 核心构造未披露；形式化范围待查 |
| OpenAI 矩阵乘法指数 ω≤9/4 | AI 生成研究级声明，已完成 Lean 形式化 | 🔴 高风险 | M*D/M*L 声明强度远超已知 | 张量构造与激光方法变体未披露；形式化范围待查 |
| OpenAI Hilbert 第 16 问题极限环一致有界 | AI 生成研究级声明，已完成 Lean 形式化 | 🔴 高风险 | M*D/M*L 百年未决问题 | 退化奇点与全局分岔 uniform 控制未披露 |
| OpenAI 一般凸体 Mahler 猜想 | AI 生成研究级声明，已完成 Lean 形式化 | 🔴 高风险 | M*D/M*L 长期未决凸几何问题 | 体积积下界与等号分类未披露；形式化范围待查 |
| OpenAI Thompson 群 F 非可均化 | AI 生成研究级声明，已完成 Lean 形式化 | 🔴 高风险 | S*L/M*L 40 年未决几何群论问题 | 非可均化判据在 F 上的适用性未披露 |
| OpenAI Bogomolov–Pop 函数域重建 | AI 生成研究级声明，已完成 Lean 形式化 | 🔴 高风险 | M*D 远阿贝尔几何难题 | 重建函子与 ℓ/特征条件未披露；形式化范围待查 |
| OpenAI Falconer 距离猜想 | AI 生成研究级声明，已完成 Lean 形式化 | 🔴 高风险 | M*D/M*L 几何测度论核心问题 | Hausdorff 维度假设与距离集正测度转换未披露 |
| OpenAI Ostmann 逆 Goldbach 猜想 | AI 生成研究级声明，已完成 Lean 形式化 | 🔴 高风险 | S*L/M*L 加性数论难题 | 「有限修改」量化与筛法一致性未披露 |
| OpenAI Erdős 倒数和与拟多项式 Szemerédi 界 | AI 生成研究级声明，已完成 Lean 形式化 | 🔴 高风险 | S*L/M*L 声明远超 Green–Tao 类结果 | 密度增量/正则性新工具未披露；形式化范围待查 |
| OpenAI 短 Egyptian 分数 | AI 生成研究级声明，已完成 Lean 形式化 | 🔴 高风险 | M*D/M*L 数论长期问题 | O(log log b) 构造与匹配下界未披露 |

---

## 1. 证伪猜想类案例

### 1.1 Fermat「所有 Fermat 数都是素数」

- **文件**：`SMP_ProofAnalysis_FermatNumbers_PrimeConjecture.md`
- **反例**：Euler 证明 641 | F₅，从而 F₅ 为合数。
- **审计要点**：反例只需一个具体 n=5 即可推翻全称命题；M*D 中 Euler 的代数技巧（641 = 5·2⁷+1 = 5⁴+2⁴）是关键。

### 1.2 Euler 幂和猜想

- **文件**：`SMP_ProofAnalysis_EulerSumPowers_Conjecture.md`
- **反例**：27⁵ + 84⁵ + 110⁵ + 133⁵ = 144⁵。
- **审计要点**：计算反例直接推翻「k 个 k 次幂之和至少需要 k 项」的全称断言；S*L 强调 ∀k 被 k=5 否定。

---

## 2. 已证猜想类案例

### 2.1 Basel 问题

- **文件**：`SMP_ProofAnalysis_Basel_Problem.md`
- **要点**：Fourier 级数法严格；Euler 原始 sin 乘积法需要额外收敛性论证。

### 2.2 Wilson 定理

- **文件**：`SMP_ProofAnalysis_Wilson_Theorem.md`
- **要点**：双向证明；⇒ 方向用逆元配对，⇐ 方向用合数真因子矛盾。

### 2.3 Fermat 小定理

- **文件**：`SMP_ProofAnalysis_FermatLittle_Theorem.md`
- **要点**：乘法重排法；核心是证明 x ↦ a·x 为 S→S 的双射。

---

## 3. AI 自动形式化误译类案例

### 3.1 Navier–Stokes「Lost in Translation」事件

- **文件**：`SMP_ProofAnalysis_NavierStokes_LostInTranslation.md`
- **事件**：OpenAI 宣布 Navier–Stokes 爆破证明，同时发布 NL 证明与 Lean 形式化；Bastounis–Circelli–Hansen（arXiv:2610.08144）发现两者不对应。
- **核心差异**：Lemma 8.6 中 NL 要求 m+4 导数，Lean 要求 m+5（严格更弱）；压力–通量估计采用不同界限与证明方法。
- **理论结果**：语义忠实自动形式化在 SCI 层次结构中位于 SCI=∞，高于停机问题。
- **审计要点**：这是 SMPDL 案例库的新类型——**「P 层通过但 S 层翻译失败」型**；Lean 编译通过与 NL 证明正确性无关；跨层拔高是 AI 时代的新型数学风险。
- **重要澄清**：论文作者**不声称** NL 证明错误，只声称**翻译不忠实**；NL 证明的正确性仍是开放问题。

---

## 4. 开放问题类案例

### 4.1 Riemann 假设

- **文件**：`SMP_RH_Diagnostic_ProofDirections.md`
- **要点**：M*L 缺口——局部/统计信息无法推进到全称结论。

### 4.2 Andrews-Curtis 猜想

- **文件**：`SMP_ProofAnalysis_AndrewsCurtis.md`
- **命题**：任意平衡平凡表示可通过 AC 变换化为平凡表示。
- **审计要点**：S/M/P 依存全部健康；M*L 存在显著缺口——缺乏统一结构性理由解释为何所有平衡平凡表示应 AC-平凡；缺乏非平凡 AC 不变量；Bridson–Lishak 超指数下界排除纯搜索方法。
- **与 RH 对比**：RH 缺口在「局部统计→全称推广」；ACC 缺口在「存在性证明非构造性」。

---

## 5. AI 生成研究级声明类案例

### 5.1 OpenAI Kaplansky 特征 2 反例

- **文件**：`SMP_ProofAnalysis_OpenAI_Kaplansky_DirectFiniteness.md`
- **声明**：构造有限域 K（特征 2）、有限表现群 G 与 a,b∈K[G]，使 ab=1 但 ba≠1。
- **审计要点**：S/M/P 依存结构清晰；M*L 关键缺口在于构造是概率存在性，未给出显式群表现或终止 prescription 的可执行实例；Lean 形式化范围未公开说明，存在 P 通过但 S/M 未独立验证风险。

### 5.2 OpenAI 一般图完美匹配 FPRAS

- **文件**：`SMP_ProofAnalysis_OpenAI_FPRAS_PerfectMatchings.md`
- **声明**：存在 FPRAS 对任意简单无向图近似计数完美匹配。
- **审计要点**：M*L 高风险——与已知近似计数基本障碍（x,y 可近似 ≠ x−y 可近似）直接冲突；论文虽声称使用全新状态空间，但未显式解释为何绕过该信息论下界；Lean 通过不能消除 M 层风险。

### 5.3 OpenAI 最优 Max-Cut NP-hardness

- **文件**：`SMP_ProofAnalysis_OpenAI_MaxCut_Hardness.md`
- **声明**：在简单无权图上，任意固定 ρ>α_GW 的 Max-Cut 近似都是 NP-hard。
- **审计要点**：M*L 高风险——声称显著超越当前无条件 NP-hardness 界限（Håstad 16/17≈0.941）；同族论文 102 声称证明 UGC，本定理根基与之绑定；若 UGC 证明失败，本定理的「direct」归约需要重新检查是否暗含等价假设。

### 5.4 OpenAI 已被审查并撤回的声明

#### 5.4.1 Weil 类代数性（分裂阿贝尔八维簇）

- **文件**：`SMP_ProofAnalysis_OpenAI_WeilClasses_SignError.md`
- **声明**：分裂阿贝尔八维簇上 Weil 类的代数性。
- **审计要点**：🔴 已撤回。符号错误导致稳定化迹论证中反向迹符号取反；Eliashberg–Murphy 消去定理前提（带符号双重点计数为零）不满足；后续手术/嵌入膜构造失效。

#### 5.4.2 K3 曲面 Kuga–Satake 对应代数性

- **文件**：`SMP_ProofAnalysis_OpenAI_KugaSatake_DependentGap.md`
- **声明**：K3 曲面 Kuga–Satake 对应是代数的。
- **审计要点**：🔴 已撤回。直接依赖已被撤回的 Weil 类构造；上游符号错误导致带符号双重点无法抵消，依赖链断裂。

#### 5.4.3 K3 曲面乘积上的有理 Hodge 猜想

- **文件**：`SMP_ProofAnalysis_OpenAI_HodgeK3_Withdrawal.md`
- **声明**：射影 K3 曲面乘积上的有理 Hodge 猜想成立。
- **审计要点**：🔴 已撤回。依赖两篇已被撤回的同族手稿（Weil 类 + Kuga–Satake），构成多重 M*D 失败；展示 AI 论文族内部相互引用的多米诺风险。

### 5.5 OpenAI 最新发表样本（2026-10-06/07）

#### 5.5.1 椭圆曲线在每个素数处的 Selmer 逆命题

- **文件**：`SMP_ProofAnalysis_OpenAI_SelmerConverse_EveryPrime.md`
- **声明**：对任意素数 `p`，椭圆曲线的 Selmer 逆命题成立。
- **审计要点**：🟡 高风险。声明强度接近 BSD 猜想与 Tate–Shafarevich 有限性量级；README 仅说明更新同族修订稿引用，未披露核心数论障碍如何克服；S*L 存在“every prime”量词范围陷阱。

#### 5.5.2 紧 Kähler 四维簇上广义 log canonical flip 的终止性

- **文件**：`SMP_ProofAnalysis_OpenAI_TerminationLogCanonical_KahlerFourfolds.md`
- **声明**：紧 Kähler 四维簇上广义 log canonical flip 在有限步后终止。
- **审计要点**：🟡 高风险。README 明确依赖“独立相对 MMP”和“双有理比较”输入，并更新到刚修订的同族论文；M*D 层存在多重依赖，Kähler 非射影情形本身即是活跃难题。

#### 5.5.3 两弧边界数据下整数 Lipschitz 高度的 GFF 极限

- **文件**：`SMP_ProofAnalysis_OpenAI_GFF_LipschitzHeights_TwoArc.md`
- **声明**：两弧边界数据下整数 Lipschitz 高度收敛到高斯自由场。
- **审计要点**：🟢/🟡 中低风险。本版明确将条件切割与环估计从伴随加权环形电路定理（`x=1`）推导；依赖链较前版清晰，但边界条件与核心收敛细节仍需概率论专家复核。

### 5.6 OpenAI 已被修复/证伪样本

#### 5.6.1 taming 蕴含 compatibility（09-23 版）

- **文件**：`SMP_ProofAnalysis_OpenAI_TamingCompatibility_Sep23_Fixed.md`
- **声明**：四维流形上 taming 蕴含 compatibility。
- **审计要点**：🔴 错误。原证明的 cone-equality claim 被 10-06 版修正为 strict-inclusion example；S*L/M*L 核心断言失败，导致“存在兼容形式”结论失去基础。

#### 5.6.2 临界 Ashkin–Teller 电流的联合 scaling limit（09-25 版）

- **文件**：`SMP_ProofAnalysis_OpenAI_AshkinTeller_JointScaling_Sep25_Fixed.md`
- **声明**：临界 Ashkin–Teller 电流的联合分布存在 scaling limit。
- **审计要点**：🔴 错误。history.md 明确列出原证明在 crossing、boundary-attachment、conditioning 和 convergence 论证上均需修复；M*D/M*L 多节点失败。

#### 5.6.3 紧 Kähler 四维簇上的有限普通 MMP（09-24 版）

- **文件**：`SMP_ProofAnalysis_OpenAI_FiniteOrdinaryMMP_KahlerFourfolds_Sep24_Fixed.md`
- **声明**：紧 Kähler 四维簇上普通 MMP 有限。
- **审计要点**：🔴 错误/不完整。history.md 说明 10-07 修复批次扩展了 positivity 与 contraction 论证，并澄清了作为输入的“已知结果”及其假设；M*D 存在输入模糊与隐藏假设。

### 5.7 OpenAI 修复前后对比样本

#### 5.7.1 taming 蕴含 compatibility（09-23 → 10-06）

- **文件**：`SMPDL_Compare_OpenAI_TamingCompatibility_PrePostFix.md`
- **对比**：修复前 cone-equality claim 错误 → 修复后声明收窄为 `h_J^- = b_2^+ - 1` 并显式给出 four-torus 严格包含反例。
- **审计要点**：🔴→🟢/🟡 风险显著下降；S*L/M*L 核心失败已被精准消除；P 层仍缺失。

#### 5.7.2 临界 Ashkin–Teller 电流的联合 scaling limit（09-25 → 10-06）

- **文件**：`SMPDL_Compare_OpenAI_AshkinTeller_JointScaling_PrePostFix.md`
- **对比**：修复前 crossing/boundary-attachment/conditioning/convergence 多节点失败 → 修复后用 signed-loop-soup/GMC 替换 excursion convergence，修正 boundary-collar/transmission。
- **审计要点**：🔴→🟡 风险下降但未根治；新依赖链引入 GMC 等高级对象，仍需外部专家验证。

#### 5.7.3 紧 Kähler 四维簇上的有限普通 MMP（09-24 → 10-06）

- **文件**：`SMPDL_Compare_OpenAI_FiniteOrdinaryMMP_PrePostFix.md`
- **对比**：修复前 positivity/contraction 输入模糊 → 修复后增加 carrier-positivity 与 multiplier-ideal 论证，修订 contraction induction，澄清输入结果。
- **审计要点**：🔴/🟡→🟡 风险下降；Kähler MMP 本身是活跃难题，领域高风险未变。

### 5.8 OpenAI 第二批高危抽样（2026-10-13）

从 719 份 OpenAI 数学手稿中再抽取 5 份声明强度最高、与已知未决问题直接相关的样本进行 SMPDL 审计。

#### 5.8.1 低 Selmer 秩的完整 BSD 公式

- **文件**：`SMP_ProofAnalysis_OpenAI_BSD_LowSelmerCorank.md`
- **声明**：若椭圆曲线 `E/ℚ` 的完整 `q`-power Selmer 群 corank 为 0 或 1，则完整 BSD 公式成立（含 Tate–Shafarevich 有限）。
- **审计要点**：🔴 高风险。BSD 为 Clay 千禧年问题；README 承认删除了对已移除支持论文的引用，历史依赖断裂。

#### 5.8.2 准 Riemann 假设 Re(s)>7/8

- **文件**：`SMP_ProofAnalysis_OpenAI_QuasiRiemannHypothesis.md`
- **声明**：所有 Dirichlet / 特定 Hecke L-函数在 `Re(s)>7/8` 无零点。
- **审计要点**：🔴 高风险。声明强度远超当前解析数论零-free 区域；Lean 形式化范围待查。

#### 5.8.3 CM 阿贝尔簇的有理 Hodge 猜想

- **文件**：`SMP_ProofAnalysis_OpenAI_Hodge_CM_AbelianVarieties.md`
- **声明**：所有复 CM 阿贝尔簇满足有理 Hodge 猜想，并推出 Tate 猜想与 Hodge 标准猜想。
- **审计要点**：🔴 高风险。Hodge 为千禧年问题；受 10-07 同族 Weil 类论文撤回事件波及，存在多米诺依赖风险。

#### 5.8.4 有理数域上的 Hilbert 第十问题

- **文件**：`SMP_ProofAnalysis_OpenAI_HilbertTenth_Rationals.md`
- **声明**：整数系数多项式是否存在有理零点不可判定。
- **审计要点**：🔴 高风险。该问题是数理逻辑长期开放问题；README 未披露从 `ℤ` 到 `ℚ` 的核心编码如何绕过已知障碍。

#### 5.8.5 自由群因子的同构

- **文件**：`SMP_ProofAnalysis_OpenAI_FreeGroupFactors_Isomorphism.md`
- **声明**：`L(𝔽₂) ≅ L(𝔽₃)`，从而所有插值自由群因子同构。
- **审计要点**：🔴 高风险。算子代数长期开放问题；摘要用 “hence” 跨结论放大，Lean 形式化范围待查。

### 5.9 OpenAI 第三批高危抽样（2026-10-13）

从 719 份 OpenAI 数学手稿中再抽取 10 份声明强度最高、与已知未决问题直接相关的样本进行 SMPDL 审计，覆盖数论、代数几何、表示论、算子代数与 anabelian 几何。

#### 5.9.1 Catalan 常数为无理数

- **文件**：`SMP_ProofAnalysis_OpenAI_Catalan_Irrationality.md`
- **声明**：Catalan 常数 G = β(2) 是无理数。
- **审计要点**：🔴 高风险。Catalan 常数无理性是长期开放问题；README 极简，未披露任何丢番图逼近构造或线性形式。

#### 5.9.2 Goldfeld 密度猜想与 2-逆命题

- **文件**：`SMP_ProofAnalysis_OpenAI_Goldfeld_Density_Twists.md`
- **声明**：二次 twists 的解析秩 0/1 各密度 1/2，平均秩 1/2；2-逆命题成立。
- **审计要点**：🔴 高风险。Goldfeld 猜想是椭圆曲线核心开放问题；需要排除 rank ≥ 2 正密度，声明强度接近 BSD/Tate–Shafarevich。

#### 5.9.3 乘性函数的普通两点相关

- **文件**：`SMP_ProofAnalysis_OpenAI_Chowla_Elliott_TwoPoint.md`
- **声明**：普通两点 Chowla 猜想与二元修正 Elliott 猜想成立，且带有 log 幂节省。
- **审计要点**：🔴 高风险。声明远超 Matomäki–Radziwiłł–Tao 的齐次结果；非比例仿射形式的逐点 log 节省需要非凡技术。

#### 5.9.4 p=2 时的 Fontaine–Mazur 模性

- **文件**：`SMP_ProofAnalysis_OpenAI_FontaineMazur_Prime2.md`
- **声明**：奇二维 2-adic Galois 表示（de Rham，不同 HT 权重）模性成立。
- **审计要点**：🔴 高风险。p=2 Fontaine–Mazur 是 Langlands 纲领核心难题；需处理所有剩余表示，包括非 ordinary 情形。

#### 5.9.5 正特征下的受限几何 Langlands 等价

- **文件**：`SMP_ProofAnalysis_OpenAI_GeometricLanglands_PosChar.md`
- **声明**：受限几何 Langlands 等价成立，并推出 Ramanujan 猜想与 Arthur 增强。
- **审计要点**：🔴 高风险。几何 Langlands 是 21 世纪最深刻项目之一；README 同时抛出多个深奥推论，依赖网络极广。

#### 5.9.6 阿贝尔簇上的 Zilber–Pink 猜想

- **文件**：`SMP_ProofAnalysis_OpenAI_ZilberPink_Abelian.md`
- **声明**：阿贝尔簇上的 Zilber–Pink 猜想成立。
- **审计要点**：🔴 高风险。Zilber–Pink 统一并推广 Manin–Mumford、Mordell–Lang；高维子簇的一致高度下界是核心障碍。

#### 5.9.7 π 的无理性指数为 2

- **文件**：`SMP_ProofAnalysis_OpenAI_Pi_IrrationalityExponent2.md`
- **声明**：π 的无理性指数 μ(π) = 2。
- **审计要点**：🔴 高风险。此前最佳上界为 Salikhov 的 7.6063；达到精确值 2 需要构造极强的有理逼近下界。

#### 5.9.8 p-adic section 猜想

- **文件**：`SMP_ProofAnalysis_OpenAI_Padic_SectionConjecture.md`
- **声明**：局部 p-adic section 猜想成立，并推出 X₀(N)/X₁(N) 的全局 section 猜想。
- **审计要点**：🔴 高风险。Grothendieck section 猜想是 anabelian 几何核心；局部→全局提升需要额外条件。

#### 5.9.9 弱非齐次 Duffin–Schaeffer 猜想

- **文件**：`SMP_ProofAnalysis_OpenAI_DuffinSchaeffer_Inhomogeneous.md`
- **声明**：对任意平移 γ 与有限值 ψ，发散条件蕴含几乎处处无限多逼近。
- **审计要点**：🔴 高风险。非齐次度量丢番图逼近是前沿难题；齐次情形由 Koukoulopoulos–Maynard 解决，非齐次重叠估计更复杂。

#### 5.9.10 虚二次域上椭圆曲线的模性

- **文件**：`SMP_ProofAnalysis_OpenAI_Modularity_ImaginaryQuadratic.md`
- **声明**：每个虚二次域上的椭圆曲线都模性，且局部参数处处匹配。
- **审计要点**：🔴 高风险。虚二次域 non-totally-real，经典 Taylor–Wiles 方法需改用 derived/torsion 框架；local-global 兼容性是关键。

### 5.10 OpenAI 第四批高危抽样：已完成 Lean 形式化但仍高风险（2026-10-13）

从 719 份 OpenAI 数学手稿中挑选 **10 份已完成 Lean 形式化、但因声明强度极大或形式化范围与纸面断言之间可能存在 scope gap 而仍具结构性高风险** 的样本进行 SMPDL 审计。审计重点从「策略未披露」转向「Lean 验证了什么 vs 论文声称了什么」之间的对齐问题。

#### 5.10.1 对数空间精确去随机化 L = RL = BPL

- **文件**：`SMP_ProofAnalysis_OpenAI_Logspace_Derandomization_L_RL_BPL.md`
- **声明**：\(\mathsf{L}=\mathsf{RL}=\mathsf{BPL}\)。
- **审计要点**：🔴 高风险。去随机化是复杂度理论核心开放问题；Lean 形式化可能只覆盖某个辅助引理，而非完整的 BPL→L 模拟；机器模型等价性、one-sided/two-sided 错误转换是核心 gap。

#### 5.10.2 矩阵乘法指数 ω ≤ 9/4

- **文件**：`SMP_ProofAnalysis_OpenAI_MatrixMultiplication_Exponent_9_4.md`
- **声明**：复数域上矩阵乘法指数 \(\omega \le 9/4\)。
- **审计要点**：🔴 高风险。声明远强于人类最好结果 \(\omega \approx 2.37\)；形式化可能只验证某个特定张量的低秩，未证明其可放大到任意 \(n\) 并完成到 \(\omega\) 上界的转换。

#### 5.10.3 Hilbert 第 16 问题：极限环一致有界

- **文件**：`SMP_ProofAnalysis_OpenAI_Hilbert16_LimitCycles.md`
- **声明**：任意 \(n\) 次实平面多项式向量场的极限环数量有仅依赖于 \(n\) 的一致上界。
- **审计要点**：🔴 高风险。百年未决问题；形式化可能只覆盖低次或局部有限性，未处理退化奇点与全局分岔的 uniform 控制。

#### 5.10.4 一般凸体的 Mahler 猜想

- **文件**：`SMP_ProofAnalysis_OpenAI_Mahler_Conjecture_General.md`
- **声明**：一般凸体 Mahler 猜想在任意维数成立，Hanner 多面体与单形分别为对称/非对称情形的唯一等号情形。
- **审计要点**：🔴 高风险。长期未决凸几何问题；形式化可能验证等号情形的计算，但未证明完整下界与分类。

#### 5.10.5 Thompson 群 F 非可均化

- **文件**：`SMP_ProofAnalysis_OpenAI_ThompsonGroup_Nonamenable.md`
- **声明**：Thompson 群 \(F\) 是非可均化的。
- **审计要点**：🔴 高风险。40 年未决的著名几何群论问题；形式化可能验证某个非可均化判据，但判据在 \(F\) 上的适用性是核心难点。

#### 5.10.6 Bogomolov–Pop 函数域重建

- **文件**：`SMP_ProofAnalysis_OpenAI_BogomolovPop_Reconstruction.md`
- **声明**：从 Milnor K-理论 / Galois 数据重建高维函数域，证明 Bogomolov–Pop 定理。
- **审计要点**：🔴 高风险。远阿贝尔几何核心问题；形式化可能覆盖低次或特殊域，未处理一般超越度 \(\ge 2\) 与 \(\ell = \mathrm{char}\) 情形。

#### 5.10.7 Falconer 距离猜想

- **文件**：`SMP_ProofAnalysis_OpenAI_Falconer_DistanceConjecture.md`
- **声明**：\(\mathbb{R}^d\) 中 Hausdorff 维数 \(> d/2\) 的紧集确定正 Lebesgue 测度的距离集。
- **审计要点**：🔴 高风险。几何测度论核心问题；形式化可能只处理 Salem 集或离散模型，未覆盖一般紧集与 Hausdorff 维度假设。

#### 5.10.8 Ostmann 逆 Goldbach 猜想

- **文件**：`SMP_ProofAnalysis_OpenAI_Ostmann_InverseGoldbach.md`
- **声明**：素数的任何有限修改都不是两个无限集的和。
- **审计要点**：🔴 高风险。加性数论难题；「有限修改」的精确定义与筛法一致性是核心 gap；形式化可能只覆盖充分大整数。

#### 5.10.9 Erdős 倒数和猜想与拟多项式 Szemerédi 界

- **文件**：`SMP_ProofAnalysis_OpenAI_ReciprocalSum_Szemeredi.md`
- **声明**：倒数和发散集包含任意长等差数列；\(r_k(N) \le N/(\log N)^{c_k}\)。
- **审计要点**：🔴 高风险。声明远超当前 Green–Tao/Gowers 类结果；形式化可能只处理 \(k=3\) 或特殊集合，未覆盖一般 \(k\) 与发散条件。

#### 5.10.10 短 Egyptian 分数

- **文件**：`SMP_ProofAnalysis_OpenAI_ShortEgyptianFractions.md`
- **声明**：任意有理数 \(a/b\) 可表为 \(O(\log\log b)\) 个不同单位分数之和，且该阶最优。
- **审计要点**：🔴 高风险。Erdős 猜想；形式化可能只证明上界构造，未给出匹配的下界或有效常数。

---

## 6. 语料级审计方法论

### 6.1 OpenAI 700+ 数学证明库

- **文件**：`SMP_OpenAI700_Corpus_AuditMethodology.md`
- **要点**：将 SMPDL 应用于整库的 7 步流程；整库风险分层；三份样例审计摘要；给数学共同体的使用建议。

---

## 7. 教学用途分组

| 教学目的 | 推荐案例 |
|---|---|
| 展示正确证明如何闭合 | 欧几里得、√2、Cantor、奇数和、AM-GM、鸽巢、Basel、Wilson、Fermat 小定理 |
| 展示经典谬误如何断裂 | 等腰三角形、Kempe 四色 |
| 展示证伪猜想的力量 | Fermat 素数猜想、Euler 幂和猜想 |
| 展示研究级证明的复杂边界 | Appel–Haken 四色定理 |
| **展示 AI 自动形式化的跨层翻译失败** | **Navier–Stokes「Lost in Translation」** |
| 展示开放问题的核心缺口 | Riemann 假设、Andrews-Curtis 猜想 |
| 展示「语义清晰但结构缺口显著」的开放问题 | Andrews-Curtis 猜想 |
| 展示「P 层通过 ≠ M 层正确」 | Navier–Stokes「Lost in Translation」 |
| 展示「符号/约定错误如何证伪证明」 | OpenAI Weil 类代数性 |
| 展示「同族论文相互依赖导致的多米诺撤回」 | OpenAI Kuga–Satake / K3 Hodge |
| 展示「集合相等 vs 严格包含」语义错误 | OpenAI taming ⇒ compatibility（09-23 版） |
| 展示「crossing + conditioning + convergence」多节点失败 | OpenAI Ashkin–Teller 联合 scaling limit（09-25 版） |
| 展示「输入假设未显式列出」导致 M*D 失败 | OpenAI 有限普通 Kähler MMP（09-24 版） |
| 展示「every」量词范围陷阱 | OpenAI Selmer 逆命题 |
| 展示「同族修订稿多重依赖」风险 | OpenAI Kähler 四维 log canonical flip 终止性 |
| 展示「依赖链明确化」降低风险 | OpenAI GFF/Lipschitz 两弧边界极限 |
| 展示「声明收窄 + 反例显式」修复 S*L/M*L | OpenAI taming ⇒ compatibility（修复前后对比） |
| 展示「核心论证重写」降低但未根除 M*D/M*L 风险 | OpenAI Ashkin–Teller 联合 scaling limit（修复前后对比） |
| 展示「输入显式化 + 工具具体化」修复 M*D | OpenAI 有限普通 Kähler MMP（修复前后对比） |
| 展示「历史依赖断裂 + 千禧年级强度」风险 | OpenAI 低 Selmer 秩完整 BSD |
| 展示「声明强度远超已知技术」风险 | OpenAI 准 Riemann 假设 |
| 展示「同族撤回事件多米诺」风险 | OpenAI CM 阿贝尔簇 Hodge |
| 展示「核心编码障碍未披露」风险 | OpenAI 有理数域 Hilbert 第十问题 |
| 展示「跨结论放大 + 形式化范围未知」风险 | OpenAI 自由群因子同构 |
| 展示「README 极简 + 核心构造未披露」风险 | OpenAI Catalan 常数无理 |
| 展示「密度猜想 + rank ≥ 2 排除」风险 | OpenAI Goldfeld 密度猜想 |
| 展示「定量 log 幂节省远超已知」风险 | OpenAI Chowla/Elliott 两点相关 |
| 展示「p=2 模性 lifting 障碍」风险 | OpenAI Fontaine–Mazur p=2 |
| 展示「深奥推论网络 + 依赖链极广」风险 | OpenAI 正特征受限几何 Langlands |
| 展示「高维 atypical 子簇一致控制」风险 | OpenAI 阿贝尔簇 Zilber–Pink |
| 展示「具体常数无理性指数精确值」风险 | OpenAI π 的无理性指数为 2 |
| 展示「局部→全局 anabelian 提升」风险 | OpenAI p-adic section 猜想 |
| 展示「非齐次度量逼近重叠估计」风险 | OpenAI 弱非齐次 Duffin–Schaeffer |
| 展示「non-totally-real 模性 + local-global」风险 | OpenAI 虚二次域椭圆曲线模性 |
| 展示「Lean 形式化 ≠ 纸面主定理」scope gap 风险（复杂度理论） | OpenAI 对数空间精确去随机化 L=RL=BPL |
| 展示「Lean 形式化 ≠ 纸面主定理」scope gap 风险（算法/代数复杂度） | OpenAI 矩阵乘法指数 ω≤9/4 |
| 展示「Lean 形式化 ≠ 纸面主定理」scope gap 风险（动力系统） | OpenAI Hilbert 第 16 问题极限环一致有界 |
| 展示「Lean 形式化 ≠ 纸面主定理」scope gap 风险（凸几何） | OpenAI 一般凸体 Mahler 猜想 |
| 展示「Lean 形式化 ≠ 纸面主定理」scope gap 风险（几何群论） | OpenAI Thompson 群 F 非可均化 |
| 展示「Lean 形式化 ≠ 纸面主定理」scope gap 风险（远阿贝尔几何） | OpenAI Bogomolov–Pop 函数域重建 |
| 展示「Lean 形式化 ≠ 纸面主定理」scope gap 风险（几何测度论） | OpenAI Falconer 距离猜想 |
| 展示「Lean 形式化 ≠ 纸面主定理」scope gap 风险（加性数论） | OpenAI Ostmann 逆 Goldbach 猜想 |
| 展示「Lean 形式化 ≠ 纸面主定理」scope gap 风险（组合/解析数论） | OpenAI Erdős 倒数和与拟多项式 Szemerédi 界 |
| 展示「Lean 形式化 ≠ 纸面主定理」scope gap 风险（数论） | OpenAI 短 Egyptian 分数 |

---

## 8. 高风险 / 中风险声明的人类科学家审查指南

- **文件**：`SMPDL_HumanReview_HighMidRisk_Guide.md`
- **要点**：五岗位（A/B/C/D/E）针对高风险与中低风险声明的具体审查动作；TRAP-CHECK 七类陷阱的专项扫描；针对本批次 OpenAI 六个样本的逐条审查建议。

---

## 9. 署名与许可

**Göttingen S/M/P × D/L 数学证明审查方法论** · v2.1  
**作者**：CAMPANASILVAE · fecit · MMXXVI  
**首发时间**：2026-10-12 GMT+8 · **更新**：2026-10-13  
**许可协议**：[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh)（署名-非商用-相同方式共享）  
**完整清单与内容指纹**：见 `SMPDL_ATTRIBUTION.md`

搬运、改写或教学引用请注明来源与本页面链接。

---

## 文献引用纪律检查

依据 SMPDL 文献引用纪律（真实性核查 + 支持性核查），本报告审查如下：

| 引用对象 | 真实性 | 支持性 | 说明 |
|---|---|---|---|
| 引用的数学/逻辑/编程经典结果 | ✅ 真实 | ✅ 支持 | 方法论文件引用的 Curry-Howard、模型论、类型论等概念属于公共知识。 |
| 引用的具体论文/书籍 | ⚠️ 待查 | ⚠️ 待查 | 若引用具体著作，需按真实性 + 支持性纪律核查。 |
| OpenAI/AI 相关案例 | ⚠️ 待查 | ⚠️ 待查 | 若用 OpenAI 论文作为例子，需核对原论文真实性与范围。 |

**核查结论**：本方法论/指南文件主要依赖经典概念；对具体案例或专著的引用应补充逐条核查。

