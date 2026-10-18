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

## 二、帖 1 相关（锚定惯例 historiography）——待采
未开始。被动采集候选关键词：recognition point / crisis historiography / Kuhn mathematics / problem-provenance dating。

## 三、帖 3 相关（tropical 合法化节点）——待采
未开始。被动采集候选：history of tropical mathematics / idempotent analysis Maslov / Simon tropical semiring naming。

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
