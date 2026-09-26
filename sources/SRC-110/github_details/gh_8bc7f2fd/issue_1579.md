# [Issue #1579] evalscope在进行gpqa_diamond数据集精度结果重新计算时(--rerun-review参数)结果错误，从结果上看rerun-review参数功能在该数据集失效

source: https://github.com/modelscope/evalscope/issues/1579
state: closed | updated: 2026-08-15T06:50:31Z
labels: 

## 正文

## 自查清单

在提交 issue 之前，请确保您已完成以下步骤:
- [√] 我已仔细阅读了[相关使用说明文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html)
- [√] 我已查看了[常见问题解答](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)
- [√] 我已搜索并查看了现有的 issues，确认这不是一个重复的问题

## 问题描述

请简要描述您遇到的问题。
evalscope eval --rerun-review 时，使用--use-cache加载之前生成的结果，得到的gpqa_diamond精度数据异常，约为25%【像是随机】

## EvalScope 版本（必填）
v1.7.0

## 使用的工具
- [√] Native / 原生框架
- [ ] Opencompass backend
- [ ] VLMEvalKit backend
- [ ] RAGEval backend
- [ ] Perf / 模型推理压测工具
- [ ] Arena / 竞技场模式

## 执行的代码或指令
evalscope eval --model XXX --datasets gpqa_diamond --use-cache xxx --rerun-review
请提供您执行的主要代码或指令。

## 错误日志

请粘贴完整的错误日志或控制台输出。
首次执行以及使用rerun-review参数重计算，两次相同的执行同样的问题target不同，导致计算出的精度结果不同。
首次执行：
{"index": 0, "target": "A", "messages": [{"id": "", "content": "Answer the following multiple choice question. The last line of your response should be of the following format: 'ANSWER: [LETTER]' (without quotes) where [LETTER] is one of A,B,C,D. Think step by step before answering.\n\nTwo quantum states with energies E1 and E2 have a lifetime of 10^-9 sec and 10^-8 sec, respectively. We want to clearly distinguish these two energy levels. Which one of the following options could be their energy difference so that they can be clearly resolved?\n\n\nA) 10^-4 eV\nB) 10^-8 eV\nC) 10^-9 eV\nD) 10^-11 eV", "source": null, "metadata": null, "internal": null, "perf_metrics": null, "role": "user", "tool_call_id": null}

rerun-review执行：
{"index": 0, "target": "C", "messages": [{"id": "", "content": "Answer the following multiple choice question. The last line of your response should be of the following format: 'ANSWER: [LETTER]' (without quotes) where [LETTER] is one of A,B,C,D. Think step by step before answering.\n\nTwo quantum states with energies E1 and E2 have a lifetime of 10^-9 sec and 10^-8 sec, respectively. We want to clearly distinguish these two energy levels. Which one of the following options could be their energy difference so that they can be clearly resolved?\n\n\nA) 10^-4 eV\nB) 10^-8 eV\nC) 10^-9 eV\nD) 10^-11 eV", "source": null, "metadata": null, "internal": null, "perf_metrics": null, "role": "user", "tool_call_id": null}

## 运行环境

- 操作系统：
- Python版本：3.12.13

## 其他信息

怀疑是gpqa_adapter.py文件中 _process_input 方法中的 random.shuffle(choices) 导致【第110行】

如果有其他相关信息，请在此处提供。


## 评论 (2)

### YuhaoLin2005 · 2026-08-15

@dkvsme your suspicion at gpqa_adapter.py:105 is right — I reproduced it locally. The unseeded `random.shuffle(choices)` makes `_process_input` non-deterministic per question, so the answer letter drifts between runs.

Same question, 8 calls to the real `_process_input`:
  targets: ['A','A','B','A','C','C','B','B']     <- answer letter drifts A/B/C
  two consecutive calls: call1 target=B, call2 target=C   <- your A->C case

Why --rerun-review breaks on top of that: on a rerun the dataset is rebuilt from scratch (record_to_sample → _process_input shuffles again), so `cache.py to_task_state` (L333, via `dataset[self.index]`) pairs the cached messages — from the original shuffle the model actually answered — with a sample whose answer key comes from the new shuffle. Review then compares the cached letter against a fresh key, so accuracy should collapse to chance (~1/4 for 4 options); I can run --rerun-review to confirm the measured drop if useful.

I verified a minimal fix direction locally: seed the shuffle from the question content (e.g. `random.Random(hashlib.sha256(question_text))`), which makes `_process_input` a pure function:
  same question, 8 calls -> all target D, identical choices (stable)
  different question -> different shuffle (order-bias protection preserved)

I'd also anchor the answer key to what was actually generated: persist the target in the cached ModelResult so `to_task_state` reuses it instead of re-deriving from the dataset.

I've verified both fix layers locally (seeded-shuffle determinism; target anchoring in the cached ModelResult) and have a regression test drafted; happy to open a PR with both layers plus red→green regression tests (a unit test asserting `_process_input` is deterministic; an integration test that the cached target survives `to_task_state`).


### Yunnglin · 2026-08-15

fixed
