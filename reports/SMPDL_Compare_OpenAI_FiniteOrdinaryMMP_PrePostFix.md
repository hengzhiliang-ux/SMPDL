# SMPDL 修复前后对比审计：OpenAI「紧 Kähler 四维簇上的有限普通极小模型纲领」

**对比对象**  
- 修复前：Finite ordinary minimal model programs on compact Kähler fourfolds（2026-09-24 版）  
- 修复后：Finite ordinary minimal model programs on compact Kähler fourfolds（2026-10-06 版）  
**审计日期**：2026-10-13  
**审计框架**：Göttingen S/M/P × D/L v1.5  
**总体评价**：🔴/🟡→🟡 **positivity/contraction 论证缺口已声明补充，输入定理及其假设已澄清，但 Kähler MMP 本身是活跃难题，仍需外部专家验证。**

---

## 1. 修复前后声明对比

| 维度 | 09-24 版 | 10-06 版 |
|---|---|---|
| **主声明** | 紧 Kähler 四维簇上，普通 MMP 有限终止 | 保持同主声明 |
| **核心论证** | positivity theorems + contraction theorems（输入模糊） | 增加 carrier-positivity 与 multiplier-ideal 论证；修订 ordinary negative-ray programs 的 contraction induction |
| **输入澄清** | 未显式列出作为输入的外部结果 | 版本说明暗示已澄清哪些结果被用作输入 |
| **版本链** | 09-24 → 10-05 → 10-06 | 10-06 基于 10-05 进一步修订 |

---

## 2. 修复前 SMPDL 失败层（详见 `SMP_ProofAnalysis_OpenAI_FiniteOrdinaryMMP_KahlerFourfolds_Sep24_Fixed.md`）

- **M*D**：positivity theorems 与 contraction theorems 作为输入未显式化；Kähler 版本的存在性不明。
- **M*L**：隐藏假设（默认射影 MMP 结果可直接套用）。
- **S*L**：“ordinary”在 Kähler 范畴中的定义不清晰。
- **P 层**：完全缺失。

**原判定**：🔴 错误/不完整。

---

## 3. 修复后 SMPDL 六格审计

### 3.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| finite ordinary MMP | carrier-positivity + multiplier-ideal + revised contraction induction | 🟡 依赖链已补充 |
| carrier-positivity | Kähler 意义下的正性理论 | 🟡 新引入，需验证 |
| multiplier-ideal 论证 | Nadel/ Kawamata 型消失 | 🟡 新引入，需验证 |
| contraction induction | ordinary negative-ray programs | 🟡 已修订 |
| 输入澄清 | 外部结果及其假设列表 | ✅ 已声明澄清 |

### 3.2 S*L — 语义逻辑结构

- “ordinary”在 Kähler MMP 中的定义仍需要正文确认，但版本说明暗示论证已围绕 ordinary negative-ray programs 重新组织。
- 新增 carrier-positity 与 multiplier-ideal 提供了更具体的技术语言，替代了原证明中模糊的“positivity theorems”。
- 🟡 **语义结构改善**：从“调用某组未命名结果”变为“引入具体技术工具”。

### 3.3 M*D — 数学依存

- 修复前依赖链：positivity（未指定） → contraction（未指定） → flip/termination → 结论。
- 修复后依赖链：**carrier-positivity** → **multiplier-ideal** → **revised contraction induction for ordinary negative-ray programs** → 结论。
- 🟡 新依赖链更具体，但 Kähler 范畴下这些工具的存在性与适用条件仍需外部专家确认。

### 3.4 M*L — 数学逻辑结构

| 检查项 | 09-24 版 | 10-06 版 |
|---|---|---|
| 量词范围 | 🟡 “ordinary”未定义 | 🟡 仍需正文确认定义 |
| 边界情况 | 🟡 奇异 Kähler 空间、非 ℚ-factorial 未说明 | 🟡 新论证仍需明确适用域 |
| 隐藏假设 | 🔴 默认射影结果可直接套用 | 🟡 已用具体工具替代，但工具适用性待验证 |
| 外部定理前提 | 🔴 未列出输入定理 | 🟡 已声明澄清，仍需逐条核对 |
| 已知障碍 | 🟡 Kähler MMP 仍是活跃难题 | 🟡 未改变 |

### 3.5 P*D / P*L — 编程层

- 无形式化更新。
- 代数几何 MMP 的形式化仍是远期目标。
- 🔴 P 层仍缺失。

---

## 4. 跨层映射检查（修复后）

| 映射 | 09-24 版 | 10-06 版 | 变化 |
|---|---|---|---|
| S → M | 🟡 “ordinary MMP”映射到 Kähler 范畴需显式 | 🟡 仍待显式，但工具更具体 | 略有改善 |
| M → P | 🔴 无形式化 | 🔴 无形式化 | 无变化 |
| S ↔ P | 🔴 无桥梁 | 🔴 无桥梁 | 无变化 |

---

## 5. 判定：修复后证明是否为真？

| 维度 | 09-24 版 | 10-06 版 |
|---|---|---|
| 自然语言声明真实性 | 🟡 可能成立但证明不完整 | 🟡 仍可能成立 |
| 原证明正确性 | 🔴 存在 positivity/contraction 缺口 | 🟡 缺口已声明补充，核心仍需专家验证 |
| 形式化验证 | ❌ 未见 | ❌ 未见 |
| 与已知数学兼容性 | 🟡 方向兼容但缺少关键假设 | 🟡 方向兼容，工具与 Kähler MMP 研究一致 |

**SMPDL 判定（修复后）**：🟡 **中风险**。修复方向正确且具体（carrier-positivity、multiplier-ideal、contraction induction），显著改善了输入模糊问题，但 Kähler MMP 本身是活跃研究领域，完整正确性仍需人类专家审阅。

---

## 6. 修复类型归类

- **修复方式**：**输入显式化 + 核心论证补强**（M*D 补充 + M*L 隐藏假设消除）。
- **是否触及 S/M/P 三层的 P 层**：否。
- **是否降低风险**：是；从 🔴/🟡 降至 🟡，但未降至 🟢，因为领域本身的高难度与外部结果依赖仍在。
- **关键 lesson**：对“使用已知结果”的模糊表述，最有效的修复是逐条列出结果名称、版本、适用假设，并用具体技术工具（carrier-positivity、multiplier-ideal）替代笼统术语。

---

## 7. 人类科学家可执行的验证动作

1. **C 岗位**：在 10-06 版 PDF 中列出所有被声明为“已知结果”的定理，逐条确认其在 Kähler 范畴下的版本是否存在及其假设。
2. **D 岗位**：重点扫描“前提域陷阱”——carrier-positivity 与 multiplier-ideal 论证是否默认了射影性或 ℚ-factorial。
3. **B 岗位**：核对“ordinary negative-ray programs”是否给出精确定义，避免与射影 MMP 的“usual MMP”混淆。
4. **E 岗位**：对比 09-24、10-05、10-06 三版 PDF，定位 positivity/contraction 段落的扩展位置，量化修改范围。

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
