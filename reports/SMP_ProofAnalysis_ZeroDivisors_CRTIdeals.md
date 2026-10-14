# SMPDL 单体审计：ℤ/n 与含零因子环视角下的分解语义

> **审计对象**：零因子存在时的结构——模算术、理想论与分解几何  
> **审计日期**：2026-10-14  
> **审计框架**：Göttingen S/M/P × D/L v1.5  
> **历史编号**：H38-PostFix  
> **总体评价**：⚪ 已确认正确——零因子解禁不是缺陷而是分解信息的载体；γ 回收（理想论）已成熟。

---

## 1. 声明与版本

**主声明**（零因子世界的三重结构）：交换环 R 含零因子时：

1. **消去律失效**：ℤ/6 中 `2·3 = 0`，`2·3 = 2·0` 但 `3 ≠ 0`——非零元不可消去；
2. **中国剩余定理（CRT）——分解的代数引擎（γ 核心）**：
   - `ℤ/6 ≅ ℤ/2 × ℤ/3`（n = ∏pᵢ ⇒ ℤ/n ≅ ∏ℤ/pᵢ）；
   - 零因子结构**精确编码环的直积分解**——CRT 把"坏环"翻译成"好环的乘积"；
   - **γ 已实现**：理想论（理想 = "广义零因子"的精确化）+ CRT + 素理想分解——**零因子从 bug 升维为分解理论的 feature**（19 世纪 Dedekind/Kummer 完成）；
3. **β 对象族**：
   - ℤ/n 全谱（n 的素因子分解 ↔ 环结构分解——算术与代数的字典）；
   - **幂零元**（aⁿ=0）：切空间/形变理论的主角（H14 概形的幂零信息 = PostFix 侧核心，非 reduced 簇的切结构）；
   - **正合零因子结构**：零化子理想谱（associated primes）——模论的分解不变量；
4. **几何镜像（H14 桥）**：`Spec(R×S) = Spec R ⊔ Spec S`——环的零因子分解 = 簇的拓扑分解；幂零元 = 簇的"无穷小肥肉"（非 reduced 结构）。

**结构性后果**：
- 唯一性语言降档：不可约分解在含零因子环失效，代之以**素理想分解**（Dedekind 域中理想唯一分解为素理想——比元素分解更稳健）；
- "方程求解"语义改变：ab=0 有非平凡解 ⇒ 解集是簇的并。

**版本信息**：
- **形式化基础**：Gauss 1801（ℤ/n 结构）；Kummer 1840s（理想数起源）；Dedekind 1871（理想论）；Noether 1920s
- **依赖前提**：交换环
- **AxiomaticBase**：`CommutativeRing` + `ZeroDivisors`（+ CRT）
- **历史定位**：γ（理想论）历史上正是**为修复零因子世界的唯一分解**而发明——"回收"不是比喻而是历史的因果。

---

## 2. S/M/P × D/L 六格审计

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| ℤ/6 消去失效 | 显式反例 | ✅ |
| CRT 分解 | n=∏p ⇒ ∏ℤ/p | ✅ |
| 理想论回收 | Dedekind | ✅ |
| 幂零元 β 对象 | 切空间/形变 | ✅ |
| 几何镜像 | Spec 分解 | ✅ |

### 2.2 S*L — 语义逻辑结构

- 零因子语义反转：**"ab=0 不再是丑闻而是信息"**——它告诉你环/簇如何分解；
- 唯一性语言迁移：元素分解 → 理想分解（更稳健——Kummer/Dedekind 的历史教训："当元素背叛你，发明更大的结构"）；
- ⚠️ 风险：在含零因子环谈"不可约分解唯一"；忽略幂零元的几何意义（把非 reduced 簇当 reduced）。

### 2.3 M*D — 数学依存

```text
ZeroDivisorWorld
    │
    ├── cancellation fails (Z/6 example)
    │
    ├── CRT: Z/n ≅ ∏ Z/p — factorization encoded
    │
    ├── ideal theory (Dedekind): prime ideal factorization recovers uniqueness
    │       └── γ realized (Kummer→Dedekind: invented FOR the repair)
    │
    ├── nilpotents (β): tangent/deformation theory (H14 non-reduced schemes)
    │
    └── geometry: Spec(R×S) = disjoint union; nilpotents = infinitesimal fuzz
```

### 2.4 M*L — 数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| CRT | ✅ | 同构构造。 |
| 理想唯一分解 | ✅ | Dedekind 域。 |
| 幂零-切空间 | ✅ | Zariski 切空间 = m/m²。 |
| Spec 分解 | ✅ | 拓扑字典。 |

### 2.5 P*D / P*L — 编程层

- Mathlib：`ZMod n`、CRT、理想/素谱形式化成熟——P 层 🟢（CRT 有显式构造）。

---

## 3. 判定

| 维度 | 状态 |
|---|---|
| 声明真实性 | ⚪ 真 |
| 证明正确性 | ⚪ 正确（Gauss/Dedekind） |
| 形式化验证 | 🟢 |
| 兼容性 | ✅ 交换代数标准 |

**SMPDL 判定**：⚪ **低风险 / 已确认正确**。

---

## 4. 人类科学家可执行的验证动作

1. 在 ℤ/6 验证消去失效与 CRT 同构。
2. 对比 ℤ[√-5] 中元素分解不唯一 vs 理想分解唯一（Kummer 场景）。
3. 说明 ℂ[x,y]/(xy) 的零因子如何编码十字簇的两个分支。

---

## 5. 署名与许可

**Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0**
