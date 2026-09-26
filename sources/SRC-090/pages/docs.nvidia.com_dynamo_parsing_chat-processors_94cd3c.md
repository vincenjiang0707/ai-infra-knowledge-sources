source: https://docs.nvidia.com/dynamo/parsing/chat-processors
lastmod: 2026-09-24T19:58:16.636Z

# Chat Processors

Pick who parses model output — the dynamo default, or vLLM/SGLang engine fallback

Every request to `/v1/chat/completions`

is handled by a **chat processor**. It renders the chat template, tokenizes, routes to the worker, assembles the OpenAI-compatible response, and — for the formats it supports — parses tool calls and reasoning out of the model’s raw output.

You have three options, selected with the `--dyn-chat-processor`

**Frontend** flag (env var `DYN_CHAT_PROCESSOR`

):

— Dynamo’s framework-agnostic Rust processor. It works on every backend (vLLM, SGLang, TRT-LLM), supports disaggregated serving, and ships built-in parsers for a broad set of model formats.`dynamo`

(default)**Use this whenever Dynamo has a parser for your model**— which is most of the time.— hand parsing back to the engine’s own Python parser. Use these`vllm`

/`sglang`

(engine fallback)**only**when Dynamo does not ship a parser for your model’s format.

All three keep Dynamo’s tokenization, routing, and disaggregated serving — the only thing that changes is who runs the parser. Your choice also decides the parser flag names and which component carries them; the tabs below show exactly where they go.

New here? Read the [Overview](https://docs.nvidia.com/dynamo/parsing/overview) first for how the chat processor relates to the tool-call and reasoning parsers.

## Configuration

###### dynamo (default)

###### vLLM

###### SGLang

**Use this whenever Dynamo has a parser for your model.** Leave `--dyn-chat-processor`

unset (it defaults to `dynamo`

). Put the parser flags on the **worker** as `--dyn-tool-call-parser`

/ `--dyn-reasoning-parser`

, using names from Dynamo’s registry. The same worker flags work on vLLM, SGLang, or TRT-LLM.

For the parser names, see [Tool Call Parsing](https://docs.nvidia.com/dynamo/parsing/tool-call-parsing) and [Reasoning Parsing](https://docs.nvidia.com/dynamo/parsing/reasoning-parsing).

Engine fallback is supported on vLLM and SGLang only. TRT-LLM engine fallback is a work in progress — on a TRT-LLM worker, keep the default `dynamo`

chat processor.

## See Also

[Overview](https://docs.nvidia.com/dynamo/parsing/overview)— how the chat processor, tool-call parser, and reasoning parser fit together[Tool Call Parsing](https://docs.nvidia.com/dynamo/parsing/tool-call-parsing)— Dynamo-native tool-call parser names[Reasoning Parsing](https://docs.nvidia.com/dynamo/parsing/reasoning-parsing)— Dynamo-native reasoning parser names[vLLM Chat Processor](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/chat-processor)/[SGLang Chat Processor](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/sg-lang/chat-processor)— engine-fallback processor details and engine parser names[Frontend Configuration Reference](https://docs.nvidia.com/dynamo/reference/components/frontend-configuration)— full CLI flag reference