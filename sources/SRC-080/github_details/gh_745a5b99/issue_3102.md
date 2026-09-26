# [Issue #3102] [Question] Is 3-bit Quantization (AWQ/GPTQ) Supported?

source: https://github.com/vllm-project/llm-compressor/issues/3102
state: closed | updated: 2026-09-09T02:04:10Z
labels: 

## 正文

1. Does the current version of llm-compressor officially support generating 3-bit AWQ or 3-bit GPTQ quantized models?
2. If supported, are the resulting quantized models compatible with the vLLM inference engine?

I just want to get it running; performance is not a concern for me.

## 评论 (1)

### dsikka · 2026-08-27

Hey @Mandaluoren - yes, you can see all supported schemes here: https://github.com/vllm-project/compressed-tensors/blob/0655ae80474380870d7fd849ae54fa8fb4f6ca5b/src/compressed_tensors/quantization/quant_scheme.py#L281

Within vLLM, these should be runnable through the Humming kernel integrations:

1. For weight-only: https://github.com/vllm-project/vllm/blob/d1e5e66ee30ba4bc020ac8e14b05e7a8c41b9302/vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16.py#L51
2. For 4 or 8 bit activations: https://github.com/vllm-project/vllm/blob/d1e5e66ee30ba4bc020ac8e14b05e7a8c41b9302/vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa4.py#L47
