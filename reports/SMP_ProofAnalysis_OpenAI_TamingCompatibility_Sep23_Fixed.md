# SMPDL 审计报告：OpenAI「四维流形上 taming 蕴含 compatibility」09-23 版（已修复）

**审计对象**：Taming implies compatibility on four-manifolds（2026-09-23 版）  
**来源**：OpenAI math 仓库，2026-09-23 发布，2026-10-06 修复  
**审计日期**：2026-10-13  
**审计框架**：Göttingen S/M/P × D/L 六格审计 v1.5  
**审计结论**：🔴 **原证明存在可识别错误。核心论证中的 cone-equality claim 在 10-06 版中被修正为 strict-inclusion example，属于 M*L/S*L 失败。**

---

## 1. 命题与声明

原论文声明：在四维流形上，若一个近复结构 `J` 被某个辛形式 `ω` tamed（即 `ω(v, Jv) > 0`），则存在一个与 `J` 兼容的辛形式 `ω'`（即 `ω'(Jv, w) = ω'(v, Jw)` 且 `ω'(v, Jv) > 0`）。

这是辛几何中一个经典类型的问题：taming 是 pointwise 的锥条件，compatibility 是更强的积分条件。

---

## 2. S/M/P × D/L 六格审计

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| taming ⇒ compatibility | 锥构造 / 凸组合论证 | ✅ 语义目标清晰 |
| 锥相等性 | 切空间上 tamed 形式的凸性 | 🔴 错误 |
| 兼容形式存在 | 锥相等性的推论 | 🔴 前提失败 |

**发现**：history.md 明确指出 09-23 版的错误是“cone-equality claim”错误；10-06 版修正为“strict-inclusion example”并移除了不必要的 cone-comparison 依赖。

### 2.2 S*L — 语义逻辑结构

- 原论证声称 tamed 形式集合与 compatible 形式集合在某个锥上相等（cone-equality）。
- 10-06 版改为给出 strict-inclusion example，说明 tamed 集合严格大于 compatible 集合。
- 🔴 **结论**：原“相等”断言在逻辑上不成立；从相等推出的存在性结论失去基础。

### 2.3 M*D — 数学依存

正向依赖链：
1. tamed 形式的集合 = compatible 形式的集合（cone-equality）
2. ⇒ 对任意 tamed `J`，存在 compatible 形式
3. ⇒ taming implies compatibility

**检查**：第 1 步错误。正确关系是 strict inclusion，而非 equality。因此第 2 步无法推出。

### 2.4 M*L — 数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| 量词范围 | ✅ | 声明限定于四维流形 |
| 边界情况 | 🔴 | 锥相等性与严格包含的混淆是核心错误 |
| 隐藏假设 | 🔴 | 默认 tamed 形式的凸性与 compatible 形式的凸性相同 |
| 操作交互 | 🟡 | 凸组合保持 taming，但不一定保持 compatibility |
| 外部定理前提 | ✅ | 无复杂外部定理误用 |

### 2.5 P*D — 编程依存

- README 未提及 Lean 形式化。
- 辛几何锥构造的形式化难度高；即使形式化，也可能仅覆盖点wise集合而非整体存在性。
- 🟡 **P 层缺失或部分缺失**。

### 2.6 P*L — 编程逻辑结构

- 无形式化代码可供审计。
- 修正后的 10-06 版保留了旧版本 PDF，符合“修改留痕”原则。

---

## 3. 跨层映射检查

| 映射 | 状态 | 风险 |
|---|---|---|
| S → M | 🔴 | “相等”到数学上“严格包含”的映射错误 |
| M → P | 🟡 | 无形式化捕获错误 |
| S ↔ P | 🔴 | 无机器可读桥梁 |

---

## 4. 已知外部证据

- OpenAI history.md（2026-10-07）明确说明：09-23 版中“corrected the cone-equality claim in Taming implies compatibility, added a strict-inclusion example”。
- 这是 OpenAI 自证错误并修复的典型案例，属于“已被审查发现错误”而非外部数学家公开证伪，但同样说明原证明不成立。
- 辛几何中，taming 与 compatibility 的关系是经典课题；已知结果通常需要额外条件（如近复结构可积、流形紧致等）才能从 taming 推出 compatibility。

---

## 5. 判定：证明是否为真？

| 维度 | 结论 |
|---|---|
| **自然语言声明的真实性** | 🔴 原证明不支持该结论 |
| **原证明的正确性** | 🔴 存在 cone-equality 错误 |
| **形式化验证** | ❌ 未见 |
| **与已知数学的兼容性** | 🔴 与严格包含实例冲突 |

**SMPDL 判定**：本论文属于 **S*L/M*L 核心断言错误** 类型。原证明已被 OpenAI 自身修正，09-23 版应标记为 🔴 **错误**。

---

## 6. 可执行验证建议

1. **D 岗位（陷阱预见）**：对任何“集合相等”断言，优先尝试构造严格包含的反例。
2. **B 岗位（语义忠实审查）**：将“cone-equality”与“strict-inclusion”在正文与图示中逐句核对。
3. **C 岗位（缺口刻画）**：明确列出从 taming 到 compatibility 所需的中间条件，标出未经验证的步骤。
4. **E 岗位（验证解读）**：用 10-06 版修正后的严格包含实例反推 09-23 版的错误位置。

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
