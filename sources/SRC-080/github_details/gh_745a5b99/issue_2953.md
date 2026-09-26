# [Issue #2953] AWQ: no architecture mappings for looped/weight-shared models (NanbeigeForCausalLM) + OOM on the basic pipeline

source: https://github.com/vllm-project/llm-compressor/issues/2953
state: closed | updated: 2026-07-24T17:04:38Z
labels: good first issue

## 正文

## Summary
AWQModifier cannot run against `Nanbeige/Nanbeige4.2-3B` (looped transformer, `num_loops=2`, Qwen3-style module naming) in llm-compressor 0.12.0:

1. **Sequential pipeline**: resolves zero AWQ mappings for the architecture (module-name patterns don't match), so nothing is smoothed. Notably the sequential tracer handles the looped forward itself fine.
2. **Basic pipeline**: OOMs on a 32GB card for this 3B model where GPTQ/RTN pipelines fit comfortably.

## Ask
The mapping registry appears to be the only real blocker for (1) — the arch uses standard q/k/v/o + gate/up/down naming, so a mapping contribution looks tractable. Is there a doc for authoring + validating a custom AWQMapping for an out-of-tree trust_remote_code arch? Happy to contribute the Nanbeige mapping if pointed at the intended extension path.

Context: on this architecture class quantization error compounds across loop passes, making activation-aware scaling particularly interesting; related GPTQ report: vllm-project/llm-compressor#2952.

## 评论 (4)

### brian-dellabetta · 2026-07-23

Hi @NullSense , mappings need to be added to registry for this to work. Will open as a good first issue

### f-baig · 2026-07-23

Happy to take this one

### brian-dellabetta · 2026-07-23

Hi @f-baig , thanks! assigned to you. 

### brian-dellabetta · 2026-07-24

the mappings have been added and look appropriate, but further issues are likely to arise related to the model's looped architecture. thread ongoing in #2952
