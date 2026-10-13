# SMPDL — OpenAI 700+ 数学证明语料审计

> Göttingen S/M/P × D/L 数学证明审查方法论

[![DOI](https://zenodo.org/badge/DOI-10.5281/zenodo.23335515.svg)](https://doi.org/10.5281/zenodo.23335515)
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
| 方法论版本 | v2.0 |
| 论文版本 | v9 |
| 页面版本 | v5.87 |
| DOI | [10.5281/zenodo.23335515](https://doi.org/10.5281/zenodo.23335515) |
| curated 样本 | 76 份 |
| 联合 SHA-256 | `747378ee121e2693060d471f72e018d41526c507a561a32287f5a4adb971536c` |

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

最新 5 份高危样本：

1. [低 Selmer 秩完整 BSD 公式](reports/SMP_ProofAnalysis_OpenAI_BSD_LowSelmerCorank.md)
2. [准 Riemann 假设 Re(s)>7/8](reports/SMP_ProofAnalysis_OpenAI_QuasiRiemannHypothesis.md)
3. [CM 阿贝尔簇 Hodge 猜想](reports/SMP_ProofAnalysis_OpenAI_Hodge_CM_AbelianVarieties.md)
4. [有理数域 Hilbert 第十问题](reports/SMP_ProofAnalysis_OpenAI_HilbertTenth_Rationals.md)
5. [自由群因子同构](reports/SMP_ProofAnalysis_OpenAI_FreeGroupFactors_Isomorphism.md)

完整样本清单见 [reports/SMPDL_Audit_SampleSuite.md](reports/SMPDL_Audit_SampleSuite.md)。

---

## 下载归档

- [SMPDL_v2.0_sample_reports_76files.zip](archives/SMPDL_v2.0_sample_reports_76files.zip) — 76 份 curated 报告官方归档
- [Zenodo 记录](https://zenodo.org/records/23335515) — 持久 DOI 与元数据

---

## 许可与声明

原创内容：[CC BY-NC-SA 4.0](LICENSE)  
OpenAI 原始内容引用声明：[DISCLAIMER.md](DISCLAIMER.md)

---

*CAMPANASILVAE · Göttingen Mathematical History Index Project · MMXXVI*
