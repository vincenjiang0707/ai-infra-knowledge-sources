# [Issue #1506] 缓存命中显示为0

source: https://github.com/modelscope/evalscope/issues/1506
state: closed | updated: 2026-07-23T08:51:41Z
labels: 

## 正文

# [Bug] Perf OpenAI API 模式未将 real_cached_tokens 写入 cached_tokens，缓存命中统计始终为 0

## 自查清单

在提交 issue 之前，请确保您已完成以下步骤:

- [x] 我已仔细阅读了[相关使用说明文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html)
- [x] 我已查看了[常见问题解答](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)
- [x] 我已搜索并查看了现有的 issues，确认这不是一个重复的问题

## 问题描述

使用 EvalScope Perf 的 OpenAI API 模式压测 SGLang Router 时，服务端响应已经通过 OpenAI 兼容字段返回缓存命中 token：

```json
{
  "usage": {
    "prompt_tokens": 152,
    "prompt_tokens_details": {
      "cached_tokens": 128
    }
  }
}
```

EvalScope 的 `DefaultApi` 也能正确解析该字段并写入 `BenchmarkData.real_cached_tokens`，但普通单轮压测流程没有将 `real_cached_tokens` 同步到报表和 workload timeline 使用的 `cached_tokens`。

因此最终报告中的以下指标始终显示为 0：

- `Cached Prompt tok/s`
- 缓存命中 token 数
- 基于缓存 token 计算的 new prompt token 数

实际接口连续发送相同请求时，第一次返回 `cached_tokens=0`，第二次已经返回 `cached_tokens=128`，说明服务端缓存命中及返回字段均正常，问题发生在 EvalScope 的统计数据传递阶段。

目前观察到多轮对话策略中存在如下赋值：

```python
data.cached_tokens = data.real_cached_tokens
```

但普通单轮 open-loop/closed-loop 流程没有执行等价处理。

建议在 `BenchmarkData.finalize()` 中统一补充：

```python
if self.cached_tokens is None and self.real_cached_tokens is not None:
    self.cached_tokens = self.real_cached_tokens
```

这样既不会覆盖已经由其他策略设置的 `cached_tokens`，也能让普通 OpenAI API 压测正确统计服务端返回的真实缓存命中数。

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

```bash
evalscope perf \
  --model GLM-5.2-NVFP4 \
  --url http://172.31.0.128:48369/v1/chat/completions \
  --api openai \
  --dataset openqa \
  --dataset-path evalscope_openqa_cachebalanced_5000.jsonl \
  --max-prompt-length 10000000 \
  --min-prompt-length 0 \
  --number 1000 \
  --parallel 48 \
  --temperature 1 \
  --name cachebalanced_p48
```

也可以用两个内容完全相同的请求进行最小复现。第二个响应的 `usage.prompt_tokens_details.cached_tokens` 已经大于 0，但 EvalScope 最终报告中的 `Cached Prompt tok/s` 仍为 `0.00`。

## 错误日志

该问题不会抛出异常，压测可以正常完成，但统计结果错误。

<img width="1466" height="905" alt="Image" src="https://github.com/user-attachments/assets/bcbcc8d0-3a67-4b84-bebc-e1d7aedb5cb7" />

服务端第二次相同请求返回的关键字段：

```text
prompt_tokens=152
prompt_tokens_details.cached_tokens=128
```

EvalScope 报告中的结果：

```text
New Prompt tok/s     34421.93
Cached Prompt tok/s      0.00
```

代码路径分析：

```text
evalscope/perf/plugin/api/default_api.py
  usage.prompt_tokens_details.cached_tokens
    -> BenchmarkData.real_cached_tokens

evalscope/perf/utils/benchmark_util.py
  workload timeline 和聚合统计读取 BenchmarkData.cached_tokens

普通单轮流程中：
  real_cached_tokens 未同步到 cached_tokens
```

在本地对 `BenchmarkData.finalize()` 增加以下逻辑后，统计恢复正常：

```python
if self.cached_tokens is None and self.real_cached_tokens is not None:
    self.cached_tokens = self.real_cached_tokens
```

验证数据：

```text
prompt_tokens=152
real_cached_tokens=128
cached_tokens=128
new_prompt_tokens=24
```

## 运行环境

- 操作系统：Ubuntu 22.04
- Python版本：Python 3.10
- EvalScope 安装方式：Python virtual environment / pip
- 推理服务：SGLang，OpenAI-compatible API
- 调用链：EvalScope Perf -> SGLang Router -> SGLang PD disaggregation workers

## 其他信息

该问题与具体推理模型无关，只要 OpenAI 兼容服务通过以下字段报告缓存命中，就可能复现：

```text
usage.prompt_tokens_details.cached_tokens
```

建议在 `BenchmarkData.finalize()` 统一完成字段归一化，而不是仅在某个多轮对话策略中赋值，以覆盖普通单轮、open-loop 和 closed-loop 压测路径。


## 评论 (1)

### Yunnglin · 2026-07-23

感谢反馈并给出了精准的定位与修复建议 🙏

该问题已在 #1508 中修复并合入 main。

根因与你分析的一致：单轮（open-loop / closed-loop）压测路径下，服务端返回的 `usage.prompt_tokens_details.cached_tokens` 虽被解析进 `BenchmarkData.real_cached_tokens`，但未同步到聚合与 workload timeline 实际消费的 `cached_tokens`（此前该同步只存在于多轮策略中），导致 `Cached Prompt tok/s`、缓存命中 token 数、`avg_cached_percent` 始终为 0。

修复方式即采用你建议的方案，在 `BenchmarkData.finalize()` 中统一归一化，覆盖单轮 / open-loop / closed-loop 路径，且不覆盖多轮策略已设置的值：

```python
if self.cached_tokens is None and self.real_cached_tokens is not None:
    self.cached_tokens = self.real_cached_tokens
```

同时补充了回归测试。更新到最新代码后即可正常统计缓存命中，欢迎验证～
