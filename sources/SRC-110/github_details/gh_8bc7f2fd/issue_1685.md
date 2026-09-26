# [Issue #1685] swe_bench_verified_agentic 测试hang住

source: https://github.com/modelscope/evalscope/issues/1685
state: closed | updated: 2026-09-16T02:31:12Z
labels: 

## 正文

## 自查清单

在提交 issue 之前，请确保您已完成以下步骤:
- [x] 我已仔细阅读了[相关使用说明文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html)
- [x] 我已查看了[常见问题解答](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)
- [x] 我已搜索并查看了现有的 issues，确认这不是一个重复的问题

## 问题描述

swe_bench_verified_agentic 测试hang住

## EvalScope 版本（必填）
v1.10.0

## 使用的工具
- [ ] Native / 原生框架
- [ ] Opencompass backend
- [ ] VLMEvalKit backend
- [ ] RAGEval backend
- [x] Perf / 模型推理压测工具
- [ ] Arena / 竞技场模式

## 执行的代码或指令

```
evalscope eval \
  --model $MODEL \
  --api-url $OPENAI_API_COMPAT_URL \
  --api-key $TOKEN \
  --eval-type openai_api \
  --datasets swe_bench_verified_agentic \
  --ignore-errors \
  --eval-batch-size 64 \
  --generation-config '{"max_tokens": 131072, "temperature": 1.0, "top_p": 0.95, "retries":3, "parallel_tool_calls":"True"}' \
  --enable-progress-tracker \
  --use-cache ./outputs
```

## 错误日志

```
[INFO:ms_enclave] [📦 dqj57qxe] 2.5.2
[INFO:ms_enclave] [📦 dqj57qxe] 5.2.0
[INFO:ms_enclave] [📦 dqj57qxe] 5.2.1
[INFO:ms_enclave] [📦 dqj57qxe] 5.2.2
[INFO:ms_enclave] [📦 dqj57qxe] 5.2.3
[INFO:ms_enclave] [📦 dqj57qxe] e856638ba Preparing release version 5.2.3 (#6190)
[INFO:ms_enclave] [📦 dqj57qxe] 5e8c47faa Preparing release version 5.2.3
[INFO:ms_enclave] [📦 dqj57qxe] dae238c9b Release version 5.2.2 (#6055)
[INFO:ms_enclave] [📦 dqj57qxe] b27ba9772 Preparing release version 5.2.2
[INFO:ms_enclave] [📦 dqj57qxe] 307652202 Merge pull request #5762 from pytest-dev/hugovk-patch-1
[INFO:ms_enclave] [📦 dqj57qxe] f050203f5 Improve help for --runxfail flag
[INFO:ms_enclave] [📦 dqj57qxe] 3cff5e252 Merge pull request #5117 from blueyed/cov-terminal
[INFO:ms_enclave] [📦 dqj57qxe] 5e26304d8 Merge pull request #5075 from blueyed/console_output_style
[INFO:ms_enclave] [📦 dqj57qxe] 951213ee0 Use new suspend/resume in global_and_fixture_disabled
[INFO:ms_enclave] [📦 dqj57qxe] 5d2e2377f Update deprecations.rst now that we have removed a few features
[INFO:ms_enclave] [📦 aowtqp7j] Welcome to the Sphinx 4.1.0 quickstart utility.
[INFO:ms_enclave] [📦 aowtqp7j]
[INFO:ms_enclave] [📦 aowtqp7j] Please enter values for the following settings (just press Enter to
[INFO:ms_enclave] [📦 aowtqp7j] accept a default value, if one is given in brackets).
[INFO:ms_enclave] [📦 aowtqp7j]
[INFO:ms_enclave] [📦 aowtqp7j] Enter the root path for documentation.
[INFO:ms_enclave] [📦 aowtqp7j]
[INFO:ms_enclave] [📦 aowtqp7j] You have two options for placing the build directory for Sphinx output.
[INFO:ms_enclave] [📦 aowtqp7j] Either, you use a directory "_build" within the root path, or you separate
[INFO:ms_enclave] [📦 aowtqp7j] "source" and "build" directories within the root path.
[INFO:ms_enclave] [📦 aowtqp7j]
[INFO:ms_enclave] [📦 aowtqp7j] Inside the root directory, two more directories will be created; "_templates"
[INFO:ms_enclave] [📦 aowtqp7j] for custom HTML templates and "_static" for custom stylesheets and other static
[INFO:ms_enclave] [📦 aowtqp7j] files. You can enter another prefix (such as ".") to replace the underscore.
[INFO:ms_enclave] [📦 aowtqp7j]
[INFO:ms_enclave] [📦 aowtqp7j] The project name will occur in several places in the built documentation.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.
[INFO:ms_enclave] [📦 aowtqp7j] * Please enter some text.

无限
```

