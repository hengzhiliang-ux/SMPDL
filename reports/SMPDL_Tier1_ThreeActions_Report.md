# SMPDL 第一梯队三动作定案报告

**执行日期**：2026-10-14 · **框架**：S/M/P × D/L v1.5 · CAMPANASILVAE

---

## #1 · 族 352：运行 Calabi 流论文自带验证脚本（P 层捷径）

**动作**：拉取 verification/ 三脚本（certificate.py / arithmetic_allowances.py / tail-check.py），按官方 README 规程运行（断言开启、无优化）。

**结果**：✅ **三脚本全部通过**

| 脚本 | 输出 | 含义 |
|---|---|---|
| certificate.py | 静默（= 成功） | 核心射击法证书：59 项 Taylor 级数 + 46 阶区间递推 + matching 断言全过 |
| arithmetic_allowances.py | `all_exact_rational_checks_pass: true` | 16 项精确有理常数检查（含误差余量 JSON 报告） |
| tail-check.py | 「All root, projection, convolution, coefficient, derivative, residual, and contraction checks passed exactly」 | 尾部估计 + 卷积界 + Lipschitz 界精确通过 |

**脚本质量审计**（certificate.py 158 行逐行读）：
- 真区间算术：2²⁵⁶ 定标整数区间（mul/inv/divn 全部向下/向上取整方向正确）；
- 非平凡结构：1/W 级数递推（recip 函数）、块演化（evolve，每块 8 步 × 56 块）、Cauchy 余项 rat(48, 4^(degree-1))、变分矩阵传播（M 矩阵 + 范数累计 D≤570000, K≤246000 断言）；
- 断言密度：核心检查 14 处硬断言（norm(res)<1/(5×10¹⁰) 级精度）；
- **结论：这是动力学系统计算机辅助证明（computer-assisted proof）的标准形态，非空验证**。

**定案**：族 352 构造合法性 = 🟢（机器证书背书 + 独立复跑成功）。剩余开放点仅「脚本的解析学解释与定理陈述的对应」（README 自述限制：successful execution ≠ verify analytic interpretation——这一对应仍需人工审 §4–6 的连续论证）。

**SMPDL 意义**：全库首个「AI 证明自带可运行验证证书」案例——**第八种审计通道**（P 层 Lean 之外的第二条机器验证路径：浮点/有理证书脚本）。C-4 预测卡⑦候选：「带验证脚本的论文 vs Lean 形式化论文的错误率对照」。

---

## #2 · 族 178：Ramanujan 图构造外部谱验证可行性评估

**动作**：评估「小 n 实例 LAPACK 谱验证」的十分钟级可行性。

**结果**：⚠️ **成本修正（诚实降级）**

- 论文构造为四阶段管线（条件期望法确定性选取 + Ihara–Bass pencil 局部谱估计 + 配对收缩 + 修复），85 页正文、依赖铅笔多项式正性追踪、成对独立种子枚举等内部机制；
- **论文目录无验证脚本、无邻接表生成器代码**（与 352 不同）；
- LAPACK 验证前置条件 = 从论文规格**重新实现完整构造算法**（天级工程），非十分钟动作。

**定案**：178 外部复算红利降级为「可验证但成本 = 天级实现工程」；建议路径改为：①向作者/OpenAI 索取构造代码；②或等待社区复现。R4「构造显式性」结论不变（算法可显式描述 ✅），但「立即可验」修正为「待实现」。

---

## #3 · 族 335：Hanke ⟹ Gromov–Lawson 称号链条核验

**动作**：核对论文内部是否存在「证明 Hanke 版 ⟹ 解决 GL aspherical 猜想」的桥接论证。

**结果**：✅ **链条完整，称号红旗解除**

论文内部显式给出完整推导链：
1. **§1.2 Consequences**：「For a connected aspherical manifold, the classifying map is a homotopy equivalence. Thus every closed connected oriented aspherical manifold is rationally essential」——aspherical ⟹ rationally essential 桥接引理（一行标准论证）；
2. **Corollary 1.2** 正式命名「The Gromov–Lawson aspherical conjecture」并给出完整陈述（含非定向情形经定向二重复盖处理）；
3. **Theorem 1.3**（标量平坦刚性）：非负曲率 aspherical ⟹ flat，走 Cheeger–Gromoll 分裂定理 + 万有覆盖收缩性论证，全文给出；
4. **称号来源对照**：论文明确说明 Hanke [18, Def 2.8/Conj 2.9] 版本「is also the classifying-map form... of Gromov's conjecture [15, Section 1.5]」——两版等价性有出处支撑；
5. 外加 Corollary 1.4（目标映射障碍版，Chodosh 记录形式）与 Corollary 1.2 的关系也完整论证。

**定案**：335 称号偏移红旗**解除**——「Gromov–Lawson aspherical conjecture」是论文 Corollary 1.2 的正式名称，桥接论证完整在文内。**审前判定「称号传递链条未披露」为误报**（CONTENTS.md 族主页的简称包装造成，论文本体纪律良好）。

**SMPDL 意义**：本例与族 034/014 共同强化预测卡⑤：**「族主页（CONTENTS.md）包装层是失真源，论文本体纪律显著更好」**——三轮 PDF 级核验（12+3 动作）中零例论文本体失真、三例族页包装失真。

---

## 第一梯队执行汇总

| 动作 | 预期 | 定案 | 判定迁移 |
|---|---|---|---|
| 352 脚本运行 | 绿灯验证红利 | ✅ 三脚本全过 + 脚本质量真证书 | 352 = 🟢 定案 |
| 178 LAPACK 验证 | 十分钟外部复算 | ⚠️ 成本修正：需天级实现（无现成代码） | 178 维持 🟡（待代码） |
| 335 称号链条 | 十分钟文献对照 | ✅ 桥接引理文内完整，红旗解除 | 335：称号风险清零，核心风险回归「无假设新方法」本体（🔴 维持但风险位收敛） |

## 累计判定状态（三轮 PDF 核验后）

🟢 定案 5 族（225 / 270 / 349 / 300 / 352）· 🟡 待研究级审计 4 族（338 / 310 / 178 / 364-B）· 🔴 维持 3 族（304 / 069 / 335——均为「证明内部技术」型残余风险）· 014/034 族级包装失真待披露。

---

## 文献引用纪律检查

| 引用对象 | 真实性 | 支持性 |
|---|---|---|
| verification/ 三脚本源码 | ✅ 直拉逐行读 | ✅ |
| 178 论文正文四阶段描述 | ✅ 直读 | ✅ |
| 335b 论文 §1.2/Cor 1.2/Thm 1.3 | ✅ 直读 | ✅ |
| Gromov [15]/Hanke [18] 外部文献 | ⚠️ 编号由论文自引 | ⚠️ 未打开外部原文（留待后续） |

## 署名与许可

Göttingen S/M/P × D/L · v1.5 · CAMPANASILVAE · fecit · MMXXVI · CC BY-NC-SA 4.0
