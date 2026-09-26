# [Issue #1119] 压测deepseek-v3.2 报错

source: https://github.com/modelscope/evalscope/issues/1119
state: closed | updated: 2026-08-11T10:03:58Z
labels: 

## 正文

## 自查清单

在提交 issue 之前，请确保您已完成以下步骤:
- [x] 我已仔细阅读了[相关使用说明文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html)
- [x] 我已查看了[常见问题解答](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)
- [x] 我已搜索并查看了现有的 issues，确认这不是一个重复的问题

## 问题描述
压测deepseek-v3.2 报错


## EvalScope 版本（必填）
v1.4

## 使用的工具
- Perf / 模型推理压测工具


## 执行的代码或指令
`evalscope perf \
  --parallel 4 \
  --model dewu-chat \
  --url http://risk-ai-platform-prd-hs-sh-deepseek-v32.prd-standard-zj-sh.shizhuang-inc.com/v1/chat/completions \
  --api openai \
  --dataset random \
  --min-tokens 128 \
  --max-tokens 128 \
  --prefix-length 64 \
  --min-prompt-length 128 \
  --max-prompt-length 128 \
  --number 500 \
  --tokenizer-path /root/workspace/models/deepseek-v3.2 \
  --debug \
  --outputs-dir "./my_output" \
  --extra-args '{"ignore_eos": true}'`


## 错误日志

`Traceback (most recent call last):
  File "/usr/local/lib/python3.10/dist-packages/evalscope/perf/utils/handler.py", line 17, in async_wrapper
    return await func(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/evalscope/perf/benchmark.py", line 166, in benchmark
    async for request in get_requests(args, api_plugin):
  File "/usr/local/lib/python3.10/dist-packages/evalscope/perf/benchmark.py", line 71, in get_requests
    async for request in generator:
  File "/usr/local/lib/python3.10/dist-packages/evalscope/perf/benchmark.py", line 42, in generate_requests_from_dataset
    for messages in message_generator.build_messages():
  File "/usr/local/lib/python3.10/dist-packages/evalscope/perf/plugin/datasets/random_dataset.py", line 98, in build_messages
    template_len = self.get_template_len()
  File "/usr/local/lib/python3.10/dist-packages/evalscope/perf/plugin/datasets/random_dataset.py", line 174, in get_template_len
    template = self.tokenizer.apply_chat_template(empty_message, tokenize=True, add_generation_prompt=True)
  File "/usr/local/lib/python3.10/dist-packages/transformers/tokenization_utils_base.py", line 1647, in apply_chat_template
    chat_template = self.get_chat_template(chat_template, tools)
  File "/usr/local/lib/python3.10/dist-packages/transformers/tokenization_utils_base.py", line 1825, in get_chat_template
    raise ValueError(
ValueError: Cannot use chat template functions because tokenizer.chat_template is not set and no template argument was passed! For information about writing templates and setting the tokenizer.chat_template attribute, please see the documentation at https://huggingface.co/docs/transformers/main/en/chat_templating`

## 运行环境

- 操作系统：ubuntu 22.04
- Python版本：3.12

## 其他信息

是不是这一版的deepseek的tokenizer_config.json 中没有 chat_template
https://huggingface.co/deepseek-ai/DeepSeek-V3.2/blob/main/tokenizer_config.json


## 评论 (7)

### Yunnglin · 2026-01-04

deepseek-v3.2 不包含Jinja格式的模板，可以尝试使用 deepseek-ai/DeepSeek-V3.1

### yonlunwu · 2026-01-13

请问 curl 是正常的，
curl http://127.0.0.1:35000/v1/chat/completions   -H "Content-Type: application/json"   -d '{
    "model": "DeepSeek-V3.2",
    "messages": [
      {"role": "user", "content": "Hello, DeepSeek-V3.2!"}
    ],
    "temperature": 0.0,
    "max_tokens": 100
  }'

问题是不是出在 evalscope 组装请求上呢？

### yangqinghao-cmss · 2026-01-28

兄弟，这个问题解决了吗，我也遇到了这个问题

### yangqinghao-cmss · 2026-01-28

> deepseek-v3.2 不包含Jinja格式的模板，可以尝试使用 deepseek-ai/DeepSeek-V3.1

不行，用的3.1的，服务报 400 BadRequest，curl命令也正常

### r4ining · 2026-03-19

> 兄弟，这个问题解决了吗，我也遇到了这个问题

试了下 这样可以

```bash
evalscope perf \
  --parallel 1 \
  --number 1 \
  --model deepseek-v3.2 \
  --url http://localhost:30000/v1/chat/completions \
  --api openai \
  --dataset random \
  --max-tokens 128 \
  --min-tokens 128 \
  --prefix-length 0 \
  --min-prompt-length 128 \
  --max-prompt-length 128 \
  --tokenizer-path deepseek-ai/DeepSeek-V3.1 \
  --extra-args '{"ignore_eos": true}'

```

### Yunnglin · 2026-03-31

> 感谢你的反馈！我们将关闭此问题。如果您有任何疑问，请随时重新打开它。如果EvalScope对您有所帮助，欢迎给我们点个STAR以示支持，谢谢！

### Yunnglin · 2026-08-11

补充：这个报错的框架侧修复已合入 main（PR #1564）。当时的根因（DeepSeek 部分权重不含 jinja chat template，`apply_chat_template()` 必然失败）现在会给出明确的失败原因和处置建议，而不是抛 transformers 的原始报错。同类问题的最新讨论见 #1548。

