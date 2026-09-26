# [Issue #5256] fused_moe_2stages passes num_rows to per_tensor_quant_hip, which asserts it is None

source: https://github.com/ROCm/aiter/issues/5256
state: open | updated: 2026-09-09T12:53:46Z
labels: 

## 正文

## Problem

`fused_moe_2stages` (`aiter/fused_moe.py:2621-2625`) calls the resolved `quant_func` with `num_rows=num_local_tokens` unconditionally:

```python
elif hidden_states.dtype != q_dtype_a:
    a1, a1_scale = quant_func(
        hidden_states,
        scale=a1_scale,
        quant_dtype=q_dtype_a,
        num_rows=num_local_tokens,
    )
```

`quant_func` comes from `get_hip_quant(quant_type)`. `per_token_quant_hip` and `per_group_quant_hip` accept `num_rows`, but for `QuantType.per_Tensor` the lookup returns `per_tensor_quant_hip` (`aiter/ops/quant.py:628`), which rejects it outright:

```python
def per_tensor_quant_hip(x, scale=None, quant_dtype=dtypes.i8,
                         num_rows: torch.Tensor | None = None, num_rows_factor=1):
    assert num_rows is None, "num_rows is not supported for per_tensor_quant_hip"
```

Any caller reaching `fused_moe_2stages` with `quant_type=per_Tensor` and a non-`None` `num_local_tokens` hits this deterministically. Expert-parallel MoE is the natural way to get there: the dispatcher reports a real per-rank token count and vLLM forwards it. In vLLM's modular-kernel sweep this is 100% of sub-cases for the per-tensor / per-output-channel FP8 quant configs.

```
File ".../aiter/fused_moe.py", line 816, in fused_moe_
    return fused_moe_2stages(
File ".../aiter/fused_moe.py", line 2625, in fused_moe_2stages
    a1, a1_scale = quant_func(
File ".../aiter/ops/quant.py", line 635, in per_tensor_quant_hip
    assert num_rows is None, "num_rows is not supported for per_tensor_quant_hip"
AssertionError: num_rows is not supported for per_tensor_quant_hip
```

Observed on gfx950 (MI350X), AITER `d9e5ef7ce08ee7045d583aed768cff41aa9210fe`.

## Two possible fixes, and why I am not sending a PR for either

**a) Skip `num_rows` for `per_Tensor` in `fused_moe_2stages`**, mirroring the existing `per_1x32` special case a few lines above. One line, but it changes semantics: the per-tensor scale would then be a max-abs over the whole buffer including the padding rows past `num_local_tokens`. For an EP dispatcher those rows are uninitialised, so if they can hold `inf`/`NaN` this silently poisons the scale for the valid rows — trading a loud assert for a quiet numerical bug.

**b) Implement `num_rows` truncation inside `per_tensor_quant_hip`**, as `per_token_quant_hip` already does. This looks like the semantically correct fix, but it is not a Python-level change: `dynamic_per_tensor_quant` / `static_per_tensor_quant` take no `num_rows` argument at any level (`csrc/include/quant.h:14-16`), so it needs kernel work.

I cannot tell from the outside whether the padding rows are guaranteed benign, which is exactly what decides between (a) and (b) — hence an issue rather than a speculative patch. Happy to prepare the PR for whichever option you prefer.

## Context

Found while enabling vLLM expert-parallel serving over DeepEP on MI350X. It is one of several contract mismatches on that boundary; the others are being fixed on the vLLM side ([#53261](https://github.com/vllm-project/vllm/pull/53261), [#55147](https://github.com/vllm-project/vllm/pull/55147)) and, for a related silent-corruption case in the topk kernels, in [ROCm/aiter#5255](https://github.com/ROCm/aiter/pull/5255).

## 评论 (1)

### i-kosarev · 2026-09-09

@valarLip @zufayu @junhaha666 please take a look if you have some time
