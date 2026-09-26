# [Issue #4237] Nightly build/test failure - 2026-09-19

source: https://github.com/kvcache-ai/Mooncake/issues/4237
state: open | updated: 2026-09-20T00:42:32Z
labels: nightly-failure

## 正文

## Nightly Failure Report

**Run**: https://github.com/kvcache-ai/Mooncake/actions/runs/35366974546
**Branch**: refs/heads/main
**Timestamp**: 2026-09-19T16:10:48.363Z

Please investigate the failed jobs in the workflow run linked above.

## 评论 (1)

### he-yufeng · 2026-09-20

Tonight's reds are runner-side, not code: both failing lanes die before the build at `Failed to update package lists` / `Failed to install system packages` (16:14Z, both within ~30s of the apt step), and the tone-sglang lane only gets as far as retrying artifact downloads. That is apt/network flake on the runners, different from #4227's three lanes (FilereadWorkerPoolTest flake tracked in #4213 with fix in #4210, and the 8080 HTTP metadata bind in the Go sanitizer job).

Nothing in the diff range is implicated — a rerun should go green, and the two real issues from #4227 still stand on their own (the Fileread flake waits on #4210; the 8080 bind is worth a per-run unique port if it recurs).
