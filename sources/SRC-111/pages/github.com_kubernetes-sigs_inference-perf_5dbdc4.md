source: https://github.com/kubernetes-sigs/inference-perf

Inference Perf is a production-scale GenAI inference performance benchmarking tool that allows you to benchmark and analyze the performance of inference deployments. It is agnostic of model servers and can be used to measure performance and compare different systems apples-to-apples.

It was founded as a part of the inference benchmarking and metrics standardization effort in [wg-serving](https://github.com/kubernetes/community/tree/master/wg-serving) to standardize the [benchmark tooling](https://github.com/kubernetes-sigs/wg-serving/tree/main/proposals/013-inference-perf) and the [metrics](https://docs.google.com/document/d/1SpSp1E6moa4HSrJnS4x3NpLuj88sMXr2tbofKlzTZpk/edit?usp=sharing&resourcekey=0-ob5dR-AJxLQ5SvPlA4rdsg) used to measure inference performance across the Kubernetes and model server communities.

**Comprehensive Latency Metrics**: TTFT, TPOT, ITL, and Normalized TPOT.**Throughput Tracking**: Input, Output, and Total tokens per second.**Goodput Measurement**: Measure rate of requests meeting your SLO constraints. See[goodput.md](https://github.com/kubernetes-sigs/inference-perf/blob/main/docs/goodput.md).**Automatic Visualization**: Generate charts for QPS vs Latency/Throughput/Goodput. See[analysis.md](https://github.com/kubernetes-sigs/inference-perf/blob/main/docs/analysis.md).

**Real-world Datasets**: Support for ShareGPT, CNN DailyMail, Infinity Instruct, Billsum, and the VisionArena image dataset.**Synthetic & Random**: Configure exact input/output distributions.**Advanced Scenarios**: Shared prefix and multi-turn chat conversations.**Multimodal**: Synthetic image, video, and audio payloads with per-modality reporting. Resolutions/profiles/durations are passed through as-is; pick values within your model's accepted range. See[docs/config.md](https://github.com/kubernetes-sigs/inference-perf/blob/main/docs/config.md#multimodal-data-generation).

**Load Patterns**: Constant rate, Poisson arrival, and concurrent user simulation.**Multi-Stage Runs**: Define stages with varying rates and durations to find saturation points.**Trace Replay**: Replay real-world traces (e.g., Azure dataset) or OpenTelemetry traces with agentic tree-of-thought simulation and visualization.

**10k+ QPS**: Scalable to very high load due to optimized multi-process architecture.**Automatic Saturation Detection**: Find the limits of your system via sweeps.

- Verified support for
**vLLM**,**SGLang**, and**TGI**with server side aggregate metrics and time series metrics. - Easily extensible to any OpenAI-compatible endpoint.

-
Install

`inference-perf`

:pip install inference-perf

-
Run a benchmark with a simple random workload:

inference-perf --server.type vllm --server.base_url http://localhost:8000 --data.type random --load.type constant --load.stages '[{"rate": 10, "duration": 60}]' --api.streaming true


Alternatively, you can run using a configuration file:

`inference-perf --config_file config.yml`

When you run `inference-perf`

, it displays a rich summary table in the CLI:

`docker run -it --rm -v $(pwd)/config.yml:/workspace/config.yml quay.io/inference-perf/inference-perf`

Refer to the [guide](https://github.com/kubernetes-sigs/inference-perf/blob/main/deploy/README.md) in `/deploy`

.

Explore detailed documentation for specific topics:

| Topic | Description | Link |
|---|---|---|
Configuration |
Full YAML configuration schema and options. |
|

**CLI Flags**[cli_flags.md](https://github.com/kubernetes-sigs/inference-perf/blob/main/docs/cli_flags.md)**Load Generation**[loadgen.md](https://github.com/kubernetes-sigs/inference-perf/blob/main/docs/loadgen.md)**Collected Metrics**[metrics.md](https://github.com/kubernetes-sigs/inference-perf/blob/main/docs/metrics.md)**Emitted Metrics**[runtime_metrics.md](https://github.com/kubernetes-sigs/inference-perf/blob/main/docs/runtime_metrics.md)**Comparability**[comparability.md](https://github.com/kubernetes-sigs/inference-perf/blob/main/docs/comparability.md)**Goodput**[goodput.md](https://github.com/kubernetes-sigs/inference-perf/blob/main/docs/goodput.md)**Reports**[reports.md](https://github.com/kubernetes-sigs/inference-perf/blob/main/docs/reports.md)**OTel Observability**[otel_instrumentation.md](https://github.com/kubernetes-sigs/inference-perf/blob/main/docs/otel_instrumentation.md)**OTel Trace Replay**[otel_trace_replay.md](https://github.com/kubernetes-sigs/inference-perf/blob/main/docs/otel_trace_replay.md)**Synthetic Agentic***(implementation in progress)*[synthetic_agentic.md](https://github.com/kubernetes-sigs/inference-perf/blob/main/docs/synthetic_agentic.md)**Weka Trace Replay**[weka_trace_replay.md](https://github.com/kubernetes-sigs/inference-perf/blob/main/docs/weka_trace_replay.md)**Conversation Replay**[conversation_replay.md](https://github.com/kubernetes-sigs/inference-perf/blob/main/docs/conversation_replay.md)**BR0.2 Reports**[br_v0_2.md](https://github.com/kubernetes-sigs/inference-perf/blob/main/docs/br_v0_2.md)**Analysis**[analysis.md](https://github.com/kubernetes-sigs/inference-perf/blob/main/docs/analysis.md)**E2E Tests**[e2e_tests.md](https://github.com/kubernetes-sigs/inference-perf/blob/main/docs/e2e_tests.md)We welcome contributions! Please join us:

**Slack**:[#inference-perf](https://kubernetes.slack.com/?redir=%2Fmessages%2Finference-perf)channel in[Kubernetes workspace](https://slack.k8s.io/).**Community Meeting**: Weekly on Thursdays alternating between 09:00 and 11:30 PDT.**Code of Conduct**: Governed by the[Kubernetes Code of Conduct](https://github.com/kubernetes-sigs/inference-perf/blob/main/code-of-conduct.md).

See [CONTRIBUTING.md](https://github.com/kubernetes-sigs/inference-perf/blob/main/CONTRIBUTING.md) for details on how to get started.