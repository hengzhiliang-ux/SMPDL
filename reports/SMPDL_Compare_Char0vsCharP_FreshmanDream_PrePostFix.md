# SMPDL 基础对比审计：特征 0 vs 特征 p 的二项式恒等式

> **对比对象**
> - “PreFix” 版本：特征 0 下完整二项式展开（见 `SMP_ProofAnalysis_Characteristic0_FreshmanDream.md`）
> - “PostFix” 版本：特征 p 下 Freshman's Dream（见 `SMP_ProofAnalysis_CharacteristicP_FreshmanDream.md`）
> 
> **审计日期**：2026-10-13  
> **审计框架**：Göttingen S/M/P × D/L v1.5  
> **总体评价**：⚪ ↔ ⚪ 两个版本在各自基础内均正确；差异来自“特征”这一基础假设，而非证明错误。

---

## 1. 版本声明对比

| 维度 | 特征 0 版本（PreFix） | 特征 p 版本（PostFix） |
|---|---|---|
| **主声明** | \((a+b)^p = \sum_{k=0}^{p} \binom{p}{k} a^k b^{p-k}\) | \((a+b)^p = a^p + b^p\) |
| **基础假设** | `CharZero R` | `CharP R p` |
| **关键数论事实** | \(p \nmid \binom{p}{k}\)（\ 0 < k < p \) | \(p \mid \binom{p}{k}\)（\ 0 < k < p \) |
| **展开结果** | \(p+1\) 项全部保留 | 仅保留首尾两项，中间项消失 |
| **常见误用** | 误以为 Freshman's Dream 成立 | 误用到特征 0 或合数指数 |
| **Mathlib 引理** | `add_pow` | `add_pow_char_of_commute` |

---

## 2. PreFix 版本 SMPDL 速览（特征 0）

详见 `SMP_ProofAnalysis_Characteristic0_FreshmanDream.md`。

- **S*D**：自然语言依赖“二项展开 → 中间系数非零 → 完整求和”。
- **S*L**：量词清晰；风险在于与特征 p 情形混淆。
- **M*D**：`CommRing` + `CharZero` + `Nat.choose` + 数论事实 \(p \nmid \binom{p}{k}\)。
- **M*L**：逻辑结构完整；Freshman's Dream 在此不成立。
- **P*D / P*L**：Mathlib 中 `add_pow` 可直接形式化。

**PreFix 判定**：⚪ 已确认正确。

---

## 3. PostFix 版本 SMPDL 六格审计（特征 p）

### 3.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| 命题 \((a+b)^p = a^p + b^p\) | 待证明 | ✅ |
| 二项展开 | 分配律 + 组合计数 | ✅ |
| 系数被 p 整除 | 数论引理 | ✅ |
| 特征 p 使系数为零 | `CharP R p` 定义 | ✅ |
| 结论 | 仅两项保留 | ✅ |

### 3.2 S*L — 语义逻辑结构

- “特征 p”必须明确是“p 是最小正整数使得 p·1=0”。
- 证明从展开到结论的跳跃关键在于“\(p \mid \binom{p}{k}\)”；自然语言中这一步常被省略。
- ⚠️ 教学风险：学生容易把 Freshman's Dream 记成“指数分配律”并滥用。

### 3.3 M*D — 数学依存

```text
FreshmanDream_CharP
    │
    ├── CommRing R
    │
    ├── CharP R p
    │
    ├── add_pow: (a+b)^p = Σ_{k=0}^p C(p,k) a^k b^{p-k}
    │
    ├── Lemma: p | C(p,k) for 0 < k < p
    │
    └── Conclusion: (a+b)^p = a^p + b^p
```

- 依赖关系闭合。

### 3.4 M*L — 数学逻辑结构

| 检查项 | 特征 0 | 特征 p | 差异说明 |
|---|---|---|---|
| 量词范围 | 任意 a,b ∈ R | 任意 a,b ∈ R | 相同 |
| 边界情况 | a=0 或 b=0 退化 | a=0 或 b=0 退化 | 相同 |
| 隐藏假设 | 无 | p 必须是素数 | 关键差异 |
| 数论引理 | \(p \nmid C(p,k)\) | \(p \mid C(p,k)\) | 结论反转 |
| 结论项数 | \(p+1\) 项 | 2 项 | 结构差异 |

### 3.5 P*D / P*L — 编程层

- 特征 0：使用 `add_pow` + `CharZero`。
- 特征 p：使用 `add_pow_char_of_commute` + `CharP R p`。
- 两个形式化版本在 Lean 4 中都非常简短，但依赖的类型类不同：`CharZero` vs `CharP`。

---

## 4. 跨层映射检查（PostFix vs PreFix）

| 映射 | 特征 0（PreFix） | 特征 p（PostFix） | 变化 |
|---|---|---|---|
| S → M | “完整展开”→ `add_pow` | “两项恒等”→ `add_pow_char_of_commute` | M 层引理不同 |
| M → P | `CharZero` 约束 | `CharP R p` 约束 | 类型类不同 |
| S ↔ P | 求和表达式 | 两项等式 | 形式化目标不同 |
| S ↔ S | 结论形式：求和 | 结论形式：两项 | `S-ISO` |
| M ↔ M | 中间系数非零 | 中间系数为零 | `M-ISO` |
| P ↔ P | `Finset.sum` | 直接等式 | `P-BISIM`（都经展开，但化简结果不同） |

**跨层结论**：两个版本的 S/M/P 层各自自洽，但基础假设 `CharZero` vs `CharP R p` 改变了 M 层数论事实，从而改变了 S 层结论形式和 P 层形式化目标。

---

## 5. 判定：PostFix 是否为真？

| 维度 | 特征 0（PreFix） | 特征 p（PostFix） |
|---|---|---|
| 自然语言声明真实性 | ⚪ 真 | ⚪ 真 |
| 证明正确性 | ⚪ 正确 | ⚪ 正确 |
| 形式化验证 | ⚪ Mathlib 直接支持 | ⚪ Mathlib 直接支持 |
| 与已知数学兼容性 | ✅ 与特征 0 交换环兼容 | ✅ 与特征 p 交换环兼容 |
| 误迁移风险 | 低 | 🟡 中（极易被滥用） |

**SMPDL 判定（PostFix）**：⚪ **低风险 / 已确认正确**。Freshman's Dream 在特征 p 下成立，但教学与审校中必须强调其适用范围。

---

## 6. 变化类型归类

- **变化方式**：**基础假设迁移**（`CharZero` → `CharP R p`）+ **数论事实反转**（\(p \nmid C(p,k)\) → \(p \mid C(p,k)\)）。
- **核心假设差异**：
  - 特征 0：所有正整数系数在环中保持非零。
  - 特征 p：素数 p 在环中“死亡”，导致其倍数系数归零。
- **证明骨架相似性**：两者都从二项展开出发；差异仅在第二步对系数的处理。
- **SMPDL 同构标签建议**：`S-ISO`（结论形式不同）、`M-ISO`（数论事实不同）、`P-BISIM`（展开程序相似）。
- **关键 lesson**：同一展开骨架在不同特征下可能得到截然相反的简化结果；AI 或人类作者若未显式声明 `CharP R p`，则不能直接写出 Freshman's Dream。

---

## 7. 人类研究者可执行的验证动作

1. **B 岗位**：核对特征 p 版本中 \(p \mid \binom{p}{k}\) 的证明是否完整（可用组合恒等式 \(\binom{p}{k} = \frac{p}{k} \binom{p-1}{k-1}\) 验证）。
2. **C 岗位**：检查合数指数情形（如 \(n=4\)）下 \((a+b)^n = a^n + b^n\) 是否一般不成立，以确认“p 为素数”前提的必要性。
3. **D 岗位**：检查两份报告的 `AxiomaticBase` 字段是否已显式声明为 `Characteristic0` 与 `CharacteristicP`。
4. **E 岗位**：对两份 Markdown 报告做 diff，确认 `CharZero`/`CharP`、`p \nmid`/`p \mid`、求和/两项等关键差异是否准确标注。

---

## 8. 文献引用纪律检查

| 引用对象 | 真实性 | 支持性 | 说明 |
|---|---|---|---|
| 标准二项式定理 | ✅ | ✅ | 两版本共同依赖。 |
| 初等数论 \(p \mid \binom{p}{k}\) | ✅ | ✅ | 特征 p 版本核心。 |
| Dummit & Foote, *Abstract Algebra* | ✅ | ✅ | Freshman's Dream 标准来源。 |
| Mathlib `add_pow` / `add_pow_char_of_commute` | ✅ | ✅ | 形式化层支持。 |

**核查结论**：引用对象真实存在，支持方向与本对比报告一致。

---

## 9. 署名与许可

**Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0**

搬运、改写或教学引用请注明来源与本页面链接。
