# SMPDL — OpenAI 700+ 数学证明语料 SMPDL 审计

> Göttingen S/M/P × D/L 数学证明审查方法论 · OpenAI 700+ 数学证明高危样本审计

[![DOI](https://zenodo.org/badge/DOI-10.5281/zenodo.23344975.svg)](https://doi.org/10.5281/zenodo.23344975)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSE)

---

## 快速入口

| 入口 | 链接 |
|---|---|
| **GitHub Pages 首页** | `https://hengzhiliang-ux.github.io/SMPDL` |
| **Zenodo 论文/数据记录** | https://zenodo.org/records/23344975 |
| **WorkBuddy 交互页面** | https://riemann-lecturer-04390.app.workbuddy.host/ |
| **141 份报告联合 SHA-256** | `9afb6a321d1164f1d62798ba8d1711ea947d3813fff297e7759b91861d47957c` |

---

## 这是什么？

**SMPDL**（Semantic / Mathematical / Programming × Dependency / Logic）是一个三层两维的数学证明与 AI 生成声明审查框架：

- **S** 语义层、**M** 数学层、**P** 编程层
- **D** 内生依存、**L** 逻辑结构
- 配套：**TRAP-CHECK** 七类陷阱检查、**五人工岗位**（A/B/C/D/E）、**反前视五步协议**、**文献引用纪律**（真实性核查 + 支持性核查）

本仓库是 Göttingen 数学史索引项目对 [OpenAI math 仓库](https://github.com/openai/math)（719 余份手稿）进行高危抽样的审计产物，同时包含经典证明、构造尝试与方法论文件。

---

## 仓库结构

```
.
├── README.md                              # 本文件（仓库首页）
├── index.md                               # GitHub Pages 首页
├── LICENSE                                # CC BY-NC-SA 4.0
├── DISCLAIMER.md                          # OpenAI 原始内容引用声明
├── _config.yml                            # GitHub Pages / Jekyll 配置
├── reports/                               # 100 份 Markdown 报告
│   ├── SMPDL_Framework.md                 # 方法论框架 v2.3
│   ├── SMPDL_Audit_SampleSuite.md           # 样本总览表
│   ├── SMPDL_ATTRIBUTION.md                 # 署名、指纹、DOI
│   ├── SMPDL_Citation_Discipline.md         # 文献引用纪律
│   ├── SMPDL_HistoryRetrospective_10PromisingSamples.md # 十个最有希望样本数学史回溯
│   ├── SMP_ProofAnalysis_*.md               # 经典证明/猜想审计
│   ├── SMPDL_Construct_*.md                 # 构造尝试（含反前视）
│   ├── SMP_ProofAnalysis_OpenAI_*.md        # OpenAI 样本审计
│   └── SMPDL_Compare_OpenAI_*_PrePostFix.md # 修复前后对比
├── archives/                              # 官方归档 zip
│   ├── SMPDL_v2.0_sample_reports_76files.zip
│   ├── SMPDL_v2.1_sample_reports_86files.zip
│   ├── SMPDL_v2.2_sample_reports_96files.zip
│   └── SMPDL_v2.5_sample_reports_141files.zip
└── zenodo/                                # Zenodo metadata
    ├── zenodo_metadata_v2.0.json
    ├── zenodo_metadata_v2.1.json
    └── zenodo_metadata_v2.2.json
```

---

## 报告清单

### 方法论与指南

- [SMPDL_Framework.md](reports/SMPDL_Framework.md) — 方法论框架 v2.3
- [SMPDL_Audit_SampleSuite.md](reports/SMPDL_Audit_SampleSuite.md) — 样本总览与教学分组
- [SMPDL_ATTRIBUTION.md](reports/SMPDL_ATTRIBUTION.md) — 署名、许可、指纹、DOI
- [SMPDL_Citation_Discipline.md](reports/SMPDL_Citation_Discipline.md) — 文献引用纪律
- [SMPDL_HumanMachine_Division.md](reports/SMPDL_HumanMachine_Division.md) — 人机分工
- [SMPDL_HumanRoles_Definitions.md](reports/SMPDL_HumanRoles_Definitions.md) — 五人工岗位定义
- [SMPDL_HumanReview_HighMidRisk_Guide.md](reports/SMPDL_HumanReview_HighMidRisk_Guide.md) — 高/中风险审查指南
- [SMPDL_TrapForesight_Taxonomy.md](reports/SMPDL_TrapForesight_Taxonomy.md) — TRAP-CHECK 七类陷阱
- [SMPDL_MachineAntiForesight_Feasibility.md](reports/SMPDL_MachineAntiForesight_Feasibility.md) — 机器反前视可行性
- [SMPDL_ProofConstruction_AntiForesight.md](reports/SMPDL_ProofConstruction_AntiForesight.md) — 反前视构造协议
- [SMP_Isomorphism_Checklist.md](reports/SMP_Isomorphism_Checklist.md) — 同构检查清单
- [SMP_OpenAI700_Corpus_AuditMethodology.md](reports/SMP_OpenAI700_Corpus_AuditMethodology.md) — OpenAI 语料审计方法论
- [SMPDL_HistoryRetrospective_10PromisingSamples.md](reports/SMPDL_HistoryRetrospective_10PromisingSamples.md) — 十个最有希望样本数学史回溯
- [SMP_RH_Diagnostic_ProofDirections.md](reports/SMP_RH_Diagnostic_ProofDirections.md) — RH 证明方向诊断
- [SMP_NearestProven_Theorems_UnsolvedConjectures.md](reports/SMP_NearestProven_Theorems_UnsolvedConjectures.md) — 邻近定理与开放猜想

### 经典证明审计

- [SMP_ProofAnalysis_Euclid_Primes.md](reports/SMP_ProofAnalysis_Euclid_Primes.md) — 欧几里得素数无限
- [SMP_ProofAnalysis_AllTrianglesIsosceles.md](reports/SMP_ProofAnalysis_AllTrianglesIsosceles.md) — 所有三角形都是等腰的（谬误）
- [SMP_ProofAnalysis_Kempe_FourColor.md](reports/SMP_ProofAnalysis_Kempe_FourColor.md) — Kempe 四色证明（谬误）
- [SMP_ProofAnalysis_Sqrt2_Irrational.md](reports/SMP_ProofAnalysis_Sqrt2_Irrational.md) — √2 无理数
- [SMP_ProofAnalysis_HarmonicSeries_Divergence.md](reports/SMP_ProofAnalysis_HarmonicSeries_Divergence.md) — 调和级数发散
- [SMP_ProofAnalysis_Ramsey33_Six.md](reports/SMP_ProofAnalysis_Ramsey33_Six.md) — Ramsey(3,3)=6
- [SMP_ProofAnalysis_Cantor_Diagonal.md](reports/SMP_ProofAnalysis_Cantor_Diagonal.md) — Cantor 对角线
- [SMP_ProofAnalysis_OddSum_Square.md](reports/SMP_ProofAnalysis_OddSum_Square.md) — 前 n 个奇数和为 n²
- [SMP_ProofAnalysis_AMGM_Two.md](reports/SMP_ProofAnalysis_AMGM_Two.md) — AM-GM 二元形式
- [SMP_ProofAnalysis_Pigeonhole_Principle.md](reports/SMP_ProofAnalysis_Pigeonhole_Principle.md) — 鸽巢原理
- [SMP_ProofAnalysis_Basel_Problem.md](reports/SMP_ProofAnalysis_Basel_Problem.md) — Basel 问题
- [SMP_ProofAnalysis_Wilson_Theorem.md](reports/SMP_ProofAnalysis_Wilson_Theorem.md) — Wilson 定理
- [SMP_ProofAnalysis_FermatLittle_Theorem.md](reports/SMP_ProofAnalysis_FermatLittle_Theorem.md) — Fermat 小定理
- [SMP_ProofAnalysis_FermatNumbers_PrimeConjecture.md](reports/SMP_ProofAnalysis_FermatNumbers_PrimeConjecture.md) — Fermat 素数猜想（证伪）
- [SMP_ProofAnalysis_EulerSumPowers_Conjecture.md](reports/SMP_ProofAnalysis_EulerSumPowers_Conjecture.md) — Euler 幂和猜想（证伪）
- [SMPDL_ResearchProof_AppelHaken_FourColor.md](reports/SMPDL_ResearchProof_AppelHaken_FourColor.md) — Appel–Haken 四色定理
- [SMPDL_Retro_Review.md](reports/SMPDL_Retro_Review.md) — 回顾综述

### 构造尝试（含反前视协议）

- [SMPDL_Construct_Euclid_Primes.md](reports/SMPDL_Construct_Euclid_Primes.md)
- [SMPDL_Construct_Isosceles_Fallacy.md](reports/SMPDL_Construct_Isosceles_Fallacy.md)
- [SMPDL_Construct_Sqrt2_Irrational.md](reports/SMPDL_Construct_Sqrt2_Irrational.md)
- [SMPDL_Construct_Cantor_Diagonal.md](reports/SMPDL_Construct_Cantor_Diagonal.md)
- [SMPDL_Construct_OddSum_Square.md](reports/SMPDL_Construct_OddSum_Square.md)
- [SMPDL_Construct_AMGM_Two.md](reports/SMPDL_Construct_AMGM_Two.md)
- [SMPDL_Construct_Pigeonhole_Principle.md](reports/SMPDL_Construct_Pigeonhole_Principle.md)
- [SMPDL_Construct_Wilson_Theorem.md](reports/SMPDL_Construct_Wilson_Theorem.md)
- [SMPDL_Construct_FermatLittle_Theorem.md](reports/SMPDL_Construct_FermatLittle_Theorem.md)
- [SMPDL_Construct_Basel_Problem.md](reports/SMPDL_Construct_Basel_Problem.md)
- [SMPDL_Construct_RH_MomentsRoute.md](reports/SMPDL_Construct_RH_MomentsRoute.md)
- [SMPDL_Construct_AndrewsCurtis.md](reports/SMPDL_Construct_AndrewsCurtis.md)
- [SMPDL_Construction_SampleSuite.md](reports/SMPDL_Construction_SampleSuite.md)
- [SMPDL_Construct_AndrewsCurtis_HumanChecklist.md](reports/SMPDL_Construct_AndrewsCurtis_HumanChecklist.md)

### OpenAI 最新发表样本审计

- [SMP_ProofAnalysis_OpenAI_Kaplansky_DirectFiniteness.md](reports/SMP_ProofAnalysis_OpenAI_Kaplansky_DirectFiniteness.md)
- [SMP_ProofAnalysis_OpenAI_FPRAS_PerfectMatchings.md](reports/SMP_ProofAnalysis_OpenAI_FPRAS_PerfectMatchings.md)
- [SMP_ProofAnalysis_OpenAI_MaxCut_Hardness.md](reports/SMP_ProofAnalysis_OpenAI_MaxCut_Hardness.md)
- [SMP_ProofAnalysis_OpenAI_SelmerConverse_EveryPrime.md](reports/SMP_ProofAnalysis_OpenAI_SelmerConverse_EveryPrime.md)
- [SMP_ProofAnalysis_OpenAI_TerminationLogCanonical_KahlerFourfolds.md](reports/SMP_ProofAnalysis_OpenAI_TerminationLogCanonical_KahlerFourfolds.md)
- [SMP_ProofAnalysis_OpenAI_GFF_LipschitzHeights_TwoArc.md](reports/SMP_ProofAnalysis_OpenAI_GFF_LipschitzHeights_TwoArc.md)
- [SMP_ProofAnalysis_OpenAI_BSD_LowSelmerCorank.md](reports/SMP_ProofAnalysis_OpenAI_BSD_LowSelmerCorank.md)
- [SMP_ProofAnalysis_OpenAI_QuasiRiemannHypothesis.md](reports/SMP_ProofAnalysis_OpenAI_QuasiRiemannHypothesis.md)
- [SMP_ProofAnalysis_OpenAI_Hodge_CM_AbelianVarieties.md](reports/SMP_ProofAnalysis_OpenAI_Hodge_CM_AbelianVarieties.md)
- [SMP_ProofAnalysis_OpenAI_HilbertTenth_Rationals.md](reports/SMP_ProofAnalysis_OpenAI_HilbertTenth_Rationals.md)
- [SMP_ProofAnalysis_OpenAI_FreeGroupFactors_Isomorphism.md](reports/SMP_ProofAnalysis_OpenAI_FreeGroupFactors_Isomorphism.md)

### OpenAI 已修复/证伪样本审计

- [SMP_ProofAnalysis_OpenAI_TamingCompatibility_Sep23_Fixed.md](reports/SMP_ProofAnalysis_OpenAI_TamingCompatibility_Sep23_Fixed.md)
- [SMP_ProofAnalysis_OpenAI_AshkinTeller_JointScaling_Sep25_Fixed.md](reports/SMP_ProofAnalysis_OpenAI_AshkinTeller_JointScaling_Sep25_Fixed.md)
- [SMP_ProofAnalysis_OpenAI_FiniteOrdinaryMMP_KahlerFourfolds_Sep24_Fixed.md](reports/SMP_ProofAnalysis_OpenAI_FiniteOrdinaryMMP_KahlerFourfolds_Sep24_Fixed.md)
- [SMP_ProofAnalysis_NavierStokes_LostInTranslation.md](reports/SMP_ProofAnalysis_NavierStokes_LostInTranslation.md)

### 修复前后对比

- [SMPDL_Compare_OpenAI_TamingCompatibility_PrePostFix.md](reports/SMPDL_Compare_OpenAI_TamingCompatibility_PrePostFix.md)
- [SMPDL_Compare_OpenAI_AshkinTeller_JointScaling_PrePostFix.md](reports/SMPDL_Compare_OpenAI_AshkinTeller_JointScaling_PrePostFix.md)
- [SMPDL_Compare_OpenAI_FiniteOrdinaryMMP_PrePostFix.md](reports/SMPDL_Compare_OpenAI_FiniteOrdinaryMMP_PrePostFix.md)

### 辅助文件

- [SMPDL_arXiv_Paper.md](reports/SMPDL_arXiv_Paper.md) — arXiv 投稿版本/早期草稿

---


---

## v2.5 新增同构-异基础案例组（H1–H10）

新增 30 份审计报告与 4 份元分析文档，将 curated 报告数从 107 扩展至 **141**：

- H1：欧氏 ↔ 球面几何（三角形内角和）
- H2：微分 ↔ 差分方程（指数增长模型）
- H3：有限 ↔ 无限图（最小度 ≥ 2 与环存在性）
- H4：交换 ↔ 非交换环（二项式幂）
- H5：特征 0 ↔ 特征 p（Freshman's Dream）
- H6：标准 ↔ 非标准分析（导数定义）
- H7：经典 ↔ 直觉主义逻辑（存在性证明）
- H8：ZFC ↔ ZF（向量空间基存在性）
- H9：集合论 ↔ 类型论（n + 0 = n）
- H10：经典 ↔ 可计算分析（中间值定理）

新增元分析文档：
- `SMPDL_HistoricalOrder_Index.md`：数学史顺序索引
- `SMPDL_HistoricalAssumption_CognitiveLogic.md`：假设基础认知历史逻辑
- `SMPDL_TuningParameter_Matrix.md`：调参来源矩阵
- `SMPDL_HistoricalMigration_Skeleton.md`：数学史迁移骨架分析

完整清单见 `reports/SMPDL_Audit_SampleSuite.md`。

## 版本信息

| 项目 | 当前值 |
|---|---|
| 方法论版本 | v2.5 |
| 论文版本 | v14 |
| 页面版本 | v5.93 |
| DOI | [10.5281/zenodo.23344975](https://doi.org/10.5281/zenodo.23344975) |
| 报告数量 | 141 份 curated |
| 联合 SHA-256 | `9afb6a321d1164f1d62798ba8d1711ea947d3813fff297e7759b91861d47957c` |

---

## 如何使用

1. **阅读总览**：从 [SMPDL_Audit_SampleSuite.md](reports/SMPDL_Audit_SampleSuite.md) 开始，了解样本分类与教学分组。
2. **学习方法论**：阅读 [SMPDL_Framework.md](reports/SMPDL_Framework.md) 与 [SMPDL_Citation_Discipline.md](reports/SMPDL_Citation_Discipline.md)。
3. **查看审计结论**：点击上方报告清单中的任意链接，GitHub 会自动渲染 Markdown。
4. **下载完整归档**：访问 [archives/SMPDL_v2.0_sample_reports_76files.zip](archives/SMPDL_v2.0_sample_reports_76files.zip) 或 Zenodo 记录。
5. **验证指纹**：在 `reports/` 目录下按 [SMPDL_ATTRIBUTION.md](reports/SMPDL_ATTRIBUTION.md) 中的顺序 `cat` 所有文件并计算 SHA-256。

---

## 引用

如使用本仓库内容，请引用 Zenodo DOI：

```bibtex
@misc{smpdl2026,
  title={A Three-Layer Dependency-and-Logic Audit for Mathematical Proofs and AI-Generated Claims: The S/M/P × D/L Framework},
  author={CAMPANASILVAE},
  year={2026},
  howpublished={\url{https://doi.org/10.5281/zenodo.23344975}},
  doi={10.5281/zenodo.23344975}
}
```

---

## 许可

本仓库原创内容采用 [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](LICENSE) 许可。

关于 OpenAI math 仓库原始 README 的引用声明，请见 [DISCLAIMER.md](DISCLAIMER.md)。
