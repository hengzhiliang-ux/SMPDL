# SMPDL 项目总 README

> **项目全称**：Göttingen S/M/P × D/L —— 数学证明与 AI 生成声明的三层依存-逻辑审计框架  
> **维护人**：CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0  
> **本版**：README v1.1（2026-10-14 · 随 Zenodo v3.1）  
> **最新 DOI**：[10.5281/zenodo.23358578](https://doi.org/10.5281/zenodo.23358578)（Concept: 10.5281/zenodo.23318734）

---

## 一、这是什么

一个用于**审计数学证明（尤其是 AI 生成的）**的结构化方法论，以及围绕它生长出的三样东西：

1. **审计框架**：S/M/P（语义/数学/编程三层）× D/L（依存/逻辑两维）六格矩阵——任何证明在哪个格坏掉、坏在哪一层，可定位、可教学、可逐步机械化；
2. **案例库**：**H1–H43**（43 组"同构证明、异基础"对比，129 份报告）——同一证明骨架在两种数学基础下的双向审计，覆盖几何到 tropical 代数 30+ 领域；
3. **理论层**：律学三维分类（强度×档位×功能）、移除-涌现两阶段理论（前向预测 **10/10**）、γ 五形态、预测机器与压测-执行-重测质检环。

另有**语料级应用**：OpenAI 700+ 证明库（719 手稿/372 族）全量结构统计——AI 证明集中域、高危域、完成度分布与人类对照。

## 二、库结构速览

| 目录/文件族 | 内容 |
|---|---|
| `SMP_ProofAnalysis_*.md`（158） | 单体审计（经典证明/谬误/OpenAI 手稿 57 份深度审计） |
| `SMPDL_Compare_*_PrePostFix.md`（46） | H1–H43 对比组 + 早期对比 |
| `SMPDL_Construct_*.md` | 反预察构造样本（欧几里得/AC 等） |
| **16 份元文档**（下表） | 框架/律学/涌现/预测/质检/回顾 |
| `SMPDL_ATTRIBUTION.md` | 版本表 + 指纹 + 许可 |
| `ks_cabello18_verify.py` | KS 构型机器验证脚本 |

### 16 份元文档导航（按阅读顺序）

| # | 文档 | 一句话 |
|---|---|---|
| 1 | `SMPDL_Framework.md` | 六格矩阵本体 |
| 2 | `SMPDL_Audit_SampleSuite.md` | 全案例总览（入口） |
| 3 | `SMPDL_HistoricalOrder_Index.md` | H1–H43 历史序索引 |
| 4 | `SMPDL_Isomorphism_Taxonomy.md` | 同构标签判定标准 |
| 5 | `SMPDL_TuningParameter_Matrix.md` | 调参旋钮矩阵 |
| 6 | `SMPDL_HistoricalMigration_Skeleton.md` | 迁移骨架分析 |
| 7 | `SMPDL_HistoricalAssumption_CognitiveLogic.md` | 认知历史映射 |
| 8 | `SMPDL_CognitiveLogic_TreeMap.md` | 五簇树图 |
| 9 | `SMPDL_MigrationParameter_Correlation.md` | 旋钮簇关联 |
| 10 | `SMPDL_LawStructure_MigrationScreening.md` | 律伴随筛选 + E/D/I 档位 |
| 11 | `SMPDL_LawGrouping_TierMigrationTimeline.md` | 七阶段 + 四集群 + G1–G6 |
| 12 | `SMPDL_LawHistoryRefinement_HumanMachineDivision.md` | 27 律全量表 + 人机分工 |
| 13 | `SMPDL_LawTier_FormalizationEvidence.md` | Mathlib 档位证据表 |
| 14 | `SMPDL_RemovalEmergence_Synthesis.md` | 移除-涌现三型 + 14 轮回验 |
| 15 | `SMPDL_FunctionalType_Reclassification.md` | T 分类学 + 两阶段理论（v2.0） |
| 16 | `SMPDL_P2_1_CabelloKS_VerificationReport.md` | KS 机器验证 |
| — | **总纲与专题（5 份）** | ↓ |
| 17 | `SMPDL_MasterMethodology_Synthesis.md` | **总纲**（迁移与升降档方法论） |
| 18 | `SMPDL_PredictionMethodology_Roadmap.md` | 预测机器（五步规程 + 路线图） |
| 19 | `SMPDL_StressTest_BLine_Report.md` | 压测 + 执行轮 |
| 20 | `SMPDL_RetroTest_UpgradedTheory.md` | 重测轮 |
| 21 | `SMPDL_TheoryEvolution_Retrospective.md` | **理论全链回顾单卷**（新手从这里读） |
| 22 | `SMPDL_OpenAI_Corpus_StructureStatistics.md` | OpenAI 372 族统计 |

## 三、当前状态（2026-10-14 终态）

- 案例库 **H1–H43 / 129 份**；律候选池 **14 条全量清零**；
- 前向回验 **10/10**；T1 n=8 / T2 n=2+ / T3 n=3；跨域锚 8 个；学科级涌现 5 例；
- Zenodo 版本线：v15 → v2.7 → v2.8 → v2.9 → v3.0 → **v3.1**（同日五连发；v3.1 = 268 份；指纹 `6b41bcde…55c9286`；含 B4 盲判三轮 + 预测机器 C-4）；
- 网页入口：[riemann-lecturer](https://riemann-lecturer-04390.app.workbuddy.host/)（43 组 CASES + 22 份元文档全挂载）。

## 四、工单台账（下一轮排期入口）

> 规则：开工前在此登记领取；完成后回写状态；新增工单按 P1/P2/C 编号续排。历史工单池原载 `SMPDL_LawHistoryRefinement_HumanMachineDivision.md` §四。

### P1 流程工单

| # | 工单 | 内容 | 状态 |
|---|---|---|---|
| P1-① | Mathlib 档位证据表 | 13 律形式化扫描 | ✅ 完成（`SMPDL_LawTier_FormalizationEvidence.md`） |
| P1-② | 七阶段全量表 | 27 律定位 | ✅ 完成（律史文档 §1.2） |
| P1-③ | **集群时间线可视化** | 四集群 + G1–G6 + 43 组律 → JSON + 网页挂载（今日体系唯一"未被看见"的出口） | ⬜ 待领 |
| P1-④ | 引用批量核查 | 全库 §8 引用 ≈200 条 Web 验证 | ⬜ 待领 |

### P2 研究工单

| # | 工单 | 内容 | 状态 |
|---|---|---|---|
| P2-① | Cabello KS 验证 | 穷举 + 奇偶双确认 | ✅ 完成 |
| P2-② | Univalence 活体档案 | HoTT D→cubical E 实时档位迁移（G6 首个活体样本，含 `#print axioms` 对照） | ⬜ 待领 |
| P2-③ | C5 集群计量 | 2020s 形式化浪潮文献计量（arXiv/mathlib 密度）——第五质疑集群证真/证伪 | ⬜ 待领 |
| P2-④ | **B4 LLM 档位盲判**（设计已定稿于压测报告 §B4） | n=25 三问盲判 vs 人工基准；≥80% → Law-Gate 可机器化；**须独立会话执行**（避免上下文污染） | ⬜ 待领 |

### C 扩展工单（当日新增）

| # | 工单 | 内容 | 状态 |
|---|---|---|---|
| C-1 | arXiv 论文升版 | `SMPDL_arXiv_Paper.md` 吸收律学 + 预测机器 + 库级统计（现落后体系 22 份元文档） | ⬜ 待领 |
| C-2 | 新律扫描周期 | Law-Gate 第八问衍生律归档 → 候选池第二轮（候选：Fubini 类比律/正则性分层律——由 43 组审计中自然涌现） | ⬜ 待领 |
| C-3 | T2 扩样 | T2 n=2+ 偏薄：终止律（Newman 语境）/ 线性推广等候选 | ⬜ 待领 |
| C-4 | 预测机器自动化 | 速查卡九条 + 五步规程 → 可执行 checklist 脚本（与 B4 联动） | ⬜ 待领 |

### 建议排期顺序（下会话）

```
P2-④（B4 盲判——设计就绪，独立会话快赢）
→ P1-③（时间线可视化——体系首次"可见"）
→ C-1（arXiv 升版——对外发布窗口）
→ P2-②/③（活体 + 计量——G6 代纵深）
```

## 五、约定与纪律

- **CRLF/指纹纪律**：curated 清单 = ATTRIBUTION v15 基线 + 新增 md；发布前重算联合 SHA-256；
- **预测纪律**：先登记后入库；偏差与命中等权登记；预测不得事后修饰（修订以修订案追加）；
- **新律入口**：Law-Gate 第八问（衍生律命名归档）——不经此入口不建新组；
- **许可**：CC BY-NC-SA 4.0；搬运/改写请注明来源与链接。

---

*README v1.0 · 2026-10-14 · 随 v3.0 定稿；工单台账为活页，领取即更新。*
