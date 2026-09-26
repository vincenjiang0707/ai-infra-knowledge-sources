source: https://docs.nvidia.com/dynamo/v1.1.0/user-guides/agents/agent-context-and-tracing
lastmod: 2026-09-24T19:58:16.636Z

# Agent Context and Tracing

Agent workloads are easier to debug when model calls and tool calls share a common workflow identity. Dynamo agent tracing provides that view without asking the harness to measure serving internals itself.

The harness adds lightweight workflow metadata to each LLM request and can publish tool lifecycle events over a local ZMQ socket. Dynamo then writes a single trace stream that combines harness-provided structure with Dynamo-owned request metrics such as token counts, timing, cache hit rate, queue depth, and worker placement.

This is passive observability. Agent context does not change routing, scheduling, or cache behavior.

## Step 1: Enable Dynamo Trace Output

For most local profiling runs, use rotating compressed JSONL:

This writes files like:

To ingest harness tool events, also configure the local ZMQ endpoint that the harness will publish on:

Then start any Dynamo OpenAI-compatible backend.

## Environment variable reference

`DYN_AGENT_TRACE_SINKS`

is the local output enable switch. Setting
`DYN_AGENT_TRACE_OUTPUT_PATH`

alone does not enable tracing. Setting only the ZMQ
endpoint enables tool ingestion but does not create local files unless a sink is
also configured.

## Step 2: Add Context to LLM Calls

Each harness LLM call should include `nvext.agent_context`

:

When using the OpenAI Python client, pass Dynamo’s extension fields through
`extra_body`

and set `x-request-id`

through `extra_headers`

:

`x-request-id`

is the harness’s logical LLM-call ID. Dynamo copies it into
`request.x_request_id`

; it is separate from Dynamo’s internal request ID.

## Step 3: Send Tool Events to Dynamo

Harnesses bind a long-lived local ZMQ PUB socket and publish tool lifecycle
records on the configured endpoint. Dynamo accepts `tool_start`

, `tool_end`

, and
`tool_error`

records from the harness and writes them to the same trace stream
as LLM request records.

The ZMQ wire format is:

