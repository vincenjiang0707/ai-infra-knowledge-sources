# [Issue #1570] [CI/CD] OCP nightlies fail with "Pods did not become ready within 30m"

source: https://github.com/llm-d/llm-d/issues/1570
state: closed | updated: 2026-09-24T01:19:53Z
labels: help wanted, CI/CD, lifecycle/rotten, release/v0.8

## 正文

Intermittent across `wva-ocp`, `tiered-prefix-cache-cpu-offloading-ocp`, `precise-prefix-cache-ocp`, `optimized-baseline-ocp`. Same guides pass on CKS. Pod state on timeout is not currently captured to workflow artifacts, so root cause is opaque.

Tracked in #1565.


## 评论 (2)

### sudoalok · 2026-05-25

Raised a fix in llm-d-infra for the missing diagnostics:
https://github.com/llm-d/llm-d-infra/pull/173

### github-actions[bot] · 2026-08-24

This issue is marked as stale after 90d of inactivity. After an additional 30d of inactivity (15d to become rotten, then 15d more), it will be closed. To prevent this issue from being closed, add a comment or remove the `lifecycle/stale` label.
