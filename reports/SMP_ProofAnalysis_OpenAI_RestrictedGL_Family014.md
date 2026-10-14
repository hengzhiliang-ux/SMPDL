# SMPDL 审计报告：OpenAI「Restricted geometric Langlands / Arthur / Ramanujan」（族 014 全量）

**审计对象**：Restricted geometric Langlands, global Arthur enhancements, and generic Ramanujan（族 014，8 篇手稿，全库第二大族）
**来源**：OpenAI math 仓库，2026-09-24 至 10-05 分批发布
**审计日期**：2026-10-14
**审计框架**：Göttingen S/M/P × D/L 六格审计 v1.5（族级全量升级：主论文旧审计 2026-10-13 已有 🔴 判定，本轮补齐 7 篇 + 族拓扑整合）
**审计结论**：🔴 **极高风险维持 + 新发现诚实性正面信号。主论文（受限 GL 等价）旧审计 🔴 判定维持；本轮细读 7 篇同族摘要发现多篇主动边界披露（「does not assert ellipticity, Arthur-packet classification, or a multiplicity formula」）——声明纪律好于库内平均；但 Ramanujan 推论链（等价 ⇒ temperedness ⇒ Ramanujan）的传递条件仍未逐段披露。**

---

## 1. 命题与声明

族 014 顶层声明（三合一 + 特征条件）：
1. **受限几何 Langlands 等价**：连通约化群 × 光滑射影连通曲线 × $\overline{\mathbb F}_q$，四个 Lie 理论特征假设下成立；任意代数闭域 char p > 0 需额外 p 非常好 + p ∤ |W_G|；
2. **泛型 Ramanujan**：全局函数域上分裂伴随绝对单例外群的 cuspidal 泛型表示在每个 place tempered（无特征/分歧深度限制）；分裂伴随绝对单群 + 泛型无分歧分量 ⇒ 每个无分歧 place tempered；
3. **全局 Arthur 增强**：**假设**有限水平 Ramanujan–Arthur 分解 ⇒ 构造 occurring cuspidal excursion 参数的 Arthur 增强，对角特化在整个 Weil 群（含惯性）恢复给定参数。

### 1.1 族内 8 篇手稿拓扑

| 层 | 手稿 | 角色 | 关键条件/结论 | 诚实性信号 |
|---|---|---|---|---|
| **主层** | Restricted GL in Positive Char（09-24） | 主等价定理 | 4 特征假设 / +非常好 p | 旧审计 🔴 |
| 主层 | Ramanujan–Arthur Decompositions（09-24） | 分解定理 | **无条件**：cuspidal 函数按对偶群幂零轨道分解；平期版 = GLR 猜想 3.4.5/3.4.6 | ✅ 明确引用对应 arXiv 2508.02237 |
| **Ramanujan 层** | Temperedness at ramified places（10-05） | 例外群 Ramanujan 收官 | 每个局部分量 tempered（无限制） | ✅ 明确「extends the unramified theorem of a companion paper」 |
| **增强层** | Global Arthur Enhancements（10-05） | 构造定理 | **假设** Thm 1.1 分解 ⇒ 增强 | ✅✅ **「does not assert ellipticity / Arthur-packet / multiplicity formula」主动三不声明** |
| **eigensheaf 层** | Constructible tame Hecke eigensheaves（10-05） | 构造 | Zariski-稠密 ℓ-adic 局部系统 + tame regular-unipotent 单值 | 奇异支撑条件已披露 |
| eigensheaf 层 | Tame Hecke Eigensheaves Several Points（10-05） | 多标志点 | **SL_n 限制 p > n**——群范围收窄 | ✅ 限制显式 |
| eigensheaf 层 | Frobenius Structures（10-05） | 算术版 | 常数域有限扩张后 | ✅ 「after a finite extension」前置 |
| **基础层** | Rationality of Canonical Unramified Arthur Filtration（09-24） | 有理性 | GLR 有理性猜想在受限理论下 | 建立 Gaitsgory–Lafforgue–Raskin 猜想 |

---

