# EC-1 候选 4 · Kimi（Zone-B 逐字归档）

> 归档：2026-10-27 06:42 咖啡回传 · 厂牌 Kimi · 会话：全新、免联网（首行声明在场 ✓）· 输入 = EC1 冻结件 C 段
> 地位：Zone-B 产物，C 区永不回改（G-L9）

---

本作答未联网检索，也未收到环境自动检索的材料。以下系统、记号与证明均为本作答内部构造。

# 一、清点：撤走 W、K 以后，演算还剩下什么

## 1.1 基本规定：把前提改为按出现次数计算的清单

称新系统为 **计量演算 \(\mathfrak M\)**。

公式仍由命题原子及 \(\land,\lor,\to,\forall,\exists\) 构成。相继式仍写作

\[
\Gamma\vdash A,
\]

但 \(\Gamma\) 不是集合，而是**有限无序清单**：同一公式的两次出现仍是两份前提。逗号表示清单合并；交换只改变次序，不改变出现次数。

唯一的初始相继式是

\[
\frac{}{A\vdash A}\qquad(\mathrm{Ax})
\]

不允许写成 \(\Gamma,A\vdash A\)，因为那会把无用的 \(\Gamma\) 凭空加入。

逻辑规则如下。

### 合取

\[
\frac{\Gamma,A,B\vdash C}
     {\Gamma,A\land B\vdash C}\;(\land L)
\]

\[
\frac{\Gamma\vdash A\qquad \Delta\vdash B}
     {\Gamma,\Delta\vdash A\land B}\;(\land R)
\]

第二规则必须把前提清单**分配**给左右两支，不能在两支中重复使用同一个 \(\Gamma\)。

### 析取

\[
\frac{\Gamma\vdash A}{\Gamma\vdash A\lor B}\;(\lor R_1)
\qquad
\frac{\Gamma\vdash B}{\Gamma\vdash A\lor B}\;(\lor R_2)
\]

\[
\frac{\Gamma,A\vdash C\qquad \Gamma,B\vdash C}
     {\Gamma,A\lor B\vdash C}\;(\lor L)
\]

这里的 \(\Gamma\) 出现在两个**互斥情形**中：实际构造时或者走 \(A\) 情形，或者走 \(B\) 情形，并非同时取得两份 \(\Gamma\)。

### 蕴涵

\[
\frac{\Gamma,A\vdash B}
     {\Gamma\vdash A\to B}\;(\to R)
\]

\[
\frac{\Gamma\vdash A\qquad \Delta,B\vdash C}
     {\Gamma,\Delta,A\to B\vdash C}\;(\to L)
\]

第一规则不是丢弃 \(A\)，而是把对它的需求记入 \(A\to B\)。第二规则中，\(\Gamma\) 用来供给函项的实项，\(\Delta\) 用来继续消耗结果 \(B\)，两者不得重叠。

### 量词

\[
\frac{\Gamma\vdash A[y/x]}
     {\Gamma\vdash \forall xA}\;(\forall R)
\]

其中 \(y\) 不得自由出现于 \(\Gamma\) 及原结论。

\[
\frac{\Gamma,A[t/x]\vdash C}
     {\Gamma,\forall xA\vdash C}\;(\forall L)
\]

\[
\frac{\Gamma\vdash A[t/x]}
     {\Gamma\vdash \exists xA}\;(\exists R)
\]

\[
\frac{\Gamma,A[y/x]\vdash C}
     {\Gamma,\exists xA\vdash C}\;(\exists L)
\]

其中 \(y\) 不得自由出现于 \(\Gamma,C,\exists xA\)。

一次使用 \(\forall xA\) 只取得一个实例；它不会在使用后仍留在清单中。

### 切

\[
\frac{\Gamma\vdash A\qquad \Delta,A\vdash C}
     {\Gamma,\Delta\vdash C}\;(\mathrm{Cut})
\]

切把一份产品 \(A\) 交给一个确实需要 \(A\) 的后续证明，不复制也不丢弃前提。

---

## 1.2 失效的推理

### （1）同一前提需要使用两次

通常由

\[
A\to(A\to B),\quad A
\]

推出 \(B\) 时，\(A\) 要供给两次。现在只能推出

\[
A\to(A\to B),\ A,\ A\vdash B,
\]

不能收缩成

\[
A\to(A\to B),\ A\vdash B.
\]

同样，

\[
A\vdash A\land A
\]

不再成立：右支与左支各需一份 \(A\)，而原清单只有一份。

### （2）投影与无用前提

通常的合取消去

\[
A\land B\vdash A,\qquad A\land B\vdash B
\]

