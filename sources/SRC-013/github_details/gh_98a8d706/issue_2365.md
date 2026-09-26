# [Issue #2365] [Incubation] Snapshot Orchestrator

source: https://github.com/llm-d/llm-d/issues/2365
state: open | updated: 2026-08-26T18:04:57Z
labels: 

## 正文

# Proposal: `snapshot-orchestrator` as an incubation project

## Summary

Snapshot Orchestrator is a Kubernetes-native controller that enables sleep/wake lifecycling of vLLM inference engines using CRIU and NVIDIA cuda-checkpoint. After a vLLM server has fully warmed up, the system freezes its state to disk as a golden snapshot via a three-layer process: vLLM sleep mode (discards GPU memory), cuda-checkpoint (suspends GPU driver state), and CRIU (dumps the CPU-only process tree). Future pods serving the same model restore from this snapshot instead of cold-booting, skipping CUDA init, warmup, and compile.

The system does not create or delete workload Pods. It observes vLLM Pods created by their own Deployment and operates as an add-on layer, coordinating exclusively through a `SnapshotCheckpoint` CRD and Pod labels/annotations. It ships a fail-closed scheduling integration for the llm-d EPP via pod labels and a custom readiness gate (`snapshot.llm-d.ai/Serving`).

## Why llm-d

**Cold-start is a first-class problem for the Inference Gateway.** The EPP makes routing decisions based on pod readiness. A pod that takes 60–120 seconds to become ready is a pod the gateway cannot use — the GPU is allocated but not serving. Snapshot restore turns this into a seconds-level operation, directly improving the gateway's ability to scale and rebalance.

**Native EPP integration.** The orchestrator publishes lifecycle state via pod labels (`snapshot.llm-d.ai/state`), letting the EPP exclude non-serving replicas (draining, checkpointing, restoring) without a separate coordination layer. This is purpose-built for llm-d's discovery model.

**Owning the API surface.** Having the orchestrator in llm-d means the `SnapshotCheckpoint` CRD, lifecycle annotations, and controller behavior can evolve with llm-d's needs — scale-to-zero, fan-out policies, multi-vendor GPU support — without external release-cadence dependencies.

**Shared primitives, independent orchestration.** The underlying tools (CRIU, cuda-checkpoint) are upstream projects. Owning the orchestration layer means future checkpoint APIs from other hardware vendors (AMD, Intel) can be integrated into one framework rather than forking per-vendor serving stacks.

## Scope

**In scope**
  - DaemonSet node agent: pod lifecycle state machine, CRIU dump/restore, cuda-checkpoint, vLLM sleep/wake, namespace entry for container operations, `SnapshotCheckpoint` CR management
  - Snapshot controller: TTL-based garbage collection of unused checkpoints, finalizer-driven on-disk cleanup, orphaned CR removal
  - Mutating admission webhook: readiness gate injection for managed pods
  - Snapshot shim: PID 1 binary for vLLM containers that holds the container alive for agent-driven cold-boot or restore
  - `SnapshotCheckpoint` CRD: compatibility-keyed checkpoint records with multi-node storage locations
  - Pod labels/annotations for EPP integration (`snapshot.llm-d.ai/state`, readiness gate)
  - Deployment manifests (DaemonSet, controller, RBAC, CRD)

**Out of scope**
  - Serving data plane — the orchestrator does not own or manage the vLLM deployment itself
  - Multi-GPU topologies (TP > 1 with NCCL/CUDA IPC, P/D, MoE) — future work
  - Pod controllers beyond Deployment (LWS, DisaggregatedSet) — future work
  - `SnapshotPolicy` CRD for per-selector cleanup policies — future work
  - Non-vLLM inference engines

  ## Why now
  