## 2. S/M/P × D/L 六格审计（族级，含旧审计整合）

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| 受限 GL 等价 | Hecke eigensheaves / perverse / Whittaker | 🔴 旧审计：策略未披露（维持） |
| 泛型 Ramanujan（例外群全 place） | unramified 定理（companion）+ ramified 扩展 | ⚠️ **传递路径明确**（伴生论文扩展）但 companion 的输入依赖等价主定理 |
| Ramanujan–Arthur 分解（无条件） | 幂零轨道指标分解 | ✅ 陈述自足；平期 ⇒ GLR 3.4.5/3.4.6 |
| Arthur 增强 | **假设** Thm 1.1 | ✅ 条件显式（「Under the ... stated in Theorem 1.1」） |
| eigensheaf 构造 ×3 | tame 单值 + p 条件 | ✅ 群/特征限制逐篇披露 |

**S*D 新发现**：与族 034 的「条件藏在 by-phrase」相反，族 014 的条件披露**显著更诚实**——主定理四特征假设、Arthur 增强的三不声明、eigensheaf 的群限制（SL_n 且 p>n）全部前置。**两族声明纪律对比本身是审计信号**（同库不同族的写作纪律差异 → 需查是否系统成因）。

### 2.2 S*L — 语义逻辑结构

- 主等价的量词链：群（连通约化）× 曲线（光滑射影连通）× 域（$\overline{\mathbb F}_q$→任意代数闭）× 特征（4 假设→+2 假设）——**双 regime 结构已披露**；
- ⚠️ Ramanujan 声明的范围分叉：例外群（无限制全 place）vs 一般分裂伴随绝对单群（仅无分歧 place + 需泛型无分歧分量）——族描述把两者并列，**细读才能区分强弱两版**；
- 「globally generic cuspidal」的全称量词域（所有 vs density-one）表述清晰。

### 2.3 M*D — 数学依存（族拓扑）

```
[基础] Rationality of Arthur Filtration (09-24, 无条件)
    ↑
[主定理] Restricted GL Equivalence (09-24)
    ↑                    ↑
[分解] Ramanujan-Arthur Decomp (09-24)   [eigensheaf 层 ×3 (10-05)]
    ↑ (作为假设 Thm 1.1)                      (构造性支撑)
[增强] Global Arthur Enhancements (10-05, 条件)
    
[Ramanujan 链] 主定理 ⇒ unramified tempered (companion) ⇒ ramified (10-05) ⇒ 全 place Ramanujan
```

**M*D 发现**：
1. **Ramanujan 链的三段传递**：等价 → 无分歧 tempered → 分歧 tempered——每段的具体引理未在摘要层披露，**传递条件（如 local-global 兼容、特征函数对应）是外部审计的关键靶点**；
2. **eigensheaf 三篇的独立价值**：构造定理（存在性）不依赖等价主定理——若主定理崩塌，构造层仍可独立存活（**族内反脆弱结构**）；
3. 🔴 主等价证明 Gaitsgory–Raskin full-support 猜想（arXiv 2508.02237 Conj 1.3.10）——外部引文真实可查（正面信号），但「证明外部 2025 猜想」的声明强度仍为最高档。

### 2.4 M*L — 数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| 量词范围 | ✅ | 双 regime + 群限制逐篇清晰 |
| 主动边界披露 | ✅✅ | Arthur 增强三不声明 = 库内最佳纪律样本 |
| 外部引用 | ✅ | GLR 2508.02237 / Gaitsgory–Raskin 编号可查 |
| 等价两边的范畴 | 🔴 | 旧审计维持：受限等价的确切范畴（哪些 support）未在摘要层披露 |
| Ramanujan 传递 | 🔴 | 三段传递的每段引理未披露 |

### 2.5 P*D — 编程依存

- 全族 8 篇无 Lean 形式化（无 [Lean] 标记）；
- ⚠️ 但主库 OAI/ 下存在 `GeometricLanglands_PosChar` 相关 comparator 候选名（lean 目录有 GeometricLanglands 文件）——**形式化状态模糊**：CONTENTS.md 族 014 无标记 vs lean/ 目录存在 GL 文件。**行动项：向 OpenAI 核实族 014 的形式化状态口径**（可能形式化了部分支柱而主定理未覆盖，或 CONTENTS.md 未更新）。

