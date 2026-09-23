# Open Research, Tooling & Optimization at PyTorch Conference North America 2026

source: https://pytorch.org/blog/open-research-tooling-optimization-at-pytorch-conference-north-america-2026/
published: Wed, 16 Sep 2026 19:00:47 +0000

### Featured projects

## TL;DR

Taking place October 20 to 21 in San Jose, California, PyTorch Conference North America 2026 highlights open research, tooling, and performance optimization across compiler architecture, cross-hardware kernel domain-specific languages, exascale distributed training, and low-precision quantization. Read this blog to learn more.

## Introduction

Every year, the beating heart of PyTorch Conference is the work that happens *underneath* the flashy headlines- the compilers, kernels, autotuners, distributed runtimes, profilers, and open-source libraries that make the rest of the ecosystem possible. At PyTorch Conference North America 2026, taking place October 20–21 in San Jose, California, this theme – **Open Research, Tooling & Optimization** – runs through dozens of sessions across the Core PyTorch, Kernel Engineering, Training, and Inference tracks.

This is where you’ll find the engineers rewriting torch.compile’s internals for speed, the teams building DSLs (Helion, CuteDSL, FlyDSL) that let a single kernel target NVIDIA, AMD, Intel, and TPU silicon, the researchers pushing quantization down to FP4 and NVFP4 without losing accuracy, and the maintainers open-sourcing tools like TinyTorch, Pyrefly, LMCache, and OpenEnv so the whole community can build on their work. It’s also where PyTorch’s own maintainers are candidly discussing how AI agents are reshaping how the framework itself gets built, reviewed, and released.

In this blog we have picked out the sessions that fall into this theme – open source tooling, systems research, and hard-won performance optimization.

