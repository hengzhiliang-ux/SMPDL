# EC-1 候选 3 · DeepSeek（Zone-B 逐字归档）

> 归档：2026-10-27 06:42 咖啡回传 · 厂牌 DeepSeek · 会话：全新、免联网（首行声明在场 ✓）· 输入 = EC1 冻结件 C 段
> 地位：Zone-B 产物，C 区永不回改（G-L9）

---

本回答未联网检索；若运行环境有自动检索，我未调用且不依赖其输出。以下只用 1935 年前可用的证明论语言；自造术语"前提表""令牌""单用证明"等均为中性记号。

---

## 一、【清点】撤走 W/K 后的存活、失效与悬空

### 1. 系统记号与规则骨架

公式含原子、\(\land,\lor,\to,\forall,\exists\)（否定暂由 \(\to\bot\) 表示；\(\bot\) 规则另注）。前提记为有限"前提表" \(\Gamma\)，**有重数、模交换 C、不合并重复**。并置 \(\Gamma;\Delta\) 表示重数相加，不是集合合并。系统 \(\mathsf L_R\) 的规则如下；**规则表中没有 W、没有 K**：

- 初始：\[
A\vdash A
\]
- 切（暂作元规则，随后消去）：\[
\frac{\Gamma\vdash A\qquad \Delta,A\vdash B}{\Gamma;\Delta\vdash B}
\]
- \(\land\)：
\[
\frac{\Gamma\vdash A\quad \Delta\vdash B}{\Gamma;\Delta\vdash A\land B}\ (\land R)
\qquad
\frac{\Gamma,A,B\vdash C}{\Gamma,A\land B\vdash C}\ (\land L)
\]
- \(\lor\)：
\[
\frac{\Gamma\vdash A}{\Gamma\vdash A\lor B}\ (\lor R_1)
\qquad
\frac{\Gamma\vdash B}{\Gamma\vdash A\lor B}\ (\lor R_2)
\]
\[
\frac{\Gamma,A\vdash C\quad \Delta,B\vdash C}{\Gamma;\Delta,A\lor B\vdash C}\ (\lor L)
\]
- \(\to\)：
\[
\frac{\Gamma,A\vdash B}{\Gamma\vdash A\to B}\ (\to R)
\qquad
\frac{\Gamma\vdash A\quad \Delta,B\vdash C}{\Gamma;\Delta,A\to B\vdash C}\ (\to L)
\]
- 量词（标准特征变量条件）：
\[
\frac{\Gamma\vdash A[y]}{\Gamma\vdash\forall xA[x]}\ (\forall R)
\qquad
\frac{\Gamma,A[t]\vdash C}{\Gamma,\forall xA[x]\vdash C}\ (\forall L)
\]
\[
\frac{\Gamma\vdash A[t]}{\Gamma\vdash\exists xA[x]}\ (\exists R)
\qquad
\frac{\Gamma,A[y]\vdash C}{\Gamma,\exists xA[x]\vdash C}\ (\exists L)
\]
其中 \(y\) 不在 \(\Gamma\) 与主公式中自由。

### 2. 失效的推理模式

1. **收缩 W 失效**：一般地
   \[
   \Gamma,A,A\vdash B\ \not\Rightarrow\ \Gamma,A\vdash B.
   \]
   例：\(A,A\vdash A\) 在 \(\mathsf L_R\) 中不可证；而 \(A\vdash A\) 可证。无切消后最后规则分析可排除其他可能。故"重复前提可合并"失效。

2. **弱化 K 失效**：
   \[
   \Gamma\vdash B\ \not\Rightarrow\ \Gamma,A\vdash B.
   \]
   例：\(\vdash A\to A\) 可证，但 \(B\vdash A\to A\) 不可证；否则最后 \(\to R\) 会要求 \(B,A\vdash A\)，而 \(B\) 无法被消耗。

3. **同一前提在证明中两次使用而结论只保留一次**失效。典型：
   \[
   A\to(A\land A)
   \]
   不可证。若可证，最后 \(\to R\) 给 \(A\vdash A\land A\)，最后只能是 \(\land R\)，两子推导各需一个 \(A\)，结论前提会变成 \(A,A\)，不能收回为一个 \(A\)。

4. **丢弃型投影失效**：
   \[
   (A\land B)\to A,\qquad (A\lor B)\to A
   \]
   均不可证。前者若可证，\(\land L\) 后需 \(A,B\vdash A\)，须丢弃 \(B\)；后者 \(\lor L\) 后需 \(B\vdash A\)，不可得。

