source: https://docs.nvidia.com/dynamo/zh-CN/kubernetes/operations/benchmarking-with-ai-perf
lastmod: 2026-09-24T19:58:16.636Z

# Benchmark a Kubernetes Deployment with AIPerf

AIPerf sends load to an OpenAI-compatible endpoint and measures latency and throughput. Use this tutorial after deploying a model with a DynamoGraphDeployment (DGD).

AIPerf measures the live deployment. It does not predict a configuration like AIConfigurator or run a GPU-free simulation like Mocker and DynoSim.

## Prerequisites

Install AIPerf on the workstation or benchmark host:

Set the namespace and forward the DGD frontend service to port 8000:

The service name is the DGD `metadata.name`

followed by `-frontend`

.

### Run a baseline benchmark

In another terminal, set `--model`

to the model name served by the deployment:

AIPerf writes artifacts to `artifacts/`

and prints a metrics summary. Record Time to First Token
(TTFT), Inter-Token Latency (ITL), end-to-end latency, and output throughput.

### Compare Kubernetes configurations

Change one deployment setting at a time, wait for the DGD to become ready, and rerun the same AIPerf command. Common comparisons include:

- aggregated versus disaggregated serving
- KV-aware versus round-robin routing
- different worker replica counts
- different TP or PP sizes recommended by AIConfigurator
- backend or engine-argument changes

Keep the request shape, concurrency, and request count fixed so the results remain comparable. Then sweep concurrency to find the saturation point of the selected deployment.

## Next steps

- Use
[Sizing with AIConfigurator](https://docs.nvidia.com/dynamo/kubernetes/disaggregated-serving/size-with-ai-configurator)to select additional DGD configurations. - Use the full
[Dynamo Benchmarking guide](https://docs.nvidia.com/dynamo/recipes/benchmarks/benchmarking)for in-cluster load generation, concurrency sweeps, arrival patterns, trace replay, visualization, and GPU telemetry. - Start from a
[Dynamo Recipe](https://github.com/ai-dynamo/dynamo/tree/v1.4.2/recipes)when a supported model and hardware combination already has a known-good baseline.