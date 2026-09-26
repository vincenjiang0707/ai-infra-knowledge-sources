source: https://docs.nvidia.com/dynamo/zh-CN/v-0-8-1/kubernetes-deployment/deployment-guide/kubernetes-quickstart
lastmod: 2026-09-23T23:30:39.914Z

# Deploying Dynamo on Kubernetes

High-level guide to Dynamo Kubernetes deployments. Start here, then dive into specific guides.

## Important Terminology

**Kubernetes Namespace**: The K8s namespace where your DynamoGraphDeployment resource is created.

- Used for: Resource isolation, RBAC, organizing deployments
- Example:
`dynamo-system`

,`dynamo-cloud`

,`team-a-namespace`


**Dynamo Namespace**: The logical namespace used by Dynamo components for [service discovery](https://docs.nvidia.com/dynamo/v-0-8-1/additional-resources/advanced-kubernetes/service-discovery).

- Used for: Runtime component communication, service discovery
- Specified in:
`.spec.services.<ServiceName>.dynamoNamespace`

field - Example:
`my-llm`

,`production-model`

,`dynamo-dev`


These are independent. A single Kubernetes namespace can host multiple Dynamo namespaces, and vice versa.

## Pre-deployment Checks

Before deploying the platform, it is recommended to run the pre-deployment checks to ensure the cluster is ready for deployment. Please refer to the [pre-deployment checks](https://github.com/ai-dynamo/dynamo/blob/v0.8.1/deploy/cloud/pre-deployment/README.md) for more details.

## 1. Install Platform First

**For Shared/Multi-Tenant Clusters:**

If your cluster has namespace-restricted Dynamo operators, add this flag to step 3:

For more details or customization options (including multinode deployments), see ** Installation Guide for Dynamo Kubernetes Platform**.

## 2. Choose Your Backend

Each backend has deployment examples and configuration options:

## 3. Deploy Your First Model

For SLA-based autoscaling, see [SLA Planner Quick Start Guide](https://docs.nvidia.com/dynamo/v-0-8-1/components/planner/sla-planner-quick-start).

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

Refer to the [API Reference and Documentation](https://docs.nvidia.com/dynamo/v-0-8-1/additional-resources/advanced-kubernetes/api-reference) for more details.

## 📖 API Reference & Documentation

For detailed technical specifications of Dynamo’s Kubernetes resources:

- Complete CRD field specifications for all Dynamo resources[API Reference](https://docs.nvidia.com/dynamo/v-0-8-1/additional-resources/advanced-kubernetes/api-reference)- Step-by-step deployment creation with DynamoGraphDeployment[Create Deployment](https://docs.nvidia.com/dynamo/v-0-8-1/additional-resources/advanced-kubernetes/create-deployment)- Dynamo operator configuration and management[Operator Guide](https://docs.nvidia.com/dynamo/v-0-8-1/kubernetes-deployment/deployment-guide/dynamo-operator)

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
[service discovery](https://docs.nvidia.com/dynamo/v-0-8-1/additional-resources/advanced-kubernetes/service-discovery)(Kubernetes-native by default) - Routes requests and handles load balancing
- Validates and preprocesses requests

### Customizing Your Deployment

Example structure:

Worker command examples per backend:

Key customization points include:

**Model Configuration**: Specify model in the args command**Resource Allocation**: Configure GPU requirements under`resources.limits`

**Scaling**: Set`replicas`

for number of worker instances**Routing Mode**: Enable KV-cache routing by setting`DYN_ROUTER_MODE=kv`

in Frontend envs**Worker Specialization**: Add`--is-prefill-worker`

flag for disaggregated prefill workers

## Additional Resources

- Complete working examples[Examples](https://github.com/ai-dynamo/dynamo/blob/v0.8.1/examples/README.md)- Build your own CRDs[Create Custom Deployments](https://docs.nvidia.com/dynamo/v-0-8-1/additional-resources/advanced-kubernetes/create-deployment)- Deploy LoRA adapters and manage models[Managing Models with DynamoModel](https://docs.nvidia.com/dynamo/v-0-8-1/kubernetes-deployment/deployment-guide/managing-models-with-dynamo-model)- How the platform works[Operator Documentation](https://docs.nvidia.com/dynamo/v-0-8-1/kubernetes-deployment/deployment-guide/dynamo-operator)- Discovery backends and configuration[Service Discovery](https://docs.nvidia.com/dynamo/v-0-8-1/additional-resources/advanced-kubernetes/service-discovery)- For advanced users[Helm Charts](https://github.com/ai-dynamo/dynamo/blob/v0.8.1/deploy/helm/README.md)- For advanced users[GitOps Deployment with FluxCD](https://docs.nvidia.com/dynamo/v-0-8-1/additional-resources/advanced-kubernetes/flux-cd)- For logging setup[Logging](https://docs.nvidia.com/dynamo/v-0-8-1/kubernetes-deployment/observability-k-8-s/logging)- For multinode deployment[Multinode Deployment](https://docs.nvidia.com/dynamo/v-0-8-1/kubernetes-deployment/multinode/multinode-deployments)- For grove details and custom installation[Grove](https://docs.nvidia.com/dynamo/v-0-8-1/kubernetes-deployment/multinode/grove)- For monitoring setup[Monitoring](https://docs.nvidia.com/dynamo/v-0-8-1/kubernetes-deployment/observability-k-8-s/metrics)- For model caching with Fluid[Model Caching with Fluid](https://docs.nvidia.com/dynamo/v-0-8-1/additional-resources/advanced-kubernetes/model-caching-with-fluid)