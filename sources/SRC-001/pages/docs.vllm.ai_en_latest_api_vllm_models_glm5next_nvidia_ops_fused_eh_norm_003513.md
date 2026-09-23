source: https://docs.vllm.ai/en/latest/api/vllm/models/glm5next/nvidia/ops/fused_eh_norm/
lastmod: 2026-09-23

#

`vllm.models.glm5next.nvidia.ops.fused_eh_norm`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.fused_eh_norm)

Functions:

-
–[fused_eh_norm](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.fused_eh_norm.fused_eh_norm)Returns cat([enorm(masked embeds), hnorm(prev_hidden)]) -> [N, 2H].


##

`_fused_eh_norm_kernel(pos_ptr, embeds_ptr, embeds_stride, prev_ptr, prev_stride, enorm_w_ptr, hnorm_w_ptr, eps, out_ptr, out_stride, H, BLOCK)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.fused_eh_norm._fused_eh_norm_kernel)

MTP input fusion: zero embeds at position 0, RMSNorm(embeds) with enorm and RMSNorm(prev_hidden) with hnorm, written side-by-side into `out`

([N, 2H]) ready for the eh_proj GEMM. Replaces where + 2x RMSNorm + cat.

## Source code in `vllm/models/glm5next/nvidia/ops/fused_eh_norm.py`


##

`fused_eh_norm(positions, inputs_embeds, previous_hidden, enorm_w, hnorm_w, eps)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.fused_eh_norm.fused_eh_norm)

Returns cat([enorm(masked embeds), hnorm(prev_hidden)]) -> [N, 2H].