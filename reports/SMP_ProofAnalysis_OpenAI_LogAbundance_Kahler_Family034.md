# SMPDL 审计报告：OpenAI「Log abundance for compact Kähler spaces」（族 034 全量）

**审计对象**：Log abundance for compact Kähler spaces under logarithmic Iitaka subadditivity（族 034，14 篇手稿，全库最大族）
**来源**：OpenAI math 仓库，2026-09-24 至 10-07 分批发布
**审计日期**：2026-10-14
**审计框架**：Göttingen S/M/P × D/L 六格审计 v1.5（族级全量升级：单篇 README 级 → 14 篇族拓扑级）
**审计结论**：🔴 **研究级高冲击声明 + 全库最高依赖链密度。主定理（Kähler log abundance 全维）以「假设对数 Iitaka 次可加性」为前提——前提本身是未解决问题；族内 14 篇形成多层条件嵌套结构，条件传递路径必须逐段核验。**

---

## 1. 命题与声明

族 034 顶层声明（三合一定理）：
1. **主结果**：假设对数 Iitaka 次可加性（logarithmic Iitaka subadditivity）⇒ 正规紧 Kähler log canonical 配对（有效有理边界）上的 log abundance 全维成立：解析 nef ℚ-Cartier adjoint ⇒ 半 ample；
2. **射影版**：特征零代数闭域上射影 log abundance + 光滑射影变体的有效 Iitaka 纤维化猜想；
3. **指数猜想**：半 log canonical log Calabi–Yau 配对的有限有理系数指数猜想（固定维数 + 固定系数集 ⇒ 一致指数，与分量数无关）。

### 1.1 族内 14 篇手稿拓扑（按依赖角色分层）

| 层 | 手稿 | 角色 | 关键条件/结论 |
|---|---|---|---|
| **主层** | Log abundance for compact Kähler（10-06） | 族主论文 | **假设** log Iitaka 次可加性 ⇒ Kähler log abundance |
| 主层 | Log abundance in characteristic zero（09-24） | 射影主定理（无条件！） | 射影 log canonical + nef ⇒ 半 ample（特征零全维） |
| **支柱层** | Uniform log Iitaka fibrations（10-04） | 次可加性支柱（d≥5） | 一致多重典范系统生成 Iitaka 场 |
| 支柱层 | Uniform Pluricanonical Iitaka Fibrations（10-03） | 有效 Iitaka 猜想（无条件） | 每维一个度数定义 Iitaka 纤维化 |
| 支柱层 | Uniform effective log Iitaka for fourfolds（09-26） | 四维版支柱 | 有限有理系数情形 |
| 支柱层 | Relative denominators / log CY fibrations（09-27） | log CY 纤维化支柱 | 一致平凡化度数 + moduli b-除子 |
| **非消失层** | Fourfold nonvanishing by minimal metrics（09-27） | 四维非消失 | K 伪有效 ⇒ H⁰(mK) ≠ 0 |
| 非消失层 | Minimal metrics and interior injectivity（09-27） | 分析工具 | 极小度量存在 + 零 Lelong 数 + H¹-注入 |
| 非消失层 | Lifting sections from reduced support（09-27） | 截面提升 | dlt 配对上 abundance after nonvanishing |
| 非消失层 | Schnell fiber spaces（09-24） | Campana–Peternell 不等式 | κ(X) ≥ κ(D) + 纤维化等式 |
| **Kähler 桥层** | Conditional good minimal models for Kähler fourfolds（10-06） | 条件 GMM | **假设** orbifold Iitaka 次可加性 + nef 四维 adjoint abundance |
| Kähler 桥层 | Abundance after nonvanishing for Kähler fourfolds（09-27） | 半 ample 桥 | 解析 nef + 有截面 ⇒ 半 ample |
| **算术层** | Arithmetic Stein-degree bounds（09-25） | Birkar Stein 度猜想 | log CY 配对的域扩张度一致界 |
| 算术层 | Uniform indices for slc log CY（10-05） | 指数猜想收官 | 一致 Cartier 指数（与分量数无关） |

---

