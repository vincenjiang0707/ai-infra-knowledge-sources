# [Issue #1548] deepseek perf测试没有tokenizer.chat_template

source: https://github.com/modelscope/evalscope/issues/1548
state: closed | updated: 2026-08-14T07:44:34Z
labels: 

## 正文

## 自查清单

在提交 issue 之前，请确保您已完成以下步骤:
- [x] 我已仔细阅读了[相关使用说明文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html)
- [x] 我已查看了[常见问题解答](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)
- [x] 我已搜索并查看了现有的 issues，确认这不是一个重复的问题

## 问题描述
evalscope perf 测试deepseek v4 模型报错
```
tokenizer.chat_template is not set and no template argument was passed
```
deepseek 官方的说明是：

<img width="787" height="668" alt="Image" src="https://github.com/user-attachments/assets/b877b1a0-1b39-48ac-b724-e55c1a29050e" />

目前是否还没有适配这种方式

## EvalScope 版本（必填）
v1.10.0

## 使用的工具
- [ ] Native / 原生框架
- [ ] Opencompass backend
- [ ] VLMEvalKit backend
- [ ] RAGEval backend
- [√] Perf / 模型推理压测工具
- [ ] Arena / 竞技场模式

## 执行的代码或指令
```
evalscope perf \
      --model "/models/deepseek-v4-flash" \
      --url "http://127.0.0.1:30000/v1/chat/completions" \
      --api openai \
      --dataset longalpaca\
      --parallel 1 2 4 8 \
      --number 20 20 20 20 \
      --min-tokens 1024 \
      --max-tokens 1024 \
      --tokenizer-path /models/deepseek-v4-flash \
      --extra-args '{"ignore_eos": true}' \
```

## 错误日志

