# SMPDL 单体审计：非结合代数视角下的交错律与例外结构

> **审计对象**：八元数与李代数中结合律失效后的残存结构  
> **审计日期**：2026-10-14  
> **审计框架**：Göttingen S/M/P × D/L v1.5  
> **历史编号**：H28-PostFix  
> **总体评价**：⚪ 失效声明正确——括号敏感性登场；交错律/雅可比恒等式成为"残存律"。

---

## 1. 声明与版本

**主声明**（非结合世界的三条战线）：

**A. 八元数 𝕆（Graves 1843.12 / Cayley 1845）**：
1. **结合律失效**：存在 `a,b,c ∈ 𝕆` 使 `(ab)c ≠ a(bc)`；
2. **交错律（alternativity）残存**：`a(ab) = a²b` 且 `(ab)b = ab²`（任意两元素生成的子代数**是**结合的——Artin 定理）；
3. **Hurwitz 定理（1898）**：ℝ 上**赋范可除**代数（含幺，范数乘性）仅有 ℝ、ℂ、ℍ、𝕆——维数封顶 8，结合律的松动换来最后一层"数系"；
4. **乘法恒等式降级链**：交换（ℂ/ℝ）→ 仅结合（ℍ）→ 仅交错（𝕆）→ 再往下（sedenions）连可除都失去（零因子出现）。

**B. 李代数 𝔤（Lie 1870s–1880s）**：
1. 乘法 `[x,y]` **反交换**（`[x,y] = -[y,x]`，⇒ `[x,x]=0`）且**非结合**；
2. 取代结合律的是**雅可比恒等式**：`[x,[y,z]] + [y,[z,x]] + [z,[x,y]] = 0`；
3. 李括号的**原生来源**是结合代数的交换子 `[a,b]=ab-ba`——结合世界"派生"出非结合结构（李三明治嵌入），雅可比恒等式正是交换子结合性的投影。

**C. 括号敏感性后果**：
- `aⁿ` 在一般非结合代数中**不良定义**（须写明括号，如 `((aa)a)a ≠ (aa)(aa)` 可能不同）；
- 交错代数中 `aⁿ` 对**单生成元**恢复良定义（Artin 定理特例）。

**版本信息**：
- **形式化基础**：Graves/Cayley（八元数 1843/45）；Lie（李代数）；Hurwitz 1898；Artin 交错理论 1950s 定型（Zorn 1931 早期）
- **依赖前提**：二元乘法、（可选）范数/可除
- **AxiomaticBase**：`NonAssociativeAlgebra` + `AlternatingLaw` / `JacobiIdentity`
- **历史定位**：Hamilton 1843.10 砸碎交换律仅两个月后（1843.12），他的朋友 Graves 就砸碎了结合律——代数律减法的连环两个月。

---

## 2. S/M/P × D/L 六格审计

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| 括号树语义 | 乘法 = 二叉树，不可压扁 | ✅ |
| 交错律 | 两元素子代数结合（Artin） | ✅ |
| 雅可比恒等式 | 李括号的替代律 | ✅ |
| Hurwitz 维数封顶 | 1,2,4,8 | ✅ |
| 零因子降临 | sedenions（16 维）起 | ✅ |

### 2.2 S*L — 语义逻辑结构

- 非结合语义：**括号是语义的一部分**——`(ab)c` 与 `a(bc)` 是不同对象；"乘积"从数变成树。
- 律的残存阶梯：结合 → 交错 → 无律，每级保留一部分记号合法性（交错保单生成元幂）。
- ⚠️ 风险：在八元数/李代数中写 `abc` 或 `aⁿ` 而不声明括号；把雅可比恒等式当作"某种结合"的等价物（它是**反**结合的替代品）。

### 2.3 M*D — 数学依存

```text
NonAssociativeWorlds
    │
    ├── Octonions 𝕆: (ab)c ≠ a(bc) sometimes
    │       ├── Alternativity survives (Artin: 2-gen subalgebras associative)
    │       └── Hurwitz: normed division ⇒ dim ∈ {1,2,4,8}, 𝕆 is terminal
    │
    ├── Lie algebras: bracket anticommutative + Jacobi (NOT associative)
    │       └── derived from associative: [a,b]=ab-ba embeds (sandwich)
    │
    └── Bracket sensitivity: a^n ill-defined in general;
        recovered for single generator under alternativity
```

### 2.4 M*L — 数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| 八元数结合反例 | ✅ | 具体三元组可显式验证。 |
| Artin 定理 | ✅ | 两生成元子代数结合。 |
| Hurwitz 定理 | ✅ | 赋范可除封顶 8 维。 |
| 雅可比 ⇔ 交换子投影 | ✅ | 结合代数派生李结构。 |

### 2.5 P*D / P*L — 编程层

- Mathlib：`Octonions` 已形式化（`Mathlib.Algebra.Octonions`）；李代数 `LieAlgebra`/`LieRing` 框架完整（含雅可比公理）——**P 层两侧都好**，但 `pow` API 在非结合侧**不可用**（库设计本身编码了断裂）。

---

## 3. 判定

| 维度 | 状态 |
|---|---|
| 声明真实性 | ⚪ 真（失效 + 残存结构正确） |
| 证明正确性 | ⚪ 正确（Graves/Cayley/Hurwitz/Artin） |
| 形式化验证 | 🟢 八元数与李代数均有 |
| 兼容性 | ✅ 非结合代数标准 |

**SMPDL 判定**：⚪ **低风险 / 已确认正确**。

---

## 4. 人类科学家可执行的验证动作

1. 在 𝕆 的 Cayley-Dickson 构造中取具体三元组验证 `(ab)c ≠ a(bc)`。
2. 验证任意 `a,b ∈ 𝕆` 生成的子代数是结合的（Artin 定理小例）。
3. 验证交换子 `[a,b]=ab-ba` 在结合代数中自动满足雅可比恒等式（"派生"通道）。
4. 检查 Mathlib 中 `Octonions` 是否不提供 `pow` 实例（断裂的库级体现）。

---

## 5. 署名与许可

**Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0**
