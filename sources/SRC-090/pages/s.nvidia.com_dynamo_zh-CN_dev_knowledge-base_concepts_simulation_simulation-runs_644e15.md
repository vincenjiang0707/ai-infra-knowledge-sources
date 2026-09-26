source: https://docs.nvidia.com/dynamo/zh-CN/dev/knowledge-base/concepts/simulation/simulation-runs
lastmod: 2026-09-23T23:30:39.914Z

# Run a DynoSim Simulation

A DynoSim prediction evaluates one workload against one simulated Dynamo configuration. AISimulate drives the simulated engine cores directly without starting a frontend, registering workers, or sending HTTP requests. It runs on CPUs and writes an AIPerf-style summary and JSON report.

For live simulation with registered Mocker workers, see
[Simulate a Local Deployment with Mocker](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/local-mocker). The former public Replay
online CLI remains unavailable, although the Python replay SDK retains online mode. For the
configuration and output contract, see the
[DynoSim Replay CLI Reference](https://docs.nvidia.com/dynamo/dev/reference/components/dyno-sim-replay-cli-reference). For
the internal execution model, see
[DynoSim Architecture](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/dyno-sim-architecture).

## Prerequisites

Run the commands from the repository root. Build the runtime bindings and install Dynamo into the project virtual environment:

Use a release build because simulation is CPU-bound.

### Run a synthetic workload

Save this configuration as `/tmp/dynosim-synthetic.yaml`

:

Run the prediction through the Dynamo stack:

Confirm that all requests completed and that `/tmp/dynosim-synthetic/prediction.json`

exists.

### Add prefix reuse and multiple turns

Override the synthetic source with three-turn sessions. `--set`

parses its right-hand side as YAML
and applies it after loading the file:

Compare the prefix-cache reuse and latency metrics with the independent-request run.

### Replay a saved trace

Download the public FAST’25 tool-agent trace:

Override the workload mappings while keeping the engine configuration fixed:

`traffic.source.block_size`

describes the trace hash granularity. The simulated KV-cache block size
remains `engine.workers.aggregated.kv_cache.block_size: 64`

.

### Compare routing modes

Run the same trace through four workers and the KV router:

Compare `/tmp/dynosim-trace/prediction.json`

with
`/tmp/dynosim-kv-router/prediction.json`

. Review throughput, Time to First Token (TTFT), Inter-Token
Latency (ITL), and prefix-cache reuse.

### Simulate disaggregated serving

Save a disaggregated configuration as `/tmp/dynosim-disaggregated.yaml`

:

Run the disaggregated prediction:

Compare the result with the aggregated baseline. To search topology and parallelism choices, use
[Sweep DynoSim Configurations](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/simulation-sweeps).

### Validate the result

DynoSim models scheduler, KV-cache, routing, and timing behavior, but it does not replace a
real-hardware benchmark. Validate the candidate with AIPerf against either a
[Kubernetes deployment](https://docs.nvidia.com/dynamo/dev/kubernetes/operations/benchmarking-with-ai-perf) or a
[local deployment](https://docs.nvidia.com/dynamo/dev/cli/operations/benchmarking-with-ai-perf).