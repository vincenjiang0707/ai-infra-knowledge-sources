source: https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/multinode/lws
lastmod: 2026-09-24T19:58:16.636Z

# LWS

Dynamo can use [LeaderWorkerSet (LWS)](https://lws.sigs.k8s.io/docs/) as the Kubernetes orchestration layer for multinode workloads. LWS is the lightweight path for spanning one Dynamo worker service across multiple nodes; Dynamo pairs it with [Volcano](https://volcano.sh/) for gang scheduling.

Use LWS when you want a simpler multinode orchestrator than Grove, or when your cluster already standardizes on LWS and Volcano. Grove remains the default when both Grove and LWS are available.

## Prerequisites

- Kubernetes cluster with GPU nodes.
- LWS version
`0.7.0`

or newer. - Volcano installed for gang scheduling.
- Dynamo Kubernetes Platform installed.

The installation guide includes the exact Helm commands for [LWS and Volcano](https://docs.nvidia.com/dynamo/kubernetes/installation/install-dynamo#lws--volcano).

## Orchestrator Selection

For multinode deployments, the Dynamo operator selects an orchestrator based on what is installed:

To force the LWS path when Grove is also present:

## Multinode Spec

Set `multinode.nodeCount`

on the service that should span nodes. The total GPU count is `multinode.nodeCount`

multiplied by the per-node GPU limit:

In this example, Dynamo asks LWS to place the backend across 2 nodes with 4 GPUs per node, for 8 GPUs total. Make sure your backend’s tensor parallel or distributed execution flags match that total.

## Backend Behavior

The operator injects backend-specific multinode settings into the generated LeaderWorkerSet:

For detailed backend-specific behavior and examples, see the [Multinode Deployments](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/multinode-deployments) guide.