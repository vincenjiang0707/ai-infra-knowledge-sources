source: https://docs.nvidia.com/dynamo/v1.3.0/user-guides/agents/agent-harnesses
lastmod: 2026-09-24T19:58:16.636Z

# Agent Harnesses

Point coding-agent CLIs at a Dynamo deployment

Dynamo exposes `v1/chat/completions`

, `v1/responses`

, and `v1/messages`

, so any agent that uses these APIs can talk to a Dynamo endpoint even if it is not listed in this guide. This guide focuses on popular agent harnesses that send stable session IDs. Dynamo normalizes these IDs for tracing and other explicitly configured consumers.

## Local Setup

To locally test these out, we have a small script that runs an SGLang-backed `zai-org/GLM-4.7-Flash`

endpoint. This script starts a TP2 instance on port 8000 and enables request tracing for replay and visualization. By default traces are saved in `/tmp/dynamo-request-trace-$(date +%Y%m%d-%H%M%S)`


To start it, run:

## Codex

Codex uses the Responses API. Add a local provider in `~/.codex/config.toml`

:

Codex sends a `session-id`

header that Dynamo maps to `session_id`

.

## Pi

Pi uses the Dynamo provider plugin. Build and install it from the [agent-plugins](https://github.com/ai-dynamo/agent-plugins/tree/main/pi-plugin) checkout:

Point it at the Dynamo OpenAI-compatible endpoint and run Pi with the `dynamo`

provider:

## Claude Code

Claude Code uses Anthropic-compatible Messages API. The local launcher above starts `dynamo.frontend`

with `--enable-anthropic-api`

; for other deployments, pass that flag when starting the frontend. Then set:

Dynamo uses `x-claude-code-session-id`

as the Claude Code session ID. For subagents, Dynamo uses `x-claude-code-agent-id`

as the child session ID. Nested subagents use `x-claude-code-parent-agent-id`

as the parent; top-level subagents fall back to the root session ID.

## OpenCode

OpenCode uses a project-local JSONC provider config; setting an endpoint env var alone is not enough. Create `.opencode/opencode.jsonc`

in the project you run OpenCode from:

Run OpenCode with the provider/model pair:

Dynamo maps OpenCode’s `x-session-id`

header to `session_id`

and `x-parent-session-id`

to `parent_session_id`

.

## OpenClaw

OpenClaw can use Dynamo through its OpenAI-compatible Responses endpoint. Install the Dynamo provider plugin:

Add a Dynamo-backed model to `~/.openclaw/openclaw.json`

:

Run OpenClaw:

The plugin copies OpenClaw’s current `sessionId`

into `x-dynamo-session-id`

on each
request. Native subagents receive their own `session_id`

and the immediate parent is
recorded as `parent_session_id`

.

## Hermes Agent

Hermes uses an OpenAI-compatible custom endpoint. Configure Hermes with the served model name and Dynamo `/v1`

base URL:

If your Dynamo endpoint requires auth, add `api_key: <token>`

to the Hermes model config or set `OPENAI_API_KEY`

.

This configuration lets you run Hermes with the `hermes`

command. To send session IDs to Dynamo, install the plugin:

The plugin copies the Hermes `session_id`

into `x-dynamo-session-id`

on each LLM request.