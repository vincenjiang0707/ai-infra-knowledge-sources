# core-pytorch-sessions-at-pytorch-conference-north-america-2026

source: https://pytorch.org/blog/core-pytorch-sessions-at-pytorch-conference-north-america-2026/

### Featured projects

**TL;DR**

PyTorch Conference North America 2026 features Core PyTorch sessions spanning compiler and runtime work, distributed communication, device portability, release engineering, CI, observability, accelerator integration, and contributor infrastructure.

**Core PyTorch at #PyTorchCon NA:**

PyTorch Conference North America 2026 comes to San Jose, CA, October 20–21, with two days of technical talks, workshops, and discussions across the open source AI stack.

Our Core PyTorch program gets into the machinery of the framework: compiler and runtime internals, distributed communication, device abstractions, hardware integration, release engineering, CI, profiling, and compatibility. The sessions below cover the APIs, implementation work, performance results, and engineering approaches shaping how PyTorch is built and extended.

[View the full conference schedule](https://hubs.ly/Q04tDx8f0)

[Register for PyTorch Conference North America 2026 by September 4 to save on your ticket](https://hubs.ly/Q04tDw_W0)

**Release Engineering, Compatibility, and Contributor Infrastructure**

**Relay and Reuse: The Dual Engine Behind PyTorch Out-of-Tree Release Readiness**

**Jiahao Chen, Huawei; Jiahao Tan, Huawei**

**October 20, 11:10–11:35 a.m. | LL21DEF | Breakout Session**

This session explains how an out-of-tree accelerator backend uses device-agnostic test reuse and cross-repository CI to keep pace with PyTorch releases. The speakers say instantiate_device_type_tests and dynamic skipping make 580K+ community test cases reusable out of the box, while the Cross-Repo CI Relay validates PyTorch PRs against accelerator code before merge.

Together, the approach supports stable out-of-tree backend releases within 30 days of each upstream update.

**Shipping PyTorch and Its Ecosystem: A Modern Release Story**

**Andrey Talman, Meta**

**October 20, 11:45–11:55 a.m. | LL21DEF | Lightning Talk**

This talk covers changes to PyTorch release engineering across three areas: a faster and more predictable release process; continuous validation of Triton and vLLM against PyTorch nightlies so breakage surfaces upstream early; and AI agents that triage CI, separate noise from regressions, and draft fixes.

The session also examines where agents accelerate release work and where humans still make the call.

**Scaling PyTorch’s Compatibility Promise: A Tiered Cross-Repository CI Relay for Out-of-Tree Backends**

**Subin George, Red Hat LLC; Jewel K M, Red Hat**

**October 20, 12:00–12:10 p.m. | LL21DEF | Lightning Talk**

This talk presents the Cross-Repository CI Relay, or CRCR, which forwards PyTorch PR and push events to downstream repositories in real time for compatibility validation before merge. It covers a four-tier trust model ranging from event dispatch through blocking merge prerequisites, along with the relay, ingestion, visualization, and security architecture.

The speakers report that deployment with Ascend NPU and RISC-V backends reduces breakage detection from days to minutes.

**Fighting Agents with Agents Bringing Claude to PyTorch CI, triage, and PR review**

**Driss Guessous, Meta**

**October 20, 12:35–12:45 p.m. | LL21DEF | Lightning Talk**

PyTorch maintainers are reviewing an increasing number of PRs written by AI agents. This talk covers how Claude was added to PyTorch infrastructure through @claude on issues and PRs, automatic issue triage, reusable onboarding for pytorch and meta-pytorch repositories, PR review skills, and CI and autorevert investigation.

The session also covers Bedrock/OIDC setup, two-stage GitHub Actions, tool allowlists, and repository-specific skills, with the stated goal of supporting maintainers rather than replacing them.

**Clearing the Path Towards an ABI Stable PyTorch C++ Extension Ecosystem**

**Sean McGovern, Red Hat; Chris Leonard, Red Hat; Jane Xu, Meta**

**October 21, 2:15–2:40 p.m. | LL21ABC | Breakout Session**

PyTorch’s stable ABI provides a binary-compatible C interface that extensions can target across PyTorch versions without recompilation. This session presents tools for identifying and inventorying unstable API usage and applying source-to-source conversion, with LLM-assisted follow-up for migration work.

The speakers demonstrate the process on libraries including vLLM and SGLang.

**Compiler, Runtime, Tensor, and Observability Work**

**Beyond Size and Stride: Unleash Performance with Device-Aware Tensor Layouts**

**Olivier Tardieu, IBM; Matthew Arnold, IBM Research**

**October 20, 4:20–4:30 p.m. | LL20AB | Lightning Talk**

PyTorch tensors encode size, stride, and storage offset, but the speakers argue that these fields are insufficient to capture hardware layouts required by modern accelerators. This session introduces a tensor layout extension for device-aware specialization, including tiling and NUMA-aware placement, while preserving standard PyTorch tensor semantics.

The speakers also demonstrate how torch.compile and Inductor can use these controls to adapt layouts to the target device and adjust computations.

**Observability Tooling for Cudagraph Workloads**

**Natalia Gimelshein, Meta; Driss Guessous, Meta**

**October 20, 4:20–4:30 p.m. | LL21DEF | Lightning Talk**

Cudagraph workloads can make profiling, stream visualization, and memory tracking difficult. This talk covers PyTorch utilities for using information captured during graph capture to enrich runtime information collected during replay.

The goal is more information-rich performance and memory monitoring at low overhead, including nearly zero-overhead always-on monitoring.

**Nested Graph Breaks: Reducing the Cost of Graph Breaks in torch.compile**

**William Wen, Meta**

**October 20, 4:35–4:45 p.m. | LL20AB | Lightning Talk**

A nested graph break previously caused O(N) duplicate graph breaks, O(N) graphs to be traced, and O(N²) frame traces for a function call O(N) layers deep.

This session presents nested graph break support in Dynamo, reducing those costs to O(1) duplicate graph breaks, O(1) graphs traced, and O(N) frame traces. The speakers report larger captured graphs, fewer graph breaks, reduced Dynamo trace time, and improved debuggability.

**Static Tensor Shape Checking for PyTorch with Pyrefly**

**Steven Troxler, Meta Platforms; Avik Chaudhuri, Meta**

**October 20, 5:30–5:55 p.m. | LL20AB | Breakout Session**

This session presents static tensor shape checking in the Pyrefly type checker, including inline tensor-shape hints and detection of mismatches before execution.

The speakers cover symbolic integers, Tensor and Dim types, a shape-transform DSL, evaluation across 28 models spanning LLMs, vision, recommenders, and reinforcement learning, and AI-assisted annotations using a Claude skill.

**TorchInsights: Zero-GPU Memory & Runtime Estimation for Distributed Training and Agentic Research**

**Sanket Jayant Purandare, Meta; Aditya Venkataraman, Meta**

**October 20, 5:45–5:55 p.m. | LL21ABC | Lightning Talk**

TorchInsights estimates memory use and runtime for distributed training without running workloads on GPUs. Using fake tensors and fake execution, it can break down peak memory, sweep training configurations, rank parallelism plans, and simulate multi-stream GPU execution with Perfetto traces.

The tool uses pluggable cost models and is also presented as a lower-cost evaluation loop for AI-agent auto-research before spending real GPU time.

**Parametrized Dynamic Shape CUDA Graphs**

**Elias Ellison, Meta; Daniel Galvez, NVIDIA**

**October 21, 11:45 a.m.–12:10 p.m. | LL21ABC | Breakout Session**

Dynamic workloads can require padding, on-device shapes, repeated recordings, or larger model changes to use CUDA Graphs. This session combines parametrized CUDA Graphs with torch.compile’s symbolic tracing and guard infrastructure to capture and re-parametrize a single CUDA Graph across dynamic shapes.

The speakers report performance wins and reduced cold-start times for inference serving.

**Native DSL Operators in PyTorch Core**

**Simon Layton, Meta**

**October 21, 2:50–3:15 p.m. | LL21ABC | Breakout Session**

DSL-authored kernels have largely remained outside PyTorch core. This talk presents work toward adding DSL-authored operators as first-class citizens of PyTorch core, tying them into dispatch and testing.

The work is intended to support new operators, highly optimized implementations, and targeted fixes for specialized performance cliffs.

**From Backed to Unbacked: Sound, Predictable, and Controllable Dynamic Shapes in PyTorch**

**Laith Sakka, Meta**

**October 21, 4:20–4:45 p.m. | LL21ABC | Breakout Session**

Backed dynamic shapes use symbolic sizes together with example-input hints and guards, which can allow recompilation. For workflows including vLLM, export, pre-compilation, and JIT deployments where dynamic-shape recompilation is not acceptable, this talk presents unbacked shapes, which disallow implicit guards on dynamic shapes.

The session covers data-dependent errors and branching, work to close the performance gap with backed shapes across TorchBench and vLLM, and APIs for shape constraints and dispatch across compiled artifacts.

**Speeding Up torch.compile: A New FakeTensor**

**Angel Li, Meta****October 21, 4:55–5:05 p.m. | LL21ABC | Lightning Talk**

FakeTensor is a lightweight substitute for regular tensors used by Dynamo and Inductor when building FX graphs, but its propagation contributes to torch.compile tracing time.

The speaker reports that one FakeTensor propagation takes around 20% of total Dynamo tracing time and that `aten.mm`

takes around 225 microseconds with a Python FakeTensor, while a C++ FakeTensor shows a 30x speedup for that operation. The talk covers key changes, design decisions, performance benchmarks, and integration with the torch.compile ecosystem.

**Lightweight FX Tracing in PyTorch**

**Richard Zou, Meta; Yidi Wu, Meta Inc.**

**October 21, 5:10–5:20 p.m. | LL21ABC | Lightning Talk**

Dynamo traces Python bytecode and can fall back to graph breaks, but the speakers say they have received feedback that Dynamo is too heavy for use cases where users require a full graph.

This talk presents a lightweight FX tracer based on make_fx for functionally pure PyTorch code. It covers the API, its guarantees, how it differs from Dynamo, and how it interacts with other APIs.

**Distributed Communication and Device Portability**

**PyTorch Generalization: A Journey Toward Write Once, Run Anywhere**

**Yu Guangye, Intel; Eikan Wang, Intel**

**October 20, 12:20–12:30 p.m. | LL21DEF | Lightning Talk**

This talk covers ongoing work to make PyTorch APIs, runtime interfaces, and testing infrastructure less backend-specific. The speakers focus on model-level API unification across Autocast, Inductor, and graph capture and replay; torch.accelerator for device, stream, event, RNG, and memory management; and test infrastructure spanning Distributed, Dynamo, Inductor, ATen operators, and more.

The stated goal is a consistent user and developer experience across in-tree and out-of-tree backends.

**Future of Distributed Communication in PyTorch: New APIs for Fault Tolerance, RDMA and Extensibility**

**Tristan Rice, Meta; Kapil Sharma, Meta**

**October 20, 4:20–4:45 p.m. | LL21ABC | Breakout Session**

This talk presents new APIs for fault tolerance, one-sided RDMA, collective hooks, backend extensibility, and backend interfaces. Examples include torch.distributed.reconfigure() for live process-group reconfiguration after rank failures, Window APIs for one-sided put/get, composable hooks for collectives, and pip-installable backends registered through entry_points.

The speakers say these features were incubated in TorchComms and are now being upstreamed into torch.distributed.

**rocSHMEM Symmetric Memory in PyTorch for AMD GPUs**

**Prachi Gupta, AMD****October 20, 4:35–4:45 p.m. | LL21DEF | Lightning Talk**

PyTorch symmetric memory issues communication from within device kernels, including Triton, allowing communication to overlap with computation. This talk covers extending that capability to AMD GPUs through rocSHMEM, now available in upstream PyTorch.

The session covers rocSHMEM device-side OpenSHMEM primitives exposed as Triton-callable operations, AMD-specific device-bitcode linking and HIP-module initialization behind a backend-agnostic layer shared with NVSHMEM, and a comparison with RCCL host-driven all-to-all on representative Mixture-of-Experts workloads.

**XCCL: Scaling PyTorch Collectives to Exascale on Intel GPUs with TorchComms**

**Panagiotis Kourdis, Intel; Tanima Dey, Intel Corporation**

**October 20, 5:10–5:20 p.m. | LL21ABC | Lightning Talk**

XCCL adds native Intel GPU support to TorchComms through an in-tree backend built on Intel’s oneCCL library.

The speakers report over 90% scaling efficiency across thousands of nodes on Argonne National Laboratory’s Aurora system while running TorchTitan and other AI workloads. The talk also covers a stream-ordered asynchronous execution model, differences between PyTorch collective semantics and oneCCL, CI, testing on Intel hardware, and comparisons with NCCL and RCCL.

**Introducing NCCL Extensions: Communication Patterns for Modern AI**

**Sreeram Potluri, NVIDIA; Artem Polyakov, NVIDIA**

**October 21, 4:55–5:20 p.m. | 210AE | Breakout Session**

NCCL domain extensions are specialized libraries built on NCCL Device APIs for emerging communication patterns. This session introduces NCCL-EP for Mixture-of-Experts dispatch and combine and NCCL-M2N for zero-copy resharding between disjoint device meshes.

The speakers cover their design rationale, APIs, and performance results, including the use of NCCL-M2N to move weight snapshots from trainers to inference replicas for reinforcement learning rollout without CPU staging.

**Accelerator Integration and Hardware-Aware Tooling**

**Integrating the IBM Spyre Accelerator**

**David Grove, IBM; Antoni Viros Martin, IBM Research; Avery Blanchard, IBM Research**

**October 20, 4:55–5:20 p.m. | LL21DEF | Breakout Session**

Torch-Spyre is an open source project that provides a PyTorch PrivateUse1 device with OpenReg, including an Inductor backend, for the IBM Spyre Accelerator.

The talk covers the state of Torch-Spyre, functional enablement and performance improvements made in 2026, and contributions made back to PyTorch. It also discusses device-specific tensor layouts and scratchpad-optimized tiling, with an emphasis on integration with upstream PyTorch.

**TorchTPU: Running PyTorch Natively on Google TPUs**

**Claudio Basile, Google****October 21, 11:10–11:35 a.m. | LL21ABC | Breakout Session**

This session presents TorchTPU as a high-performance, native PyTorch backend for Google TPUs. It covers an eager-first stack with ATen-to-StableHLO lowering and “DeferAndFuse” execution, an XLA stack that uses SparseCore for compute-communication overlap, bounded dynamism, and integrations with vLLM and TorchTitan.

The speaker reports production-scale engagements with private preview partners and describes TorchTPU as transitioning to an open source model, with a public GitHub repository release upcoming.

**From torch.profiler to Hardware Cycles: A Practical Profiling Playbook for AWS Trainium**

**Esha Lakhotia, AWS Annapurna Labs; Pinak Panigrahi, Amazon**

**October 21, 12:20–12:45 p.m. | LL21ABC | Breakout Session**

This session shows how the torch.profiler API can be used on AWS Trainium without code changes or separate tooling, from CPU dispatch and runtime orchestration down to on-device hardware execution.

The speakers walk through tracing slow model components to compiled operations and Python source, using cycle-level device timelines to identify bottlenecks, and AI-assisted analysis that identifies performance bottlenecks and suggests potential fixes.

**Explore the Full Program**

These sessions represent part of our Core PyTorch program across October 20 and 21. Explore the full PyTorch Conference North America program for additional sessions across training, inference, applications, kernel engineering, responsible AI, and more.