### 2.6 P*L — 编程逻辑结构

- 若 GL lean 文件确属族 014 主定理：需按已形式化审计线补 B 岗位回译（参照 UGC 弱化检查法）；
- 不适用部分同族 034：ℓ-adic 层构造（eigensheaf 层）形式化难度极高，零形式化合理。

## 3. 跨层映射检查

| 映射 | 状态 | 风险 |
|---|---|---|
| S → M | ⚠️ | 条件披露优于库内平均；主等价范畴定义仍缺 |
| M → P | ⚠️ | 形式化状态模糊（CONTENTS vs lean/ 目录矛盾） |
| S ↔ P | ⚫ | 待核实后补 |

## 4. 已知外部证据

- **Gaitsgory–Raskin full-support 猜想**（arXiv 2508.02237, 2025）：真实存在的外部锚点——主论文声称证明之，可独立核对猜想陈述；
- **泛型 Ramanujan（函数域例外群）**：Lafforgue（2002, GL_n）+ L. Lafforgue/Genestier（分圆）线之后的自然目标；例外群全 place tempered 若真 = 重大突破（社区 2025 状态：部分情形）；
- 同库无撤回/修复记录涉及本族。

## 5. 判定

| 维度 | 结论 |
|---|---|
| 形式一致性 | ⚫/⚠️ 零标记但 lean/ 目录存疑 |
| 自然语言声明真实性 | 🔴 无法确认（等价主定理 + Ramanujan 收官双纲领级声明） |
| 声明纪律 | ✅✅ 族内三不声明/群限制/双 regime 全披露——**库内最佳** |
| 与已知数学兼容性 | ⚠️ 例外群 Ramanujan 强于 2025 已知；等价证明 2025 猜想——张力大但方向与纲领一致 |
| 依赖链稳健性 | ⚠️ eigensheaf 层独立存活；Ramanujan 链三段传递单线 |

**SMPDL 族级判定**：🔴 **维持（极高风险）但附加正面纪律信号**。相对族 034 的三个差异：(1) 声明纪律显著更好；(2) 外部锚点（GLR 2025 猜想）可独立核对；(3) 形式化状态存在口径矛盾需核实。**风险重心从「声明是否夸张」移向「三段 Ramanujan 传递的技术有效性」。**

## 6. 可执行验证建议（人工补完方向）

1. **E 岗位（最高优先）**：请几何 Langlands 专家（Frenkel/Gaitsgory 学派邻域）审「Temperedness at ramified places」——三段传递的分歧段是否真正无条件（关键：Whittaker 泛函在 ramified place 的行为）；
2. **C 岗位**：核对 lean/OAI 下 GL 文件与族 014 的对应关系——形式化覆盖声明与 CONTENTS.md 的矛盾定案；
3. **B 岗位**：主等价的「restricted」范围回译——受限等价涵盖哪些 singular support（与完整 GL 等价的差距量化）；
4. **A 岗位**：p ∤ |W_G| 条件在例外群的隐性排除（E8 的 p=2,3,5 情形是否被「4 特征假设」覆盖）——概念边界扫描；
5. **跨族对照研究**：族 014（纪律好）vs 族 034（条件藏 by-phrase）的声明纪律差异——建立「声明纪律 → 实际错误率」的 C-4 预测卡（本轮新产出）。

---

## 文献引用纪律检查

| 引用对象 | 真实性 | 支持性 | 说明 |
|---|---|---|---|
| 族 014 全部 8 篇摘要 | ✅ CONTENTS.md 直读 | ✅ | 摘要级族审计 |
| Gaitsgory–Raskin arXiv 2508.02237 | ✅ 可查 | ✅ | 主论文自引，编号明确 |
| 旧审计 GeometricLanglands_PosChar（10-13） | ✅ 本库 | ✅ | 主论文 README 级判定整合 |

**核查结论**：主论文旧 🔴 维持；7 篇新增摘要级审计完成；PDF 级与 lean/ 目录核实待后续工单。

---

## 署名与许可

本审计使用 Göttingen S/M/P × D/L 框架 · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0
