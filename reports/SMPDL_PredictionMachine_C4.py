#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SMPDL Prediction Machine — C-4 可执行 checklist 脚本
Göttingen S/M/P × D/L · v1.0 · 2026-10-14 · CC BY-NC-SA 4.0

B4 三轮盲判定稿的落地（SMPDL_B4_LLMBlindJudge_Report.md v3.0 §五）：
  Q1 功能类型判定 —— 机器预填（判据文档随脚本分发，含向量制说明）
  Q2 涌现主型预测 —— 机器预填 + 人工复核
  Q3 γ 回收细分   —— 人工必填（程序性知识，不可文档化迁移）
  Step 3 S/M/P 断裂面扫描 —— 人工 checklist
  Step 4/5 登记/回验 —— append-only 登记簿（先登记后入库，禁事后修饰）

用法：
  python SMPDL_PredictionMachine_C4.py new --law 消去律 --group H40 \
      --strength 甲 --grade E --func T1 --double-sided no --dissent no \
      --domain 半群理论
  python SMPDL_PredictionMachine_C4.py verify            # 待回验清单
  python SMPDL_PredictionMachine_C4.py retest --group H40 --actual "..." \
      --verdict 命中|偏差|缺口
"""

import argparse
import csv
import os
import sys
import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
REGISTRY = os.path.join(BASE, "SMPDL_Prediction_Registry.csv")
CARDS = os.path.join(BASE, "prediction_cards")
HEADER = ["轮次", "日期", "组号", "律名", "登记预测", "实际", "判定", "备注"]

# ---- B4 v3.0 判据一（功能类型，含向量制说明；注入材料 B4b_criteria_injection.md 判据一+修订案A） ----
FUNC_CRITERIA = {
    "T1": "对象构成律：定义『对象是什么』，界定哪些对象合法/存在",
    "T2": "行为保证律：保证『计算/证明/推理如何运行』",
    "T3": "禁闭律：禁闭某类行为/动力学（守恒/禁闭可独立失效，双亚型）",
}

# ---- 速查卡九条（预测方法论 v1.2 §二）→ 机器可执行部分（1/2/3 主规则 + 4/5 修正项） ----
MATRIX = {
    "T1": {"即时涌现": "β 主（对象族解禁）", "γ倾向": "表征型（若乙级自带，即时）"},
    "T2": {"即时涌现": "α + 元层主（算法/判定程序）", "γ倾向": "因果型常见"},
    "T3": {"即时涌现": "β-现象（行为解禁）", "γ倾向": "渐近型可能"},
}


def yn(s):
    return str(s).strip().lower() in ("yes", "y", "1", "true", "是")


def grade_of(strength, grade, func, double_sided, dissent, law):
    """机器预填：主型/辅型向量（修订案 A 向量制）+ 修正项注记。"""
    row = MATRIX[func]
    main = row["即时涌现"]
    aux = []
    notes = []
    if func == "T2" and yn(dissent):
        aux.append("β 候选上调（β 放大器：社会性先行反对运动在案）")
        notes.append("速查卡 8：β 放大器触发")
    if yn(double_sided):
        notes.append("速查卡 4：双面律 → 学科级涌现风险 ↑")
    if str(strength).strip() == "乙":
        aux.append("γ 表征型（乙级自带，即时）")
        notes.append("速查卡 5/9：乙级 100% 携带表征 γ（γ 双标制：属性向量非互斥）")
    if func == "T1" and str(strength).strip() == "乙":
        notes.append("速查卡 6：定价优于禁止——优先预测『付费化』而非『失效』")
    return main, aux, notes, row["γ倾向"]


def card_text(law, group, strength, grade, func, ds, dissent, domain, main, aux, notes, gamma_hint):
    today = datetime.date.today().isoformat()
    aux_s = " + ".join(aux) if aux else "（无机器预填辅型）"
    note_s = "\n".join(f"- {n}" for n in notes) if notes else "- （无修正项触发）"
    return f"""# 预测卡 · {law}（{group}）

> 生成：{today} · SMPDL Prediction Machine C-4 v1.0 · 机器预填 + 人工必填
> 功能类型判据：{FUNC_CRITERIA[func]}

## 一、定坐标（Step 1）
| 字段 | 值 |
|---|---|
| 律名 | {law} |
| 组号 | {group} |
| 领域 | {domain} |
| 强度 | {strength} |
| 档位 | {grade} |
| 功能类型 | {func} |
| 双面律 | {ds} |
| 先行反对运动 | {dissent} |

## 二、查矩阵（Step 2 · 机器预填，人工复核）
| 字段 | 机器预填 |
|---|---|
| 即时涌现主型 | {main} |
| 辅型向量 | {aux_s} |
| γ 倾向 | {gamma_hint} |

修正项注记：
{note_s}

