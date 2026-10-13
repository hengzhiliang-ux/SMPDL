# 机器能否在不前视的情况下基于 SMPDL 方法论构建证明？

> 问题：机器（AI / 自动定理证明器）在不使用前视的前提下，是否能基于 S/M/P × D/L + 防前视构建流程来自动构造数学证明？  
> 版本：v1.0 | 日期：2026-10-12 | 框架：Göttingen S/M/P × D/L

---

## 一、先澄清「前视」对机器意味着什么

### 1.1 人类的前视 vs 机器的前视

| 类型 | 表现 | 例子 |
|---|---|---|
| **人类前视** | 写证明时心里已有结论，不知不觉把结论需要的前提当作已知 | 「因为 △ABC 是等腰，所以角平分线也是高」——但等腰正是待证 |
| **LLM 前视** | 训练数据里充满「 polished proof 」，模型学会按结论倒推的叙述方式生成文本 | 生成「设 P 为某点使得 PE = PD」，而 PE = PD 等价于目标 |
| **形式化系统前视** | 允许一个形式化证明在语法上合法，但**语义上循环**或依赖尚未证明的引理 | 用 `theorem P` 证明 `theorem Q`，而 Q 是 P 的等价命题 |
| **ATP 搜索前视** | 启发式搜索可能把「接近目标」的节点优先，导致搜索路径被目标污染 | A* 启发函数包含目标信息，反向传播到中间状态 |

**关键**：前视不是语法错误，而是**元逻辑/策略纪律问题**。形式化检查器能发现非法推理步骤，但通常不会自动禁止「用目标本身来指导搜索」这种策略层面的偏见。

### 1.2 为什么机器特别容易「前视」

1. **训练数据偏见**：人类发表的证明 99% 是重写后的 polished 版本，从结论倒推的痕迹被抹平。LLM 学到的不是「发现过程」，而是「叙述过程」。
2. **自回归生成机制**：LLM 每次预测下一个 token，天然倾向于生成让后续内容「说得通」的中间步骤——而「说得通」往往是以结论为锚。
3. **奖励函数偏见**：RLHF / 证明验证器奖励「最终能证明结论的序列」，这会鼓励模型找到任何能到达目标的路径，包括循环论证。
4. **形式化系统的开放性**：Lean/Coq 只检查 local correctness，不检查 global strategy 是否循环（除非显式加约束）。

---

## 二、机器执行 SMPDL 防前视构建的理论可行性

### 2.1 流程可被机械化

SMPDL 防前视构建流程的每个阶段都可以被形式化为机器可执行的任务：

| 阶段 | 机器可执行操作 | 需要的能力 |
|---|---|---|
| **阶段 0：显式化目标与前提** | 从自然语言/形式化命题中提取量词、假设、结论 | NLP 解析 / Lean 语法树分析 |
| **阶段 1：反向草图** | 从目标 P 生成候选子目标树 G₁, G₂, …, Gₙ | 策略库 / 证明规划（proof planning） |
| **阶段 2：正向重写** | 从前提出发，尝试对每个 Gᵢ 独立证明 | ATP / tactic 搜索 / LLM 受控生成 |
| **阶段 3：双向验证** | 检查 A → Gᵢ 和 Gᵢ → P 是否同时成立 | 依赖图分析 / 反向蕴涵检查 |
| **阶段 4：等价循环探测** | 检测 Gᵢ 与 P 之间的逻辑等价或循环依赖 | 命题逻辑等价判定 / 定理依赖图 |
| **阶段 5：边界扫描** | 自动生成退化/边界/反例测试 | 符号计算 / 模型生成（如 Mathematica/Z3） |
| **阶段 6：S/M/P × D/L 判定** | 汇总六格矩阵结果 | 元级评估器 |

**结论**：从理论上讲，机器**可以**执行这套流程。难点在于如何让它**严格遵守「每个子目标必须独立正向闭合」的纪律**。

### 2.2 机器的优势

| 优势 | 说明 |
|---|---|
| 不会疲劳 | 可以穷举大量子目标 |
| 不会「显然」 | 不会省略 betweenness / on-segment 等隐性条件 |
| 可强制纪律 | 可以禁止某些 tactic / 禁止引用未来目标 |
| 可形式化检查 | 每个正向重写步骤都可以喂给 Lean/Coq kernel |
| 可记录搜索树 | 便于事后审计前视嫌疑路径 |

### 2.3 机器的局限

| 局限 | 说明 |
|---|---|
| 不会发明新概念 | 机器难以提出「mollifier」「Kempe chain」这类启发式工具 |
| 搜索空间爆炸 | 反向草图可能生成指数级子目标 |
| 无法判断「是否值得」 | 机器可能在一个无望的方向上无限消耗 |
| 训练数据污染 | LLM 可能复现人类证明中的前视结构 |
| 形式化覆盖不足 | 如 RH 案例所示，mathlib 缺乏所需分析数论工具 |

