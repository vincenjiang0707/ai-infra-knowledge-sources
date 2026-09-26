source: https://docs.vllm.ai/en/latest/api/vllm/config/observability/
lastmod: 2026-09-24

#

`vllm.config.observability`

[¶](https://docs.vllm.ai#vllm.config.observability)

Classes:

-
–[ObservabilityConfig](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig)Configuration for observability - metrics and tracing.


##

`ObservabilityConfig`

[¶](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig)

Configuration for observability - metrics and tracing.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.compute_hash)WARNING: Whenever a new field is added to this config,


Attributes:

-
([collect_detailed_traces](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.collect_detailed_traces)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[DetailedTraceModules] | NoneIt makes sense to set this only if

`--otlp-traces-endpoint`

is set. If -
([collect_model_execute_time](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.collect_model_execute_time)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to collect model execute time for the request.

-
([collect_model_forward_time](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.collect_model_forward_time)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to collect model forward time for the request.

-
([cudagraph_metrics](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.cudagraph_metrics)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable CUDA graph metrics (number of padded/unpadded tokens, runtime cudagraph

-
([enable_layerwise_nvtx_tracing](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.enable_layerwise_nvtx_tracing)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable layerwise NVTX tracing. This traces the execution of each layer or

-
([enable_logging_iteration_details](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.enable_logging_iteration_details)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable detailed logging of iteration details.

-
([enable_mfu_metrics](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.enable_mfu_metrics)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable Model FLOPs Utilization (MFU) metrics.

-
([enable_mm_processor_stats](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.enable_mm_processor_stats)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable collection of timing statistics for multimodal processor operations.

-
([jit_monitor_mode](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.jit_monitor_mode)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['warn', 'error']How to handle post-warmup JIT compilation events.

-
([jit_monitor_verbose](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.jit_monitor_verbose)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Log every monitored JIT compile with runtime details. This can emit many

-
([kv_cache_metrics](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.kv_cache_metrics)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Enable KV cache residency metrics (lifetime, idle time, reuse gaps).

-
([kv_cache_metrics_sample](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.kv_cache_metrics_sample)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Sampling rate for KV cache metrics (0.0, 1.0]. Default 0.01 = 1% of blocks.

-
([otlp_traces_endpoint](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.otlp_traces_endpoint)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneTarget URL to which OpenTelemetry traces will be sent.

-
([per_request_spec_decode_metrics](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.per_request_spec_decode_metrics)

) –[Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['none', 'summary', 'detailed']Include per-request speculative-decoding acceptance metrics in the

-
([show_hidden_metrics](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.show_hidden_metrics)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Check if the hidden metrics should be shown.

-
([show_hidden_metrics_for_version](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.show_hidden_metrics_for_version)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneEnable deprecated Prometheus metrics that have been hidden since the


## Source code in `vllm/config/observability.py`


|
|

###

`collect_detailed_traces = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.collect_detailed_traces)

It makes sense to set this only if `--otlp-traces-endpoint`

is set. If set, it will collect detailed traces for the specified modules. This involves use of possibly costly and or blocking operations and hence might have a performance impact.

Note that collecting detailed timing information for each request can be expensive.

###

`collect_model_execute_time`

`cached`

`property`

[¶](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.collect_model_execute_time)

Whether to collect model execute time for the request.

###

`collect_model_forward_time`

`cached`

`property`

[¶](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.collect_model_forward_time)

Whether to collect model forward time for the request.

###

`cudagraph_metrics = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.cudagraph_metrics)

Enable CUDA graph metrics (number of padded/unpadded tokens, runtime cudagraph dispatch modes, and their observed frequencies at every logging interval).

###

`enable_layerwise_nvtx_tracing = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.enable_layerwise_nvtx_tracing)

Enable layerwise NVTX tracing. This traces the execution of each layer or module in the model and attach information such as input/output shapes to nvtx range markers. Noted that this doesn't work with CUDA graphs enabled.

###

`enable_logging_iteration_details = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.enable_logging_iteration_details)

Enable detailed logging of iteration details. If set, vllm EngineCore will log iteration details This includes number of context/generation requests and tokens and the elapsed cpu time for the iteration.

###

`enable_mfu_metrics = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.enable_mfu_metrics)

Enable Model FLOPs Utilization (MFU) metrics.

###

`enable_mm_processor_stats = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.enable_mm_processor_stats)

Enable collection of timing statistics for multimodal processor operations. This is for internal use only (e.g., benchmarks) and is not exposed as a CLI argument.

###

`jit_monitor_mode = 'warn'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.jit_monitor_mode)

How to handle post-warmup JIT compilation events.

###

`jit_monitor_verbose = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.jit_monitor_verbose)

Log every monitored JIT compile with runtime details. This can emit many logs and add overhead, so it is intended for debugging.

###

`kv_cache_metrics = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.kv_cache_metrics)

Enable KV cache residency metrics (lifetime, idle time, reuse gaps). Uses sampling to minimize overhead. Requires log stats to be enabled (i.e., --disable-log-stats not set).

###

`kv_cache_metrics_sample = Field(default=0.01, gt=0, le=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.kv_cache_metrics_sample)

Sampling rate for KV cache metrics (0.0, 1.0]. Default 0.01 = 1% of blocks.

###

`otlp_traces_endpoint = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.otlp_traces_endpoint)

Target URL to which OpenTelemetry traces will be sent.

###

`per_request_spec_decode_metrics = 'none'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.per_request_spec_decode_metrics)

Include per-request speculative-decoding acceptance metrics in the response under `metrics.speculative_decoding`

. `none`

disables; `summary`

adds mean acceptance length, draft acceptance rate, and the step-by-draft-length histogram; `detailed`

additionally records the ordered per-step accepted/proposed arrays (one entry per verify step). Only reported for single-sequence requests (`n == 1`

), mirroring the timing metrics. No effect unless speculative decoding is enabled. Independent of `--disable-log-stats`

. This is the per-request response-body counterpart of the aggregate `vllm:spec_decode_*`

Prometheus metrics. The response field is experimental and its shape may change in a future release.

###

`show_hidden_metrics`

`cached`

`property`

[¶](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.show_hidden_metrics)

Check if the hidden metrics should be shown.

###

`show_hidden_metrics_for_version = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.show_hidden_metrics_for_version)

Enable deprecated Prometheus metrics that have been hidden since the specified version. For example, if a previously deprecated metric has been hidden since the v0.7.0 release, you use `--show-hidden-metrics-for-version=0.7`

as a temporary escape hatch while you migrate to new metrics. The metric is likely to be removed completely in an upcoming release.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.observability.ObservabilityConfig.compute_hash)

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.