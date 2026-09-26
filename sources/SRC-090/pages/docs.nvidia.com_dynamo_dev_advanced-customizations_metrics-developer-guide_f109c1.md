source: https://docs.nvidia.com/dynamo/dev/advanced-customizations/metrics-developer-guide
lastmod: 2026-09-24T19:58:16.636Z

# Metrics Developer Guide

Reference for creating counters, gauges, and histograms with Dynamo’s metrics API, surfaced on the local /metrics endpoint.

This guide explains how to create and use custom metrics in Dynamo components using the Dynamo metrics API.

## Metrics Exposure

All metrics created via the Dynamo metrics API are automatically exposed on the `/metrics`

HTTP endpoint in Prometheus Exposition Format text when the following environment variable is set:

`DYN_SYSTEM_PORT=<port>`

- Port for the metrics endpoint (set to positive value to enable, default:`-1`

disabled)

Example:

Prometheus Exposition Format text metrics will be available at: `http://localhost:8081/metrics`


## Metric Name Constants

The [prometheus_names.rs](https://github.com/ai-dynamo/dynamo/tree/main/lib/runtime/src/metrics/prometheus_names.rs) module provides centralized metric name constants and sanitization functions to ensure consistency across all Dynamo components.

## Metrics API in Rust

The metrics API is accessible through the `.metrics()`

method on runtime, namespace, component, and endpoint objects.

### Available Methods

`.metrics().create_counter()`

: Create a counter metric`.metrics().create_gauge()`

: Create a gauge metric`.metrics().create_histogram()`

: Create a histogram metric`.metrics().create_countervec()`

: Create a counter with labels`.metrics().create_gaugevec()`

: Create a gauge with labels`.metrics().create_histogramvec()`

: Create a histogram with labels

### Creating Metrics

### Using Metrics

### Vector Metrics with Labels

### Advanced Features

**Custom histogram buckets:**

**Constant labels:**