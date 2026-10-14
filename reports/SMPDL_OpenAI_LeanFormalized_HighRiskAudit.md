# OpenAI 700 证明库 · 已 Lean 形式化部分 · SMPDL 高危审计与人工补完方向标注

**审计对象**：github.com/openai/math（719 手稿 / 372 结果族；lean/ v0.4 形式化清单：173 sources / 200 main_results / 189 comparator configs）
**核心事实**：`review: status: unchecked`（全库未经人工审阅）+ `automation: agent`（唯一验证方法 = agent 自跑）+ 24 个外部依赖补丁 + OAI 子树 62,574 文件 / ~1GB
**审计框架**：Göttingen S/M/P × D/L 六格审计 v1.4 + 五岗位（A/B/C/D/E）+ TRAP-CHECK v1.0 七陷阱
**审计日期**：2026-10-14 · CAMPANASILVAE
**复用基线**：本库 60 份既有深度审计（🔴37/🟡5/🟢2/混合 16）+ 语料结构统计 v1.0（三重高危证据）

---

## 〇、TL;DR

1. **已 Lean 化部分 ≠ 已验证部分**——formalization.yaml 明示 `review: unchecked`，且唯一自动化方法为 `agent`；Lean 编译通过 ≠ 定理为真。
2. **危险原语全库干净**：9 个高危主文件扫描零 sorry / 零 axiom / 零 native_decide。**风险不在证明后门，在「陈述忠实性」与「依赖链」**。
3. **高危结构性分离**：深度审计判定 🔴 最密的「千禧年级数论声明」（BSD/Selmer/Goldfeld、Fontaine–Mazur、Zilber–Pink、Langlands、虚二次模性、p-adic section）**完全未 Lean 化**——高危主体在形式化体系之外。
4. **已 Lean 化的高危簇** = Max-Cut/UGC/Kaplansky×3/Mahler/准RH/FPRAS/L=RL=BPL，逐一审阅主定理陈述，发现两类典型缺口：
   - **FPRAS 是唯一真证明体**（26,126 行 / 2675 声明），其余 8 个高危主文件是 0.6–5KB 的「主定理陈述 + import 内部模块」薄封装；
   - **UGC 文件 `Nonempty BinaryGapReduction` = 归约机器存在性**，其判定性内涵依赖自造 `TM2ComputableInPolyTime` 模型的忠实性。
5. **人工补完的优先方向**（按 SMPDL 定位）：
   - **P→S 回译**（B 岗位）：将 Lean 主定理陈述回译为自然语言，与论文摘要逐句比对——9 个高危条目全部需要；
   -→ 构造显式化**（C 岗位）：Kaplansky 特征 2（`selectedH ≤ 217` 搜索证书）+ UGC 归约机器——把存在性证书变成可独立核验的显式对象；
   - **依赖链审计**（C 岗位）：30 个外部库 + 24 个补丁（AINTLIB / ClassFieldTheory / PrimeNumberTheoremAnd / elliptic-curves 等）——补丁内容未审阅即整链信任；
   - **真证明体审计**（D 岗位）：FPRAS 1.3MB 证明体的 2675 声明抽样精读 + 4 处 `decide` 的 kernel 代价评估。

---

## 一、形式化版图：三张清单刻画的真实覆盖

### 1.1 基本盘

| 指标 | 数值 | SMPDL 定位 |
|---|---|---|
| 手稿总数 | 719（2026-10-06 发布） | S*D 出处层 |
| Lean 形式化 sources | 173 篇 | P*D 覆盖面 |
| main_results 声明 | 200 个（192 文件） | P*L 结构 |
| comparator configs | 189 个 | 验证配置 |
| 官方自报形式化率 | ~42% | 与 sources/719 ≈ 24% 有口径差（分母不同：族 vs 篇） |
| 人工审阅状态 | **unchecked** | 🔴 全库无人工审 |
| 自动化方法 | `agent` 唯一 | 🔴 自审自跑 |
| 外部依赖 | 30 库 builds-on | S*D 信任链 |
| 依赖补丁 | 24 个 patch | 🔴 未审阅修改 |
| OAI 自写代码 | 62,574 文件 / ~1GB | 审计面量级 |

