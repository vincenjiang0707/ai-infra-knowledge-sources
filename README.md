# AI Infra Knowledge Sources

> 抓取自公网公开内容（PDF 列出的 170 个推理调优相关来源）的本地知识原料。
> 仅供个人学习研究使用；内容版权归原作者所有，引用请回原链接。

## 快照信息

| 项 | 值 |
|---|---|
| 抓取快照日期 | 2026-09-23 |
| 来源数 | 170（success 163 / partial 1 / error 1 / blocked 5，SRC-043 寒武纪 forum 504 partial、SRC-129 Fireworks blog trafilatura no_md error）|
| 文件总数 | ~5060 |
| 总体积 | ~210 MB |
| 来源类型 | GitHub 80 · RSS/Blog 12 · HF 8 · 学术 5 · Sitemap/Docs 12 · 论坛/国产社区 9 · 其他 |

## 按抓取类型分组

| 类型 | 数量 | 典型产物 | 抽样 SRC |
|---|---|---|---|
| github_repo | 80 | `_meta.json` + `github_{issues,pulls,releases,changelog}.{jsonl,md}` + `github_details/` | SRC-003 vLLM, SRC-005 SGLang |
| site（sitemap 文档站）| 12 | `pages/*.md`（≤2000 页 / SRC）| SRC-001 vLLM docs, SRC-040 MUSA deploy |
| site（RSS 博客）| 12 | `feed_meta.json` + `posts/*.md` | SRC-165 vLLM blog, SRC-140 Lei Mao |
| site（菜单 BFS 兜底）| 4 | `pages/*.md`（深度3、≤200 页）| SRC-040 MUSA（Docusaurus baseUrl 错配走 BFS）|
| blog（JS 索引 + 串行抓 post）| 1 | `posts/NN_slug.md`（默认 ≤100 篇/SRC）| SRC-123 LMSYS blog 100 篇 1.5 MB |
| hf（HF 模型 / 组织）| 8 | `hf.md` | SRC-018 deepseek-ai |
| academic（arxiv / usenix）| 5 | `page.md` | SRC-067 arxiv vLLM |
| forum / 国产社区 | 9 | 多数 blocked（需登录 / 反爬）| SRC-043 寒武纪（GitHub 成功 + 论坛 504）|
| reference（topics / pages）| ~40 | 不抓取，仅在 registry 留索引 | github.com/topics/* |
| blocked | 5 | 无产物 | 见 `_summary/blocked.md` |

## 目录结构

```
.
├── README.md
├── SCRAPE_REPORT.md            抓取逻辑、状态机、性能与已知边界
├── _registry.json              170 SRC 元数据（含 status / channel 状态）
├── _summary/                   汇总报告（index / fetched / partial / not_fetched / blocked）
└── sources/
    └── SRC-XXX/
        ├── _meta.json              状态/游标/渠道结果
        ├── github_repo.md          仓库 README
        ├── github_issues.jsonl     top-100 issues (updated_at desc)
        ├── github_pulls.jsonl      top-100 PRs (updated_at desc)
        ├── github_releases.jsonl   全部 releases
        ├── github_changelog.md     聚合 CHANGELOG
        ├── github_details/         活跃 issue/PR 的评论 + reviews（filter: comments>0 && updated<90d）
        ├── feed_meta.json          RSS feed 元信息（RSS 源）
        ├── posts/                  RSS 全文章节（RSS 源）
        ├── pages/                  站点文档页（sitemap / menu BFS 抓的）
        └── hf.md                   HF 模型/组织概览（HF 源）
```

## 快速检索

- **按 SRC 号找**：直接看目录 `sources/SRC-XXX/`，`_meta.json` 含 URL 与状态
- **按类别找**：用 `_registry.json`，170 条全字段（`src_id` / `category` / `priority` / `status` / `channels` / `channel_types` / `started_at`）
- **找活跃 GH issue/PR**：看 `sources/SRC-XXX/github_details/_index.jsonl`，`fetched_at` 字段标了每条详情的抓取时间
- **找 RSS 文章**：看 `sources/SRC-XXX/posts/`，文件名是 `YYYYMMDD_slug.md`，按日期倒序即可
- **汇总报告**：`_summary/index.md` 列出所有 170 项状态、`_summary/fetched.md` 是成功清单

## 数据来源分类

11 类原始 PDF 分类：

- 推理引擎与部署配方
- NVIDIA / AMD / 通用芯片
- 昇腾 / 国产芯片
- 模型作者 / 平台
- Kernel / 编译优化
- 量化 / 推测解码
- KV / 路由 / 分布式
- Profiling / 压测
- 论文 / 会议
- 一手博客
- 精选作者 / 专业社区 / 新来源发现

## 更新方式

抓取脚本（`scrape/incremental_gh.py` / `detail_fetcher.py` / `summary_gen.py`）未在本仓发布；如需更新快照请回 `chaoyuan` 主仓运行。

抓取脚本行为：增量 + 详情抓取都是**幂等**设计，跳过已抓且未过期条目，不会重抓全量。

## Changelog

| 版本 | 日期 | 说明 |
|---|---|---|
| v1.2 | 2026-09-23 | SRC-XXX 移入 sources/ 子目录，减少顶层目录噪声 |
| v1.5 | 2026-09-23 | blog 通道上线：playwright 渲染 index + 正则抓 post permalinks + 串行访问每篇；SRC-123 LMSYS blog 全量 100 篇 1.5 MB 正文集（含 NVFP4 KV / DeepSeek-V4.1 / SGLang SSD Expert Pack / 等完整技术博文）|
| v1.4 | 2026-09-23 | js 通道批量重抓 21 个 SPA shell 候选：LMSYS blog 117→34700、PyTorch docs 95→8980、Horace He 317→276 等显著提升；SRC-016 CUDA docs timeout 退回 site；SRC-129 Fireworks blog trafilatura no_md 标 error |
| v1.3 | 2026-09-23 | js 通道上线：playwright headless chromium 抓 JS-rendered 站；修复 SCRAPE 路径 bug（SRC 目录迁移后 load_meta/save_meta/detail_fetcher/incremental_gh/summary_gen 仍走旧路径）；SRC-031 Nuxt.js SPA shell 重抓 898 → 26979 chars |
| v1.1 | 2026-09-23 | registry enriched（status/duration/channel_types），README 重写：按抓取类型分组 + 快速检索，去掉 scrape 引用 |
| v1.0 | 2026-09-23 | 首轮全量抓取快照：164 success / 1 partial / 5 blocked；增量逻辑落地 |

## 已知边界

- **抓 top-N + 90 天窗口**：活跃筛选是 `comments_count > 0` 且 `updated_at < 90d`，新开或长期未活动的条目不在首次抓取范围
- **GitHub 排序按 `updated_at` desc**：与网页默认一致，被人工置顶但 updated_at 老的条目可能漏在 top-100 之外
- **JS 渲染站**：js 通道可用（playwright headless chromium）。批量已处理 22 个：显著提升 5 个（LMSYS blog 117→34700、PyTorch docs 95→8980、Horace He 317→276 等）；3 个无变化（站点首页本就无正文，如 昇腾文档中心根）；1 个 trafilatura no_md（Fireworks blog 列表）；1 个 timeout 回退（CUDA docs）；CDN 受限时可用 `SCRAPE_CHROME` 指向本地 chromium 二进制
- **sitemap.xml 缺失站点**：走 menu BFS fallback（深度3、每 SRC ≤200 页），可能漏深层子菜单
- **多仓 SRC（如 SRC-004 vLLM + sglang docs）**：增量时合并刷新（每仓 ≤3 页）
- **详情抓取中 PR reviews 与 comments 是两个端点**：缺一会漏 claude[bot] 类自动审查
- **公网版权**：raw HTML→markdown 二次发布仅限个人研究，引用请回原链接

详见 [SCRAPE_REPORT.md](./SCRAPE_REPORT.md)。