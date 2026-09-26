source: https://docs.nvidia.com/dynamo/reference/components/dyno-sim-sweep-reference
lastmod: 2026-09-24T19:58:16.636Z

# DynoSim Sweep Reference

Input models, search behavior, and result fields for replay_optimize

`dynamo.profiler.utils.replay_optimize`

searches simulated deployment candidates by repeatedly
calling the DynoSim run harness. This page describes the Python API. For a guided workflow, see
[Sweep DynoSim Configurations](https://docs.nvidia.com/dynamo/cli/operations/dynosim/simulation-sweeps).

## Input models

The API takes a `ReplayOptimizeSpec`

with the following models and fields.

### EngineSpec

### HardwareSpec

The GPU budget is a search constraint. It is not a requirement for the host that executes the simulation.

### WorkloadSpec

`WorkloadSpec`

accepts either a synthetic workload or a trace.

Common synthetic fields include:

`isl`

`osl`

`requestCount`

`concurrency`

`sharedPrefixRatio`

`numPrefixGroups`


Trace workloads use `traceFile`

and can set `arrivalSpeedupRatio`

. Synthetic-only fields are ignored
when `traceFile`

is present. Mooncake-style traces use 512 tokens per `hash_id`

; the underlying
`run_trace_replay(...)`

API defaults `trace_block_size`

to `512`

. `WorkloadSpec`

does not currently
expose a separate `traceBlockSize`

field.

### SLASpec

`SLASpec`

can constrain:

- TTFT
- ITL
- end-to-end latency
- p95 variants of the supported latency bounds

Input fields use DynamoGraphDeploymentRequest-style lowerCamelCase names. The result DataFrames use
the DynoSim runner metric names described in [Result columns](https://docs.nvidia.com/dynamo/reference/components/dyno-sim-sweep-reference#result-columns).

### RouterSpec

### Search fields

## Search behavior

The optimizer searches tensor-parallel shapes, worker counts, and router settings under the GPU
budget. Each state is evaluated by the DynoSim run harness. States that violate any SLA or budget
constraint are retained as infeasible results but cannot become `best_feasible`

.

For disaggregated deployments, the search can vary prefill and decode tensor parallelism and worker counts independently. Aggregated searches use one tensor-parallel size and worker count.

The search is heuristic. It prioritizes states near the GPU-budget edge rather than exhaustively evaluating every possible configuration.

## Result object

`DenseReplayOptimizationResult`

contains:

## Result columns

Common DataFrame columns include:

`total_gpus_used`

is the simulated footprint of the candidate. It is not the number of physical GPUs
allocated to the process running the sweep.