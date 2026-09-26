# [Issue #5001] [Bug][v0.6.18] test_sparse_mla_sm120 timeout on Spark

source: https://github.com/flashinfer-ai/flashinfer/issues/5001
state: closed | updated: 2026-09-21T04:31:32Z
labels: needs-triage, ci: health

## 正文

## Summary
FlashInfer main (6c14bbd5) CI reports a test error affecting 1 saved failure occurrence(s) across 1 affected test(s). The saved evidence covers Spark / cu129 in flashinfer-ci.

## CI environment

- Commit: 6c14bbd5
- Branch: main
- Pipeline: [#66471033](https://nv/flashinfer-ci/-/pipelines/66471033)
- Affected scope: 1 saved failure occurrence(s) across 1 affected test(s)
- Affected tests:
  - tests/attention/test_sparse_mla_sm120.py
- Failed jobs:
  - [unit_test_spark: [cu129]](https://nv/flashinfer-ci/-/jobs/427851027)

## Failure

```text
Timeout test files:
  - tests/attention/test_sparse_mla_sm120.py (488 timeout nodes)
```

## Reproduction

```bash
pytest 'tests/attention/test_sparse_mla_sm120.py'
```

Generated from CI test identity; not independently verified.

## Case History
- 2 confirmed failure pipeline(s); first seen 2026-09-04, last seen 2026-09-06.
- 2026-09-06 — (6c14bbd5) — Spark / cu129 — [pipeline #66471033](https://nv/flashinfer-ci/-/pipelines/66471033) / [job](https://nv/flashinfer-ci/-/jobs/427851027)
- 2026-09-04 — (25344422) — Spark / cu129 — [pipeline #66202435](https://nv/flashinfer-ci/-/pipelines/66202435) / [job](https://nv/flashinfer-ci/-/jobs/425565930)



## 评论 (2)

### Champollion9012 · 2026-09-08

This suite does not time out on **discrete SM120**. At this issue's own commit:

```
GPU     NVIDIA RTX PRO 6000 Blackwell Server Edition, cc 12.0, driver 590.48.01
CUDA    13.1, torch 2.13.0+cu130
repo    6c14bbd5, submodules at their pinned revisions

pytest tests/attention/test_sparse_mla_sm120.py
  -> 488 passed in 14.30s
```

Same 488 nodes the report lists as timeouts, finishing in about fourteen seconds. The sibling
accuracy failure in #4999 also passes here; I have posted the details there, including the reason an
SM120-named suite is reporting from Spark: the file gates on `is_sm12x_supported`, i.e. the family, so
`is_sm120a` and `is_sm121a` are both admitted (on this card `is_sm120a=True`, `is_sm121a=False`), and
the narrower predicates already exist in `flashinfer.utils`.

As with #4999, this does not tell you whether the Spark side is a genuine SM121 defect or a runner
artifact — I have no Spark. It only rules out sm_120 as the cause.

One note on overlap: this is cross-referenced from #5015, where @200lz has taken the
reproduce-and-fix work on the padded CUDA-graph replay hang. If the timeout here is that hang, this
14.30 s clean run is theirs to use — I am offering the datapoint, not the issue. Happy to run
anything specific on discrete sm_120 that would help either thread.


### bkryu · 2026-09-09

Thanks @Champollion9012, the issue in fact manifests on Spark due to Spark having a small number of SMs. Please see #5048 with the fix.
