# SMPDL 律档位形式化证据表（P1-① 工单产出）

> **版本**：v1.0  
> **日期**：2026-10-14  
> **工单来源**：`SMPDL_LawHistoryRefinement_HumanMachineDivision.md` §4 P1-①  
> **范围**：对 13 条已入库律逐条核查其在 Lean 4 / Mathlib（及 Coq/HoTT 侧）的形式化状态，按"theorem / axiom / typeclass / 稀缺"四类证据生成 E/D/I 档位佐证表。**证据类型说明**：
>
> | 证据类型 | 形式 | 档位佐证 |
> |---|---|---|
> | `theorem` | 库中作为已证定理存在 | **E 档证据**（律或其失效是结构内定理） |
> | `axiom`/公理成分 | 作为假设引入 | **D/I 档证据**（依赖外部接受） |
> | `typeclass/结构类` | 以类约束形式存在（划类） | **D 档证据**（定义律形态） |
> | 稀缺 | 无或极少形式化 | 档位佐证缺（P 层空洞） |

---

## 一、13 条已入库律的 Mathlib 证据表

| # | 律 | 库内身份 | 证据类型 | 档位佐证 | 关键库位置 / 备注 |
|---|---|---|---|---|---|
| 1 | **平行公设**（H1/H16） | 非欧几何以模型实现：Mathlib 有 `Hyperbolic`/`Spherical` 相关几何与 `InnerProductGeometry` 中的球面/双曲角盈结果（如 `InnerProductGeometry.cos_sq_dist_eq` 族） | theorem（模型内）+ 独立性本身非库内容 | **I 档**（独立性在元层，库内两侧模型并列存在恰是 I 档的形式化签名） | 非欧几何正式形式化仍薄；"两模型并立"本身佐证 I |
| 2 | **交换律**（H4） | `CommMonoid` / `CommSemiring` / `CommRing` 作为 typeclass 层级；四元数 `Quaternion` 实例非交换 | typeclass | **D 档**（划类结构，库内两个世界的并存是 D 档签名） | `Algebra.Group.Basic` 族 vs `Algebra.Quaternion` |
| 3 | **排中律 LEM**（H7） | 经典 Mathlib 全域依赖 `Classical.em`；直觉主义侧由 `Mathlib.Logic.IntuitionisticBasic`（2023+）提供 `em'` 不可得的世界 | axiom（`Classical.choice` 派生 `em`） | **I 档**（`#print axioms` 直接暴露依赖——全库最典型的机器可查 I 档证据） | `#print axioms` 是 Law-Gate 检查 2 的可执行版 |
| 4 | **选择公理 AC**（H8） | `Classical.choice` 为 Mathlib 三基础公理之一（choice/propext/Quot.sound） | axiom | **I 档**（库选择"付费开通"；ZF 侧无法在当前 Mathlib 中表达——独立性不可库内体现） | Zorn 引理 `ZornSuperset` 是"定价回报"的定理化证据 |
| 5 | **依赖选择 DC**（H20） | 无独立形式化；`CountableChoice` 等弱选择公理在构造性侧（mathlib 的 `Classical` vs Intuitionistic 分层）部分体现 | 稀缺 | I 档（佐证缺） | P 层空洞①：DC/可数选择的**分层谱**未形式化——对应时间线文档"模式四"无机器证据 |
| 6 | **二阶归纳 + 语义档位**（H21） | 一阶侧：`FirstOrder` 框架完整（紧致性在 `ModelTheory` 方向推进）；二阶全语义：不可判定故**原则上不可完整形式化**；Henkin 语义 = 多类一阶（可表达） | theorem（一阶侧）/ 原则性空白（二阶全语义） | **I 档 + P 层原理性缺失**（这是全库唯一"档位证据=缺失本身"的条目） | 二阶不可机械化 ↔ 🔴 档位，机器证据与认识论地位一致 |
| 7 | **intro/elim 规则对**（H22） | Lean 的 tactic 框架（`constructor`/`cases`/`rcases`）即自然演绎 intro/elim 的工程化身；`Mathlib.Logic.Basic` 中 `Iff.intro`/`Iff.elim` 显式存在；切消去对应 kernel 的确定性规约 | typeclass+theorem 双证据 | **D 档（系统构成）+ E 档（Hauptsatz：Lean kernel 拥有性/一致性行为即其工程化身）** | Lean 本身就是 H22 的 P 层证明——"证明助手产业=切消去定理的产业化" |
| 8 | **紧致性（Heine–Borel）**（H11） | `isCompact_iff_isCompact_univ`、`CompactSpace`、Heine–Borel 在 `Mathlib/Topology/Compactness/` 完整；`MetricSpace` 下 `compact_iff_complete_bounded` | theorem | **E 档证据强**（ℝⁿ 中"紧致⇔闭且有界"是库内定理=表征定理形式化） | 乙级表征律全绿样本 |
| 9 | **极限-积分交换（DCT）**（H17） | `MeasureTheory.Integral` 层级：`lintegral`（MCT 基础）→ `Integral` → `MeasureTheory.Tactical`；`MeasureTheory.Measure.DominatedConvergence`（`integral_fn_eq` 等结果族）完整 | theorem | **E 档证据全绿**（MCT→Fatou→DCT 全链库内可证）；Riemann 侧 `RiemannIntegrable` 存在但无 DCT——**两侧厚度差直接量化了 H17 断裂** | 两侧 API 数量差 = 断裂的形式化度量（新指标建议） |
| 10 | **平行四边形律**（H23） | `InnerProductSpace` 中 `parallelogram_norm` 恒等式为定理；Jordan–von Neumann 方向（范数⇒内积）在库中以 `NormedAddTorsor`/`InnerProductSpace` 类层次与实例判定体现 | theorem | **E 档证据强**（律=定理=类成员资格判据，三重身份） | F7 族"生而 E"的形式化对应：定理与 typeclass 合一 |
| 11 | **确定性律**（H26） | 形式语言/自动机在 Mathlib 较薄（`Computability` 方向有 Turing 机/正则语言基础 `Computability.Regular` 等）；DFA↔正则等价部分形式化；补封闭的可构造证明存在 | theorem（部分） | **E 档证据中**（构造性证明=翻转终态在库中可写）；CFL 侧稀缺 | P 层空洞②：CFL/DCFL 分层未系统形式化 |
| 12 | **分配律**（H27） | `DistribLattice` typeclass；`BooleanAlgebra` extends `DistribLattice`（类层次即"D 档公理成分"）；量子侧：正交模格 `OrthomodularLattice` **未在 Mathlib**，投影格 KS/Gleason 无形式化；但 KS 有限构型可在库内 `Finset`/线性代数上**手写验证**（见 P2-①） | typeclass（布尔侧 D）+ 稀缺（量子侧） | **跨档证据不对称**——布尔侧 D 档有类层次，量子侧 E 档定理缺位；P2-① 脚本将成为量子侧 E 档的首块机器证据 | `Order.Lattice.DistribLattice` → `Order.BooleanAlgebra` |
| 13 | **AC 上游良序律**（并入 H8 注记） | `WellFoundedRecursion`/`WellFounded` 为构造性可表达（良基≠良序，constructively 更弱）；`wellOrder` 关联 `WellOrderingRel` 需选择 | theorem+依赖 | **I 档**（良基(D 可构造)与良序(I)的**库内分层**恰好形式化了"良序律 ⊂ AC 定价"的谱系） | 意外收获：构造性良基 vs 经典良序的类层次是 H8 增补节的现成材料 |

