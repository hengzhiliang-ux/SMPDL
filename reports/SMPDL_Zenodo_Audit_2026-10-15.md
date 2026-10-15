# Zenodo 上传档案审查（2026-10-15 19:0x）

> **性质**：诚实审查扩展轮——咖啡指令「包括之前上传 zenodo 的数据、文件，都进行一次审查」
> **范围**：archives/ 五个 zip、filelists/（指纹方法 + v24r 基线 + 三代清单）、zenodo/ 十份 metadata、ATTRIBUTION 版本表、index.md 版本声明、Paper_and_Data 副本一致性
> **方法**：按 `SMPDL_Fingerprint_Method.md` §一官方脚本从 zip 本体复算 v24r；逐字节比对 zip ↔ Paper_and_Data 全 287 文件；交叉核对 metadata/ATTRIBUTION/index 三处版本指针

---

## 一、完整性判定（核心结论）

| 项 | 判定 | 证据 |
|---|---|---|
| **Zenodo v3.3 上传物完整性** | ✅ **完好** | zip 本体复算 v24r = `cfb4b21f…629a2` 与登记基准**逐位一致**；287 文件、zip 内序 = `_v24_filelist.txt` 顺序核对 PASS |
| v3.3 metadata 与 zip 一致性 | ✅ | bytes 1,170,412 / MD5 `e944a0f4…` / fingerprint_snapshot a5b11a17（候选口径）与实物相符 |
| 历史 zip（v2.5/v2.6/v22/v23） | 🟢 在档 | 五个 zip 齐备（P1-⑤ 已立 v24r 向后滚动口径，历史指纹不可复算已诚实披露，维持） |

**结论：上传到 Zenodo 的东西没有假大空——指纹体系经受住了独立复算。** 问题全部在**上传之后的本地演化与文档指针**。

## 二、发现与分级处置

### Z1 · 🟡 B 级：「Paper_and_Data 287/287 与 v24 zip 字节一致」声明已失效

- **事实**：逐字节比对发现 **5 份文件真实内容差异**（非换行伪差）：FunctionalType_Reclassification / LawStructure_MigrationScreening / MasterMethodology_Synthesis / RemovalEmergence_Synthesis / TheoryEvolution_Retrospective；
- **根因**：这 5 份是 **P1-⑧ 独立审计修复批次**（2026-10-15 08:11–11:16，16 缺陷三批收口）改动的核心元文档——**晚于 v24 打包时刻（10-14 17:26）**。修复已进 GitHub_Pages git 与 Paper_and_Data，但 **Zenodo v3.3 的 zip 里是修复前版本**；
- **方向判定**：本地领先于归档（修复方向正确，非遗失）——这不是数据事故，是**版本滞后**；
- **处置**：① Fingerprint_Method §四追加「分叉登记」（声明何时真、何时破、5 文件名单、方向）；② **v25 发布决策交还咖啡**（正规路径 = 版本向前：修复文件 + FS 系列 + D-5 系列全部入 v25 清单重算指纹上传，不回改旧 zip）。

### Z2 · 🟢 C 级：ATTRIBUTION 头部指针陈旧 + 链接破损

- 头部仍写「版本 v2.8 / Zenodo 记录 23359509（v3.2 · 最新）」——实际最新 = v3.3（23362944），方法论版本 git 已升 v2.9；
- 链接格式破损：`<https://zenodo.org/records/23359509（v3.2>`（括号吃进 URL）；
- **处置**：头部指针更新（v2.9 / v3.3 / 修复链接）——ATTRIBUTION 在 287 清单内，工作副本为活页（zip 内旧版属历史记录不动）。

### Z3 · 🟢 C 级：index.md 版本口径标签混乱

- index 写「curated 287 份 … SHA-256 `a5b11a17…`（**v23**）」——287 是 v24 的份数、a5b11a17 是 v24 候选指纹，标签错为 v23；
- 「方法论版本 v2.8」与 git v2.9 不符；
- **处置**：改为「v24 候选 a5b11a17（不可复算，见诚实披露）+ 完整性锚 = v24r `cfb4b21f…`」+ 版本号对齐 v2.9。

### Z4 · ⚪ 登记项：未入档新文件池

- 今日全部新产出（D-5 系列 14 份、G-0 系列 5 份、FS 系列、五轴整合、备忘 v2.0、诚实审查两份）**均不在 v24 清单**——属 v25 候选池；今日诚实审查的 3 处修正文件（FourStructures 等）也不在 287 内，**Zenodo 上不存在被撤回内容**（A1 撤回发生在未归档文档上，无需 Zenodo 勘误）。

## 三、执行清单

- [x] v24r 从 zip 复算 PASS（§一）
- [x] 287 文件逐字节比对 + CRLF 分类（§二 Z1）
- [ ] Fingerprint_Method §四分叉登记
- [ ] ATTRIBUTION 头部修正（Z2）
- [ ] index.md 口径修正（Z3）
- [ ] commit + 双档 + 记忆
- [ ] **v25 发布决策交还咖啡**（Z1 处置的正规路径）

---
*Zenodo 审查 v1.0 · 2026-10-15 19:0x · 上传物完好 ✅ · 版本滞后 5 文件（P1-⑧ 修复未入档）· 指针三处修正 · v25 决策待咖啡*