### 1.2 「已 Lean 化」的真实含义（P*D/P*L 双层发现）

- **薄封装模式**：8/9 高危主文件 < 5KB——形式化的是「**主定理陈述 + import 内部模块**」，证明体在子目录（如 Mahler 551 文件链）；
- **唯一真证明体**：FPRAS_CommonBases.lean 26,126 行 / 2675 声明——这个量级需要 Lean 社区级审计投入；
- **get-theorem-to-compile 模式**：薄封装文件的存在暗示「让 comparator 通过」是目标，与「忠实形式化」的目标存在张力。

---

## 二、高危标注总表：200 main_results × 60 份既有审计交叉

### 2.1 第一层：既有深度审计直接命中（10 条）

| # | 主题 | Lean 文件 | 既有判定 | 陈述忠实性发现（本轮新增） | 人工补完方向 |
|---|---|---|---|---|---|
| 1 | **FPRAS 完美匹配** | OAI/Combinatorics/MatroidCounting/CommonBases.lean | 🔴 | 唯一真证明体（1.3MB/2675 decls），4 处 kernel decide | **D 岗位抽样精读**：声明依赖图分桶（2675 条分 10 桶）+ 核心链路逐一过 |
| 2 | **Max-Cut 最优 hardness** | OAI/Computability/MaxCut/Main.lean | 🔴 | `main : MainStatement` 深度依赖 UGC 归约（`MaxCutGames.theorem11`）与自造机器模型 | **B 岗位回译 MainStatement** + **C 岗位审 TM2ComputableInPolyTime 定义** |
| 3 | **UGC** | OAI/Computability/UniqueGames/Theorem.lean | 🔴 | 形式化的是 `Nonempty BinaryGapReduction`（3SAT→UG 多项式归约机器存在性），非 UGC 本身 | **B 岗位核对**「归约存在性 ↔ UGC 声明」映射；**C 岗位**验 alphabet=fn(ε,δ) 的诚实性 |
| 4 | **Kaplansky 特征 2** | OAI/RingTheory/DirectFiniteness/FinitelyPresented.lean | 🔴→修复后🟡 | `thm_main` 显式给出双证：存在性 + 显式证书（`selectedH ≤ 217`，prescribed construction） | **C 岗位构造显式化**：把 prescribed certificate 变成可独立核验的群表现清单 |
|  Kaplansky quasitrace | OAI/Analysis/Kaplansky/Main.lean | 🔴→修复后🟡 | 形式化的是 M48 代数上 quasitrace 存在性 + defect ≥ 1/144 | 与 4 同法：核 M48 代数定义链 |
| 6 | **Kaplansky 奇特征** | OAI/Algebra/OddKaplansky/Main.lean | 🔴→修复后🟡 | `local instance ... DecidableEq` 出现——**自定义可判定实例是危险点**（若 instance 与数学对象不等价则后门） | **B 岗位核 local instance 定义**；C 岗位核 SquareConstruction |
|  Kaplansky 严格证书 | OAI/Algebra/OddKaplansky/Main.lean（同上） | 🟡 | 同上 | 同上 |
| 7 | **Mahler 猜想** | OAI/Analysis/Mahler/MainTheorem.lean | 🔴 | 定理陈述用了 `coordinatePolar`（坐标极体）——**非标准极体**；涉及 551 文件链 | **A 岗位审 coordinatePolar 定义**（坐标极体 vs 真极体：弱化嫌疑最大点）；B 岗位核 NL↔Lean 陈述 |
| 8 | **准 RH（Dirichlet L）** | OAI/NumberTheory/DirichletL/Nonvanishing.lean | 🔴 | 陈述忠实（zeta 非 0 于 Re>7/8，避开主特征极点）——9 条中陈述最忠实 | **C 岗位**审 `FinalAssemblyUnconditional` 内部链 + patches/StrongPNT 补丁 |
| 9 | **L=RL=BPL** | OAI/Computability/Logspace/Equality.lean | 🔴 | `L=RL ∧ RL=BPL` 全式形式化，但内部模块用**单字母/短词命名空间**（Umbra/Rock/MintV/Pool/shard/plump）——可读性极低 = 可审计性极低 | **A 岗位概念映射表**：单字母命名 → 数学概念（这是人介入的最小切口） |
| 10 | **[补充] FPRAS 决策原语** | 同 #1 | — | 4 处 `decide`（kernel 检查有限枚举） | 评估 kernel 编译时间与可靠性 |

