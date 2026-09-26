source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/llm/
lastmod: 2026-09-24

#

`vllm.entrypoints.llm`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm)

Classes:

-
–[LLM](https://docs.vllm.ai#vllm.entrypoints.llm.LLM)An LLM for generating texts from given prompts and sampling parameters.


##

`LLM`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM)

Bases:

, [BeamSearchOfflineMixin](https://docs.vllm.ai/generate/beam_search/offline/#vllm.entrypoints.generate.beam_search.offline.BeamSearchOfflineMixin)

, [PoolingOfflineMixin](https://docs.vllm.ai/pooling/offline/#vllm.entrypoints.pooling.offline.PoolingOfflineMixin)[OfflineInferenceMixin](https://docs.vllm.ai/offline_utils/#vllm.entrypoints.offline_utils.OfflineInferenceMixin)

An LLM for generating texts from given prompts and sampling parameters.

This class includes a tokenizer, a language model (possibly distributed across multiple GPUs), and GPU memory space allocated for intermediate states (aka KV cache). Given a batch of prompts and sampling parameters, this class generates texts from the model, using an intelligent batching mechanism and efficient memory management.

Parameters:

-

(`model`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(model))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The name or path of a HuggingFace Transformers model.

-

(`tokenizer`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(tokenizer))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –The name or path of a HuggingFace Transformers tokenizer.

-

(`tokenizer_mode`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(tokenizer_mode))`TokenizerMode |`

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'auto'`

) –The tokenizer mode. See

[ModelConfig.tokenizer_mode](https://docs.vllm.ai/config/#vllm.config.ModelConfig.tokenizer_mode). -

(`skip_tokenizer_init`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(skip_tokenizer_init))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If true, skip initialization of tokenizer and detokenizer. Expect valid prompt_token_ids and None for prompt from the input.

-

(`trust_remote_code`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(trust_remote_code))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Trust remote code (e.g., from HuggingFace) when downloading the model and tokenizer.

-

(`allowed_local_media_path`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(allowed_local_media_path))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –Allowing API requests to read local images or videos from directories specified by the server file system. This is a security risk. Should only be enabled in trusted environments.

-

(`allowed_media_domains`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(allowed_media_domains))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None`None`

) –If set, only media URLs that belong to this domain can be used for multi-modal inputs.

-

(`tensor_parallel_size`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(tensor_parallel_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –The number of GPUs to use for distributed execution with tensor parallelism.

-

(`dtype`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(dtype))`ModelDType`

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

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(quantization))`QuantizationMethods | None`

, default:`None`

) –The method used to quantize the model weights. Currently, we support "awq", "gptq", and "fp8" (experimental). If None, we first check the

`quantization_config`

attribute in the model config file. If that is None, we assume the model weights are not quantized and use`dtype`

to determine the data type of the weights. -

(`revision`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(revision))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –The specific model version to use. It can be a branch name, a tag name, or a commit id.

-

(`tokenizer_revision`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(tokenizer_revision))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –The specific tokenizer version to use. It can be a branch name, a tag name, or a commit id.

-

(`chat_template`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(chat_template))

, default:[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)|[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –The chat template to apply.

-

(`seed`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(seed))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –The seed to initialize the random number generator for sampling.

-

(`gpu_memory_utilization`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(gpu_memory_utilization))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)`0.92`

) –The ratio (between 0 and 1) of GPU memory to reserve for the model weights, activations, and KV cache. Higher values will increase the KV cache size and thus improve the model's throughput. However, if the value is too high, it may cause out-of- memory (OOM) errors.

-

(`kv_cache_memory_bytes`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(kv_cache_memory_bytes))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Size of KV Cache per GPU in bytes. By default, this is set to None and vllm can automatically infer the kv cache size based on gpu_memory_utilization. However, users may want to manually specify the kv cache memory size. kv_cache_memory_bytes allows more fine-grain control of how much memory gets used when compared with using gpu_memory_utilization. Note that kv_cache_memory_bytes (when not-None) ignores gpu_memory_utilization

-

(`cpu_offload_gb`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(cpu_offload_gb))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)`0`

) –The size (GiB) of CPU memory to use for offloading the model weights. This virtually increases the GPU memory space you can use to hold the model weights, at the cost of CPU-GPU data transfer for every forward pass.

-

(`offload_group_size`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(offload_group_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –Prefetch offloading: Group every N layers together. Offload last

`offload_num_in_group`

layers of each group. Default is 0 (disabled). -

(`offload_num_in_group`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(offload_num_in_group))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –Prefetch offloading: Number of layers to offload per group. Default is 1.

-

(`offload_prefetch_step`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(offload_prefetch_step))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –Prefetch offloading: Number of layers to prefetch ahead. Higher values hide more latency but use more GPU memory. Default is 1.

-

(`offload_params`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(offload_params))

, default:[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None`None`

) –Prefetch offloading: Set of parameter name segments to selectively offload. Only parameters whose names contain one of these segments will be offloaded (e.g., {"gate_up_proj", "down_proj"} for MLP weights, or {"w13_weight", "w2_weight"} for MoE expert weights). If None or empty, all parameters are offloaded.

-

(`enforce_eager`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(enforce_eager))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether to enforce eager execution. If True, we will disable CUDA graph and always execute the model in eager mode. If False, we will use CUDA graph and eager execution in hybrid.

-

(`enable_return_routed_experts`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(enable_return_routed_experts))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether to return routed experts.

-

(`disable_custom_all_reduce`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(disable_custom_all_reduce))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –See

[ParallelConfig](https://docs.vllm.ai/config/#vllm.config.ParallelConfig). -

(`hf_token`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(hf_token))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)|[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –The token to use as HTTP bearer authorization for remote files . If

`True`

, will use the token generated when running`hf auth login`

(stored in`~/.cache/huggingface/token`

). -

(`hf_overrides`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(hf_overrides))`HfOverrides | None`

, default:`None`

) –If a dictionary, contains arguments to be forwarded to the HuggingFace config. If a callable, it is called to update the HuggingFace config.

-

(`mm_processor_kwargs`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(mm_processor_kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Arguments to be forwarded to the model's processor for multi-modal data, e.g., image processor. Overrides for the multi-modal processor obtained from

`AutoProcessor.from_pretrained`

. The available overrides depend on the model that is being run. For example, for Phi-3-Vision:`{"num_crops": 4}`

. -

(`pooler_config`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(pooler_config))

, default:[PoolerConfig](https://docs.vllm.ai/config/#vllm.config.PoolerConfig)| None`None`

) –Initialize non-default pooling config for the pooling model, e.g.,

`PoolerConfig(seq_pooling_type="MEAN", use_activation=False)`

. -

(`compilation_config`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(compilation_config))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)|[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] |[CompilationConfig](https://docs.vllm.ai/config/#vllm.config.CompilationConfig)| None`None`

) –Either an integer or a dictionary. If it is an integer, it is used as the mode of compilation optimization. If it is a dictionary, it can specify the full compilation configuration.

-

(`attention_config`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(attention_config))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] |[AttentionConfig](https://docs.vllm.ai/config/#vllm.config.AttentionConfig)| None`None`

) –Configuration for attention mechanisms. Can be a dictionary or an AttentionConfig instance. If a dictionary, it will be converted to an AttentionConfig. Allows specifying the attention backend and other attention-related settings.

-

(`return_sampling_mask`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(return_sampling_mask))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Return each sampled token's post-processing support set. Requires Model Runner V2 and processed log probabilities.

-

(`spec_method`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(spec_method))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –Top-level alias for

`speculative_config["method"]`

. -

(`spec_model`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(spec_model))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –Top-level alias for

`speculative_config["model"]`

. -

(`spec_tokens`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(spec_tokens))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Top-level alias for

`speculative_config["num_speculative_tokens"]`

. -

(`**kwargs`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM(**kwargs))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`{}`

) –Arguments for

.`EngineArgs`


## Note

This class is intended to be used for offline inference. For online serving, use the [AsyncLLMEngine](https://docs.vllm.ai/#vllm.AsyncLLMEngine) class instead.

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.__init__)LLM constructor.

-
–[__repr__](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.__repr__)Return a transformers-style hierarchical view of the model.

-
–[apply_model](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.apply_model)Run a function directly on the model inside each worker,

-
–[chat](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.chat)Generate responses for a chat conversation.

-
–[collective_rpc](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.collective_rpc)Execute an RPC call on all workers.

-
–[enqueue](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.enqueue)Enqueue prompts for generation without waiting for completion.

-
–[enqueue_chat](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.enqueue_chat)Enqueue chat conversations for generation without waiting.

-
–[finish_weight_update](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.finish_weight_update)Finish the weight update and set its version if provided.

-
–[from_engine_args](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.from_engine_args)Create an LLM instance from EngineArgs.

-
–[generate](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.generate)Generates the completions for the input prompts.

-
–[get_metrics](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.get_metrics)Return a snapshot of aggregated metrics from Prometheus.

-
–[get_weight_version](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.get_weight_version)Return the latest committed weight version.

-
–[get_world_size](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.get_world_size)Get the world size from the parallel config.

-
–[init_weight_transfer_engine](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.init_weight_transfer_engine)Initialize weight transfer for RL training.

-
–[release_kv_cache_memory](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.release_kv_cache_memory)Release the GPU physical memory backing the KV cache.

-
–[sleep](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.sleep)Put the engine to sleep. The engine should not process any requests.

-
–[start_draft_weight_update](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.start_draft_weight_update)Start a new weight update targeting the speculative draft model.

-
–[start_profile](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.start_profile)Start profiling with optional custom trace prefix.

-
–[start_weight_update](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.start_weight_update)Start a new weight update.

-
–[update_weight_version](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.update_weight_version)Set the weight version without updating weights.

-
–[update_weights](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.update_weights)Update the weights of the model.

-
–[wait_for_completion](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.wait_for_completion)Wait for all enqueued requests to complete and return results.

-
–[wake_up](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.wake_up)Wake up the engine from sleep mode. See the

[sleep](https://docs.vllm.ai/#vllm.LLM.sleep)

## Source code in `vllm/entrypoints/llm.py`


|
|

###

`__init__(model, *, runner='auto', convert='auto', tokenizer=None, tokenizer_mode='auto', skip_tokenizer_init=False, trust_remote_code=False, allowed_local_media_path='', allowed_media_domains=None, tensor_parallel_size=1, dtype='auto', quantization=None, revision=None, tokenizer_revision=None, chat_template=None, seed=0, gpu_memory_utilization=0.92, cpu_offload_gb=0, offload_group_size=0, offload_num_in_group=1, offload_prefetch_step=1, offload_params=None, enforce_eager=False, enable_return_routed_experts=False, return_sampling_mask=False, disable_custom_all_reduce=False, hf_token=None, hf_overrides=None, mm_processor_kwargs=None, pooler_config=None, structured_outputs_config=None, profiler_config=None, attention_config=None, kv_cache_memory_bytes=None, compilation_config=None, quantization_config=None, logits_processors=None, spec_method=None, spec_model=None, spec_tokens=None, **kwargs)`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.__init__)

LLM constructor.

## Source code in `vllm/entrypoints/llm.py`


|
|

###

`__repr__()`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.__repr__)

Return a transformers-style hierarchical view of the model.

## Source code in `vllm/entrypoints/llm.py`


###

`apply_model(func)`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.apply_model)

Run a function directly on the model inside each worker, returning the result for each of them.

Warning

To reduce the overhead of data transfer, avoid returning large arrays or tensors from this method. If you must return them, make sure you move them to CPU first to avoid taking up additional VRAM!

## Source code in `vllm/entrypoints/llm.py`


###

`chat(messages, sampling_params=None, use_tqdm=True, lora_request=None, chat_template=None, chat_template_content_format='auto', add_generation_prompt=True, continue_final_message=False, tools=None, chat_template_kwargs=None, tokenization_kwargs=None, mm_processor_kwargs=None)`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.chat)

Generate responses for a chat conversation.

The chat conversation is converted into a text prompt using the tokenizer and calls the [generate](https://docs.vllm.ai/#vllm.LLM.generate) method to generate the responses.

Multi-modal inputs can be passed in the same way you would pass them to the OpenAI API.

Parameters:

-

(`messages`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.chat(messages))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[ChatCompletionMessageParam] |[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[ChatCompletionMessageParam]]A sequence of conversations or a single conversation.

- Each conversation is represented as a list of messages.
- Each message is a dictionary with 'role' and 'content' keys.

-

(`sampling_params`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.chat(sampling_params))

, default:[SamplingParams](https://docs.vllm.ai/sampling_params/#vllm.sampling_params.SamplingParams)|[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[SamplingParams](https://docs.vllm.ai/sampling_params/#vllm.sampling_params.SamplingParams)] | None`None`

) –The sampling parameters for text generation. If None, we use the default sampling parameters. When it is a single value, it is applied to every prompt. When it is a list, the list must have the same length as the prompts and it is paired one by one with the prompt.

-

(`use_tqdm`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.chat(use_tqdm))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)|[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[..., tqdm]`True`

) –If

`True`

, shows a tqdm progress bar. If a callable (e.g.,`functools.partial(tqdm, leave=False)`

), it is used to create the progress bar. If`False`

, no progress bar is created. -

(`lora_request`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.chat(lora_request))

, default:[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)] |[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)| None`None`

) –LoRA request to use for generation, if any.

-

(`chat_template`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.chat(chat_template))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –The template to use for structuring the chat. If not provided, the model's default chat template will be used.

-

(`chat_template_content_format`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.chat(chat_template_content_format))`ChatTemplateContentFormatOption`

, default:`'auto'`

) –The format to render message content.

- "string" will render the content as a string. Example:
`"Who are you?"`

- "openai" will render the content as a list of dictionaries, similar to OpenAI schema. Example:
`[{"type": "text", "text": "Who are you?"}]`


- "string" will render the content as a string. Example:
-

(`add_generation_prompt`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.chat(add_generation_prompt))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –If True, adds a generation template to each message.

-

(`continue_final_message`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.chat(continue_final_message))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If True, continues the final message in the conversation instead of starting a new one. Cannot be

`True`

if`add_generation_prompt`

is also`True`

. -

(`chat_template_kwargs`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.chat(chat_template_kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Additional kwargs to pass to the chat template.

-

(`tokenization_kwargs`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.chat(tokenization_kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Overrides for

`tokenizer.encode`

. -

(`mm_processor_kwargs`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.chat(mm_processor_kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Overrides for

`processor.__call__`

. -

(`tools`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.chat(tools))

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

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.collective_rpc)

Execute an RPC call on all workers.

Parameters:

-

(`method`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.collective_rpc(method))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)|[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[..., _R]Name of the worker method to execute, or a callable that is serialized and sent to all workers to execute.

If the method is a callable, it should accept an additional

`self`

argument, in addition to the arguments passed in`args`

and`kwargs`

. The`self`

argument will be the worker object. -

(`timeout`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.collective_rpc(timeout))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)| None`None`

) –Maximum time in seconds to wait for execution. Raises a

on timeout.`TimeoutError`

`None`

means wait indefinitely. -

(`args`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.collective_rpc(args))

, default:[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)`()`

) –Positional arguments to pass to the worker method.

-

(`kwargs`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.collective_rpc(kwargs))

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

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.enqueue)

Enqueue prompts for generation without waiting for completion.

This method adds requests to the engine queue but does not start processing them. Use wait_for_completion() to process the queued requests and get results.

Parameters:

-

(`prompts`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.enqueue(prompts))

) –[PromptType](https://docs.vllm.ai/inputs/#vllm.inputs.PromptType)|[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[PromptType](https://docs.vllm.ai/inputs/#vllm.inputs.PromptType)]The prompts to the LLM. See generate() for details.

-

(`sampling_params`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.enqueue(sampling_params))

, default:[SamplingParams](https://docs.vllm.ai/sampling_params/#vllm.sampling_params.SamplingParams)|[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[SamplingParams](https://docs.vllm.ai/sampling_params/#vllm.sampling_params.SamplingParams)] | None`None`

) –The sampling parameters for text generation.

-

(`lora_request`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.enqueue(lora_request))

, default:[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)] |[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)| None`None`

) –LoRA request to use for generation, if any.

-

(`priority`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.enqueue(priority))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | None`None`

) –The priority of the requests, if any.

-

(`use_tqdm`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.enqueue(use_tqdm))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)|[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[..., tqdm]`True`

) –If True, shows a tqdm progress bar while adding requests.

-

(`tokenization_kwargs`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.enqueue(tokenization_kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Overrides for

`tokenizer.encode`

. -

(`mm_processor_kwargs`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.enqueue(mm_processor_kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Overrides for

`processor.__call__`

.

Returns:

## Source code in `vllm/entrypoints/llm.py`


###

`enqueue_chat(messages, sampling_params=None, use_tqdm=True, lora_request=None, priority=None, chat_template=None, chat_template_content_format='auto', add_generation_prompt=True, continue_final_message=False, tools=None, chat_template_kwargs=None, tokenization_kwargs=None, mm_processor_kwargs=None)`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.enqueue_chat)

Enqueue chat conversations for generation without waiting.

This method renders chat conversations and adds the resulting requests to the engine queue. Use wait_for_completion() to get results. To guarantee that all requests are queued before scheduling starts, pause scheduling with sleep(level=0) before calling this method and resume it with wake_up(tags=["scheduling"]) afterward.

Parameters:

-

(`messages`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.enqueue_chat(messages))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[ChatCompletionMessageParam] |[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[ChatCompletionMessageParam]]A sequence of conversations or a single conversation. Each conversation is represented as a list of messages.

-

(`sampling_params`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.enqueue_chat(sampling_params))

, default:[SamplingParams](https://docs.vllm.ai/sampling_params/#vllm.sampling_params.SamplingParams)|[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[SamplingParams](https://docs.vllm.ai/sampling_params/#vllm.sampling_params.SamplingParams)] | None`None`

) –The sampling parameters for text generation. If None, we use the default sampling parameters.

-

(`use_tqdm`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.enqueue_chat(use_tqdm))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)|[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[..., tqdm]`True`

) –If

`True`

, shows a tqdm progress bar while rendering conversations. -

(`lora_request`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.enqueue_chat(lora_request))

, default:[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)] |[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)| None`None`

) –LoRA request to use for generation, if any.

-

(`priority`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.enqueue_chat(priority))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | None`None`

) –The priority of the requests, if any.

-

(`chat_template`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.enqueue_chat(chat_template))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –The template to use for structuring the chat.

-

(`chat_template_content_format`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.enqueue_chat(chat_template_content_format))`ChatTemplateContentFormatOption`

, default:`'auto'`

) –The format to render message content.

-

(`add_generation_prompt`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.enqueue_chat(add_generation_prompt))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –If True, adds a generation template to each message.

-

(`continue_final_message`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.enqueue_chat(continue_final_message))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If True, continues the final message in the conversation instead of starting a new one.

-

(`tools`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.enqueue_chat(tools))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)]] | None`None`

) –Tools to make available to the model, if any.

-

(`chat_template_kwargs`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.enqueue_chat(chat_template_kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Additional kwargs to pass to the chat template.

-

(`tokenization_kwargs`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.enqueue_chat(tokenization_kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Overrides for

`tokenizer.encode`

. -

(`mm_processor_kwargs`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.enqueue_chat(mm_processor_kwargs))

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

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.finish_weight_update)

Finish the weight update and set its version if provided.

## Source code in `vllm/entrypoints/llm.py`


###

`from_engine_args(engine_args)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.from_engine_args)

###

`generate(prompts, sampling_params=None, *, use_tqdm=True, lora_request=None, priority=None, tokenization_kwargs=None, mm_processor_kwargs=None)`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.generate)

