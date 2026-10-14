# SMPDL 单体审计：λ 演算视角下的 Church–Rosser 定理

> **审计对象**：λ 演算的 Church–Rosser 定理（汇合律成立侧）与 Nichols/Hindley–Rosen 证明结构  
> **审计日期**：2026-10-14  
> **审计框架**：Göttingen S/M/P × D/L v1.5  
> **历史编号**：H31-PostFix  
> **总体评价**：⚪ 已确认正确——汇合律在 λβ 归约中成立，范式唯一性恢复。

---

## 1. 声明与版本

**主声明**（Church–Rosser 定理，1936）：在无类型 λ 演算的 β 归约中，若 `t →*_β u₁` 且 `t →*_β u₂`，则存在 `v` 使 `u₁ →*_β v` 且 `u₂ →*_β v`——**归约路径终将汇合**。

**三大结构性后果**：

1. **范式唯一性**：若 `t` 有范式，则范式**唯一**——`t` 的"计算答案"良定义，与求值策略无关；
2. **一致性（consistency）**：λ 演算的等式理论 β-convertibility 与"公共可归约"一致——**`true = false` 不可证**（Curry 组合子下 `K ≠ K*` 由 CR 分离）——证明论一致性的重写路线；
3. **策略自由**：惰性/急切/最左/完全归约在"有范式则同答案"意义下等价——**函数式语言语义的合法性基石**。

**证明骨架（并行归约 + Tait/Martin-Löf 斜条带法）**：
- 定义**并行归约 ⇒**（一步同时归约全部可归约红移）；
- 证明**斜条带引理（strip lemma）**：单步与多步的菱形性质；
- 归纳得并行归约的菱形性 ⇒ 汇合（Hindley–Rosen 引理的实例）。

**残存结构：汇合性判定技术群**：
- **Knuth–Bendix 完备化（1970）**：关键对逐一检查 + 自动补充规则——非汇合系统的"修复流水线"；
- **Newman 引理（1942）**：终止 + 局部汇合 ⇒ 汇合——弱化条件换取可判定性；
- **正交系统（orthogonal TRS）**：无重叠 + 左线性 ⇒ 自动汇合——**结构条件换汇合律免费**。

**版本信息**：
- **形式化基础**：Church–Rosser 1936；Tait/Martin-Löf 并行归约（1960s–70s 定型）；Knuth–Bendix 1970
- **依赖前提**：λ 项、β 归约、并行归约
- **AxiomaticBase**：`LambdaCalculus` + `BetaReduction` + `ChurchRosser`
- **历史定位**：与 H22 切消去（Gentzen 1935）**同期同工具**（1935/1936 双响）——C3 元数学集群的重写分支；函数式编程产业的逻辑地基。

---

## 2. S/M/P × D/L 六格审计

### 2.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| β 归约与替换 | λ 语义核心 | ✅ |
| 并行归约 ⇒ | 同步归约 | ✅ |
| 斜条带引理 | 单步-多步菱形 | ✅ |
| CR 定理 | 汇合律 | ✅ |
| 范式唯一/一致性/策略自由 | 三大后果 | ✅ |

### 2.2 S*L — 语义逻辑结构

- PostFix 语义反转：**"答案唯一"从假设恢复为定理**——但仅限 β（加入 η、δ 或带副作用扩展需逐一重证）；
- 汇合成为**可判定工程对象**：关键对/正交性/终止性三工具群把"律的检查"变成算法；
- ⚠️ 风险：把 λβ 的 CR 推广到任意扩展演算（如带 control/choice 的系统 CR 可破）。

### 2.3 M*D — 数学依存

```text
ChurchRosser
    │
    ├── parallel reduction (⇒)
    │
    ├── strip lemma (diamond for single/multi-step)
    │
    ├── diamond property of ⇒ ⇒ confluence (Hindley–Rosen)
    │
    ├── consequences: unique NF; consistency (true ≠ false);
    │   strategy-independence (lazy = eager on normalizing terms)
    │
    └── toolchain: Knuth–Bendix completion; Newman (terminating+locally
        confluent ⇒ confluent); orthogonality ⇒ free confluence
```

### 2.4 M*L — 数学逻辑结构

| 检查项 | 状态 | 说明 |
|---|---|---|
| 斜条带引理 | ✅ | 归纳于归约步。 |
| CR ⇒ 范式唯一 | ✅ | 汇合的直接推论。 |
| 一致性推论 | ✅ | true/false 分离。 |
| Newman/正交 | ✅ | 弱化条件路径。 |

### 2.5 P*D / P*L — 编程层

- Mathlib/Coq 社区：CR 定理有多个形式化（含 parellel-reduction 版本）；Knuth–Bendix 完备化有可执行实现（Spike/ CiME 等工具）。

---

## 3. 判定

| 维度 | 状态 |
|---|---|
| 声明真实性 | ⚪ 真 |
| 证明正确性 | ⚪ 正确（Church–Rosser/Tait） |
| 形式化验证 | 🟢 多实现 |
| 兼容性 | ✅ 重写理论/λ 演算标准 |

**SMPDL 判定**：⚪ **低风险 / 已确认正确**。

---

## 4. 人类科学家可执行的验证动作

1. 手推斜条带引理一步实例（`(λx.x x)(λx.x x)` 类小项）。
2. 验证范式唯一：同一项用最左/完全归约得到同一范式。
3. 用正交性判据说明组合逻辑 SKI 的汇合性免费成立。

---

## 5. 署名与许可

**Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0**
