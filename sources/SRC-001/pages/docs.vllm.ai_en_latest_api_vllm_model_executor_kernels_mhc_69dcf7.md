source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/mhc/
lastmod: 2026-09-23

#

`vllm.model_executor.kernels.mhc`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc)

Modules:

Functions:

-
–[hc_head_fused_cpu](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.hc_head_fused_cpu)CPU-ported HC head reduction (see

`test_hc_head_cpu`

in -
–[mhc_fused_post_pre_aiter](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_fused_post_pre_aiter)Fused mHC post + next mHC pre on ROCm via AITER.

-
–[mhc_fused_post_pre_tilelang](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_fused_post_pre_tilelang)Run one MHC post block followed by the next MHC pre block.

-
–[mhc_post_cpu](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_post_cpu)CPU-ported mHC post block (see

`mhc_post_torch`

for the eager reference). -
–[mhc_pre_aiter](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_aiter)Forward pass for mHC pre block.

-
–[mhc_pre_cpu](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_cpu)CPU-ported mHC pre block (see

`mhc_pre_torch`

for the eager reference). -
–[mhc_pre_delayed_aiter](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_aiter)MHC pre with the pre-mix carried in from the previous sublayer.

-
–[mhc_pre_mix_triton](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_mix_triton)Pre-mix gate for the delayed mHC pre, from AITER's split-k GEMM output.

-
–[mhc_pre_tilelang](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_tilelang)Forward pass for mHC pre block.

-
–[mhc_pre_torch](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_torch)Forward pass for mHC pre block.


##

`cdiv(a, b)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.cdiv)

##

`direct_register_custom_op(op_name, op_func, mutates_args=None, fake_impl=None, target_lib=None, dispatch_key=None, tags=())`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.direct_register_custom_op)

`torch.library.custom_op`

can have significant overhead because it needs to consider complicated dispatching logic. This function directly registers a custom op and dispatches it to the CUDA backend. See https://gist.github.com/youkaichao/ecbea9ec9fc79a45d2adce1784d7a9a5 for more details.

By default, the custom op is registered to the vLLM library. If you want to register it to a different library, you can pass the library object to the `target_lib`

argument.

IMPORTANT: the lifetime of the operator is tied to the lifetime of the library object. If you want to bind the operator to a different library, make sure the library object is alive when the operator is used.

## Source code in `vllm/utils/torch_utils.py`


##

`hc_collapse_triton(x, pre_mix)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.hc_collapse_triton)

Collapse BF16 residual streams with FP32 pre-mix coefficients.

## Source code in `vllm/model_executor/kernels/mhc/triton.py`


##

`hc_head_fused_cpu(hidden_states, hc_fn, hc_scale, hc_base, rms_norm_eps, hc_eps)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.hc_head_fused_cpu)

CPU-ported HC head reduction (see `test_hc_head_cpu`

in tests/kernels/test_mhc_kernels.py for the eager reference this is tested against).

The ported kernel's C++ signature takes `(hc_eps, norm_eps)`

-- the opposite order from this wrapper's `(rms_norm_eps, hc_eps)`

, which matches the real call site in `models/deepseek_v4/cpu/model.py`

.

## Source code in `vllm/model_executor/kernels/mhc/cpu.py`


##

`hc_head_fused_kernel_tilelang(hs_flat, fn, hc_scale, hc_base, rms_eps, hc_eps)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.hc_head_fused_kernel_tilelang)

Apply the fused hc_head kernel and return the (T, H) bf16 result.

## Source code in `vllm/model_executor/kernels/mhc/tilelang.py`


##

`mhc_fused_post_pre_aiter(x, residual, post_layer_mix, comb_res_mix, fn, hc_scale, hc_base, rms_eps, hc_pre_eps, hc_sinkhorn_eps, hc_post_mult_value, sinkhorn_repeat, n_splits=1, tile_n=1, norm_weight=None, norm_eps=0.0)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_fused_post_pre_aiter)

Fused mHC post + next mHC pre on ROCm via AITER.

Returns residual_cur, post_mix_cur, comb_mix_cur, layer_input_cur.

## Source code in `vllm/model_executor/kernels/mhc/aiter.py`


##

`mhc_fused_post_pre_delayed_tilelang(x, residual, post_layer_mix, comb_res_mix, fn, hc_scale, hc_base, rms_eps, hc_pre_eps, hc_sinkhorn_eps, hc_post_mult_value, sinkhorn_repeat, pre_mix=None, norm_weight=None, norm_eps=1e-06, capture_aux=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_fused_post_pre_delayed_tilelang)

