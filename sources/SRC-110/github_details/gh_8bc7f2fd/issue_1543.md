# [Issue #1543] ifeval测评中，同一问题repeats3次，模型回答一致，但评价指标结果不一致，langdetect.detect

source: https://github.com/modelscope/evalscope/issues/1543
state: closed | updated: 2026-08-06T04:33:59Z
labels: 

## 正文

## 自查清单

在提交 issue 之前，请确保您已完成以下步骤:
- [x] 我已仔细阅读了[相关使用说明文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html)
- [x] 我已查看了[常见问题解答](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)
- [x] 我已搜索并查看了现有的 issues，确认这不是一个重复的问题

## 问题描述
- https://github.com/modelscope/evalscope/blob/e5abf3e93cae17ca056dda000f71007b2823a936/evalscope/benchmarks/ifeval/instructions.py#L1407-L1416
- 此处评价'english_lowercase': LowercaseLettersEnglishChecker
- 模型三次回答都是完全一致的："\n\nwhat are the boys holding?"
- 但测评指标："prompt_level_strict": 1.0一次，"prompt_level_strict": 0.0两次
- 原因可能是：langdetect.detect() 基于概率模型，对于短文本多次调用可能返回不同结果。相关问题[langdetect/issues/3](https://github.com/Mimino666/langdetect/issues/3)，[langdetect/issues/120](https://github.com/Mimino666/langdetect/issues/120)
- 社区一些建议，设置种子以固定
```python
import langdetect
langdetect.DetectorFactory.seed = 0
```

- ifeval和multi-if两个数据集测评用到

- 测试结果片段：outputs/20260711_223640/reviews/Qwen3-30B-A3B-Thinking-2507/ifeval_default.jsonl
```json
{"index": 12, "target": "", "messages": [{"id": "46507a07", "content": "Given the sentence \"Two young boys with toy guns and horns.\" can you ask a question? Please ensure that your response is in English, and in all lowercase letters. No capital letters are allowed.", "source": null, "metadata": null, "internal": null, "perf_metrics": null, "role": "user", "tool_call_id": null}, {"id": "5deea83e", "content": "\n\nwhat are the boys holding?", "source": "generate", "metadata": null, "internal": null, "perf_metrics": {"latency": 23.600469122990035, "ttft": 23.297243506996892, "input_tokens": 50, "output_tokens": 528, "tpot": 0.0005753806755088086}, "role": "assistant", "tool_calls": null, "model": "Qwen3-30B-A3B-Thinking-2507"}], "trajectory": [], "sample_score": {"score": {"value": {"prompt_level_strict": 1.0, "inst_level_strict": 1.0, "prompt_level_loose": 1.0, "inst_level_loose": 1.0}, "extracted_prediction": "\n\nwhat are the boys holding?", "prediction": "\n\nwhat are the boys holding?", "explanation": null, "metadata": {}, "main_score_name": "prompt_level_strict"}, "sample_id": 12, "group_id": 4, "sample_metadata": {"key": 1019, "prompt": "Given the sentence \"Two young boys with toy guns and horns.\" can you ask a question? Please ensure that your response is in English, and in all lowercase letters. No capital letters are allowed.", "instruction_id_list": ["change_case:english_lowercase"], "kwargs": [{"num_highlights": null, "relation": null, "num_words": null, "num_placeholders": null, "prompt_to_repeat": null, "num_bullets": null, "section_spliter": null, "num_sections": null, "capital_relation": null, "capital_frequency": null, "keywords": null, "num_paragraphs": null, "language": null, "let_relation": null, "letter": null, "let_frequency": null, "end_phrase": null, "forbidden_words": null, "keyword": null, "frequency": null, "num_sentences": null, "postscript_marker": null, "first_word": null, "nth_paragraph": null}]}}}
{"index": 13, "target": "", "messages": [{"id": "3632ca98", "content": "Given the sentence \"Two young boys with toy guns and horns.\" can you ask a question? Please ensure that your response is in English, and in all lowercase letters. No capital letters are allowed.", "source": null, "metadata": null, "internal": null, "perf_metrics": null, "role": "user", "tool_call_id": null}, {"id": "b9e6d42c", "content": "\n\nwhat are the boys holding?", "source": "generate", "metadata": null, "internal": null, "perf_metrics": {"latency": 23.6287512939889, "ttft": 23.316607290995307, "input_tokens": 50, "output_tokens": 528, "tpot": 0.0005923036109935316}, "role": "assistant", "tool_calls": null, "model": "Qwen3-30B-A3B-Thinking-2507"}], "trajectory": [], "sample_score": {"score": {"value": {"prompt_level_strict": 0.0, "inst_level_strict": 0.0, "prompt_level_loose": 0.0, "inst_level_loose": 0.0}, "extracted_prediction": "\n\nwhat are the boys holding?", "prediction": "\n\nwhat are the boys holding?", "explanation": null, "metadata": {}, "main_score_name": "prompt_level_strict"}, "sample_id": 13, "group_id": 4, "sample_metadata": {"key": 1019, "prompt": "Given the sentence \"Two young boys with toy guns and horns.\" can you ask a question? Please ensure that your response is in English, and in all lowercase letters. No capital letters are allowed.", "instruction_id_list": ["change_case:english_lowercase"], "kwargs": [{"num_highlights": null, "relation": null, "num_words": null, "num_placeholders": null, "prompt_to_repeat": null, "num_bullets": null, "section_spliter": null, "num_sections": null, "capital_relation": null, "capital_frequency": null, "keywords": null, "num_paragraphs": null, "language": null, "let_relation": null, "letter": null, "let_frequency": null, "end_phrase": null, "forbidden_words": null, "keyword": null, "frequency": null, "num_sentences": null, "postscript_marker": null, "first_word": null, "nth_paragraph": null}]}}}
{"index": 14, "target": "", "messages": [{"id": "b4565929", "content": "Given the sentence \"Two young boys with toy guns and horns.\" can you ask a question? Please ensure that your response is in English, and in all lowercase letters. No capital letters are allowed.", "source": null, "metadata": null, "internal": null, "perf_metrics": null, "role": "user", "tool_call_id": null}, {"id": "7f625ee5", "content": "\n\nwhat are the boys holding?", "source": "generate", "metadata": null, "internal": null, "perf_metrics": {"latency": 23.636354201007634, "ttft": 23.329819980019238, "input_tokens": 50, "output_tokens": 528, "tpot": 0.0005816588633555912}, "role": "assistant", "tool_calls": null, "model": "Qwen3-30B-A3B-Thinking-2507"}], "trajectory": [], "sample_score": {"score": {"value": {"prompt_level_strict": 0.0, "inst_level_strict": 0.0, "prompt_level_loose": 0.0, "inst_level_loose": 0.0}, "extracted_prediction": "\n\nwhat are the boys holding?", "prediction": "\n\nwhat are the boys holding?", "explanation": null, "metadata": {}, "main_score_name": "prompt_level_strict"}, "sample_id": 14, "group_id": 4, "sample_metadata": {"key": 1019, "prompt": "Given the sentence \"Two young boys with toy guns and horns.\" can you ask a question? Please ensure that your response is in English, and in all lowercase letters. No capital letters are allowed.", "instruction_id_list": ["change_case:english_lowercase"], "kwargs": [{"num_highlights": null, "relation": null, "num_words": null, "num_placeholders": null, "prompt_to_repeat": null, "num_bullets": null, "section_spliter": null, "num_sections": null, "capital_relation": null, "capital_frequency": null, "keywords": null, "num_paragraphs": null, "language": null, "let_relation": null, "letter": null, "let_frequency": null, "end_phrase": null, "forbidden_words": null, "keyword": null, "frequency": null, "num_sentences": null, "postscript_marker": null, "first_word": null, "nth_paragraph": null}]}}}
```

- 但单独测不一定能复现出来：
```python
import langdetect
# langdetect.DetectorFactory.seed = 0

value="\n\nwhat are the boys holding?"
# value = u'並查看更'
value='\n  THIS IS AN ENGLISH SENTENCE. EVERY LETTER IS CAPITALIZED!!! AMAZING.\n  '

lang_counters = {}

for i in range(100):
    l = langdetect.detect(value)
    if l not in lang_counters:
        lang_counters[l] = 0
    lang_counters[l] += 1

print(lang_counters)

# {'en': 100} "\n\nwhat are the boys holding?"
# {'zh-tw': 45, 'ko': 55} u'並查看更'
# {'en': 96, 'de': 4} '\n  THIS IS AN ENGLISH SENTENCE. EVERY LETTER IS CAPITALIZED!!! AMAZING.\n  '


# 设置 langdetect.DetectorFactory.seed = 0

# {'en': 100} "\n\nwhat are the boys holding?"
# {'zh-tw': 100} u'並查看更'
# {'en': 100} '\n  THIS IS AN ENGLISH SENTENCE. EVERY LETTER IS CAPITALIZED!!! AMAZING.\n  '

```


## EvalScope 版本（必填）
evalscope  Version: v1.7.0
langdetect Version: 1.0.9

## 使用的工具
- [x] Native / 原生框架
- [ ] Opencompass backend
- [ ] VLMEvalKit backend
- [ ] RAGEval backend
- [ ] Perf / 模型推理压测工具
- [ ] Arena / 竞技场模式

## 执行的代码或指令

请提供您执行的主要代码或指令。

## 错误日志

请粘贴完整的错误日志或控制台输出。

## 运行环境

- 操作系统：
- Python版本：

## 其他信息

如果有其他相关信息，请在此处提供。


## 评论 (1)

### Yunnglin · 2026-08-06

感谢反馈，问题已定位并在 #1549 修复合并到 main。您指出的 `langdetect` 随机性方向是对的，但**只设种子并不足以解决**，实际主因是另一个问题。

**两个独立的不确定性来源：**

1. `langdetect` 推理阶段随机采样 —— 正如您建议的，`DetectorFactory.seed = 0` 可以解决这一项。

2. **`langdetect.detect()` 懒加载进程级全局 factory 且没有加锁**（`init_factory()` 里就是裸的 `if _factory is None`）。并发首次调用会竞态：多个线程各自新建 factory，同时另一些线程已经在用一个语言 profile 只加载了一半的实例做检测，于是并行评测最初若干样本的结果是错的，且与种子无关。这正好对应真实评测场景——冷启动 + 并发 review，也解释了为什么您三次 repeats 的同一条回答会给出不同分数。

现在的做法是在任何检测之前加锁把 factory 构建好一次（ifeval 用 double-checked locking 在首次使用时完成，multi-if 在 import 时完成，此时还是单线程）。

**实测数据**（冷 factory + 16 线程跑 128 次同一条回答 `"\n\nwhat are the boys holding?"`）：

| 版本 | 结果集合 |
| --- | --- |
| 修复前 | `{False, True}` |
| 只设 `DetectorFactory.seed = 0` | `{False, True}` |
| 加锁预热 + 设种子 | `{True}` |

这也说明为什么您单独测试时难以复现：单线程重复调用触发不到这个竞态。

已补上会在旧代码上失败的并发回归测试（`tests/benchmark/test_ifeval_language_checkers.py`），`ifeval` 和 `multi_if` 两个数据集都已覆盖。

