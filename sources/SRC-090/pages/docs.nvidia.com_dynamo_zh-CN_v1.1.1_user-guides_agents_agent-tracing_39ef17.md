source: https://docs.nvidia.com/dynamo/zh-CN/v1.1.1/user-guides/agents/agent-tracing
lastmod: 2026-09-23T23:30:39.914Z

# Agent Tracing

Attach trajectory identity and export Dynamo request and tool-event telemetry

Dynamo agent tracing writes serving-oriented trace records for agentic
requests. Each LLM call carries passive `nvext.agent_context`

identity
(session and trajectory IDs) that Dynamo records alongside its own request
metrics, plus optional harness-published tool lifecycle events. Agent context
does not change routing, scheduling, or cache behavior; trace output is
best-effort profiling data, not durable audit data.

## Request Schema

Each harness LLM call should include `nvext.agent_context`

:

A single `session_id`

can contain multiple parent and child trajectories. The
field names align with the [Agent Trajectory Interchange Format](https://github.com/harbor-framework/harbor/blob/main/rfcs/0001-trajectory-format.md) so
harness trajectory files and Dynamo serving traces join without renaming; see
the collapsed section at the bottom of this page for details.

### OpenAI Client Integration

When using the OpenAI Python client, pass Dynamo’s extension fields through
`extra_body`

and set `x-request-id`

through `extra_headers`

:

`x-request-id`

is the harness’s logical LLM-call ID. Dynamo copies it into
`request.x_request_id`

; it is separate from Dynamo’s internal request ID.

### Harness Integration Pattern

An existing harness does not need to import Dynamo packages or link against Dynamo runtime APIs. Framework integrations should use this shape:

- Add a small helper module that stores the current
`agent_context`

in a context variable. - Wrap each agent run with that context so LLM calls and tool records share the
same
`session_id`

and`trajectory_id`

. - Call one helper before each OpenAI-compatible LLM request to merge
`extra_body.nvext.agent_context`

and set`x-request-id`

. - Propagate context through thread pools, subprocesses, and subagent launches when those paths can make LLM calls or emit tool records.
- Include
`parent_trajectory_id`

when launching a subagent from a known parent trajectory.

## Enable Trace Output

For most local profiling runs, use rotating compressed JSONL:

This writes files like:

To ingest harness tool events, configure the local ZMQ endpoint that Dynamo will bind. Harness processes connect to this endpoint as producers:

Then start any Dynamo OpenAI-compatible backend.

## Environment variable reference

`DYN_AGENT_TRACE_SINKS`

is the local output enable switch. Setting
`DYN_AGENT_TRACE_OUTPUT_PATH`

alone does not enable tracing. Setting only the ZMQ
endpoint enables tool ingestion but does not create local files unless a sink is
also configured.

## Tool Events

Harnesses connect a long-lived local ZMQ PUSH socket and publish tool lifecycle
records to the endpoint Dynamo binds. Dynamo accepts `tool_start`

, `tool_end`

,
and `tool_error`

records from the harness and writes them to the same trace
stream as LLM request records.

The ZMQ wire format is:

Use a bounded queue, a background publisher thread, monotonically increasing
sequence numbers, and a PUSH socket with a high-water mark. Terminal tool
records should be self-contained with `started_at_unix_ms`

, `ended_at_unix_ms`

,
and `duration_ms`

because queue pressure, process exits, or network failures can
still drop earlier `tool_start`

records. Keep `tool_start`

for live/in-flight
status, but do not require it to reconstruct completed spans.

### Endpoint Ownership

Dynamo owns the shared ZMQ bind. Harnesses are producers and only connect.

This direction matters for production process trees. Agent frameworks often run
tools, subagents, plugins, or model wrappers in child processes. If every process
that loads a tracing integration tries to bind the same local endpoint, only one
process succeeds and the others fail during startup. With Dynamo as the single
collector bind and all harness processes connecting as PUSH producers, parent and
child processes can emit their own tool records independently while preserving
their own `agent_context.trajectory_id`

and `parent_trajectory_id`

.

The record must include `agent_context`

. Tool events should use the same
`session_type_id`

, `session_id`

, and `trajectory_id`

as the surrounding LLM
calls; include `parent_trajectory_id`

for subagent tools when it is available.
Dynamo uses these fields to group request and tool records into the same
session/trajectory lanes. Treat `tool_call_id`

as unique within a trajectory,
not globally unique; offline consumers should join tool records on `session_id`

,
`trajectory_id`

, and `tool_call_id`

.

## Inspect the Trace

Read compressed trace records directly:

Each line is a recorder envelope:

Convert traces to Chrome Trace JSON for Perfetto UI:

Open `${DYN_AGENT_TRACE_OUTPUT_PATH}.perfetto.json`

in
[Perfetto UI](https://ui.perfetto.dev/). Each LLM request becomes a timeline
slice grouped by session and trajectory lane. Tool terminal records become tool
slices on adjacent tool tracks.

Useful converter flags:

## Replay the Trace with Mocker

Request trace rows include text-free replay hashes by default. Convert a trace shard to Mooncake JSONL, then replay it through mocker:

Use the `trace_block_size`

printed by the converter when launching replay. For a
multi-worker KV-router replay:

`kv_router`

requires more than one mock worker. For a single aggregated-worker
smoke test, use `--router-mode round_robin --num-workers 1`

.

### Replay Scope and Follow-ups

What works today:

- Per-
`request_end`

cumulative input-block hashes are emitted on agent traces by default. - Single-turn agent traces convert to Mooncake JSONL with absolute timestamps
and compacted
`hash_ids`

. - Mocker replay reads these rows as wall-clock arrivals and simulates a cache pattern from the configured engine, router, and capacity model.
- Concurrent LLM fan-out from the same
`trajectory_id`

is preserved as parallel arrivals because converted rows do not share a`session_id`

.

On the roadmap:

- Live KV cache movement is simulated by the mocker, not replayed byte-for-byte from the original run. Higher-fidelity replay would need an explicit replay event stream or sidecar rather than inferring writes in the converter.
- Output token text/ids are not reconstructed. Replay only drives
`max_output_tokens`

; the original response text is not regenerated. - Causal tool and turn dependencies are not modeled in single-row Mooncake output. A request that depended on an earlier tool result is replayed by its absolute arrival time, not as “wait for the tool to finish”.
- End-to-end re-run of an agent run is on the roadmap. Replay today is request-level; reconstructing tool decisions, agent control flow, or external tool effects is follow-up work.

## Record Semantics

Dynamo emits `request_end`

after the response stream completes or is dropped.
Nullable fields are omitted when the serving path did not record them.

Request records capture Dynamo-owned serving metrics:

Trace records do not include prompt/response content, raw token IDs, sampling parameters, finish reason, or error status. Replay hashes expose prompt prefix reuse structure without storing the prompt text. Use the audit sink for request/response payload capture and OpenTelemetry export for span-based observability.

For local payload debugging, enable audit logging alongside agent tracing.
Audit and agent trace share the same `jsonl`

and `jsonl_gz`

sink primitives, so
both streams can be captured to disk in parallel:

Audit records include the raw OpenAI-compatible request, the final aggregated
response, and any `nvext.agent_context`

supplied by the harness. Join audit
records to agent trace records by `request_id`

when correlating payload text
with replay hashes and timing metrics:

Audit also accepts `stderr`

and `nats`

sinks; `DYN_AUDIT_SINKS`

takes a
comma-separated list (for example `jsonl_gz,nats`

).

Replay hashes describe the cumulative input presented to each LLM request. They
do not by themselves declare cache movement, observed reuse, or that a prior
decode stored a block in KV cache. Mooncake conversion maps these sequence
hashes to compact per-file `hash_ids`

and writes an absolute request-arrival
`timestamp`

on every converted row. Replay/mocker treats rows with explicit
per-turn timestamps as wall-clock arrivals, so LLM calls from the same
`trajectory_id`

can overlap when the original agent issued them concurrently.
Rows that use `delay`

instead keep closed-loop session behavior: the next turn
waits for the previous turn to complete plus the delay. Replay/mocker then
treats those rows as request reads and simulates KV writes/events from the
configured engine, router, capacity, admission, and timing model. The simulated
cache pattern is only as exact as those replay parameters.

## Consistency Model

Trace output is best-effort profiling data, not durable audit data. Dynamo writes LLM request records and harness tool records into the same trace stream, but it does not commit them transactionally.

Delayed tool records are expected. Each normalized record carries
`event_time_unix_ms`

, and offline tools should order records by event time
rather than by JSONL line order. The Perfetto converter does this before
rendering request and tool slices.

The trace file does not prove completeness. Records can be absent if Dynamo exits before sink workers drain, if the trace bus or sink lags and drops records, or if the ZMQ/event-plane path drops a harness event.

## Current Scope

- Agent context is passive metadata.
- Agent request trace emission is currently wired for
`/v1/chat/completions`

. - Supported sinks are
`jsonl`

,`jsonl_gz`

, and`stderr`

. - Tool events enter through the Dynamo-owned ZMQ relay.
- Dynamo does not expose a separate direct event-plane ingress path for harness tool events.
- Future scheduler/profiler consumers should read the normalized trace bus.

## ATIF alignment

The [Agent Trajectory Interchange Format (ATIF)](https://github.com/harbor-framework/harbor/blob/main/rfcs/0001-trajectory-format.md) is the JSON format
maintained as the [Harbor framework](https://github.com/harbor-framework/harbor) data schema for complete agent
trajectories (user inputs, agent steps, tool calls, observations, subagents,
rewards). Dynamo does not emit ATIF; it emits `dynamo.agent.trace.v1`

, a
serving-oriented trace covering request timing, tokens, cache, queue depth, and
worker placement. The two formats are complementary and join cleanly because
identifier names match:

A harness ATIF file and Dynamo’s trace stream can be joined offline on
`session_id`

+ `trajectory_id`

without schema changes. Full ATIF reconstruction
still requires harness trajectory data; Dynamo trace records intentionally omit
prompt and response content.