source: https://docs.nvidia.com/dynamo/zh-CN/agents/session-i-ds
lastmod: 2026-09-24T19:58:16.636Z

# Session IDs

Send a session ID on every LLM request in one reasoning chain:

## Use One ID Per Reasoning Chain

Use one `session_id`

for one agent reasoning and tool-use chain. A root agent, planner, researcher subagent, or OpenCode subtask can each have its own ID. Child sessions can also send a parent ID so traces and replay tools can rebuild the tree. Some academic papers call this a `program_id`

.


## Session ID Inputs

Custom clients should send the canonical Dynamo headers. When `X-Dynamo-Session-ID`

is present, Dynamo uses it and `X-Dynamo-Parent-Session-ID`

instead of any agent-native identity values.

One reasoning or tool chain inside the run. Maps to `agent_context.session_id`

.

Parent session when using subagents. Maps to `agent_context.parent_session_id`

.

Set to `true`

on a dedicated minimal request when the session ends. Lifecycle-aware consumers can release per-session state immediately instead of waiting for an idle timeout. This works with canonical or agent-native session identity and maps to `agent_context.session_final`

.

## Native Agent Headers

Dynamo also recognizes the current stable identity headers emitted by the following coding agents. The [frontend API surface compliance test](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/tests/frontend/test_frontend_api_surface_compliance.py) catches header changes as coding agents evolve. See [Agent Harnesses](https://docs.nvidia.com/dynamo/agents/agent-harnesses) for packaged setup.

###### Claude Code

###### Codex

###### OpenCode

###### Custom client

Dynamo reads Claude Code headers and normalizes them to `session_id`

and `parent_session_id`

:

`x-claude-code-session-id`

for root turns`x-claude-code-agent-id`

for child-agent turns`x-claude-code-parent-agent-id`

for nested children; top-level children fall back to`x-claude-code-session-id`


Session identity is passive metadata. Sending a session ID does not enable sticky sessions or change request placement. Tracing records the identity when `DYN_REQUEST_TRACE=1`

is enabled, and a session-aware routing policy can consume it only when that policy is configured separately.

## Related

[Agent Harnesses](https://docs.nvidia.com/dynamo/agents/agent-harnesses)— connect supported coding-agent CLIs to Dynamo[Agent Tracing](https://docs.nvidia.com/dynamo/agents/agent-tracing)— join LLM and tool spans on`session_id`

[Agent Simulation](https://docs.nvidia.com/dynamo/agents/agent-simulation)— replay captured agent traces[ThunderAgent Program Scheduler](https://docs.nvidia.com/dynamo/agents/thunder-agent-program-scheduler)— program-level scheduling keyed by`session_id`