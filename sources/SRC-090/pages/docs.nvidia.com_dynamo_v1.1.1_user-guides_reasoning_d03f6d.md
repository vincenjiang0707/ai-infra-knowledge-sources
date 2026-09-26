source: https://docs.nvidia.com/dynamo/v1.1.1/user-guides/reasoning
lastmod: 2026-09-24T19:58:16.636Z

# Reasoning

Separate reasoning content from assistant output for chain-of-thought models

Some models emit reasoning or thinking content separately from their final
response. Dynamo can split that output into `reasoning_content`

and normal
assistant content by configuring a reasoning parser. As with tool calling,
there are two ways to do this to ensure wide coverage and day0 model support.

## Choose a parsing path

Start with the Dynamo path. Fall back to the engine path only when Dynamo’s registry does not list a parser for your model.

## See Also

[Tool Calling](https://docs.nvidia.com/dynamo/v1.1.1/user-guides/tool-calling)— parse tool calls out of model output. Several models need both a reasoning parser and a tool-call parser configured together.[Frontend Configuration Reference](https://docs.nvidia.com/dynamo/v1.1.1/components/frontend/configuration.md)— full CLI flag reference.