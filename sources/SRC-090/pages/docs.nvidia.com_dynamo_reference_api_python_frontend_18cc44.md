source: https://docs.nvidia.com/dynamo/reference/api/python/frontend
lastmod: 2026-09-24T19:58:16.636Z

# dynamo.frontend

OpenAI-compatible HTTP frontend, argument parsing, and pre/post-processing.

`dynamo.frontend`

publishes 12 classes and 31 functions. Source: `components/src/dynamo/frontend/__init__.py`


###### EngineFactory (class)


No summary available.

`components/src/dynamo/frontend/vllm_processor.py#L931`


**Public methods**

**init**

No summary available.

#### chat_engine_factory

Called by Rust when a model is discovered.

###### FrontendArgGroup (class)


Frontend configuration parameters.

`components/src/dynamo/frontend/frontend_args.py#L171`


**Public methods**

#### add_arguments

No summary available.

###### FrontendConfig (class)


Configuration for the Dynamo frontend.

`components/src/dynamo/frontend/frontend_args.py#L53`


**Public methods**

#### validate

No summary available.

###### PreprocessError (class)


Raised by preprocess workers for user-facing errors (e.g., n!=1).

Carries a plain message because the worker→main-process boundary pickles the exception; the main process re-raises a Dynamo-typed exception so PyO3 can route it through the proper backend-error path.

`components/src/dynamo/frontend/utils.py#L83`


**Public methods**

**init**

No summary available.

###### PreprocessResult (class)


No summary available.

`components/src/dynamo/frontend/prepost.py#L45`


**Public methods**

**init**

No summary available.

###### SglangEngineFactory (class)


No summary available.

`components/src/dynamo/frontend/sglang_processor.py#L784`


**Public methods**

**init**

No summary available.

#### chat_engine_factory

Called by Rust when a model is discovered.

###### SglangPreprocessResult (class)


Result of SGLang preprocessing.

`components/src/dynamo/frontend/sglang_prepost.py#L43`


**Public methods**

**init**

No summary available.

###### SglangPreprocessWorkerResult (class)


Picklable return value from the SGLang preprocess worker.

`components/src/dynamo/frontend/sglang_processor.py#L176`


**Public methods**

**init**

No summary available.

###### SglangProcessor (class)


No summary available.

`components/src/dynamo/frontend/sglang_processor.py#L355`


**Public methods**

**init**

No summary available.

#### generator

Main entry point: preprocess, route, post-process a chat request.

###### SglangStreamingPostProcessor (class)


Streaming post-processor using SGLang parsers and HF tokenizer detokenization.

Handles:

- Incremental detokenization across tokenizer-safe boundaries
- Reasoning content extraction via SGLang ReasoningParser
- Tool call parsing via SGLang FunctionCallParser or JsonArrayParser

`components/src/dynamo/frontend/sglang_prepost.py#L953`


**Public methods**

**init**

No summary available.

#### process_output

Process a single engine response chunk into an OpenAI SSE choice dict.

**Parameters**

Dict with `token_ids`

and optional `finish_reason`

.

**Returns**

`dict[str, Any] | None`

— OpenAI choice dict or`None`

if nothing to emit yet.

###### StreamingPostProcessor (class)


No summary available.

`components/src/dynamo/frontend/prepost.py#L597`


**Public methods**

**init**

No summary available.

#### process_output

No summary available.

###### VllmProcessor (class)


No summary available.

`components/src/dynamo/frontend/vllm_processor.py#L268`


**Public methods**

**init**

No summary available.

#### generator

Run a single request through the engine. Does pre and post processing on this machine, delegates model inference to a backend using the router.

###### apply_default_thinking_mode_to_template_kwargs (function)


Merge deployment thinking default unless the request already controls it.

###### async_main (function)


Main async entry point for the Dynamo frontend.

Initializes the distributed runtime, configures routing, and starts the HTTP server or interactive mode based on command-line arguments.

###### build_response_format_guided_decoding (function)


Build Dynamo guided decoding from OpenAI chat response_format.

###### build_tool_call_guided_decoding (function)


Build tool-call guidance through vLLM’s configured tool parser.

###### build_tool_call_guided_decoding (function)


Build native-SGLang-like tool call constraints for guided decoding.

###### convert_tools (function)


Convert OpenAI tool dicts to SGLang Tool objects.

###### create_parsers (function)


Create tool call and reasoning parsers for a request.

