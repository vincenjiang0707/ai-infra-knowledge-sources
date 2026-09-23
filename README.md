# AI Infra Knowledge Sources

> 抓取自公网公开内容（PDF 列出的 170 个推理调优相关来源）的本地知识原料。
> 仅供个人学习研究使用；内容版权归原作者所有，引用请回原链接。

## 快照信息

| 项 | 值 |
|---|---|
| 抓取快照日期 | 2026-09-23 |
| 来源数 | 165 |
| 文件总数 | 5063 |
| 总体积 | 210M |

## 目录结构

```
.
├── README.md
├── SCRAPE_REPORT.md            抓取逻辑、状态机、性能与已知边界
├── _registry.json              SRC 元数据（170 项 × channel 映射）
├── _summary/                   汇总报告（index / fetched / partial / not_fetched / blocked）
└── SRC-XXX/
    ├── _meta.json              状态/游标/渠道结果
    ├── github_repo.md          仓库 README
    ├── github_issues.jsonl     top-100 issues (updated_at desc)
    ├── github_pulls.jsonl      top-100 PRs (updated_at desc)
    ├── github_releases.jsonl   全部 releases
    ├── github_changelog.md     聚合 CHANGELOG
    ├── github_details/         活跃 issue/PR 的评论 + reviews
    ├── feed_meta.json          RSS feed 元信息（RSS 源）
    ├── posts/                  RSS 全文章节（RSS 源）
    ├── pages/                  站点文档页（sitemap / menu BFS 抓的）
    └── hf.md                   HF 模型/组织概览（HF 源）
```

## 数据来源分类

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
- 精选作者

## 更新方式

```bash
# 增量刷新 GH 列表（5 页窗口，按 updated_at 倒序）
python3 scrape/incremental_gh.py

# 重抓活跃条目的评论 + reviews（filter: comments_count > 0 && updated_at < 90d）
python3 scrape/detail_fetcher.py

# 重新生成汇总报告
python3 scrape/summary_gen.py
```

## 已知边界

- 详情抓取是 top-N + 90 天窗口设计，新开/长期未活动的 issue 不会被抓
- JS 渲染站（4 个）暂未启用 playwright
- sitemap.xml 缺失站点会走 menu BFS fallback（深度3、每 SRC ≤200 页）
- 增量游标推进依赖 GH API updated_at，可能漏掉被人工置顶但 updated_at 老的条目

详见 [SCRAPE_REPORT.md](./SCRAPE_REPORT.md)。
