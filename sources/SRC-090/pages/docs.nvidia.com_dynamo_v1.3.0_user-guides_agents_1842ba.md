source: https://docs.nvidia.com/dynamo/v1.3.0/user-guides/agents
lastmod: 2026-09-24T19:58:16.636Z

# Agents

Agent-aware serving features in Dynamo

NVIDIA Dynamo optimizes agent workloads with lightweight headers and request extensions for the router, inference engine, and KV cache manager. The harness remains responsible for agent semantics, while Dynamo uses request metadata for observability, replay, routing, priority, and cache-aware serving.

The common identity concept is `session_id`

: one stable ID for one agent reasoning/tool chain. Dynamo maps supported coding-agent headers to `session_id`

, and custom harnesses can send `X-Dynamo-Session-ID`

directly. The ID is passive metadata: it does not enable sticky sessions or session-aware routing. A routing policy must opt in to use it. See [Session IDs](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/agents/session-i-ds#session-id-inputs) for the exact contract.

## Documentation

## Request Surface

Agent session identity is header-only. Agent-facing body metadata under `nvext`

is for hints and controls.

Use session IDs when you want traceability across LLM calls, tool calls, and external trajectory files. Use `agent_hints`

when you want to influence serving behavior at the router and engine layer. Configure session-aware routing separately when a routing policy supports it.