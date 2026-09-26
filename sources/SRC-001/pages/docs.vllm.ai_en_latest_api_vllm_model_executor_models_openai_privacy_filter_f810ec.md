source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/openai_privacy_filter/
lastmod: 2026-09-24

#

`vllm.model_executor.models.openai_privacy_filter`

[¶](https://docs.vllm.ai#vllm.model_executor.models.openai_privacy_filter)

Inference-only OpenAI Privacy Filter model.

gpt-oss reused as a bidirectional encoder for token classification: every layer runs non-causal attention with a banded ±sliding_window mask, and the LM head is replaced with a 33-class BIOES score head.