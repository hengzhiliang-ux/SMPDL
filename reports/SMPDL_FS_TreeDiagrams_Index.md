# SMPDL 四结构树状图存档（SVG 源文件索引）

> **版本**：v1.0 · 2026-10-15
> **用途**：FS-1~FS-4 四张树状图的标准化 SVG 存档索引（会话内联展示的源码定版），供网页挂载与后续引用
> **视觉规范**：680px 宽 viewBox · 双色系以内 · 无渐变/阴影 · 亮色底深色字（IDE 亮/暗主题自适应由 CSS 变量承担）

## 文件清单

| # | 树 | 对应文章 | 根命题 | 分层逻辑 |
|---|---|---|---|---|
| 1 | FS-1 认知结构树 | `SMPDL_FS_Paper1_Cognitive.md` | 数学进展 = 隐性假设的显性化 | 四阶段模型 → 默认机制箱 + 涌现机制箱 → 瓶颈与偏差（诚实款）→ 可检验推论 |
| 2 | FS-2 语言学结构树 | `SMPDL_FS_Paper2_Linguistic.md` | 语言 = 跨基础迁移的载体与陷阱 | 同名异义表 + S 轴判定 → 双向错误 → 术语首现司法化（F2 取证） |
| 3 | FS-3 数学结构树 | `SMPDL_FS_Paper3_Mathematical.md` | 律是坐标 · 迁移是操作 · 涌现可预测 | 律学三维坐标 → 三型涌现 + 两阶段理论 → 预测机器 10/10（前向）→ 学科生长 + 诚实款 |
| 4 | FS-4 逻辑学结构树 | `SMPDL_FS_Paper4_Logic.md` | 逻辑：从背景规则 → 被审计对象 | E/D/I 档位（I 红标静默）→ 升降档历史 + 元层代际 → 自反性（重测 ≡ #print axioms） |

## 共同视觉语法

- 根节点 = 该结构一句话主张（蓝/紫底盒）；
- 第二层 = 核心机制群（双箱或单箱，色系按语义：teal=模型/amber=机制/purple=类型/blue=体系/green=战绩/red=诚实款·危险）；
- 底层统一收「诚实款/局限」红色区块——四图同构，交叉轮可直接拼接；
- 箭头仅表「展开/支撑」关系，不表因果（因果在文章正文）。

## 引用锚

- 系列总览：`SMPDL_FourStructures_TheoryReview.md` v1.0（@ `83c306d`）
- 小论文系列：`SMPDL_FS_Paper{1-4}_*.md` v1.0（@ `68698bf`）
- 相关新增：成立侧 P0–P4（`SMPDL_HoldingSide_Evolution.md` @ `b9bc078`）；剂量学（`SMPDL_RemovalDosimetry.md` @ `e039384` + d5/ 系列）

## 网页挂载建议（P1-③ 联动）

四张 SVG 可直接嵌入 riemann-lecturer 站点四结构页；建议路由 `/four-structures/{cognitive,linguistic,mathematical,logic}`，每页 = 树状图 + 对应小论文全文。
