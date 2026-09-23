source: https://docs.vllm.ai/en/latest/api/vllm/
lastmod: 2026-09-23

#

`vllm`

[¶](https://docs.vllm.ai#vllm)

vLLM: a high-throughput and memory-efficient inference engine for LLMs.

Modules:

-
–[assets](https://docs.vllm.ai/assets/#vllm.assets) -
–[benchmarks](https://docs.vllm.ai/benchmarks/#vllm.benchmarks) -
–[collect_env](https://docs.vllm.ai/collect_env/#vllm.collect_env) -
–[compilation](https://docs.vllm.ai/compilation/#vllm.compilation) -
–[config](https://docs.vllm.ai/config/#vllm.config) -
–[connections](https://docs.vllm.ai/connections/#vllm.connections) -
–[cute_utils](https://docs.vllm.ai/cute_utils/#vllm.cute_utils) -
–[device_allocator](https://docs.vllm.ai/device_allocator/#vllm.device_allocator) -
–[distributed](https://docs.vllm.ai/distributed/#vllm.distributed) -
–[engine](https://docs.vllm.ai/engine/#vllm.engine) -
–[entrypoints](https://docs.vllm.ai/entrypoints/#vllm.entrypoints) -
–[env_override](https://docs.vllm.ai/env_override/#vllm.env_override) -
–[envs](https://docs.vllm.ai/envs/#vllm.envs) -
–[exceptions](https://docs.vllm.ai/exceptions/#vllm.exceptions)Custom exceptions for vLLM.

-
–[forward_context](https://docs.vllm.ai/forward_context/#vllm.forward_context) -
–[inputs](https://docs.vllm.ai/inputs/#vllm.inputs) -
–[ir](https://docs.vllm.ai/ir/#vllm.ir) -
–[kernels](https://docs.vllm.ai/kernels/#vllm.kernels)Kernel implementations for vLLM.

-
–[logger](https://docs.vllm.ai/logger/#vllm.logger)Logging configuration for vLLM.

-
–[logging_utils](https://docs.vllm.ai/logging_utils/#vllm.logging_utils) -
–[logits_process](https://docs.vllm.ai/logits_process/#vllm.logits_process) -
–[logprobs](https://docs.vllm.ai/logprobs/#vllm.logprobs) -
–[lora](https://docs.vllm.ai/lora/#vllm.lora) -
–[model_executor](https://docs.vllm.ai/model_executor/#vllm.model_executor) -
–[model_inspection](https://docs.vllm.ai/model_inspection/#vllm.model_inspection)Model inspection utilities for vLLM.

-
–[models](https://docs.vllm.ai/models/#vllm.models) -
–[multimodal](https://docs.vllm.ai/multimodal/#vllm.multimodal) -
–[outputs](https://docs.vllm.ai/outputs/#vllm.outputs) -
–[parser](https://docs.vllm.ai/parser/#vllm.parser) -
–[platforms](https://docs.vllm.ai/platforms/#vllm.platforms) -
–[plugins](https://docs.vllm.ai/plugins/#vllm.plugins) -
–[pooling_params](https://docs.vllm.ai/pooling_params/#vllm.pooling_params) -
–[profiler](https://docs.vllm.ai/profiler/#vllm.profiler) -
–[ray](https://docs.vllm.ai/ray/#vllm.ray) -
–[reasoning](https://docs.vllm.ai/reasoning/#vllm.reasoning) -
–[renderers](https://docs.vllm.ai/renderers/#vllm.renderers) -
–[sampling_params](https://docs.vllm.ai/sampling_params/#vllm.sampling_params)Sampling parameters for text generation.

-
–[scalar_type](https://docs.vllm.ai/scalar_type/#vllm.scalar_type) -
–[sequence](https://docs.vllm.ai/sequence/#vllm.sequence)Sequence and its related classes.

-
–[snapshot](https://docs.vllm.ai/snapshot/#vllm.snapshot)Create and restore explicitly compatible vLLM engine snapshots.

-
–`third_party`

-
–[tilelang_utils](https://docs.vllm.ai/tilelang_utils/#vllm.tilelang_utils) -
–[tokenizers](https://docs.vllm.ai/tokenizers/#vllm.tokenizers) -
–[tool_parsers](https://docs.vllm.ai/tool_parsers/#vllm.tool_parsers) -
–[tracing](https://docs.vllm.ai/tracing/#vllm.tracing) -
–[transformers_utils](https://docs.vllm.ai/transformers_utils/#vllm.transformers_utils) -
–[triton_utils](https://docs.vllm.ai/triton_utils/#vllm.triton_utils) -
–[usage](https://docs.vllm.ai/usage/#vllm.usage) -
–[utils](https://docs.vllm.ai/utils/#vllm.utils) -
–[v1](https://docs.vllm.ai/v1/#vllm.v1) -
–[version](https://docs.vllm.ai/version/#vllm.version) -
–`vllm_flash_attn`


Classes:

-
–[AsyncEngineArgs](https://docs.vllm.ai#vllm.AsyncEngineArgs)Arguments for asynchronous vLLM engine.

-
–[ClassificationOutput](https://docs.vllm.ai#vllm.ClassificationOutput)The output data of one classification output of a request.

-
–[CompletionOutput](https://docs.vllm.ai#vllm.CompletionOutput)The output data of one completion output of a request.

-
–[EmbeddingOutput](https://docs.vllm.ai#vllm.EmbeddingOutput)The output data of one embedding output of a request.

-
–[EngineArgs](https://docs.vllm.ai#vllm.EngineArgs)Arguments for vLLM engine.

-
–[LLM](https://docs.vllm.ai#vllm.LLM)An LLM for generating texts from given prompts and sampling parameters.

-
–[PoolingOutput](https://docs.vllm.ai#vllm.PoolingOutput)The output data of one pooling output of a request.

-
–[PoolingParams](https://docs.vllm.ai#vllm.PoolingParams)API parameters for pooling models.

-
–[PoolingRequestOutput](https://docs.vllm.ai#vllm.PoolingRequestOutput)The output data of a pooling request to the LLM.

-
–[RequestOutput](https://docs.vllm.ai#vllm.RequestOutput)The output data of a completion request to the LLM.

-
–[SamplingParams](https://docs.vllm.ai#vllm.SamplingParams)Sampling parameters for text generation.

-
–[ScoringOutput](https://docs.vllm.ai#vllm.ScoringOutput)The output data of one scoring output of a request.

-
–[TextPrompt](https://docs.vllm.ai#vllm.TextPrompt)Schema for a text prompt.

-
–[TokensPrompt](https://docs.vllm.ai#vllm.TokensPrompt)Schema for a tokenized prompt.


Functions:

-
–[initialize_ray_cluster](https://docs.vllm.ai#vllm.initialize_ray_cluster)Initialize the distributed cluster with Ray.


Attributes:

-
–[AsyncLLMEngine](https://docs.vllm.ai#vllm.AsyncLLMEngine)The

`AsyncLLMEngine`

class is an alias of[vllm.v1.engine.async_llm.AsyncLLM](https://docs.vllm.ai/v1/engine/async_llm/#vllm.v1.engine.async_llm.AsyncLLM). -
–[LLMEngine](https://docs.vllm.ai#vllm.LLMEngine)The

`LLMEngine`

class is an alias of[vllm.v1.engine.llm_engine.LLMEngine](https://docs.vllm.ai/v1/engine/llm_engine/#vllm.v1.engine.llm_engine.LLMEngine). -
([PromptType](https://docs.vllm.ai#vllm.PromptType)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)Schema for any prompt, regardless of model type.


##

`AsyncLLMEngine = AsyncLLM`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.AsyncLLMEngine)

The `AsyncLLMEngine`

class is an alias of [vllm.v1.engine.async_llm.AsyncLLM](https://docs.vllm.ai/v1/engine/async_llm/#vllm.v1.engine.async_llm.AsyncLLM).

##

`LLMEngine = V1LLMEngine`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.LLMEngine)

The `LLMEngine`

class is an alias of [vllm.v1.engine.llm_engine.LLMEngine](https://docs.vllm.ai/v1/engine/llm_engine/#vllm.v1.engine.llm_engine.LLMEngine).

##

`PromptType = DecoderOnlyPrompt | EncoderDecoderPrompt`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.PromptType)

Schema for any prompt, regardless of model type.

This is the input format accepted by most [ LLM](https://docs.vllm.ai/entrypoints/llm/#vllm.entrypoints.llm.LLM) APIs.

##

`AsyncEngineArgs`

`dataclass`

[¶](https://docs.vllm.ai#vllm.AsyncEngineArgs)

Bases: [EngineArgs](https://docs.vllm.ai/engine/arg_utils/#vllm.engine.arg_utils.EngineArgs)

Arguments for asynchronous vLLM engine.

## Source code in `vllm/engine/arg_utils.py`


##

`ClassificationOutput`

`dataclass`

[¶](https://docs.vllm.ai#vllm.ClassificationOutput)

The output data of one classification output of a request.

Parameters:

-

(`probs`

[¶](https://docs.vllm.ai#vllm.ClassificationOutput(probs))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[float](https://docs.python.org/3/builtins/functions.html#float)]The probability vector, which is a list of floats. Its length depends on the number of classes.


## Source code in `vllm/outputs.py`


##

`CompletionOutput`

`dataclass`

[¶](https://docs.vllm.ai#vllm.CompletionOutput)

The output data of one completion output of a request.

Parameters:

-

(`index`

[¶](https://docs.vllm.ai#vllm.CompletionOutput(index))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The index of the output in the request.

-

(`text`

[¶](https://docs.vllm.ai#vllm.CompletionOutput(text))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The generated output text.

-

(`token_ids`

[¶](https://docs.vllm.ai#vllm.CompletionOutput(token_ids))

) –[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[int](https://docs.python.org/3/builtins/functions.html#int)]The token IDs of the generated output text.

-

(`cumulative_logprob`

[¶](https://docs.vllm.ai#vllm.CompletionOutput(cumulative_logprob))

) –[float](https://docs.python.org/3/builtins/functions.html#float)| NoneThe cumulative log probability of the generated output text.

-

(`logprobs`

[¶](https://docs.vllm.ai#vllm.CompletionOutput(logprobs))`SampleLogprobs | None`

) –The log probabilities of the top probability words at each position if the logprobs are requested.

-

(`sampling_mask`

[¶](https://docs.vllm.ai#vllm.CompletionOutput(sampling_mask))

, default:[SamplingMask](https://docs.vllm.ai/outputs/#vllm.outputs.SamplingMask)| None`None`

) –The post-processing token support set for each generated token, if requested.

-

(`finish_reason`

[¶](https://docs.vllm.ai#vllm.CompletionOutput(finish_reason))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –The reason why the sequence is finished.

-

(`stop_reason`

[¶](https://docs.vllm.ai#vllm.CompletionOutput(stop_reason))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)|[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –The stop string or token id that caused the completion to stop, None if the completion finished for some other reason including encountering the EOS token.

-

(`lora_request`

[¶](https://docs.vllm.ai#vllm.CompletionOutput(lora_request))

, default:[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)| None`None`

) –The LoRA request that was used to generate the output.

-

(`spec_decode_metrics`

[¶](https://docs.vllm.ai#vllm.CompletionOutput(spec_decode_metrics))

, default:[RequestSpecDecodeMetrics](https://docs.vllm.ai/v1/metrics/stats/#vllm.v1.metrics.stats.RequestSpecDecodeMetrics)| None`None`

) –Per-sequence speculative-decoding acceptance metrics, populated on finish when speculative decoding ran and

`--per-request-spec-decode-metrics`

is enabled; None otherwise. Surfaced in the response as`metrics.speculative_decoding`

for single-sequence (`n == 1`

) requests.

## Source code in `vllm/outputs.py`


##

`EmbeddingOutput`

`dataclass`

[¶](https://docs.vllm.ai#vllm.EmbeddingOutput)

The output data of one embedding output of a request.

Parameters:

-

(`embedding`

[¶](https://docs.vllm.ai#vllm.EmbeddingOutput(embedding))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[float](https://docs.python.org/3/builtins/functions.html#float)]The embedding vector, which is a list of floats. Its length depends on the hidden dimension of the model.


## Source code in `vllm/outputs.py`


##

`EngineArgs`

`dataclass`

[¶](https://docs.vllm.ai#vllm.EngineArgs)

Arguments for vLLM engine.

Methods:

-
–[add_cli_args](https://docs.vllm.ai#vllm.EngineArgs.add_cli_args)Shared CLI arguments for vLLM engine.

-
–[create_engine_config](https://docs.vllm.ai#vllm.EngineArgs.create_engine_config)Create the VllmConfig.

-
–[create_speculative_config](https://docs.vllm.ai#vllm.EngineArgs.create_speculative_config)Initializes and returns a SpeculativeConfig object based on


Attributes:

-
([logits_processors](https://docs.vllm.ai#vllm.EngineArgs.logits_processors)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)|[type](https://docs.python.org/3/builtins/functions.html#type)[[LogitsProcessor](https://docs.vllm.ai/v1/sample/logits_processor/#vllm.v1.sample.logits_processor.LogitsProcessor)]] | NoneCustom logitproc types

-
([quantization_config](https://docs.vllm.ai#vllm.EngineArgs.quantization_config)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] |[QuantizationConfigArgs](https://docs.vllm.ai/config/quantization/#vllm.config.quantization.QuantizationConfigArgs)| NoneUser-facing quantization configuration. Carries per-layer-kind


## Source code in `vllm/engine/arg_utils.py`


|
|

###

`logits_processors = ModelConfig.logits_processors`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.EngineArgs.logits_processors)

Custom logitproc types

###

`quantization_config = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.EngineArgs.quantization_config)

User-facing quantization configuration. Carries per-layer-kind QuantSpecs (linear, moe) and ignore patterns; see :class:`QuantizationConfigArgs`

. Auto-populated from the matching online shorthand when `quantization`

is one of the values in `ONLINE_QUANT_SHORTHAND_NAMES`

.

###

`_check_feature_supported()`

[¶](https://docs.vllm.ai#vllm.EngineArgs._check_feature_supported)

Raise an error if the feature is not supported.

## Source code in `vllm/engine/arg_utils.py`


###

`_get_min_mm_batched_tokens(model_config)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.EngineArgs._get_min_mm_batched_tokens)

Get the minimum max_num_batched_tokens needed for a multimodal prefix-LM model to process at least one item of any supported modality.

Returns (token_count, modality_name) for the most expensive modality, or None if the value cannot be determined at this stage.

## Source code in `vllm/engine/arg_utils.py`


###

`add_cli_args(parser)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.EngineArgs.add_cli_args)

Shared CLI arguments for vLLM engine.

## Source code in `vllm/engine/arg_utils.py`


|
|

###

`create_engine_config(usage_context=None, headless=False)`

[¶](https://docs.vllm.ai#vllm.EngineArgs.create_engine_config)

Create the VllmConfig.

NOTE: If VllmConfig is incompatible, we raise an error.

## Source code in `vllm/engine/arg_utils.py`


|
|

###

`create_speculative_config(target_model_config, target_parallel_config)`

[¶](https://docs.vllm.ai#vllm.EngineArgs.create_speculative_config)

Initializes and returns a SpeculativeConfig object based on `speculative_config`

.

## Source code in `vllm/engine/arg_utils.py`


##

`LLM`

[¶](https://docs.vllm.ai#vllm.LLM)

Bases:

, [BeamSearchOfflineMixin](https://docs.vllm.ai/entrypoints/generate/beam_search/offline/#vllm.entrypoints.generate.beam_search.offline.BeamSearchOfflineMixin)

, [PoolingOfflineMixin](https://docs.vllm.ai/entrypoints/pooling/offline/#vllm.entrypoints.pooling.offline.PoolingOfflineMixin)[OfflineInferenceMixin](https://docs.vllm.ai/entrypoints/offline_utils/#vllm.entrypoints.offline_utils.OfflineInferenceMixin)

An LLM for generating texts from given prompts and sampling parameters.

This class includes a tokenizer, a language model (possibly distributed across multiple GPUs), and GPU memory space allocated for intermediate states (aka KV cache). Given a batch of prompts and sampling parameters, this class generates texts from the model, using an intelligent batching mechanism and efficient memory management.

Parameters:

-

(`model`

[¶](https://docs.vllm.ai#vllm.LLM(model))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The name or path of a HuggingFace Transformers model.

-

(`tokenizer`

[¶](https://docs.vllm.ai#vllm.LLM(tokenizer))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –The name or path of a HuggingFace Transformers tokenizer.

-

(`tokenizer_mode`

[¶](https://docs.vllm.ai#vllm.LLM(tokenizer_mode))`TokenizerMode |`

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'auto'`

) –The tokenizer mode. "auto" will use the fast tokenizer if available, and "slow" will always use the slow tokenizer.

-

(`skip_tokenizer_init`

[¶](https://docs.vllm.ai#vllm.LLM(skip_tokenizer_init))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If true, skip initialization of tokenizer and detokenizer. Expect valid prompt_token_ids and None for prompt from the input.

-

(`trust_remote_code`

[¶](https://docs.vllm.ai#vllm.LLM(trust_remote_code))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Trust remote code (e.g., from HuggingFace) when downloading the model and tokenizer.

-

(`allowed_local_media_path`

[¶](https://docs.vllm.ai#vllm.LLM(allowed_local_media_path))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –Allowing API requests to read local images or videos from directories specified by the server file system. This is a security risk. Should only be enabled in trusted environments.

-

(`allowed_media_domains`

[¶](https://docs.vllm.ai#vllm.LLM(allowed_media_domains))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None`None`

) –If set, only media URLs that belong to this domain can be used for multi-modal inputs.

-

(`tensor_parallel_size`

[¶](https://docs.vllm.ai#vllm.LLM(tensor_parallel_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –The number of GPUs to use for distributed execution with tensor parallelism.

-

(`dtype`

[¶](https://docs.vllm.ai#vllm.LLM(dtype))`ModelDType`

, default:`'auto'`

) –The data type for the model weights and activations. Currently, we support

`float32`

,`float16`

, and`bfloat16`

. If`auto`

, we use the`dtype`

attribute of the Transformers model's config. However, if the`dtype`

in the config is`float32`

, we will use`float16`

instead. -

(`quantization`

[¶](https://docs.vllm.ai#vllm.LLM(quantization))`QuantizationMethods | None`

, default:`None`

) –The method used to quantize the model weights. Currently, we support "awq", "gptq", and "fp8" (experimental). If None, we first check the

`quantization_config`

attribute in the model config file. If that is None, we assume the model weights are not quantized and use`dtype`

to determine the data type of the weights. -

(`revision`

[¶](https://docs.vllm.ai#vllm.LLM(revision))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –The specific model version to use. It can be a branch name, a tag name, or a commit id.

-

(`tokenizer_revision`

[¶](https://docs.vllm.ai#vllm.LLM(tokenizer_revision))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –The specific tokenizer version to use. It can be a branch name, a tag name, or a commit id.

-

(`chat_template`

[¶](https://docs.vllm.ai#vllm.LLM(chat_template))

, default:[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)|[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –The chat template to apply.

-

(`seed`

[¶](https://docs.vllm.ai#vllm.LLM(seed))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –The seed to initialize the random number generator for sampling.

-

(`gpu_memory_utilization`

[¶](https://docs.vllm.ai#vllm.LLM(gpu_memory_utilization))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)`0.92`

) –The ratio (between 0 and 1) of GPU memory to reserve for the model weights, activations, and KV cache. Higher values will increase the KV cache size and thus improve the model's throughput. However, if the value is too high, it may cause out-of- memory (OOM) errors.

-

(`kv_cache_memory_bytes`

[¶](https://docs.vllm.ai#vllm.LLM(kv_cache_memory_bytes))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Size of KV Cache per GPU in bytes. By default, this is set to None and vllm can automatically infer the kv cache size based on gpu_memory_utilization. However, users may want to manually specify the kv cache memory size. kv_cache_memory_bytes allows more fine-grain control of how much memory gets used when compared with using gpu_memory_utilization. Note that kv_cache_memory_bytes (when not-None) ignores gpu_memory_utilization

-

(`cpu_offload_gb`

[¶](https://docs.vllm.ai#vllm.LLM(cpu_offload_gb))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)`0`

) –The size (GiB) of CPU memory to use for offloading the model weights. This virtually increases the GPU memory space you can use to hold the model weights, at the cost of CPU-GPU data transfer for every forward pass.

-

(`offload_group_size`

[¶](https://docs.vllm.ai#vllm.LLM(offload_group_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –Prefetch offloading: Group every N layers together. Offload last

`offload_num_in_group`

layers of each group. Default is 0 (disabled). -

(`offload_num_in_group`

[¶](https://docs.vllm.ai#vllm.LLM(offload_num_in_group))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –Prefetch offloading: Number of layers to offload per group. Default is 1.

-

(`offload_prefetch_step`

[¶](https://docs.vllm.ai#vllm.LLM(offload_prefetch_step))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –Prefetch offloading: Number of layers to prefetch ahead. Higher values hide more latency but use more GPU memory. Default is 1.

-

(`offload_params`

[¶](https://docs.vllm.ai#vllm.LLM(offload_params))

, default:[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None`None`

) –Prefetch offloading: Set of parameter name segments to selectively offload. Only parameters whose names contain one of these segments will be offloaded (e.g., {"gate_up_proj", "down_proj"} for MLP weights, or {"w13_weight", "w2_weight"} for MoE expert weights). If None or empty, all parameters are offloaded.

-

(`enforce_eager`

[¶](https://docs.vllm.ai#vllm.LLM(enforce_eager))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether to enforce eager execution. If True, we will disable CUDA graph and always execute the model in eager mode. If False, we will use CUDA graph and eager execution in hybrid.

-

(`enable_return_routed_experts`

[¶](https://docs.vllm.ai#vllm.LLM(enable_return_routed_experts))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether to return routed experts.

-

(`disable_custom_all_reduce`

[¶](https://docs.vllm.ai#vllm.LLM(disable_custom_all_reduce))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –See

[ParallelConfig](https://docs.vllm.ai/config/#vllm.config.ParallelConfig). -

(`hf_token`

[¶](https://docs.vllm.ai#vllm.LLM(hf_token))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)|[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –The token to use as HTTP bearer authorization for remote files . If

`True`

, will use the token generated when running`hf auth login`

(stored in`~/.cache/huggingface/token`

). -

(`hf_overrides`

[¶](https://docs.vllm.ai#vllm.LLM(hf_overrides))`HfOverrides | None`

, default:`None`

) –If a dictionary, contains arguments to be forwarded to the HuggingFace config. If a callable, it is called to update the HuggingFace config.

-

(`mm_processor_kwargs`

[¶](https://docs.vllm.ai#vllm.LLM(mm_processor_kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Arguments to be forwarded to the model's processor for multi-modal data, e.g., image processor. Overrides for the multi-modal processor obtained from

`AutoProcessor.from_pretrained`

. The available overrides depend on the model that is being run. For example, for Phi-3-Vision:`{"num_crops": 4}`

. -

(`pooler_config`

[¶](https://docs.vllm.ai#vllm.LLM(pooler_config))

, default:[PoolerConfig](https://docs.vllm.ai/config/#vllm.config.PoolerConfig)| None`None`

) –Initialize non-default pooling config for the pooling model, e.g.,

`PoolerConfig(seq_pooling_type="MEAN", use_activation=False)`

. -

(`compilation_config`

[¶](https://docs.vllm.ai#vllm.LLM(compilation_config))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)|[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] |[CompilationConfig](https://docs.vllm.ai/config/#vllm.config.CompilationConfig)| None`None`

) –Either an integer or a dictionary. If it is an integer, it is used as the mode of compilation optimization. If it is a dictionary, it can specify the full compilation configuration.

-

(`attention_config`

[¶](https://docs.vllm.ai#vllm.LLM(attention_config))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] |[AttentionConfig](https://docs.vllm.ai/config/#vllm.config.AttentionConfig)| None`None`

) –Configuration for attention mechanisms. Can be a dictionary or an AttentionConfig instance. If a dictionary, it will be converted to an AttentionConfig. Allows specifying the attention backend and other attention-related settings.

-

(`return_sampling_mask`

[¶](https://docs.vllm.ai#vllm.LLM(return_sampling_mask))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Return each sampled token's post-processing support set. Requires Model Runner V2 and processed log probabilities.

-

(`spec_method`

[¶](https://docs.vllm.ai#vllm.LLM(spec_method))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –Top-level alias for

`speculative_config["method"]`

. -

(`spec_model`

[¶](https://docs.vllm.ai#vllm.LLM(spec_model))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –Top-level alias for

`speculative_config["model"]`

. -

(`spec_tokens`

[¶](https://docs.vllm.ai#vllm.LLM(spec_tokens))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Top-level alias for

`speculative_config["num_speculative_tokens"]`

. -

(`**kwargs`

[¶](https://docs.vllm.ai#vllm.LLM(**kwargs))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`{}`

) –Arguments for

.`EngineArgs`


## Note

This class is intended to be used for offline inference. For online serving, use the [AsyncLLMEngine](https://docs.vllm.ai#vllm.AsyncLLMEngine) class instead.

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.LLM.__init__)LLM constructor.

-
–[__repr__](https://docs.vllm.ai#vllm.LLM.__repr__)Return a transformers-style hierarchical view of the model.

-
–[apply_model](https://docs.vllm.ai#vllm.LLM.apply_model)Run a function directly on the model inside each worker,

-
–[chat](https://docs.vllm.ai#vllm.LLM.chat)Generate responses for a chat conversation.

-
–[collective_rpc](https://docs.vllm.ai#vllm.LLM.collective_rpc)Execute an RPC call on all workers.

-
–[enqueue](https://docs.vllm.ai#vllm.LLM.enqueue)Enqueue prompts for generation without waiting for completion.

-
–[enqueue_chat](https://docs.vllm.ai#vllm.LLM.enqueue_chat)Enqueue chat conversations for generation without waiting.

-
–[finish_weight_update](https://docs.vllm.ai#vllm.LLM.finish_weight_update)Finish the weight update and set its version if provided.

-
–[from_engine_args](https://docs.vllm.ai#vllm.LLM.from_engine_args)Create an LLM instance from EngineArgs.

-
–[generate](https://docs.vllm.ai#vllm.LLM.generate)Generates the completions for the input prompts.

-
–[get_metrics](https://docs.vllm.ai#vllm.LLM.get_metrics)Return a snapshot of aggregated metrics from Prometheus.

-
–[get_weight_version](https://docs.vllm.ai#vllm.LLM.get_weight_version)Return the latest committed weight version.

-
–[get_world_size](https://docs.vllm.ai#vllm.LLM.get_world_size)Get the world size from the parallel config.

-
–[init_weight_transfer_engine](https://docs.vllm.ai#vllm.LLM.init_weight_transfer_engine)Initialize weight transfer for RL training.

-
–[release_kv_cache_memory](https://docs.vllm.ai#vllm.LLM.release_kv_cache_memory)Release the GPU physical memory backing the KV cache.

-
–[sleep](https://docs.vllm.ai#vllm.LLM.sleep)Put the engine to sleep. The engine should not process any requests.

-
–[start_draft_weight_update](https://docs.vllm.ai#vllm.LLM.start_draft_weight_update)Start a new weight update targeting the speculative draft model.

-
–[start_profile](https://docs.vllm.ai#vllm.LLM.start_profile)Start profiling with optional custom trace prefix.

-
–[start_weight_update](https://docs.vllm.ai#vllm.LLM.start_weight_update)Start a new weight update.

-
–[update_weight_version](https://docs.vllm.ai#vllm.LLM.update_weight_version)Set the weight version without updating weights.

-
–[update_weights](https://docs.vllm.ai#vllm.LLM.update_weights)Update the weights of the model.

-
–[wait_for_completion](https://docs.vllm.ai#vllm.LLM.wait_for_completion)Wait for all enqueued requests to complete and return results.

-
–[wake_up](https://docs.vllm.ai#vllm.LLM.wake_up)Wake up the engine from sleep mode. See the

[sleep](https://docs.vllm.ai#vllm.LLM.sleep)

## Source code in `vllm/entrypoints/llm.py`


|
|

###

`__init__(model, *, runner='auto', convert='auto', tokenizer=None, tokenizer_mode='auto', skip_tokenizer_init=False, trust_remote_code=False, allowed_local_media_path='', allowed_media_domains=None, tensor_parallel_size=1, dtype='auto', quantization=None, revision=None, tokenizer_revision=None, chat_template=None, seed=0, gpu_memory_utilization=0.92, cpu_offload_gb=0, offload_group_size=0, offload_num_in_group=1, offload_prefetch_step=1, offload_params=None, enforce_eager=False, enable_return_routed_experts=False, return_sampling_mask=False, disable_custom_all_reduce=False, hf_token=None, hf_overrides=None, mm_processor_kwargs=None, pooler_config=None, structured_outputs_config=None, profiler_config=None, attention_config=None, kv_cache_memory_bytes=None, compilation_config=None, quantization_config=None, logits_processors=None, spec_method=None, spec_model=None, spec_tokens=None, **kwargs)`

[¶](https://docs.vllm.ai#vllm.LLM.__init__)

LLM constructor.

## Source code in `vllm/entrypoints/llm.py`


|
|

###

`__repr__()`

[¶](https://docs.vllm.ai#vllm.LLM.__repr__)

Return a transformers-style hierarchical view of the model.

## Source code in `vllm/entrypoints/llm.py`


###

`apply_model(func)`

[¶](https://docs.vllm.ai#vllm.LLM.apply_model)

Run a function directly on the model inside each worker, returning the result for each of them.

Warning

To reduce the overhead of data transfer, avoid returning large arrays or tensors from this method. If you must return them, make sure you move them to CPU first to avoid taking up additional VRAM!

## Source code in `vllm/entrypoints/llm.py`


###

`chat(messages, sampling_params=None, use_tqdm=True, lora_request=None, chat_template=None, chat_template_content_format='auto', add_generation_prompt=True, continue_final_message=False, tools=None, chat_template_kwargs=None, tokenization_kwargs=None, mm_processor_kwargs=None)`

[¶](https://docs.vllm.ai#vllm.LLM.chat)

Generate responses for a chat conversation.

The chat conversation is converted into a text prompt using the tokenizer and calls the [generate](https://docs.vllm.ai#vllm.LLM.generate) method to generate the responses.

Multi-modal inputs can be passed in the same way you would pass them to the OpenAI API.

Parameters:

-

(`messages`

[¶](https://docs.vllm.ai#vllm.LLM.chat(messages))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[ChatCompletionMessageParam] |[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[ChatCompletionMessageParam]]A sequence of conversations or a single conversation.

- Each conversation is represented as a list of messages.
- Each message is a dictionary with 'role' and 'content' keys.

-

(`sampling_params`

[¶](https://docs.vllm.ai#vllm.LLM.chat(sampling_params))

, default:[SamplingParams](https://docs.vllm.ai/sampling_params/#vllm.sampling_params.SamplingParams)|[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[SamplingParams](https://docs.vllm.ai/sampling_params/#vllm.sampling_params.SamplingParams)] | None`None`

) –The sampling parameters for text generation. If None, we use the default sampling parameters. When it is a single value, it is applied to every prompt. When it is a list, the list must have the same length as the prompts and it is paired one by one with the prompt.

-

(`use_tqdm`

[¶](https://docs.vllm.ai#vllm.LLM.chat(use_tqdm))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)|[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[..., tqdm]`True`

) –If

`True`

, shows a tqdm progress bar. If a callable (e.g.,`functools.partial(tqdm, leave=False)`

), it is used to create the progress bar. If`False`

, no progress bar is created. -

(`lora_request`

[¶](https://docs.vllm.ai#vllm.LLM.chat(lora_request))

, default:[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)] |[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)| None`None`

) –LoRA request to use for generation, if any.

-

(`chat_template`

[¶](https://docs.vllm.ai#vllm.LLM.chat(chat_template))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –The template to use for structuring the chat. If not provided, the model's default chat template will be used.

-

(`chat_template_content_format`

[¶](https://docs.vllm.ai#vllm.LLM.chat(chat_template_content_format))`ChatTemplateContentFormatOption`

, default:`'auto'`

) –The format to render message content.

- "string" will render the content as a string. Example:
`"Who are you?"`

- "openai" will render the content as a list of dictionaries, similar to OpenAI schema. Example:
`[{"type": "text", "text": "Who are you?"}]`


- "string" will render the content as a string. Example:
-

(`add_generation_prompt`

[¶](https://docs.vllm.ai#vllm.LLM.chat(add_generation_prompt))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –If True, adds a generation template to each message.

-

(`continue_final_message`

[¶](https://docs.vllm.ai#vllm.LLM.chat(continue_final_message))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If True, continues the final message in the conversation instead of starting a new one. Cannot be

`True`

if`add_generation_prompt`

is also`True`

. -

(`chat_template_kwargs`

[¶](https://docs.vllm.ai#vllm.LLM.chat(chat_template_kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Additional kwargs to pass to the chat template.

-

(`tokenization_kwargs`

[¶](https://docs.vllm.ai#vllm.LLM.chat(tokenization_kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Overrides for

`tokenizer.encode`

. -

(`mm_processor_kwargs`

[¶](https://docs.vllm.ai#vllm.LLM.chat(mm_processor_kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Overrides for

`processor.__call__`

. -

(`tools`

[¶](https://docs.vllm.ai#vllm.LLM.chat(tools))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)]] | None`None`

) –Tools to make available to the model, if any.


Returns:

-

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[RequestOutput](https://docs.vllm.ai/outputs/#vllm.outputs.RequestOutput)]A list of

`RequestOutput`

objects containing the generated -

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[RequestOutput](https://docs.vllm.ai/outputs/#vllm.outputs.RequestOutput)]responses in the same order as the input messages.


## Source code in `vllm/entrypoints/llm.py`


|
|

###

`collective_rpc(method, timeout=None, args=(), kwargs=None)`

[¶](https://docs.vllm.ai#vllm.LLM.collective_rpc)

Execute an RPC call on all workers.

Parameters:

-

(`method`

[¶](https://docs.vllm.ai#vllm.LLM.collective_rpc(method))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)|[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[..., _R]Name of the worker method to execute, or a callable that is serialized and sent to all workers to execute.

If the method is a callable, it should accept an additional

`self`

argument, in addition to the arguments passed in`args`

and`kwargs`

. The`self`

argument will be the worker object. -

(`timeout`

[¶](https://docs.vllm.ai#vllm.LLM.collective_rpc(timeout))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)| None`None`

) –Maximum time in seconds to wait for execution. Raises a

on timeout.`TimeoutError`

`None`

means wait indefinitely. -

(`args`

[¶](https://docs.vllm.ai#vllm.LLM.collective_rpc(args))

, default:[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)`()`

) –Positional arguments to pass to the worker method.

-

(`kwargs`

[¶](https://docs.vllm.ai#vllm.LLM.collective_rpc(kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Keyword arguments to pass to the worker method.


Returns:

-

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[_R]A list containing the results from each worker.


## Note

It is recommended to use this API to only pass control messages, and set up data-plane communication to pass data.

## Source code in `vllm/entrypoints/llm.py`


###

`enqueue(prompts, sampling_params=None, lora_request=None, priority=None, use_tqdm=True, tokenization_kwargs=None, mm_processor_kwargs=None)`

[¶](https://docs.vllm.ai#vllm.LLM.enqueue)

Enqueue prompts for generation without waiting for completion.

This method adds requests to the engine queue but does not start processing them. Use wait_for_completion() to process the queued requests and get results.

Parameters:

-

(`prompts`

[¶](https://docs.vllm.ai#vllm.LLM.enqueue(prompts))

) –[PromptType](https://docs.vllm.ai/inputs/#vllm.inputs.PromptType)|[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[PromptType](https://docs.vllm.ai/inputs/#vllm.inputs.PromptType)]The prompts to the LLM. See generate() for details.

-

(`sampling_params`

[¶](https://docs.vllm.ai#vllm.LLM.enqueue(sampling_params))

, default:[SamplingParams](https://docs.vllm.ai/sampling_params/#vllm.sampling_params.SamplingParams)|[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[SamplingParams](https://docs.vllm.ai/sampling_params/#vllm.sampling_params.SamplingParams)] | None`None`

) –The sampling parameters for text generation.

-

(`lora_request`

[¶](https://docs.vllm.ai#vllm.LLM.enqueue(lora_request))

, default:[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)] |[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)| None`None`

) –LoRA request to use for generation, if any.

-

(`priority`

[¶](https://docs.vllm.ai#vllm.LLM.enqueue(priority))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | None`None`

) –The priority of the requests, if any.

-

(`use_tqdm`

[¶](https://docs.vllm.ai#vllm.LLM.enqueue(use_tqdm))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)|[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[..., tqdm]`True`

) –If True, shows a tqdm progress bar while adding requests.

-

(`tokenization_kwargs`

[¶](https://docs.vllm.ai#vllm.LLM.enqueue(tokenization_kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Overrides for

`tokenizer.encode`

. -

(`mm_processor_kwargs`

[¶](https://docs.vllm.ai#vllm.LLM.enqueue(mm_processor_kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Overrides for

`processor.__call__`

.

Returns:

## Source code in `vllm/entrypoints/llm.py`


###

`enqueue_chat(messages, sampling_params=None, use_tqdm=True, lora_request=None, priority=None, chat_template=None, chat_template_content_format='auto', add_generation_prompt=True, continue_final_message=False, tools=None, chat_template_kwargs=None, tokenization_kwargs=None, mm_processor_kwargs=None)`

[¶](https://docs.vllm.ai#vllm.LLM.enqueue_chat)

Enqueue chat conversations for generation without waiting.

This method renders chat conversations and adds the resulting requests to the engine queue. Use wait_for_completion() to get results. To guarantee that all requests are queued before scheduling starts, pause scheduling with sleep(level=0) before calling this method and resume it with wake_up(tags=["scheduling"]) afterward.

Parameters:

-

(`messages`

[¶](https://docs.vllm.ai#vllm.LLM.enqueue_chat(messages))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[ChatCompletionMessageParam] |[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[ChatCompletionMessageParam]]A sequence of conversations or a single conversation. Each conversation is represented as a list of messages.

-

(`sampling_params`

[¶](https://docs.vllm.ai#vllm.LLM.enqueue_chat(sampling_params))

, default:[SamplingParams](https://docs.vllm.ai/sampling_params/#vllm.sampling_params.SamplingParams)|[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[SamplingParams](https://docs.vllm.ai/sampling_params/#vllm.sampling_params.SamplingParams)] | None`None`

) –The sampling parameters for text generation. If None, we use the default sampling parameters.

-

(`use_tqdm`

[¶](https://docs.vllm.ai#vllm.LLM.enqueue_chat(use_tqdm))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)|[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[..., tqdm]`True`

) –If

`True`

, shows a tqdm progress bar while rendering conversations. -

(`lora_request`

[¶](https://docs.vllm.ai#vllm.LLM.enqueue_chat(lora_request))

, default:[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)] |[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)| None`None`

) –LoRA request to use for generation, if any.

-

(`priority`

[¶](https://docs.vllm.ai#vllm.LLM.enqueue_chat(priority))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | None`None`

) –The priority of the requests, if any.

-

(`chat_template`

[¶](https://docs.vllm.ai#vllm.LLM.enqueue_chat(chat_template))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –The template to use for structuring the chat.

-

(`chat_template_content_format`

[¶](https://docs.vllm.ai#vllm.LLM.enqueue_chat(chat_template_content_format))`ChatTemplateContentFormatOption`

, default:`'auto'`

) –The format to render message content.

-

(`add_generation_prompt`

[¶](https://docs.vllm.ai#vllm.LLM.enqueue_chat(add_generation_prompt))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –If True, adds a generation template to each message.

-

(`continue_final_message`

[¶](https://docs.vllm.ai#vllm.LLM.enqueue_chat(continue_final_message))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If True, continues the final message in the conversation instead of starting a new one.

-

(`tools`

[¶](https://docs.vllm.ai#vllm.LLM.enqueue_chat(tools))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)]] | None`None`

) –Tools to make available to the model, if any.

-

(`chat_template_kwargs`

[¶](https://docs.vllm.ai#vllm.LLM.enqueue_chat(chat_template_kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Additional kwargs to pass to the chat template.

-

(`tokenization_kwargs`

[¶](https://docs.vllm.ai#vllm.LLM.enqueue_chat(tokenization_kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Overrides for

`tokenizer.encode`

. -

(`mm_processor_kwargs`

[¶](https://docs.vllm.ai#vllm.LLM.enqueue_chat(mm_processor_kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Overrides for

`processor.__call__`

.

Returns:

## Source code in `vllm/entrypoints/llm.py`


|
|

###

`finish_weight_update(weight_version=None)`

[¶](https://docs.vllm.ai#vllm.LLM.finish_weight_update)

Finish the weight update and set its version if provided.

## Source code in `vllm/entrypoints/llm.py`


###

`from_engine_args(engine_args)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.LLM.from_engine_args)

###

`generate(prompts, sampling_params=None, *, use_tqdm=True, lora_request=None, priority=None, tokenization_kwargs=None, mm_processor_kwargs=None)`

[¶](https://docs.vllm.ai#vllm.LLM.generate)

Generates the completions for the input prompts.

This class automatically batches the given prompts, considering the memory constraint. For the best performance, put all of your prompts into a single list and pass it to this method.

Parameters:

-

(`prompts`

[¶](https://docs.vllm.ai#vllm.LLM.generate(prompts))

) –[PromptType](https://docs.vllm.ai/inputs/#vllm.inputs.PromptType)|[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[PromptType](https://docs.vllm.ai/inputs/#vllm.inputs.PromptType)]The prompts to the LLM. You may pass a sequence of prompts for batch inference. See

[PromptType](https://docs.vllm.ai/inputs/#vllm.inputs.PromptType)for more details about the format of each prompt. -

(`sampling_params`

[¶](https://docs.vllm.ai#vllm.LLM.generate(sampling_params))

, default:[SamplingParams](https://docs.vllm.ai/sampling_params/#vllm.sampling_params.SamplingParams)|[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[SamplingParams](https://docs.vllm.ai/sampling_params/#vllm.sampling_params.SamplingParams)] | None`None`

) –The sampling parameters for text generation. If None, we use the default sampling parameters. When it is a single value, it is applied to every prompt. When it is a list, the list must have the same length as the prompts and it is paired one by one with the prompt.

-

(`use_tqdm`

[¶](https://docs.vllm.ai#vllm.LLM.generate(use_tqdm))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)|[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[..., tqdm]`True`

) –If

`True`

, shows a tqdm progress bar. If a callable (e.g.,`functools.partial(tqdm, leave=False)`

), it is used to create the progress bar. If`False`

, no progress bar is created. -

(`lora_request`

[¶](https://docs.vllm.ai#vllm.LLM.generate(lora_request))

, default:[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)] |[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)| None`None`

) –LoRA request to use for generation, if any.

-

(`priority`

[¶](https://docs.vllm.ai#vllm.LLM.generate(priority))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | None`None`

) –The priority of the requests, if any. Only applicable when priority scheduling policy is enabled. If provided, must be a list of integers matching the length of

`prompts`

, where each priority value corresponds to the prompt at the same index. -

(`tokenization_kwargs`

[¶](https://docs.vllm.ai#vllm.LLM.generate(tokenization_kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Overrides for

`tokenizer.encode`

. -

(`mm_processor_kwargs`

[¶](https://docs.vllm.ai#vllm.LLM.generate(mm_processor_kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Overrides for

`processor.__call__`

.

Returns:

-

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[RequestOutput](https://docs.vllm.ai/outputs/#vllm.outputs.RequestOutput)]A list of

`RequestOutput`

objects containing the -

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[RequestOutput](https://docs.vllm.ai/outputs/#vllm.outputs.RequestOutput)]generated completions in the same order as the input prompts.


## Source code in `vllm/entrypoints/llm.py`


###

`get_metrics()`

[¶](https://docs.vllm.ai#vllm.LLM.get_metrics)

Return a snapshot of aggregated metrics from Prometheus.

Returns:

-

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Metric](https://docs.vllm.ai/v1/metrics/reader/#vllm.v1.metrics.reader.Metric)]A

`MetricSnapshot`

instance capturing the current state -

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Metric](https://docs.vllm.ai/v1/metrics/reader/#vllm.v1.metrics.reader.Metric)]of all aggregated metrics from Prometheus.


## Note

This method is only available with the V1 LLM engine.

## Source code in `vllm/entrypoints/llm.py`


###

`get_weight_version()`

[¶](https://docs.vllm.ai#vllm.LLM.get_weight_version)

###

`get_world_size(include_dp=True)`

[¶](https://docs.vllm.ai#vllm.LLM.get_world_size)

Get the world size from the parallel config.

Parameters:

-

(`include_dp`

[¶](https://docs.vllm.ai#vllm.LLM.get_world_size(include_dp))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –If True (default), returns the world size including data parallelism (TP * PP * DP). If False, returns the world size without data parallelism (TP * PP).


Returns:

-

–[int](https://docs.python.org/3/builtins/functions.html#int)The world size (tensor_parallel_size * pipeline_parallel_size),

-

–[int](https://docs.python.org/3/builtins/functions.html#int)optionally multiplied by data_parallel_size if include_dp is True.


## Source code in `vllm/entrypoints/llm.py`


###

`init_weight_transfer_engine(request)`

[¶](https://docs.vllm.ai#vllm.LLM.init_weight_transfer_engine)

Initialize weight transfer for RL training.

Parameters:

-

(`request`

[¶](https://docs.vllm.ai#vllm.LLM.init_weight_transfer_engine(request))

) –[WeightTransferInitRequest](https://docs.vllm.ai/distributed/weight_transfer/base/#vllm.distributed.weight_transfer.base.WeightTransferInitRequest)|[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)Weight transfer initialization request with backend-specific info


## Source code in `vllm/entrypoints/llm.py`


###

`release_kv_cache_memory()`

[¶](https://docs.vllm.ai#vllm.LLM.release_kv_cache_memory)

Release the GPU physical memory backing the KV cache.

Requires a completed `sleep(level=0)`

and resident executor memory. Restore with `wake_up(tags=["kv_cache"])`

; kept requests are recomputed.

## Source code in `vllm/entrypoints/llm.py`


###

`sleep(level=1, mode='abort')`

[¶](https://docs.vllm.ai#vllm.LLM.sleep)

Put the engine to sleep. The engine should not process any requests. The caller should guarantee that no requests are being processed during the sleep period, before `wake_up`

is called.

Parameters:

-

(`level`

[¶](https://docs.vllm.ai#vllm.LLM.sleep(level))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –The sleep level. - Level 0: Pause scheduling but continue accepting requests. Requests are queued but not processed. - Level 1: Offload model weights to CPU, discard KV cache. The content of kv cache is forgotten. Good for sleeping and waking up the engine to run the same model again. Please make sure there's enough CPU memory to store the model weights. - Level 2: Discard all GPU memory (weights + KV cache). Good for sleeping and waking up the engine to run a different model or update the model, where previous model weights are not needed. It reduces CPU memory pressure.

-

(`mode`

[¶](https://docs.vllm.ai#vllm.LLM.sleep(mode))`PauseMode`

, default:`'abort'`

) –How to handle any existing requests, can be "abort", "wait", or "keep".


## Source code in `vllm/entrypoints/llm.py`


###

`start_draft_weight_update()`

[¶](https://docs.vllm.ai#vllm.LLM.start_draft_weight_update)

###

`start_profile(profile_prefix=None)`

[¶](https://docs.vllm.ai#vllm.LLM.start_profile)

Start profiling with optional custom trace prefix.

Parameters:

-

(`profile_prefix`

[¶](https://docs.vllm.ai#vllm.LLM.start_profile(profile_prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –Optional prefix for the trace file names. If provided, trace files will be named as "

_dp _pp _tp ". If not provided, default naming will be used.

## Source code in `vllm/entrypoints/llm.py`


###

`start_weight_update()`

[¶](https://docs.vllm.ai#vllm.LLM.start_weight_update)

###

`update_weight_version(new_version)`

[¶](https://docs.vllm.ai#vllm.LLM.update_weight_version)

###

`update_weights(request)`

[¶](https://docs.vllm.ai#vllm.LLM.update_weights)

Update the weights of the model.

Parameters:

-

(`request`

[¶](https://docs.vllm.ai#vllm.LLM.update_weights(request))

) –[WeightTransferUpdateRequest](https://docs.vllm.ai/distributed/weight_transfer/base/#vllm.distributed.weight_transfer.base.WeightTransferUpdateRequest)|[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)Weight update request with backend-specific update info


## Source code in `vllm/entrypoints/llm.py`


###

`wait_for_completion(output_type=None, *, use_tqdm=True)`

[¶](https://docs.vllm.ai#vllm.LLM.wait_for_completion)

Wait for all enqueued requests to complete and return results.

This method processes all requests currently in the engine queue and returns their outputs. Use after enqueue() to get results.

Parameters:

-

(`output_type`

[¶](https://docs.vllm.ai#vllm.LLM.wait_for_completion(output_type))

, default:[type](https://docs.python.org/3/builtins/functions.html#type)[[Any](https://docs.python.org/3/library/typing.html#typing.Any)] |[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[type](https://docs.python.org/3/builtins/functions.html#type)[[Any](https://docs.python.org/3/library/typing.html#typing.Any)], ...] | None`None`

) –The expected output type(s). If not provided, accepts both RequestOutput and PoolingRequestOutput.

-

(`use_tqdm`

[¶](https://docs.vllm.ai#vllm.LLM.wait_for_completion(use_tqdm))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)|[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[..., tqdm]`True`

) –If True, shows a tqdm progress bar.


Returns:

## Source code in `vllm/entrypoints/llm.py`


###

`wake_up(tags=None)`

[¶](https://docs.vllm.ai#vllm.LLM.wake_up)

Wake up the engine from sleep mode. See the [sleep](https://docs.vllm.ai#vllm.LLM.sleep) method for more details.

Parameters:

-

(`tags`

[¶](https://docs.vllm.ai#vllm.LLM.wake_up(tags))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None`None`

) –An optional list of tags to reallocate the engine memory for specific memory allocations. Values must be in

`("weights", "kv_cache", "scheduling")`

. If None, all memory is reallocated. wake_up should be called with all tags (or None) before the engine is used again. Use tags=["scheduling"] to resume from level 0 sleep.

## Source code in `vllm/entrypoints/llm.py`


##

`PoolingOutput`

`dataclass`

[¶](https://docs.vllm.ai#vllm.PoolingOutput)

The output data of one pooling output of a request.

Parameters:

## Source code in `vllm/outputs.py`


##

`PoolingParams`

[¶](https://docs.vllm.ai#vllm.PoolingParams)

Bases: `Struct`


API parameters for pooling models.

Attributes:

-
(`use_activation`


) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneWhether to apply activation function to the pooler outputs.

`None`

uses the pooler's default, which is`True`

in most cases. -
(`dimensions`


) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneReduce the dimensions of embeddings if model support matryoshka representation.


Methods:

-
–[clone](https://docs.vllm.ai#vllm.PoolingParams.clone)Returns a deep copy of the PoolingParams instance.


## Source code in `vllm/pooling_params.py`


|
|

##

`PoolingRequestOutput`

[¶](https://docs.vllm.ai#vllm.PoolingRequestOutput)

Bases: [Generic](https://docs.python.org/3/library/typing.html#typing.Generic)[_O]

The output data of a pooling request to the LLM.

Parameters:

-

(`request_id`

[¶](https://docs.vllm.ai#vllm.PoolingRequestOutput(request_id))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)A unique identifier for the pooling request.

-

(`outputs`

[¶](https://docs.vllm.ai#vllm.PoolingRequestOutput(outputs))

) –[PoolingOutput](https://docs.vllm.ai/outputs/#vllm.outputs.PoolingOutput)The pooling results for the given input.

-

(`prompt_token_ids`

[¶](https://docs.vllm.ai#vllm.PoolingRequestOutput(prompt_token_ids))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]A list of token IDs used in the prompt.

-

(`num_cached_tokens`

[¶](https://docs.vllm.ai#vllm.PoolingRequestOutput(num_cached_tokens))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The number of tokens with prefix cache hit.

-

(`finished`

[¶](https://docs.vllm.ai#vllm.PoolingRequestOutput(finished))

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)A flag indicating whether the pooling is completed.


## Source code in `vllm/outputs.py`


##

`RequestOutput`

[¶](https://docs.vllm.ai#vllm.RequestOutput)

The output data of a completion request to the LLM.

Parameters:

-

(`request_id`

[¶](https://docs.vllm.ai#vllm.RequestOutput(request_id))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The unique ID of the request.

-

(`prompt`

[¶](https://docs.vllm.ai#vllm.RequestOutput(prompt))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe prompt string of the request. For encoder/decoder models, this is the decoder input prompt.

-

(`prompt_token_ids`

[¶](https://docs.vllm.ai#vllm.RequestOutput(prompt_token_ids))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | NoneThe token IDs of the prompt. For encoder/decoder models, this is the decoder input prompt token ids.

-

(`prompt_logprobs`

[¶](https://docs.vllm.ai#vllm.RequestOutput(prompt_logprobs))`PromptLogprobs | None`

) –The log probabilities to return per prompt token.

-

(`outputs`

[¶](https://docs.vllm.ai#vllm.RequestOutput(outputs))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[CompletionOutput](https://docs.vllm.ai/outputs/#vllm.outputs.CompletionOutput)]The output sequences of the request.

-

(`finished`

[¶](https://docs.vllm.ai#vllm.RequestOutput(finished))

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether the whole request is finished.

-

(`metrics`

[¶](https://docs.vllm.ai#vllm.RequestOutput(metrics))

, default:[RequestStateStats](https://docs.vllm.ai/v1/metrics/stats/#vllm.v1.metrics.stats.RequestStateStats)| None`None`

) –Metrics associated with the request.

-

(`lora_request`

[¶](https://docs.vllm.ai#vllm.RequestOutput(lora_request))

, default:[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)| None`None`

) –The LoRA request that was used to generate the output.

-

(`encoder_prompt`

[¶](https://docs.vllm.ai#vllm.RequestOutput(encoder_prompt))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –The encoder prompt string of the request. None if decoder-only.

-

(`encoder_prompt_token_ids`

[¶](https://docs.vllm.ai#vllm.RequestOutput(encoder_prompt_token_ids))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | None`None`

) –The token IDs of the encoder prompt. None if decoder-only.

-

(`num_cached_tokens`

[¶](https://docs.vllm.ai#vllm.RequestOutput(num_cached_tokens))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –The number of tokens with prefix cache hit.

-

(`num_cache_creation_tokens`

[¶](https://docs.vllm.ai#vllm.RequestOutput(num_cache_creation_tokens))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Prompt tokens currently counted as local prefix-cache writes for this request.

-

(`kv_transfer_params`

[¶](https://docs.vllm.ai#vllm.RequestOutput(kv_transfer_params))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –The params for remote K/V transfer.

-

(`ec_transfer_params`

[¶](https://docs.vllm.ai#vllm.RequestOutput(ec_transfer_params))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –The params for remote encoder-cache transfer.


Methods:

-
–[add](https://docs.vllm.ai#vllm.RequestOutput.add)Merge subsequent RequestOutput into this one


## Source code in `vllm/outputs.py`


|
|

###

`add(next_output, aggregate)`

[¶](https://docs.vllm.ai#vllm.RequestOutput.add)

Merge subsequent RequestOutput into this one

## Source code in `vllm/outputs.py`


##

`SamplingParams`

[¶](https://docs.vllm.ai#vllm.SamplingParams)

Bases:

, [PydanticMsgspecMixin](https://docs.vllm.ai/v1/serial_utils/#vllm.v1.serial_utils.PydanticMsgspecMixin)`Struct`


Sampling parameters for text generation.

Overall, we follow the sampling parameters from the OpenAI text completion API (https://platform.openai.com/docs/api-reference/completions/create). In addition, we support beam search, which is not supported by OpenAI.

Methods:

-
–[clone](https://docs.vllm.ai#vllm.SamplingParams.clone)If skip_clone is True, uses shallow copy instead of deep copy.

-
–[for_sampler_warmup](https://docs.vllm.ai#vllm.SamplingParams.for_sampler_warmup)Set parameters to exercise all sampler logic.

-
–[update_from_generation_config](https://docs.vllm.ai#vllm.SamplingParams.update_from_generation_config)Update if there are non-default values from generation_config.


Attributes:

-
([allowed_token_ids](https://docs.vllm.ai#vllm.SamplingParams.allowed_token_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | NoneIf provided, the engine will construct a logits processor which only

-
([bad_words](https://docs.vllm.ai#vllm.SamplingParams.bad_words)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | NoneWords that are not allowed to be generated. More precisely, only the

-
([detokenize](https://docs.vllm.ai#vllm.SamplingParams.detokenize)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to detokenize the output.

-
([extra_args](https://docs.vllm.ai#vllm.SamplingParams.extra_args)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | NoneArbitrary additional args, that can be used by custom sampling

-
([flat_logprobs](https://docs.vllm.ai#vllm.SamplingParams.flat_logprobs)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to return logprobs in flatten format (i.e. FlatLogprob)

-
([frequency_penalty](https://docs.vllm.ai#vllm.SamplingParams.frequency_penalty)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Penalizes new tokens based on their frequency in the generated text so

-
([ignore_eos](https://docs.vllm.ai#vllm.SamplingParams.ignore_eos)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to ignore the EOS token and continue generating

-
([include_stop_str_in_output](https://docs.vllm.ai#vllm.SamplingParams.include_stop_str_in_output)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to include the stop strings in output text.

-
([logit_bias](https://docs.vllm.ai#vllm.SamplingParams.logit_bias)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[int](https://docs.python.org/3/builtins/functions.html#int),[float](https://docs.python.org/3/builtins/functions.html#float)] | NoneIf provided, the engine will construct a logits processor that applies

-
([logprob_token_ids](https://docs.vllm.ai#vllm.SamplingParams.logprob_token_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | NoneSpecific token IDs to return logprobs for. More efficient than

-
([logprobs](https://docs.vllm.ai#vllm.SamplingParams.logprobs)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneNumber of log probabilities to return per output token. When set to

-
([max_tokens](https://docs.vllm.ai#vllm.SamplingParams.max_tokens)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMaximum number of tokens to generate per output sequence.

-
([min_p](https://docs.vllm.ai#vllm.SamplingParams.min_p)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Represents the minimum probability for a token to be considered,

-
([min_tokens](https://docs.vllm.ai#vllm.SamplingParams.min_tokens)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Minimum number of tokens to generate per output sequence before EOS or

-
([n](https://docs.vllm.ai#vllm.SamplingParams.n)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of outputs to return for the given prompt request.

-
([num_logprobs](https://docs.vllm.ai#vllm.SamplingParams.num_logprobs)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneNumber of sample logprobs to return per output token, or

`None`

if -
([presence_penalty](https://docs.vllm.ai#vllm.SamplingParams.presence_penalty)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Penalizes new tokens based on whether they appear in the generated text

-
([prompt_logprobs](https://docs.vllm.ai#vllm.SamplingParams.prompt_logprobs)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneNumber of log probabilities to return per prompt token.

-
([repetition_detection](https://docs.vllm.ai#vllm.SamplingParams.repetition_detection)

) –[RepetitionDetectionParams](https://docs.vllm.ai/sampling_params/#vllm.sampling_params.RepetitionDetectionParams)| NoneParameters for detecting repetitive N-gram patterns in output tokens.

-
([repetition_penalty](https://docs.vllm.ai#vllm.SamplingParams.repetition_penalty)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Penalizes new tokens based on whether they appear in the prompt and the

-
([routed_experts_prompt_start](https://docs.vllm.ai#vllm.SamplingParams.routed_experts_prompt_start)

) –[int](https://docs.python.org/3/builtins/functions.html#int)When enable_return_routed_experts is active, skip the first

-
([seed](https://docs.vllm.ai#vllm.SamplingParams.seed)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneRandom seed to use for the generation.

-
([skip_clone](https://docs.vllm.ai#vllm.SamplingParams.skip_clone)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Internal flag indicating that this SamplingParams instance is safe to

-
([skip_special_tokens](https://docs.vllm.ai#vllm.SamplingParams.skip_special_tokens)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to skip special tokens in the output.

-
([spaces_between_special_tokens](https://docs.vllm.ai#vllm.SamplingParams.spaces_between_special_tokens)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to add spaces between special tokens in the output.

-
([stop](https://docs.vllm.ai#vllm.SamplingParams.stop)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)|[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | NoneString(s) that stop the generation when they are generated. The returned

-
([stop_token_ids](https://docs.vllm.ai#vllm.SamplingParams.stop_token_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | NoneToken IDs that stop the generation when they are generated. The returned

-
([stream_interval](https://docs.vllm.ai#vllm.SamplingParams.stream_interval)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneNumber of newly generated tokens to batch into each streamed

-
([structured_outputs](https://docs.vllm.ai#vllm.SamplingParams.structured_outputs)

) –[StructuredOutputsParams](https://docs.vllm.ai/sampling_params/#vllm.sampling_params.StructuredOutputsParams)| NoneParameters for configuring structured outputs.

-
([temperature](https://docs.vllm.ai#vllm.SamplingParams.temperature)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Controls the randomness of the sampling. Lower values make the model

-
([thinking_token_budget](https://docs.vllm.ai#vllm.SamplingParams.thinking_token_budget)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMaximum number of tokens allowed for thinking operations.

-
([top_k](https://docs.vllm.ai#vllm.SamplingParams.top_k)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Controls the number of top tokens to consider. Set to 0 (or -1) to

-
([top_p](https://docs.vllm.ai#vllm.SamplingParams.top_p)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Controls the cumulative probability of the top tokens to consider. Must

-
([trace_decode_token_ids](https://docs.vllm.ai#vllm.SamplingParams.trace_decode_token_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | NoneIf provided, forces the engine to emit this predetermined sequence of

-
([watermarking](https://docs.vllm.ai#vllm.SamplingParams.watermarking)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to apply the engine's configured watermark to this request.


## Source code in `vllm/sampling_params.py`


|
|

###

`allowed_token_ids = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.allowed_token_ids)

If provided, the engine will construct a logits processor which only retains scores for the given token ids.

###

`bad_words = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.bad_words)

Words that are not allowed to be generated. More precisely, only the last token of a corresponding token sequence is not allowed when the next generated token can complete the sequence.

###

`detokenize = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.detokenize)

Whether to detokenize the output.

###

`extra_args = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.extra_args)

Arbitrary additional args, that can be used by custom sampling implementations, plugins, etc. Not used by any in-tree sampling implementations.

###

`flat_logprobs = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.flat_logprobs)

Whether to return logprobs in flatten format (i.e. FlatLogprob) for better performance. NOTE: GC costs of FlatLogprobs is significantly smaller than list[dict[int, Logprob]]. After enabled, PromptLogprobs and SampleLogprobs would populated as FlatLogprobs.

###

`frequency_penalty = 0.0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.frequency_penalty)

Penalizes new tokens based on their frequency in the generated text so far. Values > 0 encourage the model to use new tokens, while values < 0 encourage the model to repeat tokens.

###

`ignore_eos = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.ignore_eos)

Whether to ignore the EOS token and continue generating tokens after the EOS token is generated.

###

`include_stop_str_in_output = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.include_stop_str_in_output)

Whether to include the stop strings in output text.

###

`logit_bias = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.logit_bias)

If provided, the engine will construct a logits processor that applies these logit biases.

###

`logprob_token_ids = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.logprob_token_ids)

Specific token IDs to return logprobs for. More efficient than logprobs=-1 when you only need logprobs for a small set of tokens. When set, logprobs for exactly these token IDs will be returned, in addition to the sampled token. This is useful for scoring tasks where you want to compare probabilities of specific label tokens.

###

`logprobs = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.logprobs)

Number of log probabilities to return per output token. When set to `None`

, no probability is returned. If set to a non-`None`

value, the result includes the log probabilities of the specified number of most likely tokens, as well as the chosen tokens. Note that the implementation follows the OpenAI API: The API will always return the log probability of the sampled token, so there may be up to `logprobs+1`

elements in the response. When set to -1, return all `vocab_size`

log probabilities.

###

`max_tokens = 16`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.max_tokens)

Maximum number of tokens to generate per output sequence.

###

`min_p = 0.0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.min_p)

Represents the minimum probability for a token to be considered, relative to the probability of the most likely token. Must be in [0, 1]. Set to 0 to disable this.

###

`min_tokens = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.min_tokens)

Minimum number of tokens to generate per output sequence before EOS or `stop_token_ids`

can be generated

###

`n = 1`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.n)

Number of outputs to return for the given prompt request.

The maximum allowed value is controlled by the `VLLM_MAX_N_SEQUENCES`

environment variable (default: 16384).

## NOTE

`AsyncLLM`

streams outputs by default. When `n > 1`

, all `n`

outputs are generated and streamed cumulatively per request. To see all `n`

outputs upon completion, use `output_kind=RequestOutputKind.FINAL_ONLY`

in `SamplingParams`

.

###

`num_logprobs`

`property`

[¶](https://docs.vllm.ai#vllm.SamplingParams.num_logprobs)

Number of sample logprobs to return per output token, or `None`

if no sample logprobs were requested. Takes `logprob_token_ids`

into account: when `logprobs`

is unset but `logprob_token_ids`

is set, returns `len(logprob_token_ids)`

.

###

`presence_penalty = 0.0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.presence_penalty)

Penalizes new tokens based on whether they appear in the generated text so far. Values > 0 encourage the model to use new tokens, while values < 0 encourage the model to repeat tokens.

###

`prompt_logprobs = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.prompt_logprobs)

Number of log probabilities to return per prompt token. When set to -1, return all `vocab_size`

log probabilities.

###

`repetition_detection = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.repetition_detection)

Parameters for detecting repetitive N-gram patterns in output tokens. If such repetition is detected, generation will be ended early. LLMs can sometimes generate repetitive, unhelpful token patterns, stopping only when they hit the maximum output length (e.g. 'abcdabcdabcd...' or '\emoji \emoji \emoji ...'). This feature can detect such behavior and terminate early, saving time and tokens.

###

`repetition_penalty = 1.0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.repetition_penalty)

Penalizes new tokens based on whether they appear in the prompt and the generated text so far. Values > 1 encourage the model to use new tokens, while values < 1 encourage the model to repeat tokens.

###

`routed_experts_prompt_start = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.routed_experts_prompt_start)

When enable_return_routed_experts is active, skip the first routed_experts_prompt_start prompt tokens from the returned routing data. In multi-turn agent scenarios, set this to the length of the already-returned prefix to avoid duplicating routing for prompt tokens covered by earlier turns. Default 0 returns routing for all prompt tokens.

###

`seed = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.seed)

Random seed to use for the generation.

###

`skip_clone = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.skip_clone)

Internal flag indicating that this SamplingParams instance is safe to reuse without cloning. When True, clone() will return self without performing a deep copy. This should only be set when the params object is guaranteed to be dedicated to a single request and won't be modified in ways that would affect other uses.

###

`skip_special_tokens = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.skip_special_tokens)

Whether to skip special tokens in the output.

###

`spaces_between_special_tokens = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.spaces_between_special_tokens)

Whether to add spaces between special tokens in the output.

###

`stop = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.stop)

String(s) that stop the generation when they are generated. The returned output will not contain the stop strings.

###

`stop_token_ids = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.stop_token_ids)

Token IDs that stop the generation when they are generated. The returned output will contain the stop tokens unless the stop tokens are special tokens.

###

`stream_interval = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.stream_interval)

Number of newly generated tokens to batch into each streamed `RequestOutput`

. Raises the interval above the engine-level `--stream-interval`

. Values below engine setting are clamped up to it. The first and final outputs are always emitted immediately.

###

`structured_outputs = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.structured_outputs)

Parameters for configuring structured outputs.

###

`temperature = 1.0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.temperature)

Controls the randomness of the sampling. Lower values make the model more deterministic, while higher values make the model more random. Zero means greedy sampling.

###

`thinking_token_budget = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.thinking_token_budget)

Maximum number of tokens allowed for thinking operations.

###

`top_k = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.top_k)

Controls the number of top tokens to consider. Set to 0 (or -1) to consider all tokens.

###

`top_p = 1.0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.top_p)

Controls the cumulative probability of the top tokens to consider. Must be in (0, 1]. Set to 1 to consider all tokens.

###

`trace_decode_token_ids = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.trace_decode_token_ids)

If provided, forces the engine to emit this predetermined sequence of token IDs during decoding instead of sampling randomly. Real logprobs are still computed. Conflict checking is performed at the engine level.

###

`watermarking = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.SamplingParams.watermarking)

Whether to apply the engine's configured watermark to this request.

###

`_validate_logit_bias(model_config)`

[¶](https://docs.vllm.ai#vllm.SamplingParams._validate_logit_bias)

Validate logit_bias token IDs are within vocabulary range.

## Source code in `vllm/sampling_params.py`


###

`_validate_stop_token_ids(model_config)`

[¶](https://docs.vllm.ai#vllm.SamplingParams._validate_stop_token_ids)

Validate stop_token_ids are within vocabulary range.

## Source code in `vllm/sampling_params.py`


###

`_validate_trace_replay(model_config, speculative_config)`

[¶](https://docs.vllm.ai#vllm.SamplingParams._validate_trace_replay)

Validate trace replay request compatibility.

## Source code in `vllm/sampling_params.py`


###

`clone()`

[¶](https://docs.vllm.ai#vllm.SamplingParams.clone)

If skip_clone is True, uses shallow copy instead of deep copy.

###

`for_sampler_warmup()`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.SamplingParams.for_sampler_warmup)

Set parameters to exercise all sampler logic.

## Source code in `vllm/sampling_params.py`


###

`update_from_generation_config(generation_config, eos_token_id=None)`

[¶](https://docs.vllm.ai#vllm.SamplingParams.update_from_generation_config)

Update if there are non-default values from generation_config.

## Source code in `vllm/sampling_params.py`


##

`ScoringOutput`

`dataclass`

[¶](https://docs.vllm.ai#vllm.ScoringOutput)

The output data of one scoring output of a request.

Parameters:

## Source code in `vllm/outputs.py`


##

`TextPrompt`

[¶](https://docs.vllm.ai#vllm.TextPrompt)

Bases: [_PromptOptions](https://docs.vllm.ai/inputs/llm/#vllm.inputs.llm._PromptOptions)

Schema for a text prompt.

Attributes:

## Source code in `vllm/inputs/llm.py`


###

`prompt`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.TextPrompt.prompt)

The input text to be tokenized before passing to the model.

##

`TokensPrompt`

[¶](https://docs.vllm.ai#vllm.TokensPrompt)

Bases: [_PromptOptions](https://docs.vllm.ai/inputs/llm/#vllm.inputs.llm._PromptOptions)

Schema for a tokenized prompt.

Attributes:

-
([prompt](https://docs.vllm.ai#vllm.TokensPrompt.prompt)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The prompt text corresponding to the token IDs, if available.

-
([prompt_token_ids](https://docs.vllm.ai#vllm.TokensPrompt.prompt_token_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]A list of token IDs to pass to the model.

-
([prompt_token_offsets](https://docs.vllm.ai#vllm.TokensPrompt.prompt_token_offsets)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)]] | None]Char-level (start, end) offsets per token, relative to the

-
([token_type_ids](https://docs.vllm.ai#vllm.TokensPrompt.token_type_ids)

) –[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]A list of token type IDs to pass to the cross encoder model.


## Source code in `vllm/inputs/llm.py`


###

`prompt`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.TokensPrompt.prompt)

The prompt text corresponding to the token IDs, if available.

###

`prompt_token_ids`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.TokensPrompt.prompt_token_ids)

A list of token IDs to pass to the model.

###

`prompt_token_offsets`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.TokensPrompt.prompt_token_offsets)

Char-level (start, end) offsets per token, relative to the tokenized source string. Present only when offsets were requested AND a Fast (Rust-backed) tokenizer was used AND no multimodal data was present. The list length equals the length of `prompt_token_ids`

.

###

`token_type_ids`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.TokensPrompt.token_type_ids)

A list of token type IDs to pass to the cross encoder model.

##

`initialize_ray_cluster(parallel_config, ray_address=None, require_gpu_on_driver=True)`

[¶](https://docs.vllm.ai#vllm.initialize_ray_cluster)

Initialize the distributed cluster with Ray.

it will connect to the Ray cluster and create a placement group for the workers, which includes the specification of the resources for each distributed worker.

Parameters:

-

(`parallel_config`

[¶](https://docs.vllm.ai#vllm.initialize_ray_cluster(parallel_config))

) –[ParallelConfig](https://docs.vllm.ai/config/#vllm.config.ParallelConfig)The configurations for parallel execution.

-

(`ray_address`

[¶](https://docs.vllm.ai#vllm.initialize_ray_cluster(ray_address))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –The address of the Ray cluster. If None, uses the default Ray cluster address.

-

(`require_gpu_on_driver`

[¶](https://docs.vllm.ai#vllm.initialize_ray_cluster(require_gpu_on_driver))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –If True (default), require at least one GPU on the current (driver) node and pin the first PG bundle to it. Set to False for executors like RayExecutorV2 where all GPU work is delegated to remote Ray actors.


## Source code in `vllm/v1/executor/ray_utils.py`


|
|