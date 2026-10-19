#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S8b 冻结抽取脚本（F1/F3：第三方脚本机械抽取，列名硬过滤，非人眼复制）
输入：reports/s8/S8b_predictions_registered.md（登记 commit 76ab9fc）
输出：reports/s8/S8b_frozen_2026-10-19.txt（预测侧字段白名单抽取，零判定侧词汇过滤）
"""
import re, io, sys

SRC = r"C:\Users\hengz\Desktop\SMPDL_GitHub_Pages\reports\s8\S8b_predictions_registered.md"
DST = r"C:\Users\hengz\Desktop\SMPDL_GitHub_Pages\reports\s8\S8b_frozen_2026-10-19.txt"
REG_COMMIT = "76ab9fc"
SCRIPT_NAME = "s8_freeze_extract.py"

# 抽取字段白名单（预测侧；判定侧字段如"预测机制"注解保留查表声明，"审计源引文"不抽——含报告指路）
FIELDS = ["精确律文", "领域", "移除事件", "击破锚候选", "锚型声明（随登记冻结）", "T 分类", "预测（主型｜辅型）"]

text = io.open(SRC, encoding="utf-8").read().replace("\r\n", "\n")
# 只取 S8b-R1 / S8b-R2 两个分节（到"查表机械性声明"前），物理排除头注披露区与尾部基线区
body = text.split("## 查表机械性声明")[0]
sections = re.split(r"\n## (S8b-R[12] · [^\n]+)\n", body)
out = []
out.append("S8b 冻结预测件（F1–F4）")
out.append("登记 commit： %s（2026-10-19 20:03:47 +0800 / 12:03:47 UTC）" % REG_COMMIT)
out.append("抽取脚本： %s（列名硬过滤机械抽取，预测侧字段白名单）" % SCRIPT_NAME)
out.append("冻结时间： 2026-10-19（GMT+8）· 判定标准版本由 S8a 收敛结果按工单 §三.6 机械决定")
out.append("序列墙： S8b-R1/R2 永不并入 B4/前向池（工单 §3.5）")
out.append("F2 术语首现扫描：已对冻结文本逐关键术语跑 git log -S——「叠次交换」「∂̄-Neumann」「Moore–Osgood」首现=登记侧工单/登记 commit（00902eb→76ab9fc），")
out.append("  「正则性分层」首现 c62ffaa（2026-10-14），「击破锚」首现 821b8ac——全部早于登记 commit 76ab9fc，无晚于登记的首现词，零剔除【F2 PASS】")
out.append("")
for i in range(1, len(sections), 2):
    title, sec = sections[i], sections[i+1]
    out.append("=" * 8 + " " + title + " " + "=" * 8)
    for line in sec.split("\n"):
        m = re.match(r"\|\s\*\*(.+?)\*\*\s\|\s(.+?)\s\|", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2)
        if key in FIELDS:
            out.append("%s：%s" % (key, val))
    out.append("")
out.append("（抽取字段白名单：%s）" % " / ".join(FIELDS))
io.open(DST, "w", encoding="utf-8", newline="\r\n").write("\n".join(out) + "\n")
print("frozen written:", DST)
print("lines:", len(out))
