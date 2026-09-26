source: https://docs.nvidia.com/dynamo/zh-CN/kubernetes/auto-deployment/dgdr-walkthrough
lastmod: 2026-09-24T19:58:16.636Z

# Auto Deploy with DGDR

Deploy a model by intent — describe the model, workload, and SLA targets, and let Dynamo profile your hardware and generate the DynamoGraphDeployment for you.

A **DynamoGraphDeploymentRequest (DGDR)** is Dynamo’s deploy-by-intent path. Instead of hand-authoring a [DynamoGraphDeployment (DGD)](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/deploy-with-dgd) with explicit parallelism, replica counts, and resource limits, you describe *what* you want to run — model, backend, workload, and optional latency targets — and Dynamo’s profiler analyzes your cluster’s GPUs, selects a configuration, and generates the DGD that serves traffic.

This guide walks through authoring that request, starting from the smallest possible DGDR and layering on workload targets, search strategy, hardware sizing, model caching, runtime autoscaling, and review-before-deploy as you need them. Each step builds on the previous one. For the component relationships and guidance on choosing DGDR, see the [Auto Deployment overview](https://docs.nvidia.com/dynamo/kubernetes/auto-deployment/overview). For the full field table and lifecycle reference, see the [DGDR Reference](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment-request); for ready-to-copy manifests, see [DGDR Templates](https://docs.nvidia.com/dynamo/recipes/kubernetes-templates/dgdr).

In a release installation, when you omit `spec.image`

, the DGDR webhook selects
`nvcr.io/nvidia/ai-dynamo/dynamo-planner:<operator-version>`

. For a local
operator build without a known version, set `spec.image`

explicitly. Use the
`dynamo-planner`

image from the same release as the operator. For Dynamo
releases earlier than 1.1.0, use the matching `dynamo-frontend`

image. The
generated Planner and backend images retain that registry and tag.

## Prerequisites

Before authoring a DGDR, make sure you have:

- A Kubernetes cluster with the
**Dynamo Platform installed**, including the operator and profiler. See the[Installation Guide](https://docs.nvidia.com/dynamo/kubernetes/installation/install-dynamo). `kubectl`

access to that cluster and a target namespace.- GPU nodes the operator can discover (via DCGM or node labels). The operator auto-detects SKU, VRAM, and GPU count; you can override any of these (see
[Step 4](https://docs.nvidia.com/dynamo/kubernetes/auto-deployment/dgdr-walkthrough#set-hardware-and-handle-large-or-multinode-models)). - A
**HuggingFace token secret**named`hf-token-secret`

in the namespace for gated or rate-limited models — both the profiling job and the deployed pods use it. - New to Dynamo on Kubernetes? Run one model end to end with the
[Kubernetes Quickstart](https://docs.nvidia.com/dynamo/kubernetes/getting-started/quickstart)first.

For SLA-driven autoscaling, also install [Prometheus](https://docs.nvidia.com/dynamo/kubernetes/installation/install-dynamo#kube-prometheus-stack) before creating the DGDR (see [Step 6](https://docs.nvidia.com/dynamo/kubernetes/auto-deployment/dgdr-walkthrough#enable-the-planner-for-runtime-autoscaling)).

## How a DGDR is structured

A DGDR is a small intent document. The only required field is `model`

; everything else has a default or is auto-detected. The profiler fills in the parts you leave out.

The steps below fill in these fields for progressively more demanding deployments. For the complete field reference and defaults, see the [DGDR Reference — Field Reference](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment-request#spec-reference).

### Submit a minimal DGDR

Start with the smallest request: a model. With `searchStrategy`

and `autoApply`

at their defaults, the profiler uses rapid simulation (~30 seconds, no GPUs consumed during profiling) and the operator deploys the result. In a release installation, the webhook selects the matching versioned Planner image.

Apply it and watch the request progress through its phases:

The DGDR moves through `Pending`

→ `Profiling`

→ `Ready`

→ `Deploying`

→ `Deployed`

. Once it reaches `Deployed`

, the generated DGD is running. See [Monitor profiling and deployment](https://docs.nvidia.com/dynamo/kubernetes/auto-deployment/dgdr-walkthrough#monitor-profiling-and-deployment) for the full phase list and log commands.

The generated DGD does **not** get an owner reference back to the DGDR. Deleting the DGDR leaves the DGD serving traffic. To tear everything down, delete both (see [Clean up](https://docs.nvidia.com/dynamo/kubernetes/auto-deployment/dgdr-walkthrough#clean-up)).

### Describe your workload and SLA targets

The profiler sizes the deployment against the traffic you expect and the latency you need. Provide a `workload`

shape, and optionally `sla`

targets, so the profiler optimizes for your case instead of the defaults.

SLA targets shape which configuration the profiler selects. They are also what the [Planner](https://docs.nvidia.com/dynamo/kubernetes/auto-deployment/dgdr-walkthrough#enable-the-planner-for-runtime-autoscaling) drives toward at runtime. Set realistic targets — unreachable values push the profiler to its most expensive layout.

### Choose a search strategy

The `searchStrategy`

field controls how the profiler explores configurations. The choice trades profiling time against how close to optimal you land.

**Rapid (default)** uses AIC-backed DynoSim-style performance modeling to search configurations without running real inference. Completes in ~30 seconds with no GPUs consumed during profiling.

Use rapid when getting started, iterating quickly, or running in CI/CD — provided your GPU SKU is in the [Profiler support matrix](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/profiler/profiler-guide#support-matrix). If AIC does not support your model/hardware/backend combination, the profiler falls back to a naive memory-fit config that may not be optimal.

**Thorough** enumerates candidate parallelization configs, deploys each on real GPUs, and benchmarks them with AIPerf. Takes 2–4 hours and produces measured rather than simulated data.

Use thorough when tuning for production, when your hardware is not supported by AIC (for example PCIe GPUs), or when you need measured performance. It has constraints:

**Disaggregated mode only**— thorough does not run aggregated configurations.— specify`backend: auto`

is rejected`vllm`

,`sglang`

, or`trtllm`

.**Requires GPU resources**— the profiler deploys real inference engines during profiling.

For the profiling algorithms, gate checks, and how to pick a mode, see the [Profiler Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/profiler/profiler-guide).

### Set hardware and handle large or multinode models

The operator auto-detects GPU SKU, VRAM, and count (capped at 32). Override any of these under `hardware`

when auto-detection is wrong or you want the profiler to consider more GPUs.

GPU SKUs use **lowercase underscore format** (`h100_sxm`

, not `H100-SXM5-80GB`

). For the full list of accepted values and the PCIe-support caveat, see the [DGDR Reference — SKU Format](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment-request#sku-format).

**Large and MoE models that span nodes.** When a model needs more GPUs than one node provides, the deployment is multinode and requires a gang scheduler. Install an orchestrator first — the operator returns a hard error otherwise:

[Multinode Orchestration](https://docs.nvidia.com/dynamo/kubernetes/installation/multinode-orchestration)— install-time prerequisites (Grove + KAI, or LWS + Volcano).[Grove](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/multinode/grove)(default) and[LWS](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/multinode/lws)— the two orchestration backends.

For **Mixture-of-Experts (MoE)** models (DeepSeek-R1, Qwen3-MoE), use **SGLang** for full support — vLLM and TensorRT-LLM have partial MoE support still under development. The profiler sweeps MoE models across up to **4 nodes**; beyond that, it selects the best config within range and you may need to adjust replica counts manually. See the [Profiler support matrix](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/profiler/profiler-guide#support-matrix).

DGDR does not expose `multinode.nodeCount`

. `hardware.totalGpus`

sets the
overall profiling and deployment budget, while `hardware.numGpusPerNode`

describes per-node capacity. After selecting each worker’s parallelism, the
profiler sets the generated DGD’s `multinode.nodeCount`

to the per-instance GPU
count divided by `numGpusPerNode`

, rounded up. It omits multinode configuration
when the worker fits on one node.

### Cache model weights

By default the profiling job and every generated worker pod download the model from HuggingFace. For large models (>70B) this is slow, and many replicas hit HuggingFace rate limits. Point `modelCache`

at a pre-populated `ReadWriteMany`

PVC so weights load from shared storage instead.

The operator mounts the PVC read-only into the profiling job and passes it through to the generated DGD, so both profiling and serving use the cached weights.

`pvcModelPath`

must be the HuggingFace snapshot path inside the PVC: `hub/models--<org>--<model>/snapshots/<commit-hash>`

. Substitute `/`

with `--`

in the model ID, and replace `<commit-hash>`

with the actual snapshot revision. See [Model Caching — Find the Snapshot Path](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/model-loading/model-caching#find-the-snapshot-path) for how to look it up.

**Setup:** create a `ReadWriteMany`

PVC ([Installation Guide — Shared Storage](https://docs.nvidia.com/dynamo/kubernetes/installation/install-dynamo#shared-storage-for-model-caching)), run a one-time download Job to populate it, then reference it here. See [Model Caching](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/model-loading/model-caching) for the full walkthrough.

For gated models, create the token secret the profiler and pods read automatically:

### Enable the Planner for runtime autoscaling

The **Planner** provides runtime autoscaling for disaggregated deployments: it adjusts prefill and decode replica counts to meet your SLA targets as traffic fluctuates. Enable it by setting `features.planner`

to a PlannerConfig; DGDR passes the object through to the Planner service and generates Planner support in the final DGD.

To evaluate Planner recommendations without applying scaling changes, add `advisory: true`

to the same object.

The Planner’s `sla`

optimization target reads live TTFT/ITL from Prometheus, so install [Prometheus](https://docs.nvidia.com/dynamo/kubernetes/installation/install-dynamo#kube-prometheus-stack) before creating the DGDR if you want SLA-driven scaling. The `throughput`

and `latency`

modes use internal queue-depth signals and work without Prometheus. For scaling modes and the full PlannerConfig field reference, see the [Planner Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/planner/planner-guide).

`features.planner`

is the PlannerConfig object itself; it does not use an
`enabled`

wrapper. The DGDR API passes the object through without field-level
validation. The profiler copies it, adds GPU counts from the selected
configuration, and propagates explicit DGDR latency targets unless
`features.planner.ttft_ms`

or `features.planner.itl_ms`

overrides them. It then
writes the reconciled object to `planner_config.json`

in a ConfigMap, mounts the
file into the generated Planner service, and starts the service with `--config`

.
For non-advisory operation, it also enables scaling adapters on the worker
services selected by `mode`

.

### Review the generated DGD

For production, inspect the generated DGD before it deploys. Set `autoApply: false`

so the DGDR stops at `Ready`

and stores the config instead of deploying it.

After profiling completes, extract, review, and apply the DGD yourself:

While `autoApply`

is disabled, you may set or change
`runtimeVersionOverride`

during `Profiling`

or `Ready`

. To have the operator
deploy the reviewed snapshot, enable `autoApply`

:

You may also set or change the override in the update that enables
`autoApply`

. The operator applies the current value to the new DGD without
changing the stored snapshot.

## Monitor profiling and deployment

A DGDR progresses through these phases. Profiling failures are terminal — they are not retried (`backoffLimit: 0`

).

Watch progress and read profiling logs:

For the full lifecycle, conditions, and monitoring command reference, see [DGDR Reference — Lifecycle](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment-request#lifecycle).

## Troubleshoot

### Profiling Job Fails to Schedule

GPU nodes commonly use taints. Add the required tolerations to the generated profiling Job through
`overrides.profilingJob`

:

The empty `containers`

list is a required placeholder. The operator merges the override into the
container configuration it generates for the profiling Job.

## Clean up

Deleting the DGDR does **not** delete the DGD it created — the DGD persists so it can keep serving. To remove both:

By default, the generated DGD is named `<dgdr-name>-dgd`

. An explicit
`spec.overrides.dgd.metadata.name`

replaces that default. To look up the DGD, run
`kubectl get dgd -n <namespace> -l dgdr.nvidia.com/name=my-model`

. The selected
name is also recorded in `.status.dgdName`

.

## Optional: Customize the generated DGD

Use `spec.overrides.dgd`

when the generated DGD needs a field that DGDR does not expose directly.
Provide a partial `nvidia.com/v1beta1`

DGD. DGDR merges matching components, containers, and
environment variables by `name`

after profiling selects a configuration.

For example, enable KV-aware routing on the generated `Frontend`

component:

Inspect `.status.profilingResults.selectedConfig`

with `autoApply: false`

to find the generated
component names. An override can modify only components already present in that generated DGD; it
cannot add a new worker, EPP, or other topology component.

Older overrides used the `nvidia.com/v1alpha1`

DGD shape. They remain supported for compatibility,
but their merge behavior differs: `spec.services`

entries merge by service name, and worker
`extraPodSpec.mainContainer.args`

values append to the generated arguments. In `v1beta1`

, map lists
such as components, containers, and environment variables merge by `name`

, while atomic lists such
as graph-level `spec.env`

and container `args`

replace the generated list. Use `v1beta1`

for new
overrides and include the complete desired argument list when overriding `args`

.

For the complete merge, metadata, and validation rules, see
[DGDR Reference — Generated DGD overrides](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment-request#generated-dgd-overrides).