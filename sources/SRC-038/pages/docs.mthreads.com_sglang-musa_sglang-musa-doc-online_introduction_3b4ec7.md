source: https://docs.mthreads.com/sglang-musa/sglang-musa-doc-online/introduction

# 产品简介

SGLang-MUSA 是面向摩尔线程 MUSA 架构的高性能推理框架适配方案。它让开发者无需修改代码或使用第三方分支，即可在摩尔线程全功能 GPU 上直接调用 SGLang 的高性能特性，实现了从底层硬件到上层应用生态的无缝衔接与“开箱即用”。

## 核心能力[](https://docs.mthreads.com#核心能力)

SGLang-MUSA 支持 Qwen、DeepSeek、GLM、Kimi 等 LLM/VLM 模型，以及 Wan、Qwen-Image 等 Diffusion 模型；基于 MCCL 后端，支持 TP/PP/DP/EP（含 DeepEP）与 PD 分离（Mooncake KV Transfer）；Attention层支持 FA3/MATE 原生路径并可安全 Fallback；提供 MUSA Graph 及 HiCache 能力，FP8 W8A8 Block 量化支持，以及 DeepGEMM 兼容层加速 MoE 权重计算。绝大部分 PR 已合入 SGLang 社区主干，并持续向上游回推。

## 技术架构[](https://docs.mthreads.com#技术架构)

SGLang-MUSA 采用多层兼容及运行时抽象的设计，让 SGLang 生态在 MUSA 硬件上无侵入运行。

兼容层以 torch_musa/torchada 为基础，通过 import torchada 统一拦截 CUDA API 调用重定向到 MUSA 后端，替代早期侵入式的散点修补，显著降低上游合入阻力。SGLang Runtime 内部通过多平台分发与 MultiPlatformOp 机制实现算子路由。

算子加速层以 MATE（MUSA AI Tensor Engine）为核心，提供与 FlashAttention 3 / SageAttention / FlashMLA / DeepGEMM 兼容的封装 API。 分布式侧增强 MTLink 检测与 Custom AllReduce，并与 Mooncake 协作完成跨节点 PD 分离的 KV Transfer。整体架构兼顾主干可回推与 MUSA 原生性能路径两条主线。