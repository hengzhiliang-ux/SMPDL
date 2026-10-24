# G6 Formal · 候选 3 · DeepSeek（逐字原文）

> **来源**：咖啡 2026-10-24 18:05 粘贴 · 厂牌自报「本推演未执行任何联网检索，全部内容仅凭演绎完成」
> **存证纪律**：G-L5 逐字保留 · 本件为 PFE/判定提示词嵌入底稿

---

本推演未执行任何联网检索，全部内容仅凭演绎完成。

我，1843 年 10 月 15 日晚于都柏林，明日过桥前写下此卷。以下只用实数、复数、二元组、行列式、二次型与旋转对应的已有知识；凡不能证者，明确标为未决。

## 一、清点崩溃：三维二元组式尝试为何失败

先试最自然的三秩形式：元素写作

\[
x=a+b\,\mathrm p+c\,\mathrm q,\qquad a,b,c\in\mathbb R,
\]

希望 \(1,\mathrm p,\mathrm q\) 三单位闭合，且乘法满足结合律、分配律、有单位，并令

\[
\mathrm p^2=\mathrm q^2=-1.
\]

闭合性要求

\[
\mathrm p\mathrm q=\alpha+\beta\,\mathrm p+\gamma\,\mathrm q
\]

其中 \(\alpha,\beta,\gamma\) 为实数。若乘法满足结合律，则左乘 \(\mathrm p\)：

\[
\mathrm p(\mathrm p\mathrm q)=\mathrm p^2\mathrm q=-\mathrm q.
\]

另一方面

\[
\mathrm p(\alpha+\beta\mathrm p+\gamma\mathrm q)
=\alpha\mathrm p+\beta\mathrm p^2+\gamma\mathrm p\mathrm q
=(-\beta+\gamma\alpha)+(\alpha+\gamma\beta)\mathrm p+\gamma^2\mathrm q.
\]

比较 \(\mathrm q\) 的系数，得

\[
-1=\gamma^2.
\]

但 \(\gamma\) 是实数，矛盾。

故这条三维闭合路线失败。失败点不在分配律，而在三处同时坚持：乘法闭合、结合律、以及两个独立单位平方皆为 \(-1\)。若撤去结合律或撤去平方假设，是否另有三维构造，以我现有工具不能断言；此处只如实报告该自然尝试不可修复。

## 二、重建：一个四秩非交换算术

### 定义

取四个单位 \(1,\mathrm u,\mathrm v,\mathrm w\)，元素写作

\[
x=a+b\,\mathrm u+c\,\mathrm v+d\,\mathrm w,\qquad a,b,c,d\in\mathbb R.
\]

加法、减法逐支进行。乘法由分配律与下表决定：

\[
\mathrm u^2=\mathrm v^2=\mathrm w^2=-1,
\]

\[
\mathrm u\mathrm v=\mathrm w,\quad
\mathrm v\mathrm w=\mathrm u,\quad
\mathrm w\mathrm u=\mathrm v,
\]

\[
\mathrm v\mathrm u=-\mathrm w,\quad
\mathrm w\mathrm v=-\mathrm u,\quad
\mathrm u\mathrm w=-\mathrm v.
\]

单位 \(1\) 与一切元素相乘不变。等价地，若

\[
x=(a,b,c,d),\quad y=(a',b',c',d'),
\]

则乘积为

\[
\begin{aligned}
xy={}&(aa'-bb'-cc'-dd',\\
&ab'+ba'+cd'-dc',\\
&ac'+ca'+db'-bd',\\
&ad'+da'+bc'-cb').
\end{aligned}
\]

分配律由公式对两支系数线性而成立。结合律不能靠"显然"带过；可对四个单位的每个三元组逐项核对。例如

\[
(\mathrm u\mathrm v)\mathrm w=\mathrm w\mathrm w=-1,
\]

而

\[
\mathrm u(\mathrm v\mathrm w)=\mathrm u\mathrm u=-1.
\]

其余三元组同法核对，再由线性展开推到一般元素。

### 除法与逆

定义共轭式

