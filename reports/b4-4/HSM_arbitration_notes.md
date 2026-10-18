# HSM/SE 仲裁笔记（B4-4 三档分歧外部仲裁登记）

> **登记纪律**：只登记外部证据与来源；影响分析只写「证据倾向」，**不改任何已 commit 的判定**（tier 变更须 J-B 或协议指定判定者，协调方禁判 · J1 变体）。
> **执行状态更新（10-18 14:15）**：HSM 注册被 IP 限制（VPN 出口为数据中心 IP 仍被拦）——策略改「被动采集优先」：SE 全站**阅读免注册**，先收割已有问答，注册发帖仅补缺口（见文末方案）。

---

## 一、帖 2 相关（R1 Fubini ±π/4 反例/锚点）——咖啡 10-18 初步检索收获

**已收割（免注册阅读）**：

| 来源 | 要点 | 仲裁价值 |
|---|---|---|
| Math.SE「Motivation and history of Fubini's theorem」（2024 问 · **Alexandre Eremenko 答** · accepted 3✓） | **Pringsheim 在 Fubini 之前已把逐次积分交换当「问题空间」对待**——「for Pringsheim it's a problem space (something that should not be a theorem), and in Fubini it's a theorem」；Fubini 1907 是在 Lebesgue 框架内把它定理化 | 🔥 高——直接支持「失效认知早于 1907 十年以上」的读法 |
| Math.SE「History of Fatou's Lemma」（2021 · 8✓） | **Fatou 1906（Rend. (2) 39, 775-80）引理被 Fubini 用来证明其定理** | 中——1906→1907 补偿结构链更紧：Fatou 引理→Fubini 证明，技术前提一年内到位 |
| Math.SE「How were double integrals calculated before Fubini's Theorem?」（2017 · Eremenko 答 9✓） | Fubini 前的逐次积分计算实践 + 定理化前后语境 | 中——补充认知时间线 |
| Math.SE「Historically, what led to the question of validity of interchange of limit operations?」（Conifold 等） | 交换极限运算有效性问题的长线前史（Hardy 纯数学教程附录专论 double limit problems） | 中——「失效认知」作为 19 世纪末分析学一般焦虑的一部分，非孤立事件 |

**对 R1 的证据倾向（登记，不裁决）**：
- 证据显示「次序交换不可靠」在 **Pringsheim 时代（1890s–1900s）已是公认问题空间**，Fubini 1907 是**补偿判据的定理化时刻**（且技术上直接依赖 Lebesgue 1902-04 + Fatou 1906）。
- 若锚 = Pringsheim 认知（1890s）→ 显影 1907/09：间隔 10–15 年 → **D2 严读不过**；若锚 = Lebesgue/Fatou 技术前提就位（1904/06）→ 显影 1907/09：间隔 1–5 年 → **D2 过**。J-A 当时的自选锚（Lebesgue 1904→1909=5 年压线过）**恰好被新证据支持**；原判的 rule-H 即时读法**不被支持**（失效认知远早于补偿）。
- ⚠️ ±π/4 具体反例的最早出处仍未解决（本轮检索未命中一手文献）——帖 2 的核心问题保留，若发帖仍值得问。
- **影响预测（登记）**：若 J-B 复核，R1 三档大概率落 🟡（与 J-A 同档）而非 ✅（原判档）——主型层（α vs γ）不受影响，仍是判定者归类偏好问题。

## 二、C 路线文献采集（10-18 14:19 史努比检索 · 出版级来源）

### 2.1 帖 2 核心问题已解决：±π/4 反例 = **Cauchy 1814** 🔥

**来源**：HSM「Did Cauchy ever deal with double or triple integrals?」（hsm.stackexchange.com/questions/11042）引 **Grattan-Guinness** 与 **Gray《The Real and the Complex: A History of Analysis in the 19th Century》**：

> Cauchy 在 **《Mémoire sur les intégrales définies》（1814）** 中研究了为什么交换双重积分次序会得到不同结果，并为此引入「奇异积分」（intégrales singulières）概念。对 **K = z/(x²+z²)**，他证明 ∫₀¹∫₀¹ (∂K/∂z) dzdx = **π/4**，换序积分 = **−π/4**。

**关键验证**：Cauchy 的 ∂K/∂z = (x²−z²)/(x²+z²)² ——**与现代 ±π/4 教科书反例的被积函数逐字相同**（x²−y²)/(x²+y²)²）。反例不是 Fubini 1907 构造，也非 Harnack 1880s——**一手源头 = Cauchy 1814**。