5. **传统弱化式 \(\land L\) 失效**：不能用
   \[
   \frac{\Gamma,A\vdash C}{\Gamma,A\land B\vdash C}
   \]
   因为这会丢弃 \(B\)。必须用完全式 \(\Gamma,A,B\vdash C\Rightarrow \Gamma,A\land B\vdash C\)。

6. **定理作假设失效**：空前提定理不能自由加入有前提推导。\(\vdash A\to A\) 是封闭定理，但
   \[
   B\vdash A\to A
   \]
   不可由 K 得到。

### 3. 悬空者

- 经典与直觉中依赖"复制"或"丢弃"的定理悬空：\(A\to(B\to A)\)、\(A\to(A\land A)\)、\((A\land B)\to A\)、\((A\lor B)\to A\)、\(A\to(A\to A)\) 等。
- 排中、双重否定、德摩根某些方向：在正片段中尚无统一判据；含否定与量词的完整判定，**以现有工具无法解决**，缺一套完整资源解释与变量条件的形式化归纳。下文只对正片段给可靠判据。
- 传统"把已证定理代入任意上下文"的元规则悬空；只能作显式替换，不能作弱化。

### 4. 意外存活者

- 身份 \(A\vdash A\)、交换 C。
- \(\lor\) 的资源幂等：
  \[
  A\to(A\lor A),\qquad (A\lor A)\to A
  \]
  均可证。后者由两次 \(A\vdash A\) 经 \(\lor L\) 得 \(A\lor A\vdash A\)。这里没有 W：\(A\lor A\) 公式内部提供两支资源。
- 资源配对：
  \[
  A\to(B\to(A\land B))
  \]
  可证：\(A\vdash A\)、\(B\vdash B\)，\(\land R\) 得 \(A,B\vdash A\land B\)，两次 \(\to R\)。
- 资源传递：
  \[
  ((A\to B)\land(B\to C))\to(A\to C)
  \]
  可证；证明见第三节定理二。
- \(\land\) 交换：\(A\land B\to B\land A\) 可证。
- \(\lor R\)、\(\to R\)、\(\forall R\)、\(\exists R\) 等"选择/封闭"规则存活；它们不要求丢弃前提。

### 5. 逻辑规则配对调整的结论

- \(\land L\) 必须取"完全消耗"形式；弱化式不可用。
- \(\lor L\) 两支的上下文必须并置，不能共享同一令牌；若两支都要同一前提，则结论须保留两份该前提，否则非法。
- \(\lor R\) 不需要弱化，故传统形式可留。
- \(\to L\) 合并左右上下文；\(\to R\) 把前件吸收进结论公式，是合法"消耗"而非结构丢弃。
- 量词规则只需标准特征变量条件；无 W/K 不改变变量条件，但禁止把特征变量条件借弱化绕过。

---

## 二、【判据审判】受限资源下推理合法性的判据

### 1. 令牌与账本

把前提表中每个公式出现看成一个**令牌**。相同公式的不同出现是不同令牌。证明树从叶初始 \(A\vdash A\) 产生一个令牌；逻辑规则只允许令牌发生以下三种命运：

1. **传递**：进入结论前提；
2. **变形**：被主公式规则吸收为结论公式的子公式，例如 \(\to R\) 把前提 \(A\) 吸收为结论 \(A\to B\) 的前件；\(\land L\) 把 \(A\land B\) 分解为 \(A,B\)；
3. **分支**：仅当结论前提中相应公式重数增加时，才允许同一令牌型在两条子路径出现；这体现为结论中显式多出一个令牌，而不是把两份合成一份。

于是给判据：

> **资源双射判据**：一个候选推导 \(\Pi:\Gamma\vdash A\) 合法，当且仅当存在从"结论前提 \(\Gamma\) 的令牌"到"叶初始左端令牌及被逻辑主规则吸收的令牌"的保形双射；每个令牌在树中恰出现一次，分支处若出现两次，则结论前提中该型令牌重数也相应为二。

等价地写成账本等式：对每个公式型 \(D\)，
\[
\text{叶使用数}_\Pi(D)
=
\text{结论前提重数}_\Gamma(D)
+
\text{被逻辑规则吸收数}_\Pi(D).
\]
若左边大于右边，则需要收缩 W，非法；若左边小于右边，则需要弱化 K，非法。

### 2. 复制/丢弃被允许的显式条件

