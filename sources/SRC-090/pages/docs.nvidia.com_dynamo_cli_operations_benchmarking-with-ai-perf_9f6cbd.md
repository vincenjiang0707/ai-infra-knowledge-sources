source: https://docs.nvidia.com/dynamo/cli/operations/benchmarking-with-ai-perf
lastmod: 2026-09-24T19:58:16.636Z

# Benchmark a Local Deployment with AIPerf

AIPerf sends load to an OpenAI-compatible endpoint and measures latency and throughput. Use this tutorial after starting a local Dynamo frontend and at least one model worker.

AIPerf measures the live deployment. It does not predict a configuration like AIConfigurator or run a GPU-free simulation like Mocker and DynoSim.

## Prerequisites

Start a local deployment by following [Model Deployment](https://docs.nvidia.com/dynamo/cli/model-deployment/introduction). Confirm that the frontend is
available at `http://localhost:8000`

:

Install AIPerf on the machine that will generate load:

### Run a baseline benchmark

Set the model name to the value served by the local worker:

AIPerf writes artifacts to `artifacts/`

and prints a metrics summary. Record TTFT, Inter-Token
Latency (ITL), end-to-end latency, and output throughput.

### Compare local configurations

Change one deployment setting at a time, restart the affected workers, and rerun the same AIPerf command. Common comparisons include:

- one worker versus multiple replicas
- aggregated versus disaggregated serving
- KV-aware routing versus round-robin routing
- different TP or PP sizes recommended by AIConfigurator
- backend or engine-argument changes

Keep the request shape, concurrency, and request count fixed so that the results remain comparable. Then sweep concurrency to find the saturation point of the selected configuration.

## Next steps

- Use
[Sizing with AIConfigurator](https://docs.nvidia.com/dynamo/cli/disaggregated-serving/sizing-with-ai-configurator)to select additional configurations. - Use the full
[Dynamo Benchmarking guide](https://docs.nvidia.com/dynamo/recipes/benchmarks/benchmarking)for concurrency sweeps, arrival patterns, trace replay, visualization, and GPU telemetry.