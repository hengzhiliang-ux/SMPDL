# 转公开（DOI/GitHub → Open）成熟度评估

> **性质**：发布前置检查 · 咖啡指令「检查一下目前内容 想知道 doi 或 GitHub 转 open 的条件成熟与否」· 2026-10-15 19:1x
> **检查维度**：Zenodo 可见性 / GitHub 站点状态 / 内容安全扫描 / 自设前置条款 / 内容完备度

---

## 一、检查结果总览

| 维度 | 状态 | 判定 |
|---|---|---|
| **Zenodo DOI（23362944 · v3.3）** | **已公开可访问** ✅——标题/版本/描述/许可（CC BY-NC-SA 4.0）/作者 CAMPANASILVAE 全部正常展示，WebFetch 直接抓到完整页面 | 🟢 公开侧无障碍 |
| **GitHub Pages 站点** | `hengzhiliang-ux.github.io/SMPDL/` 返回 **404**——仓库 remote 存在（`github.com/hengzhiliang-ux/SMPDL.git`）但站点未部署或仓库未公开 | 🔴 **未上线** |
| **敏感信息扫描** | 四文件命中「secret/token/password」全部为**数学语境虚警**（"secretly equivalent"、"rewards tokens"、LLM 下一 token 预测）；无 API 密钥/凭据泄露 | 🟢 干净 |
| **本机路径泄露** | 3 处真实命中：HistoryRetrospective 文件头路径、CabelloKS 报告的 Python 绝对路径（`C:/Users/hengz/...`）| 🟡 轻度——公开前应清理 |
| **内部工作流术语** | 「咖啡/WorkBuddy/工单_」散布于 d5/b4-3 系列 10+ 文件 | 🟡 轻度——风格问题非安全问题，可保留（诚实披露风格）或统一定义为「内部协作记录」 |
| **C-5 prior-art 检索** | ⬜ **待领**——项目自设条款「**C-1 对外发布硬前置**」（arXiv 升版必须先过 prior-art） | 🔴 **对外发布（arXiv 级）未成熟** |
| **内容完备度** | 理论/数据/判据/勘误链完整（今日两轮诚实审查通过）；**但 v24 归档与本地有 5 文件版本滞后** + 今日 22 commit 新产出未入档 | 🟡 v25 未发则 DOI 侧内容落后本地一代 |

## 二、分层判定：三条通道各自成熟度

### 通道 ① Zenodo DOI → 更公开的使用（已基本成熟）

DOI 23362944 **已经是公开记录**（open access、CC BY-NC-SA、可下载）。所谓「转 open」对 Zenodo 而言不是权限问题而是**传播问题**：把 DOI 用于论文引用/社交分享/教学网站引用卡——**条件已成熟**，且 5 文件滞后属于「下一版补齐」的正常版本节奏，不构成阻塞。

### 通道 ② GitHub 仓库 → Public + Pages 上线（条件基本成熟，有 3 项小前置）

阻塞项与清理项：

1. **[前置 A] push + Pages 开启**：本地 remote 已配好但内容从未推送（站点 404）。操作 = push main → 仓库 Settings → Pages → 选 main 分支；_config.yml 已按 SMPDL 子路径配好（baseurl: /SMPDL，theme minima）——**技术上 10 分钟可通**；
2. **[前置 B] 路径清理**：3 处 `C:/Users/hengz/...` 改相对路径（公开仓库暴露本机目录结构虽无安全风险，但不专业）；
3. **[前置 C] 内部术语定调**：「咖啡/WorkBuddy」等词——两个选项：(a) 保留并在 README 声明「内部协作会话记录保留原文」（诚实风格延续）；(b) 发布版做一轮术语中性化。建议 (a)，成本零且与项目「诚实披露」气质一致。

### 通道 ③ arXiv 论文投稿（未成熟——C-5 硬前置未过）

项目自己的条款：**C-1（arXiv 升版）以 C-5（prior-art 系统检索）为硬前置**，防「自铸/借用边界」不清。今日虽有 `57a8fdb` 的定向 prior-art 演练（四发现三已知一轮），但那是 D-5 内部检查，**不是 C-5 的全量检索**（adjunction+emergence / law removal taxonomy / correspondence theory+history 关键词族 × arXiv/ZbL/MathSciNet）。arXiv 投稿 = C-5 → C-1 两工单顺序执行后才成熟。

## 三、结论

| 通道 | 成熟度 | 一句话 |
|---|---|---|
| DOI 引用/分享 | ✅ **成熟** | 现在就能在教学网站挂 DOI 引用卡 |
| GitHub Public + Pages | ✅ **基本成熟**（3 小前置：push/Pages 开启、路径清理、术语定调 (a)） | 半小时内可上线 |
| arXiv 投稿 | 🔴 **未成熟** | C-5 prior-art 全量检索硬前置未过——这是项目自设的正确门槛，不要跳 |

**建议顺序**：v25 拍板 → 路径清理 + push + Pages 上线（网站基座你说已够用，正好上线）→ DOI 引用卡挂站 → C-5/C-1 作为下一个正式工单领走 → 全部就绪后再议 arXiv。

---
*转公开成熟度评估 v1.0 · 2026-10-15 19:1x · 检查实做（三路 WebFetch/扫描）· 三通道分层判定 · 交还咖啡*