都失效，因为另一分量被丢弃。保留下来的消去形式必须是：

> 若从 \(A,B,\Gamma\) 共同推出 \(C\)，才可从 \(A\land B,\Gamma\) 推出 \(C\)。

弱化失效还意味着：

\[
\vdash A
\]

不能推出

\[
B\vdash A.
\]

因此也不能把任意已证命题置于一个无用前件之后，推出 \(B\to A\)。

### （3）全称命题不能反复取用

从 \(\forall xA(x)\) 可以同时取得 \(A(t)\) 与 \(A(s)\) 的通常证明失效。若两个实例都要使用，前提清单必须本来就有两份相应的全称命题，或分别由其他前提构造出来。

---

## 1.3 空前提并未被禁止

空清单仍可用于没有未满足需求的逻辑真理。例如：

\[
\frac{A\vdash A}{\vdash A\to A}\;(\to R)
\]

这里并非"从空无构造 \(A\)"，而是把唯一的 \(A\) 同时作为函项的输入与输出账目。

但空前提结论不能随意增加前提：

\[
\vdash A\to A
\]

不能推出

\[
B\vdash A\to A.
\]

所以"允许空前提"不等于"允许弱化"。

---

## 1.4 意外存活者

下列推理仍然成立：

- 同一律：\(\vdash A\to A\)；
- 肯定前件：\(A,A\to B\vdash B\)；
- 蕴涵传递：\(A\to B,B\to C,A\vdash C\)；
- 合取交换与结合；
- 析取引入：\(\vdash A\to A\lor B\)；
- 单实例化：\(\vdash\forall xA\to A[t/x]\)；
- 存在引入：\(\vdash A[t/x]\to\exists xA\)；
- 若 \(x\) 不自由出现于 \(A\)，则 \(\vdash A\to\forall xA\)；
- 合取—蕴涵改写法，见第二节定理 2。

尤其值得注意：\(\vdash A\to A\lor B\) 并未因禁止丢弃而失效。它没有丢弃任何前提，只是给结论增加了另一种可能。

---

# 二、判据审判：复制、丢弃与经典定理的合法限度

## 2.1 受限资源下的合法性判据

一份证明合法，当且仅当它满足以下账目条件：

1. **出现条件**：前提按出现次数区分，不得把 \(A,A\) 与 \(A\) 混同。
2. **分配条件**：在 \(\land R,\to L,\mathrm{Cut}\) 中，前提清单必须分配给各支；每份出现只能进入一支。
3. **分情形条件**：只有在 \(\lor L\) 中，同一 \(\Gamma\) 可进入两个互斥情形；每个情形仍须各自完整使用它。
4. **消耗条件**：前提不能被留到证明末尾后悄然删去。由 \(\to R\) 收入蕴涵前件，不算删去。
5. **复制条件**：若一份构造确需两份 \(A\)，结论的前提清单必须反映这两项需求。两份 \(A\) 可以来自两个不相交的前提清单，却不能由同一出现自动分身。

因此，对一份旧证明中的某次 W 或 K，能否删去该步骤的判据是：

> **删去该步骤以后所得相继式，必须在 \(\mathfrak M\) 中另有一份合规证明。**

这不是准许继续使用 W/K；它只是要求拿出另一份证明。第三节将说明，命题片段中这一判据可以机械执行。

实际丢弃前提没有任何内部许可条件。切消过程中可以删去一段已经不再需要的备择子证明，但那是证明图的改写，不是从某个已证相继式中删去前提。

## 2.2 定理 1：整数数值检验可靠，可据此否定一批经典有效式

在命题片段中，给每个命题原子指定一个整数。定义：

\[
v(A\land B)=v(A)+v(B),
\]

\[
v(A\lor B)=\max(v(A),v(B)),
\]

\[
v(A\to B)=v(B)-v(A).
\]

对清单 \(\Gamma=A_1,\ldots,A_n\)，令

\[
v(\Gamma)=v(A_1)+\cdots+A_n),\qquad v(\varnothing)=0.
\]

称相继式 \(\Gamma\vdash C\) 数值成立，如果

\[
v(\Gamma)\le v(C).
\]

**定理 1。** 若 \(\Gamma\vdash C\) 在 \(\mathfrak M\) 的命题片段中可证，则它在每组整数赋值下都数值成立。

**证明。** 对证明高度作归纳。

- 初始式 \(A\vdash A\) 给出 \(v(A)\le v(A)\)。
- 对 \(\land R\)，若
  \[
  v(\Gamma)\le v(A),\qquad v(\Delta)\le v(B),
  \]
  两式相加便得
  \[
  v(\Gamma,\Delta)\le v(A)+v(B)=v(A\land B).
  \]
