# LMSYS

source: https://lmsys.org/blog/

Blog

Latest updates and releases by LMSYS Org are announced through our blogpost series.


Blog

Accelerating Long-Context and Agentic Inference with NVFP4 KV Cache

The KV cache is a fundamental building block of the modern LLM inference system. The context from multiple conversation rounds in agent sessions is cached as keys and values (KV) in GPU memory, allowi...


Blog

SGLang and Miles Add Day-0 Support for DeepSeek-V4.1

DeepSeek-V4.1 introduces several architecture choices that shape the serving stack.
Low-ratio compression and sliding-window attention (SWA). Each layer maintains an fp8 sliding-window cache for its ...


Blog

Running DeepSeek-V4-Flash and Kimi-K3 on Consumer Hardware with SSD Expert Pack

SGLang brings the core idea of SSD-LLaMA to MoE inference: keep routed experts that do not fit in VRAM and host RAM on an NVMe SSD, load only the experts selected by the router, and use Expert Pack la...


Blog

Infer-forge: Harness, Loop, and Graph Engineering Around SGLang

Inference optimization may look local in code, but its validity is global. A kernel, communication path, or scheduling change becomes meaningful only at a specific deployment point defined by the mode...


Blog

MiniMax-H3 on 8×H200: 1.95× Lossless, Up to 6.24× at 0.76–0.91 SSIM

We benchmarked MiniMax-H3 video generation on 8× NVIDIA
H200 with SGLang Diffusion, holding prompts,
seeds, resolution, frame rate, and denoising steps fixed across six workloads.
- SGLang's dense, l...


Blog

Qwen3.8-Flash-Next: Day-0 Support in SGLang

Today, the Qwen team open-sourced Qwen3.8-Flash-Next, a multimodal MoE model and an early preview of the Qwen4 architecture. It plays the same role for Qwen4 that Qwen3-Next played for Qwen3.5. The Ga...


Blog

Chasing the Batch-1 Floor: Ling-3.0-flash Speculative Decode on Blackwell

Batch-1 decode keeps getting more important. Xiaomi MiMo, for example, announced MiMo-V2.5-Pro UltraSpeed in June, claiming 1,000 tok/s decode on a one-trillion-parameter MoE model.
Batch 1 gives an ...


Blog

Fast Engine Recovery: Sub-Second Engine Restart for SGLang via Weight Cache Daemon

Nowadays, State-of-the-Art (SOTA) models are getting much bigger and reloading the model service after a crash is very expensive. Therefore, we are introducing the Weight Cache Daemon, a persistent GP...


Blog

Mooncake for Miles: From Fragmented Rollout Data to Efficient Bulk I/O

Reinforcement learning for large language models combines two very different workloads: rollout generation and model training.
During rollout, inference workers run the current policy on a set of pro...


Blog

Pushing the Limits of Serving DeepSeek-V4-Pro

DeepSeek-V4-Pro is a 1.6-trillion-parameter Mixture-of-Experts (MoE) model released with both FP8 and FP4 weights. Models at this scale naturally benefit from accelerators such as NVIDIA Blackwell GPU...


Blog

Miles v0.1: Production-level Post-training

We present Miles v0.1, a full-stack production-ready system for frontier post-training, the successor to our first Miles release. Building upon slime's clean design, Miles optimizes every stage in the...


Blog

Advanced CUDA Graph Techniques in SGLang

CUDA Graphs promise to remove kernel-launch overhead, but getting close to that benefit in a real inference engine requires graphing as much of the workload as possible without sacrificing compatibili...


Blog

SGLang and Miles Add Day-0 Support for Qwen3.8

We are excited to announce Day-0 support for Qwen3.8-2.4T-A95B in SGLang and Miles.
It is Qwen's largest open-source model, with 2.4T total parameters and 95B active per token,
and its hybrid attentio...


Blog

SGLang Adds Day-0 Support for NVIDIA Nemotron 3.5 Lightning

SGLang is excited to announce Day-0 support for NVIDIA Nemotron 3.5 Lightning, a customizable open model built to power always-on agents across local systems, the edge, the datacenter, and the cloud.
...


Blog

Unified Radix Cache: One Tree for Hybrid Model Prefix Caching

Prefix caching reuses KV when requests share the same token prefix. Under full attention, once the KV for a shared prefix is computed, it remains valid as more tokens are appended. A later request wit...


