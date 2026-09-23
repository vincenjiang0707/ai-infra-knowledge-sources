source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/nvidia/ops/third_party/kda/
lastmod: 2026-09-23

#

`vllm.models.kimi_k3.nvidia.ops.third_party.kda`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.third_party.kda)

Modules:

Functions:

-
–[chunk_kda_with_fused_gate](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.third_party.kda.chunk_kda_with_fused_gate)Run chunk KDA from raw gate and beta projections.

-
–[fused_kda_gate](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.third_party.kda.fused_kda_gate)Forward pass for KDA gate:

-
–[fused_recurrent_kda](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.third_party.kda.fused_recurrent_kda)Run recurrent KDA from raw gate and beta inputs.

-
–[fused_recurrent_kda_fwd](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.third_party.kda.fused_recurrent_kda_fwd)Launch recurrent KDA with dense inner dimensions and row strides.

-
–[fused_recurrent_kda_packed_decode](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.third_party.kda.fused_recurrent_kda_packed_decode)Run one-token KDA decode directly from packed post-conv QKV.


##

`chunk_kda_with_fused_gate(q, k, v, raw_g, raw_beta, A_log, g_bias, scale=None, initial_state=None, output_final_state=False, lower_bound=None, use_qk_l2norm_in_kernel=False, cu_seqlens=None, out=None, **kwargs)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.third_party.kda.chunk_kda_with_fused_gate)

Run chunk KDA from raw gate and beta projections.

## Source code in `vllm/models/kimi_k3/nvidia/ops/third_party/kda/chunk.py`


##

`fused_kda_gate(g, A, head_k_dim, g_bias=None, beta=1.0, threshold=20.0, lower_bound=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.third_party.kda.fused_kda_gate)

Forward pass for KDA gate: input g: [..., H*D] param A: [H] or [1, 1, H, 1] beta: softplus beta parameter threshold: softplus threshold parameter return : [..., H, D]

## Source code in `vllm/models/kimi_k3/nvidia/ops/third_party/kda/chunk.py`


##

`fused_recurrent_kda(q, k, v, raw_g, raw_beta, A_log, dt_bias, lower_bound, initial_state, cu_seqlens, ssm_state_indices, num_accepted_tokens=None, out=None, fuse_gate=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.third_party.kda.fused_recurrent_kda)

Run recurrent KDA from raw gate and beta inputs.

This vLLM wrapper applies the gate activation and beta sigmoid, selecting whether to materialize them before launching the recurrent kernel.

## Source code in `vllm/models/kimi_k3/nvidia/ops/third_party/kda/fused_recurrent.py`


##

`fused_recurrent_kda_fwd(q, k, v, g, beta, scale=None, initial_state=None, inplace_final_state=True, cu_seqlens=None, ssm_state_indices=None, num_accepted_tokens=None, use_qk_l2norm_in_kernel=True, A_log=None, dt_bias=None, lower_bound=None, use_gate_in_kernel=False, use_beta_sigmoid_in_kernel=False, out=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.third_party.kda.fused_recurrent_kda_fwd)

Launch recurrent KDA with dense inner dimensions and row strides.

## Source code in `vllm/models/kimi_k3/nvidia/ops/third_party/kda/fused_recurrent.py`


|
|

##

`fused_recurrent_kda_packed_decode(mixed_qkv, raw_g, raw_beta, A_log, dt_bias, lower_bound, initial_state, state_indices, scale=None, out=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.third_party.kda.fused_recurrent_kda_packed_decode)

Run one-token KDA decode directly from packed post-conv QKV.

## Source code in `vllm/models/kimi_k3/nvidia/ops/third_party/kda/fused_recurrent.py`


|
|