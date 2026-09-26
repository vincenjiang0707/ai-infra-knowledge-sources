source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v41/common/ops/fused_layout/
lastmod: 2026-09-24

#

`vllm.models.deepseek_v41.common.ops.fused_layout`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_layout)

Weight permutations for FlashMLA's mega-attention kernel.

The kernel reads Q with 16-element head-dim chunks interleaved across heads and writes O with 32-element chunks interleaved across the 8 heads of a `wo_a`

group. Every permutation here satisfies `fused = standard[perm]`

, and is applied once to `wq_b`

rows and `wo_a`

columns at load time so the surrounding GEMMs produce and consume the kernel's layouts directly -- no per-step shuffle.

Functions:

-
–[o_fused_chunk_permutation](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_layout.o_fused_chunk_permutation)Per-32-element-chunk form of :func:

`o_fused_permutation`

, for scales. -
–[o_fused_permutation](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_layout.o_fused_permutation)`fused[(c * G + h) * 32 + j] = standard[h * D + c * 32 + j]`

per group. -
–[permute_q_to_fused](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_layout.permute_q_to_fused)`[N, H, D]`

standard layout -> the same shape in the fused layout. -
–[permute_wo_a_](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_layout.permute_wo_a_)Permute an MXFP8

`wo_a`

shard's input columns and scales, in place. -
–[permute_wq_b_](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_layout.permute_wq_b_)Permute an MXFP8

`wq_b`

shard's rows and per-row scales, in place. -
–[q_fused_permutation](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_layout.q_fused_permutation)`fused[(d // 16) * (H * 16) + h * 16 + d % 16] = standard[h * D + d]`

.

##

`_bytes_view(t)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_layout._bytes_view)

Byte view of a 1-byte-element tensor, so fp8/ue8m0 can be gathered.

##

`o_fused_chunk_permutation(heads_per_group=WV_GROUP_SIZE, head_dim=HEAD_DIM)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_layout.o_fused_chunk_permutation)

Per-32-element-chunk form of :func:`o_fused_permutation`

, for scales.

## Source code in `vllm/models/deepseek_v41/common/ops/fused_layout.py`


##

`o_fused_permutation(heads_per_group=WV_GROUP_SIZE, head_dim=HEAD_DIM)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_layout.o_fused_permutation)

`fused[(c * G + h) * 32 + j] = standard[h * D + c * 32 + j]`

per group.

## Source code in `vllm/models/deepseek_v41/common/ops/fused_layout.py`


##

`permute_q_to_fused(q)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_layout.permute_q_to_fused)

`[N, H, D]`

standard layout -> the same shape in the fused layout.

## Source code in `vllm/models/deepseek_v41/common/ops/fused_layout.py`


##

`permute_wo_a_(weight, weight_scale, heads_per_group=WV_GROUP_SIZE)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_layout.permute_wo_a_)

Permute an MXFP8 `wo_a`

shard's input columns and scales, in place.

## Source code in `vllm/models/deepseek_v41/common/ops/fused_layout.py`


##

`permute_wq_b_(weight, weight_scale, num_local_heads)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_layout.permute_wq_b_)

Permute an MXFP8 `wq_b`

shard's rows and per-row scales, in place.

## Source code in `vllm/models/deepseek_v41/common/ops/fused_layout.py`


##

`q_fused_permutation(num_heads, head_dim=HEAD_DIM)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_layout.q_fused_permutation)

`fused[(d // 16) * (H * 16) + h * 16 + d % 16] = standard[h * D + d]`

.