source: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/fusion/rope_kvcache_fusion/
lastmod: 2026-09-24

#

`vllm.compilation.passes.fusion.rope_kvcache_fusion`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rope_kvcache_fusion)

Classes:

-
–[RopeKVCacheFusionPass](https://docs.vllm.ai#vllm.compilation.passes.fusion.rope_kvcache_fusion.RopeKVCacheFusionPass)This pass fuses the rotary embedding and KV cache update operations

-
–[RopeReshapeKVCachePattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.rope_kvcache_fusion.RopeReshapeKVCachePattern)This pattern matches the following unfused inplace ops:

-
–[RopeStaticQQuantKVCachePattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.rope_kvcache_fusion.RopeStaticQQuantKVCachePattern)Fuse rope + static Q fp8 quant while preserving explicit KV-cache update


Functions:

-
–[fused_rope_and_unified_kv_cache_update_impl](https://docs.vllm.ai#vllm.compilation.passes.fusion.rope_kvcache_fusion.fused_rope_and_unified_kv_cache_update_impl)This impl fetches the KV cache and slot mapping from the forward context,


##

`RopeKVCacheFusionPass`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rope_kvcache_fusion.RopeKVCacheFusionPass)

Bases: [VllmPatternMatcherPass](https://docs.vllm.ai/vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmPatternMatcherPass)

This pass fuses the rotary embedding and KV cache update operations into a single fused kernel if available.

It uses the pattern matcher and matches each layer manually, as strings cannot be wildcarded. This also lets us check support on attention layers upon registration instead of during pattern matching.

This fusion eliminates the need for separate kernel launches and intermediate memory operations between the RoPE and cache update steps.

## Source code in `vllm/compilation/passes/fusion/rope_kvcache_fusion.py`


##

`RopeReshapeKVCachePattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rope_kvcache_fusion.RopeReshapeKVCachePattern)

## This pattern matches the following unfused inplace ops

q, k = rotary_embedding(positions, q, k, head_size, cos_sin_cache, is_neox) kv_cache_dummy = unified_kv_cache_update(k, v, layer_name)

## and replaces it with the fused inplace op

kv_cache_dummy = fused_rope_and_unified_kv_cache_update( q, k, v, positions, cos_sin_cache, is_neox, layer_name )

## Source code in `vllm/compilation/passes/fusion/rope_kvcache_fusion.py`


|
|

###

`_mk_pattern_with_layer_name_closure(_ln)`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rope_kvcache_fusion.RopeReshapeKVCachePattern._mk_pattern_with_layer_name_closure)

Pattern/replacement with layer_name as a closure constant.

## Source code in `vllm/compilation/passes/fusion/rope_kvcache_fusion.py`


###

`_mk_pattern_with_layer_name_input(_ln)`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rope_kvcache_fusion.RopeReshapeKVCachePattern._mk_pattern_with_layer_name_input)

Pattern/replacement with layer_name as an explicit input.

## Source code in `vllm/compilation/passes/fusion/rope_kvcache_fusion.py`


##

`RopeStaticQQuantKVCachePattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rope_kvcache_fusion.RopeStaticQQuantKVCachePattern)

Fuse rope + static Q fp8 quant while preserving explicit KV-cache update dependency ordering.

## Source code in `vllm/compilation/passes/fusion/rope_kvcache_fusion.py`


|
|

##

`fused_rope_and_unified_kv_cache_update_impl(query, key, value, positions, cos_sin_cache, is_neox, layer_name)`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rope_kvcache_fusion.fused_rope_and_unified_kv_cache_update_impl)

This impl fetches the KV cache and slot mapping from the forward context, then calls the layer impl's `AttentionImpl.do_rope_and_kv_cache_update`

method. It also returns a dummy tensor, similar to `Attention.unified_kv_cache_update`

, that is passed to unified_attention to signal a side effect and the data dependency between them to ensure torch.compile preserves ordering.