source: https://docs.nvidia.com/dynamo/zh-CN/agents/overview
lastmod: 2026-09-24T19:58:16.636Z

# Agents

Agent-aware serving features in Dynamo

NVIDIA Dynamo adds agent-aware serving features without taking ownership of the agent loop: your harness still manages prompts, tools, subagents, and reasoning state, while Dynamo uses metadata attached to each LLM request to correlate work, improve routing and scheduling, manage KV cache behavior, and produce traces for replay and analysis.

## Send Your First Agent Request

Session IDs identify work for tracing and opt-in consumers. Agent hints influence serving behavior. Neither enables sticky placement unless a separate routing policy is configured.

## Choose Your Metadata

See [Session IDs](https://docs.nvidia.com/dynamo/agents/session-i-ds#session-id-inputs) and [Agent Hints](https://docs.nvidia.com/dynamo/agents/agent-hints) for the full contract.

## Implementation Checklist

### Configure a packaged harness when available

Point Codex, Pi, Claude Code, or another supported CLI at Dynamo. Supported harnesses emit native session headers, so you do not need to add `X-Dynamo-Session-ID`

yourself. See [Agent Harnesses](https://docs.nvidia.com/dynamo/agents/agent-harnesses).

### Identify agent sessions from a custom client

If you are building a custom client instead of using a packaged harness, send `X-Dynamo-Session-ID`

on every request in a reasoning chain. See [Session IDs](https://docs.nvidia.com/dynamo/agents/session-i-ds).

### Add agent hints when serving intent matters

Set `nvext.agent_hints`

only when you want router or engine behavior to change for that request. See [Agent Hints](https://docs.nvidia.com/dynamo/agents/agent-hints).

### Enable tracing if you need measurements

Set `DYN_REQUEST_TRACE=1`

on the frontend to capture timing, tool calls, and session identity. See [Agent Tracing](https://docs.nvidia.com/dynamo/agents/agent-tracing).