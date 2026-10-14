# SMPDL 基础对比审计：ZFC vs ZF 向量空间基存在性

> **对比对象**
> - "PreFix" 版本：ZFC 下任意向量空间都有基（见 `SMP_ProofAnalysis_ZFC_VectorSpaceBasis.md`）
> - "PostFix" 版本：ZF 下无法证明任意向量空间有基（见 `SMP_ProofAnalysis_ZF_VectorSpaceBasis.md`）
> 
> **审计日期**：2026-10-13  
> **审计框架**：Göttingen S/M/P × D/L v1.5  
> **总体评价**：⚪ ↔ 🟡 ZFC 版本在 ZFC 内正确；ZF 版本不是证明错误，而是基础假设（AC）缺失导致结论不可证。

---

## 1. 版本声明对比

| 维度 | ZFC 版本（PreFix） | ZF 版本（PostFix） |
|---|---|---|
| **主声明** | 在 ZFC 中，任意向量空间都有基 | 在 ZF 中，"任意向量空间都有基"不可证 |
| **选择公理 AC** | 存在 | 不存在 |
| **Zorn 引理** | 可用 | 不可用 |
| **证明策略** | 用 Zorn 引理证明极大线性无关集存在 | 无法完成最后一步；需用元数学力迫法证明独立性 |
| **结论类型** | 构造性存在性（非算法性） | 负结果 / 独立性结果 |
| **基础强度** | 强（等价于 AC） | 弱（无 AC） |
| **有限维情形** | 有基 | 有基（可用有限归纳） |
| **无限维情形** | 有基（依赖 AC） | 不可证；存在无基模型 |

---

## 2. PreFix 版本 SMPDL 速览（ZFC）

详见 `SMP_ProofAnalysis_ZFC_VectorSpaceBasis.md`。

- **S*D**：自然语言依赖"向量空间 → 线性无关集族 → Zorn 引理 → 极大元 → 基"的语义链。
- **S*L**：量词清晰，但"Zorn 引理等价于 AC"这一关键语义条件常被省略。
- **M*D**：ZFC → AC ↔ Zorn → maximal linearly independent set → basis。
- **M*L**：逻辑完整；结论为非构造性存在性定理。
- **P*D / P*L**：Mathlib 默认启用选择公理，`exists_basis` 可证；`#print axioms` 会显示 `Classical.choice`。

**PreFix 判定**：⚪ 已确认正确（在 ZFC 体系内）。

---

## 3. PostFix 版本 SMPDL 六格审计（ZF）

### 3.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| 向量空间定义 | 域 + 模公理 | ✅ |
| 线性无关集族 ℱ | 向量空间子集 | ✅ |
| 链的并仍线性无关 | 代数验证 | ✅ |
| Zorn 引理 | **AC 缺失** | 🔴 不可用 |
| 极大线性无关集存在 | **无法推出** | 🔴 断裂 |
| 任意向量空间有基 | **不可证** | 🔴 断裂 |

### 3.2 S*L — 语义逻辑结构

- ZF 版本的前半段与 ZFC 版本完全相同：构造 ℱ、验证链有上界。
- 关键差异在于最后一步：无法调用 Zorn 引理得到极大元。
- ⚠️ 自然语言极易把"Zorn 引理证明基存在"当作纯代数事实，忽略其集合论基础强度。

### 3.3 M*D — 数学依存

```text
ZF_VectorSpaceBasis_Independence
    │
    ├── ZF Axioms (no AC)
    │
    ├── Same algebraic setup as ZFC version
    │       ├── Vector space V over F
    │       └── ℱ = all linearly independent subsets
    │
    ├── Proof attempt blocked at Zorn's Lemma
    │
    ├── Metamathematical evidence
    │       ├── Cohen forcing: ∃ model of ZF + (some vector space has no basis)
    │       └── Blass (1984): "every vector space has a basis" → AC
    │
    └── Conclusion: statement is independent of ZF
```

- 依赖关系在 ZF 内部无法闭合，需借助元数学工具（力迫法）。

### 3.4 M*L — 数学逻辑结构

| 检查项 | ZFC | ZF | 差异说明 |
|---|---|---|---|
| 代数结构 | 相同 | 相同 | 向量空间定义不依赖 AC |
| 存在性结论 | 可证 | 不可证 | AC/Zorn 是关键 |
| 有限维 | 可证 | 可证 | 有限归纳无需 AC |
| 无限维 | 依赖 AC | 不可证 | 全称量词的强度来源 |
| 独立性 | 不讨论 | Cohen 力迫法证明 | 元数学层面 |

### 3.5 P*D / P*L — 编程层

- 两个版本在 Mathlib 中都可以用同一套 `Module`、`LinearIndependent`、`Basis` 类型表达。
- ZFC 版本可完成 `#print axioms` 显示 `Classical.choice`。
- ZF 版本若移除选择公理，证明无法完成；`exists_basis` 类定理失效。
- 力迫法独立性证明目前不在 Lean 类型论内部，属于元数学。

---

## 4. 跨层映射检查（PostFix vs PreFix）

| 映射 | ZFC（PreFix） | ZF（PostFix） | 变化 |
|---|---|---|---|
| S → M | "用 Zorn 得极大元" → Zorn 引理 | 同一段自然语言 → **无对应定理** | 核心映射断裂 |
| M → P | `zorn_le_nonempty` | `zorn_le_nonempty` 不可用 | 形式化策略断裂 |
| S ↔ P | 存在性证明 → `#print axioms` 显示 choice | 不可证 → `sorry` 或元注释 | 结果类型反转 |
| S ↔ S | "任意向量空间有基" | "任意向量空间有基不可证" | 结论语义反转 |
| M ↔ M | AC ↔ Zorn ↔ basis | 无 AC → Zorn 失效 | 数学基础变化 |

