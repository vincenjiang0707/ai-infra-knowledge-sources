source: https://docs.nvidia.com/dynamo/zh-CN/v1.1.0/kubernetes-deployment/deployment-guide/deploying-your-first-model
lastmod: 2026-09-23T23:30:39.914Z

# Deploying Your First Model

End-to-end tutorial for deploying `Qwen/Qwen3-0.6B`

on Kubernetes using Dynamo’s recommended
`DynamoGraphDeploymentRequest`

(DGDR) workflow — from zero to your first inference response.

This guide assumes you have already completed the
[platform installation](https://docs.nvidia.com/dynamo/v1.1.0/kubernetes-deployment/deployment-guide/detailed-installation-guide) and that the Dynamo operator and CRDs are
running in your cluster.

## What is a DynamoGraphDeploymentRequest?

A `DynamoGraphDeploymentRequest`

(DGDR) is Dynamo’s **deploy-by-intent** API. You describe what
you want to run and your performance targets; Dynamo’s profiler determines the optimal
configuration automatically, then creates the live deployment for you.

For a deeper comparison, see [Understanding Dynamo’s Custom Resources](https://docs.nvidia.com/dynamo/v1.1.0/getting-started/kubernetes-deployment#understanding-dynamos-custom-resources).

## Prerequisites

Before starting, confirm:

- Platform installed:
`kubectl get pods -n ${NAMESPACE}`

shows operator pods`Running`

- CRDs present:
`kubectl get crd | grep dynamo`

shows`dynamographdeploymentrequests.nvidia.com`

`kubectl`

and`helm`

available in your shell

Set these variables once — they are referenced throughout the guide:

`Qwen/Qwen3-0.6B`

is a public model. A HuggingFace token is not strictly required to download
it, but is recommended to avoid rate limiting.

## Step 1: Configure Namespace and Secrets

Verify the secret was created:

## Step 2: Create the DynamoGraphDeploymentRequest

Save the following as `qwen3-first-model.yaml`

:

Apply it (uses `envsubst`

to substitute the `RELEASE_VERSION`

shell variable into the YAML):

### Field reference

For the full spec reference, see the [DGDR API Reference](https://docs.nvidia.com/dynamo/v1.1.0/additional-resources/api-reference-k-8-s) and
[Profiler Guide](https://docs.nvidia.com/dynamo/v1.1.0/components/profiler/profiler-guide).

If you are using a **namespace-scoped operator** (deprecated) with GPU discovery disabled, you must also
provide explicit hardware info or the DGDR will be rejected at admission:

See the [installation guide](https://docs.nvidia.com/dynamo/v1.1.0/kubernetes-deployment/deployment-guide/detailed-installation-guide#gpu-discovery-for-dynamographdeploymentrequests-deprecated-namespace-scoped-mode)
for details.

**Note:** Namespace-scoped mode is deprecated. Use cluster-wide mode for new deployments.

## Step 3: Monitor Profiling Progress

Profiling is the automated step where Dynamo sweeps across candidate configurations (parallelism, batching, scheduling strategies) to find the one that best meets your SLA and hardware — so you don’t have to tune it manually.

Watch the DGDR status in real time:

The `PHASE`

column progresses through:

`Deployed`

is the success terminal state when `autoApply: true`

(the default).
If you set `autoApply: false`

, the phase stops at `Ready`

— profiling is complete and the
generated DGD spec is stored in `.status`

, but no deployment is created automatically.
To inspect and deploy it manually:

For a full status summary and events:

To follow the profiling job logs:

`searchStrategy: rapid`

, profiling typically completes in under 15 minutes on a single GPU.## Step 4: Verify the Deployment

Once the DGDR reaches `Deployed`

, the `DynamoGraphDeployment`

has been created automatically.
Check that everything is running:

Wait until pods are ready:

Find the frontend service name:

## Step 5: Send Your First Request

Port-forward to the frontend and send an inference request:

A successful response looks like:

Your first model is now live.

## Cleanup

To remove the deployment and profiling artifacts:

Deleting a DGDR does **not** delete the `DynamoGraphDeployment`

it created. The DGD persists
independently so it can continue serving traffic.

## Troubleshooting

**DGDR stuck in Pending**

Common causes: no available GPU nodes, image pull failure (check image tag; NGC credentials are
optional but may be needed if you hit rate limits pulling from public NGC), missing `hardware`

config for a namespace-scoped operator (deprecated).

**GPU node taints** are a frequent cause of pods staying `Pending`

. Many clusters (including
GKE by default and most shared/HPC environments) taint GPU nodes with
`nvidia.com/gpu:NoSchedule`

so that only GPU-aware workloads land on them. If the profiling
job pod is stuck with a `0/N nodes are available: … node(s) had untolerated taint`

event,
add a toleration to your DGDR via `overrides.profilingJob`

. The operator and profiler
automatically forward it to every candidate and deployed pod:

**Profiling job fails**

**Pods not starting after profiling**

**Model not responding after port-forward**

## Next Steps

**Tune for production SLAs**: Add`sla`

(TTFT, ITL) and`workload`

(ISL, OSL) targets to your DGDR so the profiler optimizes for your specific traffic. See the[Profiler Guide](https://docs.nvidia.com/dynamo/v1.1.0/components/profiler/profiler-guide)for the full configuration reference and picking modes. For ready-to-use YAML — including SLA targets, private models, MoE, and overrides — see[DGDR Examples](https://docs.nvidia.com/dynamo/v1.1.0/components/profiler/profiler-examples).**Scale the deployment**:[Autoscaling guide](https://docs.nvidia.com/dynamo/v1.1.0/kubernetes-deployment/deployment-guide/autoscaling)**SLA-aware autoscaling**: Enable the Planner via`features.planner`

in the DGDR — see the[Planner Guide](https://docs.nvidia.com/dynamo/v1.1.0/components/planner/planner-guide).**Inspect the generated config**: Set`autoApply: false`

and extract the DGD spec with`kubectl get dgdr <name> -o jsonpath='{.status.profilingResults.selectedConfig}'`

before deploying.**Direct control**:[Creating Deployments](https://docs.nvidia.com/dynamo/v1.1.0/additional-resources/creating-deployments)— write your own`DynamoGraphDeployment`

spec for full customization.**Monitor performance**:[Observability](https://docs.nvidia.com/dynamo/v1.1.0/kubernetes-deployment/observability-k-8-s/metrics)**Try specific backends**:[vLLM](https://docs.nvidia.com/dynamo/v1.1.0/backends/v-llm),[SGLang](https://docs.nvidia.com/dynamo/v1.1.0/backends/sg-lang),[TensorRT-LLM](https://docs.nvidia.com/dynamo/v1.1.0/backends/tensor-rt-llm)