source: https://docs.nvidia.com/dynamo/agents/agent-harnesses
lastmod: 2026-09-24T19:58:16.636Z

# Agent Harnesses

Point coding-agent CLIs at a Dynamo deployment

Dynamo exposes `v1/chat/completions`

, `v1/responses`

, and `v1/messages`

, so any agent that uses these APIs can talk to a Dynamo endpoint even if it is not listed in this guide. This guide focuses on popular agent harnesses that send stable session IDs. Dynamo normalizes these IDs for tracing and other explicitly configured consumers.

### Start a local agent endpoint

To locally test these out, we have a small script that runs an SGLang-backed `zai-org/GLM-4.7-Flash`

endpoint. This script starts a TP2 instance on port 8000 and enables request tracing for replay and visualization. By default traces are saved in `/tmp/dynamo-request-trace-$(date +%Y%m%d-%H%M%S)`


To start it, run: