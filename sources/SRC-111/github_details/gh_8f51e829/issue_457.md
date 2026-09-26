# [Issue #457] Support direct collection of vLLM metrics from Prometheus `/metrics` endpoint

source: https://github.com/vllm-project/guidellm/issues/457
state: open | updated: 2026-06-08T16:59:01Z
labels: 

## 正文

**Is your feature request related to a problem? Please describe.**
When benchmarking vLLM deployments with GuideLLM, I can only see client-side metrics (TTFT, ITL, throughput). I cannot directly observe server-side behavior like GPU cache usage, queue depths, or correlate performance degradation with resource saturation. It will be easier to understand why performance changes occur or to validate that client measurements align with server-side telemetry.

**Describe the solution you'd like**
Add support for collecting vLLM's native Prometheus metrics directly from the `/metrics` endpoint during benchmark runs. This would include:

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


## 评论 (7)

### albertoperdomo2 · 2025-11-11

cc: @sjmonson 

### natoscott · 2025-11-11

A more general alternative would be the inverse of this idea - exporting benchmark metrics through a new GuideLLM /metrics endpoint, while it is running, so that the many existing performance analysis and visualisation tools that understand timeseries data can more easily ingest it.

In order to do comprehensive analysis there is far more than vLLM metrics that need to be looked at (GPU, CPU, memory, storage, interconnect, system services like etcd, lmcache, databases, etc), and these tend to need more specialized tools that efficiently handle time series data.

### natoscott · 2025-11-11

> **Describe alternatives you've considered**
> I have ran Prometheus separately and manually correlate timestamps or wrote wrapper scripts around GuideLLM to scrape metrics.
> 
> These approaches lack the integration and convenience of having server metrics directly in GuideLLM's output.
> 

Another alternative I have had some success with is using PCP (you can use this alongside your existing Prometheus setup too).  There is a guidellm2pcp script which converts guidellm results into PCP metrics, for analysis alongside all of your system metrics (incl. vLLM), correctly interleaved with start/stop timestamps from each benchmark run.

You don't need to manually correlate timestamps this way, and if you use Claude or similar, you can do full-system benchmark analysis like this (the guidellm results are embedded in the PCP archives here):  https://github.com/natoscott/benchmarks/blob/main/vllm-kvcache-cpu-offload-eval/REPORT.md 


### albertoperdomo2 · 2025-11-12

I like both approaches, but I’m leaning toward the former. I’m clearly biased since I worked on a monitoring script for my GuideLLM runs that directly queries Prometheus, so having everything integrated there would be a nice touch.

As for the initial proposition of letting GuideLLM monitoring the `/metrics` endpoint itself, we should make sure the integration remains plug-and-play and doesn’t bring too much overhead to users who don’t run Prometheus i.e. query the `/metrics` endpoint directly. However, this could lead to larger output.json files. 

### natoscott · 2025-11-12

> I like both approaches, but I’m leaning toward the former.

If GuideLLM was to go down this path (I still wouldn't recommend it), it'd also be worth considering why use Prometheus exposition format over OpenTelemetry JSON format.  The latter would support both traces and metrics in GuideLLM output, and with OpenTelemetry using JSON as its default text-based format there's good symmetry with default GuideLLM output.

> I worked on a monitoring script for my GuideLLM runs that directly queries Prometheus, so having everything integrated there would be a nice touch.

You could push GuideLLM results into Prometheus at the end of each run (no need to change GuideLLM for this) - conceptually similar to the guidellm2pcp approach I mentioned.  The Prometheus exposition format allows timestamps to be included.  For PCP I write a record at the start time and again at the end time of all the benchmark results (as metrics), which allows the tools to query the GuideLLM results as they normally would any other metric, and Grafana can plot the benchmark results alongside system and vLLM activity.


### markurtz · 2025-11-19

Both generally interesting approaches, and from my side I definitely want to get the ability for GuideLLM to scrape metrics from the Prometheus endpoint. I'll add this onto the roadmap / map this out a bit more towards that and we can break this into two feature requests. Let me know if anyone is interested in trying to implement it and we can help guide through, otherwise will add it to the roadmap

### albertoperdomo2 · 2025-11-19

@markurtz I'm definitely down to give it a go, I might need guidance but it will be a fun feature to implement. 
