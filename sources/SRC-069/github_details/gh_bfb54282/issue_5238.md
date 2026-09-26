# [Issue #5238] [Bug] SM121 (DGX Spark GB10): mixed mxfp8 x mxfp4 fused MoE dies in moe_sort routing with "no kernel image is available" from a prebuilt moe_utils .so that has no SM12x image

source: https://github.com/flashinfer-ai/flashinfer/issues/5238
state: open | updated: 2026-09-23T15:18:03Z
labels: needs-triage

## 正文

## 🐛 Bug

On NVIDIA DGX Spark (GB10, SM121 / compute_121a, major version **12**), the mixed-precision CuTe-DSL path `cute_dsl_fused_moe_mxfp8_mxfp4` fails inside its routing step with `no kernel image is available for execution on the device`, raised from a **prebuilt** `moe_utils` shared object that only contains SM100-family images.

Related: PR #5237 fixes the *first* SM121 blocker in this module (the JIT arch filter `supported_major_versions=[9, 10]` -> adds `12`). With that fix applied, the JIT path builds `sm121a` cubins fine on this machine — but the mixed path still dies at routing time because a prebuilt, SM100-only `moe_utils` artifact takes precedence over the local JIT build.

## To Reproduce

Environment: DGX Spark GB10 (SM121), CUDA 13.0, torch 2.13.0+cu130, flashinfer 0.6.18 (SGLang image), flashinfer-jit-cache + cubin wheels installed.

1. Apply the PR #5237 one-liner (bind-mount `flashinfer/jit/moe_utils.py` with `supported_major_versions=[10, 12]` on 0.6.18) so that JIT compilation of `moe_utils` succeeds at all.
2. Call the mixed MoE:

```python
import torch
from flashinfer.fused_moe.cute_dsl import cute_dsl_fused_moe_mxfp8_mxfp4
# minimal call per docstring; real geometry used on our side:
#   num_experts=192, top_k=6, hidden=5120, intermediate=1152, EP2
out = cute_dsl_fused_moe_mxfp8_mxfp4(x, x_sf, topk_ids, topk_scales,
                                     w1, w1_sf, w1_alpha, w2, w2_sf, w2_alpha,
                                     num_experts=192, top_k=6)
```

3. It dies inside `moe_sort` (routing), before any GEMM:

```
RuntimeError: Error in function 'operator()' at /workspace/csrc/fused_moe/trtllm_backend/trtllm_fused_moe_routing_custom.cu:306: ... no kernel image is available for execution on the device
```

The `/workspace/csrc/...` path is the CI build container's source path (ci/bash.sh mounts the workspace at `/workspace`), i.e. the error comes from a `.so` that was compiled ahead-of-time upstream, not from the local JIT build.

Note `cute_dsl_fused_moe_mxfp8_mxfp4` and its wrapper class carry `@supported_compute_capability([100, 103])`, but that decorator only attaches metadata (`_supported_ccs` + `is_compute_capability_supported`); it does not gate the call, so on SM121 the function body runs and reaches the routing kernel.

## Root-cause analysis (from source)

The call chain is `cute_dsl_fused_moe_mxfp8_mxfp4` -> `moe_sort` -> `_get_moe_utils_module()` -> `gen_moe_utils_module().build_and_load()` (flashinfer/fused_moe/cute_dsl/moe_utils.py). The `moe_utils` JitSpec compiles `trtllm_fused_moe_routing_custom.cu` among its sources — so the routing kernels that fail are inside the `moe_utils` module.

Two upstream factors combine on SM121:

1. **AOT registration is SM100-family-only.** In `flashinfer/aot.py` (both v0.6.18 and current main), `gen_moe_utils_module()` is only appended under `if has_sm100f:`. `detect_sm_capabilities()` derives `has_sm100f` from `compute_100` appearing in `FLASHINFER_CUDA_ARCH_LIST`. An SM121 provider build (`FLASHINFER_JIT_CACHE_PROVIDER_ARCH=12.1a` or similar) has no `compute_100` in its arch list, so the packaged `moe_utils` artifact is only ever built for SM100-family provider wheels — and even those are compiled with `[10]`-filtered flags (pre-#5237), never `sm121a`.

2. **`try_load()` prefers the AOT artifact unconditionally when the shim is installed.** `JitSpecNvcc.try_load()` (flashinfer/jit/core.py) returns the AOT `.so` from `FLASHINFER_AOT_DIR` (`flashinfer-jit-cache` provider wheel) whenever it exists, with no device-arch compatibility check — the fallback comment says "Failed to load AOT artifact ... Falling back to JIT build" triggers only on load *exceptions*, and `cudaErrorNoKernelImageForDevice` surfaces later at kernel *launch*, not at dlopen. So on SM121 with the jit-cache shim installed, the SM100-only prebuilt wins over a perfectly good local `sm121a` JIT build.

Net effect: the same binary works for users without `flashinfer-jit-cache` (pure JIT path, after #5237) but fails for users with the prebuilt wheels installed — which is the documented recommended setup (`flashinfer install-jit-cache-wheel`).

## Expected behavior

Any of:
- `moe_utils` is included in SM121 provider builds with `sm121a` images (aot.py registration + arch filter), or
- `try_load()` validates the AOT artifact against the current device arch (e.g. via the provider manifest's `cuda_architectures`) and falls back to JIT when it does not cover the local GPU, or
- at minimum, the routing launcher raises a clear "this prebuilt module has no image for sm_121a; uninstall flashinfer-jit-cache-provider-<sm100-tag> or rebuild" instead of a raw launch failure.

## Environment

- GPU: 4 x NVIDIA DGX Spark (GB10, SM121, compute_121a)
- CUDA: 13.0, torch 2.13.0+cu130
- flashinfer 0.6.18 (SGLang image) + flashinfer-jit-cache/cubin wheels
- Verified #5237's JIT fix on the same machines: `moe_utils` JIT-compiles to `sm121a`, and `b12x_fused_moe(quant_mode="mxfp4")` (which carries its own routing and does not hit this prebuilt path) runs its full micro/static/dynamic kernel family correctly.

Workaround on SM121 today: uninstall/skip the jit-cache provider shim (pure JIT path) plus apply #5237, or use `b12x_fused_moe` instead of the mixed mxfp8 x mxfp4 API.

## 评论 (4)

### bkryu · 2026-09-15

Hi @mythkina thanks for filing the issue.

In short, DGX Spark (SM121) has a disparate support surface than SM100/103. The kernels are generally not compatible between the two, and the cute-dsl MoE is not available on DGX Spark; instead a full rewrite will be necessary.

We are currently working on the cuTile MoE that is starting to expand support on SM120/121. As of now we do not have support for mxfp8_mxfp4 as of now, but that will be the next target (see #4857 for progress). 

### aeichler-ac · 2026-09-23

!claim


### flashinfer-bot · 2026-09-23

Issue assigned to @aeichler-ac.

### aeichler-ac · 2026-09-23

Stepping off this issue.

@bkryu's triage points cute-dsl MoE / mxfp8_mxfp4 on Spark at the
cuTile rewrite (#4857), so an AOT/JIT routing-only fix would not land
the feature. Please unassign me when you have a moment.

