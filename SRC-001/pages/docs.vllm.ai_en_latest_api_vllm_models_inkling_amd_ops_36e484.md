source: https://docs.vllm.ai/en/latest/api/vllm/models/inkling/amd/ops/
lastmod: 2026-09-23

#

`vllm.models.inkling.amd.ops`

[¶](https://docs.vllm.ai#vllm.models.inkling.amd.ops)

Inkling kernels (NVIDIA).

`rmsnorm`

/ `sconv`

import eagerly. The SwiGLU kernels and the FA4 relative-attention wrapper are exposed lazily to keep this package's import path lightweight.

Modules:

-
–[fa4_rel_attention](https://docs.vllm.ai/fa4_rel_attention/#vllm.models.inkling.amd.ops.fa4_rel_attention)ROCm paged attention with Inkling's query-dependent relative bias.

-
–[fa4_warmup](https://docs.vllm.ai/fa4_warmup/#vllm.models.inkling.amd.ops.fa4_warmup)Compatibility shim for the ROCm relative-attention implementation.

-
–[gluon](https://docs.vllm.ai/gluon/#vllm.models.inkling.amd.ops.gluon)GFX950-only Gluon relative-attention kernels for Inkling.

-
–[norm](https://docs.vllm.ai/norm/#vllm.models.inkling.amd.ops.norm) -
–[rel_attention_decode](https://docs.vllm.ai/rel_attention_decode/#vllm.models.inkling.amd.ops.rel_attention_decode)Split-KV decode for Inkling relative attention on ROCm.

-
–[sconv](https://docs.vllm.ai/sconv/#vllm.models.inkling.amd.ops.sconv)Inkling short-convolution kernels backed by a paged sliding-window state cache.

-
–[silu_and_mul](https://docs.vllm.ai/silu_and_mul/#vllm.models.inkling.amd.ops.silu_and_mul)SwiGLU kernels for the Inkling MLP layers.