- 对 \(\to R\)，若
  \[
  v(\Gamma)+v(A)\le v(B),
  \]
  移项即得
  \[
  v(\Gamma)\le v(B)-v(A)=v(A\to B).
  \]
- 对 \(\lor L\)，若
  \[
  v(\Gamma)+v(A)\le v(C),\qquad
  v(\Gamma)+v(B)\le v(C),
  \]
  则 \(v(A),v(B)\) 都不超过 \(v(C)-v(\Gamma)\)，故其较大者也不超过它。
- 对 \(\to L\)，由
  \[
  v(\Gamma)\le v(A),\qquad v(\Delta)+v(B)\le v(C)
  \]
  得
  \[
  \begin{aligned}
  v(\Gamma,\Delta,A\to B)
  &=v(\Gamma)+v(\Delta)+v(B)-v(A)\\
  &\le v(\Delta)+v(B)\\
  &\le v(C).
  \end{aligned}
  \]
- 切的情形同理：把 \(v(\Gamma)\le v(A)\) 代入
  \(v(\Delta)+v(A)\le v(C)\)，即得
  \(v(\Gamma,\Delta)\le v(C)\)。

其余命题规则只是等值改写或同法相加。故定理成立。∎

**判定后果。** 下列公式均在通常经典真值解释下有效，却不能在 \(\mathfrak M\) 中证明：

| 公式 | 数值 | 反驳赋值 |
|---|---:|---|
| \(A\to A\land A\) | \(v(A)\) | 取 \(v(A)=-1\) |
| \(A\land B\to A\) | \(-v(B)\) | 取 \(v(B)=1\) |
| \(A\to(B\to A)\) | \(v(B)\) | 取 \(v(B)=-1\) |
| \((A\to(A\to B))\to(A\to B)\) | \(v(A)\) | 取 \(v(A)=-1\) |

空前提相继式若可证，数值必须始终非负；表中赋值都使其小于零，故由定理 1 不得可证。

这里不是宣布这些公式"假"，而是证明：**它们的经典证明不可避免地使用了复制或丢弃前提的能力。**

## 2.3 定理 2：合取与连续蕴涵仍可互相改写

**定理 2。** 对任意 \(A,B,C\)，有

\[
\vdash ((A\land B)\to C)\to(A\to(B\to C))
\]

及

\[
\vdash (A\to(B\to C))\to((A\land B)\to C).
\]

**证明。** 第一式中，取三份前提

\[
f:(A\land B)\to C,\qquad a:A,\qquad b:B.
\]

由 \(a,b\) 经 \(\land R\) 得 \(A\land B\)，再交给 \(f\)，得 \(C\)。依次收入 \(b,a,f\)，即得第一式。每份前提恰好使用一次。

第二式中，取

\[
g:A\to(B\to C),\qquad p:A\land B.
\]

由 \(\land L\) 将 \(p\) 拆成 \(a:A,b:B\)。先把 \(a\) 交给 \(g\)，得 \(B\to C\)，再把 \(b\) 交给它，得 \(C\)。依次收入 \(p,g\)，即得第二式。∎

这说明"同一命题可否改写成另一形式"与"前提能否免费复制"是两件事；受限演算并非把一切通常变形都摧毁了。

---

# 三、受限收编：把"恰用一次"建立为证明论对象

## 3.1 定义：计量证明与情形

一个**计量证明**就是按第一节规则构成的有限证明树。

- 在不含 \(\lor L\) 的证明中，每份前提按字面恰用一次。
- 含 \(\lor L\) 时，把每次选择一条析取分支称为一个**情形**。要求每份前提在每个情形中恰用一次。

因此，重复书写的 \(A,A\) 是两份资源；它们可以分别使用一次，但不得收缩。

## 3.2 定理 3：计量不变量

**定理 3。** 在任何计量证明中：

1. 没有一份前提被同一情形消费两次；
2. 没有一份前提在某个情形中未经使用便消失；
3. 两份不同出现即使在后续步骤中进入同一公式，也仍保留各自的来源账目。

**证明。** 对证明树由下往上检查。

- 初始式只含一份 \(A\)，其唯一出现用于结论 \(A\)。
- \(\land R,\to L,\mathrm{Cut}\) 的前提清单互不重叠，所以一份出现只能进入一个直接前提。
- \(\land L,\to R,\forall L,\exists L\) 只改变公式的记法或把需求收入结论，不减少清单中其他出现。
- \(\lor R,\exists R\) 保持整个 \(\Gamma\)。
- \(\lor L\) 把 \(\Gamma\) 放进两个互斥情形；对每个情形分别应用归纳假设。
- 量词规则只约束变元，不增减公式出现。

