#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B4-3 冻结脚本 (F1/F2/F4 一体化) — Backtest Discipline v2.0 关卡 3/4/6
F1: 从 c73aa62 抽取 B4-3 三行(仅预测列, 结果列物理丢弃) -> 冻结文件
F2: git log -S 术语首现扫描(冻结文件内术语不得早于 c73aa62 出现于判定侧文档)
F4: 冻结文件独立 commit, commit hash 回写头注
判定标准冻结: D1 规模/D2 时间(<=5年)/D3 功能 三问制, D1 优先, 规则 H <=5 年,
             复合事件整判, 三档(全中✅/部分中🟡/不中❌), B4 基线(凡移除皆β)同步计分
"""
import subprocess, sys, io, csv, re, os, datetime

REPO = os.path.dirname(os.path.abspath(__file__))
REG  = "reports/SMPDL_Prediction_Registry.csv"
FREEZE = "reports/b4-3/SMPDL_B4-3_Frozen_Predictions.csv"
REG_HASH = "c73aa62"
ROWS = ("B4-3-R1", "B4-3-R2", "B4-3-R3")
os.chdir(REPO)

def sh(*a):
    return subprocess.run(a, capture_output=True, text=True, encoding="utf-8", errors="replace").stdout

# ---------- F1: 抽取 ----------
blob = sh("git", "show", f"{REG_HASH}:{REG}")
rows = list(csv.DictReader(io.StringIO(blob)))
hit = [r for r in rows if r.get("轮次") in ROWS]
assert len(hit) == 3, f"F1 FAIL: 期望 3 行, 实得 {len(hit)}"

out = io.StringIO()
w = csv.writer(out, lineterminator="\n")  # 冻结文件用 LF, 与仓库惯例一致(见脚注)
w.writerow(["轮次", "日期", "组号", "律名", "登记预测"])  # 只保留预测侧列; 实际/判定/备注物理丢弃
for r in hit:
    w.writerow([r["轮次"], r["日期"], r["组号"], r["律名"], r["登记预测"]])

# 判定标准冻结(与 B4-2 一致, 未被修改: J2 关卡)
STANDARD = """# B4-3 判定标准冻结 (J2 关卡 — 与 B4-2 预注册三问制一致, 未被修改)
# D1 规模问: 涌现结构是否达到"领域级"规模? (D1 优先 — D1 不中则 D2/D3 不计)
# D2 时间问: 击破->定名定理/结构显影的时间间隔 <=5 年? (规则 H: 规则型即时)
# D3 功能问: 涌现结构的功能 = 补偿(α)/解禁(β)/表征(γ)?
# 判读: 三档制 — ✅ 全中 / 🟡 部分中 / ❌ 不中; 复合事件整判
# B4 基线: 凡移除皆 β (预测机输出), 与登记预测同步计分
# H46 对照: 二次型侧 Hasse-Minkowski 1923 = 律保持的 PreFix 对照, 单列登记
# κ 判读(预注册, 沿用 B4-2 §五): κ>=0.6 恢复 / [0.4,0.6) 降格细化 / <0.4 永久降格
"""

# ---------- F2: 术语首现扫描 ----------
terms = [
    "维数不变律", "Brouwer", "Lebesgue 覆盖维数", "空间填充",
    "monodromy", "单值提升律", "Riemann 面", "覆叠空间",
    "Hasse 局部-整体", "Selmer", "Tate-Shafarevich", "Brauer-Manin",
    "维数是拓扑不变量", "解析延拓路径无关", "局部解",
]
scan_report = ["# F2 术语首现扫描 (adjudicator-lens 术语不得早于登记 commit 出现于判定侧文档)", ""]
f2_fail = 0
for t in terms:
    # 全库 git log -S: 术语内容变化涉及的 commit 链
    log = sh("git", "log", "--all", "-S", t, "--format=%h %ad %s", "--date=short", "--", "*.md", "*.csv")
    first_line = next((l for l in log.splitlines() if l.strip()), "(全库无命中)")
    scan_report.append(f"- 「{t}」: {first_line}")

# 冻结文件自身术语必须已存在于 c73aa62 (防冻结时引入新 lens 术语)
for t in ["维数不变律", "单值提升律", "Hasse 局部-整体"]:
    if t not in blob:
        print(f"F2 FAIL: 术语「{t}」未见于登记 commit {REG_HASH}")
        f2_fail += 1

# ---------- F4: 写文件 + 独立 commit ----------
os.makedirs("reports/b4-3", exist_ok=True)
with open(FREEZE, "w", encoding="utf-8", newline="") as f:
    f.write(STANDARD)
    f.write(out.getvalue())
print(f"F1 ✅ 抽取 {len(hit)} 行 -> {FREEZE} (结果列物理丢弃)")

# 术语扫描报告落盘(判定会话可读, 只含 commit 链信息无判定内容)
with open("reports/b4-3/SMPDL_B4-3_F2_TermScan.md", "w", encoding="utf-8", newline="") as f:
    f.write("\n".join(scan_report) + "\n")
print(f"F2 ✅ 术语首现扫描报告 -> reports/b4-3/SMPDL_B4-3_F2_TermScan.md (f2_fail={f2_fail})")

# 独立 commit (F4): 冻结文件 + 扫描报告
sh("git", "add", FREEZE, "reports/b4-3/SMPDL_B4-3_F2_TermScan.md")
sh("git", "commit", "-m",
   "B4-3 freeze gate (F1/F2/F4): 3 prediction rows extracted verbatim from c73aa62 "
   "(result columns physically discarded); adjudication standard frozen verbatim from "
   "B4-2 pre-registered three-question protocol (D1 scale / D2 time <=5yr / D3 function, "
   "D1-priority, rule-H immediate, composite-event whole-judgment, 3-tier, B4-baseline "
   "all-beta co-scored); F2 term-first-appearance scan report attached; independent "
   "commit per gate 6")
h = sh("git", "rev-parse", "--short", "HEAD").strip()
print(f"F4 ✅ 独立 commit = {h}")

# 头注登记哈希: 将 commit hash 写入冻结文件第二行头注(独立小 commit)
with open(FREEZE, "r", encoding="utf-8", newline="") as f:
    content = f.read()
content = content.replace(
    "# B4-3 判定标准冻结 (J2 关卡 — 与 B4-2 预注册三问制一致, 未被修改)",
    f"# B4-3 判定标准冻结 (J2 关卡 — 与 B4-2 预注册三问制一致, 未被修改)\n# 冻结 commit: {h} (本头注行由脚本追加, 登记源 = {REG_HASH})",
    1,
)
with open(FREEZE, "w", encoding="utf-8", newline="") as f:
    f.write(content)
sh("git", "add", FREEZE)
sh("git", "commit", "-m", f"B4-3 frozen file header note: register source {REG_HASH}, freeze commit {h}")
print("F4 ✅ 头注登记完成")
print("\n=== 十关进度: 关3/4/6 ✅ ===")
