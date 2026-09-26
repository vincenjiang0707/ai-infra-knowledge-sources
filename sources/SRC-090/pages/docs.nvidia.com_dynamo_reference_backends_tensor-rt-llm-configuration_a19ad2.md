source: https://docs.nvidia.com/dynamo/reference/backends/tensor-rt-llm-configuration
lastmod: 2026-09-24T19:58:16.636Z

TensorRT-LLM Configuration (DynamoTrtllmConfig)


TensorRT-LLM Configuration (DynamoTrtllmConfig)

Field reference for the Dynamo-specific CLI flags and environment variables of the TensorRT-LLM backend wrapper.

`DynamoTrtllmConfig`

holds the Dynamo-specific configuration for the TensorRT-LLM backend (`python -m dynamo.trtllm`

). Every field, type, default, and choice on this page comes from the [ DynamoTrtllmArgGroup and DynamoTrtllmConfig](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/components/src/dynamo/trtllm/backend_args.py) definitions. For features and operational details, see the


[TensorRT-LLM Reference Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/tensor-rt-llm/reference-guide).

Unlike the vLLM and SGLang backends, TensorRT-LLM’s engine configuration is largely owned by the Dynamo flags on this page directly — parallelism, batch limits, and KV cache sizing are all specified here rather than passed through a separate engine config object. Additional low-level engine settings that are not exposed as first-class flags can be supplied via `--extra-engine-args`

(a YAML file) or `--override-engine-args`

(an inline Python dict string). These flags plus the cross-cutting [Dynamo Runtime](https://docs.nvidia.com/dynamo/reference/components/runtime-configuration) flags (`--namespace`

, `--endpoint`

, tool/reasoning parsers) form the complete Dynamo configuration surface for this backend.

## How the config is loaded

Each field is both a CLI flag and an environment variable. The CLI flag takes precedence; the environment variable is the fallback. Boolean fields are negatable — `--enable-attention-dp`

sets it on, `--no-enable-attention-dp`

sets it off.

## Model loading

Path to a disk model or HuggingFace model identifier to load. Accepts a local filesystem path or any model name resolvable by the HuggingFace Hub.

Environment variable: `DYN_TRTLLM_MODEL`


Name to serve the model under in the API. When unset, the served name is derived automatically from the model path.

Environment variable: `DYN_TRTLLM_SERVED_MODEL_NAME`


Model weight loading format passed to TensorRT-LLM. Use `auto`

to let TRT-LLM detect the format, or specify a format such as `gms`

for GMS read-only checkpoints.

Environment variable: `DYN_TRTLLM_LOAD_FORMAT`


JSON object passed as extra configuration to the model loader. For example, `'{"gms_read_only": true}'`

enables read-only GMS loading.

Environment variable: `DYN_TRTLLM_MODEL_LOADER_EXTRA_CONFIG`


## Parallelism

Tensor parallelism degree — the number of GPUs across which each layer’s weight tensors are split. Must divide evenly into the total GPU count.

Environment variable: `DYN_TRTLLM_TENSOR_PARALLEL_SIZE`


Pipeline parallelism degree — the number of pipeline stages across which the model layers are distributed. Set to 1 for no pipeline parallelism.

Environment variable: `DYN_TRTLLM_PIPELINE_PARALLEL_SIZE`


Expert parallelism degree for mixture-of-experts models. When unset, expert parallelism is not applied.

Environment variable: `DYN_TRTLLM_EXPERT_PARALLEL_SIZE`


Enable attention data parallelism. When enabled, `attention_dp_size`

is set equal to `tensor_parallel_size`

, distributing attention heads across data-parallel ranks.

Environment variable: `DYN_TRTLLM_ENABLE_ATTENTION_DP`


Number of GPUs per node. When unset, Dynamo infers the value from the environment (for example, from `CUDA_VISIBLE_DEVICES`

or the system topology).

Environment variable: `DYN_TRTLLM_GPUS_PER_NODE`


## Batch and sequence limits

Maximum number of requests that the TRT-LLM engine can schedule in a single forward pass. This value is baked into the compiled engine. When unset, it inherits the default from TensorRT-LLM’s `BuildConfig`

(`2048`

at the time of writing; the authoritative value is whatever the pinned TRT-LLM version ships).

Environment variable: `DYN_TRTLLM_MAX_BATCH_SIZE`


Maximum number of batched input tokens after padding is removed in each batch. Increasing this allows larger effective batch throughput at the cost of more memory. When unset, it inherits the default from TensorRT-LLM’s `BuildConfig`

(`8192`

at the time of writing; the authoritative value is whatever the pinned TRT-LLM version ships).

Environment variable: `DYN_TRTLLM_MAX_NUM_TOKENS`