Run one mHC post block followed by the next delayed mHC pre block.

Within the fused kernel's token range the post mapping is folded into the pre-norm GEMM, so the updated residual streams feed the projection from registers instead of a second pass over global memory. Above it this runs the same post kernel and split-k GEMM as the unfused pair.

Parameters:

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_fused_post_pre_delayed_tilelang(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)BF16 sublayer output of shape (tokens, hidden_size).

-

(`residual`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_fused_post_pre_delayed_tilelang(residual))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)BF16 residual streams of shape (tokens, hc_mult, hidden_size).

-

(`post_layer_mix`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_fused_post_pre_delayed_tilelang(post_layer_mix))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)FP32 post coefficients of shape (tokens, hc_mult, 1).

-

(`comb_res_mix`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_fused_post_pre_delayed_tilelang(comb_res_mix))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)FP32 residual coefficients, (tokens, hc_mult, hc_mult).

-

(`fn`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_fused_post_pre_delayed_tilelang(fn))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)FP32 projection of shape (hc_mult * (hc_mult + 2), input_size).

-

(`hc_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_fused_post_pre_delayed_tilelang(hc_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)FP32 scales of shape (3,).

-

(`hc_base`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_fused_post_pre_delayed_tilelang(hc_base))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)FP32 bias of shape (hc_mult * (hc_mult + 2),).

-

(`rms_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_fused_post_pre_delayed_tilelang(rms_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)RMS normalization epsilon.

-

(`hc_pre_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_fused_post_pre_delayed_tilelang(hc_pre_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Pre-mix epsilon.

-

(`hc_sinkhorn_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_fused_post_pre_delayed_tilelang(hc_sinkhorn_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Sinkhorn epsilon.

-

(`hc_post_mult_value`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_fused_post_pre_delayed_tilelang(hc_post_mult_value))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Post-mix multiplier.

-

(`sinkhorn_repeat`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_fused_post_pre_delayed_tilelang(sinkhorn_repeat))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of Sinkhorn iterations.

-

(`pre_mix`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_fused_post_pre_delayed_tilelang(pre_mix))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –FP32 coefficients from the previous sublayer, or None to select residual stream zero.

-

(`norm_weight`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_fused_post_pre_delayed_tilelang(norm_weight))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional BF16 RMSNorm weight for the collapsed input.

-

(`norm_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_fused_post_pre_delayed_tilelang(norm_eps))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)`1e-06`

) –RMSNorm epsilon for the collapsed input.

-

(`capture_aux`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_fused_post_pre_delayed_tilelang(capture_aux))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Also return the mean over the post-mapped streams, which draft models consume as the target's hidden state. It is folded into the collapse, which already reads those streams.


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The post-mapped residual streams, the post and residual coefficients,

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)the optionally normalized BF16 layer input, the next FP32 pre-mix, and

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)the BF16 stream mean (empty unless capture_aux), with shapes

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(tokens, hc_mult, hidden_size), (tokens, hc_mult, 1),

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(tokens, hc_mult, hc_mult), (tokens, hidden_size), (tokens, hc_mult),

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)and (tokens, hidden_size).


## Source code in `vllm/model_executor/kernels/mhc/tilelang.py`


|
|

##

`mhc_fused_post_pre_tilelang(x, residual, post_layer_mix, comb_res_mix, fn, hc_scale, hc_base, rms_eps, hc_pre_eps, hc_sinkhorn_eps, hc_post_mult_value, sinkhorn_repeat, n_splits=1, tile_n=1, norm_weight=None, norm_eps=1e-06)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_fused_post_pre_tilelang)

Run one MHC post block followed by the next MHC pre block.

When `norm_weight`

is provided, the layer_input_cur output is the RMSNorm'd activation (fused into the kernel); otherwise it is the raw pre-norm activation as before.

`n_splits`

and `tile_n`

are retained for the shared MHC operator API. The TileLang path selects both values internally from the runtime shape.

Returns:

-
(`residual_cur`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)post-mapped residual, shape (..., hc_mult, hidden_size)

-
(`post_mix_cur`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (..., hc_mult, 1)

-
(`comb_mix_cur`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (..., hc_mult, hc_mult)

-
(`layer_input_cur`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (..., hidden_size)


## Source code in `vllm/model_executor/kernels/mhc/tilelang.py`


|
|

##

`mhc_post_cpu(x, residual, post_layer_mix, comb_res_mix)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_post_cpu)

CPU-ported mHC post block (see `mhc_post_torch`

for the eager reference).

## Source code in `vllm/model_executor/kernels/mhc/cpu.py`


##

`mhc_pre_aiter(residual, fn, hc_scale, hc_base, rms_eps, hc_pre_eps, hc_sinkhorn_eps, hc_post_mult_value, sinkhorn_repeat, n_splits=1, norm_weight=None, norm_eps=0.0)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_aiter)

Forward pass for mHC pre block.

Parameters:

-

(`residual`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_aiter(residual))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (..., hc_mult, hidden_size), dtype torch.bfloat16

-

(`fn`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_aiter(fn))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (hc_mult3, hc_mult * hidden_size), dtype torch.float32

-

(`hc_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_aiter(hc_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (3,), dtype torch.float32

-

(`hc_base`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_aiter(hc_base))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (hc_mult3,), dtype torch.float32

-

(`rms_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_aiter(rms_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)RMS normalization epsilon

-

(`hc_pre_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_aiter(hc_pre_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)pre-mix epsilon

-

(`hc_sinkhorn_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_aiter(hc_sinkhorn_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)sinkhorn epsilon

-

(`hc_post_mult_value`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_aiter(hc_post_mult_value))

) –[float](https://docs.python.org/3/builtins/functions.html#float)post-mix multiplier value

-

(`sinkhorn_repeat`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_aiter(sinkhorn_repeat))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of sinkhorn iterations

-

(`n_splits`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_aiter(n_splits))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –split-k factor;

-

(`norm_weight`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_aiter(norm_weight))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –optional RMSNorm weight fused into the pre kernel

-

(`norm_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_aiter(norm_eps))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)`0.0`

) –epsilon for the fused RMSNorm when norm_weight is set


Returns:

-
(`post_mix`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (..., hc_mult), dtype torch.float32

-
(`comb_mix`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (..., hc_mult, hc_mult), dtype torch.float32

-
(`layer_input`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (..., hidden_size), dtype torch.bfloat16


## Source code in `vllm/model_executor/kernels/mhc/aiter.py`


##

`mhc_pre_broadcast_tilelang(residual, fn, hc_scale, hc_base, rms_eps, hc_pre_eps, hc_sinkhorn_eps, hc_post_mult_value, sinkhorn_repeat, n_splits=1, norm_weight=None, norm_eps=1e-06, fn_broadcast=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_broadcast_tilelang)

First-layer mHC pre for a residual broadcast from `(T, H)`

.

## Source code in `vllm/model_executor/kernels/mhc/tilelang.py`


|
|

##

`mhc_pre_cpu(residual, fn, hc_scale, hc_base, rms_eps, hc_pre_eps, hc_sinkhorn_eps, hc_post_mult_value, sinkhorn_repeat, n_splits=1, norm_weight=None, norm_eps=0.0)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_cpu)

CPU-ported mHC pre block (see `mhc_pre_torch`

for the eager reference).

The ported kernel (`hc_pre_fused_cpu`

) only exposes one merged `hc_eps`

(used for both `hc_pre_eps`

/`hc_sinkhorn_eps`

) and hardcodes the post-mix multiplier to 2.0 -- true of every real call site in `models/deepseek_v4/cpu/model.py`

, so this is not a capability loss here.

## Source code in `vllm/model_executor/kernels/mhc/cpu.py`


##

`mhc_pre_delayed_aiter(residual, fn, hc_scale, hc_base, rms_eps, hc_pre_eps, hc_sinkhorn_eps, hc_post_mult_value, sinkhorn_repeat, pre_mix=None, sublayer_out=None, post_layer_mix=None, comb_res_mix=None, residual_out=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_aiter)

MHC pre with the pre-mix carried in from the previous sublayer.

Matches `mhc_pre_delayed_torch`

: the stream collapse uses *pre_mix* rather than the gate computed here, and that gate is returned as the pre-mix for the next sublayer seam.

Parameters:

-

(`residual`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_aiter(residual))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (..., hc_mult, hidden_size), dtype torch.bfloat16

-

(`fn`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_aiter(fn))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (hc_mult3, hc_mult * hidden_size), dtype torch.float32

-

(`hc_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_aiter(hc_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (3,), dtype torch.float32

-

(`hc_base`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_aiter(hc_base))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (hc_mult3,), dtype torch.float32

-

(`rms_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_aiter(rms_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)RMS normalization epsilon

-

(`hc_pre_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_aiter(hc_pre_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)pre-mix epsilon

-

(`hc_sinkhorn_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_aiter(hc_sinkhorn_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)sinkhorn epsilon

-

(`hc_post_mult_value`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_aiter(hc_post_mult_value))

) –[float](https://docs.python.org/3/builtins/functions.html#float)post-mix multiplier value

-

(`sinkhorn_repeat`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_aiter(sinkhorn_repeat))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of sinkhorn iterations

-

(`pre_mix`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_aiter(pre_mix))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –shape (..., hc_mult) from the previous sublayer, or None at model entry to select residual stream zero.

-

(`sublayer_out`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_aiter(sublayer_out))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –attention or FFN output, shape (..., hidden_size). When given with the two mixes below, the preceding post block is applied here so AITER can fold it into the pre projection.

-

(`post_layer_mix`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_aiter(post_layer_mix))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –shape (..., hc_mult, 1), post gate for that block.

-

(`comb_res_mix`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_aiter(comb_res_mix))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –shape (..., hc_mult, hc_mult), residual comb for it.

-

(`residual_out`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_aiter(residual_out))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –shape (..., hc_mult, hidden_size), written with the post block's new residual. Required exactly when the post is folded in.


Returns:

-
(`post_mix`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (..., hc_mult, 1), dtype torch.float32

-
(`comb_mix`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (..., hc_mult, hc_mult), dtype torch.float32

-
(`layer_input`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (..., hidden_size), dtype torch.bfloat16

-
(`next_pre_mix`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (..., hc_mult), dtype torch.float32


## Source code in `vllm/model_executor/kernels/mhc/aiter.py`


##

`mhc_pre_delayed_tilelang(residual, fn, hc_scale, hc_base, rms_eps, hc_pre_eps, hc_sinkhorn_eps, hc_post_mult_value, sinkhorn_repeat, pre_mix=None, x=None, norm_weight=None, norm_eps=1e-06)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_tilelang)

Run mHC pre with a carried pre-mix and return the next pre-mix.

Parameters:

-

(`residual`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_tilelang(residual))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)BF16 residual streams of shape (tokens, hc_mult, hidden_size).

-

(`fn`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_tilelang(fn))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)FP32 projection of shape (hc_mult * (hc_mult + 2), input_size).

-

(`hc_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_tilelang(hc_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)FP32 scales of shape (3,).

-

(`hc_base`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_tilelang(hc_base))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)FP32 bias of shape (hc_mult * (hc_mult + 2),).

-

(`rms_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_tilelang(rms_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)RMS normalization epsilon.

-

(`hc_pre_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_tilelang(hc_pre_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Pre-mix epsilon.

-

(`hc_sinkhorn_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_tilelang(hc_sinkhorn_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Sinkhorn epsilon.

-

(`hc_post_mult_value`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_tilelang(hc_post_mult_value))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Post-mix multiplier.

-

(`sinkhorn_repeat`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_tilelang(sinkhorn_repeat))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of Sinkhorn iterations.

-

(`pre_mix`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_tilelang(pre_mix))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –FP32 coefficients from the previous sublayer, or None to select residual stream zero at model entry.

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_tilelang(x))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional BF16 projection input of shape (tokens, input_size), for the first layer's broadcast embedding and summed projection.

-

(`norm_weight`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_tilelang(norm_weight))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional BF16 RMSNorm weight for the collapsed input.

-

(`norm_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_tilelang(norm_eps))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)`1e-06`

) –RMSNorm epsilon for the collapsed input.


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Post and residual coefficients, optionally normalized BF16 layer input,

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)and the next FP32 pre-mix, with shapes (tokens, hc_mult, 1),

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(tokens, hc_mult, hc_mult), (tokens, hidden_size), and (tokens, hc_mult).


## Source code in `vllm/model_executor/kernels/mhc/tilelang.py`


|
|

##

`mhc_pre_delayed_torch(residual, fn, hc_scale, hc_base, rms_eps, hc_pre_eps, hc_sinkhorn_eps, hc_post_mult_value, sinkhorn_repeat, pre_mix=None, x=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_delayed_torch)

Reference for mHC pre using coefficients from the previous sublayer.

## Source code in `vllm/model_executor/kernels/mhc/torch.py`


##

`mhc_pre_mix_triton(gemm_out, sqrsum, hc_scale, hc_base, hc_mult, hc_hidden_size, rms_eps, hc_pre_eps)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_mix_triton)

Pre-mix gate for the delayed mHC pre, from AITER's split-k GEMM output.

AITER's `mhc_pre_big_fuse`

consumes the unreduced `[splitk, tokens, hc_mult3]`

GEMM output and the matching row square-sums, but only returns the post and comb gates. The delayed formulation also needs the pre gate, to carry into the next sublayer seam. It is the same slice of the same numbers, so recover it here rather than repeating the projection.

## Source code in `vllm/model_executor/kernels/mhc/triton.py`


##

`mhc_pre_tilelang(residual, fn, hc_scale, hc_base, rms_eps, hc_pre_eps, hc_sinkhorn_eps, hc_post_mult_value, sinkhorn_repeat, n_splits=1, norm_weight=None, norm_eps=1e-06)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_tilelang)

Forward pass for mHC pre block.

Parameters:

-

(`residual`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_tilelang(residual))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (..., hc_mult, hidden_size), dtype torch.bfloat16

-

(`fn`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_tilelang(fn))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (hc_mult3, hc_mult * hidden_size), dtype torch.float32

-

(`hc_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_tilelang(hc_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (3,), dtype torch.float32

-

(`hc_base`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_tilelang(hc_base))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (hc_mult3,), dtype torch.float32

-

(`rms_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_tilelang(rms_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)RMS normalization epsilon

-

(`hc_pre_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_tilelang(hc_pre_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)pre-mix epsilon

-

(`hc_sinkhorn_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_tilelang(hc_sinkhorn_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)sinkhorn epsilon

-

(`hc_post_mult_value`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_tilelang(hc_post_mult_value))

) –[float](https://docs.python.org/3/builtins/functions.html#float)post-mix multiplier value

-

(`sinkhorn_repeat`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_tilelang(sinkhorn_repeat))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of sinkhorn iterations

-

(`n_splits`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_tilelang(n_splits))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –retained for the shared MHC operator API; the active GEMM backend selects its split factor internally.

-

(`norm_weight`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_tilelang(norm_weight))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –optional RMSNorm weight, shape (hidden_size,), dtype torch.bfloat16. When provided, RMSNorm is fused into the layer_input write path of the big_fuse kernel.

-

(`norm_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_tilelang(norm_eps))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)`1e-06`

) –epsilon for the fused RMSNorm; only consulted when norm_weight is given.


Returns:

-
(`post_mix`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (..., hc_mult), dtype torch.float32

-
(`comb_mix`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (..., hc_mult, hc_mult), dtype torch.float32

-
(`layer_input`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (..., hidden_size), dtype torch.bfloat16


## Source code in `vllm/model_executor/kernels/mhc/tilelang.py`


|
|

##

`mhc_pre_torch(residual, fn, hc_scale, hc_base, rms_eps, hc_pre_eps, hc_sinkhorn_eps, hc_post_mult_value, sinkhorn_repeat, n_splits=1)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_torch)

Forward pass for mHC pre block.

Parameters:

-

(`residual`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_torch(residual))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (..., hc_mult, hidden_size), dtype torch.bfloat16

-

(`fn`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_torch(fn))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (hc_mult3, hc_mult * hidden_size), dtype torch.float32

-

(`hc_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_torch(hc_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (3,), dtype torch.float32

-

(`hc_base`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_torch(hc_base))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (hc_mult3,), dtype torch.float32

-

(`rms_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_torch(rms_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)RMS normalization epsilon

-

(`hc_pre_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_torch(hc_pre_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)pre-mix epsilon

-

(`hc_sinkhorn_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_torch(hc_sinkhorn_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)sinkhorn epsilon

-

(`hc_post_mult_value`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_torch(hc_post_mult_value))

) –[float](https://docs.python.org/3/builtins/functions.html#float)post-mix multiplier value

-

(`sinkhorn_repeat`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_torch(sinkhorn_repeat))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of sinkhorn iterations

-

(`n_splits`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.mhc_pre_torch(n_splits))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –split-k factor;


Returns:

-
(`post_mix`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (..., hc_mult), dtype torch.float32

-
(`comb_mix`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (..., hc_mult, hc_mult), dtype torch.float32

-
(`layer_input`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (..., hidden_size), dtype torch.bfloat16


## Source code in `vllm/model_executor/kernels/mhc/torch.py`


##

`rmsnorm_nw(x, eps)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.rmsnorm_nw)

Weight-free RMSNorm over the last dimension.

Treats *x* as `[num_rows, D]`

where `num_rows = product(shape[:-1])`

. Returns a contiguous tensor with the same shape and dtype as *x*.