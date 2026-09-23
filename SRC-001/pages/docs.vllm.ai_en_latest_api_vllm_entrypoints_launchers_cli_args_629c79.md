source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/launchers/cli_args/
lastmod: 2026-09-23

#

`vllm.entrypoints.launchers.cli_args`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args)

This file contains the command line arguments for the vLLM's online server. It is kept in a separate file for documentation purposes.

Classes:

-
–[BaseFrontendArgs](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs)Base arguments for the OpenAI-compatible frontend server.

-
–[FrontendArgs](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs)Arguments for the OpenAI-compatible frontend server.


Functions:

-
–[make_arg_parser](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.make_arg_parser)Create the CLI argument parser used by the OpenAI API server.

-
–[resolve_default_chat_template_kwargs](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.resolve_default_chat_template_kwargs)Resolve renderer defaults, including the dedicated Cohere format flag.

-
–[validate_parsed_serve_args](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.validate_parsed_serve_args)Quick checks for model serve args that raise prior to loading.


##

`BaseFrontendArgs`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs)

Base arguments for the OpenAI-compatible frontend server.

This base class does not include host, port, and server-specific arguments like SSL, CORS, and HTTP server settings. Those arguments are added by the subclasses.

Methods:

-
–[add_cli_args](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.add_cli_args)Register CLI arguments for this frontend class.


Attributes:

