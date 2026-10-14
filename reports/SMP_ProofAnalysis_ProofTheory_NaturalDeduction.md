# SMPDL 单体审计：自然演绎视角下的切消去与规范性

> **审计对象**：Gentzen 自然演绎（NK/NJ）的切消去（规范化）定理  
> **审计日期**：2026-10-14  
> **审计框架**：Göttingen S/M/P × D/L v1.5  
> **历史编号**：H22-PostFix  
> **总体评价**：⚪ 已确认正确——切消去/规范化成立，子公式性质、一致性证明、Curry–Howard 全部由此而来。

---

## 1. 声明与版本

**主声明**（Gentzen Hauptsatz，自然演绎形式）：自然演绎系统中每个证明都可**规范化**（normalize）：消除所有 detour（先 →引入后 →消除的迂回），得到满足**子公式性质**的正规证明——证明中每个公式都是结论的子公式。

**关键推论**：
1. **一致性**：若系统不一致则空上下文可推出任意式，规范化后得纯原子矛盾——不可能；
2. **直觉主义存在性质**：正规直觉主义证明 `⊢ ∃x A(x)` 的末端是显式 witness `t`——构造性信息提取；
3. **Curry–Howard 同构**：证明 = λ 项；detour 消除 = β 归约；强正规化 = SN；
4. **相继式演算的 cut elimination** 是其姊妹形式（Gentzen 1935 原版）。

**版本信息**：
- **形式化基础**：Gentzen (1935)；Prawitz 规范化 (1965)
- **依赖前提**：引入/消除规则对偶、归纳于证明结构
- **AxiomaticBase**：`NaturalDeduction` + `Normalization`
- **历史定位**：证明论的诞生——"证明本身成为数学对象"。

---

## 2. S/M/P × D/L 六格审计

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| 引入/消除规则对偶 | 联结词意义即用法 | ✅ |
| detour（最大公式） | 引入后立即消除 | ✅ |
| 规范化定理 | detour 可全消 | ✅ |
| 子公式性质 | 正规证明结构约束 | ✅ |
| Curry–Howard | 证明=程序 | ✅ |

### 2.2 S*L — 语义逻辑结构

- 自然演绎语义：**每个联结词由引入/消除对定义**——意义论先行，公理近零。
- 直觉主义片段（NJ）在规范化的加持下获得存在 witness 提取——与 H7 的构造语义在**证明论层**接通。
- ⚠️ 风险：把经典 NK 的规范化与 NJ 混同——经典系统需要额外控制（如 Prawitz 的经典规范化变体）。

### 2.3 M*D — 数学依存

```text
NaturalDeduction
    │
    ├── Intro/Elim rule pairs
    │
    ├── Detours = maximal formulas
    │
    ├── Normalization theorem (Prawitz 1965)
    │       └── local reductions, termination
    │
    ├── Subformula property
    │
    └── Consequences: consistency, witness extraction, Curry–Howard
```

### 2.4 M*L — 数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| 规范化定理 | ✅ | 对证明结构归纳。 |
| 子公式性质 | ✅ | 正规形核心性质。 |
| 一致性证明 | ✅ | 相对 PRA。 |
| witness 提取 | ✅ | 直觉主义片段。 |

### 2.5 P*D / P*L — 编程层

- Lean/Coq/Agda 的核心就是自然演绎 + Curry–Howard——本组 PostFix 是整个证明助手产业的逻辑地基。

---

## 3. 判定

| 维度 | 状态 |
|---|---|
| 声明真实性 | ⚪ 真 |
| 证明正确性 | ⚪ 正确（Gentzen/Prawitz） |
| 形式化验证 | 🟢 证明助手原生 |
| 兼容性 | ✅ 现代证明论 |

**SMPDL 判定**：⚪ **低风险 / 已确认正确**。

---

## 4. 人类科学家可执行的验证动作

1. 写出一个含 detour 的 NJ 证明并手动规范化。
2. 由子公式性质证明 NJ 的一致性。
3. 对 `⊢ ∃x (x = t)` 规范化，提取 witness。

---

## 5. 署名与许可

**Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0**
