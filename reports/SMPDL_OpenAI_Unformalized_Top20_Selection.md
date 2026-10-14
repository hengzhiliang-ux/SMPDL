# OpenAI math 库 · 未形式化高关注度手稿 · 20 个深度审计选题（第三批扩容）

**选题日期**：2026-10-14 · CAMPANASILVAE  
**选题框架**：Göttingen S/M/P × D/L v1.5  
**目标**：将深度审计从 60 份扩容至 80 份——锁定「**未 Lean 形式化 × 未审计 × 高关注度**」三向交叉的 20 个结果族

---

## 〇、选题方法与池口径

| 筛层     | 口径                                               | 剩余     |
| ------ | ------------------------------------------------ | ------ |
| 全库     | 372 结果族 / 719 手稿（CONTENTS.md 解析，逐族读 Lean 标记）     | 372    |
| − 已形式化 | `[Lean](lean/docs/NNN.md)` 标记 242 族              | 130    |
| − 已审计  | 60 份既有深度审计主题（归一化标题匹配，en-dash/撇号/变音符三陷阱已修）        | ~85    |
| 关注度打分  | 官方推理摘要族(+3) / 修复撤回史(+2) / 著名猜想名(+1~3) / 多手稿族(+1) | 65 候选  |
| 人工终选   | 声明强度 × 领域多样性 × 家族规模，剔除三处误放行（016/056/004 已审计）     | **20** |

**误放行修正记录**（诚实披露）：

- 016 Zilber–Pink（abelian）——已有 `SMP_ProofAnalysis_OpenAI_ZilberPink_Abelian.md`，剔除；
- 004 Hilbert 第十问题 ℚ——已有 `SMP_ProofAnalysis_OpenAI_HilbertTenth_Rationals.md`，撇号归一化漏配后人工拦截，剔除；
- 056 Termination of Kähler fourfold MMP——已有 `TerminationLogCanonical_KahlerFourfolds` 审计（变音符 ä 归一化漏配后人工拦截），剔除。

---

## 一、终选 20 清单（按族号）

| #  | 族   | 标题                                                                            | 篇数     | 关注度信号                                                        | SMPDL 风险预判                                                | 审计切入点                                  |
| -- | --- | ----------------------------------------------------------------------------- | ------ | ------------------------------------------------------------ | --------------------------------------------------------- | -------------------------------------- |
| 1  | 014 | Restricted geometric Langlands, global Arthur enhancements, generic Ramanujan | **8**  | Langlands+Ramanujan 双名 + 全库第二大族                              | 🔴 声称强度极高（限制性 GL + Arthur 增强 + 泛型 Ramanujan 转移三合一）；零形式化   | S*D 概念奇点：三个巨型对象在一篇族里同时「解决」             |
| 2  | 034 | Log abundance for compact Kähler spaces (log Iitaka subadditivity)            | **14** | **全库最大族** + 修复爆炸半径                                           | 🔴 14 篇互引 = 依赖链多米诺最高危；Kähler MMP 修复区邻接                    | M*D 依赖图：14 篇的引用拓扑 + 修复版边界是否波及          |
| 3  | 036 | Numerical semiampleness and generalized minimal models                        | 4      | 修复史邻接（MMP/Kähler）                                            | 🟡 半正定性「数值 ⇒ 几何」是 MMP 经典险桥                                | M*L 数值半充足 ⇒ 半 ample 的量词条件逐条核           |
| 4  | 046 | Shafarevich counterexamples dim 2 + large fundamental group                   | 2      | Shafarevich 猜想名                                              | 🔴 反例型声明 + 大基本群边界                                         | D 岗位陷阱 VI：反例是否显式构造                     |
| 5  | 069 | Global quantum geometric Langlands at irrational level                        | 1      | Langlands + 量子                                               | 🔴 无理水平全局量子 GL——物理级构造 + 数学严格性缺口天然大                        | S/M 跨层：物理论证 → 数学定理的翻译损耗                |
| 6  | 074 | Kakeya in three and four dimensions                                           | 2      | Kakeya 名问题                                                   | 🔴 与已知最好界对照的声明张力（3D/4D Kakeya 集合维数）                       | C 岗位外部一致性：对照 Katz-Zahl / Wang-Zahl 现有界 |
| 7  | 086 | L³ bound for trilinear Hilbert transform                                      | 1      | Hilbert 变换名 ⚠️ 注：存在 TriangularHilbert comparator，需先核实部分形式化状态 | 🟡 特殊点估计突破（对称点处）                                          | B 岗位：定理陈述点条件 vs 摘要全称声明                 |
| 8  | 178 | Deterministic nonbipartite Ramanujan graphs every fixed degree                | 1      | Ramanujan 图名                                                 | 🔴 与 Marcus-Spielman-Srivastava 线（双部图）的增量声明——非双部显式构造是开放方向 | M*L 显式性验证：确定性构造是否真显式                   |
| 9  | 193 | Serre's intersection-multiplicity conjecture                                  | 1      | Serre 名猜想                                                    | 🔴 交重数猜想（正特征/奇点邻域）长期开放                                    | C 岗位：与已知部分结果（正则环情形）的相容性                |
| 10 | 225 | GFF limits throughout balanced six-vertex regime                              | 1      | 六顶点模型 + GFF                                                  | 🟡 相变全程 GFF 极限——物理严格化地带                                   | D 岗位陷阱 IV：不同相区收敛模式切换                   |
| 11 | 270 | Threshold and positive-energy bound states of BFSS matrix model               | 2      | 数学物理（BFSS/矩阵模型）                                              | 🔴 物理直觉驱动证明的数学化鸿沟                                         | S*M 双层：能隙下界的物理假设显式化                    |
| 12 | 286 | Rigidity and arithmetic of lattice von Neumann algebras                       | 2      | von Neumann 代数名                                              | 🔴 格子 vN 代数刚性 + 算术——与 Connes 嵌入问题邻接                       | A 岗位：算术性质在刚性框架中的定义合法性                  |
| 13 | 300 | Approximation and quadratic strong-operator paving                            | 2      | Kadison-Singer/paving 邻域                                     | 🟡 paving 族增量结果                                           | M*D 与 MSS 定理的定量比较                      |
| 14 | 304 | Hilbert–Smith conjecture in every dimension                                   | 1      | Hilbert 名 + 拓扑名猜想                                            | 🔴 全维 HS 猜想（p-adic 作用不存在）长期开放                             | C 岗位：已知 1-3 维结果上界的声明跳跃                 |
| 15 | 310 | Quillen's conjecture in rational homology                                     | 1      | Quillen 名                                                    | 🔴 有理同调 Quillen 猜想（有限群作用）                                 | M*D 与 Quillen 原猜想的强弱关系刻画               |
| 16 | 335 | Gromov's integral scalar-curvature bound (simplicial volume)                  | 2      | Gromov 名                                                     | 🔴 数量曲率下界 × 简单体积——大范围几何硬区                                 | D 岗位：曲率积分不等式的常数与边界                     |
| 17 | 338 | Yau's uniformization conjecture                                               | 1      | Yau 名                                                        | 🔴 单值化猜想（完备 Kähler 型分类）                                   | A 岗位：猜想陈述的完备 Kähler 流形类边界              |
| 18 | 349 | Solomon–Yau least-volume conjecture                                           | 1      | Yau 名                                                        | 🔴 最小体积猜想                                                 | C 岗位：下界构造与已知例子的相容性                     |
| 19 | 352 | A finite-time singularity of Calabi flow                                      | 1      | Calabi 流名                                                    | 🔴 有限时间奇点构造——几何流大新闻型声明                                    | D 岗位陷阱 VI：奇点构造的显式性                     |
| 20 | 364 | Kinetic limits and fluctuations over Boltzmann lifespan                       | 2      | PDE 动理学（**修复率 35% 的高危域**）                                    | 🔴 PDE/几何分析域 = AI 最弱肌群（结构性统计结论）                           | 全六格：连续估计类推理逐段检查                        |

