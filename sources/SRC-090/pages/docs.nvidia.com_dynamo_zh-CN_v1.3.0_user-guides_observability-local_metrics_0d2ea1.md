source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/user-guides/observability-local/metrics
lastmod: 2026-09-23T23:30:39.914Z

# Metrics

## Overview

Dynamo provides built-in metrics capabilities through the Dynamo metrics API, which is automatically available whenever you use the `DistributedRuntime`

framework. This document serves as a reference for all available metrics in Dynamo.

**For visualization setup instructions**, see the [Prometheus and Grafana Setup Guide](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/observability-local/prometheus-grafana-setup).

**For creating custom metrics**, see the [Metrics Developer Guide](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/observability-local/metrics-developer-guide).

## Environment Variables

## Getting Started Quickly

This is a single machine example.

### Start Observability Stack

For visualizing metrics with Prometheus and Grafana, start the observability stack. See [Observability Getting Started](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/observability-local#getting-started-quickly) for instructions.

### Launch Dynamo Components

Launch a frontend and vLLM backend to test metrics:

Wait for the vLLM worker to start, then send requests and check metrics:

## Exposed Metrics

Dynamo exposes metrics in Prometheus Exposition Format text at the `/metrics`

HTTP endpoint. All Dynamo-generated metrics use the `dynamo_*`

prefix and include labels (`dynamo_namespace`

, `dynamo_component`

, `dynamo_endpoint`

) to identify the source component.

**Example Prometheus Exposition Format text:**

### Metric Categories

Dynamo exposes several categories of metrics:

**Frontend Metrics**(`dynamo_frontend_*`

) - Request handling, token processing, and latency measurements**Component Metrics**(`dynamo_component_*`

) - Request counts, processing times, byte transfers, and system uptime**Specialized Component Metrics**(e.g.,`dynamo_preprocessor_*`

) - Component-specific metrics**Engine Metrics**(Pass-through) - Backend engines expose their own metrics:[vLLM](https://docs.nvidia.com/dynamo/v1.3.0/backends/v-llm/observability)(`vllm:*`

),[SGLang](https://docs.nvidia.com/dynamo/v1.3.0/backends/sg-lang/observability)(`sglang:*`

),[TensorRT-LLM](https://docs.nvidia.com/dynamo/v1.3.0/backends/tensor-rt-llm/observability)(`trtllm_*`

)

## Runtime Hierarchy

The Dynamo metrics API is available on `DistributedRuntime`

, `Namespace`

, `Component`

, and `Endpoint`

, providing a hierarchical approach to metric collection that matches Dynamo’s distributed architecture:

`DistributedRuntime`

: Global metrics across the entire runtime`Namespace`

: Metrics scoped to a specific dynamo_namespace`Component`

: Metrics for a specific dynamo_component within a namespace`Endpoint`

: Metrics for individual dynamo_endpoint within a component

This hierarchical structure allows you to create metrics at the appropriate level of granularity for your monitoring needs.

## Available Metrics

**Note:** Labeled metrics (`HistogramVec`

, `CounterVec`

, `GaugeVec`

) register a metric *family*, not individual time series. A series for a given label combination only appears at `/metrics`

after the first `with_label_values(...)`

call for that combination — i.e., after the first matching request is served. For example, `dynamo_frontend_request_duration_seconds{model="Qwen/Qwen3-0.6B"}`

will not appear on a freshly-started frontend until a request for that model is handled. This is expected Prometheus client behavior, not a missing metric.

### Backend Component Metrics

**Backend workers** (`python -m dynamo.vllm`

, `python -m dynamo.sglang`

, etc.) expose `dynamo_component_*`

metrics on the system status port (configurable via `DYN_SYSTEM_PORT`

, disabled by default). In Kubernetes the operator typically sets `DYN_SYSTEM_PORT=9090`

; for local development you must set it explicitly (e.g. `DYN_SYSTEM_PORT=8081`

).

The core Dynamo backend system exposes metrics at the `/metrics`

endpoint with the `dynamo_component_*`

prefix for all components that use the `DistributedRuntime`

framework:

`dynamo_component_inflight_requests`

: Requests currently being processed (gauge)`dynamo_component_request_bytes_total`

: Total bytes received in requests (counter)`dynamo_component_request_duration_seconds`

: Request processing time (histogram)`dynamo_component_requests_total`

: Total requests processed (counter)`dynamo_component_errors_total`

: Total errors encountered while handling a request (counter, labeled with`error_type`

). See[Component Error Types](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/observability-local/metrics#component-error-types).`dynamo_component_response_bytes_total`

: Total bytes sent in responses (counter)`dynamo_component_uptime_seconds`

: DistributedRuntime uptime (gauge). Automatically updated before each Prometheus scrape on both the frontend (`/metrics`

on port 8000) and the system status server (`/metrics`

on`DYN_SYSTEM_PORT`

when set).

**Access backend component metrics:**

#### Component Labels

Backend `dynamo_component_*`

series carry two groups of labels: the ones the Dynamo runtime emits, and the ones Prometheus/Kubernetes attach during scraping.

**Auto-injected by the Dynamo runtime** (added by `create_metric()`

in `lib/runtime/src/metrics.rs`

for every metric registered through the namespace/component/endpoint hierarchy):

**Added at registration time by backend code** (passed via `metrics_labels=`

when the worker calls `serve_endpoint()`

— not auto-injected, so presence depends on the backend):

**Added by the metric itself**:

**Injected by Prometheus / Kubernetes (added by the scraper, not in the metric itself):**


Watch out for these collisions:

`dynamo_namespace`

(Dynamo deployment scope) vs.`namespace`

(K8s namespace).`dynamo_endpoint`

(Dynamo RPC) vs.`endpoint`

(K8s Service port name).

#### Component Names

Values you will see in the `dynamo_component`

label on `dynamo_component_*`

series. The HTTP frontend (`python -m dynamo.frontend`

) is **not** in this list — it exposes its own `dynamo_frontend_*`

metric family, not `dynamo_component_*`

.

Internal subsystems (e.g. `kvbm`

from the block manager, `sequences`

from the KV router) also create components and may appear in `dynamo_component_*`

series. The default for vLLM/SGLang can be overridden by passing `--endpoint dyn://<ns>.<component>.<endpoint>`

on the worker command line.

The name

`backend`

for the decode worker is historical. The runtime has a TODO to introduce a`decode`

constant and migrate to it (see`lib/runtime/src/metrics/prometheus_names.rs::component_names`

).

#### Endpoint Names

Values you will see in the `dynamo_endpoint`

label on backend workers:

#### Component Error Types

The `dynamo_component_errors_total`

counter is labeled with `error_type`

, identifying which stage of request handling failed:

### Specialized Component Metrics

Some components expose additional metrics specific to their functionality:

`dynamo_preprocessor_*`

: Metrics specific to preprocessor components

### Frontend Metrics

**Important:** The frontend and backend workers are separate components that expose metrics on different ports. See [Backend Component Metrics](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/observability-local/metrics#backend-component-metrics) for backend metrics.

The Dynamo HTTP Frontend (`python -m dynamo.frontend`

) exposes `dynamo_frontend_*`

metrics on port 8000 by default (configurable via `--http-port`

or `DYN_HTTP_PORT`

) at the `/metrics`

endpoint. Most metrics include `model`

labels containing the model name:

`dynamo_frontend_active_requests`

: Number of requests currently being handled by the frontend, from HTTP handler entry until the response stream completes (gauge). This is the top-level in-flight count with no stage breakdown.`dynamo_frontend_stage_requests`

: Number of requests currently in a given frontend pipeline stage (gauge, labels:`stage`

,`phase`

). See[Stage and phase labels](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/observability-local/metrics#stage-and-phase-labels)below.`dynamo_frontend_inflight_requests`

: Inflight requests (gauge).**Deprecated**— kept for backward compatibility; prefer`dynamo_frontend_active_requests`

, which has identical semantics with a clearer name.`dynamo_frontend_queued_requests`

: Number of requests in HTTP processing queue (gauge).**Deprecated**— kept for backward compatibility; the “waiting for first token” window is now the sum of`dynamo_frontend_stage_requests`

across the`preprocess`

,`route`

, and`dispatch`

stages.`dynamo_frontend_disconnected_clients`

: Number of disconnected clients (gauge)`dynamo_frontend_input_sequence_tokens`

: Input sequence length (histogram)`dynamo_frontend_cached_tokens`

: Number of cached tokens (prefix cache hits) per request (histogram)`dynamo_frontend_tokenizer_cache_hits_total`

: L1 tokenizer prefix-cache hits across all models (counter)`dynamo_frontend_tokenizer_cache_misses_total`

: L1 tokenizer prefix-cache misses across all models (counter)`dynamo_frontend_tokenizer_cache_cached_tokens_total`

: Tokens returned from the L1 tokenizer prefix cache (counter, label:`model`

)`dynamo_frontend_tokenizer_cache_uncached_tokens_total`

: Tokens freshly encoded after an L1 tokenizer prefix-cache lookup (counter, label:`model`

)`dynamo_frontend_inter_token_latency_seconds`

: Inter-token latency (histogram)`dynamo_frontend_output_sequence_tokens`

: Output sequence length (histogram)`dynamo_frontend_output_tokens_total`

: Total number of output tokens generated (counter)`dynamo_frontend_request_duration_seconds`

: LLM request duration (histogram)`dynamo_frontend_requests_total`

: Total LLM requests (counter)`dynamo_frontend_time_to_first_token_seconds`

: Time to first token (histogram)`dynamo_frontend_model_migration_total`

: Total number of request migrations due to worker unavailability (counter, labels:`model`

,`migration_type`

)

**Access frontend metrics:**

#### Tokenizer Cache Metrics

The hit and miss counters record one cache outcome per encode operation across the frontend process. A batch encode records one outcome per item. The cached and uncached token counters report exact token totals for each served model. When L1 is active, a partial hit increments both token counters because it returns a cached prefix and freshly encodes the remaining suffix. A full hit increments only the cached-token counter, and a full miss increments only the uncached-token counter.

Use the following PromQL expression to calculate the token reuse ratio for each model over five minutes:

The ratio is meaningful only for a model with an active L1 cache and observed tokens. The token
counters do not increment when `DYN_TOKENIZER_CACHE=0`

, when encoding fails, or when the cache has no
registered special-token boundaries. The tiktoken path currently has no registered boundaries, so it
bypasses L1 and exposes zero-valued token counter series; its ratio remains undefined until the cache
observes tokens.

#### Stage and phase labels

`dynamo_frontend_stage_requests`

decomposes the lifetime of an active frontend request into three sequential pipeline stages. A request is counted in exactly one stage at a time (via an RAII guard that increments on stage entry and decrements on stage exit), and is counted in `dynamo_frontend_active_requests`

for its entire lifetime. Between stages — and after `dispatch`

exits while the backend is streaming tokens — the request is still in `active_requests`

but in no `stage_requests`

bucket.

`stage`

label values:

`phase`

label values:

**Derived signals operators commonly want.** These are cluster-wide totals across all frontend pods. `stage_requests`

has no `model`

label, so you cannot split these by model; add `by (pod)`

or `by (instance)`

to any `sum(...)`

below if you need per-pod visibility. The stage filter `stage=~"preprocess|route|dispatch"`

is used explicitly to keep the “pre-first-token” semantic stable if additional stages (e.g. `postprocess`

) are added in the future.

**Requests waiting for a worker to start generating (the old “queued” semantic):**`sum(dynamo_frontend_stage_requests{stage=~"preprocess|route|dispatch"})`

— i.e. still in`preprocess`

,`route`

, or`dispatch`

.**Requests currently being processed by a backend worker:**use the worker-side gauge`sum(dynamo_component_inflight_requests{dynamo_component="backend",dynamo_endpoint="generate"})`

— this is the authoritative count, available whenever`DYN_SYSTEM_PORT`

is set on workers (see[Backend Component Metrics](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/observability-local/metrics#backend-component-metrics)).*Frontend-perspective variant*(useful if worker metrics aren’t being scraped, or when sizing frontend pods rather than workers):`sum(dynamo_frontend_active_requests) - sum(dynamo_frontend_stage_requests{stage=~"preprocess|route|dispatch"})`

. This differs from the worker gauge because its window starts when the first token arrives at the frontend and extends through streaming to the client, so it includes transit and client-buffering time.

**Router saturation:**`sum(dynamo_frontend_stage_requests{stage="route"})`

spiking indicates workers can’t be selected fast enough (e.g. all backends busy, KV-router queue full).**Backend prefill saturation:**`sum(dynamo_frontend_stage_requests{stage="dispatch"})`

spiking indicates the backend is slow to produce first tokens.

#### Deprecated frontend gauges

The following gauges are still emitted but will be removed in a future release. They were superseded by the gauges above as part of the frontend-metrics rework (PR #8162). Dashboards and alerts should migrate off them.

#### Model Configuration Metrics

The frontend also exposes model configuration metrics (on port 8000 `/metrics`

endpoint) with the `dynamo_frontend_model_*`

prefix. These metrics are populated from the worker backend registration service when workers register with the system. All model configuration metrics include a `model`

label.

**Runtime Config Metrics (from ModelRuntimeConfig):**
These metrics come from the runtime configuration provided by worker backends during registration.

`dynamo_frontend_model_total_kv_blocks`

: Total KV blocks available for a worker serving the model (gauge)`dynamo_frontend_model_max_num_seqs`

: Maximum number of sequences for a worker serving the model (gauge)`dynamo_frontend_model_max_num_batched_tokens`

: Maximum number of batched tokens for a worker serving the model (gauge)

**MDC Metrics (from ModelDeploymentCard):**
These metrics come from the Model Deployment Card information provided by worker backends during registration. Note that when multiple worker instances register with the same model name, only the first instance’s configuration metrics (runtime config and MDC metrics) will be populated. Subsequent instances with duplicate model names will be skipped for configuration metric updates.

`dynamo_frontend_model_context_length`

: Maximum context length for a worker serving the model (gauge)`dynamo_frontend_model_kv_cache_block_size`

: KV cache block size for a worker serving the model (gauge)`dynamo_frontend_model_migration_limit`

: Request migration limit for a worker serving the model (gauge)

### Request Processing Flow


Deprecated framing.The two-metric model below (inflight vs. HTTP queue) describes the legacy`dynamo_frontend_inflight_requests`

and`dynamo_frontend_queued_requests`

gauges and is kept only to help operators reading existing dashboards. New work should use`dynamo_frontend_active_requests`

and the per-stage`dynamo_frontend_stage_requests`

gauges described under[Stage and phase labels].

This section explains the distinction between two key metrics used to track request processing:

**Inflight**: Tracks requests from HTTP handler start until the complete response is finished**HTTP Queue**: Tracks requests from HTTP handler start until first token generation begins (including prefill time)

**Example Request Flow:**

**Timeline:**

**Concurrency Example:**
Suppose the backend allows 3 concurrent requests and there are 10 clients continuously hitting the frontend:

- All 10 requests will be counted as inflight (from start until complete response)
- 7 requests will be in HTTP queue most of the time
- 3 requests will be actively processed (between first token and last token)

**Key Differences:**

**Inflight**: Measures total request lifetime including processing time**HTTP Queue**: Measures queuing time before processing begins (including prefill time)**HTTP Queue ≤ Inflight**(HTTP queue is a subset of inflight time)

### Router Metrics

The router exposes metrics for monitoring routing decisions and overhead. Defined in `lib/llm/src/kv_router/metrics.rs`

.

For router deployment modes, see the [Router Guide](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/kv-cache-aware-routing). For router flags and tuning, see [Configuration and Tuning](https://docs.nvidia.com/dynamo/v1.3.0/components/router/configuration-and-tuning).

#### Metrics Availability by Configuration

Not all metrics appear in every deployment. The chart below shows which metric groups are **registered** and **populated** in each configuration:

**Key:**

**Registered and populated**: Metric appears at`/metrics`

with real values**Registered, always zero**: Metric appears at`/metrics`

but the counter/histogram is never incremented (useful for dashboards that expect the metric to exist)**Not registered / Not created**: Metric does not appear at`/metrics`

at all

**Scrape endpoints:**

- Frontend:
`/metrics`

on HTTP port (default 8000, configurable via`--http-port`

or`DYN_HTTP_PORT`

) - Standalone router:
`/metrics`

on`DYN_SYSTEM_PORT`

(must be set explicitly; default is`-1`

/ disabled) - Backend workers:
`/metrics`

on`DYN_SYSTEM_PORT`

(separate from frontend metrics)

#### Router Request Metrics (`dynamo_component_router_*`

)

Histograms and counters for aggregate request-level statistics. Eagerly registered via `from_component()`

with the DRT `MetricsRegistry`

hierarchy. On the frontend, exposed at `/metrics`

on the HTTP port (default 8000) via the `drt_metrics`

bridge. On the standalone router (`python -m dynamo.router`

), exposed on `DYN_SYSTEM_PORT`

when set. Populated per-request when `--router-mode kv`

is active; registered with zero values in non-KV modes.

All metrics carry the standard hierarchy labels (`dynamo_namespace`

, `dynamo_component`

, `dynamo_endpoint`

).

#### Per-Request Routing Overhead (`dynamo_router_overhead_*`

)

Histograms (in milliseconds) tracking the time spent in each phase of the routing decision for every request. Registered on the frontend port (default 8000) at `/metrics`

with a `router_id`

label (the frontend’s discovery instance ID). These metrics are only created when the frontend has DRT discovery enabled (i.e., `--router-mode kv`

); they do not appear in non-KV modes or on the standalone router.

#### Router Queue Metrics (`dynamo_frontend_router_queue_*`

)

Gauges track pending work in each router policy class. They are registered by the frontend and are populated when queueing is enabled through either `--router-queue-threshold`

or a threshold in `--router-policy-config`

.

**Labels:** `model`

, `worker_type`

(`prefill`

or `decode`

), and `policy_class`

. With policy-family/cache-bucket YAML, `policy_class`

is the resolved physical queue, not the family requested by the client. The rejection counter also has `reason`

.

#### KV Indexer Metrics

Tracks KV cache events applied to the frontend-embedded router’s radix tree index. The counter includes events applied to both the device tier and lower tiers such as host-pinned memory and disk. Only appears when `--router-kv-overlap-score-credit`

is greater than 0 (default) and workers are publishing KV events. Will not appear if `--router-kv-overlap-score-credit 0`

is set or no KV events have been received.

**Additional labels:** `status`

(`ok`

/ `parent_block_not_found`

/ `block_not_found`

/ `invalid_block`

/ `capacity_exhausted`

/ `indexer_invariant_violation`

), `event_type`

(`stored`

/ `removed`

/ `cleared`

)

The standalone indexer exposes the device-tier-only counter
`dynamo_kvrouter_kv_cache_events_applied`

; see the [Standalone KV Indexer](https://docs.nvidia.com/dynamo/v1.3.0/components/router/standalone-indexer).

#### Per-Worker Load and Timing Gauges (`dynamo_frontend_worker_*`

)

These appear once workers register and begin serving requests. They are registered on the frontend’s local Prometheus registry (not component-scoped) and do not carry `dynamo_namespace`

or `dynamo_component`

labels. These metrics are frontend-only and are not available on the standalone router.

**Labels:**

In disaggregated mode, the `worker_type`

label shows both `"prefill"`

and `"decode"`

values; in aggregated mode, all workers report as `"decode"`

.

## NIXL Telemetry Metrics

[NIXL](https://github.com/ai-dynamo/nixl) exposes its own Prometheus metrics on a **separate port** from Dynamo metrics. These metrics track KV cache and embedding data transfers and are only populated during **disaggregated serving** or **multimodal embedding transfers**.

To enable, set these environment variables on your worker process:

For the full list of metrics, configuration options, and architecture details, see the upstream [NIXL Telemetry documentation](https://github.com/ai-dynamo/nixl/blob/main/docs/telemetry.md) and [Prometheus exporter README](https://github.com/ai-dynamo/nixl/blob/main/src/plugins/telemetry/prometheus/README.md). For Kubernetes, see [Enable NIXL Telemetry](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/operate/observability/metrics#enable-nixl-telemetry-optional).

## Related Documentation

[Distributed Runtime Architecture](https://docs.nvidia.com/dynamo/v1.3.0/design-docs/distributed-runtime)[Dynamo Architecture Overview](https://docs.nvidia.com/dynamo/v1.3.0/design-docs/overall-architecture)[Backend Guide](https://docs.nvidia.com/dynamo/v1.3.0/backends/custom-backend/python-workers-lower-level)[Forward Pass Metrics (SGLang)](https://docs.nvidia.com/dynamo/v1.3.0/backends/sg-lang/observability#forward-pass-metrics-fpm)— Per-iteration scheduler telemetry via ZMQ/NATS for planner-driven scaling (requires the SGLang runtime to ship the upstream FPM module; available as of`sglang==0.5.13.post1`

)[Forward Pass Metrics RFC](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/proposals/vllm-rfc-forward-pass-metrics.md)- Design rationale for per-iteration metrics