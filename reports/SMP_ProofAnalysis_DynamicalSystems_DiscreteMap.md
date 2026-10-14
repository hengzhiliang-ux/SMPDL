# SMPDL 单体审计：离散映射视角下的混沌与迭代不变量

> **审计对象**：离散时间映射的混沌现象与 Poincaré 截面桥  
> **审计日期**：2026-10-14  
> **审计框架**：Göttingen S/M/P × D/L v1.5  
> **历史编号**：H25-PostFix  
> **总体评价**：⚪ 已确认正确（在离散迭代语义内）；连续侧定理大面积失效。

---

## 1. 声明与版本

**主声明**（离散侧的定理失效 + 自有理论）：

1. **P–B 类定理不存在**：离散映射无 ω-极限集二分——一维区间映射即可产生任意复杂动力学。**Li–Yorke 定理**（1975）：周期 3 ⇒ 混沌（不可数 scrambled 集）；**Sharkovsky 序**：周期 3 ⇒ 一切周期。 Logistic 映射 `x ↦ 4x(1-x)` 在 [0,1] 混沌。
2. **不变量更换**：Lyapunov 指数、拓扑熵 `h_top` 成为混沌计量；连续侧的 div/Dulac 判据**无对应**（导数结构消失）。
3. **Poincaré 截面桥（连续→离散单向）**：周期轨道附近取横截面 Σ，流诱导**首次回归映射** `P: Σ → Σ`——把连续流降维为离散映射；方向单向（不动的 Poincaré 映射只捕捉截面动力学，不还原全流）。

**版本信息**：
- **形式化基础**：离散动力系统（Sharkovsky 1964；Li–Yorke 1975；May 1976）
- **依赖前提**：迭代复合、紧性
- **AxiomaticBase**：`DiscreteDynamics` + `IterationMap`
- **历史定位**："周期三意味着混沌"是混沌理论的流行语诞生点。

---

## 2. S/M/P × D/L 六格审计

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| 迭代 f∘f∘…∘f | 离散时间 | ✅ |
| 周期点/轨道 | 离散核心 | ✅ |
| Sharkovsky 序 | 周期蕴含链 | ✅ |
| Li–Yorke 混沌 | scrambled 集 | ✅ |
| 拓扑熵 | 复杂度计量 | ✅ |
| Poincaré 截面 | 连→离桥 | ✅ |

### 2.2 S*L — 语义逻辑结构

- 离散语义：无导数场、无 Jordan 拓扑支撑——连续侧两大支柱同时消失。
- "混沌"是离散侧自有概念：初值敏感 + 传递 + 周期点稠密（Devaney）。
- ⚠️ 风险：把 Dulac/div 判据（连续专属）用于离散系统；或以为 Poincaré 截面可逆还原全流。

### 2.3 M*D — 数学依存

```text
DiscreteDynamics
    │
    ├── Iteration x_{n+1} = f(x_n)
    │
    ├── Period-p points, Sharkovsky ordering
    │       └── period 3 ⇒ all periods
    │
    ├── Li–Yorke chaos, topological entropy
    │
    ├── No div/Dulac analog (no derivatives)
    │
    └── Poincaré section: continuous flow → return map (one-way, dim -1)
```

### 2.4 M*L — 数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| Sharkovsky 定理 | ✅ | 区间映射周期全谱。 |
| Li–Yorke | ✅ | 周期3⇒混沌。 |
| 拓扑熵 | ✅ | 复杂度不变量。 |
| 截面桥单向性 | ✅ | 降维不可逆。 |

### 2.5 P*D / P*L — 编程层

- 迭代仿真是数值最友好的对象（无步长误差累积问题）；分叉图、Lyapunov 指数一键计算。

---

## 3. 判定

| 维度 | 状态 |
|---|---|
| 声明真实性 | ⚪ 真 |
| 证明正确性 | ⚪ 正确 |
| 形式化验证 | 🟡（数值强） |
| 兼容性 | ✅ 动力系统标准 |

**SMPDL 判定**：⚪ **低风险 / 已确认正确**。

---

## 4. 人类科学家可执行的验证动作

1. 数值演示 logistic `4x(1-x)` 的混沌轨道与周期 3 窗口。
2. 验证 Sharkovsky 序的蕴含方向（周期 3 ⇒ 周期 5）。
3. 对简谐振子取 Poincaré 截面，验证回归映射为旋转，并思考信息损失。

---

## 5. 署名与许可

**Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0**
