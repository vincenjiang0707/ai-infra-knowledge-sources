source: https://docs.nvidia.com/dynamo/zh-CN/v1.2.1/user-guides/parsing/parser-engine-fallback
lastmod: 2026-09-23T23:30:39.914Z

# Parser Engine Fallback

Use upstream vLLM or SGLang tool-call and reasoning parsers when Dynamo does not ship one

When Dynamo’s registry does not list a tool-call or reasoning parser for your model, fall back to the upstream engine’s parser via a **chat-processor swap**, which keeps frontend tokenization and KV routing.

For the Dynamo-native default path, see [Tool Call Parsing (Dynamo)](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/parsing/tool-call-parsing-dynamo) and [Reasoning Parsing (Dynamo)](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/parsing/reasoning-parsing-dynamo).

How `--dyn-chat-processor`

combines with the parser flags — and which combinations are invalid (engine fallback supports disaggregated serving on vLLM and SGLang; TRT-LLM engine fallback is a work in progress) — is documented once in [Parser Configuration](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/parsing/parser-configuration). Read that first; this page covers only the engine-fallback specifics.

## Configuration

Engine fallback runs parsing in the engine’s own Python frontend. Select it with `--dyn-chat-processor vllm`

or `sglang`

, then name the parser with the engine’s **frontend** flags:

`--tool-call-parser <name>`

— the engine’s tool-call parser`--reasoning-parser <name>`

— the engine’s reasoning parser

These are distinct from the Dynamo-native `--dyn-tool-call-parser`

/ `--dyn-reasoning-parser`

(which go on the worker). The accepted names come from the engine’s registry and may differ from Dynamo’s — e.g. vLLM `nemotron_v3`

vs Dynamo `nemotron3`

, SGLang `deepseekv3`

vs Dynamo `deepseek_v3`

.

## Examples

If a tool call or reasoning split comes back wrong, add `"logprobs": true`

to a single repro request and share the response. See [Troubleshooting Tool Calls](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/parsing/troubleshooting-tool-calls) for what to capture.

## See Also

[Parser Configuration](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/parsing/parser-configuration)— how the chat-processor and parser flags combine, and which combinations are invalid (start here)[Tool Call Parsing (Dynamo)](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/parsing/tool-call-parsing-dynamo)— Dynamo-native tool-call parser names[Reasoning Parsing (Dynamo)](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/parsing/reasoning-parsing-dynamo)— Dynamo-native reasoning parser names[vLLM Chat Processor](https://docs.nvidia.com/dynamo/v1.2.1/backends/v-llm/frontend-processor-fallback)— vLLM chat-processor details[SGLang Chat Processor](https://docs.nvidia.com/dynamo/v1.2.1/backends/sg-lang/frontend-processor-fallback)— SGLang chat-processor details[Frontend Configuration Reference](https://docs.nvidia.com/dynamo/v1.2.1/components/frontend/configuration-reference)— Full CLI flag reference