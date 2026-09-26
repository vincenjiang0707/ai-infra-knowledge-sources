source: https://docs.nvidia.com/dynamo/zh-CN/reference/observability/metric-labels
lastmod: 2026-09-23T23:30:39.914Z

# Metric Labels

Every label dimension attached to Dynamo metric series — where each one comes from and the values it can take.

Labels are the **dimensions** attached to Dynamo metric series, not metrics in their own right. A single metric such as `dynamo_component_requests_total`

becomes many Prometheus time series once it is split by `dynamo_namespace`

, `dynamo_component`

, `dynamo_endpoint`

, and the labels the scraper adds. This page catalogs those dimensions; for the metrics themselves see the [Metrics Catalog](https://docs.nvidia.com/dynamo/reference/observability/metrics-catalog).

A label reaches a series through one of four origins:

**Auto-injected by the Dynamo runtime**— added to every metric registered through the namespace/component/endpoint hierarchy.**Added at registration time by backend code**— passed by the worker when it registers an endpoint, so presence depends on the backend.**Added by the metric itself**— specific to one metric family.**Injected by Prometheus/Kubernetes**— attached by the scraper, not present in the exposition text the process emits.

## Scope legend

Each label is tagged with the scope in which it appears:

`[Shared]`

— emitted by the Dynamo process itself; present whether you run locally or on Kubernetes.`[Kubernetes]`

— attached by the Prometheus scraper in a Kubernetes deployment; absent when you scrape a process directly.

## Runtime-injected labels

Added by `create_metric()`

in `lib/runtime/src/metrics.rs`

for every metric registered through the namespace/component/endpoint hierarchy.

`[Shared]`

The Dynamo runtime namespace — the logical scope shared by every component (router / prefill / decode / encode) in one deployment. **Not** the Kubernetes namespace. Example: `dynamo_cloud_vllm_v1_disagg_router_071de157`

.

`[Shared]`

Service role of the emitting component. See [Component names](https://docs.nvidia.com/dynamo/reference/observability/metric-labels#component-names) for the enumeration of values. Example: `backend`

, `prefill`

, `router`

.

`[Shared]`

The RPC within that component. See [Endpoint names](https://docs.nvidia.com/dynamo/reference/observability/metric-labels#endpoint-names) for the enumeration of values. Example: `generate`

, `clear_kv_blocks`

, `worker_kv_indexer_query_dp0`

.

`[Shared]`

Hex-encoded discovery instance ID of the endpoint, providing a stable per-worker identity that does not depend on Kubernetes. Injected only when the endpoint hierarchy has a connection ID. Example: `1a2b3c4d`

.

On the per-worker frontend gauges (`dynamo_frontend_worker_*`

) this label carries the worker’s etcd lease ID instead. Example: `7890`

.

## Registration-time labels

Passed via `metrics_labels=`

when the worker calls `serve_endpoint()`

. Not auto-injected, so presence depends on the backend.

`[Shared]`

The model being served (OpenAI-style label). Added by vLLM, SGLang, and TRT-LLM workers on inference endpoints; absent on internal endpoints like `worker_kv_indexer_query_dp{N}`

. Example: `Qwen/Qwen3-0.6B`

.

`[Shared]`

Same model identifier under a second label name, retained for engine-native and dashboard back-compat. Added by vLLM and TRT-LLM workers; **not** added by SGLang. Example: `Qwen/Qwen3-0.6B`

.

## Metric-specific labels

Added by an individual metric family. Each label appears only on the metrics noted.

`[Shared]`

On `dynamo_component_errors_total`

— the stage of request handling that failed. See [Component error types](https://docs.nvidia.com/dynamo/reference/observability/metric-labels#component-error-types) for the enumeration. On `dynamo_operator_reconcile_errors_total`

the value set is different; see [Operator Metrics](https://docs.nvidia.com/dynamo/reference/observability/operator-metrics).

`[Shared]`

On `dynamo_frontend_stage_requests`

— the frontend pipeline stage a request currently occupies. See [Stage values](https://docs.nvidia.com/dynamo/reference/observability/metric-labels#stage-values).

`[Shared]`

On `dynamo_frontend_stage_requests`

— the serving phase. See [Phase values](https://docs.nvidia.com/dynamo/reference/observability/metric-labels#phase-values). The empty value is used when the stage does not distinguish phases (e.g. `preprocess`

).

`[Shared]`

On `dynamo_frontend_worker_*`

and `dynamo_frontend_router_queue_*`

— the worker role. In disaggregated mode both values appear; in aggregated mode all workers report as `decode`

.

`[Shared]`

On `dynamo_frontend_worker_*`

— the data-parallel rank of the worker. Example: `0`

.

`[Shared]`

On `dynamo_frontend_router_queue_*`

— the resolved physical scheduler queue. With policy-family or cache-bucket configuration, this can differ from the family requested by the client.

`[Shared]`

On `dynamo_frontend_router_queue_backpressure_total`

— the configured queue limit that rejected the request.

`[Shared]`

On `dynamo_frontend_model_migration_total`

— the category of request migration triggered by worker unavailability.

`[Shared]`

On `dynamo_frontend_model_cancellation_total`

— whether the cancelled request was unary or streaming.

`[Shared]`

On `dynamo_component_kv_cache_events_applied`

— the outcome of applying a KV cache event to the router’s radix-tree index.

`[Shared]`

On `dynamo_component_ckf_mutation_total`

, and on `dynamo_kvrouter_ckf_mutation_total`

from the standalone indexer — the block-level CKF mutation outcome. Both counters are registered but never incremented today, so no series carries this label in practice.

`[Shared]`

On `dynamo_component_kv_cache_events_applied`

— the kind of KV cache event.

## Scraper-injected labels (Kubernetes)

Attached by the Prometheus scraper, not present in the exposition text the process emits. These appear only when Prometheus scrapes the pod in a Kubernetes deployment.

`[Kubernetes]`

Scrape target as `<podIP>:<metricsPort>`

. Example: `192.168.133.236:9090`

.

`[Kubernetes]`

Kubernetes pod name; the per-replica disambiguator. Example: `vllm-v1-disagg-router-vllmdecodeworker-...`

.

`[Kubernetes]`

Container name inside the pod (usually `main`

). Example: `main`

.

`[Kubernetes]`

Kubernetes namespace the pod runs in. **Not** the same as `dynamo_namespace`

. Example: `dynamo-cloud`

.

`[Kubernetes]`

Prometheus scrape-job name, `<k8s-namespace>/<service-name>`

. Example: `dynamo-cloud/dynamo-worker`

.

`[Kubernetes]`

Named port on the Kubernetes Service that Prometheus scraped. **Not** the same as `dynamo_endpoint`

. Example: `system`

.

## Label collisions

Two pairs of labels share a name but mean different things depending on origin:

`dynamo_namespace`

(Dynamo deployment scope, runtime-injected) vs.`namespace`

(Kubernetes namespace, scraper-injected).`dynamo_endpoint`

(Dynamo RPC, runtime-injected) vs.`endpoint`

(Kubernetes Service port name, scraper-injected).

Always qualify with the `dynamo_`

prefix when you mean the runtime dimension.

## Enumerations

### Component names

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

The name `backend`

for the decode worker is historical. The runtime has a TODO to introduce a `decode`

constant and migrate to it (see `lib/runtime/src/metrics/prometheus_names.rs::component_names`

).

### Endpoint names

Values you will see in the `dynamo_endpoint`

label on backend workers.

### Component error types

The `dynamo_component_errors_total`

counter is labeled with `error_type`

, identifying which stage of request handling failed.

### Stage values

`dynamo_frontend_stage_requests`

decomposes the lifetime of an active frontend request into three sequential pipeline stages. A request is counted in exactly one stage at a time.

### Phase values

The `phase`

label on `dynamo_frontend_stage_requests`

.

## Related

[Metrics Catalog](https://docs.nvidia.com/dynamo/reference/observability/metrics-catalog)— the`dynamo_*`

metrics these labels attach to.[Operator Metrics](https://docs.nvidia.com/dynamo/reference/observability/operator-metrics)— Kubernetes operator metrics and their distinct label sets.[Environment Variables](https://docs.nvidia.com/dynamo/reference/observability/environment-variables)— variables that enable and configure metric emission.