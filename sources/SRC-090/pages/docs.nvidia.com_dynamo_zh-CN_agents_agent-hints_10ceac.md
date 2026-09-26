source: https://docs.nvidia.com/dynamo/zh-CN/agents/agent-hints
lastmod: 2026-09-24T19:58:16.636Z

# Agent Hints

Per-request serving hints for agentic workloads

Agent hints are optional per-request metadata that a harness sends under `nvext.agent_hints`

. Dynamo parses these hints in the frontend and passes them to the router and, where supported, backend runtimes.

Use hints only for serving-relevant intent. Use [session IDs](https://docs.nvidia.com/dynamo/agents/session-i-ds#session-id-inputs) for passive trace identity.

## Request Flow

The frontend parses `nvext.agent_hints`

, the router uses hints for queueing and worker selection, and supported backends use forwarded hints for engine-level scheduling and cache policy. For priority-specific semantics, see [Priority Scheduling](https://docs.nvidia.com/dynamo/agents/priority-scheduling).

## Backend Support

Backend support is runtime-specific. For SGLang flags and behavior, see [SGLang for Agentic Workloads](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/sg-lang/agents-on-sg-lang).

## Related Request Extensions

`agent_hints`

is separate from session identity:

- Session IDs are passive identity for traces and joins.
`agent_hints`

is active serving intent for routing, scheduling, and cache behavior.

Neither the presence of a session ID nor `agent_hints`

enables sticky sessions. Configure any session-aware routing policy separately.