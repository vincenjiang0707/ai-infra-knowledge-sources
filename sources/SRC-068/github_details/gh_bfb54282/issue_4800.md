# [Issue #4800] [Bug][v0.6.18rc10] test_trtllm_gen_attention_prefill AssertionError: Tensor-likes are not close!  Mismatched elements: 4007 / 541663232 (0.0%) Greatest absolute difference: 96.5625 at index (3626, 2, 79) (up to 0.1 allowed)

source: https://github.com/flashinfer-ai/flashinfer/issues/4800
state: closed | updated: 2026-09-21T04:31:15Z
labels: needs-triage, ci: health

## 正文

## Summary
FlashInfer 0.6.18rc10 (e62941a1) CI reports a test assertion affecting 1 saved failure occurrence(s) across 1 affected test(s). The saved evidence covers GB300 / cu129 in flashinfer-ci.

## CI environment

- Commit: e62941a1
- Branch: release-v0.6.18
- Pipeline: [#64977547](https://nv/flashinfer-ci/-/pipelines/64977547)
- Affected scope: 1 saved failure occurrence(s) across 1 affected test(s)
- Affected tests:
  - tests.attention.test_trtllm_gen_attention_prefill::test_trtllm_batch_prefill[True-True-False-True-256-2047-511-False-None-fp8-fp8-fp8--1-256-16-4-8-HND]
- Failed jobs:
  - [unit_test_gb300: [cu129]](https://nv/flashinfer-ci/-/jobs/415265464)

## Failure

```text
AssertionError: Tensor-likes are not close!  Mismatched elements: 4007 / 541663232 (0.0%) Greatest absolute difference: 96.5625 at index (3626, 2, 79) (up to 0.1 allowed) Greatest relative difference: 1.1015625 at index (3634, 2, 1) (up to 0.1 allowed)
```

## Reproduction

```bash
pytest 'tests/attention/test_trtllm_gen_attention_prefill.py::test_trtllm_batch_prefill[True-True-False-True-256-2047-511-False-None-fp8-fp8-fp8--1-256-16-4-8-HND]'
```

Generated from CI test identity; not independently verified.

## Case History
- 1 confirmed failure pipeline(s); first seen 2026-08-28, last seen 2026-08-28.
- 2026-08-28 — 0.6.18rc10 (e62941a1) — GB300 / cu129 — [pipeline #64977547](https://nv/flashinfer-ci/-/pipelines/64977547) / [job](https://nv/flashinfer-ci/-/jobs/415265464)



## 评论 (1)

### bkryu · 2026-09-15

Error no longer reproduces on main branch, and the current issue is on a RC. Closing as complete
