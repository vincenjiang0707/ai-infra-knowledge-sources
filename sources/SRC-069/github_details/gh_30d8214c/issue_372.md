# [Issue #372] transform_sf_into_required_layout: no SM120/121 (arch_major=12) branch for (gran_mn=1, gran_k=32) NVFP4 expert scales -- blocks DeepSeek-V4 weight loading

source: https://github.com/deepseek-ai/DeepGEMM/issues/372
state: open | updated: 2026-09-16T08:56:34Z
labels: 

## 正文

## Summary

`transform_sf_into_required_layout` in `csrc/apis/layout.hpp` has no branch for `arch_major=12` (SM120/SM121, i.e. RTX 5090 / RTX Pro 6000 Blackwell / NVIDIA GB10) at the `(gran_mn=1, gran_k=32)` scale-factor granularity DeepSeek-V4's NVFP4 expert weights use. This is a distinct kernel/dispatch gap from the ones already fixed in #317 / PR #318 (`tf32_hc_prenorm_gemm`, `paged_mqa_logits`) -- it blocks DeepSeek-V4 at **weight loading time** (`process_weights_after_loading`), before any forward pass is even attempted.

## Environment

- GPU: NVIDIA GB10 (DGX Spark), compute capability 12.1 (SM121)
- Framework: vLLM (`vllm-project/vllm`, personal GB10 fork), vendored DeepGEMM at `891d57b4` (2026-04-24)
- Model: `yujiepan/deepseek-v4-tiny-random` -- a small test model whose config faithfully mirrors `deepseek-ai/DeepSeek-V4-Flash`'s real quantization scheme (`expert_dtype: fp4`, same `quantization_config`), used here specifically to reproduce this on constrained hardware

## Exact failure

```
RuntimeError: Assertion error (csrc/apis/layout.hpp:59): Unknown SF transformation
```

Traceback (vLLM side):
```
File "vllm/model_executor/model_loader/utils.py", line 113, in process_weights_after_loading
File "vllm/model_executor/layers/quantization/fp8.py", line 444, in process_weights_after_loading
File "vllm/model_executor/kernels/linear/scaled_mm/deep_gemm.py", line 96, in process_weights_after_loading
File "vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 1140, in deepgemm_post_process_fp8_weight_block
File "vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 1079, in deepgemm_post_process_weight_scale_block
File "vllm/utils/deep_gemm.py", line 494, in transform_sf_into_required_layout
```

## Root cause analysis

`transform_sf_into_required_layout` (`csrc/apis/layout.hpp`) has exactly four branches:

```cpp
// (FP32, 1, 128) on SM90: transform to TMA-aligned and MN-major
if (sf.scalar_type() == torch::kFloat and gran_mn == 1 and gran_k == 128 and (arch_major == 9 or disable_ue8m0_cast))
    return get_mn_major_tma_aligned_tensor(sf);

// (FP32, 128, 128) on SM90: no need to transform, check SFB requirements
if (sf.scalar_type() == torch::kFloat and gran_mn == 128 and gran_k == 128 and (arch_major == 9 or disable_ue8m0_cast))
    return check_sf_layout(sf, mn, k, gran_mn, gran_k, num_groups, false, true, torch::kFloat);

// (FP32, x, gran_k) on SM100: transform to (INT, 1, gran_k), TMA-aligned and MN-major
if (sf.scalar_type() == torch::kFloat and (gran_k == 32 or gran_k == 128) and arch_major == 10) { ... }

// (INT, 1, gran_k) on SM100: transform to TMA-aligned and MN-major
if (sf.scalar_type() == torch::kInt and gran_mn == 1 and (gran_k == 32 or gran_k == 128) and arch_major == 10)
    return check_sf_layout(sf, mn, k, gran_mn, gran_k, num_groups, true, false, torch::kInt);

DG_HOST_UNREACHABLE("Unknown SF transformation");
```

DeepSeek-V4's NVFP4 expert scales are `(FP32, gran_mn=1, gran_k=32)` at call time (upcast from E8M0/uint8 checkpoint storage via `_upcast_e8m0_to_fp32` on the caller side). None of the four branches match on `arch_major=12`:

- Branch 1/2 require `gran_k == 128` (this call has `gran_k == 32`) -- so even with `disable_ue8m0_cast=True` (which I confirmed empirically routes vLLM's other `(gran_mn∈{1,128}, gran_k=128)` fp8-block-scale calls through the arch-agnostic fallback successfully), these two branches still can't match this granularity on any architecture.
- Branch 3/4 (the ones that do handle `gran_k == 32`) are hard-gated to `arch_major == 10` only.

So `(gran_mn=1, gran_k=32)` has **no working path on arch_major=12 at all**, regardless of `disable_ue8m0_cast`.

## Confirmed still present on current upstream

Checked against upstream `main` (currently `1f6f3f3`, well past our pinned `891d57b4`), including the most recent commit that touched this exact file (`54e22612`, "Multiple updates and refactorings (#364)", 2026-06-23) -- that commit added a `psum_layout` parameter to the function signature but did not add any `arch_major == 12` branch. The gap is still present on latest upstream.

## Impact

Blocks DeepSeek-V4 (and presumably any other model using this same NVFP4 `(1, 32)`-granularity expert-scale layout through DeepGEMM's `transform_sf_into_required_layout`) from loading at all on any SM120/SM121 GPU, independent of the forward-pass blockers already tracked in #317. This is a separate, earlier failure point (weight loading, not inference).

## Related issues

- #185, #236, #305 -- general SM120 support tracking
- #317 / PR #318 -- fixed two other missing kernel families for DeepSeek-V4 on SM120 (`tf32_hc_prenorm_gemm`, `paged_mqa_logits`); this issue is a third, distinct gap in the same DeepSeek-V4-on-SM120 effort, not covered by that PR

## Request

Would the team consider either:
1. Adding an `arch_major == 12` branch for `(gran_mn=1, gran_k=32)` (and `128`) mirroring the existing SM100 branches (3/4 above), or
2. Extending branch 1/2's `disable_ue8m0_cast` fallback to also cover `gran_k == 32`, if that's numerically valid?

As with #317, a reference implementation or guidance on the expected approach would help the community contribute, given the team's stated capacity constraints for SM120 hardware.


## 评论 (1)

### lucifer1004 · 2026-09-16

#447 adds the arch_major == 12 branch to `transform_sf_into_required_layout` (`csrc/apis/layout.hpp`): `(gran_mn=1, gran_k=32)` float SFs go through `get_mn_major_tma_aligned_packed_ue8m0_tensor` (gran_mn==1 needs no broadcast), and prepacked int input is validated by `check_sf_layout`. The backing transforms are arch-generic smxx JIT kernels with a torch fallback for odd shapes.

Coverage on arch 12: `test_sm120_symmetric_fp4_mn` (recipe (1,1,32) dense fp4, both SF orientations) and the NVFP4 m-grouped expert-scale recipes in `test_sm120_gemm.py`. This unblocks DeepSeek-V4 NVFP4 expert weight loading on SM120/SM121.

