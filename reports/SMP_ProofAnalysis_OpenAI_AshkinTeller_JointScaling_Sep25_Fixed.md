# SMPDL 审计报告：OpenAI「临界 Ashkin–Teller 电流的联合 scaling limit」09-25 版（已修复）

**审计对象**：The joint scaling limit of critical Ashkin–Teller currents（2026-09-25 版）  
**来源**：OpenAI math 仓库，2026-09-25 发布，2026-10-06 修复  
**审计日期**：2026-10-13  
**审计框架**：Göttingen S/M/P × D/L 六格审计 v1.5  
**审计结论**：🔴/🟡 **原证明存在可识别的概率论/共形场论技术错误，涉及 crossing、boundary-attachment、conditioning 与 convergence 论证。10-06 版做了修复，但未公开具体 diff。**

---

## 1. 命题与声明

原论文声明：在临界温度下，Ashkin–Teller 模型中两个 Ising 电流（current）的联合分布收敛到某个共形场论极限（通常涉及两个耦合的自由场或 SLE/CLE 对象）。

Ashkin–Teller 模型是二维统计物理中研究共形普适性的经典格子模型；其临界行为与 `c = 1` 共形场论、SLE_κ 族以及 GFF 耦合密切相关。

---

## 2. S/M/P × D/L 六格审计

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| 联合 scaling limit | crossing 估计 + boundary-attachment + conditioning | 🟡 复杂 |
| crossing 估计 | 离散复分析 / FK 表示 | 🔴 原证明有误 |
| boundary-attachment | 边界条件控制 | 🔴 原证明有误 |
| conditioning | 条件概率 tightness | 🔴 原证明有误 |
| convergence | 弱收敛 + 极限刻画 | 🔴 原证明有误 |

**发现**：history.md 明确将本论文列入 10-07 修复批次，错误类别为“repaired crossing, boundary-attachment, conditioning and convergence arguments”。

### 2.2 S*L — 语义逻辑结构

- “joint scaling limit”要求同时控制两个 Ising 电流的联合分布，而不仅仅是边缘分布。
- crossing、boundary-attachment 和 conditioning 是证明联合收敛的三大支柱；任一失败都会破坏整体极限。
- 🔴 **多节点同时失败**：history.md 列出的错误覆盖证明的主要技术支柱，说明原证明结构存在系统性问题。

### 2.3 M*D — 数学依存

正向依赖链：
1. FK/随机簇表示 ⇒ 电流的随机几何描述
2. discrete complex analysis ⇒ crossing 概率的收敛
3. 边界条件控制 ⇒ boundary-attachment 的 scaling limit
4. 条件概率 tightness ⇒ conditioning 下联合分布收敛
5. ⇒ 联合 scaling limit 结论

**检查**：根据 OpenAI 自陈，第 2–4 步在 09-25 版中存在问题。10-06 版修复了这些论证，但具体修复细节未在 README 中披露。

### 2.4 M*L — 数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| 量词范围 | ✅ | 声明限定于临界 Ashkin–Teller 模型 |
| 边界情况 | 🔴 | 边界附件与交叉事件在离散模型中高度敏感 |
| 隐藏假设 | 🟡 | 原证明可能默认了某种条件独立性或收敛速率 |
| 操作交互 | 🔴 | crossing + conditioning + convergence 的交互容易出错 |
| 外部定理前提 | 🟡 | 依赖 discrete complex analysis/FK 表示的精细结果 |

### 2.5 P*D — 编程依存

- README 未提及 Lean 形式化。
- 二维统计物理 scaling limit 的形式化在全球范围内仍处于起步阶段。
- 🔴 **P 层缺失**：无法通过机器检查捕获 crossing/conditioning 错误。

### 2.6 P*L — 编程逻辑结构

- 无公开形式化代码。
- 即使要形式化，也需要先定义 Ashkin–Teller 模型、电流、各种边界条件、弱收敛等复杂对象。

---

## 3. 跨层映射检查

| 映射 | 状态 | 风险 |
|---|---|---|
| S → M | 🟡 | 联合 scaling limit 到具体 crossing/conditioning 估计的映射复杂 |
| M → P | 🔴 | 无形式化 |
| S ↔ P | 🔴 | 无机器可读桥梁 |

---

## 4. 已知外部证据

- OpenAI history.md（2026-10-07）将本论文列入“Lipschitz heights and Ashkin–Teller currents (4 manuscripts)”修复批次，明确提到“repaired crossing, boundary-attachment, conditioning and convergence arguments, including additional work on the real-Lipschitz interface proof”。
- 10-06 版 README 未包含版本说明（可能因仓库结构不同），但 10-07 发布的版本应已修复。
- Ashkin–Teller 模型的联合 scaling limit 是统计物理中的高难度问题；即使对人类专家也需要大量技术细节。

---

## 5. 判定：证明是否为真？

| 维度 | 结论 |
|---|---|
| **自然语言声明的真实性** | 🟡 命题本身可能成立，但 09-25 版证明不支持 |
| **原证明的正确性** | 🔴 存在多处技术性错误 |
| **形式化验证** | ❌ 未见 |
| **与已知数学的兼容性** | 🟡 命题方向与共形普适性研究兼容，但原证明细节错误 |

**SMPDL 判定**：本论文属于 **M*D/M*L 多节点失败 + P 层缺失** 类型。09-25 版应标记为 🔴 **错误**（已修复）。

---

## 6. 可执行验证建议

1. **D 岗位（陷阱预见）**：对“条件收敛”类论证，重点检查 conditioning 是否改变了相关事件的 scaling exponent。
2. **B 岗位（语义忠实审查）**：核对“joint scaling limit”是否同时要求边缘分布与联合分布收敛，避免用边缘收敛替代联合收敛。
3. **C 岗位（缺口刻画）**：逐条列出 crossing、boundary-attachment、conditioning、convergence 四处的具体引理，标注哪些在 09-25 版中未完整证明。
4. **E 岗位（验证解读）**：获取 09-25 与 10-06 的 PDF diff，定位具体修改段落。

---

## 署名与许可

本审计使用 Göttingen S/M/P × D/L 框架 · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0
