source: https://docs.vllm.ai/en/latest/api/vllm/models/inkling/nvidia/ops/mm_towers/
lastmod: 2026-09-24

#

`vllm.models.inkling.nvidia.ops.mm_towers`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.mm_towers)

Fused CUDA kernels for the Inkling vision/audio towers.

Both kernels keep the reference paths' fp32 accumulation and per-op bf16 rounding points (native `rms_norm`

/ `F.gelu`

); outputs are frequently bit-identical and otherwise differ by 1-2 bf16 ulps from reduction-order (real-checkpoint-weight cosine vs reference > 0.9999998).

Functions:

-
–[dmel_embed_sum_norm](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.mm_towers.dmel_embed_sum_norm)`rmsnorm(sum_b weight[b * VOCAB + idx[:, b]])`

in one launch (no -
–[rmsnorm_gelu](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.mm_towers.rmsnorm_gelu)Fused

`gelu(rmsnorm(x))`

(or plain rmsnorm); multiple rows per block

##

`dmel_embed_sum_norm(dmel_idx, weight, norm_weight, eps)`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.mm_towers.dmel_embed_sum_norm)

`rmsnorm(sum_b weight[b * VOCAB + idx[:, b]])`

in one launch (no [T, NB, D] intermediate).

## Source code in `vllm/models/inkling/nvidia/ops/mm_towers.py`


##

`rmsnorm_gelu(x, weight, eps, gelu=True, fold=None)`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.mm_towers.rmsnorm_gelu)

Fused `gelu(rmsnorm(x))`

(or plain rmsnorm); multiple rows per block when D is small. With `fold`

, x must be [N, T, H, W, D] and the output comes back as `fold_timespace_to_depth(result, *fold)`

.