Generates the completions for the input prompts.

This class automatically batches the given prompts, considering the memory constraint. For the best performance, put all of your prompts into a single list and pass it to this method.

Parameters:

-

(`prompts`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.generate(prompts))

) –[PromptType](https://docs.vllm.ai/inputs/#vllm.inputs.PromptType)|[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[PromptType](https://docs.vllm.ai/inputs/#vllm.inputs.PromptType)]The prompts to the LLM. You may pass a sequence of prompts for batch inference. See

[PromptType](https://docs.vllm.ai/inputs/#vllm.inputs.PromptType)for more details about the format of each prompt. -

(`sampling_params`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.generate(sampling_params))

, default:[SamplingParams](https://docs.vllm.ai/sampling_params/#vllm.sampling_params.SamplingParams)|[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[SamplingParams](https://docs.vllm.ai/sampling_params/#vllm.sampling_params.SamplingParams)] | None`None`

) –The sampling parameters for text generation. If None, we use the default sampling parameters. When it is a single value, it is applied to every prompt. When it is a list, the list must have the same length as the prompts and it is paired one by one with the prompt.

-

(`use_tqdm`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.generate(use_tqdm))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)|[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[..., tqdm]`True`

) –If

`True`

, shows a tqdm progress bar. If a callable (e.g.,`functools.partial(tqdm, leave=False)`

), it is used to create the progress bar. If`False`

, no progress bar is created. -

(`lora_request`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.generate(lora_request))

, default:[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)] |[LoRARequest](https://docs.vllm.ai/lora/request/#vllm.lora.request.LoRARequest)| None`None`

) –LoRA request to use for generation, if any.