\[
\bar x=a-b\,\mathrm u-c\,\mathrm v-d\,\mathrm w.
\]

直接展开得

\[
x\bar x=\bar x x=a^2+b^2+c^2+d^2=:N(x).
\]

若 \(x\ne0\)，则 \(N(x)>0\)，故

\[
x^{-1}=\frac{\bar x}{N(x)}
\]

为双侧逆：

\[
xx^{-1}=x^{-1}x=1.
\]

所以每个非零元素可除，且左逆右逆同一。

### 非平凡计算例

\[
(1+\mathrm u)(1+\mathrm v)
=1+\mathrm u+\mathrm v+\mathrm u\mathrm v
=1+\mathrm u+\mathrm v+\mathrm w,
\]

而

\[
(1+\mathrm v)(1+\mathrm u)
=1+\mathrm u+\mathrm v+\mathrm v\mathrm u
=1+\mathrm u+\mathrm v-\mathrm w.
\]

二者不等，故乘法不交换。

又

\[
(1+\mathrm u)(1-\mathrm u)
=1-\mathrm u+\mathrm u-\mathrm u^2
=1+1=2,
\]

所以

\[
(1+\mathrm u)^{-1}=\frac{1-\mathrm u}{2}.
\]

再如

\[
(\mathrm u+\mathrm v)(\mathrm u-\mathrm v)
=\mathrm u^2-\mathrm u\mathrm v+\mathrm v\mathrm u-\mathrm v^2
=-1-\mathrm w-\mathrm w+1=-2\mathrm w,
\]

而反向相乘得 \(2\mathrm w\)，次序不可轻动。

## 三、审判：旧代数定理哪些存活、哪些先坏

### 仍成立者

加法交换、结合、消去、零与负元；乘法对加法分配；乘法结合；单位元；非零元素有逆；同底幂的指数相加律

\[
x^m x^n=x^{m+n}.
\]

一次方程若写作左乘形式

\[
ax=b,\qquad a\ne0,
\]

则有唯一左解

\[
x=a^{-1}b.
\]

若写作右乘形式

\[
xa=b,
\]

则有唯一右解

\[
x=ba^{-1}.
\]

但二者一般不同。例如

\[
\mathrm u x=\mathrm v
\]

给出 \(x=\mathrm u^{-1}\mathrm v=(-\mathrm u)\mathrm v=-\mathrm w\)，而

\[
x\mathrm u=\mathrm v
\]

给出 \(x=\mathrm v\mathrm u^{-1}=\mathrm v(-\mathrm u)=\mathrm w\)。

### 先坏者

第一，

\[
(a+b)^2=aa+ab+ba+bb.
\]

这里 \(ab\) 与 \(ba\) 不可合并为 \(2ab\)，除非已知二者相等。故旧式

\[
(a+b)^2=a^2+2ab+b^2
\]

只在交换情形成立。

第二，二次方程求根的配方一步塌。传统写法要把

\[
a(x+d)^2=ax^2+axd+adx+ad^2
\]

中的 \(axd\) 与 \(adx\) 合并为 \(2adx\)，再令其等于 \(bx\)。这一步实际用了 \(xd=dx\)。在非交换情形，\(axd+adx\) 不能合并；求根公式所依赖的配方因此失效。甚至在

\[
x^2+1=0
\]

中，\(\mathrm u,\mathrm v,\mathrm w\) 皆是根，旧"至多两根"的图像也坏了。

第三，行列式的乘法性依赖交换。取二行二列表

\[
A=\begin{pmatrix}\mathrm u&1\\0&\mathrm v\end{pmatrix},\qquad
B=\begin{pmatrix}\mathrm w&0\\1&\mathrm u\end{pmatrix},
\]

并令

\[
\det\begin{pmatrix}a&b\\c&d\end{pmatrix}=ad-bc.
\]

则

\[
\det A=\mathrm u\mathrm v=\mathrm w,\qquad \det B=\mathrm w\mathrm u=\mathrm v,
\]

故

\[
\det A\det B=\mathrm w\mathrm v=-\mathrm u.
\]

