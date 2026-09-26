source: https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/deploy-models/model-deployment-guide
lastmod: 2026-09-24T19:58:16.636Z

# Deployment Overview

Dynamo’s canonical Kubernetes deployment is a
[ DynamoGraphDeployment](https://docs.nvidia.com/dynamo/v1.3.0/additional-resources/api-reference-k-8-s#dynamographdeployment) (DGD). A DGD
describes the inference graph you want to run. The Dynamo operator reconciles
that graph into one or more

[(DCD) resources, which run the frontend, router, prefill workers, decode workers, and other graph components.](https://docs.nvidia.com/dynamo/v1.3.0/additional-resources/api-reference-k-8-s#dynamocomponentdeployment)

`DynamoComponentDeployment`

This is the Kubernetes-native control path for Dynamo: you author or generate Dynamo resources, and the operator translates them into Kubernetes workloads, services, routing metadata, model-loading resources, and status conditions. For local development or incremental adoption, you can still run the same frontend, router, and worker components outside Kubernetes.

You can create a DGD directly from a known-good manifest, or you can use a
[ DynamoGraphDeploymentRequest](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/deploy-models/dgdr-reference) (DGDR) to profile your model and
generate a DGD for you.

Most users only need three ideas before they deploy:

**Recipes are the fastest path**when one matches your model, backend, hardware, and serving pattern. They are already DGD manifests.**DGDR is the guided path**when you want Dynamo to profile and generate a DGD from model/SLA intent.**DGD is the object that serves traffic**. DGDR can create it, but the DGD is what persists after profiling completes.

You do not need to author DCDs directly for normal deployments.

## Start Here: Resource Model

## Choose Your Path

Start with the row that matches your situation. The sections later in this page are reference material; you can read them as needed instead of going linearly.

## Deploy a Tuned DGD from Recipes

If a [recipe](https://github.com/ai-dynamo/dynamo/tree/v1.3.0/recipes) matches
your target model, backend, GPU type, and serving mode, start there. Recipes are
curated `DynamoGraphDeployment`

manifests with model-cache setup and, for many
recipes, benchmark jobs.

The common recipe flow is:

Follow the README in the specific recipe directory for model-specific images, GPU requirements, cache setup, and request examples.

## Use DGDR to Generate a DGD

A DGDR is Dynamo’s deploy-by-intent path. Instead of hand-crafting a deployment spec with parallelism settings, replica counts, and resource limits, you describe what you want to run (model, backend, workload, SLA targets) and DGDR generates a DGD:

**Spec**— You submit a DGDR with your model, workload expectations, and optional SLA targets.**Hardware Discovery**— The operator discovers your cluster’s GPU hardware (SKU, VRAM, count per node) via DCGM or node labels.**Profiling**— The profiler analyzes your model against the discovered hardware, using either rapid simulation or thorough real-GPU benchmarking.**DGD Generation**— The profiler produces an optimized`DynamoGraphDeployment`

(DGD) spec with the best parallelization strategy, replica counts, and resource configuration.**Review**(when`autoApply: false`

) — The generated DGD is stored in`.status.profilingResults.selectedConfig`

for you to inspect and optionally modify before deploying.**Deploy**— With`autoApply: true`

, the operator creates the DGD. With`autoApply: false`

, you apply the generated DGD yourself.**Planner**(optional) — If enabled, the Planner monitors live traffic and adjusts replica counts at runtime to meet your SLA targets.

DGDR currently supports generated-deployment feature configuration for Planner
(`features.planner`

) and mocker mode (`features.mocker`

). The DGDR API does not
currently expose `features.kvRouter`

; configure explicit router mode in a DGD,
a tuned recipe, or a generated DGD override when you need KV-aware routing
details.

For the DGDR spec reference, field descriptions, and lifecycle phases, see the
[DGDR Reference](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/deploy-models/dgdr-reference).

## DGDR Detail: Choose a Search Strategy

The `searchStrategy`

field controls how the profiler explores configurations.
Your choice depends on how much time you can invest and how close to optimal
you need.

### Rapid (Default)

Uses AIC-backed DynoSim-style performance modeling to search deployment configurations without running real inference. Completes in ~30 seconds with no GPU resources consumed during profiling.

**Use rapid when:**

- Getting started or iterating quickly
- Running in CI/CD pipelines
- Your GPU SKU is in the
[AIC support matrix](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/deploy-models/model-deployment-guide#aic-support-matrix)

**Limitations:**

- Fallback to a naive memory-fit config only applies after DGDR accepts
`hardware.gpuSku`

. Fallback sizing depends on AIC system metadata and does not add support for additional GPU SKUs; unsupported model/GPU/backend combinations can fall back but may be suboptimal. - Simulated results may differ from real-hardware performance for unusual configurations.

### Thorough

Enumerates candidate parallelization configs, deploys each on real GPUs, and benchmarks with AIPerf. Takes 2–4 hours.

**Use thorough when:**

- Tuning for production and you need the most optimal configuration
- You want measured rather than simulated performance data

**Constraints:**

**Disaggregated mode only**— thorough does not run aggregated configurations.— you must specify`backend: auto`

is not supported`vllm`

,`sglang`

, or`trtllm`

. The DGDR will be rejected if you use`auto`

with`thorough`

.**Still requires AIC generator support**— thorough measures candidates on real GPUs, but uses AIC to enumerate candidates and generate the final DGD.**Requires GPU resources**— the profiler deploys real inference engines on your cluster during profiling.

## DGDR Detail: AIC Support Matrix

The rapid strategy relies on AIC system metadata and performance models. Check
the [AIC support matrix](https://ai-dynamo.github.io/aiconfigurator/support-matrix/)
for the latest support. Measured profiling still needs AIC system and generator
support to enumerate and render candidates; rapid also needs performance support
for the exact model/GPU/backend combination.

### GPU SKUs

Some rapid-mode SKUs use AIC estimate-only data until measured profiles are
available. Use `searchStrategy: thorough`

for measured profiling only when
DGDR accepts the SKU and AIC has system and generator support for it.

When specifying GPU SKUs manually, use lowercase underscore format (e.g.,
`h100_sxm`

, not `H100-SXM5-80GB`

). See the
[DGDR Reference — SKU Format](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/deploy-models/dgdr-reference#sku-format) for the full list.

### Backends

All three backends are supported for both rapid and thorough:

**If you are deploying a Mixture-of-Experts (MoE) model** (e.g., DeepSeek-R1,
Qwen3-MoE), use **SGLang** as the backend for full support. vLLM and TRT-LLM
have partial MoE support that is still under development.

### Parallelization Strategies

The profiler selects different parallelization strategies depending on the model architecture:

## Production Details

After the basic deployment path is clear, use this checklist to decide which production topics apply:

## Production Detail: Model Caching

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
[Model Caching](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/model-loading/model-caching#find-the-snapshot-path) for how to look up the
hash after downloading.

### Setup

- Create a
`ReadWriteMany`

PVC — see the[Installation Guide — Shared Storage](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/installation-guide#shared-storage-for-model-caching)for provider-specific options (EFS, Azure Lustre, GKE Filestore). - Run a one-time download Job to populate the PVC.
- Reference the PVC in your DGDR’s
`modelCache`

field.

See [Model Caching](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/model-loading/model-caching) for the full walkthrough with YAML
examples.

### Private and Gated Models

For models that require authentication (e.g., gated HuggingFace models), create
a Kubernetes Secret named `hf-token-secret`

with a `HF_TOKEN`

key:

The profiler and deployed pods will automatically use this token.

## Production Detail: Planner

The Planner provides **runtime autoscaling** for disaggregated deployments. It
adjusts prefill and decode replica counts to meet your SLA targets as traffic
fluctuates.

### Planner Scaling Modes

### Prometheus Requirement

The `sla`

optimization target reads live TTFT/ITL metrics from Prometheus. If
you want SLA-driven autoscaling, install Prometheus before creating the DGDR.
See the [Installation Guide — Prometheus](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/installation-guide#kube-prometheus-stack)
for setup instructions.

The `throughput`

and `latency`

modes use internal queue-depth signals and work
**without Prometheus**.

See the [Planner Guide](https://docs.nvidia.com/dynamo/v1.3.0/components/planner/planner-guide) for advanced
configuration and scaling behavior details.

## Production Detail: Multinode and RDMA

Models that require more GPUs than a single node provides (e.g., DeepSeek-R1 on 8-GPU nodes) need multinode orchestration.

### Grove and KAI Scheduler

**Grove** is required for multinode DGDR deployments. It provides gang
scheduling (all pods in a group start together or not at all), coordinated
scaling, and network topology-aware placement. The operator will return an error
if you attempt a multinode deployment without Grove or LeaderWorkerSet (LWS)
installed.

**KAI Scheduler** is optional but recommended alongside Grove for GPU-aware
scheduling and topology optimization.

See the [Installation Guide — Grove + KAI Scheduler](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/installation-guide#grove--kai-scheduler)
for setup instructions and the compatibility matrix.

### High-Speed Networking (RDMA)

Disaggregated serving transfers KV cache data between prefill and decode workers. Understanding the networking stack helps you diagnose performance issues:

When RDMA is missing or not active, NIXL can fall back to TCP. That makes KV cache movement the likely bottleneck and can produce very high TTFT or low throughput even when the model workers appear healthy.

**Enable RDMA if:**

- You are running multinode disaggregated deployments
- You need low-latency KV cache transfer between workers

See the [Installation Guide — Network Operator / RDMA](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/installation-guide#network-operator--rdma)
for provider-specific setup instructions, and the
[Disaggregated Communication Guide](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/operate/disagg-communication) for transport
details and performance expectations.

### MoE Models and Multinode Sweep Limits

The profiler sweeps MoE models across up to **4 nodes** (dense models: 1 node
max per engine during sweep). If your MoE model requires more than 4 nodes of
GPUs, the profiler will select the best config within that range and you may
need to adjust replica counts manually.

## Production Detail: Backend Selection

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

**vLLM**: Uses PyTorch multiprocessing (mp) backend with distributed initialization flags for multi-node TP/PP. Each node runs its own vLLM process with synchronized training initialization.**SGLang**: Uses`--dist-init-addr`

,`--nnodes`

,`--node-rank`

flags for distributed setup.**TRT-LLM**: MPI-based. The operator auto-generates SSH keypairs; the leader runs`mpirun`

.

## Troubleshooting

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

## Example Workflows

### Small Dense Model (Quick Start)

A small model on a single node with rapid profiling — the simplest case:

### Large Dense Model with SLA Targets

A 70B model with model caching, SLA targets, and the planner enabled:

### MoE Model (DeepSeek-R1)

A large MoE model requiring multinode, SGLang backend, and thorough profiling:

**Prerequisites for this deployment:**

[Grove and KAI Scheduler](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/installation-guide#grove--kai-scheduler)installed[RDMA](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/installation-guide#network-operator--rdma)configured for efficient KV cache transfer- Model
[cached on a shared PVC](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/installation-guide#shared-storage-for-model-caching) [Prometheus](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/installation-guide#kube-prometheus-stack)installed (for SLA-driven planner scaling)

## Further Reading

[DGDR Reference](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/deploy-models/dgdr-reference)— Spec reference, lifecycle phases, monitoring commands[DGDR Examples](https://docs.nvidia.com/dynamo/v1.3.0/components/profiler/profiler-examples)— Ready-to-use YAML for various scenarios[Profiler Guide](https://docs.nvidia.com/dynamo/v1.3.0/components/profiler/profiler-guide)— Profiling algorithms, picking modes, gate checks[Planner Guide](https://docs.nvidia.com/dynamo/v1.3.0/components/planner/planner-guide)— Scaling modes, PlannerConfig reference[Model Caching](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/model-loading/model-caching)— PVC setup, ModelExpress, and ModelStreamer[Creating Deployments](https://docs.nvidia.com/dynamo/v1.3.0/additional-resources/creating-deployments)— Manual DGD spec for hand-crafted configs[Multinode Deployments](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/scale/multinode-deployments)— Grove, LWS, and multinode details[Disaggregated Communication](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/operate/disagg-communication)— NIXL, RDMA, and networking