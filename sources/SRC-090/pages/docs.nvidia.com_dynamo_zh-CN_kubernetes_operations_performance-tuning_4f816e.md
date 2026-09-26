source: https://docs.nvidia.com/dynamo/zh-CN/kubernetes/operations/performance-tuning
lastmod: 2026-09-24T19:58:16.636Z

# Advanced Performance Tuning

Measure a deployed configuration and tune the remaining workload-specific parameters

Use this guide after you have selected an initial deployment topology. It covers the workload-specific adjustments that remain after sizing, rather than repeating the complete sizing and deployment workflow.

Before tuning:

- Use
[Sizing with AIConfigurator](https://docs.nvidia.com/dynamo/kubernetes/disaggregated-serving/size-with-ai-configurator)to select tensor parallelism, pipeline parallelism, and initial replica counts. - Use
[Deploy with DGD](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/deploy-with-dgd)to apply those values to a Kubernetes deployment. - If you separate prefill and decode workers, follow
[Disaggregated Serving](https://docs.nvidia.com/dynamo/kubernetes/disaggregated-serving/overview)to configure and verify the KV transfer path first. - Establish a repeatable workload with
[Benchmarking with AIPerf](https://docs.nvidia.com/dynamo/kubernetes/operations/benchmarking-with-ai-perf).

The configuration produced by a sizing tool is a starting point. Actual request lengths, concurrency, prefix reuse, backend versions, and cluster networking can shift the best operating point.

## Tune with a representative workload

Use the same model, input sequence length (ISL), output sequence length (OSL), concurrency, and service-level objectives for every comparison. Change one parameter group at a time and record at least:

- Time To First Token (TTFT)
- Inter-Token Latency (ITL) or Time Per Output Token (TPOT)
- Request throughput and output-token throughput
- Prefill queue depth
- Decode KV-cache utilization
- GPU utilization and out-of-memory failures

Run multiple passes before accepting a result. A change that improves peak throughput can still be a regression if it violates the latency objective or reduces stability under sustained load.

## Tune the KV block size

KV block size affects both transfer efficiency and prefix-cache reuse:

- Smaller blocks improve cache granularity but create smaller KV-transfer chunks and more bookkeeping.
- Larger blocks improve transfer efficiency but can reduce the prefix-cache hit ratio by rounding reusable prefixes to coarser boundaries.

A KV block size of 128 tokens is a useful starting point for many dense-model disaggregated deployments, but the exact option name and supported values are backend-specific and 128 is not a universal optimum. Benchmark nearby supported values with the same prefix distribution and make sure prefill and decode workers use compatible KV layouts.

## Tune prefill capacity

A prefill worker normally minimizes TTFT when it runs at the smallest workload size that saturates the GPU. Very short prompts can underutilize the device, while very long prompts increase attention cost and absolute TTFT.

The following example shows that tradeoff for Llama 3.3 70B with NVFP4 quantization on a B200 using vLLM TP1 and prefix caching disabled:


Use AIPerf to find the saturation region for your own model and hardware. If prefill requests queue while decode capacity remains available, compare these changes separately:

- Add a prefill replica.
- Increase the amount of work admitted per prefill iteration using the backend’s supported batching or token-limit controls.
- Adjust the router’s local-versus-remote prefill policy. See
[Router Configuration and Tuning](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/configuration-and-tuning).

Prefer the smallest change that meets the TTFT target. Adding prefill replicas consumes GPUs that could otherwise provide decode KV-cache capacity.

## Tune decode capacity

Decode limits trade intermediate-buffer memory against KV-cache capacity. Larger batch and token limits can increase batching opportunities, but they also reserve more memory outside the KV cache. Reducing those limits can make room for more cached sequences, although limits that are too small can lower throughput.

Tune the backend’s maximum batch and token controls together:

- Start from the AIConfigurator or recipe values.
- Increase concurrency until decode KV-cache utilization or ITL reaches the target limit.
- Change one limit at a time and repeat the same workload.
- Reject configurations that improve throughput only by exceeding the ITL or TPOT objective.

Exact option names and defaults belong to the backend configuration references:
[vLLM](https://docs.nvidia.com/dynamo/reference/backends/v-llm-configuration),
[SGLang](https://docs.nvidia.com/dynamo/reference/backends/sg-lang-configuration), and
[TensorRT-LLM](https://docs.nvidia.com/dynamo/reference/backends/tensor-rt-llm-configuration).

## Adjust prefill and decode replicas

Treat replica counts as a response to observed bottlenecks rather than as fixed ratios:

For automated, metrics-driven redistribution between the pools, use the
[Planner](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/planner/planner-guide). For a fresh topology search, rerun
[AIConfigurator](https://docs.nvidia.com/dynamo/kubernetes/disaggregated-serving/size-with-ai-configurator) with workload parameters that match the
measured traffic.