-

(`priority`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.generate(priority))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | None`None`

) –The priority of the requests, if any. Only applicable when priority scheduling policy is enabled. If provided, must be a list of integers matching the length of

`prompts`

, where each priority value corresponds to the prompt at the same index. -

(`tokenization_kwargs`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.generate(tokenization_kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –Overrides for

`tokenizer.encode`

. -

(`mm_processor_kwargs`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.generate(mm_processor_kwargs))

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

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.get_metrics)

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

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.get_weight_version)

###

`get_world_size(include_dp=True)`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.get_world_size)

Get the world size from the parallel config.

Parameters:

-

(`include_dp`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.get_world_size(include_dp))

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

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.init_weight_transfer_engine)

Initialize weight transfer for RL training.

Parameters:

-

(`request`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.init_weight_transfer_engine(request))

) –[WeightTransferInitRequest](https://docs.vllm.ai/distributed/weight_transfer/base/#vllm.distributed.weight_transfer.base.WeightTransferInitRequest)|[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)Weight transfer initialization request with backend-specific info


## Source code in `vllm/entrypoints/llm.py`


###

`release_kv_cache_memory()`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.release_kv_cache_memory)

Release the GPU physical memory backing the KV cache.

Requires a completed `sleep(level=0)`

and resident executor memory. Restore with `wake_up(tags=["kv_cache"])`

