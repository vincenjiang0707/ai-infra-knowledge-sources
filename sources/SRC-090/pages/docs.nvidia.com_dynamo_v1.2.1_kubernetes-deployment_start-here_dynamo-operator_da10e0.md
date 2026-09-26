source: https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/start-here/dynamo-operator
lastmod: 2026-09-24T19:58:16.636Z

# Dynamo Operator

## Overview

Dynamo operator is a Kubernetes operator that simplifies the deployment, configuration, and lifecycle management of DynamoGraphs. It automates the reconciliation of custom resources to ensure your desired state is always achieved. This operator is ideal for users who want to manage complex deployments using declarative YAML definitions and Kubernetes-native tooling.

## Architecture

-
**Operator Deployment:**Deployed as a Kubernetes`Deployment`

in a specific namespace. -
**Controllers:**`DynamoGraphDeploymentController`

: Watches`DynamoGraphDeployment`

CRs and orchestrates graph deployments.`DynamoComponentDeploymentController`

: Watches`DynamoComponentDeployment`

CRs and handles individual component deployments.`DynamoGraphDeploymentRequestController`

: Watches`DynamoGraphDeploymentRequest`

CRs and runs the profiling/generation flow that produces a`DynamoGraphDeployment`

.`DynamoGraphDeploymentScalingAdapterController`

: Watches scaling adapter CRs used by external autoscalers and Planner-driven scaling flows.`DynamoModelController`

: Watches`DynamoModel`

CRs and manages model lifecycle (e.g., loading LoRA adapters).`DynamoCheckpointController`

: Watches`DynamoCheckpoint`

CRs for GPU worker checkpoint/restore workflows.

-
**Workflow:**- A custom resource is created by the user or API server.
- The corresponding controller detects the change and runs reconciliation.
- Kubernetes resources (Deployments, Services, etc.) are created or updated to match the CR spec.
- Status fields are updated to reflect the current state.


## Deployment Modes

The Dynamo operator supports three deployment modes to accommodate different cluster environments and use cases:

### 1. Cluster-Wide Mode (Default, Recommended)

The operator monitors and manages DynamoGraph resources across **all namespaces** in the cluster.

**When to Use:**

- You have full cluster admin access
- You want centralized management of all Dynamo workloads
- Standard production deployment on a dedicated cluster

### 2. Namespace-Scoped Mode (DEPRECATED)


DEPRECATED:Namespace-scoped mode (`namespaceRestriction.enabled=true`

) is deprecated and will be removed in a future release. Use cluster-wide mode instead. Do not use this for new deployments.

The operator monitors and manages DynamoGraph resources **only in a specific namespace**. A lease marker is created to signal the operator’s presence to any cluster-wide operators.

**When to Use:**

- You’re on a shared/multi-tenant cluster
- You only have namespace-level permissions
- You want to test a new operator version in isolation
- You need to avoid conflicts with other operators

**Installation:**

### 3. Hybrid Mode (DEPRECATED)


DEPRECATED:Hybrid mode relies on namespace-scoped operators, which are deprecated and will be removed in a future release. Use a single cluster-wide operator instead.

A **cluster-wide operator** manages most namespaces, while **one or more namespace-scoped operators** run in specific namespaces (e.g., for testing new versions). The cluster-wide operator automatically detects and excludes namespaces with namespace-scoped operators using lease markers.

**When to Use:**

- Running production workloads with a stable operator version
- Testing new operator versions in isolated namespaces without affecting production
- Gradual rollout of operator updates
- Development/staging environments on production clusters

**How It Works:**

- Namespace-scoped operator creates a lease named
`dynamo-operator-namespace-scope`

in its namespace - Cluster-wide operator watches for these lease markers across all namespaces
- Cluster-wide operator automatically excludes any namespace with a lease marker
- If namespace-scoped operator stops, its lease expires (TTL: 30s by default)
- Cluster-wide operator automatically resumes managing that namespace

**Setup Example:**

**Observability:**

## Custom Resource Definitions (CRDs)

Dynamo installs the following Custom Resources. The main deployment path is:
create or generate a `DynamoGraphDeployment`

, then let the operator create the
lower-level resources that run it.

Advanced and operator-owned resources:

`DynamoGraphDeploymentScalingAdapter`

: scaling interface used by Planner or external autoscalers to adjust component replicas.`DynamoWorkerMetadata`

: discovery metadata written for worker pods.

For the complete technical API reference for Dynamo Custom Resource Definitions, see:

For user-focused workflows, see:

for DGD, DCD, DGDR, and recipes[Deployment Overview](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/deploy-models/model-deployment-guide)for deploy-by-intent generated deployments[DGDR Reference](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/deploy-models/dgdr-reference)[Managing Models with DynamoModel Guide](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/deploy-models/managing-models-with-dynamo-model)for[Snapshotting GPU Workers](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/advanced-platform/snapshot)`DynamoCheckpoint`


## Webhooks

The Dynamo Operator uses **Kubernetes admission webhooks** for real-time validation and mutation of custom resources before they are persisted to the cluster. Webhooks are a required component of the operator and ensure that invalid configurations are rejected immediately at the API server level.

**Key Features:**

- ✅ Shared certificate infrastructure across all webhook types
- ✅ Automatic certificate generation and rotation (default, all environments)
- ✅ cert-manager integration (optional, for custom PKI)
- ✅ Immutability enforcement for critical fields

For complete documentation on webhooks, certificate management, and troubleshooting, see:

## Observability

The Dynamo Operator provides comprehensive observability through Prometheus metrics and Grafana dashboards. This allows you to monitor:

**Controller Performance**: Reconciliation loop duration, success rates, and error rates by resource type**Webhook Activity**: Validation performance, admission rates, and denial patterns**Resource Inventory**: Current count of managed resources by state and namespace**Operational Health**: Success rates and health indicators for controllers and webhooks

### Metrics Collection

Metrics are automatically exposed on the operator’s `/metrics`

endpoint (port 8443 by default) and collected by Prometheus via a ServiceMonitor. The ServiceMonitor is automatically created when you install the operator via Helm (controlled by `metricsService.enabled`

, which defaults to `true`

).

### Grafana Dashboard

A pre-built Grafana dashboard is available for visualizing operator metrics. The dashboard includes:

**Reconciliation Metrics**: Rate, duration (P95), and errors by resource type**Webhook Metrics**: Request rate, duration (P95), and denials by resource type and operation**Resource Inventory**: Count of DynamoGraphDeployments by state and namespace**Operational Health**: Success rate gauges for controllers and webhooks

For complete setup instructions and metrics reference, see:

## Installation

### Quick Install with Helm


Note:Namespace-scoped and hybrid deployment modes are deprecated. Use cluster-wide mode for all new deployments. See[Deployment Modes]above if you need backward-compatible configurations.

### Building from Source

For detailed installation options, see the [Installation Guide](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/start-here/installation-guide)

## Development

**Code Structure:**

The operator is built using Kubebuilder and the operator-sdk, with the following structure:

`controllers/`

: Reconciliation logic`api/v1alpha1/`

: CRD types`config/`

: Manifests and Helm charts