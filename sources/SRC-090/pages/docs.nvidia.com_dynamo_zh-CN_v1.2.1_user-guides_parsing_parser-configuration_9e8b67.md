source: https://docs.nvidia.com/dynamo/zh-CN/v1.2.1/user-guides/parsing/parser-configuration
lastmod: 2026-09-23T23:30:39.914Z

# Parser Configuration

How —dyn-chat-processor, —dyn-tool-call-parser, and —dyn-reasoning-parser fit together

Dynamo turns a model’s raw tool-call and reasoning markup into structured `tool_calls`

and `reasoning_content`

. Two independent choices control how that parsing happens. This page is the single source of truth for **which flags combine and which combinations don’t make sense**. For the parser *names* themselves, follow the per-stage links at the bottom.

## The choices

**1. Who parses — --dyn-chat-processor** (a

*frontend*flag; default

`dynamo`

):`dynamo`

(default) — Dynamo’s framework-agnostic Rust parser. Works on every backend (vLLM, SGLang, TRT-LLM) and with disaggregated serving.`vllm`

/`sglang`

— delegate parsing to that engine’s own Python parser (“engine fallback”). Use only when Dynamo does not ship a parser for your model.

**2. Which parser** — the flag name *and where it goes* depend on choice 1:

## The pairing rule

- The
and go on the`--dyn-*`

parser flags pair with the`dynamo`

chat processor**worker**:`--dyn-tool-call-parser`

,`--dyn-reasoning-parser`

. - The
**bare**and go on the`--tool-call-parser`

/`--reasoning-parser`

flags pair with`vllm`

/`sglang`

**frontend**.

Tool calling and reasoning are independent — set one, the other, or both — but always from the same family as your chat processor. You never mix the two families.

## What does NOT make sense

## Examples

Default (Dynamo-native) — the common case. The same `--dyn-*`

flags work on every backend; pick one worker. The chat processor defaults to `dynamo`

, so the frontend flag is optional:

Engine fallback — only when Dynamo lacks a parser for your model. Supported on vLLM and SGLang (not TRT-LLM); the parser flags go on the **frontend** and use the engine’s own parser names:

## Parser names and per-stage details

- Tool calling:
[Tool Call Parsing (Dynamo)](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/parsing/tool-call-parsing-dynamo)(native parser names). - Reasoning:
[Reasoning Parsing (Dynamo)](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/parsing/reasoning-parsing-dynamo)(native parser names). - Engine fallback (vLLM / SGLang):
[Parser Engine Fallback](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/parsing/parser-engine-fallback). - Engine processors:
[vLLM Chat Processor](https://docs.nvidia.com/dynamo/v1.2.1/backends/v-llm/frontend-processor-fallback)and[SGLang Chat Processor](https://docs.nvidia.com/dynamo/v1.2.1/backends/sg-lang/frontend-processor-fallback). - Every frontend flag:
[Frontend Configuration Reference](https://docs.nvidia.com/dynamo/v1.2.1/components/frontend/configuration-reference).