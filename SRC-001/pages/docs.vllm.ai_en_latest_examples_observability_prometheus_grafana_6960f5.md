source: https://docs.vllm.ai/en/latest/examples/observability/prometheus_grafana/
lastmod: 2026-09-23

# Prometheus and Grafana[¶](https://docs.vllm.ai#prometheus-and-grafana)

Source [https://github.com/vllm-project/vllm/tree/main/examples/observability/prometheus_grafana](https://github.com/vllm-project/vllm/tree/main/examples/observability/prometheus_grafana).

This is a simple example that shows you how to connect vLLM metric logging to the Prometheus/Grafana stack. For this example, we launch Prometheus and Grafana via Docker. You can checkout other methods through [Prometheus](https://prometheus.io/) and [Grafana](https://grafana.com/) websites.

Install:

## Launch[¶](https://docs.vllm.ai#launch)

Prometheus metric logging is enabled by default in the OpenAI-compatible server. Launch via the entrypoint:

Launch Prometheus and Grafana servers with `docker compose`

:

Submit some sample requests to the server:

wget https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json
vllm bench serve \
--model mistralai/Mistral-7B-v0.1 \
--tokenizer mistralai/Mistral-7B-v0.1 \
--endpoint /v1/completions \
--dataset-name sharegpt \
--dataset-path ShareGPT_V3_unfiltered_cleaned_split.json \
--request-rate 3.0


Navigating to [ http://localhost:8000/metrics](http://localhost:8000/metrics) will show the raw Prometheus metrics being exposed by vLLM.

## Grafana Dashboard[¶](https://docs.vllm.ai#grafana-dashboard)

Navigate to [ http://localhost:3000](http://localhost:3000). Log in with the default username (

`admin`

) and password (`admin`

).### Add Prometheus Data Source[¶](https://docs.vllm.ai#add-prometheus-data-source)

Navigate to [ http://localhost:3000/connections/datasources/new](http://localhost:3000/connections/datasources/new) and select Prometheus.

On Prometheus configuration page, we need to add the `Prometheus Server URL`

in `Connection`

. For this setup, Grafana and Prometheus are running in separate containers, but Docker creates DNS name for each container. You can just use `http://prometheus:9090`

.

Click `Save & Test`

. You should get a green check saying "Successfully queried the Prometheus API.".

### Import Dashboard[¶](https://docs.vllm.ai#import-dashboard)

Navigate to [ http://localhost:3000/dashboard/import](http://localhost:3000/dashboard/import), upload

`grafana.json`

, and select the `prometheus`

datasource. You should see a screen that looks like the following:## Example materials[¶](https://docs.vllm.ai#example-materials)

## docker-compose.yaml

# docker-compose.yaml
version: "3"
services:
prometheus:
image: prom/prometheus:latest
extra_hosts:
- "host.docker.internal:host-gateway" # allow a direct connection from container to the local machine
ports:
- "9090:9090" # the default port used by Prometheus
volumes:
- ${PWD}/prometheus.yaml:/etc/prometheus/prometheus.yml # mount Prometheus config file
grafana:
image: grafana/grafana:latest
depends_on:
- prometheus
ports:
- "3000:3000" # the default port used by Grafana


## grafana.json

{
"annotations": {
"list": [
{
"builtIn": 1,
"datasource": {
"type": "grafana",
"uid": "-- Grafana --"
},
"enable": true,
"hide": true,
"iconColor": "rgba(0, 211, 255, 1)",
"name": "Annotations & Alerts",
"target": {
"limit": 100,
"matchAny": false,
"tags": [],
"type": "dashboard"
},
"type": "dashboard"
}
]
},
"description": "Monitoring vLLM Inference Server",
"editable": true,
"fiscalYearStartMonth": 0,
"graphTooltip": 0,
"id": 1,
"links": [],
"liveNow": false,
"panels": [
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "End to end request latency measured in seconds.",
"fieldConfig": {
"defaults": {
"color": {
"mode": "palette-classic"
},
"custom": {
"axisBorderShow": false,
"axisCenteredZero": false,
"axisColorMode": "text",
"axisLabel": "",
"axisPlacement": "auto",
"barAlignment": 0,
"barWidthFactor": 0.6,
"drawStyle": "line",
"fillOpacity": 0,
"gradientMode": "none",
"hideFrom": {
"legend": false,
"tooltip": false,
"viz": false
},
"insertNulls": false,
"lineInterpolation": "linear",
"lineWidth": 1,
"pointSize": 5,
"scaleDistribution": {
"type": "linear"
},
"showPoints": "auto",
"spanNulls": false,
"stacking": {
"group": "A",
"mode": "none"
},
"thresholdsStyle": {
"mode": "off"
}
},
"mappings": [],
"thresholds": {
"mode": "absolute",
"steps": [
{
"color": "green",
"value": null
},
{
"color": "red",
"value": 80
}
]
},
"unit": "s"
},
"overrides": []
},
"gridPos": {
"h": 8,
"w": 12,
"x": 0,
"y": 0
},
"id": 9,
"options": {
"legend": {
"calcs": [],
"displayMode": "list",
"placement": "bottom",
"showLegend": true
},
"tooltip": {
"mode": "single",
"sort": "none"
}
},
"targets": [
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "builder",
"expr": "histogram_quantile(0.99, sum by(le) (rate(vllm:e2e_request_latency_seconds_bucket{model_name=\"$model_name\"}[$__rate_interval])))",
"fullMetaSearch": false,
"includeNullMetadata": false,
"instant": false,
"legendFormat": "P99",
"range": true,
"refId": "A",
"useBackend": false
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "builder",
"expr": "histogram_quantile(0.95, sum by(le) (rate(vllm:e2e_request_latency_seconds_bucket{model_name=\"$model_name\"}[$__rate_interval])))",
"fullMetaSearch": false,
"hide": false,
"includeNullMetadata": false,
"instant": false,
"legendFormat": "P95",
"range": true,
"refId": "B",
"useBackend": false
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "builder",
"expr": "histogram_quantile(0.9, sum by(le) (rate(vllm:e2e_request_latency_seconds_bucket{model_name=\"$model_name\"}[$__rate_interval])))",
"fullMetaSearch": false,
"hide": false,
"includeNullMetadata": false,
"instant": false,
"legendFormat": "P90",
"range": true,
"refId": "C",
"useBackend": false
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "builder",
"expr": "histogram_quantile(0.5, sum by(le) (rate(vllm:e2e_request_latency_seconds_bucket{model_name=\"$model_name\"}[$__rate_interval])))",
"fullMetaSearch": false,
"hide": false,
"includeNullMetadata": false,
"instant": false,
"legendFormat": "P50",
"range": true,
"refId": "D",
"useBackend": false
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"editorMode": "code",
"expr": "rate(vllm:e2e_request_latency_seconds_sum{model_name=\"$model_name\"}[$__rate_interval])\n/\nrate(vllm:e2e_request_latency_seconds_count{model_name=\"$model_name\"}[$__rate_interval])",
"hide": false,
"instant": false,
"legendFormat": "Average",
"range": true,
"refId": "E"
}
],
"title": "E2E Request Latency",
"type": "timeseries"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "Number of tokens processed per second",
"fieldConfig": {
"defaults": {
"color": {
"mode": "palette-classic"
},
"custom": {
"axisBorderShow": false,
"axisCenteredZero": false,
"axisColorMode": "text",
"axisLabel": "",
"axisPlacement": "auto",
"barAlignment": 0,
"barWidthFactor": 0.6,
"drawStyle": "line",
"fillOpacity": 0,
"gradientMode": "none",
"hideFrom": {
"legend": false,
"tooltip": false,
"viz": false
},
"insertNulls": false,
"lineInterpolation": "linear",
"lineWidth": 1,
"pointSize": 5,
"scaleDistribution": {
"type": "linear"
},
"showPoints": "auto",
"spanNulls": false,
"stacking": {
"group": "A",
"mode": "none"
},
"thresholdsStyle": {
"mode": "off"
}
},
"mappings": [],
"thresholds": {
"mode": "absolute",
"steps": [
{
"color": "green",
"value": null
},
{
"color": "red",
"value": 80
}
]
}
},
"overrides": []
},
"gridPos": {
"h": 8,
"w": 12,
"x": 12,
"y": 0
},
"id": 8,
"options": {
"legend": {
"calcs": [],
"displayMode": "list",
"placement": "bottom",
"showLegend": true
},
"tooltip": {
"mode": "single",
"sort": "none"
}
},
"targets": [
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "builder",
"expr": "rate(vllm:prompt_tokens_total{model_name=\"$model_name\"}[$__rate_interval])",
"fullMetaSearch": false,
"includeNullMetadata": false,
"instant": false,
"legendFormat": "Prompt Tokens/Sec",
"range": true,
"refId": "A",
"useBackend": false
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "builder",
"expr": "rate(vllm:generation_tokens_total{model_name=\"$model_name\"}[$__rate_interval])",
"fullMetaSearch": false,
"hide": false,
"includeNullMetadata": false,
"instant": false,
"legendFormat": "Generation Tokens/Sec",
"range": true,
"refId": "B",
"useBackend": false
}
],
"title": "Token Throughput",
"type": "timeseries"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "Inter-token latency in seconds, measured between consecutive streamed outputs. It approximates TPOT when each output contains one token, but differs from request-level TPOT under speculative decoding or varying aggregation weights.",
"fieldConfig": {
"defaults": {
"color": {
"mode": "palette-classic"
},
"custom": {
"axisBorderShow": false,
"axisCenteredZero": false,
"axisColorMode": "text",
"axisLabel": "",
"axisPlacement": "auto",
"barAlignment": 0,
"barWidthFactor": 0.6,
"drawStyle": "line",
"fillOpacity": 0,
"gradientMode": "none",
"hideFrom": {
"legend": false,
"tooltip": false,
"viz": false
},
"insertNulls": false,
"lineInterpolation": "linear",
"lineWidth": 1,
"pointSize": 5,
"scaleDistribution": {
"type": "linear"
},
"showPoints": "auto",
"spanNulls": false,
"stacking": {
"group": "A",
"mode": "none"
},
"thresholdsStyle": {
"mode": "off"
}
},
"mappings": [],
"thresholds": {
"mode": "absolute",
"steps": [
{
"color": "green",
"value": null
},
{
"color": "red",
"value": 80
}
]
},
"unit": "s"
},
"overrides": []
},
"gridPos": {
"h": 8,
"w": 12,
"x": 0,
"y": 8
},
"id": 10,
"options": {
"legend": {
"calcs": [],
"displayMode": "list",
"placement": "bottom",
"showLegend": true
},
"tooltip": {
"mode": "single",
"sort": "none"
}
},
"targets": [
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "builder",
"expr": "histogram_quantile(0.99, sum by(le) (rate(vllm:inter_token_latency_seconds_bucket{model_name=\"$model_name\"}[$__rate_interval])))",
"fullMetaSearch": false,
"includeNullMetadata": false,
"instant": false,
"legendFormat": "P99",
"range": true,
"refId": "A",
"useBackend": false
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "builder",
"expr": "histogram_quantile(0.95, sum by(le) (rate(vllm:inter_token_latency_seconds_bucket{model_name=\"$model_name\"}[$__rate_interval])))",
"fullMetaSearch": false,
"hide": false,
"includeNullMetadata": false,
"instant": false,
"legendFormat": "P95",
"range": true,
"refId": "B",
"useBackend": false
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "builder",
"expr": "histogram_quantile(0.9, sum by(le) (rate(vllm:inter_token_latency_seconds_bucket{model_name=\"$model_name\"}[$__rate_interval])))",
"fullMetaSearch": false,
"hide": false,
"includeNullMetadata": false,
"instant": false,
"legendFormat": "P90",
"range": true,
"refId": "C",
"useBackend": false
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "builder",
"expr": "histogram_quantile(0.5, sum by(le) (rate(vllm:inter_token_latency_seconds_bucket{model_name=\"$model_name\"}[$__rate_interval])))",
"fullMetaSearch": false,
"hide": false,
"includeNullMetadata": false,
"instant": false,
"legendFormat": "P50",
"range": true,
"refId": "D",
"useBackend": false
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"editorMode": "code",
"expr": "rate(vllm:inter_token_latency_seconds_sum{model_name=\"$model_name\"}[$__rate_interval])\n/\nrate(vllm:inter_token_latency_seconds_count{model_name=\"$model_name\"}[$__rate_interval])",
"hide": false,
"instant": false,
"legendFormat": "Mean",
"range": true,
"refId": "E"
}
],
"title": "Inter Token Latency",
"type": "timeseries"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "Per-request Time Per Output Token (TPOT) in seconds, computed as (end-to-end latency - TTFT) divided by the number of output tokens minus one. Requests with no more than one output token are recorded as zero; vllm bench serve excludes these requests from its TPOT statistics.",
"fieldConfig": {
"defaults": {
"color": {
"mode": "palette-classic"
},
"custom": {
"axisBorderShow": false,
"axisCenteredZero": false,
"axisColorMode": "text",
"axisLabel": "",
"axisPlacement": "auto",
"barAlignment": 0,
"barWidthFactor": 0.6,
"drawStyle": "line",
"fillOpacity": 0,
"gradientMode": "none",
"hideFrom": {
"legend": false,
"tooltip": false,
"viz": false
},
"insertNulls": false,
"lineInterpolation": "linear",
"lineWidth": 1,
"pointSize": 5,
"scaleDistribution": {
"type": "linear"
},
"showPoints": "auto",
"spanNulls": false,
"stacking": {
"group": "A",
"mode": "none"
},
"thresholdsStyle": {
"mode": "off"
}
},
"mappings": [],
"thresholds": {
"mode": "absolute",
"steps": [
{
"color": "green",
"value": null
},
{
"color": "red",
"value": 80
}
]
},
"unit": "s"
},
"overrides": []
},
"gridPos": {
"h": 8,
"w": 12,
"x": 12,
"y": 48
},
"id": 17,
"options": {
"legend": {
"calcs": [],
"displayMode": "list",
"placement": "bottom",
"showLegend": true
},
"tooltip": {
"mode": "single",
"sort": "none"
}
},
"targets": [
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "builder",
"expr": "histogram_quantile(0.99, sum by(le) (rate(vllm:request_time_per_output_token_seconds_bucket{model_name=\"$model_name\"}[$__rate_interval])))",
"fullMetaSearch": false,
"includeNullMetadata": false,
"instant": false,
"legendFormat": "P99",
"range": true,
"refId": "A",
"useBackend": false
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "builder",
"expr": "histogram_quantile(0.95, sum by(le) (rate(vllm:request_time_per_output_token_seconds_bucket{model_name=\"$model_name\"}[$__rate_interval])))",
"fullMetaSearch": false,
"hide": false,
"includeNullMetadata": false,
"instant": false,
"legendFormat": "P95",
"range": true,
"refId": "B",
"useBackend": false
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "builder",
"expr": "histogram_quantile(0.9, sum by(le) (rate(vllm:request_time_per_output_token_seconds_bucket{model_name=\"$model_name\"}[$__rate_interval])))",
"fullMetaSearch": false,
"hide": false,
"includeNullMetadata": false,
"instant": false,
"legendFormat": "P90",
"range": true,
"refId": "C",
"useBackend": false
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "builder",
"expr": "histogram_quantile(0.5, sum by(le) (rate(vllm:request_time_per_output_token_seconds_bucket{model_name=\"$model_name\"}[$__rate_interval])))",
"fullMetaSearch": false,
"hide": false,
"includeNullMetadata": false,
"instant": false,
"legendFormat": "P50",
"range": true,
"refId": "D",
"useBackend": false
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"editorMode": "code",
"expr": "rate(vllm:request_time_per_output_token_seconds_sum{model_name=\"$model_name\"}[$__rate_interval])\n/\nrate(vllm:request_time_per_output_token_seconds_count{model_name=\"$model_name\"}[$__rate_interval])",
"hide": false,
"instant": false,
"legendFormat": "Mean",
"range": true,
"refId": "E"
}
],
"title": "Time Per Output Token (TPOT)",
"type": "timeseries"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "Number of requests in RUNNING, WAITING, and SWAPPED state",
"fieldConfig": {
"defaults": {
"color": {
"mode": "palette-classic"
},
"custom": {
"axisBorderShow": false,
"axisCenteredZero": false,
"axisColorMode": "text",
"axisLabel": "",
"axisPlacement": "auto",
"barAlignment": 0,
"barWidthFactor": 0.6,
"drawStyle": "line",
"fillOpacity": 0,
"gradientMode": "none",
"hideFrom": {
"legend": false,
"tooltip": false,
"viz": false
},
"insertNulls": false,
"lineInterpolation": "linear",
"lineWidth": 1,
"pointSize": 5,
"scaleDistribution": {
"type": "linear"
},
"showPoints": "auto",
"spanNulls": false,
"stacking": {
"group": "A",
"mode": "none"
},
"thresholdsStyle": {
"mode": "off"
}
},
"mappings": [],
"thresholds": {
"mode": "absolute",
"steps": [
{
"color": "green",
"value": null
},
{
"color": "red",
"value": 80
}
]
},
"unit": "none"
},
"overrides": []
},
"gridPos": {
"h": 8,
"w": 12,
"x": 12,
"y": 8
},
"id": 3,
"options": {
"legend": {
"calcs": [],
"displayMode": "list",
"placement": "bottom",
"showLegend": true
},
"tooltip": {
"mode": "single",
"sort": "none"
}
},
"targets": [
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "builder",
"expr": "vllm:num_requests_running{model_name=\"$model_name\"}",
"fullMetaSearch": false,
"includeNullMetadata": true,
"instant": false,
"legendFormat": "Num Running",
"range": true,
"refId": "A",
"useBackend": false
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "builder",
"expr": "vllm:num_requests_waiting{model_name=\"$model_name\"}",
"fullMetaSearch": false,
"hide": false,
"includeNullMetadata": true,
"instant": false,
"legendFormat": "Num Waiting",
"range": true,
"refId": "C",
"useBackend": false
}
],
"title": "Scheduler State",
"type": "timeseries"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "P50, P90, P95, and P99 TTFT latency in seconds.",
"fieldConfig": {
"defaults": {
"color": {
"mode": "palette-classic"
},
"custom": {
"axisBorderShow": false,
"axisCenteredZero": false,
"axisColorMode": "text",
"axisLabel": "",
"axisPlacement": "auto",
"barAlignment": 0,
"barWidthFactor": 0.6,
"drawStyle": "line",
"fillOpacity": 0,
"gradientMode": "none",
"hideFrom": {
"legend": false,
"tooltip": false,
"viz": false
},
"insertNulls": false,
"lineInterpolation": "linear",
"lineWidth": 1,
"pointSize": 5,
"scaleDistribution": {
"type": "linear"
},
"showPoints": "auto",
"spanNulls": false,
"stacking": {
"group": "A",
"mode": "none"
},
"thresholdsStyle": {
"mode": "off"
}
},
"mappings": [],
"thresholds": {
"mode": "absolute",
"steps": [
{
"color": "green",
"value": null
},
{
"color": "red",
"value": 80
}
]
},
"unit": "s"
},
"overrides": []
},
"gridPos": {
"h": 8,
"w": 12,
"x": 0,
"y": 16
},
"id": 5,
"options": {
"legend": {
"calcs": [],
"displayMode": "list",
"placement": "bottom",
"showLegend": true
},
"tooltip": {
"mode": "single",
"sort": "none"
}
},
"targets": [
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "builder",
"expr": "histogram_quantile(0.99, sum by(le) (rate(vllm:time_to_first_token_seconds_bucket{model_name=\"$model_name\"}[$__rate_interval])))",
"fullMetaSearch": false,
"hide": false,
"includeNullMetadata": false,
"instant": false,
"legendFormat": "P99",
"range": true,
"refId": "A",
"useBackend": false
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "builder",
"expr": "histogram_quantile(0.95, sum by(le) (rate(vllm:time_to_first_token_seconds_bucket{model_name=\"$model_name\"}[$__rate_interval])))",
"fullMetaSearch": false,
"includeNullMetadata": false,
"instant": false,
"legendFormat": "P95",
"range": true,
"refId": "B",
"useBackend": false
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "builder",
"expr": "histogram_quantile(0.9, sum by(le) (rate(vllm:time_to_first_token_seconds_bucket{model_name=\"$model_name\"}[$__rate_interval])))",
"fullMetaSearch": false,
"hide": false,
"includeNullMetadata": false,
"instant": false,
"legendFormat": "P90",
"range": true,
"refId": "C",
"useBackend": false
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "builder",
"expr": "histogram_quantile(0.5, sum by(le) (rate(vllm:time_to_first_token_seconds_bucket{model_name=\"$model_name\"}[$__rate_interval])))",
"fullMetaSearch": false,
"hide": false,
"includeNullMetadata": false,
"instant": false,
"legendFormat": "P50",
"range": true,
"refId": "D",
"useBackend": false
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"editorMode": "code",
"expr": "rate(vllm:time_to_first_token_seconds_sum{model_name=\"$model_name\"}[$__rate_interval])\n/\nrate(vllm:time_to_first_token_seconds_count{model_name=\"$model_name\"}[$__rate_interval])",
"hide": false,
"instant": false,
"legendFormat": "Average",
"range": true,
"refId": "E"
}
],
"title": "Time To First Token Latency",
"type": "timeseries"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "Percentage of used cache blocks by vLLM.",
"fieldConfig": {
"defaults": {
"color": {
"mode": "palette-classic"
},
"custom": {
"axisBorderShow": false,
"axisCenteredZero": false,
"axisColorMode": "text",
"axisLabel": "",
"axisPlacement": "auto",
"barAlignment": 0,
"barWidthFactor": 0.6,
"drawStyle": "line",
"fillOpacity": 0,
"gradientMode": "none",
"hideFrom": {
"legend": false,
"tooltip": false,
"viz": false
},
"insertNulls": false,
"lineInterpolation": "linear",
"lineWidth": 1,
"pointSize": 5,
"scaleDistribution": {
"type": "linear"
},
"showPoints": "auto",
"spanNulls": false,
"stacking": {
"group": "A",
"mode": "none"
},
"thresholdsStyle": {
"mode": "off"
}
},
"mappings": [],
"thresholds": {
"mode": "absolute",
"steps": [
{
"color": "green",
"value": null
},
{
"color": "red",
"value": 80
}
]
},
"unit": "percentunit"
},
"overrides": []
},
"gridPos": {
"h": 8,
"w": 12,
"x": 12,
"y": 16
},
"id": 4,
"options": {
"legend": {
"calcs": [],
"displayMode": "list",
"placement": "bottom",
"showLegend": true
},
"tooltip": {
"mode": "single",
"sort": "none"
}
},
"targets": [
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"editorMode": "code",
"expr": "vllm:kv_cache_usage_perc{model_name=\"$model_name\"}",
"instant": false,
"legendFormat": "GPU Cache Usage",
"range": true,
"refId": "A"
}
],
"title": "Cache Utilization",
"type": "timeseries"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "Heatmap of request prompt length",
"fieldConfig": {
"defaults": {
"custom": {
"hideFrom": {
"legend": false,
"tooltip": false,
"viz": false
},
"scaleDistribution": {
"type": "linear"
}
}
},
"overrides": []
},
"gridPos": {
"h": 8,
"w": 12,
"x": 0,
"y": 24
},
"id": 12,
"options": {
"calculate": false,
"cellGap": 1,
"cellValues": {
"unit": "none"
},
"color": {
"exponent": 0.5,
"fill": "dark-orange",
"min": 0,
"mode": "scheme",
"reverse": false,
"scale": "exponential",
"scheme": "Spectral",
"steps": 64
},
"exemplars": {
"color": "rgba(255,0,255,0.7)"
},
"filterValues": {
"le": 1e-9
},
"legend": {
"show": true
},
"rowsFrame": {
"layout": "auto",
"value": "Request count"
},
"tooltip": {
"mode": "single",
"showColorScale": false,
"yHistogram": true
},
"yAxis": {
"axisLabel": "Prompt Length",
"axisPlacement": "left",
"reverse": false,
"unit": "none"
}
},
"pluginVersion": "11.2.0",
"targets": [
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "builder",
"expr": "sum by(le) (increase(vllm:request_prompt_tokens_bucket{model_name=\"$model_name\"}[$__rate_interval]))",
"format": "heatmap",
"fullMetaSearch": false,
"includeNullMetadata": true,
"instant": false,
"legendFormat": "{{le}}",
"range": true,
"refId": "A",
"useBackend": false
}
],
"title": "Request Prompt Length",
"type": "heatmap"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "Heatmap of request generation length",
"fieldConfig": {
"defaults": {
"custom": {
"hideFrom": {
"legend": false,
"tooltip": false,
"viz": false
},
"scaleDistribution": {
"type": "linear"
}
}
},
"overrides": []
},
"gridPos": {
"h": 8,
"w": 12,
"x": 12,
"y": 24
},
"id": 13,
"options": {
"calculate": false,
"cellGap": 1,
"cellValues": {
"unit": "none"
},
"color": {
"exponent": 0.5,
"fill": "dark-orange",
"min": 0,
"mode": "scheme",
"reverse": false,
"scale": "exponential",
"scheme": "Spectral",
"steps": 64
},
"exemplars": {
"color": "rgba(255,0,255,0.7)"
},
"filterValues": {
"le": 1e-9
},
"legend": {
"show": true
},
"rowsFrame": {
"layout": "auto",
"value": "Request count"
},
"tooltip": {
"mode": "single",
"showColorScale": false,
"yHistogram": true
},
"yAxis": {
"axisLabel": "Generation Length",
"axisPlacement": "left",
"reverse": false,
"unit": "none"
}
},
"pluginVersion": "11.2.0",
"targets": [
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "builder",
"expr": "sum by(le) (increase(vllm:request_generation_tokens_bucket{model_name=\"$model_name\"}[$__rate_interval]))",
"format": "heatmap",
"fullMetaSearch": false,
"includeNullMetadata": true,
"instant": false,
"legendFormat": "{{le}}",
"range": true,
"refId": "A",
"useBackend": false
}
],
"title": "Request Generation Length",
"type": "heatmap"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "Number of finished requests by their finish reason: either an EOS token was generated or the max sequence length was reached.",
"fieldConfig": {
"defaults": {
"color": {
"mode": "palette-classic"
},
"custom": {
"axisBorderShow": false,
"axisCenteredZero": false,
"axisColorMode": "text",
"axisLabel": "",
"axisPlacement": "auto",
"barAlignment": 0,
"barWidthFactor": 0.6,
"drawStyle": "line",
"fillOpacity": 0,
"gradientMode": "none",
"hideFrom": {
"legend": false,
"tooltip": false,
"viz": false
},
"insertNulls": false,
"lineInterpolation": "linear",
"lineWidth": 1,
"pointSize": 5,
"scaleDistribution": {
"type": "linear"
},
"showPoints": "auto",
"spanNulls": false,
"stacking": {
"group": "A",
"mode": "none"
},
"thresholdsStyle": {
"mode": "off"
}
},
"mappings": [],
"thresholds": {
"mode": "absolute",
"steps": [
{
"color": "green"
},
{
"color": "red",
"value": 80
}
]
}
},
"overrides": []
},
"gridPos": {
"h": 8,
"w": 12,
"x": 0,
"y": 32
},
"id": 11,
"options": {
"legend": {
"calcs": [],
"displayMode": "list",
"placement": "bottom",
"showLegend": true
},
"tooltip": {
"mode": "single",
"sort": "none"
}
},
"targets": [
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "builder",
"expr": "sum by(finished_reason) (increase(vllm:request_success_total{model_name=\"$model_name\"}[$__rate_interval]))",
"fullMetaSearch": false,
"includeNullMetadata": true,
"instant": false,
"interval": "",
"legendFormat": "__auto",
"range": true,
"refId": "A",
"useBackend": false
}
],
"title": "Finish Reason",
"type": "timeseries"
},
{
"datasource": {
"default": false,
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"fieldConfig": {
"defaults": {
"color": {
"mode": "palette-classic"
},
"custom": {
"axisBorderShow": false,
"axisCenteredZero": false,
"axisColorMode": "text",
"axisLabel": "seconds",
"axisPlacement": "auto",
"barAlignment": 0,
"barWidthFactor": 0.6,
"drawStyle": "line",
"fillOpacity": 0,
"gradientMode": "none",
"hideFrom": {
"legend": false,
"tooltip": false,
"viz": false
},
"insertNulls": false,
"lineInterpolation": "linear",
"lineWidth": 1,
"pointSize": 5,
"scaleDistribution": {
"type": "linear"
},
"showPoints": "auto",
"spanNulls": false,
"stacking": {
"group": "A",
"mode": "none"
},
"thresholdsStyle": {
"mode": "off"
}
},
"mappings": [],
"thresholds": {
"mode": "absolute",
"steps": [
{
"color": "green"
},
{
"color": "red",
"value": 80
}
]
}
},
"overrides": []
},
"gridPos": {
"h": 8,
"w": 12,
"x": 12,
"y": 32
},
"id": 14,
"options": {
"legend": {
"calcs": [],
"displayMode": "list",
"placement": "bottom",
"showLegend": true
},
"tooltip": {
"mode": "single",
"sort": "none"
}
},
"targets": [
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "code",
"expr": "rate(vllm:request_queue_time_seconds_sum{model_name=\"$model_name\"}[$__rate_interval])",
"fullMetaSearch": false,
"includeNullMetadata": true,
"instant": false,
"legendFormat": "__auto",
"range": true,
"refId": "A",
"useBackend": false
}
],
"title": "Queue Time",
"type": "timeseries"
},
{
"datasource": {
"default": false,
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"fieldConfig": {
"defaults": {
"color": {
"mode": "palette-classic"
},
"custom": {
"axisBorderShow": false,
"axisCenteredZero": false,
"axisColorMode": "text",
"axisLabel": "",
"axisPlacement": "auto",
"barAlignment": 0,
"barWidthFactor": 0.6,
"drawStyle": "line",
"fillOpacity": 0,
"gradientMode": "none",
"hideFrom": {
"legend": false,
"tooltip": false,
"viz": false
},
"insertNulls": false,
"lineInterpolation": "linear",
"lineWidth": 1,
"pointSize": 5,
"scaleDistribution": {
"type": "linear"
},
"showPoints": "auto",
"spanNulls": false,
"stacking": {
"group": "A",
"mode": "none"
},
"thresholdsStyle": {
"mode": "off"
}
},
"mappings": [],
"thresholds": {
"mode": "absolute",
"steps": [
{
"color": "green"
},
{
"color": "red",
"value": 80
}
]
}
},
"overrides": []
},
"gridPos": {
"h": 8,
"w": 12,
"x": 0,
"y": 40
},
"id": 15,
"options": {
"legend": {
"calcs": [],
"displayMode": "list",
"placement": "bottom",
"showLegend": true
},
"tooltip": {
"mode": "single",
"sort": "none"
}
},
"targets": [
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "code",
"expr": "rate(vllm:request_prefill_time_seconds_sum{model_name=\"$model_name\"}[$__rate_interval])",
"fullMetaSearch": false,
"includeNullMetadata": true,
"instant": false,
"legendFormat": "Prefill",
"range": true,
"refId": "A",
"useBackend": false
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"editorMode": "code",
"expr": "rate(vllm:request_decode_time_seconds_sum{model_name=\"$model_name\"}[$__rate_interval])",
"hide": false,
"instant": false,
"legendFormat": "Decode",
"range": true,
"refId": "B"
}
],
"title": "Requests Prefill and Decode Time",
"type": "timeseries"
},
{
"datasource": {
"default": false,
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"fieldConfig": {
"defaults": {
"color": {
"mode": "palette-classic"
},
"custom": {
"axisBorderShow": false,
"axisCenteredZero": false,
"axisColorMode": "text",
"axisLabel": "",
"axisPlacement": "auto",
"barAlignment": 0,
"barWidthFactor": 0.6,
"drawStyle": "line",
"fillOpacity": 0,
"gradientMode": "none",
"hideFrom": {
"legend": false,
"tooltip": false,
"viz": false
},
"insertNulls": false,
"lineInterpolation": "linear",
"lineWidth": 1,
"pointSize": 5,
"scaleDistribution": {
"type": "linear"
},
"showPoints": "auto",
"spanNulls": false,
"stacking": {
"group": "A",
"mode": "none"
},
"thresholdsStyle": {
"mode": "off"
}
},
"mappings": [],
"thresholds": {
"mode": "absolute",
"steps": [
{
"color": "green"
},
{
"color": "red",
"value": 80
}
]
}
},
"overrides": []
},
"gridPos": {
"h": 8,
"w": 12,
"x": 12,
"y": 40
},
"id": 16,
"options": {
"legend": {
"calcs": [],
"displayMode": "list",
"placement": "bottom",
"showLegend": true
},
"tooltip": {
"mode": "single",
"sort": "none"
}
},
"targets": [
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"disableTextWrap": false,
"editorMode": "code",
"expr": "rate(vllm:request_max_num_generation_tokens_sum{model_name=\"$model_name\"}[$__rate_interval])",
"fullMetaSearch": false,
"includeNullMetadata": true,
"instant": false,
"legendFormat": "Tokens",
"range": true,
"refId": "A",
"useBackend": false
}
],
"title": "Max Generation Token in Sequence Group",
"type": "timeseries"
}
],
"refresh": "",
"schemaVersion": 39,
"tags": [],
"templating": {
"list": [
{
"current": {
"selected": false,
"text": "prometheus",
"value": "edx8memhpd9tsa"
},
"hide": 0,
"includeAll": false,
"label": "datasource",
"multi": false,
"name": "DS_PROMETHEUS",
"options": [],
"query": "prometheus",
"queryValue": "",
"refresh": 1,
"regex": "",
"skipUrlSync": false,
"type": "datasource"
},
{
"current": {
"selected": false,
"text": "/share/datasets/public_models/Meta-Llama-3-8B-Instruct",
"value": "/share/datasets/public_models/Meta-Llama-3-8B-Instruct"
},
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"definition": "label_values(model_name)",
"hide": 0,
"includeAll": false,
"label": "model_name",
"multi": false,
"name": "model_name",
"options": [],
"query": {
"query": "label_values(model_name)",
"refId": "StandardVariableQuery"
},
"refresh": 1,
"regex": "",
"skipUrlSync": false,
"sort": 0,
"type": "query"
}
]
},
"time": {
"from": "now-5m",
"to": "now"
},
"timepicker": {},
"timezone": "",
"title": "vLLM",
"uid": "b281712d-8bff-41ef-9f3f-71ad43c05e9b",
"version": 8,
"weekStart": ""
}