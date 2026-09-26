source: https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/cloud-provider-guides/azure/aks-setup
lastmod: 2026-09-24T19:58:16.636Z

Azure Kubernetes Service (AKS)


Azure Kubernetes Service (AKS)

This guide covers setting up an AKS cluster with GPU nodes and deploying Dynamo.

## Prerequisites

- An active Azure subscription with sufficient GPU VM quota
[Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)(`az`

) installed and logged in[kubectl](https://kubernetes.io/docs/tasks/tools/)installed[Helm](https://helm.sh/docs/intro/install/)v3.0+ installed

## Step 1: Create a Resource Group and Cluster

Then get credentials:

## Step 2: Add a GPU Node Pool

Add a GPU-enabled node pool with driver installation skipped. The `--skip-gpu-driver-install`

flag prevents AKS from managing GPU drivers — the NVIDIA GPU Operator (Step 3) will handle that instead.

For RDMA-capable workloads (disaggregated inference), use ND-series VMs such as `Standard_ND96asr_v4`

or `Standard_ND96isr_H100_v5`

. See the [RDMA / InfiniBand guide](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/cloud-provider-guides/azure/rdma-infini-band) for the additional setup required on those nodes.

For a full list of GPU VM sizes, see [GPU-optimized VM sizes](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes-gpu).

## Step 3: Install the NVIDIA GPU Operator

The GPU Operator manages NVIDIA drivers, container toolkit, device plugin, and monitoring on GPU nodes.

Verify the pods are running:

Expected output (abbreviated):

If you need RDMA / InfiniBand for disaggregated inference, **do not install the GPU Operator yet** — the RDMA setup requires different Helm values. See [RDMA / InfiniBand](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/cloud-provider-guides/azure/rdma-infini-band) for the full setup, which includes the correct GPU Operator install command.

## Step 4: Install Dynamo

Follow the [Installation Guide](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/installation-guide) to install the Dynamo Platform and deploy your first model.

## Additional Guides

[RDMA / InfiniBand](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/cloud-provider-guides/azure/rdma-infini-band)

Required for disaggregated inference in production. Without RDMA, KV cache transfers between prefill and decode workers fall back to TCP with severe latency degradation (~98s TTFT vs ~200–500ms with RDMA). ND-series VMs (e.g., `Standard_ND96asr_v4`

, `Standard_ND96isr_H100_v5`

) include Mellanox ConnectX InfiniBand NICs but require additional setup beyond the GPU Operator: the NVIDIA Network Operator, a NicClusterPolicy for MOFED drivers, an `ib-node-config`

DaemonSet to configure kernel modules and memlock limits, and an RDMA Shared Device Plugin to expose the NICs to pods.

[Storage for Model Caching](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/cloud-provider-guides/azure/aks-storage)

Prevents each pod from independently downloading model weights on startup. Without shared storage, large models take hours to load per pod and will hit HuggingFace rate limits at scale. Covers Azure Managed Lustre, Azure Files, Azure Disk, and Local CSI options with per-cache-type recommendations (model cache, compilation cache, performance cache).

[Azure Lustre CSI Driver](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/cloud-provider-guides/azure/azure-lustre-csi-driver)

The recommended storage for large multi-node models requiring high-throughput shared access. Azure Managed Lustre is not installed by default — this guide covers installing and configuring the Lustre CSI driver before you can use it as a PVC storage class.

[Spot VMs](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/cloud-provider-guides/azure/spot-v-ms)

Significantly reduces GPU compute costs by running on preemptible Spot VM node pools. AKS automatically taints Spot nodes with `kubernetes.azure.com/scalesetpriority=spot:NoSchedule`

, so Dynamo components need explicit tolerations. The Dynamo Helm chart includes a pre-built `values-aks-spot.yaml`

that handles this.

## Clean Up Resources

If you want to delete the GPU Operator, follow the [Uninstalling the NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/uninstall.html) guide.

If you want to delete the entire AKS cluster, follow the [Delete an AKS cluster](https://learn.microsoft.com/en-us/azure/aks/delete-cluster) guide.