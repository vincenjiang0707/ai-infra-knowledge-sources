source: https://docs.vllm.ai/en/latest/api/vllm/models/inkling/amd/
lastmod: 2026-09-23

#

`vllm.models.inkling.amd`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd)

Modules:

-
–[attention](https://docs.vllm.ai/attention/#vllm.models.inkling.amd.attention) -
–[layernorm](https://docs.vllm.ai/layernorm/#vllm.models.inkling.amd.layernorm)Inkling RMSNorm (no bias, weight-scaled), backed by the vendored Triton kernel.

-
–[logits_processor](https://docs.vllm.ai/logits_processor/#vllm.models.inkling.amd.logits_processor)Inkling logits processor (muP + LoRA aware).

-
–[mlp](https://docs.vllm.ai/mlp/#vllm.models.inkling.amd.mlp)Inkling dense SwiGLU MLP (also used as the MoE shared expert).

-
–[model](https://docs.vllm.ai/model/#vllm.models.inkling.amd.model)Inkling model implementation for AMD GPUs.

-
–[moe](https://docs.vllm.ai/moe/#vllm.models.inkling.amd.moe)Inkling mixture-of-experts on vLLM's MoERunner abstraction.

-
–[mtp](https://docs.vllm.ai/mtp/#vllm.models.inkling.amd.mtp)Inkling MTP (Multi-Token Prediction) draft model (NVIDIA).

-
–[ops](https://docs.vllm.ai/ops/#vllm.models.inkling.amd.ops)Inkling kernels (NVIDIA).

-
–[sconv_swa_attn](https://docs.vllm.ai/sconv_swa_attn/#vllm.models.inkling.amd.sconv_swa_attn)Inkling short-conv state managed as a sliding-window KV cache.

-
–[short_conv](https://docs.vllm.ai/short_conv/#vllm.models.inkling.amd.short_conv)Inkling short convolution: depthwise causal conv1d (+ residual) over a paged