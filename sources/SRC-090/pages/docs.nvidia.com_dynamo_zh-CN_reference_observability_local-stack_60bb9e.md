source: https://docs.nvidia.com/dynamo/zh-CN/reference/observability/local-stack
lastmod: 2026-09-23T23:30:39.914Z

# Local Observability Stack Reference

The local observability stack combines metrics, logs, and traces from CLI deployments. Install it
with the [Observability installation guide](https://docs.nvidia.com/dynamo/cli/installation/observability.mdx), then use
[Observe a Local Deployment](https://docs.nvidia.com/dynamo/cli/operations/observability) to configure Dynamo
processes.

## Services and Ports

Grafana uses `dynamo`

for both the default username and password. The DCGM exporter uses port `9401`

instead of its default port `9400`

to avoid conflicts with another exporter on the host.

## Signal Flow

Prometheus scrapes Dynamo metrics directly. Dynamo sends traces and exported logs to the OpenTelemetry Collector, which routes them to Tempo and Loki. Grafana queries all three backends.

## Configuration Files

## Optional Profiles

The `nvidia`

profile starts the DCGM exporter for NVIDIA GPU metrics. The `resource-monitor`

profile
starts a second Prometheus instance on port `9091`

for high-frequency local resource monitoring. See
the [Local Resource Monitor Reference](https://docs.nvidia.com/dynamo/reference/observability/local-resource-monitor-local) for its configuration and usage.