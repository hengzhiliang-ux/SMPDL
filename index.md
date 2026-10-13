# SMPDL — OpenAI 700+ 数学证明语料审计

> Göttingen S/M/P × D/L 数学证明审查方法论

[![DOI](https://zenodo.org/badge/DOI-10.5281/zenodo.23339747.svg)](https://doi.org/10.5281/zenodo.23339747)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSE)

---

## 快速入口

| 项目 | 链接 |
|---|---|
| **完整报告总览** | [reports/SMPDL_Audit_SampleSuite.md](reports/SMPDL_Audit_SampleSuite.md) |
| **方法论框架** | [reports/SMPDL_Framework.md](reports/SMPDL_Framework.md) |
| **文献引用纪律** | [reports/SMPDL_Citation_Discipline.md](reports/SMPDL_Citation_Discipline.md) |
| **署名与指纹** | [reports/SMPDL_ATTRIBUTION.md](reports/SMPDL_ATTRIBUTION.md) |
| **Zenodo 记录** | https://zenodo.org/records/23335515 |
| **WorkBuddy 交互页** | https://riemann-lecturer-04390.app.workbuddy.host/ |

---

## 当前版本

| 项目 | 值 |
|---|---|
| 方法论版本 | v2.3 |
| 论文版本 | v12 |
| 页面版本 | v5.91 |
| DOI | [10.5281/zenodo.23339747](https://doi.org/10.5281/zenodo.23339747)（v12 DOI） |
| curated 样本 | 97 份 |
| 联合 SHA-256 | `3a365aff1760cb0ed3e48502886ebba53c71174af2d4f4bad9c7834af3504be2` |

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

## 下载归档

- [SMPDL_v2.3_sample_reports_97files.zip](archives/SMPDL_v2.3_sample_reports_97files.zip) — 97 份 curated 报告官方归档（最新）
- [SMPDL_v2.2_sample_reports_96files.zip](archives/SMPDL_v2.2_sample_reports_96files.zip) — 96 份 curated 报告历史归档
- [SMPDL_v2.1_sample_reports_86files.zip](archives/SMPDL_v2.1_sample_reports_86files.zip) — 86 份 curated 报告历史归档
- [SMPDL_v2.0_sample_reports_76files.zip](archives/SMPDL_v2.0_sample_reports_76files.zip) — 76 份 curated 报告历史归档
- [Zenodo 记录](https://zenodo.org/records/23339747) — 持久 DOI 与元数据（v12 DOI）

---

## 许可与声明

原创内容：[CC BY-NC-SA 4.0](LICENSE)  
OpenAI 原始内容引用声明：[DISCLAIMER.md](DISCLAIMER.md)

---

*CAMPANASILVAE · Göttingen Mathematical History Index Project · MMXXVI*
