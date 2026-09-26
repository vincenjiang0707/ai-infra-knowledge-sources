source: https://docs.nvidia.com/dynamo/reference/components/frontend-configuration
lastmod: 2026-09-24T19:58:16.636Z

# Frontend Configuration Reference

This page documents the configuration options for the Dynamo Frontend (`python -m dynamo.frontend`

).

Every CLI argument has a corresponding environment variable. The CLI argument takes precedence; the environment variable is the fallback.

These are the frontend-specific flags. The frontend also parses the shared Dynamo runtime flags (namespace, discovery, planes, parsing) — see [Runtime Configuration](https://docs.nvidia.com/dynamo/reference/components/runtime-configuration). For the router cost model and tuning guidance behind the router flags below, see [Configuration and Tuning](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/configuration-and-tuning).

## HTTP and networking

HTTP listen address.

Environment variable: `DYN_HTTP_HOST`


HTTP listen port.

Environment variable: `DYN_HTTP_PORT`


TLS certificate path (PEM). Must be paired with `--tls-key-path`

.

Environment variable: `DYN_TLS_CERT_PATH`


TLS private key path (PEM). Must be paired with `--tls-cert-path`

.

Environment variable: `DYN_TLS_KEY_PATH`


The Rust HTTP server also reads these environment variables, which are not exposed as CLI arguments:

Maximum request body size in MB.

Maximum time the Frontend waits for admitted HTTP response bodies and `/v1/realtime`

WebSocket
tasks to finish after shutdown begins. New inference requests are rejected while draining.

HTTP status returned for overload and admission-control rejection. Use `503`

only for clients that
cannot handle 529. Values from 200 through 999 are accepted. Informational values from 100 through
199, invalid values, and out-of-range values fall back to 529. The value is read and cached on
first use.

## Router

This section is the canonical CLI and environment-variable reference for the frontend’s embedded
router. See [Router Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-guide) for deployment modes and
[Configuration and Tuning](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/configuration-and-tuning) for behavior and tuning guidance.

### Routing and readiness

Routing strategy. `power-of-two`

samples two workers and selects the worker with fewer in-flight
requests. In disaggregated prefill mode, `power-of-two`

and `least-loaded`

use the synchronous
prefill fallback path.

Environment variable: `DYN_ROUTER_MODE`


Minimum number of workers required before router startup continues. `0`

disables the startup wait.

Environment variable: `DYN_ROUTER_MIN_INITIAL_WORKERS`


Enable session affinity with this router-local idle TTL in seconds. Bindings synchronize across
router replicas on a best-effort basis. Valid values are `1`

through `31536000`

; omit the option
to disable session affinity. See [Session affinity](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/configuration-and-tuning#session-affinity).

Environment variable: `DYN_ROUTER_SESSION_AFFINITY_TTL_SECS`


Fall back to aggregated mode when prefill workers are unavailable.

Environment variable: `DYN_DECODE_FALLBACK`


### KV scoring and cache locality

Preset for KV load-aware routing without cache-reuse signals; implies `--router-mode kv`

.

Environment variable: `DYN_ROUTER_LOAD_AWARE`


Credit multiplier for device-local prefix overlap. The value must be finite and nonnegative.
Values greater than `1.0`

give device overlap extra credit, but adjusted prefill cost is
clamped at zero. See [Configuration and Tuning](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/configuration-and-tuning#tuning-guidelines).

Environment variable: `DYN_ROUTER_KV_OVERLAP_SCORE_CREDIT`


Decay rate for device-local overlap credit as active prefill load rises above the least-loaded
eligible worker. `0`

disables decay; `1`

halves the credit at one request-equivalent of excess
active prefill load.

Environment variable: `DYN_ROUTER_KV_OVERLAP_SCORE_CREDIT_DECAY`


Scale applied to adjusted prompt-side prefill load after overlap and lower-tier cache-hit credits
are subtracted. The minimum is `0.0`

; there is no hard maximum.

Environment variable: `DYN_ROUTER_PREFILL_LOAD_SCALE`


Credit multiplier from `0.0`

through `1.0`

for host-pinned, CPU-tier prefix-cache hits.

Environment variable: `DYN_ROUTER_HOST_CACHE_HIT_WEIGHT`


Credit multiplier from `0.0`

through `1.0`

for disk or other lower-tier prefix-cache hits.

Environment variable: `DYN_ROUTER_DISK_CACHE_HIT_WEIGHT`


**Experimental.** Credit multiplier from `0.0`

through `1.0`

for external shared-cache hits.

Environment variable: `DYN_SHARED_CACHE_MULTIPLIER`


**Experimental.** External shared KV-cache implementation.

Environment variable: `DYN_SHARED_CACHE_TYPE`


Softmax temperature for normalized worker sampling. `0`

selects the lowest-cost worker
deterministically; higher values add randomness.

Environment variable: `DYN_ROUTER_TEMPERATURE`


### KV state and indexers

Consume KV cache state events from workers. Disable this option to predict cache state from routing decisions instead.

Environment variable: `DYN_ROUTER_USE_KV_EVENTS`


Block TTL in seconds for prediction-based routing. Used only with `--no-router-kv-events`

.

Environment variable: `DYN_ROUTER_TTL_SECS`


Enable a local predict-on-route side indexer with this TTL in seconds. This option requires KV
events and is independent of `--router-ttl-secs`

, which configures pure approximate mode.

Environment variable: `DYN_ROUTER_PREDICTED_TTL_SECS`


KV indexer worker threads. Values greater than `1`

use the concurrent radix tree, including with
`--no-router-kv-events`

.

Environment variable: `DYN_ROUTER_EVENT_THREADS`


**Experimental.** Query a remote KV indexer served by a worker component instead of maintaining a
local primary indexer.

Environment variable: `DYN_USE_REMOTE_INDEXER`


Serve this frontend’s local KV indexers over the request plane. Requires `--router-mode kv`

and is
mutually exclusive with `--use-remote-indexer`

.

Environment variable: `DYN_SERVE_INDEXER`


Enable best-effort active-sequence synchronization through the Runtime event plane.

Environment variable: `DYN_ROUTER_REPLICA_SYNC`


Hash function for router-derived active-sequence identities. `keyed-xxh3-v1`

is experimental and
requires both a tracking key file and key ID.

Environment variable: `DYN_ROUTER_TRACKING_HASH`


File containing the provider tracking key. Keyed tracking requires exactly 32 raw bytes.

Environment variable: `DYN_ROUTER_TRACKING_KEY_FILE`


Nonempty provider-managed key epoch identifier required for keyed tracking.

Environment variable: `DYN_ROUTER_TRACKING_KEY_ID`


### Active load and queueing

Track blocks used by in-progress requests for load balancing.

Environment variable: `DYN_ROUTER_TRACK_ACTIVE_BLOCKS`


Assume KV cache reuse when tracking active blocks.

Environment variable: `DYN_ROUTER_ASSUME_KV_REUSE`


Track output blocks during generation. With `nvext.agent_hints.osl`

, fractional decay applies
to output blocks and the structurally exclusive prompt suffix; shared prompt blocks retain full weight.

Environment variable: `DYN_ROUTER_TRACK_OUTPUT_BLOCKS`


**Experimental.** Finite, nonnegative block-equivalent decode cost added for each active request on
a candidate worker. Tune this value only when decode step latency depends materially on active batch
size.

Environment variable: `DYN_ROUTER_DECODE_ACTIVE_REQUEST_WEIGHT`


Track prompt-side prefill tokens in worker load accounting.

Environment variable: `DYN_ROUTER_TRACK_PREFILL_TOKENS`


Prompt-side load model. `none`

keeps static prompt load; `aic`

decays the oldest active prefill
request using an AIC prediction. See [AIC prefill load model](https://docs.nvidia.com/dynamo/reference/components/frontend-configuration#aic-prefill-load-model).

Environment variable: `DYN_ROUTER_PREFILL_LOAD_MODEL`


Queue threshold fraction of prefill capacity. Setting a nonnegative numeric value enables queueing; priority hints affect only requests waiting in this queue.

Environment variable: `DYN_ROUTER_QUEUE_THRESHOLD`


Queue scheduling policy. `fcfs`

optimizes tail Time To First Token (TTFT); `wspt`

optimizes average
TTFT.

Environment variable: `DYN_ROUTER_QUEUE_POLICY`


Startup-only YAML for policy-class queues. When omitted,
`--router-queue-threshold`

and `--router-queue-policy`

define one synthetic policy class.
Queueing remains disabled until a threshold is configured. See [Policy-class queues](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/configuration-and-tuning#policy-class-queues).

Environment variable: `DYN_ROUTER_POLICY_CONFIG`


## AIC prefill load model

These options apply only when `--router-mode kv`

is combined with `--router-prefill-load-model aic`

.

When enabled, the frontend’s embedded KV router predicts one expected prefill duration per admitted request, using the selected worker’s overlap-derived cached prefix, then decays only the oldest active prefill request on each worker for prompt-side load accounting.

Backend family to model in AIC, for example `vllm`

or `sglang`

.

Environment variable: `DYN_AIC_BACKEND`


AIC hardware/system identifier, for example `h200_sxm`

.

Environment variable: `DYN_AIC_SYSTEM`


Model path or model identifier used for AIC perf lookup.

Environment variable: `DYN_AIC_MODEL_PATH`


Pinned AIC database version. If omitted, Dynamo uses the backend default.

Environment variable: `DYN_AIC_BACKEND_VERSION`


Tensor-parallel size to model in AIC.

Environment variable: `DYN_AIC_TP_SIZE`


MoE tensor-parallel size for models that require AIC MoE parallelism.

Environment variable: `DYN_AIC_MOE_TP_SIZE`


MoE expert-parallel size for models that require AIC MoE parallelism.

Environment variable: `DYN_AIC_MOE_EP_SIZE`


Attention data-parallel size for models that require AIC MoE parallelism.

Environment variable: `DYN_AIC_ATTENTION_DP_SIZE`


For MoE models, AIC requires `aic_tp_size * aic_attention_dp_size == aic_moe_tp_size * aic_moe_ep_size`

. For Kimi-style TP-only MoE runs, set `--aic-moe-tp-size`

to the same value as `--aic-tp-size`

, with `--aic-moe-ep-size 1`

and `--aic-attention-dp-size 1`

.

## Fault tolerance

Maximum request migrations per worker disconnect. `0`

disables migration.

Environment variable: `DYN_MIGRATION_LIMIT`


Maximum prompt-plus-output sequence length that remains eligible for migration. When a request
strictly exceeds the limit, migration and token tracking stop for that request. Must be from `1`

through `4294967295`

. Unset means no sequence-length limit.

Environment variable: `DYN_MIGRATION_MAX_SEQ_LEN`


KV cache utilization fraction from `0.0`

through `1.0`

. A numeric value independently enables
decode-block busy rejection. Decode-block telemetry requires `--router-mode kv`

; use
`--router-track-output-blocks`

when generated tokens should contribute to the observed load.

Environment variable: `DYN_ACTIVE_DECODE_BLOCKS_THRESHOLD`


Absolute active-prefill-token threshold. A numeric value greater than or equal to `0`

independently
enables this check. Uses OR logic with the fractional prefill threshold.

Environment variable: `DYN_ACTIVE_PREFILL_TOKENS_THRESHOLD`


Non-negative fraction of `max_num_batched_tokens`

used as the active-prefill-token threshold. A
numeric value independently enables this check. Uses OR logic with the absolute prefill threshold.

Environment variable: `DYN_ACTIVE_PREFILL_TOKENS_THRESHOLD_FRAC`


For guidance on choosing thresholds, see [Request Rejection](https://docs.nvidia.com/dynamo/kubernetes/fault-tolerance/request-rejection) and [Request Migration](https://docs.nvidia.com/dynamo/kubernetes/fault-tolerance/request-migration).

## Model discovery

Exact namespace for model discovery scoping.

Environment variable: `DYN_NAMESPACE`


Namespace prefix for discovery (for example, `ns`

matches `ns`

, `ns-abc123`

). Takes precedence over `--namespace`

.

Environment variable: `DYN_NAMESPACE_PREFIX`


Override model name string.

Environment variable: `DYN_MODEL_NAME`


Path to a local model directory (for private/custom models).

Environment variable: `DYN_MODEL_PATH`


KV cache block size override.

Environment variable: `DYN_KV_CACHE_BLOCK_SIZE`


## Infrastructure

Service discovery backend.

Allowed values: kubernetes etcd file memEnvironment variable: `DYN_DISCOVERY_BACKEND`


Request distribution transport. `tcp`

is the fastest.

Environment variable: `DYN_REQUEST_PLANE`


Event publishing transport. Defaults to `zmq`

for `file`

/`mem`

discovery and `nats`

for `etcd`

/`kubernetes`

.

Environment variable: `DYN_EVENT_PLANE`


## KServe gRPC

Start the KServe gRPC v2 server.

Environment variable: `DYN_KSERVE_GRPC_SERVER`


HTTP metrics port for the gRPC service.

Environment variable: `DYN_GRPC_METRICS_PORT`


The gRPC server also supports optional HTTP/2 flow-control tuning via environment variables:

HTTP/2 connection-level flow control window size in bytes. Default is the tonic default (64 KB).

HTTP/2 per-stream flow control window size in bytes. Default is the tonic default (64 KB).

See the [Frontend Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/frontend/frontend-guide) for KServe message formats, gRPC tuning examples, and integration details.

## Monitoring

Prefix for frontend Prometheus metrics.

Environment variable: `DYN_METRICS_PREFIX`


Dump the resolved config to a file path.

Environment variable: `DYN_DUMP_CONFIG_TO`


## Tokenizer

Tokenizer implementation. `default`

uses HuggingFace; `fastokens`

uses the high-performance Rust tokenizer. See [Tokenizer](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/frontend/tokenizer).

Environment variable: `DYN_TOKENIZER`


## Experimental

### Python route extensions

Load a trusted HTTP route provider by a name registered in the `dynamo.frontend.routes`

entry-point
group or by an importable `module:function`

path. Repeat the option to load multiple providers.
Providers can add static `GET`

routes but cannot override built-in routes; invalid or duplicate
routes fail startup. Extensions apply only to the HTTP frontend. See
[Python Route Extensions](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/frontend/python-route-extensions) for a packaged and direct-load example.

Environment variable: `DYN_FRONTEND_ROUTE_EXTENSIONS`

accepts whitespace-separated values.

#### Handler contract

**Provider resolution:**A registered`dynamo.frontend.routes`

entry-point name takes precedence. If no registered name matches, a value containing`:`

is resolved as`module:function`

. Unknown names fail startup and report the available registered extensions.**Provider return:**The provider callable returns one`FrontendRoute`

or an iterable of routes.**Route shape:**Extensions support static-path`GET`

routes only. Path parameters, wildcards, other HTTP methods, asynchronous handlers, and duplicates of built-in routes are rejected.**Handler signature:**A synchronous`handler(ctx: FrontendExtensionContext)`

returns a JSON-serializable body for HTTP 200, or`FrontendResponse(status_code, body)`

to override the status code.**Live state:**`FrontendExtensionContext`

exposes`is_ready()`

,`is_cancelled()`

,`has_any_ready_model()`

,`is_model_ready_to_serve(name)`

,`model_display_names()`

, and`serving_ready_display_names()`

.**Execution limits:**Handlers run in a small dedicated thread pool. A handler that exceeds 30 seconds returns 503. A saturated pool rejects new extension requests with the configured overload status code, 529 by default.**Multiple providers:**Repeating the CLI option or listing whitespace-separated environment values loads multiple providers. Duplicate provider names are de-duplicated.

### Other experimental options

Enable `/v1/messages`

(the Anthropic Messages API).

Environment variable: `DYN_ENABLE_ANTHROPIC_API`


Chat processor. See [Chat Processors](https://docs.nvidia.com/dynamo/parsing/chat-processors) for how this combines with the parser flags.

Environment variable: `DYN_CHAT_PROCESSOR`


Log per-function timing for preprocessing (vllm processor only).

Environment variable: `DYN_DEBUG_PERF`


Worker processes for CPU-bound preprocessing. `0`

uses the main event loop (vllm processor only).

Environment variable: `DYN_PREPROCESS_WORKERS`


Interactive text chat mode.

Environment variable: `DYN_INTERACTIVE`


## Host memory allocator

The frontend performs per-request host-memory allocations. Under high CPU load, allocator contention can cap frontend throughput before the GPU workers saturate. Dynamo runtime containers include jemalloc, but the frontend does not preload it by default.

Preload jemalloc for the frontend process. The library path depends on the container architecture:

In Kubernetes, set this variable on the frontend container rather than modifying the image. Locate
the installed path with `dpkg -L libjemalloc2 | grep 'libjemalloc.so'`

if the image uses a different
layout.

Configure jemalloc when it is preloaded. The best values depend on the request workload and CPU allocation. This is an empirical starting point, not a production default:

Validate allocator changes with the same AIPerf workload before and after enabling them. See
[Advanced Performance Tuning](https://docs.nvidia.com/dynamo/kubernetes/operations/performance-tuning).

## HTTP endpoints

The frontend exposes the following HTTP endpoints.

### OpenAI-compatible

### Anthropic (Experimental)

### Infrastructure

`POST /busy_threshold`

accepts `model`

plus any of `active_decode_blocks_threshold`

,
`active_prefill_tokens_threshold`

, and `active_prefill_tokens_threshold_frac`

. A numeric field enables
only that check. The router reevaluates workers on the next worker-load or runtime-configuration
update; the call does not synchronously recompute the busy set and does not change startup-only router
options such as `--router-mode kv`

or `--router-track-output-blocks`

.

### Frontend feature switches

Environment variables controlling frontend extensions. Extensions are enabled by default. Set a
truthy value (`1`

, `true`

, `yes`

, or `on`

, case-insensitive) to disable the corresponding surface.

When truthy, the frontend drops `request.nvext`

on `/v1/chat/completions`

, `/v1/completions`

,
`/v1/responses`

, `/v1/embeddings`

, and `/v1/messages`

; ignores the
`x-dynamo-worker-instance-id`

, `x-dynamo-prefill-instance-id`

, `x-dynamo-dp-rank`

,
`x-dynamo-prefill-dp-rank`

, `x-dynamo-request-priority`

, and
`x-dynamo-request-strict-priority`

routing headers and their compatibility aliases; and ignores
the response-side `nvext.extra_fields`

opt-in.

When truthy, `GET /busy_threshold`

and `POST /busy_threshold`

are not registered and return 404.
Inference, metrics, models, health, and liveness routes are unaffected.

### Endpoint path customization

All endpoint paths can be overridden via environment variables:

## Deprecated

**Deprecated and ignored.** Configure the three busy thresholds directly. The compatibility flag
and `DYN_ADMISSION_CONTROL`

are accepted only so older launch commands continue to start.

Environment variable: `DYN_ADMISSION_CONTROL`