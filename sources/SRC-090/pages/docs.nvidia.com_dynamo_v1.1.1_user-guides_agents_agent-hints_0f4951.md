source: https://docs.nvidia.com/dynamo/v1.1.1/user-guides/agents/agent-hints
lastmod: 2026-09-24T19:58:16.636Z

# Agent Hints

Per-request serving hints for agentic workloads

Agent hints are optional per-request metadata that a harness sends under
`nvext.agent_hints`

. Dynamo parses these hints in the frontend and passes them
to the router and, where supported, backend runtimes.

Use hints only for serving-relevant intent. Use
[ nvext.agent_context](https://docs.nvidia.com/dynamo/v1.1.1/user-guides/agents/agent-tracing#request-schema) for passive trace
identity.

## Request Schema

## Request Flow

The frontend parses `nvext.agent_hints`

, the router uses hints for queueing and
worker selection, and supported backends use forwarded hints for engine-level
scheduling and cache policy.

## Backend Support

Backend support is runtime-specific. For SGLang flags and behavior, see
[SGLang for Agentic Workloads](https://docs.nvidia.com/dynamo/v1.1.1/user-guides/agents/sg-lang-for-agentic-workloads).

## Related Request Extensions

`agent_hints`

is separate from `agent_context`

:

`agent_context`

is passive identity for traces and joins.`agent_hints`

is active serving intent for routing, scheduling, and cache behavior.

Session-control metadata for SGLang subagent KV isolation lives under
`nvext.session_control`

; see [NVIDIA Request Extensions](https://docs.nvidia.com/dynamo/v1.1.1/additional-resources/nvidia-request-extensions-nvext#session-control).