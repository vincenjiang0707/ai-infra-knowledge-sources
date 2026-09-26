source: https://docs.vllm.ai/en/latest/api/vllm/models/inkling/nvidia/
lastmod: 2026-09-24

#

`vllm.models.inkling.nvidia`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia)

Modules:

-
–[attention](https://docs.vllm.ai/attention/#vllm.models.inkling.nvidia.attention) -
–[layernorm](https://docs.vllm.ai/layernorm/#vllm.models.inkling.nvidia.layernorm)Inkling RMSNorm (no bias, weight-scaled), backed by the vendored Triton kernel.

-
–[logits_processor](https://docs.vllm.ai/logits_processor/#vllm.models.inkling.nvidia.logits_processor)Inkling logits processor (muP + LoRA aware).

-
–[mlp](https://docs.vllm.ai/mlp/#vllm.models.inkling.nvidia.mlp)Inkling dense SwiGLU MLP (also used as the MoE shared expert).

-
–[model](https://docs.vllm.ai/model/#vllm.models.inkling.nvidia.model)Inkling model implementation for NVIDIA GPUs.

-
–[moe](https://docs.vllm.ai/moe/#vllm.models.inkling.nvidia.moe)Inkling mixture-of-experts on vLLM's FusedMoE abstraction.

-
–[mtp](https://docs.vllm.ai/mtp/#vllm.models.inkling.nvidia.mtp)Inkling MTP (Multi-Token Prediction) draft model (NVIDIA).

-
–[ops](https://docs.vllm.ai/ops/#vllm.models.inkling.nvidia.ops)Inkling kernels (NVIDIA).

-
–[sconv_swa_attn](https://docs.vllm.ai/sconv_swa_attn/#vllm.models.inkling.nvidia.sconv_swa_attn)Inkling short-conv state managed as a sliding-window KV cache.

-
–[short_conv](https://docs.vllm.ai/short_conv/#vllm.models.inkling.nvidia.short_conv)Inkling short convolution: depthwise causal conv1d (+ residual) over a paged