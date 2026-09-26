source: https://docs.nvidia.com/dynamo/zh-CN/knowledge-base/kubernetes/kubernetes-operator/dynamo-operator
lastmod: 2026-09-23T23:30:39.914Z

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

The Dynamo operator has one supported production mode and one development/test mode.

### Cluster-Wide Mode

The operator monitors and manages DynamoGraph resources across **all namespaces** in the cluster.
It owns the cluster-wide Custom Resource Definitions (CRDs), conversion webhook, and conversion
certificate authority (CA). Deploy exactly one cluster-wide operator per cluster.

**When to Use:**

- You have full cluster admin access
- You want centralized management of all Dynamo workloads
- Standard production deployment on a dedicated cluster

### Namespace-Restricted Mode

A namespace-restricted operator reconciles, validates, and mutates resources only in its target namespace. It creates a Lease that makes the cluster-wide operator skip reconciliation and admission in that namespace. The namespace-restricted operator serves its own admission webhooks using its local feature settings.

Use this mode to test controller changes or feature settings in one namespace on a development cluster. It is not a multi-tenancy boundary.

**How It Works:**

- The namespace-restricted operator creates a Lease named
`dynamo-operator-namespace-scope`

. - The cluster-wide operator watches these Leases and skips the claimed namespace.
- The namespace-restricted ValidatingWebhookConfiguration and MutatingWebhookConfiguration select only the target namespace.
- The namespace-restricted operator manages the TLS certificate and CA bundles for its own admission configurations.
- The cluster-wide operator remains the only owner of CRDs, conversion, and conversion CA bundles.

If the namespace-restricted Pod becomes unavailable, Lease expiration lets the cluster-wide operator resume reconciliation, but does not remove the namespace-restricted webhook configurations. Admission continues to target the unavailable Service. Recover the Pod to restore namespace-restricted admission, or uninstall the release to remove its webhook configurations. Cluster-wide admission resumes after the Lease is deleted or expires.

Set `dynamo-operator.upgradeCRD=false`

. Namespace-restricted operators use the CRDs installed and
updated by the cluster-wide operator.

Set `dynamo-operator.namespaceRestriction.targetNamespace`

when the target differs from the Helm
release namespace.

Install every operator Helm release in a separate namespace. Multiple Dynamo operator releases in the same Helm release namespace are not supported.

Run the same operator version in parallel whenever possible. The cluster-wide operator should be the same version or newer and must provide the newest APIs in the cluster. A newer namespaced controller can be used for development when it does not require CRD fields absent from the cluster-wide installation.

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

for creating a DGD from a recipe, template, or custom manifest[Model Deployment](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/introduction)for generating a DGD with DGDR, the Profiler, and optional Planner autoscaling[Auto Deployment](https://docs.nvidia.com/dynamo/kubernetes/auto-deployment/overview)for DGDR fields, lifecycle, and generated deployments[DGDR Reference](https://docs.nvidia.com/dynamo/reference/api/kubernetes/dynamo-graph-deployment-request)[Managing Models with DynamoModel Guide](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/managing-models-dynamo-model)for[Snapshotting GPU Workers](https://docs.nvidia.com/dynamo/kubernetes/operations/cold-start-optimizations/dynamo-snapshot)`DynamoCheckpoint`


### CRD Storage Migration

The cluster-wide Operator automatically migrates existing resources to the current Custom Resource
Definition (CRD) storage version. Migration requires no user action under normal circumstances. The
`v1alpha1`

API remains served during migration, so existing manifests, clients, and older Operator
versions continue to work through the conversion webhook.

To verify migration progress, inspect the CRD:

Migration is complete when the observed-generation annotation matches the CRD generation and
`status.storedVersions`

contains only the CRD’s current storage version. The Operator retries
transient failures. If these values do not converge, check the Operator and conversion webhook before
upgrading to a release that stops serving `v1alpha1`

.

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

Namespace-restricted mode is only for development and testing. Use cluster-wide mode for production deployments.

### Building from Source

For detailed installation options, see the [Installation Guide](https://docs.nvidia.com/dynamo/kubernetes/installation/install-dynamo)

## Development

**Code Structure:**

The operator is built using Kubebuilder and the operator-sdk, with the following structure:

`controllers/`

: Reconciliation logic`api/v1alpha1/`

: CRD types`config/`

: Manifests and Helm charts