source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/integrations/kubernetes-integrations/lws
lastmod: 2026-09-23T23:30:39.914Z

# LWS

Dynamo can use [LeaderWorkerSet (LWS)](https://lws.sigs.k8s.io/docs/) as the Kubernetes orchestration layer for multinode workloads. LWS is the lightweight path for spanning one Dynamo worker service across multiple nodes; Dynamo pairs it with [Volcano](https://volcano.sh/) for gang scheduling.

Use LWS when you want a simpler multinode orchestrator than Grove, or when your cluster already standardizes on LWS and Volcano. Grove remains the default when both Grove and LWS are available.

## Prerequisites

- Kubernetes cluster with GPU nodes.
- LWS version
`0.7.0`

or newer. - Volcano installed for gang scheduling.
- Dynamo Kubernetes Platform installed.

The installation guide includes the exact Helm commands for [LWS and Volcano](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/start-here/installation-guide#lws--volcano).

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

For detailed backend-specific behavior and examples, see the [Multinode Deployments](https://docs.nvidia.com/dynamo/v1.3.0/kubernetes-deployment/scale/multinode-deployments) guide.