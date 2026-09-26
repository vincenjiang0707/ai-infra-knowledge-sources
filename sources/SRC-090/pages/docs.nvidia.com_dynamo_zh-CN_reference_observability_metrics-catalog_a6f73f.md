source: https://docs.nvidia.com/dynamo/zh-CN/reference/observability/metrics-catalog
lastmod: 2026-09-23T23:30:39.914Z

# Metrics Catalog

Every dynamo_* metric emitted by the frontend, backend workers, and router — name, type, and meaning.

Dynamo exposes metrics in Prometheus exposition format at the `/metrics`

HTTP endpoint. All Dynamo-generated metrics use the `dynamo_*`

prefix and carry the hierarchy labels documented in [Metric Labels](https://docs.nvidia.com/dynamo/reference/observability/metric-labels). This page is the field catalog; for setup and dashboards see the [Metrics guide](https://docs.nvidia.com/dynamo/cli/operations/observability#view-metrics-and-dashboards).

## Metric types

The `type`

on each field below is a [Prometheus metric type](https://prometheus.io/docs/concepts/metric_types/):

**counter**— a cumulative value that only increases (or resets to zero on restart), e.g. total requests.**gauge**— a single value that can go up or down, e.g. in-flight requests.**histogram**— samples observations into configurable buckets and exposes`_bucket`

,`_sum`

, and`_count`

series, e.g. request duration. Labeled histograms/counters/gauges register a metric*family*, not one series.

Labeled metrics (`HistogramVec`

, `CounterVec`

, `GaugeVec`

) register a metric *family*, not individual time series. A series for a given label combination appears at `/metrics`

only after the first request that populates it. A freshly-started process therefore shows empty families until the first matching request — this is expected Prometheus client behavior, not a missing metric.

## Where each family is exposed

Backend workers expose `dynamo_component_*`

only when `DYN_SYSTEM_PORT`

is set (disabled by default; the Kubernetes operator typically sets `9090`

, local examples use `8081`

). See [Environment Variables](https://docs.nvidia.com/dynamo/reference/observability/environment-variables#system-and-metrics).

Engine pass-through metrics (`vllm:*`

, `sglang:*`

, `trtllm_*`

) are emitted by the backend engines themselves and are cataloged separately — see [Metrics Comparison](https://docs.nvidia.com/dynamo/reference/observability/metrics-comparison). NIXL transfer metrics are exposed on their own port and owned by the [upstream NIXL project](https://github.com/ai-dynamo/nixl/blob/main/docs/telemetry.md).

## Frontend metrics

Emitted by the HTTP frontend at `/metrics`

on port 8000 by default. Most carry a `model`

label.

Requests currently being handled by the frontend, from HTTP handler entry until the response stream completes. The top-level in-flight count with no stage breakdown.

Requests currently in a given frontend pipeline stage. Labeled by `stage`

and `phase`

— see [Stage values](https://docs.nvidia.com/dynamo/reference/observability/metric-labels#stage-values) and [Phase values](https://docs.nvidia.com/dynamo/reference/observability/metric-labels#phase-values).

Inflight requests. Kept for backward compatibility; prefer `dynamo_frontend_active_requests`

, which has identical semantics with a clearer name.

Requests in the HTTP processing queue. Kept for backward compatibility; the “waiting for first token” window is now the sum of `dynamo_frontend_stage_requests`

across the `preprocess`

, `route`

, and `dispatch`

stages.

Number of disconnected clients.

Input sequence length in tokens.

Cached tokens (prefix cache hits) per request.

L1 tokenizer prefix-cache hits across all models. One outcome is recorded per encode operation or batch item.

L1 tokenizer prefix-cache misses across all models.

Tokens returned from the L1 tokenizer prefix cache. Labeled by `model`

.

Tokens freshly encoded after an L1 tokenizer cache lookup. Labeled by `model`

.

Use this PromQL expression to calculate the five-minute token reuse ratio by model:

The ratio is defined only when the model has an active L1 cache and observed tokens. Partial hits increment both token counters. When the cache is disabled with `DYN_TOKENIZER_CACHE=0`

, the per-model series are never created, so they are absent from the scrape rather than reported as zero; detect that state with `absent()`

, since a `== 0`

comparison never matches a missing series. Only the literal value `0`

disables the cache; values such as `false`

or `off`

leave it enabled. With the cache enabled, the counters remain zero when encoding fails or the tokenizer has no registered special-token boundaries.

Inter-token latency in seconds.

Output sequence length in tokens.

Total output tokens generated.

End-to-end LLM request duration in seconds.

Total LLM requests.

Time to first token in seconds.

### Migration

Counters for [request migration](https://docs.nvidia.com/dynamo/kubernetes/fault-tolerance/request-migration), the mechanism that continues in-flight requests on a healthy worker when the original worker fails. See [Request Migration Architecture](https://docs.nvidia.com/dynamo/knowledge-base/concepts/fault-tolerance/request-migration-architecture) for the internals.

Total request migrations due to worker unavailability. Labeled by `model`

and [ migration_type](https://docs.nvidia.com/dynamo/reference/observability/metric-labels#metric-specific-labels) (

`new_request`

for an initial connection failure, `ongoing_request`

for a mid-stream disconnection).Total times migration was disabled for a request because its sequence length exceeded `--migration-max-seq-len`

. A rising value may indicate the limit needs adjustment. Labeled by `model`

.

### Cancellation and rejection

Counters for requests that end early: [cancellations](https://docs.nvidia.com/dynamo/knowledge-base/concepts/fault-tolerance/request-cancellation-architecture) (the client or frontend aborts an in-flight request) and [rejections](https://docs.nvidia.com/dynamo/kubernetes/fault-tolerance/request-rejection) (the Frontend sheds load with HTTP 529 by default when all workers are busy). The worker-side counterparts are under [Component metrics](https://docs.nvidia.com/dynamo/reference/observability/metrics-catalog#component-metrics).

Total request cancellations detected by the frontend (client disconnect or stream close). Labeled by `model`

, `endpoint`

(the API route — `chat_completions`

, `completions`

, `embeddings`

, …), and [ request_type](https://docs.nvidia.com/dynamo/reference/observability/metric-labels#metric-specific-labels) (

`unary`

or `stream`

).Total requests rejected because all workers were busy (surfaced to the client as HTTP 529 by default). Incremented when the router returns `ResourceExhausted`

. Labeled by `model`

and `endpoint`

(the API route).

### Per-worker load and timing gauges

`dynamo_frontend_worker_*`

gauges appear once workers register and begin serving. They live on the frontend’s local registry (not component-scoped) and do **not** carry `dynamo_namespace`

or `dynamo_component`

labels. Frontend-only — not available on the standalone router. Labeled by `worker_id`

, `dp_rank`

, and `worker_type`

.

Active KV cache decode blocks per worker.

Active prefill tokens queued per worker.

Last observed time to first token per worker, in seconds.

Last observed input sequence length per worker.

Last observed inter-token latency per worker, in seconds.

### Model configuration metrics

`dynamo_frontend_model_*`

gauges are populated from worker backend registration and all carry a `model`

label. When multiple workers register the same model name, only the first instance’s configuration is recorded.

Total KV blocks available for a worker serving the model.

Maximum number of sequences for a worker serving the model.

Maximum number of batched tokens for a worker serving the model.

Maximum context length for a worker serving the model. Sourced from the Model Deployment Card.

KV cache block size for a worker serving the model. Sourced from the Model Deployment Card.

Request migration limit for a worker serving the model. Sourced from the Model Deployment Card.

## Component metrics

Emitted by backend workers (`python -m dynamo.vllm`

, `python -m dynamo.sglang`

, etc.) at `/metrics`

on `DYN_SYSTEM_PORT`

. All carry the hierarchy labels (`dynamo_namespace`

, `dynamo_component`

, `dynamo_endpoint`

) — see [Runtime-injected labels](https://docs.nvidia.com/dynamo/reference/observability/metric-labels#runtime-injected-labels).

Requests currently being processed by the component.

Total bytes received in requests.

Request processing time in seconds.

Total requests processed.

Total errors encountered while handling a request. Labeled by `error_type`

— see [Component error types](https://docs.nvidia.com/dynamo/reference/observability/metric-labels#component-error-types).

Total bytes sent in responses.

DistributedRuntime uptime. Updated before each Prometheus scrape on both the frontend and the system-status server.

Total requests cancelled by the work handler. Carries the hierarchy labels. Records cancellation *signals* received by the worker, not whether the engine actually aborted — deduplicated so a control message plus a socket close for the same request counts once. See [Request Cancellation Architecture](https://docs.nvidia.com/dynamo/knowledge-base/concepts/fault-tolerance/request-cancellation-architecture).

The following worker-side gauges and counter appear only when a hard concurrency cap is set with `--engine-request-limit`

; see [Worker-Side Request Admission](https://docs.nvidia.com/dynamo/knowledge-base/concepts/fault-tolerance/request-rejection-architecture#worker-side-request-admission).

Cumulative requests rejected because the worker was at capacity (engine in-flight limit and Dynamo queue both full).

Current requests being handled by the engine.

Current requests queued in Dynamo, not yet in the engine.

Specialized components expose additional families under their own prefix, e.g. `dynamo_preprocessor_*`

for preprocessor components.

## Router metrics

The router exposes metrics for routing decisions and overhead. Not every metric appears in every deployment — see [Availability by configuration](https://docs.nvidia.com/dynamo/reference/observability/metrics-catalog#availability-by-configuration).

### Router request metrics

`dynamo_component_router_*`

histograms and counters for aggregate request-level statistics. On the frontend, exposed at `/metrics`

on the HTTP port; on the standalone router, exposed on `DYN_SYSTEM_PORT`

. Populated per-request when `--router-mode kv`

is active; registered with zero values in non-KV modes.

Requests admitted by the router scheduler.

Total requests processed by the router.

Time to first token in seconds.

Average inter-token latency in seconds.

Input sequence length in tokens.

Output sequence length in tokens.

Predicted KV cache hit rate at routing time (0.0–1.0).

### Per-request routing overhead

`dynamo_router_overhead_*`

histograms (milliseconds) track time spent in each phase of the routing decision. Registered on the frontend port with a `router_id`

label (the frontend’s discovery instance ID). Created only when the frontend has DRT discovery enabled (`--router-mode kv`

); absent in non-KV modes and on the standalone router.

Time computing block hashes.

Time in indexer `find_matches`

.

Time computing sequence hashes.

Time in scheduler worker selection.

Total routing overhead per request.

### Router queue metrics

The frontend registers these metrics when queueing is enabled by `--router-queue-threshold`

or a threshold in `--router-policy-config`

. They carry `model`

, `worker_type`

, and `policy_class`

. With policy-family or cache-bucket configuration, `policy_class`

is the resolved physical queue.

Requests pending in the router scheduler queue.

Raw input-sequence tokens pending in the queue.

Cached-token estimate captured when each request enters the queue.

Queue rejections by configured limit reason. Also labeled by `reason`

.

### KV indexer metrics

KV cache events applied to the router’s radix-tree index. Includes events applied to the device tier and lower tiers such as host-pinned memory and disk. Appears only when `--router-kv-overlap-score-credit`

is greater than 0 and workers publish KV events. Labeled by `status`

and `event_type`

— see [Metric-specific labels](https://docs.nvidia.com/dynamo/reference/observability/metric-labels#metric-specific-labels).

CKF block-level mutation outcomes recorded by the router indexer, labeled by `outcome`

— see [Metric-specific labels](https://docs.nvidia.com/dynamo/reference/observability/metric-labels#metric-specific-labels). **Registered, always zero.** The series is created and exported, but no code path currently increments it, so it reads 0 in every deployment. Do not build alerts or dashboard panels on it. The standalone indexer exports the same counter as `dynamo_kvrouter_ckf_mutation_total`

, with the same caveat.

The standalone indexer exposes the device-tier-only counter `dynamo_kvrouter_kv_cache_events_applied`

and the CKF counter as `dynamo_kvrouter_ckf_mutation_total`

; see [Standalone KV Indexer](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/standalone-indexer).

### Availability by configuration

Not all router metrics appear in every deployment. This matrix shows which groups are **registered** and **populated** in each configuration.

**Key:**

**Registered and populated**— the metric appears at`/metrics`

with real values.**Registered, always zero**— the metric appears at`/metrics`

but is never incremented (useful for dashboards that expect it to exist).**Not registered / Not created**— the metric does not appear at`/metrics`

at all.

## Related

[Metric Labels](https://docs.nvidia.com/dynamo/reference/observability/metric-labels)— the dimensions attached to these metrics.[Environment Variables](https://docs.nvidia.com/dynamo/reference/observability/environment-variables)— variables that enable and configure metric emission.[Operator Metrics](https://docs.nvidia.com/dynamo/reference/observability/operator-metrics)— Kubernetes operator metrics catalog.[Metrics Comparison](https://docs.nvidia.com/dynamo/reference/observability/metrics-comparison)— engine pass-through metrics (`vllm:*`

,`sglang:*`

,`trtllm_*`

).