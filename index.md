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
| 方法论版本 | v2.1 |
| 论文版本 | v10 |
| 页面版本 | v5.88 |
| DOI | [10.5281/zenodo.23335515](https://doi.org/10.5281/zenodo.23335515) |
| curated 样本 | 86 份 |
| 联合 SHA-256 | `be26f9d200470a8b3521ad667d633e04b23a3c83ef44e1140db3483a0e5bd624` |

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

最新 5 份高危样本（第四批：已完成 Lean 形式化但仍高风险）：

1. [对数空间精确去随机化 L=RL=BPL](reports/SMP_ProofAnalysis_OpenAI_Logspace_Derandomization_L_RL_BPL.md)
2. [矩阵乘法指数 ω≤9/4](reports/SMP_ProofAnalysis_OpenAI_MatrixMultiplication_Exponent_9_4.md)
3. [Hilbert 第 16 问题极限环一致有界](reports/SMP_ProofAnalysis_OpenAI_Hilbert16_LimitCycles.md)
4. [一般凸体 Mahler 猜想](reports/SMP_ProofAnalysis_OpenAI_Mahler_Conjecture_General.md)
5. [Thompson 群 F 非可均化](reports/SMP_ProofAnalysis_OpenAI_ThompsonGroup_Nonamenable.md)

完整样本清单见 [reports/SMPDL_Audit_SampleSuite.md](reports/SMPDL_Audit_SampleSuite.md)。

---

## 下载归档

- [SMPDL_v2.1_sample_reports_86files.zip](archives/SMPDL_v2.1_sample_reports_86files.zip) — 86 份 curated 报告官方归档
- [SMPDL_v2.0_sample_reports_76files.zip](archives/SMPDL_v2.0_sample_reports_76files.zip) — 76 份 curated 报告历史归档
- [Zenodo 记录](https://zenodo.org/records/23335515) — 持久 DOI 与元数据

---

## 许可与声明

原创内容：[CC BY-NC-SA 4.0](LICENSE)  
OpenAI 原始内容引用声明：[DISCLAIMER.md](DISCLAIMER.md)

---

*CAMPANASILVAE · Göttingen Mathematical History Index Project · MMXXVI*
