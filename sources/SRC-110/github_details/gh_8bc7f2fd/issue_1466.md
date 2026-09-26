# [Issue #1466] perf OpenAI completions streaming response may be parsed as str, causing AttributeError

source: https://github.com/modelscope/evalscope/issues/1466
state: closed | updated: 2026-07-09T02:49:36Z
labels: 

## 正文

## 自查清单

在提交 issue 之前，请确保您已完成以下步骤:
- [x] 我已仔细阅读了[相关使用说明文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html)
- [x] 我已查看了[常见问题解答](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)
- [x] 我已搜索并查看了现有的 issues，确认这不是一个重复的问题

## 问题描述

使用 EvalScope Perf 工具压测 OpenAI-compatible /v1/completions 接口，并开启 stream=true 时，服务端返回的是 SSE 格式数据。

当前 EvalScope 在统计阶段似乎没有把 SSE/JSON 字符串响应先解析成 dict，而是直接把字符串传给 openai_api.py 里的响应解析逻辑，后续调用 response.get(...) 时会报错：

AttributeError: 'str' object has no attribute 'get'

我本地临时验证过：在 evalscope/perf/plugin/api/openai_api.py 的 parse_responses() 里，先把字符串形式的 SSE data: {...} 或普通 JSON 字符串 json.loads() 成 dict 后，压测可以正常完成。

## EvalScope 版本（必填）

v1.9.0

## 使用的工具

- [ ] Native / 原生框架
- [ ] Opencompass backend
- [ ] VLMEvalKit backend
- [ ] RAGEval backend
- [x] Perf / 模型推理压测工具
- [ ] Arena / 竞技场模式

## 执行的代码或指令

使用的 wrapper 内部调用 evalscope.perf.main.run_perf_benchmark，核心参数如下：

    from evalscope.perf.main import run_perf_benchmark
    from evalscope.perf.arguments import Arguments

    task_cfg = Arguments(
        parallel=[1],
        number=[1],
        model="DeepSeek-V4-Flash-DSpark",
        url="http://172.31.0.130:8080/v1/completions",
        api="openai",
        dataset="random",
        min_tokens=None,
        max_tokens=256,
        min_prompt_length=256,
        max_prompt_length=256,
        tokenizer_path="/data2/models/DeepSeek-V4-Flash",
        apply_chat_template=False,
        stream=True,
        temperature=0.0,
        extra_args={"ignore_eos": True},
        seed=42,
    )

    run_perf_benchmark(task_cfg)

请求发往 OpenAI-compatible completions 接口：

    POST http://172.31.0.130:8080/v1/completions

请求体中确认包含：

    {
      "model": "DeepSeek-V4-Flash-DSpark",
      "max_tokens": 256,
      "stream": true,
      "temperature": 0.0,
      "ignore_eos": true
    }

## 错误日志

关键错误如下：

    Exception in async function 'statistic_benchmark_metric': 'str' object has no attribute 'get'
    Traceback (most recent call last):
      File ".../evalscope/perf/utils/handler.py", line 84, in async_wrapper
        return await func(*args, **kwargs)
      File ".../evalscope/perf/core/metrics_consumer.py", line 103, in statistic_benchmark_metric
        accumulator.update(benchmark_data, api_plugin)
      File ".../evalscope/perf/utils/benchmark_util.py", line 214, in update
        data.finalize(api_plugin)
      File ".../evalscope/perf/utils/benchmark_util.py", line 88, in finalize
        self.prompt_tokens, self.completion_tokens = api_plugin.parse_responses(
      File ".../evalscope/perf/plugin/api/openai_api.py", line 190, in parse_responses
        self.__process_response_object(response, delta_contents)
      File ".../evalscope/perf/plugin/api/openai_api.py", line 198, in __process_response_object
        if not response.get('choices'):
    AttributeError: 'str' object has no attribute 'get'

Debug 日志中可以看到服务端返回的是 SSE 字符串，例如：

    data: {"id":"cmpl-xxx","object":"text_completion","created":...,"model":"DeepSeek-V4-Flash-DSpark","choices":[...]}
    ...
    data: {"id":"cmpl-xxx","object":"text_completion","choices":[],"usage":{"prompt_tokens":256,"total_tokens":512,"completion_tokens":256}}
    data: [DONE]

## 运行环境

- 操作系统：Ubuntu 22.04
- Python版本：Python 3.10
- EvalScope 安装方式：venv 中 pip 安装
- EvalScope 版本：1.9.0
- 后端服务：vLLM OpenAI-compatible API
- 接口类型：/v1/completions
- 是否开启 stream：是，stream=true

## 其他信息

这个问题和后端模型本身关系不大。服务端返回里包含合法的 usage 字段：

    {
      "usage": {
        "prompt_tokens": 256,
        "total_tokens": 512,
        "completion_tokens": 256
      }
    }

本地临时 workaround 是在 evalscope/perf/plugin/api/openai_api.py 的 parse_responses() 开头对 responses 做归一化：

- 如果 response 是 dict，保持不变；
- 如果 response 是普通 JSON 字符串，先 json.loads(response)；
- 如果 response 是 SSE 字符串，逐行解析 data: {...}，跳过 data: [DONE]。

这样 stream=true 下 Perf 压测可以正常完成。


## 评论 (3)

### Yunnglin · 2026-07-08

Thanks for the detailed report. This does look like a real robustness issue on the EvalScope side: `parse_responses()` should not crash when it receives a raw SSE string.

To confirm why the raw SSE string reaches the parser instead of being decoded earlier, could you please share the actual response headers from your `/v1/completions` endpoint, especially `Content-Type`? A minimal `curl -i -N` output with the first few `data:` lines would be very helpful.

In the standard path, EvalScope detects `Content-Type: text/event-stream` and parses each SSE `data: {...}` chunk into a dict before metric calculation. The traceback suggests the response may have been returned as raw text, for example due to a missing/non-standard `Content-Type` or a proxy/wrapper changing the response.

### H1W0XXX · 2026-07-08

测试时候我直接拉的vllm源码启动的router
`python3 ./vllm/examples/disaggregated/disaggregated_serving/disagg_proxy_demo.py --model DeepSeek-V4-Flash-DSpark --prefill 172.31.0.130:8000 --decode 172.31.0.123:8201 --port 8080`
可能他那个是临时用的，没有完整实现openai的协议，之前没设 text/event-stream，现在已经让ai帮我重新做了个router，用标准的openai协议就不会有这个问题了

### Yunnglin · 2026-07-09

Thanks for the update. Since this was caused by a temporary router that did not fully follow the OpenAI-compatible streaming protocol, and the issue is resolved after switching to a standard OpenAI-compatible router with Content-Type: text/event-stream, I will close this issue for now. Feel free to reopen it if the same problem occurs with a compliant OpenAI-compatible endpoint.
