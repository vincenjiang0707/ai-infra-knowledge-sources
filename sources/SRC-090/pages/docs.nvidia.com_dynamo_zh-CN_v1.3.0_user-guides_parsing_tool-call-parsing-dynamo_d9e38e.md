source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/user-guides/parsing/tool-call-parsing-dynamo
lastmod: 2026-09-23T23:30:39.914Z

工具调用解析（Dynamo）


工具调用解析（Dynamo）

使用 Dynamo 内置的工具调用解析器，将模型连接到外部工具和服务

你可以通过工具调用把 Dynamo 连接到外部工具和服务。通过提供一组可用函数，Dynamo 可以为相关函数输出函数参数，你执行这些函数后，即可用外部信息来增强提示。

工具调用由 `tool_choice`

和 `tools`

请求参数控制。

本页介绍默认的 Dynamo 原生路径的解析器名称。如果 Dynamo 未列出适用于你的模型的解析器，请参阅
[Parser Engine Fallback](https://docs.nvidia.com/dynamo/dev/user-guides/parsing/parser-engine-fallback)。关于 `--dyn-tool-call-parser`

如何与
`--dyn-chat-processor`

和 `--dyn-reasoning-parser`

组合（以及哪些组合是无效的），请参阅
[Parser Configuration](https://docs.nvidia.com/dynamo/dev/user-guides/parsing/parser-configuration)。

## 前置条件

启动后端 worker 时设置以下 flag 即可启用该功能：

`--dyn-tool-call-parser`

：从下方支持列表中选择工具调用解析器

如果你的模型默认的 chat template 不支持工具调用，但模型本身支持，你可以为每个 worker 指定自定义 chat template：
`python -m dynamo.<backend> --custom-jinja-template </path/to/template.jinja>`

。

如果你的模型还会输出需要与正常内容分离的推理内容，请参阅 [Reasoning Parsing (Dynamo)](https://docs.nvidia.com/dynamo/dev/user-guides/parsing/reasoning-parsing-dynamo) 了解支持的 `--dyn-reasoning-parser`

取值。

## 支持的工具调用解析器

下表列出 Dynamo 注册表中当前支持的工具调用解析器。**Upstream name** 列标出 vLLM 或 SGLang 的解析器名称与 Dynamo 不同之处——在使用 `--dyn-chat-processor vllm`

或 `sglang`

时（参阅 [Parser Engine Fallback](https://docs.nvidia.com/dynamo/dev/user-guides/parsing/parser-engine-fallback)）尤为相关。upstream 列为空表示同名在各处通用。`Dynamo-only`

表示该格式没有对应的上游解析器。

对于 Kimi K2.5 thinking 模型，将 `--dyn-tool-call-parser kimi_k2`

与 [Reasoning Parsing (Dynamo)](https://docs.nvidia.com/dynamo/dev/user-guides/parsing/reasoning-parsing-dynamo) 中的 `--dyn-reasoning-parser kimi_k25`

配对，以便从同一响应中正确解析 `<think>`

块和工具调用。

## 示例

### 启动 Dynamo Frontend 和 Backend

### 工具调用请求示例

Dynamo 会从模型输出中解析出工具调用，并在响应中以兼容 OpenAI 的 `tool_calls`

形式呈现。

如果工具调用返回结果不正确，请向单个复现请求添加 `"logprobs": true`

并分享响应。有关报告问题时需要捕获和包含的内容，请参阅
[工具调用故障排查](https://docs.nvidia.com/dynamo/dev/user-guides/parsing/troubleshooting-tool-calls)。

## 可选：结构化标签（structural tags）

你可以启用 **xgrammar 结构化标签**，让引导式解码在 token 粒度上匹配解析器的工具调用格式。参阅 [Structural tag (guided decoding for tool calls)](https://github.com/ai-dynamo/dynamo/blob/5f62ed542a20c273d38555a294dbebe0bd1bddb4/docs/tool-calling/structural-tag.md)。