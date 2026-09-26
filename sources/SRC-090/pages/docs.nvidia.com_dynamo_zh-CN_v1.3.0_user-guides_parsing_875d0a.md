source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/user-guides/parsing
lastmod: 2026-09-23T23:30:39.914Z

Tool Calling & Reasoning Parsing


Tool Calling & Reasoning Parsing

Parse tool calls and reasoning out of model output into OpenAI-compatible tool_calls and reasoning_content

Dynamo parses tool-call and reasoning markup out of raw model output and surfaces it as OpenAI-compatible `tool_calls`

and `reasoning_content`

on the response. Tool calling is controlled by the `tool_choice`

and `tools`

request parameters; reasoning parsing is enabled per-model with a reasoning parser.

There are two ways to parse, depending on whether the parser lives in Dynamo’s own registry or in an upstream engine frontend (`vllm serve`

, `sglang serve`

, or `trtllm-serve`

).

## Choose a parsing path

Start with the Dynamo path. Fall back to the engine path only when Dynamo’s registry doesn’t list a parser for your model. For exactly which flags combine and which combinations don’t make sense, see [Parser Configuration](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/parsing/parser-configuration).

## Why Dynamo parses in the frontend

In `vllm serve`

, `sglang serve`

, and `trtllm-serve`

, tool-call and reasoning parsing happen in each engine’s own frontend, with subtle behavioral differences across them. For performance, Dynamo orchestrates routing and tokenization and passes tokens directly to each engine, bypassing the engine’s OpenAI server to avoid duplicate work per request. So Dynamo implements parsing in its frontend as a framework-agnostic Rust layer — one tested OpenAI-compatible contract across vLLM, SGLang, and TRT-LLM, on a hot path that stays concurrent without a Python GIL bottleneck. The `vllm`

/`sglang`

chat processors (engine fallback) opt back into the engine’s own parser when Dynamo doesn’t ship one for your model.

## See Also

[Parser Configuration](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/parsing/parser-configuration)— which flags combine, and which combinations don’t make sense[Tool Call Parsing (Dynamo)](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/parsing/tool-call-parsing-dynamo)/[Reasoning Parsing (Dynamo)](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/parsing/reasoning-parsing-dynamo)— Dynamo-native parser names[Parser Engine Fallback](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/parsing/parser-engine-fallback)— upstream vLLM / SGLang parsers[Tool Calling Probe Snapshot for Dynamo 1.2](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/parsing/tool-calling-probe-snapshot-for-dynamo-1-2)— static release-readiness probe results[Troubleshooting Tool Calls](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/parsing/troubleshooting-tool-calls)— capture`logprobs`

so issues can be localized[Frontend Configuration Reference](https://docs.nvidia.com/dynamo/v1.3.0/components/frontend/configuration-reference)— full CLI flag reference