## 2. S/M/P × D/L 六格审计（族级）

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| Kähler log abundance 全维 | log Iitaka 次可加性（**假设**）+ 射影 abundance | ⚠️ 条件前提为开放问题——「假设 X 证明 Y」语义已披露，但族主页只说 proves 不说 conditional |
| 射影 log abundance（特征零） | Uniform Iitaka 支柱层 + 提升层 | 🔴 无条件全维声明——强度远超社区共识（abundance 猜想本身开放） |
| 指数猜想（slc log CY） | 一致化支柱 + 已有 ≤3 维定理 | ⚠️ 固定维数+固定系数集的一致界，量词结构已披露 |
| Birkar Stein 度猜想 | —（独立） | ⚠️ 收缩到点形式（contraction-to-a-point formulation）——需核对是否为完整猜想的等价形式 |

**S*D 发现**：族描述用「Using logarithmic Iitaka subadditivity, proves log abundance」——把假设藏在 by-phrases 里，主声明读起来像无条件。**语义忠实性风险点 #1**。

### 2.2 S*L — 语义逻辑结构

- 量词结构：主定理「every dimension」+「effective rational boundary」+「analytically nef ⇒ semiample」——量词链完整；
- ⚠️ 「analytically nef」（解析 nef）vs 射影版「nef」：两版定理的 nef 概念不同域（解析 vs 代数），跨版推理需显式桥接；
- 🔴 条件嵌套深度：Kähler 四重态 GMM 论文假设「orbifold Iitaka 次可加性 **和** nef 四维 adjoint abundance」——后者是另一篇的结论、前者又是开放假设，**条件叠加未在族描述中分层披露**。

### 2.3 M*D — 数学依存（族拓扑分析——本轮核心增量）

14 篇的条件流向图（提取自各摘要的条件从句）：

```
[假设] log Iitaka subadditivity (open conjecture)
    │
    ├─→ 主论文: Kähler log abundance (conditional)
    │        │
    │        ←── Abundance after nonvanishing (Kähler 4-fold, 无条件)
    │        ←── Conditional GMM (假设 orbifold subadd + 4-fold abundance)
    │
[无条件支柱]
    ├─→ Log abundance char 0 (射影, 无条件) ←─ Schnell fiber spaces
    │        ←─ Lifting sections ←─ Minimal metrics (分析工具)
    │        ←─ Uniform Iitaka (d≥5) / Fourfold Iitaka (d=4)
    │
[算术层]  Stein degree + Uniform slc indices (相对独立)
```

**M*D 发现**：
1. **双主定理结构**：族内同时存在条件版（Kähler）与无条件版（射影 char 0）——射影版是无条件全维 abundance，**这本身是重大突破级声明**（abundance 猜想全维无条件解决 = 冲击 Shokurov/Kollár 纲领核心）；
2. **无条件射影版依赖链**：射影 abundance ← Schnell 纤维空间 + 截面提升 + 极小度量 + 一致 Iitaka——每篇各自无条件，但**组合后的整体证明长度 ≈ 14 篇 × 平均数十页**，人审成本极高；
3. 🔴 **依赖链多米诺**：若 Uniform Iitaka（10-04，d≥5）有缺口，射影 abundance 全维崩塌；若 Minimal metrics 有分析缺口，非消失层崩塌——单点失效 ⇒ 族级雪崩（与 Weil classes 3 篇连锁撤回同构风险）。

### 2.4 M*L — 数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| 量词范围 | ✅ | 各篇量词结构清晰（固定维/固定系数集） |
| 条件披露 | 🔴 | 族主页未分层披露条件嵌套；「conditional GMM」标题有 conditional 但族描述省略 |
| 概念边界 | ⚠️ | 「analytically nef」「globally strongly ℚ-factorial」等非标准术语的精确定义域待查 |
| 一致界有效性 | ⚠️ | 「uniform index independent of number of components」的一致界是否存在有效常数（摘要未给数值）——**有效性质疑点** |
| 操作交互 | ✅ | Iitaka 纤维化/半 ample 的复合运算无序次问题 |

### 2.5 P*D — 编程依存

- 全族 **14 篇均无 Lean 形式化**（CONTENTS.md 无 [Lean] 标记）；
- 🔴 与同库 Kähler 四重态修复区（FiniteOrdinaryMMP/Termination/Ashkin–Teller 修复版）主题高度交叠：族 036（numerical semiampleness）、族 056（termination Kähler fourfold）为近邻——**Kähler MMP 是本库已发生 3 撤回 14 修复的高危带**；
- 无 reasoning summary、无 comparator、无任何机器检查。