GPU cold-start is the most common complaint in production inference deployments. A typical vLLM server takes 60–120 seconds to become ready — loading weights, warming CUDA kernels, initializing KV cache. During this window the GPU is allocated but idle, wasting expensive compute. As models grow and llm-d adoption increases, this problem scales linearly with fleet size. The primitives are ready. vLLM sleep mode (level 2) is shipping, with gRPC control plane support in flight ([vllm-project/vllm#51316](https://github.com/vllm-project/vllm/pull/51316)). NVIDIA's cuda-checkpoint handles GPU driver state. CRIU is mature. The prototype has validated the full sleep → cuda-checkpoint → CRIU chain end-to-end, including the CUDA VMM (cumem) allocator that sleep mode uses.

  ## Evidence

The internal prototype (under neuralmagic private org has validated the end-to-end chain.  Comparison across models:

| | Qwen3-8B | Qwen3-30B-A3B (MoE) |
  |---|---|---|
  | Cold boot | ~1m35s | ~3m51s |
  | Checkpoint | ~12.5s | ~20.3s |
  | Restore | ~8.4s | ~15.8s |
  | Dump size | 4.7 GiB | 5.6 GiB |
  
## Demand
  
Any organization running GPU inference at scale hits the cold-start wall. Specific scenarios where snapshot restore is critical:
  - **Autoscaling:** scaling from 0→N or N→N+M replicas means N or M GPUs sitting idle during cold-boot. Snapshot restore makes scale-up near-instant.
  - **Preemption recovery:** spot/preemptible GPU instances get reclaimed. Restarting on a new node with a snapshot avoids repeating the full init.
  - **Model rollout:** deploying a new model version across a fleet means a rolling wave of cold-boots. Snapshotting the first pod and restoring the rest turns an
  O(N) cold-boot into O(1) + O(N) fast restores.
  
  ## First milestone
  
  Deliberately narrow — get the core loop production-ready:
  
  - [ ] Transfer repository to `llm-d/snapshot-orchestrator`
  - [ ] Implement the mutating admission webhook (readiness gate injection)
  - [ ] Selective finalizer removal in the controller (currently removes all, has a known TODO)
  - [ ] Unit and integration test coverage for agent lifecycle state machine and controller GC
  - [ ] CI pipeline (lint, test, build) in llm-d CI infrastructure
  - [ ] End-to-end test: Deployment annotation → cold-boot → checkpoint → delete pod → new pod restores from snapshot
  - [ ] Documentation: installation guide, architecture overview, EPP integration guide
  
## Maintainers
  
  - Omer Aplatony (@omerap12, Red Hat) 
  - Will Eaton (@wseaton , Red Hat)
  - Edoardo Vacchi (@evacchi, Red Hat)
  
## The ask
  
  Create `llm-d/snapshot-orchestrator` as an incubation-stage repository under the llm-d org. The existing prototype at neuralmagic org would be transferred as the starting point. The first milestone focuses on production-readying the core checkpoint/restore loop with proper test coverage, the missing webhook, and llm-d CI integration. The orchestrator is designed to integrate with the EPP out of the box via pod labels and readiness gates, requiring no changes to existing llm-d components.

## 评论 (4)

### omerap12 · 2026-08-24

/cc @anishasthana @vMaroon 

### ahg-g · 2026-08-26

/cc @nicolexin 

### nicolexin · 2026-08-26

@omerap12 Have you seen [vllm-project/vllm#34303](https://github.com/vllm-project/vllm/issues/34303)? It's an RFC for CUDA checkpoint/restore inside vLLM, and its later phases cover CRIU integration too, so there's some overlap with the node agent here. Curious to get your thoughts on how we might best align the two approaches. 

### aishukamal · 2026-08-26

@omerap12 This is great to see! We've been working on something very similar in llm-d incubation: [snapshot-agent](https://github.com/llm-d-incubation/llm-d-rl-time-slicing/blob/main/guides/snapshot-agent/README.md). We built it for time-slicing RL workloads. At its core, snapshot-agent is a Kubernetes DaemonSet that provides pluggable snapshot backends to move data between VRAM and host.

It already has cuda-checkpoint and vLLM sleep/wake backends, so two of the three layers in your proposal are covered. We also have plans to add a CRIU backend down the road. We already cover other engines (like SGLang) and are starting to work on multi-GPU support, which would align well with your planned future work.

We would love to collaborate and consolidate the efforts if you're open to it!

/cc @BogdanAtWork
