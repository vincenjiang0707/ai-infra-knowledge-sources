source: https://docs.vllm.ai/en/latest/api/vllm/models/inkling/nvidia/ops/
lastmod: 2026-09-24

#

`vllm.models.inkling.nvidia.ops`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.ops)

Inkling kernels (NVIDIA).

`rmsnorm`

/ `sconv`

import eagerly. The SwiGLU kernels and the FA4 relative-attention wrapper are exposed lazily to keep this package's import path lightweight.

Modules:

-
–[fa4_rel_attention](https://docs.vllm.ai/fa4_rel_attention/#vllm.models.inkling.nvidia.ops.fa4_rel_attention) -
–[lamport](https://docs.vllm.ai/lamport/#vllm.models.inkling.nvidia.ops.lamport)Deadlock-free fused RS + short-conv + AG + residual + RMSNorm.

-
–[mm_towers](https://docs.vllm.ai/mm_towers/#vllm.models.inkling.nvidia.ops.mm_towers)Fused CUDA kernels for the Inkling vision/audio towers.

-
–[norm](https://docs.vllm.ai/norm/#vllm.models.inkling.nvidia.ops.norm) -
–[sconv](https://docs.vllm.ai/sconv/#vllm.models.inkling.nvidia.ops.sconv)Inkling short-convolution kernels backed by a paged sliding-window state cache.

-
–[silu_and_mul](https://docs.vllm.ai/silu_and_mul/#vllm.models.inkling.nvidia.ops.silu_and_mul)SwiGLU kernels for the Inkling MLP layers.