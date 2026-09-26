source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/kubernetes-deployment/cloud-provider-guides/azure/aks-storage
lastmod: 2026-09-23T23:30:39.914Z

# Storage for Model Caching on AKS

For implementing tiered storage on AKS, you can take advantage of the different storage options available in Azure. This guide covers choosing the right storage for each Dynamo cache type and configuring PVCs.

## Available Storage Options

Azure Managed Lustre and Local CSI (ephemeral disk) are not installed by default in AKS and require additional setup before use. Azure Disk, Azure Files, and Azure Blob CSI drivers are available out of the box. See the [Azure Lustre CSI Driver](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/cloud-provider-guides/azure/azure-lustre-csi-driver) guide for Lustre setup, or the [AKS CSI storage options documentation](https://learn.microsoft.com/azure/aks/csi-storage-drivers) for a full overview of built-in drivers.

For Azure Managed Lustre setup, see the [Azure Lustre CSI Driver](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/cloud-provider-guides/azure/azure-lustre-csi-driver) guide.

## Recommendations by Cache Type

-
**Model Cache**— raw model artifacts, configuration files, tokenizers, etc.- Persistence: Required to avoid repeated downloads and reduce cold-start latency.
- Recommended storage: Azure Managed Lustre (shared, high throughput) or Azure Disk (single-replica, persistent).

-
**Compilation Cache**— backend-specific compiled artifacts (e.g., TensorRT engines).- Persistence: Optional.
- Recommended storage: Local CSI (fast, node-local) or Azure Disk (persistent when GPU configuration is fixed).

-
**Performance Cache**— runtime tuning and profiling data.- Persistence: Not required.
- Recommended storage: Local CSI (or other ephemeral storage).


## Check Available Storage Classes

List the storage classes available in your AKS cluster:

## Example PVC Configuration

In the `cache.yaml`

in the different [recipes](https://github.com/ai-dynamo/dynamo/tree/v1.3.0/recipes), you can set the `storageClassName`

to a storage option available in your AKS cluster:

## See Also

[Azure Lustre CSI Driver](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/cloud-provider-guides/azure/azure-lustre-csi-driver)— Full setup guide for Azure Managed Lustre[Model Caching](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/model-loading/model-caching)— Full walkthrough for setting up model caching with Dynamo, including download Jobs and mount configuration[AKS CSI Storage Drivers](https://learn.microsoft.com/azure/aks/csi-storage-drivers)— Microsoft documentation for all built-in CSI drivers