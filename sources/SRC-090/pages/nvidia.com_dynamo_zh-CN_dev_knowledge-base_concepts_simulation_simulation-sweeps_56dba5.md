source: https://docs.nvidia.com/dynamo/zh-CN/dev/knowledge-base/concepts/simulation/simulation-sweeps
lastmod: 2026-09-23T23:30:39.914Z

# Sweep DynoSim Configurations

`aisimulate recommend --stack dynamo`

searches simulated deployment configurations and writes each
selected candidate as a concrete prediction YAML. The search runs offline on CPUs; the GPU count is
a simulated constraint rather than a host requirement.

Use recommendation after a single [DynoSim prediction](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/simulation-runs) works. For field and
domain semantics, see the
[DynoSim Sweep Reference](https://docs.nvidia.com/dynamo/dev/reference/components/dyno-sim-sweep-reference).

## Prerequisites

Run from the repository root. Build the runtime bindings and install Dynamo, which installs the pinned AISimulate release:

Do not install the standalone `aiconfigurator`

package. AISimulate includes the performance-model
compatibility code used by the Dynamo stack.

### Create a recommendation configuration

Save this configuration as `/tmp/dynosim-recommend.yaml`

:

Each parallelism preset is a complete mapping and becomes one categorical choice. Router and scheduler domains add independent search dimensions.

### Run the recommendation

The command prints ranked candidates and writes concrete files under
`/tmp/dynosim-recommendations/recommendations/`

.

### Predict the best candidate

Pass the highest-ranked recommendation directly to `predict`

:

Compare the prediction metrics with the baseline before deploying the candidate.

### Search against a trace

Download the public FAST’25 tool-agent trace:

Override the workload while retaining the engine and search domains:

Use a shorter virtual-time cutoff or trial budget while iterating on large traces.

### Customize the objective

Set `optimization.target`

to `throughput`

, `throughput_per_gpu`

, `throughput_per_user`

, `goodput`

,
`goodput_per_gpu`

, `ttft`

, `e2e_latency`

, or `pareto`

. Goodput targets require `evaluation.sla`

.
Pareto output contains the complete nondominated front rather than a scalar ranking.

Change one domain at a time. Use `choices`

for categorical values, `range`

for numeric domains, and
complete preset mappings for correlated knobs such as parallelism.

### Validate a candidate

A recommendation is a heuristic simulation result, not proof of optimality. Run the generated YAML
through `aisimulate predict`

, then deploy the candidate on its target hardware and benchmark it with
AIPerf using either the
[Kubernetes workflow](https://docs.nvidia.com/dynamo/dev/kubernetes/operations/benchmarking-with-ai-perf) or the
[local workflow](https://docs.nvidia.com/dynamo/dev/cli/operations/benchmarking-with-ai-perf).