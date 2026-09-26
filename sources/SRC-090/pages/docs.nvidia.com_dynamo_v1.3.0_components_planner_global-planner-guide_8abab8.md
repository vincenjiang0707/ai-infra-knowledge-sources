source: https://docs.nvidia.com/dynamo/v1.3.0/components/planner/global-planner-guide
lastmod: 2026-09-24T19:58:16.636Z

# Global Planner Deployment Guide

Deploys GlobalPlanner as the centralized scaling layer for multi-DGD policy enforcement and single-endpoint multi-pool deployments.

This guide explains how to deploy `GlobalPlanner`

and when to use it. `GlobalPlanner`

is the centralized scaling execution layer for deployments where multiple DGDs should delegate scaling through one component, whether those DGDs expose separate endpoints or sit behind one shared endpoint.


New to Planner?We recommend starting with a single-DGD deployment using either throughput-based or load-based scaling before adopting GlobalPlanner. See the[Planner overview]and[Planner Guide]to get started.

## Why Global Planner?

Without `GlobalPlanner`

, each DGD’s local planner scales only its own deployment directly. That is fine for isolated deployments, but it becomes awkward when you want one place to:

- apply centralized scaling policy across multiple DGDs
- enforce shared constraints such as authorization or total GPU budget
- coordinate scaling for a single-endpoint, multi-pool deployment

`GlobalPlanner`

solves that by becoming the common scale-execution endpoint for multiple local planners.

## Terminology

**Planner**: The`dynamo.planner`

