source: https://docs.nvidia.com/dynamo/zh-CN/v1.0.1/backends/tensor-rt-llm/prometheus-metrics
lastmod: 2026-09-23T23:30:39.914Z

# Prometheus

For general TensorRT-LLM features and configuration, see the [Reference Guide](https://docs.nvidia.com/dynamo/v1.0.1/backends/tensor-rt-llm/reference-guide).

## Overview

When running TensorRT-LLM through Dynamo, TensorRT-LLM’s Prometheus metrics are automatically passed through and exposed on Dynamo’s `/metrics`

endpoint (default port 8081). This allows you to access both TensorRT-LLM engine metrics (prefixed with `trtllm_`

) and Dynamo runtime metrics (prefixed with `dynamo_*`

) from a single worker backend endpoint.

Additional performance metrics are available via non-Prometheus APIs (see [Non-Prometheus Performance Metrics](https://docs.nvidia.com/dynamo/v1.0.1/backends/tensor-rt-llm/prometheus-metrics#non-prometheus-performance-metrics) below).

As of the date of this documentation, the included TensorRT-LLM version 1.1.0rc5 exposes **5 basic Prometheus metrics**. Note that the `trtllm_`

prefix is added by Dynamo.

**For Dynamo runtime metrics**, see the [Dynamo Metrics Guide](https://docs.nvidia.com/dynamo/v1.0.1/user-guides/observability-local/metrics).

**For visualization setup instructions**, see the [Prometheus and Grafana Setup Guide](https://docs.nvidia.com/dynamo/v1.0.1/user-guides/observability-local/prometheus-grafana-setup).

## Environment Variables

## Getting Started Quickly

This is a single machine example.

### Start Observability Stack

For visualizing metrics with Prometheus and Grafana, start the observability stack. See [Observability Getting Started](https://docs.nvidia.com/dynamo/v1.0.1/user-guides/observability-local#getting-started-quickly) for instructions.

### Launch Dynamo Components

Launch a frontend and TensorRT-LLM backend to test metrics:

**Note:** The `backend`

must be set to `"pytorch"`

for metrics collection (enforced in `components/src/dynamo/trtllm/main.py`

). TensorRT-LLM’s `MetricsCollector`

integration has only been tested/validated with the PyTorch backend.

Wait for the TensorRT-LLM worker to start, then send requests and check metrics:

## Exposed Metrics

TensorRT-LLM exposes metrics in Prometheus Exposition Format text at the `/metrics`

HTTP endpoint. All TensorRT-LLM engine metrics use the `trtllm_`

prefix and include labels (e.g., `model_name`

, `engine_type`

, `finished_reason`

) to identify the source.

**Note:** TensorRT-LLM uses `model_name`

instead of Dynamo’s standard `model`

label convention.

**Example Prometheus Exposition Format text:**

**Note:** The specific metrics shown above are examples and may vary depending on your TensorRT-LLM version. Always inspect your actual `/metrics`

endpoint for the current list.

### Metric Categories

TensorRT-LLM provides metrics in the following categories (all prefixed with `trtllm_`

):

**Request metrics**- Request success tracking and latency measurements**Performance metrics**- Time to first token (TTFT), time per output token (TPOT), and queue time

**Note:** Metrics may change between TensorRT-LLM versions. Always inspect the `/metrics`

endpoint for your version.

## Available Metrics

The following metrics are exposed via Dynamo’s `/metrics`

endpoint (with the `trtllm_`

prefix added by Dynamo) for TensorRT-LLM version 1.1.0rc5:

`trtllm_request_success_total`

(Counter) — Count of successfully processed requests by finish reason- Labels:
`model_name`

,`engine_type`

,`finished_reason`


- Labels:
`trtllm_e2e_request_latency_seconds`

(Histogram) — End-to-end request latency (seconds)- Labels:
`model_name`

,`engine_type`


- Labels:
`trtllm_time_to_first_token_seconds`

(Histogram) — Time to first token, TTFT (seconds)- Labels:
`model_name`

,`engine_type`


- Labels:
`trtllm_time_per_output_token_seconds`

(Histogram) — Time per output token, TPOT (seconds)- Labels:
`model_name`

,`engine_type`


- Labels:
`trtllm_request_queue_time_seconds`

(Histogram) — Time a request spends waiting in the queue (seconds)- Labels:
`model_name`

,`engine_type`


- Labels:

These metric names and availability are subject to change with TensorRT-LLM version updates.

TensorRT-LLM provides Prometheus metrics through the `MetricsCollector`

class (see [tensorrt_llm/metrics/collector.py](https://github.com/NVIDIA/TensorRT-LLM/blob/main/tensorrt_llm/metrics/collector.py)).

### Additional Operational Metrics

Dynamo adds the following operational metrics for TensorRT-LLM workers. These complement the engine’s native metrics above with request-level observability that the engine does not provide. All metrics use the `trtllm_`

prefix and are automatically enabled when `--publish-events-and-metrics`

is set.

Metric name constants are defined in `lib/runtime/src/metrics/prometheus_names.rs`

(`trtllm_additional`

module).

#### Request Type Tracking

`trtllm_request_type_image_total`

(Counter) — Total number of requests containing image/multimodal content- Labels:
`model_name`

,`disaggregation_mode`

,`engine_type`


- Labels:
`trtllm_request_type_structured_output_total`

(Counter) — Total number of requests using guided/structured decoding (JSON, regex, grammar, etc.)- Labels:
`model_name`

,`disaggregation_mode`

,`engine_type`


- Labels:

#### Abort Tracking

`trtllm_num_aborted_requests_total`

(Counter) — Total number of aborted/cancelled requests- Labels:
`model_name`

,`disaggregation_mode`

,`engine_type`


- Labels:

#### KV Cache Transfer Metrics (Disaggregated Deployments)

These metrics are only recorded in disaggregated (prefill + decode) deployments when a KV cache transfer actually occurs. They are sourced from TensorRT-LLM’s `RequestPerfMetrics.timing_metrics`

.

`trtllm_kv_transfer_success_total`

(Counter) — Total number of successful KV cache transfers (recorded on prefill side)- Labels:
`model_name`

,`disaggregation_mode`

,`engine_type`


- Labels:
`trtllm_kv_transfer_latency_seconds`

(Histogram) — KV cache transfer latency per request in seconds- Labels:
`model_name`

,`disaggregation_mode`

,`engine_type`


- Labels:
`trtllm_kv_transfer_bytes`

(Histogram) — KV cache transfer size per request in bytes- Labels:
`model_name`

,`disaggregation_mode`

,`engine_type`

- Buckets: 100KB, 500KB, 1MB, 5MB, 10MB, 50MB, 100MB, 500MB, 1GB, 5GB

- Labels:
`trtllm_kv_transfer_speed_gb_s`

(Histogram) — KV cache transfer speed per request in GB/s- Labels:
`model_name`

,`disaggregation_mode`

,`engine_type`


- Labels:

## Non-Prometheus Performance Metrics

TensorRT-LLM provides extensive performance data beyond the basic Prometheus metrics. These are not currently exposed to Prometheus.

### Available via Code References

**RequestPerfMetrics Structure**:[tensorrt_llm/executor/result.py](https://github.com/NVIDIA/TensorRT-LLM/blob/main/tensorrt_llm/executor/result.py)- KV cache, timing, speculative decoding metrics**Engine Statistics**:`engine.llm.get_stats_async()`

- System-wide aggregate statistics**KV Cache Events**:`engine.llm.get_kv_cache_events_async()`

- Real-time cache operations

### Example RequestPerfMetrics JSON Structure

**Note:** These structures are valid as of the date of this documentation but are subject to change with TensorRT-LLM version updates.

## Implementation Details

**Prometheus Integration**: Uses the`MetricsCollector`

class from`tensorrt_llm.metrics`

(see[collector.py](https://github.com/NVIDIA/TensorRT-LLM/blob/main/tensorrt_llm/metrics/collector.py))**Dynamo Integration**: Uses`register_engine_metrics_callback()`

function with`metric_prefix_filter=["trtllm_"]`

**Engine Configuration**:`return_perf_metrics`

set to`True`

when`--publish-events-and-metrics`

is enabled**Initialization**: Metrics appear after TensorRT-LLM engine initialization completes**Metadata**:`MetricsCollector`

initialized with model metadata (model name, engine type)

## Related Documentation

### TensorRT-LLM Metrics

- See the
[Non-Prometheus Performance Metrics](https://docs.nvidia.com/dynamo/v1.0.1/backends/tensor-rt-llm/prometheus-metrics#non-prometheus-performance-metrics)section above for detailed performance data and source code references [TensorRT-LLM Metrics Collector](https://github.com/NVIDIA/TensorRT-LLM/blob/main/tensorrt_llm/metrics/collector.py)- Source code reference

### Dynamo Metrics

[Dynamo Metrics Guide](https://docs.nvidia.com/dynamo/v1.0.1/user-guides/observability-local/metrics)- Complete documentation on Dynamo runtime metrics[Prometheus and Grafana Setup](https://docs.nvidia.com/dynamo/v1.0.1/user-guides/observability-local/prometheus-grafana-setup)- Visualization setup instructions- Dynamo runtime metrics (prefixed with
`dynamo_*`

) are available at the same`/metrics`

endpoint alongside TensorRT-LLM metrics- Implementation:
`lib/runtime/src/metrics.rs`

(Rust runtime metrics) - Metric names:
`lib/runtime/src/metrics/prometheus_names.rs`

(metric name constants) - Integration code:
`components/src/dynamo/common/utils/prometheus.py`

- Prometheus utilities and callback registration

- Implementation: