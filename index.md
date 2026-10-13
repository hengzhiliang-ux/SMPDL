# SMPDL — OpenAI 700+ 数学证明语料审计

> Göttingen S/M/P × D/L 数学证明审查方法论

[![DOI](https://zenodo.org/badge/DOI-10.5281/zenodo.23353609.svg)](https://doi.org/10.5281/zenodo.23353609)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSE)

---

## 快速入口

| 项目 | 链接 |
|---|---|
| **完整报告总览** | [reports/SMPDL_Audit_SampleSuite.md](reports/SMPDL_Audit_SampleSuite.md) |
| **方法论框架** | [reports/SMPDL_Framework.md](reports/SMPDL_Framework.md) |
| **文献引用纪律** | [reports/SMPDL_Citation_Discipline.md](reports/SMPDL_Citation_Discipline.md) |
| **署名与指纹** | [reports/SMPDL_ATTRIBUTION.md](reports/SMPDL_ATTRIBUTION.md) |
| **Zenodo 记录** | https://zenodo.org/records/23353609 |
| **WorkBuddy 交互页** | https://riemann-lecturer-04390.app.workbuddy.host/ |

---

## 当前版本

| 项目 | 值 |
|---|---|
| 方法论版本 | v2.6 |
| 论文版本 | v15 |
| 页面版本 | v5.97 |
| DOI | [10.5281/zenodo.23353609](https://doi.org/10.5281/zenodo.23353609)（v15 · Zenodo 记录 23353609） |
| curated 样本 | 146 份 |
| 联合 SHA-256 | `3f1a4c6c1ee04b3c67ed129ffa58aed02c2c3ca53a34583f292a70d31cecb7fe` |

---

## 关于 SMPDL

SMPDL 将数学证明审查拆分为三层（语义 S / 数学 M / 编程 P）与两维（内生依存 D / 逻辑结构 L），形成六格审计矩阵。配套工具包括：

- **TRAP-CHECK** 七类陷阱检查
- **五人工岗位** A/B/C/D/E 分工
- **反前视五步协议**
- **文献引用纪律**：真实性核查 + 支持性核查

---

## OpenAI 700+ 语料高危抽样

本仓库包含对 [OpenAI math 仓库](https://github.com/openai/math)中 719 余份数学手稿的抽样审计，重点关注：

- 已发表但高风险的研究级声明
- 已被人类数学家证伪/撤回的声明
- 修复前后对比

最新 5 份高危样本（第五批：结构相对完善但仍有补证需求）：

1. [四次多项式无平方值与幂自由值](reports/SMP_ProofAnalysis_OpenAI_Squarefree_Quartics.md)
2. [Jacobsthal 函数二次上界](reports/SMP_ProofAnalysis_OpenAI_Jacobsthal_QuadraticBound.md)
3. [totient 原像数目渐近公式](reports/SMP_ProofAnalysis_OpenAI_Totient_Asymptotic.md)
4. [高斯素数图有界连通分支](reports/SMP_ProofAnalysis_OpenAI_GaussianPrime_BoundedComponents.md)
5. [平面图与有界树宽图 L1 嵌入](reports/SMP_ProofAnalysis_OpenAI_Planar_L1_Embeddings.md)

完整样本清单见 [reports/SMPDL_Audit_SampleSuite.md](reports/SMPDL_Audit_SampleSuite.md)。

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


---

## v2.6 补全 curated 语料并修复元数据

在 v2.5 的 141 份 curated 报告基础上补入 5 份遗漏文档，扩展至 **146**：

- `SMPDL_Construct_AndrewsCurtis_HumanChecklist.md` — Andrews-Curtis 构造人工清单
- `SMP_ProofAnalysis_OpenAI_WeilClasses_SignError.md` — OpenAI Weil 类代数性撤回事件审计
- `SMP_ProofAnalysis_OpenAI_KugaSatake_DependentGap.md` — OpenAI Kuga-Satake 对应代数性撤回事件审计
- `SMP_ProofAnalysis_OpenAI_HodgeK3_Withdrawal.md` — OpenAI K3 曲面乘积 Hodge 猜想撤回事件审计
- `SMPDL_arXiv_Paper.md` — SMPDL 方法论 arXiv 论文源文件

同时修复：
- ATTRIBUTION 清单表格分隔符格式错误；
- 2 份旧报告仍指向 Zenodo v1 DOI；
- `SMPDL_HistoricalAssumption_CognitiveLogic.md` 中「9 组」→「10 组」笔误。

新联合 SHA-256：`3f1a4c6c1ee04b3c67ed129ffa58aed02c2c3ca53a34583f292a70d31cecb7fe`。

> Zenodo v2.6.1 DOI 与指纹已回填本页面。

## 下载归档

- [SMPDL_v2.6_sample_reports_146files.zip](archives/SMPDL_v2.6_sample_reports_146files.zip) — 146 份 curated 报告官方归档（最新）
- [SMPDL_v2.5_sample_reports_141files.zip](archives/SMPDL_v2.5_sample_reports_141files.zip) — 141 份 curated 报告历史归档
- [SMPDL_v2.2_sample_reports_96files.zip](archives/SMPDL_v2.2_sample_reports_96files.zip) — 96 份 curated 报告历史归档
- [SMPDL_v2.1_sample_reports_86files.zip](archives/SMPDL_v2.1_sample_reports_86files.zip) — 86 份 curated 报告历史归档
- [SMPDL_v2.0_sample_reports_76files.zip](archives/SMPDL_v2.0_sample_reports_76files.zip) — 76 份 curated 报告历史归档
- [Zenodo 记录](https://zenodo.org/records/23353609) — 持久 DOI 与元数据（v15 · 记录 23353609）

---

## 许可与声明

原创内容：[CC BY-NC-SA 4.0](LICENSE)  
OpenAI 原始内容引用声明：[DISCLAIMER.md](DISCLAIMER.md)

---

*CAMPANASILVAE · Göttingen Mathematical History Index Project · MMXXVI*