[View the full conference schedule](https://hubs.ly/Q04tDx8f0)

[Register for PyTorch Conference North America 2026](https://hubs.ly/Q04tDx8f0)

## Compilers, Graph Capture & Dynamic Shapes

Everything to do with torch.compile, Dynamo, and the machinery that turns eager PyTorch code into a graph format that can be optimized at runtime, or used to generate artifacts for later execution

**Beyond Size and Stride: Unleash Performance with Device-Aware Tensor Layouts**

Olivier Tardieu; Matthew Arnold (IBM)

Tue 20 Oct, 16:20–16:30, LL20AB

A lightweight tensor layout extension that lets torch.compile (Inductor) automatically adapt tiling and NUMA-aware placement to the target device, without changing existing PyTorch model code.

**Nested Graph Breaks: Reducing the Cost of Graph Breaks in torch.compile**

William Wen (Meta)

Tue 20 Oct, 16:35–16:45, LL20AB

New Dynamo support reduces the cost of a graph break nested O(N) layers deep from O(N) duplicate breaks and O(N²) frame traces down to O(1) duplicate breaks and O(N) frame traces – yielding larger captured graphs, fewer breaks, and faster, more debuggable compilation.

**Static Tensor Shape Checking for PyTorch with Pyrefly**

Steven Troxler; Avik Chaudhuri (Meta)

Tue 20 Oct, 17:30–17:55, LL20AB

Shape mismatches cause roughly 45% of deep learning program failures and drive slow torch.compile recompilations. Pyrefly brings static, near-instant tensor shape checking to the type checker itself, evaluated across 28 real LLM, vision, recommender, and RL models.

**Parametrized Dynamic Shape CUDA Graphs**

Elias Ellison (Meta); Daniel Galvez (NVIDIA)

Wed 21 Oct, 11:45–12:10, LL21ABC

Building on parametrized CUDA Graphs and torch.compile’s symbolic tracing and guard infrastructure, this work captures and re-parametrizes a single CUDA Graph across dynamic shapes, eliminating the need for whole-model rewrites, padding, or re-recording across every possible shape.

**From Backed to Unbacked: Sound, Predictable, and Controllable Dynamic Shapes in PyTorch**

Laith Sakka (Meta)

Wed 21 Oct, 16:20–16:45, LL21ABC

This session explains why explicit graph-capture workflows (vLLM, export, pre-compilation) need unbacked dynamic shapes, which disallow implicit guards and force the compiler to prove general validity.

**Speeding Up torch.compile: A New FakeTensor**

Angel Li (Meta)

Wed 21 Oct, 16:55–17:05, LL21ABC

FakeTensor propagation eats roughly 20% of Dynamo’s tracing time. This talk introduces a new C++ FakeTensor implementation that delivers a 30x speedup on operations like aten.mm, meaningfully cutting torch.compile’s notorious cold-start compilation time.

**Lightweight FX Tracing in PyTorch**

Richard Zou; Yidi Wu (Meta)

Wed 21 Oct, 17:10–17:20, LL21ABC

A new FX tracer based on make_fx, targeting functionally pure PyTorch code instead of trying to capture full Python semantics like Dynamo. This means trading flexibility for a much simpler, more learnable, JAX-style tracing programming model for users who need a full graph.

**Unlocking the Full Potential of TorchDynamo: Accelerating, Comparing, and Debugging ML Systems**

Yi Pan (UC Berkeley); Megan Frisella (University of Washington); Stephanie Wang (Paul Allen School, University of Washington)

Wed 21 Oct, 17:30–17:55, LL21ABC

Research using TorchDynamo’s graph-interception capability well beyond torch.compile itself. DynaFlow and Piper for transparent parallelism acceleration, Magneton for automatically comparing equivalent operations across competing systems, and numerical debugging via matched-subgraph tensor comparison.

## Kernel Engineering & Domain-Specific Languages

The DSLs, autotuners, and hand- and agent-written kernels that squeeze more performance out of every GPU cycle, spanning Triton, Helion, CUTLASS, FlyDSL, and the agentic pipelines now writing and optimizing kernels themselves.

**Extending TorchInductor with FlyDSL: A New MLIR-Native Backend for High-Performance GEMMs**

Liz Li (AMD)

Tue 20 Oct, 11:10–11:35, 210BF

AMD’s FlyDSL, a Python-native, MLIR-based GPU kernel DSL, gets integrated into TorchInductor’s GEMM compilation pipeline. The talk covers how FlyDSL plugs into autotuning, coexists with existing backends, and delivers measured speedups over Triton on AMD Instinct GPUs.

**Helion: CuteDSL and TPU Backends for Heterogeneous Hardware, and Why It Suits Agents**

Oguz Ulgen, Dunfan Lu, Jason Ansel (Meta)

Tue 20 Oct, 11:45–12:10, 210BF

Helion, PyTorch’s high-level kernel-authoring DSL, gains two new compiler backends – CuteDSL for recent NVIDIA GPUs and Pallas for TPUs – letting one kernel source target very different hardware. The second half explores why Helion’s abstraction level is particularly well suited to LLM-agent-generated kernel code.

**Practical GPU Programming with Triton for PyTorch Developers**

Suman Debnath, JanakiRam Goteti (Crusoe AI)

Tue 20 Oct, 11:45–12:10, LL20CD

A friendly, from-scratch introduction to writing GPU kernels in Triton – no CUDA or C++ required. Building from a simple vector-add up to a small matrix multiplication, with an emphasis on reading and understanding what PyTorch already generates for you.

**High-Velocity GPU Kernel Authoring with CUTLASS Python**

Michael Goldfarb, Guray Ozen (NVIDIA)

Tue 20 Oct, 12:20–12:45, 210BF

New Python-first capabilities in CUTLASS’s CuTe DSL – high-level building blocks, low-level hardware-instruction primitives, and a zero-cost Resource and Task Scheduler – that reduce boilerplate for kernel authors while keeping the DSL’s zero-cost abstractions intact.

**Smarter Autotuning for Kernels: From Bayesian Optimization to LLM-Guided Search in Helion DSL**

Jongsok Choi; Ethan Che (Meta)

Tue 20 Oct, 14:15–14:40, 210BF

Two leaps in Helion’s autotuning: Likelihood-Free Bayesian Optimization (LFBO), which cuts tuning time by 36.5% via an on-the-fly Random Forest filter, and LLM-guided autotuning, which proposes strong kernel configurations in seconds – up to 10x faster tuning on NVIDIA B200.

**KernelAgent: Hardware-Guided GPU Kernel Optimization via Multi-Agent Orchestration**

Kaiming Cheng; Laura Wang (Meta)

Tue 20 Oct, 14:15–14:40, LL21DEF

Building on KernelAgent’s 100% correctness across all KernelBench L1/L2/L3 tasks, this talk adds a hardware-guided optimization layer that feeds GPU performance signals into a closed-loop multi-agent workflow, achieving 1.56x speedup over default torch.compile and 89% of H100 roofline efficiency.

**From Weeks to Overnight: Autonomous Day-0 Kernel Bring-Up with Agent Pipelines**

Xiaogang Gu; Qun Yang (Intel)

Tue 20 Oct, 17:30–17:40, 210BF

A pipeline-driven autonomous system that encodes GPU kernel optimization (Profile, Analyze, CodeGen, Verify, Fix, Benchmark, Evaluate) as a deterministic workflow with specialized agents per stage and long-term memory, cutting kernel bring-up cycles from weeks to unattended overnight runs.

**Beyond the Brrr: Building a Unified Ecosystem for Optimized Kernels**

Sayak Paul (Hugging Face)

Wed 21 Oct, 11:10–11:35, 210BF

Generic operators often use only 20–30% of available GPU performance. This talk introduces Hugging Face’s Kernels library, which makes discovering and swapping in optimized custom kernels as simple as loading a model checkpoint – already delivering 2–5x speedups in production Transformers workloads.

**Making vLLM Faster on Intel GPUs with Triton Kernels**

Whitney Tsang, Artur Fierka (Intel)

Wed 21 Oct, 12:20–12:30, 210BF

Treats Intel GPU architectures like Arc as first-class optimization targets rather than portability afterthoughts, covering Triton kernel strategies for unified attention, fused and batched MoE, and fusion opportunities like QK-norm+RoPE that outperform hand-written SYCL on key vLLM serving paths.

**FlexGEMM: Flexible PyTorch Epilogues**

Driss Guessous (Meta)

Wed 21 Oct, 12:35–12:45, 210BF

A proposed PyTorch frontend for writing GEMM epilogues – bias, activation, residual adds, fp8 scaling, SwiGLU-style gating – as ordinary PyTorch functions, giving the compiler a clear, fail-closed contract for fusing them directly into the GEMM store path.

**Native DSL Operators in PyTorch Core**

Simon Layton (Meta)

Wed 21 Oct, 14:50–15:15, LL21ABC

DSL-authored kernels (as used in FlashAttention) have stayed outside PyTorch’s core dispatch system. This talk presents ongoing work to make DSL operators first-class citizens, tied into dispatch and testing, enabling new operators and targeted performance fixes.

**Portable Paged Attention: From Triton to Helion**

Burkhard Ringlein (IBM Research)

Wed 21 Oct, 15:25–15:50, 210BF

Building on the state-of-the-art portable Triton attention backend in vLLM, this team wrote an experimental Helion attention backend for Paged Attention – vLLM’s core kernel – reporting up to 50% lower latency and 10% higher end-to-end throughput than the optimized Triton version.

## Distributed Training, Parallelism & Systems

Systems and abstractions for training at scale — sharding, single-GPU-to-cluster developer experience, and the frameworks that decide how a model gets split across thousands of devices.

**Monarch – Single-Machine DevX at Distributed Scale**

Marius Eriksen (Meta)

Tue 20 Oct, 11:10–11:35, LL20CD

Monarch lets developers program an entire cluster as if it were a single machine, using actor-based IPC and RDMA so remote logs, filesystems, and debugging behave like they’re local. The talk demos how it speeds up building large-scale post-training frameworks.

**FlexShard: Pluggable Sharding Placements for Matrix Optimizers and Block-wise Quantization**

Wei Feng; Anshul Sinha; Ailing Zhang (Meta)

Wed 21 Oct, 11:10–11:35, LL20CD

A prototype PyTorch abstraction that decouples parameter sharding from FSDP’s runtime machinery via a small Placement contract, enabling optimizer-aware sharding for matrix optimizers like Muon and quantization-aligned sharding for block-wise FP8 all-gather.

**DeepSpeed Is Not Just ZeRO: Tensor, Sequence, and Expert Parallelism with ZeRO-Level Usability**

Masahiro Tanaka (Anyscale)

Wed 21 Oct, 11:10–11:35, LL21DEF

DeepSpeed’s AutoTP, AutoSP, and AutoEP bring tensor, sequence, and expert parallelism to existing model implementations, including many Hugging Face models, without rewriting code, and can be combined with ZeRO for large dense models, long-context training, and MoE workloads.

**Precompile for Training**

Bob Ren; Aaron Orenstein (Meta)

Wed 21 Oct, 12:00–12:10, LL20CD

A new abstraction for compiling distributed SPMD training programs once and reusing the artifact across every rank, eliminating redundant per-rank compilation, preventing divergent compiler decisions that cause NCCL hangs, and guaranteeing identical kernel selection across the cluster.

**From Full DTensor to spmd_types: Making Parallelism Explicit in TorchTitan**

Chien-Chin Huang, Pian Pawakapan (Meta)

Wed 21 Oct, 14:15–14:40, LL21DEF

The evolution from an all-DTensor approach to spmd_types, a lightweight, zero-runtime-overhead type system where sharding is part of a tensor’s type, collectives are explicit, and backward gradient sharding follows predictably from forward, covering both global and local SPMD modes.

**AutoParallel: Automatic Discovery of Distributed Training Strategies in PyTorch**

Sanket Jayant Purandare, Francisco Massa (Meta)

Wed 21 Oct, 15:25–15:50, LL21DEF

Given only a device mesh, memory budget, and sample batch, AutoParallel searches for an optimal parallelization strategy directly on the model graph – no manual FSDP/TP/SP/EP placement – matching a strong hand-tuned baseline on Llama-3 8B at 12% less memory, fully open source under meta-pytorch.

## Communication & Collective Libraries

The collective-communication layer underneath distributed training and inference: symmetric memory, NCCL extensions, and fault-tolerant libraries built to survive failures at exascale.

**EP-Overlap: Hiding Expert-Parallel Communication in MoE Training**

Sanket Jayant Purandare (Meta)

Tue 20 Oct, 15:25–15:35, LL21DEF

A general technique for hiding expert-parallel all-to-all communication behind any available compute, not just DualPipe pipeline schedules, implemented as graph passes in TorchTitan’s GraphTrainer, hiding 76–86% of EP communication on DeepSeek-V3 for a ~1.3x throughput gain.

**Future of Distributed Communication in PyTorch: New APIs for Fault Tolerance, RDMA and Extensibility**

Tristan Rice, Kapil Sharma (Meta)

Tue 20 Oct, 16:20–16:45, LL21ABC

New torch.distributed APIs incubated in TorchComms and now upstreaming directly. Live process-group reconfiguration after rank failures, one-sided RDMA put/get windows, composable collective hooks, and pip-installable backend extensibility – all with zero migration cost for existing users.

**rocSHMEM Symmetric Memory in PyTorch for AMD GPUs**

Prachi Gupta (AMD)

Tue 20 Oct, 16:35–16:45, LL21DEF

Extends PyTorch’s symmetric memory, previously NVIDIA/NVSHMEM-only, to AMD GPUs via rocSHMEM, exposing one-sided put/get and signal/wait primitives as Triton-callable ops so a single Triton kernel can run MoE all-to-all dispatch and combine on either vendor’s hardware.

**XCCL: Scaling PyTorch Collectives to Exascale on Intel GPUs with TorchComms**

Panagiotis Kourdis, Tanima Dey (Intel)

Tue 20 Oct, 17:10–17:20, LL21ABC

XCCL extends TorchComms with native Intel GPU support built on oneCCL, validated on Argonne’s Aurora exascale supercomputer with over 90% scaling efficiency across thousands of nodes, plus a stream-ordered async execution model that overlaps computation and communication.

**Beyond Collectives: Building Fused Compute-Communication Kernels with PyTorch Symmetric Memory**

Ke Wen (NVIDIA), Natalia Gimelshein, Kapil Sharma (Meta)

Wed 21 Oct, 11:45–12:10, 210BF

PyTorch Symmetric Memory gives every rank a direct window into peers’ GPU memory, letting communication happen inline inside a kernel rather than as a black-box collective. This covers compute–communication fusion, CuTe-DSL bindings for NCCL device primitives, and new profiling and CUDA Graph support.

**Introducing NCCL Extensions: Communication Patterns for Modern AI**

Sreeram Potluri, Artem Polyakov (NVIDIA)

Wed 21 Oct, 16:55–17:20, 210AE

Debuts NCCL-EP, bringing tuned MoE dispatch/combine natively into NCCL with GPU-initiated RDMA and NVLink, and NCCL-M2N, enabling zero-copy resharding between disjoint device meshes for RL weight rollout. Both are built on NCCL’s new Device APIs for custom, fused communication patterns.

**MCCL: Fault-Tolerant Collective Communication for Large-Scale GPU Training**

Ben Carver (Meta)

Wed 21 Oct, 17:30–17:55, 210AE

The Meta Collective Communication Library (MCCL) treats hardware failure as a first-class design principle at tens-of-thousands-of-GPU scale, enabling dynamic communicator reconfiguration, shrinking and growing as ranks fail or recover, without full job restarts, integrated with TorchComms.

Quantization & Low-Precision Training

Pushing training and inference into 4- and 8-bit formats — NVFP4, HiFloat, and the recipes that close the accuracy gap with BF16 while unlocking large throughput gains.

**HiFloat: Democratizing Ultra-Low Precision Training and Inference in PyTorch Ecosystems**

Yun Zhao, Haonan Zhang (Huawei)

Wed 21 Oct, 14:50–15:00, LL20AB

HiFloat8 and HiFloat4 are tapered-precision formats designed to match neural network weight and gradient distributions without complex delayed scaling, achieving FP16 loss parity with a 1.5x–1.7x GEMM speedup, integrated via PyTorch custom ops, Triton kernels, and torch.compile.

**Efficient Pretraining of LLMs in NVFP4**

Anjulie Agrusa, Ryan Spring, Bruce Zitelli (NVIDIA)

Wed 21 Oct, 15:25–15:50, LL20AB

NVFP4 GEMMs offer 2x–3x higher peak throughput than FP8 on GB200/GB300, but quality gaps persist versus BF16 at smaller model sizes. This talk presents recipe improvements that close that gap, upstreamed into TorchAO and TorchTitan for native PyTorch NVFP4 pretraining.

## Optimizers & Multi-Loss Training

New training algorithms and loss-aggregation techniques moving beyond AdamW and single-loss optimization.

**Beyond AdamW: A Practical PyTorch Walkthrough of Muon, Dion, and Orthogonalized Optimizer Variants**

Jennifer Wei (Bird of Paradise AI)

Wed 21 Oct, 14:50–15:15, LL21DEF

A hands-on walkthrough of Muon’s matrix-orthogonalization approach to hidden-layer updates – momentum, Newton-Schulz iteration, parameter grouping, AdamW compatibility – bridging from single-GPU implementation to distributed training and touching on newer Dion/Dion2 developments.

**TorchJD: Training PyTorch Models with Multiple Losses**

Valérian Rey, Khush Patel (SimplexLab)

Wed 21 Oct, 15:05–15:15, LL20AB

Now part of the PyTorch ecosystem, TorchJD implements Jacobian descent, aggregating the per-loss gradient Jacobian so parameter updates benefit every objective, with applications spanning multitask learning, machine unlearning, federated learning, and adversarial fairness.

Reinforcement Learning Systems

Open frameworks and infrastructure for agentic and multi-turn RL — from standardized environments to the training frameworks and numerical-consistency fixes that keep large-scale RL stable.

**Open Source Reinforcement Learning with Agent Harnesses**

Ben Burtenshaw (Hugging Face)

Tue 20 Oct, 17:30–17:55, 210AE

OpenEnv is an interoperability layer, co-owned by Hugging Face, Meta, Unsloth, Prime Intellect, Modal, NVIDIA, and Mercor, that standardizes how RL environments are published, deployed, and consumed via a consistent HTTP/WebSocket/MCP API, decoupling environments from harness and trainer choice.

**Torchtitan RL: A Unified and Extensible Training Framework for Agentic Tasks**

Felipe Mello, Jiani Wang (Meta)

Wed 21 Oct, 16:20–16:45, LL21DEF

Addresses the two core instabilities in frontier-scale asynchronous RL – numerical mismatch between training and generation, and infrastructure complexity. This is done through a single shared model definition for both roles and a hackable, forkable stack built on TorchTitan’s large-scale trainer.

**When Rollout and Training Disagree: Lessons from Building a Mismatch-Free RL Engine** Neiwen Ling (ByteDance), Tianle Zhong (University of Virginia)

Wed 21 Oct, 16:55–17:05, LL21DEF

Introduces VeXact, an open-source rollout backend that aligns rollout log-probabilities with the training path in verl-based RL systems, showing that small token-level numerical disagreements between inference and training stacks can independently destabilize PPO/GRPO objectives.

Inference & Serving Optimization

Tools that make LLM serving faster and cheaper to operate, from checkpoint loading to prompt caching.

**Faster LLM Serving Startup with fastsafetensors**

Takeshi Yoshimura (IBM)

Tue 20 Oct, 15:25–15:35, LL20CD

fastsafetensors treats checkpoint loading as a data-movement problem, removing per-tensor copies and host staging to deliver 4.8x–7.5x faster model loading and up to 28 GB/s of NVMe throughput, now a portable, cross-vendor library with ROCm and Windows DirectStorage support.

**LMCache: A Cluster-Wide Open-Source Solution for LLM Prompt Caching**

Kuntai Du (Tensormesh, Inc.)

Tue 20 Oct, 15:40–15:50, LL20CD

LMCache is one of the most widely adopted open-source prompt-caching solutions, spanning vLLM, SGLang, and TensorRT-LLM inference engines and storage backends from Mooncake to Redis to S3. This talk includes a quick tutorial for deploying it on Kubernetes.

## Hardware Portability & Accelerator Backends

The backends and compilers bringing native PyTorch support to TPUs, Trainium, Spyre, dataflow accelerators, Intel XPUs, and edge hardware — the work that keeps PyTorch truly hardware-agnostic.

**Unlocking PyTorch for Dataflow Accelerators: An Open-Source Kernel Tile IR and Dataflow Scheduler**

Prasanth Chatarasi, Bardia Mahjour, Viji Srinivasan (IBM)

Tue 20 Oct, 16:55–17:20, 210BF

KTIR, an open-source MLIR-based tile IR, extends data-parallel abstractions with distributed scratchpads and inter-tile communication, paired with an architecture-agnostic dataflow scheduler. Both are open sourced and integrated with PyTorch via TorchInductor to power IBM’s Spyre accelerator.

**Portable PyTorch Across AI Accelerators: A Triton Operator Stack from Eager Mode to vLLM**

Yonghua Lin (Beijing Academy of Artificial Intelligence)

Tue 20 Oct, 16:55–17:20, LL20CD

FlagOS is an open source Triton-based operator, compiler, and runtime stack (FlagGems, FlagTree, vllm-plugin-fl) tested on 20+ chips and architectures, enabling Day-0 support for frontier open models across NVIDIA GPUs, non-CUDA accelerators, and ARM CPUs.

**Integrating the IBM Spyre Accelerator**

David Grove, Antoni Viros Martin, Avery Blanchard (IBM)

Tue 20 Oct, 16:55–17:20, LL21DEF

Torch-Spyre, an open source PyTorch PrivateUse1 device with an Inductor backend for IBM’s 32-core Spyre accelerator, now runs thousands of Hugging Face and vLLM models. This talk covers device-specific tensor layouts, scratchpad tiling, and the upstream contributions that made it possible.

**TorchNeuron: Native PyTorch on AWS Trainium — From Research to Production Without Compromise**

Yahav Biran (Annapurna Labs)

Tue 20 Oct, 17:30–17:40, LL21ABC

An open-source native PyTorch backend for Trainium via PrivateUse1 — change .to(‘cuda’) to .to(‘neuron’) and keep unmodified code – covering adaptive eager execution, native FSDP/DDP/TP+SP distributed support, and custom NKI kernels integrated into compiled graphs.

**TorchTPU: Running PyTorch Natively on Google TPUs**

Claudio Basile (Google)

Wed 21 Oct, 11:10–11:35, LL21ABC

TorchTPU brings native, high-performance PyTorch to TPUs (previously JAX-only) through an ATen-to-StableHLO lowering path and “DeferAndFuse” execution for automated op fusion, integrating with vLLM for serving and TorchTitan for training, and moving to a public open-source release.

**Integrating TorchTPU into TorchTitan and Optimizing Models for TPUs**

Aleksey Vlasenko (Google), Will Constable (Meta)

Wed 21 Oct, 17:10–17:20, LL21DEF

A concise look at the process of adding TorchTPU support into TorchTitan and optimizing selected models to run on TPU, with a direct performance comparison against GPU.

**From PyTorch to the Edge: Agentic Synthesis of Inference Runtimes for Heterogeneous Hardware**

Thomas Cottenier (Arm)

Wed 21 Oct, 17:30–17:55, LL20AB

An agentic harness that synthesizes bespoke inference runtimes per edge target, routing through torch.export, ExecuTorch backends, torchao quantization, or direct kernel generation as needed. This is then validated on Apple silicon against llama.cpp and MLX, then extended to Arm hardware with no existing baseline.

**Scaling PyTorch on Intel XPU: Field Notes from AI for Science on Aurora**

Sam Foreman (Argonne National Laboratory), Panagiotis Kourdis, Tanima Dey (Intel)

Wed 21 Oct, 17:30–17:55, LL20CD

Field notes from training scientific foundation models in production on 63,000+ Intel XPUs on Argonne’s Aurora system, covering the migration from Megatron-DeepSpeed to torchtitan + DTensor + FSDP2, and the operational machinery (silent-hang detection, bad-node failover) that long-running jobs demand.

## Profiling, Observability & Performance Diagnostics

Tools and techniques for actually seeing what your PyTorch code is doing on the hardware – reading traces, diagnosing bottlenecks, and estimating memory and runtime before you touch a cluster.

**What You Cannot Profile, You Cannot Optimize: Learning to Read PyTorch Traces**

Aritra Roy Gosthipaty, Suvaditya Mukherjee (Hugging Face)

Tue 20 Oct, 14:50–15:15, LL20AB

A Socratic, no-prerequisites walkthrough of PyTorch profiler traces, from a simple matmul-plus-bias workload up to a real GeGLU MLP, teaching durable mental models for overhead-bound vs. compute-bound execution and the CPU→ATen→cuBLAS→GPU dispatch chain.

**Observability Tooling for Cudagraph Workloads**

Natalia Gimelshein, Driss Guessous (Meta)

Tue 20 Oct, 16:20–16:30, LL21DEF

CUDA graphs help solve CPU overhead on Blackwell-class hardware but make profiles harder to read. This talk covers new PyTorch utilities that make cudagraph profiling and memory monitoring information-rich with near-zero overhead, by cross-referencing capture-time and replay-time data.

**Five Bottlenecks, Five Fixes: Systematic Performance Diagnosis for PyTorch Distributed Training**

Paulo Aragao (Amazon Web Services)

Tue 20 Oct, 16:55–17:20, 210AE

Five real case studies – from an 83x DataLoader speedup to a 6.8x end-to-end gain on an autonomous-driving model – mapped to a repeatable diagnostic framework for classifying distributed training bottlenecks as compute-, memory-, communication-, or I/O-bound.

**TorchInsights: Zero-GPU Memory & Runtime Estimation for Distributed Training and Agentic Research**

Sanket Jayant Purandare, Aditya Venkataraman (Meta)

Tue 20 Oct, 17:45–17:55, LL21ABC

Using fake tensors and simulated multi-stream GPU execution, TorchInsights predicts peak memory and runtime across FSDP/TP/EP/CP/PP configurations before touching a real cluster, published at ICML 2025 as TorchSim and fully open source under meta-pytorch.

## Data Loading, Storage & Media Pipelines

Feeding hungry GPUs – high-speed storage protocols, dataloader scaling, and efficient image/video/audio preprocessing.

**Keeping GPUs Busy: High-Speed Storage for PyTorch via fsspec**

Ankita Luthra, Trinadh Kotturu (Google)

Tue 20 Oct, 15:40–15:50, LL21DEF

“Rapid Storage” brings Google’s Colossus stateful protocol to PyTorch through the fsspec interface, bypassing REST APIs via persistent gRPC streams to achieve sub-1ms random I/O latency and 6 TB/s aggregate throughput for training and checkpointing.

**From Bytes to Tensors: Efficient Media Processing with PyTorch in 2026**

Nicolas Hug, Scott Schneider (Meta)

Wed 21 Oct, 16:20–16:45, 210BF

A tour of how TorchVision, TorchCodec, and TorchAudio together form an efficient end-to-end media preprocessing pipeline, plus techniques from the past year – CUDA-accelerated decoding, SIMD-optimized transforms, pre-computed frame indices – that eliminate preprocessing bottlenecks starving the GPU.

**Scaling PyTorch Dataloaders 10x: A Case Study**

Ian Stenbit, Christine Cheng, Dylan Doblar (NVIDIA)

Wed 21 Oct, 16:55–17:20, 210BF

Over two years, NVIDIA’s autonomous vehicles team scaled a research dataloader to full production across thousands of GPUs, sharing lessons on profiling with Nsight and cprofiler, distributed filesystems, CUDA pipelining, and scaling video decoding to hit a 10x throughput improvement.

## AI Agents, Open-Source Community & Release Engineering

How AI agents are reshaping PyTorch’s own development process, plus the open-source education and release-engineering tooling that keeps the ecosystem healthy.

**Contributing to PyTorch with AI Agents**

Edward Yang (Meta)

Tue 20 Oct, 10:35–11:05, Community Expo (Birds of a Feather)

A community discussion on how AI agents can be used productively to contribute to PyTorch itself – how to get a PR reviewed, what maintainers want to see, and lessons from the project’s own devlog on AI coding practices.

**Relay and Reuse: The Dual Engine Behind PyTorch Out-of-Tree Release Readiness**

Jiahao Chen, Jiahao Tan (Huawei)

Tue 20 Oct, 11:10–11:35, LL21DEF

How device-agnostic test reuse and a Cross-Repo CI Relay (CRCR) let out-of-tree hardware backends ship high-quality releases within 30 days of each PyTorch update, turning 580K+ community tests into a shared safety net.

**Scaling PyTorch’s Compatibility Promise: A Tiered Cross-Repository CI Relay for Out-of-Tree Backends**

Subin George, Jewel K M (Red Hat)

Tue 20 Oct, 12:00–12:10, LL21DEF

A deeper technical dive into CRCR’s four-tier trust model (event dispatch through blocking merge prerequisites), its DynamoDB/ClickHouse ingestion pipeline, and how it cut breakage detection for out-of-tree backends like Ascend NPU and RISC-V from days to minutes.

**Fighting Agents with Agents — Bringing Claude to PyTorch CI, Triage, and PR Review**

Driss Guessous (Meta)

Tue 20 Oct, 12:35–12:45, LL21DEF

How the PyTorch project brought Claude into its own infrastructure: @claude on issues and PRs, automatic issue triage, reusable onboarding skills, and CI/autorevert investigation – plus the Bedrock/OIDC setup and adoption trends behind it.

**From Scratch to PyTorch: Demystifying ML Frameworks by Building Your Own**

Andrea Mattia Garavagno (University of Genoa), Vijay Janapa Reddi (Harvard University)

Tue 20 Oct, 14:15–14:40, LL20AB

TinyTorch is an open-source CLI teaching tool which guides developers through rebuilding PyTorch’s foundational components – tensors, autograd, optimizers, transformers – in pure Python, closing the gap between using a framework and understanding it.

## Conclusion

Taken together, these sessions tell a consistent story: the PyTorch ecosystem’s edge doesn’t just come from bigger models – it comes from relentless, open, collaborative work on the tools underneath them. Whether it’s a new DSL that lets one kernel run on five different chips, a profiler that finally makes CUDA graphs legible, or an autotuner that shaves days off a training run, this is the research and tooling that quietly makes everything else in AI possible. And because so much of it ships as open source – Helion, TinyTorch, Pyrefly, LMCache, OpenEnv, TorchJD, and dozens more – every session here is also an invitation to go build with it yourself.

If you work anywhere near performance, compilers, distributed systems, or open-source ML infrastructure, this track alone is worth the trip. [ Register now for PyTorch Conference North America 2026](https://hubs.ly/Q04tDx8f0), taking place October 20–21 in San Jose, California, and get direct access to the people building the tools that power the next generation of open AI. Seats fill up fast for the technical breakout sessions – secure yours today.

*PyTorch Conference is the open source AI community’s town square. Where what’s next gets decided.*