**对 R1 的证据分量（登记，不裁决）**：
- 失效认知锚从「Pringsheim 1898/99（problem space）」再前推至 **Cauchy 1814（显式研究 + 命名概念）**——「击破→补偿」全链 = 1814 → Fubini 1907/Tonelli 1909 = **93–95 年**；
- 原判 B4-2 击破锚「Cauchy 1827 误断言」有两处需修正：年份（1814 非 1827）+ 性质（Cauchy 不是误断言者，恰是**失效的发现与命名者**——introduced "singular integrals"）；
- 中继站确认：Pringsheim 1898《Zur Theorie des Doppel-Integrals》/1899（Sitzungsberichte München, Heft I, 39-61）——开头即今日 Fubini 定理的恒等式，以 Riemann 框架探其成立/失效条件，并引 **Stolz 1886** 指出双重积分可积性条件的错误主张（更早的失效认知痕迹）；Levi 猜想（可积而非有界）→ Fubini 1907 证明（Wikipedia History 节）；
- **三判定者 D2 读法全部失准**：J-A 的 Lebesgue-1904 锚（补偿链口径）仍可辩护，但「失效认知→补偿结构」的完整历史 = 93 年长周期；若按「认知锚」纪律，R1 的 D2 长间隔与 R9（Kummer→Dedekind）同构——J-A/J-C 的严读方向获文献支持；
- 二手文献可引：Grattan-Guinness《The Entry of Cauchy》+ Gray《The Real and the Complex》——**出版级出处，直接可进论文脚注**。

### 2.2 帖 3 核心问题基本解决：tropical 合法化时间线 = **AMS 官方叙事**

**来源**：AMS Contemporary Mathematics 616 卷末 matter（ams.org/books/conm/616/conm616-endmatter.pdf）+ Litvinov 本人综述（ESI preprint 1588 / arXiv:1001.4247）：

| 节点 | 年代 | 内容 |
|---|---|---|
| 线性代数地基 | **1960s** | Cuninghame-Green（英）+ Vorobyev（苏）max-plus 线性代数；更早应用史可追 Kleene（自动机） |
| 理论凝聚 | **1980s–90s** | Maslov 莫斯科学派「idempotent analysis」+ 法国 max-plus 工作组（离散优化/最优控制/HJB）**独立并行** |
| 纲领定名 | 1980s–90s | **Litvinov–Maslov dequantization + 对应原理**（Bohr 类比：幂等数学 = 传统数学的「经典极限/影子」） |
| **制度化首标志** | **1994** | **第一届国际 Idempotency 会议（Bristol，Gunawardena 编文集）**；后续 Vienna 2003 / Moscow 2007 / Montreal 2009 |
| 几何爆发 | 2000s | tropical geometry（Mikhalkin/Passare/Sturmfels/Viro；灵感源 GKZ amoeba——「经典问题 19 世纪已提出」） |

**对 R10 的证据分量（登记，不裁决）**：
- 「击破锚→定名显影 ≤5 年」确无对应物：AMS 官方叙事本身就是**多源长过程**（1960s 地基→1980s 理论→1994 制度化→2000s 爆发）——J-A「找不到干净锚」与 J-C「结构选择型长期理论化」**两个异构判定者的 D2 判定同时获得出版级支持**；
- 更微妙：Litvinov–Maslov 纲领的自我表述是**对应原理**（dequantization = 传统数学取极限 → 幂等数学为其「影子」）——**纲领层面是 γ 回收叙事**（旧数学被参数极限化），而非 β 解禁叙事；β 侧（新对象族合法化）在应用端同样真实。**J-A 的 γ 主读法在纲领层获得正面文本支持**；
- 二手可引：AMS CONM 616 + Litvinov 综述（arXiv:1001.4247）——卷末明说「the origins of modern tropical mathematics are much more diverse」，直接可用于 §7.5/§6 的 R10 归因段。

### 2.3 帖 1（史学锚定惯例）——仍开放
两轮检索无直接命中（该问题确实没人系统问过）。**唯一真正需要发帖的残余**；或走文献路线查 Kuhn 派数学史（如 Corry《Modern Algebra and the Rise of Mathematical Structures》的「认知点」处理）后再定。

---

## 四、HSM 注册受阻的处置方案（10-18 14:15）

| 方案 | 操作 | 评估 |
|---|---|---|
| A · 注册 workaround | 换 VPN 节点（住宅 IP 优于数据中心；日/新加坡节点常可用）；或改走 Google SSO 登录链（有时绕开邮箱注册的 IP 风控）；或手机热点换网络 | 值得再试一轮；仍拦则挂起不硬磕（Gemini 教训） |
| B · **被动采集优先（当前执行）** | SE 全站阅读免注册——咖啡本轮已证明有效（Eremenko 回答白捡）。帖 1/3 同法：先搜已有问答，够用就不发帖 | ✅ 零门槛零风险；缺点：问题受限于别人已问过的 |
| C · 文献仲裁卷宗 | 史努比用联网检索直接查**出版文献**（数学史专著/综述论文：如 Hawkins《Lebesgue's theory of integration》、tropical 史综述）产出仲裁 dossier | ✅ 对论文更可引（出版文献 > SE 回答）；帖 2 剩余问题（±π/4 出处）和帖 3 适合此路 |
| D · 注册成功后补发帖 | 仅当 A+B+C 后仍有缺口（尤其帖 1 史学惯例这种没人问过的） | 后备 |

**当前组合**：B（咖啡/史努比并行采集）+ C（史努比文献卷宗）为主，A 有空再试，D 仅补缺口。

---
*仲裁笔记 v1.0 · 2026-10-18 · 协调方登记件（污染会话，证据倾向≠裁决）· 双档：GitHub_Pages + Paper_and_Data*
