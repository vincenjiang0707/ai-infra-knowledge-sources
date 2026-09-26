source: https://docs.nvidia.com/dynamo/zh-CN/v1.2.1/user-guides/observability-local
lastmod: 2026-09-23T23:30:39.914Z

Observability (Local)


Observability (Local)

## Required environment variables

Set these on every Dynamo process (frontend, router, workers) for metrics, traces, and logs to flow:

Source of truth: `lib/runtime/src/logging.rs`

`setup_logging()`

.

Passing `--enable-metrics`

on an individual backend only exposes metrics *per backend*. The unified frontend metrics surface (scraped by Prometheus) requires `DYN_SYSTEM_PORT`

to be set on the frontend process as well — setting it on workers alone is not enough.

Prometheus metric families in Dynamo are registered lazily: each label set is created the first time it fires, so a freshly-started process shows empty metric families until the first relevant request. This is expected — an idle cluster does not mean scraping is broken.

## Getting Started Quickly

This is an example to get started quickly on a single machine.

### Prerequisites

Install these on your machine:

### Starting the Observability Stack

Dynamo provides a Docker Compose-based observability stack that includes Prometheus, Grafana, Tempo, Loki, an OpenTelemetry Collector, and various exporters for metrics, tracing, logging, and visualization.

From the Dynamo root directory:

For detailed setup instructions and configuration, see [Prometheus + Grafana Setup](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/observability-local/prometheus-grafana-setup).

## Observability Documentation

**Variables marked with † are shared across multiple observability systems.**

## Developer Guides

## Kubernetes

For Kubernetes-specific setup and configuration, see [docs/kubernetes/observability/](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/operate/observability/metrics).

**Operator Metrics**: The Dynamo Operator running in Kubernetes exposes its own set of metrics for monitoring controller reconciliation, webhook validation, and resource inventory. See the [Operator Metrics Guide](https://docs.nvidia.com/dynamo/v1.2.1/kubernetes-deployment/operate/observability/operator-metrics).

## Topology

This provides:

**Prometheus**on`http://localhost:9090`

- metrics collection and querying**Grafana**on`http://localhost:3000`

- visualization dashboards (username:`dynamo`

, password:`dynamo`

)**Tempo**on`http://localhost:3200`

- distributed tracing backend**Loki**on`http://localhost:3100`

- log aggregation backend**OpenTelemetry Collector**on`http://localhost:4317`

(gRPC) /`http://localhost:4318`

(HTTP) - receives OTLP signals and routes traces to Tempo and logs to Loki**DCGM Exporter**on`http://localhost:9401/metrics`

- GPU metrics**NATS Exporter**on`http://localhost:7777/metrics`

- NATS messaging metrics

### Service Relationship Diagram

The dcgm-exporter service in the Docker Compose network is configured to use port 9401 instead of the default port 9400. This adjustment is made to avoid port conflicts with other dcgm-exporter instances that may be running simultaneously. Such a configuration is typical in distributed systems like SLURM.

### Configuration Files

The following configuration files are located in the `dev/observability/`

directory:

[docker-compose.yml](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/deploy/docker-compose.yml): Defines NATS and etcd services[docker-observability.yml](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/deploy/docker-observability.yml): Defines Prometheus, Grafana, Tempo, and exporters[prometheus.yml](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/deploy/observability/prometheus.yml): Contains Prometheus scraping configuration[grafana-datasources.yml](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/deploy/observability/grafana-datasources.yml): Contains Grafana datasource configuration[otel-collector.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/deploy/observability/otel-collector.yaml): OpenTelemetry Collector configuration (routes traces to Tempo, logs to Loki)[loki.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/deploy/observability/loki.yaml): Loki log aggregation configuration[loki-datasource.yml](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/deploy/observability/loki-datasource.yml): Grafana Loki datasource with trace ID linking to Tempo[grafana_dashboards/dashboard-providers.yml](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/deploy/observability/grafana_dashboards/dashboard-providers.yml): Contains Grafana dashboard provider configuration[grafana_dashboards/dynamo.json](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/deploy/observability/grafana_dashboards/dynamo.json): Engine-agnostic per-model dashboard covering frontend, KV-router, and worker metrics. Filterable by`model`

. See the[per-model dashboard guide](https://docs.nvidia.com/dynamo/v1.2.1/user-guides/observability-local/prometheus-grafana-setup#per-model-dynamo-dashboard)for details.[grafana_dashboards/dcgm-metrics.json](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/deploy/observability/grafana_dashboards/dcgm-metrics.json): Contains Grafana dashboard configuration for DCGM GPU metrics[grafana_dashboards/kvbm.json](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/deploy/observability/grafana_dashboards/kvbm.json): Contains Grafana dashboard configuration for KVBM metrics