- **复制允许条件**：只有当结论前提中相应公式重数已经增加时，才允许同一型令牌在两条子路径出现。例：由 \(A\vdash A\) 与 \(A\vdash A\) 经 \(\land R\) 得
  \[
  A,A\vdash A\land A.
  \]
  这里"两个 \(A\)"在结论前提中显式保留为两份。绝不能由此得 \(A\vdash A\land A\)。
- **丢弃允许条件**：只有当该令牌作为某个逻辑主公式被规则吸收时，才允许它从前提表消失。例：\(\to R\) 把 \(A\) 吸收为 \(A\to B\) 的前件；\(\land L\) 把 \(A\land B\) 分解为 \(A,B\)；\(\lor L\) 把 \(A\lor B\) 分成两支。不得仅因"结论不需要"而删除令牌。

这不是把 W/K 换名：系统规则表未增加任何结构规则；判据只是检验一个推导是否已经满足资源账本。

### 3. 正片段中仍立与不立的经典定理

**仍立（可证）**：
\[
A\to A,\quad
A\to(A\lor A),\quad
(A\lor A)\to A,
\]
\[
A\to(B\to(A\land B)),
\]
\[
((A\to B)\land(B\to C))\to(A\to C),
\]
\[
(A\land B)\to(B\land A).
\]

**不立（在正片段中由切消与最后规则分析判定）**：
\[
A\to(B\to A),\quad
(A\land B)\to A,\quad
A\to(A\land A),\quad
(A\lor B)\to A,\quad
A\to(A\to A).
\]
理由分别是：需丢弃一个前提、需复制一个前提而结论不保留第二份、或需把空前提定理弱化进有前提上下文。

含否定、排中、量词的完整经典定理表：**以现有工具无法解决**；缺一套覆盖否定与量词资源账本的完整解释，以及相应的切消归纳细节。

---

## 三、【受限收编】"每个前提恰用一次"的证明对象

### 1. 定义性框架

**定义（单用证明）**：\(\mathsf L_R\) 中一个推导 \(\Pi:\Gamma\vdash A\) 称为**单用的**，若其资源账本满足第二节双射判据，且结论前提中每个令牌在从结论回溯到叶的路径上恰好被主公式规则作用一次；分支只在结论显式保留相应重数时发生。

**定义（单用证明对象）**：一个单用证明对象是三元组
\[
(\Gamma,A,\Pi,\tau),
\]
其中 \(\Pi:\Gamma\vdash A\) 是单用推导，\(\tau\) 是结论前提令牌到叶令牌的保形双射。两个对象在交换前提次序下相同。

这不是把 W/K 重新引入：对象不允许在固定结论上合并重复或删除前提；它只是把"恰好用一次"的记账显式化。

### 2. 非平凡定理

**定理一（单用保持）**：若 \(\Pi_1:\Gamma\vdash A\) 与 \(\Pi_2:\Delta\vdash B\) 单用且其令牌集不交，则经 \(\land R\) 所得
\[
\Pi:\Gamma;\Delta\vdash A\land B
\]
单用；反之，若 \(\Pi:\Gamma,A,B\vdash C\) 单用，则经 \(\land L\) 所得 \(\Gamma,A\land B\vdash C\) 单用。

证明：\(\land R\) 只是把两个不交令牌集并置，结论前提重数为二者和；\(\land L\) 只是把 \(A\land B\) 一个令牌保形分解为 \(A,B\) 两个子令牌，账本等式两边同时替换，故保持。

**定理二（资源传递律）**：
\[
\vdash ((A\to B)\land(B\to C))\to(A\to C)
\]
在 \(\mathsf L_R\) 中可证，且其自然证明是单用的。

证明：
\[
A\vdash A\qquad B\vdash B
\]
经 \(\to L\)（主公式 \(A\to B\)）得
\[
A,A\to B\vdash B.
\]
又 \(C\vdash C\)，经 \(\to L\)（主公式 \(B\to C\)）得
\[
A,A\to B,B\to C\vdash C.
\]
经 \(\to R\) 得
\[
A\to B,B\to C\vdash A\to C.
\]
两次 \(\land L\) 合并前件，得
\[
(A\to B)\land(B\to C)\vdash A\to C.
\]
最后 \(\to R\) 得所要定理。令牌 \(A,B,C\) 各用一次，两个蕴含前提各用一次。

**定理三（受限替换/单用切）**：若 \(\Pi:\Gamma\vdash A\) 单用，\(\Sigma:\Delta,A\vdash B\) 单用且 \(\Sigma\) 中 \(A\) 令牌恰被使用一次，则代入得
\[
\Gamma;\Delta\vdash B
\]
单用。

