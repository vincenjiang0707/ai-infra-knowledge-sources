# [Issue #1707] [Bug] longbench_v2 数据集指定 few_shot_num 后报错 KeyError: 'fewshot'

source: https://github.com/modelscope/evalscope/issues/1707
state: closed | updated: 2026-09-08T06:49:40Z
labels: 

## 正文

## 自查清单

在提交 issue 之前，请确保您已完成以下步骤:
- [x] 我已仔细阅读了[相关使用说明文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html)
- [x] 我已查看了[常见问题解答](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)
- [x] 我已搜索并查看了现有的 issues，确认这不是一个重复的问题

## 问题描述

在使用 EvalScope 对 longbench_v2 数据集进行评测时，如果按照[ModelScope](https://www.modelscope.cn/models/deepseek-ai/DeepSeek-V4-Flash) 参数文档在 --dataset-args 中指定参数 few_shot_num 设置为1，程序会抛出 KeyError: 'fewshot' 异常并终止评测。该错误在移除 few_shot_num 参数后消失，但评测会回退到默认的 0-shot 模式。

## EvalScope 版本（必填）
v1.11.1

## 使用的工具
- [x] Native / 原生框架

## 执行的代码或指令

evalscope eval \
  --model DeepSeek-V4-Flash-W4A8 \
  --dataset-args '{"longbench_v2": {"few_shot_num": 1}}' \
  --generation-config '{"temperature":1.0,"top_p":1.0,"max_tokens":32768,"n":1,"do_sample":true}' \
  --eval-batch-size 64 \
  --datasets longbench_v2 \
  --work-dir /agent/var/build/249/ws/test_result \
  --api-url http://127.0.0.1:9989/v1 \
  --api-key EMPTY \
  --eval-type openai_api

## 错误日志

`
Traceback (most recent call last):
  File "/usr/local/bin/evalscope", line 6, in <module>
    sys.exit(run_cmd())
             ^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/evalscope/cli/cli.py", line 31, in run_cmd
    cmd.execute()
  File "/usr/local/lib/python3.12/site-packages/evalscope/cli/start_eval.py", line 30, in execute
    run_task(self.args)
  File "/usr/local/lib/python3.12/site-packages/evalscope/run.py", line 33, in run_task
    return run_single_task(task_cfg)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/evalscope/run.py", line 48, in run_single_task
    result = evaluate_model(task_cfg, outputs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/evalscope/run.py", line 213, in evaluate_model
    res_dict = evaluator.eval()
               ^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/evalscope/evaluator/evaluator.py", line 173, in eval
    dataset_dict = {k: v for k, v in self.benchmark.load_dataset().items() if len(v) > 0}
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/evalscope/api/benchmark/adapters/default_data_adapter.py", line 68, in load_dataset
    self._post_process_samples()
  File "/usr/local/lib/python3.12/site-packages/evalscope/api/benchmark/adapters/default_data_adapter.py", line 133, in _post_process_samples
    sample.input = self.process_sample_str_input(sample, subset)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/evalscope/api/benchmark/adapters/default_data_adapter.py", line 145, in process_sample_str_input
    input_text = self.process_sample_input(sample, subset=subset)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/evalscope/api/benchmark/adapters/default_data_adapter.py", line 194, in process_sample_input
    input_text = self.format_fewshot_template(fewshot=few_shot, sample=sample)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/evalscope/api/benchmark/adapters/multi_choice_adapter.py", line 62, in format_fewshot_template
    return prompt(
           ^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/evalscope/utils/multi_choices.py", line 122, in prompt
    return template.format(
           ^^^^^^^^^^^^^^^^
KeyError: 'fewshot'
`

## 运行环境

- 操作系统：Linux
- Python版本：3.12

## 其他信息

如果有其他相关信息，请在此处提供。


## 评论 (1)

### Yunnglin · 2026-09-08

Thanks for the report. PR #1714 now validates few-shot capabilities before dataset loading: LongBench-v2 rejects non-zero `few_shot_num` with a clear error instead of raising `KeyError: 'fewshot'`. The fix also preserves benchmarks with fixed built-in examples and dynamic train-split few-shot support.
