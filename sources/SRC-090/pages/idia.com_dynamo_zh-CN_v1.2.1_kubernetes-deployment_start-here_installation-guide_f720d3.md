source: https://docs.nvidia.com/dynamo/zh-CN/v1.2.1/kubernetes-deployment/start-here/installation-guide
lastmod: 2026-09-23T23:30:39.914Z

# Installation Guide

This guide walks you through installing everything needed to deploy models with Dynamo on Kubernetes. Follow the steps in order — each builds on the previous one.

## Prerequisites

Before you begin, make sure you have:

- A
**Kubernetes cluster (v1.24+)**with GPU-capable nodes. See the cloud provider guides if you need to create one:[Amazon EKS](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/cloud-provider-guides/aws/eks-setup)|[Azure AKS](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/cloud-provider-guides/azure/aks-setup)|[Google GKE](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/cloud-provider-guides/gcp/gke-setup)- For local development:
[Minikube Setup](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/start-here/minikube-setup)

**kubectl**v1.24+ —[Install kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)**Helm**v3.0+ —[Install Helm](https://helm.sh/docs/intro/install/)

**Cloud provider GPU drivers**: The GPU Operator (Step 1) installs GPU drivers for you. When creating your cluster’s GPU node pools, **do not enable provider-managed GPU driver installation** (e.g., skip AKS GPU driver install, don’t use GKE `--accelerator gpu-driver-version=latest`

). If your nodes already have provider-managed drivers, see the GPU Operator step for how to handle this.

Verify your tools:

## Overview

Every Dynamo deployment requires two Helm charts: the **GPU Operator** (Step 1) and the **Dynamo Platform** (Step 2). Everything else is optional. Decide what optional components you need before starting so you can install them in Step 3.

**Grove + KAI Scheduler** — Grove is the default multinode orchestrator. The operator returns a hard error on multinode deployments if neither Grove nor [LeaderWorkerSet (LWS)](https://github.com/kubernetes-sigs/lws#installation) is available. KAI Scheduler is optional but recommended alongside Grove for GPU-aware scheduling. See [Grove](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/scale/grove) for details.

**Network Operator / RDMA** — Without RDMA, disaggregated inference falls back to TCP automatically, but with severe performance degradation (~98s TTFT vs ~200-500ms with RDMA). Required for any production disaggregated deployment. Setup is cloud-provider-specific — see the [Disaggregated Communication Guide](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/operate/disagg-communication) and your cloud provider guide.

**kube-prometheus-stack** — Required for the Planner’s `sla`

optimization mode (it reads live TTFT/ITL metrics from Prometheus). Also required for KEDA/HPA-based autoscaling. The Planner’s `throughput`

mode can function without it using internal queue depth signals, but metrics-driven features will not work. See [Metrics](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/operate/observability/metrics) for details.

**Shared storage** — Prevents each pod from downloading model weights independently. Without it, large models (>70B) take hours to download per pod, and many replicas will hit HuggingFace rate limits. Not enforced by the operator — this is an operational concern. See [Model Caching](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/model-loading/model-caching) for the full walkthrough.

## Step 1: Install the GPU Operator

The [NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/getting-started.html) automates deployment of all NVIDIA software components needed to provision GPUs — drivers, container toolkit, device plugin, and monitoring.

If your GPU nodes already have provider-managed drivers installed (e.g., you used GKE’s `--accelerator gpu-driver-version=latest`

), uncomment the `driver.enabled=false`

line above so the operator doesn’t conflict with the existing drivers.

Some cloud providers require additional GPU Operator configuration. See your provider guide for details:

[AKS GPU Operator setup](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/cloud-provider-guides/azure/aks-setup)— skip AKS-managed GPU driver install on node pools[EKS GPU Operator setup](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/cloud-provider-guides/aws/eks-setup)[GKE GPU Operator setup](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/cloud-provider-guides/gcp/gke-setup)—`LD_LIBRARY_PATH`

and`ldconfig`

init requirements

Verify the GPU Operator is running:

## Step 2: Install the Dynamo Platform

Set your environment variables:

All `helm install`

commands can be customized with your own values file: `helm install ... -f your-values.yaml`


**Shared/Multi-Tenant Clusters**: If a cluster-wide Dynamo operator is already running, do **not** install another one. Check with:

**Namespace-restricted mode** (`namespaceRestriction.enabled=true`

) is deprecated and will be removed in a future release. Use the default cluster-wide mode for all new deployments.

Verify the Dynamo platform is running:

## Step 3: Install Optional Components

The Dynamo install command above includes commented flags for each optional component. Install the component first, then uncomment the corresponding flag before running `helm install`

in Step 2 (or run `helm upgrade --reuse-values`

with the flag if you’ve already installed Dynamo).

### Multinode:

Multinode deployments require either Grove + KAI Scheduler or an alternative orchestrator setup (LeaderWorkerSet + Volcano) to enable gang scheduling for workloads that span multiple nodes. See the [Multinode Deployment Guide](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/scale/multinode-deployments) for details on orchestrator selection and configuration.

#### Grove + KAI Scheduler

There are two ways to enable Grove and KAI Scheduler, controlled by which flags you uncomment in the Dynamo install command:

— Dynamo installs and manages Grove/KAI as bundled subcharts. Simplest path; recommended for dev/testing.`install=true`

— Tells Dynamo that Grove/KAI are already installed and externally managed. Use this when you install Grove/KAI separately (e.g., to manage their lifecycle independently or share them across namespaces). Recommended for production.`enabled=true`


For the `enabled=true`

path, install Grove and KAI Scheduler separately first. See the [Grove installation guide](https://github.com/NVIDIA/grove/blob/main/docs/installation.md) and [KAI Scheduler deployment guide](https://github.com/NVIDIA/KAI-Scheduler) for instructions.

**Compatibility matrix:**

#### LWS + Volcano

If you are not using Grove for multinode, you can use [LeaderWorkerSet (LWS)](https://lws.sigs.k8s.io/docs/installation/) (>= v0.7.0) with [Volcano](https://github.com/volcano-sh/volcano#quick-start-guide) for gang scheduling. Both must be installed before deploying multinode workloads.

- Install Volcano:

- Install LWS (>= v0.7.0) with Volcano gang scheduling enabled:

See the [LWS docs](https://lws.sigs.k8s.io/docs/) and [Volcano docs](https://github.com/volcano-sh/volcano#quick-start-guide) for configuration options, and the [Multinode Deployment Guide](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/scale/multinode-deployments) for orchestrator selection.

### Network Operator / RDMA

RDMA setup is cloud-provider-specific. See the [Disaggregated Communication Guide](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/operate/disagg-communication) for transport options, UCX configuration, and performance expectations, and your cloud provider guide for setup instructions:

[AKS — InfiniBand + Network Operator](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/cloud-provider-guides/azure/rdma-infini-band)[EKS — EFA device plugin](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/cloud-provider-guides/aws/eks-setup)(also see the[EFA configuration guide](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/operate/disagg-communication#aws-efa-configuration))[GKE — GPUDirect-TCPXO](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/cloud-provider-guides/gcp/gke-setup)

### kube-prometheus-stack

Install Prometheus before running the Dynamo install command so you can set the endpoint in one pass:

Then uncomment the `prometheusEndpoint`

line in the Dynamo install command. The Dynamo operator automatically creates PodMonitors for its components. See [Metrics](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/operate/observability/metrics) for dashboard setup and available metrics, and [Logging](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/operate/observability/logging) for the Grafana Loki + Alloy logging stack.

### Shared Storage for Model Caching

Set up a `ReadWriteMany`

PVC so all pods share downloaded model weights instead of each downloading independently. No Dynamo chart flags are needed — storage is configured in your deployment spec. Setup is cloud-provider-specific:

[AKS — Azure Files / Managed Lustre](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/cloud-provider-guides/azure/aks-storage)[EKS — EFS](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/cloud-provider-guides/aws/efs)- GKE — Cloud Filestore (see
[GKE guide](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/cloud-provider-guides/gcp/gke-setup))

For large clusters with frequent model updates, consider [ModelExpress](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/model-loading/model-caching#option-2-modelexpress-p2p-distribution) for P2P model distribution and ModelStreamer for direct streaming from object storage. See [Model Caching](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/model-loading/model-caching) for the full walkthrough including the download Job, mount configuration, and ModelExpress setup.

## Step 4: Pre-Deployment Check

Run the pre-deployment check script to validate your cluster is ready for deployments:

This checks kubectl connectivity, default StorageClass configuration, GPU node availability, and GPU Operator status. See [Pre-Deployment Checks](https://github.com/ai-dynamo/dynamo/tree/v1.2.1/deploy/pre-deployment/README.md) for details.

## Next Steps

Your cluster is ready. Follow the ** Deployment Overview** to choose between applying a tuned DGD recipe, creating a DGD directly, or using DGDR to generate one.

## Troubleshooting

**“VALIDATION ERROR: Cannot install cluster-wide Dynamo operator”**

Cause: Attempting cluster-wide install on a shared cluster with existing namespace-restricted operators.

Solution: Migrate the existing namespace-restricted operators to cluster-wide mode. Namespace-restricted mode is deprecated.

**CRDs already exist**

Cause: Installing CRDs on a cluster where they’re already present (common on shared clusters).

Solution: CRDs are installed automatically by the Helm chart. If you encounter conflicts, check existing CRDs with `kubectl get crd | grep dynamo`

.

**Pods not starting?**

**Bitnami etcd “unrecognized” image?**

Add to the helm install command:

**Clean uninstall?**

## Advanced: Build from Source

If you need to contribute to Dynamo or use the latest unreleased features from the main branch: