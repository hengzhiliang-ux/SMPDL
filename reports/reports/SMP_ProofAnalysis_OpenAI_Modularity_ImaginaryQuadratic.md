# SMPDL 审计报告：OpenAI「虚二次域上椭圆曲线的模性」

**审计对象**：Modularity of elliptic curves over imaginary quadratic fields  
**来源**：OpenAI math 仓库，2026-10-04 发布  
**审计日期**：2026-10-13  
**审计框架**：Göttingen S/M/P × D/L 六格审计 v1.5  
**审计结论**：🔴 **极高风险研究级声明。虚二次域上的椭圆曲线模性猜想是 Langlands 纲领在 non-totally-real 情形的关键问题；本 README 未披露任何证明策略。**

---

## 1. 命题与声明

论文声称：**每个定义在任意虚二次域 K 上的椭圆曲线 E 都是模性的**，即存在 K 上的 cuspidal automorphic representation π，使得 E 的 L-函数等于 π 的 L-函数；并且局部参数在每个地方都匹配。

---

## 2. S/M/P × D/L 六格审计

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| 虚二次域模性 | Galois 形变、automorphic cycles、p-adic 局部 Langlands | 🔴 策略未披露 |
| 每个地方局部参数匹配 | local-global 兼容性 | 🔴 策略未披露 |
| 与 ℚ 上模性的联系 | Wiles, Taylor, Breuil-Conrad-Diamond-Taylor | 🟡 已知 |

**发现**：README 仅一句话声明，未给出任何证明路线。

### 2.2 S*L — 语义逻辑结构

- "every elliptic curve over every imaginary quadratic field" — 极强全称量词。
- "matching local parameters at every place" — 要求完整的 local-global 对应。
- 风险：可能证明了对某些虚二次域或某些曲线成立，但未覆盖所有情况。

### 2.3 M*D — 数学依存

| 依赖 | 状态 |
|---|---|
| Calegari–Geraghty derived deformation theory | 🟡 已知工具 |
| Harris–Lan–Taylor–Thorne 潜在自守 | ⚠️ 未说明 |
| 虚二次域上的 automorphic cycles | ⚠️ 未说明 |
| p-adic Langlands / Emerton 完成上同调 | ⚠️ 未说明 |
| Fontaine–Mazur（虚二次域情形） | 🔴 相关且同样困难 |

**关键风险**：虚二次域不是 totally real，经典的 Taylor–Wiles 方法需要改用 derived 或 torsion 方法。需要同时处理复乘法（CM）和非 CM 曲线，以及多个分裂/惰性素数。

### 2.4 M*L — 数学逻辑结构

- 证明通常需要：
  1. 建立 E 的 Galois 表示与某个 automorphic 表示的对应；
  2. 证明局部参数匹配；
  3. 处理所有 conductor。
- 风险：可能某一步仅对 good reduction 或 ordinary 素数成立。

### 2.5 P*D — 编程/形式化依存

- 未明确提及 Lean。
- 若涉及具体虚二次域上曲线的计算，需确认覆盖范围。

### 2.6 P*L — 编程逻辑结构

- 若使用算法验证，需检查是否覆盖了所有判别式/所有 j-invariant。

---

## 3. TRAP-CHECK v1.0 风险点

| 陷阱类别 | 风险描述 | 等级 |
|---|---|---|
| T1 前视构造 | 用模性假设构造自守提升 | 🔴 高 |
| T2 量词滑移 | 「某些虚二次域」→「所有虚二次域」 | 🔴 高 |
| T3 同族依赖 | 可能与 010 Fontaine–Mazur 等同族结果互相依赖 | 🔴 高 |
| T5 领域障碍 | 虚二次域模性是长期核心问题 | 🔴 高 |
| T7 结论放大 | 从 potential modularity 宣称为完整 modularity | 🟡 中 |

---

## 4. 五人工岗位动作

| 岗位 | 动作 |
|---|---|
| **A 概念奇点审查** | 区分「potential modularity」「modularity」「local-global compatibility」 |
| **B 语义忠实审查** | 核对「every place」是否包括 ramified、additive places |
| **C 缺口刻画** | 要求披露：如何处理 non-ordinary 素数、CM 曲线、虚二次域的特殊性 |
| **D 陷阱预见** | 检查是否把 Calegari–Geraghty 的部分结果宣称为完整解决 |
| **E 验证解读** | 若给出具体例子，用已知的小 conductor 曲线验证 |

---

## 5. 人工可能需要确认/补充证明的地方

1. **Galois 表示来源**：明确 E 的 p-adic Galois 表示满足哪些条件（de Rham, Hodge–Tate,  potentially semistable）。
2. **自守循环构造**：在虚二次域上如何构造与 E 对应的 automorphic representation。
3. **Taylor–Wiles 系统**：说明如何应对 non-totally-real 带来的困难（derived deformation rings 等）。
4. **局部兼容性**：确认在 split、inert、ramified 素数处的局部 Langlands 对应。
5. **与 Fontaine–Mazur 的关系**：若该结果成立，是否反过来推出某些 Fontaine–Mazur 情形。

---

## 6. 文献引用纪律检查

| 引用对象 | 真实性 | 支持性 | 说明 |
|---|---|---|---|
| OpenAI 原论文 README/PDF | ✅ 真实 | ⚠️ 待查 | README 存在，PDF 未审计。 |
| Wiles–Taylor 模性定理 | ✅ 真实 | ✅ 支持 | ℚ 上模性已解决。 |
| Calegari–Geraghty, Harris–Lan–Taylor–Thorne | ✅ 真实 | ⚠️ 待查 | 若引用，需确认支持方向。 |
| OpenAI 同族修订稿 | ⚠️ 待查 | ⚠️ 待查 | 可能与 Fontaine–Mazur 等同族互相依赖。 |

**核查结论**：本报告基于声明强度与领域背景判定 🔴 高风险；具体引用支持性需 PDF 审计后补充。

---

## 7. 署名与许可

本审计使用 Göttingen S/M/P × D/L 框架 · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0
