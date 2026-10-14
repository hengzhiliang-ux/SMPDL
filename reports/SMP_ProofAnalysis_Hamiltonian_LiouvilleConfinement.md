# SMPDL 单体审计：Hamiltonian 保守流视角下的 Liouville 定理

> **审计对象**：Hamilton 相空间中保体积流的 Liouville 定理与禁闭结构  
> **审计日期**：2026-10-14  
> **审计框架**：Göttingen S/M/P × D/L v1.5  
> **历史编号**：H35-PreFix  
> **总体评价**：⚪ 已确认正确（在哈密顿语义内）。

---

## 1. 声明与版本

**主声明**（Liouville 定理，1838）：设 `(M, ω)` 为辛流形（2n 维），`H` 为哈密顿量，`X_H` 其哈密顿向量场，`φ_t` 为流。则：

1. **保体积**：`φ_t` 保持相体积（Liouville 测度 `ωⁿ/n!`）：`φ_t* (ωⁿ) = ωⁿ`——**相空间不可压缩流体**；
2. **辛结构更强**：`φ_t* ω = ω`（保辛形式）——保体积只是保辛的拓扑维影子（n=1 时相等，n≥2 辛更强）；
3. **Noether 联锁**（H33 桥）：哈密顿守恒量 ⇔ 正则变换对称——Liouville 定理是 Noether 对偶在**相空间几何层**的投影（时间平移保 H ⇒ 流保 ω ⇒ 保体积）；
4. **禁闭后果**：**没有吸引子**——保守流不能有渐近稳定集（体积收缩才能聚焦轨道）；统计力学的遍历理论（ergodic hypothesis，Boltzmann）建立在 Liouville 禁闭之上；
5. **Poincaré 回归**：有限测度相空间中几乎处处轨道回归——保守世界的"永恒轮回"定理。

**版本信息**：
- **形式化基础**：Liouville 1838（J. Liouville，"Sur la théorie de la perturbation des planètes"）；现代几何化（辛几何，1960s–70s Arnold/Weinstein）
- **依赖前提**：辛结构、哈密顿向量场、流
- **AxiomaticBase**：`SymplecticManifold` + `HamiltonianFlow`
- **历史定位**：T3 不变禁闭律的**教科书样本**——守恒（H33）禁闭动力学，Liouville 把禁闭精确到测度层。

---

## 2. S/M/P × D/L 六格审计

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| 辛形式 ω | 闭非退化 2-形式 | ✅ |
| 哈密顿向量场 | ι_{X_H}ω = dH | ✅ |
| 流的辛保持 | φ_t*ω = ω | ✅ |
| 体积保持（影子） | ωⁿ 不变 | ✅ |
| 无吸引子/回归 | 禁闭后果 | ✅ |

### 2.2 S*L — 语义逻辑结构

- 哈密顿语义核心：**"相空间是不可压缩的"**——流如理想流体，轨道体积永不收缩；
- 禁闭层级：保辛 ⇒ 保体积 ⇒ 无吸引子 ⇒ 回归——**一条律的四层禁闭瀑布**；
- ⚠️ 风险：把耗散系统的吸引子直觉（H25/H33-PreFix）带入保守语境；把保体积当保辛的等价物（n≥2 时不等）。

### 2.3 M*D — 数学依存

```text
HamiltonianConfinement
    │
    ├── (M, ω) symplectic; X_H via ι_Xω = dH
    │
    ├── L_Xω = 0 (Cartan: dι_Xω + ι_Xdω = d²H + 0 = 0)
    │
    ├── φ_t*ω = ω ⇒ φ_t*(ωⁿ) = ωⁿ (Liouville measure invariant)
    │
    ├── no attractors (volume can't shrink)
    │
    └── Poincaré recurrence (finite measure)
```

### 2.4 M*L — 数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| L_Xω = 0 计算 | ✅ | Cartan 公式两行。 |
| 辛 ⇒ 体积 | ✅ | 幂次保持。 |
| 无吸引子论证 | ✅ | 测度矛盾。 |
| 回归定理 | ✅ | 测度论论证。 |

### 2.5 P*D / P*L — 编程层

- Mathlib：辛几何形式化发展中（`Symplectic` 方向）；统计力学仿真（HMC 采样器 = Hamiltonian Monte Carlo）以 Liouville 为正确性根基——**MCMC 产业隐形押注本律**。

---

## 3. 判定

| 维度 | 状态 |
|---|---|
| 声明真实性 | ⚪ 真 |
| 证明正确性 | ⚪ 正确（Liouville 1838） |
| 形式化验证 | 🟡 发展中（工程强） |
| 兼容性 | ✅ 几何力学标准 |

**SMPDL 判定**：⚪ **低风险 / 已确认正确**。

---

## 4. 人类科学家可执行的验证动作

1. 用 Cartan 公式验证 `L_{X_H}ω = 0`。
2. 解释为什么保守流不能有渐近稳定不动点（体积矛盾）。
3. 数值对照：谐振子（保守，轨道环面）vs 阻尼振子（耗散，吸引到不动点）。

---

## 5. 署名与许可

**Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0**
