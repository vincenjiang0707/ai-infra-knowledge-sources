source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/mhc/tilelang/
lastmod: 2026-09-23

#

`vllm.model_executor.kernels.mhc.tilelang`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang)

Functions:

-
–[hc_head_fused_kernel_tilelang](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.hc_head_fused_kernel_tilelang)Apply the fused hc_head kernel and return the (T, H) bf16 result.

-
–[mhc_fused_post_pre_delayed_tilelang](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_fused_post_pre_delayed_tilelang)Run one mHC post block followed by the next delayed mHC pre block.

-
–[mhc_fused_post_pre_tilelang](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_fused_post_pre_tilelang)Run one MHC post block followed by the next MHC pre block.

-
–[mhc_pre_broadcast_tilelang](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_broadcast_tilelang)First-layer mHC pre for a residual broadcast from

`(T, H)`

. -
–[mhc_pre_delayed_tilelang](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_delayed_tilelang)Run mHC pre with a carried pre-mix and return the next pre-mix.

-
–[mhc_pre_tilelang](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_tilelang)Forward pass for mHC pre block.


##

`hc_head_fused_kernel_tilelang(hs_flat, fn, hc_scale, hc_base, rms_eps, hc_eps)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.hc_head_fused_kernel_tilelang)

Apply the fused hc_head kernel and return the (T, H) bf16 result.

## Source code in `vllm/model_executor/kernels/mhc/tilelang.py`


##

`mhc_fused_post_pre_delayed_tilelang(x, residual, post_layer_mix, comb_res_mix, fn, hc_scale, hc_base, rms_eps, hc_pre_eps, hc_sinkhorn_eps, hc_post_mult_value, sinkhorn_repeat, pre_mix=None, norm_weight=None, norm_eps=1e-06, capture_aux=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_fused_post_pre_delayed_tilelang)

Run one mHC post block followed by the next delayed mHC pre block.

Within the fused kernel's token range the post mapping is folded into the pre-norm GEMM, so the updated residual streams feed the projection from registers instead of a second pass over global memory. Above it this runs the same post kernel and split-k GEMM as the unfused pair.

Parameters:

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_fused_post_pre_delayed_tilelang(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)BF16 sublayer output of shape (tokens, hidden_size).

-

(`residual`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_fused_post_pre_delayed_tilelang(residual))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)BF16 residual streams of shape (tokens, hc_mult, hidden_size).

-

(`post_layer_mix`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_fused_post_pre_delayed_tilelang(post_layer_mix))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)FP32 post coefficients of shape (tokens, hc_mult, 1).

-

(`comb_res_mix`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_fused_post_pre_delayed_tilelang(comb_res_mix))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)FP32 residual coefficients, (tokens, hc_mult, hc_mult).

-

(`fn`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_fused_post_pre_delayed_tilelang(fn))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)FP32 projection of shape (hc_mult * (hc_mult + 2), input_size).

-