Blog

SGLang Adds Day-0 Support for Muse Glimmer, a Multimodal Model Built for Local Agentic Workflows

We're excited to partner with Meta Superintelligence Labs to bring Day-0 support for Muse Glimmer to SGLang, with dedicated optimizations tailored for high-performance inference of agentic workflows o...


Blog

HPC-Ops × SGLang: High-Performance Attention, Router GEMM, and MoE Kernels from Tencent Hunyuan

HPC-Ops is an open-source operator library for LLM inference, deployed in Tencent's large-scale production serving. Its core operators, including Dynamic Attention and Fused MoE, play a critical role ...


Blog

Full-Stack Performance Optimization of AR+DiT in SGL-Diffusion

- Replaces the HF backend with SRT to accelerate AR modeling and resolve parallelism conflicts, with dedicated TP for AR and SP for DiT
- Boosts hardware utilization via dynamic batching and enables e...


Blog

SpecForge v0.3.0: a Unified Disaggregated and Colocated Speculative Decoding Stack, and New Open SpecBundle Draft Models

When we first released SpecForge, a training job owned both the frozen target model and the draft model being optimized. This made EAGLE3 draft-model training practical and directly compatible with SG...


News

RadixArk Joins Forces with Google to Bring Full SGLang Features to TPUs

RadixArk and Google Cloud are partnering to bring SGLang to TPUs, giving developers ultimate flexibility for running workloads on their choice of hardware.


Blog

Towards Blackwell-Native 8-bit and 4-bit RL: End-to-End MXFP8 and NVFP4 RL in Miles

TL;DR: We implemented two Blackwell-native RL recipes in Miles: end-to-end MXFP8 and per-token NVFP4 for MoE experts. Both are supported by fine-grained precision control across checkpoint conversion,...


Blog

Toward a Cleaner Quantization Stack in SGLang

Quantization has moved from an advanced feature to an essential part of high-throughput LLM serving. As the number of checkpoint formats, model architectures, and hardware backends grows, the quantiza...


Blog

SGLang and Miles Add Day-0 Support for Kimi K3

We are excited to announce Day-0 support for Kimi K3
in SGLang and Miles. K3 is the first open-source model in the 3-trillion-parameter class,
and its hybrid architecture departs from convention in al...


Blog

OPD Support in Miles

We recently implemented On-Policy Distillation (OPD) as an important feature in Miles. OPD is now integrated into Miles rollout and training flow, so users can train a student model either solely with...


Blog

SGLang and Miles Add Day-0 Support for Inkling, a Frontier Multimodal Model

We're excited to partner with the Thinking Machines team to bring Day-0 support for Inkling to SGLang and Miles, with dedicated optimizations for its new architecture and broad feature coverage, and w...


Blog

Serving GLM5.2 NVFP4 Agentic Workload with SGLang: Reaching 500 TPS in 2 Weeks

- More than 500 TPS on 8xB300 (bs=1)
- Sync free speculative decoding for GLM 5.2 MTP
- Built-in IndexShare MTP with Spec V2
- 2.33x faster TopK-V2 for ISL 80k
- Indexer prologue fusion
- Gemm kernels...


News

Bringing DeepSeek-V4 Flash RL Training to AMD Instinct MI355X GPUs with Miles

DeepSeek-V4 RL is now supported in Miles on AMD Instinct™ MI355X GPUs with ROCm™! RL requires SGLang rollout and Megatron training to implement the same policy closely enough that token probabilities ...


Blog

Accelerating SGLang HiCache with Netpreme X-Mem™ MPU

Netpreme X-Mem™ Memory Processing Unit (MPU) makes SGLang HiCache faster and more scalable by augmenting the slower Host DRAM offload tier with a purpose-built high-bandwidth KV memory tier.
- Pr...


Blog

DSpark in SGLang: Speculative Decoding with Confidence-Driven, Variable-Length Verification

Speculative decoding trades extra compute for fewer decode steps, and the trade
sours as load grows: at batch size B with K speculative tokens the target
verifies B K tokens every step, and past a poi...


Blog

Agent-Assisted SGLang Development: An Initial Exploration

SGLang development increasingly goes beyond isolated code changes. The same repository now spans LLM serving, distributed runtime, GPU kernels, diffusion pipelines, model-specific execution paths, and...


