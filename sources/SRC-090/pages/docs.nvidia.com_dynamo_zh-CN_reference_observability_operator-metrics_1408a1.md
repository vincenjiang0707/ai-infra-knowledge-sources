source: https://docs.nvidia.com/dynamo/zh-CN/reference/observability/operator-metrics
lastmod: 2026-09-23T23:30:39.914Z

# Operator Metrics

Kubernetes-only dynamo_operator_* metrics and the annotations and Helm values that enable metrics collection.

The Dynamo Operator exposes its own Prometheus metrics for controller reconciliation, webhook validation, and resource inventory. These are **Kubernetes-scoped** — they exist only where the operator runs, and are separate from the application metrics emitted by frontends and workers (see [Metrics Catalog](https://docs.nvidia.com/dynamo/reference/observability/metrics-catalog)). For enablement and dashboards (including the operator dashboard), see the [Kubernetes observability guide](https://docs.nvidia.com/dynamo/kubernetes/operations/observability).

All operator metrics use the `dynamo_operator`

prefix. Unlike application metrics (which use a PodMonitor), the operator is scraped via a ServiceMonitor created by the Helm chart.

## Reconciliation metrics

Track how efficiently controllers process `DynamoGraphDeployment`

, `DynamoComponentDeployment`

, `DynamoModel`

, `DynamoGraphDeploymentRequest`

, and `DynamoGraphDeploymentScalingAdapter`

resources.

Duration of reconciliation loops. Labeled by `resource_type`

, `namespace`

, and `result`

.

Total number of reconciliations. Labeled by `resource_type`

, `namespace`

, and `result`

.

Total reconciliation errors by type. Labeled by `resource_type`

, `namespace`

, and `error_type`

.

## Webhook metrics

Track performance and outcomes of admission webhook requests.

Duration of webhook validation requests. Labeled by `resource_type`

and `operation`

.

Total webhook admission requests. Labeled by `resource_type`

, `operation`

, and `result`

.

Total webhook denials with reasons. Labeled by `resource_type`

, `operation`

, and `reason`

.

## Resource inventory metrics

Current count of managed resources by state. Labeled by `resource_type`

, `namespace`

, and `status`

.

## Operator metric labels

These labels are specific to operator metrics and are distinct from the application [Metric Labels](https://docs.nvidia.com/dynamo/reference/observability/metric-labels).

The managed CRD: `DynamoGraphDeployment`

, `DynamoComponentDeployment`

, `DynamoModel`

, `DynamoGraphDeploymentRequest`

, or `DynamoGraphDeploymentScalingAdapter`

.

Target Kubernetes namespace of the resource.

Outcome of the operation. On reconcile metrics: `success`

, `error`

, `requeue`

. On webhook metrics: `allowed`

, `denied`

.

On `dynamo_operator_reconcile_errors_total`

— the failure category.

On webhook metrics — the admission operation.

Allowed values: CREATE UPDATE DELETEOn `dynamo_operator_webhook_denials_total`

— the validation failure reason, e.g. `immutable_field_changed`

, `invalid_config`

.

On `dynamo_operator_resources_total`

— resource state derived from each CRD’s status. Common values: `ready`

, `not_ready`

, `unknown`

(DCD, DM, DGDSA). DGD uses `pending`

, `successful`

, `failed`

from `.status.state`

. DGDR uses `Pending`

, `Profiling`

, `Ready`

, `Deploying`

, `Deployed`

, `Failed`

from `.status.phase`

.

## Kubernetes enablement knobs

Metrics collection on Kubernetes is controlled by CRD annotations and Helm values — **not** environment variables. These knobs govern whether application and operator metrics are scraped at all.

These fields also appear in the CRD and Helm references. They are reproduced here so the observability enablement path is documented in one place. For the operator’s full Helm value set, see the [Dynamo Operator guide](https://docs.nvidia.com/dynamo/knowledge-base/kubernetes/kubernetes-operator/dynamo-operator).

Pod label the operator adds to every managed pod so the PodMonitor discovers and scrapes it. Present automatically; you do not set it by hand.

Annotation on a `DynamoGraphDeployment`

to opt a deployment **out** of metrics collection. Set to `false`

to disable scraping for that deployment.

Helm value controlling whether the operator’s metrics Service and ServiceMonitor are created. Set to `false`

to disable operator metrics collection.

Helm value pointing the operator at your Prometheus endpoint, e.g. `http://prometheus-kube-prometheus-prometheus.monitoring.svc.cluster.local:9090`

.

To disable operator metrics collection:

To opt a single deployment out of application metrics:

## Related

[Kubernetes observability guide](https://docs.nvidia.com/dynamo/kubernetes/operations/observability)— signal enablement and the operator Grafana dashboard.[Kubernetes Metrics guide](https://docs.nvidia.com/dynamo/kubernetes/operations/observability)— PodMonitor and Prometheus walkthrough for application metrics.[Metrics Catalog](https://docs.nvidia.com/dynamo/reference/observability/metrics-catalog)— application`dynamo_*`

metrics.[Metric Labels](https://docs.nvidia.com/dynamo/reference/observability/metric-labels)— application metric label dimensions.