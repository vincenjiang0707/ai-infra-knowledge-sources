# [Issue #5367] [Bug][nightly-release] Missing JIT-cache provider wheels due to build timeouts and runner acquisition failures

source: https://github.com/flashinfer-ai/flashinfer/issues/5367
state: open | updated: 2026-09-21T07:56:50Z
labels: needs-triage, ci: health

## 正文

## Description

Three consecutive Nightly Release runs each missed one expected JIT-cache provider artifact.

Each run expected 42 provider artifacts and 6 shim artifacts, but only 41 providers were produced. The missing provider caused provider validation, release creation, nightly installation tests, and wheel-index updates to be
skipped.

The failures fall into two categories:

1. A provider build reached the final Ninja link steps, stopped producing output, and was cancelled after the 6-hour job timeout.
2. A provider job was never acquired by a matching self-hosted runner.


## Affected nightly runs

| Nightly run | Missing artifact | Failed/cancelled job | Observed error |
|---|---|---|---|
| [#385](https://github.com/flashinfer-ai/flashinfer/actions/runs/35306860005) | `jit-cache-provider-cu134-x86_64-sm90a` | [JIT cache provider (cu134, x86_64, sm90a)](https://github.com/flashinfer-ai/flashinfer/actions/runs/35306860005/job/105482987504) | Provider build stopped near the end and exceeded the 6-hour timeout |
| [#386](https://github.com/flashinfer-ai/flashinfer/actions/runs/35421090746) | `jit-cache-provider-cu129-x86_64-sm103a` | [JIT cache provider (cu129, x86_64, sm103a)](https://github.com/flashinfer-ai/flashinfer/actions/runs/35421090746/job/105840320418) | Job was not acquired by a self-hosted runner |
| [#387](https://github.com/flashinfer-ai/flashinfer/actions/runs/35489728650) | `jit-cache-provider-cu129-x86_64-sm90a` | [JIT cache provider (cu129, x86_64, sm90a)](https://github.com/flashinfer-ai/flashinfer/actions/runs/35489728650/job/106023662663) | Provider build stopped near the end and exceeded the 6-hour timeout |

## Impact
In every affected run:
- one of the 42 expected provider artifacts was missing;
- all 6 shim artifacts were generated successfully;
- `flashinfer-python-dist` and `flashinfer-cubin-wheel` were generated;
- provider validation was skipped;
- `create-release` was skipped;
- `test-nightly-build` was skipped;
- `update-wheel-index` was skipped.
Therefore, the nightly release was not completed or published even though the other provider matrix jobs succeeded.


## Possible causes
### Build hangs in [#385](https://github.com/flashinfer-ai/flashinfer/actions/runs/35306860005) and [#387](https://github.com/flashinfer-ai/flashinfer/actions/runs/35489728650)
Both jobs progressed to `[4450/4452]` and then stopped during a `c++` shared library link command. However, they stopped on different output libraries and different CUDA configurations:
- [#385](https://github.com/flashinfer-ai/flashinfer/actions/runs/35306860005): CUDA 13.4 SM90a, linking `fmha_cudnn_gen.so`
- [#387](https://github.com/flashinfer-ai/flashinfer/actions/runs/35489728650): CUDA 12.9 SM90a, linking `topk.so`
There was no compiler or linker error before cancellation.
This pattern suggests an intermittent worker or subprocess hang rather than a deterministic source compilation failure. Possible causes include:
- a stuck linker or child process;
- resource exhaustion or severe swapping;
- disk or filesystem I/O stalls;
- container/runtime instability;
- an unhealthy on-demand self-hosted runner.

### Runner acquisition failure in [#386](https://github.com/flashinfer-ai/flashinfer/actions/runs/35421090746)
The job was never assigned to a runner with these labels:
```
self-hosted
linux
x64
cpu
on-demand
```
This likely points to the self-hosted runner autoscaler or runner registration path, such as insufficient capacity, provisioning failure, or a runner that failed to register before GitHub stopped retrying.

## 评论 (1)

### cindyzxq · 2026-09-21

@dierksen Could you please help check this issue? This happened multiple times and make the nightly release actions unstable. Thank you.