故三条性质在所有规则下均保持。∎

这条定理也说明：本系统不是"先使用 W/K，再在外表上隐藏它们"；根本没有可执行复制或丢弃的内部步骤。

## 3.3 定理 4：切消定理仍然成立

**定理 4。** 任一含切的计量证明，都能改写成结论相同且不含切的计量证明；改写过程不添加 W 或 K。

**证明要点。** 以切公式复杂度为第一归纳参数，以证明高度为第二参数。

### 主切：合取

若切的一侧由

\[
\frac{\Gamma_1\vdash A\qquad\Gamma_2\vdash B}
     {\Gamma_1,\Gamma_2\vdash A\land B}
\]

结束，另一侧由

\[
\frac{\Delta,A,B\vdash C}
     {\Delta,A\land B\vdash C}
\]

结束，则改成两次较低复杂度的切：

\[
\Gamma_2\vdash B
\quad\text{与}\quad
\Delta,A,B\vdash C
\]

先切，得 \(\Delta,A,\Gamma_2\vdash C\)；再以 \(\Gamma_1\vdash A\) 切去 \(A\)，得

\[
\Gamma_1,\Gamma_2,\Delta\vdash C.
\]

### 主切：蕴涵

若一侧由 \(\Pi,A\vdash B\) 得 \(\Pi\vdash A\to B\)，另一侧由

\[
\Sigma\vdash A,\qquad\Theta,B\vdash C
\]

得 \(\Sigma,\Theta,A\to B\vdash C\)，则：

1. 用 \(\Sigma\vdash A\) 切进 \(\Pi,A\vdash B\)，得 \(\Pi,\Sigma\vdash B\)；
2. 再切进 \(\Theta,B\vdash C\)，得 \(\Pi,\Sigma,\Theta\vdash C\)。

两次切分别作用于 \(A\) 与 \(B\)，复杂度均低于 \(A\to B\)。

### 主切：析取

若左方由 \(\lor R_1\) 从 \(\Pi\vdash A\) 得来，右方由

\[
\Sigma,A\vdash C,\qquad\Sigma,B\vdash C
\]

得来，则只保留实际选用的 \(A\) 分支，并把 \(\Pi\vdash A\) 切进 \(\Sigma,A\vdash C\)。删除的是未被选择的备择证明支，不是相继式中的前提。

### 主切：量词

- 对 \(\forall\)，把全称引入所用的本征变元替换为另一侧的项 \(t\)，再对 \(A[t/x]\) 作较低复杂度的切。
- 对 \(\exists\)，把存在消去所用的本征变元替换为存在引入的见证项 \(t\)，再作同样的切。

若切公式并非某一侧最后规则的主公式，就把切上移到最后规则之前；此时切公式复杂度不变而高度降低。遇到 \(\lor L\)，至多把同一改写分别用于两个互斥情形，不产生同时使用两份资源的情形。故按双重归纳最终除去一切切。∎

## 3.4 定理 5：命题片段的合法性可机械判定

**定理 5。** 对不含量词的相继式，"是否在 \(\mathfrak M\) 中可证"存在有限判定程序。

**证明。** 由定理 4，只需寻找无切证明。

从结论自下而上枚举可能的最后规则：

- 每条逻辑规则都至少拆解一个联结词；
- 不引入原相继式所没有的新公式；
- \(\land R\) 与 \(\to L\) 只需枚举有限多种清单分配；
- \(\lor L\) 虽在两个分支中重写同一清单，但每个分支都严格减少一个 \(\lor\)；
- 每条分支最多只能进行原相继式中联结词总数所限制的那么多次拆解。

因此候选证明树的总数有限。逐棵检查末端是否都是 \(A\vdash A\) 即可。∎

**诚实降级。** 对含量词的全部相继式，**以现有工具无法解决普遍有限判定问题**。障碍在于 \(\forall L\) 与 \(\exists R\) 允许选取任意项，单步枚举不再天然有限；目前不能从命题片段的有限性推出全系统的有限性。这里只申报缺少有限搜索界限，不虚构全局判定程序。

---

# 四、镜像：证明与构造性对象的局部对应

以下限于命题的 \(\land,\lor,\to\) 片段。

## 4.1 构造项

采用以下构造：

\[
x\mid \lambda x.t\mid st\mid
\langle s,t\rangle\mid
\operatorname{let}\langle x,y\rangle=s\ \operatorname{in}\ t
\]

以及

\[
\operatorname{inl}t\mid \operatorname{inr}t\mid
\operatorname{case}s\ \operatorname{of}\
(\operatorname{inl}x\mapsto u;\ \operatorname{inr}y\mapsto v).
\]

