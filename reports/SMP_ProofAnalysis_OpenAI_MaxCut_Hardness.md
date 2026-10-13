# SMPDL 审计报告：OpenAI「最优 Max-Cut 困难性直接证明」

**审计对象**：A Direct Proof of Optimal Max-Cut Hardness  
**来源**：OpenAI math 仓库，2026-09-23  
**审计日期**：2026-10-13  
**审计框架**：Göttingen S/M/P × D/L 六格审计 v1.4  
**审计结论**：🔴 **极高风险声明，声称证明 UGC 且给出 NP-hardness；与公开知识状态存在显著张力，需独立专家完整验证。**

---

## 1. 命题与声明

**主定理**：对任意固定因子 ρ > α_GW（Goemans–Williamson 常数，≈0.87856），在简单无向无权图上近似 Max-Cut 到比率 ρ 是 NP-hard 的。

**意义**：
- 在 UGC 成立的前提下，Khot–Kindler–Mossel–O'Donnell (KKMO 2004) 已证明该困难性。
- OpenAI 声称**不假设 UGC**，直接给出 NP-hardness。
- 同族论文 102（The Unique Games Theorem）声称直接证明 Unique Games Conjecture 本身；若该证明成立，则本定理是推论。但反过来，本定理成立并不意味着 UGC 成立。

---

## 2. S/M/P × D/L 六格审计

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| 主定理（NP-hardness） | 3SAT → Unique Games / Label Cover → 加权 Max-Cut → 无权 Max-Cut | ✅ 结构清晰 |
| 无权图结果 | 加权图结果 + 重采样/放大技术 | ✅ 依赖明确 |
| 最优性（α_GW） | 与 GW 算法上界匹配 | ✅ 上界来源正确 |

**发现**：摘要直接声称「direct proof of optimal Max-Cut hardness」；引言说明其使用 established PCP and Label Cover hardness results。

### 2.2 S*L — 语义逻辑结构

- 量词：「any fixed factor greater than α_GW」「simple unweighted graphs」。
- 无「所有图」到「几乎所有图」的退化。
- ⚠️ 标题中「direct proof」是修辞性术语；需确认它是否等价于「不依赖 UGC 的直接 NP-hardness 归约」，还是仅表示证明技术更初等。

### 2.3 M*D — 数学依存

正向依赖链（根据目录）：
1. Introduction / Preliminaries：定义 Max-Cut、GW 常数、SDP 上界。
2. Tree / Tree Fourier / Hashing：建立新的 PCP 测试 gadget。
3. Reduction：从 3SAT / Label Cover 归约到加权 Max-Cut。
4. Extraction / Decoding：完备性/可靠性分析。
5. Unweighted：通过放大/图乘积去掉权重。

**检查**：依赖链条长；核心 gadget（tree + Fourier + hashing）是新构造，未引用独立验证的对应物。

### 2.4 M*L — 数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| 量词范围 | ✅ | 全称所有简单无权图 |
| 边界情况 | ⚠️ | 「ρ > α_GW」是严格大于；当 ρ 接近 α_GW 时，归约参数趋向无穷，需检查多项式性 |
| 与已知结果的兼容性 | 🔴 | 目前公开数学知识：Håstad 3-bit PCP 给出 16/17≈0.941 的 NP-hardness；KKMO 在 UGC 下给出 α_GW+ε。OpenAI 声称改进 Håstad 的 NP-hardness 阈值到 α_GW，这是数十年未解决的开放问题 |
| 隐藏假设 | 🔴 | 若证明使用「established PCP and Label Cover hardness results」，则 hardness 结论的间隙可能受限于这些结果的参数。把间隙精确控制到 α_GW 需要 gadget 恰好匹配 GW  SDP 松弛，这是非平凡的 |
| 等价循环 | ⚠️ | 同族「The Unique Games Theorem」声称证明 UGC；本论文若依赖 UGC 的某种等价形式，则可能出现「用等价命题证明目标」的循环风险 |

### 2.5 P*D — 编程依存

- Lean 形式化已列出（formalization.yaml）。
- 依赖外部 PCP/Label Cover 形式化库；若这些底层结果未在 mathlib 中覆盖，可能引入 `sorry` 或临时公理。

