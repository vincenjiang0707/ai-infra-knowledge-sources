source: https://docs.nvidia.com/dynamo/v1.3.0/user-guides/agents/agent-tracing
lastmod: 2026-09-24T19:58:16.636Z

# Agent Tracing

Export Dynamo request traces, tool-call metadata, and Perfetto timelines

Agent tracing records what Dynamo measured for each eligible LLM request. When a request carries [session identity](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/agents/session-i-ds), trace rows include the session fields so you can join LLM requests, inferred tool calls, optional harness tool spans, and Perfetto slices. Recording session identity does not enable sticky sessions or session-aware routing.

Dynamo does not store tool-call arguments in request traces. Include `request_payload`

in `DYN_REQUEST_TRACE_RECORDS`

when you need request or response payloads.

## Enable Output

The fast path is one environment variable:

That selects gzip-compressed JSONL file output at `/tmp/dynamo-request-trace.*.jsonl.gz`

. Tool-call understanding works immediately from `request_end`

finish metadata: no harness tooling required. The optional ZMQ tool-event ingress is opt-in; see [Tool Call Observability](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/agents/agent-tracing#tool-call-observability).

To relocate captures, set an output path:

`DYN_REQUEST_TRACE`

is the only trace switch. The same request trace stream contains compact replay rows when no session identity is present and enriched agent rows when it is. All request trace variables are documented in [Request Replay Tracing](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/observability/request-tracing.md).

## Dynamo `request_end`

Record

Dynamo emits `request_end`

after the response stream finishes or is dropped. The record carries session identity, `output_tokens`

, and autodetected `finish_reason_metadata`

such as tool-call names and finish reasons. `request_id`

correlates with `request_payload`

rows when payload logging is enabled. The `replay`

block lets DynoSim load the original request trace directly when Dynamo can represent the request as one replay request. Tool-call metadata is IDs and names only; arguments are intentionally not stored.

## Full `request_end`

record

Current request tracing skips unsupported multi-choice replay shapes such as `n > 1`

and `best_of > 1`

, so do not assume every session turn is present unless skipped-row warnings are absent. For chat streams, finish metadata is recorded after parser and jail rewrites. Completion streams record the final OpenAI-compatible completion finish reason.

## Tool Call Observability

Default behavior requires no harness work. Dynamo parses each response stream and records the tool calls the model made into [ request_end.finish_reason_metadata](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/agents/agent-tracing#dynamo-request_end-record): the per-turn

`finish_reason`

and each call’s `name`

and `id`

. Arguments are never stored. This is active whenever `DYN_REQUEST_TRACE=1`

and the worker runs a tool-call parser with `--dyn-tool-call-parser`

.You can recover tool-wait time offline without tool events. Within a session, the agent is sequential, so the gap between one turn finishing and the next arriving is the tool plus agent-overhead time:

`request_received_ms`

is stamped at the frontend before the request enters the router queue or pause path. Server wait time lands in each request’s own duration, not in the inter-turn gap. For agentic replay, that gap becomes the inter-request delay. Autodetect cannot split tool execution from agent overhead; it gives the wall-clock union of any parallel tool calls.

## Optional explicit tool events over ZMQ

For precise tool call timing information, you can have your agent harness send tool call events with the relevant `session_id`

attached. Set `DYN_REQUEST_TRACE_TOOL_EVENTS_ZMQ_ENDPOINT`

to bind the ingress, then have the harness publish tool events. Use this when you need per-tool attribution: `duration_ms`

, `status`

, output size, or error type.

Wire format is `[topic, seq_be_u64, msgpack(RequestTraceToolEventIngress)]`

; the default topic is `agent-tool-events`

. Use a background publisher, bounded queue, monotonic sequence, and PUSH with HWM. Terminal `tool_end`

and `tool_error`

rows should carry timing (`started_at_unix_ms`

, `ended_at_unix_ms`

, `duration_ms`

) even if `tool_start`

was dropped.

Use the same session identity as the surrounding LLM calls. Dynamo converts `session_id`

and `parent_session_id`

into the internal request trace context. `tool_call_id`

should be unique per session. Join offline on `session_id`

and `tool_call_id`

.

Example `tool_end`

:

Optional top-level key: `parent_session_id`

. Optional `tool`

keys: `output_tokens`

, `output_bytes`

, `tool_name_hash`

, `error_type`

. Status values: `running`

, `succeeded`

, `error`

, `cancelled`

; synonyms `ok`

/`success`

, `failed`

, `timeout`

, and `canceled`

also deserialize.

## Request Payloads

Request traces do not save input or output payloads unless payload logging is
enabled. To include chat-completion payload rows in the same request trace
stream, select both `request_end`

and `request_payload`

records with
`DYN_REQUEST_TRACE_RECORDS=request_end,request_payload`

.

After the run, split metadata and payload rows by `event_type`

:

Each JSONL line wraps the record:

`timestamp`

is sink-relative elapsed time in milliseconds. Use
`event.event_time_unix_ms`

for wall-clock ordering.

## View Traces in Perfetto

Convert request trace JSONL files into a [Perfetto](https://ui.perfetto.dev/) trace file:

Open the output in [Perfetto UI](https://ui.perfetto.dev/). The default view shows the normal request stack for LLM requests, backend stages, and tool spans when present.

To replay collected traces using the dynamo mock inference engines, see [Agent Simulation](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/agents/agent-simulation).