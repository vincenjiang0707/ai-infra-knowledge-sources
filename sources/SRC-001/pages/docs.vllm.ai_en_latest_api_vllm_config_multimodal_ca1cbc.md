source: https://docs.vllm.ai/en/latest/api/vllm/config/multimodal/
lastmod: 2026-09-24

#

`vllm.config.multimodal`

[¶](https://docs.vllm.ai#vllm.config.multimodal)

Classes:

-
–[AudioDummyOptions](https://docs.vllm.ai#vllm.config.multimodal.AudioDummyOptions)Options for generating dummy audio data during profiling.

-
–[BaseDummyOptions](https://docs.vllm.ai#vllm.config.multimodal.BaseDummyOptions)Base options for generating dummy data during profiling.

-
–[ImageDummyOptions](https://docs.vllm.ai#vllm.config.multimodal.ImageDummyOptions)Options for generating dummy image data during profiling.

-
–[MultiModalConfig](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig)Controls the behavior of multimodal models.

-
–[MultiModalDummyOptions](https://docs.vllm.ai#vllm.config.multimodal.MultiModalDummyOptions)Dummy data options for each modality.

-
–[VideoDummyOptions](https://docs.vllm.ai#vllm.config.multimodal.VideoDummyOptions)Options for generating dummy video data during profiling.


Attributes:

-
([MMProcessorDevice](https://docs.vllm.ai#vllm.config.multimodal.MMProcessorDevice)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)`"auto"`

,`"cpu"`

, or the platform's own accelerator name

##

`MMProcessorDevice = str`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MMProcessorDevice)

`"auto"`

, `"cpu"`

, or the platform's own accelerator name (`current_platform.device_type`

, e.g. `"cuda"`

on CUDA and ROCm, `"xpu"`

on XPU). Validated against that set by the CLI.

##

`AudioDummyOptions`

[¶](https://docs.vllm.ai#vllm.config.multimodal.AudioDummyOptions)

Bases: [BaseDummyOptions](https://docs.vllm.ai#vllm.config.multimodal.BaseDummyOptions)

Options for generating dummy audio data during profiling.

## Source code in `vllm/config/multimodal.py`


##

`BaseDummyOptions`

[¶](https://docs.vllm.ai#vllm.config.multimodal.BaseDummyOptions)

##

`ImageDummyOptions`

[¶](https://docs.vllm.ai#vllm.config.multimodal.ImageDummyOptions)

Bases: [BaseDummyOptions](https://docs.vllm.ai#vllm.config.multimodal.BaseDummyOptions)

Options for generating dummy image data during profiling.

## Source code in `vllm/config/multimodal.py`


##

`MultiModalConfig`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig)

Controls the behavior of multimodal models.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.compute_hash)WARNING: Whenever a new field is added to this config,

-
–[fold_mm_processor_device](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.fold_mm_processor_device)Fold the

`mm_processor_device`

convenience flag into the kwargs. -
–[get_limit_per_prompt](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.get_limit_per_prompt)Get the maximum number of input items allowed per prompt

-
–[get_mm_processor_device_type](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.get_mm_processor_device_type)The torch device type

`mm_processor_kwargs["device"]`

names. -
–[get_video_pruning_spec](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.get_video_pruning_spec)Return

`(method, rate)`

when video pruning is enabled, else None. -
–[merge_mm_processor_kwargs](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.merge_mm_processor_kwargs)Get the keyword arguments to pass to the multi-modal processor

-
–[use_gpu_video_backend](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.use_gpu_video_backend)Return whether the configured video loader or codec uses the GPU.

-
–[validate_mm_processor_device](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.validate_mm_processor_device)Check

`mm_processor_kwargs["device"]`

for this deployment.

Attributes:

-
([allow_missing_mm_embeddings](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.allow_missing_mm_embeddings)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether a pre-computed-embedding input may omit the

`*_embeds`

tensor. -
([enable_mm_embeds](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.enable_mm_embeds)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If

`True`

, enables passing multimodal embeddings: -
([interleave_mm_strings](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.interleave_mm_strings)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable fully interleaved support for multimodal prompts, while using

-
([language_model_only](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.language_model_only)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If True, disables all multimodal inputs by setting all modality limits to 0.

-
([limit_per_prompt](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.limit_per_prompt)

) –[MultiModalDummyOptions](https://docs.vllm.ai#vllm.config.multimodal.MultiModalDummyOptions)The maximum number of input items and options allowed per

-
([media_io_kwargs](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.media_io_kwargs)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)]]Additional args passed to process media inputs, keyed by modalities.

-
([mm_device_do_normalize](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_device_do_normalize)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneMove the do_normalize computation in the mm preprocessing to before the ViT,

-
([mm_encoder_attn_backend](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_encoder_attn_backend)

) –[AttentionBackendEnum](https://docs.vllm.ai/v1/attention/backends/registry/#vllm.v1.attention.backends.registry.AttentionBackendEnum)| NoneOptional override for the multi-modal encoder attention backend when

-
([mm_encoder_attn_dtype](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_encoder_attn_dtype)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['fp8'] | NoneOptional dtype override for ViT encoder attention. Set to

`"fp8"`

to -
([mm_encoder_fp8_scale_path](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_encoder_fp8_scale_path)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NonePath to a JSON file containing per-layer FP8 Q/K/V scales for ViT

-
([mm_encoder_fp8_scale_save_margin](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_encoder_fp8_scale_save_margin)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Safety margin multiplied onto scales when auto-saving. A value > 1

-
([mm_encoder_fp8_scale_save_path](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_encoder_fp8_scale_save_path)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneWhen set with dynamic FP8 scaling (

`mm_encoder_attn_dtype="fp8"`

-
([mm_encoder_only](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_encoder_only)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)When enabled, skips the language component of the model.

-
([mm_encoder_tp_mode](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_encoder_tp_mode)`MMEncoderTPMode`

) –Indicates how to optimize multi-modal encoder inference using tensor

-
([mm_hasher_algorithm](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_hasher_algorithm)`MMHasherAlgorithm`

) –Hash algorithm to use for multi-modal input caching. Use

`"sha256"`

or -
([mm_ipc_gpu_memory_gb](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_ipc_gpu_memory_gb)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Amount of GPU memory (in GiB) sequestered on the engine's device for

-
([mm_processor_cache_gb](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_processor_cache_gb)

) –[float](https://docs.python.org/3/builtins/functions.html#float)The size (in GiB) of the multi-modal processor cache, which is used to

-
([mm_processor_cache_type](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_processor_cache_type)`MMCacheType`

) –Type of cache to use for the multi-modal preprocessor/mapper. If

`shm`

, -
([mm_processor_kwargs](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_processor_kwargs)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[object](https://docs.python.org/3/builtins/functions.html#object)] | NoneArguments to be forwarded to the model's processor for multi-modal data,

-
([mm_shm_cache_max_object_size_mb](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_shm_cache_max_object_size_mb)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Size limit (in MiB) for each object stored in the multi-modal processor

-
([mm_tensor_ipc](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_tensor_ipc)`MMTensorIPC`

) –IPC (inter-process communication) method for multimodal tensors.

-
([skip_mm_profiling](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.skip_mm_profiling)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)When enabled, skips multimodal memory profiling and only profiles with

-
([video_pruning_method](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.video_pruning_method)`VideoPruningMethod`

) –Video token pruning algorithm applied when

`video_pruning_rate`

> 0: -
([video_pruning_rate](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.video_pruning_rate)

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NoneFraction of video tokens to prune from each video. Value sits in range


## Source code in `vllm/config/multimodal.py`


|
|

###

`allow_missing_mm_embeddings = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.allow_missing_mm_embeddings)

Whether a pre-computed-embedding input may omit the `*_embeds`

tensor.

In an encode/prefill/decode (EPD) deployment the encoder instance publishes embeddings through the EC connector. An EC consumer loads those embeddings from the connector, while a KV consumer receives the resulting prompt KV cache. Their requests only need the grid/size metadata that sizes the placeholder range.

Derived, not user-settable: `VllmConfig.__post_init__`

sets this to True on EC and KV consumers. Everywhere else it stays False so that a request which forgets its embeddings still fails fast in the frontend, with a clear error, rather than deep inside the model.

###

`enable_mm_embeds = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.enable_mm_embeds)

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

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.interleave_mm_strings)

Enable fully interleaved support for multimodal prompts, while using --chat-template-content-format=string.

###

`language_model_only = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.language_model_only)

If True, disables all multimodal inputs by setting all modality limits to 0. Equivalent to setting `--limit-mm-per-prompt`

to 0 for every modality.

###

`limit_per_prompt = Field(default_factory=MultiModalDummyOptions)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.limit_per_prompt)

The maximum number of input items and options allowed per prompt for each modality.

Defaults to 999 for each modality.

Legacy format (count only):

Configurable format (with options): {"video": {"count": 1, "num_frames": 32, "width": 512, "height": 512}, "image": {"count": 5, "width": 512, "height": 512}}

Mixed format (combining both): {"image": 16, "video": {"count": 1, "num_frames": 32, "width": 512, "height": 512}}

###

`media_io_kwargs = Field(default_factory=dict)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.media_io_kwargs)

Additional args passed to process media inputs, keyed by modalities. For example, to set num_frames for video, set `--media-io-kwargs '{"video": {"num_frames": 40} }'`


###

`mm_device_do_normalize = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_device_do_normalize)

Move the do_normalize computation in the mm preprocessing to before the ViT, and let the device do it, so that CPU computation can be saved.

###

`mm_encoder_attn_backend = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_encoder_attn_backend)

Optional override for the multi-modal encoder attention backend when using vision transformers. Accepts any value from `vllm.v1.attention.backends.registry.AttentionBackendEnum`

(e.g. `FLASH_ATTN`

).

###

`mm_encoder_attn_dtype = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_encoder_attn_dtype)

Optional dtype override for ViT encoder attention. Set to `"fp8"`

to enable FP8 quantization via the FlashInfer cuDNN backend. When set to `"fp8"`

without a scale file, dynamic scaling is used automatically. See docs/features/quantization/fp8_vit_attn.md for details.

###

`mm_encoder_fp8_scale_path = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_encoder_fp8_scale_path)

Path to a JSON file containing per-layer FP8 Q/K/V scales for ViT encoder attention. When provided (with `mm_encoder_attn_dtype="fp8"`

), static scaling is used. When omitted, dynamic scaling is used.

###

`mm_encoder_fp8_scale_save_margin = Field(default=1.5, gt=0.0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_encoder_fp8_scale_save_margin)

Safety margin multiplied onto scales when auto-saving. A value > 1 leaves headroom so that inputs with larger activations than the calibration set do not overflow FP8 range. Default 1.5.

###

`mm_encoder_fp8_scale_save_path = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_encoder_fp8_scale_save_path)

When set with dynamic FP8 scaling (`mm_encoder_attn_dtype="fp8"`

and no `mm_encoder_fp8_scale_path`

), saves the calibrated scales to this file after the amax history buffer is full. The saved file can then be used as `mm_encoder_fp8_scale_path`

in subsequent runs.

###

`mm_encoder_only = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_encoder_only)

When enabled, skips the language component of the model.

This is usually only valid in disaggregated Encoder process.

###

`mm_encoder_tp_mode = 'weights'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_encoder_tp_mode)

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

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_hasher_algorithm)

Hash algorithm to use for multi-modal input caching. Use `"sha256"`

or `"sha512"`

for FIPS-compliant deployments.

###

`mm_ipc_gpu_memory_gb = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_ipc_gpu_memory_gb)

Amount of GPU memory (in GiB) sequestered on the engine's device for GPU-side multimodal work in the API-server (frontend) process, such as hardware video decoding.

This budget is carved out of the engine's KV-cache memory so the headroom physically exists, and frontend GPU decode paths acquire from a blocking byte-counting semaphore of this size before allocating on the device.

Set to `0`

(default) to disable frontend GPU multimodal memory gating.

###

`mm_processor_cache_gb = Field(default=4, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_processor_cache_gb)

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

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_processor_cache_type)

Type of cache to use for the multi-modal preprocessor/mapper. If `shm`

, use shared memory FIFO cache. If `lru`

, use mirrored LRU cache.

###

`mm_processor_kwargs = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_processor_kwargs)

Arguments to be forwarded to the model's processor for multi-modal data, e.g., image processor. Overrides for the multi-modal processor obtained from `transformers.AutoProcessor.from_pretrained`

.

The available overrides depend on the model that is being run.

For example, for Phi-3-Vision: `{"num_crops": 4}`

.

###

`mm_shm_cache_max_object_size_mb = Field(default=128, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_shm_cache_max_object_size_mb)

Size limit (in MiB) for each object stored in the multi-modal processor shared memory cache. Only effective when `mm_processor_cache_type`

is `"shm"`

.

###

`mm_tensor_ipc = 'direct_rpc'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.mm_tensor_ipc)

IPC (inter-process communication) method for multimodal tensors. - "direct_rpc": Use msgspec serialization via RPC - "torch_shm": Use torch.multiprocessing shared memory for zero-copy IPC Defaults to "direct_rpc".

###

`skip_mm_profiling = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.skip_mm_profiling)

When enabled, skips multimodal memory profiling and only profiles with language backbone model during engine initialization.

This reduces engine startup time but shifts the responsibility to users for estimating the peak memory usage of the activation of multimodal encoder and embedding cache.

###

`video_pruning_method = 'evs'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.video_pruning_method)

Video token pruning algorithm applied when `video_pruning_rate`

> 0: - "evs": Efficient Video Sampling. - "vidcom2": Video Compression Commander.

###

`video_pruning_rate = Field(default=None, ge=0.0, lt=1.0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.video_pruning_rate)

Fraction of video tokens to prune from each video. Value sits in range [0;1); pruning is enabled when it is greater than 0. The pruning algorithm is selected by `video_pruning_method`

.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

## Source code in `vllm/config/multimodal.py`


###

`fold_mm_processor_device(mm_processor_kwargs, mm_processor_device)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.fold_mm_processor_device)

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

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.fold_mm_processor_device(mm_processor_kwargs))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | NoneThe kwargs as given, or None.

-

(`mm_processor_device`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.fold_mm_processor_device(mm_processor_device))

) –[MMProcessorDevice](https://docs.vllm.ai#vllm.config.multimodal.MMProcessorDevice)| NoneThe flag's value, or None when unset.


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

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.get_limit_per_prompt)

Get the maximum number of input items allowed per prompt for the given modality (backward compatible).

## Source code in `vllm/config/multimodal.py`


###

`get_mm_processor_device_type()`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.get_mm_processor_device_type)

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

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.get_video_pruning_spec)

Return `(method, rate)`

when video pruning is enabled, else None. `rate`

is the fraction of video tokens to prune.

## Source code in `vllm/config/multimodal.py`


###

`merge_mm_processor_kwargs(inference_kwargs)`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.merge_mm_processor_kwargs)

Get the keyword arguments to pass to the multi-modal processor according to the extra arguments passed during inference.

## Source code in `vllm/config/multimodal.py`


###

`use_gpu_video_backend()`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.use_gpu_video_backend)

Return whether the configured video loader or codec uses the GPU.

## Source code in `vllm/config/multimodal.py`


###

`validate_mm_processor_device(ec_config)`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.validate_mm_processor_device)

Check `mm_processor_kwargs["device"]`

for this deployment.

The only place the requested device is validated, so it runs even on a CPU-only platform: the value is parsed before any early return.

Parameters:

-

(`ec_config`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalConfig.validate_mm_processor_device(ec_config))

) –[ECTransferConfig](https://docs.vllm.ai/ec_transfer/#vllm.config.ec_transfer.ECTransferConfig)| NoneThe deployment's EC config, or None when it is not an encode/prefill/decode deployment. Passed in because it is not reachable from here, and because a field assigned after construction would not re-trigger this config's validators.


Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)If the requested device is not a torch device, or if it is the accelerator on an instance that also runs the language model.


## Source code in `vllm/config/multimodal.py`


##

`MultiModalDummyOptions`

[¶](https://docs.vllm.ai#vllm.config.multimodal.MultiModalDummyOptions)

Bases: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), [BaseDummyOptions](https://docs.vllm.ai#vllm.config.multimodal.BaseDummyOptions)]

Dummy data options for each modality.

Lookups of the modalities predefined by vLLM return their own options class, while any other modality returns [ BaseDummyOptions](https://docs.vllm.ai#vllm.config.multimodal.BaseDummyOptions).

## Source code in `vllm/config/multimodal.py`


##

`VideoDummyOptions`

[¶](https://docs.vllm.ai#vllm.config.multimodal.VideoDummyOptions)

Bases: [BaseDummyOptions](https://docs.vllm.ai#vllm.config.multimodal.BaseDummyOptions)

Options for generating dummy video data during profiling.