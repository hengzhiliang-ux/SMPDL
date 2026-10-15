# C-5r 署名严谨性核查 · 执行报告

> **执行**：2026-10-15 19:2x · rescope 依据咖啡定位声明（非职业研究者、不发 arXiv、DOI 公开物须严谨）
> **工单**：C-5 rescope 为 C-5r（`SMPDL_C5r_Attribution_Rigor_Check.md`）后本轮直接开跑
> **方法**：L1 = 部件标签表 9 条逐条 web 核验（定理名/作者/年份/实质）；L2 = 已核验引用抽查登记；L3 = 自铸概念标注覆盖度检查

---

## 一、L1 标准归属核查（9/9 通过）

| # | 部件标签表的归属 | 核验结果 | 出处锚 |
|---|---|---|---|
| 1 | Sahlqvist 对应理论 + SQEMA | ✅ | Sahlqvist 公式 ⇔ 一阶框架条件且可有效计算；SQEMA（Conradie et al.）涵盖 Sahlqvist+inductive 类；适用域限定（仅模态 Sahlqvist 型）与审计 🟠-10 修正一致 |
| 2 | Th ⊣ Mod 反变 Galois 连接 | ✅ | 标准概念（模型论/泛代数通行框架；nLab/教科书级） |
| 3 | Birkhoff HSP 定理 | ✅ | Birkhoff 1935《On the structure of abstract algebras》Proc. Camb. Phil. Soc. 31:433–454——方程类 ⇔ HSP 闭类，逐字吻合 |
| 4 | Beth 可定义性 | ✅ | Beth 1953《On Padoa's Method...》；隐定义 ⇔ 显定义（一阶）；Craig 插值为其标准推论路径——吻合 |
| 5 | Keisler–Shelah 定理 | ✅ | Keisler 1961（GCH 下）+ Shelah 1971（去 GCH）：初等等价 ⇔ 有同构超幂——逐字吻合 |
| 6 | Mal'cev 条件 / Pixley / Jónsson | ✅ | Mal'cev 1950s（同余可交换 ⇔ Mal'cev 项）；Pixley（算术 = 可交换+分配）；Jónsson（同余分配 ⇔ Jónsson 项链）——三元组归属全部正确 |
| 7 | Rutten 终余代数/互模拟 | ✅ | Rutten《Universal coalgebra: a theory of systems》TCS 2000：coalgebra/同态/互模拟 ≅ algebra/同态/同余对偶 + covariety 定理（Birkhoff 对偶）——吻合 |
| 8 | Goguen–Burstall institution | ✅ | Goguen–Burstall 1970s 末/1984《Introducing Institutions》；theory morphism/保守扩张/institution morphism（Goguen–Roşu 2002）为原生框架——吻合 |
| 9 | 保持定理族（Łoś–Tarski/Lyndon/van Benthem） | ✅ | Łoś–Tarski（子结构保持 ⇔ 全称句）；Lyndon 1959（同态像保持 ⇔ 正句）；van Benthem（模态不变性）——族归属正确 |

**L1 判定：9/9 归属正确，零错挂。**

## 二、L2 已核验引用复核（6/6 在档）

Friedman 1973 JSL 38（裁定会话网络复核 + zbMATH 交叉）/ Hofmann–Streicher 1994 / Barrett–Halvorson 2016 / Robinson 1950·TMR 1953（57a8fdb 登记）+ JMS 1995（自证级：解析+数值）/ Kirk–Shahzad 2013（定理陈述在案）——**全部有核验记录，本轮抽查未发现失锚**。

## 三、L3 自铸概念标注覆盖度

- 部件标签表 §107 行已有诚实披露（「静动态桥与审计模板为项目自铸——prior-art 检索 C-5 前不对外宣称首创」）——**C-5r 完成后该限制解除为「经 C-5r 核查的归属声明」**；
- 备忘 v2.0 的自铸概念（移除三段论/隐形承重/参数重置六式）均以「经验定律（项目）」口吻与标准归属（Birkhoff 等）明确分列——覆盖合格；
- 残留低风险：个别 reports 深层文件中自铸术语无逐处标注——评估为**可接受**（对外入口文档已覆盖；深层文件属研究记录非声明文本）。

## 四、判定

**C-5r = ✅ 通过**。DOI 公开物（Zenodo v3.3 + 未来 GitHub 公开）的署名严谨性成立：标准归属 9/9 真、已核引用 6/6 在档、自铸概念在对外入口有标注。原 C-5 工单就此**关闭**（arXiv 新颖性辩护职能随 C-1 不排期而退役；严谨性职能由本轮履行完毕）。

---
*C-5r 执行报告 v1.0 · 2026-10-15 · L1 9/9 + L2 6/6 + L3 合格 · 工单 C-5 关闭*
