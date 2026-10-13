# SMPDL 修复前后对比审计：OpenAI「临界 Ashkin–Teller 电流的联合 scaling limit」

**对比对象**  
- 修复前：The joint scaling limit of critical Ashkin–Teller currents（2026-09-25 版）  
- 修复后：The joint scaling limit of critical Ashkin–Teller currents（2026-10-06 版）  
**审计日期**：2026-10-13  
**审计框架**：Göttingen S/M/P × D/L v1.5  
**总体评价**：🔴→🟡 **多节点技术性错误已声明修复，但修复范围涉及 crossing、boundary-collar、convergence 等核心论证，需外部专家审阅 PDF 后才能降级。**

---

## 1. 修复前后声明对比

| 维度 | 09-25 版 | 10-06 版 |
|---|---|---|
| **主声明** | 临界 Ashkin–Teller 模型中两个 Ising 电流的联合分布收敛到某个共形场论极限 | 保持同主声明 |
| **核心论证** | crossing 估计 + boundary-attachment + conditioning + excursion convergence | 修正 transmission/boundary-collar；用 signed-loop-soup/GMC 论证替换 excursion convergence |
| **依赖文献** | 未更新同伴论文引用 | 更新 companion-paper citation |
| **版本说明** | 无 | 明确列出四项修正 |

---

## 2. 修复前 SMPDL 失败层（详见 `SMP_ProofAnalysis_OpenAI_AshkinTeller_JointScaling_Sep25_Fixed.md`）

- **M*D**：crossing 估计、boundary-attachment、conditioning、convergence 四个技术节点同时失败。
- **M*L**：多节点失败导致整体极限结论缺乏支撑。
- **P 层**：完全缺失，无法机器检查。

**原判定**：🔴 错误。

---

## 3. 修复后 SMPDL 六格审计

### 3.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| 联合 scaling limit | signed-loop-soup/GMC + boundary-collar 控制 + corrected transmission | 🟡 依赖链已更新 |
| signed-loop-soup/GMC | Gaussian multiplicative chaos / 随机 loop soup 技术 | 🟡 技术复杂，需外部验证 |
| boundary-collar 控制 | 边界区域离散→连续估计 | 🟡 已声明修正 |
| transmission 修正 | 交叉事件的概率传输估计 | 🟡 已声明修正 |
| companion-paper 引用 | 同伴论文版本对齐 | ✅ 已更新 |

### 3.2 S*L — 语义逻辑结构

- 声明本身未变，但支持声明的技术支柱被整体替换。
- 原论证是「crossing → boundary-attachment → conditioning → excursion convergence」；修复后是「corrected transmission/boundary-collar → signed-loop-soup/GMC」。
- 🟡 **逻辑链重写**：从多节点失败变为新的、更复杂的技术栈；风险从“结构错误”转为“技术细节待验证”。

### 3.3 M*D — 数学依存

- 修复前依赖链：FK/随机簇 → discrete complex analysis → crossing → boundary-attachment → conditioning → excursion convergence → 结论。
- 修复后依赖链：FK/随机簇 → **corrected transmission** → **signed-loop-soup/GMC** → 结论。
- 🟡 新依赖链避免了原失败节点，但引入了 Gaussian multiplicative chaos 等高级对象，其收敛性仍需专家核验。

### 3.4 M*L — 数学逻辑结构

| 检查项 | 09-25 版 | 10-06 版 |
|---|---|---|
| 量词范围 | ✅ 临界 AT 模型 | ✅ 临界 AT 模型 |
| 边界情况 | 🔴 boundary-attachment 敏感 | 🟡 已声明修正，但未公开 diff |
| 隐藏假设 | 🟡 默认条件独立/收敛速率 | 🟡 新论证仍需检查 GMC 正则性 |
| 操作交互 | 🔴 crossing+conditioning+convergence 交互出错 | 🟡 新交互（loop soup/GMC）待验证 |
| 外部定理前提 | 🟡 discrete complex analysis 依赖 | 🟡 GMC/loop soup 依赖 |

### 3.5 P*D / P*L — 编程层

- 无形式化更新。
- 二维统计物理 scaling limit 的形式化仍不现实。
- 🔴 P 层仍缺失。

---

## 4. 跨层映射检查（修复后）

| 映射 | 09-25 版 | 10-06 版 | 变化 |
|---|---|---|---|
| S → M | 🟡 复杂但多节点失败 | 🟡 复杂但失败节点已替换 | 有改善但未根治 |
| M → P | 🔴 无形式化 | 🔴 无形式化 | 无变化 |
| S ↔ P | 🔴 无桥梁 | 🔴 无桥梁 | 无变化 |

---

## 5. 判定：修复后证明是否为真？

| 维度 | 09-25 版 | 10-06 版 |
|---|---|---|
| 自然语言声明真实性 | 🟡 可能成立 | 🟡 仍可能成立 |
| 原证明正确性 | 🔴 多处技术性错误 | 🟡 核心错误已声明修复，但新论证待验证 |
| 形式化验证 | ❌ 未见 | ❌ 未见 |
| 与已知数学兼容性 | 🟡 方向兼容但细节错误 | 🟡 方向兼容，新工具与 CFT/SLE 研究一致 |

**SMPDL 判定（修复后）**：🟡 **中风险**。修复声明覆盖了原失败节点，但涉及高难度概率论/共形场论技术，必须经人类专家审阅完整 PDF 后才能进一步降级。

---

## 6. 修复类型归类

- **修复方式**：**核心论证重写**（M*D 多节点替换 + S*D 依赖链更新）。
- **是否触及 S/M/P 三层的 P 层**：否。
- **是否降低风险**：是；从 🔴 降至 🟡，但未降至 🟢，因为修复引入了新的高技术门槛依赖。
- **关键 lesson**：当证明多节点同时失败时，简单补丁不够，往往需要重写一条新的技术路径；新路径本身也需要独立审计。

---

## 7. 人类科学家可执行的验证动作

1. **C 岗位**：逐条定位 09-25 版中 crossing、boundary-attachment、conditioning、excursion convergence 四段，与 10-06 版做段落级 diff。
2. **B 岗位**：确认 signed-loop-soup/GMC 论证是否准确翻译了“联合 scaling limit”的语义目标——即同时控制两个 Ising 电流的联合分布，而非仅边缘分布。
3. **D 岗位**：检查 GMC 正则性条件是否被显式化；GMC 在 critical 点的存在性通常需要额外假设。
4. **E 岗位**：确认 companion-paper citation 更新后，相关外部结果是否真正支持新论证。

---

## 文献引用纪律检查

依据 SMPDL 文献引用纪律（真实性核查 + 支持性核查），本报告审查如下：

| 引用对象 | 真实性 | 支持性 | 说明 |
|---|---|---|---|
| OpenAI 论文修复前版本 | ⚠️ 待查 | ⚠️ 待查 | 需核对原版本 PDF 与 README 是否真实存在且与报告描述一致。 |
| OpenAI 论文修复后版本 | ⚠️ 待查 | ⚠️ 待查 | 需核对修订版是否真正修复了报告指出的缺口。 |
| 引用的外部定理/工具 | ⚠️ 待查 | ⚠️ 待查 | 对比报告若引用外部数学结果，需逐条核查其真实性与支持方向。 |

**核查结论**：本对比报告依赖 OpenAI 论文的两个版本，需按真实性 + 支持性纪律逐条核对；对 OpenAI 同族修订稿尤需确认版本一致性。

---

## 署名与许可

Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0