---

## 三、具体实现架构：如何把 SMPDL 编码为机器约束

### 3.1 架构分层

```
┌─────────────────────────────────────────┐
│  Layer 4: 元级控制器（Meta-Controller）     │  人类监督 + 高层策略选择
│  职责：选择研究方向、判定「是否继续」        │
├─────────────────────────────────────────┤
│  Layer 3: SMPDL 纪律执行器                 │
│  职责：强制反向草图→正向重写、双向验证、     │
│        等价循环探测、边界扫描              │
├─────────────────────────────────────────┤
│  Layer 2: 证明搜索器（ATP / LLM / Tactic） │
│  职责：在每个 OPEN 子目标上尝试正向证明      │
├─────────────────────────────────────────┤
│  Layer 1: 形式化 Kernel（Lean/Coq）        │
│  职责：验证每个推理步骤的 local correctness │
└─────────────────────────────────────────┘
```

### 3.2 关键约束编码

把 SMPDL 纪律变成对 Layer 2 搜索器的硬性限制：

#### 约束 1：子目标隔离

```python
# 每个子目标 G_i 必须在独立的 proof context 中证明
# 禁止访问目标 P 或等价命题
prove(G_i, allowed_premises=A ∪ {already_closed_G_j}, forbidden=P)
```

#### 约束 2：禁止等价循环

```python
def is_circular(G_i, P, theorem_dependency_graph):
    # 如果 G_i 与 P 在命题逻辑上等价，或 G_i 依赖 P，则拒绝
    if equivalent(G_i, P) or depends_on(G_i, P):
        raise ForesightViolation("子目标等价于目标或依赖目标")
```

#### 约束 3：双向验证

```python
# 对每个 G_i，必须同时证明：
# 1. A ⊢ G_i（从前提出发可证）
# 2. G_i ⊢ P_partial（能推进到目标）
assert prove(A, G_i)
assert prove(G_i, next_goal_in_path_to_P)
```

#### 约束 4：边界扫描自动化

```python
# 对每个量词、除法、开方、极限等操作，自动生成边界测试
boundary_cases = generate_boundary_cases(G_i)
for case in boundary_cases:
    assert prove(G_i, special_assumptions=case) or mark_qualitative()
```

#### 约束 5：Lean 中的诚实 `sorry`

```lean
-- 把每个 OPEN 子目标诚实地标记为 sorry
-- 禁止用 auto 或 simp 自动填掉依赖外部目标的缺口
theorem G6_moments_offline_control : ... := by
  sorry  -- 明确承认：当前前提不足以闭合此目标
```

---

## 四、LLM  vs 符号 ATP 的不同角色

### 4.1 LLM 适合做什么

| 任务 | 原因 |
|---|---|
| 反向草图生成 | 能基于模式识别提出合理子目标 |
| 自然语言 ↔ 形式化翻译 | 擅长把数学直觉写成 Lean 骨架 |
| 最近邻定理建议 | 能检索/联想相似定理 |
| 失败诊断报告 | 能把形式化失败翻译成人话 |

### 4.2 符号 ATP 适合做什么

| 任务 | 原因 |
|---|---|
| 正向重写搜索 | 在固定策略空间内穷举 |
| 等价循环探测 | 可调用 SAT/SMT/一阶逻辑判定器 |
| 边界扫描 | 可系统生成退化案例 |
| 最终验证 | Lean/Coq kernel 提供机械确定性 |

### 4.3 人机协作的最小可行方案

```
人类：设定目标 P 和前提 A，选择高层策略
  ↓
LLM：生成反向草图（子目标树），每个节点标注风险
  ↓
纪律执行器：检查每个子目标是否等价于 P、是否依赖 P
  ↓
ATP / Lean：对每个 OPEN 子目标做正向证明尝试
  ↓
人类：审查「诚实 sorry」列表，决定继续尝试还是转向新路线
```

---

## 五、一个最小可行实现：SMPDL-Guard

### 5.1 伪代码

