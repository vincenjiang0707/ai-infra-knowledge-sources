source: https://docs.nvidia.com/dynamo/v1.1.0/kubernetes-deployment/deployment-guide/detailed-installation-guide
lastmod: 2026-09-24T19:58:16.636Z

# Detailed Installation Guide

Deploy and manage Dynamo inference graphs on Kubernetes with automated orchestration and scaling, using the Dynamo Kubernetes Platform.

## Before You Start

Determine your cluster environment:

**Shared/Multi-Tenant Cluster** (K8s cluster with existing Dynamo artifacts):

- CRDs already installed cluster-wide - skip CRD installation step
- A cluster-wide Dynamo operator is likely already running
**Do NOT install another operator**- use the existing cluster-wide operator

**Dedicated Cluster** (full cluster admin access):

- You install CRDs yourself
- Can use cluster-wide operator (default)

**Local Development** (Minikube, testing):

- See
[Minikube Setup](https://docs.nvidia.com/dynamo/v1.1.0/kubernetes-deployment/deployment-guide/minikube-setup)first, then follow installation steps below

To check if CRDs already exist:

To check if a cluster-wide operator already exists:

## Installation Paths

Platform is installed using Dynamo Kubernetes Platform [helm chart](https://github.com/ai-dynamo/dynamo/tree/v1.1.0/deploy/helm/charts/platform/README.md).

**Path A: Pre-built Artifacts**

- Use case: Production deployment, shared or dedicated clusters
- Source: NGC published Helm charts
- Time: ~10 minutes
- Jump to:
[Path A](https://docs.nvidia.com/dynamo/v1.1.0/kubernetes-deployment/deployment-guide/detailed-installation-guide#path-a-production-install)

**Path B: Custom Build from Source**

- Use case: Contributing to Dynamo, using latest features from main branch, customization
- Requirements: Docker build environment
- Time: ~30 minutes
- Jump to:
[Path B](https://docs.nvidia.com/dynamo/v1.1.0/kubernetes-deployment/deployment-guide/detailed-installation-guide#path-b-custom-build-from-source)

All helm install commands could be overridden by either setting the values.yaml file or by passing in your own values.yaml:

and/or setting values as flags to the helm install command, as follows:

## Prerequisites

Before installing the Dynamo Kubernetes Platform, ensure you have the following tools and access:

### Required Tools

### Cluster and Access Requirements

**Kubernetes cluster v1.24+**with admin or namespace-scoped access**Cluster type determined**(shared vs dedicated) — see[Before You Start](https://docs.nvidia.com/dynamo/v1.1.0/kubernetes-deployment/deployment-guide/detailed-installation-guide#before-you-start)**CRD status checked**if on a shared cluster**NGC credentials**(optional) — required only if pulling NVIDIA images from NGC

### Verify Installation

Run the following to confirm your tools are correctly installed:

### Pre-Deployment Checks

Before proceeding, run the pre-deployment check script to verify your cluster meets all requirements:

This script validates kubectl connectivity, default StorageClass configuration, and GPU node availability. See [Pre-Deployment Checks](https://github.com/ai-dynamo/dynamo/tree/v1.1.0/deploy/pre-deployment/README.md) for details.


No cluster?See[Minikube Setup]for local development.

**Estimated installation time:** 5-30 minutes depending on path

## Path A: Production Install

Install from [NGC published artifacts](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/collections/ai-dynamo/artifacts).

**v0.9.0 Helm Chart Issue:** The initial v0.9.0 `dynamo-platform`

Helm chart sets the operator image to v0.7.1 instead of v0.9.0. Use `RELEASE_VERSION=0.9.0-post1`

or add `--set dynamo-operator.controllerManager.manager.image.tag=0.9.0`

to your helm install command.

**For Shared/Multi-Tenant Clusters:**


DEPRECATED:Namespace-restricted mode (`namespaceRestriction.enabled=true`

) is deprecated and will be removed in a future release. New deployments should use the default cluster-wide mode. If you are currently using namespace-restricted mode, plan to migrate to cluster-wide mode.

For multinode deployments, you need to install multinode orchestration components:

**Option 1 (Recommended): Grove + KAI Scheduler**

For production environments, Grove and KAI Scheduler should be installed **separately** from the dynamo-platform chart. This allows independent lifecycle management, version pinning, and upgrade control.

**Compatibility Matrix:**

After installing them separately, enable Dynamo integration:

For **development/testing only**, you can install them as bundled subcharts:

Note: `global.kai-scheduler.install`

/ `global.grove.install`

control whether the bundled subcharts are deployed. When set, integration is automatically enabled. `global.kai-scheduler.enabled`

/ `global.grove.enabled`

can be set independently when using externally-managed installations.

**Option 2: LeaderWorkerSet (LWS) + Volcano**

- LWS >= v0.7.0 is required for native gang scheduling support.
- If using LWS for multinode deployments, you must also install Volcano (required dependency):
[LWS Installation](https://github.com/kubernetes-sigs/lws#installation)(>= v0.7.0)[Volcano Installation](https://volcano.sh/en/docs/installation/)(required for gang scheduling with LWS)

- When installing LWS with Volcano for gang scheduling, set the gang scheduling value:
See the
[LWS documentation](https://lws.sigs.k8s.io/docs/)for details. - These must be installed manually before deploying multinode workloads with LWS.

See the [Multinode Deployment Guide](https://docs.nvidia.com/dynamo/v1.1.0/kubernetes-deployment/multinode/multinode-deployments) for details on orchestrator selection.

By default, Model Express Server is not used. If you wish to use an existing Model Express Server, you can set the modelExpressURL to the existing server’s URL in the helm install command:

**DEPRECATED:** Namespace-restricted mode is deprecated and will be removed in a future release.
By default, Dynamo Operator is installed cluster-wide and will monitor all namespaces. This is the recommended and only supported mode going forward.

### GPU Discovery for DynamoGraphDeploymentRequests (Deprecated Namespace-Scoped Mode)


DEPRECATED:This section applies only to the deprecated namespace-restricted mode. New deployments should use cluster-wide mode, which has GPU discovery by default.

GPU discovery is **enabled by default** for namespace-scoped operators. The Helm chart automatically provisions a ClusterRole/ClusterRoleBinding granting the operator read-only access to node GPU labels.

**To disable GPU discovery** (if your installer lacks ClusterRole creation permissions):

When GPU discovery is disabled, you must provide hardware configuration manually in each DynamoGraphDeploymentRequest:


Note: If GPU discovery is disabled and no hardware config is provided, the DGDR will be rejected at admission time with a clear error message.

## Path B: Custom Build from Source

Build and deploy from source for customization, contributing to Dynamo, or using the latest features from the main branch.

Note: This gives you access to the latest unreleased features and fixes on the main branch.

## Verify Installation

## Next Steps

-
**Deploy Model/Workflow** -
**Explore Backend Guides** -
**Optional:**[Set up Prometheus & Grafana](https://docs.nvidia.com/dynamo/v1.1.0/kubernetes-deployment/observability-k-8-s/metrics)[SLA Planner Guide](https://docs.nvidia.com/dynamo/v1.1.0/components/planner/planner-guide)(for SLA-aware scheduling and autoscaling)


## Troubleshooting

**“VALIDATION ERROR: Cannot install cluster-wide Dynamo operator”**

Cause: Attempting cluster-wide install on a shared cluster with existing namespace-restricted operators.

Solution: Migrate the existing namespace-restricted operators to cluster-wide mode. Namespace-restricted mode is deprecated and should no longer be used.

**CRDs already exist**

Cause: Installing CRDs on a cluster where they’re already present (common on shared clusters).

Solution: Skip step 2 (CRD installation), proceed directly to platform installation.

To check if CRDs exist:

**Pods not starting?**

**HuggingFace model access?**

**Bitnami etcd “unrecognized” image?**

This error that you might encounter during helm install is due to bitnami changing their docker repository to a [secure one](https://github.com/bitnami/charts/tree/main/bitnami/etcd#%EF%B8%8F-important-notice-upcoming-changes-to-the-bitnami-catalog).

just add the following to the helm install command:

**Clean uninstall?**

To uninstall the platform, you can run the following command:

To uninstall the CRDs, follow these steps:

Get all of the dynamo CRDs installed in your cluster:

You should see something like this:

Delete each CRD one by one: