# [Issue #4957] [Bug] test_multistream_overlap.py CUDA error: unspecified launch failure Search for `cudaErrorLaunchFailure'

source: https://github.com/flashinfer-ai/flashinfer/issues/4957
state: closed | updated: 2026-09-21T04:31:20Z
labels: ci: health, arch: sm107

## 正文

## Summary
FlashInfer main(971b0a6b) CI reports a test assertion affecting 1 saved failure occurrence(s) across 1 affected test(s). The saved evidence covers unknown / cu134 in flashinfer-ci.

## CI environment

- Commit: 971b0a6b
- Branch: main
- Pipeline: [#66007281](https://nv/flashinfer-ci/-/pipelines/66007281)
- Affected scope: 1 saved failure occurrence(s) across 1 affected test(s)
- Affected tests:
  - evidence.failure_group.0fd0ce3cc0860ac7a6dc::__failure_group__:0fd0ce3cc0860ac7a6dc
- Failed jobs:
  - [unit_test_vr200_cu134](https://nv/flashinfer-ci/-/jobs/423917323)

## Failure

```text
torch.AcceleratorError: CUDA error: unspecified launch failure Search for `cudaErrorLaunchFailure' in https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__TYPES.html for more information. CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below migh
```

## Reproduction

```bash
pytest 'evidence/failure_group/0fd0ce3cc0860ac7a6dc.py::__failure_group__:0fd0ce3cc0860ac7a6dc'
```

Generated from CI test identity; not independently verified.

## Case History
- 1 confirmed failure pipeline(s); first seen 2026-09-03, last seen 2026-09-03.
- 2026-09-03 —  (971b0a6b) — unknown GPU / cu134 — [pipeline #66007281](https://nv/flashinfer-ci/-/pipelines/66007281) / [job](https://nv/flashinfer-ci/-/jobs/423917323)


## 评论 (3)

### aleozlx · 2026-09-11

@nvamyt can you v2c?

### nvamyt · 2026-09-14

> [@nvamyt](https://github.com/nvamyt) can you v2c?

Sure. Still fail with 0.7rc1:[unit_test_vr200_cu134](https://nv/flashinfer-ci/-/jobs/433055693)
```shell
E   torch.AcceleratorError: CUDA error: unspecified launch failure
    Search for `cudaErrorLaunchFailure' in https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__TYPES.html for more information.
    CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
    For debugging consider passing CUDA_LAUNCH_BLOCKING=1
    The CUDA driver logged these messages, which may provide useful details:
    Returning 719 (CUDA_ERROR_LAUNCH_FAILED) from cuCtxSynchronize_v2
``` 

### Vinnie6167 · 2026-09-15

#5227 adds a workaround fix. Filed a bug against CuTe-DSL for a long term solution.
