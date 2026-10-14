# SMPDL 单体审计：多复变视角下的 Hartogs 现象与全纯域

> **审计对象**：多复变中 Hartogs 现象与全纯域（域的全纯凸性）理论  
> **审计日期**：2026-10-14  
> **审计框架**：Göttingen S/M/P × D/L v1.5  
> **历史编号**：H19-PostFix  
> **总体评价**：⚪ 已确认正确（在多复变语义内）；结论与单复变直觉直接冲突。

---

## 1. 声明与版本

**主声明**（Hartogs 现象，1906）：在 `ℂⁿ`（`n ≥ 2`）中，存在域 `Ω` 与紧集 `K ⊂ Ω`，使得**每一个**在 `Ω \ K` 上全纯的函数都自动延拓到整个 `Ω` 上全纯。

**Hartogs 球壳现象**：设 `n ≥ 2`，域

```text
Ω = { z ∈ ℂⁿ : (|z| < R_outer) } \ { z : (|z| ≤ R_inner) }（去掉实心球后）
```

的任意同心"洞" `K = {|z| ≤ r < R_inner, w-坐标受限}` 上——更精确的经典形式：单位多圆柱中挖去"竖直薄集"后，全纯函数必然填回。

**推论（Hartogs 延拓定理）**：`n ≥ 2` 时，`ℂⁿ` 中**紧集上的孤立奇点不存在**——孤立奇点必可去。

**结构性后果**：
1. 并非每个域都是全纯域（domain of holomorphy）；
2. "全纯域"由 Cartan–Thullen 刻画为**全纯凸**域；
3. Levi 问题的提出与解决（伪凸性 ⇔ 全纯域）成为多复变核心课题；
4. `n=1` 与 `n≥2` 的分歧是**维度引发的定性断裂**。

**版本信息**：
- **形式化基础**：多复变函数论（Hartogs 1906；Cartan–Thullen 1932；Oka 1940s；Grauert 1950s）
- **依赖前提**：Cauchy 积分（逐变量）、多圆柱展开、全纯凸性
- **AxiomaticBase**：`SeveralComplexVariables` + `HolomorphicConvexity`
- **历史定位**：Hartogs 1906 是多复变学科的出生证明——第一个"多变量特有"现象。

---

## 2. S/M/P × D/L 六格审计

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| 多圆柱 Cauchy 积分 | 逐变量积分 | ✅ |
| Hartogs 现象 | n≥2 的几何余维 | ✅ |
| 全纯域定义 | 不能延拓出边界的域 | ✅ |
| Cartan–Thullen 定理 | 全纯域 ⇔ 全纯凸 | ✅ |
| Levi 问题 | 伪凸 ⇔ 全纯域 | ✅ |

### 2.2 S*L — 语义逻辑结构

- 多复变的语义反转：**"域"不再自由**——某些域上全体全纯函数"被迫"延拓出去，域本身不是任何函数的自然定义域。
- 孤立奇点消失：`n≥2` 中紧集不能承载奇点，奇点必须"挂"在实余维 1 的集合上。
- ⚠️ 风险：把单复变的奇点分类/Laurent 工具直接搬入多复变——无对应物。

### 2.3 M*D — 数学依存

```text
SeveralComplexVariables
    │
    ├── Polydisc Cauchy formula (variable-by-variable)
    │
    ├── Hartogs phenomenon (n ≥ 2)
    │       └── codimension-2 "hole" auto-filled
    │
    ├── Isolated singularities removable
    │
    ├── Domain of holomorphy ≠ every domain
    │
    ├── Cartan–Thullen: holomorphically convex
    │
    └── Levi problem: pseudoconvex ⇔ domain of holomorphy
```

### 2.4 M*L — 数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| Hartogs 定理 | ✅ | n≥2 时洞自动填满。 |
| 孤立奇点可去 | ✅ | 与 n=1 本性奇点理论断裂。 |
| 非全纯域存在 | ✅ | 如去掉一点的单位球（n≥2）不是全纯域。 |
| Levi 问题 | ✅ | Oka（ℂⁿ 情形）等解决。 |

### 2.5 P*D / P*L — 编程层

- Mathlib：多复变形式化极少；`SeveralComplexVariables` 几乎空白。
- 这是 H19 两侧 P 层差距极大的一组：单复变成熟、多复变荒漠。

---

## 3. 判定

| 维度 | 状态 |
|---|---|
| 声明真实性 | ⚪ 真 |
| 证明正确性 | ⚪ 正确（Hartogs 1906） |
| 形式化验证 | 🔴 多复变形式化稀缺 |
| 兼容性 | ✅ 现代多复变标准 |

**SMPDL 判定**：⚪ **低风险 / 已确认正确**（但 P 层支持极弱）。

---

## 4. 人类科学家可执行的验证动作

1. 用逐变量 Cauchy 积分写出 Hartogs 延拓的核心构造（对 `z₁` 逐点延拓，用 `z₂...z_n` 方向的正则性）。
2. 验证 `B² \ {0}`（ℂ² 中去心球）上所有全纯函数延拓到 `B²`——孤立奇点可去。
3. 对比：`ℂ` 中 `f=1/z` 在去心圆盘上不可延拓——维度改变结论反转。

---

## 5. 署名与许可

**Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0**