Use the same producer pattern as our KV event publisher pattern in [vllm](https://github.com/vllm-project/vllm/blob/399005a986a2b99f435919777427b6d73d36a277/vllm/distributed/kv_events.py#L103) and [SGLang](https://github.com/sgl-project/sglang/blob/main/python/sglang/srt/disaggregation/kv_events.py): a bounded queue, a background
publisher thread, monotonically increasing sequence numbers, and a PUB socket
with a high-water mark. Plain ZMQ PUB/SUB is best-effort for early frames, so a
terminal tool record should be self-contained with `started_at_unix_ms`

,
`ended_at_unix_ms`

, and `duration_ms`

. Keep `tool_start`

for live/in-flight
status, but do not require it to reconstruct completed spans.

### Publisher Ownership

Most framework integrations should create one exporter per harness or runtime instance. In-process systems, such as callback or middleware integrations, can emit records directly into the root queued publisher.

If a harness runs tools or subagents in child processes, do not let each child
bind the same ZMQ endpoint. Keep the root process as the only network publisher
and forward child records to it over the framework event bus, a multiprocessing
queue, or a local collector. The child should forward the same normalized
`AgentTraceRecord`

; the parent handles ZMQ framing and sequence numbers.

A compact publisher implementation is included below for harness authors that need a reference.

## Compact Python publisher

The record must include `agent_context`

. Tool events should use the same
`workflow_type_id`

, `workflow_id`

, and `program_id`

as the surrounding LLM calls;
include `parent_program_id`

for subagent tools when it is available. Dynamo uses
these fields to group request and tool records into the same workflow/program
lanes.

The runtime event-plane hop is internal to Dynamo. Harnesses should publish to the ZMQ endpoint, not directly to Dynamo’s event plane.

## Step 4: Inspect the Trace

Read compressed trace records directly:

Each line is a recorder envelope:

Convert traces to Chrome Trace JSON for Perfetto UI:

Open `${DYN_AGENT_TRACE_OUTPUT_PATH}.perfetto.json`

in
[Perfetto UI](https://ui.perfetto.dev/). Each LLM request becomes a timeline
slice grouped by workflow and program lane. Tool terminal records become tool
slices on adjacent tool tracks. The converter prefers explicit
`started_at_unix_ms`

/`ended_at_unix_ms`

, falls back to `duration_ms`

, then pairs
with the matching `tool_start`

record when present.

Useful converter flags:

## Harness Integration Patterns

An existing harness does not need to import Dynamo packages or link against Dynamo runtime APIs. Framework integrations should use this shape:

- Add a small helper module that stores the current
`agent_context`

in a context variable. - Wrap each agent run with that context so LLM calls and tool records share the
same
`workflow_id`

and`program_id`

. - Call one helper before each OpenAI-compatible LLM request to merge
`extra_body.nvext.agent_context`

and set`x-request-id`

. - For LangGraph/LangChain-style in-process runtimes, implement callbacks or middleware that emit directly to the root publisher.
- Emit
`tool_start`

and a terminal`tool_end`

or`tool_error`

wherever the harness executes model-requested tools. Include`started_at_unix_ms`

,`ended_at_unix_ms`

, and`duration_ms`

on terminal records so completed spans survive best-effort PUB/SUB startup loss. - Propagate context through thread pools, subprocesses, and subagent launches when those paths can make LLM calls or emit tool records.
- Register a queued ZMQ publisher at process startup when tool tracing is enabled.
- If tools or subagents run in subprocesses, forward normalized tool records back to the root publisher instead of binding another ZMQ endpoint.

You do not need custom code in every tool implementation when existing tool
calls already pass through shared harness code. Add explicit hooks only for paths
that bypass that flow, such as direct OpenAI calls inside a tool, background
executor work that loses context variables, or subagent launches that need
`parent_program_id`

.

That keeps the harness dependency boundary simple:

## End-to-End Example with ms-agent

The ms-agent integration currently lives on Ishan’s fork:

- Fork:
[github.com/ishandhanani/ms-agent](https://github.com/ishandhanani/ms-agent) - Branch:
`idhanani/dynamo-agent-trace`


Install the fork in editable mode:

Start Dynamo with trace sinks and the tool-event relay enabled:

Point ms-agent at the Dynamo frontend from a second shell:

Use `DYN_AGENT_TRACE_*`

variables for the Dynamo runtime and
`DYN_AGENT_*`

variables for the ms-agent harness process.

The fork automatically attaches `nvext.agent_context`

and `x-request-id`

to
ms-agent OpenAI-compatible LLM calls while an agent context is active. When
`DYN_AGENT_TOOL_EVENTS_ZMQ_ENDPOINT`

is set, the ms-agent CLI also binds a
ZMQ PUB socket and publishes tool lifecycle records to Dynamo’s tool-event
relay. Shared tool execution paths publish directly to that root publisher;
`agent_tools`

subprocesses forward normalized tool records back to the root
process, so subprocess isolation remains enabled without each child binding the
endpoint. Python entrypoints that do not use the CLI lazily initialize the same
publisher on the first tool event.

For DeepResearch v2, keep the normal ms-agent setup: configure
`OPENAI_BASE_URL`

, `OPENAI_API_KEY`

, search keys such as `EXA_API_KEY`

, and the
model names in `projects/deep_research/v2/*.yaml`

. Then run the workflow from
the fork root:

`--trust_remote_code true`

is security-sensitive. Use it only with trusted
repositories and configs.

The CLI path captures Dynamo LLM request records through the forked ms-agent OpenAI wrappers and publishes tool events from shared ms-agent tool execution paths.

## Record Semantics

Dynamo emits `request_end`

after the response stream completes or is dropped.
Nullable fields are omitted when the serving path did not record them.

Request records capture Dynamo-owned serving metrics:

Trace records do not include prompt/response content, sampling parameters, finish reason, or error status. Use the audit sink for request/response payload capture and OpenTelemetry export for span-based observability.

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