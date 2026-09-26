source: https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/cloud-provider-guides/azure/spot-v-ms
lastmod: 2026-09-24T19:58:16.636Z

# AKS Spot VMs

[Azure Spot VMs](https://azure.microsoft.com/en-us/products/virtual-machines/spot) offer significant cost savings for GPU workloads but can be evicted by Azure at any time. This guide covers the configuration required to schedule Dynamo on Spot VM node pools.

## How AKS Taints Spot Nodes

When a node pool uses Spot VMs, AKS automatically applies the following taint to all nodes in that pool:

This prevents standard workloads from landing on Spot nodes by default. Any pod that should run on a Spot node must explicitly tolerate this taint.

## Required Toleration

Add the following toleration to any workload that should run on Spot nodes:

## Deploying Dynamo on Spot Nodes

The Dynamo platform Helm chart includes a pre-built values file for Spot VM deployments — [ examples/deployments/AKS/values-aks-spot.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/examples/deployments/AKS/values-aks-spot.yaml) — which adds the required toleration to all Dynamo components:

- Dynamo operator controller manager
- Webhook CA inject and cert generation jobs
- etcd
- NATS
- MPI SSH key generation job
- Other core Dynamo platform pods

Install Dynamo with the Spot values file (from `examples/deployments/AKS/`

):

To upgrade an existing installation:

## Creating a Spot GPU Node Pool

Add a Spot GPU node pool to an existing AKS cluster:

`--spot-max-price -1`

means pay up to the on-demand price (recommended). `--eviction-policy Delete`

removes evicted nodes from the pool; use `Deallocate`

if you want to preserve node state across evictions.