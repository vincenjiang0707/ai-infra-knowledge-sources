# [Issue #6202] Support `LogitsPostProcessorConfig` in Triton Backend

source: https://github.com/NVIDIA/TensorRT-LLM/issues/6202
state: open | updated: 2026-09-01T06:48:28Z
labels: feature request, Community want to contribute, stale, Community Engagement

## 正文

https://github.com/NVIDIA/TensorRT-LLM/blob/98428f330e2f1d1b5606ca55ec4d30f0970dcab4/triton_backend/inflight_batcher_llm/src/model_instance_state.cc#L697

`LogitsPostProcessorConfig` is currently hardcoded to null. Please add support for logits so that we users can set it in config.pbtxt

If a maintainer can give pointers, I can implement this change and raise a PR.

Thank you.

## 评论 (9)

### SimengLiu-nv · 2025-07-22

Hi @devm777 , thank you for your interest in contribution! 
Reference for Log usage: [test_logits_post_processor](https://github.com/NVIDIA/TensorRT-LLM/blob/b7c8a672da7709dd8847e7861028168c661f9fda/tests/unittest/bindings/test_executor_bindings.py#L1854)
Reference for triton_backend implementation: you can check the code changes related to `decodingConfig`. 


### devm777 · 2025-07-22

Hi @SimengLiu-nv, thanks for that resource. I have one more question: how will the user specify logit processor functions in `config.pbtxt`?

### SimengLiu-nv · 2025-07-22

> Hi [@SimengLiu-nv](https://github.com/SimengLiu-nv), thanks for that resource. I have one more question: how will the user specify logit processor functions in `config.pbtxt`?

I am unaware of ways to do that throught `config.pbtxt`.
One work-around I can think of is to use the LLMAPI model and add the lambda function as string to the model config [yaml](https://github.com/NVIDIA/TensorRT-LLM/blob/main/triton_backend/all_models/llmapi/tensorrt_llm/1/model.yaml) and eval it later to construct the  `LogitsPostProcessorConfig`.

### karljang · 2025-11-04

@devm777 , were you able to resolve your question regarding LogitsPostProcessorConfig? Just checking in to see if this issue is still relevant for you.

### devm777 · 2025-11-05

Hi @karljang, unfortunately there is still no way to specify `LogitsPostProcessorConfig` in Triton backend which makes it impossible to do things like token biasing. So this issue is still very much relevant

### karljang · 2025-11-14

Discussing it with the team~

### github-actions[bot] · 2025-11-29

Issue has not received an update in over 14 days. Adding stale label.

### github-actions[bot] · 2025-12-13

This issue was closed because it has been 14 days without activity since it has been marked as stale.

### harshal-96 · 2026-09-01

Hi @SimengLiu-nv, I picked this up and submitted #18507: named logits post-processors declared in the LLMAPI model.yaml (python import specs, not eval'ed lambdas) and selected per request via a new optional sampling_param_logits_post_processor_name input, routed into SamplingParams(logits_processor=...). Covered by CPU unit tests. Feedback welcome.
