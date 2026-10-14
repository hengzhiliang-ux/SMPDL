# SMPDL 单体审计：一阶逻辑视角下的紧致性与 LS 定理

> **审计对象**：一阶逻辑的紧致性定理与 Löwenheim–Skolem 定理  
> **审计日期**：2026-10-14  
> **审计框架**：Göttingen S/M/P × D/L v1.5  
> **历史编号**：H21-PreFix  
> **总体评价**：⚪ 已确认正确（在一阶语义内）；两条元定理标志一阶逻辑的"柔性"。

---

## 1. 声明与版本

**主声明**（一阶两大元定理）：

1. **紧致性定理**：理论 `T` 的每个有限子集可满足 ⇒ `T` 可满足。
2. **（向下）Löwenheim–Skolem**：`T` 有无限模型 ⇒ `T` 有可数模型。

**证明骨架**：
- 紧致性：Henkin 常量 + Zorn 引理扩展极大一致集 → 模型（依赖 AC/超滤）。
- LS：Skolem 函数化 + 子模型闭包取可数片段。

**结构性后果**：
- 非标准分析模型（含无穷小 `*ℝ`）由紧致性直接构造——H6 的非标准分析在元层正是一阶紧致性的应用；
- Skolem 悖论：ZFC 若有模型则有望可数模型（而内部证明存在不可数集）——"可数/不可数"是**模型相对**的。

**版本信息**：
- **形式化基础**：一阶模型论（Löwenheim 1915；Skolem 1920；Gödel 紧致性 1930）
- **依赖前提**：一阶量词语义、Henkin 构造、选择公理
- **AxiomaticBase**：`FirstOrderLogic` + `CompactnessLS`
- **历史定位**：一阶逻辑"表达力弱但元性质好"的黄金组合。

---

## 2. S/M/P × D/L 六格审计

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| 一阶量词 | 仅论域元素 | ✅ |
| Henkin 常量 | 见证扩充 | ✅ |
| 紧致性 | 有限⇒整体 | ✅ |
| LS 向下 | Skolem 闭包 | ✅ |
| Skolem 悖论 | 相对性 | ✅ |

### 2.2 S*L — 语义逻辑结构

- 一阶语义核心：**量词只遍历论域元素**，不能量化关系/子集——表达力受限换来元定理。
- "不可数"在模型内是语句集合的效应，模型外观可以可数（Skolem 相对性）。
- ⚠️ 风险：把"不可数"当作跨模型的绝对属性。

### 2.3 M*D — 数学依存

```text
FirstOrderMetatheorems
    │
    ├── Henkin construction (witness constants)
    │
    ├── Zorn/AC → maximal consistent set
    │
    ├── Compactness theorem
    │
    ├── Skolemization → downward LS
    │
    └── Applications: nonstandard models, Skolem paradox
```

### 2.4 M*L — 数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| 紧致性证明 | ✅ | Henkin + Zorn。 |
| LS 证明 | ✅ | Skolem 闭包可数。 |
| 非标准模型构造 | ✅ | 紧致性直接应用。 |
| Skolem 悖论解释 | ✅ | 内/外视角相对性。 |

### 2.5 P*D / P*L — 编程层

- Mathlib：`FirstOrder` 框架相当完整（紧致性在 `ModelTheory` 发展中）。

---

## 3. 判定

| 维度 | 状态 |
|---|---|
| 声明真实性 | ⚪ 真 |
| 证明正确性 | ⚪ 正确 |
| 形式化验证 | 🟢 较成熟 |
| 兼容性 | ✅ 模型论标准 |

**SMPDL 判定**：⚪ **低风险 / 已确认正确**。

---

## 4. 人类科学家可执行的验证动作

1. 用 Henkin 构造写出紧致性证明的极大一致集步骤。
2. 由紧致性构造含无穷小的 `*ℝ` 初等扩充。
3. 阐述 Skolem 悖论为何不是矛盾（内/外视角）。

---

## 5. 署名与许可

**Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0**
