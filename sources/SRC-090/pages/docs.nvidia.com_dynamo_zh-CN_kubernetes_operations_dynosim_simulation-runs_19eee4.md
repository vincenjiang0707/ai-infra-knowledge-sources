source: https://docs.nvidia.com/dynamo/zh-CN/kubernetes/operations/dynosim/simulation-runs
lastmod: 2026-09-24T19:58:16.636Z

# Run a DynoSim Simulation

A DynoSim run evaluates one workload against one simulated Dynamo configuration. This is an
**offline replay**: the harness drives simulated engine cores directly without starting a frontend,
registering workers, or sending HTTP requests. The command runs on your local machine, but the
configuration you evaluate can be a candidate for either Kubernetes or local CLI deployment. It
does not require GPUs and produces an AIPerf-style summary plus a JSON report.

Use [Simulate a Local Deployment with Mocker](https://docs.nvidia.com/dynamo/cli/operations/dynosim/mocker-live-simulation) instead when you need to exercise the
live Dynamo frontend, discovery, routing, event publication, and worker lifecycle.

Use this tutorial to establish a working baseline before changing topology, routing, or timing
settings. For all flags, trace fields, constraints, and report fields, see the
[DynoSim Replay CLI Reference](https://docs.nvidia.com/dynamo/reference/components/dyno-sim-replay-cli-reference). For the internal
execution model, see [DynoSim Architecture](https://docs.nvidia.com/dynamo/knowledge-base/concepts/simulation/dyno-sim-architecture).

## Prerequisites

Run the commands from the repository root. Use the project virtual environment and build the runtime bindings if they are not already available:

The release build is recommended because the simulation is CPU-bound.

### Run a synthetic workload

Start with a small aggregated simulation:

The command prints a latency and throughput table. Confirm that all requests completed and that
`/tmp/dynosim-synthetic.json`

was created.

### Add prefix reuse and multiple turns

Run a second synthetic workload with shared prefixes and three turns per session:

Compare the prefix-cache reuse and latency metrics with the first run. Keep the worker count and engine arguments fixed so the workload change is the only variable.

### Replay a saved trace

Download the public FAST’25 tool-agent trace:

Replay it with the trace block size used by the dataset:

`--trace-block-size`

describes how the trace encodes `hash_ids`

. The engine `block_size`

describes
the simulated KV-cache block size, so the two values do not need to match.

### Compare routing modes

Run the same trace through the KV router. Change only the routing settings:

Compare `/tmp/dynosim-trace.json`

and `/tmp/dynosim-kv-router.json`

. Review throughput, Time to First
Token (TTFT), Inter-Token Latency (ITL), and prefix-cache reuse before deciding whether the routing
change is promising.

### Simulate disaggregated serving

Use separate prefill and decode worker pools and engine arguments:

Compare this report with the aggregated baseline. If the result is worth exploring, use
[Sweep DynoSim Configurations](https://docs.nvidia.com/dynamo/kubernetes/operations/dynosim/simulation-sweeps) to search more worker and topology combinations.

### Validate the result

DynoSim models scheduler, KV-cache, routing, and timing behavior, but it does not replace a
real-hardware benchmark. Validate the candidate with AIPerf against either a
[Kubernetes deployment](https://docs.nvidia.com/dynamo/kubernetes/operations/benchmarking-with-ai-perf) or a [local CLI deployment](https://docs.nvidia.com/dynamo/cli/operations/benchmarking-with-ai-perf) to include
frontend, transport, engine, and GPU behavior.