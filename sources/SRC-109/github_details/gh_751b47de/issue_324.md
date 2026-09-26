# [Issue #324] Feature request

source: https://github.com/triton-inference-server/perf_analyzer/issues/324
state: closed | updated: 2025-05-14T21:01:13Z
labels: 

## 正文

Is possible to add a new backend? I want to run the GenAI-Perf with Hugging Face Inference API

## 评论 (2)

### debermudez · 2025-03-10

The docs located [here](https://github.com/triton-inference-server/perf_analyzer/blob/main/genai-perf/docs/customizable_frontends.md) should help guide you to adding the implementation yourself. We can review it and add it to the codebase.



### nv-hwoo · 2025-05-14

Closing due to inactivity.

Also, if you mean Huggingface Text Generation Inference (TGI) API, then GenaAI-Perf already supports it: https://github.com/triton-inference-server/perf_analyzer/blob/main/genai-perf/docs/huggingface_tgi.md
