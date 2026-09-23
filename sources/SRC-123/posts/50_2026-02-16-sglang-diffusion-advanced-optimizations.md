# 2026-02-16-sglang-diffusion-advanced-optimizations

source: https://lmsys.org/blog/2026-02-16-sglang-diffusion-advanced-optimizations

# SGLang-Diffusion: Advanced Optimizations for Production-Ready Video Generation

Following our [two-month progress update](https://lmsys.org/blog/2026-01-16-sglang-diffusion/), we're excited to share a
deeper dive into the advanced optimizations that make SGLang-Diffusion a production-ready framework for video
generation. These improvements focus on scalability, efficiency, and stability—essential for deploying diffusion models
at scale.

Here's what we've been working on:

## Overview

As video generation models continue to grow in complexity, we've identified and addressed critical bottlenecks across the entire inference pipeline:

**Smarter Parallelism**: Token-level sequence sharding and parallel folding for optimal resource utilization**Distributed VAE**: Parallel encoding/decoding to eliminate memory bottlenecks for high-resolution video**Production-Ready Serving**: Fixed Cache-DiT integration bugs for stable multi-request serving**Optimized I/O**: Accelerated video save operations by eliminating unnecessary serialization**Fused Kernels**: Custom JIT kernels for LayerNorm variants, reducing GPU bubbles

Let's dive into the technical details.

## Key Improvements

### 1. SP-Sharding Improvement: From Frame-Level to Token-Level

For Video DiT models, input tensors typically have shape `B, T, H, W, C`

. For a common configuration with
`num_frames=81`

, this might be: `1, 21, 90, 160, 3`

.

In an 8×H100 setup with Ulysses Sequence Parallel (N=8), the framework needs to shard along the sequence dimension during non-attention operations, then use all-to-all communication to switch to head dimension sharding for attention.

#### Previous Approach: Frame-Level Sharding

Our initial implementation sharded directly along the `T`

(temporal) dimension. However, 21 frames cannot be evenly
divided by 8 GPUs, leading to two suboptimal solutions:

**Adjust-frame**: Modify`num_frames`

during preprocessing to make T divisible by N**Token Padding**: Pad the temporal dimension to the next multiple of N (21 → 24)

The frame-level padding approach introduces significant overhead: each padded token requires `H × W × C`

redundant
computations.

#### New Approach: Token-Level Sharding

To minimize padding overhead, we now **flatten T × H × W into a single sequence dimension** before sharding. This has
two major benefits:

**Reduced or Zero Padding**: For common resolutions and VAE configurations,`H × W`

is often divisible by 8, eliminating padding entirely**Lower Communication Volume**: When padding is needed, the overhead is minimal compared to frame-level padding

### Comparison: Shape and Comm Volume Analysis

| Solution | Padding Overhead | Input Tensor Shape (Per-rank) | All-to-All Comm Volume |
|---|---|---|---|
Frame Sharding | 3 frames (14.3%) | `3, 90, 160, C` (24/8) | `1.0 × feature_map` |
Token Sharding | 0 frames | `2.625, 90, 160, C` (21/8) | `0.875 × feature_map` |

This optimization delivers both faster communication and reduced memory footprint, especially for video models.

See related [PR](https://github.com/sgl-project/sglang/pull/18161) for technical details.

### 2. Parallel Folding: Decoupling Text Encoder and DiT Parallelism

In our original implementation, the Text Encoder and DiT shared the same Tensor Parallel (TP) group. When DiT used only Sequence Parallel (SP), this meant the Text Encoder ran with TP=1—each GPU held a complete model copy, wasting memory and compute.

Since Text Encoder and DiT computations are **completely decoupled**, we introduced **Parallel Folding**: the Text
Encoder now uses the DiT's SP group as its TP group.

**What this means in practice:**

**For Text Encoder**: Apply TP across the SP group to maximize speed and reduce memory**For Denoiser**: Apply SP to optimize throughput and memory for sequence processing

This approach ensures both components use optimal parallelism strategies without interference, improving overall efficiency.

See related [PR](https://github.com/sgl-project/sglang/pull/17818) for technical details.

### 3. Parallel VAE: Distributed Encoding/Decoding

VAE encoding/decoding involves heavy 3D convolution operations. For high-resolution video, single-GPU implementations are slow and prone to OOM.

The two common approaches to alleviate this are:

**Tiling**: Split feature maps into tiles, process them sequentially—reduces peak memory but increases latency**Parallel**: Distribute tiles across GPUs for concurrent processing—reduces both peak memory and latency

We implemented **Parallel VAE** for Wan-VAE with the following strategy:

**Height-wise Sharding**: Split feature maps along the height dimension across ranks**Conv Operations**: Use`halo_exchange`

to share boundary pixels between neighboring ranks (P2P), ensuring mathematical equivalence with global convolution**Attention Operations**: Use`all_gather`

for global context when needed**Result Aggregation**:`all_gather`

to reconstruct full height at the end of encoding/decoding

This approach eliminates VAE as a bottleneck for high-resolution video generation, enabling higher resolutions and longer sequences without OOM.

### 4. Serving with Cache-DiT: Fixing Multi-Request Stability

[Cache-DiT](https://github.com/vipshop/cache-dit) in SGLang-Diffusion accelerates inference by caching residuals and
skipping redundant
computations. However, its correct operation depends on proper `num_inference_steps`

configuration, which determines
step counting and the Selective Computation Mask (SCM).

**The Problem:**

Wan2.2 uses a dual-transformer architecture, where `transformer`

and `transformer_2`

execute `num_high_noise_steps`

and
`num_low_noise_steps`

respectively (summing to `num_inference_steps`

). Our initial implementation had two critical bugs:

- Both transformers incorrectly used total
`num_inference_steps`

to configure their cache contexts - In serving mode, cache contexts persisted across requests, even when different requests used different
`num_inference_steps`


These issues caused incorrect step counting and cache buffer contamination. When consecutive requests had different
video shapes, cache buffers would encounter shape mismatches, **crashing the server**.

**Our Solution:**

`transformer`

and`transformer_2`

now use`num_high_noise_steps`

and`num_low_noise_steps`

respectively to configure independent cache contexts- For each new request, we recalculate timestep splits and
**refresh**cache contexts using Cache-DiT's API, completely isolating requests

This ensures stable, production-ready serving with Cache-DiT acceleration.

### 5. Optimize Video Save: Eliminating Serialization Overhead

In our serving architecture, `scheduler_client`

and `gpu_worker`

communicate via ZMQ.

Previously, `gpu_worker`

would:

- Complete inference
- Serialize output tensor
- Send tensor to
`scheduler_client`

via ZMQ `scheduler_client`

deserializes tensor`scheduler_client`

processes tensor and saves video

This introduced significant overhead from serialization/deserialization and memory copies.

**Our Solution:**

`gpu_worker`

now directly processes the output tensor and saves the video to disk, returning only the file path to
`scheduler_client`

.

This eliminates serialization/deserialization overhead, while avoiding duplicate tensor copies.

### 6. WanVideo LayerNorm Fusion: CuTeDSL JIT Kernels

WanVideo introduces two specialized LayerNorm patterns:

-
**LayerNormScaleShift**:`y = LN(x) * (1 + scale) + shift`

-
**ScaleResidualLayerNormScaleShift**:`residual_out = residual + gate * x`

`y = LN(residual_out) * (1 + scale) + shift`



These patterns combine elementwise operations with normalization reductions. Implementing them as separate kernels would introduce multiple kernel launches and intermediate memory traffic, creating GPU bubbles.

**Our Solution:**

We implemented **fused JIT kernels** using CuTeDSL (located in [ sglang/jit_kernel/diffusion/cutedsl](https://github.com/sgl-project/sglang/tree/main/python/sglang/jit_kernel/diffusion/cutedsl)) that combine
these operations into single, efficient kernels.

**Benefits:**

**Fewer Kernel Launches**: Reduced launch overhead**Lower Memory Traffic**: Eliminates intermediate reads/writes**Better GPU Utilization**: Reduces bubbles and improves throughput

These micro-optimizations add up, especially for multi-layer architectures like WanVideo.

## Performance Results

Here's a comparison of SGLang-Diffusion and LightX2V for Wan2.2 T2V under different settings:

## What's Next

We continue to push the boundaries of diffusion model serving. Please refer to [ SGLang-Diffusion's Roadmap for 26Q1](https://github.com/sgl-project/sglang/issues/18286) for more details.

Stay tuned for more updates as we continue to optimize SGLang-Diffusion for production deployments.

## Acknowledgment

- We would like to thank the following contributors for their work on these optimizations:
**Skywork.ai,**[Song Rui](https://github.com/Songrui625), SGLang-Diffusion Team - Special thanks to our compute partners for their continued support.

Try diffusion generation, proudly powered by SGLang-Diffusion: [APIFree](https://www.apifree.ai/home)

## Learn More

**Slack channel**:[#diffusion](https://sgl-fru7574.slack.com/archives/C09P0HTKE6A)(join via slack.sglang.io)**Cookbook for SGLang-Diffusion****Documentation on SGLang-Diffusion****Previous Update: Two Months In**
