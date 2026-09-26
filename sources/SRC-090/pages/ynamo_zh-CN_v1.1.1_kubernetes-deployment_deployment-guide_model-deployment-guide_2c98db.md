source: https://docs.nvidia.com/dynamo/zh-CN/v1.1.1/kubernetes-deployment/deployment-guide/model-deployment-guide
lastmod: 2026-09-23T23:30:39.914Z

# Model Deployment Guide

This guide explains how to deploy your model on Dynamo using a
`DynamoGraphDeploymentRequest`

(DGDR). If you’ve completed the
[Quickstart](https://docs.nvidia.com/dynamo/v1.1.1/getting-started/kubernetes-deployment) and want to understand how DGDR works end-to-end, how
to choose the right settings for your model, and how to avoid common pitfalls,
this is the place.

For the DGDR spec reference, field descriptions, and lifecycle phases, see the
[DGDR Reference](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/dgdr-reference).

## What is a DGDR?

A DGDR is Dynamo’s **deploy-by-intent** Custom Resource. Instead of hand-crafting
a deployment spec with parallelism settings, replica counts, and resource limits,
you describe *what* you want to run (model, backend, SLA targets) and DGDR
automates the rest:

**Spec**— You submit a DGDR with your model, workload expectations, and optional SLA targets.**Hardware Discovery**— The operator discovers your cluster’s GPU hardware (SKU, VRAM, count per node) via DCGM or node labels.**Profiling**— The profiler analyzes your model against the discovered hardware, using either rapid simulation or thorough real-GPU benchmarking.**DGD Generation**— The profiler produces an optimized`DynamoGraphDeployment`

(DGD) spec with the best parallelization strategy, replica counts, and resource configuration.**Review**(when`autoApply: false`

) — The generated DGD is stored in`.status.profilingResults.selectedConfig`

for you to inspect and optionally modify before deploying.**Deploy**— The operator creates the DGD, which provisions the inference pods.**Planner**(optional) — If enabled, the Planner monitors live traffic and adjusts replica counts at runtime to meet your SLA targets.

## Choosing a Search Strategy

The `searchStrategy`

field controls how the profiler explores configurations.
Your choice depends on how much time you can invest and how close to optimal
you need.

### Rapid (Default)

Uses the **AI Configurator (AIC)** to simulate GPU performance without
running real inference. Completes in ~30 seconds with no GPU resources consumed
during profiling.

**Use rapid when:**

- Getting started or iterating quickly
- Running in CI/CD pipelines
- Your GPU SKU is in the
[AIC support matrix](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/model-deployment-guide#aic-support-matrix)

**Limitations:**

- If AIC does not support your model/hardware/backend combination, the profiler falls back to a naive memory-fit config (basic TP calculation) which may not be optimal.
- Simulated results may differ from real-hardware performance for unusual configurations.

### Thorough

Enumerates candidate parallelization configs, deploys each on real GPUs, and benchmarks with AIPerf. Takes 2–4 hours.

**Use thorough when:**

- Tuning for production and you need the most optimal configuration
- Your hardware is not supported by AIC (e.g., PCIe GPUs)
- You want measured rather than simulated performance data

**Constraints:**

**Disaggregated mode only**— thorough does not run aggregated configurations.— you must specify`backend: auto`

is not supported`vllm`

,`sglang`

, or`trtllm`

. The DGDR will be rejected if you use`auto`

with`thorough`

.**Requires GPU resources**— the profiler deploys real inference engines on your cluster during profiling.

## AIC Support Matrix

The rapid strategy relies on AIC performance models. AIC currently supports:

### GPU SKUs

If your GPU is not in the “Supported” column, rapid mode will fall back to a
naive config. Use `searchStrategy: thorough`

for optimal results on
unsupported hardware.

When specifying GPU SKUs manually, use lowercase underscore format (e.g.,
`h100_sxm`

, not `H100-SXM5-80GB`

). See the
[DGDR Reference — SKU Format](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/dgdr-reference#sku-format) for the full list.

### Backends

All three backends are supported for both rapid and thorough:

**If you are deploying a Mixture-of-Experts (MoE) model** (e.g., DeepSeek-R1,
Qwen3-MoE), use **SGLang** as the backend for full support. vLLM and TRT-LLM
have partial MoE support that is still under development.

### Parallelization Strategies

The profiler selects different parallelization strategies depending on the model architecture:

## Model Caching

**Set up model caching before deploying if any of these apply:**

- Your model is large (>70B parameters) — downloading hundreds of GB per pod takes hours
- You are scaling to many replicas — each pod downloads the full model independently, and HuggingFace will rate-limit concurrent downloads
- You want fast pod startup on scaling events

### How It Works with DGDR

Add a `modelCache`

section to your DGDR spec that points to a pre-populated PVC:

The operator mounts this PVC at `pvcMountPath`

read-only into the profiling job
and passes it through to the generated DGD, so both profiling and serving use
the cached weights.

`pvcModelPath`

must be the HuggingFace snapshot path inside the PVC —
`hub/models--<org>--<model>/snapshots/<commit-hash>`

. This follows the layout
that `huggingface-cli download`

creates when `HF_HOME`

is set to the mount
point. Replace `<org>--<model>`

by substituting `/`

with `--`

in the model ID,
and replace `<commit-hash>`

with the actual snapshot revision. See
[Model Caching](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/model-caching.md#find-the-snapshot-path) for how to look up the
hash after downloading.

### Setup

- Create a
`ReadWriteMany`

PVC — see the[Installation Guide — Shared Storage](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/installation-guide#shared-storage-for-model-caching)for provider-specific options (EFS, Azure Lustre, GKE Filestore). - Run a one-time download Job to populate the PVC.
- Reference the PVC in your DGDR’s
`modelCache`

field.

See [Model Caching](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/model-caching.md) for the full walkthrough with YAML
examples.

### Private and Gated Models

For models that require authentication (e.g., gated HuggingFace models), create
a Kubernetes Secret named `hf-token-secret`

with a `HF_TOKEN`

key:

The profiler and deployed pods will automatically use this token.

## Enabling the Planner

The Planner provides **runtime autoscaling** for disaggregated deployments. It
adjusts prefill and decode replica counts to meet your SLA targets as traffic
fluctuates.

### Planner Scaling Modes

### Prometheus Requirement

The `sla`

optimization target reads live TTFT/ITL metrics from Prometheus. If
you want SLA-driven autoscaling, install Prometheus before creating the DGDR.
See the [Installation Guide — Prometheus](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/installation-guide#kube-prometheus-stack)
for setup instructions.

The `throughput`

and `latency`

modes use internal queue-depth signals and work
**without Prometheus**.

See the [Planner Guide](https://docs.nvidia.com/dynamo/v1.1.1/components/planner/planner-guide) for advanced
configuration and scaling behavior details.

## Multinode Deployments

Models that require more GPUs than a single node provides (e.g., DeepSeek-R1 on 8-GPU nodes) need multinode orchestration.

### Grove and KAI Scheduler

**Grove** is required for multinode DGDR deployments. It provides gang
scheduling (all pods in a group start together or not at all), coordinated
scaling, and network topology-aware placement. The operator will return an error
if you attempt a multinode deployment without Grove or LeaderWorkerSet (LWS)
installed.

**KAI Scheduler** is optional but recommended alongside Grove for GPU-aware
scheduling and topology optimization.

See the [Installation Guide — Grove + KAI Scheduler](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/installation-guide#grove--kai-scheduler)
for setup instructions and the compatibility matrix.

### High-Speed Networking (RDMA)

Disaggregated serving transfers KV cache data between prefill and decode workers. Understanding the networking stack helps you diagnose performance issues:

Without RDMA, NIXL falls back to TCP, causing **~40x degradation** in TTFT
(from ~355ms to 10+ seconds).

**Enable RDMA if:**

- You are running multinode disaggregated deployments
- You need low-latency KV cache transfer between workers

See the [Installation Guide — Network Operator / RDMA](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/installation-guide#network-operator--rdma)
for provider-specific setup instructions, and the
[Disaggregated Communication Guide](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/disagg-communication) for transport
details and performance expectations.

### MoE Models and Multinode Sweep Limits

The profiler sweeps MoE models across up to **4 nodes** (dense models: 1 node
max per engine during sweep). If your MoE model requires more than 4 nodes of
GPUs, the profiler will select the best config within that range and you may
need to adjust replica counts manually.

## Backend Selection

The `backend`

field controls which inference engine is used. The default
(`auto`

) lets the profiler pick the best backend, but you should specify a
backend explicitly in these cases:

TensorRT-LLM does not support Python 3.11. If your environment uses
Python 3.11, use `vllm`

or `sglang`

instead.

### Multinode Backend Behavior

Each backend handles multinode inference differently:

**vLLM**: Uses Ray for multi-node TP/PP. Ray head runs on the leader, agents on workers.**SGLang**: Uses`--dist-init-addr`

,`--nnodes`

,`--node-rank`

flags for distributed setup.**TRT-LLM**: MPI-based. The operator auto-generates SSH keypairs; the leader runs`mpirun`

.

## Common Pitfalls

### OOM During Profiling or Serving

**Cause**: The model doesn’t fit in GPU memory with the selected TP size.**Fix**: Ensure`hardware.totalGpus`

is large enough for your model. The profiler calculates minimum TP from model size and VRAM, but edge cases (large context lengths, KV cache overhead) may require more GPUs than the minimum.

### GPU Auto-Detection Cap

The operator caps auto-detected GPU count at **32**. If your cluster has more
GPUs and you want the profiler to use them, set `hardware.totalGpus`

explicitly:

### Profiling Job Fails to Schedule

GPU nodes often have taints. Add tolerations via the `overrides`

field:

### DGDR Spec Is Immutable

Once the DGDR enters the `Profiling`

phase, the spec cannot be changed. If you
need to adjust settings, delete the DGDR and recreate it:

### DGD Persists After DGDR Deletion

Deleting a DGDR does **not** delete the DGD it created. This is intentional —
the DGD continues serving traffic independently. To clean up fully:

## Putting It Together: Example Workflows

### Small Dense Model (Quick Start)

A small model on a single node with rapid profiling — the simplest case:

### Large Dense Model with SLA Targets

A 70B model with model caching, SLA targets, and the planner enabled:

### MoE Model (DeepSeek-R1)

A large MoE model requiring multinode, SGLang backend, and thorough profiling:

**Prerequisites for this deployment:**

[Grove and KAI Scheduler](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/installation-guide#grove--kai-scheduler)installed[RDMA](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/installation-guide#network-operator--rdma)configured for efficient KV cache transfer- Model
[cached on a shared PVC](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/installation-guide#shared-storage-for-model-caching) [Prometheus](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/installation-guide#kube-prometheus-stack)installed (for SLA-driven planner scaling)

## Further Reading

[DGDR Reference](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/dgdr-reference)— Spec reference, lifecycle phases, monitoring commands[DGDR Examples](https://docs.nvidia.com/dynamo/v1.1.1/components/profiler/profiler-examples)— Ready-to-use YAML for various scenarios[Profiler Guide](https://docs.nvidia.com/dynamo/v1.1.1/components/profiler/profiler-guide)— Profiling algorithms, picking modes, gate checks[Planner Guide](https://docs.nvidia.com/dynamo/v1.1.1/components/planner/planner-guide)— Scaling modes, PlannerConfig reference[Model Caching](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/model-caching.md)— PVC setup and Model Express[Creating Deployments](https://docs.nvidia.com/dynamo/v1.1.1/additional-resources/creating-deployments)— Manual DGD spec for hand-crafted configs[Multinode Deployments](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/multinode/multinode-deployments)— Grove, LWS, and multinode details[Disaggregated Communication](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/disagg-communication)— NIXL, RDMA, and networking