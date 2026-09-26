source: https://docs.nvidia.com/dynamo/v1.3.0/user-guides/parsing/reasoning-parsing-dynamo
lastmod: 2026-09-24T19:58:16.636Z

Reasoning Parsing (Dynamo)


Reasoning Parsing (Dynamo)

Configure Dynamo’s built-in reasoning parsers for models that emit thinking content

Some models emit reasoning or thinking content separately from their final response. Dynamo can split that output into `reasoning_content`

and normal assistant content by configuring `--dyn-reasoning-parser`

on the backend worker.

This page covers parser names for the default Dynamo-native path. If Dynamo
does not list a parser for your model, see
[Parser Engine Fallback](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/parsing/parser-engine-fallback). For how
`--dyn-reasoning-parser`

combines with `--dyn-chat-processor`

and
`--dyn-tool-call-parser`

(and which combinations are invalid), see
[Parser Configuration](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/parsing/parser-configuration).

## Prerequisites

To enable reasoning parsing, launch the backend worker with:

`--dyn-reasoning-parser`

: select the reasoning parser from the supported list below

For vLLM structured output, or SGLang required/named tool choice, also configure
the engine’s native `--reasoning-parser`

. It controls when the grammar starts;
Dynamo’s parser populates `reasoning_content`

. Parser names can differ between
registries.

Some models need both a reasoning parser and a tool call parser. For supported tool call parser names, see [Tool Call Parsing (Dynamo)](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/parsing/tool-call-parsing-dynamo).

## Supported Reasoning Parsers

The table below lists the currently supported reasoning parsers in Dynamo’s registry. The
**Upstream name** column shows where the vLLM or SGLang parser name differs
from Dynamo’s. This is relevant for engine fallback and when configuring the
native structured-output reasoning gate. A blank upstream
column means the same name works everywhere. `Dynamo-only`

means no upstream
parser exists for this format.

Parsers marked **force-reasoning** emit reasoning content from token one
without requiring an explicit opening tag (`<think>`

, etc.). All others
require the opening tag to be present in the model output.

## Model-Specific Limitations

Kimi K2.7 may ignore `chat_template_kwargs.thinking=false`

and continue to
generate reasoning. Dynamo can separate emitted reasoning when a compatible
parser is configured, but it cannot force the model to disable reasoning.
Treat the request flag as best-effort for Kimi K2.7.

## Common Parser Pairings

Some models need both parsers configured together. Common pairings include:

`openai/gpt-oss-*`

:`--dyn-tool-call-parser harmony --dyn-reasoning-parser gpt_oss`

`deepseek-ai/DeepSeek-V4-*`

:`--dyn-tool-call-parser deepseek_v4 --dyn-reasoning-parser deepseek_v4`

`zai-org/GLM-4.7`

:`--dyn-tool-call-parser glm47 --dyn-reasoning-parser glm45`

`moonshotai/Kimi-K2.5*`

/ Kimi K2.6 format-compatible outputs:`--dyn-tool-call-parser kimi_k2 --dyn-reasoning-parser kimi_k25`

`google/gemma-4-*`

thinking models:`--dyn-tool-call-parser gemma4 --dyn-reasoning-parser gemma4 --custom-jinja-template examples/chat_templates/gemma4_tool.jinja`

`Qwen/Qwen3.5*`

:`--dyn-tool-call-parser qwen3_coder --dyn-reasoning-parser qwen3`

- MiniMax M2 style outputs:
`--dyn-tool-call-parser minimax_m2 --dyn-reasoning-parser minimax_m2`

- MiniMax M3 style outputs:
`--dyn-tool-call-parser minimax_m3 --dyn-reasoning-parser minimax_m3`


`minimax_append_think`

is deprecated for MiniMax M2 tool-calling deployments.
Use `--dyn-reasoning-parser minimax_m2`

with `--dyn-tool-call-parser minimax_m2`

so Dynamo can separate reasoning and pass MiniMax XML tool calls to the tool
parser.

## Tool Calling Interplay

Reasoning parsing happens before tool call parsing. If a model emits both reasoning content and tool calls, configure both parsers so Dynamo can first separate reasoning text and then parse tool calls from the remaining assistant output.

## Examples

### Launch Dynamo Frontend and Backend

### Reasoning Request Example

Dynamo splits the model output so the chain-of-thought lands in
`reasoning_content`

and the user-facing answer stays in `content`

: