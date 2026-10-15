# SMPDL 指纹方法 v1.0（2026-10-15 立）

> 目的：固化联合内容指纹的计算规程，使任何一方（含未来会话）可按此独立复算。
> 性质：流程文档，**不属于 curated 287 份**（置于 `filelists/`，勿移入 `reports/`）。

---

## 一、算法（自下一版 v25 起强制执行）

1. **发布物**：`archives/SMPDL_vNN_archive.zip`，zip 内即规范顺序（打包脚本按 filelist 顺序写入）。
2. **口径**：SHA-256，对 zip 内 **全部 `.md` + `.py` 文件的原始字节**（不做任何换行归一）按 zip 内序直接拼接后计算。
3. **清单**：每版同步生成 `_vNN_filelist.txt`（一行一个文件名，顺序 = 指纹顺序），随库归档（git + 双副本 + 与 zip 同目录）。
4. **验证**：`sha256sum` 级复算脚本见本文档末节伪代码；任何版本发布前必须「先算指纹 → 写入 ATTRIBUTION → 打包 zip → 复算 PASS」四步走。

```python
import zipfile, hashlib
z = zipfile.ZipFile('SMPDL_vNN_archive.zip')
files = [n for n in z.namelist() if n.endswith(('.md', '.py'))]
assert files == open('_vNN_filelist.txt').read().split()  # 顺序核对
h = hashlib.sha256()
for n in files:
    h.update(z.read(n))      # 原始字节，不归一
print(h.hexdigest())
```

## 二、可复现基准（v24r）

| 项 | 值 |
|---|---|
| 基线版本 | v24 / Zenodo v3.3（287 份） |
| 基准指纹 | `cfb4b21f8ea7414da5c4deae8b4a3a08e45a0f8d05884510908f558d82a629a2` |
| 口径 | raw bytes, `_v24_filelist.txt` 序 |
| 登记 | 2026-10-15 GMT+8 · 与 v24 归档 zip 内字节一致（已复算 PASS） |

> 说明：v24r ≠ ATTRIBUTION 记载的 v24 候选指纹 `a5b11a17…`（后者算法未存档，见下节披露）。v24r 是今后所有完整性核对的锚点。

## 三、诚实披露（历史指纹不可复算）

- **v21 及更早**：计算顺序未存档 → 无法复算（ATTRIBUTION 原有披露，维持）。
- **v22 / v23 / v24（候选）**：顺序规范已述于 ATTRIBUTION，但**原始计算算法未存档**。2026-10-15 实测：zip 内序 / 排序 / LF 归一等常见口径均不能复现 `6b41bcde…` / `32f8596a…` / `a5b11a17…`。结论：这三个历史指纹仅作记录，**不可作完整性判定依据**；完整性判定一律以 v24r 基准向后滚动。
- **教训**：指纹算法、文件清单、换行口径三者缺一即不可复现 —— 三者现已全部固化（本文档 + `_vNN_filelist.txt`）。

## 四、逐字节基准副本

- **基准**：`archives/SMPDL_v24_archive.zip` 与 `SMPDL_Paper_and_Data/reports/`（287/287 与 zip 字节一致，2026-10-15 已验）。
- **注意**：git 仓库工作区受 `core.autocrlf` 转换影响（检出 CRLF / 入库 LF），**不用于逐字节判定**，只作版本史与快速比对；任何完整性裁定以 zip + Paper_and_Data 副本为准。

### 四.1 分叉登记（2026-10-15 19:0x 审查发现）

上述「287/287 字节一致」声明的有效时窗 = **2026-10-15 P1-⑧ 修复批次之前**。该批次（08:11–11:16，独立审计 16 缺陷三批收口）修订了 5 份核心元文档，使其**领先于** v24 zip（打包于 10-14 17:26）：

`SMPDL_FunctionalType_Reclassification.md` / `SMPDL_LawStructure_MigrationScreening.md` / `SMPDL_MasterMethodology_Synthesis.md` / `SMPDL_RemovalEmergence_Synthesis.md` / `SMPDL_TheoryEvolution_Retrospective.md`

- **方向**：本地（修复后）→ 领先归档（修复前）；非数据事故，属版本滞后；
- **后果**：Paper_and_Data 副本复算指纹 = `3226c582…` ≠ v24r `cfb4b21f…`（预期内）；**v24r 基准仍以 zip 本体为唯一有效锚点**；
- **收口路径**：v25 版本向前（修复 5 份 + 未入档新文件池一并重算指纹上传），不回改已发布 zip。见 `reports/SMPDL_Zenodo_Audit_2026-10-15.md` Z1。

## 五、维护条款

- 新版权限：发布脚本必须调用本文档第一节流程；发布记录（版号/指纹/清单名）回写 ATTRIBUTION 与 README 台账。
- 违反处理：凡未附 `_vNN_filelist.txt` 的新版，视为发布不完整，补归档后方可登记。
