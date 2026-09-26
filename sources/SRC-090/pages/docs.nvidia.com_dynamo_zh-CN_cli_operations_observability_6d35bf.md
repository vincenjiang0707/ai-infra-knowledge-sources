source: https://docs.nvidia.com/dynamo/zh-CN/cli/operations/observability
lastmod: 2026-09-24T19:58:16.636Z

# Observe a Local Deployment

Use the stack from [Install Observability](https://docs.nvidia.com/dynamo/cli/installation/observability.mdx) to inspect a local Dynamo
deployment. This guide covers the common operational workflows; configuration fields and signal
internals live in Reference and Design Documents.

## View Metrics and Dashboards

### Start a worker

In another terminal, start a vLLM worker and expose its system metrics on port `8081`

:

The supplied Prometheus configuration scrapes the frontend at `host.docker.internal:8000`

and
workers at `host.docker.internal:8081`

and `host.docker.internal:8082`

.

### Inspect the metrics

Check the frontend at `http://localhost:8000/metrics`

and the worker at
`http://localhost:8081/metrics`

. Then open Grafana at `http://localhost:3000`

, sign in with username
`dynamo`

and password `dynamo`

, and open **Dashboards > Dynamo Dashboard**.

Prometheus registers labeled series after the first matching request, so some metric families remain empty until the deployment serves traffic.

For metric definitions and labels, see the [Metrics Catalog](https://docs.nvidia.com/dynamo/reference/observability/metrics-catalog)
and [Metric Labels](https://docs.nvidia.com/dynamo/reference/observability/metric-labels).

## Inspect Traces and Exported Logs

Dynamo exports traces and logs together when OpenTelemetry Protocol (OTLP) export is enabled. The local OpenTelemetry Collector sends traces to Tempo and logs to Loki.

### Launch a traced deployment

Run the aggregated vLLM tracing example:

For a two-GPU prefill/decode deployment, use `./disagg_tracing.sh`

instead. The scripts enable JSONL
logging and OTLP export over gRPC and assign service names to the Dynamo processes.

### Send an identifiable request

Use the model name printed by the launch script. Add `x-request-id`

to correlate the request across
traces and logs:

To configure export endpoints, sampling, service names, or logging levels, see
[Environment Variables](https://docs.nvidia.com/dynamo/reference/observability/environment-variables). For log formats and
fields, see [Logging Reference](https://docs.nvidia.com/dynamo/reference/observability/logging). For the signal pipeline and
span relationships, see [Observability Architecture](https://docs.nvidia.com/dynamo/knowledge-base/concepts/observability-architecture).

## Capture Forward Pass Metrics

Forward Pass Metrics (FPM) tracing records backend scheduler telemetry to rotating gzip JSONL files. It is a best-effort observability stream: Dynamo continues publishing FPM events to the event plane while writing a local copy for analysis.

FPM trace files can contain detailed workload-shape information. Store them according to your organization’s telemetry retention and access policies.

### Choose a trace path

Set a writable output prefix. The default, `/tmp/dynamo-fpm`

, is suitable for temporary local
analysis:

Each worker writes a producer-specific sequence such as
`/tmp/dynamo-fpm.4192.000000.jsonl.gz`

.

### Start a worker with FPM tracing

Use the worker CLI switch:

Or set `DYN_FPM_TRACE=1`

before starting a supported worker. The default `sampled`

mode keeps the
latest changed record per worker and data-parallel rank every five seconds. To capture every valid
payload, including idle heartbeats, set `DYN_FPM_MODE=full`

; full mode can generate substantially
more I/O.

### Inspect the trace

Generate representative traffic, list the segments, and decompress one producer’s files in index order:

Replace `4192`

with the producer ID in the file name. Use `worker_id`

, `dp_rank`

, and `counter_id`

together when checking continuity. Gaps can result from sampling, queue pressure, transport loss, or
worker termination.

For the complete variable list, supported topologies, record schema, capacity planning, and rotation
behavior, see [Forward Pass Metrics Trace Reference](https://docs.nvidia.com/dynamo/reference/observability/forward-pass-metrics-traces).
For the publication and persistence flow, see
[Observability Architecture](https://docs.nvidia.com/dynamo/knowledge-base/concepts/observability-architecture#forward-pass-metrics-persistence).

## Capture and Replay Requests

Request tracing records replay metadata for eligible OpenAI chat and completion requests. It can also capture chat request and response payloads and export records through the OpenTelemetry Protocol (OTLP) log pipeline.

Request payloads and captured HTTP headers can contain sensitive data. Restrict access to trace sinks and do not allowlist credential-bearing headers.

### Capture Replay Metadata

Enable the default rotating gzip file sink before starting the frontend:

After sending representative traffic, confirm that Dynamo writes segments such as
`/tmp/dynamo-request-trace.000000.jsonl.gz`

. The default record selection is `request_end,tool`

.
Session headers enrich supported rows with session identity and dependencies; they do not enable
sticky routing.

### Capture Request and Response Payloads

Select the payload record and one or more sinks:

To retain replay metadata and payloads in one stream, set
`DYN_REQUEST_TRACE_RECORDS=request_end,request_payload,tool`

. Canceled and failed chat requests
retain the request body and omit the response body.

To capture selected request headers, provide a comma- or whitespace-separated allowlist:

Header matching is case-insensitive. Dynamo does not redact captured values.

### Export Payloads over OTLP

Include the `otel`

sink and configure the logs endpoint and protocol:

Use `file,otel`

to retain a local copy. Setting an OTLP logs endpoint without including `otel`

does
not export request trace records. In Grafana, query Loki for scope `dynamo.request_trace`

or body
`request_payload`

.

### Replay a Capture

Pass `dynamo.request.trace.v1`

JSONL or JSONL.GZ shards directly to DynoSim:

No Mooncake conversion is required. DynoSim derives and validates the trace block size. It preserves session dependencies and tool waits when every request has session context and rejects mixed session-aware and context-free trace sets.

For all variables, compatibility aliases, sinks, record schemas, and supported request shapes, see
[Request Trace Reference](https://docs.nvidia.com/dynamo/reference/observability/request-traces).

## Check Deployment Health

Use Dynamo’s HTTP health endpoints to check local processes or configure an external supervisor. The
frontend serves its endpoints on the HTTP port. Workers and standalone routers serve health endpoints
through the system-status server when `DYN_SYSTEM_PORT`

is enabled.

### Enable Active Worker Checks

Canary checks send a small inference request through an idle worker endpoint. Enable them when you need active failure detection:

Normal successful traffic resets the idle timer. After the configured idle period, Dynamo sends a canary request; a timeout marks the endpoint unhealthy.

### Troubleshoot Health Checks

**Connection refused:**Set`DYN_SYSTEM_PORT`

before starting a worker and query that port.**Worker remains**Inspect startup logs and confirm the engine registered its serving endpoint.`notready`

:**Canary checks do not run:**Confirm`DYN_HEALTH_CHECK_ENABLED=true`

was set before startup.**Canary checks time out:**Inspect engine errors and increase`DYN_HEALTH_CHECK_REQUEST_TIMEOUT`

only when normal inference latency requires it.

For response fields, status codes, custom paths, active-check defaults, and endpoint differences, see
[Health Check Reference](https://docs.nvidia.com/dynamo/reference/observability/health-checks). For the canary lifecycle, see
[Observability Architecture](https://docs.nvidia.com/dynamo/knowledge-base/concepts/observability-architecture#active-worker-health-checks).

## Troubleshoot Collection

**Prometheus target is down:**Open`http://localhost:9090/targets`

, confirm the process uses the configured port, and confirm it is reachable through`host.docker.internal`

.**Tempo or Loki is empty:**Set`OTEL_EXPORT_ENABLED=true`

on every process. For gRPC, use the Collector endpoint`http://localhost:4317`

. For HTTP/protobuf, set`OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf`

and use the Collector HTTP endpoint. Logs do not fall back to the traces-only endpoint.**Only some components appear:**Environment variables are process-local. Export the OTLP and logging variables before starting the frontend, router, and each worker.**Stack service is unhealthy:**Run`docker compose -f dev/docker-observability.yml ps`

and inspect the relevant service with`docker compose -f dev/docker-observability.yml logs <service>`

.

Service ports, configuration files, and optional profiles are listed in the
[Local Observability Stack Reference](https://docs.nvidia.com/dynamo/reference/observability/local-stack).