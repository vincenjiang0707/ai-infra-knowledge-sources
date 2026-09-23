source: https://docs.vllm.ai/en/latest/api/vllm/models/inkling/nvidia/mlp/
lastmod: 2026-09-23

#

`vllm.models.inkling.nvidia.mlp`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.mlp)

Inkling dense SwiGLU MLP (also used as the MoE shared expert).

The checkpoint stores the gate/up projection as a single fused, *interleaved* weight (`[gate0, up0, gate1, up1, ...]`

), so we use a plain `ColumnParallelLinear`

whose contiguous row-sharding keeps each gate/up pair together, and an interleaved SwiGLU activation.