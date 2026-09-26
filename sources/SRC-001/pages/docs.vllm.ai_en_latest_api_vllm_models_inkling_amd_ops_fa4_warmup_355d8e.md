source: https://docs.vllm.ai/en/latest/api/vllm/models/inkling/amd/ops/fa4_warmup/
lastmod: 2026-09-24

#

`vllm.models.inkling.amd.ops.fa4_warmup`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.ops.fa4_warmup)

Compatibility shim for the ROCm relative-attention implementation.

ROCm uses a Triton kernel which is compiled by vLLM's normal model warmup. The NVIDIA path registers ahead-of-time CuTeDSL units; importing that provider on ROCm would pull in CUDA-only tml-fa4 code.

Functions:

-
–[register_fa4_warmup](https://docs.vllm.ai#vllm.models.inkling.amd.ops.fa4_warmup.register_fa4_warmup)Triton compilation is triggered by the ordinary vLLM warmup forward.