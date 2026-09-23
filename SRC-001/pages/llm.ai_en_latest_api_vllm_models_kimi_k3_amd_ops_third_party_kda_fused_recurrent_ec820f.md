source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/amd/ops/third_party/kda/fused_recurrent/
lastmod: 2026-09-23

#

`vllm.models.kimi_k3.amd.ops.third_party.kda.fused_recurrent`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.third_party.kda.fused_recurrent)

Functions:

-
–[fused_recurrent_kda](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.third_party.kda.fused_recurrent.fused_recurrent_kda)Run recurrent KDA from raw gate and beta inputs.

-
–[fused_recurrent_kda_fwd](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.third_party.kda.fused_recurrent.fused_recurrent_kda_fwd)Launch recurrent KDA with dense inner dimensions and row strides.

-
–[fused_recurrent_kda_packed_decode](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.third_party.kda.fused_recurrent.fused_recurrent_kda_packed_decode)Run one-token KDA decode directly from packed post-conv QKV.


##

`fused_recurrent_kda(q, k, v, raw_g, raw_beta, A_log, dt_bias, lower_bound, initial_state, cu_seqlens, ssm_state_indices, num_accepted_tokens=None, out=None, fuse_gate=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.third_party.kda.fused_recurrent.fused_recurrent_kda)

Run recurrent KDA from raw gate and beta inputs.

This vLLM wrapper applies the gate activation and beta sigmoid, selecting whether to materialize them before launching the recurrent kernel.

## Source code in `vllm/models/kimi_k3/amd/ops/third_party/kda/fused_recurrent.py`


##

`fused_recurrent_kda_fwd(q, k, v, g, beta, scale=None, initial_state=None, inplace_final_state=True, cu_seqlens=None, ssm_state_indices=None, num_accepted_tokens=None, use_qk_l2norm_in_kernel=True, A_log=None, dt_bias=None, lower_bound=None, use_gate_in_kernel=False, use_beta_sigmoid_in_kernel=False, out=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.third_party.kda.fused_recurrent.fused_recurrent_kda_fwd)

Launch recurrent KDA with dense inner dimensions and row strides.

## Source code in `vllm/models/kimi_k3/amd/ops/third_party/kda/fused_recurrent.py`


|
|

##

`fused_recurrent_kda_packed_decode(mixed_qkv, raw_g, raw_beta, A_log, dt_bias, lower_bound, initial_state, state_indices, scale=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.ops.third_party.kda.fused_recurrent.fused_recurrent_kda_packed_decode)

Run one-token KDA decode directly from packed post-conv QKV.

## Source code in `vllm/models/kimi_k3/amd/ops/third_party/kda/fused_recurrent.py`


|
|