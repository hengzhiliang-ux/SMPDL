# SMPDL 项目总 README

> **项目全称**：Göttingen S/M/P × D/L —— 数学证明与 AI 生成声明的三层依存-逻辑审计框架  
> **维护人**：CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0  
> **本版**：README v1.0（2026-10-14 · 随 Zenodo v3.0）  
> **最新 DOI**：[10.5281/zenodo.23357269](https://doi.org/10.5281/zenodo.23357269)（Concept: 10.5281/zenodo.23318734）

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
- Zenodo 版本线：v15 → **v2.7 → v2.8 → v2.9 → v3.0**（单日四连发；259 份；指纹 `4157e06a…cdd7ba`）；
- 网页入口：[riemann-lecturer](https://riemann-lecturer-04390.app.workbuddy.host/)（43 组 CASES + 22 份元文档全挂载）。

## 四、工单台账（下一轮排期入口）

> 规则：开工前在此登记领取；完成后回写状态；新增工单按 P1/P2/C 编号续排。历史工单池原载 `SMPDL_LawHistoryRefinement_HumanMachineDivision.md` §四。

### P1 流程工单

| # | 工单 | 内容 | 状态 |
|---|---|---|---|
| P1-① | Mathlib 档位证据表 | 13 律形式化扫描 | ✅ 完成（`SMPDL_LawTier_FormalizationEvidence.md`） |
| P1-② | 七阶段全量表 | 27 律定位 | ✅ 完成（律史文档 §1.2） |
| P1-③ | **集群时间线可视化** | 四集群 + G1–G6 + 43 组律 → JSON + 网页挂载（今日体系唯一"未被看见"的出口） | ✅ 完成（2026-10-15 `75b5d8e`：canonical JSON `reports/data/SMPDL_LawTimeline.json`（43 律/5 集群/6 代际/19 事件，cluster 字段仅源文档明示才赋值）+ 自包含交互页 `reports/SMPDL_LawTimeline_Visual.html`（8 泳道/集群带/C5 虚线假说态/双集群徽章/悬停 tooltip/过滤器/G 系纸风）+ 站点 index 挂载；node --check + JSON parse 双 PASS；双档同步） |
| P1-④ | 引用批量核查 | 全库 §8 引用 ≈200 条 Web 验证 | ⬜ 待领 |
| P1-⑤ | 指纹纪律固化 | filelist + 算法 + 换行口径纳入每版归档；历史指纹不可复算问题收口 | ✅ 完成（2026-10-15：重建 `_v22/_v23/_v24_filelist.txt`；立 `filelists/SMPDL_Fingerprint_Method.md`；登记可复现基准 **v24r = `cfb4b21f…629a2`**（raw bytes, filelist 序）；诚实披露 v22/v23/v24 候选指纹原算法未存档、不可复算，完整性判定一律以 v24r 向后滚动） |
| P1-⑥ | 双副本簿记同步 | Paper_and_Data 簿记落后半版（v3.2 簿记 / v3.3 内容）收口 | ✅ 完成（2026-10-15：v24 zip + ATTRIBUTION v24 + DISCLAIMER + 18 份扩容文件同步进 Paper_and_Data；旧 ATTRIBUTION 留档 `archives/SMPDL_ATTRIBUTION_v23_legacy.md`；终验 paper 副本 287/287 与 v24 zip 字节一致、raw 拼接 == v24r ✅） |
| P1-⑦ | 统计全量重跑（43 组） | LawScreening §七「统计纪律框」登记：🔴 率 RR 小样本 3.73 / 大样本 2.24（均探索性、显著性不稳健）；H31–H43 十三组律组强度评级缺登记；§三–§五 分组表未按 43 组重排 | ⬜ 待领（方法：先补 H31+ 强度评级 → 43×2 列联表 → RR+CI+Fisher → 预注册判读口径——防"看结果选口径"） |
| P1-⑧ | 独立审计回收 | 两独立代理（逻辑审计 + OS-6~9 样本外）运行中；报告到 outputs/ 后按缺陷清单修复 + 样本重分拣 | ✅ 完成（2026-10-15：16 缺陷全修复三批收口 git 1f8ce3e/04f5217/349debe；OS-II 独立判定 2✅+2🟡；规则修订 H/②收窄/裁定盲评生效；P3'' 经独立重测存活） |
| **B4-2** | **14 轮前向预测独立盲判重跑** | 🔴-1 根治：预注册三问制判定标准（D1 规模/D2 时间 5 年/D3 功能）+ 14 样本冻结 + git 时间戳存证 + κ 判读规则；**必须独立会话执行**；规格书 = 桌面 `工单_B4-2_独立盲判重跑_2026-10-15.md` | ✅ 完成（2026-10-15 08:19 独立会话：主型 κ=1.00 + 三档 κ=1.00（法证审计剔除冻结回填列后）；v1.2 终版 `f31701d`；三连翻车→纪律 v2.0 `5530dfd` 十关制） |
| **B4-3** | **扩样预注册 + 判定（纪律 v2.0 首例）** | 免回测直接扩样三律（H44 维数不变/H45 单值提升/H46 Hasse 局部-整体）；十关制首次全程执行；规格书 = 桌面 `工单_B4-3_扩样预注册与判定_2026-10-15.md` | ✅ 完成（2026-10-15：登记 `c73aa62` → 冻结 `04d85e9` → 判定 `dada2ff` → 回填 `6fa5dab`，十关全闭；主型 κ=1.00 tier-1 通过、三档 1✅2🟡、三档 κ=N/A（单判定者如实披露）；B4 基线 H45/H46 0/2 受压=预注册声明成立；H46 史实勘误 E1（Lind–Reichardt 1940/42 挠子）；案例库 H43→H46、前向 10/10→13/13） |
| **B4-4** | **异构判定（跨系 κ + 调节子复现）** | 堵「判定者同系」硬伤：J-A 异构 LLM + J-B 人类专家对 B4-2/B4-3 冻结 17 轮重判，算跨系 κ₁/κ₂/κ₃；规格书 = `2026-10-18-00-00-36` 会话目录 `工单_B4-4_异构判定_2026-10-18.md` | ✅ **机器侧全链完成**（2026-10-18 单日：J-A=Kimi 判定 `72704e7` → κ₁ 主型 **0.734** ✅ / 三档 0.316（E4 如实报）`6192399` → 分歧解剖：6/7 三档分歧=D2 锚型单一变量 + 调节子 Fisher p=0.012 `24a8b44` → J-C=DeepSeek + **预注册 P1–P5**（冻结 `4886ef0`）：P1/P4/P5 中（调节子获第二异构系复现；主型 κ=0.854）P2/P3 如实报（R2 三向分裂→分类学边界标本；D1 因果门槛显影=第三判定者变量）`c9e1227` → 外部仲裁三帖实质解决（±π/4=**Cauchy 1814** 一手命中·Grattan-Guinness/Gray；R10=tropical 多源长过程+Litvinov–Maslov 纲领自述=γ 叙事；锚定惯例无正典→Corry 身体/图像框架背书协议修订方向）`5365b74`/`6b8f4ce`/`f4c3abe`；**§7.5 素材全就绪**；J-B 人类判定者未到位（κ₂/κ₃ 悬置，材料包已备）；产物全在 `reports/b4-4/`） |
| C-5 | prior-art 系统检索 | 自铸/借用边界白纸黑字化（部件标签表见 PreservingOperator_Audit §一）；arXiv/ZbL/MathSciNet 查 adjunction+emergence、law removal taxonomy、correspondence theory+history 等关键词族 | ⬜ 待领（**C-1 对外发布硬前置**） |

### P2 研究工单

| # | 工单 | 内容 | 状态 |
|---|---|---|---|
| P2-① | Cabello KS 验证 | 穷举 + 奇偶双确认 | ✅ 完成 |
| P2-② | Univalence 活体档案 | HoTT D→cubical E 实时档位迁移（G6 首个活体样本，含 `#print axioms` 对照） | ⬜ 待领 |
| P2-③ | C5 集群计量 | 2020s 形式化浪潮文献计量（arXiv/mathlib 密度）——第五质疑集群证真/证伪 | ⬜ 待领 |
| P2-④ | **B4 LLM 档位盲判** | n=25 三问盲判 vs 人工基准；≥80% → Law-Gate 可机器化；**须独立会话执行**（避免上下文污染） | ✅ 完成（三轮并读：试点半盲 53% / 正式裸判 63.3% / B4b 判据注入 63.3%；分问分层裁决——Q1 功能类型 90% 文档化可机器化、Q2 涌现主型裸判 90% 机器预填+人工复核、Q3 γ 细分 30% 人工必填；产物 `SMPDL_B4_LLMBlindJudge_Report.md` v3.0 + 三份冻结盲答卷） |

### C 扩展工单（当日新增）

| # | 工单 | 内容 | 状态 |
|---|---|---|---|
| C-1 | arXiv 论文升版 | `SMPDL_arXiv_Paper.md` 吸收律学 + 预测机器 + 库级统计（现落后体系 22 份元文档） | ⬜ 待领 |
| C-2 | 新律扫描周期 | Law-Gate 第八问衍生律归档 → 候选池第二轮（候选：Fubini 类比律/正则性分层律——由 43 组审计中自然涌现） | ⬜ 待领（**10-18 升格为 S8b 唯一新血来源**：候选池已空，见下方 E1 勘误） |
| C-3 | T2 扩样 | T2 n=2+ 偏薄：终止律（Newman 语境）/ 线性推广等候选 | ⬜ 待领 |
| C-4 | 预测机器自动化 | 速查卡九条 + 五步规程 → 可执行 checklist 脚本（与 B4 联动） | ⬜ 待领 |

### 建议排期顺序（下会话）

> **⚠️ 勘误 E1（2026-10-18 全库扫描 · commit `c4e22d6`）——候选池已空**
> `RemovalEmergence_Synthesis §七` 与 `FunctionalType §2.2` 的池表曾长期挂「待验」状态，实际全部池律已于 10-15 随 B4-2 前向轮消费（R5/R7/R8/R9/R10/R11/R12/R14 = H34/H36/H37/H38/H39/H40/H41/H43）。该滞后标记曾误导下游（重审报告 §四.4 → T3 工单 D3），10-18 已全库修复并回写消费状态。
> **影响面**：B4-4（J-A Kimi / J-C DeepSeek 全链）**零影响**——其为已冻结预测的再判定，不依赖池可用性。
> **新规**：① 跨文档消费关系（池→前向轮）**消费当轮必须回写状态列**（本勘误为「材料包泄漏」教训的记账版）；② 新前向候选只从 **C-2 双律**（Fubini 类比律/正则性分层律，零暴露史）或全新律出（反对称律可用；有限性律有 B4 试点暴露史慎选）；③ 本勘误链进 T3 论文 §7.5 诚实披露（记录污染类型①变体：状态滞后污染）。

```
P2-④（B4 盲判——设计就绪，独立会话快赢）
→ P1-③（时间线可视化——体系首次"可见"）
→ C-1（arXiv 升版——对外发布窗口）
→ P2-②/③（活体 + 计量——G6 代纵深）
```

## 五、约定与纪律

- **CRLF/指纹纪律**：curated 清单 = ATTRIBUTION v15 基线 + 新增 md；发布前重算联合 SHA-256；
- **回测纪律 v2.0**（取代旧"预测纪律"三条款）：五阶段协议（登记/冻结/遮蔽/判定/解禁）+ 勘误版本纪律 + 十关 checklist——全文见 `SMPDL_Paper_and_Data/reports/SMPDL_Backtest_Discipline.md`；B4-2 三连翻车（同日自判/材料包泄露/冻结算子列回填）逐条立例；**新回测缺十关不开判**；
- **新律入口**：Law-Gate 第八问（衍生律命名归档）——不经此入口不建新组；
- **许可**：CC BY-NC-SA 4.0；搬运/改写请注明来源与链接。

---

*README v1.0 · 2026-10-14 · 随 v3.0 定稿；工单台账为活页，领取即更新。*
