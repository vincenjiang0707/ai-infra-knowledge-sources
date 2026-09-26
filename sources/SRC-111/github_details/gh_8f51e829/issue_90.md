# [Issue #90] Integrate lm-eval into GuideLLM

source: https://github.com/vllm-project/guidellm/issues/90
state: closed | updated: 2026-06-08T16:52:41Z
labels: internal

## 正文

**Description**
We've talked about adding in [lm-eval ](https://github.com/EleutherAI/lm-evaluation-harness)to become a native pathway in GuideLLM to enable developers to run both benchmarks and accuracy evaluations in just one tool. This ticket will outline the necessary work to integrate lm-eval into GuideLLM. 

**Acceptance Criteria**
- Package up the lm-eval-harness library into GuideLLM
- Create new command: guidellm-eval that can then take the same input parameters as lm-eval:
- - model hf \
- - model_args pretrained=EleutherAI/gpt-j-6B \
- - tasks hellaswag \
- - device cuda:0 \
- - batch_size 8

## 评论 (2)

### markurtz · 2025-05-13

@jennyyangyi-magic to scope this out a bit more and update

### dbutenhof · 2026-06-08

Not currently planned.

Eval Hub is integrating GuideLLM into their workflow. Not clear exactly what we can practically offer beyond that.
