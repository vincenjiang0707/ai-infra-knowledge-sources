source: https://docs.vllm.ai/en/latest/examples/observability/dashboards/
lastmod: 2026-09-24

# Monitoring Dashboards[¶](https://docs.vllm.ai#monitoring-dashboards)

Source [https://github.com/vllm-project/vllm/tree/main/examples/observability/dashboards](https://github.com/vllm-project/vllm/tree/main/examples/observability/dashboards).

This directory contains monitoring dashboard configurations for vLLM, providing comprehensive observability for your vLLM deployments.

## Dashboard Platforms[¶](https://docs.vllm.ai#dashboard-platforms)

We provide dashboards for two popular observability platforms:

## Dashboard Format Approach[¶](https://docs.vllm.ai#dashboard-format-approach)

All dashboards are provided in **native formats** that work across different deployment methods:

### Grafana (JSON)[¶](https://docs.vllm.ai#grafana-json)

- ✅ Works with any Grafana instance (cloud, self-hosted, Docker)
- ✅ Direct import via Grafana UI or API
- ✅ Can be wrapped in Kubernetes operators when needed
- ✅ No vendor lock-in or deployment dependencies

### Perses (YAML)[¶](https://docs.vllm.ai#perses-yaml)

- ✅ Works with standalone Perses instances
- ✅ Compatible with Perses API and CLI
- ✅ Supports Dashboard-as-Code workflows
- ✅ Can be wrapped in Kubernetes operators when needed

## Dashboard Contents[¶](https://docs.vllm.ai#dashboard-contents)

Both platforms provide equivalent monitoring capabilities:

| Dashboard | Description |
|---|---|
Performance Statistics | Tracks latency, throughput, and performance metrics |
Query Statistics | Monitors request volume, query performance, and KPIs |

## Quick Start[¶](https://docs.vllm.ai#quick-start)

First, navigate to this example's directory:

### Grafana[¶](https://docs.vllm.ai#grafana)

Import the JSON directly into the Grafana UI, or use the API:

curl -X POST http://grafana/api/dashboards/db \
-H "Content-Type: application/json" \
-d @grafana/performance_statistics.json


### Perses[¶](https://docs.vllm.ai#perses)

Import via the Perses CLI:

## Requirements[¶](https://docs.vllm.ai#requirements)

**Prometheus**metrics from your vLLM deployment**Data source**configured in your monitoring platform**vLLM metrics**enabled and accessible

## Platform-Specific Documentation[¶](https://docs.vllm.ai#platform-specific-documentation)

For detailed deployment instructions and platform-specific options, see:

- JSON dashboards, operator usage, manual import[Grafana Documentation](https://github.com/vllm-project/vllm/tree/main/examples/observability/dashboards/grafana)- YAML specs, CLI usage, operator wrapping[Perses Documentation](https://github.com/vllm-project/vllm/tree/main/examples/observability/dashboards/perses)

## Contributing[¶](https://docs.vllm.ai#contributing)

When adding new dashboards, please:

- Provide native formats (JSON for Grafana, YAML specs for Perses)
- Update platform-specific README files
- Ensure dashboards work across deployment methods
- Test with the latest platform versions

## Example materials[¶](https://docs.vllm.ai#example-materials)

## grafana/README.md

# Grafana Dashboards for vLLM Monitoring[¶](https://docs.vllm.ai#grafana-dashboards-for-vllm-monitoring)

This directory contains Grafana dashboard configurations (as JSON) designed to monitor vLLM performance and metrics.

## Requirements[¶](https://docs.vllm.ai#requirements_1)

- Grafana 8.0+
- Prometheus data source configured in Grafana
- vLLM deployment with Prometheus metrics enabled

## Dashboard Descriptions[¶](https://docs.vllm.ai#dashboard-descriptions)

**performance_statistics.json**: Tracks performance metrics including latency and throughput for your vLLM service.**query_statistics.json**: Tracks query performance, request volume, and key performance indicators for your vLLM service.

## Deployment Options[¶](https://docs.vllm.ai#deployment-options)

### Manual Import (Recommended)[¶](https://docs.vllm.ai#manual-import-recommended)

The easiest way to use these dashboards is to manually import the JSON configurations directly into your Grafana instance:

- Navigate to your Grafana instance
- Click the '+' icon in the sidebar
- Select 'Import'
- Copy and paste the JSON content from the dashboard files, or upload the JSON files directly

### Grafana Operator[¶](https://docs.vllm.ai#grafana-operator)

If you're using the [Grafana Operator](https://github.com/grafana-operator/grafana-operator) in Kubernetes, you can wrap these JSON configurations in a `GrafanaDashboard`

custom resource:

# Note: Adjust the instanceSelector to match your Grafana instance's labels
# You can check with: kubectl get grafana -o yaml
apiVersion: grafana.integreatly.org/v1beta1
kind: GrafanaDashboard
metadata:
name: vllm-performance-dashboard
spec:
instanceSelector:
matchLabels:
dashboards: grafana # Adjust to match your Grafana instance labels
folder: "vLLM Monitoring"
json: |
# Replace this comment with the complete JSON content from
# performance_statistics.json - The JSON should start with { and end with }


Then apply to your cluster:

## grafana/performance_statistics.json

```json
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
"type": "dashboard"
}
]
},
"editable": true,
"fiscalYearStartMonth": 0,
"graphTooltip": 0,
"id": 26,
"links": [],
"panels": [
{
"collapsed": false,
"gridPos": {
"h": 1,
"w": 24,
"x": 0,
"y": 0
},
"id": 9,
"panels": [],
"title": "Graph: E2E latency over time ",
"type": "row"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "End-to-End latency of requests, showing average and key percentiles over time.",
"fieldConfig": {
"defaults": {
"color": {
"mode": "palette-classic"
},
"custom": {
"axisBorderShow": false,
"axisCenteredZero": false,
"axisColorMode": "text",
"axisLabel": "Latency",
"axisPlacement": "auto",
"barAlignment": 0,
"barWidthFactor": 0.6,
"drawStyle": "line",
"fillOpacity": 18,
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
"spanNulls": true,
"stacking": {
"group": "A",
"mode": "none"
},
"thresholdsStyle": {
"mode": "off"
}
},
"decimals": 2,
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
"y": 1
},
"id": 1,
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
"pluginVersion": "11.3.0",
"targets": [
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"editorMode": "code",
"expr": "rate(vllm:e2e_request_latency_seconds_sum[$__interval]) / rate(vllm:e2e_request_latency_seconds_count[$__interval])",
"format": "table",
"legendFormat": "E2E Latency",
"range": true,
"refId": "A"
}
],
"title": "E2E Latency over Time",
"type": "timeseries"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "99th percentile of End-to-End request latency over the selected time range.",
"fieldConfig": {
"defaults": {
"color": {
"mode": "thresholds"
},
"decimals": 2,
"displayName": "P99",
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
"h": 4,
"w": 6,
"x": 12,
"y": 1
},
"id": 5,
"options": {
"colorMode": "value",
"graphMode": "area",
"justifyMode": "auto",
"orientation": "auto",
"percentChangeColorMode": "standard",
"reduceOptions": {
"calcs": [
"lastNotNull"
],
"fields": "",
"values": false
},
"showPercentChange": false,
"textMode": "auto",
"wideLayout": true
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "histogram_quantile(0.99, sum by(le) (rate(vllm:e2e_request_latency_seconds_bucket[$__range])))",
"legendFormat": "__auto",
"range": true,
"refId": "A"
}
],
"title": "E2E Latency (P99)",
"type": "stat"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "90th percentile of End-to-End request latency over the selected time range.",
"fieldConfig": {
"defaults": {
"color": {
"mode": "thresholds"
},
"decimals": 2,
"displayName": "P90",
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
"h": 4,
"w": 6,
"x": 18,
"y": 1
},
"id": 4,
"options": {
"colorMode": "value",
"graphMode": "area",
"justifyMode": "auto",
"orientation": "auto",
"percentChangeColorMode": "standard",
"reduceOptions": {
"calcs": [
"lastNotNull"
],
"fields": "",
"values": false
},
"showPercentChange": false,
"textMode": "auto",
"wideLayout": true
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "histogram_quantile(0.90, sum by(le) (rate(vllm:e2e_request_latency_seconds_bucket[$__range])))",
"legendFormat": "__auto",
"range": true,
"refId": "A"
}
],
"title": "E2E Latency (P90)",
"type": "stat"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "Average End-to-End request latency over the selected time range.",
"fieldConfig": {
"defaults": {
"color": {
"mode": "thresholds"
},
"decimals": 2,
"displayName": "Average",
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
"h": 4,
"w": 6,
"x": 12,
"y": 5
},
"id": 2,
"options": {
"colorMode": "value",
"graphMode": "area",
"justifyMode": "auto",
"orientation": "auto",
"percentChangeColorMode": "standard",
"reduceOptions": {
"calcs": [
"lastNotNull"
],
"fields": "",
"values": false
},
"showPercentChange": false,
"textMode": "auto",
"wideLayout": true
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "(sum(increase(vllm:e2e_request_latency_seconds_sum[$__range])) / sum(increase(vllm:e2e_request_latency_seconds_count[$__range])))",
"legendFormat": "Average E2E Latency",
"range": true,
"refId": "A"
}
],
"title": "E2E Latency (Avg)",
"type": "stat"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "50th percentile (median) of End-to-End request latency over the selected time range.",
"fieldConfig": {
"defaults": {
"color": {
"mode": "thresholds"
},
"decimals": 2,
"displayName": "P50",
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
"h": 4,
"w": 6,
"x": 18,
"y": 5
},
"id": 3,
"options": {
"colorMode": "value",
"graphMode": "area",
"justifyMode": "auto",
"orientation": "auto",
"percentChangeColorMode": "standard",
"reduceOptions": {
"calcs": [
"lastNotNull"
],
"fields": "",
"values": false
},
"showPercentChange": false,
"textMode": "auto",
"wideLayout": true
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "histogram_quantile(0.50, sum by(le) (rate(vllm:e2e_request_latency_seconds_bucket[$__range])))",
"legendFormat": "__auto",
"range": true,
"refId": "A"
}
],
"title": "E2E Latency (P50)",
"type": "stat"
},
{
"collapsed": false,
"gridPos": {
"h": 1,
"w": 24,
"x": 0,
"y": 9
},
"id": 8,
"panels": [],
"title": "Graph: TTFT(Time To First Token) over time ",
"type": "row"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "Time to first token (TTFT) latency, showing average and key percentiles over time.",
"fieldConfig": {
"defaults": {
"color": {
"mode": "palette-classic"
},
"custom": {
"axisBorderShow": false,
"axisCenteredZero": false,
"axisColorMode": "text",
"axisLabel": "Latency",
"axisPlacement": "auto",
"barAlignment": 0,
"barWidthFactor": 0.6,
"drawStyle": "line",
"fillOpacity": 18,
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
"decimals": 2,
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
"y": 10
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
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "rate(vllm:time_to_first_token_seconds_sum[$__interval]) / rate(vllm:time_to_first_token_seconds_count[$__interval])",
"format": "table",
"legendFormat": "TTFT (Avg)",
"range": true,
"refId": "A"
}
],
"title": "TTFT Over Time",
"type": "timeseries"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "99th percentile of Time To First Token latency over the selected time range.",
"fieldConfig": {
"defaults": {
"color": {
"mode": "thresholds"
},
"decimals": 2,
"displayName": "P99",
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
"h": 4,
"w": 6,
"x": 12,
"y": 10
},
"id": 14,
"options": {
"colorMode": "value",
"graphMode": "area",
"justifyMode": "auto",
"orientation": "auto",
"percentChangeColorMode": "standard",
"reduceOptions": {
"calcs": [
"lastNotNull"
],
"fields": "",
"values": false
},
"showPercentChange": false,
"textMode": "auto",
"wideLayout": true
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "histogram_quantile(0.99, sum by(le) (rate(vllm:time_to_first_token_seconds_bucket[$__range])))",
"legendFormat": "TTFT (p99)",
"range": true,
"refId": "A"
}
],
"title": "TTFT (P99)",
"type": "stat"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "90th percentile of Time To First Token latency over the selected time range.",
"fieldConfig": {
"defaults": {
"color": {
"mode": "thresholds"
},
"decimals": 2,
"displayName": "P90",
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
"h": 4,
"w": 6,
"x": 18,
"y": 10
},
"id": 13,
"options": {
"colorMode": "value",
"graphMode": "area",
"justifyMode": "auto",
"orientation": "auto",
"percentChangeColorMode": "standard",
"reduceOptions": {
"calcs": [
"lastNotNull"
],
"fields": "",
"values": false
},
"showPercentChange": false,
"textMode": "auto",
"wideLayout": true
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "histogram_quantile(0.90, sum by(le) (rate(vllm:time_to_first_token_seconds_bucket[$__range])))",
"legendFormat": "TTFT (p90)",
"range": true,
"refId": "A"
}
],
"title": "TTFT (P90)",
"type": "stat"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "Average Time To First Token latency over the selected time range.",
"fieldConfig": {
"defaults": {
"color": {
"mode": "thresholds"
},
"decimals": 2,
"displayName": "Average",
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
"h": 4,
"w": 6,
"x": 12,
"y": 14
},
"id": 11,
"options": {
"colorMode": "value",
"graphMode": "area",
"justifyMode": "auto",
"orientation": "auto",
"percentChangeColorMode": "standard",
"reduceOptions": {
"calcs": [
"lastNotNull"
],
"fields": "",
"values": false
},
"showPercentChange": false,
"textMode": "auto",
"wideLayout": true
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "(sum(increase(vllm:time_to_first_token_seconds_sum[$__range])) / sum(increase(vllm:time_to_first_token_seconds_count[$__range])))",
"legendFormat": "__auto",
"range": true,
"refId": "A"
}
],
"title": "TTFT (Avg)",
"type": "stat"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "50th percentile (median) of Time To First Token latency over the selected time range.",
"fieldConfig": {
"defaults": {
"color": {
"mode": "thresholds"
},
"displayName": "P50",
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
"h": 4,
"w": 6,
"x": 18,
"y": 14
},
"id": 12,
"options": {
"colorMode": "value",
"graphMode": "area",
"justifyMode": "auto",
"orietitletChangeColorMode": "standard",
"reduceOptions": {
"calcs": [
"lastNotNull"
],
"fields": "",
"values": false
},
"showPercentChange": false,
"textMode": "auto",
"wideLayout": true
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "histogram_quantile(0.50, sum by(le) (rate(vllm:time_to_first_token_seconds_bucket[$__range])))",
"legendFormat": "__auto",
"range": true,
"refId": "A"
}
],
"title": "TTFT (P50)",
"type": "stat"
},
{
"collapsed": false,
"gridPos": {
"h": 1,
"w": 24,
"x": 0,
"y": 18
},
"id": 7,
"panels": [],
"title": "ITL (Iteration Latency / Time Per Output Token) over time.",
"type": "row"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "Iteration latency, or average time taken to generate a single output token, with percentiles.",
"fieldConfig": {
"defaults": {
"color": {
"mode": "palette-classic"
},
"custom": {
"axisBorderShow": false,
"axisCenteredZero": false,
"axisColorMode": "text",
"axisLabel": "Latency",
"axisPlacement": "auto",
"barAlignment": 0,
"barWidthFactor": 0.6,
"drawStyle": "line",
"fillOpacity": 17,
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
"decimals": 2,
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
"y": 19
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
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "rate(vllm:inter_token_latency_seconds_sum[$__interval]) / rate(vllm:inter_token_latency_seconds_count[$__interval])",
"legendFormat": "ITL (Avg)",
"range": true,
"refId": "A"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"editorMode": "code",
"expr": "histogram_quantile(0.50, sum by(le) (rate(vllm:inter_token_latency_seconds_bucket[$__interval])))",
"hide": false,
"instant": false,
"legendFormat": "ITL (p50)",
"range": true,
"refId": "B"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"editorMode": "code",
"expr": "histogram_quantile(0.90, sum by(le) (rate(vllm:inter_token_latency_seconds_bucket[$__interval])))",
"hide": false,
"instant": false,
"legendFormat": "ITL (p90)",
"range": true,
"refId": "C"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"editorMode": "code",
"expr": "histogram_quantile(0.99, sum by(le) (rate(vllm:inter_token_latency_seconds_bucket[$__interval])))",
"hide": false,
"instant": false,
"legendFormat": "ITL (p99)",
"range": true,
"refId": "D"
}
],
"title": "ITL (Time Per Output Token) Over Time",
"type": "timeseries"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "90th percentile of Iteration Latency over the selected time range.",
"fieldConfig": {
"defaults": {
"color": {
"mode": "thresholds"
},
"decimals": 2,
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
"h": 4,
"w": 6,
"x": 12,
"y": 19
},
"id": 18,
"options": {
"colorMode": "value",
"graphMode": "area",
"justifyMode": "auto",
"orientation": "auto",
"percentChangeColorMode": "standard",
"reduceOptions": {
"calcs": [
"lastNotNull"
],
"fields": "",
"values": false
},
"showPercentChange": false,
"textMode": "auto",
"wideLayout": true
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "histogram_quantile(0.90, sum by(le) (rate(vllm:inter_token_latency_seconds_bucket[$__range])))",
"legendFormat": "__auto",
"range": true,
"refId": "A"
}
],
"title": "ITL (P90)",
"type": "stat"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "99th percentile of Iteration Latency over the selected time range.\n\n",
"fieldConfig": {
"defaults": {
"color": {
"mode": "thresholds"
},
"decimals": 2,
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
"h": 4,
"w": 6,
"x": 18,
"y": 19
},
"id": 19,
"options": {
"colorMode": "value",
"graphMode": "area",
"justifyMode": "auto",
"orientation": "auto",
"percentChangeColorMode": "standard",
"reduceOptions": {
"calcs": [
"lastNotNull"
],
"fields": "",
"values": false
},
"showPercentChange": false,
"textMode": "auto",
"wideLayout": true
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "histogram_quantile(0.99, sum by(le) (rate(vllm:inter_token_latency_seconds_bucket[$__range])))",
"legendFormat": "__auto",
"range": true,
"refId": "A"
}
],
"title": "ITL (P99)",
"type": "stat"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "Average Iteration Latency (time per output token) over the selected time range.",
"fieldConfig": {
"defaults": {
"color": {
"mode": "thresholds"
},
"decimals": 2,
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
"h": 4,
"w": 6,
"x": 12,
"y": 23
},
"id": 16,
"options": {
"colorMode": "value",
"graphMode": "area",
"justifyMode": "auto",
"orientation": "auto",
"percentChangeColorMode": "standard",
"reduceOptions": {
"calcs": [
"lastNotNull"
],
"fields": "",
"values": false
},
"showPercentChange": false,
"textMode": "auto",
"wideLayout": true
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "(sum(increase(vllm:inter_token_latency_seconds_sum[$__range])) / sum(increase(vllm:inter_token_latency_seconds_count[$__range])))",
"legendFormat": "__auto",
"range": true,
"refId": "A"
}
],
"title": "ITL (Avg)",
"type": "stat"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "50th percentile (median) of Iteration Latency over the selected time range.",
"fieldConfig": {
"defaults": {
"color": {
"mode": "thresholds"
},
"decimals": 2,
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
"h": 4,
"w": 6,
"x": 18,
"y": 23
},
"id": 17,
"options": {
"colorMode": "value",
"graphMode": "area",
"justifyMode": "auto",
"orientation": "auto",
"percentChangeColorMode": "standard",
"reduceOptions": {
"calcs": [
"lastNotNull"
],
"fields": "",
"values": false
},
"showPercentChange": false,
"textMode": "auto",
"wideLayout": true
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "histogram_quantile(0.50, sum by(le) (rate(vllm:inter_token_latency_seconds_bucket[$__range])))",
"legendFormat": "__auto",
"range": true,
"refId": "A"
}
],
"title": "ITL (P50)",
"type": "stat"
},
{
"collapsed": false,
"gridPos": {
"h": 1,
"w": 24,
"x": 0,
"y": 27
},
"id": 6,
"panels": [],
"title": "TPS (Tokens Per Second)",
"type": "row"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"description": "Rate of tokens processed per second, including prompt and generation phases.",
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
"unit": "tokens/sec (tps)"
},
"overrides": []
},
"gridPos": {
"h": 8,
"w": 12,
"x": 0,
"y": 28
},
"id": 20,
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
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "rate(vllm:generation_tokens_total[$__interval])",
"legendFormat": "Generation TPS",
"range": true,
"refId": "A"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"editorMode": "code",
"expr": "rate(vllm:prompt_tokens_total[$__interval])",
"hide": false,
"instant": false,
"legendFormat": "Prompt TPS",
"range": true,
"refId": "B"
},
{
"datasource": {
"type": "prometheus",
"uid": "${DS_PROMETHEUS}"
},
"editorMode": "code",
"expr": "rate(vllm:iteration_tokens_total_count[$__interval])",
"hide": false,
"instant": false,
"legendFormat": "Overall Iteration TPS",
"range": true,
"refId": "C"
}
],
"title": "TPS (Tokens Per Second) Over Time",
"type": "timeseries"
}
],
"preload": false,
"schemaVersion": 40,
"tags": [],
"templating": {
"list": [
{
"name": "DS_PROMETHEUS",
"type": "datasource",
"label": "datasource",
"query": "prometheus",
"refresh": 1,
"current": {
"text": "Prometheus",
"value": "prometheus"
}
},
{
"current": {
"text": "avg : Average\n0.50 : P50\n0.90 : P90\n0.99 : P99\n0.999 : Max (Approx)",
"value": "avg : Average\n0.50 : P50\n0.90 : P90\n0.99 : P99\n0.999 : Max (Approx)"
},
"label": "Aggregation",
"name": "agg_method",
"options": [
{
"selected": true,
"text": "avg : Average\n0.50 : P50\n0.90 : P90\n0.99 : P99\n0.999 : Max (Approx)",
"value": "avg : Average\n0.50 : P50\n0.90 : P90\n0.99 : P99\n0.999 : Max (Approx)"
}
],
"query": "avg : Average\n0.50 : P50\n0.90 : P90\n0.99 : P99\n0.999 : Max (Approx)",
"type": "custom"
},
{
"current": {
"text": [
"granite-33-2b-instruct"
],
"value": [
"granite-33-2b-instruct"
]
},
"definition": "label_values(vllm:generation_tokens_total,model_name)",
"includeAll": true,
"label": "Deployment_ID",
"multi": true,
"name": "Deployment_id",
"options": [],
"query": {
"qryType": 1,
"query": "label_values(vllm:generation_tokens_total,model_name)",
"refId": "PrometheusVariableQueryEditor-VariableQuery"
},
"refresh": 1,
"regex": "",
"type": "query"
}
]
},
"time": {
"from": "now-12h",
"to": "now"
},
"timezone": "browser",
"uid": "performance-statistics",
"title": "Performance Statistics",
"version": 40,
"weekStart": ""
}
```


## grafana/query_statistics.json

```json
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
"type": "dashboard"
}
]
},
"description": "High-level overview of VLLM model deployment behavior and key performance indicators. Designed for Data Scientists and Product Managers to monitor request volume, token throughput, and latency",
"editable": true,
"fiscalYearStartMonth": 0,
"graphTooltip": 0,
"id": 47,
"links": [],
"panels": [
{
"collapsed": true,
"gridPos": { "h": 1, "w": 24, "x": 0, "y": 0 },
"id": 20,
"panels": [],
"title": "Request Over Time",
"type": "row"
},
{
"datasource": { "type": "prometheus", "uid": "${DS_PROMETHEUS}" },
"fieldConfig": {
"defaults": {
"color": { "mode": "palette-classic" },
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
"hideFrom": { "legend": false, "tooltip": false, "viz": false },
"insertNulls": false,
"lineInterpolation": "linear",
"lineWidth": 1,
"pointSize": 5,
"scaleDistribution": { "type": "linear" },
"showPoints": "auto",
"spanNulls": false,
"stacking": { "group": "A", "mode": "none" },
"thresholdsStyle": { "mode": "off" }
},
"mappings": [],
"thresholds": {
"mode": "absolute",
"steps": [{ "color": "green", "value": null }, { "color": "red", "value": 80 }]
},
"unit": "req/s"
},
"overrides": []
},
"gridPos": { "h": 6, "w": 10, "x": 0, "y": 1 },
"id": 1,
"options": {
"legend": { "calcs": [], "displayMode": "list", "placement": "bottom", "showLegend": true },
"tooltip": { "mode": "single", "sort": "none" }
},
"pluginVersion": "11.3.0",
"targets": [
{
"datasource": { "type": "prometheus", "uid": "${DS_PROMETHEUS}" },
"editorMode": "code",
"expr": "sum by (model_name) (\n rate(vllm:request_success_total{model_name=~\"$Deployment_id\"}[$__rate_interval])\n)",
"interval": "1",
"legendFormat": "{{model_name}}",
"range": true,
"refId": "A"
}
],
"title": "Successful Requests Over Time",
"type": "timeseries"
},
{
"datasource": { "type": "prometheus", "uid": "${DS_PROMETHEUS}" },
"fieldConfig": {
"defaults": {
"color": { "mode": "thresholds" },
"mappings": [],
"thresholds": {
"mode": "absolute",
"steps": [{ "color": "green", "value": null }, { "color": "red", "value": 80 }]
},
"unit": "req/s"
},
"overrides": []
},
"gridPos": { "h": 3, "w": 7, "x": 10, "y": 1 },
"id": 2,
"options": {
"colorMode": "value",
"graphMode": "area",
"justifyMode": "auto",
"orientation": "auto",
"percentChangeColorMode": "standard",
"reduceOptions": { "calcs": ["mean"], "fields": "", "values": false },
"showPercentChange": false,
"textMode": "auto",
"wideLayout": true
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "sum(rate(vllm:request_success_total{model_name=~\"$Deployment_id\"}[$__rate_interval]))",
"legendFormat": "__auto",
"range": true,
"refId": "A"
}
],
"title": "Requests Avg Rate",
"type": "stat"
},
{
"datasource": { "type": "prometheus", "uid": "${DS_PROMETHEUS}" },
"fieldConfig": {
"defaults": {
"color": { "mode": "thresholds" },
"mappings": [
{ "options": { "Calcultaions": { "index": 0, "text": "Last (not null)" } }, "type": "value" }
],
"thresholds": {
"mode": "absolute",
"steps": [{ "color": "green", "value": null }, { "color": "red", "value": 80 }]
},
"unit": "ms"
},
"overrides": []
},
"gridPos": { "h": 3, "w": 7, "x": 17, "y": 1 },
"id": 3,
"options": {
"colorMode": "value",
"graphMode": "area",
"justifyMode": "auto",
"orientation": "auto",
"percentChangeColorMode": "standard",
"reduceOptions": { "calcs": ["lastNotNull"], "fields": "", "values": false },
"showPercentChange": false,
"textMode": "auto",
"wideLayout": true
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "histogram_quantile(0.50, sum by(le, model_name) (rate(vllm:e2e_request_latency_seconds_bucket{model_name=~\"$Deployment_id\"}[$__rate_interval])))",
"legendFormat": "__auto",
"range": true,
"refId": "A"
}
],
"title": "p50 Latency",
"type": "stat"
},
{
"datasource": { "type": "prometheus", "uid": "${DS_PROMETHEUS}" },
"fieldConfig": {
"defaults": {
"color": { "mode": "thresholds" },
"mappings": [
{ "options": { "Calculation": { "index": 0, "text": "Last (not null)" } }, "type": "value" }
],
"thresholds": {
"mode": "absolute",
"steps": [{ "color": "green", "value": null }, { "color": "red", "value": 80 }]
},
"unit": "ms"
},
"overrides": []
},
"gridPos": { "h": 3, "w": 7, "x": 10, "y": 4 },
"id": 4,
"options": {
"colorMode": "value",
"graphMode": "area",
"justifyMode": "auto",
"orientation": "auto",
"percentChangeColorMode": "standard",
"reduceOptions": { "calcs": ["lastNotNull"], "fields": "", "values": false },
"showPercentChange": false,
"textMode": "auto",
"wideLayout": true
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "histogram_quantile(0.90, sum by(le, model_name) (rate(vllm:e2e_request_latency_seconds_bucket{model_name=~\"$Deployment_id\"}[$__rate_interval])))",
"legendFormat": "__auto",
"range": true,
"refId": "A"
}
],
"title": "p90 Latency",
"type": "stat"
},
{
"datasource": { "type": "prometheus", "uid": "${DS_PROMETHEUS}" },
"fieldConfig": {
"defaults": {
"color": { "mode": "thresholds" },
"mappings": [
{ "options": { "Calculation": { "index": 0, "text": "Last (not null)" } }, "type": "value" }
],
"thresholds": {
"mode": "absolute",
"steps": [{ "color": "green", "value": null }, { "color": "red", "value": 80 }]
},
"unit": "ms"
},
"overrides": []
},
"gridPos": { "h": 3, "w": 7, "x": 17, "y": 4 },
"id": 5,
"options": {
"colorMode": "value",
"graphMode": "area",
"justifyMode": "auto",
"orientation": "auto",
"percentChangeColorMode": "standard",
"reduceOptions": { "calcs": ["lastNotNull"], "fields": "", "values": false },
"showPercentChange": false,
"textMode": "auto",
"wideLayout": true
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "histogram_quantile(0.99, sum by(le, model_name) (rate(vllm:e2e_request_latency_seconds_bucket{model_name=~\"$Deployment_id\"}[$__rate_interval])))",
"legendFormat": "__auto",
"range": true,
"refId": "A"
}
],
"title": "p99 Latency",
"type": "stat"
},
{
"collapsed": false,
"gridPos": { "h": 1, "w": 24, "x": 0, "y": 7 },
"id": 19,
"panels": [],
"title": "Size Distribution",
"type": "row"
},
{
"datasource": { "type": "prometheus", "uid": "${DS_PROMETHEUS}" },
"fieldConfig": {
"defaults": {
"color": { "mode": "palette-classic" },
"custom": {
"fillOpacity": 80,
"gradientMode": "none",
"hideFrom": { "legend": false, "tooltip": false, "viz": false },
"lineWidth": 1,
"stacking": { "group": "A", "mode": "none" }
},
"mappings": [],
"thresholds": {
"mode": "absolute",
"steps": [{ "color": "green", "value": null }, { "color": "red", "value": 80 }]
},
"unit": "cps"
},
"overrides": []
},
"gridPos": { "h": 6, "w": 10, "x": 0, "y": 8 },
"id": 6,
"options": {
"legend": { "calcs": [], "displayMode": "list", "placement": "bottom", "showLegend": true },
"tooltip": { "mode": "single", "sort": "none" }
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "sum by (le, model_name) (rate(vllm:request_prompt_tokens_bucket{model_name=~\"$Deployment_id\"}[$__rate_interval]))",
"legendFormat": "{{model_name}} le={{le}}",
"range": true,
"refId": "A"
}
],
"title": "Input Token Size Distribution",
"type": "histogram"
},
{
"datasource": { "type": "prometheus", "uid": "${DS_PROMETHEUS}" },
"fieldConfig": {
"defaults": {
"color": { "mode": "thresholds" },
"mappings": [
{ "options": { "calculation ": { "index": 0, "text": "Last (not null)" } }, "type": "value" }
],
"thresholds": {
"mode": "absolute",
"steps": [{ "color": "green", "value": null }, { "color": "red", "value": 80 }]
},
"unit": "cps"
},
"overrides": []
},
"gridPos": { "h": 3, "w": 7, "x": 10, "y": 8 },
"id": 9,
"options": {
"colorMode": "value",
"graphMode": "area",
"justifyMode": "auto",
"orientation": "auto",
"percentChangeColorMode": "standard",
"reduceOptions": { "calcs": ["lastNotNull"], "fields": "", "values": false },
"showPercentChange": false,
"textMode": "auto",
"wideLayout": true
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "histogram_quantile(0.90, sum by(le, model_name) (rate(vllm:request_prompt_tokens_bucket{model_name=~\"$Deployment_id\"}[$__rate_interval])))",
"legendFormat": "__auto",
"range": true,
"refId": "A"
}
],
"title": "Input Token Size p90",
"type": "stat"
},
{
"datasource": { "type": "prometheus", "uid": "${DS_PROMETHEUS}" },
"fieldConfig": {
"defaults": {
"color": { "mode": "thresholds" },
"mappings": [
{ "options": { "Calculation": { "index": 0, "text": "Last (not null)" } }, "type": "value" }
],
"thresholds": {
"mode": "absolute",
"steps": [{ "color": "green", "value": null }, { "color": "red", "value": 80 }]
},
"unit": "cps"
},
"overrides": []
},
"gridPos": { "h": 3, "w": 7, "x": 17, "y": 8 },
"id": 8,
"options": {
"colorMode": "value",
"graphMode": "area",
"justifyMode": "auto",
"orientation": "auto",
"percentChangeColorMode": "standard",
"reduceOptions": { "calcs": ["lastNotNull"], "fields": "", "values": false },
"showPercentChange": false,
"textMode": "auto",
"wideLayout": true
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "histogram_quantile(0.50, sum by(le, model_name) (rate(vllm:request_prompt_tokens_bucket{model_name=~\"$Deployment_id\"}[$__rate_interval])))",
"legendFormat": "__auto",
"range": true,
"refId": "A"
}
],
"title": "Input Token Size p50",
"type": "stat"
},
{
"datasource": { "type": "prometheus", "uid": "${DS_PROMETHEUS}" },
"fieldConfig": {
"defaults": {
"color": { "mode": "thresholds" },
"mappings": [
{ "options": { "Calcultaion": { "index": 0, "text": "mean" } }, "type": "value" }
],
"thresholds": {
"mode": "absolute",
"steps": [{ "color": "green", "value": null }, { "color": "red", "value": 80 }]
},
"unit": "cps"
},
"overrides": []
},
"gridPos": { "h": 3, "w": 7, "x": 10, "y": 11 },
"id": 7,
"options": {
"colorMode": "value",
"graphMode": "area",
"justifyMode": "auto",
"orientation": "auto",
"percentChangeColorMode": "standard",
"reduceOptions": { "calcs": ["lastNotNull"], "fields": "", "values": false },
"showPercentChange": false,
"textMode": "auto",
"wideLayout": true
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "sum(rate(vllm:prompt_tokens_total{model_name=~\"$Deployment_id\"}[$__rate_interval]))\n/\nsum(rate(vllm:request_success_total{model_name=~\"$Deployment_id\"}[$__rate_interval]))",
"legendFormat": "__auto",
"range": true,
"refId": "A"
}
],
"title": "Input Token Size Avg",
"type": "stat"
},
{
"datasource": { "type": "prometheus", "uid": "${DS_PROMETHEUS}" },
"fieldConfig": {
"defaults": {
"color": { "mode": "thresholds" },
"mappings": [
{ "options": { "Calculation": { "index": 0, "text": "Last (not null)" } }, "type": "value" }
],
"thresholds": {
"mode": "absolute",
"steps": [{ "color": "green", "value": null }, { "color": "red", "value": 80 }]
},
"unit": "cps"
},
"overrides": []
},
"gridPos": { "h": 3, "w": 7, "x": 17, "y": 11 },
"id": 10,
"options": {
"colorMode": "value",
"graphMode": "area",
"justifyMode": "auto",
"orientation": "auto",
"percentChangeColorMode": "standard",
"reduceOptions": { "calcs": ["lastNotNull"], "fields": "", "values": false },
"showPercentChange": false,
"textMode": "auto",
"wideLayout": true
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "histogram_quantile(0.99, sum by(le, model_name) (rate(vllm:request_prompt_tokens_bucket{model_name=~\"$Deployment_id\"}[$__rate_interval])))",
"legendFormat": "__auto",
"range": true,
"refId": "A"
}
],
"title": "Input Token Size p99",
"type": "stat"
},
{
"collapsed": true,
"gridPos": { "h": 1, "w": 24, "x": 0, "y": 14 },
"id": 18,
"panels": [],
"title": "Input Token Over Time",
"type": "row"
},
{
"datasource": { "type": "prometheus", "uid": "${DS_PROMETHEUS}" },
"fieldConfig": {
"defaults": {
"color": { "mode": "palette-classic" },
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
"hideFrom": { "legend": false, "tooltip": false, "viz": false },
"insertNulls": false,
"lineInterpolation": "linear",
"lineWidth": 1,
"pointSize": 5,
"scaleDistribution": { "type": "linear" },
"showPoints": "auto",
"spanNulls": false,
"stacking": { "group": "A", "mode": "none" },
"thresholdsStyle": { "mode": "off" }
},
"mappings": [],
"thresholds": {
"mode": "absolute",
"steps": [{ "color": "green", "value": null }, { "color": "red", "value": 80 }]
},
"unit": "cps"
},
"overrides": []
},
"gridPos": { "h": 6, "w": 10, "x": 0, "y": 15 },
"id": 11,
"options": {
"legend": { "calcs": [], "displayMode": "list", "placement": "bottom", "showLegend": true },
"tooltip": { "mode": "single", "sort": "none" }
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "sum by (model_name) (rate(vllm:prompt_tokens_total{model_name=~\"$Deployment_id\"}[$__rate_interval]))",
"legendFormat": "{{model_name}}",
"range": true,
"refId": "A"
}
],
"title": "Input Tokens Over Time",
"type": "timeseries"
},
{
"datasource": { "type": "prometheus", "uid": "${DS_PROMETHEUS}" },
"fieldConfig": {
"defaults": {
"color": { "mode": "thresholds" },
"mappings": [
{ "options": { "Calculation": { "index": 0, "text": "mean" } }, "type": "value" }
],
"thresholds": {
"mode": "absolute",
"steps": [{ "color": "green", "value": null }, { "color": "red", "value": 80 }]
},
"unit": "cps"
},
"overrides": []
},
"gridPos": { "h": 3, "w": 7, "x": 10, "y": 15 },
"id": 12,
"options": {
"colorMode": "value",
"graphMode": "area",
"justifyMode": "auto",
"orientation": "auto",
"percentChangeColorMode": "standard",
"reduceOptions": { "calcs": ["lastNotNull"], "fields": "", "values": false },
"showPercentChange": false,
"textMode": "auto",
"wideLayout": true
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "sum(rate(vllm:prompt_tokens_total{model_name=~\"$Deployment_id\"}[$__rate_interval]))",
"legendFormat": "__auto",
"range": true,
"refId": "A"
}
],
"title": "Input Tokens/Sec Avg",
"type": "stat"
},
{
"collapsed": false,
"gridPos": { "h": 1, "w": 24, "x": 0, "y": 21 },
"id": 17,
"panels": [],
"title": "Output Token Over Time",
"type": "row"
},
{
"datasource": { "type": "prometheus", "uid": "${DS_PROMETHEUS}" },
"fieldConfig": {
"defaults": {
"color": { "mode": "palette-classic" },
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
"hideFrom": { "legend": false, "tooltip": false, "viz": false },
"insertNulls": false,
"lineInterpolation": "linear",
"lineWidth": 1,
"pointSize": 5,
"scaleDistribution": { "type": "linear" },
"showPoints": "auto",
"spanNulls": false,
"stacking": { "group": "A", "mode": "none" },
"thresholdsStyle": { "mode": "off" }
},
"mappings": [],
"thresholds": {
"mode": "absolute",
"steps": [{ "color": "green", "value": null }, { "color": "red", "value": 80 }]
},
"unit": "cps"
},
"overrides": []
},
"gridPos": { "h": 6, "w": 10, "x": 0, "y": 22 },
"id": 13,
"options": {
"legend": { "calcs": [], "displayMode": "list", "placement": "bottom", "showLegend": true },
"tooltip": { "mode": "single", "sort": "none" }
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "sum by (model_name) (rate(vllm:generation_tokens_total{model_name=~\"$Deployment_id\"}[$__rate_interval]))",
"legendFormat": "{{model_name}}",
"range": true,
"refId": "A"
}
],
"title": "Output Tokens Over Time",
"type": "timeseries"
},
{
"datasource": { "type": "prometheus", "uid": "${DS_PROMETHEUS}" },
"fieldConfig": {
"defaults": {
"color": { "mode": "thresholds" },
"mappings": [
{ "options": { "Calculation": { "index": 0, "text": "mean" } }, "type": "value" }
],
"thresholds": {
"mode": "absolute",
"steps": [{ "color": "green", "value": null }, { "color": "red", "value": 80 }]
},
"unit": "cps"
},
"overrides": []
},
"gridPos": { "h": 3, "w": 7, "x": 10, "y": 22 },
"id": 14,
"options": {
"colorMode": "value",
"graphMode": "area",
"justifyMode": "auto",
"orientation": "auto",
"percentChangeColorMode": "standard",
"reduceOptions": { "calcs": ["lastNotNull"], "fields": "", "values": false },
"showPercentChange": false,
"textMode": "auto",
"wideLayout": true
},
"pluginVersion": "11.3.0",
"targets": [
{
"editorMode": "code",
"expr": "sum(rate(vllm:generation_tokens_total{model_name=~\"$Deployment_id\"}[$__rate_interval]))",
"legendFormat": "__auto",
"range": true,
"refId": "A"
}
],
"title": "Output Tokens/Sec Avg",
"type": "stat"
}
],
"preload": false,
"schemaVersion": 40,
"tags": [],
"templating": {
"list": [
{
"current": { "text": "Prometheus", "value": "4184fc20-68a7-483a-8d9b-7caa59c680dd" },
"label": "datasource",
"name": "DS_PROMETHEUS",
"options": [],
"query": "prometheus",
"refresh": 1,
"type": "datasource"
},
{
"current": { "text": ["All"], "value": ["$__all"] },
"definition": "label_values(vllm:request_success_total,model_name)",
"includeAll": true,
"label": "Deployment_ID",
"multi": true,
"name": "Deployment_id",
"options": [],
"query": {
"qryType": 1,
"query": "label_values(vllm:request_success_total,model_name)",
"refId": "PrometheusVariableQueryEditor-VariableQuery"
},
"refresh": 1,
"regex": "",
"sort": 1,
"type": "query"
},
{
"current": { "text": "All hours", "value": "All hours" },
"hide": 2,
"label": "Rush Hours Only",
"name": "rush_hours",
"options": [
{ "selected": true, "text": "false", "value": "All hours" },
{ "selected": false, "text": "true", "value": "Rush hours" }
],
"query": "false : All hours, true : Rush hours",
"type": "custom"
},
{
"current": { "text": "All", "value": "All" },
"hide": 2,
"label": "Rush Hours Type",
"name": "rush_hours_type",
"options": [
{ "selected": true, "text": "^All__.*$", "value": "All" },
{ "selected": false, "text": "^Static__.*$", "value": "Static" },
{ "selected": false, "text": "^Dynamic__.*$", "value": "Dynamic" }
],
"query": "^All__.*$ : All, ^Static__.*$ : Static, ^Dynamic__.*$ : Dynamic",
"type": "custom"
},
{
"current": { "text": "", "value": "" },
"hide": 2,
"name": "query0",
"options": [],
"query": "",
"refresh": 1,
"regex": "",
"type": "query"
}
]
},
"time": { "from": "now-12h", "to": "now" },
"timepicker": {},
"timezone": "browser",
"title": "Query Statistics_New4",
"uid": "query-statistics4",
"version": 2,
"weekStart": ""
}
```


## perses/README.md

# Perses Dashboards for vLLM Monitoring[¶](https://docs.vllm.ai#perses-dashboards-for-vllm-monitoring)

This directory contains Perses dashboard configurations designed to monitor vLLM performance and metrics.

## Requirements[¶](https://docs.vllm.ai#requirements_2)

- Perses instance (standalone or via operator)
- Prometheus data source configured in Perses
- vLLM deployment with Prometheus metrics enabled

## Dashboard Format[¶](https://docs.vllm.ai#dashboard-format)

We provide dashboards in the **native Perses YAML format** that works across all deployment methods:

**Files**:`*.yaml`

(native Perses dashboard specifications)**Format**: Pure dashboard specifications that work everywhere**Usage**: Works with standalone Perses, API imports, CLI, and file provisioning**Kubernetes**: Directly compatible with Perses Operator

## Dashboard Descriptions[¶](https://docs.vllm.ai#dashboard-descriptions_1)

**performance_statistics.yaml**: Performance metrics with aggregated latency statistics**query_statistics.yaml**: Query performance and deployment metrics

## Deployment Options[¶](https://docs.vllm.ai#deployment-options_1)

### Direct Import to Perses[¶](https://docs.vllm.ai#direct-import-to-perses)

Import the dashboard specifications via Perses API or CLI:

### Perses Operator (Kubernetes)[¶](https://docs.vllm.ai#perses-operator-kubernetes)

The native YAML format works directly with the Perses Operator:

### File Provisioning[¶](https://docs.vllm.ai#file-provisioning)

Place the YAML files in a Perses provisioning folder for automatic loading.

## perses/performance_statistics.yaml

kind: PersesDashboard
metadata:
name: performance-statistics
createdAt: 0001-01-01T00:00:00Z
updatedAt: 0001-01-01T00:00:00Z
version: 0
project: ""
spec:
display:
name: Performance Statistics
variables:
- kind: ListVariable
spec:
display:
name: Deployment_ID
hidden: false
name: Deployment_id
allowAllValue: true
allowMultiple: true
defaultValue:
- $__all
sort: alphabetical-asc
plugin:
kind: PrometheusLabelValuesVariable
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
labelName: model_name
matchers:
# Any one vllm metric that always carries model_name
- vllm:generation_tokens_total{}
panels:
"1":
kind: Panel
spec:
display:
name: E2E Latency over Time
plugin:
kind: TimeSeriesChart
spec:
legend:
mode: table
position: bottom
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
# avg latency by model = sum(rate(sum)) / sum(rate(count))
query: >
sum by (model_name) (rate(vllm:e2e_request_latency_seconds_sum{model_name=~"$Deployment_id"}[$__interval]))
/
sum by (model_name) (rate(vllm:e2e_request_latency_seconds_count{model_name=~"$Deployment_id"}[$__interval]))
seriesNameFormat: '{{model_name}}'
"2":
kind: Panel
spec:
display:
name: E2E Latency (Avg)
plugin:
kind: StatChart
spec:
calculation: last-number
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
query: >
(sum by (model_name) (increase(vllm:e2e_request_latency_seconds_sum{model_name=~"$Deployment_id"}[$__range])))
/
(sum by (model_name) (increase(vllm:e2e_request_latency_seconds_count{model_name=~"$Deployment_id"}[$__range])))
"3":
kind: Panel
spec:
display:
name: E2E Latency (P50)
plugin:
kind: StatChart
spec:
calculation: last-number
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
query: >
histogram_quantile(
0.50,
sum by (le, model_name) (
rate(vllm:e2e_request_latency_seconds_bucket{model_name=~"$Deployment_id"}[$__interval])
)
)
"4":
kind: Panel
spec:
display:
name: E2E Latency (P90)
plugin:
kind: StatChart
spec:
calculation: last-number
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
query: >
histogram_quantile(
0.90,
sum by (le, model_name) (
rate(vllm:e2e_request_latency_seconds_bucket{model_name=~"$Deployment_id"}[$__interval])
)
)
"5":
kind: Panel
spec:
display:
name: E2E Latency (P99)
plugin:
kind: StatChart
spec:
calculation: last-number
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
query: >
histogram_quantile(
0.99,
sum by (le, model_name) (
rate(vllm:e2e_request_latency_seconds_bucket{model_name=~"$Deployment_id"}[$__interval])
)
)
"6":
kind: Panel
spec:
display:
name: TTFT over Time
plugin:
kind: TimeSeriesChart
spec:
legend:
mode: table
position: bottom
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
query: >
sum by (model_name) (rate(vllm:time_to_first_token_seconds_sum{model_name=~"$Deployment_id"}[$__interval]))
/
sum by (model_name) (rate(vllm:time_to_first_token_seconds_count{model_name=~"$Deployment_id"}[$__interval]))
seriesNameFormat: '{{model_name}}'
"7":
kind: Panel
spec:
display:
name: TTFT (Avg)
plugin:
kind: StatChart
spec:
calculation: last-number
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
query: >
(sum by (model_name) (increase(vllm:time_to_first_token_seconds_sum{model_name=~"$Deployment_id"}[$__range])))
/
(sum by (model_name) (increase(vllm:time_to_first_token_seconds_count{model_name=~"$Deployment_id"}[$__range])))
"8":
kind: Panel
spec:
display:
name: TTFT (P50)
plugin:
kind: StatChart
spec:
calculation: last-number
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
query: >
histogram_quantile(
0.50,
sum by (le, model_name) (
rate(vllm:time_to_first_token_seconds_bucket{model_name=~"$Deployment_id"}[$__interval])
)
)
"9":
kind: Panel
spec:
display:
name: TTFT (P90)
plugin:
kind: StatChart
spec:
calculation: last-number
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
query: >
histogram_quantile(
0.90,
sum by (le, model_name) (
rate(vllm:time_to_first_token_seconds_bucket{model_name=~"$Deployment_id"}[$__interval])
)
)
"10":
kind: Panel
spec:
display:
name: TTFT (P99)
plugin:
kind: StatChart
spec:
calculation: last-number
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
query: >
histogram_quantile(
0.99,
sum by (le, model_name) (
rate(vllm:time_to_first_token_seconds_bucket{model_name=~"$Deployment_id"}[$__interval])
)
)
"11":
kind: Panel
spec:
display:
name: ITL (Time per Output Token) over Time
plugin:
kind: TimeSeriesChart
spec:
legend:
mode: table
position: bottom
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
query: >
sum by (model_name) (rate(vllm:inter_token_latency_seconds_sum{model_name=~"$Deployment_id"}[$__interval]))
/
sum by (model_name) (rate(vllm:inter_token_latency_seconds_count{model_name=~"$Deployment_id"}[$__interval]))
seriesNameFormat: '{{model_name}}'
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
query: >
histogram_quantile(
0.50,
sum by (le, model_name) (
rate(vllm:inter_token_latency_seconds_bucket{model_name=~"$Deployment_id"}[$__interval])
)
)
seriesNameFormat: '{{model_name}} p50'
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
query: >
histogram_quantile(
0.90,
sum by (le, model_name) (
rate(vllm:inter_token_latency_seconds_bucket{model_name=~"$Deployment_id"}[$__interval])
)
)
seriesNameFormat: '{{model_name}} p90'
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
query: >
histogram_quantile(
0.99,
sum by (le, model_name) (
rate(vllm:inter_token_latency_seconds_bucket{model_name=~"$Deployment_id"}[$__interval])
)
)
seriesNameFormat: '{{model_name}} p99'
"12":
kind: Panel
spec:
display:
name: ITL (Avg)
plugin:
kind: StatChart
spec:
calculation: last-number
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
query: >
(sum by (model_name) (increase(vllm:inter_token_latency_seconds_sum{model_name=~"$Deployment_id"}[$__range])))
/
(sum by (model_name) (increase(vllm:inter_token_latency_seconds_count{model_name=~"$Deployment_id"}[$__range])))
"13":
kind: Panel
spec:
display:
name: ITL (P50)
plugin:
kind: StatChart
spec:
calculation: last-number
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
query: >
histogram_quantile(
0.50,
sum by (le, model_name) (
rate(vllm:inter_token_latency_seconds_bucket{model_name=~"$Deployment_id"}[$__interval])
)
)
"14":
kind: Panel
spec:
display:
name: ITL (P90)
plugin:
kind: StatChart
spec:
calculation: last-number
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
query: >
histogram_quantile(
0.90,
sum by (le, model_name) (
rate(vllm:inter_token_latency_seconds_bucket{model_name=~"$Deployment_id"}[$__interval])
)
)
"15":
kind: Panel
spec:
display:
name: ITL (P99)
plugin:
kind: StatChart
spec:
calculation: last-number
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
query: >
histogram_quantile(
0.99,
sum by (le, model_name) (
rate(vllm:inter_token_latency_seconds_bucket{model_name=~"$Deployment_id"}[$__interval])
)
)
"16":
kind: Panel
spec:
display:
name: TPS (Tokens/sec) over Time
plugin:
kind: TimeSeriesChart
spec:
legend:
mode: table
position: bottom
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
query: >
sum by (model_name) (rate(vllm:generation_tokens_total{model_name=~"$Deployment_id"}[$__interval]))
seriesNameFormat: '{{model_name}} generation'
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
query: >
sum by (model_name) (rate(vllm:prompt_tokens_total{model_name=~"$Deployment_id"}[$__interval]))
seriesNameFormat: '{{model_name}} prompt'
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
# overall iteration tokens/sec if exposed
query: >
rate(vllm:iteration_tokens_total_count[$__interval])
seriesNameFormat: 'iteration overall'
"17":
kind: Panel
spec:
display:
name: KV Cache Usage (avg %)
plugin:
kind: StatChart
spec:
calculation: last-number
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
# Multiply by 100 so we can read it as a percentage without setting a unit (avoids CUE unit conflicts)
query: >
100 * avg(vllm:kv_cache_usage_perc)
"18":
kind: Panel
spec:
display:
name: Running Requests by Pod
plugin:
kind: TimeSeriesChart
spec:
legend:
mode: table
position: bottom
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
query: >
sum by (pod) (vllm:num_requests_running)
seriesNameFormat: '{{pod}}'
"19":
kind: Panel
spec:
display:
name: Waiting Requests by Pod
plugin:
kind: TimeSeriesChart
spec:
legend:
mode: table
position: bottom
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
query: >
sum by (pod) (vllm:num_requests_waiting)
seriesNameFormat: '{{pod}}'
"20":
kind: Panel
spec:
display:
name: Running Requests (sum)
plugin:
kind: StatChart
spec:
calculation: last-number
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
query: sum(vllm:num_requests_running)
"21":
kind: Panel
spec:
display:
name: Waiting Requests (sum)
plugin:
kind: StatChart
spec:
calculation: last-number
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource:
kind: PrometheusDatasource
name: accelerators-thanos-querier-datasource
query: sum(vllm:num_requests_waiting)
layouts:
- kind: Grid
spec:
display:
title: Overview
items:
- x: 0
y: 0
width: 6
height: 3
content: { $ref: '#/spec/panels/17' } # KV cache %
- x: 6
y: 0
width: 6
height: 3
content: { $ref: '#/spec/panels/20' } # running sum
- x: 12
y: 0
width: 6
height: 3
content: { $ref: '#/spec/panels/21' } # waiting sum
- kind: Grid
spec:
display:
title: E2E Latency
items:
- x: 0
y: 1
width: 10
height: 6
content: { $ref: '#/spec/panels/1' }
- x: 10
y: 1
width: 7
height: 3
content: { $ref: '#/spec/panels/2' }
- x: 17
y: 1
width: 7
height: 3
content: { $ref: '#/spec/panels/3' }
- x: 10
y: 4
width: 7
height: 3
content: { $ref: '#/spec/panels/4' }
- x: 17
y: 4
width: 7
height: 3
content: { $ref: '#/spec/panels/5' }
- kind: Grid
spec:
display:
title: TTFT
items:
- x: 0
y: 8
width: 10
height: 6
content: { $ref: '#/spec/panels/6' }
- x: 10
y: 8
width: 7
height: 3
content: { $ref: '#/spec/panels/7' }
- x: 17
y: 8
width: 7
height: 3
content: { $ref: '#/spec/panels/8' }
- x: 10
y: 11
width: 7
height: 3
content: { $ref: '#/spec/panels/9' }
- x: 17
y: 11
width: 7
height: 3
content: { $ref: '#/spec/panels/10' }
- kind: Grid
spec:
display:
title: ITL (Time per Output Token)
items:
- x: 0
y: 15
width: 10
height: 6
content: { $ref: '#/spec/panels/11' }
- x: 10
y: 15
width: 7
height: 3
content: { $ref: '#/spec/panels/12' }
- x: 17
y: 15
width: 7
height: 3
content: { $ref: '#/spec/panels/13' }
- x: 10
y: 18
width: 7
height: 3
content: { $ref: '#/spec/panels/14' }
- x: 17
y: 18
width: 7
height: 3
content: { $ref: '#/spec/panels/15' }
- kind: Grid
spec:
display:
title: TPS (Prompt / Generation / Iteration)
items:
- x: 0
y: 22
width: 14
height: 6
content: { $ref: '#/spec/panels/16' }
- kind: Grid
spec:
display:
title: Per-Pod Request State
items:
- x: 0
y: 28
width: 12
height: 6
content: { $ref: '#/spec/panels/18' }
- x: 12
y: 28
width: 12
height: 6
content: { $ref: '#/spec/panels/19' }


## perses/query_statistics.yaml

kind: PersesDashboard
metadata:
name: query-statistics
createdAt: 0001-01-01T00:00:00Z
updatedAt: 0001-01-01T00:00:00Z
version: 0
project: ""
spec:
display:
name: Query Statistics_New
variables:
- kind: ListVariable
spec:
name: NS
display: { name: Namespace }
allowMultiple: false
defaultValue: llm-d
plugin:
kind: PrometheusLabelValuesVariable
spec:
datasource: { kind: PrometheusDatasource, name: accelerators-thanos-querier-datasource }
labelName: namespace
matchers:
- up{service=~".*vllm.*"}
- kind: ListVariable
spec:
name: SVC
display: { name: Service }
allowMultiple: false
defaultValue: vllm-qwen2-0-5b-sim
plugin:
kind: PrometheusLabelValuesVariable
spec:
datasource: { kind: PrometheusDatasource, name: accelerators-thanos-querier-datasource }
labelName: service
matchers:
- up{namespace="$NS",service=~".*vllm.*"}
- kind: ListVariable
spec:
name: MODEL
display: { name: Model (real vLLM) }
allowAllValue: true
allowMultiple: true
defaultValue: ["$__all"]
plugin:
kind: PrometheusLabelValuesVariable
spec:
datasource: { kind: PrometheusDatasource, name: accelerators-thanos-querier-datasource }
labelName: model_name
matchers:
- vllm:request_success_total{namespace="$NS",service="$SVC"}
panels:
# --- Core (works on Simulator & Real) ---
core_running_now:
kind: Panel
spec:
display: { name: Running Requests (now) }
plugin: { kind: StatChart, spec: { calculation: last-number } }
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource: { kind: PrometheusDatasource, name: accelerators-thanos-querier-datasource }
query: sum(vllm:num_requests_running{namespace="$NS",service="$SVC"}) or vector(0)
minStep: "15s"
core_waiting_now:
kind: Panel
spec:
display: { name: Waiting Requests (now) }
plugin: { kind: StatChart, spec: { calculation: last-number } }
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource: { kind: PrometheusDatasource, name: accelerators-thanos-querier-datasource }
query: sum(vllm:num_requests_waiting{namespace="$NS",service="$SVC"}) or vector(0)
minStep: "15s"
core_kv_usage_now:
kind: Panel
spec:
display: { name: KV Cache Usage (0–1) }
plugin: { kind: StatChart, spec: { calculation: last-number } }
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource: { kind: PrometheusDatasource, name: accelerators-thanos-querier-datasource }
query: avg(vllm:kv_cache_usage_perc{namespace="$NS",service="$SVC"}) or vector(0)
minStep: "15s"
core_running_ts:
kind: Panel
spec:
display: { name: Running Over Time }
plugin:
kind: TimeSeriesChart
spec:
legend: { mode: table, position: bottom }
visual: { display: line, lineWidth: 1, areaOpacity: 0.3 }
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource: { kind: PrometheusDatasource, name: accelerators-thanos-querier-datasource }
query: sum by (service) (vllm:num_requests_running{namespace="$NS",service="$SVC"}) or vector(0)
minStep: "15s"
core_waiting_ts:
kind: Panel
spec:
display: { name: Waiting Over Time }
plugin:
kind: TimeSeriesChart
spec:
legend: { mode: table, position: bottom }
visual: { display: line, lineWidth: 1, areaOpacity: 0.3 }
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource: { kind: PrometheusDatasource, name: accelerators-thanos-querier-datasource }
query: sum by (service) (vllm:num_requests_waiting{namespace="$NS",service="$SVC"}) or vector(0)
minStep: "15s"
core_targets_up:
kind: Panel
spec:
display: { name: Scrape Targets Up }
plugin: { kind: StatChart, spec: { calculation: last-number } }
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource: { kind: PrometheusDatasource, name: accelerators-thanos-querier-datasource }
query: count(up{namespace="$NS",service="$SVC"} == 1) or vector(0)
minStep: "15s"
# --- KV Cache as Percent (works on Simulator & Real) ---
core_kv_usage_pct_now:
kind: Panel
spec:
display: { name: KV Cache Usage (%) – now }
plugin: { kind: StatChart, spec: { calculation: last-number } }
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource: { kind: PrometheusDatasource, name: accelerators-thanos-querier-datasource }
# multiply by 100 to present percentage; omit format.unit to avoid schema conflicts
query: (avg(vllm:kv_cache_usage_perc{namespace="$NS",service="$SVC"}) * 100) or vector(0)
minStep: "15s"
core_kv_usage_pct_ts:
kind: Panel
spec:
display: { name: KV Cache Usage (%) – over time }
plugin:
kind: TimeSeriesChart
spec:
legend: { mode: table, position: bottom }
visual: { display: line, lineWidth: 1, areaOpacity: 0.3 }
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource: { kind: PrometheusDatasource, name: accelerators-thanos-querier-datasource }
query: (avg by (service) (vllm:kv_cache_usage_perc{namespace="$NS",service="$SVC"}) * 100) or vector(0)
minStep: "15s"
# --- Per-Pod breakdowns (works on Simulator & Real) ---
per_pod_running_ts:
kind: Panel
spec:
display: { name: Running by Pod }
plugin:
kind: TimeSeriesChart
spec:
legend: { mode: table, position: bottom }
visual: { display: line, lineWidth: 1, areaOpacity: 0.3 }
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource: { kind: PrometheusDatasource, name: accelerators-thanos-querier-datasource }
query: sum by (pod) (vllm:num_requests_running{namespace="$NS",service="$SVC"}) or vector(0)
minStep: "15s"
per_pod_waiting_ts:
kind: Panel
spec:
display: { name: Waiting by Pod }
plugin:
kind: TimeSeriesChart
spec:
legend: { mode: table, position: bottom }
visual: { display: line, lineWidth: 1, areaOpacity: 0.3 }
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource: { kind: PrometheusDatasource, name: accelerators-thanos-querier-datasource }
query: sum by (pod) (vllm:num_requests_waiting{namespace="$NS",service="$SVC"}) or vector(0)
minStep: "15s"
per_pod_kv_pct_ts:
kind: Panel
spec:
display: { name: KV Cache (%) by Pod }
plugin:
kind: TimeSeriesChart
spec:
legend: { mode: table, position: bottom }
visual: { display: line, lineWidth: 1, areaOpacity: 0.3 }
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource: { kind: PrometheusDatasource, name: accelerators-thanos-querier-datasource }
# if your exporter labels kv metric with pod (the sim does), this works; otherwise it will just return empty
query: (avg by (pod) (vllm:kv_cache_usage_perc{namespace="$NS",service="$SVC"}) * 100) or vector(0)
minStep: "15s"
# --- Real vLLM only (zeros on simulator) ---
real_req_rate_ts:
kind: Panel
spec:
display: { name: Request Rate (real vLLM) }
plugin:
kind: TimeSeriesChart
spec:
legend: { mode: table, position: bottom }
visual: { display: line, lineWidth: 1, areaOpacity: 0.3 }
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource: { kind: PrometheusDatasource, name: accelerators-thanos-querier-datasource }
query: sum by (model_name) (rate(vllm:request_success_total{namespace="$NS",service="$SVC",model_name=~"$MODEL"}[$__interval])) or vector(0)
minStep: "15s"
real_p50:
kind: Panel
spec:
display: { name: p50 Latency (real vLLM) }
plugin: { kind: StatChart, spec: { calculation: last-number } }
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource: { kind: PrometheusDatasource, name: accelerators-thanos-querier-datasource }
query: histogram_quantile(0.50, sum by (le, model_name) (rate(vllm:e2e_request_latency_seconds_bucket{namespace="$NS",service="$SVC",model_name=~"$MODEL"}[$__interval]))) or vector(0)
minStep: "15s"
real_p90:
kind: Panel
spec:
display: { name: p90 Latency (real vLLM) }
plugin: { kind: StatChart, spec: { calculation: last-number } }
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource: { kind: PrometheusDatasource, name: accelerators-thanos-querier-datasource }
query: histogram_quantile(0.90, sum by (le, model_name) (rate(vllm:e2e_request_latency_seconds_bucket{namespace="$NS",service="$SVC",model_name=~"$MODEL"}[$__interval]))) or vector(0)
minStep: "15s"
real_p99:
kind: Panel
spec:
display: { name: p99 Latency (real vLLM) }
plugin: { kind: StatChart, spec: { calculation: last-number } }
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource: { kind: PrometheusDatasource, name: accelerators-thanos-querier-datasource }
query: histogram_quantile(0.99, sum by (le, model_name) (rate(vllm:e2e_request_latency_seconds_bucket{namespace="$NS",service="$SVC",model_name=~"$MODEL"}[$__interval]))) or vector(0)
minStep: "15s"
real_input_tokens_ts:
kind: Panel
spec:
display: { name: Input Tokens / sec (real vLLM) }
plugin:
kind: TimeSeriesChart
spec:
legend: { mode: table, position: bottom }
visual: { display: line, lineWidth: 1, areaOpacity: 0.3 }
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource: { kind: PrometheusDatasource, name: accelerators-thanos-querier-datasource }
query: sum by (model_name) (rate(vllm:prompt_tokens_total{namespace="$NS",service="$SVC",model_name=~"$MODEL"}[$__interval])) or vector(0)
minStep: "15s"
real_output_tokens_ts:
kind: Panel
spec:
display: { name: Output Tokens / sec (real vLLM) }
plugin:
kind: TimeSeriesChart
spec:
legend: { mode: table, position: bottom }
visual: { display: line, lineWidth: 1, areaOpacity: 0.3 }
queries:
- kind: TimeSeriesQuery
spec:
plugin:
kind: PrometheusTimeSeriesQuery
spec:
datasource: { kind: PrometheusDatasource, name: accelerators-thanos-querier-datasource }
query: sum by (model_name) (rate(vllm:generation_tokens_total{namespace="$NS",service="$SVC",model_name=~"$MODEL"}[$__interval])) or vector(0)
minStep: "15s"
layouts:
- kind: Grid
spec:
display: { title: Core (Sim & Real) }
items:
- { x: 0, y: 0, width: 6, height: 3, content: { $ref: '#/spec/panels/core_running_now' } }
- { x: 6, y: 0, width: 6, height: 3, content: { $ref: '#/spec/panels/core_waiting_now' } }
- { x: 12, y: 0, width: 6, height: 3, content: { $ref: '#/spec/panels/core_kv_usage_now' } }
- { x: 18, y: 0, width: 6, height: 3, content: { $ref: '#/spec/panels/core_targets_up' } }
- { x: 0, y: 3, width: 12, height: 6, content: { $ref: '#/spec/panels/core_running_ts' } }
- { x: 12, y: 3, width: 12, height: 6, content: { $ref: '#/spec/panels/core_waiting_ts' } }
- kind: Grid
spec:
display: { title: KV Cache (%) }
items:
- { x: 0, y: 9, width: 6, height: 3, content: { $ref: '#/spec/panels/core_kv_usage_pct_now' } }
- { x: 6, y: 9, width: 18, height: 6, content: { $ref: '#/spec/panels/core_kv_usage_pct_ts' } }
- kind: Grid
spec:
display: { title: Per-Pod breakdowns }
items:
- { x: 0, y: 15, width: 12, height: 6, content: { $ref: '#/spec/panels/per_pod_running_ts' } }
- { x: 12, y: 15, width: 12, height: 6, content: { $ref: '#/spec/panels/per_pod_waiting_ts' } }
- { x: 0, y: 21, width: 24, height: 6, content: { $ref: '#/spec/panels/per_pod_kv_pct_ts' } }
- kind: Grid
spec:
display: { title: Real vLLM only (shows 0 on simulator) }
items:
- { x: 0, y: 27, width: 12, height: 6, content: { $ref: '#/spec/panels/real_req_rate_ts' } }
- { x: 12, y: 27, width: 4, height: 3, content: { $ref: '#/spec/panels/real_p50' } }
- { x: 16, y: 27, width: 4, height: 3, content: { $ref: '#/spec/panels/real_p90' } }
- { x: 20, y: 27, width: 4, height: 3, content: { $ref: '#/spec/panels/real_p99' } }
- { x: 0, y: 33, width: 12, height: 6, content: { $ref: '#/spec/panels/real_input_tokens_ts' } }
- { x: 12, y: 33, width: 12, height: 6, content: { $ref: '#/spec/panels/real_output_tokens_ts' } }