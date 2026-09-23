source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/mamba/ops/gdn_chunk_cutedsl/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.mamba.ops.gdn_chunk_cutedsl`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.gdn_chunk_cutedsl)

Modules:

Functions:

-
–[chunk_gated_delta_rule_cutedsl](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.gdn_chunk_cutedsl.chunk_gated_delta_rule_cutedsl)Run the GDN chunk CuteDSL prefill kernels.


##

`chunk_gated_delta_rule_cutedsl(q, k, v, g, beta, initial_state, cu_seqlens, chunk_indices, chunk_offsets, core_attn_out=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.gdn_chunk_cutedsl.chunk_gated_delta_rule_cutedsl)

Run the GDN chunk CuteDSL prefill kernels.

Parameters:

-

(`q`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.gdn_chunk_cutedsl.chunk_gated_delta_rule_cutedsl(q))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Query tensor with shape

`[1, T, H, K]`

. -

(`k`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.gdn_chunk_cutedsl.chunk_gated_delta_rule_cutedsl(k))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Key tensor with shape

`[1, T, H, K]`

. -

(`v`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.gdn_chunk_cutedsl.chunk_gated_delta_rule_cutedsl(v))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Value tensor with shape

`[1, T, Hv, V]`

. -

(`g`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.gdn_chunk_cutedsl.chunk_gated_delta_rule_cutedsl(g))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Log-space decay tensor with shape

`[1, T, Hv]`

. -

(`beta`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.gdn_chunk_cutedsl.chunk_gated_delta_rule_cutedsl(beta))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Delta-rule beta tensor with shape

`[1, T, Hv]`

. -

(`initial_state`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.gdn_chunk_cutedsl.chunk_gated_delta_rule_cutedsl(initial_state))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Recurrent state with shape

`[N, Hv, V, K]`

. -

(`cu_seqlens`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.gdn_chunk_cutedsl.chunk_gated_delta_rule_cutedsl(cu_seqlens))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Cumulative sequence lengths with shape

`[N + 1]`

. -

(`chunk_indices`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.gdn_chunk_cutedsl.chunk_gated_delta_rule_cutedsl(chunk_indices))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Chunk index metadata with shape

`[NT, 2]`

. -

(`chunk_offsets`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.gdn_chunk_cutedsl.chunk_gated_delta_rule_cutedsl(chunk_offsets))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Cumulative chunk offsets with shape

`[N + 1]`

. -

(`core_attn_out`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.gdn_chunk_cutedsl.chunk_gated_delta_rule_cutedsl(core_attn_out))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional output buffer with shape

`[T, Hv, V]`

.

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)A tuple

`(output, final_state)`

where`output`

has shape -

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`[1, T, Hv, V]`

and`final_state`

has shape`[N, Hv, V, K]`

. -

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]When

`core_attn_out`

is provided,`output`

is an unsqueezed view of -

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]that buffer.


## Source code in `vllm/model_executor/layers/mamba/ops/gdn_chunk_cutedsl/__init__.py`


|
|