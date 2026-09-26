source: https://docs.nvidia.com/dynamo/kubernetes/installation/multinode-orchestration
lastmod: 2026-09-25T12:26:00.485Z

# Multinode Orchestration

Multinode deployments require either Grove + KAI Scheduler or an alternative orchestrator setup (LeaderWorkerSet + Volcano) to enable gang scheduling for workloads that span multiple nodes. See the [Multinode Deployment Guide](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/multinode-deployments) for details on orchestrator selection and configuration.

## Option 1: Grove + KAI Scheduler

Grove is the default and recommended orchestrator for multinode deployments. It requires KAI Scheduler as well. There are two ways to enable Grove and KAI Scheduler, either dynamo can install it automatically (recommended for development and testing), or you can install them separately (recommended for production).

###### Managed Installation

###### External Installation

The managed installation is recommended for development and testing. It is the simplest path, and allows Dynamo to manage the lifecycle of Grove and KAI Scheduler as bundled subcharts. Run the following command to install Dynamo with Grove and KAI Scheduler:

## Option 2: LeaderWorkerSet + Volcano

If you are not using Grove for multinode, you can use [LeaderWorkerSet (LWS)](https://lws.sigs.k8s.io/docs/installation/) (>= v0.7.0) with [Volcano](https://github.com/volcano-sh/volcano#quick-start-guide) for gang scheduling. Both must be installed before deploying multinode workloads.

- Install Volcano:

- Install LWS (>= v0.7.0) with Volcano gang scheduling enabled:

See the [LWS docs](https://lws.sigs.k8s.io/docs/) and [Volcano docs](https://github.com/volcano-sh/volcano#quick-start-guide) for configuration options, and the [Multinode Deployment Guide](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/multinode-deployments) for orchestrator selection.