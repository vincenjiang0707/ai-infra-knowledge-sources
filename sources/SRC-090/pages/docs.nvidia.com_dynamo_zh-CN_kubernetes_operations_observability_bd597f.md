source: https://docs.nvidia.com/dynamo/zh-CN/kubernetes/operations/observability
lastmod: 2026-09-24T19:58:16.636Z

# Observability

Dynamo provides four core signals for running deployments:

**Metrics**expose request, latency, routing, worker, cache, and operator measurements. Metrics are enabled by default, and the operator creates the resources required for Prometheus discovery.**Logs**record component events on standard output. Enable structured JSONL output when you need reliable filtering and request correlation.**Distributed traces**follow requests from the frontend through participating Dynamo components. Configure an OpenTelemetry Protocol (OTLP) collector endpoint to export them.**Health status**is available through`/live`

and`/health`

. The operator uses these signals for Kubernetes health probes.

The monitoring stack must already be installed. See [Install Observability](https://docs.nvidia.com/dynamo/kubernetes/installation/observability.md)
for the Prometheus, Grafana, DCGM exporter, Loki, and Alloy setup.

Use this page to:

[View metrics and dashboards](https://docs.nvidia.com/dynamo/kubernetes/operations/observability#view-metrics-and-dashboards)[Configure structured logs](https://docs.nvidia.com/dynamo/kubernetes/operations/observability#configure-structured-logs)[Export distributed traces and logs](https://docs.nvidia.com/dynamo/kubernetes/operations/observability#export-distributed-traces-and-logs)[Capture Forward Pass Metrics](https://docs.nvidia.com/dynamo/kubernetes/operations/observability#capture-forward-pass-metrics)[Check and customize health probes](https://docs.nvidia.com/dynamo/kubernetes/operations/observability#check-and-customize-health-probes)[Troubleshoot collection](https://docs.nvidia.com/dynamo/kubernetes/operations/observability#troubleshoot-collection)

For exact metric names, labels, variables, schemas, and endpoint responses, use the
[Observability Reference](https://docs.nvidia.com/dynamo/reference/observability/metrics-catalog).

## View Metrics and Dashboards

Application metrics are enabled by default. The operator creates a `PodMonitor`

and labels managed
pods for discovery, so a normal DynamoGraphDeployment (DGD) requires no metrics configuration.
Operator metrics use a separate `ServiceMonitor`

created by the Helm chart.

### Verify Prometheus discovery

Confirm that the application and operator monitors exist:

Then confirm the Dynamo targets are `UP`

in Prometheus. If Prometheus is not externally available,
port-forward it:

Open `http://localhost:9090/targets`

and find the Dynamo targets.

### Load the Dynamo dashboards

Apply the supplied dashboard ConfigMaps and the Loki data source:

Each dashboard ConfigMap carries the Grafana discovery label, so the Grafana sidecar imports it automatically.

### Open the dashboards

Retrieve the Grafana credentials and port-forward the service:

Open `http://localhost:3000`

. Under **Dashboards**, open the Dynamo application, operator, or logs
dashboard. The application dashboard includes frontend latency and request metrics, KV router and
worker metrics, GPU utilization, and pod resource usage.

### Query Dynamo metrics

Use the dashboard or Prometheus to inspect a Dynamo-specific signal:

See the [Metrics Catalog](https://docs.nvidia.com/dynamo/reference/observability/metrics-catalog),
[Metric Labels](https://docs.nvidia.com/dynamo/reference/observability/metric-labels), and
[Operator Metrics](https://docs.nvidia.com/dynamo/reference/observability/operator-metrics) for the complete lookup
information.

### Enable NIXL Telemetry

NIXL transfer metrics are optional and are populated during disaggregated serving or multimodal embedding transfers.

### Enable telemetry on the worker

Add `NIXL_TELEMETRY_ENABLE`

to each worker that should expose transfer metrics:

NIXL exposes these metrics on its telemetry port, which defaults to `19090`

. See
[Environment Variables](https://docs.nvidia.com/dynamo/reference/observability/environment-variables#system-and-metrics)
for the complete NIXL telemetry configuration.

To disable the default application metrics for an entire deployment, set the
`nvidia.com/enable-metrics: "false"`

annotation on the DGD.

## Configure Structured Logs

Dynamo writes logs to standard output by default. Configure JSONL output when Loki or another log backend needs structured fields for filtering and trace correlation.

### Enable JSONL logging

Set the logging variables at graph level to apply them to every component:

See [Logging](https://docs.nvidia.com/dynamo/reference/observability/logging) for the output fields and
[Environment Variables](https://docs.nvidia.com/dynamo/reference/observability/environment-variables#logging) for the
complete configuration.

## Export Distributed Traces and Logs

Dynamo exports distributed spans and structured log records over OTLP. This is separate from request trace capture, which records replay metadata and optional request payloads.

### Identify the collector endpoint

Choose an OTLP endpoint reachable from the Dynamo pods. The following example uses a collector named
`otel-collector`

in the `observability`

namespace:

The collector is responsible for routing traces and logs to the configured storage backends.

### Enable OTLP export

Add the OpenTelemetry settings to the DGD:

`OTEL_EXPORT_ENABLED`

is the master switch for distributed traces and exported logs. For
HTTP/protobuf, set `OTEL_EXPORTER_OTLP_PROTOCOL`

to `http/protobuf`

. Use signal-specific endpoints
only when traces and logs use different collectors.

### Generate and inspect a trace

Apply the updated DGD and send an inference request through the frontend. In your tracing backend, find the frontend root request span and its child spans from participating Dynamo components. Structured log events emitted inside the request can include the trace and span identifiers used for correlation.

See [Environment Variables](https://docs.nvidia.com/dynamo/reference/observability/environment-variables#opentelemetry-traces-and-logs)
for all export settings. For the internal signal flow, see
[Observability Architecture](https://docs.nvidia.com/dynamo/knowledge-base/concepts/observability-architecture).

## Capture Forward Pass Metrics

Forward Pass Metrics (FPM) tracing records backend scheduler telemetry to rotating gzip JSONL files. It is an opt-in diagnostic capture rather than a routine distributed trace.

### Prepare persistent storage

Create or select a persistent volume claim that can retain trace files across pod replacement. The
example below expects an existing PVC named `fpm-traces`

.

### Enable FPM tracing

Mount the PVC on each worker that should write a trace and set the output prefix inside the mount:

Replace `VllmWorker`

with every worker service that should write scheduler telemetry.

### Collect the trace files

Apply the updated DGD and run the workload you want to investigate. Dynamo writes a separate
producer-specific file sequence for each worker. Retrieve the resulting `.jsonl.gz`

files from the
PVC for analysis.

Graceful shutdown flushes accepted records, but node loss, forced termination, queue pressure, and transport loss can create gaps. Treat these files as diagnostic data, not as a durable event log or replay input.

See [Forward Pass Metrics Traces](https://docs.nvidia.com/dynamo/reference/observability/forward-pass-metrics-traces) for
supported topologies, capture modes, rotation, retention, and the record schema.

## Check and Customize Health Probes

Dynamo exposes `/live`

and `/health`

, and the operator configures Kubernetes startup, liveness, and
readiness probes that consume those endpoints. Most deployments should keep the operator defaults.
Override them only when model startup, failure-detection requirements, or a custom engine health
endpoint requires different behavior.

### Check pod readiness

List the pods for a DGD and inspect their readiness state:

A ready pod has passed the readiness probe configured by the operator.

### Review the operator defaults

The frontend uses an exec readiness probe that calls `/health`

. Workers use the system port, which
defaults to `9090`

:

The worker startup probe allows approximately two hours for model download and engine warm-up.
User-specified probes take precedence over these defaults. See the
[API Reference](https://docs.nvidia.com/dynamo/reference/api/kubernetes/full-api-reference) for defaults that vary by component type.

### Inspect a failing probe

Describe the pod and inspect recent events and container logs:

If startup is delayed by downloading model weights, prefer
[Model Caching](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/model-loading/model-caching) over extending the probe indefinitely.

### Override the probes

Set standard Kubernetes probes on the `main`

container in the component’s `podTemplate`

. This example
extends the startup window and allows several consecutive liveness failures:

For a startup budget, calculate `failureThreshold`

as the expected startup time in seconds divided by
`periodSeconds`

. Change paths or ports only when a custom engine exposes health differently.

Multinode deployments adjust probes by backend and node role. Review
[Multinode Deployments](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/multinode-deployments) before overriding probes on a
multinode worker.

See [Health Checks](https://docs.nvidia.com/dynamo/reference/observability/health-checks) for endpoint paths, responses,
status codes, and active worker checks.

## Troubleshoot Collection

### Metrics Do Not Appear in Prometheus

-
Confirm that the

`PodMonitor`

and`ServiceMonitor`

exist: -
Open the Prometheus targets page and confirm that the Dynamo targets are

`UP`

. -
Check the Prometheus selector configuration:


Prometheus metric families are registered lazily. A newly started or idle deployment can show empty families until the first relevant request or transfer occurs.

### Dashboard Does Not Appear in Grafana

-
Confirm that the dashboard ConfigMap carries the discovery label:

The command should return

`1`

. -
Confirm that the Grafana sidecar watches for the label:

-
Restart Grafana to force a refresh:


### Traces or Exported Logs Do Not Appear

- Confirm
`OTEL_EXPORT_ENABLED=true`

is applied to every participating component. - Confirm the collector service name, namespace, port, and protocol match the DGD configuration.
- Confirm the collector can route the signal to the selected backend.
- For exported logs, enable structured JSONL output and confirm that the log endpoint is configured; a logs endpoint does not fall back to a traces-only endpoint.