source: https://docs.nvidia.com/dynamo/dev/cli/installation/observability
lastmod: 2026-09-24T19:58:16.636Z

# Install Observability

Install Dynamo’s local observability stack to collect metrics, logs, and traces from a CLI deployment. The Docker Compose stack includes Prometheus, Grafana, Tempo, Loki, an OpenTelemetry Collector, and the NATS Prometheus exporter.

## Prerequisites

Install the following software:

Run the commands on this page from the root of the Dynamo repository.

## Install the Stack

### Start the Dynamo infrastructure

Start NATS and etcd. The observability stack joins the Docker network created by this command and collects metrics from both services.

The stack is now installed. Continue with [Observe a Local Deployment](https://docs.nvidia.com/dynamo/dev/cli/operations/observability)
to configure metrics, traces, and exported logs. For service ports and configuration files, see the
[Local Observability Stack Reference](https://docs.nvidia.com/dynamo/dev/reference/observability/local-stack).

## Stop the Stack

To stop the observability services without deleting stored data, run:

To delete the Grafana, Tempo, and Loki volumes as well, add `--volumes`

.