### 2.6 P*L — 编程逻辑结构

- Lean 编译 reportedly 通过。
- ⚠️ 复杂性 gadget 的形式化通常只覆盖最终结论，不覆盖全部组合分析细节。
- ⚠️ 「NP-hardness」在形式化中通常表述为「存在从 3SAT 到问题的多项式时间归约」；实际归约构造是否可执行、是否保持参数承诺，需要人工核对。

---

## 3. 跨层映射检查

| 映射 | 状态 | 风险 |
|---|---|---|
| S → M | ⚠️ | 「direct proof」可能被误读为「初等证明」；实际上仍使用 PCP/Label Cover，只是声称不假设 UGC |
| M → P | ⚠️ | Lean 形式化很可能只覆盖定理语句，不覆盖完整 gadget 分析 |
| S ↔ P | 🔴 | 缺少 NL ↔ Lean 的逐行对应 metadata |

---

## 4. 已知外部证据

- 公开资料（Wikiwand / Wikipedia）确认：在**无额外假设**下，目前已知最好的 NP-hardness 近似比是 Håstad 的 16/17≈0.941；α_GW+ε 的困难性目前只在 UGC 假设下成立。
- OpenAI 同族论文 102 声称证明 UGC 本身。若该论文正确，则本论文作为推论成立；但证明 UGC 的难度不亚于本论文。
- 2026-10-07 OpenAI 撤回 3 篇论文，本论文不在撤回清单中，但未获得独立专家公开确认。

---

## 5. 判定：证明是否为真？

| 维度 | 结论 |
|---|---|
| **Lean 形式一致性** | ✅ 已通过（据 OpenAI） |
| **与公开知识状态的兼容性** | 🔴 **高度张力**：声称解决了一个长期开放问题，且与已知最好无条件 NP-hardness 结果差距显著 |
| **依赖族 102（UGC 证明）** | ⚠️ 若族 102 正确，本论文是推论；但族 102 本身待验证 |
| **独立可验证性** | ⚠️ 论文 38 页， gadget 复杂，专家验证需数周 |

**SMPDL 判定**：本论文属于**极高风险的研究级声明**。S/M/P 依存结构未发现循环，但 M*L 存在「声称显著超越当前无条件 NP-hardness 界限」的结构性张力；P 层通过不能消除 M 层风险。按 SMPDL 风险分级，标记为 **M*L 显著缺口 / 研究级待验证**。

---

## 6. 可执行验证建议

1. **A 岗位（概念奇点）**：识别 gadget（tree + Fourier + hashing）是否真正新颖，还是已有技术的重新包装。
2. **B 岗位（语义忠实审查）**：核对「direct proof」是否精确等同于「不假设 UGC 的 NP-hardness 归约」。
3. **C 岗位（缺口刻画）**：定位证明是否真的不依赖 UGC；若某步暗中使用了与 UGC 等价的 hardness 假设，则构成等价循环。
4. **D 岗位（陷阱预见）**：检查 ρ→α_GW⁺ 时归约参数是否仍保持多项式（边界 / 前提域陷阱 V）。
5. **E 岗位（验证解读）**：区分「Lean 通过该定理语句」与「整个 38 页证明已被形式化」。

---

## 文献引用纪律检查

依据 SMPDL 文献引用纪律（真实性核查 + 支持性核查），本报告审查如下：

| 引用对象 | 真实性 | 支持性 | 说明 |
|---|---|---|---|
| OpenAI 原论文 README/PDF | ⚠️ 待查 | ⚠️ 待查 | 需从 OpenAI math 仓库核对标题、日期、摘要是否与报告一致。 |
| OpenAI 同族修订稿/依赖论文 | ⚠️ 待查 | ⚠️ 待查 | 若原论文引用同族结果，需核查版本号与结论范围。 |
| 引用的外部数学定理 | ⚠️ 待查 | ⚠️ 待查 | 报告若提及已知定理/障碍，需确认其真实且确实支持当前风险判断。 |

**核查结论**：本报告审计 OpenAI 生成声明；除经典数学背景外，对 OpenAI 论文自身及同族引用的支持性核查尚属未决风险。

---

## 署名与许可

本审计使用 Göttingen S/M/P × D/L 框架 · v1.4 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0
