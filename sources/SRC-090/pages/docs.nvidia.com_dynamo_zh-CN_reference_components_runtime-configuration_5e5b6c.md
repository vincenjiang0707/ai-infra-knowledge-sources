source: https://docs.nvidia.com/dynamo/zh-CN/reference/components/runtime-configuration
lastmod: 2026-09-23T23:30:39.914Z

Runtime Configuration (DynamoRuntimeConfig)


Runtime Configuration (DynamoRuntimeConfig)

Field reference for the cross-cutting Dynamo runtime CLI flags and environment variables shared by every backend and the frontend.

`DynamoRuntimeConfig`

holds the configuration that is **common to every Dynamo process** — the frontend, the standalone router, and all three backend workers (vLLM, SGLang, TRT-LLM) parse this same argument group. Most fields, types, defaults, and choices on this page come from the [ DynamoRuntimeArgGroup and DynamoRuntimeConfig](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/components/src/dynamo/common/configuration/groups/runtime_args.py) definitions. The page also catalogs runtime environment-only controls implemented below the Python argument layer.


These are the **shared** Dynamo runtime flags. Each backend also has its own backend-specific flags: [vLLM Configuration](https://docs.nvidia.com/dynamo/reference/backends/v-llm-configuration), [SGLang Configuration](https://docs.nvidia.com/dynamo/reference/backends/sg-lang-configuration), and [TensorRT-LLM Configuration](https://docs.nvidia.com/dynamo/reference/backends/tensor-rt-llm-configuration). This page covers neither native engine arguments nor backend-specific `DYN_*`

prefixed flags — only the flags from `DynamoRuntimeArgGroup`

.

## How the config is loaded

Unless a field is marked environment-only, it has both a CLI flag and an environment variable. The CLI flag takes precedence; the environment variable is the fallback. Boolean fields are negatable — `--dyn-enable-structural-tag`

sets it on, `--no-dyn-enable-structural-tag`

sets it off.

## Model discovery and namespace

Dynamo namespace that scopes service discovery. All components in a deployment must share the same namespace to find each other. If `DYN_NAMESPACE_WORKER_SUFFIX`

is also set, `-{suffix}`

is automatically appended to the resolved value to support multiple worker pools serving the same model.

On Kubernetes the operator sets this automatically to `{k8s_namespace}-{dgd_name}`

; override only deliberately.

Environment variable: `DYN_NAMESPACE`


Dynamo endpoint string in `dyn://namespace.component.endpoint`

format, for example `dyn://dynamo.backend.generate`

. When unset, the endpoint address is inferred from the component’s registration in the discovery backend.

Environment variable: `DYN_ENDPOINT`


Comma-separated list of OpenAI-compatible endpoint types to enable. Use `completions`

alone for models that do not have a chat template. The obsolete alias `--dyn-endpoint-types`

is accepted for backward compatibility.

Environment variable: `DYN_ENDPOINT_TYPES`


## Communication planes

Service discovery backend. `kubernetes`

uses the K8s API; `etcd`

uses a distributed key-value store (configured via `ETCD_*`

env vars such as `ETCD_ENDPOINTS`

); `file`

uses the local filesystem (path from `DYN_FILE_KV`

, defaulting to `$TMPDIR/dynamo_store_kv`

); `mem`

uses an in-memory store suitable for single-process development. See [Discovery Plane](https://docs.nvidia.com/dynamo/knowledge-base/concepts/communication-planes/discovery-plane) for design details.

On Kubernetes the operator sets this automatically to `kubernetes`

; override only deliberately.

Environment variable: `DYN_DISCOVERY_BACKEND`


Transport used to distribute requests from routers to workers. `tcp`

provides the lowest latency and is recommended for production. `nats`

uses NATS messaging. See [Request Plane](https://docs.nvidia.com/dynamo/knowledge-base/concepts/communication-planes/request-plane) for design details.

Environment variable: `DYN_REQUEST_PLANE`


Preferred payload codec advertised by every request-plane endpoint served by this process. Clients
select the codec independently for each destination endpoint. They use the destination’s advertised
codec, or `json`

when a legacy destination does not advertise one. Setting this variable does not
force the codec for outbound requests from the process.

Dynamo caches this process-wide value on its first codec lookup. Restart the process after changing it.

Allowed values: json msgpackEvent publishing transport. ZMQ is the default for every discovery backend; select `nats`

explicitly to use NATS Core. See [Event Plane](https://docs.nvidia.com/dynamo/knowledge-base/concepts/communication-planes/event-plane) for design details.

Environment variable: `DYN_EVENT_PLANE`


KV-cache transfer connector. Accepts zero or more values. Deprecated for vLLM — use `--kv-transfer-config`

instead. For TRT-LLM, valid options are `nixl`

, `lmcache`

, `kvbm`

, `null`

, and `none`

.

Environment variable: `DYN_CONNECTOR`


## Parsing

Tool call parser name for the model. When unset, the backend’s default tool call parsing is used. Valid parser names are determined at runtime by the installed `dynamo._core`

extension — run `python -m dynamo.vllm --help`

to see the available choices on your installation.

Environment variable: `DYN_TOOL_CALL_PARSER`


Reasoning/chain-of-thought parser name for the model. When unset, no reasoning parsing is performed. Valid parser names are determined at runtime by the installed `dynamo._core`

extension — run `python -m dynamo.vllm --help`

to see the available choices on your installation.

Environment variable: `DYN_REASONING_PARSER`


Thinking mode to apply when a request omits an explicit thinking control. Request-level `thinking`

, `reasoning_effort`

, and controls in `chat_template_args`

or `chat_template_kwargs`

take precedence. When unset, Dynamo preserves the model or chat template’s native default. See [Deployment-Level Thinking Default](https://docs.nvidia.com/dynamo/parsing/reasoning-parsing#deployment-level-thinking-default) for examples and precedence details.

Environment variable: `DYN_DEFAULT_THINKING_MODE`


Exclude tool definitions from the chat template when `tool_choice='none'`

. Prevents models from generating unsolicited raw XML tool calls in the content field. This flag controls the Rust-native chat template path; a matching flag in `FrontendArgGroup`

controls the Python processor side independently.

Environment variable: `DYN_EXCLUDE_TOOLS_WHEN_TOOL_CHOICE_NONE`


Enable structural tag guided decoding for tool calls. When enabled, configure activation scope and parameter schema strictness with `--dyn-structural-tag-scope`

and `--dyn-structural-tag-schema`

.

Environment variable: `DYN_ENABLE_STRUCTURAL_TAG`


Controls when structural tags are activated. `auto`

activates them for required or named `tool_choice`

, or when any tool has `strict=true`

or `parallel_tool_calls`

is false. `always`

additionally activates them for `tool_choice=auto`

without those conditions. `tool_choice=none`

is unaffected by either setting. Only meaningful when `--dyn-enable-structural-tag`

is set.

Environment variable: `DYN_STRUCTURAL_TAG_SCOPE`


Controls parameter schema strictness inside structural tags. `auto`

applies the real parameter schema only to tools with `strict=true`

, leaving all other tools syntactically constrained but schema-unconstrained. `strict`

applies the real parameter schema to every tool. Only meaningful when `--dyn-enable-structural-tag`

is set.

Environment variable: `DYN_STRUCTURAL_TAG_SCHEMA`


Path to a custom Jinja template file to override the model’s default chat template. This template takes precedence over any template found in the model repository.

Environment variable: `DYN_CUSTOM_JINJA_TEMPLATE`


## Multimodal and media output

Capacity of the multimodal embedding cache in GB. Set to `0`

to disable the cache entirely. Increase this for workloads with repeated image or audio inputs to avoid redundant re-encoding.

Environment variable: `DYN_MULTIMODAL_EMBEDDING_CACHE_CAPACITY_GB`


Space-separated list of output modalities for omni or diffusion mode, for example `--output-modalities text image`

. Defaults to `text`

only. Use `image`

, `video`

, or `audio`

when deploying image/video/audio generation models.

Environment variable: `DYN_OUTPUT_MODALITIES`


Filesystem URL for storing generated images and videos. Accepts a local `file://`

path or a remote object-storage URL such as `s3://bucket/path`

.

Environment variable: `DYN_MEDIA_OUTPUT_FS_URL`


Base HTTP URL for rewriting media file paths in API responses, for example `http://localhost:8000/media`

. When unset, raw filesystem paths are returned in the response body.

Environment variable: `DYN_MEDIA_OUTPUT_HTTP_URL`


## Fault tolerance

Maximum number of seconds that a runtime client locally removes a worker from normal routing after
a request-path failure while service discovery propagates the worker state. Set to `0`

to disable
local inhibition. The process reads this value once when the first client initializes; restart the
process after changing it. Discovery updates remain authoritative, and direct dispatch bypasses the
local inhibited set while the selected worker remains in discovery.

## Operations

Dump the fully resolved configuration to the specified file path at startup. Useful for auditing the effective values after all env-var and CLI overrides have been applied.

Environment variable: `DYN_DUMP_CONFIG_TO`


Override the runtime health-check canary payload used by the unified backend’s `Worker`

. Accepts a JSON object string, for example `'{"token_ids": [1], "stop_conditions": {"max_tokens": 1}}'`

, or a file reference prefixed with `@`

, for example `@/path/to/payload.json`

. Takes precedence over the engine’s default `health_check_payload()`

. Applies to the unified backend only.

Environment variable: `DYN_HEALTH_CHECK_PAYLOAD`


Maximum requests handled concurrently by the engine. Setting a positive integer enables worker-side admission control. When the engine slots and the Dynamo overflow queue are full, the worker rejects the request and the Frontend returns the configured overload status, 529 by default.

Environment variable: `DYN_ENGINE_REQUEST_LIMIT`


Advanced overflow-queue size for requests waiting in Dynamo before entering the engine. Applies only
when `--engine-request-limit`

or `DYN_ENGINE_REQUEST_LIMIT`

is set. Must be at least `2`

; the
effective per-worker cap is the engine limit plus this queue limit.