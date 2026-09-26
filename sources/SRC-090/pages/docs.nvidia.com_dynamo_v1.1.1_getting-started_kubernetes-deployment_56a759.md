source: https://docs.nvidia.com/dynamo/v1.1.1/getting-started/kubernetes-deployment
lastmod: 2026-09-24T19:58:16.636Z

# Quickstart

Get a model running on Kubernetes in minutes.

## Prerequisites

- Kubernetes cluster (v1.24+) with GPU nodes
[kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)(v1.24+)[Helm](https://helm.sh/docs/intro/install/)(v3.0+) installed[NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/getting-started.html)installed on the cluster- HuggingFace token secret on cluster

### HuggingFace token secret

Create a HuggingFace token secret for model downloads. If you don’t have a token, see the HuggingFace [token guide](https://huggingface.co/docs/hub/en/security-tokens).

### GPU Operator quick install

If you don’t have the GPU Operator yet:

If your cluster already provides GPU drivers (e.g., GKE with `gpu-driver-version=latest`

, or AKS), add:

### Detailed installation

The GPU Operator is the only prerequisite for a basic deployment. For additional features like RDMA, Prometheus, or multinode scheduling with Grove/KAI Scheduler, see the [Installation Guide](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/installation-guide).

If your GPU SKU and cloud provider are supported, you can use [AICR](https://github.com/NVIDIA/aicr) for rapid installation of prerequisites and the Dynamo Helm chart.

### Verify cluster is ready

Optionally, verify your cluster is ready:

## Install Dynamo

Wait for the platform pods:

## Deploy Your First Model

Deploy `Qwen/Qwen3-0.6B`

using a DynamoGraphDeploymentRequest (DGDR).

The DGDR is the entrypoint for deploying models. It runs automatic profiling for your model/hardware and creates an auto-configured DynamoGraphDeployment (DGD). After that, the DGDR is completed and reaches a terminal state, similar to a K8s Job and can be cleaned up. The DGD is the resource that persists and serves your model.

Watch the DGDR progress from `Pending`

→ `Profiling`

→ `Deploying`

→ `Deployed`

:

Dynamo supports vLLM, TensorRT-LLM, and SGLang backends. Setting `backend: auto`

lets the profiler choose the best one for your model and hardware. See the [backends guide](https://docs.nvidia.com/dynamo/v1.1.1/backends) for details.

## Send a Request

Once the DGDR shows `Deployed`

:

## Cleanup

## Next Steps

— Cloud provider setup, GPU Operator details, optional components (Grove, RDMA, model caching, Prometheus)[Installation Guide](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/installation-guide)— Strategy selection, model caching, planner, multinode, common pitfalls[Model Deployment Guide](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/model-deployment-guide)— Spec reference, lifecycle phases, monitoring commands, DGDR vs DGD[DGDR Reference](https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/deployment-guide/dgdr-reference)— Hand-craft a DGD spec for full control[Creating Deployments](https://docs.nvidia.com/dynamo/v1.1.1/additional-resources/creating-deployments)