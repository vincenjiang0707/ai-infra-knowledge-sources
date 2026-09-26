# [Issue #4652] [Bug][v0.6.18][b300|gb200] test_mm_bf16_fp4_reference_correctness  ValueError: too many values to unpack (expected 2)

source: https://github.com/flashinfer-ai/flashinfer/issues/4652
state: closed | updated: 2026-09-21T04:31:08Z
labels: needs-triage, ci: health

## 正文

## Summary
FlashInfer 0.6.18 (ad8bb37b) CI reports a test assertion affecting 8 saved failure occurrence(s) across 2 affected test(s). The saved evidence covers B300 / cu130, B300 / cu129, GB200 / cu130, GB200 / cu129 in flashinfer-ci.

## CI environment

- Commit: ad8bb37b
- Branch: main
- Pipeline: [#63648836](https://nv/flashinfer-ci/-/pipelines/63648836)
- Affected scope: 8 saved failure occurrence(s) across 2 affected test(s)
- Affected tests:
  - tests.trace.test_mm_bf16_fp4_reference_correctness::test_mm_bf16_fp4_reference_correctness[shape_kwargs1-cute-dsl]
  - tests.trace.test_mm_bf16_fp4_reference_correctness::test_mm_bf16_fp4_reference_correctness[shape_kwargs0-cute-dsl]
- Failed jobs:
  - [unit_test_b300: [cu130]](https://nv/flashinfer-ci/-/jobs/404810626)
  - [unit_test_b300: [cu129]](https://nv/flashinfer-ci/-/jobs/404810594)
  - [unit_test_gb200: [cu130]](https://nv/flashinfer-ci/-/jobs/404810511)
  - [unit_test_gb200: [cu129]](https://nv/flashinfer-ci/-/jobs/404810498)

## Failure

```text
ValueError: too many values to unpack (expected 2)
```

## Reproduction

```bash
pytest 'tests/trace/test_mm_bf16_fp4_reference_correctness.py'
```

Generated from the affected CI test file identity; not independently verified.
### Likely root cause
https://github.com/flashinfer-ai/flashinfer/pull/4466

### Fix PR
https://github.com/flashinfer-ai/flashinfer/pull/4620 May fix.
## Case History
- 4 confirmed failure pipeline(s); first seen 2026-08-18, last seen 2026-08-20.
- 2026-08-20 — 0.6.18 (ad8bb37b) — B300, GB200 / cu129, cu130 — [pipeline #63648836](https://nv/flashinfer-ci/-/pipelines/63648836) / [job](https://nv/flashinfer-ci/-/jobs/404810498)
- 2026-08-19 — 0.6.18 (d90c6f18) — B300, GB200, GB300 / cu129, cu130 — [pipeline #63457917](https://nv/flashinfer-ci/-/pipelines/63457917) / [job](https://nv/flashinfer-ci/-/jobs/403249426)
- 2026-08-19 — 0.6.18rc4 (87ba7ff1) — B300, GB200, GB300 / cu129, cu130 — [pipeline #63405311](https://nv/flashinfer-ci/-/pipelines/63405311) / [job](https://nv/flashinfer-ci/-/jobs/402816208)
- 2026-08-18 — 0.6.18 (27a5a294) — B300, GB200, GB300 / cu129, cu130 — [pipeline #63265553](https://nv/flashinfer-ci/-/pipelines/63265553) / [job](https://nv/flashinfer-ci/-/jobs/401713624)



## 评论 (1)

### jimmyzho · 2026-09-08

https://github.com/flashinfer-ai/flashinfer/pull/4620 Fixed