(`hc_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_fused_post_pre_delayed_tilelang(hc_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)FP32 scales of shape (3,).

-

(`hc_base`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_fused_post_pre_delayed_tilelang(hc_base))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)FP32 bias of shape (hc_mult * (hc_mult + 2),).

-

(`rms_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_fused_post_pre_delayed_tilelang(rms_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)RMS normalization epsilon.

-

(`hc_pre_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_fused_post_pre_delayed_tilelang(hc_pre_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Pre-mix epsilon.

-

(`hc_sinkhorn_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_fused_post_pre_delayed_tilelang(hc_sinkhorn_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Sinkhorn epsilon.

-

(`hc_post_mult_value`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_fused_post_pre_delayed_tilelang(hc_post_mult_value))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Post-mix multiplier.

-

(`sinkhorn_repeat`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_fused_post_pre_delayed_tilelang(sinkhorn_repeat))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of Sinkhorn iterations.

-

(`pre_mix`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_fused_post_pre_delayed_tilelang(pre_mix))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –FP32 coefficients from the previous sublayer, or None to select residual stream zero.

-

(`norm_weight`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_fused_post_pre_delayed_tilelang(norm_weight))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional BF16 RMSNorm weight for the collapsed input.

-

(`norm_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_fused_post_pre_delayed_tilelang(norm_eps))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)`1e-06`

) –RMSNorm epsilon for the collapsed input.

-

(`capture_aux`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_fused_post_pre_delayed_tilelang(capture_aux))

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

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_fused_post_pre_tilelang)

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

`mhc_pre_broadcast_tilelang(residual, fn, hc_scale, hc_base, rms_eps, hc_pre_eps, hc_sinkhorn_eps, hc_post_mult_value, sinkhorn_repeat, n_splits=1, norm_weight=None, norm_eps=1e-06, fn_broadcast=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_broadcast_tilelang)

First-layer mHC pre for a residual broadcast from `(T, H)`

.

## Source code in `vllm/model_executor/kernels/mhc/tilelang.py`


|
|

##

`mhc_pre_delayed_tilelang(residual, fn, hc_scale, hc_base, rms_eps, hc_pre_eps, hc_sinkhorn_eps, hc_post_mult_value, sinkhorn_repeat, pre_mix=None, x=None, norm_weight=None, norm_eps=1e-06)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_delayed_tilelang)

Run mHC pre with a carried pre-mix and return the next pre-mix.

Parameters:

-

(`residual`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_delayed_tilelang(residual))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)BF16 residual streams of shape (tokens, hc_mult, hidden_size).

-

(`fn`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_delayed_tilelang(fn))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)FP32 projection of shape (hc_mult * (hc_mult + 2), input_size).

-

(`hc_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_delayed_tilelang(hc_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)FP32 scales of shape (3,).

-

(`hc_base`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_delayed_tilelang(hc_base))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)FP32 bias of shape (hc_mult * (hc_mult + 2),).

-

(`rms_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_delayed_tilelang(rms_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)RMS normalization epsilon.

-

(`hc_pre_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_delayed_tilelang(hc_pre_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Pre-mix epsilon.

-

(`hc_sinkhorn_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_delayed_tilelang(hc_sinkhorn_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Sinkhorn epsilon.

-

(`hc_post_mult_value`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_delayed_tilelang(hc_post_mult_value))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Post-mix multiplier.

-

(`sinkhorn_repeat`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_delayed_tilelang(sinkhorn_repeat))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of Sinkhorn iterations.

-

(`pre_mix`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_delayed_tilelang(pre_mix))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –FP32 coefficients from the previous sublayer, or None to select residual stream zero at model entry.

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_delayed_tilelang(x))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional BF16 projection input of shape (tokens, input_size), for the first layer's broadcast embedding and summed projection.

-

(`norm_weight`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_delayed_tilelang(norm_weight))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional BF16 RMSNorm weight for the collapsed input.

-

(`norm_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_delayed_tilelang(norm_eps))

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

`mhc_pre_tilelang(residual, fn, hc_scale, hc_base, rms_eps, hc_pre_eps, hc_sinkhorn_eps, hc_post_mult_value, sinkhorn_repeat, n_splits=1, norm_weight=None, norm_eps=1e-06)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_tilelang)

Forward pass for mHC pre block.

Parameters:

-

(`residual`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_tilelang(residual))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (..., hc_mult, hidden_size), dtype torch.bfloat16

-

(`fn`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_tilelang(fn))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (hc_mult3, hc_mult * hidden_size), dtype torch.float32

-

(`hc_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_tilelang(hc_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (3,), dtype torch.float32

-

(`hc_base`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_tilelang(hc_base))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (hc_mult3,), dtype torch.float32

-

(`rms_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_tilelang(rms_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)RMS normalization epsilon

-

(`hc_pre_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_tilelang(hc_pre_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)pre-mix epsilon

-

(`hc_sinkhorn_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_tilelang(hc_sinkhorn_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)sinkhorn epsilon

-

(`hc_post_mult_value`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_tilelang(hc_post_mult_value))

) –[float](https://docs.python.org/3/builtins/functions.html#float)post-mix multiplier value

-

(`sinkhorn_repeat`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_tilelang(sinkhorn_repeat))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of sinkhorn iterations

-

(`n_splits`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_tilelang(n_splits))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –retained for the shared MHC operator API; the active GEMM backend selects its split factor internally.

-

(`norm_weight`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_tilelang(norm_weight))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –optional RMSNorm weight, shape (hidden_size,), dtype torch.bfloat16. When provided, RMSNorm is fused into the layer_input write path of the big_fuse kernel.

-

(`norm_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.tilelang.mhc_pre_tilelang(norm_eps))

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