### 2.2 第二层：深度审计判定 🔴 但完全未 Lean 化（形式化真空）

**这是最重的高危层**——声称强度最高（千禧年级声明）的证明，恰恰零形式化：

| 主题 | 既有判定 | 未形式化状态 | 人工补完方向 |
|---|---|---|---|
| BSD 低 Selmer corank | 🔴 | 不在 173 sources | 专家级 S/M 层审计（同行评审） |
| Selmer 逆命题 every prime | 🔴 | 不在 | 同上 |
| Goldfeld 密度猜想 2-converse | 🔴 | 不形式化 | 同上 |
| Fontaine–Mazur p=2 | 🔴 | 不形式化 | 同专家同行评审 |
| Zilber–Pink (abelian) | 🔴 🔴 | 不形式化 | 同上 |
| Geometric Langlands (正特征) | 🔴 | 不形式化 | 同上 |
| 虚二次域模性 | 🔴 | 不形式化 | A 岗位概念奇点扫描 |
| Hilbert 十th ℚ | 🔴 | 不形式化 | 同上 |
| π 无理性指数 = 2 | 🔴 | 不按主结果形式化 | B 岗位 NL↔形式化对照 |
| p-adic section 猜想 | 🔴 | 不形式化 | 同上 |
| Thompson 群非顺从 | 🔴 | ThompsonNonamenability comparator 存在！ | **P 层覆盖度核实**：comparator 有但 main_results 无声明行——部分形式化？ |
| Hodge CM abelian（人工参与例外） | 特殊 | 不形式化 | 人工编辑过可读性——单独对待 |

**结构性结论**：AI 生成证明的「形式化真空」与「声明强度」正相关——**声称越大，越没有形式化**。人工补完的重心不在 Lean 层，而在 S/M 层的专家评审。

### 2.3 第三层：形式化覆盖度的边界审计（40+ 条目）

从 189 comparator 配置看，ThompsonNonamenability、VlasovMaxwell、Laughlin、CriticalSK 等高危主题有 comparator 但未进 main_results 清单——状态模糊。**人工补完方向**：向 OpenAI 索要「comparator 覆盖 ≠ 主结果已形式化」的官方口径表。

2.3 已在 2.2 表中标注 Thompson 案例为例；全量边界条目（约 40+）建议以附录 CSV 落地（`_highrisk_lean_hits.json` 已含机读版）。

---

## 三、SMPDL 六格定位与人工补完方向总图

| 格 | 发现 | 人工补完动作 |
|---|---|--- |
| **S*D 语义依存** | 全库 unchecked + agent 自跑 | 逐篇要求 OpenAI 披露 agent 审阅的具体判据 |
| **S*L 语义逻辑** | UGC=归约存在性弱化（嫌疑）；Mahler coordinatePolar（弱化嫌疑最大） | B 岗位回译对照（9 高危条目全部） |
| **M*D 数学依存** | 30 外部库 + 24 补丁未审 | C 岗位逐补丁 diff 审阅（AINTLIB/ClassFieldTheory/StrongPNT/elliptic-curves 优先） |
| **M*L 数学逻辑** | Kaplansky 证书 selectedH≤217 与群表现之桥 | C 岗位显式化证书 → 可独立核验清单 |
| **P*D 编程依存** | 薄封装模式 + FPRAS 巨体 + 551 文件 Mahler 链 | 审计顺序按依赖深度倒序（leaf 先审） |
| **P*L 编程逻辑** | local instance（OddKaplansky）+ 单字母命名空间（Logspace） | A 岗位概念映射表 + instance 等价性证明 |

