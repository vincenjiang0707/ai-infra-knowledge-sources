source: https://docs.nvidia.com/dynamo/kubernetes/operations/dynosim/simulation-sweeps
lastmod: 2026-09-25T12:26:00.485Z

# Sweep DynoSim Configurations

A DynoSim sweep evaluates many simulated configurations and ranks candidates against latency and GPU
budget constraints. The sweep runs locally, but its candidates can be used for either Kubernetes or
local CLI deployment. Use a sweep after a single [DynoSim run](https://docs.nvidia.com/dynamo/kubernetes/operations/dynosim/simulation-runs) works and you want to identify
configurations to validate on real hardware.

The current Python API is `dynamo.profiler.utils.replay_optimize`

. For the input models, field names,
result object, and output columns, see the
[DynoSim Sweep Reference](https://docs.nvidia.com/dynamo/reference/components/dyno-sim-sweep-reference).

## Prerequisites

Run from the repository root. Build the runtime bindings and install the project:

The checked-in example uses AIConfigurator-backed timing. Install AIConfigurator into the project environment:

When running directly from the source checkout, expose the in-repository Python components and runtime bindings:

### Run the example sweep

Run the checked-in driver with four parallel evaluations:

The default example searches a synthetic disaggregated workload with a KV router. It prints the best feasible state and a table of highly ranked feasible configurations. The GPU budget is a simulated constraint; the machine running the sweep does not need that number of physical GPUs.

Start with a low parallel-evaluation count. Increase it only after confirming that the host has enough CPU and memory for concurrent trials.

### Inspect the result

Review the best feasible candidate and the evaluated table. At minimum, compare:

- prefill and decode tensor-parallel sizes
- prefill and decode worker counts
- total simulated GPUs
- output throughput
- TTFT, ITL, and end-to-end latency
- prefix-cache reuse
- router overlap and prefill-load settings

A candidate is feasible only when it meets every configured SLA and GPU-budget constraint. Keep the best infeasible result as a diagnostic: it can show which bound prevented an otherwise useful configuration from being selected.

### Run a sweep against a trace

Download the public FAST’25 tool-agent trace:

Run the same search against the trace:

The trace replaces the synthetic input-length, output-length, request-count, concurrency, and prefix
settings in the example. Keep `--arrival-speedup-ratio 1.0`

for the first run so the original arrival
shape remains unchanged.

### Customize the search

Copy the example driver and change one search dimension at a time. Common experiments include:

- changing
`HardwareSpec.totalGpus`

- adding TTFT, ITL, end-to-end latency, or p95 bounds to
`SLASpec`

- changing
`RouterSpec.overlapCredits`

- changing
`RouterSpec.prefillLoadScales`

- changing shared-prefix settings in
`WorkloadSpec`

- switching
`RouterSpec.mode`

to compare routing strategies - changing the base prefill or decode engine arguments

Run the modified script again and compare the feasible tables. Persist `evaluated_df`

and
`feasible_df`

to CSV or Parquet when you need repeatable analysis across multiple searches.

### Validate a candidate

A sweep is a heuristic search over simulated states, not an exhaustive proof that one configuration is optimal. Take the highest-ranked feasible candidates through these checks:

- Run the configuration again with
[Run a DynoSim Simulation](https://docs.nvidia.com/dynamo/kubernetes/operations/dynosim/simulation-runs). - Exercise the live frontend and router with
[Simulate a Local Deployment](https://docs.nvidia.com/dynamo/cli/operations/dynosim/mocker-live-simulation)or[Simulate a Kubernetes Deployment](https://docs.nvidia.com/dynamo/kubernetes/operations/dynosim/live-simulation-with-mocker). - Deploy the candidate on the target hardware and benchmark it with AIPerf using either the
[Kubernetes workflow](https://docs.nvidia.com/dynamo/kubernetes/operations/benchmarking-with-ai-perf)or the[local CLI workflow](https://docs.nvidia.com/dynamo/cli/operations/benchmarking-with-ai-perf).