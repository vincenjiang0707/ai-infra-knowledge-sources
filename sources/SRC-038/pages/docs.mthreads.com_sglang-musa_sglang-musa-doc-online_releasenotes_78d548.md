source: https://docs.mthreads.com/sglang-musa/sglang-musa-doc-online/releasenotes

# 版本发布信息

## SGLang-MUSA v0.5.12/13[](https://docs.mthreads.com#sglang-musa-v051213)

### 镜像地址[](https://docs.mthreads.com#镜像地址)

| 适用模型 | CPU 平台 | 镜像地址 |
|---|---|---|
| GLM-5.1,5.2,5.3 | Intel/AMD | `registry.mthreads.com/devtech/glm5.2:2.3.0-20260830` |
| GLM-5.1,5.2,5.3 | Hygon | `registry.mthreads.com/mcconline/inference/sglang:glm5.2-2.3.0-hygon-20260915` |
| DeepSeek-V4-Flash，V4-Flash-0731 | Intel/AMD | `registry.mthreads.com/devtech/sglang-dsv4:3.1-20260907` |
| DeepSeek-V4-Flash，V4-Flash-0731 | Hygon | `registry.mthreads.com/mcconline/inference/sglang:dsv4-3.1-hygon-20260915` |
| Qwen系列, Minimax-M3, Kimi-K2.5/2.6 及其他模型 | Intel/AMD | `registry.mthreads.com/mcconline/inference/sglang:v0.5.12.post1-ph1-4.3.5-torch2.9.0-20260805` |
| Qwen系列, Minimax-M3, Kimi-K2.5/2.6 及其他模型 | Hygon | `registry.mthreads.com/mcconline/inference/sglang:v0.5.12.post1-ph1-hygon-4.3.5-torch2.9.0-20260810-1700` |

-
GLM 及 DeepSeek-V4 对应的镜像基于社区 SGLang 0.5.13 版本优化。

-
Qwen系列, Minimax-M3, Kimi-K2.5/2.6 及其他模型对应的镜像基于社区 SGLang 0.5.12.post1 版本优化。


### 功能特性[](https://docs.mthreads.com#功能特性)

-
新增 GLM-5.2 & GLM-5.3 模型优化，提供长上下文能力，支持 FP8 KV Cache，同显存占用下提升缓存 token 数和并发上限。

-
新增 DeepSeek-V4-Flash 模型优化，支持自投机解码，Online Compress，BF16 Compress State，融合压缩算子及 L1 前缀缓存 （radix-cache）。

-
新增 Qwen 3.6 模型优化，Qwen3-VL vision 路径增强，支持 vision QKV unpack 与 rope 融合。

-
新增 MiniMax-M3 模型优化，支持 MUSA Triton block-sparse attention（MSA）。

-
新增 Beam Search 支持，OpenAI 入口、scheduler、tokenizer/detokenizer 全链路打通。

-
补齐 MUSA deterministic inference 支持，包含 TP 场景、RNG seed、sampler / dispatch 相关修复。

-
MUSA kernel 与量化优化：新增 top-k renorm kernel，compact masked activation quant path，DeepSeek V4 FP8 / indexer / group quant / decode 相关 kernel 性能增强，MoE 相关算子优化。

-
通信与并行能力增强：新增 MUSA custom all-gather parallel-source path，优化 custom all-reduce + RMSNorm fusion

-
稳定性与可用性修复：修复 fused MRoPE KV cache 写入、单组 topk 路由、Qwen3.5 MTP shared expert 等问题，修复 / 加固 PP 与 TP 通信、空 collective、sampling seed 等问题。


## SGLang-MUSA v0.5.6.post3[](https://docs.mthreads.com#sglang-musa-v056post3)

### 镜像链接[](https://docs.mthreads.com#镜像链接)

`# Intel/AMD 平台`

registry.mthreads.com/mcconline/inference/sglang:v0.5.6.post3-ph1-4.3.5-torch2.9.0-20260605

# Hygon 平台

registry.mthreads.com/mcconline/inference/sglang:v0.5.6.post3-ph1-4.3.5-torch2.9.0-20260604-hygon



### 功能特性[](https://docs.mthreads.com#功能特性-1)

-
**深度适配主流开源大模型：**支持 GLM，Kimi，Qwen，DeepSeek 系列模型，并在 PD 分离架构下的性能进行深度优化。 -
**PD 分离部署：**支持 Prefill/Decode 节点分离部署，通过 RDMA 实现高效 KV Cache 传输，适用于大规模 MoE 模型的高吞吐场景，支持多种实例配比。 -
**并行策略：**支持张量并行 (TP)、流水线并行 (PP)、专家并行 (EP) 以及数据并行 (DP) Attention。 -
**精度支持：**全面支持**FP8**精度推理，在保证精度的前提下显著降低显存占用。 -
**DeepEP MoE 加速：**集成 DeepEP normal/low_latency 模式，支持 EP (Expert Parallelism) + DP Attention 高效分布式推理。 -
**FlashAttention 3：**attention-backend 与 mm-attention-backend 均采用 FA3，提升 Attention 计算效率。 -
**DeepGEMM：**MoE Runner 使用 DeepGEMM 后端，优化 MoE 层矩阵运算性能。 -
**EAGLE3 投机采样：**部分模型支持 EAGLE3 投机采样，加速解码速度。 -
**MUSA Graph 优化：**支持细粒度 MUSA Graph BS 配置，降低 kernel launch 开销。 -
**静态 EPLB (Expert-Level Load Balancing)：**Prefill/Decode 节点支持静态专家负载均衡。