## 运行环境

- 操作系统：
- Python版本：

## 其他信息

如果有其他相关信息，请在此处提供。


## 评论 (4)

### Yunnglin · 2026-09-01

@ltm920716 感谢反馈。麻烦补充以下信息，方便定位：

1. 卡住样本的 `instance_id`；
2. 对应 `outputs/<timestamp>/predictions/` 中该样本的完整记录，尤其是 bash 工具调用的 `command` 和 `timeout`；
3. `pip show ms-enclave evalscope swebench` 输出；
4. 完整运行日志及已卡住时长。

也可以直接打包上传对应的 `outputs/<timestamp>/` 目录。

### ltm920716 · 2026-09-02

抱歉，数据清空了，后续如果遇到再补充到这里，谢谢

### ChenCJ-io · 2026-09-08

I don't have the reporter's `outputs/` either, but the log tail is enough to name one concrete gap, and it is reproducible without Docker.

**What the log shows.** `sphinx-quickstart` is interactive. It asks for a value, rejects an empty answer, and asks again — `* Please enter some text.` repeated forever is that prompt loop, not a stuck download. The model ran an interactive CLI inside the sandbox and it never terminates on its own.

**Why that hangs the run rather than timing out.** `EnclaveAgentEnvironment.exec` hands the deadline to ms_enclave and then waits with nothing bounding the wait:

```python
result = await handle.execute_tool(
    'shell_executor',
    {'command': shell_argv, 'timeout': timeout_s},
)
```

If the sandbox layer does not come back — the command is unkillable, the exec channel is wedged, the reply is lost — this `await` never returns. `LocalAgentEnvironment` does not have that problem; it wraps the subprocess in `asyncio.wait_for` and returns `timed_out=True` on expiry. Only the enclave path relies entirely on the layer below it.

Reproducible with no Docker and no ms_enclave installed, by stubbing the handle:

```python
class HangingHandle:
    sandbox_id = 'stub'
    async def execute_tool(self, name, args):
        await asyncio.sleep(3600)      # the sandbox never answers

env = EnclaveAgentEnvironment.__new__(EnclaveAgentEnvironment)
env._handle = HangingHandle(); env._timeout = 60.0; env._interpreter = ['bash', '-c']
await asyncio.wait_for(env.exec(['/bin/bash', '-c', 'sphinx-quickstart'], timeout=1.0), timeout=5)
```

```
STILL RUNNING after 5.0s despite exec(timeout=1.0)
```

One sample then blocks its worker for the rest of the run, which matches "hangs" with no traceback and no progress.

I've opened a PR that adds a local backstop: `exec` stops waiting at `timeout + grace` and returns a timed-out `ExecResult`, so the sample fails and the run moves on. It deliberately waits out the grace first, because ms_enclave's own `TIMEOUT` status carries the output the command produced before its deadline and that is the more useful answer.

This bounds the damage; it does not explain why the sandbox failed to enforce its own timeout in the first place, and the reporter's `instance_id` plus `pip show ms-enclave` would still be worth having if it recurs.

**Two related gaps I noticed while reading that code**, both separate from this one:

1. `EnclaveAgentEnvironment.exec` accepts `input=` and never uses it, so stdin is silently dropped in a sandbox. `runners/mock.py` passes `input=task.instruction`, and `runners/codex.py` already carries a comment working around it.
2. `LocalAgentEnvironment` runs commands with `stdin=None`, so a child inherits the parent process's stdin. With a terminal attached, an interactive command blocks on it until the tool timeout (verified: `read -p` under a pty waits the full timeout and reports `timed_out=True`). `DEVNULL` would make those commands fail fast instead.

Happy to send either as its own PR if they look worth fixing.


### Yunnglin · 2026-09-16

Closing for now because the reported hang cannot be reproduced with the supported `ms-enclave>=0.0.8` Docker timeout path, and the original runtime data is no longer available.

PR #1717 is also being closed: its detached caller-side timeout does not safely cancel the underlying sandbox operation.

Please reopen with the affected sample trace, bash command and timeout, `pip show ms-enclave evalscope swebench`, and complete logs if this recurs.

