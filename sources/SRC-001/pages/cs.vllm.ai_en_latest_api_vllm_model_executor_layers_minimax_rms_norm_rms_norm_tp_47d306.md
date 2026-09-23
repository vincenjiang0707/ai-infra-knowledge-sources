source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.minimax_rms_norm.rms_norm_tp`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.minimax_rms_norm.rms_norm_tp)

##

`_all_reduce_variance(var)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.minimax_rms_norm.rms_norm_tp._all_reduce_variance)

All-reduce a per-token variance tensor across the TP group.

Variance is accumulated in fp32 for numerical stability. The FlashInfer fused all-reduce caches a single global workspace keyed to the model's 16-bit activation dtype (`use_fp32_lamport=False`

); routing an fp32 reduction through it would read against a mismatched workspace and corrupt the result. FlashInfer's fast-path only triggers for 2D inputs, so reducing a flattened (1D) view keeps these fp32 reductions on custom all-reduce / pynccl, both of which handle fp32 correctly.

## Source code in `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py`


##

`_minimax_qk_norm_tp_eager(qkv, q_weight, k_weight, q_size, kv_size, tp_world, eps)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.minimax_rms_norm.rms_norm_tp._minimax_qk_norm_tp_eager)

Pure-torch reference path used when Triton is unavailable.

## Source code in `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py`


##

`_minimax_qk_norm_tp_fallback(qkv, q_weight, k_weight, q_size, kv_size, tp_rank, tp_world, eps)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.minimax_rms_norm.rms_norm_tp._minimax_qk_norm_tp_fallback)

All-reduce + QK RMSNorm without the Lamport fused kernel.

The all-reduce is a TP communication barrier and cannot live inside a single kernel, so the eager-torch path is split into two Triton kernels around it: a variance reduction before the all-reduce and a normalize after. Compared to the `torch.compile`

path this avoids materializing fp32 copies of q/k and the `cat`

/`chunk`

temporaries.

## Source code in `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py`


##

`_minimax_qk_var_kernel(qkv_ptr, var_ptr, row_stride, q_size, kv_size, BLOCK)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.minimax_rms_norm.rms_norm_tp._minimax_qk_var_kernel)

TP-pre stage: per-token mean-of-squares for the q and k segments.

Accumulates in fp32 while reading the 16-bit qkv in place, so no fp32 copy of q/k is materialized. `var[:, 0]`

is the q variance and `var[:, 1]`

the k variance; both are the local-shard means, ready for the all-reduce that follows.

## Source code in `vllm/model_executor/layers/minimax_rms_norm/rms_norm_tp.py`


##

`_minimax_rms_apply_kernel(qkv_ptr, var_ptr, q_w_ptr, k_w_ptr, q_out_ptr, k_out_ptr, row_stride, q_size, kv_size, tp_world, eps, BLOCK)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.minimax_rms_norm.rms_norm_tp._minimax_rms_apply_kernel)

TP-post stage: `x * rsqrt(var / tp_world + eps) * weight`

.

A single program normalizes both the q and k segments of one token, so q and k share one launch instead of two. The all-reduce yields the sum of per-shard means, so the `/ tp_world`

that recovers the global mean-of-squares is folded into the `rsqrt`

here rather than run as a separate elementwise pass over the `[num_tokens, 2]`

variance tensor.