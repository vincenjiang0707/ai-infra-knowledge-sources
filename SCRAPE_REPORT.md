# 推理调优知识库抓取报告

## 1. 目标与背景

`推理调优知识.pdf` 列出 170 个公网来源入口（11 类、385 个独立 URL），覆盖 vLLM/SGLang/TensorRT-LLM 等推理引擎、HuggingFace 模型、博客与论文。目标是把这 170 个入口的原始载体（README、Issue、PR、Release、博客文章、文档页）抓下来落到本地，建立可检索的知识原料层。

## 2. 最终成果

| 指标 | 数值 |
|---|---|
| 来源总数 | 170 |
| 抓取成功 | 164 |
| 部分成功 | 1（SRC-043 寒武纪：GitHub org 成功，论坛真 504） |
| 待人工（blocked）| 5（PDF 预标，未发请求）|
| 未抓取 | 0 |
| 产物文件 | 3585 项 / 155.4 MB |

## 3. 数据流

```
推理调优知识.pdf
  │ pypdf 注释(494) + pdfminer 行坐标反推 SRC-XXX 编号
  ▼
_registry.json （一次性，170 SRC × 频道映射）
  │
  │ scrape.py 调度（2 路并发，简单先跑）
  ▼
knowledge-sources/SRC-XXX/
  ├─ _meta.json               状态/游标/渠道结果
  ├─ github_*.{md,jsonl}      ├ feed_meta.json + posts/*.md
  │                            ├ pages/*.md
  │                            └ hf.md
  └─ github_details/          每条活跃 issue/PR 一文件
                                含正文 + 会话评论 + PR reviews
  ▼
summary_gen.py → _summary/{index,fetched,partial,not_fetched,blocked}.md
```

## 4. 频道分发策略

`scrapers/site.py` 是路由器，按 URL 特征分发到不同抓取路径：

