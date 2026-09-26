source: https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/autoscaling
lastmod: 2026-09-24T19:58:16.636Z

# Autoscaling

This guide explains how to configure autoscaling for DynamoGraphDeployment (DGD) services using the `sglang-agg`

example from `examples/backends/sglang/deploy/agg.yaml`

.

## Scale-to-Zero Limitation

Scale-to-zero is currently not fully supported for DGD worker components. The
`DynamoGraphDeploymentScalingAdapter`

(DGDSA) and operator accept a replica count of `0`

, but when
every worker for a model scales to zero, the frontend removes the model from `/v1/models`

because
no live `ModelDeploymentCard`

remains. Requests for the model return HTTP 404 and do not provide
a model-specific demand signal that Kubernetes Event-driven Autoscaling (KEDA) or Planner can use
to scale the workers up again. For request-driven autoscaling, keep at least one replica for each
required worker component by setting `minReplicas: 1`

for the Kubernetes Horizontal Pod
Autoscaler (HPA) or `minReplicaCount: 1`

for KEDA. Scaling back up from zero requires a manual
action or another external signal that does not depend on frontend model discovery.

## Example DGD

All examples in this guide use the following DGD:

**Key identifiers:**

**DGD name**:`sglang-agg`

**Namespace**:`default`

**Services**:`Frontend`

,`decode`

**dynamo_namespace label**:`default-sglang-agg`

(used for metric filtering)

## Overview

Dynamo provides flexible autoscaling through the `DynamoGraphDeploymentScalingAdapter`

