source: https://docs.nvidia.com/dynamo/v1.2.1/user-guides/parsing/tool-call-parsing-dynamo
lastmod: 2026-09-24T19:58:16.636Z

Tool Call Parsing (Dynamo)


Tool Call Parsing (Dynamo)

Connect Dynamo to external tools and services using Dynamo’s built-in tool call parsers

You can connect Dynamo to external tools and services using tool calling. By providing a list of available functions, Dynamo can choose to output function arguments for the relevant function(s) which you can execute to augment the prompt with relevant external information.

Tool calling is controlled using the `tool_choice`

and `tools`

request
parameters.

This page covers parser names for the default Dynamo-native path. If Dynamo
does not list a parser for your model, see
[Parser Engine Fallback](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/parsing/parser-engine-fallback). For how
`--dyn-tool-call-parser`

combines with `--dyn-chat-processor`

and
`--dyn-reasoning-parser`

(and which combinations are invalid), see
[Parser Configuration](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/parsing/parser-configuration).

## Prerequisites

To enable this feature, you should set the following flag while launching the backend worker

`--dyn-tool-call-parser`

: select the tool call parser from the supported list below

If your model’s default chat template doesn’t support tool calling, but the model itself does, you can specify a custom chat template per worker
with `python -m dynamo.<backend> --custom-jinja-template </path/to/template.jinja>`

.

If your model also emits reasoning content that should be separated from normal output, see [Reasoning Parsing (Dynamo)](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/parsing/reasoning-parsing-dynamo) for the supported `--dyn-reasoning-parser`

values.

## Supported Tool Call Parsers

The table below lists the currently supported tool call parsers in Dynamo’s registry. The
**Upstream name** column shows where the vLLM or SGLang parser name differs
from Dynamo’s — relevant when using `--dyn-chat-processor vllm`

or `sglang`

(see [Parser Engine Fallback](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/parsing/parser-engine-fallback)). A blank upstream
column means the same name works everywhere. `Dynamo-only`

means no upstream
parser exists for this format.

For Kimi K2.5 thinking models, pair `--dyn-tool-call-parser kimi_k2`

with
`--dyn-reasoning-parser kimi_k25`

from [Reasoning Parsing (Dynamo)](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/parsing/reasoning-parsing-dynamo) so that both `<think>`

blocks and tool calls
are parsed correctly from the same response.

## Examples

### Launch Dynamo Frontend and Backend

### Tool Calling Request Example

Dynamo parses the tool calls out of the model output and surfaces them as
OpenAI-compatible `tool_calls`

entries on the response:

If a tool call comes back wrong, add `"logprobs": true`

to a single repro
request and share the response. See
[Troubleshooting Tool Calls](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/parsing/troubleshooting-tool-calls) for what to capture and
include when reporting an issue.

## Optional: structural tags

You can optionally turn on **xgrammar structural tags** so guided decoding matches the parser’s tool-call format at token granularity. See [Structural tag (guided decoding for tool calls)](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/parsing/structural-tag.md).