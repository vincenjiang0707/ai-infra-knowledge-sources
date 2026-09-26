# [Issue #2611] CI: build-flags job appears to hit runner disk/network instability across recent PRs

source: https://github.com/kvcache-ai/Mooncake/issues/2611
state: open | updated: 2026-09-24T03:17:10Z
labels: stale

## 正文

### Summary

Recent `Build & Test (Linux)` workflow runs appear to be failing for CI infrastructure reasons rather than PR-specific code failures.

In PR #2601, the latest failure is in `build-flags (3.10)` and the log shows the GitHub-hosted runner running out of disk space while linking a store test executable:

```text
[356/424] Linking CXX executable mooncake-store/tests/master_metrics_test
FAILED: [code=1] mooncake-store/tests/master_metrics_test
##[error]No space left on device : '/home/runner/actions-runner/cached/2.335.1/_diag/pages/...log'
```

The PR itself only touches EP buffer validation files:

```text
mooncake-ep/src/ep_py.cpp
mooncake-ep/src/mooncake_ep_buffer.cpp
mooncake-wheel/mooncake/mooncake_ep_buffer.py
```

So this failure does not look directly related to the PR changes.

### Related observations

I also noticed similar CI instability on recent runs from other PRs / main-branch workflow runs. Several recent `Build & Test (Linux)` runs were failing, queued, or stuck in progress around the same period.

The previous run of PR #2601 also failed for infrastructure-looking reasons, including `sccache` / GitHub Actions cache DNS failures and GitHub fetch/network errors, for example:

```text
sccache: error: Server startup failed: cache storage failed to read: Unexpected (temporary) at read => send http request
error sending request ... dns error: failed to lookup address information: Try again
fatal: unable to access 'https://github.com/...': Failed to connect to github.com port 443
```

### Possible cause

The `build-flags` job seems especially heavy. It builds multiple configurations in the same runner, including transfer engine, full project builds, Rust bindings, EP variants, TENT, nvlink allocator, and wheel artifacts.

The run logs also show the root filesystem becoming increasingly full during the job, while `/mnt` still has much more free space available. This suggests the job may need either more aggressive cleanup or to place large build/cache directories under `/mnt`.

### Suggested checks

Could maintainers please take a look at the CI environment for this workflow?

Some possible mitigations:

- Split `build-flags` into smaller jobs or separate matrix stages.
- Clean intermediate build directories before the next large build phase.
- Move large build/cache directories to `/mnt` on GitHub-hosted runners.
- Add `df -h` / `du -sh` diagnostics after each major build phase.
- Consider disabling or isolating `sccache` when the Actions cache backend is unstable.

This would help distinguish real PR failures from runner resource/network failures and should reduce noise for recent contributors.

## 评论 (3)

### github-actions[bot] · 2026-06-25

Thanks for opening this issue, @VectorPeak!

| Field | Value |
|-------|-------|
| **Issue** | #2611 |
| **GitHub user ID** | `73048950` |
| **Reporter** | @VectorPeak |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### ykwd · 2026-06-25

This issue has been a long-standing pain point. We started running into it a long time ago and have already gone through many rounds of optimization. If anyone in the community has a good solution, PRs are very welcome.


### github-actions[bot] · 2026-09-24

This issue has had no activity for 90 days and will be closed in 7 days if there is no further activity. Please comment or react if it should stay open.
