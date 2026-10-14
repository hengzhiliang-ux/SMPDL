# SMPDL 单体审计：连续流视角下的 Poincaré–Bendixson 与不变量

> **审计对象**：平面连续流的 Poincaré–Bendixson 定理与流量守恒律  
> **审计日期**：2026-10-14  
> **审计框架**：Göttingen S/M/P × D/L v1.5  
> **历史编号**：H25-PreFix  
> **总体评价**：⚪ 已确认正确（在连续流语义内）。

---

## 1. 声明与版本

**主声明**（Poincaré–Bendixson + 散度判据）：设平面 `ℝ²` 上 `C¹` 向量场生成流 `φ_t`：

1. **Poincaré–Bendixson 定理**：有界轨道的 ω-极限集若是有限个奇点之并则为奇点轨道；否则必含**闭轨（周期轨道）**——平面连续流的极限集只有"静止或环绕"两种归宿；
2. **Bendixson–Dulac 判据**：若单连通域上 `div(f) ≠ 0`（或存在 Dulac 函数使 `div(Bf) ≠ 0`），则**无闭轨**；
3. **不变量结构**：流的守恒量 `H`（Hamiltonian `H(q,p)` 沿流常数）是**连续时间**不变量；`d/dt H(φ_t x) = ∇H · f = 0`。

**版本信息**：
- **形式化基础**：定性动力系统理论（Poincaré 1880s；Bendixson 1901）
- **依赖前提**：向量场唯一性（Lipschitz）、平面 Jordan 曲线拓扑
- **AxiomaticBase**：`ContinuousFlow` + `PlaneTopology`
- **历史定位**：P–B 定理是平面特有（依赖 Jordan 曲线分离性），**三维即失效**（Lorenz 混沌）。

---

## 2. S/M/P × D/L 六格审计

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| 向量场 f(x) | 导数场 | ✅ |
| 流 φ_t | ODE 解 | ✅ |
| ω-极限集 | 渐近行为 | ✅ |
| Jordan 曲线分离 | 平面拓扑 | ✅ |
| 闭轨/奇点二分 | P–B 核心 | ✅ |

### 2.2 S*L — 语义逻辑结构

- 连续语义：时间是 `ℝ`，解曲线光滑；"极限集"概念依赖连续统结构。
- P–B 二分是**平面维度 + Jordan 分离**的联合产物。
- ⚠️ 风险：把 P–B 推广到 `ℝ³`——Lorenz 吸引子立即反例（ Strange attractor，非奇点非闭轨）。

### 2.3 M*D — 数学依存

```text
ContinuousFlow
    │
    ├── x' = f(x), f ∈ C¹ (Lipschitz → uniqueness)
    │
    ├── Flow φ_t, ω-limit set
    │
    ├── Jordan curve topology (plane-only)
    │
    ├── Poincaré–Bendixson dichotomy
    │
    └── Bendixson–Dulac div test (no closed orbit)
```

### 2.4 M*L — 数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| P–B 二分 | ✅ | 平面专属。 |
| Dulac 判据 | ✅ | div ≠ 0 排除闭轨。 |
| Hamiltonian 守恒 | ✅ | 连续不变量。 |
| 维度依赖 | ✅ | Jordan 分离是平面拓扑。 |

### 2.5 P*D / P*L — 编程层

- 数值 ODE（RK45）仿真顺畅；P–B 本身难形式化（拓扑内容重）。

---

## 3. 判定

| 维度 | 状态 |
|---|---|
| 声明真实性 | ⚪ 真 |
| 证明正确性 | ⚪ 正确 |
| 形式化验证 | 🟡（数值强/形式弱） |
| 兼容性 | ✅ 动力系统标准 |

**SMPDL 判定**：⚪ **低风险 / 已确认正确**。

---

## 4. 人类科学家可执行的验证动作

1. 证明 `div f ≠ 0`（单连通域）⇒ 无闭轨（Green 公式矛盾）。
2. 验证 Lorenz 系统的吸引子违反 P–B 二分（数值演示）。
3. 验证 Hamiltonian `H` 沿流守恒的链式法则推导。

---

## 5. 署名与许可

**Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0**
