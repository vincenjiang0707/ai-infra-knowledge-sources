source: https://docs.nvidia.com/dynamo/zh-CN/v1.2.1/backends/v-llm/frontend-processor-fallback
lastmod: 2026-09-23T23:30:39.914Z

# vLLM Chat Processor

vLLM-native preprocessing and postprocessing for chat completions

The vLLM chat processor enables vLLM-native preprocessing and postprocessing in the Dynamo frontend. It uses vLLM’s tokenizer, chat templates, tool call parser, and reasoning parser directly — bypassing the default Rust preprocessor for `v1/chat/completions`

requests.

## When to Use

Use `--dyn-chat-processor vllm`

when Dynamo’s built-in Rust preprocessor does not yet support a tool call parser or reasoning parser you need. The vLLM processor delegates to vLLM’s Python implementations, so any parser vLLM supports works immediately.

Common cases:

- A
**tool call format**not yet in the Rust`tool_calling`

library - A
**reasoning parser**not yet supported natively - A
**chat template**that the Rust preprocessor doesn’t handle correctly

If the parser you need is missing from the Rust preprocessor, consider [opening an issue or PR](https://github.com/ai-dynamo/dynamo/issues) to add native support — native parsers avoid the Python GIL overhead entirely.

## Quick Start

## Frontend Arguments

These arguments are passed to the **frontend** (not the worker) when using `--dyn-chat-processor vllm`

. The frontend forwards unknown arguments to vLLM’s own CLI parser (`AsyncEngineArgs`

and `FrontendArgs`

), so any vLLM frontend or engine flag is accepted.

### Environment Variables

## Tool Calling

The processor supports all vLLM tool call formats. Pass `--tool-call-parser`

(and typically `--enable-auto-tool-choice`

) on the frontend:

Any parser supported by vLLM can be used. See the [vLLM documentation](https://docs.vllm.ai/) for the full list of available tool call parsers.

### Example: Tool Call Request

Response:

## Reasoning Parsing

For models that produce chain-of-thought reasoning (e.g., Qwen3, DeepSeek-R1), pass `--reasoning-parser`

:

The parser separates think tag content into the `reasoning_content`

field and regular content into the `content`

field.

## See Also

: General tool calling guide[Tool Calling](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/parsing/tool-call-parsing-dynamo): Full vLLM backend reference[Reference Guide](https://docs.nvidia.com/dynamo/v1.2.1/backends/v-llm/reference-guide): vLLM deployment examples[Examples](https://docs.nvidia.com/dynamo/v1.2.1/backends/v-llm/examples)