Blog

Improving DeepEP MoE Load Balance in SGLang with Waterfill and LPLB

Mixture-of-Experts (MoE) models rely on Expert Parallelism (EP) to scale inference across multiple GPUs. In SGLang, DeepEP and EPLB provide high-performance serving under EP, but the workload seen by ...


Blog

Optimizing Ling-2.6-1T on TPU with SGLang-JAX: Hiding MoE Data Movement Behind Compute with One Pallas Kernel

SGLang-JAX now supports efficient serving of inclusionAI's Ling-2.6-1T on TPU v7x. With a working baseline in place, profiling pointed to the Mixture-of-Experts (MoE) path as the main bottleneck: each...


Blog

MOSS-TTS Local Transformer v1.5 on SGLang-Omni: Serving Native-Streaming 48 kHz Speech

Today we are announcing end-to-end serving for MOSS-TTS-Local-Transformer-v1.5 on SGLang-Omni, together with MOSI and the OpenMOSS Team.
MOSS-TTS-Local-Transformer-v1.5 is an open TTS model for 48 kH...


Blog

The next generation of speculative decoding: DFlash and Spec V2

Using Modal and Z Lab's DFlash speculative decoding models with SGLang’s newly default Spec V2 engine, you can achieve state-of-the-art latencies for LLM inference serving. Our new, jointly-released D...


News

Announcing the Recipient of the 2026 LMSYS PhD Fellowship

We are delighted to announce the first recipient of the LMSYS Fellowship Program: Will Lin.
Following the launch of our Fellowship Program and careful review of applications, we selected Will for his...


Blog

No Token Left Behind: Demystifying Token-In-Token-Out in Miles

In agentic RL, a rollout is not a single generation. It is a chain of model calls, tool outputs, harness messages, and resumed generations. Token-In-Token-Out (TITO) is a design principle that address...


Blog

Higgs Audio v3 TTS on SGLang-Omni: Real-Time, Controllable Speech for Voice Agents

Today we are announcing end-to-end serving for Higgs Audio v3 TTS on SGLang-Omni. Higgs Audio v3 TTS is Boson AI's text-to-speech model for conversational voice agents: it generates natural and expres...


Blog

SGLang and Miles Add Day-0 Support for NVIDIA Nemotron 3 Ultra for Long-Running Autonomous Agents

We are excited to announce that SGLang and Miles support NVIDIA Nemotron 3 Ultra on Day 0\.
Agentic AI systems are moving from short prompt-response interactions to persistent workflows that plan, us...


Blog

Heterogeneous CPU + GPU EPD Disaggregation to Boost VLM Serving

