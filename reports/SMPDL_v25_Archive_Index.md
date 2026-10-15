# SMPDL v25 候选池 · 梳理建档总索引

> **性质**：v25 发布前的建档梳理——今日（2026-10-15）全部新增产出的分类归档 + v25 打包预清单 · 咖啡指令「把这一部分也进行梳理建档 到时候一起放 zenodo」
> **状态**：建档完成，**发布待咖啡 token**（发布时按 Fingerprint_Method v1.0 四步走：算指纹 → 写 ATTRIBUTION → 打包 zip → 复算 PASS）
> **数量**：v24 287 份 + 新增 **45 份** = v25 **332 份**（md+py+csv）

---

## 一、新增 45 份分档索引（八大系列）

### ① D-5 剂量学系列（17 份 · reports/d5/）
今日下午主线。按证据链顺序：

| 子链 | 文件 | 内容 |
|---|---|---|
| 预注册 | SMPDL_D5_Round2_PreRegistration.md | F1–F4 量化判伪登记（冻结 `6b2d48f`） |
| 数据 | SMPDL_D5_Run2_Data.md | F1–F4 测量档案（双读数/零判定） |
| 裁定 | SMPDL_D5_Run2_Adjudication_Report.md | 独立裁定（F4 退役头注 v1.1） |
| 理论 | SMPDL_D5_Run2_TheoryInterpretation.md | 反向数学对偶定位 + 三变量骨架 |
| 循环 | SMPDL_D5_F4_Circularity_Assessment.md | F4 三层解剖 + 五途径 |
| 内窥 | SMPDL_D5_OperatorEndoscopy.md | 七文法 + 五元签名 + H-endo 三假设 |
| G-0 | SMPDL_D5_G0_LayerFirst_Protocol.md / T1_JudgingPack / T3_Predictions_Frozen / T1T2T3_Results / LogicalReinterpretation / T3B_Retest_and_Erratum | 层文法首测全链（含勘误） |
| 封存 | SMPDL_D5_Run3_Sealed.md | run 3 素材封存登记 |
| 早间 | SMPDL_D5_PreRegistered_Guesses / Run1_Report / PriorArt_Check / WorkOrder_Round2_Archive | 早会话产出（42 例普查 + prior-art） |

### ② B4-3 扩样系列（4 份 · reports/b4-3/）
裁定报告 + F2 术语扫描 + 冻结预测 CSV + 冻结脚本（十关制首例全程执行的完整工件）。

### ③ 理论综述系列（5 份）
FourStructures_TheoryReview（四结构综述）/ FS_Paper1–4（认知/语言/数学/逻辑小论文）/ FS_TreeDiagrams_Index。

### ④ Operator Lens 系列（3 份）
Restructuring / Part2_OntologyDynamics / OutOfSample_Test（OS 轮 + 🟠-10 修正）。

### ⑤ 剂量学与参数重置（3 份）
RemovalDosimetry（剂量学 v1.0 立项）/ ParameterRebuild_Reaudit（参数重建 6ef180a）/ HoldingSide_Evolution（守恒侧 P0–P4）。

### ⑥ 保律算子（1 份）
PreservingOperator_Audit（部件标签表 9 条——**C-5r 已核验 9/9**）。

### ⑦ 纪律与登记（2 份）
Backtest_Discipline（回测纪律 v2.0 十关制）/ Prediction_Registry.csv（预测登记簿）。

### ⑧ 评估与治理（10 份）
Honesty_Audit（全量诚实审查）/ Zenodo_Audit（上传档案审查）/ C5r×2（署名严谨性核查）/ OpenReadiness（转公开评估）/ Publication_Readiness（发表评估）/ Theory_Asset_Map（理论总账）/ TheoryIntegration_FiveAspects（五轴整合）/ Memo_AuditStructure_and_Removal（学术备忘 v2.0）。

---

## 二、v25 打包预清单（发布时执行）

1. **filelist 生成**：v24 清单 287 + 上表 45 = `_v25_filelist.txt`（332 行）；
2. **指纹**：按 Fingerprint_Method §一官方脚本对 332 份 raw bytes 拼接算 SHA-256 → 登记 ATTRIBUTION + `filelists/v25_baseline.txt`；
3. **打包**：`archives/SMPDL_v25_archive.zip`（按 filelist 序写入）→ 复算 PASS 四步走；
4. **双档同步**：Paper_and_Data reports/ 与 zip 字节一致核对（修复后 5 文件 + 新 45 份一并对齐）；
5. **Zenodo v3.4**：metadata 更新（版本号/描述「45 additions: D-5 dosimetry series / G-0 layer grammar / B4-3 expansion artifacts / theory reviews / governance audits」）→ 上传；
6. **README/台账回写**：版本线 v24→v25、方法论 v2.9→v3.0 候选、index.md 指纹双声明更新。

## 三、建档说明

- **命名空间**：d5/ 与 b4-3/ 子目录维持（与库内既有惯例一致）；根目录重复副本（根/b4-3/*）在 v25 打包时**不入清单**（reports/ 下为准）；
- **html/json 资产**（LawTimeline_Visual.html + data/SMPDL_LawTimeline.json）不入 curated 指纹清单（指纹口径 = md+py+csv），但作为 P1-③ 交付物随库分发；
- **维护条款**：本索引随 v25 发布后归档为发布记录；理论总账（Theory_Asset_Map）按「每大轮次更新」条款独立维护。

---
*v25 建档总索引 v1.0 · 2026-10-15 19:4x · 45 新增分八系列 · 发布待 token · 发布链 = Fingerprint_Method 四步 + Zenodo v3.4 + 台账回写*