-
([chat_template](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.chat_template)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe file path to the chat template, or the template in single-line form

-
([chat_template_content_format](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.chat_template_content_format)`ChatTemplateContentFormatOption`

) –The format to render message content within a chat template.

-
([cohere_format](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.cohere_format)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Cohere

`--tokenizer-mode cohere`

only. Which Cohere prompt -
([cohere_is_reasoning_model](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.cohere_is_reasoning_model)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Cohere

`/cohere/v2/chat`

only. Whether the served model is a -
([default_chat_template_kwargs](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.default_chat_template_kwargs)

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | NoneDefault keyword arguments to pass to the chat template renderer.

-
([enable_auto_tool_choice](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.enable_auto_tool_choice)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable auto tool choice for supported models. Use

`--tool-call-parser`

-
([enable_force_include_usage](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.enable_force_include_usage)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If set to True, including usage on every request.

-
([enable_log_deltas](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.enable_log_deltas)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If set to False, output deltas will not be logged. Relevant only if

-
([enable_log_outputs](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.enable_log_outputs)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If set to True, log model outputs (generations). Requires

-
([enable_per_request_metrics](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.enable_per_request_metrics)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If set to True, include per-request timing metrics in API responses.

-
([enable_prompt_tokens_details](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.enable_prompt_tokens_details)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If set to True, enable prompt_tokens_details in usage.

-
([enable_scale_out](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.enable_scale_out)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If set to True, register the scale-out endpoints (

`/render`

,`/derender`

, -
([enable_server_load_tracking](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.enable_server_load_tracking)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If set to True, enable tracking server_load_metrics in the app state.

-
([enable_tokenizer_info_endpoint](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.enable_tokenizer_info_endpoint)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable the

`/tokenizer_info`

endpoint. May expose chat -
([exclude_tools_when_tool_choice_none](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.exclude_tools_when_tool_choice_none)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If specified, exclude tool definitions in prompts when

-
([fingerprint_mode](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.fingerprint_mode)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['full', 'hash', 'custom', 'none']Controls the

`system_fingerprint`

field on responses. -
([fingerprint_value](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.fingerprint_value)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneLiteral fingerprint string used when

`--fingerprint-mode=custom`

. -
([log_config_file](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.log_config_file)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NonePath to logging config JSON file for both vllm and uvicorn

-
([log_error_stack](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.log_error_stack)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If set to True, log the stack trace of error responses

-
([lora_modules](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.lora_modules)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[LoRAModulePath] | NoneLoRA modules configurations in either 'name=path' format or JSON format

-
([max_log_len](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.max_log_len)

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneMax number of prompt characters or prompt ID numbers being printed in

-
([response_role](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.response_role)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The role name to return if

`request.add_generation_prompt=true`

. -
([return_tokens_as_token_ids](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.return_tokens_as_token_ids)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)When

`--max-logprobs`

is specified, represents single tokens as -
([sse_keep_alive_interval](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.sse_keep_alive_interval)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Send an SSE keep-alive comment line every this many seconds when a

-
([tokens_only](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.tokens_only)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If set to True, only enable the Tokens In<>Out endpoint.

-
([tool_call_parser](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.tool_call_parser)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneSelect the tool call parser depending on the model that you're using.

-
([tool_parser_plugin](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.tool_parser_plugin)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Special the tool parser plugin write to parse the model-generated tool

-
([tool_server](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.tool_server)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneComma-separated list of host:port pairs (IPv4, IPv6, or hostname).

-
([tool_strict_level](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.tool_strict_level)`ToolStrictLevelName`

) –Server-side floor for structural-tag based tool calling, applied on top

-
([trust_request_chat_template](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.trust_request_chat_template)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to trust the chat template provided in the request. If False,


## Source code in `vllm/entrypoints/launchers/cli_args.py`


|
|

###

`chat_template = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.chat_template)

The file path to the chat template, or the template in single-line form for the specified model.

###

`chat_template_content_format = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.chat_template_content_format)

The format to render message content within a chat template.

- "string" will render the content as a string. Example:
`"Hello World"`

- "openai" will render the content as a list of dictionaries, similar to OpenAI schema. Example:
`[{"type": "text", "text": "Hello world!"}]`


###

`cohere_format = 'cmd4'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.cohere_format)

Cohere `--tokenizer-mode cohere`

only. Which Cohere prompt format to render: `cmd4`

(current Command A+ models; default) or `cmd3`

(earlier Cmd-A and Cmd-A reasoning models). Selecting the wrong format silently produces a prompt the model wasn't trained on, which most commonly manifests as the model emitting text but no citations / tool calls / thinking blocks. Equivalent to passing `--default-chat-template-kwargs '{"cohere_format": "..."}'`

-- any explicit request-level `chat_template_kwargs.cohere_format`

takes priority.

###

`cohere_is_reasoning_model = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.cohere_is_reasoning_model)

Cohere `/cohere/v2/chat`

only. Whether the served model is a reasoning Command-family model. When True (default), the assistant's chain-of-thought is surfaced as a `thinking`

content block (or `content-*`

events on the stream). When False, reasoning is surfaced as Cohere's `tool_plan`

field (or `tool-plan-delta`

events) whenever the model emits tool calls, matching older non- reasoning Command models. Has no effect on the non-Cohere endpoints.

###

`default_chat_template_kwargs = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.default_chat_template_kwargs)

Default keyword arguments to pass to the chat template renderer. These will be merged with request-level chat_template_kwargs, with request values taking precedence. Useful for setting default behavior for reasoning models. Example: '{"enable_thinking": false}' to disable thinking mode by default for Qwen3/DeepSeek models.

###

`enable_auto_tool_choice = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.enable_auto_tool_choice)

Enable auto tool choice for supported models. Use `--tool-call-parser`

to specify which parser to use.

###

`enable_force_include_usage = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.enable_force_include_usage)

If set to True, including usage on every request.

###

`enable_log_deltas = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.enable_log_deltas)

If set to False, output deltas will not be logged. Relevant only if --enable-log-outputs is set.

###

`enable_log_outputs = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.enable_log_outputs)

If set to True, log model outputs (generations). Requires `--enable-log-requests`

. Output text and finish reasons are logged at INFO, while output token IDs are logged at DEBUG.

###

`enable_per_request_metrics = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.enable_per_request_metrics)

If set to True, include per-request timing metrics in API responses.

###

`enable_prompt_tokens_details = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.enable_prompt_tokens_details)

If set to True, enable prompt_tokens_details in usage.

###

`enable_scale_out = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.enable_scale_out)

If set to True, register the scale-out endpoints (`/render`

, `/derender`

, and `/inference/v1/generate`

) on `vllm serve`

. Has no effect on `vllm launch render`

or `vllm serve --tokens-only`

, which always register their required endpoints regardless of this flag.

###

`enable_server_load_tracking = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.enable_server_load_tracking)

If set to True, enable tracking server_load_metrics in the app state.

###

`enable_tokenizer_info_endpoint = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.enable_tokenizer_info_endpoint)

Enable the `/tokenizer_info`

endpoint. May expose chat templates and other tokenizer configuration.

###

`exclude_tools_when_tool_choice_none = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.exclude_tools_when_tool_choice_none)

If specified, exclude tool definitions in prompts when tool_choice='none'.

###

`fingerprint_mode = 'full'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.fingerprint_mode)

Controls the `system_fingerprint`

field on responses.

`full`

(default):`vllm-<version>[-<parallelism>]-<hash8>`

. Encodes server version, non-trivial parallelism degrees (tp/pp/dp/ep), and an 8-char config hash.`hash`

:`vllm-<version>-<hash8>`

. Parallelism stripped.`custom`

: emits the literal string from`--fingerprint-value`

.`none`

: the field is omitted (serialized as`null`

).

###

`fingerprint_value = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.fingerprint_value)

Literal fingerprint string used when `--fingerprint-mode=custom`

.

###

`log_config_file = envs.VLLM_LOGGING_CONFIG_PATH`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.log_config_file)

Path to logging config JSON file for both vllm and uvicorn

###

`log_error_stack = envs.VLLM_SERVER_DEV_MODE`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.log_error_stack)

If set to True, log the stack trace of error responses

###

`lora_modules = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.lora_modules)

LoRA modules configurations in either 'name=path' format or JSON format or JSON list format. Example (old format): `'name=path'`

Example (new format): `{"name": "name", "path": "lora_path", "base_model_name": "id"}`


###

`max_log_len = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.max_log_len)

Max number of prompt characters or prompt ID numbers being printed in log. The default of None means unlimited.

###

`response_role = 'assistant'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.response_role)

The role name to return if `request.add_generation_prompt=true`

.

###

`return_tokens_as_token_ids = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.return_tokens_as_token_ids)

When `--max-logprobs`

is specified, represents single tokens as strings of the form 'token_id:{token_id}' so that tokens that are not JSON-encodable can be identified.

###

`sse_keep_alive_interval = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.sse_keep_alive_interval)

Send an SSE keep-alive comment line every this many seconds when a `/v1/chat/completions`

or `/v1/completions`

streaming response is idle (queued, prefill, or between tokens), to prevent reverse proxies/tunnels with read timeouts from closing the connection. Defaults to 0, which disables keep-alive comments entirely.

###

`tokens_only = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.tokens_only)

If set to True, only enable the Tokens In<>Out endpoint. This is intended for use in a Disaggregated Everything setup.

###

`tool_call_parser = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.tool_call_parser)

Select the tool call parser depending on the model that you're using. This is used to parse the model-generated tool call into OpenAI API format. Required for `--enable-auto-tool-choice`

. You can choose any option from the built-in parsers or register a plugin via `--tool-parser-plugin`

.

###

`tool_parser_plugin = ''`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.tool_parser_plugin)

Special the tool parser plugin write to parse the model-generated tool into OpenAI API format, the name register in this plugin can be used in `--tool-call-parser`

.

###

`tool_server = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.tool_server)

Comma-separated list of host:port pairs (IPv4, IPv6, or hostname). Examples: 127.0.0.1:8000, [::1]:8000, localhost:1234. Or `demo`

for built-in demo tools (browser and Python code interpreter). WARNING: The `demo`

Python tool executes model-generated code in Docker without network isolation by default. See the security guide for more information.

###

`tool_strict_level = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.tool_strict_level)

Server-side floor for structural-tag based tool calling, applied on top of the per-tool `strict`

field. `auto`

follows the request's tool choice and per-tool strictness; `function`

constrains the tool-call envelope (markup and function name) for every request with tools; `parameter`

additionally pins argument schemas, as if every tool were `strict: true`

.

###

`trust_request_chat_template = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.trust_request_chat_template)

Whether to trust the chat template provided in the request. If False, the server will always use the chat template specified by `--chat-template`

or the ones from tokenizer.

###

`_customize_cli_kwargs(frontend_kwargs)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs._customize_cli_kwargs)

Customize argparse kwargs before arguments are registered.

Subclasses should override this and call `super()._customize_cli_kwargs(frontend_kwargs)`

first.

## Source code in `vllm/entrypoints/launchers/cli_args.py`


###

`add_cli_args(parser)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs.add_cli_args)

Register CLI arguments for this frontend class.

Subclasses should override `_customize_cli_kwargs`

instead of this method so that base-class postprocessing is always applied.

## Source code in `vllm/entrypoints/launchers/cli_args.py`


##

`FrontendArgs`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs)

Bases: [BaseFrontendArgs](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.BaseFrontendArgs)

Arguments for the OpenAI-compatible frontend server.

Attributes:

-
([allow_credentials](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.allow_credentials)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Allow credentials.

-
([allowed_headers](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.allowed_headers)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Allowed headers.

-
([allowed_methods](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.allowed_methods)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Allowed methods.

-
([allowed_origins](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.allowed_origins)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Allowed origins.

-
([api_key](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.api_key)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | NoneIf provided, the server will require one of these keys to be presented in

-
([data_parallel_supervisor_port](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.data_parallel_supervisor_port)

) –[int](https://docs.python.org/3/builtins/functions.html#int)HTTP port for aggregated health endpoints in multi-port external LB

-
([disable_access_log_for_endpoints](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.disable_access_log_for_endpoints)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneComma-separated list of endpoint paths to exclude from uvicorn access

-
([disable_fastapi_docs](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.disable_fastapi_docs)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Disable FastAPI's OpenAPI schema, Swagger UI, and ReDoc endpoint.

-
([disable_uvicorn_access_log](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.disable_uvicorn_access_log)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Disable uvicorn access log.

-
([dp_supervisor_probe_failure_threshold](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.dp_supervisor_probe_failure_threshold)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of consecutive connection-error retries before a child health

-
([dp_supervisor_probe_interval_s](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.dp_supervisor_probe_interval_s)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Seconds between aggregated health probes in multi-port external LB mode.

-
([dp_supervisor_probe_timeout_s](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.dp_supervisor_probe_timeout_s)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Seconds to wait between retries when a child health probe fails with a

-
([enable_flash_late_interaction](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.enable_flash_late_interaction)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If set, run pooling score MaxSim on GPU in the API server process.

-
([enable_offline_docs](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.enable_offline_docs)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable offline FastAPI documentation for air-gapped environments.

-
([enable_request_id_headers](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.enable_request_id_headers)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)If specified, API server will add X-Request-Id header to responses.

-
([enable_ssl_refresh](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.enable_ssl_refresh)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Refresh SSL Context when SSL certificate files change

-
([h11_max_header_count](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.h11_max_header_count)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum number of HTTP headers allowed in a request for h11 parser.

-
([h11_max_incomplete_event_size](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.h11_max_incomplete_event_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum size (bytes) of an incomplete HTTP event (header or body) for

-
([host](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.host)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneHost name.

-
([middleware](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.middleware)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Additional ASGI middleware to apply to the app. We accept multiple

-
([port](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.port)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Port number.

-
([root_path](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.root_path)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneFastAPI root_path when app is behind a path based routing proxy.

-
([ssl_ca_certs](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.ssl_ca_certs)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe CA certificates file.

-
([ssl_cert_reqs](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.ssl_cert_reqs)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Whether client certificate is required (see stdlib ssl module's).

-
([ssl_certfile](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.ssl_certfile)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe file path to the SSL cert file.

-
([ssl_ciphers](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.ssl_ciphers)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneSSL cipher suites for HTTPS (TLS 1.2 and below only).

-
([ssl_keyfile](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.ssl_keyfile)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe file path to the SSL key file.

-
([uds](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.uds)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneUnix domain socket path. If set, host and port arguments are ignored.

-
([uvicorn_log_level](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.uvicorn_log_level)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['critical', 'error', 'warning', 'info', 'debug', 'trace']Log level for uvicorn.


## Source code in `vllm/entrypoints/launchers/cli_args.py`


|
|

###

`allow_credentials = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.allow_credentials)

Allow credentials.

###

`allowed_headers = field(default_factory=(lambda: ['*']))`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.allowed_headers)

Allowed headers.

###

`allowed_methods = field(default_factory=(lambda: ['*']))`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.allowed_methods)

Allowed methods.

###

`allowed_origins = field(default_factory=(lambda: ['*']))`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.allowed_origins)

Allowed origins.

###

`api_key = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.api_key)

If provided, the server will require one of these keys to be presented in the header.

Warning: this only authenticates endpoints under the `/v1`

, `/v2`

, and `/inference`

path prefixes. Other endpoints on the same server, including `/invocations`

(which exposes the same inference capabilities as `/v1`

), remain unauthenticated. Do not rely on `--api-key`

alone to secure vLLM; see https://docs.vllm.ai/en/latest/usage/security.html#api-key-authentication-limitations for what it does and does not protect.

###

`data_parallel_supervisor_port = 9256`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.data_parallel_supervisor_port)

HTTP port for aggregated health endpoints in multi-port external LB mode.

###

`disable_access_log_for_endpoints = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.disable_access_log_for_endpoints)

Comma-separated list of endpoint paths to exclude from uvicorn access logs. This is useful to reduce log noise from high-frequency endpoints like health checks. Example: "/health,/metrics,/ping". When set, access logs for requests to these paths will be suppressed while keeping logs for other endpoints.

###

`disable_fastapi_docs = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.disable_fastapi_docs)

Disable FastAPI's OpenAPI schema, Swagger UI, and ReDoc endpoint.

###

`disable_uvicorn_access_log = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.disable_uvicorn_access_log)

Disable uvicorn access log.

###

`dp_supervisor_probe_failure_threshold = 3`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.dp_supervisor_probe_failure_threshold)

Number of consecutive connection-error retries before a child health probe is declared failed in multi-port external LB mode.

###

`dp_supervisor_probe_interval_s = 5.0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.dp_supervisor_probe_interval_s)

Seconds between aggregated health probes in multi-port external LB mode.

###

`dp_supervisor_probe_timeout_s = 5.0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.dp_supervisor_probe_timeout_s)

Seconds to wait between retries when a child health probe fails with a connection error in multi-port external LB mode.

###

`enable_flash_late_interaction = True`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.enable_flash_late_interaction)

If set, run pooling score MaxSim on GPU in the API server process. Can significantly improve late-interaction scoring performance.

###

`enable_offline_docs = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.enable_offline_docs)

Enable offline FastAPI documentation for air-gapped environments. Uses vendored static assets bundled with vLLM.

###

`enable_request_id_headers = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.enable_request_id_headers)

If specified, API server will add X-Request-Id header to responses.

###

`enable_ssl_refresh = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.enable_ssl_refresh)

Refresh SSL Context when SSL certificate files change

###

`h11_max_header_count = H11_MAX_HEADER_COUNT_DEFAULT`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.h11_max_header_count)

Maximum number of HTTP headers allowed in a request for h11 parser. Helps mitigate header abuse. Default: 256.

###

`h11_max_incomplete_event_size = H11_MAX_INCOMPLETE_EVENT_SIZE_DEFAULT`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.h11_max_incomplete_event_size)

Maximum size (bytes) of an incomplete HTTP event (header or body) for h11 parser. Helps mitigate header abuse. Default: 4194304 (4 MB).

###

`host = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.host)

Host name.

###

`middleware = field(default_factory=(lambda: []))`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.middleware)

Additional ASGI middleware to apply to the app. We accept multiple --middleware arguments. The value should be an import path. If a function is provided, vLLM will add it to the server using `@app.middleware('http')`

. If a class is provided, vLLM will add it to the server using `app.add_middleware()`

.

###

`port = 8000`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.port)

