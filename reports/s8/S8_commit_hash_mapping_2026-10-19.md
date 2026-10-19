# S8 链 commit 哈希映射（2026-10-19 rebase 存证）

> **事由**：2026-10-19 22:1x GMT+8 为公开 GitHub 存证 push 前，本地 main 需 rebase 到远端新增的 `jekyll-gh-pages.yml`（a976ce1）之上——rebase 改写了 S8 链全部 commit 哈希。本表为**新旧哈希权威映射**，外部引用以本表 + GitHub 公开 commit URL 为准。rebase 只改哈希不改内容/时间序（36 commits 全部 fast-forward 重放，无冲突）。
> **公开存证**：repo = https://github.com/hengzhiliang-ux/SMPDL（public）· push 完成 2026-10-19 22:1x GMT+8（UTC 14:1x）· push 后 HEAD = `a2a4179`
> **预注册锚点注记**：工单与 v2 提示词的预注册锚点原为 `00902eb`——rebase 后新哈希见下表；提示词正文 SHA-256 `a8815811…3eb0` 与内容**不受 rebase 影响**（哈希只锚内容，不锚 commit id）。

| 环节 | 旧哈希（证书链原引） | 新哈希（GitHub 公开） | UTC 时刻（+0800 减 8） |
|---|---|---|---|
| 工单预注册锚点（v2 提示词冻结） | 00902eb | **1ba8426**（https://github.com/hengzhiliang-ux/SMPDL/commit/1ba8426） | 2026-10-19 11:35:23 |
| S8b 登记（Step 4 / R2） | 76ab9fc | 9a5d506 | 12:03:47 |
| S8b 冻结（Step 5 / F4） | 9c81083 | f8bd854 | 12:05:17 |
| 时间墙证书回填 | b1c57f3 | 9248bf5 | 12:0x |
| J-E 输出落盘 | 566a70b | 30306ba | 13:13:33 |
| J-D 输出落盘 | 2424aef | 63f08ef | 13:17:45 |
| Step 4 机械汇总 | 2114e75 | 3026a8b | 13:18:17 |
| Step 6 收敛报告 | 9d8c05d | 358f56b | 13:20:20 |
| Phase 2 工单回填 | 153c62d | ebd8c09 | 13:21 |
| Phase 3 完成 | b16468e | f60f1d3 | 13:46:14 |
| E1 勘误 | da23bb8 | a63fea0 | 13:55:06 |
| 排期表描述同步 | 97df238 | a2a4179 | — |

*00902eb 新哈希已核实：`1ba8426`（commit message "Workorder S8 v1.0 established"，GitHub URL 见表行）。

**纪律注记**：工单 §八证书与各文件头注中的旧哈希**不追改**（E2 旧版留档精神——哈希本身也是历史证据）；外部有效性由本映射表 + GitHub 承担。本表随 Zenodo v3.5 一并存证。
