# [Issue #70] LiteLLM Integeration & Batch Call Interface

source: https://github.com/ScalingIntelligence/KernelBench/issues/70
state: closed | updated: 2025-11-19T02:24:16Z
labels: help wanted

## 正文

I wrote a very manual LLM inference engine system for the initial version of KernelBench.

Two things we should do to better integrate 
* Use `litellm` and `.env` so we can support a variety of future models and not writing a new backend for each
* For `pass@k` and test-time compute settings, we should use the batch call API to simultaneously call rather than a thread of each.

Will implement with team @pythonomar22 @nathanjpaek @AffectionateCurry .

## 评论 (1)

### simonguozirui · 2025-11-09

#78 added LiteLLM support. 

leaving batch call for future PRs, contributions welcomed.
