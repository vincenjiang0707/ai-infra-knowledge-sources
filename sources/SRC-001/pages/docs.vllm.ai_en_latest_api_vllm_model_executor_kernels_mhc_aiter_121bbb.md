source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/mhc/aiter/
lastmod: 2026-09-24

#

`vllm.model_executor.kernels.mhc.aiter`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter)

Functions:

-
–[mhc_fused_post_pre_aiter](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_fused_post_pre_aiter)Fused mHC post + next mHC pre on ROCm via AITER.

-
–[mhc_pre_aiter](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_aiter)Forward pass for mHC pre block.

-
–[mhc_pre_delayed_aiter](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_delayed_aiter)MHC pre with the pre-mix carried in from the previous sublayer.


##

`mhc_fused_post_pre_aiter(x, residual, post_layer_mix, comb_res_mix, fn, hc_scale, hc_base, rms_eps, hc_pre_eps, hc_sinkhorn_eps, hc_post_mult_value, sinkhorn_repeat, n_splits=1, tile_n=1, norm_weight=None, norm_eps=0.0)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_fused_post_pre_aiter)

Fused mHC post + next mHC pre on ROCm via AITER.

Returns residual_cur, post_mix_cur, comb_mix_cur, layer_input_cur.

## Source code in `vllm/model_executor/kernels/mhc/aiter.py`


##

`mhc_pre_aiter(residual, fn, hc_scale, hc_base, rms_eps, hc_pre_eps, hc_sinkhorn_eps, hc_post_mult_value, sinkhorn_repeat, n_splits=1, norm_weight=None, norm_eps=0.0)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_aiter)

Forward pass for mHC pre block.

Parameters:

-

(`residual`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_aiter(residual))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (..., hc_mult, hidden_size), dtype torch.bfloat16

-

(`fn`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_aiter(fn))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (hc_mult3, hc_mult * hidden_size), dtype torch.float32

-

(`hc_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_aiter(hc_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (3,), dtype torch.float32

-

(`hc_base`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_aiter(hc_base))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (hc_mult3,), dtype torch.float32

-

(`rms_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_aiter(rms_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)RMS normalization epsilon

-

(`hc_pre_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_aiter(hc_pre_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)pre-mix epsilon

-

(`hc_sinkhorn_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_aiter(hc_sinkhorn_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)sinkhorn epsilon

-

(`hc_post_mult_value`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_aiter(hc_post_mult_value))

) –[float](https://docs.python.org/3/builtins/functions.html#float)post-mix multiplier value

-

(`sinkhorn_repeat`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_aiter(sinkhorn_repeat))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of sinkhorn iterations

-

(`n_splits`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_aiter(n_splits))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –split-k factor;

-

(`norm_weight`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_aiter(norm_weight))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –optional RMSNorm weight fused into the pre kernel

-

(`norm_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_aiter(norm_eps))

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

`mhc_pre_delayed_aiter(residual, fn, hc_scale, hc_base, rms_eps, hc_pre_eps, hc_sinkhorn_eps, hc_post_mult_value, sinkhorn_repeat, pre_mix=None, sublayer_out=None, post_layer_mix=None, comb_res_mix=None, residual_out=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_delayed_aiter)

MHC pre with the pre-mix carried in from the previous sublayer.

Matches `mhc_pre_delayed_torch`

: the stream collapse uses *pre_mix* rather than the gate computed here, and that gate is returned as the pre-mix for the next sublayer seam.

Parameters:

-

(`residual`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_delayed_aiter(residual))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (..., hc_mult, hidden_size), dtype torch.bfloat16

-

(`fn`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_delayed_aiter(fn))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (hc_mult3, hc_mult * hidden_size), dtype torch.float32

-

(`hc_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_delayed_aiter(hc_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (3,), dtype torch.float32

-

(`hc_base`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_delayed_aiter(hc_base))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (hc_mult3,), dtype torch.float32

-

(`rms_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_delayed_aiter(rms_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)RMS normalization epsilon

-

(`hc_pre_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_delayed_aiter(hc_pre_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)pre-mix epsilon

-

(`hc_sinkhorn_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_delayed_aiter(hc_sinkhorn_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)sinkhorn epsilon

-

(`hc_post_mult_value`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_delayed_aiter(hc_post_mult_value))

) –[float](https://docs.python.org/3/builtins/functions.html#float)post-mix multiplier value

-

(`sinkhorn_repeat`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_delayed_aiter(sinkhorn_repeat))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of sinkhorn iterations

-

(`pre_mix`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_delayed_aiter(pre_mix))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –shape (..., hc_mult) from the previous sublayer, or None at model entry to select residual stream zero.

-

(`sublayer_out`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_delayed_aiter(sublayer_out))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –attention or FFN output, shape (..., hidden_size). When given with the two mixes below, the preceding post block is applied here so AITER can fold it into the pre projection.

-

(`post_layer_mix`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_delayed_aiter(post_layer_mix))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –shape (..., hc_mult, 1), post gate for that block.

-

(`comb_res_mix`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_delayed_aiter(comb_res_mix))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –shape (..., hc_mult, hc_mult), residual comb for it.

-

(`residual_out`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.aiter.mhc_pre_delayed_aiter(residual_out))

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