TL;DR
We enabled heterogeneous Encode-Prefill-Decode (EPD) disaggregation via Dynamo and SGLang for Vision-Language Models (VLMs). By offloading vision encoding tasks to CPUs (the easiest-getting CPU...


Blog

Win on TCO: How AMD Instinct™ MI355X Achieves Cost-Competitive Distributed Inference Through SGLang with MoRI

The SGLang and AMD team has worked closely to unlock competitive Total Cost of Ownership (TCO) for large-scale DeepSeek-R1 disaggregated inference on AMD Instinct™ MI355X GPUs. Building on SGLang's se...


Blog

Updating 1T parameters in seconds — P2P weight transfer in Large Scale Distributed RL

We introduced a RDMA-based, Peer to Peer weight update mechanism for RL workloads in SGLang as a supplement to traditional NCCL broadcast methods, compatible with all major open source models. By util...


Blog

DeepSeek-V4 on Day 0: From Fast Inference to Verified RL with SGLang and Miles

We are thrilled to announce Day-0 support for DeepSeek-V4 across both inference and RL training. SGLang and Miles form the first open-source stack to serve and train DeepSeek-V4 on launch day — with s...


Blog

HiSparse: Turbocharging Sparse Attention with Hierarchical Memory

Self-attention has become a major bottleneck in scaling LLMs to long contexts because of its quadratic compute and memory/IO cost. This has driven growing interest in efficient attention mechanisms. A...


News

Highlights of SGLang at NVIDIA GTC 2026

SGLang came to NVIDIA GTC 2026 with panels, a happy hour, a 200-person meetup, and a hands-on training lab. Three days, five events, one packed week at the center of the LLM ecosystem and left with a ...


Blog

Elastic EP in SGLang: Achieving Partial Failure Tolerance for DeepSeek MoE Deployments

To serve massive Mixture-of-Experts (MoE) models efficiently, deploying a "wide" Expert Parallelism (EP) strategy—often spanning 32 GPUs or more per inference instance—is not just an option; it is a n...


News

ROCm Support for Miles: Large-Scale RL Post-Training on AMD Instinct™ GPUs

Reinforcement learning (RL) has rapidly become a core stage of modern foundation-model development. While large-scale pretraining remains essential, today's most capable models rely heavily on post-tr...


News

SGLang Adds Day-0 Support for NVIDIA Nemotron 3 Super for building High-Efficiency Multi-Agent Systems

We are excited to announce that SGLang supports NVIDIA Nemotron 3 Super on Day 0.
Nemotron 3 Super is a leading open model in the Nemotron 3 family, built for running many collaborating agents togeth...


Blog

Unlocking 25x Inference Performance with SGLang on NVIDIA GB300 NVL72

The SGLang team has worked closely with NVIDIA across multiple GPU generations to unlock step-function gains in inference performance for large-scale deployments of Mixture of Expert (MoE) reasoning m...


Blog

Deploying DeepSeek on GB300 NVL72: Big Wins in Long-Context Inference

As the latest addition to the Blackwell family, the GB300 NVL72 is the most powerful platform for long-context LLM inference. In this blog post, we share our latest progress on optimizing DeepSeek R1-...


Blog

SGLang-Diffusion: Advanced Optimizations for Production-Ready Video Generation

Following our two-month progress update, we're excited to share a
deeper dive into the advanced optimizations that make SGLang-Diffusion a production-ready framework for video
generation. These improv...


Blog

Unleashing Computational Power: Ultimate Latency Optimization of Qwen3 and Qwen3-VL on AMD MI300X Series

Qwen is a series of large-scale, high-performance Large Language Models (LLMs) developed by the Qwen Team of Alibaba Cloud. From the first generation to the latest third-generation flagship models, al...


Blog

Squeezing 1TB Model Rollout into a Single H200: INT4 QAT RL End-to-End Practice

💡 TL;DR:
Inspired by the Kimi K2 team, the SGLang RL team successfully landed an INT4 Quantization-Aware Training (QAT) pipeline. By combining fake quantization during training with real quantizati...


Blog

Optimizing GLM4-MoE for Production: 65% Faster TTFT with SGLang

A suite of production-tested, high-impact optimizations has been developed by Novita AI for deploying GLM4-MOE models based on SGLANG.
We introduce an end-to-end performance optimization strategy that...


Blog

SGLang-Diffusion: Two Months In

Since its release in early Nov. 2025, SGLang-Diffusion has gained significant attention and widespread adoption
within the community. We are deeply grateful for the extensive feedback and growing numb...


Blog

Pipeline Parallelism in SGLang: Scaling to Million-Token Contexts and Beyond

We are excited to introduce SGLang's highly optimized Pipeline Parallelism (PP) implementation, specifically engineered to tackle the challenges of ultra-long context inference. By integrating Chunked...


Blog

EPD Disaggregation: Elastic Encoder Scaling for Vision-Language Models in SGLang

We introduce Encoder-Prefill-Decode (EPD) Disaggregation in SGLang, a novel architecture that separates vision encoding from language processing in Vision-Language Models (VLMs). This can enable:
- I...


Blog

SpecBundle & SpecForge v0.2: Production-Ready Speculative Decoding Models and Framework

The SpecForge team has collaborated with multiple industry partners - including Ant, Meituan, Nex-AGI, and EigenAI - to release SpecBundle (Phase 1), a collection of production-grade EAGLE-3 model che...


Blog

Power Up Diffusion LLMs: Day‑0 Support for LLaDA 2.0

We are excited to introduce the design and implementation of the Diffusion Large Language Model (dLLM) framework within SGLang. By leveraging the existing Chunked-Prefill mechanism, our system achieve...


Blog

Mini-SGLang: Efficient Inference Engine in a Nutshell

We're excited to introduce Mini-SGLang, a lightweight yet high-performance inference framework for Large Language Models (LLMs). Derived from the SGLang project, Mini-SGLang is designed to demystify t...


News

SGLang Day-0 Support for MiMo-V2-Flash Model

XiaomiMiMo/MiMo-V2-Flash, with 309B total parameters and 15B activated parameters, is a new inference-centric model designed to maximize decoding efficiency. It is based on two key designs: sliding wi...


News

SGLang Adds Day-0 Support for the Highly Efficient, Open Nemotron 3 Nano Hybrid MoE Model

Jan 28th Update: NVIDIA just released their Nemotron 3 Nano model in NVFP4 precision. This model is supported by SGLang out of the box and it uses a new method called Quantization-Aware Distillation (...


Blog

Let Tensors Fly — Accelerating Large Model Weight Loading with R-Fork

We introduce Tensor R-Fork (stands for Tensor Remote Fork), a novel weight loading methodology that leverages efficient inter-node device-to-device interconnect to load tensors from a running SGLang i...


Blog

Boost SGLang Inference: Native NVIDIA Model Optimizer Integration for Seamless Quantization and Deployment

(Updated on Dec 2)
We are thrilled to announce a major new feature in SGLang: native support for NVIDIA Model Optimizer quantization! This integration streamlines the entire model optimization and de...


Blog

From research to production: Accelerate OSS LLM with EAGLE-3 on Vertex

TL;DR: Speculative decoding boosts LLM inference, but traditional methods require a separate, inefficient draft model. Vertex AI utilizes EAGLE-3, adding a small draft head (2-5% of the target model) ...


Blog

Unified FP8: Moving Beyond Mixed Precision for Stable and Accelerated MoE RL

TL;DR: We have implemented fully FP8-based sampling and training in RL. Experiments show that for MoE models, the larger the model, the more severe the train–inference discrepancy becomes when using B...


News

LMSYS Fellowship Program

We are thrilled to announce the launch of the LMSYS Fellowship Program!
This year, the program is dedicated to supporting full-time PhD students in the United States who have made significant contrib...


News

Introducing Miles — RL Framework To Fire Up Large-Scale MoE Training

A journey of a thousand miles is made one small step at a time.
Today, we are releasing Miles, an enterprise-grade reinforcement learning framework tailored for large-scale MoE training and productio...


Blog

🚀 AutoRound Meets SGLang: Enabling Quantized Model Inference with AutoRound

We are thrilled to announce an official collaboration between SGLang and AutoRound, enabling low-bit quantization for efficient LLM inference.
Through this integration, developers can now quantize la...


Blog

SGLang Diffusion: Accelerating Video and Image Generation

We are excited to introduce SGLang Diffusion, which brings SGLang's state-of-the-art performance to accelerate image and video generation for diffusion models.
SGLang Diffusion supports major open-sou...


Blog

"No Free Lunch": Deconstruct Efficient Attention with MiniMax M2

We are excited to announce day-one support for the new flagship model, MiniMax M2, on SGLang. The MiniMax M2 redefines efficiency for agents: it is a compact, fast, and cost-effective Mixture of Exper...


Blog

Optimizing GPT-OSS on NVIDIA DGX Spark: Getting the Most Out of Your Spark

We’ve got some exciting updates about the NVIDIA DGX Spark\! In the week following the official launch, we collaborated closely with NVIDIA and successfully brought GPT-OSS 20B and GPT-OSS 120B suppor...


Blog

SGLang-Jax: An Open-Source Solution for Native TPU Inference

We're excited to introduce SGLang-Jax, a state-of-the-art open-source inference engine built entirely on Jax and XLA.
It leverages SGLang's high-performance server architecture and uses Jax to compile...


Blog

Accelerating Hybrid Inference in SGLang with KTransformers CPU Kernels

Modern Mixture-of-Experts (MoE) language models such as DeepSeek-V3 contain hundreds of billions of parameters, but only a small subset of experts are activated per token.
This sparse activation patt...


Blog

SGLang and NVIDIA Accelerating SemiAnalysis InferenceMAX and GB200 Together

The SGLang and NVIDIA teams have a strong track record of collaboration, consistently delivering inference optimizations and system-level improvements to ensure exceptional performance of the SGLang f...


Blog

NVIDIA DGX Spark In-Depth Review: A New Standard for Local AI Inference

Thanks to NVIDIA’s early access program, we are thrilled to get our hands on the NVIDIA DGX™ Spark. It’s quite an unconventional system, as NVIDIA rarely releases compact, all-in-one machines that bri...


News

SGLang Day 0 Support for DeepSeek-V3.2 with Sparse Attention

We are excited to announce that SGLang supports DeepSeek-V3.2 on Day 0! According to the DeepSeek tech report, it equips DeepSeek-V3.1-Terminus with DeepSeek Sparse Attention (DSA) through continued t...


Blog

PD-Multiplexing: Unlocking High-Goodput LLM Serving with GreenContext

This post highlights our initial efforts to support a new serving paradigm, PD-Multiplexing, in SGLang. It is designed to deliver higher goodput in LLM serving. PD-Multiplexing leverages GreenContext,...


Blog

Together with SGLang: Best Practices for Serving DeepSeek-R1 on H20-96G

Operationalizing scaled Mixture-of-Experts (MoE) models such as DeepSeek-R1 requires a careful balance of latency, throughput, and cost. The challenge is especially acute on hardware with asymmetric p...


Blog

Deploying DeepSeek on GB200 NVL72 with PD and Large Scale EP (Part II): 3.8x Prefill, 4.8x Decode Throughput

The GB200 NVL72 is one of the most powerful hardware for deep learning. In this blog post, we share our progress after our previous blog post to optimize the inference performance of DeepSeek V3/R1 wi...


Blog

Towards Deterministic Inference in SGLang and Reproducible RL Training

TL;DR: This post shares our efforts to enable deterministic inference in SGLang and our collaboration with slime to work towards reproducible RL training.
<br /
Recently, the Thinking Machines Lab ...


Blog

Optimizing FP4 Mixed-Precision Inference on AMD GPUs

As frontier large language models (LLMs) continue scaling to unprecedented sizes, they demand increasingly more compute power and memory bandwidth from GPUs. Both GPU manufacturers and model developer...


Blog

SGLang HiCache: Fast Hierarchical KV Caching with Your Favorite Storage Backends

In a coding agent scenario using Qwen3-Coder-480B, the observed dialogues often stretched past 25K tokens around 8 turns per session. Without full KV cache retention, nearly every request required cos...


Blog

LongCat-Flash: Deploying Meituan's Agentic Model with SGLang

LongCat-Flash, Meituan's open-source Agentic Mixture-of-Experts (MoE) model is now available from huggingface LongCat-Flash-Chat. Released by Meituan LongCat Team, it features:
- 560B total params
- 1...


Blog

Fine-tune and deploy gpt-oss MXFP4: ModelOpt + SGLang

(Updated on Aug 29)
OpenAI recently released gpt-oss, the first open source model family from OpenAI's lab since GPT-2. These models demonstrate strong math, coding, and general capabilities. Part of...


News

SGLang for gpt-oss: From Day 0 Support to Enhanced Performance

We are excited to announce a major update for SGLang, focusing on deep performance optimizations and new features for the recently released openai/gpt-oss-120b model. While we had support from day zer...


Blog

GLM-4.5 Meets SGLang: Reasoning, Coding, and Agentic Abilities

Today, we are excited to introduce our latest flagship models GLM-4.5 and GLM-4.5-Air, along with their FP8 variants. All models are now available with day-one support on SGLang.
GLM-4.5 and GLM-4.5-A...


Blog

SpecForge: Accelerating Speculative Decoding Training for SGLang

Speculative decoding is a powerful technique for accelerating Large Language Model (LLM) inference. In this blog post, we are excited to announce the open-sourcing of SpecForge, our new training frame...


Blog

Deploying Kimi K2 with PD Disaggregation and Large-Scale Expert Parallelism on 128 H200 GPUs

Kimi K2 is currently the most advanced open-source Mixture-of-Experts (MoE) model available.
Released by Moonshot AI in 2025, it features:
- 1 trillion total parameters
- 32 billion activated parame...


Blog

Accelerating SGLang with Multiple Token Prediction

SGLang now supports smooth combination of these advanced features: Multiple Token Prediction (MTP), Large-Scale Expert Parallelism (EP), and Prefill-Decode disaggregation. This integration delivers up...


Blog

How to support new VLMs into SGLang: A Case Study with NVILA

The world of LLMs is evolving at a remarkable pace, with Visual Language Models (VLMs) at the forefront of this revolution. These models power applications that can understand and reason about both im...


Blog

Cost Effective Deployment of DeepSeek R1 with Intel® Xeon® 6 CPU on SGLang

The impressive performance of DeepSeek R1 marked a rise of giant Mixture of Experts (MoE) models in Large Language Models (LLM). However, its massive model size and unique architecture have posed new ...


Blog

slime: An SGLang-Native Post-Training Framework for RL Scaling

We believe in RL. We believe RL is the final piece toward AGI.
If you feel the same way, you'll share our vision:
- Every field should be end-to-end RLed and every task should become an agent enviro...


Blog

OME: Revolutionizing LLM Infrastructure with Model-Driven Architecture

In any large organization deploying LLMs, two distinct teams emerge with conflicting needs:
The ML Engineers spend months benchmarking models, experimenting with serving technologies, and crafting op...


Blog

Deploying DeepSeek on GB200 NVL72 with PD and Large Scale EP (Part I): 2.7x Higher Decoding Throughput

The GB200 NVL72 is the world's most advanced hardware for AI training and inference. In this blog post, we're excited to share early results from running DeepSeek 671B with prefill-decode disaggregati...


Blog

Deploying DeepSeek with PD Disaggregation and Large-Scale Expert Parallelism on 96 H100 GPUs

DeepSeek is a popular open-source large language model (LLM) praised for its strong performance. However, its large size and unique architecture, which uses Multi-head Latent Attention (MLA) and Mixtu...


Blog

SGLang v0.4: Zero-Overhead Batch Scheduler, Cache-Aware Load Balancer, Faster Structured Outputs

We’re excited to release SGLang v0.4, featuring significant performance improvements and new features:
- Zero-overhead batch scheduler: 1.1x increase in throughput.
- Cache-aware load balancer: up t...


News

Announcing a New Site for Chatbot Arena

We’re excited to share that Chatbot Arena now has its own dedicated website: lmarena.ai and blog!
You might be wondering why we’re making this change. Over the past year, with the incredible support ...


Blog

RedTeam Arena: An Open-Source, Community-driven Jailbreaking Platform

We are excited to launch RedTeam Arena, a community-driven redteaming platform, built in collaboration with Pliny and the BASI community!
<img src="/images/blog/redteamarena/badwords.png" style="di...


News

SGLang v0.3 Release: 7x Faster DeepSeek MLA, 1.5x Faster torch.compile, Multi-Image/Video LLaVA-OneVision

We're excited to announce the release of SGLang v0.3, which brings significant performance enhancements and expanded support for novel model architectures. Here are the key updates:
- Up to 7x higher...


Blog

Does style matter? Disentangling style and substance in Chatbot Arena

Why is GPT-4o-mini so good? Why does Claude rank so low, when anecdotal experience suggests otherwise?
We have answers for you. We controlled for the effect of length and markdown, and indeed, the ra...


Blog

Achieving Faster Open-Source Llama3 Serving with SGLang Runtime (vs. TensorRT-LLM, vLLM)

At LMSYS.org, we've been running the Chatbot Arena platform for over a year, serving millions of users. We know firsthand how crucial efficient serving is for AI products and research. Through our ope...


Blog

RouteLLM: An Open-Source Framework for Cost-Effective LLM Routing

LLMs have demonstrated remarkable capabilities across a range of tasks, but there exists wide variation in their costs and capabilities, as seen from the plot of performance against cost in Figure 1. ...


News

The Multimodal Arena is Here!

We added image support to Chatbot Arena! You can now chat with your favorite vision-language models from OpenAI, Anthropic, Google, and most other major LLM providers to help discover how these models...


News

Introducing Hard Prompts Category in Chatbot Arena

Introducing Hard Prompts, a new and challenging category in the Chatbot Arena Leaderboard.
Over the past few months, the community has shown a growing interest in more challenging prompts that push ...


Blog

What’s up with Llama 3? Arena data analysis

On April 18th, Meta released Llama 3, their newest open-weight large language model. Since then, Llama 3-70B has quickly risen to the top of the English Chatbot Arena leaderboard with over 50,000 batt...


News

LMSYS Kaggle Competition – Predicting Human Preference with $100,000 in Prizes

LMSYS and Kaggle are launching a human preference prediction competition! You are challenged to predict which responses users will prefer in head-to-head battles between Large Language Models (LLMs). ...


Blog

From Live Data to High-Quality Benchmarks: The Arena-Hard Pipeline

Building an affordable and reliable benchmark for LLM chatbots has become a critical challenge. A high-quality benchmark should 1) robustly separate model capability, 2) reflect human preference in re...