但

\[
AB=\begin{pmatrix}1-\mathrm v&\mathrm u\\ \mathrm v&-\mathrm w\end{pmatrix},
\]

于是

\[
\det(AB)=(1-\mathrm v)(-\mathrm w)-\mathrm u\mathrm v
=-\mathrm w+\mathrm v\mathrm w-\mathrm w
=\mathrm u-2\mathrm w.
\]

而 \(\mathrm u-2\mathrm w\ne-\mathrm u\)。所以

\[
\det(AB)=\det A\det B
\]

不成立。其证明中把展开项因子重排，正是隐蔽使用交换。

## 四、镜像：复数的哪些性质由交换律给出

逐条判定如下。

**一次方程。** 在复数中 \(ax=b\) 与 \(xa=b\) 同解，因为 \(a\) 与 \(x\) 可交换。非交换四秩算术中，左解 \(a^{-1}b\) 与右解 \(ba^{-1}\) 一般不同；左右可解性仍存活，同解性坏。

**加法结构。** 加法交换、结合、零元、负元、分配律全部存活；实数部分与一切元素可交换，也存活。

**共轭式。** 加性

\[
\overline{x+y}=\bar x+\bar y
\]

存活。乘性必须反序：

\[
\overline{xy}=\bar y\,\bar x.
\]

例如

\[
\overline{\mathrm u\mathrm v}=\overline{\mathrm w}=-\mathrm w,
\]

而

\[
\bar{\mathrm v}\bar{\mathrm u}=(-\mathrm v)(-\mathrm u)=\mathrm v\mathrm u=-\mathrm w.
\]

但旧式

\[
\overline{xy}=\bar x\bar y
\]

一般不成立；它由交换律给出。

**模长。** 定义

\[
N(x)=x\bar x=\bar x x=a^2+b^2+c^2+d^2.
\]

它恒为实数且非负，零仅当 \(x=0\)。并且

\[
N(xy)=N(x)N(y)
\]

在本构造中仍成立，可由乘法表直接展开核对。例如

\[
N(1+\mathrm u)=2,\quad N(1+\mathrm v)=2,
\]

而

\[
(1+\mathrm u)(1+\mathrm v)=1+\mathrm u+\mathrm v+\mathrm w,
\]

其模长为 \(1+1+1+1=4\)。故模长乘性不靠交换律；但旧式展开中若把共轭因子随意换序，就会偷偷把交换律请回来。

**存活清单。** 加法结构、分配、结合、单位、逆、左/右一次方程、共轭加性、共轭反序乘性、模长及其乘性存活。乘法交换、\(ab=ba\)、二项式合并、因式分解、二次方程旧求根公式、行列式乘性、共轭直接乘性、左右方程同解性先坏。

**隐蔽使用交换的一处传统证明。** 配方

\[
a(x+d)^2=ax^2+axd+adx+ad^2
\]

中，传统把 \(axd+adx\) 写成 \(2adx\)，表面只说"合并同类项"，实际需要 \(xd=dx\)。这正是表面未提 \(ab=ba\)、实际依赖交换的位置。

## 五、总结：能造什么，不能断言什么

能造出四秩非交换算术：其元素可加、可减、可乘、可除，乘法对加法分配，乘法满足结合律，但乘法不交换。三维二元组式在"闭合、结合、两单位平方为 \(-1\)"的同时要求下失败，失败点为 \(\gamma^2=-1\) 而 \(\gamma\) 为实数。

但"非交换数系在几个秩上存在"的完全刻画，以我现有工具无法解决。已知者仅：一秩实数交换；二秩复数交换；四秩有上述构造；三秩在上述自然假设下失败。卡点在于：需对所有可能的乘法表同时解结合条件与每非零元素有逆的条件；行列式方法只在交换情形可靠；二次型与旋转对应只提供局部线索；现有工具既不能排除更高秩构造，也不能证明其不可能。故此问题如实申报为未决，不把未证之事写成已证。

---

*G6-C3 · DeepSeek · 逐字保真 · 2026-10-24*