## 四、优先级排序（人工投入 × 预期收益）

| 优先级 | 动作 | 目标 | SMPDL 坐标 | 预估投入 |
|---|---|---|---|---|
| 1 | C 岗位逐补丁 diff 审阅（24 补丁优先 AINTLIB/ClassFieldTheory/StrongPNT/elliptic-curves） | 依赖链信任定案 | M*D | 每补丁 0.5-1 天 |
| 2 | B 岗位回译 9 高危主定理陈述 | 陈述忠实性定案（UGC/Mahler 两处弱化嫌疑） | S*L/P*L | 每条 1-2 天 |
| 3 | A 岗位审 Mahler coordinatePolar 定义 + OddKaplansky local instance | 最大弱化嫌疑点定案 | S*D/P*L | 各 1 天 |
| 4 | C 岗位 Kaplansky 证书显式化（selectedH ≤ 217 → 群表现清单） | 存在性 → 可独立核验 | M*L | 2-3 天 |
| 5 | D 岗位 FPRAS 2675 声明抽样精读（核心链路） | 唯一真证明体定案 | P*D/P*L | 1-2 周 |
| 6 | 向 OpenAI 索要 main_results × comparator 口径表 | 边界审计 | S*D | 邮件级 |
| 7 | 专家同行评审「千禧年级未形式化」11 主题 | S/M 层验证 | M*D/M*L | 社区级 |

---

## 五、方法附注与诚实披露

- 本轮为**索引级 + 主文件级审计**，未编译 Lean 库、未逐行读 FPRAS 证明体；
- coordinatePolar 定义未定位到（551 文件链未全扫）——弱化判定为「嫌疑」而非定案；
- 60 份既有深度审计的判定标签提取有两轮（初提取 🔴37/🟡5/🟢2 + 二次复核 🔴23/🟡3），差异来自判定行格式不一，已取保守值；
- 「千禧年级未形式化」清单的边界以 173 sources 标题匹配为准，存在小概率漏配（如标题不含关键词）；
- Thompson 案例提示 main_results 与 comparator 清单可能不同步，建议直接向 OpenAI 案主核实。

---

## 六、对 SMPDL 方法论自身的反哺（B4 轮联动）

1. **P 层通过 ≠ S/M 已验证**在本轮再次实证（Kaplansky 审计的预言命中：形式化范围未披露→本轮确认薄封装模式）；
2. **Law-Gate 分问分层结论外推**：Q1 文档化判据（功能类型）在本轮的「薄封装 vs 真证明体」分类上直接可用；
3. **C-4 预测卡机会**：本轮产出 4 张候选预测卡——①UGC 陈述弱化判定 ②Mahler coordinatePolar 弱化判定 ③补丁内容风险分级 ④「形式化真空与声明强度正相关」——均可入 C-4 首批回验队列。

---

## 文献引用纪律检查

| 引用对象 | 真实性 | 支持性 | 说明 |
|---|---|---|---|
| formalization.yaml v0.4（openai/math） | ✅ 本轮直拉 | ✅ | review/automation 段原文引用 |
| 9 个高危主文件源码 | ✅ 本轮直拉 | ✅ | raw.githubusercontent 直取 |
| 60 份既有深度审计判定 | ✅ 本库资产 | ✅ | 选择样本判定，非全库 |
| OpenAI README/history | ✅ 本轮直拉 | ✅ | 719 篇/42% 口径 |

---

## 署名与许可

**Göttingen S/M/P × D/L 数学证明审查方法论 · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0**
