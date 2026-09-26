source: https://docs.vllm.ai/en/latest/api/vllm/models/inkling/amd/ops/rel_attention_decode/
lastmod: 2026-09-24

#

`vllm.models.inkling.amd.ops.rel_attention_decode`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.ops.rel_attention_decode)

Split-KV decode for Inkling relative attention on ROCm.

Adapted from LightSeek TokenSpeed's portable Triton relative-MHA decode.

Functions:

-
–[decode_split_count](https://docs.vllm.ai#vllm.models.inkling.amd.ops.rel_attention_decode.decode_split_count)Return the number of parallel KV partitions for decode.

-
–[inkling_rel_attention_split_kv_decode](https://docs.vllm.ai#vllm.models.inkling.amd.ops.rel_attention_decode.inkling_rel_attention_split_kv_decode)Run split-KV relative attention for single-token decode.

-
–[use_split_kv_decode](https://docs.vllm.ai#vllm.models.inkling.amd.ops.rel_attention_decode.use_split_kv_decode)Select split-KV only where it outperforms the single-pass kernel.


##

`decode_split_count(max_kv_len, window_left)`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.ops.rel_attention_decode.decode_split_count)

Return the number of parallel KV partitions for decode.

## Source code in `vllm/models/inkling/amd/ops/rel_attention_decode.py`


##

`inkling_rel_attention_split_kv_decode(q, key_cache, value_cache, *, block_table, cache_seqlens, softmax_scale, window_left, rel_extent, rel_logits, max_kv_len, out)`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.ops.rel_attention_decode.inkling_rel_attention_split_kv_decode)

Run split-KV relative attention for single-token decode.

## Source code in `vllm/models/inkling/amd/ops/rel_attention_decode.py`


|
|

##

`use_split_kv_decode(*, max_query_len, max_kv_len, page_size, window_left)`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.ops.rel_attention_decode.use_split_kv_decode)

Select split-KV only where it outperforms the single-pass kernel.