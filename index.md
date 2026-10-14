# SMPDL — OpenAI 700+ 数学证明语料审计

> Göttingen S/M/P × D/L 数学证明审查方法论

[![DOI](https://zenodo.org/badge/DOI-10.5281/zenodo.23359509.svg)](https://doi.org/10.5281/zenodo.23359509)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSE)

---

## 快速入口

| 项目 | 链接 |
|---|---|
| **完整报告总览** | [reports/SMPDL_Audit_SampleSuite.md](reports/SMPDL_Audit_SampleSuite.md) |
| **方法论框架** | [reports/SMPDL_Framework.md](reports/SMPDL_Framework.md) |
| **文献引用纪律** | [reports/SMPDL_Citation_Discipline.md](reports/SMPDL_Citation_Discipline.md) |
| **署名与指纹** | [reports/SMPDL_ATTRIBUTION.md](reports/SMPDL_ATTRIBUTION.md) |
| **Zenodo 记录** | https://zenodo.org/records/23359509（v3.2 · 最新） |
| **WorkBuddy 交互页** | https://riemann-lecturer-04390.app.workbuddy.host/ |

---

## 当前版本

| 项目 | 值 |
|---|---|
| 方法论版本 | v2.8 |
| 论文版本 | v23（curated 269 份 = H1–H43 案例库 + 元文档 + B4 盲判 + C-4 + 人机交互六模式） |
| 页面版本 | v5.94 |
| DOI | [10.5281/zenodo.23359509](https://doi.org/10.5281/zenodo.23359509)（Zenodo v3.2 · Concept DOI 10.5281/zenodo.23318734） |
| curated 样本 | 269 份 |
| 联合 SHA-256 | `32f8596a3cb296a713921bd392695a79a43cfc12ea7f74231ffc510555b700d4`（v23 · 顺序规范见 `reports/SMPDL_ATTRIBUTION.md`） |

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

最新 10 份高危样本（第六批：继续扩大的 Lean 形式化高风险/中风险样本）：

1. [Deligne–Drinfeld 猜想](reports/SMP_ProofAnalysis_OpenAI_DeligneDrinfeld_Conjecture.md)
2. [Erdős–Pomerance 联合 Dickman 猜想](reports/SMP_ProofAnalysis_OpenAI_ErdosPomerance_JointDickman.md)
3. [大素数间隙正密度](reports/SMP_ProofAnalysis_OpenAI_LargePrimeGaps_PositiveDensity.md)
4. [高余维 Riesz 变换可求长性](reports/SMP_ProofAnalysis_OpenAI_RieszTransform_Rectifiability.md)
5. [Erdős 相似性猜想 dyadic 情形](reports/SMP_ProofAnalysis_OpenAI_ErdosSimilarity_Dyadic.md)
6. [对数 Brunn–Minkowski 不等式](reports/SMP_ProofAnalysis_OpenAI_LogBrunnMinkowski.md)
7. [Unique Games 猜想](reports/SMP_ProofAnalysis_OpenAI_UniqueGames_Conjecture.md)
8. [平面不同距离与单位距离界](reports/SMP_ProofAnalysis_OpenAI_PlanarDistinctDistances.md)
9. [Benjamini–Schramm 非唯一性猜想](reports/SMP_ProofAnalysis_OpenAI_BenjaminiSchramm_Nonuniqueness.md)
10. [Connes 双中心化子猜想](reports/SMP_ProofAnalysis_OpenAI_ConnesBicentralizer.md)

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

- [SMPDL_v23_archive.zip](archives/SMPDL_v23_archive.zip) — 269 份 curated 报告官方归档（最新 · Zenodo v3.2 存档镜像；历史归档见 Zenodo v3.1 及更早记录）
- [Zenodo 记录](https://zenodo.org/records/23359509) — 持久 DOI 与元数据（v3.2 · Concept DOI 10.5281/zenodo.23318734）

---

## 许可与声明

原创内容：[CC BY-NC-SA 4.0](LICENSE)  
OpenAI 原始内容引用声明：[DISCLAIMER.md](DISCLAIMER.md)

---

*CAMPANASILVAE · Göttingen Mathematical History Index Project · MMXXVI*
