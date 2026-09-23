source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/amd/ops/third_party/kda/chunk/
lastmod: 2026-09-23

#

`vllm.models.kimi_k3.amd.ops.third_party.kda.chunk`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.third_party.kda.chunk)

Functions:

-
–[chunk_kda_with_fused_gate](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.third_party.kda.chunk.chunk_kda_with_fused_gate)Run chunk KDA from raw gate and beta projections.

-
–[fused_kda_gate](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.third_party.kda.chunk.fused_kda_gate)Forward pass for KDA gate:


##

`chunk_kda_with_fused_gate(q, k, v, raw_g, raw_beta, A_log, g_bias, scale=None, initial_state=None, output_final_state=False, lower_bound=None, use_qk_l2norm_in_kernel=False, cu_seqlens=None, chunk_indices=None, chunk_offsets=None, **kwargs)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.third_party.kda.chunk.chunk_kda_with_fused_gate)

Run chunk KDA from raw gate and beta projections.

## Source code in `vllm/models/kimi_k3/amd/ops/third_party/kda/chunk.py`


##

`fused_kda_gate(g, A, head_k_dim, g_bias=None, beta=1.0, threshold=20.0, lower_bound=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.third_party.kda.chunk.fused_kda_gate)

Forward pass for KDA gate: input g: [..., H*D] param A: [H] or [1, 1, H, 1] beta: softplus beta parameter threshold: softplus threshold parameter return : [..., H, D]