解释如下：

- \(x:A\) 是一份前提出现的名称；
- \(\lambda x.t\) 对应 \(\to R\)；
- \(st\) 对应把函项用于一份实项；
- \(\langle s,t\rangle\) 对应 \(\land R\)，其两份自由前提清单必须不相交；
- \(\operatorname{let}\langle x,y\rangle=s\ \operatorname{in}\ t\) 对应同时取用合取的两部分；
- \(\operatorname{case}\) 对应 \(\lor L\)，两个分支是在不同情形下使用同一外围清单。

所谓"项属于 \(\Gamma\vdash A\)"，就是它的自由前提名称与 \(\Gamma\) 的出现一一相应，并满足上述使用约束。

## 4.2 定理 6：化约保持相继式与计量不变量

**代入引理。** 若 \(x\) 在 \(u\) 的每个情形中恰出现一次，而 \(a\) 使用清单 \(\Delta\)，则以 \(a\) 替换 \(x\)，不会复制或删除 \(\Delta\) 中的任何前提；只是把 \(a\) 的构造接入唯一的 \(x\) 位置。

**定理 6。** 以下三种基本化约都保持所属相继式及"每情形恰用一次"的性质：

\[
(\lambda x.u)a\ \longrightarrow\ u[x:=a],
\]

\[
\operatorname{let}\langle x,y\rangle=\langle a,b\rangle
\ \operatorname{in}\ u
\ \longrightarrow\
u[x:=a,y:=b],
\]

\[
\operatorname{case}(\operatorname{inl}a)\ \operatorname{of}\
(\operatorname{inl}x\mapsto u;\ \operatorname{inr}y\mapsto v)
\ \longrightarrow\
u[x:=a],
\]

注入右侧的情形同理。

**证明。** 第一式直接使用代入引理：\(x\) 只有一个使用位置，所以 \(a\) 不会被复制；\(u\) 又确实含有 \(x\)，所以 \(a\) 不会被丢弃。

第二式中，配对构造的两个分量分别替换 \(x,y\)。两个代入位置所承担的合计需求，正好等于原来对 \(A,B\) 的需求。

第三式中，未选分支被删除，但该分支只是另一情形的备选构造；所选结论及其余前提不变。右注入情形相同。∎

这些化约正是定理 4 中主切消去的构造写法。因此局部对应为：

\[
\boxed{
\text{计量证明}
\;\longleftrightarrow\;
\text{受使用约束的构造项}
}
\]

\[
\boxed{
\text{主切消去}
\;\longleftrightarrow\;
\text{构造的一步化约}
}
\]

这里不是把证明仅仅解释为真值，而是解释为"怎样把给定构造材料装配成结论"。

## 4.3 定理 7：析取与存在的构造性见证

**定理 7。**

1. 若 \(\vdash A\lor B\) 可证，则 \(\vdash A\) 或 \(\vdash B\) 可证。
2. 若 \(\vdash\exists xA\) 可证，则存在某个项 \(t\)，使 \(\vdash A[t/x]\) 可证。

**证明。** 先由定理 4 取无切证明。空前提前提下，最后一条规则不可能是任何左规则，因为左规则需要清单中已有公式；也不可能是初始式或切。

- 若结论是 \(A\lor B\)，最后规则只能是 \(\lor R_1\) 或 \(\lor R_2\)，其直接前提即给出第一项结论。
- 若结论是 \(\exists xA\)，最后规则只能是 \(\exists R\)，其直接前提已经对某个确定的 \(t\) 给出 \(\vdash A[t/x]\)。

故两项都成立。∎

---

# 五、总结：牺牲了什么，生成了什么

我们牺牲的是前提的免费供应：不能再把一份假设当作任意多份，也不能把不合用的假设弃之不顾。通常的合取投影、无用前件、全称命题的反复取用，以及一批依赖这些步骤的经典有效式，都随之退出。

但演算并未坍塌。我们得到了：

- 一套明确的前提出现账目；
- 合取、析取、蕴涵和量词之间仍然成立的变形；
- 不借助 W/K 的切消定理；
- 命题片段的有限合法性判据；
- 整数数值反驳法；
- 证明与受限构造项之间的对应；
- 析取结论与存在结论的见证性质。

用本年的语言说：**旧演算研究的是"哪些命题可由哪些命题推出"；新演算进一步追问，"每份假设在推理中究竟被使用了几次"。前提不再只是写出一次的名称，而成为必须在证明中逐项交代的材料。**

**下一步可把命题片段的有限判定程序展开成一份逐规则的证明搜索表。**
