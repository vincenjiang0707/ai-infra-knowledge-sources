source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/mhc/torch/
lastmod: 2026-09-23

#

`vllm.model_executor.kernels.mhc.torch`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.torch)

Functions:

-
–[mhc_pre_delayed_torch](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.torch.mhc_pre_delayed_torch)Reference for mHC pre using coefficients from the previous sublayer.

-
–[mhc_pre_torch](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.torch.mhc_pre_torch)Forward pass for mHC pre block.


##

`mhc_pre_delayed_torch(residual, fn, hc_scale, hc_base, rms_eps, hc_pre_eps, hc_sinkhorn_eps, hc_post_mult_value, sinkhorn_repeat, pre_mix=None, x=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.torch.mhc_pre_delayed_torch)

Reference for mHC pre using coefficients from the previous sublayer.

## Source code in `vllm/model_executor/kernels/mhc/torch.py`


##

`mhc_pre_torch(residual, fn, hc_scale, hc_base, rms_eps, hc_pre_eps, hc_sinkhorn_eps, hc_post_mult_value, sinkhorn_repeat, n_splits=1)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.torch.mhc_pre_torch)

Forward pass for mHC pre block.

Parameters:

-

(`residual`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.torch.mhc_pre_torch(residual))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (..., hc_mult, hidden_size), dtype torch.bfloat16

-

(`fn`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.torch.mhc_pre_torch(fn))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (hc_mult3, hc_mult * hidden_size), dtype torch.float32

-

(`hc_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.torch.mhc_pre_torch(hc_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (3,), dtype torch.float32

-

(`hc_base`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.torch.mhc_pre_torch(hc_base))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)shape (hc_mult3,), dtype torch.float32

-

(`rms_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.torch.mhc_pre_torch(rms_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)RMS normalization epsilon

-

(`hc_pre_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.torch.mhc_pre_torch(hc_pre_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)pre-mix epsilon

-

(`hc_sinkhorn_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.torch.mhc_pre_torch(hc_sinkhorn_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)sinkhorn epsilon

-

(`hc_post_mult_value`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.torch.mhc_pre_torch(hc_post_mult_value))

) –[float](https://docs.python.org/3/builtins/functions.html#float)post-mix multiplier value

-

(`sinkhorn_repeat`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.torch.mhc_pre_torch(sinkhorn_repeat))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of sinkhorn iterations

-

(`n_splits`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.torch.mhc_pre_torch(n_splits))

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