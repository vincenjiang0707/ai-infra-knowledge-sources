source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/attention/encoder_only_attention/
lastmod: 2026-09-24

Bases: [Attention](../#vllm.model_executor.layers.attention.Attention)


Encoder attention is a special case that doesn't need a KV Cache.

## Source code in `vllm/model_executor/layers/attention/encoder_only_attention.py`


| class EncoderOnlyAttention(Attention):
"""Encoder attention is a special case that doesn't need a KV Cache."""
def __init__(
self,
num_heads: int,
head_size: int,
scale: float,
cache_config: CacheConfig | None = None,
attn_type: str | None = None,
**kwargs,
):
dtype = torch.get_default_dtype()
if cache_config is not None:
kv_cache_dtype = cache_config.cache_dtype
else:
kv_cache_dtype = "auto"
underlying_attn_backend = get_attn_backend(
head_size,
dtype,
kv_cache_dtype,
attn_type=AttentionType.ENCODER_ONLY,
)
attn_backend = create_encoder_only_attention_backend(underlying_attn_backend)
if attn_type is not None:
assert attn_type == AttentionType.ENCODER_ONLY, (
"EncoderOnlyAttention only supports AttentionType.ENCODER_ONLY"
)
super().__init__(
num_heads=num_heads,
head_size=head_size,
scale=scale,
cache_config=cache_config,
attn_backend=attn_backend,
attn_type=AttentionType.ENCODER_ONLY,
**kwargs,
)
def get_kv_cache_spec(self, vllm_config: VllmConfig) -> KVCacheSpec | None:
# Does not need KV cache
return None
|