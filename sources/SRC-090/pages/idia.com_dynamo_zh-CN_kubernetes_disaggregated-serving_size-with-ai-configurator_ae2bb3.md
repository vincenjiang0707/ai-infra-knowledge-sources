source: https://docs.nvidia.com/dynamo/zh-CN/kubernetes/disaggregated-serving/size-with-ai-configurator
lastmod: 2026-09-24T19:58:16.636Z

# Size a Kubernetes Deployment with AIConfigurator

Generate a tensor- and pipeline-parallel layout for your DGD worker from a latency target

This page is a detour from the **Determine topology and parallelism** step of [Deploy with DGD](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/deploy-with-dgd). Rather than hand-pick tensor- and pipeline-parallel sizes, run AIConfigurator to search layouts against a latency target, then copy the recommended parallelism into your worker. It covers parallelism sizing only. For the full workflow — aggregated versus disaggregated comparison, generating complete manifests, and validating with AIPerf — see the [AIConfigurator](https://docs.nvidia.com/dynamo/additional-resources/ai-configurator-reference) reference.

AIConfigurator itself is not Kubernetes-specific. You can run the same optimizer for a local or
bare-metal Dynamo deployment and translate the recommended TP, PP, and replica counts into worker
commands. This tutorial is Kubernetes-specific only because its final step applies the result to a
DGD. For that workflow, see [Sizing a Local Deployment with AIConfigurator](https://docs.nvidia.com/dynamo/cli/disaggregated-serving/sizing-with-ai-configurator).

AIConfigurator uses analytical and profiled performance models to estimate candidate configurations. It is sometimes described as performance simulation, but it does not run the request-by-request Dynamo scheduler, router, or KV-cache lifecycle. Mocker provides the simulated engine behavior, and DynoSim supplies the replay and sweep harness; DynoSim can use AIConfigurator estimates as its forward-pass timing model.

## Prerequisites

- A DGD in progress from
[Deploy with DGD](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/deploy-with-dgd), with the Frontend and worker defined and only parallelism left to set. - AIConfigurator installed:
`pip3 install aiconfigurator`

. - Your checkpoint’s HuggingFace ID, GPU system (for example
`h200_sxm`

), backend (`vllm`

,`sglang`

, or`trtllm`

), the total GPUs you can allocate, and your SLA: Time To First Token (TTFT), Time Per Output Token (TPOT), and typical input/output sequence lengths (ISL/OSL).

AIConfigurator only models supported checkpoint + system + backend combinations. Confirm yours before sizing with `aiconfigurator cli support --model-path <model> --system <sku> --backend <backend>`

. See the [support matrix](https://ai-dynamo.github.io/aiconfigurator/support-matrix/).

### Generate a configuration

Run `aiconfigurator cli default`

with your GPU budget, system, backend, and SLA:

`--total-gpus`

— GPUs available for the deployment; the search stays within this budget.`--system`

— GPU SKU (`h200_sxm`

,`h100_sxm`

,`a100_sxm`

).`--backend`

/`--backend-version`

— inference engine and version.`--isl`

/`--osl`

— input and output sequence lengths, in tokens.`--ttft`

/`--tpot`

— latency targets, in milliseconds; candidates that miss them are filtered out.

### Understand the GPU and node model

`--total-gpus`

is a budget, not a flat list with no topology. The selected `--system`

definition
includes GPUs per node, intra-node bandwidth, inter-node bandwidth, PCIe bandwidth, and communication
latency. AIConfigurator uses that system model when evaluating parallel configurations and can
produce workers that span multiple nodes.

AIConfigurator does not inspect your live cluster. It assumes a homogeneous pool described by the system definition and GPU budget; it does not account for current node availability, GPU fragmentation, scheduler placement, or cluster-specific network differences.

The manual DGD example below assumes `gpus/worker`

does not exceed the system’s GPUs per node. If a
recommended worker spans nodes, use the generated multi-node artifacts from the full
[AIConfigurator workflow](https://docs.nvidia.com/dynamo/additional-resources/ai-configurator-reference) and make sure the
cluster supports the required LeaderWorkerSet deployment.

### Read the recommended parallelism

AIConfigurator ranks the layouts that meet your SLA. The `parallel`

column is the layout to copy, and `gpus/worker`

is the GPUs it needs (abridged):

Read the top-ranked row:

—`parallel`

`tp4pp1`

means tensor-parallel 4, pipeline-parallel 1.— GPUs one worker needs; equals TP × PP.`gpus/worker`

— how many copies of the worker to run.`replicas`


### Apply it to your worker

Copy those three numbers into the worker you built in the DGD guide:

Disaggregating? The `disagg`

table sizes prefill and decode separately, as `(p)parallel`

/ `(p)gpus/worker`

and `(d)parallel`

/ `(d)gpus/worker`

. Apply each to the matching prefill and decode worker from the DGD guide’s disaggregated step.

## Next steps

- Return to
[Deploy with DGD](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/deploy-with-dgd)to apply the deployment and send a request. - For aggregated versus disaggregated comparison, generating complete Kubernetes manifests with
`--deployment-target dynamo-j2`

, and validating predictions with AIPerf, see the[AIConfigurator](https://docs.nvidia.com/dynamo/additional-resources/ai-configurator-reference)reference.