Shared by both the single-process preprocessing path and the pool path (which must recreate non-picklable parsers in the main process).

If `sglang_tools`

is provided, reuses them; otherwise converts from
the request’s `tools`

field.

For `tool_choice="required"`

or a named function, uses
`JsonArrayParser`

(matching native SGLang) since guided decoding
constrains the output to a JSON array. Otherwise uses the model-specific
`FunctionCallParser`

.

###### detect_force_reasoning_from_template (function)


Return True if the chat template auto-opens a reasoning block.

Intended to be called once at processor startup with
`tokenizer.chat_template`

and cached on the processor.

###### extract_mm_urls (function)


Extract media and vLLM image processor-cache UUIDs from chat messages.

URL-backed parts become `Url`

variants. Image parts with no URL and an
opaque `uuid`

become `UuidOnly`

variants for vLLM’s multimodal
processor cache. Cache UUIDs on audio and video are rejected. Image UUID
lists preserve slot order

The UUID map is `None`

when no user UUID is present. A media content part
with neither a URL nor UUID is rejected instead of being silently dropped.

###### graceful_shutdown (function)


Handle graceful shutdown of the distributed runtime.

**Parameters**

The DistributedRuntime instance to shut down.

###### handle_engine_error (function)


Classify an invalid engine response and return an OpenAI-style error dict.

Called when engine_response is None or missing ‘token_ids’.

###### load_frontend_route_extensions (function)


Load trusted frontend route extensions.

Each value is either a name registered under the `dynamo.frontend.routes`

entry-point group (preferred) or a direct `module:function`

path.

###### main (function)


###### make_backend_error (function)


Build an OpenAI-style error dict, guarding against None/missing message.

###### make_internal_error (function)


Build an OpenAI-style internal error dict with request-specific fallback.

###### map_finish_reason (function)


###### nvext_extra_field_requested (function)


Return whether a request opted into a response nvext field.

###### parse_args (function)


Parse command-line arguments for the Dynamo frontend.

**Returns**

`tuple[FrontendConfig, Optional[Namespace], Optional[Namespace]]`

— Tuple of (FrontendConfig, vllm_flags, sglang_flags).

###### preprocess_chat_request (function)


###### preprocess_chat_request (function)


Preprocess a chat request using SGLang tokenizer and parser APIs.

`template_force_reasoning`

is the static per-server flag derived from
the chat template (see `detect_force_reasoning_from_template`

);
the effective per-request value combines it with the configured parser and
request-level thinking controls.

Synchronous — suitable for both main-process and worker-process execution.

###### random_call_id (function)


###### random_uuid (function)


###### read_jinja_chat_template (function)


Read a Jinja chat template using backend-specific file semantics.

###### resolve_chat_template (function)


Return a chat template stored beside the model, or None.

Covers models (e.g. Qwen3-Omni) whose template lives in chat_template.json or chat_template.jinja rather than tokenizer_config.json, which the HF tokenizer does not merge. The backend selects native .jinja file semantics.

###### resolve_request_force_reasoning (function)


Resolve the effective force_reasoning flag for a single request.

Mirrors sglang.srt.entrypoints.openai.serving_chat._get_reasoning_from_request combined with template_manager.force_reasoning:

- opt-out families (
`glm45`

/`qwen3`

/`kimi_k2`

/…): on by default,`chat_template_kwargs.enable_thinking=False`

(or`thinking=False`

for`kimi_k2`

) disables it. - MiniMax-M3 defaults to adaptive, but SGLang still enables the
reasoning parser unless
`chat_template_kwargs.thinking_mode`

is explicitly`"disabled"`

. - Mistral is enabled only when
`reasoning_effort`

is present and not`"none"`

. - opt-in families (
`deepseek-v3`

/`gemma4`

): off by default, enabled by`chat_template_kwargs.{thinking,enable_thinking}=True`

. - anything else: follow the statically-detected template default.

###### runtime_default_thinking_mode (function)


Read deployment-level default thinking mode from model runtime metadata.

###### setup_engine_factory (function)


When using vllm pre and post processor, create the EngineFactory that creates the engines that run requests.

###### setup_sglang_engine_factory (function)


When using sglang pre and post processor, create the SglangEngineFactory that creates the engines that run requests.

###### validate_model_name (function)


###### validate_model_path (function)


Validate that model-path is a valid directory on disk.

###### worker_warmup (function)


Dummy task to ensure a ProcessPoolExecutor worker is fully initialized.