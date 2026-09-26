# [Issue #1151] [Question] Why choose `guidellm` instead of `vllm bench` for speculator evaluation?

source: https://github.com/vllm-project/speculators/issues/1151
state: open | updated: 2026-09-22T18:42:55Z
labels: 

## 正文

Hi Authors,

I'm curious about the design choice of using `guidellm` for speculative decoding evaluation.

In my testing, `vllm bench` already supports key metrics like acceptance length, position-wise acceptance, TTFT/TPOT, and throughput. Switching to `vllm bench` alone would seem to reduce both code complexity and dependencies.

Are there specific technical reasons (e.g., metric consistency, guided generation support, or fairness in comparison) for preferring `guidellm` in this context?

Thanks for clarifying!

## 评论 (1)

### fynnsu · 2026-09-22

Hi, this is partly for historical reasons because `vllm bench` didn't support the metric collection / datasets we wanted.

We could compare `vllm bench` and see if it is a viable alternative. We are also putting in some work to improve our eval suite which includes switching to per-request specdec metric collection, and adding long-context benchmark tasks. I'm not sure if all of this is already well supported by vllm bench. 
