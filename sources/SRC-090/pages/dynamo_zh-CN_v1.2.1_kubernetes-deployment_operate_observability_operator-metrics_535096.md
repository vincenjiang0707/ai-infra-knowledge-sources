source: https://docs.nvidia.com/dynamo/zh-CN/v1.2.1/kubernetes-deployment/operate/observability/operator-metrics
lastmod: 2026-09-23T23:30:39.914Z

# Operator Metrics

## Overview

The Dynamo Operator exposes Prometheus metrics for monitoring its own health and performance. These metrics are separate from application metrics (frontend/worker) and provide visibility into:

**Controller Reconciliation**: How efficiently controllers process DynamoGraphDeployments, DynamoComponentDeployments, and DynamoModels**Webhook Validation**: Performance and outcomes of admission webhook requests**Resource Inventory**: Current count of managed resources by state and namespace

## Prerequisites

The operator metrics feature requires the same monitoring infrastructure as application metrics. For detailed setup instructions, see the [Kubernetes Metrics Guide](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/operate/observability/metrics#prerequisites).

**Quick checklist:**

- ✅ kube-prometheus-stack installed (for ServiceMonitor support)
- ✅ Prometheus and Grafana running
- ✅ Dynamo Operator installed via Helm

## Metrics Collection

### ServiceMonitor

Operator metrics are automatically collected via a ServiceMonitor, which is created by the Helm chart when `metricsService.enabled: true`

(default).

**Unlike application metrics** (which use PodMonitor), the operator uses ServiceMonitor and requires no manual RBAC configuration. The operator’s metrics endpoint uses controller-runtime’s built-in `WithAuthenticationAndAuthorization`

filter for secure serving.

To verify the ServiceMonitor is created:

### Disabling Metrics Collection

To disable operator metrics collection:

## Available Metrics

All metrics use the `dynamo_operator`

namespace prefix.

### Reconciliation Metrics

**Labels:**

`resource_type`

:`DynamoGraphDeployment`

,`DynamoComponentDeployment`

,`DynamoModel`

,`DynamoGraphDeploymentRequest`

,`DynamoGraphDeploymentScalingAdapter`

`namespace`

: Target namespace of the resource`result`

:`success`

,`error`

,`requeue`

`error_type`

:`not_found`

,`already_exists`

,`conflict`

,`validation`

,`bad_request`

,`unauthorized`

,`forbidden`

,`timeout`

,`server_timeout`

,`unavailable`

,`rate_limited`

,`internal`


### Webhook Metrics

**Labels:**

`resource_type`

: Same as reconciliation metrics`operation`

:`CREATE`

,`UPDATE`

,`DELETE`

`result`

:`allowed`

,`denied`

`reason`

: Validation failure reason (e.g.,`immutable_field_changed`

,`invalid_config`

)

### Resource Inventory Metrics

**Labels:**

`resource_type`

:`DynamoGraphDeployment`

,`DynamoComponentDeployment`

,`DynamoModel`

,`DynamoGraphDeploymentRequest`

,`DynamoGraphDeploymentScalingAdapter`

`namespace`

: Resource namespace`status`

: Resource state derived from each CRD’s status. Common values:`"ready"`

- Resource is healthy and operational (DCD, DM, DGDSA)`"not_ready"`

- Resource exists but is not operational (DCD, DM, DGDSA)`"unknown"`

- State cannot be determined (default for empty status)- DGD uses:
`"pending"`

,`"successful"`

,`"failed"`

from`.status.state`

- DGDR uses:
`"Pending"`

,`"Profiling"`

,`"Ready"`

,`"Deploying"`

,`"Deployed"`

,`"Failed"`

from`.status.phase`



## Example Queries

### Reconciliation Performance

### Webhook Performance

### Resource Inventory

## Grafana Dashboard

A pre-built Grafana dashboard is available for visualizing operator metrics.

### Dashboard Sections

-
**Reconciliation Metrics**(3 panels)- Reconciliation rate by resource type and result
- P95 reconciliation duration
- Reconciliation errors by type

-
**Webhook Metrics**(3 panels)- Webhook request rate by operation
- P95 webhook duration
- Webhook denials by reason

-
**Resource Inventory**(2 panels)- Resource inventory timeline by state and namespace (filterable by resource type)
- Current resource count by state (filterable by resource type)

-
**Operational Health**(2 panels)- Reconciliation success rate gauges
- Webhook admission success rate gauges


### Deploying the Dashboard

The dashboard will automatically appear in Grafana (assuming you have the Grafana dashboard sidecar configured, which is included in kube-prometheus-stack).

### Finding the Dashboard

-
Port-forward to Grafana (if needed):

-
Log in to Grafana at

[http://localhost:3000](http://localhost:3000/) -
Navigate to

**Dashboards**→ Search for**“Dynamo Operator”**

### Dashboard Filters

The dashboard includes two filter variables:

**Namespace**: View metrics across all namespaces or filter by specific ones (multi-select)**Resource Type**: Filter all panels by resource type or select “All” to see aggregated metrics across all CRDs (single select)

When “All” is selected for Resource Type, all panels will show data for all five managed CRDs with resource_type labels for differentiation.

## Accessing Metrics Directly

For instructions on accessing Prometheus and Grafana, see the [Kubernetes Metrics Guide](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/operate/observability/metrics#viewing-the-metrics).

Once you have access to Prometheus, you can query operator metrics directly:

## Troubleshooting

### Metrics Not Appearing in Prometheus

-
**Check ServiceMonitor exists:** -
**Check ServiceMonitor is discovered by Prometheus:**- Go to Prometheus UI → Status → Targets
- Look for
`serviceMonitor/dynamo-system/dynamo-platform-dynamo-operator-operator`

- Should show state:
`UP`


-
**Check Prometheus selector configuration:**Ensure

`serviceMonitorSelectorNilUsesHelmValues: false`

was set during kube-prometheus-stack installation.

### Dashboard Not Appearing in Grafana

-
**Check ConfigMap is created:** -
**Check ConfigMap has the label:**Should return

`"1"`

-
**Check Grafana dashboard sidecar configuration:**The sidecar should be configured to watch for

`grafana_dashboard: "1"`

label. -
**Restart Grafana pod**to force dashboard refresh:

## Related Documentation

[Kubernetes Metrics Guide](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/operate/observability/metrics)- Application metrics for frontends and workers[Dynamo Operator Guide](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/start-here/dynamo-operator)- Operator architecture and deployment modes[Operator Webhooks](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/advanced-platform/webhooks)- Webhook validation details