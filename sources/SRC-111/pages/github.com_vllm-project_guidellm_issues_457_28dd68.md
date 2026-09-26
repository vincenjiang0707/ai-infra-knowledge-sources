source: https://github.com/vllm-project/guidellm/issues/457

**Is your feature request related to a problem? Please describe.**

When benchmarking vLLM deployments with GuideLLM, I can only see client-side metrics (TTFT, ITL, throughput). I cannot directly observe server-side behavior like GPU cache usage, queue depths, or correlate performance degradation with resource saturation. It will be easier to understand why performance changes occur or to validate that client measurements align with server-side telemetry.

**Describe the solution you'd like**

Add support for collecting vLLM's native Prometheus metrics directly from the `/metrics`

endpoint during benchmark runs. This would include:

- Queue metrics: vllm:num_requests_running, vllm:num_requests_waiting
- Resource utilization: vllm:gpu_cache_usage_perc
- Server-side latencies: vllm:time_to_first_token_seconds_bucket, vllm:time_per_output_token_seconds_bucket
- Request outcomes: vllm:request_success_total

Proposed usage:

```
guidellm \
--target http://localhost:8000/v1 \
--model meta-llama/Llama-3.1-8B-Instruct \
--prometheus-endpoint http://localhost:8000/metrics \
--prometheus-scrape-interval 5s
```


The benchmark report would include these metrics time-correlated with client-side measurements, enabling comprehensive performance analysis.

**Describe alternatives you've considered**

I have ran Prometheus separately and manually correlate timestamps or wrote wrapper scripts around GuideLLM to scrape metrics.

These approaches lack the integration and convenience of having server metrics directly in GuideLLM's output.

**Additional context**

vLLM exposes comprehensive Prometheus metrics documented [here](https://docs.vllm.ai/en/latest/design/metrics/#metrics)

Is your feature request related to a problem? Please describe.When benchmarking vLLM deployments with GuideLLM, I can only see client-side metrics (TTFT, ITL, throughput). I cannot directly observe server-side behavior like GPU cache usage, queue depths, or correlate performance degradation with resource saturation. It will be easier to understand why performance changes occur or to validate that client measurements align with server-side telemetry.

Describe the solution you'd likeAdd support for collecting vLLM's native Prometheus metrics directly from the

`/metrics`

endpoint during benchmark runs. This would include:Proposed usage:

The benchmark report would include these metrics time-correlated with client-side measurements, enabling comprehensive performance analysis.

Describe alternatives you've consideredI have ran Prometheus separately and manually correlate timestamps or wrote wrapper scripts around GuideLLM to scrape metrics.

These approaches lack the integration and convenience of having server metrics directly in GuideLLM's output.

Additional contextvLLM exposes comprehensive Prometheus metrics documented here