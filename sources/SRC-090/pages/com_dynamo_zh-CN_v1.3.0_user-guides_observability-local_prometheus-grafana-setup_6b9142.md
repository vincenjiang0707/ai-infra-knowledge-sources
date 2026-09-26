source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/user-guides/observability-local/prometheus-grafana-setup
lastmod: 2026-09-23T23:30:39.914Z

Prometheus + Grafana Setup


Prometheus + Grafana Setup

Single-machine setup for collecting Dynamo metrics in Prometheus and visualizing them in Grafana for local development and demos.

## Overview

This guide shows how to set up Prometheus and Grafana for visualizing Dynamo metrics on a single machine for demo purposes.


**Components:**

**Prometheus Server**- Collects and stores metrics from Dynamo services**Grafana**- Provides dashboards by querying the Prometheus Server

**For metrics reference**, see [Metrics Documentation](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/observability-local/metrics).

## Environment Variables

## Getting Started Quickly

This is a single machine example.

### Start the Observability Stack

Start the observability stack (Prometheus, Grafana, Tempo, exporters). See [Observability Getting Started](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/observability-local#getting-started-quickly) for instructions and prerequisites.

### Start Dynamo Components

Start frontend and worker (a simple single GPU example):

After the workers are running, send a few test requests to populate metrics in the system:

After sending a few requests, the Prometheus Exposition Format text metrics are available at:

- Frontend:
`http://localhost:8000/metrics`

- Backend worker:
`http://localhost:8081/metrics`


**Note:** Labeled series (e.g., `...{model="..."}`

) only appear after the first matching request is served. See [Available Metrics](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/observability-local/metrics#available-metrics) for details.

### Access Web Interfaces

Once Dynamo components are running:

- Open
**Grafana**at`http://localhost:3000`

(username:`dynamo`

, password:`dynamo`

) - Click on
**Dashboards**in the left sidebar - Select
**Dynamo Dashboard**to view metrics and traces

Other interfaces:

**Prometheus**:`http://localhost:9090`

**Tempo**(tracing): Accessible through Grafana’s Explore view. See[Tracing Guide](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/observability-local/tracing)for details.

**Note:** If accessing from another machine, replace `localhost`

with the machine’s hostname or IP address, and ensure firewall rules allow access to these ports (3000, 9090).

## Configuration

### Prometheus

The Prometheus configuration is specified in [prometheus.yml](https://docs.nvidia.com/dynamo/v1.3.0/dev/observability/prometheus.yml). This file is set up to collect metrics from the metrics aggregation service endpoint.

Please be aware that you might need to modify the target settings to align with your specific host configuration and network environment.

After making changes to prometheus.yml, restart the Prometheus service. See [Observability Getting Started](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/observability-local#getting-started-quickly) for Docker Compose commands.

### Grafana

Grafana is pre-configured with:

- Prometheus datasource
- A set of sample dashboards under
`dev/observability/grafana_dashboards/`

(see below)

### Dashboards

#### Per-Model Dynamo Dashboard

The per-model dashboard at [dev/observability/grafana_dashboards/dynamo.json](https://docs.nvidia.com/dynamo/v1.3.0/dev/observability/grafana_dashboards/dynamo.json) is auto-provisioned with the observability stack.

Sections:

**Overview**- request KPIs (success rate, totals, latency averages).**Frontend**- request rates, latency quantiles, sequence-length distributions, cache hits.**KV Routing**- per-worker active blocks, hit rate, routing-overhead breakdown, KV cache events.**Workers**- per-worker request breakdown, request duration, component throughput.

Metric panels read the `dynamo_frontend_*`

, `dynamo_component_*`

, and `dynamo_router_*`

metric surfaces, filtered by the `${model}`

template variable.

The Kubernetes version is provisioned from [deploy/observability/grafana-dynamo-dashboard-configmap.yaml](https://docs.nvidia.com/dynamo/v1.3.0/deploy/observability/grafana-dynamo-dashboard-configmap.yaml).

### Troubleshooting

-
Verify services are running using

`docker compose ps`

-
Check logs using

`docker compose logs`

-
Check Prometheus targets at

`http://localhost:9090/targets`

to verify metric collection. -
If you encounter issues with stale data or configuration, stop services and wipe volumes using

`docker compose down -v`

then restart.

**Note:** The `-v`

flag removes named volumes (grafana-data, tempo-data), which will reset dashboards and stored metrics.

For specific Docker Compose commands, see [Observability Getting Started](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/observability-local#getting-started-quickly).

## Developer Guide

For detailed information on creating custom metrics in Dynamo components, see: