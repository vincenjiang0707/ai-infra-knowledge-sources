source: https://docs.nvidia.com/dynamo/zh-CN/reference/observability/request-traces
lastmod: 2026-09-23T23:30:39.914Z

# Request Trace Reference

Request tracing emits replay metadata, optional chat payloads, and optional harness tool events to
one or more sinks. For the capture and replay workflow, see
[Observe a Local Deployment](https://docs.nvidia.com/dynamo/cli/operations/observability#capture-and-replay-requests).

## Configuration

Legacy `jsonl`

and `jsonl_gz`

sink values, `DYN_REQUEST_TRACE_OUTPUT_PATH`

, and
`DYN_REQUEST_TRACE_JSONL_*`

remain migration aliases. `DYN_AUDIT_*`

variables are migration shims,
not wire-compatibility aliases. Prefer `DYN_REQUEST_TRACE_*`

for new deployments.

## Sink Behavior

The `otel`

sink maps each row to one OTLP `LogRecord`

in scope `dynamo.request_trace`

. It resolves
transport settings in this order:

- Protocol:
`OTEL_EXPORTER_OTLP_LOGS_PROTOCOL`

, then`OTEL_EXPORTER_OTLP_PROTOCOL`

, then`grpc`

. - Endpoint:
`OTEL_EXPORTER_OTLP_LOGS_ENDPOINT`

, then`OTEL_EXPORTER_OTLP_ENDPOINT`

, then the protocol default. Dynamo appends`/v1/logs`

only to a generic HTTP/protobuf endpoint. - Service name:
`OTEL_SERVICE_NAME`

, default`dynamo`

.

Setting `DYN_REQUEST_TRACE_SINKS=stderr`

does not enable OTLP export. Include `otel`

, for example
`file,otel`

or `stderr,otel`

.

## Record Types

`request_end`


Contains compact replay metadata. Session headers can enrich the row with session identity, request metrics, finish metadata, and tool-call metadata. Session identity does not enable sticky routing.

`request_payload`


Contains the OpenAI `/v1/chat/completions`

client request and, when available, its response. Dynamo
emits one row per eligible request. Canceled or failed requests omit `payload.response`

. Oversized
OTLP bodies use `payload_complete=false`

and `payload_drop_reason`

.

Allowlisted headers appear at `payload.http_request_headers`

. Matching is case-insensitive. Empty,
non-UTF-8, and unlisted values are omitted. Because values are not redacted, do not capture
credential-bearing headers.

### Tool Events

Harness events enter through the optional ZMQ endpoint and are normalized into request trace rows before fan-out to the configured sinks.

## Record Schema

All rows use `schema: dynamo.request.trace.v1`

and an `event_type`

. A context-free replay row
contains request timing, output length, KV block size, input length, and rolling input-sequence
hashes:

A payload row stores the client request under `payload.request`

, the completed response under
`payload.response`

, and a `payload_complete`

marker. Optional captured headers appear under
`payload.http_request_headers`

.

`input_sequence_hashes`

are Dynamo’s sequence-aware rolling hashes. DynoSim maps them to compact
internal IDs while loading the original trace; it does not create an intermediate Mooncake file.

## Supported Replay Requests

Context-free replay rows must represent one model request. Dynamo skips requests with `n > 1`

,
`best_of > 1`

, prompt embeddings, multimodal inputs, or no usable tracker and KV cache block size.
Session context does not bypass these checks.

DynoSim accepts `dynamo.request.trace.v1`

JSONL and JSONL.GZ directly, derives the trace block size,
and rejects mixed session-aware and context-free trace sets.