# [Issue #179] Token Efficiency Benchmarking

source: https://github.com/vllm-project/guidellm/issues/179
state: open | updated: 2026-09-10T20:04:22Z
labels: internal

## 正文

Benchmarks that crown the “best” reasoning LLMs routinely publish a single headline score, yet ignore how many tokens—and therefore how much time, energy, and money—the model spent to achieve that score. When practitioners must meet strict service‑level objectives (SLOs) for latency and cost, a system that needs five‑times more tokens per answer is rarely competitive, even if its accuracy is marginally higher. Recent work on agent evaluation has highlighted similar blind spots by arguing for cost‑controlled leaderboards and Pareto visualizations of accuracy versus dollars. Building on this insight, we must shift the focus from dollars to the more fundamental currency of inference: tokens.

Token Efficiency Benchmarking (TEB) will be a systematic framework that measures the quality–token trade‑off of reasoning LLMs and test‑time compute optimization techniques. For each model or technique, TEB will record 
(i) task‑level quality metrics—e.g., exact‑string accuracy on GSM‑8K or pass@k on HumanEval—and 
(ii) the total number of prompt, generation, and tool‑use tokens consumed to reach the reported score. 

The ask is for implementing TEB in guidellm.

cc @rgreenberg1 @sjmonson @markurtz @dagrayvid 

## 评论 (3)

### RagulMcodes · 2026-09-10

I'm interested in working on implementing the Token Efficiency Benchmarking (TEB) framework for guidellm as outlined here. Since this has been moved to the backlog, is it open for external contribution? If so, are there any specific design constraints I should follow before I get started?"

### sjmonson · 2026-09-10

This is on the backlog because it mostly falls outside the current scope of the GuideLLM project. It requires knowing both how much your hardware costs to run and how accurate the model is for your use-case. We interested in eventually looking into accuracy within GuideLLM, but it is first and foremost a performance benchmarking tool. Accuracy falls outside our expertise so its hard to outline all of the architectural needs, but at minimum we would want an experts opinion on any actual implementation and whatever implementation is created should not interfere with the normal performance benchmark pipeline.

### ashishkamra · 2026-09-10

> It requires knowing both how much your hardware costs to run and how accurate the model is for your use-case.

That's not accurate @sjmonson . There is no mention of hardware costs. The ask is to compute total tokens consumed when running certain accuracy benchmarks. But yes, GuideLLM currently does not support running accuracy benchmarks so that will probably the first contribution @RagulMcodes 
