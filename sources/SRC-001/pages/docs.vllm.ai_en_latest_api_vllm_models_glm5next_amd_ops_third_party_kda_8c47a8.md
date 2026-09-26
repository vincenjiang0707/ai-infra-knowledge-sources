source: https://docs.vllm.ai/en/latest/api/vllm/models/glm5next/amd/ops/third_party/kda/
lastmod: 2026-09-24

#

`vllm.models.glm5next.amd.ops.third_party.kda`

[¶](https://docs.vllm.ai#vllm.models.glm5next.amd.ops.third_party.kda)

Modules:

Functions:

-
–[chunk_kda_with_fused_gate](https://docs.vllm.ai#vllm.models.glm5next.amd.ops.third_party.kda.chunk_kda_with_fused_gate)Run chunk KDA from raw gate projection using fused gate+cumsum.


##

`chunk_kda_with_fused_gate(q, k, v, raw_g, beta, A_log, g_bias, scale=None, initial_state=None, output_final_state=False, use_qk_l2norm_in_kernel=False, cu_seqlens=None, safe_gate=False, lower_bound=-5.0, **kwargs)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.amd.ops.third_party.kda.chunk_kda_with_fused_gate)

Run chunk KDA from raw gate projection using fused gate+cumsum.