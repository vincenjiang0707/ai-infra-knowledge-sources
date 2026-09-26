source: https://docs.nvidia.com/dynamo/v1.1.1/backends/sg-lang/chat-processor
lastmod: 2026-09-24T19:58:16.636Z

# SGLang Chat Processor

SGLang-native preprocessing and postprocessing for chat completions

The SGLang chat processor enables SGLang-native preprocessing and postprocessing in the Dynamo frontend. It uses SGLang’s tokenizer, chat templates, tool call parser, and reasoning parser directly — bypassing the default Rust preprocessor for `v1/chat/completions`

requests.

## When to Use

Use `--dyn-chat-processor sglang`

when Dynamo’s built-in Rust preprocessor does not yet support a tool call parser or reasoning parser you need. The SGLang processor delegates to SGLang’s Python implementations, so any parser SGLang supports works immediately.

Common cases:

- A
**tool call format**not yet in the Rust`tool_calling`

library - A
**reasoning parser**not yet supported natively - A
**chat template**that the Rust preprocessor doesn’t handle correctly

If the parser you need is missing from the Rust preprocessor, consider [opening an issue or PR](https://github.com/ai-dynamo/dynamo/issues) to add native support — native parsers avoid the Python GIL overhead entirely.

## Quick Start

## Frontend Arguments

These arguments are passed to the **frontend** (not the worker) when using `--dyn-chat-processor sglang`

:

### Environment Variables

## Tool Calling

The processor supports all SGLang tool call formats. Pass `--tool-call-parser`

on the frontend:

Any parser supported by SGLang can be used. See the [SGLang documentation](https://docs.sglang.ai/) for the full list of available tool call parsers.

### Example: Tool Call Request

Response:

## Reasoning Parsing

For models that produce chain-of-thought reasoning (e.g., Qwen3, DeepSeek-R1), pass `--reasoning-parser`

:

The parser separates think tag content into the `reasoning_content`

field and regular content into the `content`

field.

## Migration from `--use-sglang-tokenizer`


`--use-sglang-tokenizer`

on the **worker** is deprecated. Replace with `--dyn-chat-processor sglang`

on the **frontend**:

Key differences:

## See Also

: General tool calling guide[Tool Calling](https://docs.nvidia.com/dynamo/v1.1.1/agents/tool-calling.md): Full SGLang backend reference[Reference Guide](https://docs.nvidia.com/dynamo/v1.1.1/backends/sg-lang/reference-guide): Priority scheduling and cache pinning for agents[Agentic Workloads](https://docs.nvidia.com/dynamo/v1.1.1/user-guides/agents/sg-lang-for-agentic-workloads)