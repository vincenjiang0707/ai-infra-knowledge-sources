source: https://docs.nvidia.com/dynamo/zh-CN/v1.1.1/user-guides/tool-calling/tool-call-parsing-engine-fallback
lastmod: 2026-09-23T23:30:39.914Z

Tool Call Parsing (Engine Fallback)


Tool Call Parsing (Engine Fallback)

Use upstream vLLM or SGLang tool-call parsers when Dynamo does not ship one

When Dynamo’s registry does not list a tool-call parser for your model, fall
back to the upstream engine’s parser via a **chat-processor swap**, which
keeps frontend tokenization and KV routing.

For Dynamo-native parsers, see [Tool Call Parsing (Dynamo)](https://docs.nvidia.com/dynamo/v1.1.1/user-guides/tool-calling/tool-call-parsing-dynamo). For
the equivalent reasoning fallback, see
[Reasoning Parsing (Engine Fallback)](https://docs.nvidia.com/dynamo/v1.1.1/user-guides/reasoning/reasoning-parsing-engine-fallback).

**Known Issue:** Engine-fallback tool call parsing does not currently work
with [disaggregated serving](https://docs.nvidia.com/dynamo/v1.1.1/user-guides/disaggregated-serving)
(support coming soon). Use the [Dynamo-native tool call parser](https://docs.nvidia.com/dynamo/v1.1.1/user-guides/tool-calling/tool-call-parsing-dynamo)
for disaggregated deployments today.

## Configurations

`--dyn-tool-call-parser`

selects the **Dynamo-native** parser path, while
`--tool-call-parser`

selects the **engine fallback** (vLLM or SGLang)
parser path. The accepted values for each flag come from a different
registry and may differ slightly based on the definitions from each
framework (e.g., SGLang’s `deepseekv3`

vs Dynamo’s `deepseek_v3`

).

## Examples

If a tool call comes back wrong, add `"logprobs": true`

to a single repro
request and share the response. See
[Troubleshooting Tool Calls](https://docs.nvidia.com/dynamo/v1.1.1/user-guides/tool-calling/troubleshooting-tool-calls) for what to capture and
include when reporting an issue.

## See Also

[Troubleshooting Tool Calls](https://docs.nvidia.com/dynamo/v1.1.1/user-guides/tool-calling/troubleshooting-tool-calls)— capture raw model output with`logprobs`

so tool-call issues can be localized[Tool Call Parsing (Dynamo)](https://docs.nvidia.com/dynamo/v1.1.1/user-guides/tool-calling/tool-call-parsing-dynamo)— Dynamo-native parsers and request examples[Reasoning Parsing (Engine Fallback)](https://docs.nvidia.com/dynamo/v1.1.1/user-guides/reasoning/reasoning-parsing-engine-fallback)— Equivalent fallback for reasoning[vLLM Chat Processor](https://docs.nvidia.com/dynamo/v1.1.1/backends/v-llm/frontend-processor-fallback)— vLLM chat-processor details[SGLang Chat Processor](https://docs.nvidia.com/dynamo/v1.1.1/backends/sg-lang/chat-processor)— SGLang chat-processor details[Frontend Configuration Reference](https://docs.nvidia.com/dynamo/v1.1.1/user-guides/components/frontend/configuration.md)— Full CLI flag reference