component that computes desired replica counts to maintain latency SLAs. See the[Planner overview](https://docs.nvidia.com/dynamo/v1.3.0/components/planner).**Local Planner**: A pool-local instance of the Planner running inside a single DGD.**Global Planner**: The centralized execution and policy layer that receives scale requests from local planners.**Single-endpoint multi-pool deployment**: One model endpoint backed by multiple DGDs for the same model. This pattern uses both`GlobalRouter`

and`GlobalPlanner`

.

## Deployment Patterns

Use `GlobalPlanner`

in one of these two patterns:

## Pattern 1: Multiple Model Endpoints Or Independent DGDs

Use this pattern when you have multiple DGDs, often for different models, and you want them to share centralized scaling policy without collapsing them into one endpoint.

Typical examples:

- DGD A:
`qwen-0.6b`

disaggregated deployment with its own local planner - DGD B:
`qwen-32b`

disaggregated deployment with its own local planner - one shared
`GlobalPlanner`

that all local planners delegate to

In this pattern:

- each DGD keeps its own normal local planner
- each local planner is configured with
`environment: "global-planner"`

- all those planners point at the same
`global_planner_namespace`

- each DGD keeps its own endpoint or frontend as needed
- you do
**not**need`GlobalRouter`


This is the pattern to use when the goal is centralized scaling control across multiple deployments or models.

## Pattern 2: One Model Endpoint, Multiple DGDs

Use this pattern when all of the following are true:

- You want one public endpoint for a single model.
- You want different private pools for different request classes, such as short ISL vs. long ISL requests, or different latency targets.
- You want each pool to autoscale independently.
- You want routing and scale execution to be centralized instead of exposing multiple endpoints to clients.

Typical examples:

- short-input requests are cheaper on a smaller prefill pool
- long-input requests need a larger prefill pool
- decode capacity should scale independently from prefill capacity

If you only need one pool for one model, use a single Local Planner and DGD/DGDR instead.

## What You Deploy

In the current implementation, the single-endpoint pattern is composed from multiple resources:


Current workflowA single DGDR does

notgenerate the full single-endpoint multi-pool topology today. Instead, run one DGDR or profiling job per intended pool, then compose the final control DGD plus pool DGDs manually.

## Architecture

Read the diagram left to right for request traffic: clients call the control `Frontend`

, `GlobalRouter`

selects a private pool, and each pool’s `LocalRouter`

sends the request to workers. Read the dotted and lower paths for scaling: each pool-local `Planner`

reads that pool’s router metrics, sends a scale request to `GlobalPlanner`

, and `GlobalPlanner`

applies the Kubernetes replica changes centrally.

## Prerequisites

- Dynamo Kubernetes Platform installed. See
[Kubernetes Quickstart](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/kubernetes-quickstart). - Prometheus deployed and scraping router metrics. The global planner examples assume cluster Prometheus is available.
- Backend images available for your chosen framework (
`vllm`

,`sglang`

, or`trtllm`

). - Secrets for model access, such as a Hugging Face token secret.
- A storage strategy for model weights if your workers should share a model cache PVC.

For SLA throughput-based scaling, each pool needs either native AIC support, optional bootstrap profiling data, or enough live FPM observations to warm the fallback model. See [Profiler Guide](https://docs.nvidia.com/dynamo/v1.3.0/components/profiler/profiler-guide).

## Inputs You Need To Decide Up Front

Before writing manifests, decide the following:

## Step 1: Profile Each Intended Pool Independently

Start by deciding what each pool should specialize in. Common examples:

- Prefill pool 0: lower-cost pool for short prompts.
- Prefill pool 1: larger pool for long prompts.
- Decode pool 0: standard decode pool for most requests.

For each intended pool, run a separate DGDR or profiling job with the workload and SLA that represent that pool.

Example DGDR skeleton:

Repeat this once per planned pool, changing the workload and SLA inputs for each request class.

What to keep from each profiling result:

- Worker shape (
`tensor-parallel-size`

, GPUs per worker, memory/caching settings). - Planner profile data directory or generated ConfigMaps.
- Planner settings such as
`prefill_engine_num_gpu`

or`decode_engine_num_gpu`

. - Any backend-specific flags that differ across pools.

See [DGDR Examples](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/deploy-models/dgdr-examples) and [Profiler Guide](https://docs.nvidia.com/dynamo/v1.3.0/components/profiler/profiler-guide) for DGDR details.

## Step 2: Create The Control DGD

Deploy one control DGD that contains:

`Frontend`

: the single public model endpoint.`GlobalRouter`

: chooses which pool receives each request.`GlobalPlanner`

: receives scale requests from pool planners and applies replica changes.

The vLLM example topology is in [examples/global_planner/global-planner-vllm-test.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/examples/global_planner/global-planner-vllm-test.yaml).

The `GlobalPlanner`

section is minimal:

The values passed to `--managed-namespaces`

are the pool planners’ **Dynamo namespaces** (`caller_namespace`

), not raw Kubernetes namespaces. In many examples they share the same string prefix, but they are logically different identifiers.

**Management modes**: When `--managed-namespaces`

is set (explicit mode), only the listed Dynamo namespaces are authorized to send scale requests, and only their corresponding DGDs count toward the GPU budget. DGD names are derived from the Dynamo namespace using the operator convention `DYN_NAMESPACE = {k8s_namespace}-{dgd_name}`

. When omitted (implicit mode), any caller is accepted and all DGDs in the Kubernetes namespace count toward the GPU budget.

If you want the central executor to reject scale requests that exceed a total GPU budget, add `--max-total-gpus`

. See [examples/global_planner/global-planner-gpu-budget.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/examples/global_planner/global-planner-gpu-budget.yaml).

## Step 3: Create One DGD Per Pool

Each private pool gets its own DGD. A pool DGD usually contains:

`LocalRouter`

- one worker type (
`prefill`

or`decode`

) - one
`Planner`


The planner inside each pool must be configured for `global-planner`

mode so it delegates scaling to the control stack:

`global_planner_namespace`

must point to the control stack’s **Dynamo namespace**. In the reference manifests, that is the namespace string passed to the control `Frontend`

and `GlobalRouter`

.

`throughput_metrics_source: "router"`

is required for pool-local Planner in GlobalPlanner deployments. The pool Planner should forecast demand from its own `LocalRouter`

`dynamo_component_router_*`

Prometheus metrics, not from the shared public `Frontend`

. See the [Planner overview](https://docs.nvidia.com/dynamo/v1.3.0/components/planner#prometheus-metrics) for the exact frontend and router metric sources.

Use:

`mode: "prefill"`

for prefill-only pools`mode: "decode"`

for decode-only pools

The worker and planner settings for each pool come from the pool-specific profiling result you created in Step 1.

In the reference vLLM example:

`gp-prefill-0`

uses a 1-GPU TP1 prefill worker`gp-prefill-1`

uses a 2-GPU TP2 prefill worker`gp-decode-0`

uses a 1-GPU TP1 decode worker

See [global-planner-vllm-test.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/examples/global_planner/global-planner-vllm-test.yaml).

## Step 4: Configure GlobalRouter To Select Pools

`GlobalRouter`

reads a JSON config that lists the pool namespaces and a routing grid for each request type.

Example:

The `prefill_pool_dynamo_namespaces`

and `decode_pool_dynamo_namespaces`

entries are **Dynamo namespaces** that the pool-local routers register under.

Important runtime behavior:

- Prefill pool selection uses
**ISL + TTFT target** - Decode pool selection uses
**context length + ITL target** - OSL is useful for
**designing and profiling pools**, but it is**not a direct routing key**in the current`GlobalRouter`

- Optional priority retry is enabled with
`enable_priority_retry`

; lower values in`*_pool_priorities`

are faster pools, and omitted priority lists default to pool order (`0`

,`1`

, …)

Clients can pass request targets through `extra_args`

:

For more details, see [Global Router README](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/components/src/dynamo/global_router/README.md).

## Step 5: Deploy In Order

For a fresh cluster, the usual order is:

- Install Dynamo platform and Prometheus.
- Create secrets and PVCs needed by workers.
- Create the
`GlobalRouter`

ConfigMap. - Apply the control DGD.
- Apply the pool DGDs.
- Wait for all DGDs to reach ready state.
- Expose or port-forward the control
`Frontend`

.

Example:

The single user-facing endpoint is the `Frontend`

in the control DGD, not the pool DGDs.

## Step 6: Validate The Stack

Validate the deployment from outside in:

- Confirm the control
`Frontend`

is healthy and serving the model endpoint. - Confirm
`GlobalRouter`

logs show requests being assigned to the expected pool namespaces. - Confirm pool-local planners are producing scale requests.
- Confirm
`GlobalPlanner`

logs show accepted scale operations. - Confirm the target DGDs’ replica counts change as expected.

If you use Prometheus and Grafana, also inspect:

- TTFT and ITL over time
- per-pool worker counts
- per-pool request mix
- total GPU usage

## Recommended Workflow For New Deployments

For most teams, the easiest way to build this deployment is:

- Design your pool classes from expected traffic patterns.
- Run one DGDR per pool class to generate or validate the pool configuration.
- Copy the selected worker shape and planner settings into the final pool DGDs.
- Build one control DGD with
`Frontend`

,`GlobalRouter`

, and`GlobalPlanner`

. - Route all client traffic through the control
`Frontend`

.

This keeps profiling and pool selection simple while still giving you one public endpoint for the model.

## Current Limitations

- Single-endpoint
`GlobalPlanner`

deployments are assembled manually today. One DGDR does not emit the full control DGD plus pool DGDs topology. `GlobalRouter`

routes by ISL/TTFT and context-length/ITL grids, not directly by OSL.- In the single-endpoint pattern, all pools are expected to serve the same model.

## See Also

[Planner README](https://docs.nvidia.com/dynamo/v1.3.0/components/planner)— Planner overview and quick start[Planner Guide](https://docs.nvidia.com/dynamo/v1.3.0/components/planner/planner-guide)— Planner configuration reference[DGDR Examples](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/deploy-models/dgdr-examples)— DGDR examples for generating per-pool configs[Profiler Guide](https://docs.nvidia.com/dynamo/v1.3.0/components/profiler/profiler-guide)— Pre-deployment profiling workflow[Global Planner README](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/components/src/dynamo/global_planner/README.md)— Centralized scale execution[Global Router README](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/components/src/dynamo/global_router/README.md)— Cross-pool request routing[vLLM global planner example](https://github.com/ai-dynamo/dynamo/blob/v1.3.0/examples/global_planner/global-planner-vllm-test.yaml)— End-to-end reference manifest