source: https://docs.nvidia.com/dynamo/zh-CN/kubernetes/getting-started/quickstart
lastmod: 2026-09-24T19:58:16.636Z

# Kubernetes Quickstart

Select **NVIDIA GPU** or **Intel GPU** based on the accelerator hardware in your cluster, and
follow that tab throughout the guide. The Intel GPU path uses the XPU runtime and tooling.

### Choose your Kubernetes build

Unavailable combinations remain visible to show the current support boundary.

export DYNAMO_VERSION=1.5.0 export DYNAMO_IMAGE="nvcr.io/nvidia/ai-dynamo/dynamo-planner:${DYNAMO_VERSION}"

### Check the prerequisites

###### NVIDIA GPU

###### Intel GPU

You need:

- A Kubernetes v1.30 or later cluster with NVIDIA GPU nodes
`kubectl`

v1.30 or later configured for the cluster- Helm v3 or later

### Install accelerator support

###### NVIDIA GPU

###### Intel GPU

Install the NVIDIA GPU Operator:

If your cluster provider installs the NVIDIA driver, add `--set driver.enabled=false`

.
Add `--set toolkit.enabled=false`

only when the provider also configures the GPU container runtime.

### Install Dynamo

Use the `DYNAMO_VERSION`

value from the selector above to install the Dynamo platform chart in a dedicated namespace. Helm creates the namespace for you:

For the NVIDIA GPU DGDR path, `DYNAMO_IMAGE`

points to the Dynamo planner image from the selector above. The planner profiles the model and creates the worker deployment; you do not need to choose a separate runtime image for that path.

### Create the model access secret

`Qwen/Qwen3-0.6B`

is public and does not require a Hugging Face token. The DGDR profiler and
example DGD expect a Secret named `hf-token-secret`

, so create it with an empty token:

For a gated or private model, replace the empty value with your Hugging Face token.

## What You Did

- Installed the accelerator support required by your hardware.
- Installed the Dynamo platform on your Kubernetes cluster.
- Created either a DGDR that generated a DGD, or a DGD directly.
- Sent an OpenAI-compatible request to the deployed model.

## Clean Up

Stop the port-forward and remove the quickstart deployment: