# [Issue #2326] CI: onnx example lanes fail with CUDNN_STATUS_SUBLIBRARY_LOADING_FAILED on linux-amd64-gpu-rtxpro6000-latest-1

source: https://github.com/NVIDIA/Model-Optimizer/issues/2326
state: closed | updated: 2026-09-03T20:17:53Z
labels: 

## 正文

## Summary

Every PR that actually runs the `onnx` example lane is currently failing with a cuDNN loading error, blocking the `example-pr-required-check` gate. Reproduced across three PRs on three distinct runner nodes, so this is not a single bad node.

```
RuntimeError: CUDNN_BACKEND_TENSOR_DESCRIPTOR cudnnFinalize failed ptrDesc->finalize()
              cudnn_status: CUDNN_STATUS_SUBLIBRARY_LOADING_FAILED
```

## Affected jobs

- `onnx (diffusers) / run-test` — `tests/examples/diffusers/sparsity/test_sparsity.py` (`test_wan22_baseline`, `test_wan22_triton_baseline`)
- `onnx (torch_onnx) / run-test` — `tests/examples/torch_onnx/test_torch_quant_to_onnx.py` (`vit_tiny-fp8`, `vit_tiny-int8`)
- `example-pr-required-check` — aggregate gate, fails as a consequence

The subprocess under test exits 1; the cuDNN error is the underlying cause.

## Scope

| PR | torch_onnx runner node | Result |
|---|---|---|
| #2201 | `cfc3-l-amd-g-rtxpro6000-l-1-vkjrx-runner-74bd7` | failure |
| #2319 | `cfc3-l-amd-g-rtxpro6000-l-1-vkjrx-runner-n57z2` | failure |
| #2317 | `cfc3-l-amd-g-rtxpro6000-l-1-vkjrx-runner-fr9h7` | failure |

All on runner label `linux-amd64-gpu-rtxpro6000-latest-1`. The three PRs are unrelated in content — a Megatron quantizer resharding fix, an ONNX AutoCast fix, and a docs-only skills change — which rules out any one PR as the cause.

## Notes for whoever picks this up

- The lane's image is **pinned** (`nvcr.io/nvidia/tensorrt:26.05-py3`, `.github/workflows/example_tests.yml`) and unchanged, so this looks like a driver/runtime change on the runner pool rather than an image bump. `CUDNN_STATUS_SUBLIBRARY_LOADING_FAILED` typically means the cuDNN sublibraries can't be dlopened — a driver/cuDNN version mismatch or an incomplete install in the node image.
- **This is probably under-reported.** PRs that appear green on `example_tests` may simply have the lane gated off by path filters (#2325 and #2264 did not run `torch_onnx` at all), so the true blast radius is every PR touching paths that trigger the lane.
- First failures observed 2026-09-03.

cc @NVIDIA/modelopt-setup-codeowners (owns `.github`)

## 评论 (1)

### kevalmorabia97 · 2026-09-03

Already fixed in main. Please rebate to include fix in your branch
