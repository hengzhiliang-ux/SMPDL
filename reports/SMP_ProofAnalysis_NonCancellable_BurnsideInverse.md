# SMPDL 单体审计：非可消半群视角下的 Burnside 世界与逆半群

> **审计对象**：消去律失效后的半群宇宙——Burnside 问题、正则半群与逆半群理论  
> **审计日期**：2026-10-14  
> **审计框架**：Göttingen S/M/P × D/L v1.5  
> **历史编号**：H40-PostFix  
> **总体评价**：⚪ 失效声明正确——β 对象族解禁 + γ 因果型回收（逆半群为修复而建）双段涌现。

---

## 1. 声明与版本

**主声明**（非可消世界的结构）：消去律失效时：

1. **最小反例**：2 元变换半群 `T₂`（全变换幺半群）——非单射映射复合不可消（`fg = fh` 但 `g ≠ h`）；矩阵环 MR 的奇异矩阵（H38 零因子的半群面）；
2. **β 对象族解禁——Burnside 世界（1902 百年工程）**：
   - **Burnside 问题**：有限生成 + 指数有界（xⁿ=e）⇒ 有限？——**三问三答跨越百年**：指数 2,3 为有限（Burnside 自己）；4 有限（Sanov 1940）；**奇数大指数无限**（Novikov–Adian 1968）——"消去缺席的世界能有多野"的完整测量；
   - 自由 Burnside 群 B(m,n)（无限怪兽对象族）；Golod–Shafarevich 无限性反例（1964，另一路）；
   - **幂等元爆炸**：非可消半群可含大量幂等元（矩形带/全变换半群的幂等格）——幂等结构学（连接 H39）；
3. **γ 因果型回收——逆半群理论（为修复而发明）**：
   - **问题**：部分可逆变换（非双射映射）如何"尽量像群"？
   - **解**：**逆半群（inverse semigroup，Wagner 1952/Preston 1954）**——每个元素有唯一"逆"（弱化意义：`axa=a, xax=x`），偏序 + 部分恒等（idempotent 交换律为定义成分）——**"群论的忠实影子"**：群刻画整体对称，逆半群刻画**部分对称**；
   - **Wagner–Preston 表示定理**：逆半群 ⇔ 部分双射半群——对应 Cayley 定理的逆半群版（表征定理 γ）；
   - **发明动机有记录**：Victor Wagner 明确为推广群对称概念而建——γ 因果型（主动回收）第二例（第一例 H38 理想论）；
4. **结构分层谱系**：群 ⊂ 逆半群 ⊂ 正则半群 ⊂ 半群——**"可逆性"的连续降档阶梯**（与 H37 坐标降档阶梯同构的又一例）。

**结构性后果**：
- 方程论降级：`ax=b` 从唯一解变为"解集分析"；
- 计数与唯一性分离：消去不在场时"数元素"与"解方程"变成不同问题（Burnside 问题的本质）。

**版本信息**：
- **形式化基础**：Burnside 1902（问题）；Wagner/Preston 1952-54（逆半群）；Novikov–Adian 1968（无限性）；Howie 教材体系化
- **依赖前提**：半群公理
- **AxiomaticBase**：`Semigroup` + `NOT_Cancellation`（+ `InverseSemigroup`）
- **历史定位**：β（Burnside 百年工程）与 γ（逆半群因果回收）**双段齐备**的教科书样本。

---

## 2. S/M/P × D/L 六格审计

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| T₂ 非可消 | 变换复合 | ✅ |
| Burnside 三问答 | 1902–1968 | ✅ |
| 自由 Burnside 群 | 怪兽对象 | ✅ |
| 逆半群定义 | 弱逆 + 幂等交换 | ✅ |
| Wagner–Preston | 部分双射表征 | ✅ |
| 可逆性阶梯 | 群⊂逆⊂正则⊂半群 | ✅ |

### 2.2 S*L — 语义逻辑结构

- 非可消语义核心：**"等式两边不能随便做动作"**——移项/约分死亡，方程论降级为解集分析；
- "部分对称"的合法化：逆半群教我们**对称性本身可分档**（整体可逆 vs 局部可逆）——物理中的部分粒子置换/晶格部分对称有精确代数家；
- ⚠️ 风险：非可消语境做约分；把逆半群的"逆"当群逆用（xax=x 是弱化条件）。

### 2.3 M*D — 数学依存

```text
NonCancellableWorld
    │
    ├── T₂: smallest witness; singular matrices (H38 link)
    │
    ├── Burnside program (β): bounded exponent ≠ finite
    │       └── free Burnside groups (monsters), Novikov–Adian
    │
    ├── idempotent explosion (H39 link)
    │
    └── inverse semigroups (γ, causal): Wagner–Preston representation
        = partial bijections = partial symmetry
    └── ladder: group ⊂ inverse ⊂ regular ⊂ semigroup (invertibility dial)
```

### 2.4 M*L — 数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| Burnside 无限性 | ✅ | Novikov–Adian。 |
| 逆半群表征 | ✅ | Wagner–Preston。 |
| 阶梯包含链 | ✅ | 各级真包含。 |

### 2.5 P*D / P*L — 编程层

- 半群计算软件（GAP 半群包）成熟；自由 Burnside 群有限商可计算——P 层 🟡。

---

## 3. 判定

| 维度 | 状态 |
|---|---|
| 声明真实性 | ⚪ 真 |
| 证明正确性 | ⚪ 正确（Burnside/Wagner/Novikov–Adian 谱系） |
| 形式化验证 | 🟡 计算强/理论形式化中 |
| 兼容性 | ✅ 半群理论标准 |

**SMPDL 判定**：⚪ **低风险 / 已确认正确**。

---

## 4. 人类科学家可执行的验证动作

1. 在 T₂ 中找 `fg=fh, g≠h` 的显式反例。
2. 验证逆半群定义中幂等交换性的作用（为何群情形自动成立）。
3. 数矩形带（rectangular band）的幂等元，体会"幂等爆炸"。

---

## 5. 署名与许可

**Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0**
