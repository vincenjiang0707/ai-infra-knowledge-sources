source: https://docs.nvidia.com/dynamo/reference/observability/environment-variables
lastmod: 2026-09-24T19:58:16.636Z

# Environment Variables

This page catalogs the environment variables that govern Dynamo observability. Set them on every
frontend, router, or worker that should emit a signal. For local procedures, see
[Observe a Local Deployment](https://docs.nvidia.com/dynamo/cli/operations/observability) and
[Observe a Local Deployment](https://docs.nvidia.com/dynamo/cli/operations/observability#check-deployment-health).

The canonical list of variable names lives in [ lib/runtime/src/config/environment_names.rs](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/lib/runtime/src/config/environment_names.rs), which groups them by area (logging, OTLP, system server, canary, request trace). The logging and OTLP variables are read in


`lib/runtime/src/logging.rs`

`setup_logging()`

; the `DYN_SYSTEM_*`

and health variables are read by the system-status server. The backend log-level variables (`VLLM_LOGGING_LEVEL`

, `TLLM_LOG_LEVEL`

) are read by the respective engines, not the Dynamo runtime.Every variable on this page is set the same way whether you run locally or on Kubernetes — the same name, only the value or convention differs. A few fields note an **Operator preset**: the value the Dynamo operator injects on Kubernetes, which your own configuration overrides. Kubernetes-only *metrics enablement* is controlled by CRD annotations and Helm values rather than environment variables — see [Operator Metrics](https://docs.nvidia.com/dynamo/reference/observability/operator-metrics#kubernetes-enablement-knobs).

Prometheus metric families in Dynamo are registered lazily: each label set is created the first time it fires, so a freshly-started process shows empty metric families until the first relevant request. An idle cluster does not mean scraping is broken.

## Setting these variables

Every Dynamo process reads its own environment at startup, so set these on each process you want to emit signals — the frontend, the router, and each worker. The tabs below cover the two ways to do that; everything inside applies to whichever environment you pick.

## System and metrics

Port for the backend component’s system-status server, which serves `/metrics`

and the health endpoints. Disabled by default; local examples use `8081`

. Must be set explicitly for backend workers and the standalone router to expose metrics.

**Operator preset:** `9090`

on worker, prefill, decode, and planner pods.

Frontend HTTP port, where `dynamo_frontend_*`

metrics are served at `/metrics`

. Also configurable via the `--http-port`

flag.

**Operator preset:** `8000`

on frontend pods.

Enables [NIXL](https://github.com/ai-dynamo/nixl) telemetry. NIXL metrics track KV cache and embedding data transfers and are populated only during disaggregated serving or multimodal embedding transfers.

**Operator preset:** `n`

on worker, prefill, and decode pods.

NIXL telemetry exporter to use, e.g. `prometheus`

.

**Operator preset:** `prometheus`

on worker, prefill, and decode pods.

Port for NIXL’s Prometheus exporter — a separate port from the Dynamo metrics port. Use distinct values per worker (e.g. `19090`

prefill, `19091`

decode) to avoid collisions.

**Operator preset:** `19090`

on worker, prefill, and decode pods.

## OpenTelemetry (traces and logs)

Master switch for OTLP export. Gates both traces and runtime logs. Request trace records require the separate `otel`

request-trace sink.

Generic endpoint for traces and logs. For `grpc`

, Dynamo uses it as-is. For `http/protobuf`

, Dynamo appends `/v1/traces`

or `/v1/logs`

. When unset, each signal uses its protocol default.

Trace-only endpoint, used as-is. Falls back to `OTEL_EXPORTER_OTLP_ENDPOINT`

, then `http://localhost:4317`

for `grpc`

or `http://localhost:4318/v1/traces`

for `http/protobuf`

.

Log-only endpoint, used as-is. Falls back to `OTEL_EXPORTER_OTLP_ENDPOINT`

, then `http://localhost:4317`

for `grpc`

or `http://localhost:4318/v1/logs`

for `http/protobuf`

. It does not fall back to the traces endpoint.

Default OTLP transport for traces and logs.

Allowed values: grpc http/protobufTrace-only protocol override. Falls back to `OTEL_EXPORTER_OTLP_PROTOCOL`

.

Log-only protocol override. Falls back to `OTEL_EXPORTER_OTLP_PROTOCOL`

.

Head-sampling ratio in `[0.0, 1.0]`

. Unset exports every trace. For example, `0.01`

retains approximately one percent of traces.

Service name attached to exported telemetry. Use a per-component value such as `dynamo-frontend`

to distinguish services.

## Logging

Emit logs as JSONL. When enabled, logs include `trace_id`

and `span_id`

fields and spans are created per request. Recommended for Loki.

Emit span entry/close events (`SPAN_FIRST_ENTRY`

, `SPAN_CLOSED`

messages).

Log level, optionally per target: `<default_level>,<module_path>=<level>,...`

. Example: `info,dynamo_runtime::system_status_server:trace`

.

Use the local timezone for log timestamps. Default is UTC.

Path to a custom TOML logging configuration. Unset by default.

vLLM backend log level. Completely independent of `DYN_LOG`

.

TensorRT-LLM backend log level. Independent of `DYN_LOG`

and read **once at import time** — it must be set before the process starts.

Disable Dynamo’s SGLang log configuration so you can manage the SGLang engine’s logging independently (e.g. via the worker’s `--log-level`

flag).

## Health checks

Path of the frontend health endpoint.

Path of the frontend liveness endpoint.

Initial health status a component reports before its required endpoints are served.

Allowed values: ready notreadyPath of the health endpoint on the system-status server.

Path of the liveness endpoint on the system-status server.

Deprecated compatibility variable. The current runtime logs a warning and does not use this value to select endpoints for system health.

**Operator preset:** `["generate"]`

on worker, prefill, and decode pods.

Enables canary health checks, which actively probe worker endpoints during idle periods. Defaults to `false`

. The shadow-engine failover path may re-enable it per engine. (The health-check *guide* describes canary checks as “automatically enabled” in Kubernetes — that reflects the intended failover behavior, not the base value the operator injects.)

**Operator preset:** `false`

on worker, prefill, and decode pods.

Seconds of endpoint idle time before a canary health check is sent. Lower values check more frequently.

Maximum seconds to wait for a canary health-check response before marking the endpoint unhealthy.

Optional canary payload override for unified backends. Accepts a JSON object or
`@/path/to/payload.json`

and takes precedence over the backend’s default payload.

## Forward Pass Metrics tracing

Enables Forward Pass Metrics persistence. Equivalent to the worker `--fpm-trace`

switch.

Output prefix for `<prefix>.<producer-id>.<index>.jsonl.gz`

files.

Capture mode: `sampled`

writes the latest changed value per worker and data-parallel rank; `full`

writes every valid payload.

Sampling interval used by `sampled`

mode.

Segment roll threshold in uncompressed JSONL bytes.

Number of segments retained independently for each producer.

See [Forward Pass Metrics Trace Reference](https://docs.nvidia.com/dynamo/reference/observability/forward-pass-metrics-traces) for topology support and file semantics.

## Request tracing

Master switch. When enabled without an explicit record selection, emits `request_end,tool`

.

Comma-separated record types: `request_end`

, `request_payload`

, and `tool`

.

Comma-separated sinks: `file`

, `stderr`

, `nats`

, and `otel`

.

Literal JSONL path or gzip segment prefix, depending on `DYN_REQUEST_TRACE_FILE_FORMAT`

.

File encoding: `jsonl`

or rotating `jsonl_gz`

.

Best-effort in-process broadcast capacity.

Subject used by the `nats`

sink.

Maximum serialized OTLP payload attribute size. Oversized payload rows emit an incomplete marker.

File batching threshold in bytes.

Periodic file flush interval in milliseconds.

Gzip roll threshold in uncompressed bytes.

Optional gzip roll threshold in records.

Optional ZMQ PULL bind address for harness tool events. Configure it on only one process.

First-frame ZMQ topic filter.

Comma- or whitespace-separated allowlist of HTTP header names captured on `request_payload`

rows. Values are not redacted.

See [Request Trace Reference](https://docs.nvidia.com/dynamo/reference/observability/request-traces) for compatibility aliases, sink behavior, and record semantics.

## Related

[Metrics Catalog](https://docs.nvidia.com/dynamo/reference/observability/metrics-catalog)— the`dynamo_*`

metrics these variables expose.[Metric Labels](https://docs.nvidia.com/dynamo/reference/observability/metric-labels)— the dimensions attached to those metrics.[Operator Metrics](https://docs.nvidia.com/dynamo/reference/observability/operator-metrics)— Kubernetes-only metrics enablement knobs.[Local Resource Monitor (Local)](https://docs.nvidia.com/dynamo/reference/observability/local-resource-monitor-local)— host-side per-process exporter.