; kept requests are recomputed.

## Source code in `vllm/entrypoints/llm.py`


###

`sleep(level=1, mode='abort')`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.sleep)

Put the engine to sleep. The engine should not process any requests. The caller should guarantee that no requests are being processed during the sleep period, before `wake_up`

is called.

Parameters:

-

(`level`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.sleep(level))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –The sleep level. - Level 0: Pause scheduling but continue accepting requests. Requests are queued but not processed. - Level 1: Offload model weights to CPU, discard KV cache. The content of kv cache is forgotten. Good for sleeping and waking up the engine to run the same model again. Please make sure there's enough CPU memory to store the model weights. - Level 2: Discard all GPU memory (weights + KV cache). Good for sleeping and waking up the engine to run a different model or update the model, where previous model weights are not needed. It reduces CPU memory pressure.

-

(`mode`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.sleep(mode))`PauseMode`

, default:`'abort'`

) –How to handle any existing requests, can be "abort", "wait", or "keep".


## Source code in `vllm/entrypoints/llm.py`


###

`start_draft_weight_update()`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.start_draft_weight_update)

###

`start_profile(profile_prefix=None)`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.start_profile)

Start profiling with optional custom trace prefix.

Parameters:

-

(`profile_prefix`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.start_profile(profile_prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –Optional prefix for the trace file names. If provided, trace files will be named as "

_dp _pp _tp ". If not provided, default naming will be used.

## Source code in `vllm/entrypoints/llm.py`


###

`start_weight_update()`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.start_weight_update)

###

`update_weight_version(new_version)`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.update_weight_version)