Traceback (most recent call last):
  File "/root/miniconda/envs/python310_torch25_cuda/bin/evalscope", line 6, in <module>
    sys.exit(run_cmd())
  File "/root/miniconda/envs/python310_torch25_cuda/lib/python3.10/site-packages/evalscope/cli/cli.py", line 31, in run_cmd
    cmd.execute()
  File "/root/miniconda/envs/python310_torch25_cuda/lib/python3.10/site-packages/evalscope/cli/start_perf.py", line 39, in execute
    run_perf_benchmark(self.args)
  File "/root/miniconda/envs/python310_torch25_cuda/lib/python3.10/site-packages/evalscope/perf/main.py", line 179, in run_perf_benchmark
    results = run_multi_benchmark(args, output_path=output_path)
  File "/root/miniconda/envs/python310_torch25_cuda/lib/python3.10/site-packages/evalscope/perf/main.py", line 119, in run_multi_benchmark
    benchmark_result = run_one_benchmark(args, output_path=cur_output_path)
  File "/root/miniconda/envs/python310_torch25_cuda/lib/python3.10/site-packages/evalscope/perf/main.py", line 63, in run_one_benchmark
    metrics_result, percentile_result, trace_summary, workload_throughput = loop.run_until_complete(
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/root/miniconda/envs/python310_torch25_cuda/lib/python3.10/site-packages/evalscope/perf/utils/handler.py", line 97, in async_wrapper
    return await func(*args, **kwargs)
  File "/root/miniconda/envs/python310_torch25_cuda/lib/python3.10/site-packages/evalscope/perf/benchmark.py", line 149, in run_benchmark
    metrics, trace_summary, workload_timeline, result_db_path = await run_benchmark_pipeline(
  File "/root/miniconda/envs/python310_torch25_cuda/lib/python3.10/site-packages/evalscope/perf/core/pipeline.py", line 35, in run_benchmark_pipeline
    await producer_task
  File "/root/miniconda/envs/python310_torch25_cuda/lib/python3.10/site-packages/evalscope/perf/core/strategies/closed_loop.py", line 53, in run
    warmup_requests, benchmark_requests = await self._partition_requests(self._request_generator)
  File "/root/miniconda/envs/python310_torch25_cuda/lib/python3.10/site-packages/evalscope/perf/core/strategies/base.py", line 74, in _partition_requests
    async for request, is_warmup in gen:
  File "/root/miniconda/envs/python310_torch25_cuda/lib/python3.10/site-packages/evalscope/perf/utils/handler.py", line 84, in async_generator_wrapper
    async for item in func(*args, **kwargs):
  File "/root/miniconda/envs/python310_torch25_cuda/lib/python3.10/site-packages/evalscope/perf/benchmark.py", line 111, in get_requests
    async for request, is_warmup in generator:
  File "/root/miniconda/envs/python310_torch25_cuda/lib/python3.10/site-packages/evalscope/perf/benchmark.py", line 79, in _generate_from_dataset
    for messages in pbar:
  File "/root/miniconda/envs/python310_torch25_cuda/lib/python3.10/site-packages/tqdm/std.py", line 1181, in __iter__
    for obj in iterable:
  File "/root/miniconda/envs/python310_torch25_cuda/lib/python3.10/site-packages/evalscope/perf/plugin/datasets/longalpaca.py", line 28, in build_messages
    result = self.prepare_messages(prompt)
  File "/root/miniconda/envs/python310_torch25_cuda/lib/python3.10/site-packages/evalscope/perf/plugin/datasets/base.py", line 288, in prepare_messages
    prepared = self.prepare_prompt(prompt)
  File "/root/miniconda/envs/python310_torch25_cuda/lib/python3.10/site-packages/evalscope/perf/plugin/datasets/base.py", line 209, in prepare_prompt
    is_valid, _ = self.check_prompt_length(prompt)
  File "/root/miniconda/envs/python310_torch25_cuda/lib/python3.10/site-packages/evalscope/perf/plugin/datasets/base.py", line 352, in check_prompt_length
    prompt_length = len(tokenize_chat_messages(self.tokenizer, messages))
  File "/root/miniconda/envs/python310_torch25_cuda/lib/python3.10/site-packages/evalscope/perf/plugin/datasets/utils.py", line 60, in tokenize_chat_messages
    result = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=add_generation_prompt)
  File "/root/miniconda/envs/python310_torch25_cuda/lib/python3.10/site-packages/transformers/tokenization_utils_base.py", line 3066, in apply_chat_template
    chat_template = self.get_chat_template(chat_template, tools)
  File "/root/miniconda/envs/python310_torch25_cuda/lib/python3.10/site-packages/transformers/tokenization_utils_base.py", line 3248, in get_chat_template
    raise ValueError(
ValueError: Cannot use chat template functions because tokenizer.chat_template is not set and no template argument was passed! For information about writing templates and setting the tokenizer.chat_template attribute, please see the documentation at https://huggingface.co/docs/transformers/main/en/chat_templating

## 运行环境

- 操作系统：Linux
- Python版本：3.10

## 其他信息

如果有其他相关信息，请在此处提供。


## 评论 (6)

### lroundly · 2026-08-06

已经解决了，不传--tokenizer-path就不会报错了。

### Yunnglin · 2026-08-06

这个不是 EvalScope 的适配问题，也不是 transformers 版本问题：DeepSeek-V4 官方刻意没有提供 jinja 模板。model card 里写的是

> This release does not include a Jinja-format chat template. Instead, we provide a dedicated `encoding` folder with Python scripts…

所以这个权重目录里既没有 `chat_template`，也没有 `chat_template.jinja`，`apply_chat_template()` 必然报错。

你的解法（不传 `--tokenizer-path`）就是目前推荐的做法。perf 里 tokenizer 只用于客户端 token 核算，SGLang 会返回 `usage`，压测指标不受影响。唯一副作用是 `--min/max-prompt-length` 会按字符数而不是 token 数过滤，你这条命令用的是默认值，不影响。

框架侧确实该改：模板缺失应该是降级 + 一次性告警，而不是直接中断压测。我们会跟进修复，修好后在这里同步，issue 先保持 open。


### 45min-on-the-git · 2026-08-07

> 这个不是 EvalScope 的适配问题，也不是 transformers 版本问题：DeepSeek-V4 官方刻意没有提供 jinja 模板。model card 里写的是
> 
> > This release does not include a Jinja-format chat template. Instead, we provide a dedicated `encoding` folder with Python scripts…
> 
> 所以这个权重目录里既没有 `chat_template`，也没有 `chat_template.jinja`，`apply_chat_template()` 必然报错。
> 
> 你的解法（不传 `--tokenizer-path`）就是目前推荐的做法。perf 里 tokenizer 只用于客户端 token 核算，SGLang 会返回 `usage`，压测指标不受影响。唯一副作用是 `--min/max-prompt-length` 会按字符数而不是 token 数过滤，你这条命令用的是默认值，不影响。
> 
> 框架侧确实该改：模板缺失应该是降级 + 一次性告警，而不是直接中断压测。我们会跟进修复，修好后在这里同步，issue 先保持 open。

我有个疑问，如果指定其它deepseek系列的模型的tokenizer文件可以吗？例如Deepseek-32B，V3或R1的，就下载他模型文件里面的tokenizer文件。

### Yunnglin · 2026-08-11

可以，前提是**词表一致**：

- **V3 / R1 / V3.1 / V3.2 之间**可以借。上次同样的问题（#1119，压 V3.2）就有人用 V3.1 的 tokenizer 跑通了。
- **借给 V4 需要先验证**。官方连模板方案都换了，词表是否和 V3 一致没有依据。V4 目录里的 tokenizer 本身可用（只是缺 jinja 模板），所以用两个 tokenizer 分别 `encode` 同一句话，结果一致才能借。
- **`Deepseek-32B` 不要用**。如果指 R1-Distill-Qwen-32B，那是 Qwen 词表，偏差最大。

另外，加了 `--tokenize-prompt` 时绝对不能借：那条路径会把客户端算出的 token id 直接发给服务端，词表不一致就是压错了内容。

最稳的做法仍然是不传 `--tokenizer-path`，让服务端的 `usage` 提供 token 数，只有 `random` 系列数据集必须提供 tokenizer。

框架侧修复已提交 #1564。这里更正我上一条回复：最终没有做“降级 + 告警”，而是**明确报错并列出三条处置方式**——降级会让报告里的 prompt token 数静默偏低，压测数据是要被引用的，宁可让用户显式选一次。


### Yunnglin · 2026-08-11

修复已合入 main（PR #1564）。

现在用没有 chat template 的分词器压 `chat/completions` 接口时，不再抛 transformers 的原始报错，而是给出明确的失败原因和三条处置方式：去掉 `--tokenizer-path` 改用服务端 `usage`、换一个自带模板且词表一致的分词器、或用 `--no-apply-chat-template` 压 completions 接口。文档的「分词器与 chat template」小节也补上了说明。

关于借用其它 DeepSeek 分词器的问题见[上一条回复](https://github.com/modelscope/evalscope/issues/1548#issuecomment-5251538945)：同词表家族（V3 / R1 / V3.1 / V3.2）可以借，借给 V4 需先实测编码结果一致，且 `--tokenize-prompt` 下绝不能借。

顺带在 #1565 记录了这次发现的两个相关的错误处理缺陷（报错被吞成 None / 连接检测重试到超时），会另行跟进。先关闭本 issue，如仍有问题欢迎重开。


### CarryCKW · 2026-08-14

模型路径中加入以下缺失的chat_template.jinja即可：https://huggingface.co/trl-internal-testing/tiny-DeepseekV4ForCausalLM/blob/refs%2Fpr%2F6/chat_template.jinja