Maximum total length of a single request in tokens, including both prompt and output tokens. When unset, the value is deduced from the model configuration by TensorRT-LLM’s `BuildConfig`

.

Environment variable: `DYN_TRTLLM_MAX_SEQ_LEN`


Maximum number of beams for beam search decoding. Set to `1`

for greedy or sampling decoding (no beam search). When unset, it inherits the default from TensorRT-LLM’s `BuildConfig`

(`1`

at the time of writing).

Environment variable: `DYN_TRTLLM_MAX_BEAM_WIDTH`


## KV cache and events

Size of a single KV cache block in tokens. Larger blocks improve memory-copy efficiency but reduce cache granularity and reuse flexibility.

Environment variable: `DYN_TRTLLM_KV_BLOCK_SIZE`


Fraction of free GPU memory (after model weights and buffers are allocated) to reserve for the KV cache pool. Valid range is `(0.0, 1.0]`

.

Environment variable: `DYN_TRTLLM_FREE_GPU_MEMORY_FRACTION`


Publish KV cache events to the Dynamo KV router, enabling KV-aware routing and disaggregated KV transfer. The `dynamo_component_*`

gauges and `trtllm_*`

vendor metrics emit unconditionally regardless of this flag. The legacy flag name `--publish-events-and-metrics`

is also accepted but deprecated.

Environment variable: `DYN_TRTLLM_PUBLISH_KV_EVENTS`


## Engine args passthrough

Path to a YAML file containing additional keyword arguments to pass through to the TRT-LLM engine at build/load time. Use this for low-level engine settings not exposed as first-class flags.

Environment variable: `DYN_TRTLLM_EXTRA_ENGINE_ARGS`


Python dictionary string that overrides specific engine arguments sourced from the YAML file specified by `--extra-engine-args`

. Applied after the YAML is loaded, so it takes precedence. Example: `'{"tensor_parallel_size": 2, "kv_cache_config": {"enable_block_reuse": false}}'`

.

Environment variable: `DYN_TRTLLM_OVERRIDE_ENGINE_ARGS`


## Disaggregation and multimodal

Worker disaggregation role. Use `agg`

for a standard aggregated (prefill + decode) serving worker, `pd`

for a combined prefill+decode disaggregated worker, or `prefill`

, `decode`

, or `encode`

for individual disaggregated worker roles. The removed `prefill_and_decode`

value is rejected; use `agg`

or `pd`

.

Environment variable: `DYN_TRTLLM_DISAGGREGATION_MODE`


Enable multimodal LLM request processing (vision-language models). For diffusion modalities (video/image generation), use `--modality`

instead; `--enable-multimodal`

cannot be combined with diffusion modalities.

Environment variable: `DYN_TRTLLM_ENABLE_MULTIMODAL`


Modality of the served model. For multimodal LLM serving (vision-language), prefer `--enable-multimodal`

; use `--modality`

to select diffusion model types.

Environment variable: `DYN_TRTLLM_MODALITY`


Dynamo endpoint address (in `dyn://namespace.component.endpoint`

format) for the encode worker in a multimodal EPD topology. Required when running a decode-only worker that delegates encoding to a remote encode worker.

Environment variable: `DYN_TRTLLM_ENCODE_ENDPOINT`


Path to a local directory that the model is permitted to access for reading media files (images, video). Requests referencing files outside this path will be rejected.

Environment variable: `DYN_TRTLLM_ALLOWED_LOCAL_MEDIA_PATH`


Maximum size in megabytes of downloadable embedding files or image URLs. Requests referencing files larger than this limit will be rejected.

Environment variable: `DYN_TRTLLM_MAX_FILE_SIZE_MB`


Enable frontend decoding of multimodal images. Images are decoded in the Rust frontend and transferred to the backend via NIXL RDMA, bypassing in-engine HTTP fetch and decode. Engine-specific topology constraints may apply.

Environment variable: `DYN_TRTLLM_FRONTEND_DECODING`


## Guided decoding

Backend to use for guided decoding (structured output generation). When unset, guided decoding is disabled. Both `xgrammar`

and `llguidance`

provide grammar-constrained generation for JSON schema, regex, and similar output formats.

Environment variable: `DYN_TRTLLM_GUIDED_DECODING_BACKEND`


## Diffusion (experimental)

*These flags configure the experimental diffusion pipeline (video and image generation). They are only relevant when --modality is set to video_diffusion or image_diffusion. See *



