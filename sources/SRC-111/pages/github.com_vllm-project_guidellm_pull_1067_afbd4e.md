source: https://github.com/vllm-project/guidellm/pull/1067

# feat: add OrcaRouter HTTP backend - #1067

[nissrin2020ali-ux](https://github.com/nissrin2020ali-ux)wants to merge 1 commit into

[nissrin2020ali-ux](https://github.com/nissrin2020ali-ux) wants to merge 1 commit into

[nissrin2020ali-ux](https://github.com/nissrin2020ali-ux)wants to merge 1 commit into

## Conversation

Add a first-class `orcarouter_http` backend that mirrors the existing `openai_http` backend and targets the OrcaRouter API, an OpenAI-compatible AI gateway. OrcaRouter exposes a provider/model namespace across many models with adaptive routing and automatic failover, so users can benchmark through it directly instead of configuring an anonymous custom base URL. The backend reuses the OpenAI-compatible request machinery, specializes the validation probe to the `/v1/models` endpoint (OrcaRouter has no `/health` route), and defaults the model to `orcarouter/auto` when none is configured. Documentation and unit tests are included. Generated-by: Claude Signed-off-by: nissrin2020ali-ux <nissrin2020ali-ux@users.noreply.github.com>

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

I like to see that it's reusing a lot of the existing HTTP backend, but I'm curious what made it so that separating it out was worth it. The main things I see is you overrode the validation method and added a new default model.


**reviewed**

[sjmonson](https://github.com/sjmonson)Sep 3, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Yeah aside from offering some offering some better defaults for this use-case I don't see the reason to have this as a separate backend.

|
Thanks To answer the "why a separate backend" question directly: the request path is 100% reused.
The new args schema exists mainly to give those two defaults a home (default target + default model); everything else (streaming, request formats, extras, timeouts, auth) is inherited unchanged. That's why the delta is small — it is, by design. If you'd still rather not add a backend kind for this, I'm happy to instead make those two hard-coded bits configurable on |

### This branch has not been deployed

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

GuideLLM lets teams benchmark real-world LLM workloads against OpenAI-compatible endpoints — but until now, benchmarking a hosted gateway meant treating it as an anonymous custom

`openai_http`

base URL. This PR addsorcarouter_httpas a first-class backend, mirroring how GuideLLM already treats OpenAI-compatible HTTP servers, so users of the platform can point a benchmark at OrcaRouter directly and get the gateway's full provider/model namespace out of the box.## Details

OrcaRouter is an OpenAI-compatible AI gateway built for both models and agents. Like OpenRouter, it exposes a provider/model namespace across many models — but it also combines adaptive routing, automatic failover, zero-markup inference, observability, guardrails, and agent-tool governance behind the same endpoint. Adding orcarouter as a first-class provider means this project's users can use that stack directly, without treating OrcaRouter as an anonymous custom base URL. It also runs gateway-level, zero-trust security for AI agents on the same endpoint — screening every prompt/response and governing every tool call on a default-deny basis, with no application code changes.

Changes:

`orcarouter_http`

backend kind registered in the`Backend`

registry, mirroring the existing`openai_http`

implementation (`src/guidellm/backends/orcarouter/http.py`

).`OrcaRouterHTTPBackendArgs`

schema that extends`OpenAIHTTPBackendArgs`

, defaulting`target`

to`https://api.orcarouter.ai`

and documenting`orcarouter/*`

and provider-prefixed model identifiers (`src/guidellm/schemas/backends/orcarouter_http.py`

).`/health`

route, so`validate()`

probes the`/v1/models`

endpoint instead.`orcarouter/auto`

when none is configured — OrcaRouter routes each request to the best provider for the workload.`guidellm.backends`

and`guidellm.schemas.backends`

, plus unit tests and a docs entry in`docs/guides/backends.md`

.## Test Plan

`ruff check`

,`ruff format --check`

, and`mypy`

pass on all changed files.`tests/unit/backends`

, 516 tests), including 11 new tests for`orcarouter_http`

.`lint-imports`

).`Backend.create`

→`process_startup`

→`validate`

(200 on`/v1/models`

) →`resolve`

returned a chat completion from`orcarouter/auto`

.I'm an engineer on the OrcaRouter team.

Discord: discord.gg/YEubt8enRA · X: https://x.com/OrcaRouter

## Use of AI

## git log

commit

e95d4c2Author: nissrin2020ali-ux nissrin2020ali-ux@users.noreply.github.com

Date: Mon Aug 31 13:02:51 2026 +0000

Generated-by: Claude

Signed-off-by: nissrin2020ali-ux nissrin2020ali-ux@users.noreply.github.com