source: https://docs.nvidia.com/dynamo/parsing/reasoning-parsing
lastmod: 2026-09-24T19:58:16.636Z

Reasoning Parsing (Dynamo)


Reasoning Parsing (Dynamo)

Configure Dynamo’s built-in reasoning parsers for models that emit thinking content

Some models emit reasoning separately from their final response. Dynamo can split that output into `reasoning_content`

and normal assistant `content`

by configuring `--dyn-reasoning-parser`

on the backend worker. This page covers Dynamo-native parsing; if your model is not listed, use [engine fallback](https://docs.nvidia.com/dynamo/parsing/chat-processors), which also explains valid combinations of `--dyn-reasoning-parser`

, `--dyn-chat-processor`

, and `--dyn-tool-call-parser`

.

## Configure Reasoning Parsing

### Launch Dynamo backend

Select `--dyn-reasoning-parser`

from the supported list below. The backend can be SGLang, TensorRT-LLM, vLLM, or another installed backend.

For vLLM structured output or SGLang required/named tool choice, also configure the engine’s native `--reasoning-parser`

. The native parser controls when the grammar starts; Dynamo’s parser populates `reasoning_content`

. Parser names can differ between registries.

To inspect the available worker flags, run:

The following example starts an SGLang worker for Qwen3.5:

## Some models need both parsers configured together. Common pairings include:

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

is deprecated for MiniMax M2 tool-calling deployments. Use `--dyn-reasoning-parser minimax_m2`

with `--dyn-tool-call-parser minimax_m2`

so Dynamo can separate reasoning and pass MiniMax XML tool calls to the tool parser.

Reasoning parsing happens before tool call parsing. See [Tool Call Parsing (Dynamo)](https://docs.nvidia.com/dynamo/parsing/tool-call-parsing) for supported `--dyn-tool-call-parser`

values.

## Deployment-Level Thinking Default

Set `--dyn-default-thinking-mode`

on a backend worker to choose the thinking
mode used when a request does not provide one. The worker publishes the value
through model runtime metadata, and the frontend applies it while rendering the
chat template. The option works with vLLM, SGLang, and TensorRT-LLM workers.

For example, make thinking disabled by default for a Qwen3 deployment:

You can configure the same value through the environment:

Use the same setting on every worker that serves the model. When the option is unset, Dynamo preserves the model or chat template’s native default.

Thinking controls use this precedence order:

- An explicit request control
`--dyn-default-thinking-mode`

or`DYN_DEFAULT_THINKING_MODE`

- The model or chat template’s native default

Explicit request controls include root-level `thinking`

, top-level
`reasoning_effort`

, and the `thinking`

, `enable_thinking`

, `thinking_mode`

, or
`reasoning_effort`

fields in `chat_template_args`

or
`chat_template_kwargs`

.

The deployment option intentionally accepts only `enabled`

and `disabled`

.
Models that support adaptive thinking can still select it per request:

Dynamo normalizes this request to `thinking_mode=adaptive`

. Because adaptive is
an explicit request control, it takes precedence over an `enabled`

or
`disabled`

deployment default.

This option controls chat-template rendering. It does not force the inference engine or model to follow the requested mode. Models that ignore their template’s thinking control may still emit reasoning.

## Supported Reasoning Parsers

Choose a model family, then expand the matching model option to see its parser name and configuration details.

The **Upstream name** column shows where the vLLM or SGLang parser name differs from Dynamo’s. This is relevant for engine fallback and when configuring the native structured-output reasoning gate. A blank upstream column means the same name works everywhere. `Dynamo-only`

means no upstream parser exists for this format.

Parsers marked **Force-reasoning: Yes** emit reasoning content from token one without requiring an explicit opening tag such as `<think>`

. All others require the opening tag in the model output.

###### Kimi


###### Kimi K2.5 / Kimi K2.6 format-compatible thinking models


**Parser:** `kimi_k25`


**Upstream name:** Dynamo-only

**Force-reasoning:** Yes

**Notes:** `<think>...</think>`

with force-reasoning

###### Kimi K2 Instruct / Thinking with Unicode delimiters


**Parser:** `kimi`


**Upstream name:** Dynamo-only

**Force-reasoning:** No

**Notes:** `◁think▷...◁/think▷`


Kimi K2.7 may ignore `chat_template_kwargs.thinking=false`

and continue to generate reasoning. Dynamo can separate emitted reasoning when a compatible parser is configured, but it cannot force the model to disable reasoning. Treat the request flag as best-effort for Kimi K2.7.

###### MiniMax


###### MiniMax M2 / M2.5 / M2.7


**Parser:** `minimax_m2`


**Upstream name:** vLLM: `minimax_m2`


**Force-reasoning:** Yes

**Notes:** `<think>...</think>`

with force-reasoning

###### MiniMax M3


**Parser:** `minimax_m3`


**Upstream name:** vLLM: `minimax_m3`


**Force-reasoning:** No

**Notes:** `<mm:think>...</mm:think>`

; recovers a prompt-prefilled opener

###### MiniMax M2 / M2.1 (legacy)


**Parser:** `minimax_append_think`

Deprecated

**Upstream name:** Dynamo-only

**Force-reasoning:** No

**Notes:** Legacy pass-through with an implicit `<think>`

opener. Use `minimax_m2`

for MiniMax M2 tool-calling deployments.

###### DeepSeek


###### DeepSeek V4 Pro / Flash


**Parser:** `deepseek_v4`


**Upstream name:** vLLM: `deepseek_v4`

; SGLang: `deepseek-v4`


**Force-reasoning:** No

**Notes:** `<think>...</think>`

. Aliases: `deepseek-v4`

, `deepseekv4`


###### DeepSeek R1, DeepSeek V3.1, and DeepSeek V3.2


**Parser:** `deepseek_r1`


**Upstream name:** Same name across Dynamo, vLLM, and SGLang

**Force-reasoning:** Yes

**Notes:** Pass explicitly for V3.1/V3.2 (no alias)

###### Qwen and QwQ


###### Qwen3.5, QwQ-32B, Qwen3-Think, and Qwen3-Coder


**Parser:** `qwen3`


**Upstream name:** Same name across Dynamo, vLLM, and SGLang

**Force-reasoning:** No

**Notes:** `<think>...</think>`


###### GLM


###### GLM-4.5 and GLM-4.7


**Parser:** `glm45`


**Upstream name:** Dynamo-only

**Force-reasoning:** No

**Notes:** Alias for `nemotron_deci`

. `<think>...</think>`


###### Nemotron


###### Nemotron-3 / Mini


**Parser:** `nemotron3`


**Upstream name:** vLLM: `nemotron_v3`


**Force-reasoning:** Yes

**Notes:** Alias for `deepseek_r1`

. Also accepts `nemotron_v3`


###### Nemotron-Super / -Ultra / -Deci and Llama-Nemotron


**Parser:** `nemotron_deci`


**Upstream name:** Dynamo-only

**Force-reasoning:** No

**Notes:** `<think>...</think>`


###### Nemotron-Nano


**Parser:** `nemotron_nano`


**Upstream name:** Dynamo-only

**Force-reasoning:** Yes

**Notes:** Alias for `deepseek_r1`


###### Gemma


###### Google Gemma 4 thinking models


**Parser:** `gemma4`


**Upstream name:** vLLM: `gemma4`


**Force-reasoning:** No

**Notes:** `<\|channel>thought\n...<channel\|>`

with `thought\n`

role label stripped. Aliases: `gemma-4`


###### gpt-oss


###### gpt-oss-20b and gpt-oss-120b


**Parser:** `gpt_oss`


**Upstream name:** Dynamo-only

**Force-reasoning:** No

**Notes:** Harmony channel reasoning format

###### Mistral


###### Magistral


**Parser:** `mistral`


**Upstream name:** Same name across Dynamo, vLLM, and SGLang

**Force-reasoning:** Yes

**Notes:** `[THINK]...[/THINK]`


###### Granite


###### IBM Granite 3.x / Granite 3.2 language models


**Parser:** `granite`


**Upstream name:** Same name across Dynamo, vLLM, and SGLang

**Force-reasoning:** No

**Notes:** `Here's my thought process:`

/ `Here's my response:`


###### Step


###### Step-3 / Step-3-Reasoning


**Parser:** `step3`


**Upstream name:** Dynamo-only

**Force-reasoning:** Yes

**Notes:** `<think>...</think>`


###### Generic


###### Generic chain-of-thought models


**Parser:** `basic`


**Upstream name:** Dynamo-only

**Force-reasoning:** No

**Notes:** Plain `<think>...</think>`