Port number.

###

`root_path = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.root_path)

FastAPI root_path when app is behind a path based routing proxy.

###

`ssl_ca_certs = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.ssl_ca_certs)

The CA certificates file.

###

`ssl_cert_reqs = int(ssl.CERT_NONE)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.ssl_cert_reqs)

Whether client certificate is required (see stdlib ssl module's).

###

`ssl_certfile = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.ssl_certfile)

The file path to the SSL cert file.

###

`ssl_ciphers = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.ssl_ciphers)

SSL cipher suites for HTTPS (TLS 1.2 and below only). Example: 'ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-CHACHA20-POLY1305'

###

`ssl_keyfile = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.ssl_keyfile)

The file path to the SSL key file.

###

`uds = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.uds)

Unix domain socket path. If set, host and port arguments are ignored.

###

`uvicorn_log_level = 'info'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.FrontendArgs.uvicorn_log_level)

Log level for uvicorn.

##

`make_arg_parser(parser)`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.make_arg_parser)

Create the CLI argument parser used by the OpenAI API server.

We rely on the helper methods of `FrontendArgs`

and `AsyncEngineArgs`

to register all arguments instead of manually enumerating them here. This avoids code duplication and keeps the argument definitions in one place.

## Source code in `vllm/entrypoints/launchers/cli_args.py`


##

`resolve_default_chat_template_kwargs(args)`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.resolve_default_chat_template_kwargs)

Resolve renderer defaults, including the dedicated Cohere format flag.

## Source code in `vllm/entrypoints/launchers/cli_args.py`


##

`validate_parsed_serve_args(args)`

[¶](https://docs.vllm.ai#vllm.entrypoints.launchers.cli_args.validate_parsed_serve_args)

Quick checks for model serve args that raise prior to loading.