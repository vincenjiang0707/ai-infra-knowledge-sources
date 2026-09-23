source: https://docs.vllm.ai/en/latest/api/vllm/config/
lastmod: 2026-09-23

#

`vllm.config`

[¶](https://docs.vllm.ai#vllm.config)

Modules:

-
–[attention](https://docs.vllm.ai/attention/#vllm.config.attention) -
–[aux_output](https://docs.vllm.ai/aux_output/#vllm.config.aux_output)Configuration for execution auxiliary outputs.

-
–[cache](https://docs.vllm.ai/cache/#vllm.config.cache) -
–[compilation](https://docs.vllm.ai/compilation/#vllm.config.compilation) -
–[device](https://docs.vllm.ai/device/#vllm.config.device) -
–[diffusion](https://docs.vllm.ai/diffusion/#vllm.config.diffusion)Configuration for discrete diffusion (dLLM) models.

-
–[ec_manager_config](https://docs.vllm.ai/ec_manager_config/#vllm.config.ec_manager_config) -
–[ec_transfer](https://docs.vllm.ai/ec_transfer/#vllm.config.ec_transfer) -
–[engram](https://docs.vllm.ai/engram/#vllm.config.engram) -
–[fault_tolerance](https://docs.vllm.ai/fault_tolerance/#vllm.config.fault_tolerance) -
–[kernel](https://docs.vllm.ai/kernel/#vllm.config.kernel) -
–[kv_events](https://docs.vllm.ai/kv_events/#vllm.config.kv_events) -
–[kv_transfer](https://docs.vllm.ai/kv_transfer/#vllm.config.kv_transfer) -
–[load](https://docs.vllm.ai/load/#vllm.config.load) -
–[lora](https://docs.vllm.ai/lora/#vllm.config.lora) -
–[mamba](https://docs.vllm.ai/mamba/#vllm.config.mamba) -
–[model](https://docs.vllm.ai/model/#vllm.config.model) -
–[model_arch](https://docs.vllm.ai/model_arch/#vllm.config.model_arch) -
–[multimodal](https://docs.vllm.ai/multimodal/#vllm.config.multimodal) -
–[observability](https://docs.vllm.ai/observability/#vllm.config.observability) -
–[offload](https://docs.vllm.ai/offload/#vllm.config.offload)Configuration for model weight offloading.

-
–[parallel](https://docs.vllm.ai/parallel/#vllm.config.parallel) -
–[pooler](https://docs.vllm.ai/pooler/#vllm.config.pooler) -
–[profiler](https://docs.vllm.ai/profiler/#vllm.config.profiler) -
–[quantization](https://docs.vllm.ai/quantization/#vllm.config.quantization) -
–[reasoning](https://docs.vllm.ai/reasoning/#vllm.config.reasoning) -
–[scheduler](https://docs.vllm.ai/scheduler/#vllm.config.scheduler) -
–[speculative](https://docs.vllm.ai/speculative/#vllm.config.speculative) -
–[speech_to_text](https://docs.vllm.ai/speech_to_text/#vllm.config.speech_to_text) -
–[structured_outputs](https://docs.vllm.ai/structured_outputs/#vllm.config.structured_outputs) -
–[utils](https://docs.vllm.ai/utils/#vllm.config.utils)Utility functions for vLLM config dataclasses.

-
–[vllm](https://docs.vllm.ai/vllm/#vllm.config.vllm) -
–[watermarking](https://docs.vllm.ai/watermarking/#vllm.config.watermarking) -
–[weight_transfer](https://docs.vllm.ai/weight_transfer/#vllm.config.weight_transfer)

Classes:

-
–[AttentionConfig](https://docs.vllm.ai#vllm.config.AttentionConfig)Configuration for attention mechanisms in vLLM.

-
–[AuxOutputConfig](https://docs.vllm.ai#vllm.config.AuxOutputConfig)Configuration for auxiliary-output delivery.

-
–[CUDAGraphMode](https://docs.vllm.ai#vllm.config.CUDAGraphMode)Constants for the cudagraph mode in CompilationConfig.

-
–[CacheConfig](https://docs.vllm.ai#vllm.config.CacheConfig)Configuration for the KV cache.

-
–[CompilationConfig](https://docs.vllm.ai#vllm.config.CompilationConfig)Configuration for compilation.

-
–[CompilationMode](https://docs.vllm.ai#vllm.config.CompilationMode)The compilation approach used for torch.compile-based compilation of the

-
–[DeviceConfig](https://docs.vllm.ai#vllm.config.DeviceConfig)Configuration for the device to use for vLLM execution.

-
–[DiffusionConfig](https://docs.vllm.ai#vllm.config.DiffusionConfig)Configuration for discrete diffusion language models (dLLMs).

-
–[ECTransferConfig](https://docs.vllm.ai#vllm.config.ECTransferConfig)Configuration for distributed EC cache transfer.

-
–[EPLBConfig](https://docs.vllm.ai#vllm.config.EPLBConfig)Configuration for Expert Parallel Load Balancing (EP).

-
–[EncoderCacheManagerConfig](https://docs.vllm.ai#vllm.config.EncoderCacheManagerConfig) -
–[EngramConfig](https://docs.vllm.ai#vllm.config.EngramConfig)Configuration for Engram embedding storage and sharding.

-
–[FaultToleranceConfig](https://docs.vllm.ai#vllm.config.FaultToleranceConfig)Configuration for fault tolerance.

-
–[HiSparseConfig](https://docs.vllm.ai#vllm.config.HiSparseConfig)Configuration for HiSparse sparse-MLA KV offloading.

-
–[KVEventsConfig](https://docs.vllm.ai#vllm.config.KVEventsConfig)Configuration for KV event publishing.

-
–[KVTransferConfig](https://docs.vllm.ai#vllm.config.KVTransferConfig)Configuration for distributed KV cache transfer.

-
–[KernelConfig](https://docs.vllm.ai#vllm.config.KernelConfig)Configuration for kernel selection and warmup behavior.

-
–[LoRAConfig](https://docs.vllm.ai#vllm.config.LoRAConfig)Configuration for LoRA.

-
–[LoadConfig](https://docs.vllm.ai#vllm.config.LoadConfig)Configuration for loading the model weights.

-
–[MambaConfig](https://docs.vllm.ai#vllm.config.MambaConfig)Configuration for Mamba SSM backends.

-
–[ModelConfig](https://docs.vllm.ai#vllm.config.ModelConfig)Configuration for the model.

-
–[MultiModalConfig](https://docs.vllm.ai#vllm.config.MultiModalConfig)Controls the behavior of multimodal models.

-
–[ObservabilityConfig](https://docs.vllm.ai#vllm.config.ObservabilityConfig)Configuration for observability - metrics and tracing.

-
–[OffloadConfig](https://docs.vllm.ai#vllm.config.OffloadConfig)Configuration for model weight offloading to reduce GPU memory usage.

-
–[ParallelConfig](https://docs.vllm.ai#vllm.config.ParallelConfig)Configuration for the distributed execution.

-
–[PassConfig](https://docs.vllm.ai#vllm.config.PassConfig)Configuration for custom Inductor passes.

-
–[PoolerConfig](https://docs.vllm.ai#vllm.config.PoolerConfig)Controls the behavior of output pooling in pooling models.

-
–[PrefetchOffloadConfig](https://docs.vllm.ai#vllm.config.PrefetchOffloadConfig)Configuration for prefetch-based CPU offloading.

-
–[ProfilerConfig](https://docs.vllm.ai#vllm.config.ProfilerConfig)Dataclass which contains profiler config for the engine.

-
–[ReasoningConfig](https://docs.vllm.ai#vllm.config.ReasoningConfig)Configuration for reasoning models.

-
–[SchedulerConfig](https://docs.vllm.ai#vllm.config.SchedulerConfig)Scheduler configuration.

-
–[SpeculativeConfig](https://docs.vllm.ai#vllm.config.SpeculativeConfig)Configuration for speculative decoding.

-
–[SpeechToTextConfig](https://docs.vllm.ai#vllm.config.SpeechToTextConfig)Configuration for speech-to-text models.

-
–[SpeechToTextParams](https://docs.vllm.ai#vllm.config.SpeechToTextParams)All parameters consumed by

`get_generation_prompt()`

. -
–[StructuredOutputsConfig](https://docs.vllm.ai#vllm.config.StructuredOutputsConfig)Dataclass which contains structured outputs config for the engine.

-
–[UVAOffloadConfig](https://docs.vllm.ai#vllm.config.UVAOffloadConfig)Configuration for UVA (Unified Virtual Addressing) CPU offloading.

-
–[VllmConfig](https://docs.vllm.ai#vllm.config.VllmConfig)Dataclass which contains all vllm-related configuration. This

-
–[WatermarkConfig](https://docs.vllm.ai#vllm.config.WatermarkConfig)Configuration for text watermark generation.

-
–[WeightTransferConfig](https://docs.vllm.ai#vllm.config.WeightTransferConfig)Configuration for weight transfer during RL training.


Functions:

-
–[config](https://docs.vllm.ai#vllm.config.config)Decorator to create a pydantic dataclass with default config. The default config

-
–[get_attr_docs](https://docs.vllm.ai#vllm.config.get_attr_docs)Get any docstrings placed after attribute assignments in a class body.

-
–[get_cached_compilation_config](https://docs.vllm.ai#vllm.config.get_cached_compilation_config)Cache config to avoid repeated calls to get_current_vllm_config()

-
–[get_layers_from_vllm_config](https://docs.vllm.ai#vllm.config.get_layers_from_vllm_config)Get layers from the vLLM config.

-
–[replace](https://docs.vllm.ai#vllm.config.replace)Like

,`dataclasses.replace`

-
–[set_current_vllm_config](https://docs.vllm.ai#vllm.config.set_current_vllm_config)Temporarily set the current vLLM config.


##

`AttentionConfig`

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig)

Configuration for attention mechanisms in vLLM.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.AttentionConfig.compute_hash)Provide a hash that uniquely identifies all the configs

-
–[resolve_indexer_kv_dtype](https://docs.vllm.ai#vllm.config.AttentionConfig.resolve_indexer_kv_dtype)Resolve

`indexer_kv_dtype`

, substituting`default`

for "auto". -
–[validate_backend_before](https://docs.vllm.ai#vllm.config.AttentionConfig.validate_backend_before)Enable parsing of the

`backend`

enum type from string. -
–[validate_backend_per_kind_before](https://docs.vllm.ai#vllm.config.AttentionConfig.validate_backend_per_kind_before)Parse the

`backend_per_kind`

map from strings. -
–[validate_mla_prefill_backend_before](https://docs.vllm.ai#vllm.config.AttentionConfig.validate_mla_prefill_backend_before)Enable parsing of the

`mla_prefill_backend`

enum type from string.

Attributes:

-
([backend](https://docs.vllm.ai#vllm.config.AttentionConfig.backend)

) –[AttentionBackendEnum](https://docs.vllm.ai/v1/attention/backends/registry/#vllm.v1.attention.backends.registry.AttentionBackendEnum)| NoneAttention backend to use. Use "auto" or None for automatic selection.

-
([backend_per_kind](https://docs.vllm.ai#vllm.config.AttentionConfig.backend_per_kind)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[AttentionBackendEnum](https://docs.vllm.ai/v1/attention/backends/registry/#vllm.v1.attention.backends.registry.AttentionBackendEnum)]Per-KV-cache-group attention backend overrides, keyed by

-
([disable_flashinfer_q_quantization](https://docs.vllm.ai#vllm.config.AttentionConfig.disable_flashinfer_q_quantization)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If set, when using fp8 kv, do not quantize Q to fp8.

-
([flash_attn_max_num_splits_for_cuda_graph](https://docs.vllm.ai#vllm.config.AttentionConfig.flash_attn_max_num_splits_for_cuda_graph)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Flash Attention max number splits for cuda graph decode.

-
([flash_attn_version](https://docs.vllm.ai#vllm.config.AttentionConfig.flash_attn_version)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)[2, 3, 4] | NoneForce vllm to use a specific flash-attention version (2, 3, or 4).

-
([flex_attn_block_m](https://docs.vllm.ai#vllm.config.AttentionConfig.flex_attn_block_m)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneTriton kernel BLOCK_M tile size for flex attention.

-
([flex_attn_block_n](https://docs.vllm.ai#vllm.config.AttentionConfig.flex_attn_block_n)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneTriton kernel BLOCK_N tile size for flex attention.

-
([flex_attn_kv_block_size](https://docs.vllm.ai#vllm.config.AttentionConfig.flex_attn_kv_block_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneLogical KV block size for the flex attention block mask.

-
([flex_attn_q_block_size](https://docs.vllm.ai#vllm.config.AttentionConfig.flex_attn_q_block_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneLogical Q block size for the flex attention block mask.

-
([hisparse_config](https://docs.vllm.ai#vllm.config.AttentionConfig.hisparse_config)

) –[HiSparseConfig](https://docs.vllm.ai/attention/#vllm.config.attention.HiSparseConfig)| NoneHiSparse host-resident KV configuration. Setting this enables experimental

-
([indexer_kv_dtype](https://docs.vllm.ai#vllm.config.AttentionConfig.indexer_kv_dtype)`IndexerKVDType`

) –Data type for the sparse-attention indexer K cache. "auto" picks the

-
([indexer_sparse_logits](https://docs.vllm.ai#vllm.config.AttentionConfig.indexer_sparse_logits)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)DeepSeek V4.1 two-level indexer: score only the candidate blocks with

-
([minimax_m3_msa_decode_backend](https://docs.vllm.ai#vllm.config.AttentionConfig.minimax_m3_msa_decode_backend)`MiniMaxM3MSADecodeBackend`

) –Sparse decode kernel used by the MiniMax M3 MSA backend.

-
([mla_prefill_backend](https://docs.vllm.ai#vllm.config.AttentionConfig.mla_prefill_backend)

) –[MLAPrefillBackendEnum](https://docs.vllm.ai/v1/attention/backends/mla/prefill/registry/#vllm.v1.attention.backends.mla.prefill.registry.MLAPrefillBackendEnum)| NoneMLA prefill backend to use. If None, will be selected automatically.

-
([sparse_mla_force_mqa](https://docs.vllm.ai#vllm.config.AttentionConfig.sparse_mla_force_mqa)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Force sparse MLA to use forward_mqa for all requests, including prefill.

-
([tq_max_kv_splits_for_cuda_graph](https://docs.vllm.ai#vllm.config.AttentionConfig.tq_max_kv_splits_for_cuda_graph)

) –[int](https://docs.python.org/3/builtins/functions.html#int)TurboQuant max NUM_KV_SPLITS for cuda graph decode.

-
([use_non_causal](https://docs.vllm.ai#vllm.config.AttentionConfig.use_non_causal)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to use non-causal (bidirectional) attention.

-
([use_prefill_query_quantization](https://docs.vllm.ai#vllm.config.AttentionConfig.use_prefill_query_quantization)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If set, quantize query for attention in prefill.

-
([use_trtllm_attention](https://docs.vllm.ai#vllm.config.AttentionConfig.use_trtllm_attention)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneIf set to True/False, use or don't use the TRTLLM attention backend


## Source code in `vllm/config/attention.py`


|
|

###

`backend = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig.backend)

Attention backend to use. Use "auto" or None for automatic selection.

###

`backend_per_kind = field(default_factory=dict)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig.backend_per_kind)

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

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig.disable_flashinfer_q_quantization)

If set, when using fp8 kv, do not quantize Q to fp8.

###

`flash_attn_max_num_splits_for_cuda_graph = 32`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig.flash_attn_max_num_splits_for_cuda_graph)

Flash Attention max number splits for cuda graph decode.

###

`flash_attn_version = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig.flash_attn_version)

Force vllm to use a specific flash-attention version (2, 3, or 4). Only valid when using the flash-attention backend.

###

`flex_attn_block_m = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig.flex_attn_block_m)

Triton kernel BLOCK_M tile size for flex attention. Must be a power of 2 >= 16. If None and VLLM_BATCH_INVARIANT=1, defaults to 16.

###

`flex_attn_block_n = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig.flex_attn_block_n)

Triton kernel BLOCK_N tile size for flex attention. Must be a power of 2 >= 16. If None and VLLM_BATCH_INVARIANT=1, defaults to 16.

###

`flex_attn_kv_block_size = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig.flex_attn_kv_block_size)

Logical KV block size for the flex attention block mask. Must be a power of 2 and divisible by flex_attn_block_n. If None, uses the KV cache block size for paged KV attention on PyTorch >= 2.9, and 128 for encoder-only attention or older PyTorch versions.

###

`flex_attn_q_block_size = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig.flex_attn_q_block_size)

Logical Q block size for the flex attention block mask. Must be a power of 2 and divisible by flex_attn_block_m. If None, uses 16 for paged KV attention on PyTorch >= 2.9, and 128 for encoder-only attention or older PyTorch versions.

###

`hisparse_config = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig.hisparse_config)

HiSparse host-resident KV configuration. Setting this enables experimental Model Runner V2-only HiSparse sparse-MLA decode hot-buffering. It is inferred with defaults when HiSparseConnector is configured (directly or via MultiConnector); set it explicitly only to tune its fields.

###

`indexer_kv_dtype = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig.indexer_kv_dtype)

Data type for the sparse-attention indexer K cache. "auto" picks the model's default (bf16 for MiniMax M3, fp8 for the DeepSeek sparse indexer). Quantized formats (fp8, mxfp4, nvfp4) require indexer kernel support in the backend.

###

`indexer_sparse_logits = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig.indexer_sparse_logits)

DeepSeek V4.1 two-level indexer: score only the candidate blocks with DeepGEMM's sparse MQA-logits kernels instead of computing dense logits over the whole context and masking them. Requires `indexer_kv_dtype="mxfp4"`

, an SM100-class GPU, DeepGEMM >= 2.8 and the DeepSelect top-k extension (the top-k runs on the kernels' bf16 logits). The sparse path costs O(candidate blocks) per query regardless of context length, so it pays off for long contexts (roughly 32K tokens and beyond) and is slower below.

###

`minimax_m3_msa_decode_backend = 'triton'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig.minimax_m3_msa_decode_backend)

Sparse decode kernel used by the MiniMax M3 MSA backend.

###

`mla_prefill_backend = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig.mla_prefill_backend)

MLA prefill backend to use. If None, will be selected automatically. Valid options: FLASH_ATTN (FA3/FA4), FLASHINFER, TRTLLM_RAGGED.

###

`sparse_mla_force_mqa = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig.sparse_mla_force_mqa)

Force sparse MLA to use forward_mqa for all requests, including prefill. When False (default), pure prefill batches use forward_mha when implemented. Set to True to always use the MQA path.

###

`tq_max_kv_splits_for_cuda_graph = 32`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig.tq_max_kv_splits_for_cuda_graph)

TurboQuant max NUM_KV_SPLITS for cuda graph decode. Fixes the split count so grid dimensions are constant across captures, and buffers can be pre-allocated to avoid inflating the memory estimate.

###

`use_non_causal = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig.use_non_causal)

Whether to use non-causal (bidirectional) attention.

###

`use_prefill_query_quantization = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig.use_prefill_query_quantization)

If set, quantize query for attention in prefill.

###

`use_trtllm_attention = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig.use_trtllm_attention)

If set to True/False, use or don't use the TRTLLM attention backend in flashinfer. If None, auto-detect the attention backend in flashinfer.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig.compute_hash)

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

## Source code in `vllm/config/attention.py`


###

`resolve_indexer_kv_dtype(default)`

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig.resolve_indexer_kv_dtype)

Resolve `indexer_kv_dtype`

, substituting `default`

for "auto".

###

`validate_backend_before(value)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig.validate_backend_before)

Enable parsing of the `backend`

enum type from string.

The special value "auto" is treated as None, which triggers automatic backend selection.

## Source code in `vllm/config/attention.py`


###

`validate_backend_per_kind_before(value)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig.validate_backend_per_kind_before)

Parse the `backend_per_kind`

map from strings.

Keys must be valid `KVCacheSpecKind`

values; values are parsed like `backend`

(enum name, case-insensitive).

## Source code in `vllm/config/attention.py`


###

`validate_mla_prefill_backend_before(value)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.AttentionConfig.validate_mla_prefill_backend_before)

Enable parsing of the `mla_prefill_backend`

enum type from string.

## Source code in `vllm/config/attention.py`


##

`AuxOutputConfig`

[¶](https://docs.vllm.ai#vllm.config.AuxOutputConfig)

Configuration for auxiliary-output delivery.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.AuxOutputConfig.compute_hash)Hash AuxOutput settings that alter the model forward graph.


Attributes:

-
([enable_return_routed_experts](https://docs.vllm.ai#vllm.config.AuxOutputConfig.enable_return_routed_experts)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Capture and return routed-experts auxiliary outputs.

-
([enabled](https://docs.vllm.ai#vllm.config.AuxOutputConfig.enabled)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether any execution auxiliary output is enabled.

-
([max_bytes](https://docs.vllm.ai#vllm.config.AuxOutputConfig.max_bytes)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneLRU capacity, or

`None`

to derive it from the KV cache capacity.

## Source code in `vllm/config/aux_output.py`


###

`enable_return_routed_experts = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.AuxOutputConfig.enable_return_routed_experts)

Capture and return routed-experts auxiliary outputs.

###

`enabled`

`property`

[¶](https://docs.vllm.ai#vllm.config.AuxOutputConfig.enabled)

Whether any execution auxiliary output is enabled.

###

`max_bytes = Field(default=None, gt=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.AuxOutputConfig.max_bytes)

LRU capacity, or `None`

to derive it from the KV cache capacity.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.AuxOutputConfig.compute_hash)

Hash AuxOutput settings that alter the model forward graph.

##

`CUDAGraphMode`

[¶](https://docs.vllm.ai#vllm.config.CUDAGraphMode)

Bases: [Enum](https://docs.python.org/3/library/enum.html#enum.Enum)

Constants for the cudagraph mode in CompilationConfig. Meanwhile, the subset enum `NONE`

, `PIECEWISE`

and `FULL`

are also treated as concrete runtime mode for cudagraph runtime dispatching.

## Source code in `vllm/config/compilation.py`


##

`CacheConfig`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig)

Configuration for the KV cache.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.CacheConfig.compute_hash)WARNING: Whenever a new field is added to this config,


Attributes:

-
([block_size](https://docs.vllm.ai#vllm.config.CacheConfig.block_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Size of a contiguous cache block in number of tokens.

-
([cache_dtype](https://docs.vllm.ai#vllm.config.CacheConfig.cache_dtype)`CacheDType`

) –Data type for kv cache storage. If "auto", will use model data type.

-
([device_memory_utilization](https://docs.vllm.ai#vllm.config.CacheConfig.device_memory_utilization)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Device-neutral alias for

`gpu_memory_utilization`

. -
([effective_attention_block_size](https://docs.vllm.ai#vllm.config.CacheConfig.effective_attention_block_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneFull-attention block size in tokens, including DCP, or None if unavailable.

-
([enable_mamba_shared_prefix_checkpoint](https://docs.vllm.ai#vllm.config.CacheConfig.enable_mamba_shared_prefix_checkpoint)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Also register a Mamba "align" checkpoint at the shared-prefix junction --

-
([enable_prefix_caching](https://docs.vllm.ai#vllm.config.CacheConfig.enable_prefix_caching)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to enable prefix caching.

-
([gpu_memory_utilization](https://docs.vllm.ai#vllm.config.CacheConfig.gpu_memory_utilization)

) –[float](https://docs.python.org/3/builtins/functions.html#float)The fraction of GPU memory to be used for the model executor, which can

-
([is_attention_free](https://docs.vllm.ai#vllm.config.CacheConfig.is_attention_free)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether the model is attention-free. This is primarily set in

-
([kv_cache_dtype_skip_layers](https://docs.vllm.ai#vllm.config.CacheConfig.kv_cache_dtype_skip_layers)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Layer patterns to skip KV cache quantization. Accepts layer indices

-
([kv_cache_layout](https://docs.vllm.ai#vllm.config.CacheConfig.kv_cache_layout)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneResolved physical KV cache layout name (a

`KVCacheLayout`

member). -
([kv_cache_max_concurrency](https://docs.vllm.ai#vllm.config.CacheConfig.kv_cache_max_concurrency)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NonePer-DP-engine maximum concurrency at max_model_len tokens.

-
([kv_cache_memory_bytes](https://docs.vllm.ai#vllm.config.CacheConfig.kv_cache_memory_bytes)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneSize of KV Cache per GPU in bytes. By default, this is set to None

-
([kv_cache_size_tokens](https://docs.vllm.ai#vllm.config.CacheConfig.kv_cache_size_tokens)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NonePer-DP-engine KV cache capacity in tokens (group-aware). Uses

-
([kv_offloading_backend](https://docs.vllm.ai#vllm.config.CacheConfig.kv_offloading_backend)`KVOffloadingBackend`

) –The backend to use for KV cache offloading. Supported backends include

-
([kv_offloading_size](https://docs.vllm.ai#vllm.config.CacheConfig.kv_offloading_size)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NoneSize of the KV cache offloading buffer in GiB. When TP > 1, this is

-
([kv_sharing_fast_prefill](https://docs.vllm.ai#vllm.config.CacheConfig.kv_sharing_fast_prefill)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)In some KV sharing setups, e.g. YOCO (https://arxiv.org/abs/2405.05254),

-
([mamba_block_size](https://docs.vllm.ai#vllm.config.CacheConfig.mamba_block_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneSize of a contiguous cache block in number of tokens for mamba cache.

-
([mamba_cache_dtype](https://docs.vllm.ai#vllm.config.CacheConfig.mamba_cache_dtype)`MambaDType`

) –The data type to use for the Mamba cache (both the conv as well as the

-
([mamba_cache_mode](https://docs.vllm.ai#vllm.config.CacheConfig.mamba_cache_mode)`MambaCacheMode`

) –The cache strategy for Mamba layers:

-
([mamba_page_size_padded](https://docs.vllm.ai#vllm.config.CacheConfig.mamba_page_size_padded)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneOptional override for mamba page size; used by hybrid mamba/attention

-
([mamba_ssm_cache_dtype](https://docs.vllm.ai#vllm.config.CacheConfig.mamba_ssm_cache_dtype)`MambaDType`

) –The data type to use for the Mamba cache (ssm state only, conv state will

-
([num_cpu_blocks](https://docs.vllm.ai#vllm.config.CacheConfig.num_cpu_blocks)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneThe number of blocks to allocate for CPU memory.

-
([num_gpu_blocks](https://docs.vllm.ai#vllm.config.CacheConfig.num_gpu_blocks)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneThe number of blocks to allocate for GPU memory.

-
([num_gpu_blocks_override](https://docs.vllm.ai#vllm.config.CacheConfig.num_gpu_blocks_override)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneNumber of GPU blocks to use. This overrides the profiled

`num_gpu_blocks`

-
([prefix_cache_retention_interval](https://docs.vllm.ai#vllm.config.CacheConfig.prefix_cache_retention_interval)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneToken interval between retained sliding-window and Mamba prefix-cache

-
([prefix_caching_hash_algo](https://docs.vllm.ai#vllm.config.CacheConfig.prefix_caching_hash_algo)`PrefixCachingHashAlgo`

) –Set the hash algorithm for prefix caching:

-
([prefix_match_unit](https://docs.vllm.ai#vllm.config.CacheConfig.prefix_match_unit)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneThe finest token boundary (in tokens) a prefix-cache hit can land on.

-
([replayssm_buffer_len](https://docs.vllm.ai#vllm.config.CacheConfig.replayssm_buffer_len)

) –[int](https://docs.python.org/3/builtins/functions.html#int)ReplaySSM logical history length B for Mamba2. Triton uses B physical

-
([skip_page_size_padded](https://docs.vllm.ai#vllm.config.CacheConfig.skip_page_size_padded)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneOptional override for the page size of layers skipped from KV cache

-
([sliding_window](https://docs.vllm.ai#vllm.config.CacheConfig.sliding_window)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneSliding window size for the KV cache. This is primarily set in

-
([swa_bounded_replay](https://docs.vllm.ai#vllm.config.CacheConfig.swa_bounded_replay)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Keep the sliding-window KV of models that support it (DeepSeek-V4.1)

-
([use_kda_recoverssm](https://docs.vllm.ai#vllm.config.CacheConfig.use_kda_recoverssm)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether Kimi-K3 KDA uses RecoverSSM speculative decode.

-
([use_replayssm](https://docs.vllm.ai#vllm.config.CacheConfig.use_replayssm)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Use the ReplaySSM Mamba2 decode kernel: cache recent SSM inputs and skip

-
([user_specified_block_size](https://docs.vllm.ai#vllm.config.CacheConfig.user_specified_block_size)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether block_size was explicitly provided. Derived automatically.

-
([user_specified_mamba_block_size](https://docs.vllm.ai#vllm.config.CacheConfig.user_specified_mamba_block_size)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether mamba_block_size was explicitly provided. Derived automatically.


## Source code in `vllm/config/cache.py`


|
|

###

`_block_size_resolved = field(default=False, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig._block_size_resolved)

Guard against pydantic re-running _apply_block_size_default.

###

`block_size = Field(default=None, gt=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.block_size)

Size of a contiguous cache block in number of tokens. Accepts None (meaning "use default"). After construction, always int.

###

`cache_dtype = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.cache_dtype)

Data type for kv cache storage. If "auto", will use model data type. CUDA 11.8+ supports fp8 (=fp8_e4m3) and fp8_e5m2. ROCm (AMD GPU) supports fp8 (=fp8_e4m3). Intel Gaudi (HPU) supports fp8 (using fp8_inc). Some models (namely DeepSeekV3.2) default to fp8, set to bfloat16 to use bfloat16 instead, this is an invalid option for models that do not default to fp8. "nvfp4_4over6" uses the NVFP4 layout and selects between max/6 and max/4 scales per 16 values by minimizing squared reconstruction error.

###

`device_memory_utilization`

`property`

`writable`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.device_memory_utilization)

Device-neutral alias for `gpu_memory_utilization`

.

###

`effective_attention_block_size = field(default=None, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.effective_attention_block_size)

Full-attention block size in tokens, including DCP, or None if unavailable.

###

`enable_mamba_shared_prefix_checkpoint = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.enable_mamba_shared_prefix_checkpoint)

Also register a Mamba "align" checkpoint at the shared-prefix junction -- where an EAGLE/MTP sibling was observed to resume -- instead of only at the prompt tail. Off by default; only takes effect with `mamba_cache_mode`

"align", EAGLE on the Mamba group, and a prefix match unit smaller than the Mamba block size.

###

`enable_prefix_caching = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.enable_prefix_caching)

Whether to enable prefix caching.

###

`gpu_memory_utilization = Field(default=0.92, gt=0, le=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.gpu_memory_utilization)

The fraction of GPU memory to be used for the model executor, which can range from 0 to 1. For example, a value of 0.5 would imply 50% GPU memory utilization. If unspecified, will use the default value of 0.92. This is a per-instance limit, and only applies to the current vLLM instance. It does not matter if you have another vLLM instance running on the same GPU. For example, if you have two vLLM instances running on the same GPU, you can set the GPU memory utilization to 0.5 for each instance. On non-GPU installs, this value controls the corresponding device memory utilization.

###

`is_attention_free = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.is_attention_free)

Whether the model is attention-free. This is primarily set in `ModelConfig`

and that value should be manually duplicated here.

###

`kv_cache_dtype_skip_layers = field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.kv_cache_dtype_skip_layers)

Layer patterns to skip KV cache quantization. Accepts layer indices (e.g., '0', '2', '4') or attention type names (e.g., 'sliding_window').

###

`kv_cache_layout = field(default=None, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.kv_cache_layout)

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

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.kv_cache_max_concurrency)

Per-DP-engine maximum concurrency at max_model_len tokens.

###

`kv_cache_memory_bytes = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.kv_cache_memory_bytes)

Size of KV Cache per GPU in bytes. By default, this is set to None and vllm can automatically infer the kv cache size based on gpu_memory_utilization. However, users may want to manually specify the kv cache memory size. kv_cache_memory_bytes allows more fine-grain control of how much memory gets used when compared with using gpu_memory_utilization. Note that kv_cache_memory_bytes (when not-None) ignores gpu_memory_utilization

###

`kv_cache_size_tokens = field(default=None, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.kv_cache_size_tokens)

Per-DP-engine KV cache capacity in tokens (group-aware). Uses group-aware capacity since num_gpu_blocks * block_size can be wrong for hybrid models where requests occupy multiple KV cache groups.

###

`kv_offloading_backend = 'native'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.kv_offloading_backend)

The backend to use for KV cache offloading. Supported backends include 'native' (vLLM native CPU offloading), 'lmcache'. KV offloading is only activated when kv_offloading_size is set.

###

`kv_offloading_size = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.kv_offloading_size)

Size of the KV cache offloading buffer in GiB. When TP > 1, this is the total buffer size summed across all TP ranks. By default, this is set to None, which means no KV offloading is enabled. When set, vLLM will enable KV cache offloading to CPU using the kv_offloading_backend.

###

`kv_sharing_fast_prefill = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.kv_sharing_fast_prefill)

In some KV sharing setups, e.g. YOCO (https://arxiv.org/abs/2405.05254), some layers can skip tokens corresponding to prefill. This flag enables attention metadata for eligible layers to be overridden with metadata necessary for implementing this optimization in some models (e.g. Gemma3n)

###

`mamba_block_size = Field(default=None, gt=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.mamba_block_size)

Size of a contiguous cache block in number of tokens for mamba cache. Can be set only when prefix caching is enabled. Value must be a multiple of 8 to align with causal_conv1d kernel.

###

`mamba_cache_dtype = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.mamba_cache_dtype)

The data type to use for the Mamba cache (both the conv as well as the ssm state). If set to 'auto', the data type will be inferred from the model config.

###

`mamba_cache_mode = 'none'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.mamba_cache_mode)

The cache strategy for Mamba layers:

- "none": set when prefix caching is disabled.
- "all": cache the mamba state of all tokens at position i * block_size.
- "align": only cache the mamba state of the last token of each scheduler step and when the token is at position i * block_size. This is the default when prefix caching is enabled.

###

`mamba_page_size_padded = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.mamba_page_size_padded)

Optional override for mamba page size; used by hybrid mamba/attention models to ensure exact alignment with attention page size.

###

`mamba_ssm_cache_dtype = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.mamba_ssm_cache_dtype)

The data type to use for the Mamba cache (ssm state only, conv state will still be controlled by mamba_cache_dtype). If set to 'auto', the data type for the ssm state will be determined by mamba_cache_dtype.

###

`num_cpu_blocks = field(default=None, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.num_cpu_blocks)

The number of blocks to allocate for CPU memory.

###

`num_gpu_blocks = field(default=None, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.num_gpu_blocks)

The number of blocks to allocate for GPU memory.

###

`num_gpu_blocks_override = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.num_gpu_blocks_override)

Number of GPU blocks to use. This overrides the profiled `num_gpu_blocks`

if specified. Does nothing if `None`

. Used for testing preemption.

###

`prefix_cache_retention_interval = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.prefix_cache_retention_interval)

Token interval between retained sliding-window and Mamba prefix-cache checkpoints. `0`

retains only semantic checkpoints, including the latest replay boundary and shared-prefix junctions. Positive values additionally retain periodic checkpoints at the specified interval, which must be a multiple of the scheduler block size. `None`

retains checkpoints densely. Applies only to sliding-window and Mamba cache groups.

###

`prefix_caching_hash_algo = 'sha256'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.prefix_caching_hash_algo)

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

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.prefix_match_unit)

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

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.replayssm_buffer_len)

ReplaySSM logical history length B for Mamba2. Triton uses B physical rows and FlashInfer uses B+1. Kimi-K3 speculative decode does not use B. Default 16.

###

`skip_page_size_padded = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.skip_page_size_padded)

Optional override for the page size of layers skipped from KV cache quantization (`--kv-cache-dtype-skip-layers`

); set during block-size alignment so unquantized skip layers pad up to the quantized primary's page.

###

`sliding_window = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.sliding_window)

Sliding window size for the KV cache. This is primarily set in `ModelConfig`

and that value should be manually duplicated here.

###

`swa_bounded_replay = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.swa_bounded_replay)

Keep the sliding-window KV of models that support it (DeepSeek-V4.1) out of prefix caching and rebuild it after a prefix hit by recomputing the hit's last window. Requires model runner V2.

###

`use_kda_recoverssm = field(default=False, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.use_kda_recoverssm)

Whether Kimi-K3 KDA uses RecoverSSM speculative decode.

###

`use_replayssm = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.use_replayssm)

Use the ReplaySSM Mamba2 decode kernel: cache recent SSM inputs and skip the per-step full-state store, writing the checkpoint back only on flush. Requires mamba_cache_mode 'none' or 'align' (prefix caching) and the Triton or FlashInfer mamba backend; standard (non-speculative) decode only. In align mode flushes are most efficient when mamba_block_size is a multiple of replayssm_buffer_len, but this is not required.

###

`user_specified_block_size = field(default=False, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.user_specified_block_size)

Whether block_size was explicitly provided. Derived automatically.

###

`user_specified_mamba_block_size = field(default=False, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.user_specified_mamba_block_size)

Whether mamba_block_size was explicitly provided. Derived automatically.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.CacheConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

## Source code in `vllm/config/cache.py`


##

`CompilationConfig`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig)

Configuration for compilation.

You must pass CompilationConfig to VLLMConfig constructor. VLLMConfig's post_init does further initialization. If used outside of the VLLMConfig, some fields will be left in an improper state.

It contains PassConfig, which controls the custom fusion/transformation passes. The rest has three parts:

- Top-level Compilation control:
- CudaGraph capture:
- Inductor compilation:
`compile_sizes`

- [
`compile_ranges_endpoints`

] [vllm.config.CompilationConfig.compile_ranges_endpoints] `inductor_compile_config`

`inductor_passes`

- custom inductor passes


Why we have different sizes for cudagraph and inductor: - cudagraph: a cudagraph captured for a specific size can only be used for the same size. We need to capture all the sizes we want to use. - inductor: a graph compiled by inductor for a general shape can be used for different sizes. Inductor can also compile for specific sizes, where it can have more information to optimize the graph with fully static shapes. However, we find the general shape compilation is sufficient for most cases. It might be beneficial to compile for certain small batchsizes, where inductor is good at optimizing.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.CompilationConfig.compute_hash)Provide a hash that uniquely identifies all the configs

-
–[custom_op_log_check](https://docs.vllm.ai#vllm.config.CompilationConfig.custom_op_log_check)This method logs the enabled/disabled custom ops and checks that the

-
–[get_compile_ranges](https://docs.vllm.ai#vllm.config.CompilationConfig.get_compile_ranges)Get the compile ranges for the compilation config.

-
–[init_backend](https://docs.vllm.ai#vllm.config.CompilationConfig.init_backend)Initialize the backend for the compilation config from a vllm config.

-
–[post_init_cudagraph_sizes](https://docs.vllm.ai#vllm.config.CompilationConfig.post_init_cudagraph_sizes)To complete the initialization after cudagraph related

-
–[validate_cudagraph_mode_before](https://docs.vllm.ai#vllm.config.CompilationConfig.validate_cudagraph_mode_before)Enable parsing of the

`cudagraph_mode`

enum type from string. -
–[validate_mode_before](https://docs.vllm.ai#vllm.config.CompilationConfig.validate_mode_before)Enable parsing the

`mode`

field from string mode names. -
–[validate_pass_config_before](https://docs.vllm.ai#vllm.config.CompilationConfig.validate_pass_config_before)Enable parsing of the

`pass_config`

field from a dictionary.

Attributes:

-
([backend](https://docs.vllm.ai#vllm.config.CompilationConfig.backend)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The backend for compilation. It needs to be a string:

-
([cache_dir](https://docs.vllm.ai#vllm.config.CompilationConfig.cache_dir)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The directory to store the compiled graph, to accelerate Inductor

-
([compilation_time](https://docs.vllm.ai#vllm.config.CompilationConfig.compilation_time)

) –[float](https://docs.python.org/3/builtins/functions.html#float)time taken for compilation

-
([compile_cache_save_format](https://docs.vllm.ai#vllm.config.CompilationConfig.compile_cache_save_format)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['binary', 'unpacked']Format for saving torch compile cache:

-
([compile_mm_encoder](https://docs.vllm.ai#vllm.config.CompilationConfig.compile_mm_encoder)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether or not to compile the multimodal encoder.

-
([compile_ranges_endpoints](https://docs.vllm.ai#vllm.config.CompilationConfig.compile_ranges_endpoints)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | NoneEndpoints for Inductor compile ranges.

-
([compile_sizes](https://docs.vllm.ai#vllm.config.CompilationConfig.compile_sizes)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)|[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | NoneSizes to compile for inductor. In addition

-
([cudagraph_capture_sizes](https://docs.vllm.ai#vllm.config.CompilationConfig.cudagraph_capture_sizes)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]Sizes to capture cudagraph.

-
([cudagraph_copy_inputs](https://docs.vllm.ai#vllm.config.CompilationConfig.cudagraph_copy_inputs)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to copy input tensors for

-
([cudagraph_mm_encoder](https://docs.vllm.ai#vllm.config.CompilationConfig.cudagraph_mm_encoder)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable CUDA graph capture for multimodal encoder (ViT).

-
([cudagraph_mode](https://docs.vllm.ai#vllm.config.CompilationConfig.cudagraph_mode)

) –[CUDAGraphMode](https://docs.vllm.ai/compilation/#vllm.config.compilation.CUDAGraphMode)The mode of the cudagraph:

-
([cudagraph_num_of_warmups](https://docs.vllm.ai#vllm.config.CompilationConfig.cudagraph_num_of_warmups)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of warmup runs for cudagraph.

-
([cudagraph_specialize_lora](https://docs.vllm.ai#vllm.config.CompilationConfig.cudagraph_specialize_lora)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to create separate cuda graphs for cases with and without active

-
([custom_ops](https://docs.vllm.ai#vllm.config.CompilationConfig.custom_ops)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Fine-grained control over which custom ops to enable/disable. Use 'all'

-
([debug_dump_path](https://docs.vllm.ai#vllm.config.CompilationConfig.debug_dump_path)

) –[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)| NoneThe path to dump the debug information.

-
([disabled_custom_ops](https://docs.vllm.ai#vllm.config.CompilationConfig.disabled_custom_ops)

) –[Counter](https://docs.python.org/3/library/collections.html#collections.Counter)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]custom ops that are disabled

-
([dynamic_shapes_config](https://docs.vllm.ai#vllm.config.CompilationConfig.dynamic_shapes_config)

) –[DynamicShapesConfig](https://docs.vllm.ai/compilation/#vllm.config.compilation.DynamicShapesConfig)Configuration for dynamic shapes options

-
([enabled_custom_ops](https://docs.vllm.ai#vllm.config.CompilationConfig.enabled_custom_ops)

) –[Counter](https://docs.python.org/3/library/collections.html#collections.Counter)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]custom ops that are enabled

-
([encoder_compilation_time](https://docs.vllm.ai#vllm.config.CompilationConfig.encoder_compilation_time)

) –[float](https://docs.python.org/3/builtins/functions.html#float)time taken for multimodal encoder compilation

-
([encoder_cudagraph_max_frames_per_batch](https://docs.vllm.ai#vllm.config.CompilationConfig.encoder_cudagraph_max_frames_per_batch)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMaximum total video frames per batch for encoder CUDA graph capture.

-
([encoder_cudagraph_max_vision_items_per_batch](https://docs.vllm.ai#vllm.config.CompilationConfig.encoder_cudagraph_max_vision_items_per_batch)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum number of images/videos per batch for encoder CUDA graph capture.

-
([encoder_cudagraph_token_budgets](https://docs.vllm.ai#vllm.config.CompilationConfig.encoder_cudagraph_token_budgets)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]Token budget levels for encoder CUDA graph capture.

-
([fast_moe_cold_start](https://docs.vllm.ai#vllm.config.CompilationConfig.fast_moe_cold_start)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneOptimization for fast MOE cold start.

-
([inductor_compile_config](https://docs.vllm.ai#vllm.config.CompilationConfig.inductor_compile_config)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)Additional configurations for inductor.

-
([inductor_passes](https://docs.vllm.ai#vllm.config.CompilationConfig.inductor_passes)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Additional passes for inductor. It is a dictionary

-
([ir_enable_torch_wrap](https://docs.vllm.ai#vllm.config.CompilationConfig.ir_enable_torch_wrap)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If True, enable vllm_ir torch custom op wrapping during the forward pass.

-
([local_cache_dir](https://docs.vllm.ai#vllm.config.CompilationConfig.local_cache_dir)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)local cache dir for each rank

-
([max_cudagraph_capture_size](https://docs.vllm.ai#vllm.config.CompilationConfig.max_cudagraph_capture_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The maximum cudagraph capture size.

-
([mode](https://docs.vllm.ai#vllm.config.CompilationConfig.mode)

) –[CompilationMode](https://docs.vllm.ai/compilation/#vllm.config.compilation.CompilationMode)The compilation approach used for torch.compile-based compilation of the

-
([pass_config](https://docs.vllm.ai#vllm.config.CompilationConfig.pass_config)

) –[PassConfig](https://docs.vllm.ai/compilation/#vllm.config.compilation.PassConfig)Custom inductor passes, see PassConfig for more details

-
([splitting_ops](https://docs.vllm.ai#vllm.config.CompilationConfig.splitting_ops)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | NoneA list of ops to exclude from cudagraphs, used in piecewise compilation.

-
([static_all_moe_layers](https://docs.vllm.ai#vllm.config.CompilationConfig.static_all_moe_layers)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The names of all the MOE layers in the model

-
([static_forward_context](https://docs.vllm.ai#vllm.config.CompilationConfig.static_forward_context)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)]Per-model forward context

-
([traced_files](https://docs.vllm.ai#vllm.config.CompilationConfig.traced_files)

) –[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]files that are traced for compilation

-
([use_inductor_graph_partition](https://docs.vllm.ai#vllm.config.CompilationConfig.use_inductor_graph_partition)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Use inductor graph partition to split the graph at cudagraph_unsafe ops.


## Source code in `vllm/config/compilation.py`


|
|

###

`backend = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.backend)

The backend for compilation. It needs to be a string:

- "" (empty string): use the default backend ("inductor" on CUDA-alike platforms).
- "eager"/"openxla"/...: use the specified backend registered in PyTorch.
- "full.module.name": a qualified name which can be used to import the

backend function. We use string to avoid serialization issues when using compilation in a distributed setting. When the compilation mode is 1 or 2, the backend is used for the compilation directly (it sees the whole graph). When the compilation mode is 3, the backend supports both whole graph and piecewise compilation, available backends include eager, inductor, and custom backends, the latter of which can be defined via `get_compile_backend`

. Furthermore, compilation is only piecewise if splitting ops is set accordingly and use_inductor_graph_partition is off. Note that the default options for splitting ops are sufficient for piecewise compilation.

###

`cache_dir = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.cache_dir)

The directory to store the compiled graph, to accelerate Inductor compilation. By default, it will use model-related information to generate a cache directory.

###

`compilation_time = field(default=0.0, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.compilation_time)

time taken for compilation

###

`compile_cache_save_format = field(default_factory=(lambda: envs.VLLM_COMPILE_CACHE_SAVE_FORMAT))`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.compile_cache_save_format)

Format for saving torch compile cache:

-
"binary": saves as binary file (multiprocess safe)

-
"unpacked": saves as directory structure for inspection/debugging (NOT multiprocess safe)


Defaults to `VLLM_COMPILE_CACHE_SAVE_FORMAT`

if not specified.

###

`compile_mm_encoder = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.compile_mm_encoder)

Whether or not to compile the multimodal encoder. Currently, this only works for `Qwen2_5_vl`

and `mLLaMa4`

models on selected platforms. It may also work for models loaded with the Transformers modeling backend if the encoder is compilable. Disabled by default until more models are supported/tested to work.

###

`compile_ranges_endpoints = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.compile_ranges_endpoints)

Endpoints for Inductor compile ranges. The compile ranges are [1, endpoints[0]], [endpoints[0] + 1, endpoints[1]], ..., [endpoints[-1] + 1, max_num_batched_tokens]. Compile sizes are also used single element ranges, the range is represented as [compile_sizes[i], compile_sizes[i]].

If a range overlaps with the compile size, graph for compile size will be prioritized, i.e. if we have a range [1, 8] and a compile size 4, graph for compile size 4 will be compiled and used instead of the graph for range [1, 8].

###

`compile_sizes = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.compile_sizes)

Sizes to compile for inductor. In addition to integers, it also supports "cudagraph_capture_sizes" to specify the sizes for cudagraph capture.

###

`cudagraph_capture_sizes = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.cudagraph_capture_sizes)

Sizes to capture cudagraph. - None (default): capture sizes are inferred from vllm config. - list[int]: capture sizes are specified as given.

###

`cudagraph_copy_inputs = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.cudagraph_copy_inputs)

Whether to copy input tensors for cudagraph. If the caller can guarantee that the same input buffers are always used, it can set this to False. Otherwise, it should set this to True, and the compiler will copy the input to an internally managed buffer. Default is False. Note that this flag is only effective when cudagraph_mode is PIECEWISE.

###

`cudagraph_mm_encoder = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.cudagraph_mm_encoder)

Enable CUDA graph capture for multimodal encoder (ViT). When enabled, captures full encoder forward as CUDA graph for each token budget level.

###

`cudagraph_mode = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.cudagraph_mode)

The mode of the cudagraph:

- NONE, no cudagraph capture.
- PIECEWISE.
- FULL.
- FULL_DECODE_ONLY.
- FULL_AND_PIECEWISE. (v1 default)

PIECEWISE mode build piecewise cudagraph only, keeping the cudagraph incompatible ops (i.e. some attention ops) outside the cudagraph for general flexibility.

FULL mode: Capture full cudagraph for all batches. Can be good for small models or workloads with small prompts; not supported by many backends. Generally for performance FULL_AND_PIECEWISE is better.

FULL_DECODE_ONLY mode: Capture full cudagraph for decode batches only. Mixed prefill-decode batches are run without cudagraphs. Can be good for decode instances in a P/D setup where prefill is not as important so we can save some memory.

FULL_AND_PIECEWISE mode: Capture full cudagraph for decode batches and piecewise cudagraph for prefill and mixed prefill-decode batches. This is the most performant mode for most models and is the default.

Currently, the cudagraph mode is only used for the v1 engine. Note that the cudagraph logic is generally orthogonal to the compilation logic. While piecewise cudagraphs require piecewise compilation (mode=VLLM_COMPILE and non-empty splitting_ops), full cudagraphs are supported with and without compilation.

Warning: This flag is new and subject to change in addition more modes may be added.

###

`cudagraph_num_of_warmups = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.cudagraph_num_of_warmups)

Number of warmup runs for cudagraph. It means the first several runs will be treated as warmup runs. Only after that, the execution will be recorded, and the recorded cudagraph will be used for subsequent runs.

###

`cudagraph_specialize_lora = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.cudagraph_specialize_lora)

Whether to create separate cuda graphs for cases with and without active LoRA adapters. When set to False, the LoRA-enabled cuda graph will be used for all cases, incurring the overhead of running LoRA ops even when no adapters are active. Setting this to True will remove this overhead at the cost of increased startup time and slightly higher memory usage. When `enable_lora`

is False, this option has no effect.

###

`custom_ops = field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.custom_ops)

Fine-grained control over which custom ops to enable/disable. Use 'all' to enable all, 'none' to disable all. Also specify a list of custom op names to enable (prefixed with a '+'), or disable (prefixed with a '-'). Examples:

- 'all,-op1' to enable all except op1
- 'none,+op1,+op2' to enable only op1 and op2

By default, all custom ops are enabled when running without Inductor and disabled when running with Inductor: mode>CompilationMode.NONE and backend="inductor". Inductor generates (fused) Triton kernels for disabled custom ops.

###

`debug_dump_path = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.debug_dump_path)

The path to dump the debug information.

###

`disabled_custom_ops = field(default_factory=Counter, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.disabled_custom_ops)

custom ops that are disabled

###

`dynamic_shapes_config = field(default_factory=DynamicShapesConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.dynamic_shapes_config)

Configuration for dynamic shapes options

###

`enabled_custom_ops = field(default_factory=Counter, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.enabled_custom_ops)

custom ops that are enabled

###

`encoder_compilation_time = field(default=0.0, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.encoder_compilation_time)

time taken for multimodal encoder compilation

###

`encoder_cudagraph_max_frames_per_batch = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.encoder_cudagraph_max_frames_per_batch)

Maximum total video frames per batch for encoder CUDA graph capture. Controls the cu_seqlens buffer size (one entry per attention sequence, i.e. one per video frame). If None (default), auto-inferred as encoder_cudagraph_max_vision_items_per_batch * max_frames_per_video (model-specific value according to processing_info). Positive value overrides auto-inference and applies to all budget levels. If we limit the video count per prompt to `0`

, it will also be set to `0`

(i.e., fall back to image-only mode).

###

`encoder_cudagraph_max_vision_items_per_batch = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.encoder_cudagraph_max_vision_items_per_batch)

Maximum number of images/videos per batch for encoder CUDA graph capture. Determines the fixed batch size used during graph capture. If 0 (default), auto-inferred as max_budget // min_budget from the model's budget range. User-provided positive value overrides auto-inference.

###

`encoder_cudagraph_token_budgets = field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.encoder_cudagraph_token_budgets)

Token budget levels for encoder CUDA graph capture. Each budget defines a fixed token capacity. At runtime, images are greedy-packed into the smallest fitting budget and the corresponding CUDA graph is replayed. If empty (default), auto-inferred from model architecture as power-of-2 levels from the model's estimated min budget to max budget. User-provided values override auto-inference. Example: [2048, 4096, 8192, 13824]

###

`fast_moe_cold_start = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.fast_moe_cold_start)

Optimization for fast MOE cold start.

This is a bit of a hack that assumes that: 1. the only decoder forward pass being run is the current model 2. the decoder forward pass runs all of the MOEs in the order in which they are initialized

When the above two conditions hold, this option greatly decreases cold start time for MOE models.

The options are: - True: optimization is always on - False: optimization is always off - None: optimization is on usually but off for speculative decoding

If conditions 1&2 don't hold then this option will lead to silent incorrectness. The only condition in which this doesn't hold is speculative decoding, where there is a draft model that may have MOEs in them.

NB: We're working on a longer-term solution that doesn't need these assumptions.

###

`inductor_compile_config = field(default_factory=dict)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.inductor_compile_config)

Additional configurations for inductor. - None: use default configurations.

###

`inductor_passes = field(default_factory=dict)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.inductor_passes)

Additional passes for inductor. It is a dictionary from pass name to pass function qualified name. We use function name because the config uses JSON format. If we pass the config from Python, functions can also be passed directly via Python object constructor, e.g. `CompilationConfig(inductor_passes={"a": func})`

.

###

`ir_enable_torch_wrap = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.ir_enable_torch_wrap)

If True, enable vllm_ir torch custom op wrapping during the forward pass. When False, torch custom op wrapping is disabled, allowing Dynamo to trace the selected implementation directly or avoiding torch custom op overhead in eager mode. Defaults to True when using Inductor with vllm-compile (backend=="inductor" and mode == VLLM_COMPILE), False otherwise.

###

`local_cache_dir = field(default=None, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.local_cache_dir)

local cache dir for each rank

###

`max_cudagraph_capture_size = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.max_cudagraph_capture_size)

The maximum cudagraph capture size.

If cudagraph_capture_sizes is specified, this will be set to the largest size in that list (or checked for consistency if specified). If cudagraph_capture_sizes is not specified, the list of sizes is generated automatically following the pattern:

```
[1, 2, 4] + list(range(8, 256, 8)) + list(
range(256, max_cudagraph_capture_size + 1, 16))
```


If not specified, max_cudagraph_capture_size is capped at 512 by default, or 1024 on data center Blackwell GPUs. This avoids OOM in tight memory scenarios with small max_num_seqs, and limits capture of large graphs that increase startup time and memory usage. Uniform decode sizes are appended only within this default ceiling.

###

`mode = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.mode)

The compilation approach used for torch.compile-based compilation of the model.

- None: If None, we will select the default compilation mode. For V1 engine this is 3.
- 0: NONE: No torch.compile compilation is applied, model runs in fully eager pytorch mode. The model runs as-is.
- 1: STOCK_TORCH_COMPILE: The standard
`torch.compile`

compilation pipeline. - 2: DYNAMO_TRACE_ONCE: Single Dynamo trace through the model, avoiding recompilation by removing guards. Requires no dynamic-shape-dependent control-flow.
- 3: VLLM_COMPILE: Custom vLLM Inductor-based backend with caching, piecewise compilation, shape specialization, and custom passes.

###

`pass_config = field(default_factory=PassConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.pass_config)

Custom inductor passes, see PassConfig for more details

###

`splitting_ops = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.splitting_ops)

A list of ops to exclude from cudagraphs, used in piecewise compilation.

The behavior depends on use_inductor_graph_partition:

-
When use_inductor_graph_partition=False (default): These ops are used for Dynamo FX-level graph splitting. The graph is split at these ops before Inductor compilation, creating separate subgraphs for cudagraph capture.

-
When use_inductor_graph_partition=True: These ops are used to register Inductor partition rules. The graph partitioning happens at Inductor codegen time after all passes and fusions are finished, allowing compilation and custom passes to operate on the full graph while still excluding these ops from cudagraphs.


If None, defaults to attention ops for piecewise cudagraphs. If empty list [], no ops are excluded (suitable for full cudagraphs).

###

`static_all_moe_layers = field(default_factory=list, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.static_all_moe_layers)

The names of all the MOE layers in the model

###

`static_forward_context = field(default_factory=dict, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.static_forward_context)

Per-model forward context Map from layer name to layer objects that need to be accessed outside model code, e.g., Attention, FusedMOE when dp_size>1.

###

`traced_files = field(default_factory=set, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.traced_files)

files that are traced for compilation

###

`use_inductor_graph_partition = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.use_inductor_graph_partition)

Use inductor graph partition to split the graph at cudagraph_unsafe ops. This partition happens at inductor codegen time after all passes and fusions are finished. It generates a single `call`

function which wraps cudagraph-safe ops into partition functions and leave cudagraph-unsafe ops outside the partition functions. For a graph with N cudagraph-unsafe ops (e.g., Attention), there would be N+1 partitions. To mark an op as cudagraph unsafe, we can add `tags=(torch._C.Tag.cudagraph_unsafe)`

when register the custom op.

This config supports both full cudagraph and piecewise cudagraph without compiling twice. For piecewise cudagraph, it applies vLLM CUDAGraph wrapper to each partition. For N+1 partitions, there would be N+1 CUDAGraph wrapper instances.

For full CUDAGraph, we always apply a single CUDAGraph wrapper outside the inductor `call`

function in the model runner. The top-level full cudagraph capture ignores all partitioning.

###

`_skip_none_validation(value, handler)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig._skip_none_validation)

Skip validation if the value is `None`

when initialisation is delayed.

## Source code in `vllm/config/compilation.py`


###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.compute_hash)

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

## Source code in `vllm/config/compilation.py`


###

`custom_op_log_check()`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.custom_op_log_check)

This method logs the enabled/disabled custom ops and checks that the passed custom_ops field only contains relevant ops. It is called at the end of set_current_vllm_config, after the custom ops have been instantiated.

## Source code in `vllm/config/compilation.py`


###

`get_compile_ranges()`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.get_compile_ranges)

Get the compile ranges for the compilation config.

## Source code in `vllm/config/compilation.py`


###

`init_backend(vllm_config, prefix='', is_encoder=False)`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.init_backend)

Initialize the backend for the compilation config from a vllm config.

Parameters:

-

(`vllm_config`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.init_backend(vllm_config))

) –[VllmConfig](https://docs.vllm.ai#vllm.config.VllmConfig)The vllm config to initialize the backend from.

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.init_backend(prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –Cache directory prefix for this compiled module.

-

(`is_encoder`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.init_backend(is_encoder))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether this module is used in an encoder (as opposed to a text backbone).


Returns:

## Source code in `vllm/config/compilation.py`


###

`post_init_cudagraph_sizes()`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.post_init_cudagraph_sizes)

To complete the initialization after cudagraph related configs are set. This includes: - initialize compile_sizes

## Source code in `vllm/config/compilation.py`


###

`validate_cudagraph_mode_before(value)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.validate_cudagraph_mode_before)

Enable parsing of the `cudagraph_mode`

enum type from string.

## Source code in `vllm/config/compilation.py`


###

`validate_mode_before(value)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.validate_mode_before)

Enable parsing the `mode`

field from string mode names. Accepts both integers (0-3) and string names, like NONE, STOCK_TORCH_COMPILE, DYNAMO_TRACE_ONCE, VLLM_COMPILE.

## Source code in `vllm/config/compilation.py`


###

`validate_pass_config_before(value)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.CompilationConfig.validate_pass_config_before)

Enable parsing of the `pass_config`

field from a dictionary.

## Source code in `vllm/config/compilation.py`


##

`CompilationMode`

[¶](https://docs.vllm.ai#vllm.config.CompilationMode)

Bases: [IntEnum](https://docs.python.org/3/library/enum.html#enum.IntEnum)

The compilation approach used for torch.compile-based compilation of the model.

Attributes:

-
–[DYNAMO_TRACE_ONCE](https://docs.vllm.ai#vllm.config.CompilationMode.DYNAMO_TRACE_ONCE)Single Dynamo trace through the model, avoiding recompilation.

-
–[NONE](https://docs.vllm.ai#vllm.config.CompilationMode.NONE)No torch.compile compilation is applied, model runs in fully eager pytorch mode.

-
–[STOCK_TORCH_COMPILE](https://docs.vllm.ai#vllm.config.CompilationMode.STOCK_TORCH_COMPILE)The standard

`torch.compile`

compilation pipeline. -
–[VLLM_COMPILE](https://docs.vllm.ai#vllm.config.CompilationMode.VLLM_COMPILE)Custom vLLM Inductor-based backend with caching, piecewise compilation,


## Source code in `vllm/config/compilation.py`


###

`DYNAMO_TRACE_ONCE = 2`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationMode.DYNAMO_TRACE_ONCE)

Single Dynamo trace through the model, avoiding recompilation.

###

`NONE = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationMode.NONE)

No torch.compile compilation is applied, model runs in fully eager pytorch mode. The model runs as-is.

###

`STOCK_TORCH_COMPILE = 1`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationMode.STOCK_TORCH_COMPILE)

The standard `torch.compile`

compilation pipeline.

###

`VLLM_COMPILE = 3`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.CompilationMode.VLLM_COMPILE)

Custom vLLM Inductor-based backend with caching, piecewise compilation, shape specialization, and custom passes.

##

`DeviceConfig`

[¶](https://docs.vllm.ai#vllm.config.DeviceConfig)

Configuration for the device to use for vLLM execution.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.DeviceConfig.compute_hash)WARNING: Whenever a new field is added to this config,


Attributes:

-
([device](https://docs.vllm.ai#vllm.config.DeviceConfig.device)`SkipValidation[Device |`

) –[device](https://pytorch.org/docs/stable/tensor_attributes.html#torch.device)| None]Device type for vLLM execution.

-
([device_type](https://docs.vllm.ai#vllm.config.DeviceConfig.device_type)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Device type from the current platform. This is set in


## Source code in `vllm/config/device.py`


###

`device = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.DeviceConfig.device)

Device type for vLLM execution. This parameter is deprecated and will be removed in a future release. It will now be set automatically based on the current platform.

###

`device_type = field(init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.DeviceConfig.device_type)

Device type from the current platform. This is set in `__post_init__`

.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.DeviceConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

## Source code in `vllm/config/device.py`


##

`DiffusionConfig`

[¶](https://docs.vllm.ai#vllm.config.DiffusionConfig)

Configuration for discrete diffusion language models (dLLMs).

dLLMs generate tokens via iterative denoising over a fixed-length canvas rather than left-to-right autoregressive decoding. They reuse the speculative-decoding data path (draft token ids, scheduled spec decode tokens) with overloaded semantics for block-based generation.

Attributes:

-
([canvas_length](https://docs.vllm.ai#vllm.config.DiffusionConfig.canvas_length)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Length of the denoising canvas (block). Also determines the number of

-
([max_denoising_steps](https://docs.vllm.ai#vllm.config.DiffusionConfig.max_denoising_steps)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMaximum number of denoising iterations per canvas block.


## Source code in `vllm/config/diffusion.py`


###

`canvas_length = Field(default=None, gt=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.DiffusionConfig.canvas_length)

Length of the denoising canvas (block). Also determines the number of speculative tokens scheduled per step.

###

`max_denoising_steps = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.DiffusionConfig.max_denoising_steps)

Maximum number of denoising iterations per canvas block. If not set, read from the model's generation_config.json.

##

`ECTransferConfig`

[¶](https://docs.vllm.ai#vllm.config.ECTransferConfig)

Configuration for distributed EC cache transfer.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.ECTransferConfig.compute_hash)WARNING: Whenever a new field is added to this config,


Attributes:

-
([ec_buffer_device](https://docs.vllm.ai#vllm.config.ECTransferConfig.ec_buffer_device)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe device used by ec connector to buffer the EC cache.

-
([ec_buffer_size](https://docs.vllm.ai#vllm.config.ECTransferConfig.ec_buffer_size)

) –[float](https://docs.python.org/3/builtins/functions.html#float)The buffer size for TorchDistributedConnector. Measured in number of

-
([ec_connector](https://docs.vllm.ai#vllm.config.ECTransferConfig.ec_connector)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe EC connector for vLLM to transmit EC caches between vLLM instances.

-
([ec_connector_extra_config](https://docs.vllm.ai#vllm.config.ECTransferConfig.ec_connector_extra_config)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)]any extra config that the connector may need.

-
([ec_connector_module_path](https://docs.vllm.ai#vllm.config.ECTransferConfig.ec_connector_module_path)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe Python module path to dynamically load the EC connector from.

-
([ec_ip](https://docs.vllm.ai#vllm.config.ECTransferConfig.ec_ip)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The EC connector ip, used to build distributed connection.

-
([ec_parallel_size](https://docs.vllm.ai#vllm.config.ECTransferConfig.ec_parallel_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The number of parallel instances for EC cache transfer. For

-
([ec_port](https://docs.vllm.ai#vllm.config.ECTransferConfig.ec_port)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The EC connector port, used to build distributed connection.

-
([ec_rank](https://docs.vllm.ai#vllm.config.ECTransferConfig.ec_rank)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneThe rank of this vLLM instance in the EC cache transfer. Typical value:

-
([ec_role](https://docs.vllm.ai#vllm.config.ECTransferConfig.ec_role)`ECRole | None`

) –Whether this vLLM instance produces, consumes EC cache, or both. Choices

-
([engine_id](https://docs.vllm.ai#vllm.config.ECTransferConfig.engine_id)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe engine id for EC transfers.

-
([is_encode_only](https://docs.vllm.ai#vllm.config.ECTransferConfig.is_encode_only)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether this instance encodes but does not run the language model.


## Source code in `vllm/config/ec_transfer.py`


|
|

###

`ec_buffer_device = 'cuda'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ECTransferConfig.ec_buffer_device)

The device used by ec connector to buffer the EC cache. Currently only support 'cuda'.

###

`ec_buffer_size = 1000000000.0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ECTransferConfig.ec_buffer_size)

The buffer size for TorchDistributedConnector. Measured in number of bytes. Recommended value: 1e9 (about 1GB).

###

`ec_connector = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ECTransferConfig.ec_connector)

The EC connector for vLLM to transmit EC caches between vLLM instances.

Built-in options include `ECExampleConnector`

(shared filesystem via safetensors) and `ECMooncakeConnector`

(Mooncake TransferEngine RDMA; requires `mooncake-transfer-engine`

and matching producer/consumer `ec_connector_extra_config`

; see `mooncake_ec_connector`

module docstring). Set `cross_encoder_cache`

in Mooncake extra config to reuse shared Encoder outputs from Store before encoding, retaining P2P delivery.

###

`ec_connector_extra_config = field(default_factory=dict)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ECTransferConfig.ec_connector_extra_config)

any extra config that the connector may need.

###

`ec_connector_module_path = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ECTransferConfig.ec_connector_module_path)

The Python module path to dynamically load the EC connector from. Only supported in V1.

###

`ec_ip = '127.0.0.1'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ECTransferConfig.ec_ip)

The EC connector ip, used to build distributed connection.

###

`ec_parallel_size = 1`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ECTransferConfig.ec_parallel_size)

The number of parallel instances for EC cache transfer. For PyNcclConnector, this should be 2.

###

`ec_port = 14579`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ECTransferConfig.ec_port)

The EC connector port, used to build distributed connection.

###

`ec_rank = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ECTransferConfig.ec_rank)

The rank of this vLLM instance in the EC cache transfer. Typical value: 0 for encoder, 1 for pd instance. Currently only 1P1D is supported.

###

`ec_role = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ECTransferConfig.ec_role)

Whether this vLLM instance produces, consumes EC cache, or both. Choices are 'ec_producer', 'ec_consumer', 'ec_both'.

###

`engine_id = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ECTransferConfig.engine_id)

The engine id for EC transfers.

###

`is_encode_only`

`property`

[¶](https://docs.vllm.ai#vllm.config.ECTransferConfig.is_encode_only)

Whether this instance encodes but does not run the language model.

It allocates no KV cache either -- `GPUModelRunner.get_kv_cache_spec`

returns {} for it -- so it is the one role that can spend accelerator time and memory on frontend work.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.ECTransferConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

## Source code in `vllm/config/ec_transfer.py`


##

`EPLBConfig`

[¶](https://docs.vllm.ai#vllm.config.EPLBConfig)

Configuration for Expert Parallel Load Balancing (EP).

Attributes:

-
([communicator](https://docs.vllm.ai#vllm.config.EPLBConfig.communicator)`EPLBCommunicatorBackend | None`

) –Backend for EPLB expert weight communication:

-
([log_balancedness](https://docs.vllm.ai#vllm.config.EPLBConfig.log_balancedness)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Log the balancedness each step of expert parallelism.

-
([log_balancedness_interval](https://docs.vllm.ai#vllm.config.EPLBConfig.log_balancedness_interval)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Interval for logging the balancedness.

-
([num_redundant_experts](https://docs.vllm.ai#vllm.config.EPLBConfig.num_redundant_experts)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of redundant experts to use for expert parallelism.

-
([policy](https://docs.vllm.ai#vllm.config.EPLBConfig.policy)`EPLBPolicyOption`

) –The policy type for expert parallel load balancing (EPLB).

-
([step_interval](https://docs.vllm.ai#vllm.config.EPLBConfig.step_interval)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Interval for rearranging experts in expert parallelism.

-
([use_async](https://docs.vllm.ai#vllm.config.EPLBConfig.use_async)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to use non-blocking EPLB.

-
([window_size](https://docs.vllm.ai#vllm.config.EPLBConfig.window_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Window size for expert load recording.


## Source code in `vllm/config/parallel.py`


###

`communicator = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.EPLBConfig.communicator)

Backend for EPLB expert weight communication: - "torch_nccl": Use torch.distributed on the device process group - "torch_gloo": Use torch.distributed gloo with CPU staging - "torch_xccl": Use torch.distributed XCCL device P2P on XPU - "nixl": Use NIXL with staged send/recv buffers - "pynccl": Use PyNccl send/recv - None: Auto-select backend ("torch_xccl" on XPU, prefers "nixl" on CUDA, falls back to "torch_gloo")

###

`log_balancedness = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.EPLBConfig.log_balancedness)

Log the balancedness each step of expert parallelism. This is turned off by default since it will cause communication overhead.

###

`log_balancedness_interval = Field(default=1, gt=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.EPLBConfig.log_balancedness_interval)

Interval for logging the balancedness.

###

`num_redundant_experts = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.EPLBConfig.num_redundant_experts)

Number of redundant experts to use for expert parallelism.

###

`policy = 'default'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.EPLBConfig.policy)

The policy type for expert parallel load balancing (EPLB).

###

`step_interval = Field(default=3000, gt=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.EPLBConfig.step_interval)

Interval for rearranging experts in expert parallelism.

Note that if this is greater than the EPLB window size, only the metrics of the last `lb_window_size`

steps will be used for rearranging experts.

###

`use_async = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.EPLBConfig.use_async)

Whether to use non-blocking EPLB.

###

`window_size = Field(default=1000, gt=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.EPLBConfig.window_size)

Window size for expert load recording.

##

`EncoderCacheManagerConfig`

[¶](https://docs.vllm.ai#vllm.config.EncoderCacheManagerConfig)

Attributes:

-
([encoder_cache_manager_cls](https://docs.vllm.ai#vllm.config.EncoderCacheManagerConfig.encoder_cache_manager_cls)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneFully qualified class name of the custom encoder cache manager.

-
([manager_config](https://docs.vllm.ai#vllm.config.EncoderCacheManagerConfig.manager_config)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)]Opaque configuration interpreted by the custom cache manager.


## Source code in `vllm/config/ec_manager_config.py`


##

`EngramConfig`

[¶](https://docs.vllm.ai#vllm.config.EngramConfig)

Configuration for Engram embedding storage and sharding.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.EngramConfig.compute_hash)Hash settings that affect embedding execution and graph structure.

-
–[get_parallel_size](https://docs.vllm.ai#vllm.config.EngramConfig.get_parallel_size)Derive the embedding group size from the parallel configuration.

-
–[resolve_dp_shared_memory](https://docs.vllm.ai#vllm.config.EngramConfig.resolve_dp_shared_memory)Share host tables by default wherever the configuration permits.

-
–[verify_model_config](https://docs.vllm.ai#vllm.config.EngramConfig.verify_model_config)Reject Engram configuration for models without n-gram embeddings.

-
–[verify_parallel_config](https://docs.vllm.ai#vllm.config.EngramConfig.verify_parallel_config)Reject unsupported embedding parallel topologies.


Attributes:

-
([cpu_offload](https://docs.vllm.ai#vllm.config.EngramConfig.cpu_offload)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Store embedding weights in pinned CPU memory for UVA lookup.

-
([dp_shared_memory](https://docs.vllm.ai#vllm.config.EngramConfig.dp_shared_memory)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneShare CPU-offloaded embedding weights between co-located

-
([embedding_across_dp](https://docs.vllm.ai#vllm.config.EngramConfig.embedding_across_dp)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Shard embeddings across TP and all DP ranks when enabled.


## Source code in `vllm/config/engram.py`


###

`cpu_offload = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.EngramConfig.cpu_offload)

Store embedding weights in pinned CPU memory for UVA lookup.

###

`dp_shared_memory = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.EngramConfig.dp_shared_memory)

Share CPU-offloaded embedding weights between co-located DP replicas. Each node stores one copy of every TP shard, reducing host memory without per-step Engram DP collectives. Requires sufficient /dev/shm capacity and a shared IPC namespace. Defaults to enabled whenever the other settings allow it, falling back to per-replica tables when DP replicas are not co-located on one node or /dev/shm cannot hold them.

###

`embedding_across_dp = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.EngramConfig.embedding_across_dp)

Shard embeddings across TP and all DP ranks when enabled. Otherwise, each DP rank has a separate TP-sharded embedding replica.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.EngramConfig.compute_hash)

###

`get_parallel_size(parallel_config)`

[¶](https://docs.vllm.ai#vllm.config.EngramConfig.get_parallel_size)

Derive the embedding group size from the parallel configuration.

## Source code in `vllm/config/engram.py`


###

`resolve_dp_shared_memory(parallel_config)`

[¶](https://docs.vllm.ai#vllm.config.EngramConfig.resolve_dp_shared_memory)

Share host tables by default wherever the configuration permits.

## Source code in `vllm/config/engram.py`


###

`verify_model_config(model_config)`

[¶](https://docs.vllm.ai#vllm.config.EngramConfig.verify_model_config)

Reject Engram configuration for models without n-gram embeddings.

## Source code in `vllm/config/engram.py`


###

`verify_parallel_config(parallel_config)`

[¶](https://docs.vllm.ai#vllm.config.EngramConfig.verify_parallel_config)

Reject unsupported embedding parallel topologies.

## Source code in `vllm/config/engram.py`


##

`FaultToleranceConfig`

[¶](https://docs.vllm.ai#vllm.config.FaultToleranceConfig)

Configuration for fault tolerance.

Attributes:

-
([engine_recovery_timeout_sec](https://docs.vllm.ai#vllm.config.FaultToleranceConfig.engine_recovery_timeout_sec)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Timeout (in seconds) to wait for error handling instructions


## Source code in `vllm/config/fault_tolerance.py`


###

`engine_recovery_timeout_sec = 120`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.FaultToleranceConfig.engine_recovery_timeout_sec)

Timeout (in seconds) to wait for error handling instructions before raising an exception. If the EngineCore encounters an error, it waits up to this many seconds for vLLM to receive instructions on how to handle the error and then recover from the fault. If vLLM does not recover during this time, the original error is raised.

##

`HiSparseConfig`

[¶](https://docs.vllm.ai#vllm.config.HiSparseConfig)

Configuration for HiSparse sparse-MLA KV offloading.

Attributes:

-
([device_buffer_size](https://docs.vllm.ai#vllm.config.HiSparseConfig.device_buffer_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneTotal per-request GPU hot-buffer rows, including the newest-token slot.

-
([eager_host_mirror](https://docs.vllm.ai#vllm.config.HiSparseConfig.eager_host_mirror)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Mirror decode-written KV rows to the host pool during the forward so


## Source code in `vllm/config/attention.py`


###

`device_buffer_size = Field(default=None, gt=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.HiSparseConfig.device_buffer_size)

Total per-request GPU hot-buffer rows, including the newest-token slot.

Defaults to one top-k per decode query plus one top-k of LRU slack. The physical allocation is rounded up to the GPU cache block size selected from the active backends.

###

`eager_host_mirror = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.HiSparseConfig.eager_host_mirror)

Mirror decode-written KV rows to the host pool during the forward so page spills complete without moving data. When disabled, decode rows stay resident-only and evicted pages are copied to host at spill time. Prefill rows are always mirrored during the forward.

##

`KVEventsConfig`

[¶](https://docs.vllm.ai#vllm.config.KVEventsConfig)

Configuration for KV event publishing.

Attributes:

-
([buffer_steps](https://docs.vllm.ai#vllm.config.KVEventsConfig.buffer_steps)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The number of steps to cache for replay endpoint. Will only save

-
([enable_kv_cache_events](https://docs.vllm.ai#vllm.config.KVEventsConfig.enable_kv_cache_events)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If True, enable KV cache events for tracking block storage and removal.

-
([endpoint](https://docs.vllm.ai#vllm.config.KVEventsConfig.endpoint)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The zmq endpoint to use for publishing kv events.

-
([hwm](https://docs.vllm.ai#vllm.config.KVEventsConfig.hwm)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The zmq high water mark for the event publisher. After queueing N events,

-
([max_queue_size](https://docs.vllm.ai#vllm.config.KVEventsConfig.max_queue_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The maximum number of events to queue while waiting for publishing.

-
([publisher](https://docs.vllm.ai#vllm.config.KVEventsConfig.publisher)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['null', 'zmq']The publisher to use for publishing kv events. Can be "null", "zmq".

-
([replay_endpoint](https://docs.vllm.ai#vllm.config.KVEventsConfig.replay_endpoint)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe zmq endpoint to use for replaying kv events.

-
([topic](https://docs.vllm.ai#vllm.config.KVEventsConfig.topic)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The topic to use for the event publisher. Consumers can subscribe to


## Source code in `vllm/config/kv_events.py`


###

`buffer_steps = 10000`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KVEventsConfig.buffer_steps)

The number of steps to cache for replay endpoint. Will only save events from the last N steps for the replay endpoint.

###

`enable_kv_cache_events = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KVEventsConfig.enable_kv_cache_events)

If True, enable KV cache events for tracking block storage and removal. Events can be published externally by zmq using the event publisher config.

###

`endpoint = 'tcp://*:5557'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KVEventsConfig.endpoint)

The zmq endpoint to use for publishing kv events.

###

`hwm = 100000`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KVEventsConfig.hwm)

The zmq high water mark for the event publisher. After queueing N events, events will start dropping if the consumer is not keeping up.

###

`max_queue_size = 100000`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KVEventsConfig.max_queue_size)

The maximum number of events to queue while waiting for publishing.

###

`publisher = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KVEventsConfig.publisher)

The publisher to use for publishing kv events. Can be "null", "zmq".

###

`replay_endpoint = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KVEventsConfig.replay_endpoint)

The zmq endpoint to use for replaying kv events.

###

`topic = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KVEventsConfig.topic)

The topic to use for the event publisher. Consumers can subscribe to this topic to receive events.

##

`KVTransferConfig`

[¶](https://docs.vllm.ai#vllm.config.KVTransferConfig)

Configuration for distributed KV cache transfer.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.KVTransferConfig.compute_hash)WARNING: Whenever a new field is added to this config,

-
–[has_connector](https://docs.vllm.ai#vllm.config.KVTransferConfig.has_connector)Whether

`connector_name`

is configured, directly or in MultiConnector.

Attributes:

-
([enable_permute_local_kv](https://docs.vllm.ai#vllm.config.KVTransferConfig.enable_permute_local_kv)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Experiment feature flag to enable HND to NHD KV Transfer

-
([engine_id](https://docs.vllm.ai#vllm.config.KVTransferConfig.engine_id)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe engine id for KV transfers.

-
([kv_buffer_device](https://docs.vllm.ai#vllm.config.KVTransferConfig.kv_buffer_device)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The device used by kv connector to buffer the KV cache. Choices are

-
([kv_buffer_size](https://docs.vllm.ai#vllm.config.KVTransferConfig.kv_buffer_size)

) –[float](https://docs.python.org/3/builtins/functions.html#float)The buffer size for TorchDistributedConnector. Measured in number of

-
([kv_connector](https://docs.vllm.ai#vllm.config.KVTransferConfig.kv_connector)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe KV connector for vLLM to transmit KV caches between vLLM instances.

-
([kv_connector_extra_config](https://docs.vllm.ai#vllm.config.KVTransferConfig.kv_connector_extra_config)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)]any extra config that the connector may need.

-
([kv_connector_module_path](https://docs.vllm.ai#vllm.config.KVTransferConfig.kv_connector_module_path)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe Python module path to dynamically load the KV connector from.

-
([kv_ip](https://docs.vllm.ai#vllm.config.KVTransferConfig.kv_ip)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The KV connector ip, used to build distributed connection.

-
([kv_load_failure_policy](https://docs.vllm.ai#vllm.config.KVTransferConfig.kv_load_failure_policy)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['recompute', 'fail']Policy for handling KV cache load failures.

-
([kv_parallel_size](https://docs.vllm.ai#vllm.config.KVTransferConfig.kv_parallel_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The number of parallel instances for KV cache transfer.

-
([kv_port](https://docs.vllm.ai#vllm.config.KVTransferConfig.kv_port)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The KV connector port, used to build distributed connection.

-
([kv_rank](https://docs.vllm.ai#vllm.config.KVTransferConfig.kv_rank)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneThe rank of this vLLM instance in the KV cache transfer. Typical value:

-
([kv_role](https://docs.vllm.ai#vllm.config.KVTransferConfig.kv_role)`KVRole | None`

) –Whether this vLLM instance produces, consumes KV cache, or both. Choices


## Source code in `vllm/config/kv_transfer.py`


|
|

###

`enable_permute_local_kv = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KVTransferConfig.enable_permute_local_kv)

Experiment feature flag to enable HND to NHD KV Transfer

###

`engine_id = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KVTransferConfig.engine_id)

The engine id for KV transfers.

###

`kv_buffer_device = field(default_factory=kv_buffer_device_default_factory)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KVTransferConfig.kv_buffer_device)

The device used by kv connector to buffer the KV cache. Choices are 'cuda', 'cpu' and 'xpu'.

###

`kv_buffer_size = 1000000000.0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KVTransferConfig.kv_buffer_size)

The buffer size for TorchDistributedConnector. Measured in number of bytes. Recommended value: 1e9 (about 1GB).

###

`kv_connector = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KVTransferConfig.kv_connector)

The KV connector for vLLM to transmit KV caches between vLLM instances.

###

`kv_connector_extra_config = field(default_factory=dict)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KVTransferConfig.kv_connector_extra_config)

any extra config that the connector may need.

###

`kv_connector_module_path = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KVTransferConfig.kv_connector_module_path)

The Python module path to dynamically load the KV connector from. Only supported in V1.

###

`kv_ip = '127.0.0.1'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KVTransferConfig.kv_ip)

The KV connector ip, used to build distributed connection.

###

`kv_load_failure_policy = 'fail'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KVTransferConfig.kv_load_failure_policy)

Policy for handling KV cache load failures. 'recompute': reschedule the request to recompute failed blocks 'fail': immediately fail the request with an error finish reason (default)

###

`kv_parallel_size = 1`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KVTransferConfig.kv_parallel_size)

The number of parallel instances for KV cache transfer.

###

`kv_port = 14579`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KVTransferConfig.kv_port)

The KV connector port, used to build distributed connection.

###

`kv_rank = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KVTransferConfig.kv_rank)

The rank of this vLLM instance in the KV cache transfer. Typical value: 0 for prefill instance, 1 for decode instance. Currently only 1P1D is supported.

###

`kv_role = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KVTransferConfig.kv_role)

Whether this vLLM instance produces, consumes KV cache, or both. Choices are 'kv_producer', 'kv_consumer', and 'kv_both'.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.KVTransferConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

## Source code in `vllm/config/kv_transfer.py`


###

`has_connector(connector_name)`

[¶](https://docs.vllm.ai#vllm.config.KVTransferConfig.has_connector)

Whether `connector_name`

is configured, directly or in MultiConnector.

## Source code in `vllm/config/kv_transfer.py`


##

`KernelConfig`

[¶](https://docs.vllm.ai#vllm.config.KernelConfig)

Configuration for kernel selection and warmup behavior.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.KernelConfig.compute_hash)Produces a hash unique to the pass configuration.

-
–[set_platform_defaults](https://docs.vllm.ai#vllm.config.KernelConfig.set_platform_defaults)Set platform-specific defaults for the kernel config.


Attributes:

-
([enable_cutedsl_warmup](https://docs.vllm.ai#vllm.config.KernelConfig.enable_cutedsl_warmup)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Deprecated: run legacy CuTeDSL warmup providers.

-
([enable_flashinfer_autotune](https://docs.vllm.ai#vllm.config.KernelConfig.enable_flashinfer_autotune)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If True, run FlashInfer autotuning during kernel warmup.

-
([enable_jit_warmup](https://docs.vllm.ai#vllm.config.KernelConfig.enable_jit_warmup)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If True, run JIT compile warmup during kernel warmup.

-
([ir_op_priority](https://docs.vllm.ai#vllm.config.KernelConfig.ir_op_priority)

) –[IrOpPriorityConfig](https://docs.vllm.ai/kernel/#vllm.config.kernel.IrOpPriorityConfig)vLLM IR op priority for dispatching/lowering during the forward pass.

-
([linear_backend](https://docs.vllm.ai#vllm.config.KernelConfig.linear_backend)`LinearBackend`

) –Backend for linear layer GEMM kernels. Available options:

-
([linear_backend_per_quant](https://docs.vllm.ai#vllm.config.KernelConfig.linear_backend_per_quant)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), LinearBackend] | NoneBackend overrides keyed by linear quantization scheme. Overrides take

-
([moe_backend](https://docs.vllm.ai#vllm.config.KernelConfig.moe_backend)`MoEBackend`

) –Backend for MoE expert computation kernels. Available options:

-
([sparse_indexer_topk_backend](https://docs.vllm.ai#vllm.config.KernelConfig.sparse_indexer_topk_backend)`SparseIndexerTopkBackend`

) –Backend for the DSA sparse indexer decode top-k kernel. Available options:


## Source code in `vllm/config/kernel.py`


|
|

###

`enable_cutedsl_warmup = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KernelConfig.enable_cutedsl_warmup)

Deprecated: run legacy CuTeDSL warmup providers.

###

`enable_flashinfer_autotune = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KernelConfig.enable_flashinfer_autotune)

If True, run FlashInfer autotuning during kernel warmup.

###

`enable_jit_warmup = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KernelConfig.enable_jit_warmup)

If True, run JIT compile warmup during kernel warmup.

###

`ir_op_priority = Field(default_factory=IrOpPriorityConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KernelConfig.ir_op_priority)

vLLM IR op priority for dispatching/lowering during the forward pass. Platform defaults appended automatically during VllmConfig.**post_init**.

###

`linear_backend = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KernelConfig.linear_backend)

Backend for linear layer GEMM kernels. Available options:

Layer types without an implementation from the requested backend use automatic selection.

- "auto": Automatically select the best backend based on model and hardware
- "cutlass": Use CUTLASS-based kernels
- "flashinfer_cutlass": Use FlashInfer with CUTLASS kernels
- "flashinfer_cutedsl": Use FlashInfer with CuTe-DSL kernels (BF16, NVFP4, MXFP8, W4A16_NVFP4)
- "flashinfer_trtllm": Use FlashInfer with TensorRT-LLM kernels
- "flashinfer_cudnn": Use FlashInfer with cuDNN kernels
- "flashinfer_b12x": Use FlashInfer b12x CuteDSL NVFP4 GEMM (SM120+)
- "b12x": Use native B12X FP8 and FP4 linear kernels on SM12x
- "marlin": Use Marlin kernels
- "triton": Use Triton-based kernels
- "deep_gemm": Use DeepGEMM kernels
- "torch": Use PyTorch native scaled_mm kernels
- "aiter": Use AMD AITer kernels (ROCm only)
- "machete": Use Machete kernels (mixed-precision)
- "fbgemm": Use FBGEMM kernels
- "conch": Use Conch mixed-precision kernels
- "exllama": Use Exllama mixed-precision kernels
- "emulation": Use slow dequant-to-BF16 emulation (for testing only)
- "xpu": Use XPU kernels
- "xpu_woq": Use XPU kernels for weight-only quantization (e.g. W8A16)

###

`linear_backend_per_quant = Field(default=None, min_length=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KernelConfig.linear_backend_per_quant)

Backend overrides keyed by linear quantization scheme. Overrides take precedence over `linear_backend`

; for example, `{"nvfp4_w4a16": "humming"}`

.

###

`moe_backend = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KernelConfig.moe_backend)

Backend for MoE expert computation kernels. Available options:

- "auto": Automatically select the best backend based on model and hardware
- "triton": Use Triton-based fused MoE kernels
- "batched_triton": Use batched Triton experts (moe_mmk) on the batched activation format ([E_local, max_num_tokens, K])
- "deep_gemm": Use DeepGEMM kernels (FP8 block-quantized only)
- "deep_gemm_mega_moe": Use DeepGEMM mega MoE kernels
- "cutlass": Use vLLM CUTLASS kernels
- "flashinfer_trtllm": Use FlashInfer with TRTLLM-GEN kernels
- "flashinfer_cutlass": Use FlashInfer with CUTLASS kernels
- "flashinfer_cutedsl": Use FlashInfer with CuteDSL kernels (FP4 only)
- "flashinfer_b12x": Use FlashInfer CuteDSL fused MoE for SM12x (RTX Pro 6000 / DGX Spark)
- "b12x": Use b12x FP4 MoE kernels on SM12x
- "flashinfer_moe_ep_mega_deep_gemm": Use the FlashInfer moe_ep expert-parallel mega-MoE with the DeepGEMM megakernel, which consumes an MXFP4 checkpoint verbatim (Blackwell, requires expert parallel; DeepSeek-V4 only)
- "flashinfer_moe_ep_mega_cutedsl": Same, with the CuteDSL megakernel (additionally requires NVSHMEM). The checkpoint selects the weight path: an NVFP4 checkpoint is consumed prequantized, MXFP4 weights are requantized at load
- "marlin": Use Marlin kernels (weight-only quantization)
- "humming": Use Humming Mixed Precision kernels
- "triton_unfused": Use Triton unfused MoE kernels
- "aiter": Use AMD AITer kernels (ROCm only)
- "aiter_triton_mxfp4_bf16": Use the AITER Triton MXFP4 W4A16 (moe_gemm_a16w4) MoE kernel (ROCm gfx942/gfx950/gfx1250)
- "flydsl": Use AMD FlyDSL kernels (ROCm only)
- "rdna3": Use the fused RDNA3 W4A16 HIP kernel (ROCm gfx1100 only)
- "hpc": Use HPC kernels (FP8 and Hopper only)
- "emulation": use BF16/FP16 GEMM, dequantizing weights and running QDQ on activations.

###

`sparse_indexer_topk_backend = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.KernelConfig.sparse_indexer_topk_backend)

Backend for the DSA sparse indexer decode top-k kernel. Available options:

- "auto": The pre-existing chain (cooperative -> persistent -> per_row); the other backends are opt-in
- "deep_select": Use DeepSelect kernels (SM100a/SM103a only)
- "cooperative": Use vLLM's cooperative_topk kernel
- "persistent": Use vLLM's persistent_topk kernel
- "per_row": Use vLLM's top_k_per_row_decode kernel
- "flashinfer": Use FlashInfer's top_k_ragged_transform kernel
- "torch": Use a plain torch.topk implementation (debug reference)

Explicit values raise RuntimeError when their constraints are not met.

###

`_skip_none_validation(value, handler)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.KernelConfig._skip_none_validation)

Skip validation if the value is `None`

when initialization is delayed.

## Source code in `vllm/config/kernel.py`


###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.KernelConfig.compute_hash)

Produces a hash unique to the pass configuration. Any new fields that affect compilation should be added to the hash. Any future fields that don't affect compilation should be excluded.

## Source code in `vllm/config/kernel.py`


###

`set_platform_defaults(vllm_config)`

[¶](https://docs.vllm.ai#vllm.config.KernelConfig.set_platform_defaults)

Set platform-specific defaults for the kernel config.

## Source code in `vllm/config/kernel.py`


##

`LoRAConfig`

[¶](https://docs.vllm.ai#vllm.config.LoRAConfig)

Configuration for LoRA.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.LoRAConfig.compute_hash)WARNING: Whenever a new field is added to this config,


Attributes:

-
([default_mm_loras](https://docs.vllm.ai#vllm.config.LoRAConfig.default_mm_loras)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | NoneDictionary mapping specific modalities to LoRA model paths; this field

-
([enable_mixed_moe_lora_format](https://docs.vllm.ai#vllm.config.LoRAConfig.enable_mixed_moe_lora_format)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If True, force the engine to use the universal 2D MoE LoRA wrapper

-
([enable_moe_shared_loras](https://docs.vllm.ai#vllm.config.LoRAConfig.enable_moe_shared_loras)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If True, load MoE expert adapters in the "shared-outer" layout, where the

-
([enable_tower_connector_lora](https://docs.vllm.ai#vllm.config.LoRAConfig.enable_tower_connector_lora)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, LoRA support for the tower (vision encoder) and connector -
([fully_sharded_loras](https://docs.vllm.ai#vllm.config.LoRAConfig.fully_sharded_loras)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)By default, only half of the LoRA computation is sharded with tensor

-
([lora_dtype](https://docs.vllm.ai#vllm.config.LoRAConfig.lora_dtype)

) –[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)| LoRADTypeData type for LoRA. If auto, will default to base model dtype.

-
([max_cpu_loras](https://docs.vllm.ai#vllm.config.LoRAConfig.max_cpu_loras)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMaximum number of LoRAs to store in CPU memory. Must be >= than

-
([max_lora_rank](https://docs.vllm.ai#vllm.config.LoRAConfig.max_lora_rank)`MaxLoRARanks`

) –Max LoRA rank.

-
([max_loras](https://docs.vllm.ai#vllm.config.LoRAConfig.max_loras)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Max number of LoRAs in a single batch.

-
([specialize_active_lora](https://docs.vllm.ai#vllm.config.LoRAConfig.specialize_active_lora)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to construct lora kernel grid by the number of active LoRA adapters.

-
([target_modules](https://docs.vllm.ai#vllm.config.LoRAConfig.target_modules)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | NoneRestrict LoRA to specific module suffixes (e.g., ["o_proj", "qkv_proj"]).


## Source code in `vllm/config/lora.py`


|
|

###

`default_mm_loras = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.LoRAConfig.default_mm_loras)

Dictionary mapping specific modalities to LoRA model paths; this field is only applicable to multimodal models and should be leveraged when a model always expects a LoRA to be active when a given modality is present. Note that currently, if a request provides multiple additional modalities, each of which have their own LoRA, we do NOT apply default_mm_loras because we currently only support one lora adapter per prompt. When run in offline mode, the lora IDs for n modalities will be automatically assigned to 1-n with the names of the modalities in alphabetic order.

###

`enable_mixed_moe_lora_format = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.LoRAConfig.enable_mixed_moe_lora_format)

If True, force the engine to use the universal 2D MoE LoRA wrapper (`FusedMoEWithLoRA`

) regardless of the model's `is_3d_moe_weight`

flag, so that 2D-format and 3D-format MoE LoRA adapters can be served in the same deployment. Only meaningful for MoE models; ignored otherwise. Default False keeps the existing model-driven behavior.

###

`enable_moe_shared_loras = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.LoRAConfig.enable_moe_shared_loras)

If True, load MoE expert adapters in the "shared-outer" layout, where the gate/up (`w1`

/`w3`

) lora_A and the down (`w2`

) lora_B are shared across all experts (stored once with expert-dim 1) instead of per-expert. The shared factors are broadcast to the expert count at kernel time. Only meaningful for MoE models whose adapters use this layout; ignored otherwise.

###

`enable_tower_connector_lora = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.LoRAConfig.enable_tower_connector_lora)

If `True`

, LoRA support for the tower (vision encoder) and connector of multimodal models will be enabled. This is an experimental feature and currently only supports some MM models such as the Qwen VL series. The default is False.

###

`fully_sharded_loras = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.LoRAConfig.fully_sharded_loras)

By default, only half of the LoRA computation is sharded with tensor parallelism. Enabling this will use the fully sharded layers. At high sequence length, max rank or tensor parallel size, this is likely faster.

###

`lora_dtype = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.LoRAConfig.lora_dtype)

Data type for LoRA. If auto, will default to base model dtype.

###

`max_cpu_loras = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.LoRAConfig.max_cpu_loras)

Maximum number of LoRAs to store in CPU memory. Must be >= than `max_loras`

.

###

`max_lora_rank = 16`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.LoRAConfig.max_lora_rank)

Max LoRA rank.

###

`max_loras = Field(default=1, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.LoRAConfig.max_loras)

Max number of LoRAs in a single batch.

###

`specialize_active_lora = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.LoRAConfig.specialize_active_lora)

Whether to construct lora kernel grid by the number of active LoRA adapters. When set to True, separate cuda graphs will be captured for different counts of active LoRAs (powers of 2 up to max_loras), which can improve performance for variable LoRA usage patterns at the cost of increased startup time and memory usage. Only takes effect when cudagraph_specialize_lora is True.

###

`target_modules = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.LoRAConfig.target_modules)

Restrict LoRA to specific module suffixes (e.g., ["o_proj", "qkv_proj"]). If None, all supported LoRA modules are used. This allows deployment-time control over which modules have LoRA applied, useful for performance tuning.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.LoRAConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

## Source code in `vllm/config/lora.py`


##

`LoadConfig`

[¶](https://docs.vllm.ai#vllm.config.LoadConfig)

Configuration for loading the model weights.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.LoadConfig.compute_hash)WARNING: Whenever a new field is added to this config,


Attributes:

-
([device](https://docs.vllm.ai#vllm.config.LoadConfig.device)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneDevice to which model weights will be loaded, default to

-
([download_dir](https://docs.vllm.ai#vllm.config.LoadConfig.download_dir)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneDirectory to download and load the weights, default to the default

-
([ignore_patterns](https://docs.vllm.ai#vllm.config.LoadConfig.ignore_patterns)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] |[str](https://docs.python.org/3/builtins/stdtypes.html#str)The list of patterns to ignore when loading the model. Default to

-
([load_format](https://docs.vllm.ai#vllm.config.LoadConfig.load_format)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| LoadFormatsThe format of the model weights to load.

-
([model_loader_extra_config](https://docs.vllm.ai#vllm.config.LoadConfig.model_loader_extra_config)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)|[TensorizerConfig](https://docs.vllm.ai/model_executor/model_loader/tensorizer/#vllm.model_executor.model_loader.tensorizer.TensorizerConfig)Extra config for model loader. This will be passed to the model loader

-
([pt_load_map_location](https://docs.vllm.ai#vllm.config.LoadConfig.pt_load_map_location)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)|[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The map location for loading pytorch checkpoint, to support loading

-
([safetensors_load_strategy](https://docs.vllm.ai#vllm.config.LoadConfig.safetensors_load_strategy)`SafetensorsLoadStrategy | None`

) –Specifies the loading strategy for safetensors weights.

-
([safetensors_prefetch_block_size](https://docs.vllm.ai#vllm.config.LoadConfig.safetensors_prefetch_block_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Read size in bytes for each safetensors checkpoint file prefetch.

-
([safetensors_prefetch_num_threads](https://docs.vllm.ai#vllm.config.LoadConfig.safetensors_prefetch_num_threads)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of worker threads used to prefetch safetensors checkpoint files

-
([use_tqdm_on_load](https://docs.vllm.ai#vllm.config.LoadConfig.use_tqdm_on_load)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to enable tqdm for showing progress bar when loading model


## Source code in `vllm/config/load.py`


|
|

###

`device = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.LoadConfig.device)

Device to which model weights will be loaded, default to device_config.device

###

`download_dir = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.LoadConfig.download_dir)

Directory to download and load the weights, default to the default cache directory of Hugging Face.

###

`ignore_patterns = Field(default_factory=(lambda: ['original/**/*']))`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.LoadConfig.ignore_patterns)

The list of patterns to ignore when loading the model. Default to "original/**/*" to avoid repeated loading of llama's checkpoints.

###

`load_format = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.LoadConfig.load_format)

The format of the model weights to load.

- "auto" will try to load the weights in the safetensors format and fall back to the pytorch bin format if safetensors format is not available.
- "pt" will load the weights in the pytorch bin format.
- "safetensors" will load the weights in the safetensors format.
- "instanttensor" will load the Safetensors weights on CUDA devices using InstantTensor, which enables distributed loading with pipelined prefetching and fast direct I/O.
- "ipc_cache" will map post-quantized weights from a local weight cache daemon via CUDA IPC for fast engine restarts. See
`vllm/model_executor/model_loader/weight_cache/daemon.py`

for how to launch the daemon. - "npcache" will load the weights in pytorch format and store a numpy cache to speed up the loading.
- "dummy" will initialize the weights with random values, which is mainly for profiling.
- "tensorizer" will use CoreWeave's tensorizer library for fast weight loading. See the Tensorize vLLM Model script in the Examples section for more information.
- "runai_streamer" will load the Safetensors weights using Run:ai Model Streamer.
- "runai_streamer_sharded" will load weights from pre-sharded checkpoint files using Run:ai Model Streamer.
- "sharded_state" will load weights from pre-sharded checkpoint files, supporting efficient loading of tensor-parallel models.
- "mistral" will load weights from consolidated safetensors files used by Mistral models.
- "modelexpress" will load weights using ModelExpress.
- Other custom values can be supported via plugins.

###

`model_loader_extra_config = Field(default_factory=dict)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.LoadConfig.model_loader_extra_config)

Extra config for model loader. This will be passed to the model loader corresponding to the chosen load_format.

###

`pt_load_map_location = 'cpu'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.LoadConfig.pt_load_map_location)

The map location for loading pytorch checkpoint, to support loading checkpoints can only be loaded on certain devices like "cuda", this is equivalent to `{"": "cuda"}`

. Another supported format is mapping from different devices like from GPU 1 to GPU 0: `{"cuda:1": "cuda:0"}`

. Note that when passed from command line, the strings in dictionary need to be double quoted for json parsing. For more details, see the original doc for `map_location`

parameter in [ torch.load](https://pytorch.org/docs/stable/generated/torch.load.html#torch.load) parameter.

###

`safetensors_load_strategy = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.LoadConfig.safetensors_load_strategy)

Specifies the loading strategy for safetensors weights.

- None (default): Uses memory-mapped (lazy) loading. When an NFS filesystem is detected and the total checkpoint size fits within 90%% of available RAM, prefetching is enabled automatically.
- "lazy": Weights are memory-mapped from the file. This enables on-demand loading and is highly efficient for models on local storage. Unlike the default (None), auto-prefetch on NFS is not performed.
- "eager": The entire file is read into CPU memory upfront before loading. This is recommended for models on network filesystems (e.g., Lustre, NFS) as it avoids inefficient random reads, significantly speeding up model initialization. However, it uses more CPU RAM.
- "prefetch": Checkpoint files are read into the OS page cache before workers load them, speeding up the model loading phase. Useful on network or high-latency storage.
- "torchao": Weights are loaded in upfront and then reconstructed into torchao tensor subclasses. This is used when the checkpoint was quantized using torchao and saved using safetensors. Needs
`torchao >= 0.14.0`

.

###

`safetensors_prefetch_block_size = Field(default=DEFAULT_SAFETENSORS_PREFETCH_BLOCK_SIZE, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.LoadConfig.safetensors_prefetch_block_size)

Read size in bytes for each safetensors checkpoint file prefetch.

###

`safetensors_prefetch_num_threads = Field(default=DEFAULT_SAFETENSORS_PREFETCH_NUM_THREADS, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.LoadConfig.safetensors_prefetch_num_threads)

Number of worker threads used to prefetch safetensors checkpoint files into the OS page cache when safetensors prefetching is enabled.

###

`use_tqdm_on_load = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.LoadConfig.use_tqdm_on_load)

Whether to enable tqdm for showing progress bar when loading model weights.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.LoadConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

## Source code in `vllm/config/load.py`


##

`MambaConfig`

[¶](https://docs.vllm.ai#vllm.config.MambaConfig)

Configuration for Mamba SSM backends.

Methods:

-
–[validate_backend_before](https://docs.vllm.ai#vllm.config.MambaConfig.validate_backend_before)Enable parsing of the

`backend`

enum type from string.

Attributes:

-
([backend](https://docs.vllm.ai#vllm.config.MambaConfig.backend)

) –[MambaBackendEnum](https://docs.vllm.ai/mamba/#vllm.config.mamba.MambaBackendEnum)Mamba SSU backend to use.

-
([enable_stochastic_rounding](https://docs.vllm.ai#vllm.config.MambaConfig.enable_stochastic_rounding)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable stochastic rounding when writing SSM state to fp16 cache.

-
([ssu_algorithm](https://docs.vllm.ai#vllm.config.MambaConfig.ssu_algorithm)`MambaSSUAlgorithm | None`

) –Selective state update algorithm to use with the FlashInfer backend.

-
([stochastic_rounding_philox_rounds](https://docs.vllm.ai#vllm.config.MambaConfig.stochastic_rounding_philox_rounds)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of Philox PRNG rounds for stochastic rounding random number


## Source code in `vllm/config/mamba.py`


###

`backend = MambaBackendEnum.TRITON`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MambaConfig.backend)

Mamba SSU backend to use.

###

`enable_stochastic_rounding = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MambaConfig.enable_stochastic_rounding)

Enable stochastic rounding when writing SSM state to fp16 cache. Uses random bits to unbias the rounding error, which can improve numerical stability for long sequences.

###

`ssu_algorithm = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MambaConfig.ssu_algorithm)

Selective state update algorithm to use with the FlashInfer backend. None defaults to FlashInfer's "auto" algorithm. Forced algorithms must be supported by FlashInfer for the active GPU, state dtype, and decoding mode.

###

`stochastic_rounding_philox_rounds = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MambaConfig.stochastic_rounding_philox_rounds)

Number of Philox PRNG rounds for stochastic rounding random number generation. 0 uses the Triton default. Higher values improve randomness quality at the cost of compute.

###

`validate_backend_before(value)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.MambaConfig.validate_backend_before)

Enable parsing of the `backend`

enum type from string.

## Source code in `vllm/config/mamba.py`


##

`ModelConfig`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig)

Configuration for the model.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.ModelConfig.compute_hash)WARNING: Whenever a new field is added to this config,

-
–[get_diff_sampling_param](https://docs.vllm.ai#vllm.config.ModelConfig.get_diff_sampling_param)This method returns a dictionary containing the non-default sampling

-
–[get_mamba_chunk_size](https://docs.vllm.ai#vllm.config.ModelConfig.get_mamba_chunk_size)Returns the mamba chunk size if it exists.

-
–[get_multimodal_config](https://docs.vllm.ai#vllm.config.ModelConfig.get_multimodal_config)Get the multimodal configuration of the model.

-
–[get_num_attention_heads](https://docs.vllm.ai#vllm.config.ModelConfig.get_num_attention_heads)Returns the number of attention heads per GPU.

-
–[get_num_kv_heads](https://docs.vllm.ai#vllm.config.ModelConfig.get_num_kv_heads)Returns the number of KV heads per GPU.

-
–[get_sliding_window](https://docs.vllm.ai#vllm.config.ModelConfig.get_sliding_window)Get the sliding window size from the HF text config if present.

-
–[get_total_num_kv_heads](https://docs.vllm.ai#vllm.config.ModelConfig.get_total_num_kv_heads)Returns the total number of KV heads.

-
–[maybe_pull_model_tokenizer_for_runai](https://docs.vllm.ai#vllm.config.ModelConfig.maybe_pull_model_tokenizer_for_runai)Pull model/tokenizer from Object Storage to temporary

-
–[maybe_untie_word_embeddings](https://docs.vllm.ai#vllm.config.ModelConfig.maybe_untie_word_embeddings)Stop trusting

`tie_word_embeddings`

when the checkpoint disagrees. -
–[try_get_generation_config](https://docs.vllm.ai#vllm.config.ModelConfig.try_get_generation_config)This method attempts to retrieve the non-default values of the

-
–[using_transformers_backend](https://docs.vllm.ai#vllm.config.ModelConfig.using_transformers_backend)Check if the model is using the Transformers modeling backend class.

-
–[validate_model_config_after](https://docs.vllm.ai#vllm.config.ModelConfig.validate_model_config_after)Called after

**post_init**.

Attributes:

-
([allow_deprecated_quantization](https://docs.vllm.ai#vllm.config.ModelConfig.allow_deprecated_quantization)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to allow deprecated quantization methods.

-
([allowed_local_media_path](https://docs.vllm.ai#vllm.config.ModelConfig.allowed_local_media_path)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Allowing API requests to read local images or videos from directories

-
([allowed_media_domains](https://docs.vllm.ai#vllm.config.ModelConfig.allowed_media_domains)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | NoneIf set, only media URLs that belong to this domain can be used for

-
([architecture](https://docs.vllm.ai#vllm.config.ModelConfig.architecture)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The architecture vllm actually used.

-
([attn_type](https://docs.vllm.ai#vllm.config.ModelConfig.attn_type)`AttnTypeStr`

) –Determine the attention type based on model configuration.

-
([code_revision](https://docs.vllm.ai#vllm.config.ModelConfig.code_revision)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe specific revision to use for the model code on the Hugging Face Hub.

-
([config_format](https://docs.vllm.ai#vllm.config.ModelConfig.config_format)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| ConfigFormatThe format of the model config to load:

-
([convert](https://docs.vllm.ai#vllm.config.ModelConfig.convert)`ConvertOption`

) –Convert the model using adapters defined in

-
([disable_cascade_attn](https://docs.vllm.ai#vllm.config.ModelConfig.disable_cascade_attn)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Disable cascade attention for V1. While cascade attention does not

-
([disable_sliding_window](https://docs.vllm.ai#vllm.config.ModelConfig.disable_sliding_window)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to disable sliding window. If True, we will disable the sliding

-
([dtype](https://docs.vllm.ai#vllm.config.ModelConfig.dtype)`ModelDType |`

) –[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)Data type for model weights and activations:

-
([enable_cumem_allocator](https://docs.vllm.ai#vllm.config.ModelConfig.enable_cumem_allocator)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable the custom cumem allocator to leverage advanced GPU memory

-
([enable_nccl_comm_suspend](https://docs.vllm.ai#vllm.config.ModelConfig.enable_nccl_comm_suspend)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable releasing NCCL communicator memory during sleep mode

-
([enable_prompt_embeds](https://docs.vllm.ai#vllm.config.ModelConfig.enable_prompt_embeds)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, enables passing text embeddings as inputs via the -
([enable_sleep_mode](https://docs.vllm.ai#vllm.config.ModelConfig.enable_sleep_mode)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable sleep mode for the engine (only cuda and

-
([enable_trace_replay](https://docs.vllm.ai#vllm.config.ModelConfig.enable_trace_replay)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to allow requests to set

-
([enforce_eager](https://docs.vllm.ai#vllm.config.ModelConfig.enforce_eager)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to always use eager-mode PyTorch. If True, we will disable CUDA

-
([generation_config](https://docs.vllm.ai#vllm.config.ModelConfig.generation_config)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The folder path to the generation config. Defaults to

`"auto"`

, the -
([head_dtype](https://docs.vllm.ai#vllm.config.ModelConfig.head_dtype)

) –[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)The "head" refers to the last Linear layer(s) of an LLM,

-
([hf_config](https://docs.vllm.ai#vllm.config.ModelConfig.hf_config)`PretrainedConfig`

) –The Hugging Face config of the model.

-
([hf_config_path](https://docs.vllm.ai#vllm.config.ModelConfig.hf_config_path)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneName or path of the Hugging Face config to use. If unspecified, model

-
([hf_overrides](https://docs.vllm.ai#vllm.config.ModelConfig.hf_overrides)`HfOverrides`

) –If a dictionary, contains arguments to be forwarded to the Hugging Face

-
([hf_text_config](https://docs.vllm.ai#vllm.config.ModelConfig.hf_text_config)`PretrainedConfig`

) –The Hugging Face config of the text model (same as hf_config for text models).

-
([hf_token](https://docs.vllm.ai#vllm.config.ModelConfig.hf_token)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)|[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe token to use as HTTP bearer authorization for remote files . If

-
([io_processor_plugin](https://docs.vllm.ai#vllm.config.ModelConfig.io_processor_plugin)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneIOProcessor plugin name to load at model startup

-
([is_diffusion](https://docs.vllm.ai#vllm.config.ModelConfig.is_diffusion)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Detect discrete diffusion (dLLM) models from HF config.

-
([is_encoder_decoder](https://docs.vllm.ai#vllm.config.ModelConfig.is_encoder_decoder)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Extract the HF encoder/decoder model flag.

-
([is_submodel_config](https://docs.vllm.ai#vllm.config.ModelConfig.is_submodel_config)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether this is a submodule view derived by

`VllmConfig.with_hf_config`

-
([logits_processors](https://docs.vllm.ai#vllm.config.ModelConfig.logits_processors)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)|[type](https://docs.python.org/3/builtins/functions.html#type)[[LogitsProcessor](https://docs.vllm.ai/v1/sample/logits_processor/#vllm.v1.sample.logits_processor.LogitsProcessor)]] | NoneOne or more logits processors' fully-qualified class names or class

-
([logprobs_mode](https://docs.vllm.ai#vllm.config.ModelConfig.logprobs_mode)`LogprobsMode`

) –Indicates the content returned in the logprobs and prompt_logprobs.

-
([max_logprobs](https://docs.vllm.ai#vllm.config.ModelConfig.max_logprobs)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum number of log probabilities to return when

`logprobs`

is -
([max_model_len](https://docs.vllm.ai#vllm.config.ModelConfig.max_model_len)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Model context length (prompt and output). If unspecified, will be

-
([model](https://docs.vllm.ai#vllm.config.ModelConfig.model)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Name or path of the Hugging Face model to use. It is also used as the

-
([model_class_overrides](https://docs.vllm.ai#vllm.config.ModelConfig.model_class_overrides)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Override the model class used for one or more architectures, mapping the

-
([model_impl](https://docs.vllm.ai#vllm.config.ModelConfig.model_impl)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| ModelImplWhich implementation of the model to use:

-
([model_weights](https://docs.vllm.ai#vllm.config.ModelConfig.model_weights)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Original model weights path. Used when the model is pulled from object

-
([multimodal_config](https://docs.vllm.ai#vllm.config.ModelConfig.multimodal_config)

) –[MultiModalConfig](https://docs.vllm.ai/multimodal/#vllm.config.multimodal.MultiModalConfig)| NoneConfiguration for multimodal model. If

`None`

, this will be inferred -
([override_generation_config](https://docs.vllm.ai#vllm.config.ModelConfig.override_generation_config)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)]Overrides or sets generation config. e.g.

`{"temperature": 0.5}`

. If -
([pooler_config](https://docs.vllm.ai#vllm.config.ModelConfig.pooler_config)

) –[PoolerConfig](https://docs.vllm.ai/pooler/#vllm.config.pooler.PoolerConfig)| NonePooler config which controls the behaviour of output pooling in pooling

-
([quantization](https://docs.vllm.ai#vllm.config.ModelConfig.quantization)`QuantizationMethods |`

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneMethod used to quantize the weights. If

`None`

, we first check the -
([quantization_config](https://docs.vllm.ai#vllm.config.ModelConfig.quantization_config)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] |[QuantizationConfigArgs](https://docs.vllm.ai/quantization/#vllm.config.quantization.QuantizationConfigArgs)| NoneUser-facing quantization configuration. Carries per-layer-kind specs

-
([renderer_num_workers](https://docs.vllm.ai#vllm.config.ModelConfig.renderer_num_workers)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of worker threads in the renderer thread pool. The pool is

-
([return_sampling_mask](https://docs.vllm.ai#vllm.config.ModelConfig.return_sampling_mask)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to return the post-processing token support for each sample.

-
([revision](https://docs.vllm.ai#vllm.config.ModelConfig.revision)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe specific model version to use. It can be a branch name, a tag name,

-
([runner](https://docs.vllm.ai#vllm.config.ModelConfig.runner)`RunnerOption`

) –The type of model runner to use. Each vLLM instance only supports one

-
([score_type](https://docs.vllm.ai#vllm.config.ModelConfig.score_type)`ScoreType`

) –Scoring API handles score/rerank for:

-
([seed](https://docs.vllm.ai#vllm.config.ModelConfig.seed)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Random seed for reproducibility.

-
([served_model_name](https://docs.vllm.ai#vllm.config.ModelConfig.served_model_name)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)|[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | NoneThe model name(s) used in the API. If multiple names are provided, the

-
([skip_tokenizer_init](https://docs.vllm.ai#vllm.config.ModelConfig.skip_tokenizer_init)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Skip initialization of tokenizer and detokenizer. Expects valid

-
([sleep_mode_backend](https://docs.vllm.ai#vllm.config.ModelConfig.sleep_mode_backend)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Mechanism used to free and restore GPU state for sleep mode.

`"cumem"`

-
([sleep_preserve_parameter_names](https://docs.vllm.ai#vllm.config.ModelConfig.sleep_preserve_parameter_names)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Parameter-name globs to preserve across level-2 sleep.

-
([spec_target_max_model_len](https://docs.vllm.ai#vllm.config.ModelConfig.spec_target_max_model_len)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneSpecify the maximum length for spec decoding draft models.

-
([tokenizer](https://docs.vllm.ai#vllm.config.ModelConfig.tokenizer)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Name or path of the Hugging Face tokenizer to use. If unspecified, model

-
([tokenizer_mode](https://docs.vllm.ai#vllm.config.ModelConfig.tokenizer_mode)`TokenizerMode |`

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Tokenizer mode:

-
([tokenizer_revision](https://docs.vllm.ai#vllm.config.ModelConfig.tokenizer_revision)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe specific revision to use for the tokenizer on the Hugging Face Hub.

-
([trust_remote_code](https://docs.vllm.ai#vllm.config.ModelConfig.trust_remote_code)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Trust remote code (e.g., from HuggingFace) when downloading the model

-
([use_fp64_gumbel](https://docs.vllm.ai#vllm.config.ModelConfig.use_fp64_gumbel)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to use FP64 (instead of FP32) random noise for Gumbel-max and

-
([word_embeddings_untied_by_checkpoint](https://docs.vllm.ai#vllm.config.ModelConfig.word_embeddings_untied_by_checkpoint)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether

`tie_word_embeddings`

was overridden to`False`

because the checkpoint

## Source code in `vllm/config/model.py`


|
|

###

`allow_deprecated_quantization = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.allow_deprecated_quantization)

Whether to allow deprecated quantization methods.

###

`allowed_local_media_path = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.allowed_local_media_path)

Allowing API requests to read local images or videos from directories specified by the server file system. This is a security risk. Should only be enabled in trusted environments.

###

`allowed_media_domains = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.allowed_media_domains)

If set, only media URLs that belong to this domain can be used for multi-modal inputs.

###

`architecture`

`property`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.architecture)

The architecture vllm actually used.

###

`attn_type`

`property`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.attn_type)

Determine the attention type based on model configuration.

###

`code_revision = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.code_revision)

The specific revision to use for the model code on the Hugging Face Hub. It can be a branch name, a tag name, or a commit id. If unspecified, will use the default version.

###

`config_format = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.config_format)

The format of the model config to load:

- "auto" will try to load the config in hf format if available after trying to load in mistral format.
- "hf" will load the config in hf format.
- "mistral" will load the config in mistral format.

###

`convert = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.convert)

Convert the model using adapters defined in [vllm.model_executor.models.adapters](https://docs.vllm.ai/model_executor/models/adapters/#vllm.model_executor.models.adapters). The most common use case is to adapt a text generation model to be used for pooling tasks.

###

`disable_cascade_attn = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.disable_cascade_attn)

Disable cascade attention for V1. While cascade attention does not change the mathematical correctness, disabling it could be useful for preventing potential numerical issues. This defaults to True, so users must opt in to cascade attention by setting this to False. Even when this is set to False, cascade attention will only be used when the heuristic tells that it's beneficial.

###

`disable_sliding_window = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.disable_sliding_window)

Whether to disable sliding window. If True, we will disable the sliding window functionality of the model, capping to sliding window size. If the model does not support sliding window, this argument is ignored.

###

`dtype = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.dtype)

Data type for model weights and activations:

- "auto" will use FP16 precision for FP32 and FP16 models, and BF16 precision for BF16 models.
- "half" for FP16. Recommended for AWQ quantization.
- "float16" is the same as "half".
- "bfloat16" for a balance between precision and range.
- "float" is shorthand for FP32 precision.
- "float32" for FP32 precision.

###

`enable_cumem_allocator = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.enable_cumem_allocator)

Enable the custom cumem allocator to leverage advanced GPU memory allocation features such as multi-node NVLink support.

Sleep mode automatically enables this allocator. Only cuda and hip platforms are supported.

###

`enable_nccl_comm_suspend = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.enable_nccl_comm_suspend)

Enable releasing NCCL communicator memory during sleep mode (`ncclCommSuspend`

/`ncclCommResume`

). Experimental; when disabled (the default) sleep still releases weights/KV-cache memory as before.

###

`enable_prompt_embeds = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.enable_prompt_embeds)

If `True`

, enables passing text embeddings as inputs via the `prompt_embeds`

key.

WARNING: The vLLM engine may crash if incorrect shape of embeddings is passed. Only enable this flag for trusted users!

###

`enable_sleep_mode = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.enable_sleep_mode)

Enable sleep mode for the engine (only cuda and hip platforms are supported).

###

`enable_trace_replay = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.enable_trace_replay)

Whether to allow requests to set `SamplingParams.trace_decode_token_ids`

, which forces decoding to follow a predetermined token sequence while still computing real logprobs. Reserved for debugging and RL workflows: enabling it reserves a per-request trace buffer, so it is off by default.

###

`enforce_eager = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.enforce_eager)

Whether to always use eager-mode PyTorch. If True, we will disable CUDA graph and always execute the model in eager mode. If False, we will use CUDA graph and eager execution in hybrid for maximal performance and flexibility.

NOTE: This disables both `torch.compile`

and CUDA graphs, and is equivalent to setting `-cc.mode=none -cc.cudagraph_mode=none`

.

###

`generation_config = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.generation_config)

The folder path to the generation config. Defaults to `"auto"`

, the generation config will be loaded from model path. If set to `"vllm"`

, no generation config is loaded, vLLM defaults will be used. If set to a folder path, the generation config will be loaded from the specified folder path. If `max_new_tokens`

is specified in generation config, then it sets a server-wide limit on the number of output tokens for all requests.

###

`head_dtype`

`property`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.head_dtype)

The "head" refers to the last Linear layer(s) of an LLM, such as the lm_head in a generation model, or the score or classifier in a classification model.

- Pooling models default to an fp32 head; use --hf-overrides '{"head_dtype": "model"}' to disable it.
- Generation models default to the model dtype; set --hf-overrides '{"head_dtype": "float32"}' to run the lm_head in fp32, which is required for RL training-inference consistency (the trainer computes logits in fp32).

###

`hf_config = field(init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.hf_config)

The Hugging Face config of the model.

###

`hf_config_path = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.hf_config_path)

Name or path of the Hugging Face config to use. If unspecified, model name or path will be used.

###

`hf_overrides = field(default_factory=dict)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.hf_overrides)

If a dictionary, contains arguments to be forwarded to the Hugging Face config. If a callable, it is called to update the HuggingFace config.

###

`hf_text_config = field(init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.hf_text_config)

The Hugging Face config of the text model (same as hf_config for text models).

###

`hf_token = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.hf_token)

The token to use as HTTP bearer authorization for remote files . If `True`

, will use the token generated when running `hf auth login`

(stored in `~/.cache/huggingface/token`

).

###

`io_processor_plugin = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.io_processor_plugin)

IOProcessor plugin name to load at model startup

###

`is_diffusion`

`cached`

`property`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.is_diffusion)

Detect discrete diffusion (dLLM) models from HF config.

###

`is_encoder_decoder`

`cached`

`property`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.is_encoder_decoder)

Extract the HF encoder/decoder model flag.

###

`is_submodel_config = field(default=False, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.is_submodel_config)

Whether this is a submodule view derived by `VllmConfig.with_hf_config`

(e.g. a multimodal model's text stack). Its architecture list is empty, so deployment-level validation must not run against it.

###

`logits_processors = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.logits_processors)

One or more logits processors' fully-qualified class names or class definitions

###

`logprobs_mode = 'raw_logprobs'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.logprobs_mode)

Indicates the content returned in the logprobs and prompt_logprobs. Supported mode: 1) raw_logprobs, 2) processed_logprobs, 3) raw_logits, 4) processed_logits. Raw means the values before applying any logit processors, like bad words. Processed means the values after applying all processors, including temperature and top_k/top_p. Note: for prompt_logprobs, processed_* and raw_* yield identical results because prompt tokens do not go through sampling processors.

###

`max_logprobs = Field(default=20, ge=(-1))`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.max_logprobs)

Maximum number of log probabilities to return when `logprobs`

is specified in `SamplingParams`

. The default value comes the default for the OpenAI Chat Completions API. -1 means no cap, i.e. all (output_length * vocab_size) logprobs are allowed to be returned and it may cause OOM.

###

`max_model_len = Field(default=None, ge=(-1))`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.max_model_len)

Model context length (prompt and output). If unspecified, will be automatically derived from the model config.

When passing via `--max-model-len`

, supports k/m/g/K/M/G in human-readable format. Examples:

- 1k -> 1000
- 1K -> 1024
- 25.6k -> 25,600
- -1 or 'auto' -> Automatically choose the maximum model length that fits in GPU memory. This will use the model's maximum context length if it fits, otherwise it will find the largest length that can be accommodated.

###

`model = 'Qwen/Qwen3-0.6B'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.model)

Name or path of the Hugging Face model to use. It is also used as the content for `model_name`

tag in metrics output when `served_model_name`

is not specified.

###

`model_class_overrides = field(default_factory=dict)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.model_class_overrides)

Override the model class used for one or more architectures, mapping the architecture name to a `"module:class"`

target (the same format accepted by `ModelRegistry.register_model`

). This registers the target class at runtime, e.g. `{"GlmMoeDsaForCausalLM": "vllm.models.deepseek_v32.nvidia.model:DeepseekV32ForCausalLM"}`

. This argument is for development and debugging purposes only.

###

`model_impl = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.model_impl)

Which implementation of the model to use:

- "auto" will try to use the vLLM implementation, if it exists, and fall back to the Transformers implementation if no vLLM implementation is available.
- "vllm" will use the vLLM model implementation.
- "transformers" will use the Transformers model implementation.
- "terratorch" will use the TerraTorch model implementation.

###

`model_weights = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.model_weights)

Original model weights path. Used when the model is pulled from object storage (e.g., RunAI) to preserve the original URI while `model`

points to the local directory.

###

`multimodal_config = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.multimodal_config)

Configuration for multimodal model. If `None`

, this will be inferred from the architecture of `self.model`

.

###

`override_generation_config = field(default_factory=dict)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.override_generation_config)

Overrides or sets generation config. e.g. `{"temperature": 0.5}`

. If used with `--generation-config auto`

, the override parameters will be merged with the default config from the model. If used with `--generation-config vllm`

, only the override parameters are used.

###

`pooler_config = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.pooler_config)

Pooler config which controls the behaviour of output pooling in pooling models.

###

`quantization = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.quantization)

Method used to quantize the weights. If `None`

, we first check the `quantization_config`

attribute in the model config file. If that is `None`

, we assume the model weights are not quantized and use `dtype`

to determine the data type of the weights.

###

`quantization_config = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.quantization_config)

User-facing quantization configuration. Carries per-layer-kind specs (linear, moe) and ignore patterns; see :class:`QuantizationConfigArgs`

. Auto-populated from the matching online shorthand when `quantization`

is one of the values in `ONLINE_QUANT_SHORTHAND_NAMES`

.

###

`renderer_num_workers = 1`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.renderer_num_workers)

Number of worker threads in the renderer thread pool. The pool is consumed by the async renderer path (e.g. the OpenAI-compatible API server started by `vllm serve`

) to parallelize tokenization, chat template rendering, and multimodal preprocessing across concurrent requests.

The offline `LLM`

entrypoint uses the synchronous renderer path and processes prompts (including multimodal preprocessing) serially, so this setting has no effect there.

###

`return_sampling_mask = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.return_sampling_mask)

Whether to return the post-processing token support for each sample.

###

`revision = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.revision)

The specific model version to use. It can be a branch name, a tag name, or a commit id. If unspecified, will use the default version.

###

`runner = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.runner)

The type of model runner to use. Each vLLM instance only supports one model runner, even if the same model can be used for multiple types.

###

`score_type`

`property`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.score_type)

Scoring API handles score/rerank for:

- "classify" task (score_type: cross-encoder models)
- "embed" task (score_type: bi-encoder models)
- "token_embed" task (score_type: late interaction models)

###

`seed = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.seed)

Random seed for reproducibility.

We must set the global seed because otherwise, different tensor parallel workers would sample different tokens, leading to inconsistent results.

###

`served_model_name = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.served_model_name)

The model name(s) used in the API. If multiple names are provided, the server will respond to any of the provided names. The model name in the model field of a response will be the first name in this list. If not specified, the model name will be the same as the `--model`

argument. Noted that this name(s) will also be used in `model_name`

tag content of prometheus metrics, if multiple names provided, metrics tag will take the first one.

###

`skip_tokenizer_init = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.skip_tokenizer_init)

Skip initialization of tokenizer and detokenizer. Expects valid `prompt_token_ids`

and `None`

for prompt from the input. The generated output will contain token ids.

###

`sleep_mode_backend = 'cumem'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.sleep_mode_backend)

Mechanism used to free and restore GPU state for sleep mode. `"cumem"`

(default) uses the built-in `CuMemAllocator`

and is behavior-compatible with prior releases. Additional backends (CUDA checkpoint, CRIU, durable snapshot) may be registered in-tree or by plugins (RFC #34303).

###

`sleep_preserve_parameter_names = field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.sleep_preserve_parameter_names)

Parameter-name globs to preserve across level-2 sleep. The sender must omit these parameters; loaders must preserve their storage.

###

`spec_target_max_model_len = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.spec_target_max_model_len)

Specify the maximum length for spec decoding draft models.

###

`tokenizer = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.tokenizer)

Name or path of the Hugging Face tokenizer to use. If unspecified, model name or path will be used.

###

`tokenizer_mode = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.tokenizer_mode)

Tokenizer mode:

- "auto" will use the tokenizer from
`mistral_common`

for Mistral models if available, otherwise it will use the "hf" tokenizer. - "hf" will use the fast tokenizer if available.
- "slow" will always use the slow tokenizer.
- "mistral" will always use the tokenizer from
`mistral_common`

. - "deepseek_v32" will always use the tokenizer from
`deepseek_v32`

. - "deepseek_v4" will always use the tokenizer from
`deepseek_v4`

. - "deepseek_v41" will use the DeepSeek V4.1 prompt encoder.
- "kimi_k3" will always use the "hf" tokenizer but render chat prompts with Kimi K3's Python XTML encoding instead of a Jinja template.
- "cohere" uses the standard HF tokenizer but renders the chat template via the
`cohere_melody`

library (cmd3 / cmd4 templates) instead of Jinja, and surfaces grounded-citation metadata on responses. - Other custom values can be supported via plugins.

To swap the Rust BPE backend that powers HF fast tokenizers for the [fastokens](https://github.com/crusoecloud/fastokens) implementation, set `VLLM_USE_FASTOKENS=1`

instead — that override applies to any mode that loads an HF fast tokenizer (`hf`

, `deepseek_v32`

, `deepseek_v4`

, …).

###

`tokenizer_revision = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.tokenizer_revision)

The specific revision to use for the tokenizer on the Hugging Face Hub. It can be a branch name, a tag name, or a commit id. If unspecified, will use the default version.

###

`trust_remote_code = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.trust_remote_code)

Trust remote code (e.g., from HuggingFace) when downloading the model and tokenizer.

###

`use_fp64_gumbel = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.use_fp64_gumbel)

Whether to use FP64 (instead of FP32) random noise for Gumbel-max and equivalent exponential-race sampling. FP64 preserves lower-tail sampling events that fp32 uniform/exponential draws can truncate, at the cost of significantly lower throughput on most GPUs.

###

`word_embeddings_untied_by_checkpoint = field(default=False, init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.word_embeddings_untied_by_checkpoint)

Whether `tie_word_embeddings`

was overridden to `False`

because the checkpoint contains an `lm_head`

of its own. The two may still turn out to be identical, in which case they are re-tied once the weights have been loaded.

###

`_apply_dict_overrides(config, overrides)`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig._apply_dict_overrides)

Apply dict overrides, handling both nested configs and dict values.

## Source code in `vllm/config/model.py`


###

`_get_transformers_backend_cls()`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig._get_transformers_backend_cls)

Determine which Transformers modeling backend class will be used if `model_impl`

is set to `transformers`

or `auto`

.

## Source code in `vllm/config/model.py`


###

`_skip_none_validation(value, handler)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig._skip_none_validation)

Skip validation if the value is `None`

when initialisation is delayed.

## Source code in `vllm/config/model.py`


###

`_supports_multimodal_for_mm_prefix()`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig._supports_multimodal_for_mm_prefix)

Whether multimodal inputs can still appear for this deployment.

This runs more than once per config: once early in `__post_init__`

(before `multimodal_config`

exists), again after it is created, and then for every `get_model_arch_config`

regeneration -- notably `with_hf_config`

, which deep-copies this `ModelConfig`

and swaps `hf_config`

for a text-only submodule (e.g. `Gemma4ForCausalLM`

).

The result is cached for correctness, not just to save work: on the `with_hf_config`

copy the submodule architecture has no registered multimodal processor, so re-querying the registry would raise and be treated as text-only, wrongly clearing `is_mm_prefix_lm`

even when a vision modality is still enabled (e.g. `image=0`

but video allowed). The deep-copied cache preserves the top-level decision instead.

## Source code in `vllm/config/model.py`


###

`_supports_multimodal_inputs()`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig._supports_multimodal_inputs)

Checks if the model supports multimodal inputs. Returns True if the model is multimodal with any non-zero supported modalities, otherwise returns False, effectively running in text-only mode.

## Source code in `vllm/config/model.py`


###

`_update_nested(target, updates)`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig._update_nested)

Recursively updates a config or dict with nested updates.

## Source code in `vllm/config/model.py`


###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

## Source code in `vllm/config/model.py`


###

`get_diff_sampling_param()`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.get_diff_sampling_param)

This method returns a dictionary containing the non-default sampling parameters with `override_generation_config`

applied.

The default sampling parameters are:

- vLLM's neutral defaults if
`self.generation_config="vllm"`

- the model's defaults if
`self.generation_config="auto"`

- as defined in
`generation_config.json`

if`self.generation_config="path/to/generation_config/dir"`


Returns:

## Source code in `vllm/config/model.py`


###

`get_mamba_chunk_size()`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.get_mamba_chunk_size)

Returns the mamba chunk size if it exists.

## Source code in `vllm/config/model.py`


###

`get_multimodal_config()`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.get_multimodal_config)

Get the multimodal configuration of the model.

Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)If the model is not multimodal.


## Source code in `vllm/config/model.py`


###

`get_num_attention_heads(parallel_config, arch_config=None)`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.get_num_attention_heads)

Returns the number of attention heads per GPU.

Pass `arch_config`

(from `model_arch_config[layer_idx]`

) to size a single layer of a heterogeneous model rather than the model as a whole.

## Source code in `vllm/config/model.py`


###

`get_num_kv_heads(parallel_config, arch_config=None)`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.get_num_kv_heads)

Returns the number of KV heads per GPU.

Pass `arch_config`

(from `model_arch_config[layer_idx]`

) to size a single layer of a heterogeneous model rather than the model as a whole.

## Source code in `vllm/config/model.py`


###

`get_sliding_window()`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.get_sliding_window)

###

`get_total_num_kv_heads()`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.get_total_num_kv_heads)

###

`maybe_pull_model_tokenizer_for_runai(model, tokenizer)`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.maybe_pull_model_tokenizer_for_runai)

Pull model/tokenizer from Object Storage to temporary directory when needed.

Parameters:

## Source code in `vllm/config/model.py`


###

`maybe_untie_word_embeddings()`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.maybe_untie_word_embeddings)

Stop trusting `tie_word_embeddings`

when the checkpoint disagrees.

A config may claim the word embeddings are tied while the checkpoint ships an `lm_head`

of its own. Tying regardless would silently discard that tensor, so build the `lm_head`

as if untied and let it load. The two are compared once loaded, and re-tied if they turn out to match, by [maybe_retie_word_embeddings](https://docs.vllm.ai/model_executor/model_loader/weight_tying/#vllm.model_executor.model_loader.weight_tying.maybe_retie_word_embeddings).

Transformers makes the same decision in `PreTrainedModel.tie_weights`

, where it can compare the two tensors directly.

## Source code in `vllm/config/model.py`


###

`try_get_generation_config()`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.try_get_generation_config)

This method attempts to retrieve the non-default values of the generation config for this model.

The generation config can contain information about special tokens, as well as sampling parameters. Which is why this method exists separately to `get_diff_sampling_param`

.

Returns:

## Source code in `vllm/config/model.py`


###

`using_transformers_backend()`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.using_transformers_backend)

Check if the model is using the Transformers modeling backend class.

## Source code in `vllm/config/model.py`


###

`validate_model_config_after()`

[¶](https://docs.vllm.ai#vllm.config.ModelConfig.validate_model_config_after)

Called after **post_init**.

## Source code in `vllm/config/model.py`


##

`MultiModalConfig`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig)

Controls the behavior of multimodal models.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.MultiModalConfig.compute_hash)WARNING: Whenever a new field is added to this config,

-
–[fold_mm_processor_device](https://docs.vllm.ai#vllm.config.MultiModalConfig.fold_mm_processor_device)Fold the

`mm_processor_device`

convenience flag into the kwargs. -
–[get_limit_per_prompt](https://docs.vllm.ai#vllm.config.MultiModalConfig.get_limit_per_prompt)Get the maximum number of input items allowed per prompt

-
–[get_mm_processor_device_type](https://docs.vllm.ai#vllm.config.MultiModalConfig.get_mm_processor_device_type)The torch device type

`mm_processor_kwargs["device"]`

names. -
–[get_video_pruning_spec](https://docs.vllm.ai#vllm.config.MultiModalConfig.get_video_pruning_spec)Return

`(method, rate)`

when video pruning is enabled, else None. -
–[merge_mm_processor_kwargs](https://docs.vllm.ai#vllm.config.MultiModalConfig.merge_mm_processor_kwargs)Get the keyword arguments to pass to the multi-modal processor

-
–[use_gpu_video_backend](https://docs.vllm.ai#vllm.config.MultiModalConfig.use_gpu_video_backend)Return whether the configured video loader or codec uses the GPU.

-
–[validate_mm_processor_device](https://docs.vllm.ai#vllm.config.MultiModalConfig.validate_mm_processor_device)Check

`mm_processor_kwargs["device"]`

for this deployment.

Attributes:

-
([allow_missing_mm_embeddings](https://docs.vllm.ai#vllm.config.MultiModalConfig.allow_missing_mm_embeddings)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether a pre-computed-embedding input may omit the

`*_embeds`

tensor. -
([enable_mm_embeds](https://docs.vllm.ai#vllm.config.MultiModalConfig.enable_mm_embeds)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, enables passing multimodal embeddings: -
([interleave_mm_strings](https://docs.vllm.ai#vllm.config.MultiModalConfig.interleave_mm_strings)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable fully interleaved support for multimodal prompts, while using

-
([language_model_only](https://docs.vllm.ai#vllm.config.MultiModalConfig.language_model_only)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If True, disables all multimodal inputs by setting all modality limits to 0.

-
([limit_per_prompt](https://docs.vllm.ai#vllm.config.MultiModalConfig.limit_per_prompt)

) –[MultiModalDummyOptions](https://docs.vllm.ai/multimodal/#vllm.config.multimodal.MultiModalDummyOptions)The maximum number of input items and options allowed per

-
([media_io_kwargs](https://docs.vllm.ai#vllm.config.MultiModalConfig.media_io_kwargs)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)]]Additional args passed to process media inputs, keyed by modalities.

-
([mm_device_do_normalize](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_device_do_normalize)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneMove the do_normalize computation in the mm preprocessing to before the ViT,

-
([mm_encoder_attn_backend](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_encoder_attn_backend)

) –[AttentionBackendEnum](https://docs.vllm.ai/v1/attention/backends/registry/#vllm.v1.attention.backends.registry.AttentionBackendEnum)| NoneOptional override for the multi-modal encoder attention backend when

-
([mm_encoder_attn_dtype](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_encoder_attn_dtype)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['fp8'] | NoneOptional dtype override for ViT encoder attention. Set to

`"fp8"`

to -
([mm_encoder_fp8_scale_path](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_encoder_fp8_scale_path)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NonePath to a JSON file containing per-layer FP8 Q/K/V scales for ViT

-
([mm_encoder_fp8_scale_save_margin](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_encoder_fp8_scale_save_margin)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Safety margin multiplied onto scales when auto-saving. A value > 1

-
([mm_encoder_fp8_scale_save_path](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_encoder_fp8_scale_save_path)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneWhen set with dynamic FP8 scaling (

`mm_encoder_attn_dtype="fp8"`

-
([mm_encoder_only](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_encoder_only)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)When enabled, skips the language component of the model.

-
([mm_encoder_tp_mode](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_encoder_tp_mode)`MMEncoderTPMode`

) –Indicates how to optimize multi-modal encoder inference using tensor

-
([mm_hasher_algorithm](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_hasher_algorithm)`MMHasherAlgorithm`

) –Hash algorithm to use for multi-modal input caching. Use

`"sha256"`

or -
([mm_ipc_gpu_memory_gb](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_ipc_gpu_memory_gb)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Amount of GPU memory (in GiB) sequestered on the engine's device for

-
([mm_processor_cache_gb](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_processor_cache_gb)

) –[float](https://docs.python.org/3/builtins/functions.html#float)The size (in GiB) of the multi-modal processor cache, which is used to

-
([mm_processor_cache_type](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_processor_cache_type)`MMCacheType`

) –Type of cache to use for the multi-modal preprocessor/mapper. If

`shm`

, -
([mm_processor_kwargs](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_processor_kwargs)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[object](https://docs.python.org/3/builtins/functions.html#object)] | NoneArguments to be forwarded to the model's processor for multi-modal data,

-
([mm_shm_cache_max_object_size_mb](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_shm_cache_max_object_size_mb)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Size limit (in MiB) for each object stored in the multi-modal processor

-
([mm_tensor_ipc](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_tensor_ipc)`MMTensorIPC`

) –IPC (inter-process communication) method for multimodal tensors.

-
([skip_mm_profiling](https://docs.vllm.ai#vllm.config.MultiModalConfig.skip_mm_profiling)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)When enabled, skips multimodal memory profiling and only profiles with

-
([video_pruning_method](https://docs.vllm.ai#vllm.config.MultiModalConfig.video_pruning_method)`VideoPruningMethod`

) –Video token pruning algorithm applied when

`video_pruning_rate`

> 0: -
([video_pruning_rate](https://docs.vllm.ai#vllm.config.MultiModalConfig.video_pruning_rate)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NoneFraction of video tokens to prune from each video. Value sits in range


## Source code in `vllm/config/multimodal.py`


|
|

###

`allow_missing_mm_embeddings = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.allow_missing_mm_embeddings)

Whether a pre-computed-embedding input may omit the `*_embeds`

tensor.

In an encode/prefill/decode (EPD) deployment the encoder instance publishes embeddings through the EC connector. An EC consumer loads those embeddings from the connector, while a KV consumer receives the resulting prompt KV cache. Their requests only need the grid/size metadata that sizes the placeholder range.

Derived, not user-settable: `VllmConfig.__post_init__`

sets this to True on EC and KV consumers. Everywhere else it stays False so that a request which forgets its embeddings still fails fast in the frontend, with a clear error, rather than deep inside the model.

###

`enable_mm_embeds = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.enable_mm_embeds)

If `True`

, enables passing multimodal embeddings: for `LLM`

class, this refers to tensor inputs under `multi_modal_data`

; for the OpenAI-compatible server, this refers to chat messages with content `"type": "*_embeds"`

.

When enabled with `--limit-mm-per-prompt`

set to 0 for a modality, precomputed embeddings skip count validation for that modality, saving memory by not loading encoder modules while still enabling embeddings as an input. Limits greater than 0 still apply to embeddings.

WARNING: The vLLM engine may crash if incorrect shape of embeddings is passed. Only enable this flag for trusted users!

###

`interleave_mm_strings = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.interleave_mm_strings)

Enable fully interleaved support for multimodal prompts, while using --chat-template-content-format=string.

###

`language_model_only = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.language_model_only)

If True, disables all multimodal inputs by setting all modality limits to 0. Equivalent to setting `--limit-mm-per-prompt`

to 0 for every modality.

###

`limit_per_prompt = Field(default_factory=MultiModalDummyOptions)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.limit_per_prompt)

The maximum number of input items and options allowed per prompt for each modality.

Defaults to 999 for each modality.

Legacy format (count only):

Configurable format (with options): {"video": {"count": 1, "num_frames": 32, "width": 512, "height": 512}, "image": {"count": 5, "width": 512, "height": 512}}

Mixed format (combining both): {"image": 16, "video": {"count": 1, "num_frames": 32, "width": 512, "height": 512}}

###

`media_io_kwargs = Field(default_factory=dict)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.media_io_kwargs)

Additional args passed to process media inputs, keyed by modalities. For example, to set num_frames for video, set `--media-io-kwargs '{"video": {"num_frames": 40} }'`


###

`mm_device_do_normalize = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_device_do_normalize)

Move the do_normalize computation in the mm preprocessing to before the ViT, and let the device do it, so that CPU computation can be saved.

###

`mm_encoder_attn_backend = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_encoder_attn_backend)

Optional override for the multi-modal encoder attention backend when using vision transformers. Accepts any value from `vllm.v1.attention.backends.registry.AttentionBackendEnum`

(e.g. `FLASH_ATTN`

).

###

`mm_encoder_attn_dtype = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_encoder_attn_dtype)

Optional dtype override for ViT encoder attention. Set to `"fp8"`

to enable FP8 quantization via the FlashInfer cuDNN backend. When set to `"fp8"`

without a scale file, dynamic scaling is used automatically. See docs/features/quantization/fp8_vit_attn.md for details.

###

`mm_encoder_fp8_scale_path = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_encoder_fp8_scale_path)

Path to a JSON file containing per-layer FP8 Q/K/V scales for ViT encoder attention. When provided (with `mm_encoder_attn_dtype="fp8"`

), static scaling is used. When omitted, dynamic scaling is used.

###

`mm_encoder_fp8_scale_save_margin = Field(default=1.5, gt=0.0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_encoder_fp8_scale_save_margin)

Safety margin multiplied onto scales when auto-saving. A value > 1 leaves headroom so that inputs with larger activations than the calibration set do not overflow FP8 range. Default 1.5.

###

`mm_encoder_fp8_scale_save_path = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_encoder_fp8_scale_save_path)

When set with dynamic FP8 scaling (`mm_encoder_attn_dtype="fp8"`

and no `mm_encoder_fp8_scale_path`

), saves the calibrated scales to this file after the amax history buffer is full. The saved file can then be used as `mm_encoder_fp8_scale_path`

in subsequent runs.

###

`mm_encoder_only = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_encoder_only)

When enabled, skips the language component of the model.

This is usually only valid in disaggregated Encoder process.

###

`mm_encoder_tp_mode = 'weights'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_encoder_tp_mode)

Indicates how to optimize multi-modal encoder inference using tensor parallelism (TP).

`"weights"`

: Within the same vLLM engine, split the weights of each layer across TP ranks. (default TP behavior)`"data"`

: Within the same vLLM engine, split the batched input data across TP ranks to process the data in parallel, while hosting the full weights on each TP rank. This batch-level DP is not to be confused with API request-level DP (which is controlled by`--data-parallel-size`

). This is only supported on a per-model basis and falls back to`"weights"`

if the encoder does not support DP.

###

`mm_hasher_algorithm = 'blake3'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_hasher_algorithm)

Hash algorithm to use for multi-modal input caching. Use `"sha256"`

or `"sha512"`

for FIPS-compliant deployments.

###

`mm_ipc_gpu_memory_gb = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_ipc_gpu_memory_gb)

Amount of GPU memory (in GiB) sequestered on the engine's device for GPU-side multimodal work in the API-server (frontend) process, such as hardware video decoding.

This budget is carved out of the engine's KV-cache memory so the headroom physically exists, and frontend GPU decode paths acquire from a blocking byte-counting semaphore of this size before allocating on the device.

Set to `0`

(default) to disable frontend GPU multimodal memory gating.

###

`mm_processor_cache_gb = Field(default=4, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_processor_cache_gb)

The size (in GiB) of the multi-modal processor cache, which is used to avoid re-processing past multi-modal inputs.

This cache is duplicated for each API process and engine core process, resulting in a total memory usage of `mm_processor_cache_gb * (api_server_count + data_parallel_size)`

.

A single processed item larger than this budget is served uncached (with a warning) instead of failing. Raise this value to cache such items.

Set to `0`

to disable this cache completely (not recommended).

###

`mm_processor_cache_type = 'lru'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_processor_cache_type)

Type of cache to use for the multi-modal preprocessor/mapper. If `shm`

, use shared memory FIFO cache. If `lru`

, use mirrored LRU cache.

###

`mm_processor_kwargs = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_processor_kwargs)

Arguments to be forwarded to the model's processor for multi-modal data, e.g., image processor. Overrides for the multi-modal processor obtained from `transformers.AutoProcessor.from_pretrained`

.

The available overrides depend on the model that is being run.

For example, for Phi-3-Vision: `{"num_crops": 4}`

.

###

`mm_shm_cache_max_object_size_mb = Field(default=128, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_shm_cache_max_object_size_mb)

Size limit (in MiB) for each object stored in the multi-modal processor shared memory cache. Only effective when `mm_processor_cache_type`

is `"shm"`

.

###

`mm_tensor_ipc = 'direct_rpc'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.mm_tensor_ipc)

IPC (inter-process communication) method for multimodal tensors. - "direct_rpc": Use msgspec serialization via RPC - "torch_shm": Use torch.multiprocessing shared memory for zero-copy IPC Defaults to "direct_rpc".

###

`skip_mm_profiling = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.skip_mm_profiling)

When enabled, skips multimodal memory profiling and only profiles with language backbone model during engine initialization.

This reduces engine startup time but shifts the responsibility to users for estimating the peak memory usage of the activation of multimodal encoder and embedding cache.

###

`video_pruning_method = 'evs'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.video_pruning_method)

Video token pruning algorithm applied when `video_pruning_rate`

> 0: - "evs": Efficient Video Sampling. - "vidcom2": Video Compression Commander.

###

`video_pruning_rate = Field(default=None, ge=0.0, lt=1.0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.video_pruning_rate)

Fraction of video tokens to prune from each video. Value sits in range [0;1); pruning is enabled when it is greater than 0. The pruning algorithm is selected by `video_pruning_method`

.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

## Source code in `vllm/config/multimodal.py`


###

`fold_mm_processor_device(mm_processor_kwargs, mm_processor_device)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.fold_mm_processor_device)

Fold the `mm_processor_device`

convenience flag into the kwargs.

The flag keeps no state of its own: `mm_processor_kwargs["device"]`

is the only representation of where the processor runs, so an explicit `device`

there always wins and `"auto"`

stays unresolved for `VllmConfig`

, which is where the EC role needed to resolve it lives.

Parameters:

-

(`mm_processor_kwargs`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.fold_mm_processor_device(mm_processor_kwargs))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | NoneThe kwargs as given, or None.

-

(`mm_processor_device`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.fold_mm_processor_device(mm_processor_device))

) –[MMProcessorDevice](https://docs.vllm.ai/multimodal/#vllm.config.multimodal.MMProcessorDevice)| NoneThe flag's value, or None when unset.


Returns:

-

–[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | NoneThe kwargs to build the config with, unchanged unless the flag adds

-

–[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | Nonea

`device`

.

## Source code in `vllm/config/multimodal.py`


###

`get_limit_per_prompt(modality)`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.get_limit_per_prompt)

Get the maximum number of input items allowed per prompt for the given modality (backward compatible).

## Source code in `vllm/config/multimodal.py`


###

`get_mm_processor_device_type()`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.get_mm_processor_device_type)

The torch device type `mm_processor_kwargs["device"]`

names.

`mm_processor_kwargs`

is untyped, so `device`

may be any form torch accepts -- `"cuda"`

, `"cuda:1"`

, `torch.device(...)`

, or a bare index. Normalising through torch rather than parsing the string keeps the non-string forms from slipping past a caller's comparison.

Returns:

-

–[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe device type, or None when no device is requested.


Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)If

`device`

is not something`torch.device`

accepts.`validate_mm_processor_device`

is what surfaces this during startup, so the value is only parsed once.

## Source code in `vllm/config/multimodal.py`


###

`get_video_pruning_spec()`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.get_video_pruning_spec)

Return `(method, rate)`

when video pruning is enabled, else None. `rate`

is the fraction of video tokens to prune.

## Source code in `vllm/config/multimodal.py`


###

`merge_mm_processor_kwargs(inference_kwargs)`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.merge_mm_processor_kwargs)

Get the keyword arguments to pass to the multi-modal processor according to the extra arguments passed during inference.

## Source code in `vllm/config/multimodal.py`


###

`use_gpu_video_backend()`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.use_gpu_video_backend)

Return whether the configured video loader or codec uses the GPU.

## Source code in `vllm/config/multimodal.py`


###

`validate_mm_processor_device(ec_config)`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.validate_mm_processor_device)

Check `mm_processor_kwargs["device"]`

for this deployment.

The only place the requested device is validated, so it runs even on a CPU-only platform: the value is parsed before any early return.

Parameters:

-

(`ec_config`

[¶](https://docs.vllm.ai#vllm.config.MultiModalConfig.validate_mm_processor_device(ec_config))

) –[ECTransferConfig](https://docs.vllm.ai/ec_transfer/#vllm.config.ec_transfer.ECTransferConfig)| NoneThe deployment's EC config, or None when it is not an encode/prefill/decode deployment. Passed in because it is not reachable from here, and because a field assigned after construction would not re-trigger this config's validators.


Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)If the requested device is not a torch device, or if it is the accelerator on an instance that also runs the language model.


## Source code in `vllm/config/multimodal.py`


##

`ObservabilityConfig`

[¶](https://docs.vllm.ai#vllm.config.ObservabilityConfig)

Configuration for observability - metrics and tracing.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.ObservabilityConfig.compute_hash)WARNING: Whenever a new field is added to this config,


Attributes:

-
([collect_detailed_traces](https://docs.vllm.ai#vllm.config.ObservabilityConfig.collect_detailed_traces)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[DetailedTraceModules] | NoneIt makes sense to set this only if

`--otlp-traces-endpoint`

is set. If -
([collect_model_execute_time](https://docs.vllm.ai#vllm.config.ObservabilityConfig.collect_model_execute_time)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to collect model execute time for the request.

-
([collect_model_forward_time](https://docs.vllm.ai#vllm.config.ObservabilityConfig.collect_model_forward_time)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to collect model forward time for the request.

-
([cudagraph_metrics](https://docs.vllm.ai#vllm.config.ObservabilityConfig.cudagraph_metrics)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable CUDA graph metrics (number of padded/unpadded tokens, runtime cudagraph

-
([enable_layerwise_nvtx_tracing](https://docs.vllm.ai#vllm.config.ObservabilityConfig.enable_layerwise_nvtx_tracing)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable layerwise NVTX tracing. This traces the execution of each layer or

-
([enable_logging_iteration_details](https://docs.vllm.ai#vllm.config.ObservabilityConfig.enable_logging_iteration_details)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable detailed logging of iteration details.

-
([enable_mfu_metrics](https://docs.vllm.ai#vllm.config.ObservabilityConfig.enable_mfu_metrics)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable Model FLOPs Utilization (MFU) metrics.

-
([enable_mm_processor_stats](https://docs.vllm.ai#vllm.config.ObservabilityConfig.enable_mm_processor_stats)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable collection of timing statistics for multimodal processor operations.

-
([jit_monitor_mode](https://docs.vllm.ai#vllm.config.ObservabilityConfig.jit_monitor_mode)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['warn', 'error']How to handle post-warmup JIT compilation events.

-
([jit_monitor_verbose](https://docs.vllm.ai#vllm.config.ObservabilityConfig.jit_monitor_verbose)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Log every monitored JIT compile with runtime details. This can emit many

-
([kv_cache_metrics](https://docs.vllm.ai#vllm.config.ObservabilityConfig.kv_cache_metrics)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable KV cache residency metrics (lifetime, idle time, reuse gaps).

-
([kv_cache_metrics_sample](https://docs.vllm.ai#vllm.config.ObservabilityConfig.kv_cache_metrics_sample)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Sampling rate for KV cache metrics (0.0, 1.0]. Default 0.01 = 1% of blocks.

-
([otlp_traces_endpoint](https://docs.vllm.ai#vllm.config.ObservabilityConfig.otlp_traces_endpoint)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneTarget URL to which OpenTelemetry traces will be sent.

-
([per_request_spec_decode_metrics](https://docs.vllm.ai#vllm.config.ObservabilityConfig.per_request_spec_decode_metrics)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['none', 'summary', 'detailed']Include per-request speculative-decoding acceptance metrics in the

-
([show_hidden_metrics](https://docs.vllm.ai#vllm.config.ObservabilityConfig.show_hidden_metrics)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Check if the hidden metrics should be shown.

-
([show_hidden_metrics_for_version](https://docs.vllm.ai#vllm.config.ObservabilityConfig.show_hidden_metrics_for_version)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneEnable deprecated Prometheus metrics that have been hidden since the


## Source code in `vllm/config/observability.py`


|
|

###

`collect_detailed_traces = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ObservabilityConfig.collect_detailed_traces)

It makes sense to set this only if `--otlp-traces-endpoint`

is set. If set, it will collect detailed traces for the specified modules. This involves use of possibly costly and or blocking operations and hence might have a performance impact.

Note that collecting detailed timing information for each request can be expensive.

###

`collect_model_execute_time`

`cached`

`property`

[¶](https://docs.vllm.ai#vllm.config.ObservabilityConfig.collect_model_execute_time)

Whether to collect model execute time for the request.

###

`collect_model_forward_time`

`cached`

`property`

[¶](https://docs.vllm.ai#vllm.config.ObservabilityConfig.collect_model_forward_time)

Whether to collect model forward time for the request.

###

`cudagraph_metrics = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ObservabilityConfig.cudagraph_metrics)

Enable CUDA graph metrics (number of padded/unpadded tokens, runtime cudagraph dispatch modes, and their observed frequencies at every logging interval).

###

`enable_layerwise_nvtx_tracing = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ObservabilityConfig.enable_layerwise_nvtx_tracing)

Enable layerwise NVTX tracing. This traces the execution of each layer or module in the model and attach information such as input/output shapes to nvtx range markers. Noted that this doesn't work with CUDA graphs enabled.

###

`enable_logging_iteration_details = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ObservabilityConfig.enable_logging_iteration_details)

Enable detailed logging of iteration details. If set, vllm EngineCore will log iteration details This includes number of context/generation requests and tokens and the elapsed cpu time for the iteration.

###

`enable_mfu_metrics = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ObservabilityConfig.enable_mfu_metrics)

Enable Model FLOPs Utilization (MFU) metrics.

###

`enable_mm_processor_stats = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ObservabilityConfig.enable_mm_processor_stats)

Enable collection of timing statistics for multimodal processor operations. This is for internal use only (e.g., benchmarks) and is not exposed as a CLI argument.

###

`jit_monitor_mode = 'warn'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ObservabilityConfig.jit_monitor_mode)

How to handle post-warmup JIT compilation events.

###

`jit_monitor_verbose = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ObservabilityConfig.jit_monitor_verbose)

Log every monitored JIT compile with runtime details. This can emit many logs and add overhead, so it is intended for debugging.

###

`kv_cache_metrics = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ObservabilityConfig.kv_cache_metrics)

Enable KV cache residency metrics (lifetime, idle time, reuse gaps). Uses sampling to minimize overhead. Requires log stats to be enabled (i.e., --disable-log-stats not set).

###

`kv_cache_metrics_sample = Field(default=0.01, gt=0, le=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ObservabilityConfig.kv_cache_metrics_sample)

Sampling rate for KV cache metrics (0.0, 1.0]. Default 0.01 = 1% of blocks.

###

`otlp_traces_endpoint = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ObservabilityConfig.otlp_traces_endpoint)

Target URL to which OpenTelemetry traces will be sent.

###

`per_request_spec_decode_metrics = 'none'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ObservabilityConfig.per_request_spec_decode_metrics)

Include per-request speculative-decoding acceptance metrics in the response under `metrics.speculative_decoding`

. `none`

disables; `summary`

adds mean acceptance length, draft acceptance rate, and the step-by-draft-length histogram; `detailed`

additionally records the ordered per-step accepted/proposed arrays (one entry per verify step). Only reported for single-sequence requests (`n == 1`

), mirroring the timing metrics. No effect unless speculative decoding is enabled. Independent of `--disable-log-stats`

. This is the per-request response-body counterpart of the aggregate `vllm:spec_decode_*`

Prometheus metrics. The response field is experimental and its shape may change in a future release.

###

`show_hidden_metrics`

`cached`

`property`

[¶](https://docs.vllm.ai#vllm.config.ObservabilityConfig.show_hidden_metrics)

Check if the hidden metrics should be shown.

###

`show_hidden_metrics_for_version = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ObservabilityConfig.show_hidden_metrics_for_version)

Enable deprecated Prometheus metrics that have been hidden since the specified version. For example, if a previously deprecated metric has been hidden since the v0.7.0 release, you use `--show-hidden-metrics-for-version=0.7`

as a temporary escape hatch while you migrate to new metrics. The metric is likely to be removed completely in an upcoming release.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.ObservabilityConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

## Source code in `vllm/config/observability.py`


##

`OffloadConfig`

[¶](https://docs.vllm.ai#vllm.config.OffloadConfig)

Configuration for model weight offloading to reduce GPU memory usage.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.OffloadConfig.compute_hash)Provide a hash that uniquely identifies all the offload configs.

-
–[validate_offload_config](https://docs.vllm.ai#vllm.config.OffloadConfig.validate_offload_config)Validate offload configuration constraints.


Attributes:

-
([offload_backend](https://docs.vllm.ai#vllm.config.OffloadConfig.offload_backend)`OffloadBackend`

) –The backend for weight offloading. Options:

-
([prefetch](https://docs.vllm.ai#vllm.config.OffloadConfig.prefetch)

) –[PrefetchOffloadConfig](https://docs.vllm.ai/offload/#vllm.config.offload.PrefetchOffloadConfig)Parameters for prefetch offloading backend.

-
([uva](https://docs.vllm.ai#vllm.config.OffloadConfig.uva)

) –[UVAOffloadConfig](https://docs.vllm.ai/offload/#vllm.config.offload.UVAOffloadConfig)Parameters for UVA offloading backend.


## Source code in `vllm/config/offload.py`


###

`offload_backend = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.OffloadConfig.offload_backend)

The backend for weight offloading. Options: - "auto": Selects based on which sub-config has non-default values (prefetch if offload_group_size > 0, uva if cpu_offload_gb > 0). - "uva": UVA (Unified Virtual Addressing) zero-copy offloading. - "prefetch": Async prefetch with group-based layer offloading.

###

`prefetch = Field(default_factory=PrefetchOffloadConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.OffloadConfig.prefetch)

Parameters for prefetch offloading backend.

###

`uva = Field(default_factory=UVAOffloadConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.OffloadConfig.uva)

Parameters for UVA offloading backend.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.OffloadConfig.compute_hash)

Provide a hash that uniquely identifies all the offload configs.

All fields are included because PrefetchOffloader patches module forwards and inserts custom ops (wait_prefetch, start_prefetch) into the computation graph. Changing any offload setting can alter which layers are hooked and how prefetch indices are computed, so the compilation cache must distinguish them.

## Source code in `vllm/config/offload.py`


###

`validate_offload_config()`

[¶](https://docs.vllm.ai#vllm.config.OffloadConfig.validate_offload_config)

Validate offload configuration constraints.

## Source code in `vllm/config/offload.py`


##

`ParallelConfig`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig)

Configuration for the distributed execution.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.ParallelConfig.compute_hash)Provide a hash that uniquely identifies all the configs

-
–[get_next_dp_init_port](https://docs.vllm.ai#vllm.config.ParallelConfig.get_next_dp_init_port)We might need to initialize process groups in multiple

-
–[reconfigure_for_independent_dp_rank](https://docs.vllm.ai#vllm.config.ParallelConfig.reconfigure_for_independent_dp_rank)Reconfigure for a single independent non-MoE DP rank.

-
–[set_dcp_defaults](https://docs.vllm.ai#vllm.config.ParallelConfig.set_dcp_defaults)Fill in the DCP options the user left unset.

-
–[sync_dp_state](https://docs.vllm.ai#vllm.config.ParallelConfig.sync_dp_state)Combined all-reduce for DP state synchronization.


Attributes:

-
([all2all_backend](https://docs.vllm.ai#vllm.config.ParallelConfig.all2all_backend)`All2AllBackend`

) –All2All backend for MoE expert parallel communication. Available options:

-
([assigned_physical_gpu_ids](https://docs.vllm.ai#vllm.config.ParallelConfig.assigned_physical_gpu_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | NoneMapping from vLLM-local logical GPU IDs to physical GPU IDs.

-
([cp_kv_cache_interleave_size](https://docs.vllm.ai#vllm.config.ParallelConfig.cp_kv_cache_interleave_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Interleave size of kv_cache storage while using DCP.

-
([cpu_distributed_timeout_seconds](https://docs.vllm.ai#vllm.config.ParallelConfig.cpu_distributed_timeout_seconds)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneTimeout (in seconds) for cpu communication groups. If None, PyTorch's

-
([data_parallel_backend](https://docs.vllm.ai#vllm.config.ParallelConfig.data_parallel_backend)`DataParallelBackend`

) –Backend to use for data parallel, either "mp" or "ray".

-
([data_parallel_external_lb](https://docs.vllm.ai#vllm.config.ParallelConfig.data_parallel_external_lb)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to use "external" DP LB mode. Applies only to online serving

-
([data_parallel_hybrid_lb](https://docs.vllm.ai#vllm.config.ParallelConfig.data_parallel_hybrid_lb)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to use "hybrid" DP LB mode. Applies only to online serving

-
([data_parallel_index](https://docs.vllm.ai#vllm.config.ParallelConfig.data_parallel_index)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Equal to the data parallel rank but not used for torch process groups

-
([data_parallel_master_ip](https://docs.vllm.ai#vllm.config.ParallelConfig.data_parallel_master_ip)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)IP of the data parallel master.

-
([data_parallel_master_port](https://docs.vllm.ai#vllm.config.ParallelConfig.data_parallel_master_port)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Port of the data parallel master.

-
([data_parallel_rank](https://docs.vllm.ai#vllm.config.ParallelConfig.data_parallel_rank)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Rank of the data parallel group. The runtime check at

-
([data_parallel_rank_local](https://docs.vllm.ai#vllm.config.ParallelConfig.data_parallel_rank_local)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneLocal rank of the data parallel group, set only in SPMD mode.

-
([data_parallel_rpc_port](https://docs.vllm.ai#vllm.config.ParallelConfig.data_parallel_rpc_port)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Fixed port for data parallel messaging, shared by all nodes.

-
([data_parallel_size](https://docs.vllm.ai#vllm.config.ParallelConfig.data_parallel_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of data parallel groups. MoE layers will be sharded according to

-
([data_parallel_size_local](https://docs.vllm.ai#vllm.config.ParallelConfig.data_parallel_size_local)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of local data parallel groups. A value of 0 is a sentinel used by

-
([dbo_decode_token_threshold](https://docs.vllm.ai#vllm.config.ParallelConfig.dbo_decode_token_threshold)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The threshold for dual batch overlap for batches only containing decodes.

-
([dbo_prefill_token_threshold](https://docs.vllm.ai#vllm.config.ParallelConfig.dbo_prefill_token_threshold)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The threshold for dual batch overlap for batches that contain one or more

-
([dcp_comm_backend](https://docs.vllm.ai#vllm.config.ParallelConfig.dcp_comm_backend)`DCPCommBackend | None`

) –Communication backend for Decode Context Parallel (DCP).

-
([dcp_kv_cache_interleave_size](https://docs.vllm.ai#vllm.config.ParallelConfig.dcp_kv_cache_interleave_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Interleave size of kv_cache storage while using DCP.

-
([dcp_q_replicate](https://docs.vllm.ai#vllm.config.ParallelConfig.dcp_q_replicate)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneReplicate the MLA query projection within each DCP group so decode can skip the

-
([decode_context_parallel_size](https://docs.vllm.ai#vllm.config.ParallelConfig.decode_context_parallel_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of ranks that shard the decode KV cache. DCP does not expand

-
([disable_custom_all_reduce](https://docs.vllm.ai#vllm.config.ParallelConfig.disable_custom_all_reduce)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Disable the custom all-reduce kernel and fall back to NCCL.

-
([disable_nccl_for_dp_synchronization](https://docs.vllm.ai#vllm.config.ParallelConfig.disable_nccl_for_dp_synchronization)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneForces the dp synchronization logic in vllm/v1/worker/dp_utils.py

-
([distributed_executor_backend](https://docs.vllm.ai#vllm.config.ParallelConfig.distributed_executor_backend)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| DistributedExecutorBackend |[type](https://docs.python.org/3/builtins/functions.html#type)[[Executor](https://docs.vllm.ai/v1/executor/#vllm.v1.executor.Executor)] | NoneBackend to use for distributed model workers, either "ray" or "mp"

-
([distributed_timeout_seconds](https://docs.vllm.ai#vllm.config.ParallelConfig.distributed_timeout_seconds)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneTimeout in seconds for distributed operations (e.g., init_process_group).

-
([dp_sync_interval](https://docs.vllm.ai#vllm.config.ParallelConfig.dp_sync_interval)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Steps between DP finish-sync all-reduces; must match across DP ranks.

-
([elastic_ep_max_dp_size](https://docs.vllm.ai#vllm.config.ParallelConfig.elastic_ep_max_dp_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum data parallel size supported by elastic expert parallelism.

-
([enable_batch_sharded_sampling](https://docs.vllm.ai#vllm.config.ParallelConfig.enable_batch_sharded_sampling)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneUse sharded sampling across tensor parallel ranks. Each rank samples

-
([enable_dbo](https://docs.vllm.ai#vllm.config.ParallelConfig.enable_dbo)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable dual batch overlap for the model executor.

-
([enable_elastic_ep](https://docs.vllm.ai#vllm.config.ParallelConfig.enable_elastic_ep)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable elastic expert parallelism with stateless NCCL groups for DP/EP.

-
([enable_ep_weight_filter](https://docs.vllm.ai#vllm.config.ParallelConfig.enable_ep_weight_filter)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Skip non-local expert weights during model loading when expert

-
([enable_eplb](https://docs.vllm.ai#vllm.config.ParallelConfig.enable_eplb)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable expert parallelism load balancing for MoE layers.

-
([enable_expert_parallel](https://docs.vllm.ai#vllm.config.ParallelConfig.enable_expert_parallel)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Use expert parallelism instead of tensor parallelism for MoE layers.

-
([enable_fault_tolerance](https://docs.vllm.ai#vllm.config.ParallelConfig.enable_fault_tolerance)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable fault tolerance for detailed error recovery,

-
([eplb_config](https://docs.vllm.ai#vllm.config.ParallelConfig.eplb_config)

) –[EPLBConfig](https://docs.vllm.ai/parallel/#vllm.config.parallel.EPLBConfig)Expert parallelism configuration.

-
([expert_placement_strategy](https://docs.vllm.ai#vllm.config.ParallelConfig.expert_placement_strategy)`ExpertPlacementStrategy`

) –The expert placement strategy for MoE layers:

-
([fault_tolerance_config](https://docs.vllm.ai#vllm.config.ParallelConfig.fault_tolerance_config)

) –[FaultToleranceConfig](https://docs.vllm.ai/fault_tolerance/#vllm.config.fault_tolerance.FaultToleranceConfig)The configurations for fault tolerance.

-
([is_moe_model](https://docs.vllm.ai#vllm.config.ParallelConfig.is_moe_model)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneWhether the deployed model is MoE (if known).

-
([local_engines_only](https://docs.vllm.ai#vllm.config.ParallelConfig.local_engines_only)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Client manages local+remote EngineCores in pure internal LB case.

-
([master_addr](https://docs.vllm.ai#vllm.config.ParallelConfig.master_addr)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)distributed master address for multi-node distributed

-
([master_port](https://docs.vllm.ai#vllm.config.ParallelConfig.master_port)

) –[int](https://docs.python.org/3/builtins/functions.html#int)distributed master port for multi-node distributed

-
([max_parallel_loading_workers](https://docs.vllm.ai#vllm.config.ParallelConfig.max_parallel_loading_workers)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMaximum number of parallel loading workers when loading model

-
([nnodes](https://docs.vllm.ai#vllm.config.ParallelConfig.nnodes)

) –[int](https://docs.python.org/3/builtins/functions.html#int)num of nodes for multi-node distributed

-
([nnodes_within_dp](https://docs.vllm.ai#vllm.config.ParallelConfig.nnodes_within_dp)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of nodes one DP replica spans.

-
([node_rank](https://docs.vllm.ai#vllm.config.ParallelConfig.node_rank)

) –[int](https://docs.python.org/3/builtins/functions.html#int)distributed node rank for multi-node distributed

-
([numa_bind](https://docs.vllm.ai#vllm.config.ParallelConfig.numa_bind)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable NUMA binding for GPU worker subprocesses.

-
([numa_bind_cpus](https://docs.vllm.ai#vllm.config.ParallelConfig.numa_bind_cpus)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | NoneOptional CPU lists to bind each GPU worker to.

-
([numa_bind_nodes](https://docs.vllm.ai#vllm.config.ParallelConfig.numa_bind_nodes)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | NoneNUMA node to bind each GPU worker to.

-
([pipeline_parallel_size](https://docs.vllm.ai#vllm.config.ParallelConfig.pipeline_parallel_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of pipeline parallel groups.

-
([placement_group](https://docs.vllm.ai#vllm.config.ParallelConfig.placement_group)`PlacementGroup | None`

) –ray distributed model workers placement group.

-
([prefill_context_parallel_size](https://docs.vllm.ai#vllm.config.ParallelConfig.prefill_context_parallel_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of ranks that split prefill sequence computation. PCP expands

-
([rank](https://docs.vllm.ai#vllm.config.ParallelConfig.rank)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Global rank in distributed setup.

-
([ray_runtime_env](https://docs.vllm.ai#vllm.config.ParallelConfig.ray_runtime_env)`RuntimeEnv | None`

) –Ray runtime environment to pass to distributed workers.

-
([ray_workers_use_nsight](https://docs.vllm.ai#vllm.config.ParallelConfig.ray_workers_use_nsight)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to profile Ray workers with nsight, see https://docs.ray.io/en/latest/ray-observability/user-guides/profiling.html#profiling-nsight-profiler.

-
([sd_worker_cls](https://docs.vllm.ai#vllm.config.ParallelConfig.sd_worker_cls)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The full name of the worker class to use for speculative decoding.

-
([tensor_parallel_size](https://docs.vllm.ai#vllm.config.ParallelConfig.tensor_parallel_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of tensor parallel groups.

-
([ubatch_size](https://docs.vllm.ai#vllm.config.ParallelConfig.ubatch_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of ubatch size.

-
([worker_cls](https://docs.vllm.ai#vllm.config.ParallelConfig.worker_cls)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The full name of the worker class to use. If "auto", the worker class

-
([worker_extension_cls](https://docs.vllm.ai#vllm.config.ParallelConfig.worker_extension_cls)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The full name of the worker extension class to use. The worker extension

-
([world_size](https://docs.vllm.ai#vllm.config.ParallelConfig.world_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)world_size is TPxPP, it affects the number of workers we create.

-
([world_size_across_dp](https://docs.vllm.ai#vllm.config.ParallelConfig.world_size_across_dp)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Process world size across TP, PCP, PP, and DP.


## Source code in `vllm/config/parallel.py`


|
|

###

`_allow_auto_resolve_cp_interleave_size = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig._allow_auto_resolve_cp_interleave_size)

Whether NIXL may select the interleave size automatically.

###

`_api_process_count = Field(default=1, gt=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig._api_process_count)

The number of API processes initialized.

## Note

This is an internal config that is only valid for and should only be set by API server scale-out.

###

`_api_process_rank = Field(default=0, ge=(-1))`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig._api_process_rank)

The rank of this API process, or `-1`

for engine core processes under API server scale-out.

## Note

This is an internal config that is only valid for and should only be set by API server scale-out.

###

`_coord_store_port = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig._coord_store_port)

Port of the coordination TCPStore. Can be set by the API server; workers connect as clients to exchange self-picked group ports at runtime.

###

`_data_parallel_master_port_list = Field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig._data_parallel_master_port_list)

List of open port auto-queried for data parallel messaging. Set to be private as it's not intended to be configured by users.

###

`all2all_backend = 'allgather_reducescatter'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.all2all_backend)

All2All backend for MoE expert parallel communication. Available options:

- "allgather_reducescatter": All2all based on allgather and reducescatter
- "deepep_high_throughput": Use deepep high-throughput kernels
- "deepep_low_latency": Use deepep low-latency kernels
- "mori_high_throughput": MoRI EP with InterNodeV1 for multi-node
- "mori_low_latency": MoRI EP with InterNodeV1LL for multi-node
- "moonep": MoonEP balanced EP with dynamic redundant experts (NVLink)
- "nixl_ep": Use nixl-ep kernels
- "flashinfer_nvlink_one_sided": Use flashinfer high-throughput a2a kernels
- "flashinfer_nvlink_two_sided": Use flashinfer two-sided kernels for mnnvl

###

`assigned_physical_gpu_ids = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.assigned_physical_gpu_ids)

Mapping from vLLM-local logical GPU IDs to physical GPU IDs.

For example, `[2, 3]`

means logical GPU 0 maps to physical GPU 2, and logical GPU 1 maps to physical GPU 3. Physical IDs are used only at platform/topology boundaries such as NVML, NIC affinity, P2P checks, and final CUDA device selection when needed. When None, logical IDs map to visible device IDs in order.

###

`cp_kv_cache_interleave_size = 1`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.cp_kv_cache_interleave_size)

Interleave size of kv_cache storage while using DCP. Store interleave_size tokens on dcp_rank i, then store next interleave_size tokens on dcp_rank i+1. Interleave_size=1: token-level alignment, where token `i`

is stored on dcp_rank `i % dcp_world_size`

. Interleave_size=block_size: block-level alignment, where tokens are first populated to the preceding ranks. Tokens are then stored in (rank i+1, block j) only after (rank i, block j) is fully occupied. Block_size should be greater than or equal to cp_kv_cache_interleave_size. Block_size should be divisible by cp_kv_cache_interleave_size.

When --cp-kv-cache-interleave-size is omitted (None), the interleave size is resolved automatically based on NIXL transfer requirements. Explicit settings take priority.

###

`cpu_distributed_timeout_seconds = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.cpu_distributed_timeout_seconds)

Timeout (in seconds) for cpu communication groups. If None, PyTorch's default timeout is used (1800s for gloo).

###

`data_parallel_backend = 'mp'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.data_parallel_backend)

Backend to use for data parallel, either "mp" or "ray".

###

`data_parallel_external_lb = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.data_parallel_external_lb)

Whether to use "external" DP LB mode. Applies only to online serving and when data_parallel_size > 0. This is useful for a "one-pod-per-rank" wide-EP setup in Kubernetes. Supported only for MoE deployments; non-MoE models should use independent vLLM instances without --data-parallel-* arguments. Set implicitly when --data-parallel-rank is provided explicitly to vllm serve.

###

`data_parallel_hybrid_lb = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.data_parallel_hybrid_lb)

Whether to use "hybrid" DP LB mode. Applies only to online serving and when data_parallel_size > 0. Enables running an AsyncLLM and API server on a "per-node" basis where vLLM load balances between local data parallel ranks, but an external LB balances between vLLM nodes/replicas. Set explicitly in conjunction with --data-parallel-start-rank.

###

`data_parallel_index = Field(init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.data_parallel_index)

Equal to the data parallel rank but not used for torch process groups and not overridden for dense models.

###

`data_parallel_master_ip = '127.0.0.1'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.data_parallel_master_ip)

IP of the data parallel master.

###

`data_parallel_master_port = 29500`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.data_parallel_master_port)

Port of the data parallel master.

###

`data_parallel_rank = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.data_parallel_rank)

Rank of the data parallel group. The runtime check at `__post_init__`

further bounds this by `data_parallel_size`

.

###

`data_parallel_rank_local = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.data_parallel_rank_local)

Local rank of the data parallel group, set only in SPMD mode.

###

`data_parallel_rpc_port = Field(default=29550, ge=1, le=65535)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.data_parallel_rpc_port)

Fixed port for data parallel messaging, shared by all nodes.

###

`data_parallel_size = Field(default=1, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.data_parallel_size)

Number of data parallel groups. MoE layers will be sharded according to the product of the tensor, prefill-context, and data parallel sizes.

###

`data_parallel_size_local = Field(default=1, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.data_parallel_size_local)

Number of local data parallel groups. A value of 0 is a sentinel used by the engine-args layer to signal that data parallelism was specified externally (see `ParallelConfig.__post_init__`

).

###

`dbo_decode_token_threshold = Field(default=32, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.dbo_decode_token_threshold)

The threshold for dual batch overlap for batches only containing decodes. If the number of tokens in the request is greater than this threshold, microbatching will be used. Otherwise, the request will be processed in a single batch.

###

`dbo_prefill_token_threshold = Field(default=512, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.dbo_prefill_token_threshold)

The threshold for dual batch overlap for batches that contain one or more prefills. If the number of tokens in the request is greater than this threshold, microbatching will be used. Otherwise, the request will be processed in a single batch.

###

`dcp_comm_backend = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.dcp_comm_backend)

Communication backend for Decode Context Parallel (DCP). - "ag_rs": AllGather + ReduceScatter (existing behavior) - "a2a": All-to-All exchange of partial outputs + LSE, then combine with Triton kernel. Reduces NCCL calls from 3 to 2 per layer for MLA models.

`None`

selects the model default, which is "ag_rs" unless the model overrides it via [ set_dcp_defaults](https://docs.vllm.ai#vllm.config.ParallelConfig.set_dcp_defaults).

###

`dcp_kv_cache_interleave_size = 1`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.dcp_kv_cache_interleave_size)

Interleave size of kv_cache storage while using DCP. dcp_kv_cache_interleave_size has been replaced by cp_kv_cache_interleave_size, and will be deprecated when PCP is fully supported.

###

`dcp_q_replicate = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.dcp_q_replicate)

Replicate the MLA query projection within each DCP group so decode can skip the query all-gather.

With DCP the KV cache is sharded across the group, so the standard MLA decode path all-gathers the query every step. Replicating the (small) query projection at load time lets each rank materialize the full group-local head set and skip that collective, at the cost of computing the projection redundantly on every rank in the group.

###

`decode_context_parallel_size = Field(default=1, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.decode_context_parallel_size)

Number of ranks that shard the decode KV cache. DCP does not expand the process world size. Without PCP, DCP reuses TP ranks. With PCP, DCP either spans the PCP axis or the full TP x PCP block.

###

`disable_custom_all_reduce = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.disable_custom_all_reduce)

Disable the custom all-reduce kernel and fall back to NCCL.

###

`disable_nccl_for_dp_synchronization = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.disable_nccl_for_dp_synchronization)

Forces the dp synchronization logic in vllm/v1/worker/dp_utils.py to use Gloo instead of NCCL for its all reduce.

Defaults to True when async scheduling is enabled, False otherwise.

###

`distributed_executor_backend = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.distributed_executor_backend)

Backend to use for distributed model workers, either "ray" or "mp" (multiprocessing). If the product of pipeline_parallel_size and tensor_parallel_size is less than or equal to the number of GPUs available, "mp" will be used to keep processing on a single host. Otherwise, an error will be raised. To use "mp" you must also set nnodes, and to use "ray" you must manually set distributed_executor_backend to "ray".

## Note

[TPU](https://docs.vllm.ai/projects/tpu/en/latest/) platform only supports Ray for distributed inference.

###

`distributed_timeout_seconds = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.distributed_timeout_seconds)

Timeout in seconds for distributed operations (e.g., init_process_group). If set, this value is passed to torch.distributed.init_process_group as the timeout parameter. If None, PyTorch's default timeout is used (600s for NCCL). Increase this for multi-node setups where model downloads may be slow.

###

`dp_sync_interval = Field(default=16, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.dp_sync_interval)

Steps between DP finish-sync all-reduces; must match across DP ranks.

###

`elastic_ep_max_dp_size = Field(default=None, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.elastic_ep_max_dp_size)

Maximum data parallel size supported by elastic expert parallelism.

###

`enable_batch_sharded_sampling = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.enable_batch_sharded_sampling)

Use sharded sampling across tensor parallel ranks. Each rank samples a slice of the batch instead of every rank sampling all of it. Currently defaults to False if not set. Enabling it explicitly raises when the config cannot support it (`tensor_parallel_size`

must be > 1, `max_num_seqs`

at least `tensor_parallel_size`

, and `max_logprobs`

non-negative). Models opt in by implementing `compute_logits_local`

.

###

`enable_dbo = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.enable_dbo)

Enable dual batch overlap for the model executor.

###

`enable_elastic_ep = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.enable_elastic_ep)

Enable elastic expert parallelism with stateless NCCL groups for DP/EP.

###

`enable_ep_weight_filter = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.enable_ep_weight_filter)

Skip non-local expert weights during model loading when expert parallelism is active. Each rank only reads its own expert shard from disk, which can drastically reduce storage I/O for MoE models with per-expert weight tensors (e.g. DeepSeek, Mixtral, Kimi-K2.5). Has no effect on 3D fused-expert checkpoints (e.g. GPT-OSS) or non-MoE models.

###

`enable_eplb = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.enable_eplb)

Enable expert parallelism load balancing for MoE layers.

###

`enable_expert_parallel = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.enable_expert_parallel)

Use expert parallelism instead of tensor parallelism for MoE layers.

###

`enable_fault_tolerance = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.enable_fault_tolerance)

Enable fault tolerance for detailed error recovery, such as scaling down fault DPEngineCore.

###

`eplb_config = Field(default_factory=EPLBConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.eplb_config)

Expert parallelism configuration.

###

`expert_placement_strategy = 'linear'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.expert_placement_strategy)

The expert placement strategy for MoE layers:

- "linear": Experts are placed in a contiguous manner. For example, with 4 experts and 2 ranks, rank 0 will have experts [0, 1] and rank 1 will have experts [2, 3].
- "round_robin": Experts are placed in a round-robin manner. For example, with 4 experts and 2 ranks, rank 0 will have experts [0, 2] and rank 1 will have experts [1, 3]. This strategy can help improve load balancing for grouped expert models with no redundant experts.

###

`fault_tolerance_config = Field(default_factory=FaultToleranceConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.fault_tolerance_config)

The configurations for fault tolerance.

###

`is_moe_model = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.is_moe_model)

Whether the deployed model is MoE (if known).

###

`local_engines_only`

`property`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.local_engines_only)

Client manages local+remote EngineCores in pure internal LB case. Client manages local EngineCores in hybrid and external LB case.

###

`master_addr = '127.0.0.1'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.master_addr)

distributed master address for multi-node distributed inference when distributed_executor_backend is mp.

###

`master_port = 29501`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.master_port)

distributed master port for multi-node distributed inference when distributed_executor_backend is mp.

###

`max_parallel_loading_workers = Field(default=None, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.max_parallel_loading_workers)

Maximum number of parallel loading workers when loading model sequentially in multiple batches. To avoid RAM OOM when using tensor parallel and large models.

###

`nnodes = Field(default=1, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.nnodes)

num of nodes for multi-node distributed inference when distributed_executor_backend is mp.

###

`nnodes_within_dp`

`property`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.nnodes_within_dp)

Number of nodes one DP replica spans.

External LB pins `data_parallel_size_local`

to 1, so the ratio rounds down to 0 once DP replicas outnumber nodes. A replica that does not span nodes still occupies exactly one.

###

`node_rank = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.node_rank)

distributed node rank for multi-node distributed inference when distributed_executor_backend is mp.

###

`numa_bind = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.numa_bind)

Enable NUMA binding for GPU worker subprocesses.

By default, workers are pinned to their GPU's NUMA-local CPUs and memory; on PCT-capable Xeons they also auto-bind to the SKU's PCT priority cores.

###

`numa_bind_cpus = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.numa_bind_cpus)

Optional CPU lists to bind each GPU worker to.

Specify one CPU list per visible GPU, for example `["0-3", "4-7", "8-11", "12-15"]`

. When set, vLLM uses `numactl --physcpubind`

instead of `--cpunodebind`

. This is useful for custom policies such as binding to PCT or other high-frequency cores. Each entry must use `numactl --physcpubind`

CPU-list syntax, for example `"0-3"`

or `"0,2,4-7"`

.

###

`numa_bind_nodes = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.numa_bind_nodes)

NUMA node to bind each GPU worker to.

Specify one NUMA node per visible GPU, for example `[0, 0, 1, 1]`

for a 4-GPU system with GPUs 0-1 on NUMA node 0 and GPUs 2-3 on NUMA node 1. If unset and `numa_bind=True`

, vLLM auto-detects the GPU-to-NUMA topology. The values are passed to `numactl --membind`

and `--cpunodebind`

, so they must be valid `numactl`

NUMA node indices.

###

`pipeline_parallel_size = Field(default=1, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.pipeline_parallel_size)

Number of pipeline parallel groups.

###

`placement_group = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.placement_group)

ray distributed model workers placement group.

###

`prefill_context_parallel_size = Field(default=1, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.prefill_context_parallel_size)

Number of ranks that split prefill sequence computation. PCP expands the process world size but does not increase the KV-cache shard count.

###

`rank = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.rank)

Global rank in distributed setup.

###

`ray_runtime_env = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.ray_runtime_env)

Ray runtime environment to pass to distributed workers.

###

`ray_workers_use_nsight = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.ray_workers_use_nsight)

Whether to profile Ray workers with nsight, see https://docs.ray.io/en/latest/ray-observability/user-guides/profiling.html#profiling-nsight-profiler.

###

`sd_worker_cls = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.sd_worker_cls)

The full name of the worker class to use for speculative decoding. If "auto", the worker class will be determined based on the platform.

###

`tensor_parallel_size = Field(default=1, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.tensor_parallel_size)

Number of tensor parallel groups.

###

`ubatch_size = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.ubatch_size)

Number of ubatch size.

###

`worker_cls = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.worker_cls)

The full name of the worker class to use. If "auto", the worker class will be determined based on the platform.

###

`worker_extension_cls = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.worker_extension_cls)

The full name of the worker extension class to use. The worker extension class is dynamically inherited by the worker class. This is used to inject new attributes and methods to the worker class for use in collective_rpc calls.

###

`world_size = Field(init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.world_size)

world_size is TPxPP, it affects the number of workers we create.

###

`world_size_across_dp`

`property`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.world_size_across_dp)

Process world size across TP, PCP, PP, and DP.

###

`_pick_stateless_dp_port()`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig._pick_stateless_dp_port)

Return `(port, listen_socket)`

for DP group init.

With a coord store, rank 0 binds a socket and publishes the port; others read it. Without one, pops a pre-allocated port and returns `listen_socket=None`

.

## Source code in `vllm/config/parallel.py`


###

`_skip_none_validation(value, handler)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig._skip_none_validation)

Skip validation if the value is `None`

when initialisation is delayed.

## Source code in `vllm/config/parallel.py`


###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.compute_hash)

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

This hash is also used for DP worker configuration validation to prevent hangs from mismatched collective communication patterns.

## Source code in `vllm/config/parallel.py`


###

`get_next_dp_init_port()`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.get_next_dp_init_port)

We might need to initialize process groups in multiple processes that is related to data parallelism, e.g. both in the worker and in the engine, which can live in different processes. To avoid port conflicts, we pop a new port from the prepared port list each time we need to initialize a new process group related to data parallelism.

## Source code in `vllm/config/parallel.py`


###

`reconfigure_for_independent_dp_rank()`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.reconfigure_for_independent_dp_rank)

Reconfigure for a single independent non-MoE DP rank.

## Source code in `vllm/config/parallel.py`


###

`set_dcp_defaults(comm_backend='ag_rs', q_replicate=False)`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.set_dcp_defaults)

Fill in the DCP options the user left unset.

Models can set their preferred DCP settings by calling this from their `verify_and_update_config`

hook.

## Source code in `vllm/config/parallel.py`


###

`sync_dp_state(dp_group, has_unfinished, pending_pause)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.config.ParallelConfig.sync_dp_state)

Combined all-reduce for DP state synchronization.

## Uses a single SUM all-reduce on a 2-element tensor

[0] = 1 if this rank has unfinished work, else 0. SUM > 0 ≡ logical OR across ranks → any rank has work. [1] = 1 if this rank has a pending pause request, else 0. SUM == dp_size ≡ all ranks reached pause consensus.

has_unfinished_global is true if any rank has unfinished work, or if some ranks are waiting for a pause consensus.

Returns:

## Source code in `vllm/config/parallel.py`


##

`PassConfig`

[¶](https://docs.vllm.ai#vllm.config.PassConfig)

Configuration for custom Inductor passes.

This is separate from general `CompilationConfig`

so that inductor passes don't all have access to full configuration - that would create a cycle as the `PassManager`

is set as a property of config.

You must pass PassConfig to VLLMConfig constructor via the CompilationConfig constructor. VLLMConfig's post_init does further initialization. If used outside of the VLLMConfig, some fields may be left in an improper state.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.PassConfig.compute_hash)Produces a hash unique to the pass configuration.

-
–[flashinfer_max_size](https://docs.vllm.ai#vllm.config.PassConfig.flashinfer_max_size)Returns the max communication size in bytes for flashinfer

-
–[log_enabled_passes](https://docs.vllm.ai#vllm.config.PassConfig.log_enabled_passes)Log the enabled custom fusion passes.


Attributes:

-
([eliminate_noops](https://docs.vllm.ai#vllm.config.PassConfig.eliminate_noops)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Eliminate no-op ops.

-
([enable_qk_norm_rope_fusion](https://docs.vllm.ai#vllm.config.PassConfig.enable_qk_norm_rope_fusion)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable fused Q/K RMSNorm + RoPE pass.

-
([enable_sp](https://docs.vllm.ai#vllm.config.PassConfig.enable_sp)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable sequence parallelism. Requires TP>1. Automatically disabled

-
([fi_allreduce_fusion_max_size_mb](https://docs.vllm.ai#vllm.config.PassConfig.fi_allreduce_fusion_max_size_mb)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NoneThe threshold of the communicated tensor sizes under which

-
([fuse_act_padding](https://docs.vllm.ai#vllm.config.PassConfig.fuse_act_padding)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Fuse the custom RMSNorm + padding ops.

-
([fuse_act_quant](https://docs.vllm.ai#vllm.config.PassConfig.fuse_act_quant)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Fuse the custom SiluMul + quant ops.

-
([fuse_allreduce_rms](https://docs.vllm.ai#vllm.config.PassConfig.fuse_allreduce_rms)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable flashinfer allreduce fusion.

-
([fuse_attn_quant](https://docs.vllm.ai#vllm.config.PassConfig.fuse_attn_quant)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Fuse the custom Attention and MLAAttention + quant ops.

-
([fuse_gemm_comms](https://docs.vllm.ai#vllm.config.PassConfig.fuse_gemm_comms)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable async TP.

-
([fuse_mla_dual_rms_norm](https://docs.vllm.ai#vllm.config.PassConfig.fuse_mla_dual_rms_norm)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Fuse paired q/kv RMS norms in MLA attention.

-
([fuse_norm_quant](https://docs.vllm.ai#vllm.config.PassConfig.fuse_norm_quant)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Fuse the custom RMSNorm + quant ops.

-
([fuse_qk_norm_rope_kvcache](https://docs.vllm.ai#vllm.config.PassConfig.fuse_qk_norm_rope_kvcache)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Fuse QK RMSNorm + RoPE + KV cache update into a single AITER HIP

-
([fuse_rope_kvcache](https://docs.vllm.ai#vllm.config.PassConfig.fuse_rope_kvcache)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Fuse the QK rope + KV cache ops.

-
([fuse_rope_kvcache_cat_mla](https://docs.vllm.ai#vllm.config.PassConfig.fuse_rope_kvcache_cat_mla)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable fused MLA KV cache update with RoPE.

-
([rope_kvcache_fusion_max_token_num](https://docs.vllm.ai#vllm.config.PassConfig.rope_kvcache_fusion_max_token_num)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The threshold for ROCm AITER RoPE+KVCache fusion e.g. for small batch decode.

-
([sp_min_token_num](https://docs.vllm.ai#vllm.config.PassConfig.sp_min_token_num)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneThe minimum number of tokens above which vllm should use


## Source code in `vllm/config/compilation.py`


|
|

###

`eliminate_noops = Field(default=True)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PassConfig.eliminate_noops)

Eliminate no-op ops.

###

`enable_qk_norm_rope_fusion = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PassConfig.enable_qk_norm_rope_fusion)

Enable fused Q/K RMSNorm + RoPE pass.

###

`enable_sp = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PassConfig.enable_sp)

Enable sequence parallelism. Requires TP>1. Automatically disabled if the model's hidden_size is too small for SP to be beneficial (threshold is device-capability dependent).

###

`fi_allreduce_fusion_max_size_mb = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PassConfig.fi_allreduce_fusion_max_size_mb)

The threshold of the communicated tensor sizes under which vllm should use flashinfer fused allreduce. Specified as a float in MB. Unspecified will fallback to default values which are compute capability and world size dependent. FI_ALLREDUCE_FUSION_MAX_SIZE_MB = { 90: { 2: 64, # 64MB 4: 2, # 2MB 8: 1, # 1MB }, 100: { 2: 64, # 64MB 4: 32, # 32MB 8: 1, # 1MB }, }, where key is the device capability

###

`fuse_act_padding = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PassConfig.fuse_act_padding)

Fuse the custom RMSNorm + padding ops.

###

`fuse_act_quant = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PassConfig.fuse_act_quant)

Fuse the custom SiluMul + quant ops.

###

`fuse_allreduce_rms = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PassConfig.fuse_allreduce_rms)

Enable flashinfer allreduce fusion.

###

`fuse_attn_quant = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PassConfig.fuse_attn_quant)

Fuse the custom Attention and MLAAttention + quant ops.

###

`fuse_gemm_comms = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PassConfig.fuse_gemm_comms)

Enable async TP.

###

`fuse_mla_dual_rms_norm = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PassConfig.fuse_mla_dual_rms_norm)

Fuse paired q/kv RMS norms in MLA attention.

###

`fuse_norm_quant = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PassConfig.fuse_norm_quant)

Fuse the custom RMSNorm + quant ops.

###

`fuse_qk_norm_rope_kvcache = Field(default=None)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PassConfig.fuse_qk_norm_rope_kvcache)

Fuse QK RMSNorm + RoPE + KV cache update into a single AITER HIP kernel. Supersedes both enable_qk_norm_rope_fusion and fuse_rope_kvcache for layers that support it. Auto-enabled at O1+ on ROCm for models with QK-norm (e.g. Qwen3-MoE).

###

`fuse_rope_kvcache = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PassConfig.fuse_rope_kvcache)

Fuse the QK rope + KV cache ops.

###

`fuse_rope_kvcache_cat_mla = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PassConfig.fuse_rope_kvcache_cat_mla)

Enable fused MLA KV cache update with RoPE.

###

`rope_kvcache_fusion_max_token_num = 256`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PassConfig.rope_kvcache_fusion_max_token_num)

The threshold for ROCm AITER RoPE+KVCache fusion e.g. for small batch decode. Larger batch sizes e.g. during prefill will use the unfused kernels. Also applies to the fused QK-Norm+RoPE+KVCache pass.

###

`sp_min_token_num = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PassConfig.sp_min_token_num)

The minimum number of tokens above which vllm should use sequence parallelism. Specified as an integer token count. Unspecified will fallback to default values which are compute capability and world size dependent.

###

`_skip_none_validation(value, handler)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.PassConfig._skip_none_validation)

Skip validation if the value is `None`

when initialisation is delayed.

## Source code in `vllm/config/compilation.py`


###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.PassConfig.compute_hash)

Produces a hash unique to the pass configuration. Any new fields that affect compilation should be added to the hash. Any future fields that don't affect compilation should be excluded.

## Source code in `vllm/config/compilation.py`


###

`flashinfer_max_size(world_size)`

[¶](https://docs.vllm.ai#vllm.config.PassConfig.flashinfer_max_size)

Returns the max communication size in bytes for flashinfer allreduce fusion for the given world size. Returns None if world size is not supported by configs as it's not supported by flashinfer.

## Source code in `vllm/config/compilation.py`


###

`log_enabled_passes()`

[¶](https://docs.vllm.ai#vllm.config.PassConfig.log_enabled_passes)

Log the enabled custom fusion passes. This is called at the end of VLLMConfig post_init, after all defaults are finalized. TODO also log the compile ranges for which this is enabled.

## Source code in `vllm/config/compilation.py`


##

`PoolerConfig`

[¶](https://docs.vllm.ai#vllm.config.PoolerConfig)

Controls the behavior of output pooling in pooling models.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.PoolerConfig.compute_hash)WARNING: Whenever a new field is added to this config,


Attributes:

-
([dimensions](https://docs.vllm.ai#vllm.config.PoolerConfig.dimensions)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneReduce the dimensions of embeddings if model

-
([enable_chunked_processing](https://docs.vllm.ai#vllm.config.PoolerConfig.enable_chunked_processing)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to enable chunked processing for long inputs that exceed the model's

-
([logit_mean](https://docs.vllm.ai#vllm.config.PoolerConfig.logit_mean)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NoneIf provided, subtract this value from classification logits before

-
([logit_sigma](https://docs.vllm.ai#vllm.config.PoolerConfig.logit_sigma)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NoneIf provided, divide the classification logits by this value after

-
([max_embed_len](https://docs.vllm.ai#vllm.config.PoolerConfig.max_embed_len)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMaximum input length allowed for embedding generation. When set, allows

-
([pooling_type](https://docs.vllm.ai#vllm.config.PoolerConfig.pooling_type)`SequencePoolingType | TokenPoolingType | None`

) –The pooling method used for pooling.

-
([returned_token_ids](https://docs.vllm.ai#vllm.config.PoolerConfig.returned_token_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | NoneA list of indices for the vocabulary dimensions to be extracted,

-
([seq_pooling_type](https://docs.vllm.ai#vllm.config.PoolerConfig.seq_pooling_type)`SequencePoolingType | None`

) –The pooling method used for sequence pooling.

-
([step_tag_id](https://docs.vllm.ai#vllm.config.PoolerConfig.step_tag_id)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneIf set, only the score corresponding to the

`step_tag_id`

in the -
([task](https://docs.vllm.ai#vllm.config.PoolerConfig.task)`PoolingTask | None`

) –The task used for pooling.

-
([tok_pooling_type](https://docs.vllm.ai#vllm.config.PoolerConfig.tok_pooling_type)`TokenPoolingType | None`

) –The pooling method used for tokenwise pooling.

-
([use_activation](https://docs.vllm.ai#vllm.config.PoolerConfig.use_activation)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneWhether to apply activation function to the pooler outputs.


## Source code in `vllm/config/pooler.py`


|
|

###

`dimensions = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PoolerConfig.dimensions)

Reduce the dimensions of embeddings if model support matryoshka representation. Defaults to None.

###

`enable_chunked_processing = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PoolerConfig.enable_chunked_processing)

Whether to enable chunked processing for long inputs that exceed the model's maximum position embeddings. When enabled, long inputs will be split into chunks, processed separately, and then aggregated using weighted averaging. This allows embedding models to handle arbitrarily long text without CUDA errors. Defaults to False.

###

`logit_mean = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PoolerConfig.logit_mean)

If provided, subtract this value from classification logits before activation. Used for affine score calibration (Platt scaling): activation((logit - logit_mean) / logit_sigma). Defaults to None.

###

`logit_sigma = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PoolerConfig.logit_sigma)

If provided, divide the classification logits by this value after mean subtraction. Used for affine score calibration (Platt scaling): activation((logit - logit_mean) / logit_sigma). Defaults to None.

###

`max_embed_len = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PoolerConfig.max_embed_len)

Maximum input length allowed for embedding generation. When set, allows inputs longer than max_embed_len to be accepted for embedding models. When an input exceeds max_embed_len, it will be handled according to the original max_model_len validation logic. Defaults to None (i.e. set to max_model_len).

###

`pooling_type = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PoolerConfig.pooling_type)

The pooling method used for pooling.

If set, `seq_pooling_type`

or `tok_pooling_type`

are automatically populated with this field. Alternatively, users can set `seq_pooling_type`

and `tok_pooling_type`

explicitly.

This field is mainly for user convenience. Internal code should always use `seq_pooling_type`

or `tok_pooling_type`

instead of `pooling_type`

.

###

`returned_token_ids = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PoolerConfig.returned_token_ids)

A list of indices for the vocabulary dimensions to be extracted, such as the token IDs of `good_token`

and `bad_token`

in the `math-shepherd-mistral-7b-prm`

model.

###

`seq_pooling_type = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PoolerConfig.seq_pooling_type)

The pooling method used for sequence pooling.

###

`step_tag_id = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PoolerConfig.step_tag_id)

If set, only the score corresponding to the `step_tag_id`

in the generated sentence should be returned. Otherwise, the scores for all tokens are returned.

###

`task = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PoolerConfig.task)

The task used for pooling.

###

`tok_pooling_type = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PoolerConfig.tok_pooling_type)

The pooling method used for tokenwise pooling.

###

`use_activation = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PoolerConfig.use_activation)

Whether to apply activation function to the pooler outputs. `None`

uses the pooler's default, which is `True`

in most cases.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.PoolerConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

## Source code in `vllm/config/pooler.py`


##

`PrefetchOffloadConfig`

[¶](https://docs.vllm.ai#vllm.config.PrefetchOffloadConfig)

Configuration for prefetch-based CPU offloading.

Groups layers and uses async H2D prefetch to hide transfer latency.

Attributes:

-
([offload_group_size](https://docs.vllm.ai#vllm.config.PrefetchOffloadConfig.offload_group_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Group every N layers together. Offload last

`offload_num_in_group`

-
([offload_num_in_group](https://docs.vllm.ai#vllm.config.PrefetchOffloadConfig.offload_num_in_group)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of layers to offload per group.

-
([offload_params](https://docs.vllm.ai#vllm.config.PrefetchOffloadConfig.offload_params)

) –[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The set of parameter name segments to target for prefetch offloading.

-
([offload_prefetch_step](https://docs.vllm.ai#vllm.config.PrefetchOffloadConfig.offload_prefetch_step)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of layers to prefetch ahead.


## Source code in `vllm/config/offload.py`


###

`offload_group_size = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PrefetchOffloadConfig.offload_group_size)

Group every N layers together. Offload last `offload_num_in_group`

layers of each group. Default is 0 (disabled). Example: group_size=8, num_in_group=2 offloads layers 6,7,14,15,22,23,... Unlike cpu_offload_gb, this uses explicit async prefetching to hide transfer latency.

###

`offload_num_in_group = Field(default=1, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PrefetchOffloadConfig.offload_num_in_group)

Number of layers to offload per group. Must be <= offload_group_size. Default is 1.

###

`offload_params = Field(default_factory=set)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PrefetchOffloadConfig.offload_params)

The set of parameter name segments to target for prefetch offloading. Unmatched parameters are not offloaded. If this set is empty, ALL parameters of each offloaded layer are offloaded. Uses segment matching: "w13_weight" matches "mlp.experts.w13_weight" but not "mlp.experts.w13_weight_scale".

###

`offload_prefetch_step = Field(default=1, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.PrefetchOffloadConfig.offload_prefetch_step)

Number of layers to prefetch ahead. Higher values hide more latency but use more GPU memory. Default is 1.

##

`ProfilerConfig`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig)

Dataclass which contains profiler config for the engine.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.ProfilerConfig.compute_hash)WARNING: Whenever a new field is added to this config,


Attributes:

-
([active_iterations](https://docs.vllm.ai#vllm.config.ProfilerConfig.active_iterations)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of active iterations for PyTorch profiler schedule.

-
([capture_torch_profiler](https://docs.vllm.ai#vllm.config.ProfilerConfig.capture_torch_profiler)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, enables a torch profiler during CUDA graph capture on rank 0. -
([delay_iterations](https://docs.vllm.ai#vllm.config.ProfilerConfig.delay_iterations)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of engine iterations to skip before starting profiling.

-
([detailed_trace_annotation](https://docs.vllm.ai#vllm.config.ProfilerConfig.detailed_trace_annotation)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, uses detailed annotations with roofline metrics (sk, sqsq, -
([ignore_frontend](https://docs.vllm.ai#vllm.config.ProfilerConfig.ignore_frontend)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, disables the front-end profiling of AsyncLLM when using the -
([max_iterations](https://docs.vllm.ai#vllm.config.ProfilerConfig.max_iterations)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum number of engine iterations to profile after starting profiling.

-
([profiler](https://docs.vllm.ai#vllm.config.ProfilerConfig.profiler)`ProfilerKind | None`

) –Which profiler to use. Defaults to None. Options are:

-
([proton_backend](https://docs.vllm.ai#vllm.config.ProfilerConfig.proton_backend)`ProtonBackend | None`

) –Proton GPU backend.

`None`

lets Proton select CUPTI automatically. -
([proton_context](https://docs.vllm.ai#vllm.config.ProfilerConfig.proton_context)`ProtonContext`

) –Proton context source.

`shadow`

records explicit scopes with low -
([proton_data](https://docs.vllm.ai#vllm.config.ProfilerConfig.proton_data)`ProtonData`

) –Proton output type.

`tree`

produces Hatchet data and`trace`

-
([proton_graph_attribution](https://docs.vllm.ai#vllm.config.ProfilerConfig.proton_graph_attribution)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Observe CUDA graph capture so replayed kernels can be attributed.

-
([proton_hook](https://docs.vllm.ai#vllm.config.ProfilerConfig.proton_hook)`ProtonHook | None`

) –Optional Proton hook. Use

`triton`

to add Triton launch metadata. -
([proton_mode](https://docs.vllm.ai#vllm.config.ProfilerConfig.proton_mode)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneOptional backend-specific Proton mode string, such as

`pcsampling`

. -
([proton_output_format](https://docs.vllm.ai#vllm.config.ProfilerConfig.proton_output_format)`ProtonOutputFormat | None`

) –Optional format passed to Proton when finalizing a profile.

`None`

-
([proton_profiler_dir](https://docs.vllm.ai#vllm.config.ProfilerConfig.proton_profiler_dir)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Directory to save Triton Proton profiles. Each worker writes a

-
([torch_profiler_activities](https://docs.vllm.ai#vllm.config.ProfilerConfig.torch_profiler_activities)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[TorchProfilerActivity] | NoneActivities recorded by workers using the torch profiler. When unset,

-
([torch_profiler_dir](https://docs.vllm.ai#vllm.config.ProfilerConfig.torch_profiler_dir)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Directory to save torch profiler traces. Both AsyncLLM's CPU traces and

-
([torch_profiler_dump_cuda_time_total](https://docs.vllm.ai#vllm.config.ProfilerConfig.torch_profiler_dump_cuda_time_total)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, dumps total CUDA time in torch profiler traces. Enabled by default. -
([torch_profiler_record_shapes](https://docs.vllm.ai#vllm.config.ProfilerConfig.torch_profiler_record_shapes)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, records tensor shapes in the torch profiler. Disabled by default. -
([torch_profiler_use_gzip](https://docs.vllm.ai#vllm.config.ProfilerConfig.torch_profiler_use_gzip)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, saves torch profiler traces in gzip format. Enabled by default -
([torch_profiler_with_flops](https://docs.vllm.ai#vllm.config.ProfilerConfig.torch_profiler_with_flops)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, enables FLOPS counting in the torch profiler. Disabled by default. -
([torch_profiler_with_memory](https://docs.vllm.ai#vllm.config.ProfilerConfig.torch_profiler_with_memory)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, enables memory profiling in the torch profiler. -
([torch_profiler_with_stack](https://docs.vllm.ai#vllm.config.ProfilerConfig.torch_profiler_with_stack)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, enables stack tracing in the torch profiler. Enabled by default -
([wait_iterations](https://docs.vllm.ai#vllm.config.ProfilerConfig.wait_iterations)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of wait iterations for PyTorch profiler schedule.

-
([warmup_iterations](https://docs.vllm.ai#vllm.config.ProfilerConfig.warmup_iterations)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of warmup iterations for PyTorch profiler schedule.


## Source code in `vllm/config/profiler.py`


|
|

###

`active_iterations = Field(default=5, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.active_iterations)

Number of active iterations for PyTorch profiler schedule. This is the number of iterations where profiling data is actually collected. Defaults to 5 active iterations.

###

`capture_torch_profiler = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.capture_torch_profiler)

If `True`

, enables a torch profiler during CUDA graph capture on rank 0. Traces are saved to a `capture_traces`

subdirectory under `torch_profiler_dir`

. Requires `profiler`

to be set to 'torch'.

###

`delay_iterations = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.delay_iterations)

Number of engine iterations to skip before starting profiling. Defaults to 0, meaning profiling starts immediately after receiving /start_profile.

###

`detailed_trace_annotation = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.detailed_trace_annotation)

If `True`

, uses detailed annotations with roofline metrics (sk, sqsq, sqsk) in profiler trace events. If `False`

, uses simple annotations with only context/generation request counts and token counts. Disabled by default.

###

`ignore_frontend = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.ignore_frontend)

If `True`

, disables the front-end profiling of AsyncLLM when using the 'torch' profiler. This is needed to reduce overhead when using delay/limit options, since the front-end profiling does not track iterations and will capture the entire range.

###

`max_iterations = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.max_iterations)

Maximum number of engine iterations to profile after starting profiling. Defaults to 0, meaning no limit.

###

`profiler = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.profiler)

Which profiler to use. Defaults to None. Options are:

- 'torch': Use PyTorch profiler.
- 'cuda': Use CUDA profiler.
- 'proton': Use Triton Proton profiler.

###

`proton_backend = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.proton_backend)

Proton GPU backend. `None`

lets Proton select CUPTI automatically.

###

`proton_context = 'shadow'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.proton_context)

Proton context source. `shadow`

records explicit scopes with low overhead; `python`

records Python call stacks.

###

`proton_data = 'tree'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.proton_data)

Proton output type. `tree`

produces Hatchet data and `trace`

produces a Chrome trace.

###

`proton_graph_attribution = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.proton_graph_attribution)

Observe CUDA graph capture so replayed kernels can be attributed. Requires Triton >= 3.7 and `proton_data='tree'`

.

###

`proton_hook = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.proton_hook)

Optional Proton hook. Use `triton`

to add Triton launch metadata.

###

`proton_mode = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.proton_mode)

Optional backend-specific Proton mode string, such as `pcsampling`

.

###

`proton_output_format = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.proton_output_format)

Optional format passed to Proton when finalizing a profile. `None`

uses the default format for `proton_data`

.

###

`proton_profiler_dir = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.proton_profiler_dir)

Directory to save Triton Proton profiles. Each worker writes a separate rank-qualified file.

###

`torch_profiler_activities = Field(default=None, min_length=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.torch_profiler_activities)

Activities recorded by workers using the torch profiler. When unset, each worker uses its platform default: CPU; CPU and CUDA; or CPU and XPU.

###

`torch_profiler_dir = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.torch_profiler_dir)

Directory to save torch profiler traces. Both AsyncLLM's CPU traces and worker's traces (CPU & GPU) will be saved under this directory. Note that it must be an absolute path.

###

`torch_profiler_dump_cuda_time_total = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.torch_profiler_dump_cuda_time_total)

If `True`

, dumps total CUDA time in torch profiler traces. Enabled by default.

###

`torch_profiler_record_shapes = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.torch_profiler_record_shapes)

If `True`

, records tensor shapes in the torch profiler. Disabled by default.

###

`torch_profiler_use_gzip = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.torch_profiler_use_gzip)

If `True`

, saves torch profiler traces in gzip format. Enabled by default

###

`torch_profiler_with_flops = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.torch_profiler_with_flops)

If `True`

, enables FLOPS counting in the torch profiler. Disabled by default.

###

`torch_profiler_with_memory = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.torch_profiler_with_memory)

If `True`

, enables memory profiling in the torch profiler. Disabled by default.

###

`torch_profiler_with_stack = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.torch_profiler_with_stack)

If `True`

, enables stack tracing in the torch profiler. Enabled by default as it is useful for debugging. Can be disabled via --profiler-config.torch_profiler_with_stack=false CLI flag.

###

`wait_iterations = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.wait_iterations)

Number of wait iterations for PyTorch profiler schedule. During wait, the profiler is completely off with zero overhead. This allows skipping initial iterations before warmup begins. Defaults to 0 (no wait period).

###

`warmup_iterations = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.warmup_iterations)

Number of warmup iterations for PyTorch profiler schedule. During warmup, the profiler runs but data is discarded. This helps reduce noise from JIT compilation and other one-time costs in the profiled trace. Defaults to 0 (schedule-based profiling disabled, recording all iterations). Set to a positive value (e.g., 2) to enable schedule-based profiling.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.ProfilerConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

## Source code in `vllm/config/profiler.py`


##

`ReasoningConfig`

[¶](https://docs.vllm.ai#vllm.config.ReasoningConfig)

Configuration for reasoning models.

Set `reasoning_start_str`

and `reasoning_end_str`

to the strings used to enter and forcibly terminate reasoning. The end string may include a transition phrase before the parser's natural reasoning end marker. Token IDs are derived automatically by `initialize_token_ids`

.

Methods:

-
–[initialize_token_ids](https://docs.vllm.ai#vllm.config.ReasoningConfig.initialize_token_ids)Initialize reasoning token IDs from strings using the tokenizer.


Attributes:

-
([enabled](https://docs.vllm.ai#vllm.config.ReasoningConfig.enabled)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Returns True if reasoning is enabled (i.e. if token IDs have been

-
([natural_reasoning_end_token_ids](https://docs.vllm.ai#vllm.config.ReasoningConfig.natural_reasoning_end_token_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | NoneToken IDs that indicate the model naturally ended reasoning.

-
([reasoning_end_str](https://docs.vllm.ai#vllm.config.ReasoningConfig.reasoning_end_str)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)String forced when the thinking budget is exhausted.

-
([reasoning_end_token_ids](https://docs.vllm.ai#vllm.config.ReasoningConfig.reasoning_end_token_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | NoneToken IDs forced when the thinking budget is exhausted.

-
([reasoning_parser](https://docs.vllm.ai#vllm.config.ReasoningConfig.reasoning_parser)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The name of the ReasoningParser to use for this model.

-
([reasoning_start_str](https://docs.vllm.ai#vllm.config.ReasoningConfig.reasoning_start_str)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)String that indicates the start of reasoning.

-
([reasoning_start_token_ids](https://docs.vllm.ai#vllm.config.ReasoningConfig.reasoning_start_token_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | NoneToken IDs derived from

`reasoning_start_str`

. Set automatically by

## Source code in `vllm/config/reasoning.py`


|
|

###

`_enabled = field(default=False, init=False, repr=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ReasoningConfig._enabled)

Private field indicating whether reasoning token IDs have been initialized. Set to True by `initialize_token_ids`

once token IDs are initialized.

###

`_natural_reasoning_end_token_ids = field(default=None, init=False, repr=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ReasoningConfig._natural_reasoning_end_token_ids)

Token IDs that naturally terminate reasoning, as defined by the parser.

###

`_reasoning_end_token_ids = field(default=None, init=False, repr=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ReasoningConfig._reasoning_end_token_ids)

Private backing field for forced reasoning end token IDs.

###

`_reasoning_start_token_ids = field(default=None, init=False, repr=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ReasoningConfig._reasoning_start_token_ids)

Private backing field for `reasoning_start_token_ids`

. Set by `initialize_token_ids`

. Not intended to be configured directly.

###

`enabled`

`property`

[¶](https://docs.vllm.ai#vllm.config.ReasoningConfig.enabled)

Returns True if reasoning is enabled (i.e. if token IDs have been initialized), False otherwise.

###

`natural_reasoning_end_token_ids`

`property`

[¶](https://docs.vllm.ai#vllm.config.ReasoningConfig.natural_reasoning_end_token_ids)

Token IDs that indicate the model naturally ended reasoning.

###

`reasoning_end_str = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ReasoningConfig.reasoning_end_str)

String forced when the thinking budget is exhausted.

###

`reasoning_end_token_ids`

`property`

[¶](https://docs.vllm.ai#vllm.config.ReasoningConfig.reasoning_end_token_ids)

Token IDs forced when the thinking budget is exhausted.

###

`reasoning_parser = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ReasoningConfig.reasoning_parser)

The name of the ReasoningParser to use for this model.

###

`reasoning_start_str = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.ReasoningConfig.reasoning_start_str)

String that indicates the start of reasoning.

###

`reasoning_start_token_ids`

`property`

[¶](https://docs.vllm.ai#vllm.config.ReasoningConfig.reasoning_start_token_ids)

Token IDs derived from `reasoning_start_str`

. Set automatically by `initialize_token_ids`

. Not intended to be configured directly.

###

`initialize_token_ids(model_config)`

[¶](https://docs.vllm.ai#vllm.config.ReasoningConfig.initialize_token_ids)

Initialize reasoning token IDs from strings using the tokenizer.

## Source code in `vllm/config/reasoning.py`


##

`SchedulerConfig`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig)

Scheduler configuration.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.SchedulerConfig.compute_hash)WARNING: Whenever a new field is added to this config,

-
–[default_factory](https://docs.vllm.ai#vllm.config.SchedulerConfig.default_factory)Create a

`SchedulerConfig`

with default values for its`InitVar`

s.

Attributes:

-
([async_scheduling](https://docs.vllm.ai#vllm.config.SchedulerConfig.async_scheduling)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneIf set to False, disable async scheduling. Async scheduling helps to

-
([disable_chunked_mm_input](https://docs.vllm.ai#vllm.config.SchedulerConfig.disable_chunked_mm_input)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If set to true and chunked prefill is enabled, we do not want to

-
([disable_hybrid_kv_cache_manager](https://docs.vllm.ai#vllm.config.SchedulerConfig.disable_hybrid_kv_cache_manager)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneIf set to True, KV cache manager will allocate the same size of KV cache

-
([enable_chunked_prefill](https://docs.vllm.ai#vllm.config.SchedulerConfig.enable_chunked_prefill)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If True, prefill requests can be chunked based

-
([encoder_cache_size](https://docs.vllm.ai#vllm.config.SchedulerConfig.encoder_cache_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Multimodal encoder cache size, only used in V1.

-
([is_multimodal_model](https://docs.vllm.ai#vllm.config.SchedulerConfig.is_multimodal_model)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)True if the model is multimodal.

-
([long_prefill_token_threshold](https://docs.vllm.ai#vllm.config.SchedulerConfig.long_prefill_token_threshold)

) –[int](https://docs.python.org/3/builtins/functions.html#int)For chunked prefill, a request is considered long if the prompt is

-
([max_num_active_seqs](https://docs.vllm.ai#vllm.config.SchedulerConfig.max_num_active_seqs)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMaximum number of requests the scheduler admits into RUNNING.

-
([max_num_batched_tokens](https://docs.vllm.ai#vllm.config.SchedulerConfig.max_num_batched_tokens)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum number of tokens that can be processed in a single iteration.

-
([max_num_encoder_input_tokens](https://docs.vllm.ai#vllm.config.SchedulerConfig.max_num_encoder_input_tokens)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Multimodal encoder compute budget, only used in V1.

-
([max_num_queued_reqs](https://docs.vllm.ai#vllm.config.SchedulerConfig.max_num_queued_reqs)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMaximum number of requests that can be in-flight (waiting or running)

-
([max_num_queued_tokens](https://docs.vllm.ai#vllm.config.SchedulerConfig.max_num_queued_tokens)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMaximum total prompt tokens of requests currently in the prefill

-
([max_num_scheduled_tokens](https://docs.vllm.ai#vllm.config.SchedulerConfig.max_num_scheduled_tokens)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMaximum number of tokens that the scheduler may issue in a single iteration.

-
([max_num_seqs](https://docs.vllm.ai#vllm.config.SchedulerConfig.max_num_seqs)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum number of sequences to be processed in a single iteration.

-
([policy](https://docs.vllm.ai#vllm.config.SchedulerConfig.policy)`SchedulerPolicy`

) –The scheduling policy to use:

-
([prefill_schedule_interval](https://docs.vllm.ai#vllm.config.SchedulerConfig.prefill_schedule_interval)

) –[int](https://docs.python.org/3/builtins/functions.html#int)For data-parallel deployments, only admit new prefill requests

-
([runner_type](https://docs.vllm.ai#vllm.config.SchedulerConfig.runner_type)`RunnerType`

) –The runner type to launch for the model.

-
([scheduler_cls](https://docs.vllm.ai#vllm.config.SchedulerConfig.scheduler_cls)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)|[type](https://docs.python.org/3/builtins/functions.html#type)[[object](https://docs.python.org/3/builtins/functions.html#object)] | NoneThe scheduler class to use. "vllm.v1.core.sched.scheduler.Scheduler" is

-
([scheduler_reserve_full_isl](https://docs.vllm.ai#vllm.config.SchedulerConfig.scheduler_reserve_full_isl)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If True, the scheduler checks whether the full input sequence length

-
([stream_interval](https://docs.vllm.ai#vllm.config.SchedulerConfig.stream_interval)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The interval (or buffer size) for streaming in terms of token length.

-
([watermark](https://docs.vllm.ai#vllm.config.SchedulerConfig.watermark)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Fraction of total KV cache blocks to keep free (the watermark) when


## Source code in `vllm/config/scheduler.py`


|
|

###

`async_scheduling = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig.async_scheduling)

If set to False, disable async scheduling. Async scheduling helps to avoid gaps in GPU utilization, leading to better latency and throughput.

###

`disable_chunked_mm_input = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig.disable_chunked_mm_input)

If set to true and chunked prefill is enabled, we do not want to partially schedule a multimodal item. Only used in V1 This ensures that if a request has a mixed prompt (like text tokens TTTT followed by image tokens IIIIIIIIII) where only some image tokens can be scheduled (like TTTTIIIII, leaving IIIII), it will be scheduled as TTTT in one step and IIIIIIIIII in the next.

###

`disable_hybrid_kv_cache_manager = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig.disable_hybrid_kv_cache_manager)

If set to True, KV cache manager will allocate the same size of KV cache for all attention layers even if there are multiple type of attention layers like full attention and sliding window attention. If set to None, the default value will be determined based on the environment and starting configuration.

###

`enable_chunked_prefill = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig.enable_chunked_prefill)

If True, prefill requests can be chunked based on the remaining `max_num_batched_tokens`

.

The default value here is mainly for convenience when testing. In real usage, this should be set in `EngineArgs.create_engine_config`

.

###

`encoder_cache_size = Field(init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig.encoder_cache_size)

Multimodal encoder cache size, only used in V1.

NOTE: This is not currently configurable. It will be overridden by max_num_batched_tokens in case max multimodal embedding size is larger.

###

`is_multimodal_model = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig.is_multimodal_model)

True if the model is multimodal.

###

`long_prefill_token_threshold = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig.long_prefill_token_threshold)

For chunked prefill, a request is considered long if the prompt is longer than this number of tokens. 0 disables the cap (default).

The cap is not applied when the request is the only one in the batch, since there is no other request for it to starve.

###

`max_num_active_seqs = Field(default=None, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig.max_num_active_seqs)

Maximum number of requests the scheduler admits into RUNNING.

`max_num_seqs`

sizes the model runner (per-request buffers and CUDA graph capture) and is also the default admission limit. Setting this lowers only the number of requests that may occupy RUNNING, so decode batches stay smaller without shrinking runner or graph capacity. Must be `<= max_num_seqs`

. `None`

(default) keeps current behavior.

###

`max_num_batched_tokens = Field(default=DEFAULT_MAX_NUM_BATCHED_TOKENS, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig.max_num_batched_tokens)

Maximum number of tokens that can be processed in a single iteration.

The default value here is mainly for convenience when testing. In real usage, this should be set in `EngineArgs.create_engine_config`

.

###

`max_num_encoder_input_tokens = Field(init=False)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig.max_num_encoder_input_tokens)

Multimodal encoder compute budget, only used in V1.

NOTE: This is not currently configurable. It will be overridden by max_num_batched_tokens in case max multimodal embedding size is larger.

###

`max_num_queued_reqs = Field(default=None, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig.max_num_queued_reqs)

Maximum number of requests that can be in-flight (waiting or running) at the same time, or None for no limit. When the limit is reached, new requests are rejected with HTTP 503 so the client can retry on another instance. This bounds vLLM's otherwise unbounded request queue and is primarily a coarse capacity valve.

Unlike `max_num_seqs`

, which applies per data-parallel rank, this limit is enforced in the API server process and counts in-flight requests across all DP ranks it routes to. Size it as roughly `data_parallel_size * max_num_seqs`

plus the desired queue depth if it should not bind before per-rank admission does.

###

`max_num_queued_tokens = Field(default=None, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig.max_num_queued_tokens)

Maximum total prompt tokens of requests currently in the prefill phase, or None for no limit. When the limit is reached, new requests are rejected with HTTP 503.

This is a TTFT QoS mechanism: by setting it to `target_TTFT * prefill_throughput`

you reject requests when the prefill backlog would exceed the latency target. In a disaggregated prefill-decode setup this maps directly to the prefill pool's capacity.

Like `max_num_queued_reqs`

, this limit is enforced in the API server process and covers the prefill backlog across all DP ranks it routes to, so `prefill_throughput`

in the formula above is the aggregate throughput of the deployment.

Note: the count is conservative. A partially prefilled request still contributes its full `prompt_len`

until it transitions out of the prefill phase, because the scheduler's per-iteration `num_computed_tokens`

progress is not propagated to the API server process during prefill (`EngineCoreOutput`

is only emitted once the request starts producing tokens). Similarly, prefix-cache hits (`num_cached_tokens`

) are only known to the OutputProcessor after prefill completes. This overestimates the real backlog, causing earlier rejection than strictly necessary — the safe direction for QoS. The impact is limited to long prompts under chunked prefill; short prompts that prefill in a single iteration are unaffected.

###

`max_num_scheduled_tokens = Field(default=None, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig.max_num_scheduled_tokens)

Maximum number of tokens that the scheduler may issue in a single iteration.

This is usually equal to max_num_batched_tokens, but can be smaller in cases when the model might append tokens into the batch (such as speculative decoding). Defaults to max_num_batched_tokens.

###

`max_num_seqs = Field(default=DEFAULT_MAX_NUM_SEQS, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig.max_num_seqs)

Maximum number of sequences to be processed in a single iteration.

The default value here is mainly for convenience when testing. In real usage, this should be set in `EngineArgs.create_engine_config`

.

###

`policy = 'fcfs'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig.policy)

The scheduling policy to use:

- "fcfs" means first come first served, i.e. requests are handled in order of arrival.
- "priority" means requests are handled based on given priority (lower value means earlier handling) and time of arrival deciding any ties).

###

`prefill_schedule_interval = Field(default=1, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig.prefill_schedule_interval)

For data-parallel deployments, only admit new prefill requests once every N engine steps, aligned across DP ranks, to better balance per-step forward-pass times.

###

`runner_type = 'generate'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig.runner_type)

The runner type to launch for the model.

###

`scheduler_cls = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig.scheduler_cls)

The scheduler class to use. "vllm.v1.core.sched.scheduler.Scheduler" is the default scheduler. Can be a class directly or the path to a class of form "mod.custom_class".

###

`scheduler_reserve_full_isl = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig.scheduler_reserve_full_isl)

If True, the scheduler checks whether the full input sequence length fits in the KV cache before admitting a new request, rather than only checking the first chunk. Prevents over-admission and KV cache thrashing with chunked prefill.

###

`stream_interval = Field(default=1, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig.stream_interval)

The interval (or buffer size) for streaming in terms of token length. A smaller value (1) makes streaming smoother by sending each token immediately, while a larger value (e.g., 10) reduces host overhead and may increase throughput by batching multiple tokens before sending.

###

`watermark = Field(default=0.0, ge=0.0, lt=1.0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig.watermark)

Fraction of total KV cache blocks to keep free (the watermark) when admitting waiting or preempted requests into the running queue. This headroom helps avoid frequent KV cache eviction and the resulting repeated preemption of requests when GPU memory is scarce. Must be in the range [0.0, 1.0); 0.0 (the default) disables the watermark.

###

`_skip_none_validation(value, handler)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig._skip_none_validation)

Skip validation if the value is `None`

when initialisation is delayed.

## Source code in `vllm/config/scheduler.py`


###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

## Source code in `vllm/config/scheduler.py`


###

`default_factory(**kwargs)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.config.SchedulerConfig.default_factory)

Create a `SchedulerConfig`

with default values for its `InitVar`

s.

## Source code in `vllm/config/scheduler.py`


##

`SpeculativeConfig`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig)

Configuration for speculative decoding.

Methods:

-
–[apply_draft_overrides](https://docs.vllm.ai#vllm.config.SpeculativeConfig.apply_draft_overrides)Overlay this config's kernel overrides onto a target VllmConfig.

-
–[compose_draft_hf_overrides](https://docs.vllm.ai#vllm.config.SpeculativeConfig.compose_draft_hf_overrides)Build the

`hf_overrides`

for the draft`ModelConfig`

. -
–[compute_hash](https://docs.vllm.ai#vllm.config.SpeculativeConfig.compute_hash)WARNING: Whenever a new field is added to this config,

-
–[create_draft_parallel_config](https://docs.vllm.ai#vllm.config.SpeculativeConfig.create_draft_parallel_config)Create a parallel config for use by the draft worker.

-
–[update_arch_](https://docs.vllm.ai#vllm.config.SpeculativeConfig.update_arch_)EagleConfig and ExtractHiddenStatesConfig update architectures, so update all

-
–[use_eagle_block_drop](https://docs.vllm.ai#vllm.config.SpeculativeConfig.use_eagle_block_drop)Whether volatile trailing cache blocks should be discarded.


Attributes:

-
([attention_backend](https://docs.vllm.ai#vllm.config.SpeculativeConfig.attention_backend)

) –[AttentionBackendEnum](https://docs.vllm.ai/v1/attention/backends/registry/#vllm.v1.attention.backends.registry.AttentionBackendEnum)| NoneAttention backend to use for the draft model. When

`None`

, the backend is -
([code_revision](https://docs.vllm.ai#vllm.config.SpeculativeConfig.code_revision)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe specific revision to use for the draft model code on Hugging Face

-
([disable_eagle_block_drop](https://docs.vllm.ai#vllm.config.SpeculativeConfig.disable_eagle_block_drop)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Disable dropping the trailing prefix-cache block for EAGLE-like

-
([disable_padded_drafter_batch](https://docs.vllm.ai#vllm.config.SpeculativeConfig.disable_padded_drafter_batch)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Disable input padding for speculative decoding. If set to True,

-
([draft_load_config](https://docs.vllm.ai#vllm.config.SpeculativeConfig.draft_load_config)

) –[LoadConfig](https://docs.vllm.ai#vllm.config.LoadConfig)| NoneLoad config for the draft model. If not specified, will use the load

-
([draft_model_config](https://docs.vllm.ai#vllm.config.SpeculativeConfig.draft_model_config)`SkipValidation[`

) –[ModelConfig](https://docs.vllm.ai/model/#vllm.config.model.ModelConfig)]The configuration of the draft model initialized internal.

-
([draft_parallel_config](https://docs.vllm.ai#vllm.config.SpeculativeConfig.draft_parallel_config)`SkipValidation[`

) –[ParallelConfig](https://docs.vllm.ai/parallel/#vllm.config.parallel.ParallelConfig)]The parallel configuration for the draft model initialized internal.

-
([draft_sample_method](https://docs.vllm.ai#vllm.config.SpeculativeConfig.draft_sample_method)`DraftSampleMethod`

) –How the draft model samples tokens. 'greedy' always picks the argmax

-
([draft_tensor_parallel_size](https://docs.vllm.ai#vllm.config.SpeculativeConfig.draft_tensor_parallel_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneThe degree of the tensor parallelism for the draft model. Can only be 1

-
([dspark_draft_topk](https://docs.vllm.ai#vllm.config.SpeculativeConfig.dspark_draft_topk)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneFor Qwen3 DSpark drafting, evaluate the Markov projection only for the

-
([enable_adaptive_verification](https://docs.vllm.ai#vllm.config.SpeculativeConfig.enable_adaptive_verification)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to adaptively size the draft-verification budget from per-request

-
([enforce_eager](https://docs.vllm.ai#vllm.config.SpeculativeConfig.enforce_eager)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneOverride the default enforce_eager from model_config

-
([index_share_for_mtp_iteration](https://docs.vllm.ai#vllm.config.SpeculativeConfig.index_share_for_mtp_iteration)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneOverride whether MTP iterations reuse the first step's sparse indices.

-
([kv_cache_dtype](https://docs.vllm.ai#vllm.config.SpeculativeConfig.kv_cache_dtype)`CacheDType | None`

) –KV cache dtype for the draft model. When

`None`

, the draft inherits the -
([max_model_len](https://docs.vllm.ai#vllm.config.SpeculativeConfig.max_model_len)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneThe maximum model length of the draft model. Used when testing the

-
([max_num_new_slots_for_drafting](https://docs.vllm.ai#vllm.config.SpeculativeConfig.max_num_new_slots_for_drafting)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Return the maximum additional drafting slots per request.

-
([method](https://docs.vllm.ai#vllm.config.SpeculativeConfig.method)`SpeculativeMethod | None`

) –The name of the speculative method to use. If users provide and set the

-
([model](https://docs.vllm.ai#vllm.config.SpeculativeConfig.model)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe name of the draft model, eagle head, or additional weights, if

-
([moe_backend](https://docs.vllm.ai#vllm.config.SpeculativeConfig.moe_backend)`MoEBackend | None`

) –MoE backend to use for the draft model. When

`None`

, the draft model -
([num_speculative_tokens](https://docs.vllm.ai#vllm.config.SpeculativeConfig.num_speculative_tokens)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The number of speculative tokens, if provided. It will default to the

-
([num_speculative_tokens_per_batch_size](https://docs.vllm.ai#vllm.config.SpeculativeConfig.num_speculative_tokens_per_batch_size)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)]] | NoneBatch-size schedule used to dynamically choose speculative-token count.

-
([parallel_drafting](https://docs.vllm.ai#vllm.config.SpeculativeConfig.parallel_drafting)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable parallel drafting, where all speculative tokens are generated

-
([prompt_lookup_max](https://docs.vllm.ai#vllm.config.SpeculativeConfig.prompt_lookup_max)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMaximum size of ngram token window when using Ngram proposer, required

-
([prompt_lookup_min](https://docs.vllm.ai#vllm.config.SpeculativeConfig.prompt_lookup_min)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMinimum size of ngram token window when using Ngram proposer, if

-
([quantization](https://docs.vllm.ai#vllm.config.SpeculativeConfig.quantization)`QuantizationMethods |`

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneQuantization method that was used to quantize the draft model weights.

-
([rejection_sample_method](https://docs.vllm.ai#vllm.config.SpeculativeConfig.rejection_sample_method)`RejectionSampleMethod`

) –The rejection sampling method to use. 'standard' uses probabilistic

-
([revision](https://docs.vllm.ai#vllm.config.SpeculativeConfig.revision)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe specific model version to use for the draft model. It can be a

-
([suffix_decoding_max_cached_requests](https://docs.vllm.ai#vllm.config.SpeculativeConfig.suffix_decoding_max_cached_requests)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The maximum number of requests to cache in the global suffix tree. If

-
([suffix_decoding_max_spec_factor](https://docs.vllm.ai#vllm.config.SpeculativeConfig.suffix_decoding_max_spec_factor)

) –[float](https://docs.python.org/3/builtins/functions.html#float)The maximum spec factor for suffix decoding. The spec factor controls

-
([suffix_decoding_max_tree_depth](https://docs.vllm.ai#vllm.config.SpeculativeConfig.suffix_decoding_max_tree_depth)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The maximum depth of the suffix decoding global and prompt trees. The

-
([suffix_decoding_min_token_prob](https://docs.vllm.ai#vllm.config.SpeculativeConfig.suffix_decoding_min_token_prob)

) –[float](https://docs.python.org/3/builtins/functions.html#float)The minimum token probability for suffix decoding. Will only speculate

-
([synthetic_acceptance_length](https://docs.vllm.ai#vllm.config.SpeculativeConfig.synthetic_acceptance_length)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NoneTarget mean acceptance length for synthetic rejection sampling, in

-
([synthetic_acceptance_rates](https://docs.vllm.ai#vllm.config.SpeculativeConfig.synthetic_acceptance_rates)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[float](https://docs.python.org/3/builtins/functions.html#float)] | NonePer-position

*unconditional*acceptance rates for synthetic rejection -
([target_model_config](https://docs.vllm.ai#vllm.config.SpeculativeConfig.target_model_config)`SkipValidation[`

) –[ModelConfig](https://docs.vllm.ai/model/#vllm.config.model.ModelConfig)]The configuration of the target model.

-
([target_parallel_config](https://docs.vllm.ai#vllm.config.SpeculativeConfig.target_parallel_config)`SkipValidation[`

) –[ParallelConfig](https://docs.vllm.ai/parallel/#vllm.config.parallel.ParallelConfig)]The parallel configuration for the target model.

-
([tensor_parallel_size](https://docs.vllm.ai#vllm.config.SpeculativeConfig.tensor_parallel_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneUsers should pass "draft_tensor_parallel_size". This parameter's purpose is to

-
([use_heterogeneous_vocab](https://docs.vllm.ai#vllm.config.SpeculativeConfig.use_heterogeneous_vocab)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Allow draft and target models to use different vocabularies.

-
([use_local_argmax_reduction](https://docs.vllm.ai#vllm.config.SpeculativeConfig.use_local_argmax_reduction)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Use vocab-parallel local argmax instead of all-gathering full logits


## Source code in `vllm/config/speculative.py`


|
|

###

`attention_backend = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.attention_backend)

Attention backend to use for the draft model. When `None`

, the backend is automatically selected. Useful when the drafter requires a different attention backend (e.g. DFlash needs a backend that supports non-causal attention).

###

`code_revision = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.code_revision)

The specific revision to use for the draft model code on Hugging Face Hub. It can be a branch name, a tag name, or a commit id. If unspecified, will use the default version.

###

`disable_eagle_block_drop = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.disable_eagle_block_drop)

Disable dropping the trailing prefix-cache block for EAGLE-like speculative methods. This is an experimental option for measuring the acceptance-rate impact of reusing that block. It does not disable the speculative drafter itself.

###

`disable_padded_drafter_batch = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.disable_padded_drafter_batch)

Disable input padding for speculative decoding. If set to True, speculative input batches can contain sequences of different lengths, which may only be supported by certain attention backends. This currently only affects the EAGLE method of speculation.

###

`draft_load_config = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.draft_load_config)

Load config for the draft model. If not specified, will use the load config from the target model.

###

`draft_model_config = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.draft_model_config)

The configuration of the draft model initialized internal.

###

`draft_parallel_config = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.draft_parallel_config)

The parallel configuration for the draft model initialized internal.

###

`draft_sample_method = 'greedy'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.draft_sample_method)

How the draft model samples tokens. 'greedy' always picks the argmax token, and the draft probabilities are treated as one-hot during rejection sampling. 'probabilistic' samples stochastically from the draft distribution and uses the full draft logits for the probability ratio test during rejection sampling. This comes at the cost of additional GPU memory usage.

###

`draft_tensor_parallel_size = Field(default=None, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.draft_tensor_parallel_size)

The degree of the tensor parallelism for the draft model. Can only be 1 or the same as the target model's tensor parallel size.

###

`dspark_draft_topk = Field(default=None, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.dspark_draft_topk)

For Qwen3 DSpark drafting, evaluate the Markov projection only for the top-k base-logit candidates. Requires draft tensor parallel size 1.

###

`enable_adaptive_verification = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.enable_adaptive_verification)

Whether to adaptively size the draft-verification budget from per-request confidence. Currently only supported for method="dspark".

###

`enforce_eager = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.enforce_eager)

Override the default enforce_eager from model_config

###

`index_share_for_mtp_iteration = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.index_share_for_mtp_iteration)

Override whether MTP iterations reuse the first step's sparse indices. If `None`

, use the value from the draft model's Hugging Face config.

###

`kv_cache_dtype = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.kv_cache_dtype)

KV cache dtype for the draft model. When `None`

, the draft inherits the target model's `--kv-cache-dtype`

.

###

`max_model_len = Field(default=None, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.max_model_len)

The maximum model length of the draft model. Used when testing the ability to skip speculation for some sequences.

###

`max_num_new_slots_for_drafting`

`property`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.max_num_new_slots_for_drafting)

Return the maximum additional drafting slots per request.

The scheduler budget already includes one query slot per decoding request. Let K be `num_speculative_tokens`

. Standard configurations require:

==================== ============= ======== ================ Algorithm Method Parallel Additional slots ==================== ============= ======== ================ EAGLE3 eagle3 No 0 P-EAGLE eagle3 Yes K - 1 DFlash dflash Yes K DSpark dspark Yes K - 1 MTP mtp No 0 N-gram ngram No 0 Draft model draft_model No 1 PARD draft_model Yes K ==================== ============= ======== ================

###

`method = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.method)

The name of the speculative method to use. If users provide and set the `model`

param, the speculative method type will be detected automatically if possible, if `model`

param is not provided, the method name must be provided.

If using `ngram`

method, the related configuration `prompt_lookup_max`

and `prompt_lookup_min`

should be considered.

###

`model = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.model)

The name of the draft model, eagle head, or additional weights, if provided.

###

`moe_backend = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.moe_backend)

MoE backend to use for the draft model. When `None`

, the draft model inherits the target model's `--moe-backend`

setting. Useful when the drafter and generator require different MoE kernels (e.g. quantized generator with unquantized drafter).

###

`num_speculative_tokens = Field(default=None, gt=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.num_speculative_tokens)

The number of speculative tokens, if provided. It will default to the number in the draft model config if present, otherwise, it is required.

###

`num_speculative_tokens_per_batch_size = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.num_speculative_tokens_per_batch_size)

Batch-size schedule used to dynamically choose speculative-token count.

Each entry is `(range_start, range_end, num_speculative_tokens)`

with an inclusive batch-size range.

###

`parallel_drafting = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.parallel_drafting)

Enable parallel drafting, where all speculative tokens are generated in parallel rather than sequentially. This can improve performance but requires the speculative model be trained to support parallel drafting. Only compatible with EAGLE and draft model methods.

###

`prompt_lookup_max = Field(default=None, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.prompt_lookup_max)

Maximum size of ngram token window when using Ngram proposer, required when method is set to ngram.

###

`prompt_lookup_min = Field(default=None, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.prompt_lookup_min)

Minimum size of ngram token window when using Ngram proposer, if provided. Defaults to 1.

###

`quantization = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.quantization)

Quantization method that was used to quantize the draft model weights. If `None`

, we assume the model weights are not quantized. Note that it only takes effect when using the draft model-based speculative method.

###

`rejection_sample_method = 'standard'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.rejection_sample_method)

The rejection sampling method to use. 'standard' uses probabilistic rejection sampling (with or without cached draft logits, controlled by draft_sample_method). 'synthetic' accepts draft tokens with a decaying probability calibrated to synthetic_acceptance_rate. 'block' uses block verification (Sun et al.), which jointly verifies the draft tokens as a block instead of one at a time.

###

`revision = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.revision)

The specific model version to use for the draft model. It can be a branch name, a tag name, or a commit id. If unspecified, will use the default version.

###

`suffix_decoding_max_cached_requests = 10000`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.suffix_decoding_max_cached_requests)

The maximum number of requests to cache in the global suffix tree. If exceeded, will trigger eviction in FIFO order. If set to 0, the global suffix tree is disabled and past responses are not cached (prompt trees are still used).

###

`suffix_decoding_max_spec_factor = 1.0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.suffix_decoding_max_spec_factor)

The maximum spec factor for suffix decoding. The spec factor controls speculation lengths based on the prefix match length: max_spec_tokens = max_spec_factor * prefix_match_length.

###

`suffix_decoding_max_tree_depth = 24`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.suffix_decoding_max_tree_depth)

The maximum depth of the suffix decoding global and prompt trees. The tree depth limits the sum of the prefix match and speculation lengths.

###

`suffix_decoding_min_token_prob = 0.1`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.suffix_decoding_min_token_prob)

The minimum token probability for suffix decoding. Will only speculate tokens with estimated probability (based on frequency counts) greater than or equal to this value.

###

`synthetic_acceptance_length = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.synthetic_acceptance_length)

Target mean acceptance length for synthetic rejection sampling, in [1, num_speculative_tokens + 1]. Resolved internally to synthetic_acceptance_rates. Only valid when rejection_sample_method is 'synthetic'. Mutually exclusive with synthetic_acceptance_rates.

###

`synthetic_acceptance_rates = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.synthetic_acceptance_rates)

Per-position *unconditional* acceptance rates for synthetic rejection sampling. Position i's entry is the marginal probability that the first i+1 draft tokens are all accepted; the list must have length num_speculative_tokens, each entry in [0, 1], and be monotonically non-increasing. Only valid when rejection_sample_method is 'synthetic'. Mutually exclusive with synthetic_acceptance_length.

###

`target_model_config = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.target_model_config)

The configuration of the target model.

###

`target_parallel_config = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.target_parallel_config)

The parallel configuration for the target model.

###

`tensor_parallel_size = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.tensor_parallel_size)

Users should pass "draft_tensor_parallel_size". This parameter's purpose is to warn users when they mistakenly provide the wrong argument.

###

`use_heterogeneous_vocab = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.use_heterogeneous_vocab)

Allow draft and target models to use different vocabularies. When enabled, builds a token-level intersection at init and constrains draft logits to shared tokens only (TLI algorithm). Requires method='draft_model'.

###

`use_local_argmax_reduction = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.use_local_argmax_reduction)

Use vocab-parallel local argmax instead of all-gathering full logits for draft token generation. Reduces communication from O(vocab_size) to O(2 * tp_size) per token. Only applies to greedy draft selection in non-tree speculation.

###

`_acceptance_length_to_rates(length, n)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig._acceptance_length_to_rates)

Mean acceptance length to unconditional per-position rates, using the minimum-variance schedule.

## Source code in `vllm/config/speculative.py`


###

`_is_custom_proposer_path(model)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig._is_custom_proposer_path)

True if `model`

is a dotted import path (e.g. `pkg.MyProposer`

).

## Source code in `vllm/config/speculative.py`


###

`_maybe_override_draft_max_model_len(speculative_max_model_len, draft_max_model_len, target_max_model_len)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig._maybe_override_draft_max_model_len)

Determine the max sequence len for the draft model. This is usually the draft_max_model_len, but may be the target_max_model_len if it is less than the draft_max_model_len, or may be speculative_max_model_len if it is specified.

This is necessary so that sequences do not exceed the capacity of the draft model or the target model.

speculative_max_model_len is mainly used for testing that sequences can skip speculation.

## Source code in `vllm/config/speculative.py`


###

`_maybe_override_draft_max_position_embeddings(draft_hf_config, target_max_model_len)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig._maybe_override_draft_max_position_embeddings)

Raise an EAGLE draft's max_position_embeddings up to the target's.

The proposer feeds the draft positions up to the target's max_model_len, while max_position_embeddings sizes the draft's rotary cos_sin_cache. A smaller checkpoint value (e.g. 2048 for yuhuili/EAGLE3-LLaMA3.1-Instruct-8B) makes that cache gather go out of bounds (#48894).

Parameters:

-

(`draft_hf_config`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig._maybe_override_draft_max_position_embeddings(draft_hf_config))`PretrainedConfig`

) –The draft model's HF config, mutated in place.

-

(`target_max_model_len`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig._maybe_override_draft_max_position_embeddings(target_max_model_len))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The target model's max_model_len.


## Source code in `vllm/config/speculative.py`


###

`_resolve_synthetic_acceptance_rates(n, rates, length)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig._resolve_synthetic_acceptance_rates)

Return per-position unconditional acceptance rates from exactly one of `rates`

or `length`

(validates range, length, and monotonicity).

## Source code in `vllm/config/speculative.py`


###

`_verify_and_get_draft_tp(target_parallel_config, speculative_draft_tensor_parallel_size, draft_hf_config)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig._verify_and_get_draft_tp)

Verifies and adjusts the tensor parallel size for a draft model specified using speculative_draft_tensor_parallel_size.

## Source code in `vllm/config/speculative.py`


###

`apply_draft_overrides(vllm_config)`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.apply_draft_overrides)

Overlay this config's kernel overrides onto a target VllmConfig.

Only non-None fields override, so an unset field keeps whatever the target resolved.

## Source code in `vllm/config/speculative.py`


###

`compose_draft_hf_overrides(target_hf_overrides)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.compose_draft_hf_overrides)

Build the `hf_overrides`

for the draft `ModelConfig`

.

Callable overrides on the target are config-to-config transforms (e.g. test harnesses shrinking `num_hidden_layers`

) and must also reach the draft config — otherwise a draft belonging to a large target is instantiated at full size even when the target is shrunk. Dict overrides are target-specific key patches and are not applied to the draft.

The composed override must stay picklable: the draft `ModelConfig`

is sent to spawned engine-core processes, so a local closure would fail with `Can't get local object`

during pickling. Bind the target via `functools.partial`

over a module-referenceable static method instead.

## Source code in `vllm/config/speculative.py`


###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

## Source code in `vllm/config/speculative.py`


###

`create_draft_parallel_config(target_parallel_config, speculative_draft_tensor_parallel_size, draft_model_config=None)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.create_draft_parallel_config)

Create a parallel config for use by the draft worker.

Use the draft TP size and disable inherited EP for known dense drafts. Without a draft model config, preserve the previous EP inheritance.

## Source code in `vllm/config/speculative.py`


###

`update_arch_()`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.update_arch_)

EagleConfig and ExtractHiddenStatesConfig update architectures, so update all architectures-related fields in self.draft_model_config

## Source code in `vllm/config/speculative.py`


###

`use_eagle_block_drop()`

[¶](https://docs.vllm.ai#vllm.config.SpeculativeConfig.use_eagle_block_drop)

##

`SpeechToTextConfig`

[¶](https://docs.vllm.ai#vllm.config.SpeechToTextConfig)

Configuration for speech-to-text models.

Attributes:

-
([max_audio_clip_s](https://docs.vllm.ai#vllm.config.SpeechToTextConfig.max_audio_clip_s)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMaximum duration in seconds for a single audio clip without chunking.

-
([min_energy_split_window_size](https://docs.vllm.ai#vllm.config.SpeechToTextConfig.min_energy_split_window_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneWindow size in samples for finding low-energy (quiet) regions to split

-
([overlap_chunk_second](https://docs.vllm.ai#vllm.config.SpeechToTextConfig.overlap_chunk_second)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Overlap duration in seconds between consecutive audio chunks when

-
([sample_rate](https://docs.vllm.ai#vllm.config.SpeechToTextConfig.sample_rate)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Sample rate (Hz) to resample input audio to. Most speech models expect


## Source code in `vllm/config/speech_to_text.py`


###

`max_audio_clip_s = 30`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeechToTextConfig.max_audio_clip_s)

Maximum duration in seconds for a single audio clip without chunking. Audio longer than this will be split into smaller chunks if `allow_audio_chunking`

evaluates to True, otherwise it will be rejected. `None`

means audio duration can be unlimited and won't be chunked.

###

`min_energy_split_window_size = 1600`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeechToTextConfig.min_energy_split_window_size)

Window size in samples for finding low-energy (quiet) regions to split audio chunks. The algorithm looks for the quietest moment within this window to minimize cutting through speech. Default 1600 samples ≈ 100ms at 16kHz. If None, no chunking will be done.

###

`overlap_chunk_second = 1`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeechToTextConfig.overlap_chunk_second)

Overlap duration in seconds between consecutive audio chunks when splitting long audio. This helps maintain context across chunk boundaries and improves transcription quality at split points.

###

`sample_rate = 16000`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeechToTextConfig.sample_rate)

Sample rate (Hz) to resample input audio to. Most speech models expect 16kHz audio input. The input audio will be automatically resampled to this rate before processing.

##

`SpeechToTextParams`

`dataclass`

[¶](https://docs.vllm.ai#vllm.config.SpeechToTextParams)

All parameters consumed by `get_generation_prompt()`

.

`TranscriptionRequest.build_stt_params()`

constructs this object, mapping API-level fields into typed attributes. Models only receive this object, so new parameters can be added here without changing the `get_generation_prompt`

signature.

Attributes:

-
([audio](https://docs.vllm.ai#vllm.config.SpeechToTextParams.audio)

) –[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)Resampled audio waveform for a single chunk.

-
([hotwords](https://docs.vllm.ai#vllm.config.SpeechToTextParams.hotwords)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| Nonehotwords refers to a list of important words or phrases that the model

-
([language](https://docs.vllm.ai#vllm.config.SpeechToTextParams.language)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneISO 639-1 language code (validated / auto-detected).

-
([model_config](https://docs.vllm.ai#vllm.config.SpeechToTextParams.model_config)

) –[ModelConfig](https://docs.vllm.ai/model/#vllm.config.model.ModelConfig)Model configuration.

-
([request_prompt](https://docs.vllm.ai#vllm.config.SpeechToTextParams.request_prompt)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Optional text prompt to guide the model.

-
([stt_config](https://docs.vllm.ai#vllm.config.SpeechToTextParams.stt_config)

) –[SpeechToTextConfig](https://docs.vllm.ai/speech_to_text/#vllm.config.speech_to_text.SpeechToTextConfig)Server-level speech-to-text configuration.

-
([task_type](https://docs.vllm.ai#vllm.config.SpeechToTextParams.task_type)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)`"transcribe"`

or`"translate"`

. -
([to_language](https://docs.vllm.ai#vllm.config.SpeechToTextParams.to_language)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneTarget language for translation (model-dependent).


## Source code in `vllm/config/speech_to_text.py`


###

`audio`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeechToTextParams.audio)

Resampled audio waveform for a single chunk.

###

`hotwords = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeechToTextParams.hotwords)

hotwords refers to a list of important words or phrases that the model should pay extra attention to during transcription.

###

`language = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeechToTextParams.language)

ISO 639-1 language code (validated / auto-detected).

###

`model_config`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeechToTextParams.model_config)

Model configuration.

###

`request_prompt = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeechToTextParams.request_prompt)

Optional text prompt to guide the model.

###

`stt_config`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeechToTextParams.stt_config)

Server-level speech-to-text configuration.

###

`task_type = 'transcribe'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeechToTextParams.task_type)

`"transcribe"`

or `"translate"`

.

###

`to_language = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.SpeechToTextParams.to_language)

Target language for translation (model-dependent).

##

`StructuredOutputsConfig`

[¶](https://docs.vllm.ai#vllm.config.StructuredOutputsConfig)

Dataclass which contains structured outputs config for the engine.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.StructuredOutputsConfig.compute_hash)WARNING: Whenever a new field is added to this config,


Attributes:

-
([backend](https://docs.vllm.ai#vllm.config.StructuredOutputsConfig.backend)`StructuredOutputsBackend`

) –Which engine will be used for structured outputs (e.g. JSON schema,

-
([disable_additional_properties](https://docs.vllm.ai#vllm.config.StructuredOutputsConfig.disable_additional_properties)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, the`guidance`

backend will not use`additionalProperties`

-
([disable_any_whitespace](https://docs.vllm.ai#vllm.config.StructuredOutputsConfig.disable_any_whitespace)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, json output will always be compact without any whitespace. -
([enable_in_reasoning](https://docs.vllm.ai#vllm.config.StructuredOutputsConfig.enable_in_reasoning)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to use structured input for reasoning.

-
([reasoning_parser](https://docs.vllm.ai#vllm.config.StructuredOutputsConfig.reasoning_parser)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Select the reasoning parser depending on the model that you're using.

-
([reasoning_parser_plugin](https://docs.vllm.ai#vllm.config.StructuredOutputsConfig.reasoning_parser_plugin)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Path to a dynamically reasoning parser plugin that can be dynamically


## Source code in `vllm/config/structured_outputs.py`


###

`backend = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.StructuredOutputsConfig.backend)

Which engine will be used for structured outputs (e.g. JSON schema, regex, etc) by default. With "auto", we will make opinionated choices based on request contents and what the backend libraries currently support, so the behavior is subject to change in each release.

###

`disable_additional_properties = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.StructuredOutputsConfig.disable_additional_properties)

If `True`

, the `guidance`

backend will not use `additionalProperties`

in the JSON schema. This is only supported for the `guidance`

backend and is used to better align its behaviour with `outlines`

and `xgrammar`

.

###

`disable_any_whitespace = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.StructuredOutputsConfig.disable_any_whitespace)

If `True`

, json output will always be compact without any whitespace. If `False`

, the model may generate whitespace between JSON fields, which is still valid JSON. This is only supported for xgrammar and guidance backends.

###

`enable_in_reasoning = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.StructuredOutputsConfig.enable_in_reasoning)

Whether to use structured input for reasoning.

###

`reasoning_parser = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.StructuredOutputsConfig.reasoning_parser)

Select the reasoning parser depending on the model that you're using. This is used to parse the reasoning content into OpenAI API format.

###

`reasoning_parser_plugin = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.StructuredOutputsConfig.reasoning_parser_plugin)

Path to a dynamically reasoning parser plugin that can be dynamically loaded and registered.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.StructuredOutputsConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

## Source code in `vllm/config/structured_outputs.py`


##

`UVAOffloadConfig`

[¶](https://docs.vllm.ai#vllm.config.UVAOffloadConfig)

Configuration for UVA (Unified Virtual Addressing) CPU offloading.

Uses zero-copy access from CPU-pinned memory. Simple but requires fast CPU-GPU interconnect.

Attributes:

-
([cpu_offload_gb](https://docs.vllm.ai#vllm.config.UVAOffloadConfig.cpu_offload_gb)

) –[float](https://docs.python.org/3/builtins/functions.html#float)The space in GiB to offload to CPU, per GPU. Default is 0, which means

-
([cpu_offload_params](https://docs.vllm.ai#vllm.config.UVAOffloadConfig.cpu_offload_params)

) –[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The set of parameter name segments to target for CPU offloading.


## Source code in `vllm/config/offload.py`


###

`cpu_offload_gb = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.UVAOffloadConfig.cpu_offload_gb)

The space in GiB to offload to CPU, per GPU. Default is 0, which means no offloading. Intuitively, this argument can be seen as a virtual way to increase the GPU memory size. For example, if you have one 24 GB GPU and set this to 10, virtually you can think of it as a 34 GB GPU. Then you can load a 13B model with BF16 weight, which requires at least 26GB GPU memory. Note that this requires fast CPU-GPU interconnect, as part of the model is loaded from CPU memory to GPU memory on the fly in each model forward pass. This uses UVA (Unified Virtual Addressing) for zero-copy access.

###

`cpu_offload_params = Field(default_factory=set)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.UVAOffloadConfig.cpu_offload_params)

The set of parameter name segments to target for CPU offloading. Unmatched parameters are not offloaded. If this set is empty, parameters are offloaded non-selectively until the memory limit defined by `cpu_offload_gb`

is reached. Examples: - For parameter name "mlp.experts.w2_weight": - "experts" or "experts.w2_weight" will match. - "expert" or "w2" will NOT match (must be exact segments). This allows distinguishing parameters like "w2_weight" and "w2_weight_scale".

##

`VllmConfig`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig)

Dataclass which contains all vllm-related configuration. This simplifies passing around the distinct configurations in the codebase.

Methods:

-
–[__post_init__](https://docs.vllm.ai#vllm.config.VllmConfig.__post_init__)Verify configs are valid & consistent with each other.

-
–[adjust_dcp_kv_cache_interleave_size](https://docs.vllm.ai#vllm.config.VllmConfig.adjust_dcp_kv_cache_interleave_size)Normalize DCP interleave size against block_size for NIXL P/D.

-
–[compile_debug_dump_path](https://docs.vllm.ai#vllm.config.VllmConfig.compile_debug_dump_path)Returns a rank-aware path for dumping

-
–[compute_hash](https://docs.vllm.ai#vllm.config.VllmConfig.compute_hash)WARNING: Whenever a new field is added to this config,

-
–[enable_trace_function_call_for_thread](https://docs.vllm.ai#vllm.config.VllmConfig.enable_trace_function_call_for_thread)Set up function tracing for the current thread,

-
–[validate_block_size](https://docs.vllm.ai#vllm.config.VllmConfig.validate_block_size)Validate block_size against DCP and mamba constraints.


Attributes:

-
([additional_config](https://docs.vllm.ai#vllm.config.VllmConfig.additional_config)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)| SupportsHashAdditional config for specified platform. Different platforms may

-
([attention_config](https://docs.vllm.ai#vllm.config.VllmConfig.attention_config)

) –[AttentionConfig](https://docs.vllm.ai/attention/#vllm.config.attention.AttentionConfig)Attention configuration.

-
([aux_output_config](https://docs.vllm.ai#vllm.config.VllmConfig.aux_output_config)

) –[AuxOutputConfig](https://docs.vllm.ai/aux_output/#vllm.config.aux_output.AuxOutputConfig)Execution auxiliary output configuration.

-
([cache_config](https://docs.vllm.ai#vllm.config.VllmConfig.cache_config)

) –[CacheConfig](https://docs.vllm.ai/cache/#vllm.config.cache.CacheConfig)Cache configuration.

-
([compilation_config](https://docs.vllm.ai#vllm.config.VllmConfig.compilation_config)

) –[CompilationConfig](https://docs.vllm.ai/compilation/#vllm.config.compilation.CompilationConfig)`torch.compile`

and cudagraph capture configuration for the model. -
([device_config](https://docs.vllm.ai#vllm.config.VllmConfig.device_config)

) –[DeviceConfig](https://docs.vllm.ai/device/#vllm.config.device.DeviceConfig)Device configuration.

-
([diffusion_config](https://docs.vllm.ai#vllm.config.VllmConfig.diffusion_config)

) –[DiffusionConfig](https://docs.vllm.ai/diffusion/#vllm.config.diffusion.DiffusionConfig)| NoneDiffusion LLM (dLLM) configuration.

-
([ec_manager_config](https://docs.vllm.ai#vllm.config.VllmConfig.ec_manager_config)

) –[EncoderCacheManagerConfig](https://docs.vllm.ai/ec_manager_config/#vllm.config.ec_manager_config.EncoderCacheManagerConfig)The configurations for custom encoder cache manager.

-
([ec_transfer_config](https://docs.vllm.ai#vllm.config.VllmConfig.ec_transfer_config)

) –[ECTransferConfig](https://docs.vllm.ai/ec_transfer/#vllm.config.ec_transfer.ECTransferConfig)| NoneThe configurations for distributed EC cache transfer.

-
([engram_config](https://docs.vllm.ai#vllm.config.VllmConfig.engram_config)

) –[EngramConfig](https://docs.vllm.ai/engram/#vllm.config.engram.EngramConfig)| NoneN-gram embedding storage and sharding settings.

-
([instance_id](https://docs.vllm.ai#vllm.config.VllmConfig.instance_id)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The ID of the vLLM instance.

-
([kernel_config](https://docs.vllm.ai#vllm.config.VllmConfig.kernel_config)

) –[KernelConfig](https://docs.vllm.ai/kernel/#vllm.config.kernel.KernelConfig)Kernel configuration.

-
([kv_events_config](https://docs.vllm.ai#vllm.config.VllmConfig.kv_events_config)

) –[KVEventsConfig](https://docs.vllm.ai/kv_events/#vllm.config.kv_events.KVEventsConfig)| NoneThe configurations for event publishing.

-
([kv_transfer_config](https://docs.vllm.ai#vllm.config.VllmConfig.kv_transfer_config)

) –[KVTransferConfig](https://docs.vllm.ai/kv_transfer/#vllm.config.kv_transfer.KVTransferConfig)| NoneThe configurations for distributed KV cache transfer.

-
([load_config](https://docs.vllm.ai#vllm.config.VllmConfig.load_config)

) –[LoadConfig](https://docs.vllm.ai/load/#vllm.config.load.LoadConfig)Load configuration.

-
([lora_config](https://docs.vllm.ai#vllm.config.VllmConfig.lora_config)

) –[LoRAConfig](https://docs.vllm.ai/lora/#vllm.config.lora.LoRAConfig)| NoneLoRA configuration.

-
([mamba_config](https://docs.vllm.ai#vllm.config.VllmConfig.mamba_config)

) –[MambaConfig](https://docs.vllm.ai/mamba/#vllm.config.mamba.MambaConfig)Mamba configuration.

-
([model_config](https://docs.vllm.ai#vllm.config.VllmConfig.model_config)

) –[ModelConfig](https://docs.vllm.ai/model/#vllm.config.model.ModelConfig)Model configuration.

-
([needs_dp_coordinator](https://docs.vllm.ai#vllm.config.VllmConfig.needs_dp_coordinator)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Determine if the DPCoordinator process is needed.

-
([num_lookahead_tokens](https://docs.vllm.ai#vllm.config.VllmConfig.num_lookahead_tokens)

) –[int](https://docs.python.org/3/builtins/functions.html#int)KV slots to reserve past the tokens the target model is scheduled for.

-
([num_prefill_lookahead_tokens](https://docs.vllm.ai#vllm.config.VllmConfig.num_prefill_lookahead_tokens)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Prefill tokens past the computed range that the drafter reads.

-
([observability_config](https://docs.vllm.ai#vllm.config.VllmConfig.observability_config)

) –[ObservabilityConfig](https://docs.vllm.ai/observability/#vllm.config.observability.ObservabilityConfig)Observability configuration.

-
([offload_config](https://docs.vllm.ai#vllm.config.VllmConfig.offload_config)

) –[OffloadConfig](https://docs.vllm.ai/offload/#vllm.config.offload.OffloadConfig)Model weight offloading configuration.

-
([optimization_level](https://docs.vllm.ai#vllm.config.VllmConfig.optimization_level)

) –[OptimizationLevel](https://docs.vllm.ai/vllm/#vllm.config.vllm.OptimizationLevel)The optimization level. These levels trade startup time cost for

-
([parallel_config](https://docs.vllm.ai#vllm.config.VllmConfig.parallel_config)

) –[ParallelConfig](https://docs.vllm.ai/parallel/#vllm.config.parallel.ParallelConfig)Parallel configuration.

-
([performance_mode](https://docs.vllm.ai#vllm.config.VllmConfig.performance_mode)`PerformanceMode`

) –Performance mode for runtime behavior, 'balanced' is the default.

-
([profiler_config](https://docs.vllm.ai#vllm.config.VllmConfig.profiler_config)

) –[ProfilerConfig](https://docs.vllm.ai/profiler/#vllm.config.profiler.ProfilerConfig)Profiling configuration.

-
([quant_config](https://docs.vllm.ai#vllm.config.VllmConfig.quant_config)

) –[QuantizationConfig](https://docs.vllm.ai/model_executor/layers/quantization/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizationConfig)| NoneQuantization configuration.

-
([reasoning_config](https://docs.vllm.ai#vllm.config.VllmConfig.reasoning_config)

) –[ReasoningConfig](https://docs.vllm.ai/reasoning/#vllm.config.reasoning.ReasoningConfig)| NoneThe configurations for reasoning model.

-
([scheduler_config](https://docs.vllm.ai#vllm.config.VllmConfig.scheduler_config)

) –[SchedulerConfig](https://docs.vllm.ai/scheduler/#vllm.config.scheduler.SchedulerConfig)Scheduler configuration.

-
([shutdown_timeout](https://docs.vllm.ai#vllm.config.VllmConfig.shutdown_timeout)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Shutdown grace period for in-flight requests. Shutdown will be delayed for

-
([speculative_config](https://docs.vllm.ai#vllm.config.VllmConfig.speculative_config)

) –[SpeculativeConfig](https://docs.vllm.ai/speculative/#vllm.config.speculative.SpeculativeConfig)| NoneSpeculative decoding configuration.

-
([structured_outputs_config](https://docs.vllm.ai#vllm.config.VllmConfig.structured_outputs_config)

) –[StructuredOutputsConfig](https://docs.vllm.ai/structured_outputs/#vllm.config.structured_outputs.StructuredOutputsConfig)Structured outputs configuration.

-
([uniform_decode_query_len](https://docs.vllm.ai#vllm.config.VllmConfig.uniform_decode_query_len)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Query length of every request in a uniform decode batch.

-
([watermark_config](https://docs.vllm.ai#vllm.config.VllmConfig.watermark_config)

) –[WatermarkConfig](https://docs.vllm.ai/watermarking/#vllm.config.watermarking.WatermarkConfig)| NoneText watermarking configuration.

-
([weight_transfer_config](https://docs.vllm.ai#vllm.config.VllmConfig.weight_transfer_config)

) –[WeightTransferConfig](https://docs.vllm.ai/weight_transfer/#vllm.config.weight_transfer.WeightTransferConfig)| NoneThe configurations for weight transfer during RL training.


## Source code in `vllm/config/vllm.py`


|
|

###

`additional_config = Field(default_factory=dict)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.additional_config)

Additional config for specified platform. Different platforms may support different configs. Make sure the configs are valid for the platform you are using. Contents must be hashable.

###

`attention_config = Field(default_factory=AttentionConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.attention_config)

Attention configuration.

###

`aux_output_config = Field(default_factory=AuxOutputConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.aux_output_config)

Execution auxiliary output configuration.

###

`cache_config = Field(default_factory=CacheConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.cache_config)

Cache configuration.

###

`compilation_config = Field(default_factory=CompilationConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.compilation_config)

`torch.compile`

and cudagraph capture configuration for the model.

As a shorthand, one can append compilation arguments via -cc.parameter=argument such as `-cc.mode=3`

(same as `-cc='{"mode":3}'`

).

You can specify the full compilation config like so: `{"mode": 3, "cudagraph_capture_sizes": [1, 2, 4, 8]}`


###

`device_config = Field(default_factory=DeviceConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.device_config)

Device configuration.

###

`diffusion_config = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.diffusion_config)

Diffusion LLM (dLLM) configuration.

###

`ec_manager_config = Field(default_factory=EncoderCacheManagerConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.ec_manager_config)

The configurations for custom encoder cache manager.

###

`ec_transfer_config = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.ec_transfer_config)

The configurations for distributed EC cache transfer.

###

`engram_config = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.engram_config)

N-gram embedding storage and sharding settings.

###

`instance_id = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.instance_id)

The ID of the vLLM instance.

###

`kernel_config = Field(default_factory=KernelConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.kernel_config)

Kernel configuration.

###

`kv_events_config = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.kv_events_config)

The configurations for event publishing.

###

`kv_transfer_config = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.kv_transfer_config)

The configurations for distributed KV cache transfer.

###

`load_config = Field(default_factory=LoadConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.load_config)

Load configuration.

###

`lora_config = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.lora_config)

LoRA configuration.

###

`mamba_config = Field(default_factory=MambaConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.mamba_config)

Mamba configuration.

###

`model_config = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.model_config)

Model configuration.

###

`needs_dp_coordinator`

`property`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.needs_dp_coordinator)

Determine if the DPCoordinator process is needed.

The DPCoordinator is needed in two cases: 1. For MoE models with DP > 1: to handle wave coordination (even in external LB mode, since wave coordination runs in the coordinator) 2. For non-MoE models in internal/hybrid LB mode: to collect and publish queue stats for load balancing across DP ranks

Returns:

-

–[bool](https://docs.python.org/3/builtins/functions.html#bool)True if DPCoordinator process is needed, False otherwise.


###

`num_lookahead_tokens`

`property`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.num_lookahead_tokens)

KV slots to reserve past the tokens the target model is scheduled for.

The drafter writes KV for positions beyond the target model's query range, so every component that reserves blocks must add this margin: the scheduler through `allocate_slots`

, and the worker warmup, which builds its own `SchedulerOutput`

s. Consumers must read this property rather than re-deriving their own per-method lookahead, so the scheduler and warmup cannot drift apart.

###

`num_prefill_lookahead_tokens`

`property`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.num_prefill_lookahead_tokens)

Prefill tokens past the computed range that the drafter reads.

Mid-prefill the drafter consumes tokens the target model has not been scheduled for yet, so every component that has to keep them available must apply this margin: the scheduler, which never ends a chunk within it and shifts encoder scheduling by it, and the KV cache manager, which treats the trailing `this - 1`

tokens as re-prefillable rather than finalized. Consumers must read this property rather than re-deriving their own per-method lookahead, so those components cannot drift apart.

###

`observability_config = Field(default_factory=ObservabilityConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.observability_config)

Observability configuration.

###

`offload_config = Field(default_factory=OffloadConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.offload_config)

Model weight offloading configuration.

###

`optimization_level = OptimizationLevel.O2`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.optimization_level)

The optimization level. These levels trade startup time cost for performance, with -O0 having the best startup time and -O3 having the best performance. -O2 is used by default. See OptimizationLevel for full description.

###

`parallel_config = Field(default_factory=ParallelConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.parallel_config)

Parallel configuration.

###

`performance_mode = 'balanced'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.performance_mode)

Performance mode for runtime behavior, 'balanced' is the default. 'interactivity' favors low end-to-end per-request latency at small batch sizes (fine-grained CUDA graphs, latency-oriented kernels). 'throughput' favors aggregate tokens/sec at high concurrency (larger CUDA graphs, more aggressive batching, throughput-oriented kernels).

###

`profiler_config = Field(default_factory=ProfilerConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.profiler_config)

Profiling configuration.

###

`quant_config = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.quant_config)

Quantization configuration.

###

`reasoning_config = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.reasoning_config)

The configurations for reasoning model.

###

`scheduler_config = Field(default_factory=(SchedulerConfig.default_factory))`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.scheduler_config)

Scheduler configuration.

###

`shutdown_timeout = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.shutdown_timeout)

Shutdown grace period for in-flight requests. Shutdown will be delayed for up to this amount of time to allow already-running requests to complete. Any remaining requests are aborted once the timeout is reached.

###

`speculative_config = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.speculative_config)

Speculative decoding configuration.

###

`structured_outputs_config = Field(default_factory=StructuredOutputsConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.structured_outputs_config)

Structured outputs configuration.

###

`uniform_decode_query_len`

`property`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.uniform_decode_query_len)

Query length of every request in a uniform decode batch.

A decode step submits one query for the newly sampled token plus one for each draft token, so the widest uniform decode batch the scheduler can build is `max_num_seqs * uniform_decode_query_len`

tokens. Anything that has to cover a decode batch reads this, so the sizing rule cannot drift between the places that apply it.

This deliberately does not derive from the KV slots a drafter reserves past the target's query range, which is a *reservation* contract rather than a query-length one. The two do not differ by a constant: DFlash reserves `num_speculative_tokens + 1`

slots yet still verifies `1 + num_speculative_tokens`

queries, while EAGLE reserves `num_speculative_tokens`

and verifies the same `1 + n`

. Deriving one from the other would under-size EAGLE by a full request width, which is the failure this property exists to prevent.

###

`watermark_config = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.watermark_config)

Text watermarking configuration.

###

`weight_transfer_config = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.weight_transfer_config)

The configurations for weight transfer during RL training.

###

`__post_init__()`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.__post_init__)

Verify configs are valid & consistent with each other.

## Source code in `vllm/config/vllm.py`


|
|

###

`_apply_optimization_level_defaults(defaults)`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig._apply_optimization_level_defaults)

Apply optimization level defaults using self as root.

Recursively applies values from defaults into nested config objects. Only fields present in defaults are overwritten.

If the user configuration does not specify a value for a default field and if the default field is still None after all user selections are applied, then default values will be applied to the field. User specified fields will not be overridden by the default.

Parameters:

## Source code in `vllm/config/vllm.py`


###

`_dflash_needs_multi_kv_group()`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig._dflash_needs_multi_kv_group)

Whether a DFlash draft mixes sliding-window and full attention.

## Source code in `vllm/config/vllm.py`


###

`_get_dbo_unsupported_features()`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig._get_dbo_unsupported_features)

Collect what the V2 model runner cannot combine with DBO.

The V2 runner microbatches a plain decoder forward pass. Anything that slices or replays the batch differently (drafting, adapters, pipeline stages, context parallelism, encoders) is not handled yet.

## Source code in `vllm/config/vllm.py`


###

`_get_quantization_config(model_config, load_config)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig._get_quantization_config)

Get the quantization config.

## Source code in `vllm/config/vllm.py`


###

`_get_v2_model_runner_unsupported_features()`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig._get_v2_model_runner_unsupported_features)

Collect features not yet supported by the V2 model runner.

## Source code in `vllm/config/vllm.py`


###

`_is_dflash2_draft()`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig._is_dflash2_draft)

Whether the DFlash draft is a DFlash2 one, by the architecture the speculator selects on (v1/worker/gpu/spec_decode/**init**.py).

## Source code in `vllm/config/vllm.py`


###

`_post_init_kv_transfer_config()`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig._post_init_kv_transfer_config)

Update KVTransferConfig based on top-level configs in VllmConfig.

Right now, this function reads the offloading settings from CacheConfig and configures the KVTransferConfig accordingly.

## Source code in `vllm/config/vllm.py`


###

`_resolve_and_verify_engram_config()`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig._resolve_and_verify_engram_config)

Resolve defaults and validate n-gram embedding settings.

## Source code in `vllm/config/vllm.py`


###

`_resolve_mm_embedding_inputs()`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig._resolve_mm_embedding_inputs)

Accept embedding inputs, tensor optional, on disaggregated consumers.

An EC consumer loads embeddings from its connector. A KV consumer receives the prompt KV produced from those embeddings, so it does not need the tensors either. On every other deployment a missing tensor is a client error and must keep failing fast in the frontend.

## Source code in `vllm/config/vllm.py`


###

`_resolve_mm_encoder_only()`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig._resolve_mm_encoder_only)

Enable encoder-only mode for a dedicated EC producer.

## Source code in `vllm/config/vllm.py`


###

`_resolve_mm_processor_device()`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig._resolve_mm_processor_device)

Settle `--mm-processor-device=auto`

now that the EC role is known.

"auto" means "the accelerator, but only where the processor has it to itself and its output can be handed over without a copy back to host": an encode-only instance whose tensor transport carries device tensors. Every other deployment keeps the processor on CPU.

An explicit device -- from `--mm-processor-device`

or straight from `mm_processor_kwargs`

-- is already folded in by `MultiModalConfig`

, so it is left alone here and validated by `_validate_mm_processor_device`

.

## Source code in `vllm/config/vllm.py`


###

`_resolve_mm_video_decode_device()`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig._resolve_mm_video_decode_device)

Default video decoding to torchcodec GPU backend for EPD encoder-only instance if the mm processor runs on CUDA.

The processor consumes the decoded frames on-device in that case, so keeping the frames on the GPU skips the host round-trip through the CPU media path. An explicit codec/backend choice in `--media-io-kwargs`

is left alone, and the default is skipped where torchcodec (or its FFmpeg runtime) is unavailable.

## Source code in `vllm/config/vllm.py`


###

`_set_compile_ranges()`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig._set_compile_ranges)

Set the compile ranges for the compilation config.

## Source code in `vllm/config/vllm.py`


|
|

###

`_set_config_default(config_obj, key, value)`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig._set_config_default)

Set config attribute to default if not already set by user.

Parameters:

-

(`config_obj`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig._set_config_default(config_obj))

) –[Any](https://docs.python.org/3/library/typing.html#typing.Any)Configuration object to update.

-

(`key`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig._set_config_default(key))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Attribute name.

-

(`value`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig._set_config_default(value))

) –[Any](https://docs.python.org/3/library/typing.html#typing.Any)Default value (static or callable).


## Source code in `vllm/config/vllm.py`


###

`_set_cudagraph_sizes()`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig._set_cudagraph_sizes)

VLLM defines the default candidate list of batch sizes for CUDA graph capture as:

```python default_max_graph_size = 1024 if is_data_center_blackwell else 512 decode_query_len = self.uniform_decode_query_len max_graph_size = min( max_num_seqs * decode_query_len * 2, default_max_graph_size )

#### 1, 2, 4, then multiples of 8 up to 256 and then multiples of 16[¶](https://docs.vllm.ai#vllm.config.VllmConfig._set_cudagraph_sizes--1-2-4-then-multiples-of-8-up-to-256-and-then-multiples-of-16)

#### up to max_graph_size[¶](https://docs.vllm.ai#vllm.config.VllmConfig._set_cudagraph_sizes--up-to-max_graph_size)

cudagraph_capture_sizes = [1, 2, 4] + list(range(8, 256, 8)) + list( range(256, max_graph_size + 1, 16))

`max_num_batched_tokens`

is also appended to the list if it fits within `max_cudagraph_capture_size`

, so the max batch size is captured even when off-stride. Uniform decode sizes are appended when they fit within the platform's default capture ceiling, since they need not land on an 8- or 16-token stride.

In the end, `vllm_config.compilation_config.cudagraph_capture_sizes`

will be the final sizes to capture cudagraph (in ascending order).

These sizes are used to capture and reuse CUDA graphs for performance-critical paths (e.g., decoding). Capturing enables significantly faster kernel dispatch by avoiding Python overhead. The list is then filtered based on `max_num_batched_tokens`

(e.g., 8192 on most GPUs), which controls the total allowed number of tokens in a batch. Since each sequence may have a variable number of tokens, the maximum usable batch size will depend on actual sequence lengths.

Example: With `max_num_batched_tokens = 8192`

, and typical sequences averaging ~32 tokens, most practical batch sizes fall below 256. However, the system will still allow capture sizes up to the platform default if shape and memory permit.

Note: If users explicitly specify cudagraph capture sizes in the compilation config, those will override this default logic. At runtime:

```
- If batch size <= one of the `cudagraph_capture_sizes`, the closest
padded CUDA graph will be used.
- If batch size > largest `cudagraph_capture_sizes`, cudagraph will
not be used.
```


## Source code in `vllm/config/vllm.py`


|
|

###

`_set_max_num_scheduled_tokens()`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig._set_max_num_scheduled_tokens)

In most cases, the scheduler may schedule a batch with as many tokens as the worker is configured to handle.

## Source code in `vllm/config/vllm.py`


###

`_validate_batch_sharded_sampling()`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig._validate_batch_sharded_sampling)

Validate `enable_batch_sharded_sampling`

against the rest of the config.

## Source code in `vllm/config/vllm.py`


###

`_validate_mm_processor_device()`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig._validate_mm_processor_device)

Hand the EC config to `MultiModalConfig`

, which owns the rule.

## Source code in `vllm/config/vllm.py`


###

`_validate_v2_model_runner()`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig._validate_v2_model_runner)

Check for features not yet supported by the V2 model runner.

## Source code in `vllm/config/vllm.py`


###

`_verify_aux_output_compatibility()`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig._verify_aux_output_compatibility)

Reject configurations unsupported by enabled auxiliary outputs.

## Source code in `vllm/config/vllm.py`


###

`_verify_kv_transfer_compat()`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig._verify_kv_transfer_compat)

Reject configurations that silently corrupt KV transfers.

## Source code in `vllm/config/vllm.py`


###

`adjust_dcp_kv_cache_interleave_size(kv_cache_config)`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.adjust_dcp_kv_cache_interleave_size)

Normalize DCP interleave size against block_size for NIXL P/D.

Called by each worker (via ensure_kv_transfer_initialized), once it knows its own final block_size via kv_cache_config.

## Source code in `vllm/config/vllm.py`


###

`compile_debug_dump_path()`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.compile_debug_dump_path)

Returns a rank-aware path for dumping torch.compile debug information.

## Source code in `vllm/config/vllm.py`


###

`compute_hash(include_version=True)`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

Parameters:

## Source code in `vllm/config/vllm.py`


|
|

###

`enable_trace_function_call_for_thread()`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.enable_trace_function_call_for_thread)

Set up function tracing for the current thread, if enabled via the `VLLM_TRACE_FUNCTION`

environment variable.

## Source code in `vllm/config/vllm.py`


###

`validate_block_size()`

[¶](https://docs.vllm.ai#vllm.config.VllmConfig.validate_block_size)

Validate block_size against DCP and mamba constraints.

Called after Platform.update_block_size_for_backend() has finalised block_size.

## Source code in `vllm/config/vllm.py`


##

`WatermarkConfig`

[¶](https://docs.vllm.ai#vllm.config.WatermarkConfig)

Configuration for text watermark generation.

Attributes:

-
([algorithm](https://docs.vllm.ai#vllm.config.WatermarkConfig.algorithm)`WatermarkingAlgorithm`

) –Algorithm used to watermark generated text.

-
([allow_target_only_watermarking](https://docs.vllm.ai#vllm.config.WatermarkConfig.allow_target_only_watermarking)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Allow speculative decoding without watermarking draft tokens.

-
([alpha](https://docs.vllm.ai#vllm.config.WatermarkConfig.alpha)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Probability of selecting key B for dual-key watermarking.

-
([context_width](https://docs.vllm.ai#vllm.config.WatermarkConfig.context_width)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of prior tokens used by the watermark PRF.

-
([deduplicate_contexts](https://docs.vllm.ai#vllm.config.WatermarkConfig.deduplicate_contexts)`WatermarkContextScope`

) –Which history is searched for a repeated context before a token is

-
([deduplicate_contexts_max_history](https://docs.vllm.ai#vllm.config.WatermarkConfig.deduplicate_contexts_max_history)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneNumber of most recent history positions searched (default 8192), or

-
([key](https://docs.vllm.ai#vllm.config.WatermarkConfig.key)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Secret key used to watermark generated text.

-
([prf](https://docs.vllm.ai#vllm.config.WatermarkConfig.prf)`WatermarkPRFName`

) –Pseudorandom function used by the watermarking algorithm.


## Source code in `vllm/config/watermarking.py`


###

`algorithm = 'gumbel'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.WatermarkConfig.algorithm)

Algorithm used to watermark generated text.

###

`allow_target_only_watermarking = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.WatermarkConfig.allow_target_only_watermarking)

Allow speculative decoding without watermarking draft tokens.

###

`alpha = Field(default=0.1, ge=0, le=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.WatermarkConfig.alpha)

Probability of selecting key B for dual-key watermarking.

###

`context_width = Field(default=4, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.WatermarkConfig.context_width)

Number of prior tokens used by the watermark PRF.

###

`deduplicate_contexts = 'single_turn'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.WatermarkConfig.deduplicate_contexts)

Which history is searched for a repeated context before a token is sampled; a repeated context is sampled without the watermark. `none`

disables the search. `single_turn`

(default) searches this request's generated tokens. `all`

also searches the prompt and samples the first `context_width`

generated tokens without watermarking.

###

`deduplicate_contexts_max_history = Field(default=8192, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.WatermarkConfig.deduplicate_contexts_max_history)

Number of most recent history positions searched (default 8192), or `None`

for the whole scope. Each position is compared over the `context_width`

tokens before it. Ignored when `deduplicate_contexts`

is `none`

.

###

`key = Field(ge=0, repr=False, exclude=True)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.WatermarkConfig.key)

Secret key used to watermark generated text.

###

`prf = 'philox'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.WatermarkConfig.prf)

Pseudorandom function used by the watermarking algorithm.

##

`WeightTransferConfig`

[¶](https://docs.vllm.ai#vllm.config.WeightTransferConfig)

Configuration for weight transfer during RL training.

Attributes:

-
([backend](https://docs.vllm.ai#vllm.config.WeightTransferConfig.backend)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['nccl', 'ipc', 'sparse_nccl', 'sharded_rdt'] |[str](https://docs.python.org/3/builtins/stdtypes.html#str)The backend to use for weight transfer. Validated against the


## Source code in `vllm/config/weight_transfer.py`


###

`backend = 'nccl'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.WeightTransferConfig.backend)

The backend to use for weight transfer. Validated against the `WeightTransferEngineFactory`

registry at engine creation time.

##

`config(cls=None, *, config=None, **kwargs)`

[¶](https://docs.vllm.ai#vllm.config.config)

Decorator to create a pydantic dataclass with default config. The default config for the dataclass forbids extra fields.

All config classes in vLLM should use this decorator.

Parameters:

-

(`cls`

[¶](https://docs.vllm.ai#vllm.config.config(cls))

, default:[type](https://docs.python.org/3/builtins/functions.html#type)[ConfigT] | None`None`

) –The class to decorate

-

(`config`

[¶](https://docs.vllm.ai#vllm.config.config(config))`ConfigDict | None`

, default:`None`

) –The pydantic ConfigDict to use. If provided, it will be merged with the default config.

-

(`**kwargs`

[¶](https://docs.vllm.ai#vllm.config.config(**kwargs))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`{}`

) –Additional arguments to pass to pydantic.dataclass.


## Source code in `vllm/config/utils.py`


##

`get_attr_docs(cls)`

[¶](https://docs.vllm.ai#vllm.config.get_attr_docs)

Get any docstrings placed after attribute assignments in a class body.

https://davidism.com/mit-license/

## Source code in `vllm/config/utils.py`


##

`get_cached_compilation_config()`

`cached`

[¶](https://docs.vllm.ai#vllm.config.get_cached_compilation_config)

Cache config to avoid repeated calls to get_current_vllm_config()

##

`get_layers_from_vllm_config(vllm_config, layer_type, layer_names=None)`

[¶](https://docs.vllm.ai#vllm.config.get_layers_from_vllm_config)

Get layers from the vLLM config.

Parameters:

-

(`vllm_config`

[¶](https://docs.vllm.ai#vllm.config.get_layers_from_vllm_config(vllm_config))

) –[VllmConfig](https://docs.vllm.ai/vllm/#vllm.config.vllm.VllmConfig)The vLLM config.

-

(`layer_type`

[¶](https://docs.vllm.ai#vllm.config.get_layers_from_vllm_config(layer_type))

) –[type](https://docs.python.org/3/builtins/functions.html#type)[T]The type of the layer to get.

-

(`layer_names`

[¶](https://docs.vllm.ai#vllm.config.get_layers_from_vllm_config(layer_names))

, default:[Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None`None`

) –The names of the layers to get. If None, return all layers.


## Source code in `vllm/config/vllm.py`


##

`replace(dataclass_instance, /, **kwargs)`

[¶](https://docs.vllm.ai#vllm.config.replace)

Like [ dataclasses.replace](https://docs.python.org/3/library/dataclasses.html#dataclasses.replace), but compatible with Pydantic dataclasses which use

`pydantic.fields.Field`

instead of `dataclasses.field`

## Source code in `vllm/config/utils.py`


##

`set_current_vllm_config(vllm_config, check_compile=False, prefix=None)`

[¶](https://docs.vllm.ai#vllm.config.set_current_vllm_config)

Temporarily set the current vLLM config. Used during model initialization. We save the current vLLM config in a global variable, so that all modules can access it, e.g. custom ops can access the vLLM config to determine how to dispatch.