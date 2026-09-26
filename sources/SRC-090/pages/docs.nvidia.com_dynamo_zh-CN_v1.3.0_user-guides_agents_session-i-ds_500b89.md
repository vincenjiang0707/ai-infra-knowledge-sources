source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/user-guides/agents/session-i-ds
lastmod: 2026-09-23T23:30:39.914Z

# Session IDs

A session ID is the stable identifier Dynamo uses for one agent reasoning/tool chain. A root agent, planner, researcher subagent, or OpenCode subtask can each have its own session. Every LLM request in that chain should carry the same `session_id`

; child sessions can also carry a `parent_session_id`

so traces and replay tools can rebuild the tree. Some academic papers also call this a `program_id`

.

Session identity is passive metadata. Sending `X-Dynamo-Session-ID`

does not enable sticky sessions or change request placement. Tracing records the identity when `DYN_REQUEST_TRACE`

is enabled, and a session-aware routing policy can consume it only when that policy is configured separately.

## Session ID Inputs

Custom clients should send the canonical Dynamo headers. When `X-Dynamo-Session-ID`

is present, Dynamo uses it and `X-Dynamo-Parent-Session-ID`

instead of any agent-native identity values.

### Native Agent Headers

Dynamo also recognizes the current stable identity headers emitted by the following coding agents. The [frontend API surface compliance test](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/tests/frontend/test_frontend_api_surface_compliance.py) catches header changes as coding agents evolve.

`X-Dynamo-Session-Final`

applies with either canonical or agent-native session identity.

### Custom Agent Harnesses

For a custom HTTP client that only needs a session ID, send the generic header: