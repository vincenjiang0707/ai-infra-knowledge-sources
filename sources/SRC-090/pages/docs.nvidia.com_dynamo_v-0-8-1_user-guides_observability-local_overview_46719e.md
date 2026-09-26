source: https://docs.nvidia.com/dynamo/v-0-8-1/user-guides/observability-local/overview
lastmod: 2026-09-24T19:58:16.636Z

# Dynamo Observability

## Getting Started Quickly

This is an example to get started quickly on a single machine.

### Prerequisites

Install these on your machine:

### Starting the Observability Stack

Dynamo provides a Docker Compose-based observability stack that includes Prometheus, Grafana, Tempo, and various exporters for metrics, tracing, and visualization.

From the Dynamo root directory:

For detailed setup instructions and configuration, see [Prometheus + Grafana Setup](https://docs.nvidia.com/dynamo/v-0-8-1/user-guides/observability-local/prometheus-grafana-setup).

## Observability Documentations

**Variables marked with † are shared across multiple observability systems.**

## Developer Guides

## Kubernetes

For Kubernetes-specific setup and configuration, see [Kubernetes Observability](https://docs.nvidia.com/dynamo/v-0-8-1/kubernetes-deployment/observability-k-8-s/metrics).

## Topology

This provides:

**Prometheus**on`http://localhost:9090`

- metrics collection and querying**Grafana**on`http://localhost:3000`

- visualization dashboards (username:`dynamo`

, password:`dynamo`

)**Tempo**on`http://localhost:3200`

- distributed tracing backend**DCGM Exporter**on`http://localhost:9401/metrics`

- GPU metrics**NATS Exporter**on`http://localhost:7777/metrics`

- NATS messaging metrics

### Service Relationship Diagram

The dcgm-exporter service in the Docker Compose network is configured to use port 9401 instead of the default port 9400. This adjustment is made to avoid port conflicts with other dcgm-exporter instances that may be running simultaneously. Such a configuration is typical in distributed systems like SLURM.

### Configuration Files

The following configuration files are located in the `deploy/observability/`

directory:

[docker-compose.yml](https://github.com/ai-dynamo/dynamo/blob/v0.8.1/deploy/docker-compose.yml): Defines NATS and etcd services[docker-observability.yml](https://github.com/ai-dynamo/dynamo/blob/v0.8.1/deploy/docker-observability.yml): Defines Prometheus, Grafana, Tempo, and exporters[prometheus.yml](https://github.com/ai-dynamo/dynamo/blob/v0.8.1/deploy/observability/prometheus.yml): Contains Prometheus scraping configuration[grafana-datasources.yml](https://github.com/ai-dynamo/dynamo/blob/v0.8.1/deploy/observability/grafana-datasources.yml): Contains Grafana datasource configuration[grafana_dashboards/dashboard-providers.yml](https://github.com/ai-dynamo/dynamo/blob/v0.8.1/deploy/observability/grafana_dashboards/dashboard-providers.yml): Contains Grafana dashboard provider configuration[grafana_dashboards/dynamo.json](https://github.com/ai-dynamo/dynamo/blob/v0.8.1/deploy/observability/grafana_dashboards/dynamo.json): A general Dynamo Dashboard for both SW and HW metrics[grafana_dashboards/dcgm-metrics.json](https://github.com/ai-dynamo/dynamo/blob/v0.8.1/deploy/observability/grafana_dashboards/dcgm-metrics.json): Contains Grafana dashboard configuration for DCGM GPU metrics[grafana_dashboards/kvbm.json](https://github.com/ai-dynamo/dynamo/blob/v0.8.1/deploy/observability/grafana_dashboards/kvbm.json): Contains Grafana dashboard configuration for KVBM metrics