### 2.6 P*L — 编程逻辑结构

- 不适用（零形式化）——但反面角度：**全库 242/372 族已 Lean 化 vs 本族 0/14**——最大族完全绕过机器检查，与「~42% top-line 形式化」的官方口径形成结构性反差；
- ⚠️ 反差解释假设：(a) 解析方法（极小度量/Lelong 数）难形式化——合理；(b) 选择性形式化（易的做、难的放）——若成立则形式化覆盖率指标失真。

---

## 3. 跨层映射检查

| 映射 | 状态 | 风险 |
|---|---|---|
| S → M | 🔴 | 族描述「Using X, proves Y」掩盖条件结构；conditional 与 unconditional 双主定理并列易误读 |
| M → P | ⚫ | 零形式化——无机器锚点，全部依赖人审 |
| S ↔ P | ⚫ | 同上 |

## 4. 已知外部证据

- **与已知数学的张力**：射影 log abundance（char 0 全维无条件）若为真，是 abundance 猜想的完全解决——**超过 2025 年社区最好已知**（已知：d≤3 完整 + d=4 大量情形；全维无条件 = 纲领级突破）。外部一致性检查最高优先；
- **同库交叉**：族 056（Termination Kähler fourfold，已有审计）与族 036（numerical semiampleness）是近邻依赖；Ashkin–Teller/MMP 修复史证明该团队 Kähler 方向曾出错并修复——**先验失败率非零**；
- 2026-10-07 撤回 3 篇均在 Hodge/Weil 方向，不在本族；修复 14 篇中 Kähler MMP 占 4 篇（本族邻接带）。

## 5. 判定

| 维度 | 结论 |
|---|---|
| 形式一致性 | ⚫ 零形式化 |
| 自然语言声明真实性 | 🔴 **无法确认**：无条件射影 abundance 全维 = 纲领级突破，超社区共识 |
| 构造可验证性 | ⚠️ 一致界数值未披露（有效性存疑） |
| 与已知数学兼容性 | 🔴 张力极大（abundance 猜想全维开放） |
| 依赖链稳健性 | 🔴 14 篇多层嵌套，单点失效族级雪崩 |

**SMPDL 族级判定**：🔴 **全库最高优先人工审计对象**。三层风险叠加：(1) 声称强度（abundance 纲领级）；(2) 条件结构复杂（conditional/unconditional 双主定理 + 条件嵌套未分层披露）；(3) 零形式化 + 最大族依赖链。**旧审计（FiniteOrdinaryMMP/Termination 单篇）覆盖 < 15% 族内容，本轮为族级首审。**

## 6. 可执行验证建议（人工补完方向）

1. **E 岗位（最高优先）**：请双有理几何/MMP 专家审「Log abundance in characteristic zero」（09-24 射影主定理）——若证明有效，是纲领级结果；重点核 Schnell 纤维空间层与截面提升层的接口；
2. **C 岗位**：画 14 篇完整引用图（含版本时间线 09-24→10-07 三轮迭代），标注每个「假设」的来源与去处——条件传递路径全披露；
3. **B 岗位**：核对族主页「Using X proves Y」表述 vs 主论文「Assume X, We prove Y」——条件披露等级差异；
4. **D 岗位**：一致界数值验证——「uniform index」是否给出显式常数（依赖 DCC 集合的有限性论证是否有效）；
5. **A 岗位**：「analytically nef」vs「nef」在 Kähler 非射影范畴的定义合法性（解析 nef 的理论尚未完全标准）。

---

## 文献引用纪律检查

| 引用对象 | 真实性 | 支持性 | 说明 |
|---|---|---|---|
| 族 034 全部 14 篇摘要 | ✅ CONTENTS.md 直读 | ✅ | 本报告仅基于官方摘要级审计 |
| 旧审计（FiniteOrdinaryMMP/Termination） | ✅ 本库 | ✅ | 用于邻接带失败率先验 |
| Gaitsgory–Lafforgue–Raskin 等外部引用 | ⚠️ | ⚠️ | 属族 014 引用，此处不展开 |

**核查结论**：本报告为**摘要级族审计**；PDF 级逐篇审计待后续工单。

---

## 署名与许可

本审计使用 Göttingen S/M/P × D/L 框架 · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0