[TensorRT-LLM Diffusion](https://docs.nvidia.com/dynamo/diffusion/overview)for usage details.

Quantization algorithm for diffusion models. BF16 weights are quantized on-the-fly during loading. When unset, no quantization is applied.

Allowed values: FP8 FP8_BLOCK_SCALES NVFP4 W4A16_AWQ W4A8_AWQ W8A8_SQ_PER_CHANNELEnvironment variable: `DYN_TRTLLM_QUANT_ALGO`


Enable dynamic weight quantization — BF16 weights are quantized on-the-fly during model loading. Disable (`--no-quant-dynamic`

) to use static pre-quantized weights.

Environment variable: `DYN_TRTLLM_QUANT_DYNAMIC`


Enable TeaCache optimization for faster diffusion generation by caching and reusing transformer hidden states across timesteps.

Environment variable: `DYN_TRTLLM_ENABLE_TEACACHE`


Use retention steps for TeaCache. When enabled, TeaCache selects which timesteps to cache based on a retention-step schedule.

Environment variable: `DYN_TRTLLM_TEACACHE_USE_RET_STEPS`


TeaCache similarity threshold. Hidden states whose cosine distance to the cached state falls below this threshold are reused rather than recomputed.

Environment variable: `DYN_TRTLLM_TEACACHE_THRESH`


Torch data type for diffusion model loading. `bfloat16`

is recommended for Ampere and later GPUs.

Environment variable: `DYN_TRTLLM_TORCH_DTYPE`


HuggingFace Hub revision (branch name, tag, or full commit SHA) used when downloading the diffusion model. When unset, the default branch is used.

Environment variable: `DYN_TRTLLM_REVISION`


Disable `torch.compile`

optimization for the diffusion transformer. By default, `torch.compile`

is applied; set this flag to fall back to eager mode.

Environment variable: `DYN_TRTLLM_DISABLE_TORCH_COMPILE`


Enable `torch.compile`

fullgraph mode, which enforces that the entire model graph is compiled without graph breaks. Stricter than the default partial-graph mode, but can yield better performance when the model is fully compatible.

Environment variable: `DYN_TRTLLM_ENABLE_FULLGRAPH`


Enable CUDA graph capture for diffusion transformer forward passes. Can reduce kernel-launch overhead significantly for fixed-shape workloads. Mutually exclusive with `torch.compile`

.

Environment variable: `DYN_TRTLLM_ENABLE_CUDA_GRAPH`


Attention backend for diffusion transformer layers. `VANILLA`

uses PyTorch’s scaled dot-product attention (SDPA); `TRTLLM`

uses TensorRT-LLM optimized attention kernels.

Environment variable: `DYN_TRTLLM_ATTN_BACKEND`


Ulysses sequence-parallel degree for the Diffusion Transformer (DiT). Set to values greater than 1 to distribute sequence-dimension attention across multiple ranks.

Environment variable: `DYN_TRTLLM_DIT_ULYSSES_SIZE`


Ring attention parallel degree for the DiT. Set to values greater than 1 to use ring-style attention parallelism across multiple ranks.

Environment variable: `DYN_TRTLLM_DIT_RING_SIZE`


Classifier-Free Guidance (CFG) parallel degree for the DiT. Set to values greater than 1 to distribute conditional and unconditional forward passes across ranks.

Environment variable: `DYN_TRTLLM_DIT_CFG_SIZE`


Enable per-layer NVTX range markers in the diffusion forward pass. Use with NVIDIA Nsight Systems to attribute GPU time to individual transformer layers.

Environment variable: `DYN_TRTLLM_ENABLE_LAYERWISE_NVTX_MARKER`


Skip the warmup inference pass during initialization. Useful for faster startup in development or testing; not recommended for production as it defers first-request latency.

Environment variable: `DYN_TRTLLM_SKIP_WARMUP`


## Diffusion request defaults (experimental)

*These flags set the default values applied to video and image generation requests that do not specify the corresponding parameter. They are only relevant when --modality is video_diffusion or image_diffusion. See *



[TensorRT-LLM Diffusion](https://docs.nvidia.com/dynamo/diffusion/overview)for usage details.

Default output height in pixels for video or image generation requests that do not specify a height.

Environment variable: `DYN_TRTLLM_DEFAULT_HEIGHT`


Default output width in pixels for video or image generation requests that do not specify a width.

Environment variable: `DYN_TRTLLM_DEFAULT_WIDTH`


Default number of diffusion denoising steps for requests that do not specify a step count. More steps generally improve quality but increase latency.

Environment variable: `DYN_TRTLLM_DEFAULT_NUM_INFERENCE_STEPS`


Default Classifier-Free Guidance (CFG) scale applied to generation requests that do not specify a guidance scale. Higher values increase adherence to the text prompt at the cost of diversity.

Environment variable: `DYN_TRTLLM_DEFAULT_GUIDANCE_SCALE`


Default number of frames for video generation requests that do not specify a frame count.

Environment variable: `DYN_TRTLLM_DEFAULT_NUM_FRAMES`


Default number of images to generate per prompt for image generation requests that do not specify a count.

Environment variable: `DYN_TRTLLM_DEFAULT_NUM_IMAGES_PER_PROMPT`