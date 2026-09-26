source: https://docs.vllm.ai/en/latest/api/vllm/config/attention/
lastmod: 2026-09-24

#

`vllm.config.attention`

[¶](https://docs.vllm.ai#vllm.config.attention)

Classes:

-
–[AttentionConfig](https://docs.vllm.ai#vllm.config.attention.AttentionConfig)Configuration for attention mechanisms in vLLM.

-
–[HiSparseConfig](https://docs.vllm.ai#vllm.config.attention.HiSparseConfig)Configuration for HiSparse sparse-MLA KV offloading.


##

`AttentionConfig`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig)

Configuration for attention mechanisms in vLLM.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.compute_hash)Provide a hash that uniquely identifies all the configs

-
–[resolve_indexer_kv_dtype](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.resolve_indexer_kv_dtype)Resolve

`indexer_kv_dtype`

, substituting`default`

for "auto". -
–[validate_backend_before](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.validate_backend_before)Enable parsing of the

`backend`

enum type from string. -
–[validate_backend_per_kind_before](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.validate_backend_per_kind_before)Parse the

`backend_per_kind`

map from strings. -
–[validate_mla_prefill_backend_before](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.validate_mla_prefill_backend_before)Enable parsing of the

`mla_prefill_backend`

enum type from string.

Attributes:

-
([backend](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.backend)

) –[AttentionBackendEnum](https://docs.vllm.ai/v1/attention/backends/registry/#vllm.v1.attention.backends.registry.AttentionBackendEnum)| NoneAttention backend to use. Use "auto" or None for automatic selection.

-
([backend_per_kind](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.backend_per_kind)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[AttentionBackendEnum](https://docs.vllm.ai/v1/attention/backends/registry/#vllm.v1.attention.backends.registry.AttentionBackendEnum)]Per-KV-cache-group attention backend overrides, keyed by

-
([disable_flashinfer_q_quantization](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.disable_flashinfer_q_quantization)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If set, when using fp8 kv, do not quantize Q to fp8.

-
([flash_attn_max_num_splits_for_cuda_graph](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.flash_attn_max_num_splits_for_cuda_graph)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Flash Attention max number splits for cuda graph decode.

-
([flash_attn_version](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.flash_attn_version)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)[2, 3, 4] | NoneForce vllm to use a specific flash-attention version (2, 3, or 4).

-
([flex_attn_block_m](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.flex_attn_block_m)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneTriton kernel BLOCK_M tile size for flex attention.

-
([flex_attn_block_n](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.flex_attn_block_n)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneTriton kernel BLOCK_N tile size for flex attention.

-
([flex_attn_kv_block_size](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.flex_attn_kv_block_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneLogical KV block size for the flex attention block mask.

-
([flex_attn_q_block_size](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.flex_attn_q_block_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneLogical Q block size for the flex attention block mask.

-
([hisparse_config](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.hisparse_config)

) –[HiSparseConfig](https://docs.vllm.ai#vllm.config.attention.HiSparseConfig)| NoneHiSparse host-resident KV configuration. Setting this enables experimental

-
([indexer_kv_dtype](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.indexer_kv_dtype)`IndexerKVDType`

) –Data type for the sparse-attention indexer K cache. "auto" picks the

-
([indexer_sparse_logits](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.indexer_sparse_logits)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)DeepSeek V4.1 two-level indexer: score only the candidate blocks with

-
([minimax_m3_msa_decode_backend](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.minimax_m3_msa_decode_backend)`MiniMaxM3MSADecodeBackend`

) –Sparse decode kernel used by the MiniMax M3 MSA backend.

-
([mla_prefill_backend](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.mla_prefill_backend)

) –[MLAPrefillBackendEnum](https://docs.vllm.ai/v1/attention/backends/mla/prefill/registry/#vllm.v1.attention.backends.mla.prefill.registry.MLAPrefillBackendEnum)| NoneMLA prefill backend to use. If None, will be selected automatically.

-
([sparse_mla_force_mqa](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.sparse_mla_force_mqa)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Force sparse MLA to use forward_mqa for all requests, including prefill.

-
([tq_max_kv_splits_for_cuda_graph](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.tq_max_kv_splits_for_cuda_graph)

) –[int](https://docs.python.org/3/builtins/functions.html#int)TurboQuant max NUM_KV_SPLITS for cuda graph decode.

-
([use_non_causal](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.use_non_causal)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to use non-causal (bidirectional) attention.

-
([use_prefill_query_quantization](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.use_prefill_query_quantization)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If set, quantize query for attention in prefill.

-
([use_trtllm_attention](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.use_trtllm_attention)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneIf set to True/False, use or don't use the TRTLLM attention backend


## Source code in `vllm/config/attention.py`


|
|

###

`backend = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.backend)

Attention backend to use. Use "auto" or None for automatic selection.

###

`backend_per_kind = field(default_factory=dict)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.backend_per_kind)

Per-KV-cache-group attention backend overrides, keyed by `KVCacheSpecKind`

(e.g. `{"mla_attention": "FLASHINFER_MLA", "sliding_window_mla": "TRITON_MLA"}`

). This lets a model that splits its layers across multiple KV-cache groups (e.g. interleaved full and sliding-window attention) use a different backend per group.

An entry overrides `backend`

for layers of the matching kind; kinds not listed fall back to `backend`

(or automatic selection). A selected backend that is invalid for that kind raises at startup.

###

`disable_flashinfer_q_quantization = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.disable_flashinfer_q_quantization)

If set, when using fp8 kv, do not quantize Q to fp8.

###

`flash_attn_max_num_splits_for_cuda_graph = 32`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.flash_attn_max_num_splits_for_cuda_graph)

Flash Attention max number splits for cuda graph decode.

###

`flash_attn_version = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.flash_attn_version)

Force vllm to use a specific flash-attention version (2, 3, or 4). Only valid when using the flash-attention backend.

###

`flex_attn_block_m = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.flex_attn_block_m)

Triton kernel BLOCK_M tile size for flex attention. Must be a power of 2 >= 16. If None and VLLM_BATCH_INVARIANT=1, defaults to 16.

###

`flex_attn_block_n = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.flex_attn_block_n)

Triton kernel BLOCK_N tile size for flex attention. Must be a power of 2 >= 16. If None and VLLM_BATCH_INVARIANT=1, defaults to 16.

###

`flex_attn_kv_block_size = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.flex_attn_kv_block_size)

Logical KV block size for the flex attention block mask. Must be a power of 2 and divisible by flex_attn_block_n. If None, uses the KV cache block size for paged KV attention on PyTorch >= 2.9, and 128 for encoder-only attention or older PyTorch versions.

###

`flex_attn_q_block_size = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.flex_attn_q_block_size)

Logical Q block size for the flex attention block mask. Must be a power of 2 and divisible by flex_attn_block_m. If None, uses 16 for paged KV attention on PyTorch >= 2.9, and 128 for encoder-only attention or older PyTorch versions.

###

`hisparse_config = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.hisparse_config)

HiSparse host-resident KV configuration. Setting this enables experimental Model Runner V2-only HiSparse sparse-MLA decode hot-buffering. It is inferred with defaults when HiSparseConnector is configured (directly or via MultiConnector); set it explicitly only to tune its fields.

###

`indexer_kv_dtype = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.indexer_kv_dtype)

Data type for the sparse-attention indexer K cache. "auto" picks the model's default (bf16 for MiniMax M3, fp8 for the DeepSeek sparse indexer). Quantized formats (fp8, mxfp4, nvfp4) require indexer kernel support in the backend.

###

`indexer_sparse_logits = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.indexer_sparse_logits)

DeepSeek V4.1 two-level indexer: score only the candidate blocks with DeepGEMM's sparse MQA-logits kernels instead of computing dense logits over the whole context and masking them. Requires `indexer_kv_dtype="mxfp4"`

, an SM100-class GPU, DeepGEMM >= 2.8 and the DeepSelect top-k extension (the top-k runs on the kernels' bf16 logits). The sparse path costs O(candidate blocks) per query regardless of context length, so it pays off for long contexts (roughly 32K tokens and beyond) and is slower below.

###

`minimax_m3_msa_decode_backend = 'triton'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.minimax_m3_msa_decode_backend)

Sparse decode kernel used by the MiniMax M3 MSA backend.

###

`mla_prefill_backend = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.mla_prefill_backend)

MLA prefill backend to use. If None, will be selected automatically. Valid options: FLASH_ATTN (FA3/FA4), FLASHINFER, TRTLLM_RAGGED.

###

`sparse_mla_force_mqa = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.sparse_mla_force_mqa)

Force sparse MLA to use forward_mqa for all requests, including prefill. When False (default), pure prefill batches use forward_mha when implemented. Set to True to always use the MQA path.

###

`tq_max_kv_splits_for_cuda_graph = 32`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.tq_max_kv_splits_for_cuda_graph)

TurboQuant max NUM_KV_SPLITS for cuda graph decode. Fixes the split count so grid dimensions are constant across captures, and buffers can be pre-allocated to avoid inflating the memory estimate.

###

`use_non_causal = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.use_non_causal)

Whether to use non-causal (bidirectional) attention.

###

`use_prefill_query_quantization = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.use_prefill_query_quantization)

If set, quantize query for attention in prefill.

###

`use_trtllm_attention = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.use_trtllm_attention)

If set to True/False, use or don't use the TRTLLM attention backend in flashinfer. If None, auto-detect the attention backend in flashinfer.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.compute_hash)

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

## Source code in `vllm/config/attention.py`


###

`resolve_indexer_kv_dtype(default)`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.resolve_indexer_kv_dtype)

Resolve `indexer_kv_dtype`

, substituting `default`

for "auto".

###

`validate_backend_before(value)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.validate_backend_before)

Enable parsing of the `backend`

enum type from string.

The special value "auto" is treated as None, which triggers automatic backend selection.

## Source code in `vllm/config/attention.py`


###

`validate_backend_per_kind_before(value)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.validate_backend_per_kind_before)

Parse the `backend_per_kind`

map from strings.

Keys must be valid `KVCacheSpecKind`

values; values are parsed like `backend`

(enum name, case-insensitive).

## Source code in `vllm/config/attention.py`


###

`validate_mla_prefill_backend_before(value)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.attention.AttentionConfig.validate_mla_prefill_backend_before)

Enable parsing of the `mla_prefill_backend`

enum type from string.

## Source code in `vllm/config/attention.py`


##

`HiSparseConfig`

[¶](https://docs.vllm.ai#vllm.config.attention.HiSparseConfig)

Configuration for HiSparse sparse-MLA KV offloading.

Attributes:

-
([device_buffer_size](https://docs.vllm.ai#vllm.config.attention.HiSparseConfig.device_buffer_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneTotal per-request GPU hot-buffer rows, including the newest-token slot.

-
([eager_host_mirror](https://docs.vllm.ai#vllm.config.attention.HiSparseConfig.eager_host_mirror)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Mirror decode-written KV rows to the host pool during the forward so


## Source code in `vllm/config/attention.py`


###

`device_buffer_size = Field(default=None, gt=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.attention.HiSparseConfig.device_buffer_size)

Total per-request GPU hot-buffer rows, including the newest-token slot.

Defaults to one top-k per decode query plus one top-k of LRU slack. The physical allocation is rounded up to the GPU cache block size selected from the active backends.

###

`eager_host_mirror = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.attention.HiSparseConfig.eager_host_mirror)

Mirror decode-written KV rows to the host pool during the forward so page spills complete without moving data. When disabled, decode rows stay resident-only and evicted pages are copied to host at spill time. Prefill rows are always mirrored during the forward.