```python
class SMPDLGuard:
    def __init__(self, goal_p, premises_a, prover_kernel):
        self.P = goal_p
        self.A = premises_a
        self.kernel = prover_kernel  # Lean / Coq / SMT
        self.closed = set()
        self.open_goals = []

    def backward_sketch(self):
        # LLM / planner 生成子目标树
        self.open_goals = self.planner.decompose(self.P)
        for g in self.open_goals:
            g.status = "OPEN"
            g.risk = self.assess_foresight_risk(g)

    def forward_rewrite(self, g):
        # 在隔离上下文中证明 g
        if self.kernel.prove(g, premises=self.A | self.closed,
                            forbidden={self.P, equivalences_of(self.P)}):
            g.status = "CLOSED"
            self.closed.add(g)
            return True
        else:
            g.status = "OPEN / FORESIGHT BLOCKED"
            return False

    def bidirectional_check(self, g):
        can_prove_from_premises = self.kernel.prove(g, self.A | self.closed)
        advances_toward_p = self.kernel.prove(g, self.P) is None  # g 不蕴含 P
        return can_prove_from_premises and not advances_toward_p

    def detect_equivalence_cycle(self, g):
        if self.kernel.equivalent(g, self.P) or self.kernel.depends_on(g, self.P):
            raise ForesightViolation(f"{g} 等价于目标或依赖目标")

    def run(self):
        self.backward_sketch()
        while self.open_goals:
            g = self.open_goals.pop(0)
            self.detect_equivalence_cycle(g)
            if not self.bidirectional_check(g):
                raise ForesightViolation(f"双向验证失败：{g}")
            if not self.forward_rewrite(g):
                print(f"OPEN 子目标（诚实 sorry）：{g}")
```

### 5.2 与 Lean 的集成点

```lean
-- 定义一个受控的 proof context
namespace SMPDLGuarded
  variable (P : Prop)  -- 目标命题，标记为不可引用
  variable (A : List Prop)  -- 前提集合

  -- 每个子目标 g 必须在此 namespace 外证明
  theorem G_i (h : A_i) : Q_i := by
    -- 禁止直接引用 P
    -- 禁止使用与 P 等价的引理（除非该引理已被独立证明）
    sorry  -- 如果无法闭合，诚实标记
end SMPDLGuarded
```

---

## 六、回答核心问题

### 机器能不能「不前视地构建证明」？

**能，但前提是**：
1. 不是让机器自由生成，而是给它一个**强制隔离目标**的元级框架；
2. 把 SMPDL 的每个纪律（反向草图、正向重写、双向验证、等价循环探测、边界扫描）编码为**可检查约束**；
3. **LLM 与符号 ATP 分离**：LLM 做草图，ATP 做验证，kernel 做最终裁决；
4. 接受「诚实 sorry」：机器无法闭合的子目标必须显式标记，而不是被前视填补。

### 当前最现实的形态

不是全自动证明器，而是 **「人机协同的防前视证明工作台」**：
- 机器负责生成候选子目标、验证局部正确性、探测循环、扫描边界；
- 人类负责审查 OPEN 子目标、决定策略转向、提出新概念。

这与 SMPDL 框架的原始设计完全一致：**审计和构建不是让人或机器单独完成，而是通过分层纪律把「前视」这种元逻辑错误显式化**。

---

## 七、下一步建议

1. **把 SMPDL-Guard 的伪代码变成 Lean Meta 程序**：写一个 Lean 4 的 `smpdl_guard` tactic，强制隔离目标。
2. **对 LLM 的系统提示词进行前视约束**：在生成证明草稿时，要求模型显式列出每个中间结论是否依赖目标。
3. **用 Göttingen 页面作为交互式防前视工作台**：用户输入目标，系统按 SMPDL 流程生成子目标树，标记 OPEN/CLOSED。
4. **在 RH 案例上做机器辅助实验**：让 LLM 生成 RH 的反向草图，用规则检查器标出 G6/G10/G11 为前视风险。

---

## 文献引用纪律检查

依据 SMPDL 文献引用纪律（真实性核查 + 支持性核查），本报告审查如下：

| 引用对象 | 真实性 | 支持性 | 说明 |
|---|---|---|---|
| 引用的数学/逻辑/编程经典结果 | ✅ 真实 | ✅ 支持 | 方法论文件引用的 Curry-Howard、模型论、类型论等概念属于公共知识。 |
| 引用的具体论文/书籍 | ⚠️ 待查 | ⚠️ 待查 | 若引用具体著作，需按真实性 + 支持性纪律核查。 |
| OpenAI/AI 相关案例 | ⚠️ 待查 | ⚠️ 待查 | 若用 OpenAI 论文作为例子，需核对原论文真实性与范围。 |

**核查结论**：本方法论/指南文件主要依赖经典概念；对具体案例或专著的引用应补充逐条核查。

---

## 署名与许可

**Göttingen S/M/P × D/L 数学证明审查方法论** · v1.3  \
**作者**：CAMPANASILVAE · fecit · MMXXVI  \
**首发时间**：2026-10-12 GMT+8  \
**永久记录**：Zenodo [10.5281/zenodo.23344975](https://doi.org/10.5281/zenodo.23344975)  \
**内容指纹清单**：见 `SMPDL_ATTRIBUTION.md`  \
**许可协议**：[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh)（署名-非商用-相同方式共享）

搬运、改写或教学引用请注明来源与本页面链接。