Blog

LMSYS Chatbot Arena: Live and Community-Driven LLM Evaluation

Chatbot Arena (lmarena.ai) is an open-source project developed by members from LMSYS and UC Berkeley SkyLab. Our mission is to advance LLM development and understanding through live, open, and communi...


Blog

Fast JSON Decoding for Local LLMs with Compressed Finite State Machine

Constraining an LLM to consistently generate valid JSON or YAML that adheres to a specific schema is a critical feature for many applications.
In this blog post, we introduce an optimization that sign...


Blog

Fast and Expressive LLM Inference with RadixAttention and SGLang

Large Language Models (LLMs) are increasingly utilized for complex tasks that require multiple chained generation calls, advanced prompting techniques, control flow, and interaction with external envi...


News

Chatbot Arena: New models & Elo system update

Welcome to our latest update on the Chatbot Arena, our open evaluation platform to test the most advanced LLMs. We're excited to share that over 130,000 votes that are now collected to rank the most c...


Blog

Break the Sequential Dependency of LLM Inference Using Lookahead Decoding

TL;DR: We introduce lookahead decoding, a new, exact, and parallel decoding algorithm to accelerate LLM inference.
Lookahead decoding breaks the sequential dependency in autoregressive decoding by c...


Blog

Recipe for Serving Thousands of Concurrent LoRA Adapters

