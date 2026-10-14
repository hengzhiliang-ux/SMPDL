# SMPDL 基础对比审计：经典半环 ↔ tropical 半环的幂等律（含 T1 第五验）

> **对比对象**
> - "PreFix" 版本：经典半环（累积加法 + 消去）（`SMP_ProofAnalysis_ClassicalSemiring_AccumulatingAddition.md`）
> - "PostFix" 版本：tropical 半环（幂等 ⊕ + 代数-优化对偶）（`SMP_ProofAnalysis_TropicalSemiring_IdempotentDuality.md`）
> 
> **审计日期**：2026-10-14  
> **审计框架**：Göttingen S/M/P × D/L v1.5  
> **历史编号**：H39  
> **律登记**：甲级律（公理级）——幂等律 `a ⊕ a = a`（加法幂等） | **T1 对象构成律**（定义幂等半环类） | E 档（幂等半环定理群完整）| 模式一+二（L1 千年 → 1960s 调度论 → Maslov/Viro 渐近回收）| E′ = dequantization/幂等分析  
> **T1 第五验预测**（登记于入库前）：**β 主（tropical 对象族解禁）+ γ 进行中（dequantization 渐近回收）+ H2 离散化联动**——见 §7 回验  
> **总体评价**：⚪ ↔ ⚪ 两侧各自正确；**T1 五验命中 + γ 第三形态发现（渐近型）**——γ 分类学完成三形态：表征型/因果型/渐近型。

---

## 1. 版本声明对比

| 维度 | 经典半环（PreFix） | tropical 半环（PostFix） |
|---|---|---|
| **律** | ❌ a+a=a 仅 0 | ✅ 幂等（⊕=max） |
| **加法语义** | 累积（都要） | 取优（选最好） |
| **加法逆/消去** | ✅ | ❌（无减法） |
| **多项式** | 解析函数 | 分段线性凸函数 |
| **根** | 代数根 | 折点（FTA tropical 版成立） |
| **行列式** | 交错和 | 指派问题（max over perms） |
| **特征值** | 谱 | 最小圈均值（Karp） |
| **优化地位** | 外部操作 | **内嵌于算术** |
| **与经典的关系** | —— | **渐近影子**（ε→0 dequantization） |
| **历史定位** | 古典默认 | Cuninghame-Green 1960s / Maslov 1980s / Viro 2000 |
| **形式化** | 🟢 默认 | 🟡 算法强/理论少 |

---

## 2. PreFix 版本 SMPDL 速览（经典半环）

- **S*D**：累积加法 + 消去 + max 独立存在。
- **S*L**：⚠️ "加法=累积"是数系默认；优化与代数的分离是习惯不是必然。
- **判定**：⚪ 框架内正确。

---

## 3. PostFix 版本 SMPDL 六格审计（tropical）

### 3.1 S*D — 语义依存

| 节点 | 前驱 | 状态 |
|---|---|---|
| ⊕=max 公理 | 幂等半环 | ✅ |
| tropical 线代 | 最短路字典 | ✅ |
| tropical FTA | 折点=根 | ✅ |
| Karp 谱 | 圈均值 | ✅ |
| dequantization | 渐近极限 | ✅ |

### 3.2 S*L — 语义逻辑结构

- 语义反转核心：**"加法从累积变为择优"**——优化问题的求解变成"做算术"；调度/最短路/指派问题全体获得统一的代数语言；
- 同名异义密度全库最高：加/乘/多项式/根/行列式/特征值**六项全部换义**——组内语义反转数量的极端样本；
- dequantization 视角：tropical 是经典的**极限影子**——不是平行世界而是渐近端点（γ 独特形态）；
- ⚠️ 风险：tropical 语境用减法/负元；把 tropical det 的组合性质当交错性质。

### 3.3 M*D — 数学依存

```text
accumulating addition (classical)
    ↕ idempotent switch (⊕ = max)
optimization embedded in arithmetic
    ↕ new objects (β)
tropical matrices/poly/roots/det/eigenvalues (full dictionary)
    ↕ asymptotic recovery (γ in progress, Viro/Maslov)
tropical = ε→0 shadow: log-sum-exp → max; GW invariants → tropical counts
```

### 3.4 M*L — 数学逻辑结构

| 检查项 | 经典 | tropical | 差异 |
|---|---|---|---|
| 加法 | 累积 | 择优 | 反转 |
| FTA | 代数闭域 | 折点计数 | 平行成立 |
| det | 交错 | 指派 | 换义 |
| 谱 | 线性 | 图论（圈） | 换义 |
| 关系 | 自身 | 渐近影子 | γ 新形态 |

### 3.5 P*D / P*L — 编程层

- Floyd-Warshall/Hungarian 算法 = tropical 线代的工程化身（算法先于理论命名数十年）——**"工程先到、理论后至"的独特时序**（对照 Rust-bang 的平行发明）。

---

## 4. 跨层映射检查

| 映射 | 经典（PreFix） | tropical（PostFix） |
|---|---|---|
| S → M | "累积" → 消去定理 | "择优" → 幂等半环 |
| M → P | 数值计算默认 | 最短路/指派算法 |
| S ↔ S | "加法" = 累积 | "加法" = max（六项换义之首） |
| M ↔ M | 自洽体系 | 渐近影子（dequantization） |

**跨层结论**：本组与 H2（连续/离散）的联动确证：**dequantization 是 H2 离散化的算术面**（H2 管拓扑/几何的离散化，H39 管代数的"取整"——同为"极限过程改变结构"家族）；与 H5（特征律）构成**半环双律轴**：H5 拨特征（Freshman's dream），H39 拨幂等（加法换义）——两条律正交且都产生"教科书定理换血"。

