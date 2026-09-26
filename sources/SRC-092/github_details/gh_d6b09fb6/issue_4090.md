# [Issue #4090] Nightly build/test failure - 2026-09-13

source: https://github.com/kvcache-ai/Mooncake/issues/4090
state: open | updated: 2026-09-13T16:45:20Z
labels: nightly-failure

## 正文

## Nightly Failure Report

**Run**: https://github.com/kvcache-ai/Mooncake/actions/runs/34704452077
**Branch**: refs/heads/main
**Timestamp**: 2026-09-13T16:11:12.774Z

Please investigate the failed jobs in the workflow run linked above.

## 评论 (1)

### he-yufeng · 2026-09-13

Root cause: the TestPyPI project has hit its size cap, not a package or runner problem.

Evidence chain:

- The upload reaches 100% (78.7 MB bar completes) and only then gets a bare `400 Bad Request` from `test.pypi.org/legacy` — the server rejects when accounting the new total, not while receiving bytes. The package itself is unchanged night over night.
- The project `mooncake-transfer-engine` on TestPyPI now holds **24 releases, 131 files, ~10.67 GB** (queried from the TestPyPI JSON API). The largest recent nightlies are ~700-720 MB each.
- The failure onset lines up exactly with crossing the ~10 GB default project limit: `0.3.14.dev20260910` (722 MB) is the newest version on TestPyPI; every nightly since (`dev20260911`, `dev20260912`, plus the rerun) has failed with the identical 400. Same signature every time, so it is deterministic, not a transient TestPyPI rejection.

What will not help: re-running the workflow (already failed identically), `--skip-existing` (it is in place and irrelevant — no new file is registered at all).

What will help, in order of effort:

1. **Prune old nightly releases on TestPyPI.** Deleting a handful of the oldest `0.3.x.dev*` versions frees several GB immediately. This needs project-owner credentials on TestPyPI.
2. **Ask PyPI support for a project size-limit increase** on the TestPyPI project if nightlies should keep long retention.
3. **Add an age-based pruning step to `publish-testpypi`** (delete `0.3.*.dev*` releases older than N days before upload), so the cap stops being a recurring midnight failure.

Happy to draft the pruning step for `nightly.yml` if the direction sounds right.

Same root cause as #4069 — that issue can be closed as a duplicate of this analysis.

