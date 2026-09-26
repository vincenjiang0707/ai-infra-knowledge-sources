#!/usr/bin/env bash
# Publish chaoyuan/knowledge-sources/ to github.com/vincenjiang0707/ai-infra-knowledge-sources
#
# Usage:
#   bash publish_to_github.sh                # 正常：init + commit + push
#   bash publish_to_github.sh --dry-run     # 只生成 .gitignore + README + 看 git status
#   bash publish_to_github.sh --skip-push   # commit 但不 push
#
# Assumes:
#   - ssh key / gh auth configured for vincenjiang0707
#   - target repo already created on github (empty)
#
# Idempotent: re-running on an existing clone only adds new commits.

set -euo pipefail

SRC_DIR="/mnt/d/vincenjiang/AI学习/chaoyuan/knowledge-sources"
REMOTE="git@github.com:vincenjiang0707/ai-infra-knowledge-sources.git"
BRANCH="main"
GITIGNORE="${SRC_DIR}/.gitignore"
README="${SRC_DIR}/README.md"

DRY_RUN=0
SKIP_PUSH=0
for a in "$@"; do
  case "$a" in
    --dry-run) DRY_RUN=1 ;;
    --skip-push) SKIP_PUSH=1 ;;
    *) echo "unknown arg: $a"; exit 2 ;;
  esac
done

# 1. write .gitignore — only exclude transient/lock files
cat > "$GITIGNORE" <<'EOF'
# transient scrape state
*.tmp
*.swp
.DS_Store
EOF

# 2. write README — provenance disclaimer is required (raw public web content).
# README content is the canonical one on first commit; subsequent runs overwrite
# with placeholders so manual edits don't get clobbered.
SNAPSHOT_DATE=$(date -u +%Y-%m-%d)
SRC_COUNT=$(find "$SRC_DIR" -maxdepth 1 -type d -name 'SRC-*' | wc -l)
FILE_COUNT=$(find "$SRC_DIR" -type f | wc -l)
TOTAL_SIZE=$(du -sh "$SRC_DIR" 2>/dev/null | cut -f1)

# if README already exists with a Changelog section, preserve it
PREV_CHANGELOG=""
if [[ -f "$README" ]] && grep -q '^## Changelog' "$README"; then
  PREV_CHANGELOG=$(awk '/^## Changelog/{flag=1; next} /^## /{if(flag) exit; next} flag' "$README")
fi

cat > "$README" <<EOF
# AI Infra Knowledge Sources

> 抓取自公网公开内容（PDF 列出的 170 个推理调优相关来源）的本地知识原料。
> 仅供个人学习研究使用；内容版权归原作者所有，引用请回原链接。

## 快照信息

| 项 | 值 |
|---|---|
| 抓取快照日期 | ${SNAPSHOT_DATE} |
| 来源数 | ${SRC_COUNT} |
| 文件总数 | ${FILE_COUNT} |
| 总体积 | ${TOTAL_SIZE} |

## 按抓取类型分组

