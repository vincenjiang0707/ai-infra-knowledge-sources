source: https://docs.nvidia.com/dynamo/zh-CN/reference/observability/logging
lastmod: 2026-09-23T23:30:39.914Z

# Logging Reference

Dynamo writes readable text or newline-delimited JSON (JSONL) to standard error. With OTLP export
enabled, it also sends structured log records to the configured OpenTelemetry Collector. For a local
Loki workflow, see [Observe a Local Deployment](https://docs.nvidia.com/dynamo/cli/operations/observability#inspect-traces-and-exported-logs).

## Output Formats

Set `DYN_LOGGING_JSONL=false`

for readable text:

Set `DYN_LOGGING_JSONL=true`

for structured output:

Fields vary by event and active span. Common fields include:

`DYN_LOGGING_SPAN_EVENTS=true`

adds span creation and exit events. This is useful for detailed
debugging but increases log volume.

## Log Levels

`DYN_LOG`

accepts standard tracing filter syntax, including per-target overrides.

For example, keep the default at `info`

and enable trace output for the system-status server:

## OTLP Export

`OTEL_EXPORT_ENABLED=true`

is the master switch for runtime trace and log export. Configure a
generic endpoint for both signals:

Use `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT`

or `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT`

for signal-specific
destinations. Signal-specific endpoints are used as-is. For a generic `http/protobuf`

endpoint,
Dynamo appends `/v1/traces`

or `/v1/logs`

.

`OTEL_EXPORTER_OTLP_LOGS_ENDPOINT`

does not fall back to
`OTEL_EXPORTER_OTLP_TRACES_ENDPOINT`

. If only the traces endpoint is set, logs use the generic
endpoint or the protocol default and can be silently dropped when no collector is listening there.

Set these variables on every process whose telemetry you want to export. Use
`OTEL_TRACES_SAMPLE_RATIO`

to apply head sampling to traces; leaving it unset exports every trace.

## Request Payload Export

Request payload logging uses the request trace pipeline rather than the runtime log stream. Enable
the `request_payload`

record and include the `otel`

sink:

Each request trace row maps to one OTLP `LogRecord`

in scope `dynamo.request_trace`

. Combining
sinks, such as `file,otel`

, writes the same row to every selected destination. `stderr`

alone never
exports over OTLP.

Canceled and failed chat requests retain the request payload and omit the response. Set
`DYN_REQUEST_TRACE_HTTP_HEADER_CAPTURE_LIST`

to capture selected request headers. Captured values
are unredacted, so do not allowlist credentials.

For limits and record semantics, see [Request Trace Reference](https://docs.nvidia.com/dynamo/reference/observability/request-traces).

## Request Correlation

When a request includes an `x-request-id`

header, Dynamo propagates it through the distributed trace
context and records it as `x_request_id`

on participating spans and log events. JSONL logs also carry
`trace_id`

and `span_id`

, allowing Loki results to link to the corresponding Tempo trace.

For the span hierarchy and propagation model, see
[Observability Architecture](https://docs.nvidia.com/dynamo/knowledge-base/concepts/observability-architecture#trace-and-log-correlation).

## Backend Engine Controls

`DYN_LOG`

controls Dynamo. Inference engines retain separate controls:

See [Environment Variables](https://docs.nvidia.com/dynamo/reference/observability/environment-variables#logging) for defaults and the complete logging
and OTLP variable catalog.