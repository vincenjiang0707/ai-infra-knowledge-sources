# [Issue #4498] [Bug][v0.6.18] test_collection_isolates_sm90_pull_multirank_modules failed on Spark E   AssertionError: assert ['pytest-of-u...y::test_sm90'] == ['test_aaa_sm...y::test_sm90']

source: https://github.com/flashinfer-ai/flashinfer/issues/4498
state: closed | updated: 2026-09-26T14:20:34Z
labels: needs-triage, ci: health

## 正文

## Summary
FlashInfer 0.6.18 (`06597125`) CI reports a test assertion affecting 2 saved failure occurrence(s) across 1 affected test(s). The saved evidence covers Spark / cu130, Spark / cu129 in flashinfer-ci.

## CI environment

- Version / commit: 0.6.18 / `06597125`
- Pipeline:
  - Pipeline: [pipeline](https://nv/flashinfer-ci/-/pipelines/62301362)
- Affected scope: 2 saved failure occurrence(s) across 1 affected test(s)
- Affected tests:
  - `tests.test_sharding.test_runner_cli::test_collection_isolates_sm90_pull_multirank_modules`
- Failed jobs:
  - [unit_test_spark: [cu130]](https://nv/flashinfer-ci/-/jobs/394169955) — `unit_test_spark / Spark / cu130`
  - [unit_test_spark: [cu129]](https://nv/flashinfer-ci/-/jobs/394169915) — `unit_test_spark / Spark / cu129`

## Failure

```text
AssertionError: assert ['pytest-of-u...y::test_sm90'] == ['test_aaa_sm...y::test_sm90']      At index 0 diff: 'pytest-of-unknown/pytest-1/test_collection_isolates_sm90_0/suite/test_aaa_sm100.py::test_sm100' != 'test_aaa_sm100.py::test_sm100'   Use -v to get more diff
```

## Reproduction

```bash
pytest 'tests/test_sharding/test_runner_cli.py::test_collection_isolates_sm90_pull_multirank_modules'
```

Generated from CI test identity; not independently verified.

## Case History
- 1 confirmed failure pipeline(s); first seen 2026-08-13, last seen 2026-08-13.
- 2026-08-13 — 0.6.18 (06597125) — `Spark` / `cu129, cu130` — [pipeline #62301362](https://nv/flashinfer-ci/-/pipelines/62301362) / [job](https://nv/flashinfer-ci/-/jobs/394169915)



## 评论 (1)

### nvamyt · 2026-09-26

Verified via FlashInfer CI: `test_collection_isolates_sm90_pull_multirank_modules` no longer appears in the failure list of the last 5 pipeline(s): 69776365 (2026-09-25), 69628264 (2026-09-24), 69428841 (2026-09-23), 69216098 (2026-09-22), 69123755 (2026-09-22). Closing.
