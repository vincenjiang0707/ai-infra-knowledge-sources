source: https://docs.nvidia.com/dynamo/v1.1.1/kubernetes-deployment/observability-k-8-s/logging
lastmod: 2026-09-24T19:58:16.636Z

# Logging

This guide demonstrates how to set up logging for Dynamo in Kubernetes using Grafana Loki and Alloy. This setup provides a simple reference logging setup that can be followed in Kubernetes clusters including Minikube and MicroK8s.

This setup is intended for development and testing purposes. For production environments, please refer to the official documentation for high-availability configurations.

## Components Overview

-
: Fast and cost-effective Kubernetes-native log aggregation system.[Grafana Loki](https://grafana.com/oss/loki/) -
: OpenTelemetry collector that replaces Promtail, gathering logs, metrics and traces from Kubernetes pods.[Grafana Alloy](https://grafana.com/oss/alloy/) -
: Visualization platform for querying and exploring logs.[Grafana](https://grafana.com/grafana/)

## Prerequisites

### 1. Dynamo Kubernetes Platform

This guide assumes you have installed Dynamo Kubernetes Platform. For more information, see [Dynamo Kubernetes Platform](https://docs.nvidia.com/dynamo/v1.1.1/getting-started/kubernetes-deployment).

### 2. Kube-prometheus

While this guide does not use Prometheus, it assumes Grafana is pre-installed with the kube-prometheus. For more information, see [kube-prometheus](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack).

### 3. Environment Variables

#### Kubernetes Setup Variables

The following env variables are set:

`MONITORING_NAMESPACE`

: The namespace where Loki is installed`DYN_NAMESPACE`

: The namespace where Dynamo Kubernetes Platform is installed

#### Dynamo Logging Variables

## Installation Steps

### 1. Install Loki

First, we’ll install Loki in single binary mode, which is ideal for testing and development:

Our configuration (`loki-values.yaml`

) sets up Loki in a simple configuration that is suitable for testing and development. It uses a local MinIO for storage. The installation pods can be viewed with:

### 2. Install Grafana Alloy

Next, install the Grafana Alloy collector to gather logs from your Kubernetes cluster and forward them to Loki. Here we use the Helm chart `k8s-monitoring`

provided by Grafana to install the collector:

The values file (`alloy-values.yaml`

) includes the following configurations for the collector:

- Destination to forward logs to Loki
- Namespace to collect logs from
- Pod labels to be mapped to Loki labels
- Collection method (kubernetesApi or tailing
`/var/log/containers/`

)

### 3. Configure Grafana with the Loki datasource and Dynamo Logs dashboard

We will be viewing the logs associated with our DynamoGraphDeployment in Grafana. To do this, we need to configure Grafana with the Loki datasource and Dynamo Logs dashboard.

Since we are using Grafana with the Prometheus Operator, we can simply apply the following ConfigMaps to quickly achieve this configuration.

If using Grafana installed without the Prometheus Operator, you can manually import the Loki datasource and Dynamo Logs dashboard using the Grafana UI.

### 4. Deploy a DynamoGraphDeployment with JSONL Logging

At this point, we should have everything in place to collect and view logs in our Grafana instance. All that is left is to deploy a DynamoGraphDeployment to collect logs from.

To enable structured logs in a DynamoGraphDeployment, we need to set the `DYN_LOGGING_JSONL`

environment variable to `1`

. This is done for us in the `agg_logging.yaml`

setup for the Sglang backend. We can now deploy the DynamoGraphDeployment with:

Send a few chat completions requests to generate structured logs across the frontend and worker pods across the DynamoGraphDeployment. We are now all set to view the logs in Grafana.

## Viewing Logs in Grafana

Port-forward the Grafana service to access the UI:

If everything is working, under Home > Dashboards > Dynamo Logs, you should see a dashboard that can be used to view the logs associated with our DynamoGraphDeployments

The dashboard enables filtering by DynamoGraphDeployment, namespace, and component type (e.g., frontend, worker, etc.).