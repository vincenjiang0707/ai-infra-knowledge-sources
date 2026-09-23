source: https://docs.vllm.ai/en/latest/api/vllm/models/glm5next/nvidia/ops/third_party/kda/kernels/
lastmod: 2026-09-23

#

`vllm.models.glm5next.nvidia.ops.third_party.kda.kernels`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.kernels)

Functions:

-
–[chunk_kda_scaled_dot_kkt_fwd](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.kernels.chunk_kda_scaled_dot_kkt_fwd)Compute beta * K * K^T.

-
–[chunk_kda_with_fused_gate](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.kernels.chunk_kda_with_fused_gate)Run chunk KDA from raw gate projection using fused gate+cumsum.

-
–[fused_kda_gate](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.kernels.fused_kda_gate)Forward pass for KDA gate:


##

`chunk_kda_scaled_dot_kkt_fwd(q, k, gk=None, beta=None, scale=None, cu_seqlens=None, chunk_indices=None, chunk_size=FLA_CHUNK_SIZE, output_dtype=torch.float32)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.kernels.chunk_kda_scaled_dot_kkt_fwd)

Compute beta * K * K^T.

Parameters:

-

(`q`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.kernels.chunk_kda_scaled_dot_kkt_fwd(q))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The query tensor of shape

`[B, T, H, K]`

. -

(`k`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.kernels.chunk_kda_scaled_dot_kkt_fwd(k))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The key tensor of shape

`[B, T, H, K]`

. -

(`beta`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.kernels.chunk_kda_scaled_dot_kkt_fwd(beta))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`None`

) –The beta tensor of shape

`[B, T, H]`

. -

(`gk`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.kernels.chunk_kda_scaled_dot_kkt_fwd(gk))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`None`

) –The cumulative sum of the gate tensor of shape

`[B, T, H, K]`

applied to the key tensor. Default:`None`

. -

(`scale`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.kernels.chunk_kda_scaled_dot_kkt_fwd(scale))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)`None`

) –Scale applied to the query-key products. Default:

`None`

. -

(`cu_seqlens`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.kernels.chunk_kda_scaled_dot_kkt_fwd(cu_seqlens))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`None`

) –The cumulative sequence lengths of the input tensor. Default: None

-

(`chunk_indices`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.kernels.chunk_kda_scaled_dot_kkt_fwd(chunk_indices))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`None`

) –Precomputed chunk indices for

`cu_seqlens`

. Default:`None`

. -

(`chunk_size`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.kernels.chunk_kda_scaled_dot_kkt_fwd(chunk_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`FLA_CHUNK_SIZE`

) –The chunk size. Default: 64.

-

(`output_dtype`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.kernels.chunk_kda_scaled_dot_kkt_fwd(output_dtype))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)`float32`

) –The dtype of the output tensor. Default:

`torch.float32`


Returns:

## Source code in `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py`


|
|

##

`chunk_kda_with_fused_gate(q, k, v, raw_g, beta, A_log, g_bias, scale=None, initial_state=None, output_final_state=False, use_qk_l2norm_in_kernel=False, cu_seqlens=None, safe_gate=False, lower_bound=-5.0, **kwargs)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.kernels.chunk_kda_with_fused_gate)

Run chunk KDA from raw gate projection using fused gate+cumsum.

## Source code in `vllm/models/glm5next/nvidia/ops/third_party/kda/kernels.py`


##

`fused_kda_gate(g, A, head_k_dim, g_bias=None, beta=1.0, threshold=20.0, safe_gate=False, lower_bound=-5.0)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.kernels.fused_kda_gate)

Forward pass for KDA gate: input g: [..., H*D] param A: [H] or [1, 1, H, 1] beta: softplus beta parameter (softplus branch only) threshold: softplus threshold parameter (softplus branch only) safe_gate: when False (default) compute y = -exp(A)*softplus(g+g_bias); when True compute the bounded y = lower_bound*sigmoid(exp(A)*(g+g_bias)) lower_bound: floor for the safe_gate branch (default -5.0) return : [..., H, D]