**跨层结论**：两个版本的局部 S/M/P 映射几乎一致，但核心存在性映射在 ZF 中断裂。这不是证明错误，而是基础假设（AC）缺失导致的不可证性。

---

## 5. 判定：PostFix 是否为真？

| 维度 | ZFC（PreFix） | ZF（PostFix） |
|---|---|---|
| 自然语言声明真实性 | ⚪ 真 | ⚪ 真（作为元数学命题） |
| 证明正确性 | ⚪ 正确 | N/A（无法完成证明） |
| 形式化验证 | ✅ Mathlib `exists_basis` | 🔴 在缺选择公理时不可证 |
| 与已知数学兼容性 | ✅ 与 ZFC 兼容 | ✅ 与 ZF + 独立性结果兼容 |
| 退化/极限情况 | 有限维、无限维均可证 | 有限维可证；无限维不可证 |

**SMPDL 判定（PostFix）**：🟡 **基础依赖风险**。ZF 版本不是对 ZFC 版本的“修复”，而是“在较弱基础下，同一全称命题不可证”的元数学事实。

---

## 6. 变化类型归类

- **变化方式**：**基础假设迁移**（foundation shift），而非证明错误修复。
- **核心假设差异**：
  - ZFC 版本：承认选择公理 AC（因此 Zorn 引理可用）。
  - ZF 版本：不承认 AC（因此 Zorn 引理不可用）。
- **证明骨架相似性**：两者前段骨架相同（构造 ℱ、验证链有上界），但最后一步在 ZF 中无法完成。
- **SMPDL 同构标签建议**：`S-BISIM / M-BISIM / P-BISIM`。
  - S-BISIM：自然语言前段骨架相同，但结论语义不同（存在性 vs 不可证性）。
  - M-BISIM：代数结构相同，但存在性工具（Zorn/AC）的存否改变结论。
  - P-BISIM：都使用 Mathlib 的 `Module` / `Basis` 类型，但一个可调用 `zorn_le_nonempty`，另一个不能。
- **关键 lesson**：基础集合论假设可以改变一个“纯代数”结论的可证性。在跨基础迁移时，必须显式声明 `AxiomaticBase` 并检查关键工具（如 Zorn 引理）是否可用。

---
---

## 6.5 概念奇点（Conceptual Singularity）

### 6.5.1 本组对比中的关键人工洞察

- **认识到“任意向量空间有基”依赖选择公理**：在 ZFC 中这是 Zorn 引理的直接推论，但数学家曾长期认为这是纯线性代数定理。
- **在 ZF 中接受该命题的不可证性**：Cohen 的独立性结果表明，存在无基的向量空间模型与“任意空间有基”模型都兼容。
- **用“极大线性无关集”作为关键中间构造**：该构造在 ZFC 中可通过 Zorn 引理完成，在 ZF 中则可能无法保证其存在。

### 6.5.2 为什么机器难以自动迁移

机器可以自动应用 Zorn 引理完成 ZFC 证明，但**判断“极大线性无关集 ⇒ 基”这一步是否在 ZF 中仍然合法**需要集合论独立性知识。识别 AC 是隐性依赖也需要历史经验。

## 6.6 断裂强度（Breakage Strength）

| 评估项 | 等级 | 说明 |
|---|---|---|
| **断裂强度** | 🔴 结论反转或不可证 | ZFC 中“任意向量空间有基”可证；ZF 中不可证（Cohen 独立性 + Blass 反向结果）。 |
| **S 层影响** | 低 | “基”的术语相同。 |
| **M 层影响** | 高 | 存在性结论在替代基础中失效，核心工具 Zorn 引理不可用。 |
| **P 层影响** | 中高 | 形式化中需显式声明是否使用 `Classical.choice` 或类似公理。 |

**判定**：本组迁移是**公理移除导致的存在性结论不可证**，故评为 🔴。

## 7. 人类科学家可执行的验证动作

1. **B 岗位**：核对 Cohen (1963) 力迫法模型中是否存在无基向量空间，参考 Jech / Kunen 教材。
2. **C 岗位**：核对 Blass (1984) 论文中“每个向量空间有基 ⇒ 某种 AC”的具体形式。
3. **D 岗位**：检查两份报告的 `AxiomaticBase` 字段是否已显式声明（`ZFC` vs `ZF`）。
4. **E 岗位**：在 Lean 4 中尝试禁用 `Classical.choice` 后证明 `exists_basis`，观察证明失败位置。
5. **F 岗位**：生成两份报告的 PDF 并对比“任意”一词在全称量词中的覆盖范围（有限维 vs 无限维）。

---

## 8. 文献引用纪律检查

| 引用对象 | 真实性 | 支持性 | 说明 |
|---|---|---|---|
| Cohen (1963) 力迫法 | ✅ | ✅ | AC 独立于 ZF 的奠基性工作。 |
| Blass (1984) 反向结果 | ✅ | ✅ | "Every vector space has a basis implies AC"。 |
| Jech / Kunen 集合论教材 | ✅ | ✅ | 标准参考。 |
| Zorn 引理与 AC 的等价性 | ✅ | ✅ | 标准集合论事实。 |
| Mathlib `exists_basis` | ✅ | ✅ | 形式化层参考。 |

**核查结论**：所有引用对象真实存在，支持方向与本对比报告一致。

---

## 9. 署名与许可

**Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0**

搬运、改写或教学引用请注明来源与本页面链接。
