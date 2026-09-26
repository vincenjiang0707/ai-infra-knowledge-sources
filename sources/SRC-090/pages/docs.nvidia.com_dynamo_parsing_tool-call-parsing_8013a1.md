source: https://docs.nvidia.com/dynamo/parsing/tool-call-parsing
lastmod: 2026-09-24T19:58:16.636Z

Tool Call Parsing (Dynamo)


Tool Call Parsing (Dynamo)

Connect Dynamo to external tools and services using Dynamo’s built-in tool call parsers

Tool calling lets Dynamo connect models to external tools and services by returning function arguments for your application to execute. Requests use the `tool_choice`

and `tools`

parameters. This page covers Dynamo-native parsing; if your model is not listed, use [engine fallback](https://docs.nvidia.com/dynamo/parsing/chat-processors), which also explains valid combinations of `--dyn-tool-call-parser`

, `--dyn-chat-processor`

, and `--dyn-reasoning-parser`

.

## Configure Tool Calling

### Launch Dynamo Backend

Select a `--dyn-tool-call-parser`

that matches your model based on the list below. The backend can be SGLang, TensorRT-LLM, vLLM, or another installed backend.

To inspect the available worker flags, run:

The following example starts an SGLang worker for Qwen3.5:

If the model supports tool calling but its default chat template does not, add `--custom-jinja-template /path/to/template.jinja`

to the worker command. The template must be readable inside the container.

If the model emits reasoning content that should be separated from normal output, see [Reasoning Parsing (Dynamo)](https://docs.nvidia.com/dynamo/parsing/reasoning-parsing) for supported `--dyn-reasoning-parser`

values.

### Send a Tool-Calling Request

Send an OpenAI-compatible chat completion request with the available tools:

Dynamo parses the model output and returns OpenAI-compatible `tool_calls`

.

###### View an example response


If a tool call is parsed incorrectly, add `"logprobs": true`

to one reproduction request and share the response. See [Troubleshooting Tool Calls](https://docs.nvidia.com/dynamo/parsing/troubleshooting-tool-calls) for what to capture when reporting an issue.

## Supported Tool Call Parsers

Choose a model family, then expand the matching model option to see its parser name and configuration details.

The **Upstream name** column shows where the vLLM or SGLang parser name differs from Dynamo’s — relevant when using `--dyn-chat-processor vllm`

or `sglang`

(see [Parser Engine Fallback](https://docs.nvidia.com/dynamo/parsing/chat-processors)). A blank upstream column means the same name works everywhere. `Dynamo-only`

means no upstream parser exists for this format.

###### Kimi


###### Kimi K2 Instruct/Thinking and Kimi K2.5


**Parser:** `kimi_k2`


**Upstream name:** Same name across Dynamo, vLLM, and SGLang

**Notes:** Pair with `--dyn-reasoning-parser kimi`

or `kimi_k25`

. For Kimi K2.5 thinking models, use `kimi_k25`

so `<think>`

blocks and tool calls are parsed from the same response. See [Reasoning Parsing (Dynamo)](https://docs.nvidia.com/dynamo/parsing/reasoning-parsing).

###### MiniMax


###### MiniMax M2 and M2.1


**Parser:** `minimax_m2`


**Upstream name:** vLLM: `minimax_m2`


**Notes:** XML `<minimax:tool_call>`


###### MiniMax M3


**Parser:** `minimax_m3`


**Upstream name:** vLLM: `minimax_m3`


**Notes:** MiniMax namespace-token XML

###### DeepSeek


###### DeepSeek V4 Pro / Flash


**Parser:** `deepseek_v4`


**Upstream name:** vLLM: `deepseek_v4`

; SGLang: `deepseekv4`


**Notes:** DSML tags (`<｜DSML｜tool_calls>...`

). Aliases: `deepseek-v4`

, `deepseekv4`


###### DeepSeek V3 and DeepSeek R1-0528+


**Parser:** `deepseek_v3`


**Upstream name:** SGLang: `deepseekv3`


**Notes:** Special Unicode markers

###### DeepSeek V3.1


**Parser:** `deepseek_v3_1`


**Upstream name:** Dynamo-only

**Notes:** JSON separators

###### DeepSeek V3.2+


**Parser:** `deepseek_v3_2`


**Upstream name:** Dynamo-only

**Notes:** DSML tags (`<｜DSML｜function_calls>...`

)

###### Qwen, QwQ, and NousHermes


###### Qwen3.5 and Qwen3-Coder


**Parser:** `qwen3_coder`


**Upstream name:** Same name across Dynamo, vLLM, and SGLang

**Notes:** XML `<tool_call><function=...>`


###### Qwen2.5-*, QwQ-32B, Qwen3-Instruct, Qwen3-Think, and NousHermes-2/3


**Parser:** `hermes`


**Upstream name:** vLLM: `qwen2_5`

; SGLang: `qwen25`

(for Qwen models)

**Notes:** `<tool_call>`

JSON

###### GLM


###### GLM-4.5 and GLM-4.7


**Parser:** `glm47`


**Upstream name:** Dynamo-only

**Notes:** XML `<arg_key>/<arg_value>`


###### Nemotron


###### Nemotron-Super / -Ultra / -Deci and Llama-Nemotron-Ultra / -Super


**Parser:** `nemotron_deci`


**Upstream name:** Dynamo-only

**Notes:** `<TOOLCALL>`

JSON

###### Nemotron-Nano


**Parser:** `nemotron_nano`


**Upstream name:** Dynamo-only

**Notes:** Alias for `qwen3_coder`


###### Gemma


###### Google Gemma 4 thinking models


**Parser:** `gemma4`


**Upstream name:** vLLM: `gemma4`


**Notes:** Custom non-JSON grammar with `<\|"\|>`

string delimiters and `<\|tool_call>...<tool_call\|>`

markers. Aliases: `gemma-4`

. Pair with `--dyn-reasoning-parser gemma4`

and `--custom-jinja-template examples/chat_templates/gemma4_tool.jinja`

.

###### gpt-oss


###### gpt-oss-20b and gpt-oss-120b


**Parser:** `harmony`


**Upstream name:** Dynamo-only

**Notes:** Harmony channel format

###### Phi


###### Phi-4, Phi-4-mini, and Phi-4-mini-reasoning


**Parser:** `phi4`


**Upstream name:** vLLM: `phi4_mini_json`


**Notes:** `functools[...]`

JSON

###### Llama


###### Llama 4 Scout / Maverick


**Parser:** `pythonic`


**Upstream name:** Same name across Dynamo, vLLM, and SGLang

**Notes:** Python-list tool syntax

###### Llama 3 / 3.1 / 3.2 / 3.3 Instruct


**Parser:** `llama3_json`


**Upstream name:** Same name across Dynamo, vLLM, and SGLang

**Notes:** `<\|python_tag\|>`

tool syntax

###### Mistral


###### Mistral, Mixtral, Mistral-Nemo, and Magistral


**Parser:** `mistral`


**Upstream name:** Same name across Dynamo, vLLM, and SGLang

**Notes:** `[TOOL_CALLS]...[/TOOL_CALLS]`


###### Jamba


###### Jamba 1.5 / 1.6 / 1.7


**Parser:** `jamba`


**Upstream name:** Dynamo-only

**Notes:** `<tool_calls>`

JSON

###### Fallback


###### Default parser


**Parser:** `default`


**Upstream name:** Dynamo-only

**Notes:** Empty JSON config (no start/end tokens). Prefer a model-specific parser for production use.

You can enable **xgrammar structural tags** so guided decoding matches the parser’s tool-call format at token granularity. See [Structural Tag (Guided Decoding for Tool Calls)](https://docs.nvidia.com/dynamo/parsing/structural-tag).