| 类型 | 数量 | 典型产物 | 抽样 SRC |
|---|---|---|---|
| github_repo | 80 | _meta + github_*.{jsonl,md} + github_details/ | SRC-003 vLLM, SRC-005 SGLang |
| site（sitemap 文档站）| 12 | pages/*.md (≤2000 页/SRC) | SRC-001 vLLM docs, SRC-040 MUSA |
| site（RSS 博客）| 12 | feed_meta.json + posts/*.md | SRC-165 vLLM blog, SRC-140 Lei Mao |
| site（菜单 BFS 兜底）| 4 | pages/*.md (深度3、≤200 页) | SRC-040 MUSA（Docusaurus 走 BFS）|
| hf（HF 模型/组织）| 8 | hf.md | SRC-018 deepseek-ai |
| academic | 5 | page.md | SRC-067 arxiv vLLM |
| forum/国产社区 | 9 | 多数 blocked | SRC-043 寒武纪 |
| reference | ~40 | 仅 registry 索引 | github.com/topics/* |
| blocked | 5 | 无产物 | 见 _summary/blocked.md |

## 目录结构

\`\`\`
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
        ├── github_details/         活跃 issue/PR 的评论 + reviews
        ├── feed_meta.json          RSS feed 元信息
        ├── posts/                  RSS 全文章节
        ├── pages/                  站点文档页
        └── hf.md                   HF 模型/组织概览
\`\`\`

## 快速检索

- 按 SRC 号：直接看目录 SRC-XXX/，_meta.json 含 URL 与状态
- 按类别：用 _registry.json，170 条全字段
- 找活跃 GH issue/PR：看 SRC-XXX/github_details/_index.jsonl
- 找 RSS 文章：看 SRC-XXX/posts/，文件名 YYYYMMDD_slug.md
- 汇总报告：_summary/index.md 列所有 170 项状态

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

抓取脚本（scrape/incremental_gh.py / detail_fetcher.py / summary_gen.py）未在本仓发布；如需更新快照请回 chaoyuan 主仓运行。

抓取脚本行为：增量 + 详情抓取都是幂等设计，跳过已抓且未过期条目，不会重抓全量。

## Changelog

${PREV_CHANGELOG:-新增 v1.0 快照。}

| v1.2 | 2026-09-23 | SRC-XXX 移入 sources/ 子目录 |

## 已知边界

- 抓 top-N + 90 天窗口：新开或长期未活动条目不在首次抓取范围
- GitHub 排序按 updated_at desc：与网页默认一致；人工置顶老条目可能漏
- JS 渲染站（4 个）：playwright 通道未启用
- sitemap.xml 缺失站点：menu BFS fallback（深度3、≤200 页）
- 多仓 SRC：增量时合并刷新（每仓 ≤3 页）
- 详情抓取中 PR reviews 与 comments 是两个端点：缺一会漏 claude[bot] 类
- 公网版权：raw HTML→markdown 二次发布仅限个人研究

详见 [SCRAPE_REPORT.md](./SCRAPE_REPORT.md)。
EOF

if [[ "$DRY_RUN" == 1 ]]; then
  echo "[dry-run] wrote .gitignore + README.md"
  echo "[dry-run] cd $SRC_DIR && git status would show:"
  cd "$SRC_DIR" && git status --short 2>/dev/null || echo "  (no git repo yet)"
  exit 0
fi

# 3. git init / fetch
cd "$SRC_DIR"
if [[ ! -d .git ]]; then
  git init -b "$BRANCH"
  git remote add origin "$REMOTE"
else
  # ensure correct remote + branch
  if ! git remote get-url origin >/dev/null 2>&1; then
    git remote add origin "$REMOTE"
  fi
  current_remote=$(git remote get-url origin)
  if [[ "$current_remote" != "$REMOTE" ]]; then
    echo "remote origin = $current_remote, expected $REMOTE"
    exit 1
  fi
fi

# 4. git identity (set local-only; user may have global)
if ! git config user.email >/dev/null; then
  git config user.email "vincenjiang0707@users.noreply.github.com"
  git config user.name "vincenjiang"
fi

# 5. add + commit
git add .gitignore README.md _registry.json _summary/ SCRAPE_REPORT.md

# git pathspec has trouble with Chinese path + glob; use find to enumerate
git add $(find . -maxdepth 3 -name '_meta.json' -path './sources/SRC-*' | sort)
git add $(find . -maxdepth 3 -name 'github_repo.md' -path './sources/SRC-*' | sort)
git add $(find . -maxdepth 3 -name 'github_*.jsonl' -path './sources/SRC-*' | sort)
git add $(find . -maxdepth 3 -name 'github_changelog.md' -path './sources/SRC-*' | sort)
git add $(find . -maxdepth 3 -name 'github_details' -type d -path './sources/SRC-*' | sort)
git add $(find . -maxdepth 3 -name 'feed_meta.json' -path './sources/SRC-*' | sort)
git add $(find . -maxdepth 3 -name 'posts' -type d -path './sources/SRC-*' | sort)
git add $(find . -maxdepth 3 -name 'pages' -type d -path './sources/SRC-*' | sort)
git add $(find . -maxdepth 3 -name 'hf.md' -path './sources/SRC-*' | sort)
git add $(find . -maxdepth 3 -name 'page.md' -path './sources/SRC-*' | sort)

# stage anything else (channel-specific outputs we missed)
git add -A 'sources/' 2>/dev/null || true

# exclude ignored files from stage (just in case; ignore failures on first init)
git rm --cached --ignore-unmatch -- .DS_Store 2>/dev/null || true
git rm --cached --ignore-unmatch -- '**/.DS_Store' 2>/dev/null || true

if git diff --cached --quiet; then
  echo "no changes to commit"
  exit 0
fi

git commit -m "feat: 推理调优知识库首批 ${SRC_COUNT} SRC 抓取快照 (${SNAPSHOT_DATE})

- 170 个公网来源入口（11 类）
- 抓取产物：jsonl + md + feed/posts/pages
- 汇总报告：_summary/{index,fetched,partial,not_fetched,blocked}.md
- 抓取逻辑详见 SCRAPE_REPORT.md"

echo "committed."

# 6. push
if [[ "$SKIP_PUSH" == 0 ]]; then
  git push -u origin "$BRANCH"
  echo "pushed to $REMOTE ($BRANCH)"
else
  echo "skipped push (--skip-push)"
fi