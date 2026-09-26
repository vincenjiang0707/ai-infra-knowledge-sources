# [Issue #140] Support using models from HuggingFace directly

source: https://github.com/AI-Hypercomputer/JetStream/issues/140
state: open | updated: 2024-10-30T23:18:50Z
labels: 

## 正文

I should be able to serve a model by simply providing the HuggingFace model ID. Requiring users to convert checkpoints is too troublesome.

## 评论 (2)

### vipannalla · 2024-10-30

Thanks for the feedback. This feature is currently not supported, but we have added it to our roadmap to simplify. Some models (such as LLama variants) need explicit acknowledgements from Meta's site before you can use them.

### samos123 · 2024-10-30

That can be handled by respecting HF_TOKEN environment variable to automatically download auth gated models. That's how vLLM and other OSS does it.
