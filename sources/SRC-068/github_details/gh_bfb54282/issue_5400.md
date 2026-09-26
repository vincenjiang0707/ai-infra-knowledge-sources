# [Issue #5400] [Bug] test_tensor_cores_decode.py Mismatched elements: 2 / 8192 (0.0%) Greatest absolute difference: 0.00115966796875 at index (10, 224) (up to 0.001 allowed) Greatest relative difference: 0.03363037109375 at index (10, 116) (up to 0.001 allowed)

source: https://github.com/flashinfer-ai/flashinfer/issues/5400
state: open | updated: 2026-09-24T08:07:13Z
labels: needs-triage, ci: health

## 正文

<!-- dlqa-triage:flashinfer-ci:v1 -->
<!-- dlqa-triage:flashinfer-ci-request:ec1903ac182e2c8265b2a401c376a807efaa17dae8b17428805bdf31e6b64f35 -->

## Summary
FlashInfer main (975f9058) CI reports a test assertion affecting 1 saved failure occurrence(s) across 1 affected test(s). The saved evidence covers Spark / cu129 in flashinfer-ci.

## CI environment

- Commit: 975f9058
- Branch: main
- Pipeline: [#68873160](https://nv/flashinfer-ci/-/pipelines/68873160)
- Affected scope: 1 saved failure occurrence(s) across 1 affected test(s)
- Affected tests:
  - tests/attention/test_tensor_cores_decode.py::test_single_decode_tensor_cores[ROPE_LLAMA-HND-256-4-8-54]
- Failed jobs:
  - [unit_test_spark: [cu129]](https://nv/flashinfer-ci/-/jobs/448314280)

## Failure

```text
AssertionError: Tensor-likes are not close!  Mismatched elements: 2 / 8192 (0.0%) Greatest absolute difference: 0.00115966796875 at index (10, 224) (up to 0.001 allowed) Greatest relative difference: 0.03363037109375 at index (10, 116) (up to 0.001 allowed)
```

## Reproduction

```bash
pytest 'tests/attention/test_tensor_cores_decode.py::test_single_decode_tensor_cores[ROPE_LLAMA-HND-256-4-8-54]'
```

Generated from CI test identity;

## Case History
- 1 confirmed failure pipeline(s); first seen 2026-09-20, last seen 2026-09-20.
- 2026-09-20 — 975f9058 — Spark / cu129 — [pipeline #68873160](https://nv/flashinfer-ci/-/pipelines/68873160) / [job](https://nv/flashinfer-ci/-/jobs/448314280)


## 评论 (3)

### aeichler-ac · 2026-09-24

!claim


### flashinfer-bot · 2026-09-24

Issue assigned to @aeichler-ac.

### aeichler-ac · 2026-09-24

Reproduced the cited node on DGX Spark GB10 (SM121), torch 2.13.0+cu130,
flashinfer main.

Under `atol=rtol=1e-3` the failure is a fp16 tensor-core vs cuda-core
rounding bound: CI reported abs ~1.16e-3 (and rel ~3.3e-2 on another
element). Locally the same param usually sits under 1e-3; stress draws
still reach abs ~2e-3.

Opened a PR that loosens the TC-vs-cuda-core checks in
`test_tensor_cores_decode.py` to `atol=2e-3, rtol=1e-2` (same ballpark as
other fp16 attention compares). No kernel change.

CI will need `@flashinfer-bot run`.

