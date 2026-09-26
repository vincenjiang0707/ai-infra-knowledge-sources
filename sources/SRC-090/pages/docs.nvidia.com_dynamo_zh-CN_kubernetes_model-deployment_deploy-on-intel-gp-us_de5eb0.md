source: https://docs.nvidia.com/dynamo/zh-CN/kubernetes/model-deployment/deploy-on-intel-gp-us
lastmod: 2026-09-24T19:58:16.636Z

# Deploy on Intel GPUs with DRA

This tutorial adapts the aggregated vLLM deployment from [Deploy with DGD](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/deploy-with-dgd) to run on
Intel GPUs. It focuses only on what changes for Intel XPU: cluster device support, the runtime image,
and GPU allocation with Kubernetes Dynamic Resource Allocation (DRA).

The result is a two-document manifest:

- A
`ResourceClaimTemplate`

that requests an Intel GPU from the`gpu.intel.com`

`DeviceClass`

. - A
`DynamoGraphDeployment`

(DGD) whose vLLM worker consumes that claim.

This tutorial follows the checked-in vLLM XPU DRA manifests. Dynamo also supports running SGLang on Intel XPU locally, but this tutorial stays with the Kubernetes path represented by the repository’s XPU deployment examples.

## Before you begin

Complete the base [Deploy with DGD](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/deploy-with-dgd) tutorial first, or be familiar with its Frontend,
worker, image, Secret, and `podTemplate`

structure. You also need:

- A Kubernetes 1.34 or later cluster with Intel GPU nodes and the
`resource.k8s.io/v1`

DRA API. - The
[Intel resource drivers for Kubernetes](https://github.com/intel/intel-resource-drivers-for-kubernetes)installed with a`DeviceClass`

named`gpu.intel.com`

. - The Dynamo Platform installed in the cluster.
- Docker, access to a container registry, and a local Dynamo checkout.

The Dynamo Platform Helm chart does not install the Intel GPU node driver or the Intel resource
driver. Install the Intel device support before deploying the DGD. The Dynamo operator detects the
`resource.k8s.io/v1`

API automatically; you do not need a Dynamo Helm flag to enable DRA.

### Verify Intel GPU allocation support

Confirm that the cluster serves the DRA v1 API and that the Intel resource driver publishes the
expected `DeviceClass`

and device inventory:

Do not continue until `gpu.intel.com`

exists and at least one `ResourceSlice`

describes the Intel GPU
nodes. Installing Dynamo alone does not create either resource.

### Build the vLLM XPU runtime image

Dynamo does not publish a prebuilt Intel XPU runtime image. From the root of your Dynamo checkout, render the vLLM XPU Dockerfile, build it, and push it to a registry your cluster can pull from:

Use the same Dynamo source revision for the XPU worker image and the Frontend image. Export the Frontend image and deployment namespace for the manifest:

If the registry is private, create its image-pull Secret in `${NAMESPACE}`

. The operator can discover
matching registry credentials in the namespace, as described in [Deploy with DGD](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/deploy-with-dgd#choose-your-backend).

### Create the model access Secret

This tutorial serves the public `Qwen/Qwen3-0.6B`

model. The example worker still imports a Secret
named `hf-token-secret`

, so create it with an empty token. Replace the value for a gated or private
model:

### Request an Intel GPU with DRA

Start `qwen3-xpu.yaml`

with a `ResourceClaimTemplate`

. The request selects one device from the
`gpu.intel.com`

class:

The `ResourceClaimTemplate`

is a Kubernetes resource alongside the DGD, not a DGD field. A worker pod
that references it receives its own generated `ResourceClaim`

.

### Attach the claim to the XPU worker

Add the DGD as the second YAML document. The Frontend does not need a GPU and uses the regular Dynamo vLLM runtime image. The worker uses the XPU image and connects the claim at two levels:

`podTemplate.spec.resourceClaims`

attaches a claim generated from`qwen3-xpu-gpu`

to the pod.`containers[].resources.claims`

grants the`main`

container access to that claim.

The XPU worker also sets `VLLM_TARGET_DEVICE=xpu`

. The `--block-size 64`

argument matches the
checked-in Intel XPU deployment examples.

Your complete `qwen3-xpu.yaml`

now contains the `ResourceClaimTemplate`

, the `---`

separator, and the
DGD.

### Apply the manifest

Expand the image variables, validate both resources with the API server, and apply them:

The namespace passed to `kubectl`

applies to both namespaced resources in the multi-document file.

### Verify the DRA claim and deployment

Confirm that Kubernetes created and allocated the worker’s claim:

Then wait for the DGD:

If the worker remains pending, inspect the pod and claim:

A missing `gpu.intel.com`

class, no matching devices, or an unallocated claim indicates a cluster
DRA/resource-driver problem rather than a DGD reconciliation problem.

## Extend the deployment

Once the aggregated deployment works, you can apply the same Intel-specific changes to other vLLM DGD patterns:

- Give each GPU worker a DRA claim.
- Keep
`VLLM_TARGET_DEVICE=xpu`

on every vLLM worker. - For disaggregated serving, set
`kv_buffer_device`

to`xpu`

in the vLLM NIXL connector configuration.

See [Disaggregated Serving](https://docs.nvidia.com/dynamo/kubernetes/disaggregated-serving/overview) for the DGD topology and
[Disaggregated Communication](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/disagg-communication) for the network requirements. Validate
an aggregated deployment first so device allocation and the XPU runtime are known to work before you
add KV transfer.