In this blog post, we introduce S-LoRA (code), a system designed for the scalable serving of many LoRA adapters. S-LoRA adopts the idea of
1. Unified Paging for KV cache and adapter weights to reduce...


Blog

Catch me if you can! How to beat GPT-4 with a 13B model

Announcing Llama-rephraser: 13B models reaching GPT-4 performance in major benchmarks (MMLU/GSK-8K/HumanEval)!
To ensure result validity, we followed OpenAI's decontamination method and found no evid...


Blog

ToxicChat: A Benchmark for Content Moderation in Real-world User-AI Interactions

In this blogpost, we introduce ToxicChat, a benchmark consisting of 10K high-quality data for content moderation in real-world user-AI interactions. Evaluation results show that fine-tuning on this be...


News

Chatbot Arena Conversation Dataset Release

Since its launch three months ago, Chatbot Arena has become a widely cited LLM evaluation platform that emphasizes large-scale, community-based, and interactive human evaluation. In that short time sp...


Blog

How Long Can Open-Source LLMs Truly Promise on Context Length?

In this blogpost, we introduce our latest series of chatbot models, LongChat-7B and LongChat-13B, featuring a new level of extended context length up to 16K tokens.
Evaluation results show that the lo...


News

Chatbot Arena Leaderboard Week 8: Introducing MT-Bench and Vicuna-33B

