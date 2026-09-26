source: https://docs.nvidia.com/dynamo/kubernetes/installation/install-dynamo
lastmod: 2026-09-25T12:26:00.485Z

# Installation Guide

This guide walks you through installing everything needed to deploy models with Dynamo on Kubernetes. Follow the steps in order — each builds on the previous one.

## Prerequisites

Before you begin, make sure you have Helm v3 or later and choose the accelerator type in your cluster:

###### NVIDIA GPU

###### Intel GPU

- A Kubernetes 1.30 or later cluster with NVIDIA GPU nodes. See the cloud provider guides if you need to create one:
[Amazon EKS](https://docs.nvidia.com/dynamo/kubernetes/installation/managed-kubernetes/eks/eks-setup)|[Azure AKS](https://docs.nvidia.com/dynamo/kubernetes/installation/managed-kubernetes/azure/aks-setup)|[Google GKE](https://docs.nvidia.com/dynamo/kubernetes/installation/managed-kubernetes/gcp/gke-setup)- For local development:
[Minikube Setup](https://docs.nvidia.com/dynamo/cli/installation/minikube-setup)

`kubectl`

1.30 or later.

The GPU Operator in the first installation step can install NVIDIA drivers. Do not also enable provider-managed drivers when you create the GPU node pool. If the nodes already have drivers, disable GPU Operator driver management as shown in that step.

Verify the client tools:

## Overview

Every Dynamo deployment requires accelerator support and the **Dynamo Platform**. NVIDIA GPU clusters can use the NVIDIA GPU Operator. Intel GPU clusters use the Intel resource driver with DRA. The Dynamo Platform installation is the same after the cluster exposes its accelerator resources. Everything else is optional.

**Grove + KAI Scheduler** — Grove is the default multinode orchestrator. The operator returns a hard error on multinode deployments if neither Grove nor [LeaderWorkerSet (LWS)](https://github.com/kubernetes-sigs/lws#installation) is available. KAI Scheduler is optional but recommended alongside Grove for GPU-aware scheduling. See [Grove](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/multinode/grove) for details.

**Network Operator / RDMA** — Without RDMA, disaggregated inference falls back to TCP automatically, but with severe performance degradation (~98s TTFT vs ~200-500ms with RDMA). Required for any production disaggregated deployment. Setup is cloud-provider-specific — see the [Disaggregated Communication Guide](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/disagg-communication) and your cloud provider guide.

**kube-prometheus-stack** — Required for the Planner’s `sla`

optimization mode (it reads live TTFT/ITL metrics from Prometheus). Also required for KEDA/HPA-based autoscaling. The Planner’s `throughput`

mode can function without it using internal queue depth signals, but metrics-driven features will not work. See [Metrics](https://docs.nvidia.com/dynamo/kubernetes/operations/observability) for details.

**Shared storage** — Prevents each pod from downloading model weights independently. Without it, large models (>70B) take hours to download per pod, and many replicas will hit HuggingFace rate limits. Not enforced by the operator — this is an operational concern. See [Model Caching](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/model-loading/model-caching) for the full walkthrough.

### Install accelerator support

###### NVIDIA GPU

###### Intel GPU

The [NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/getting-started.html) automates deployment of the drivers, container toolkit, device plugin, and monitoring components used by NVIDIA GPU nodes.

Set `driver.enabled=false`

when the nodes already have provider-managed NVIDIA drivers. See the
[AKS](https://docs.nvidia.com/dynamo/kubernetes/installation/managed-kubernetes/azure/aks-setup), [EKS](https://docs.nvidia.com/dynamo/kubernetes/installation/managed-kubernetes/eks/eks-setup), or
[GKE](https://docs.nvidia.com/dynamo/kubernetes/installation/managed-kubernetes/gcp/gke-setup) guide for provider-specific requirements.

Verify the installation:

### Install the Dynamo Platform

Set your environment variables:

All `helm install`

commands can be customized with your own values file: `helm install ... -f your-values.yaml`


**Shared/Multi-Tenant Clusters**: If a cluster-wide Dynamo operator is already running, do **not** install another one. Check with:

**Namespace-restricted mode** (`namespaceRestriction.enabled=true`

) is only for development and
testing. It is not supported for production. Set `dynamo-operator.upgradeCRD=false`

; see
[Dynamo Operator](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/dynamo-operator#namespace-restricted-mode).

Verify the Dynamo platform is running:

### Install Optional Components

The Dynamo install command above includes commented flags for each optional component. Install the component first, then uncomment the corresponding flag before running `helm install`

in Step 2 (or run `helm upgrade --reuse-values`

with the flag if you’ve already installed Dynamo).

### Multinode:

Multinode deployments require either Grove + KAI Scheduler or an alternative orchestrator setup (LeaderWorkerSet + Volcano) to enable gang scheduling for workloads that span multiple nodes. See the [Multinode Deployment Guide](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/multinode-deployments) for details on orchestrator selection and configuration.

#### Grove + KAI Scheduler

There are two ways to enable Grove and KAI Scheduler, controlled by which flags you uncomment in the Dynamo install command:

— Dynamo installs and manages Grove/KAI as bundled subcharts. Simplest path; recommended for dev/testing.`install=true`

— Tells Dynamo that Grove/KAI are already installed and externally managed. Use this when you install Grove/KAI separately (e.g., to manage their lifecycle independently or share them across namespaces). Recommended for production.`enabled=true`


For the `enabled=true`

path, install Grove and KAI Scheduler separately first. See the [Grove installation guide](https://github.com/NVIDIA/grove/blob/main/docs/installation.md) and [KAI Scheduler deployment guide](https://github.com/NVIDIA/KAI-Scheduler) for instructions.

**Compatibility matrix:**

Upgrade Grove in lockstep with Dynamo while the Grove APIs remain unstable. Dynamo 1.3.x expects
Grove’s earlier `ClusterTopology`

API and is incompatible with the newer
`ClusterTopologyBinding`

API. Dynamo 1.4.x expects `ClusterTopologyBinding`

.

#### LWS + Volcano

If you are not using Grove for multinode, you can use [LeaderWorkerSet (LWS)](https://lws.sigs.k8s.io/docs/installation/) (>= v0.7.0) with [Volcano](https://github.com/volcano-sh/volcano#quick-start-guide) for gang scheduling. Both must be installed before deploying multinode workloads.

- Install Volcano:

- Install LWS (>= v0.7.0) with Volcano gang scheduling enabled:

See the [LWS docs](https://lws.sigs.k8s.io/docs/) and [Volcano docs](https://github.com/volcano-sh/volcano#quick-start-guide) for configuration options, and the [Multinode Deployment Guide](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/multinode-deployments) for orchestrator selection.

### Network Operator / RDMA

RDMA setup is cloud-provider-specific. See the [Disaggregated Communication Guide](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/disagg-communication) for transport options, UCX configuration, and performance expectations, and your cloud provider guide for setup instructions:

[AKS — InfiniBand + Network Operator](https://docs.nvidia.com/dynamo/kubernetes/installation/rdma-setup/infiniband-on-azure)[EKS — EFA device plugin](https://docs.nvidia.com/dynamo/kubernetes/installation/managed-kubernetes/eks/eks-setup)(also see the[EFA configuration guide](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/disagg-communication#aws-efa-configuration))[GKE — GPUDirect-TCPXO](https://docs.nvidia.com/dynamo/kubernetes/installation/managed-kubernetes/gcp/gke-setup)

### kube-prometheus-stack

Install Prometheus before running the Dynamo install command so you can set the endpoint in one pass:

Then uncomment the `prometheusEndpoint`

line in the Dynamo install command. The Dynamo operator automatically creates PodMonitors for its components. See [Metrics](https://docs.nvidia.com/dynamo/kubernetes/operations/observability) for dashboard setup and available metrics, and [Logging](https://docs.nvidia.com/dynamo/kubernetes/installation/observability.md) for the Grafana Loki + Alloy logging stack.

### Shared Storage for Model Caching

Set up a `ReadWriteMany`

PVC so all pods share downloaded model weights instead of each downloading independently. No Dynamo chart flags are needed — storage is configured in your deployment spec. Setup is cloud-provider-specific:

[AKS — Azure Files / Managed Lustre](https://docs.nvidia.com/dynamo/kubernetes/installation/model-storage/aks-storage)[EKS — EFS](https://docs.nvidia.com/dynamo/kubernetes/installation/model-storage/efs)- GKE — Cloud Filestore (see
[GKE guide](https://docs.nvidia.com/dynamo/kubernetes/installation/managed-kubernetes/gcp/gke-setup))

For large clusters with frequent model updates, consider [ModelExpress](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/model-loading/model-caching#option-2-modelexpress-p2p-distribution) for P2P model distribution and ModelStreamer for direct streaming from object storage. See [Model Caching](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/model-loading/model-caching) for the full walkthrough including the download Job, mount configuration, and ModelExpress setup.

### Pre-Deployment Check

Run the pre-deployment check script to validate your cluster is ready for deployments:

This checks kubectl connectivity, default StorageClass configuration, GPU node availability, and GPU Operator status. See [Pre-Deployment Checks](https://github.com/ai-dynamo/dynamo/tree/v1.4.2/deploy/pre-deployment/README.md) for details.

## Alternative: Install with AICR

Steps 1–3 install each component — GPU Operator, Dynamo Platform, Grove, RDMA — with its own Helm command. [NVIDIA AI Cluster Runtime (AICR)](https://github.com/NVIDIA/aicr) is an alternative that generates one version-locked **recipe** for the whole stack, then renders it into deployment-ready bundles for Helm, Argo CD, Flux, or Helmfile. For a supported environment, the `aicr`

CLI drives the entire installation flow from a single recipe: GPU Operator, NVIDIA DRA driver, Network Operator (RDMA), Grove, KAI Scheduler, cert-manager, kube-prometheus-stack, and the Dynamo Platform.

AICR is a new, separately maintained project. It validates **specific combinations** of cloud, GPU, and OS, so it fits a cluster that matches a validated Dynamo recipe rather than an arbitrary environment. You still bring your own Kubernetes cluster — AICR generates and validates the runtime configuration, it does not provision clusters. See the [AICR documentation](https://docs.nvidia.com/aicr) for the authoritative support matrix.

AICR validates recipes across these dimensions; not every combination has a Dynamo recipe, so check the AICR docs for the validated set:

Dynamo recipes use Dynamic Resource Allocation (DRA) for GPUs, which requires **Kubernetes 1.34+**.

### Install Dynamo with the AICR CLI

- Install the CLI with Homebrew:

Or use the install script:

- Generate a recipe for your environment. Set
`--platform dynamo`

and match`--service`

,`--accelerator`

, and`--os`

to your cluster:

- Render the recipe into deployment bundles. Choose the deployer that matches your workflow (
`helm`

,`argocd`

,`flux`

, or`helmfile`

):

- Deploy the generated bundles to your cluster, then validate the running cluster against the recipe:

For manual installation, the full command reference, and the supported environment matrix, see the [AICR documentation](https://docs.nvidia.com/aicr). Once AICR has installed the Dynamo Platform, continue with the verification steps above and Next Steps below.

## Next Steps

Your cluster is ready. Follow the ** Model Deployment guide** to choose between applying a tuned DGD recipe, creating a DGD directly, or using DGDR to generate one.

## Troubleshooting

**“VALIDATION ERROR: Cannot install cluster-wide Dynamo operator”**

Cause: Attempting cluster-wide install on a shared cluster with existing namespace-restricted operators.

Solution: Remove the development/test namespace-restricted operators, then install one cluster-wide operator for production use.

**CRDs already exist**

Cause: Installing CRDs on a cluster where they’re already present (common on shared clusters).

Solution: The cluster-wide operator’s `crd-apply`

init container manages CRDs automatically. If you
encounter conflicts, check existing CRDs with `kubectl get crd | grep dynamo`

.

**Pods not starting?**

**Bitnami etcd “unrecognized” image?**

Add to the helm install command:

**Clean uninstall?**