(DGDSA) resource. To have the operator create a DGDSA for a service, follow the Enabling DGDSA for a Service section below. These adapters implement the Kubernetes [Scale subresource](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#scale-subresource), enabling integration with:


⚠️ Deprecation Notice: The`spec.services[X].autoscaling`

field in DGD isdeprecated and ignored. Use DGDSA with HPA, KEDA, or Planner instead. If you have existing DGDs with`autoscaling`

configured, you’ll see a warning. Remove the field to silence the warning.

## Architecture

**How it works:**

- You deploy a DGD with services (Frontend, decode)
- The operator auto-creates one DGDSA per service
- Autoscalers (KEDA, HPA, Planner) target the adapters via
`/scale`

subresource - Adapter controller syncs replica changes to the DGD
- DGD controller reconciles the underlying pods

## Viewing Scaling Adapters

After deploying the `sglang-agg`

DGD, verify the auto-created adapters:

## Replica Ownership Model

When DGDSA is enabled, it becomes the **source of truth** for replica counts. This follows the same pattern as Kubernetes Deployments owning ReplicaSets.

### How It Works

**DGDSA owns replicas**: Autoscalers (HPA, KEDA, Planner) update the DGDSA’s`spec.replicas`

**DGDSA syncs to DGD**: The DGDSA controller writes the replica count to the DGD’s service**Direct DGD edits blocked**: A validating webhook prevents users from directly editing`spec.services[X].replicas`

in the DGD**Controllers allowed**: Only authorized controllers (operator, Planner) can modify DGD replicas

### Manual Scaling with DGDSA Enabled

When DGDSA is enabled, use `kubectl scale`

on the adapter (not the DGD):

## Enabling DGDSA for a Service

By default, no DGDSA is created for services, allowing direct replica management via the DGD. To enable autoscaling via HPA, KEDA, or Planner, explicitly enable the scaling adapter:

In `nvidia.com/v1beta1`

, `scalingAdapter`

is a marker: including it — even as the empty object
`scalingAdapter: {}`

— creates the DGDSA. Omit the field to keep direct replica management.

**When to enable DGDSA:**

- You want to use HPA, KEDA, or Planner for autoscaling
- You want a clear separation between “desired scale” (adapter) and “deployment config” (DGD)
- You want protection against accidental direct replica edits

**When to keep DGDSA disabled (default):**

- You want simple, manual replica management
- You don’t need autoscaling for that service
- You prefer direct DGD edits over adapter-based scaling

## Autoscaling with Dynamo Planner

The Dynamo Planner is an LLM-aware autoscaler that optimizes scaling decisions based on inference-specific metrics like Time To First Token (TTFT), Inter-Token Latency (ITL), and KV cache utilization.

**When to use Planner:**

- You want LLM-optimized autoscaling out of the box
- You need coordinated scaling across prefill/decode services
- You want SLA-driven scaling (e.g., target TTFT < 500ms)

**How Planner works:**

Planner is deployed as a service component within your DGD. It:

- Queries Prometheus for frontend metrics (request rate, latency, etc.)
- Uses profiling data to predict optimal replica counts
- Scales prefill/decode workers to meet SLA targets

**Deployment:**

The recommended way to deploy Planner is via `DynamoGraphDeploymentRequest`

(DGDR). See the [SLA Planner Quick Start](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/planner/planner-guide) for complete instructions.

Example configurations with Planner:

`examples/backends/vllm/deploy/disagg_planner.yaml`

`examples/backends/sglang/deploy/disagg_planner.yaml`

`examples/backends/trtllm/deploy/disagg_planner.yaml`


For more details, see the [SLA Planner documentation](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/planner/planner-guide).

## Autoscaling with Kubernetes HPA

The Horizontal Pod Autoscaler (HPA) is Kubernetes’ native autoscaling solution.

**When to use HPA:**

- You have simple, predictable scaling requirements
- You want to use standard Kubernetes tooling
- You need CPU or memory-based scaling

For custom metrics (like TTFT or queue depth), consider using [KEDA](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/autoscaling#autoscaling-with-keda-recommended) instead - it’s simpler to configure.

### Basic HPA (CPU-based)

### HPA with Dynamo Metrics

Dynamo exports several metrics useful for autoscaling. These are available at the `/metrics`

endpoint on each frontend pod.


See also: For a complete list of Dynamo metrics, see the[Metrics Catalog]. For Kubernetes dashboards, see[Observability].

#### Available Dynamo Metrics

For the definitions of the `stage`

and `phase`

labels, see
[Metric Labels](https://docs.nvidia.com/dynamo/reference/observability/metric-labels#stage-values).

#### Metric Labels

Dynamo metrics include these labels for filtering:

When you have multiple DGDs in the same namespace, use `dynamo_namespace`

to filter metrics for a specific DGD.

#### Example: Scale Decode Service Based on TTFT

Using HPA with Prometheus Adapter requires configuring external metrics.

**Step 1: Configure Prometheus Adapter**

Add this to your Helm values file (e.g., `prometheus-adapter-values.yaml`

):

**Step 2: Install Prometheus Adapter**

**Step 3: Verify the metric is available**

**Step 4: Create the HPA**

**How it works:**

- Frontend pods export
`dynamo_frontend_time_to_first_token_seconds`

histogram - Prometheus Adapter calculates p95 TTFT per
`dynamo_namespace`

- HPA monitors this metric filtered by
`dynamo_namespace: "default-sglang-agg"`

- When TTFT p95 > 500ms, HPA scales up the
`sglang-agg-decode`

adapter - Adapter controller syncs the replica count to the DGD’s
`decode`

service - More decode workers are created, reducing TTFT

#### Example: Scale Based on Queue Depth

“Queue depth” here means the number of requests that have entered the frontend but haven’t yet received a first token — i.e. the sum of `dynamo_frontend_stage_requests`

across the `preprocess`

, `route`

, and `dispatch`

stages. This replaces the deprecated `dynamo_frontend_queued_requests`

gauge.

Add this rule to your `prometheus-adapter-values.yaml`

(alongside the TTFT rule):

Then create the HPA:

## Autoscaling with KEDA (Recommended)

KEDA (Kubernetes Event-driven Autoscaling) extends Kubernetes with event-driven autoscaling, supporting 50+ scalers including Prometheus.

**Advantages over HPA + Prometheus Adapter:**

- No Prometheus Adapter configuration needed
- PromQL queries are defined in the ScaledObject itself (declarative, per-deployment)
- Easy to update - just
`kubectl apply`

the ScaledObject - Supports multiple triggers per object

**When to use KEDA:**

- You want simpler configuration (no Prometheus Adapter to manage)
- You need event-driven scaling (e.g., queue depth, Kafka, etc.)
- You want event-driven scaling while retaining at least one replica for each required worker component

### Installing KEDA

If you have Prometheus Adapter installed, either uninstall it first (`helm uninstall prometheus-adapter -n monitoring`

) or install KEDA with `--set metricsServer.enabled=false`

to avoid API conflicts.

### Example: Scale Decode Based on TTFT

Using the `sglang-agg`

DGD from `examples/backends/sglang/deploy/agg.yaml`

:

Apply it:

### Verify KEDA Scaling

### Example: Scale Based on Queue Depth

### How KEDA Works

KEDA creates and manages an HPA under the hood:

## Mixed Autoscaling

For disaggregated deployments (prefill + decode), you can use different autoscaling strategies for different services:

## Manual Scaling

### With DGDSA Enabled

When DGDSA is enabled, scale via the adapter:

Verify the scaling:

If an autoscaler (KEDA, HPA, Planner) is managing the adapter, your change will be overwritten on the next evaluation cycle.

### With DGDSA Disabled (default)

If you’ve disabled the scaling adapter for a service, edit the DGD directly:

Or edit the YAML (no `scalingAdapter.enabled: true`

means direct edits are allowed):

## Best Practices

### 1. Choose One Autoscaler Per Service

Avoid configuring multiple autoscalers for the same service:

### 2. Use Appropriate Metrics

### 3. Configure Stabilization Windows

Prevent thrashing with appropriate stabilization:

### 4. Set Sensible Min/Max Replicas

Always configure minimum and maximum replicas in your HPA/KEDA. For request-driven autoscaling, set
the minimum to `1`

or higher for each required worker component because scale-to-zero is not fully
supported. Set a maximum to prevent unbounded scaling that exhausts cluster resources.

## Troubleshooting

### Adapters Not Created

### Scaling Not Working

### Metrics Not Available

If HPA/KEDA shows `<unknown>`

for metrics:

### Rapid Scaling Up and Down

If you see unstable scaling:

- Check if multiple autoscalers are targeting the same adapter
- Increase
`cooldownPeriod`

in KEDA ScaledObject - Increase
`stabilizationWindowSeconds`

in HPA behavior