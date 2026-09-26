source: https://docs.nvidia.com/dynamo/zh-CN/recipes/kubernetes-templates/dgdr
lastmod: 2026-09-24T19:58:16.636Z

# DGDR Templates

Ready-to-apply DynamoGraphDeploymentRequest manifests for profiling and generating DynamoGraphDeployments.

A `DynamoGraphDeploymentRequest`

(DGDR) describes a model, workload, hardware, and optional latency
targets. Dynamo profiles that intent and generates the `DynamoGraphDeployment`

(DGD) that serves
traffic. Use these templates when you want Dynamo to choose a deployment configuration instead of
writing the complete DGD yourself.

Each manifest is embedded from
[ examples/deployments/dgdr/](https://github.com/ai-dynamo/dynamo/tree/main/examples/deployments/dgdr).
Open an example, use the copy button, and adjust its model, backend, hardware, and namespace before
applying it.

## Prerequisites

- Install the Dynamo Kubernetes platform and operator.
- Create
`hf-token-secret`

in the target namespace when the model requires authentication. - For namespace-restricted operator installations, set
`hardware.gpuSku`

,`hardware.vramMb`

, and`hardware.numGpusPerNode`

explicitly.

Release installations select the matching profiler image when `spec.image`

is omitted. For a local
operator build without a known release version, set `spec.image`

to a compatible `dynamo-planner`

image.

Apply a template with:

## Generate a DGD

###### rapid.yaml · Fast generation with AIConfigurator estimates


Uses simulated performance estimates to generate a DGD without benchmarking candidate engines on real GPUs.

###### thorough.yaml · Measure candidate configurations on GPUs


Deploys and benchmarks candidate configurations before selecting and generating the DGD.

###### planner.yaml · Generate a deployment with SLA-driven autoscaling


Adds a Planner configuration so the generated disaggregated deployment can adjust prefill and decode replicas at runtime.

###### moe-sglang.yaml · Profile a multinode MoE deployment


Uses SGLang and a 32-GPU budget for a large Mixture-of-Experts model. Adapt its hardware, scheduling, model-cache, and SLA settings before applying it.

## Review and Customize the Generated DGD

###### review-before-deploy.yaml · Inspect the generated DGD first


Sets `autoApply: false`

so the request stops after generation instead of creating the DGD.

###### generated-dgd-override.yaml · Add KV-aware routing


Merges an environment-variable override into the generated frontend component. Overrides can modify generated components but cannot add a new topology component.

## Test and Inspect Profiling

###### mocker.yaml · Generate a simulated deployment


Replaces model-serving workers with mock workers for testing routing, profiling, and Planner behavior without serving the model on GPUs.

###### profiling-artifacts.yaml · Persist detailed profiler output


Replaces the profiling output volume with the existing `dynamo-pvc`

claim so plots, logs,
configurations, and raw profiling data remain available after the Job completes.

## Inspect the Result

Watch the request until it reaches `Deployed`

or `Ready`

:

For a request with `autoApply: false`

, extract the generated DGD:

See [Auto Deploy with DGDR](https://docs.nvidia.com/dynamo/dev/kubernetes/auto-deployment/dgdr-walkthrough) for the task-oriented workflow and the
[DGDR Reference](https://docs.nvidia.com/dynamo/dev/reference/api/kubernetes/dynamo-graph-deployment-request) for field definitions, lifecycle phases, and
validation behavior.