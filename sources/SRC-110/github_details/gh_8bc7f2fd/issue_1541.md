# [Issue #1541] [LiveCodeBench] [Bug] Discrepancy in LiveCodeBench system prompt usage compared to official repo

source: https://github.com/modelscope/evalscope/issues/1541
state: closed | updated: 2026-08-06T09:39:44Z
labels: 

## 正文

## Self-Check List

Before submitting an issue, please ensure you have completed the following steps:
- [x] I have carefully read the [relevant user documentation](https://evalscope.readthedocs.io/en/latest/get_started/parameters.html)
- [x] I have reviewed the [Frequently Asked Questions](https://evalscope.readthedocs.io/en/latest/get_started/faq.html)
- [x] I have searched and reviewed existing issues to confirm this is not a duplicate problem

## Problem Description

While evaluating on LiveCodeBench, I noticed that the system prompts defined in [prompts.py](https://github.com/modelscope/evalscope/blob/main/evalscope/benchmarks/live_code_bench/prompts.py) do not seem to be utilized during the actual evaluation process.

This behavior differs from the official [LiveCodeBench repo](https://github.com/LiveCodeBench/LiveCodeBench/blob/main/lcb_runner/prompts/code_generation.py), and this discrepancy leads to significantly different evaluation scores.

Could you please clarify the reason behind this design choice? 

Thanks ahead.

## EvalScope Version (Required)
main branch

## Tools Used
- [ ] Native / Native framework
- [ ] Opencompass backend
- [ ] VLMEvalKit backend
- [ ] RAGEval backend
- [ ] Perf / Model inference stress testing tool
- [ ] Arena / Arena mode

## Executed Code or Instructions

Please provide the main code or instructions you executed.

## Error Log

Please paste the complete error log or console output.

## Running Environment

- Operating System:
- Python Version:

## Additional Information

If there is any other relevant information, please provide it here.


## 评论 (2)

### Yunnglin · 2026-08-06

Thanks for catching this — your observation was correct, and it is now fixed in #1549 (merged to main).

There was no design rationale behind it: the system messages in `live_code_bench/prompts.py` were simply never wired up. Only `CodeGenerationPromptConstants.FORMATTING_*` was used (to build the `### Format` part of the user message), while `SYSTEM_MESSAGE_GENERIC` and the other system messages were defined but never referenced. As a result EvalScope sent a single user message, whereas the official `lcb_runner` sends a system message plus the user message.

The fix registers the official generic system message as the benchmark's system prompt, so requests now carry:

```
role=system   You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification and passes all tests. You will NOT return anything except for the program.
role=user     ### Question: ... ### Format: ... ### Answer: (use the provided format with backticks)
```

which matches the official runner's structure. Verified on a real `release_v1` run that both messages are actually sent.

⚠️ **Note on comparability:** LiveCodeBench results produced after this change are not directly comparable with your earlier EvalScope runs. If you need the previous behaviour, you can disable the system prompt per run:

```python
dataset_args={'live_code_bench': {'system_prompt': None}}
```

One caveat on our side: on a small sample (8 problems from `release_v1`) we saw no score difference with and without the system prompt, so we could not quantify the gap you observed. If you have numbers from a fuller run comparing EvalScope against the official repo, they would be very welcome — the remaining difference may point at a further divergence we have not spotted yet.


### liudl85 · 2026-08-06

@Yunnglin Thanks for the prompt fix, great work! 

Just as a reference, for DeepSeek-V4-Flash-0731, we're currently seeing roughly a 10% score difference between the official LiveCodeBench and EvalScope on `release_v6`, still verifying the exact figures.
