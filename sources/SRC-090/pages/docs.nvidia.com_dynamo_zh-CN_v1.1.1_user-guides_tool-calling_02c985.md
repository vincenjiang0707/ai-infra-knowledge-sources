source: https://docs.nvidia.com/dynamo/zh-CN/v1.1.1/user-guides/tool-calling
lastmod: 2026-09-23T23:30:39.914Z

# Tool Calling

Parse tool calls from model output and surface them as OpenAI-compatible tool_calls

Dynamo can connect models to external tools and services by parsing tool-call
syntax out of raw model output and surfacing it as OpenAI-compatible
`tool_calls`

on the response. Tool calling is controlled by the `tool_choice`

and `tools`

request parameters on the chat completions API.

There are two ways to parse tool calls in Dynamo, depending on whether the parser lives in Dynamo’s own registry or in the upstream engine (vLLM, SGLang).

## Choose a parsing path

Start with the Dynamo path. Fall back to the engine path only when Dynamo’s registry does not list a parser for your model.

## Troubleshooting

If a tool call comes back wrong, add `logprobs: true`

to a single repro
request and share the response. See
[Troubleshooting Tool Calls](https://docs.nvidia.com/dynamo/v1.1.1/user-guides/tool-calling/troubleshooting-tool-calls) for what to capture and
include when reporting an issue.

## See Also

[Troubleshooting Tool Calls](https://docs.nvidia.com/dynamo/v1.1.1/user-guides/tool-calling/troubleshooting-tool-calls)— capture raw model output with`logprobs`

so tool-call issues can be localized.[Reasoning](https://docs.nvidia.com/dynamo/v1.1.1/user-guides/reasoning)— separate`reasoning_content`

from assistant content for chain-of-thought models. Several models need both a tool-call parser and a reasoning parser configured together.[Frontend Configuration Reference](https://docs.nvidia.com/dynamo/v1.1.1/components/frontend/configuration.md)— full CLI flag reference.