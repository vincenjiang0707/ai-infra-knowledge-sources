# [Issue #4069] Nightly build/test failure - 2026-09-12

source: https://github.com/kvcache-ai/Mooncake/issues/4069
state: open | updated: 2026-09-13T00:18:28Z
labels: nightly-failure

## 正文

## Nightly Failure Report

**Run**: https://github.com/kvcache-ai/Mooncake/actions/runs/34620633139
**Branch**: refs/heads/main
**Timestamp**: 2026-09-12T16:11:14.165Z

Please investigate the failed jobs in the workflow run linked above.

## 评论 (1)

### he-yufeng · 2026-09-13

Broke the three failures down against last night's run:

- `publish-testpypi`: first occurrence. The wheel uploads to 100% and TestPyPI answers 400 after the body, with `--skip-existing` already in place, so this is not the usual "file already exists" case. One-off TestPyPI-side rejection is the most likely read; if tonight's run 400s the same way, the nightly version stamp's metadata is the next suspect.
- `tone-sglang-integration / test-sglang-integration`: second night in a row, and it fails before any test runs — the job cannot fetch the Build & Test artifact for the SHA ("Failed to fetch artifacts for workflow run ... after $max_attempts attempts"). Recurring, so this is a real breakage in the artifact handoff, not a flake; worth a look at whatever changed in the upstream run naming/retention.
- `build-musa` (09-11 only, gone tonight): transient.

No code regression in either night that I can see from the logs.

