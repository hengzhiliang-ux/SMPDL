# Readme

This repository contains mathematical manuscripts and supporting proof artifacts produced by an internal OpenAI model. 

As part of model development, we evaluate our models on open research problems. We expanded these evaluations after performance on our existing mathematical evaluations saturated. Some outputs build upon earlier results produced by the models.

This collection includes results at different stages of verification. Not all have accompanying Lean formalizations. We will continue to update this repository with Lean formalizations as we obtain them. 

Some of the unformalized results could have issues. We will endeavor to fix any such issues quickly.
We are also exploring community-hosted repositories for these materials. 

## Navigating the collection

The current catalogue contains 719 manuscripts organized into 372 families. A family groups related papers, which may include a principal result, companion arguments, consequences, or alternative proofs. Each family is classified by mathematical discipline.

- Start with the [overview](overview.pdf) for descriptions of the families.
- Use the [manuscript map](CONTENTS.md) to find individual papers and their supporting materials.
- The [`preprints/`](preprints/) directory contains PDFs, source files, and manuscript-specific citation and build instructions.
- The [Lean library](lean/README.md) and [formalization catalogue](lean/formalization.yaml) describe the available formal proofs, their associated papers, and verification configurations. See the [Comparator instructions](lean/ComparatorChallenges/README.md) for additional checking instructions. The repository has ~42% top-line results formalized.
- Updates to the repo are described in the [history](history.md).

### Reasoning summaries

We are also releasing abridged summaries of the model's reasoning, covering the following results:

| Family | Subject |
|---|---|
| **GitHub Pages 首页** | `https://hengzhiliang-ux.github.io/SMPDL` |
| **Zenodo 论文/数据记录** | https://zenodo.org/records/23339747 |
| **WorkBuddy 交互页面** | https://riemann-lecturer-04390.app.workbuddy.host/ |
| **107 份报告联合 SHA-256** | `055a1154abae60bd2dfd6a4b6b48c492b6ee23c69458f0da036fc20fc581e870` |


## How the results were produced

The vast majority of results were obtained with the same procedure using an unreleased internal OpenAI model. On average, each result used three hours of ChatGPT Pro thinking compute with that model. Over the course of the evaluation, the model was posed approximately 4,000 problems. Aggregating the output into result families and manuscripts and requiring an appropriate level of significance led to the catalog outlined above.

Exceptions to this fixed procedure include work on a zero-free region for the Riemann zeta function and proof of the Hodge Conjecture for CM abelian varieties. Additionally, the writeup for the Re(s) > 11/12 zero-free region for the Riemann zeta function was human edited for readability. 


## Versions and citations

We will preserve the public release history of this collection. Corrections and revisions will be recorded as new versions, with previously released versions remaining accessible. 

```
.
├── README.md                              # 本文件（仓库首页）
├── index.md                               # GitHub Pages 首页
├── LICENSE                                # CC BY-NC-SA 4.0
├── DISCLAIMER.md                          # OpenAI 原始内容引用声明
├── _config.yml                            # GitHub Pages / Jekyll 配置
├── reports/                               # 100 份 Markdown 报告
│   ├── SMPDL_Framework.md                 # 方法论框架 v2.4
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
│   ├── SMPDL_v2.3_sample_reports_97files.zip
│   └── SMPDL_v2.4_sample_reports_107files.zip
└── zenodo/                                # Zenodo metadata
    ├── zenodo_metadata_v2.0.json
    ├── zenodo_metadata_v2.1.json
    └── zenodo_metadata_v2.2.json
```

---

## 报告清单

### 方法论与指南

- [SMPDL_Framework.md](reports/SMPDL_Framework.md) — 方法论框架 v2.4
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

## 版本信息

| 项目 | 当前值 |
|---|---|
| 方法论版本 | v2.3 |
| 论文版本 | v12 |
| 页面版本 | v5.91 |
| DOI | [10.5281/zenodo.23339747](https://doi.org/10.5281/zenodo.23339747) |
| 报告数量 | 97 份 curated |
| 联合 SHA-256 | `3a365aff1760cb0ed3e48502886ebba53c71174af2d4f4bad9c7834af3504be2` |

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
  howpublished={\url{https://doi.org/10.5281/zenodo.23339747}},
  doi={10.5281/zenodo.23339747}
}
```

---

## 许可

本仓库原创内容采用 [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](LICENSE) 许可。

关于 OpenAI math 仓库原始 README 的引用声明，请见 [DISCLAIMER.md](DISCLAIMER.md)。