## 三、γ 回收细分 [人工必填 · B4 判据：此字段机器化暂缓]
- γ 形态（表征/因果/渐近/成熟/翻译，可多选——γ 双标制属性向量）：
- 依据（回验史类比案例）：

## 四、断裂面预扫描（Step 3 · 人工 checklist）
- [ ] S 层：同名异义词清单（哪些词在两侧同名异义）：
- [ ] M 层：定理群账本（哪些定理生死反转）：
- [ ] P 层：框架盲区押注（家族第几例 / 自动拦截是否覆盖）：

## 五、桥点与接盘（人工）
- 桥点清单（残存律/免费区/降档阶梯/镜像字典）：
- 跨域锚候选：

## 六、登记行（Step 4 · 已写入登记簿，禁事后修饰）
（见 SMPDL_Prediction_Registry.csv 末行）

## 七、回验（Step 5 · 留空待回验）
- 判定：＿＿＿（✅ 命中 / ❌ 偏差→修订案 / ⚠️ 缺口→新现象）
- 实际涌现：
"""


def cmd_new(a):
    main, aux, notes, gamma_hint = grade_of(
        a.strength, a.grade, a.func, a.double_sided, a.dissent, a.law)
    pred = f"主型[{main}] 辅型[{'+'.join(aux) if aux else '无'}] γ[人工待定] γ倾向[{gamma_hint}]"
    today = datetime.date.today().isoformat()
    os.makedirs(CARDS, exist_ok=True)
    path = os.path.join(CARDS, f"card_{a.group}_{a.law}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(card_text(a.law, a.group, a.strength, a.grade, a.func,
                          a.double_sided, a.dissent, a.domain, main, aux, notes, gamma_hint))
    exists = os.path.exists(REGISTRY)
    with open(REGISTRY, "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        if not exists:
            w.writerow(HEADER)
        w.writerow(["", today, a.group, a.law, pred, "", "待回验", ""])
    print(f"[C-4] 预测卡已生成：{path}")
    print(f"[C-4] 登记簿已追加（先登记后入库 ✓）：{REGISTRY}")
    print(f"[C-4] 机器预填：{pred}")
    print("[C-4] 人工待办：γ 细分 / S·M·P 扫描 / 桥点接盘（见卡内 checklist）")


def cmd_verify(_a):
    if not os.path.exists(REGISTRY):
        print("[C-4] 登记簿为空。")
        return
    with open(REGISTRY, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    pending = [r for r in rows if r["判定"] in ("待回验", "")]
    print(f"[C-4] 登记总数 {len(rows)}，待回验 {len(pending)}：")
    for r in pending:
        print(f"  - {r['组号']} {r['律名']}（{r['日期']}）：{r['登记预测']}")


def cmd_retest(a):
    if not os.path.exists(REGISTRY):
        sys.exit("[C-4] 登记簿不存在。")
    with open(REGISTRY, encoding="utf-8") as f:
        rows = list(csv.reader(f))
    hit = None
    for i in range(len(rows) - 1, 0, -1):
        if len(rows[i]) >= 4 and rows[i][2] == a.group and rows[i][6] in ("待回验", ""):
            hit = i
            break
    if hit is None:
        sys.exit(f"[C-4] 未找到 {a.group} 的待回验登记行。")
    rows[hit][5] = a.actual
    rows[hit][6] = {"命中": "✅ 命中", "偏差": "❌ 偏差→修订案", "缺口": "⚠️ 缺口→新现象"}[a.verdict]
    rows[hit][7] = a.note
    rows[hit][0] = a.round
    with open(REGISTRY, "w", encoding="utf-8", newline="") as f:
        csv.writer(f).writerows(rows)
    print(f"[C-4] 回验已登记：{a.group} → {rows[hit][6]}（登记预测列保持原样，未修饰 ✓）")


def main():
    p = argparse.ArgumentParser(description="SMPDL Prediction Machine C-4")
    sub = p.add_subparsers(dest="cmd", required=True)
    n = sub.add_parser("new")
    n.add_argument("--law", required=True)
    n.add_argument("--group", required=True)
    n.add_argument("--strength", required=True, choices=["甲", "乙", "丙"])
    n.add_argument("--grade", required=True, choices=["E", "D", "I"])
    n.add_argument("--func", required=True, choices=["T1", "T2", "T3"])
    n.add_argument("--double-sided", default="no")
    n.add_argument("--dissent", default="no")
    n.add_argument("--domain", default="")
    n.set_defaults(fn=cmd_new)
    v = sub.add_parser("verify")
    v.set_defaults(fn=cmd_verify)
    r = sub.add_parser("retest")
    r.add_argument("--group", required=True)
    r.add_argument("--actual", required=True)
    r.add_argument("--verdict", required=True, choices=["命中", "偏差", "缺口"])
    r.add_argument("--round", default="")
    r.add_argument("--note", default="")
    r.set_defaults(fn=cmd_retest)
    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
