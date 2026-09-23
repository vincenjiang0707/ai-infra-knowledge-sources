source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/mamba/ops/ssd_combined/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.mamba.ops.ssd_combined`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssd_combined)

Functions:

-
–[mamba_chunk_scan_combined_varlen](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssd_combined.mamba_chunk_scan_combined_varlen)Argument:


##

`mamba_chunk_scan_combined_varlen(x, dt, A, B, C, chunk_size, cu_seqlens, cu_chunk_seqlens, last_chunk_indices, seq_idx, out, D=None, z=None, dt_bias=None, initial_states=None, dt_softplus=False, dt_limit=(0.0, float('inf')), return_intermediate_states=False, state_dtype=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssd_combined.mamba_chunk_scan_combined_varlen)

## Argument

x: (seqlen, nheads, headdim) dt: (seqlen, nheads) A: (nheads) B: (seqlen, ngroups, dstate) C: (seqlen, ngroups, dstate) chunk_size: int cu_seqlens: (batch + 1,) cu_chunk_seqlens: (nchunks + 1,) last_chunk_indices: (batch,) seq_idx: (nchunks,) out: (seqlen, nheads, headdim) preallocated output tensor D: (nheads, headdim) or (nheads,) z: (seqlen, nheads, headdim) dt_bias: (nheads,) initial_states: (batch, nheads, headdim, dstate) dt_softplus: Whether to apply softplus to dt out: (seqlen, nheads, headdim) preallocated output tensor state_dtype: The data type of the ssm state

Return: varlen_states: (batch, nheads, headdim, dstate)