| 入口特征 | 路径 | 产出 |
|---|---|---|
| `github.com/{owner}/{repo}` | github.py | repo.md + top-100 issues/pulls + 全部 releases + 聚合 changelog |
| `.txt`/`.md` 结尾（llms.txt）| 原文直存 | page.md |
| 含 RSS/Atom（`<link rel=alternate>` + 6 路径探测）| feedparser + 逐帖 trafilatura | feed_meta.json + posts/*.md（≤500 帖） |
| docs 类站（docs.* / /docs 等）| sitemap 探测 → 多候选 + 单页兜底 | pages/*.md（≤2000 页） |
| 其余普通页 | trafilatura 单页提取 | page.md |
| `huggingface.co/{org}` | HF REST：org overview → models?author= | hf.md |
| `huggingface.co/models·blog·papers` | 转 site 路径 | 同上 |
| PDF 预标 5 项 blocked | 不发请求直接落 blocked | 无 |

## 5. GitHub 三层抓取

### 第一层：列表快照

- 一次 API 调用拿 100 条元数据，含 body 正文（0 额外调用）
- issues：top-100 by updated_at，filter 掉 `pull_request` 字段
- pulls：top-100 by updated_at，独立端点（拉取的数据没有 comments_count 字段）
- releases：全部（body 全文保留）
- changelog：探测 4 个文件名（CHANGELOG/CHANGES/HISTORY/NEWS），缺则聚合 releases.body

### 第二层：详情抓取（活跃条目）

筛选规则：

- issue：comments_count > 0 且 updated_at 近 90 天（约 2573 条）
- PR：updated_at 近 90 天（约 4424 条，因为 pulls 端点不含 comments_count 字段）
- 每条调用 `issues/{n}/comments`，PR 额外调用 `pulls/{n}/reviews`
- 输出 `github_details/{issue|pr}_{number}.md` + `_index.jsonl`

### 第三层：增量与刷新

```
增量列表  incremental_gh.py
          拉 updated 倒序 ≤5 页 → 新号 append、旧号数据原地刷新 → cursor.last_updated_at 推进
          多仓 SRC 走 ≤3 页/仓全量合并

详情刷新  detail_fetcher.py 索引 _index.jsonl 行含 fetched_at
          jsonl updated_at > fetched_at → 重抓
          legacy 行（无 fetched_at）→ 重抓一次（补 reviews）
          其余跳过
```

## 6. 状态机

```
SRC 状态由渠道状态聚合：
  全部 ok              → success
  部分 ok 部分 error    → partial
  全部 blocked         → blocked
  全部 transient       → not_fetched

渠道级状态：ok / error / blocked(401·403·404) / partial

增量跳过的规则：
  success               → 跳过
  partial               → 不跳，全渠道重跑（error 渠道补）
  blocked / not_fetched → 跳过，除非 --retry-blocked
```

## 7. 工具栈与决策

| 工具 | 角色 | 实测表现 |
|---|---|---|
| gh CLI | GitHub API（5000/h）| 主仓用，已 auth |
| curl + trafilatura | 静态站主方案 | 0.5-1.3s 抓 + 0.04s 抽取，blog post 实测 16k chars / 单帖 |
| feedparser | RSS / Atom 解析 | 11 feed 实测均可 |
| WebFetch | 弃用 | JS 站 hang/timeout，静态比 trafilatura 慢 |
| kimi-webbridge | 弃用 | 需用户真实浏览器 session，不适合批量 |
| baoyu-url-to-md | 弃用 | WSL2 + --no-sandbox 调通复杂 |
| playwright-cli | 未用 | 预留兜底（4 个 JS 渲染站暂未启用） |
| huggingface_hub | 用 REST API | 无需装包 |

## 8. 性能与成本

```
Phase 1  POC（3 个样本）          ~2 min
Phase 2  GH 80 仓                ~30 min（50-80s/仓）
Phase 3  RSS 11 feed              ~5 min
Phase 4  HF 11 模型               ~3 min
Phase 5  Sitemap 10 站           ~25 min（vLLM docs 2723 URL 单独 ~5 min）
Phase 6  body 回填 + 增量       ~10 min
Phase 7  detail 抓取             进行中
─────────────────────────────────────────
总计  ~2h
磁盘  ~170 MB
gh 调用  ~7-10k（含重抓）
```

## 9. 已发现并修复的关键缺陷

```
1. registry 分类  github.com/topics/* 误分类为仓库
   修复  改 reference 类型

2. sitemap 探测  只试单路径，子路径站 404 误判 blocked
   修复  多候选（url 根 + origin 根 + index 变体）+ llms.txt + 单页兜底

3. site.run 覆盖  无条件 meta_channels[ch_key]=out 把 sitemap 成功结果抹掉
   修复  handled 即 return，不走末尾赋值

4. PR 58256/58267 类时间窗滞后  抓取快照后新开 issue/PR 不在 jsonl
   修复  incremental_gh.py 拉前 5 页 append + refresh + 推进 cursor

5. PR 58269 评论竞态 + review 缺失  抓取后评论晚 1 分钟才出现，且
   review 走独立端点 pulls/{n}/reviews（旧逻辑只抓会话评论）
   修复  fetched_at 索引刷新规则 + 加 reviews 端点 + legacy 行一次补抓
```

## 10. 已知边界与待办

```
未抓边界：
  - JS 渲染站 4 个（lmsys / baseten / fireworks / anyscale）→ playwright 通道未启用
  - sitemap 未列的菜单子页（fallback 爬内链未实现）
  - diff/文件级变更（pulls/{n}/files）→ 量太大不抓
  - 跨源去重 / 知识卡生成 → out of scope

待办：
  - detail_fetcher.py 全量重抓收尾
  - tasks 6.7 增量游标最终验收
  - 脚本入仓与 archive change
```

## 11. 关键脚本入口

```
scrape/scrape.py                主入口，调度 SRC 渠道
scrape/scrapers/
  ├── github.py                GH 仓库三层抓取
  ├── site.py                  路由器：RSS / sitemap / 单页 / llms.txt
  ├── sitemap.py               sitemap 解析 + 递归抓
  ├── hf.py                    HF REST API
  └── common.py                meta io、HTTP、trafilatura
scrape/incremental_gh.py       GH 列表增量 append + refresh
scrape/detail_fetcher.py       评论 + reviews 详情抓取
scrape/backfill_bodies.py      body 回填（历史缺失字段补全）
scrape/summary_gen.py          生成 _summary/ 5 个 md
```

## 12. 复盘要点

- **PDF 是图像型表格**，SRC 编号在注释里不在文本流里；通过 `pypdf` 提取 `/Annots/.../A/URI` + `pdfminer` 取行坐标，按 y-overlap 把 URL 反推到对应 SRC（替代简单 y-segment 切分，避免 11 个 URL 漏归位）
- **增量游标是 PRD 中要求「确认 cursor 生效」的硬指标**，缺失时 PR 58256/58267 类新开条目永久丢失
- **reviews 与会话评论在 GitHub 是两个端点**，原始演示中合并了导致 PR 58269 漏掉 claude[bot] 的 review
- **sitemap 的去重** 完全靠 URL 字符串 md5；vLLM docs 有 ~50 个 `/api/*` 与 `/en/latest/api/*` 别名 URL 同 slug 文件会被覆盖（无害但有重复抓）