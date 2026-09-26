# [Issue #4776] [Bug][v0.6.18rc9] AssertionError: Tensor-likes are not close! Mismatched elements: 12292 / 524288 (2.3%) Greatest absolute difference: 1.0343796014785767 at index (233, 3, 2) (up to 0.1 allowed) Great

source: https://github.com/flashinfer-ai/flashinfer/issues/4776
state: closed | updated: 2026-09-21T04:31:13Z
labels: needs-triage, ci: health

## 正文

## Summary
FlashInfer 0.6.18rc9 CI reports 3 distinct saved failure signature(s) affecting 8 selected test(s) across 3 environment(s). The evidence from 9 selected failure group(s) is de-duplicated by failure, job, environment, and history pipeline below.

## CI environment
- Commit: eadfae36
- Branch: release-v0.6.18
- Pipeline: [#64780358](https://nv/flashinfer-ci/-/pipelines/64780358)
- Affected tests:
  - tests.attention.test_trtllm_ragged_dit.py::test_trtllm_ragged_dit_sage_qdq[16-1-128-8-256-256-2-False]
  - tests.attention.test_trtllm_ragged_dit.py::test_trtllm_ragged_dit_sage_qdq[4-1-128-8-256-256-2-False]
  - tests.attention.test_trtllm_ragged_dit.py::test_trtllm_ragged_dit_sage_qdq[16-1-128-1-512-2048-2-False]
  - tests.attention.test_trtllm_ragged_dit.py::test_trtllm_ragged_dit_sage_qdq[16-1-128-1-256-256-2-False]
  - tests.attention.test_trtllm_ragged_dit.py::test_trtllm_ragged_dit_sage_qdq[4-1-128-1-512-2048-2-False]
  - tests.attention.test_trtllm_ragged_dit.py::test_trtllm_ragged_dit_sage_qdq[4-1-128-8-512-2048-2-False]
  - tests.attention.test_trtllm_ragged_dit.py::test_trtllm_ragged_dit_sage_qdq[16-1-128-8-512-2048-2-False]
  - tests.attention.test_trtllm_ragged_dit.py::test_trtllm_ragged_dit_sage_qdq[4-1-128-1-256-256-2-False]
- Environments:
  - unit_test_gb200 / GB200 / cu129, cu130
  - unit_test_gb200 / GB200 / cu130
  - unit_test_gb200 / GB200 / cu129
- Failed jobs:
  - [unit_test_gb200: \[cu129\] #413687934](https://nv/flashinfer-ci/-/jobs/413687934)
  - [unit_test_gb200: \[cu130\] #413687935](https://nv/flashinfer-ci/-/jobs/413687935)

## Failure

**Failure 1 — affects tests.attention.test_trtllm_ragged_dit.py::test_trtllm_ragged_dit_sage_qdq[16-1-128-8-256-256-2-False]**

```text
AssertionError: Tensor-likes are not close! Mismatched elements: 12292 / 524288 (2.3%) Greatest absolute difference: 1.0343796014785767 at index (233, 3, 2) (up to 0.1 allowed) Greatest relative difference: 52559.12890625 at index (73, 1, 2) (up to 0.1 allowed)
```

**Failure 2 — affects tests.attention.test_trtllm_ragged_dit.py::test_trtllm_ragged_dit_sage_qdq[4-1-128-8-256-256-2-False]**

```text
AssertionError: Tensor-likes are not close! Mismatched elements: 16121 / 524288 (3.1%) Greatest absolute difference: 0.9921048879623413 at index (109, 2, 84) (up to 0.1 allowed) Greatest relative difference: 61854.8203125 at index (23, 5, 44) (up to 0.1 allowed)
```

**Failure 3 — affects tests.attention.test_trtllm_ragged_dit.py::test_trtllm_ragged_dit_sage_qdq[16-1-128-1-512-2048-2-False]**

```text
AssertionError: Tensor-likes are not close! Mismatched elements: 271 / 131072 (0.2%) Greatest absolute difference: 0.5841161608695984 at index (592, 0, 127) (up to 0.1 allowed) Greatest relative difference: 2745.787353515625 at index (785, 0, 81) (up to 0.1 allowed)
```
6 additional distinct failures omitted.

## Reproduction

```bash
pytest \
  'tests/attention/test_trtllm_ragged_dit.py::test_trtllm_ragged_dit_sage_qdq[16-1-128-8-256-256-2-False]' \
  'tests/attention/test_trtllm_ragged_dit.py::test_trtllm_ragged_dit_sage_qdq[4-1-128-8-256-256-2-False]' \
  'tests/attention/test_trtllm_ragged_dit.py::test_trtllm_ragged_dit_sage_qdq[16-1-128-1-512-2048-2-False]' \
  'tests/attention/test_trtllm_ragged_dit.py::test_trtllm_ragged_dit_sage_qdq[16-1-128-1-256-256-2-False]' \
  'tests/attention/test_trtllm_ragged_dit.py::test_trtllm_ragged_dit_sage_qdq[4-1-128-1-512-2048-2-False]' \
  'tests/attention/test_trtllm_ragged_dit.py::test_trtllm_ragged_dit_sage_qdq[4-1-128-8-512-2048-2-False]' \
  'tests/attention/test_trtllm_ragged_dit.py::test_trtllm_ragged_dit_sage_qdq[16-1-128-8-512-2048-2-False]' \
  'tests/attention/test_trtllm_ragged_dit.py::test_trtllm_ragged_dit_sage_qdq[4-1-128-1-256-256-2-False]'
```

Generated from 8 saved CI test identities; run from the FlashInfer repository root. Not independently verified.

## Case History
1 unique confirmed historical failure pipeline(s) shown; first seen 2026-08-27, last seen 2026-08-27.
- 2026-08-27 — 0.6.18rc9 (eadfae36) — unit_test_gb200 / GB200 / cu129, cu130; unit_test_gb200 / GB200 / cu130; unit_test_gb200 / GB200 / cu129 — [pipeline #64780358](https://nv/flashinfer-ci/-/pipelines/64780358) — affects tests.attention.test_trtllm_ragged_dit.py::test_trtllm_ragged_dit_sage_qdq[16-1-128-8-256-256-2-False], tests.attention.test_trtllm_ragged_dit.py::test_trtllm_ragged_dit_sage_qdq[4-1-128-8-256-256-2-False], tests.attention.test_trtllm_ragged_dit.py::test_trtllm_ragged_dit_sage_qdq[16-1-128-1-512-2048-2-False] / [unit_test_gb200: \[cu129\] #413687934](https://nv/flashinfer-ci/-/jobs/413687934), [unit_test_gb200: \[cu130\] #413687935](https://nv/flashinfer-ci/-/jobs/413687935)



## 评论 (1)

### bkryu · 2026-08-31

Closing issue as it pertains to an rc version of 0.6.18 and 0.6.18 has been released