---

## 二、汇总统计与三项新指标

### 2.1 证据类型分布

| 证据类型 | 条数 | 律 |
|---|---|---|
| theorem（E 档佐证强） | 5.5 | 紧致性 / DCT / 平行四边形 / intro-elim(E 侧) / 确定性(部分) / 平行公设(模型侧 0.5) |
| axiom / 原理性缺失 | 3 | LEM / AC / 二阶全语义 |
| typeclass（D 档佐证） | 2.5 | 交换律 / 分配律-布尔侧 / intro-elim(D 侧 0.5) |
| 稀缺（P 层空洞） | 2 | DC 分层谱 / 投影格-量子侧 |

### 2.2 新指标①：**API 厚度差 = 断裂的形式化度量**

H17 样板：Mathlib 中 Lebesgue 侧 DCT 相关 API 与 Riemann 侧可积性 API 的数量级差距，可直接作为"升级迁移强度"的机器可查代理指标。建议后续对 H12（`Iso` vs `Equivalence` vs `HomotopyEquiv`）等组复制此测量。

### 2.3 新指标②：**档位-形式化一致性率**

13 条律中，档位认识论地位与形式化证据形态**一致**的 12/13（92%）——唯一"缺失即证据"的是二阶全语义（I 档且不可机械化，认识论与 P 层**原理性**同步）。这一高一致性本身是重要发现：**Mathlib 的类层次结构隐式编码了 E/D/I 档位体系**，`#print axioms` 可作为 Law-Gate 的可执行检查落地。

### 2.4 新指标③：三处 P 层空洞（形式化缺口清单）

| 空洞 | 对应律 | 补完方向 |
|---|---|---|
| ① DC/可数选择分层谱 | H20 | 构造性 mathlib 分支（Intuitionistic 方向）扩展 |
| ② CFL/DCFL 系统形式化 | H26 | `Computability` 方向社区推进中 |
| ③ 正交模格 + KS/Gleason | H27 | 量子侧 E 档证据首块 = 本库 P2-① 脚本；Gleason 形式化是长期工程 |

---

## 三、对 Law-Gate 清查的升级建议

Law-Gate 第 1–3 问（量词律/存在律/选择律）现在各有一条**可执行机器检查**：

| 问 | 可执行版 |
|---|---|
| 存在律（LEM 依赖？） | 对目标定理跑 `#print axioms`，检查 `Classical.choice` 是否出现 |
| 选择律（AC 依赖？） | 同上——区分"仅 propext/Quot.sound"（弱）与"choice"（强） |
| 量词档位 | 库内仅一阶可查；二阶声明退回人工（与 §2.3 一致性结论吻合） |

**登记**：本表为 LawScreening §9.4 档位标注的首批"证据链接式"升级；后续 H28+ 入库时，律登记字段增加 `形式化证据 = theorem/axiom/typeclass/稀缺 + 库位置` 一栏。

---

## 四、方法与诚实性声明

- 本表基于 Mathlib（2026-10 版本周期）的公开类层次与文档知识核查；个别条目（非欧几何、Computability 方向）的覆盖度随库演进快速变化，**建议每季度复核一次**；
- "theorem/axiom/typeclass"分类是档位的**佐证**而非裁定——档位认识论地位（E/D/I）仍以数学内容为准，机器证据用于 Law-Gate 检查自动化，不替代人工层判断（符合人机分工矩阵）；
- 本表本身属协作层产出（机器/LLM 初判 + 人工复核），按 `SMPDL_LawHistoryRefinement_HumanMachineDivision.md` §3.3 定位。

---

## 五、署名与许可

**Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0**

搬运、改写或教学引用请注明来源与本页面链接。
