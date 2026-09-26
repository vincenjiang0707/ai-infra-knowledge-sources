source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/amd/ops/kda_prefill/
lastmod: 2026-09-24

#

`vllm.models.kimi_k3.amd.ops.kda_prefill`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill)

KDA prefill backend selection for ROCm.

The Kimi-K3 KDA layer calls :func:`chunk_kda_prefill`

, which either runs the fused HIP kernels in `kda_chunk`

or falls back to the vendored Triton chunk path.

Functions:

-
–[chunk_kda_prefill](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill)Run chunk KDA from raw gate and beta projections.


##

`chunk_kda_prefill(q, k, v, raw_g, raw_beta, A_log, g_bias=None, scale=None, initial_state=None, output_final_state=False, lower_bound=None, use_qk_l2norm_in_kernel=False, cu_seqlens=None, chunk_indices=None, chunk_offsets=None, use_fused_chunk=False, out=None, checkpoint_state=None, checkpoint_offsets=None, checkpoint_state_indices=None, state_cache=None, state_indices=None, has_initial_state=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill)

Run chunk KDA from raw gate and beta projections.

Parameters:

-

(`q`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill(q))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)query tensor,

`[1, T, H, K]`

. -

(`k`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill(k))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)key tensor,

`[1, T, H, K]`

. -

(`v`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill(v))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)value tensor,

`[1, T, H, V]`

. -

(`raw_g`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill(raw_g))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)raw gate projection, before the activation.

-

(`raw_beta`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill(raw_beta))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)raw beta projection, before the activation.

-

(`A_log`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill(A_log))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)log of the per-head gate decay.

-

(`g_bias`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill(g_bias))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –optional per-head gate bias.

-

(`scale`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill(scale))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)| None`None`

) –scale applied to the query-key products. Defaults to

`k.shape[-1] ** -0.5`

. -

(`initial_state`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill(initial_state))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –fp32 per-sequence initial recurrent state, or

`None`

. -

(`output_final_state`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill(output_final_state))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –whether to return the final recurrent state.

-

(`lower_bound`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill(lower_bound))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)| None`None`

) –optional floor applied to the gate.

-

(`use_qk_l2norm_in_kernel`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill(use_qk_l2norm_in_kernel))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –fold the q/k L2 norm into the kernel.

-

(`cu_seqlens`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill(cu_seqlens))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –int32 cumulative sequence lengths.

-

(`chunk_indices`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill(chunk_indices))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –precomputed chunk indices for

`cu_seqlens`

. -

(`chunk_offsets`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill(chunk_offsets))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –int32 per-sequence first chunk index.

-

(`use_fused_chunk`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill(use_fused_chunk))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –request the two-kernel ROCm path. It is used only when every one of its preconditions holds; otherwise the Triton path runs unchanged.

-

(`out`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill(out))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –buffer the result must land in. Honoured by both backends, so the caller can hand in a slice of its own output and skip a copy.

-

(`checkpoint_state`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill(checkpoint_state))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –destination for mid-prefill recurrent state snapshots, letting a later prefix-cache hit resume from a mamba block boundary. See :func:

`fused_kda_chunk`

. -

(`checkpoint_offsets`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill(checkpoint_offsets))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –per-sequence token offset to snapshot at,

`0`

for none. -

(`checkpoint_state_indices`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill(checkpoint_state_indices))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –optional per-sequence destination row.

-

(`state_cache`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill(state_cache))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –the paged recurrent state. When given, the fused backend reads and writes it in place and neither a gather nor a scatter is needed around this call; the returned final state is

`None`

. -

(`state_indices`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill(state_indices))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –per-sequence cache row.

-

(`has_initial_state`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.kda_prefill.chunk_kda_prefill(has_initial_state))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –per-sequence flag; false starts from a zero state.


Returns:

## Source code in `vllm/models/kimi_k3/amd/ops/kda_prefill.py`


|
|