证明：把 \(\Sigma\) 中 \(A\) 的叶令牌替换为 \(\Pi\) 的结论令牌；因 \(A\) 恰用一次，无双份替换，账本等式保持。这正是无 W/K 下切消的正面形式。

**定理四（切消保持单用性）**：\(\mathsf L_R\) 中切可局部消去；消去后不引入 W/K，且单用性保持。

证明略述：对切公式复杂度与切高度双归纳。关键在 \(\land R/\land L\)、\(\to R/\to L\) 交换时，上下文按重数并置；无 W/K 时不需收缩或弱化，故上下文直接合并。特征变量条件在切上移时用标准"变量不自由出现"检查。完整形式归纳较长，但局部各情形已可逐条验证。

**定理五（非复制/非丢弃的不可证性）**：
\[
A\vdash A\land A
\quad\text{与}\quad
A\land A\vdash A
\]
均无单用证明，因而 \(A\to(A\land A)\) 与 \((A\land A)\to A\) 均不可证。

证明：前者最后只能是 \(\land R\)，会要求结论前提为 \(A,A\)，与一个 \(A\) 矛盾；后者最后只能是 \(\land L\)，会要求子前提 \(A,A\vdash A\)，其中一支 \(A\) 必被丢弃，违反账本等式。由切消可排除绕道切。

---

## 四、【镜像】证明与构造性对象的局部对应

在正片段中定义"单用构造项"：

- 恒等：\(A\vdash A\) 对应 \(x^A\)，自由变量 \(x\) 恰一次。
- \(\land R\)：若 \(t:\Gamma\vdash A\)，\(u:\Delta\vdash B\)，对应配对 \(\langle t,u\rangle:\Gamma;\Delta\vdash A\land B\)。
- \(\land L\)：若 \(t:\Gamma,A,B\vdash C\)，对应解包项
  \[
  \mathsf{let}\ (x^A,y^B)=p^{A\land B}\ \mathsf{in}\ t,
  \]
  其中 \(p\) 恰一次，\(x,y\) 各一次。
- \(\to R\)：若 \(t:\Gamma,A\vdash B\)，对应抽象 \(\lambda x^A.t:\Gamma\vdash A\to B\)，约束变量 \(x\) 在 \(t\) 中恰一次。
- \(\to L\)：若 \(t:\Gamma\vdash A\)，\(u:\Delta,B\vdash C\)，主公式 \(A\to B\)，对应把函数 \(f^{A\to B}\) 作用于 \(t\) 得 \(B\)，再交给 \(u\)：
  \[
  u[f\,t],
  \]
  其中 \(f,t\) 各一次。
- \(\lor R\)：对应左注入 \(\mathsf{inl}(t)\) 或右注入 \(\mathsf{inr}(t)\)。
- \(\lor L\)：对应分情况消去
  \[
  \mathsf{case}\ s^{A\lor B}\ \mathsf{of}\ \mathsf{inl}(x^A)\mapsto t;\ \mathsf{inr}(y^B)\mapsto u,
  \]
  两支资源并置，不共享令牌。

局部对应定理：在上述正片段中，单用证明 \(\Pi:\Gamma\vdash A\) 与"自由变量类型表为 \(\Gamma\)、每个自由变量恰出现一次、类型为 \(A\)"的单用构造项 \(t\) 一一对应；对应保持规则形状。此处不声称覆盖否定与量词的完整对应；那需要额外处理空前提与特征变量，**以现有工具无法完整解决**。

---

## 五、【总结】1935 年语言下的牺牲与生成

牺牲者：前提可任意复制与丢弃的自由；传统收缩与弱化；由之而来的投影、弱化型定理、定理作假设、\(A\to(B\to A)\)、\(A\to(A\land A)\) 等常见推理。空前提定理不能再自由嵌入任意上下文。传统弱化式 \(\land L\) 必须改为完全消耗式。切虽可消，但其上下文不能借结构规则合并。

生成者：一门以"令牌账本"为核心的自洽受限相继式理论。它保留了身份、交换、逻辑规则与切消，却把证明变成资源守恒的对象；产生资源配对律、资源传递律、\(\lor\) 的资源幂等、单用替换定理、单用范式与证明—构造的局部对应。复制只在结论显式保留重数时允许，丢弃只在逻辑主公式吸收时允许；二者都不是 W/K 的复归。

未能解决者：含否定、排中、双重否定与全称存在交错时的完整判据；量词特征变量与资源账本的完整形式化；完整切消归纳的逐情形长证明。此处缺的不是新结构规则，而是一套覆盖全部公式的资源解释与更长的归纳工具。