In this blog post, we share the latest update on Chatbot Arena leaderboard, which now includes more open models and three metrics:
1. Chatbot Arena Elo, based on 42K anonymous votes from Chatbot Aren...


Blog

Building a Truly "Open" OpenAI API Server with Open Models Locally

Many applications have been built on closed-source OpenAI APIs, but now you can effortlessly port them to use open-source alternatives without modifying the code. FastChat's OpenAI-compatible API serv...


News

Chatbot Arena Leaderboard Updates (Week 4)

In this update, we are excited to welcome the following models joining the Chatbot Arena:
1. Google PaLM 2, chat-tuned with the code name chat-bison@001 on Google Cloud Vertex AI
2. Anthropic Claude-...


News

Chatbot Arena Leaderboard Updates (Week 2)

We release an updated leaderboard with more models and new data we collected last week, after the announcement of the anonymous Chatbot Arena. We are actively iterating on the design of the arena and ...


Blog

Chatbot Arena: Benchmarking LLMs in the Wild with Elo Ratings

We present Chatbot Arena, a benchmark platform for large language models (LLMs) that features anonymous, randomized battles in a crowdsourced manner. In this blog post, we are releasing our initial re...


Blog

Vicuna: An Open-Source Chatbot Impressing GPT-4 with 90%* ChatGPT Quality

We introduce Vicuna-13B, an open-source chatbot trained by fine-tuning LLaMA on user-shared conversations collected from ShareGPT. Preliminary evaluation using GPT-4 as a judge shows Vicuna-13B achiev...
