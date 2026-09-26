source: https://docs.vllm.ai/en/latest/api/vllm/models/inkling/nvidia/ops/norm/
lastmod: 2026-09-24

#

`vllm.models.inkling.nvidia.ops.norm`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.norm)

Functions:

-
–[add_rmsnorm](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.norm.add_rmsnorm)Fused

`res = residual + delta; y = rmsnorm(res)`

. -
–[embed_dual_rmsnorm_cat](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.norm.embed_dual_rmsnorm_cat)The MTP depth-layer input in one launch:

-
–[embed_rmsnorm](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.norm.embed_rmsnorm)Fused

`rmsnorm(embed_table[input_ids], weight)`

row gather + norm.

##

`add_rmsnorm(residual, delta, weight, eps)`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.norm.add_rmsnorm)

Fused `res = residual + delta; y = rmsnorm(res)`

.

Returns `(y, res)`

; both are fresh tensors (cudagraph-friendly, no in-place update of the inputs).

## Source code in `vllm/models/inkling/nvidia/ops/norm.py`


##

`embed_dual_rmsnorm_cat(hidden, hidden_weight, embed_weight, eps, *, embeds=None, input_ids=None, embed_table=None, pre_norm_weight=None)`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.norm.embed_dual_rmsnorm_cat)

The MTP depth-layer input in one launch: `cat([rmsnorm(hidden, w_h), rmsnorm(pre?(emb), w_e)], -1)`

.

The embed side is either a fused row gather `embed_table[input_ids]`

(draft decode steps) or precomputed `embeds`

([T, N], the target-merged multimodal embeddings at draft prefill); `pre_norm_weight`

chains the backbone embed_norm in front of the depth embed_norm (bit-exact vs the unfused sequence). The concat copies collapse into direct writes.

## Source code in `vllm/models/inkling/nvidia/ops/norm.py`


##

`embed_rmsnorm(input_ids, embed_table, weight, eps, chain_weight=None)`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops.norm.embed_rmsnorm)

Fused `rmsnorm(embed_table[input_ids], weight)`

row gather + norm.

Requires the full vocab on-rank (replicated or tp_size == 1). `weight=None`

skips the norm (`use_embed_norm=False`

), leaving a pure embedding-table gather. `chain_weight`

additionally emits `rmsnorm(out, chain_weight)`

(the first decoder layer's pre-attention norm) as a second output, still one launch. Bit-exact vs the unfused module sequence.