---

## 二、领域分布与结构说明

| 域             | 数量 | 族号                 |
| ------------- | -- | ------------------ |
| 表示论/Langlands | 2  | 014, 069           |
| 代数几何/交换代数     | 4  | 034, 036, 046, 193 |
| 调和分析          | 2  | 074, 086           |
| 组合/图论         | 1  | 178                |
| 概率/统计力学       | 1  | 225                |
| 数学物理          | 1  | 270                |
| 算子代数          | 2  | 286, 300           |
| 拓扑            | 2  | 304, 310           |
| 微分几何/几何分析     | 4  | 335, 338, 349, 352 |
| PDE/动理学       | 1  | 364                |

- 分布与语料结构统计 v1.0 的领域权重基本同构（AG 偏重），但**刻意纳入 PDE 1 例（364）与数学物理 2 例（270, 225）**——对准「修复率 35% 的 AI 最弱肌群」；
- 🔴 预判 14 / 🟡 预判 6——🔴 率高于全库基线，符合「按声明强度优先抽审」的选样策略（结构性偏差已披露）；
- 族规模覆盖：最大族 034（14 篇）+ 第二大族 014（8 篇）均入选——依赖链多米诺风险最大的两个簇。

## 三、执行建议

1. **审计顺序**：先 034 / 014（族规模×声明强度双高）→ 再 PDE 物理带（364/270/225）→ 后单篇名猜想（304/310/338/349/352）；
2. 每份沿用六格审计模板（命题 → 六格 → 跨层映射 → 外部证据 → 判定 → 可执行验证建议）；
3. **086 入审前先核实** TriangularHilbert comparator 是否已覆盖主陈述（若覆盖则转入已形式化审计线）；
4. 全部完成后深度审计数达 80 份，占 372 族的 21.5%——可做第二轮语料级统计推断。

---

## 文献引用纪律检查

| 引用对象                     | 真实性                   | 支持性                    | 说明                 |
| ------------------------ | --------------------- | ---------------------- | ------------------ |
| CONTENTS.md（openai/math） | ✅ 本轮直拉 638KB          | ✅                      | 族标题/篇数/Lean 标记逐族解析 |
| formalization.yaml v0.4  | ✅ 本轮直拉                | ✅                      | 已形式化排除层            |
| 60 份既有审计清单               | ✅ 本库资产                | ✅                      | 归一化匹配三处漏配已人工修正并披露  |
| 关注度信号（推理摘要/修复史/著名名）      | ✅ 官方 README + history | ⚠️ 打分为主观权重，排序稳健性未做扰动检验 |                    |

---

## 署名与许可

**Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0**