###

`update_weights(request)`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.update_weights)

Update the weights of the model.

Parameters:

-

(`request`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.update_weights(request))

) –[WeightTransferUpdateRequest](https://docs.vllm.ai/distributed/weight_transfer/base/#vllm.distributed.weight_transfer.base.WeightTransferUpdateRequest)|[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)Weight update request with backend-specific update info


## Source code in `vllm/entrypoints/llm.py`


###

`wait_for_completion(output_type=None, *, use_tqdm=True)`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.wait_for_completion)

Wait for all enqueued requests to complete and return results.

This method processes all requests currently in the engine queue and returns their outputs. Use after enqueue() to get results.

Parameters:

-

(`output_type`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.wait_for_completion(output_type))

, default:[type](https://docs.python.org/3/builtins/functions.html#type)[[Any](https://docs.python.org/3/library/typing.html#typing.Any)] |[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[type](https://docs.python.org/3/builtins/functions.html#type)[[Any](https://docs.python.org/3/library/typing.html#typing.Any)], ...] | None`None`

) –The expected output type(s). If not provided, accepts both RequestOutput and PoolingRequestOutput.

-

(`use_tqdm`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.wait_for_completion(use_tqdm))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)|[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[..., tqdm]`True`

) –If True, shows a tqdm progress bar.


Returns:

## Source code in `vllm/entrypoints/llm.py`


###

`wake_up(tags=None)`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.wake_up)

Wake up the engine from sleep mode. See the [sleep](https://docs.vllm.ai/#vllm.LLM.sleep) method for more details.

Parameters:

-

(`tags`

[¶](https://docs.vllm.ai#vllm.entrypoints.llm.LLM.wake_up(tags))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None`None`

) –An optional list of tags to reallocate the engine memory for specific memory allocations. Values must be in

`("weights", "kv_cache", "scheduling")`

. If None, all memory is reallocated. wake_up should be called with all tags (or None) before the engine is used again. Use tags=["scheduling"] to resume from level 0 sleep.