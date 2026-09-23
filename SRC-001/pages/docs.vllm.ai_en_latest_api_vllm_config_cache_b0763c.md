source: https://docs.vllm.ai/en/latest/api/vllm/config/cache/
lastmod: 2026-09-23

#

`vllm.config.cache`

[¶](https://docs.vllm.ai#vllm.config.cache)

Classes:

-
–[CacheConfig](https://docs.vllm.ai#vllm.config.cache.CacheConfig)Configuration for the KV cache.


##

`CacheConfig`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig)

Configuration for the KV cache.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.cache.CacheConfig.compute_hash)WARNING: Whenever a new field is added to this config,


Attributes:

-
([block_size](https://docs.vllm.ai#vllm.config.cache.CacheConfig.block_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Size of a contiguous cache block in number of tokens.

-
([cache_dtype](https://docs.vllm.ai#vllm.config.cache.CacheConfig.cache_dtype)`CacheDType`

) –Data type for kv cache storage. If "auto", will use model data type.

-
([device_memory_utilization](https://docs.vllm.ai#vllm.config.cache.CacheConfig.device_memory_utilization)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Device-neutral alias for

`gpu_memory_utilization`

. -
([effective_attention_block_size](https://docs.vllm.ai#vllm.config.cache.CacheConfig.effective_attention_block_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneFull-attention block size in tokens, including DCP, or None if unavailable.

-
([enable_mamba_shared_prefix_checkpoint](https://docs.vllm.ai#vllm.config.cache.CacheConfig.enable_mamba_shared_prefix_checkpoint)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Also register a Mamba "align" checkpoint at the shared-prefix junction --

-
([enable_prefix_caching](https://docs.vllm.ai#vllm.config.cache.CacheConfig.enable_prefix_caching)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to enable prefix caching.

-
([gpu_memory_utilization](https://docs.vllm.ai#vllm.config.cache.CacheConfig.gpu_memory_utilization)

) –[float](https://docs.python.org/3/builtins/functions.html#float)The fraction of GPU memory to be used for the model executor, which can

-
([is_attention_free](https://docs.vllm.ai#vllm.config.cache.CacheConfig.is_attention_free)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether the model is attention-free. This is primarily set in

-
([kv_cache_dtype_skip_layers](https://docs.vllm.ai#vllm.config.cache.CacheConfig.kv_cache_dtype_skip_layers)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Layer patterns to skip KV cache quantization. Accepts layer indices

-
([kv_cache_layout](https://docs.vllm.ai#vllm.config.cache.CacheConfig.kv_cache_layout)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneResolved physical KV cache layout name (a

`KVCacheLayout`

member). -
([kv_cache_max_concurrency](https://docs.vllm.ai#vllm.config.cache.CacheConfig.kv_cache_max_concurrency)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NonePer-DP-engine maximum concurrency at max_model_len tokens.

-
([kv_cache_memory_bytes](https://docs.vllm.ai#vllm.config.cache.CacheConfig.kv_cache_memory_bytes)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneSize of KV Cache per GPU in bytes. By default, this is set to None

-
([kv_cache_size_tokens](https://docs.vllm.ai#vllm.config.cache.CacheConfig.kv_cache_size_tokens)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NonePer-DP-engine KV cache capacity in tokens (group-aware). Uses

-
([kv_offloading_backend](https://docs.vllm.ai#vllm.config.cache.CacheConfig.kv_offloading_backend)`KVOffloadingBackend`

) –The backend to use for KV cache offloading. Supported backends include

-
([kv_offloading_size](https://docs.vllm.ai#vllm.config.cache.CacheConfig.kv_offloading_size)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NoneSize of the KV cache offloading buffer in GiB. When TP > 1, this is

-
([kv_sharing_fast_prefill](https://docs.vllm.ai#vllm.config.cache.CacheConfig.kv_sharing_fast_prefill)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)In some KV sharing setups, e.g. YOCO (https://arxiv.org/abs/2405.05254),

-
([mamba_block_size](https://docs.vllm.ai#vllm.config.cache.CacheConfig.mamba_block_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneSize of a contiguous cache block in number of tokens for mamba cache.

-
([mamba_cache_dtype](https://docs.vllm.ai#vllm.config.cache.CacheConfig.mamba_cache_dtype)`MambaDType`

) –The data type to use for the Mamba cache (both the conv as well as the

-
([mamba_cache_mode](https://docs.vllm.ai#vllm.config.cache.CacheConfig.mamba_cache_mode)`MambaCacheMode`

) –The cache strategy for Mamba layers:

-
([mamba_page_size_padded](https://docs.vllm.ai#vllm.config.cache.CacheConfig.mamba_page_size_padded)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneOptional override for mamba page size; used by hybrid mamba/attention

-
([mamba_ssm_cache_dtype](https://docs.vllm.ai#vllm.config.cache.CacheConfig.mamba_ssm_cache_dtype)`MambaDType`

) –The data type to use for the Mamba cache (ssm state only, conv state will

-
([num_cpu_blocks](https://docs.vllm.ai#vllm.config.cache.CacheConfig.num_cpu_blocks)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneThe number of blocks to allocate for CPU memory.

-
([num_gpu_blocks](https://docs.vllm.ai#vllm.config.cache.CacheConfig.num_gpu_blocks)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneThe number of blocks to allocate for GPU memory.

-
([num_gpu_blocks_override](https://docs.vllm.ai#vllm.config.cache.CacheConfig.num_gpu_blocks_override)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneNumber of GPU blocks to use. This overrides the profiled

`num_gpu_blocks`

-
([prefix_cache_retention_interval](https://docs.vllm.ai#vllm.config.cache.CacheConfig.prefix_cache_retention_interval)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneToken interval between retained sliding-window and Mamba prefix-cache

-
([prefix_caching_hash_algo](https://docs.vllm.ai#vllm.config.cache.CacheConfig.prefix_caching_hash_algo)`PrefixCachingHashAlgo`

) –Set the hash algorithm for prefix caching:

-
([prefix_match_unit](https://docs.vllm.ai#vllm.config.cache.CacheConfig.prefix_match_unit)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneThe finest token boundary (in tokens) a prefix-cache hit can land on.

-
([replayssm_buffer_len](https://docs.vllm.ai#vllm.config.cache.CacheConfig.replayssm_buffer_len)

) –[int](https://docs.python.org/3/builtins/functions.html#int)ReplaySSM logical history length B for Mamba2. Triton uses B physical

-
([skip_page_size_padded](https://docs.vllm.ai#vllm.config.cache.CacheConfig.skip_page_size_padded)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneOptional override for the page size of layers skipped from KV cache

-
([sliding_window](https://docs.vllm.ai#vllm.config.cache.CacheConfig.sliding_window)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneSliding window size for the KV cache. This is primarily set in

-
([swa_bounded_replay](https://docs.vllm.ai#vllm.config.cache.CacheConfig.swa_bounded_replay)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Keep the sliding-window KV of models that support it (DeepSeek-V4.1)

-
([use_kda_recoverssm](https://docs.vllm.ai#vllm.config.cache.CacheConfig.use_kda_recoverssm)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether Kimi-K3 KDA uses RecoverSSM speculative decode.

-
([use_replayssm](https://docs.vllm.ai#vllm.config.cache.CacheConfig.use_replayssm)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Use the ReplaySSM Mamba2 decode kernel: cache recent SSM inputs and skip

-
([user_specified_block_size](https://docs.vllm.ai#vllm.config.cache.CacheConfig.user_specified_block_size)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether block_size was explicitly provided. Derived automatically.

-
([user_specified_mamba_block_size](https://docs.vllm.ai#vllm.config.cache.CacheConfig.user_specified_mamba_block_size)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether mamba_block_size was explicitly provided. Derived automatically.


## Source code in `vllm/config/cache.py`


|
|

###

`_block_size_resolved = field(default=False, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig._block_size_resolved)

Guard against pydantic re-running _apply_block_size_default.

###

`block_size = Field(default=None, gt=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.block_size)

Size of a contiguous cache block in number of tokens. Accepts None (meaning "use default"). After construction, always int.

###

`cache_dtype = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.cache_dtype)

Data type for kv cache storage. If "auto", will use model data type. CUDA 11.8+ supports fp8 (=fp8_e4m3) and fp8_e5m2. ROCm (AMD GPU) supports fp8 (=fp8_e4m3). Intel Gaudi (HPU) supports fp8 (using fp8_inc). Some models (namely DeepSeekV3.2) default to fp8, set to bfloat16 to use bfloat16 instead, this is an invalid option for models that do not default to fp8. "nvfp4_4over6" uses the NVFP4 layout and selects between max/6 and max/4 scales per 16 values by minimizing squared reconstruction error.

###

`device_memory_utilization`

`property`

`writable`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.device_memory_utilization)

Device-neutral alias for `gpu_memory_utilization`

.

###

`effective_attention_block_size = field(default=None, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.effective_attention_block_size)

Full-attention block size in tokens, including DCP, or None if unavailable.

###

`enable_mamba_shared_prefix_checkpoint = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.enable_mamba_shared_prefix_checkpoint)

Also register a Mamba "align" checkpoint at the shared-prefix junction -- where an EAGLE/MTP sibling was observed to resume -- instead of only at the prompt tail. Off by default; only takes effect with `mamba_cache_mode`

"align", EAGLE on the Mamba group, and a prefix match unit smaller than the Mamba block size.

###

`enable_prefix_caching = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.enable_prefix_caching)

Whether to enable prefix caching.

###

`gpu_memory_utilization = Field(default=0.92, gt=0, le=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.gpu_memory_utilization)

The fraction of GPU memory to be used for the model executor, which can range from 0 to 1. For example, a value of 0.5 would imply 50% GPU memory utilization. If unspecified, will use the default value of 0.92. This is a per-instance limit, and only applies to the current vLLM instance. It does not matter if you have another vLLM instance running on the same GPU. For example, if you have two vLLM instances running on the same GPU, you can set the GPU memory utilization to 0.5 for each instance. On non-GPU installs, this value controls the corresponding device memory utilization.

###

`is_attention_free = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.is_attention_free)

Whether the model is attention-free. This is primarily set in `ModelConfig`

and that value should be manually duplicated here.

###

`kv_cache_dtype_skip_layers = field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.kv_cache_dtype_skip_layers)

Layer patterns to skip KV cache quantization. Accepts layer indices (e.g., '0', '2', '4') or attention type names (e.g., 'sliding_window').

###

`kv_cache_layout = field(default=None, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.kv_cache_layout)

Resolved physical KV cache layout name (a `KVCacheLayout`

member).

`None`

means the layout has not been resolved yet. The engine core resolves it once (`resolve_kv_cache_layout`

) before memory profiling, and every worker process adopts the resolved name — via the `set_kv_cache_layout`

RPC, or `KVCacheConfig.kv_cache_layout`

for workers spawned after resolution — before the KV cache is allocated. Once set the value is final and read with `get_resolved_kv_cache_layout`

, which raises on `None`

. Tests and standalone tools may pre-set a value, which resolution then honors as-is.

###

`kv_cache_max_concurrency = field(default=None, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.kv_cache_max_concurrency)

Per-DP-engine maximum concurrency at max_model_len tokens.

###

`kv_cache_memory_bytes = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.kv_cache_memory_bytes)

Size of KV Cache per GPU in bytes. By default, this is set to None and vllm can automatically infer the kv cache size based on gpu_memory_utilization. However, users may want to manually specify the kv cache memory size. kv_cache_memory_bytes allows more fine-grain control of how much memory gets used when compared with using gpu_memory_utilization. Note that kv_cache_memory_bytes (when not-None) ignores gpu_memory_utilization

###

`kv_cache_size_tokens = field(default=None, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.kv_cache_size_tokens)

Per-DP-engine KV cache capacity in tokens (group-aware). Uses group-aware capacity since num_gpu_blocks * block_size can be wrong for hybrid models where requests occupy multiple KV cache groups.

###

`kv_offloading_backend = 'native'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.kv_offloading_backend)

The backend to use for KV cache offloading. Supported backends include 'native' (vLLM native CPU offloading), 'lmcache'. KV offloading is only activated when kv_offloading_size is set.

###

`kv_offloading_size = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.kv_offloading_size)

Size of the KV cache offloading buffer in GiB. When TP > 1, this is the total buffer size summed across all TP ranks. By default, this is set to None, which means no KV offloading is enabled. When set, vLLM will enable KV cache offloading to CPU using the kv_offloading_backend.

###

`kv_sharing_fast_prefill = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.kv_sharing_fast_prefill)

In some KV sharing setups, e.g. YOCO (https://arxiv.org/abs/2405.05254), some layers can skip tokens corresponding to prefill. This flag enables attention metadata for eligible layers to be overridden with metadata necessary for implementing this optimization in some models (e.g. Gemma3n)

###

`mamba_block_size = Field(default=None, gt=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.mamba_block_size)

Size of a contiguous cache block in number of tokens for mamba cache. Can be set only when prefix caching is enabled. Value must be a multiple of 8 to align with causal_conv1d kernel.

###

`mamba_cache_dtype = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.mamba_cache_dtype)

The data type to use for the Mamba cache (both the conv as well as the ssm state). If set to 'auto', the data type will be inferred from the model config.

###

`mamba_cache_mode = 'none'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.mamba_cache_mode)

The cache strategy for Mamba layers:

- "none": set when prefix caching is disabled.
- "all": cache the mamba state of all tokens at position i * block_size.
- "align": only cache the mamba state of the last token of each scheduler step and when the token is at position i * block_size. This is the default when prefix caching is enabled.

###

`mamba_page_size_padded = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.mamba_page_size_padded)

Optional override for mamba page size; used by hybrid mamba/attention models to ensure exact alignment with attention page size.

###

`mamba_ssm_cache_dtype = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.mamba_ssm_cache_dtype)

The data type to use for the Mamba cache (ssm state only, conv state will still be controlled by mamba_cache_dtype). If set to 'auto', the data type for the ssm state will be determined by mamba_cache_dtype.

###

`num_cpu_blocks = field(default=None, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.num_cpu_blocks)

The number of blocks to allocate for CPU memory.

###

`num_gpu_blocks = field(default=None, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.num_gpu_blocks)

The number of blocks to allocate for GPU memory.

###

`num_gpu_blocks_override = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.num_gpu_blocks_override)

Number of GPU blocks to use. This overrides the profiled `num_gpu_blocks`

if specified. Does nothing if `None`

. Used for testing preemption.

###

`prefix_cache_retention_interval = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.prefix_cache_retention_interval)

Token interval between retained sliding-window and Mamba prefix-cache checkpoints. `0`

retains only semantic checkpoints, including the latest replay boundary and shared-prefix junctions. Positive values additionally retain periodic checkpoints at the specified interval, which must be a multiple of the scheduler block size. `None`

retains checkpoints densely. Applies only to sliding-window and Mamba cache groups.

###

`prefix_caching_hash_algo = 'sha256'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.prefix_caching_hash_algo)

Set the hash algorithm for prefix caching:

- "sha256" uses Pickle for object serialization before hashing. This is the current default, as SHA256 is the most secure choice to avoid potential hash collisions.
- "sha256_cbor" provides a reproducible, cross-language compatible hash. It serializes objects using canonical CBOR and hashes them with SHA-256.
- "xxhash" uses Pickle serialization with xxHash (128-bit) for faster, non-cryptographic hashing. Requires the optional
`xxhash`

package. IMPORTANT: Use of a hashing algorithm that is not considered cryptographically secure theoretically increases the risk of hash collisions, which can cause undefined behavior or even leak private information in multi-tenant environments. Even if collisions are still very unlikely, it is important to consider your security risk tolerance against the performance benefits before turning this on. - "xxhash_cbor" combines canonical CBOR serialization with xxHash for reproducible hashing. Requires the optional
`xxhash`

package.

###

`prefix_match_unit = Field(default=None, gt=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.prefix_match_unit)

The finest token boundary (in tokens) a prefix-cache hit can land on.

Prefix-cache keys are computed every `prefix_match_unit`

tokens. It can be set finer than the physical KV cache block sizes (e.g. 32 vs a 1024-token hybrid-model block) as long as every KV cache group's `block_size`

is divisible by it, enabling cache hits at boundaries inside a physical block. It controls matching granularity only, not how often states are stored.

This equals to the `hash_block_size`

used throughout the KV cache code.

###

`replayssm_buffer_len = Field(default=16, gt=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.replayssm_buffer_len)

ReplaySSM logical history length B for Mamba2. Triton uses B physical rows and FlashInfer uses B+1. Kimi-K3 speculative decode does not use B. Default 16.

###

`skip_page_size_padded = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.skip_page_size_padded)

Optional override for the page size of layers skipped from KV cache quantization (`--kv-cache-dtype-skip-layers`

); set during block-size alignment so unquantized skip layers pad up to the quantized primary's page.

###

`sliding_window = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.sliding_window)

Sliding window size for the KV cache. This is primarily set in `ModelConfig`

and that value should be manually duplicated here.

###

`swa_bounded_replay = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.swa_bounded_replay)

Keep the sliding-window KV of models that support it (DeepSeek-V4.1) out of prefix caching and rebuild it after a prefix hit by recomputing the hit's last window. Requires model runner V2.

###

`use_kda_recoverssm = field(default=False, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.use_kda_recoverssm)

Whether Kimi-K3 KDA uses RecoverSSM speculative decode.

###

`use_replayssm = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.use_replayssm)

Use the ReplaySSM Mamba2 decode kernel: cache recent SSM inputs and skip the per-step full-state store, writing the checkpoint back only on flush. Requires mamba_cache_mode 'none' or 'align' (prefix caching) and the Triton or FlashInfer mamba backend; standard (non-speculative) decode only. In align mode flushes are most efficient when mamba_block_size is a multiple of replayssm_buffer_len, but this is not required.

###

`user_specified_block_size = field(default=False, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.user_specified_block_size)

Whether block_size was explicitly provided. Derived automatically.

###

`user_specified_mamba_block_size = field(default=False, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.user_specified_mamba_block_size)

Whether mamba_block_size was explicitly provided. Derived automatically.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.cache.CacheConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.