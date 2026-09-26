# [Issue #4642] [CAKE] Training Kernel Progress Tracker (Forward & Backward)

source: https://github.com/flashinfer-ai/flashinfer/issues/4642
state: open | updated: 2026-09-24T02:52:26Z
labels: needs-triage, op: misc, op: linear attention

## 正文

Training kernels deserve the whole CAKE, not just a forward slice. This issue tracks CAKE-generated kernels for end-to-end training workloads, with forward and backward paths baked together.

Have a training hotspot you want us to bake? Leave a comment or create a sub-issue with the operator, shapes, dtype, layout, target GPU, and baseline. We will put it in the oven! 🍰🔥

## Pull requests

### Linear attention

#### Recurrent KDA backward

- #5028 — fix the C16 forward triangular-matrix orientation in the recurrent KDA training implementation.

- #4636
- #4726 

#### Chunked KDA training backward

- #5376 — deterministic chunked training backward (chunk 64, K = V = 128, in-kernel Q/K L2 norm, lower-bound safe gate, sigmoid beta, `dt_bias`) for SM100a and SM103a: bit-identical repeated backward, 1.2–3.6x vs the flash-linear-attention v0.5.2 Triton backward on the Kimi K3 production rows

### Activation / quantization

#### Fused SwiGLU + MXFP8 quantization

- #4638 — fused forward and backward rowwise/colwise MXFP8 quantization for SM100a and SM103a

## 评论 (2)

### haok1402 · 2026-08-23

@yyihuang Thanks for bringing CAKE into the training workloads :-)

Is context parallelism something being considered for these training kernels where applicable (e.g. KDA)? Sharding long sequences across devices needs the kernel to expose a little more, and I am not sure the current interface has the granularity for a multi-device operator to be built on top of it. Curious whether that is in scope here, or meant to live in the framework layer.

### yyihuang · 2026-08-29

> [@yyihuang](https://github.com/yyihuang) Thanks for bringing CAKE into the training workloads :-)
> 
> Is context parallelism something being considered for these training kernels where applicable (e.g. KDA)? Sharding long sequences across devices needs the kernel to expose a little more, and I am not sure the current interface has the granularity for a multi-device operator to be built on top of it. Curious whether that is in scope here, or meant to live in the framework layer.

Hi @haok1402. We would welcome any new kernel requests! Feel free to raise a github issue with kernels + shapes/workloads you're interested in.
