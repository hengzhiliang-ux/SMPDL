# SMPDL 审计报告：OpenAI「紧 Kähler 四维簇上的有限普通极小模型纲领」09-24 版（已修复）

**审计对象**：Finite ordinary minimal model programs on compact Kähler fourfolds（2026-09-24 版）  
**来源**：OpenAI math 仓库，2026-09-24 发布，2026-10-07 修复  
**审计日期**：2026-10-13  
**审计框架**：Göttingen S/M/P × D/L 六格审计 v1.5  
**审计结论**：🔴/🟡 **原证明存在积极性（positivity）与收缩（contraction）论证的缺口，且未充分澄清哪些结果被用作输入。10-07 版做了修复，但具体 diff 未公开。**

---

## 1. 命题与声明

原论文声明：在紧 Kähler 四维簇上，普通（ordinary）极小模型纲领（MMP）在有限步后终止，并产生一个极小模型或 Mori fiber space。

这是射影 MMP 向 Kähler（非射影）范畴推广的关键一步：在射影情形，Birkar–Cascini–Hacon–McKernan 证明了 flip 的有限性；在非射影 Kähler 情形，termination 与 contraction 的论证需要额外工具。

---

## 2. S/M/P × D/L 六格审计

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| finite ordinary MMP | positivity theorems + contraction theorems | 🟡 复杂 |
| positivity theorems | Kähler 意义下的 nef/big 刻画 | 🔴 原证明有缺口 |
| contraction theorems | extremal ray 理论在 Kähler 范畴 | 🔴 原证明有缺口 |
| termination | 上述两步骤 + 离散不变量控制 | 🟡 依赖前驱 |

**发现**：history.md 将本论文所在批次描述为“Kähler minimal model programs and abundance (6 manuscripts)”，错误类别为“expanded positivity and contraction arguments and clarified which results are used as inputs, with their required hypotheses”。

### 2.2 S*L — 语义逻辑结构

- “ordinary MMP”在 Kähler 范畴下需要明确：哪些 extremal rays 可收缩、收缩后是否仍保持 Kähler、flip 是否存在。
- 原证明在“哪些结果被用作输入”上未充分澄清，导致读者无法判断每个外部定理的适用域。
- 🔴 **输入模糊风险**：自然语言中“使用已知结果”若未列出具体定理与假设，容易触发“前提域陷阱”。

### 2.3 M*D — 数学依存

正向依赖链：
1. Kähler 范畴下的 positivity 定理（如 Kawamata–Viehweg 型消失定理）
2. Kähler 范畴下的 contraction 定理（extremal contraction 存在性）
3. flip 存在性 + 离散不变量下降
4. ⇒ finite ordinary MMP

**检查**：根据 OpenAI 自陈，09-24 版在第 1、2 步的论证存在缺口，且未清晰说明“哪些结果被用作输入”。10-07 版扩展了这些论证。

### 2.4 M*L — 数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| 量词范围 | 🟡 | “ordinary”在 Kähler MMP 中需要定义 |
| 边界情况 | 🟡 | 奇异 Kähler 空间、非 ℚ-factorial 情形未说明 |
| 隐藏假设 | 🔴 | 未显式列出作为输入的外部结果及其假设 |
| 外部定理前提 | 🔴 | positivity/contraction 定理的 Kähler 版本可能尚未建立 |
| 已知障碍 | 🟡 | Kähler MMP 是活跃研究领域，完全推广仍有障碍 |

### 2.5 P*D — 编程依存

- README 未提及 Lean 形式化。
- 代数几何 MMP 的形式化需要 scheme theory, cohomology, intersection theory 等庞大前置库。
- 🔴 **P 层缺失**。

### 2.6 P*L — 编程逻辑结构

- 无形式化代码。
- 若要形式化，首先需形式化 Kähler MMP 的基本对象（Kähler manifold, extremal ray, flip, minimal model），这在当前技术下不现实。

---

## 3. 跨层映射检查

| 映射 | 状态 | 风险 |
|---|---|---|
| S → M | 🟡 | “ordinary MMP”到 Kähler 范畴的具体定义需显式 |
| M → P | 🔴 | 无形式化 |
| S ↔ P | 🔴 | 无机器可读桥梁 |

---

## 4. 已知外部证据

- OpenAI history.md（2026-10-07）将本论文列入“Kähler minimal model programs and abundance (6 manuscripts)”修复批次，明确提到“expanded positivity and contraction arguments and clarified which results are used as inputs, with their required hypotheses”。
- 09-24 版 README 无版本说明；10-05/10-06/10-07 有后续版本，说明该论文经历了多轮修订。
- 射影 MMP 的 termination 由 Birkar 等人证明，但 Kähler 推广仍是开放且困难的方向。

---

## 5. 判定：证明是否为真？

| 维度 | 结论 |
|---|---|
| **自然语言声明的真实性** | 🟡 命题可能是真的，但 09-24 版证明不完整 |
| **原证明的正确性** | 🔴 存在 positivity/contraction 论证缺口 |
| **形式化验证** | ❌ 未见 |
| **与已知数学的兼容性** | 🟡 方向与 Kähler MMP 研究兼容，但原证明缺少关键假设 |

**SMPDL 判定**：本论文属于 **M*D 输入模糊 + M*L 隐藏假设** 类型。09-24 版应标记为 🔴 **错误/不完整**（已修复）。

---

## 6. 可执行验证建议

1. **C 岗位（缺口刻画）**：列出所有被声明为“已知结果”的输入定理，并逐条确认其在 Kähler 范畴下的版本是否存在。
2. **D 岗位（陷阱预见）**：重点扫描“前提域陷阱”——射影 MMP 的 positivity/contraction 定理不能直接套用到非射影 Kähler 情形。
3. **B 岗位（语义忠实审查）**：核对“ordinary”在正文中是否给出精确定义，避免与射影情形的“usual MMP”混淆。
4. **E 岗位（验证解读）**：对比 09-24、10-05、10-06、10-07 各版的 PDF，定位 positivity/contraction 论证的扩展位置。

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

本审计使用 Göttingen S/M/P × D/L 框架 · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0
