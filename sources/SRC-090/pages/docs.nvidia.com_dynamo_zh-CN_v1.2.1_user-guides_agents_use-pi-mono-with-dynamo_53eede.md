source: https://docs.nvidia.com/dynamo/zh-CN/v1.2.1/user-guides/agents/use-pi-mono-with-dynamo
lastmod: 2026-09-23T23:30:39.914Z

Use Pi-Mono with Dynamo


Use Pi-Mono with Dynamo

[Pi-Mono](https://github.com/badlogic/pi-mono) is an open-source coding-agent harness whose clean plugin architecture has made it a popular substrate for patterns like subagents and planner/implementer loops. The [ pi-dynamo-provider](https://github.com/ai-dynamo/pi-dynamo-provider) extension uses that plugin surface to register Dynamo as a Pi model provider. It runs in-process, adds Dynamo’s

[and](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/agents/agent-tracing)

`agent_context`

[to each request, and emits Pi’s tool lifecycle events to Dynamo over ZMQ.](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/agents/agent-hints)

`agent_hints`

This page is one worked example of how to wire a harness up to Dynamo’s tracing and hint APIs — use it as a reference, not a prescription.

## Why run Pi through Dynamo

You can already point Pi at any OpenAI-compatible endpoint — Ollama, vLLM, a hosted API, or Dynamo out of the box. Routing through Dynamo *with this extension* gives you two things you don’t get from plain hosting:

**Harness-aware observability.**Pi’s session and trajectory IDs flow into Dynamo’s`request_end`

traces, and Pi’s tool spans land on the same timeline. One Perfetto view shows LLM requests, prefill/decode stages, and tool calls together.**Harness-aware orchestration.**Once Dynamo knows which trajectory a request belongs to, it can act on agent hints (priority, expected output length, speculative prefill) for smarter scheduling and KV-aware routing. That same trajectory awareness is what lets backends like[SGLang](https://docs.nvidia.com/dynamo/v1.2.1/backends/sg-lang/agentic-workloads)apply priority-based radix eviction and session-scoped KV isolation.

The integration works against any Dynamo backend — vLLM, SGLang, or TRT-LLM — without backend-specific glue.

## What the extension does

- Registers a
`dynamo`

provider in Pi:`pi --model dynamo/<model-id>`

. - Discovers models from Dynamo’s
`/v1/models`

. - Injects
`nvext.agent_context`

(session/trajectory IDs) into every chat-completion request. - Adds
`x-request-id`

when one is not already set. - Relays Pi’s
`tool_start`

/`tool_end`

/`tool_error`

events to Dynamo over ZMQ so LLM and tool spans share one trace.

## Quickstart

### 1. Install the provider

Build from source and install it into Pi:

### 2. Launch Dynamo with tracing enabled

Use the in-repo SGLang launcher (`examples/backends/sglang/launch/agg_agent.sh`

), which starts a frontend with KV routing plus one SGLang worker with streaming sessions, KV events, and reasoning/tool parsers wired up. Export the agent-trace env vars first so the worker records traces to a JSONL file and binds the ZMQ socket Pi will connect to:

By default this serves `zai-org/GLM-4.7-Flash`

on TP 2. Override with `--model-path`

/ `--tp`

if needed. See [Agent Tracing → Enable output](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/agents/agent-tracing#enable-output) for the full env-var reference. The provider works equally well against any Dynamo backend (vLLM, SGLang, TRT-LLM); the SGLang launcher is just the most batteries-included starting point.

### 3. Point Pi at Dynamo

`DYN_AGENT_SESSION_ID`

becomes the trace’s `session_id`

; if `DYN_AGENT_TRAJECTORY_ID`

is unset, Pi’s session id is used as the trajectory id.

### 4. View the trace in Perfetto

Open the result at [ui.perfetto.dev](https://ui.perfetto.dev/). You’ll see:

`dynamo.llm`

spans for each LLM request.`dynamo.llm.stage`

spans for prefill/decode when Dynamo records them.`dynamo.agent.tool`

spans for every Pi tool invocation.

## Pi environment variables

See the [provider README](https://github.com/ai-dynamo/pi-dynamo-provider) for the full variable list, aliases, and ZMQ wire format.

## Troubleshooting

## Further reading

[pi-dynamo-provider repo](https://github.com/ai-dynamo/pi-dynamo-provider)— install, scripts, and source.[Agent Tracing](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/agents/agent-tracing)— the underlying trace protocol and`request_end`

schema.[Agent Hints](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/agents/agent-hints)— per-request hints (`priority`

,`osl`

,`speculative_prefill`

) Pi-Mono can forward via`nvext.agent_hints`

.