---

## 5. 判定

| 维度 | 经典 | tropical |
|---|---|---|
| 声明真实性 | ⚪ | ⚪ |
| 证明正确性 | ⚪ | ⚪ |
| 形式化验证 | 🟢 | 🟡 |
| 兼容性 | ✅ | ✅ |

**SMPDL 判定（PostFix）**：⚪ **低风险 / 已确认正确**。

---

## 6. 变化类型归类

- **变化方式**：**公理切换（甲级律：幂等律加入加法位）引发六项同名异义 + 优化代数化 + 渐近影子关系**。
- **SMPDL 同构标签建议**：`S-BISIM / M-BISIM / P-BISIM`。
- **关键 lesson**：AI 在 tropical 语境生成证明时，减法/加法逆非法；"多项式根"须译为折点；det/特征值的组合语义（指派/圈均值）不可用线性代数直觉；调度/最短路问题的代数化表述是合法且推荐的统一语言。

---

## 6.5 概念奇点（Conceptual Singularity）

### 6.5.1 关键人工洞察

- **把优化焊进算术**：max 当加法不是记号游戏——它让**整类组合优化问题获得代数结构**（可交换/可分配/可"求导"），tropical 几何的爆发源于此；
- **dequantization 的世界观**：tropical 不是入侵者而是**经典的量子退火极限**（ε→0）——"新世界是旧世界的影子"比"平行世界"更深刻，它给了两个世界之间的**翻译定理**而非仅有类比；
- **理论的迟到**：算法（最短路 1950s/指派 1950s）先于理论命名（tropical 1990s）数十年——工程实践的"无名 tropical 时代"证明数学结构可以先于概念化存在（L1 潜默的算法版）。

### 6.5.2 为什么机器难以自动迁移

机器求解最短路/指派毫秒级——但**意识到这些是 tropical 线代**是概念化跃迁；框架押注家族第七例（数值计算默认经典半环）。dequantization 极限的"影子关系"需要极限过程的双语能力（经典式↔tropical 式互译），非单一框架内可得。

## 6.6 断裂强度（Breakage Strength）

| 评估项 | 等级 | 说明 |
|---|---|---|
| **断裂强度** | 🟠 引理替换 | 六项同名异义 + 语义全面反转；但字典完整（det↔指派、谱↔圈均值）且有渐近桥（dequantization）。 |
| **S 层影响** | **极高** | 全库单组同名异义密度之最（六项）。 |
| **M 层影响** | 高 | 完整平行定理群（FTA/Karp/det）。 |
| **P 层影响** | 中高 | 算法产业隐身存在。 |

**判定**：语义全面反转 + 完整字典 + 渐近桥，评为 🟠。

---

## 7. T1 第五验回验（§7 专设）

| 预测（第四轮登记） | 实际 | 判定 |
|---|---|---|
| **β 主**（tropical 对象族解禁） | tropical 矩阵/多项式/根/det/谱全字典 + tropical 几何整门学科——对象族规模兑现 | ✅ **命中** |
| **γ 进行中**（幂等分析回收） | Maslov 幂等分析 + Viro dequantization + 枚举几何 GW 对应——**回收以"渐近极限"形态进行中** | ✅ **命中 + γ 第三形态发现**：**渐近型 γ**（新世界 = 旧世界的极限影子）——对照表征型（H37 即时）与因果型（H38 理想论） |
| **H2 联动** | dequantization = H2 离散化的算术面（"极限过程改变结构"家族确证） | ✅ **命中** |
| 预测缺口 | 未预测到：**算法先于理论数十年**（最短路 1950s vs tropical 命名 1990s）——"L1 潜默的算法版"，律史时间线的工程学入口 | 新观察登记 |

**回验结论**：T1 第五验**全中**；γ 分类学完成**三形态**：表征型（⇔ 即时）/ 因果型（为修复而发明）/ 渐近型（极限影子）——两阶段理论的阶段二全面结构化。回验累计：后验 4/5 + 前向 **6/6**。已回写 FunctionalType 与 RemovalEmergence。

---

## 8. 人类科学家可执行的验证动作

1. **B 岗位**：tropical 半环公理验证；计算具体 tropical 多项式折点。
2. **C 岗位**：Floyd-Warshall 写成 tropical 矩阵幂；log-sum-exp 极限验证。
3. **D 岗位**：检查 `AxiomaticBase` 分别为 `Semiring+NOT_IdempotentAdd` / `IdempotentSemiring(Tropical)`。
4. **E 岗位**：diff 确认六项同名异义清单与渐近桥（dequantization）已标注。

---

## 9. 文献引用纪律检查

| 引用对象 | 真实性 | 支持性 | 说明 |
|---|---|---|---|
| Cuninghame-Green (1960s–79) | ✅ | ✅ | 调度论 max-plus。 |
| Maslov 学派（1980s，幂等分析） | ✅ | ✅ | 渐近回收。 |
| Pin（1994 命名 joke） | ✅ | ✅ | tropical 得名。 |
| Viro (2000+, dequantization) | ✅ | ✅ | 影子关系。 |
| Karp (1978, 圈均值) | ✅ | ✅ | 谱字典。 |
| Maclagan–Sturmfels, *Tropical Geometry* (2015) | ✅ | ✅ | 教材。 |

**核查结论**：引用真实，支持一致。

---

## 10. 署名与许可

**Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0**

搬运、改写或教学引用请注明来源与本页面链接。
