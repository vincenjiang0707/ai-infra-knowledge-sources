source: https://docs.nvidia.com/dynamo/v1.1.0/getting-started/kubernetes-deployment
lastmod: 2026-09-24T19:58:16.636Z

# Deployment Guide

High-level guide to Dynamo Kubernetes deployments. Start here, then dive into specific guides.

## Important Terminology

**Kubernetes Namespace**: The K8s namespace where your DynamoGraphDeployment resource is created.

- Used for: Resource isolation, RBAC, organizing deployments
- Example:
`dynamo-system`

,`team-a-namespace`


**Dynamo Namespace**: The logical namespace used by Dynamo components for [service discovery](https://docs.nvidia.com/dynamo/v1.1.0/kubernetes-deployment/deployment-guide/service-discovery).

- Used for: Runtime component communication, service discovery
- Specified in:
`.spec.services.<ServiceName>.dynamoNamespace`

field - Example:
`my-llm`

,`production-model`

,`dynamo-dev`


These are independent. A single Kubernetes namespace can host multiple Dynamo namespaces, and vice versa.

## Prerequisites

Before you begin, ensure you have the following tools installed:

Verify your installation:

For detailed installation instructions, see the [Prerequisites section](https://docs.nvidia.com/dynamo/v1.1.0/kubernetes-deployment/deployment-guide/detailed-installation-guide#prerequisites) in the Installation Guide.

## Pre-deployment Checks

Before deploying the platform, run the pre-deployment checks to ensure the cluster is ready:

This validates kubectl connectivity, StorageClass configuration, and GPU availability. See [pre-deployment checks](https://github.com/ai-dynamo/dynamo/tree/v1.1.0/deploy/pre-deployment/README.md) for more details.

## 1. Install Platform First

**v0.9.0 Helm Chart Issue:** The initial v0.9.0 `dynamo-platform`

Helm chart sets the operator image to v0.7.1 instead of v0.9.0. Use `RELEASE_VERSION=0.9.0-post1`

or add `--set dynamo-operator.controllerManager.manager.image.tag=0.9.0`

to your helm install command.

**For Shared/Multi-Tenant Clusters:**


DEPRECATED:Namespace-restricted mode (`namespaceRestriction.enabled=true`

) is deprecated and will be removed in a future release. Use cluster-wide mode (the default) instead.

For more details or customization options (including multinode deployments), see ** Installation Guide for Dynamo Kubernetes Platform**.

## 2. Choose Your Backend

Each backend has deployment examples and configuration options:

## 3. Deploy Your First Model

Follow the ** Deploying Your First Model** guide for a complete end-to-end
walkthrough using

`DynamoGraphDeploymentRequest`

(DGDR) — Dynamo’s recommended path that
handles profiling and configuration automatically.The tutorial deploys `Qwen/Qwen3-0.6B`

with vLLM and walks you through every step: creating
the DGDR, watching the profiling lifecycle, and sending your first inference request.

For SLA-based autoscaling, see [SLA Planner Guide](https://docs.nvidia.com/dynamo/v1.1.0/components/planner/planner-guide).

## Understanding Dynamo’s Custom Resources

Dynamo provides two main Kubernetes Custom Resources for deploying models:

### DynamoGraphDeploymentRequest (DGDR) - Simplified SLA-Driven Configuration

The **recommended approach** for generating optimal configurations. DGDR provides a high-level interface where you specify:

- Model name and backend framework
- SLA targets (latency requirements)
- GPU type (optional)

Dynamo automatically handles profiling and generates an optimized DGD spec in the status. Perfect for:

- SLA-driven configuration generation
- Automated resource optimization
- Users who want simplicity over control

**Note**: DGDR generates a DGD spec which you can then use to deploy.

### DynamoGraphDeployment (DGD) - Direct Configuration

A lower-level interface that defines your complete inference pipeline:

- Model configuration
- Resource allocation (GPUs, memory)
- Scaling policies
- Frontend/backend connections

Use this when you need fine-grained control or have already completed profiling.

Refer to the [API Reference and Documentation](https://docs.nvidia.com/dynamo/v1.1.0/additional-resources/api-reference-k-8-s) for more details.

## 📖 API Reference & Documentation

For detailed technical specifications of Dynamo’s Kubernetes resources:

- Complete CRD field specifications for all Dynamo resources[API Reference](https://docs.nvidia.com/dynamo/v1.1.0/additional-resources/api-reference-k-8-s)- Step-by-step deployment creation with DynamoGraphDeployment[Create Deployment](https://docs.nvidia.com/dynamo/v1.1.0/additional-resources/creating-deployments)- Dynamo operator configuration and management[Operator Guide](https://docs.nvidia.com/dynamo/v1.1.0/kubernetes-deployment/deployment-guide/dynamo-operator)

### Choosing Your Architecture Pattern

When creating a deployment, select the architecture pattern that best fits your use case:

**Development / Testing**- Use`agg.yaml`

as the base configuration**Production with Load Balancing**- Use`agg_router.yaml`

to enable scalable, load-balanced inference**High Performance / Disaggregated**- Use`disagg_router.yaml`

for maximum throughput and modular scalability

### Frontend and Worker Components

You can run the Frontend on one machine (e.g., a CPU node) and workers on different machines (GPU nodes). The Frontend serves as a framework-agnostic HTTP entry point that:

- Provides OpenAI-compatible
`/v1/chat/completions`

endpoint - Auto-discovers backend workers via
[service discovery](https://docs.nvidia.com/dynamo/v1.1.0/kubernetes-deployment/deployment-guide/service-discovery)(Kubernetes-native by default) - Routes requests and handles load balancing
- Validates and preprocesses requests

### Customizing Your Deployment

Example structure:

Worker command examples per backend:

Key customization points include:

**Model Configuration**: Specify model in the args command**Resource Allocation**: Configure GPU requirements under`resources.limits`

**Scaling**: Set`replicas`

for number of worker instances**Routing Mode**: Enable KV-cache routing by setting`DYN_ROUTER_MODE=kv`

in Frontend envs**Worker Specialization**: Add`--disaggregation-mode prefill`

flag for disaggregated prefill workers

## Additional Resources

- Complete working examples[Examples](https://github.com/ai-dynamo/dynamo/tree/v1.1.0/examples/README.md)- Build your own CRDs[Create Custom Deployments](https://docs.nvidia.com/dynamo/v1.1.0/additional-resources/creating-deployments)- Deploy LoRA adapters and manage models[Managing Models with DynamoModel](https://docs.nvidia.com/dynamo/v1.1.0/kubernetes-deployment/deployment-guide/managing-models-with-dynamo-model)- How the platform works[Operator Documentation](https://docs.nvidia.com/dynamo/v1.1.0/kubernetes-deployment/deployment-guide/dynamo-operator)- Discovery backends and configuration[Service Discovery](https://docs.nvidia.com/dynamo/v1.1.0/kubernetes-deployment/deployment-guide/service-discovery)- For advanced users[Helm Charts](https://github.com/ai-dynamo/dynamo/tree/v1.1.0/deploy/helm/README.md)- Fast pod startup with checkpoint/restore[Snapshot](https://docs.nvidia.com/dynamo/v1.1.0/kubernetes-deployment/deployment-guide/snapshot)- For advanced users[GitOps Deployment with FluxCD](https://docs.nvidia.com/dynamo/v1.1.0/additional-resources/flux-cd)- For logging setup[Logging](https://docs.nvidia.com/dynamo/v1.1.0/kubernetes-deployment/observability-k-8-s/logging)- For multinode deployment[Multinode Deployment](https://docs.nvidia.com/dynamo/v1.1.0/kubernetes-deployment/multinode/multinode-deployments)- Configure topology-aware workload placement[Topology Aware Scheduling](https://docs.nvidia.com/dynamo/v1.1.0/kubernetes-deployment/multinode/topology-aware-scheduling)- For grove details and custom installation[Grove](https://docs.nvidia.com/dynamo/v1.1.0/kubernetes-deployment/multinode/grove)- For monitoring setup[Monitoring](https://docs.nvidia.com/dynamo/v1.1.0/kubernetes-deployment/observability-k-8-s/metrics)- For model caching with Fluid[Model Caching with Fluid](https://docs.nvidia.com/dynamo/v1.1.0/additional-resources/model-caching-with-fluid)