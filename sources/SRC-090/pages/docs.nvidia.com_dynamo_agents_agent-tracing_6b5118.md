source: https://docs.nvidia.com/dynamo/agents/agent-tracing
lastmod: 2026-09-24T19:58:16.636Z

# Agent Tracing

Export Dynamo request traces, tool-call metadata, and Perfetto timelines

Agent tracing captures request timing, token counts, worker placement, finish metadata, and replay hashes for eligible LLM requests. Requests with [session identity](https://docs.nvidia.com/dynamo/agents/session-i-ds) also carry agent context, which lets analysis tools group LLM turns and tool activity into the same run.

Request traces contain metadata, not payloads. Dynamo does not store prompts, responses, or tool-call arguments in these traces.


## Capture Your First Agent Trace

### Enable request tracing

Set the master switch before starting the Dynamo frontend:

Dynamo writes rotating gzip-compressed JSONL segments to `/tmp/dynamo-request-trace.NNNNNN.jsonl.gz`

.

To use another segment prefix, set `DYN_REQUEST_TRACE_OUTPUT_PATH`

:

### Run your agent workload

Send requests through a configured [Agent Harness](https://docs.nvidia.com/dynamo/agents/agent-harnesses) or custom client. Session identity enriches eligible `request_end`

rows automatically; it does not require another trace flag.

### Open the timeline

Open `/tmp/dynamo-request-trace.perfetto.json`

in the [Perfetto UI](https://ui.perfetto.dev/). The default view shows LLM request slices, prefill and decode stages, and tool slices when the trace contains tool metadata.

For every request-trace environment variable and default, see [Request Trace Reference](https://docs.nvidia.com/dynamo/reference/observability/request-traces#configuration).

## Choose the Tool Detail You Need

## Tool Call Observability

### Record Tool Calls Automatically

When request tracing is enabled and the worker uses `--dyn-tool-call-parser`

, Dynamo records the final finish reason and each parsed tool call’s name and ID in `request_end.finish_reason_metadata`

. Tool-call arguments are intentionally omitted.

The Perfetto converter infers a tool span from the end of a tool-call response to the next request in the same trajectory. You can calculate the same interval from the trace:

This interval includes tool execution and agent overhead. It cannot separate parallel tools or attribute time to one tool.

### Record Precise Tool Timing

For per-tool attribution, configure the frontend to receive events from the harness:

The endpoint is a ZMQ PULL bind address. The harness publishes `agent-tool-events`

as the first frame unless you override the topic with `DYN_REQUEST_TRACE_TOOL_EVENTS_ZMQ_TOPIC`

.

## Tool-event wire format and example

The wire format is `[topic, seq_be_u64, msgpack(RequestTraceRecord)]`

. Use a monotonic sequence and a background PUSH publisher with a bounded queue. Include `started_at_unix_ms`

, `ended_at_unix_ms`

, and `duration_ms`

on terminal `tool_end`

and `tool_error`

events so timing survives a dropped `tool_start`

.

Use the same agent context as the surrounding LLM requests. Make each `tool_call_id`

unique within its trajectory.

Optional `tool`

fields are `output_tokens`

, `output_bytes`

, `tool_name_hash`

, and `error_type`

. Status values are `running`

, `succeeded`

, `error`

, and `cancelled`

; supported aliases include `ok`

, `success`

, `failed`

, `timeout`

, and `canceled`

.

## Dynamo `request_end`

Record

Dynamo emits `request_end`

after an eligible response stream finishes or is dropped. The record can contain agent context, request timing and token metrics, worker information, finish metadata, and replay hashes.

## Full agent-enriched `request_end`

example

For chat streams, Dynamo records finish metadata after parser and jail rewrites. Completion streams record the final OpenAI-compatible completion finish reason.

Request tracing currently covers eligible Rust OpenAI chat-completions and completions requests. It skips unsupported replay shapes, including `n > 1`

, `best_of > 1`

, `prompt_embeds`

, multimodal inputs, and requests without a tracker or usable KV cache block size. Sinks use best-effort delivery and can drop records when they lag, so check warnings and validate row counts before treating a capture as complete.