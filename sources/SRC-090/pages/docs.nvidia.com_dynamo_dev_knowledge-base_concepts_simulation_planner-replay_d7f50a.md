source: https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/planner-replay
lastmod: 2026-09-24T19:58:16.636Z

# Benchmark Planner Decisions with DynoSim

Run the Dynamo Planner inside an offline DynoSim prediction to compare aggregated and disaggregated topologies, service-level objective (SLO) targets, and worker startup delays without a live cluster.

The production Planner scales Kubernetes or Global Planner deployments; it does not autoscale a
local deployment. `aisimulate predict --stack dynamo`

runs locally but evaluates Planner decisions
for the deployment described by its YAML input.

For the general workflow, see
[Run a DynoSim Simulation](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/simulation-runs). For
Planner field types and defaults, see the
[Planner Configuration reference](https://docs.nvidia.com/dynamo/dev/reference/components/planner-configuration). For
the simulation adapter, see
[DynoSim Architecture](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/dyno-sim-architecture#planner-simulation-adapter).

## Prerequisites

Build the Rust runtime bindings and install Dynamo from the repository root:

Use a release build because repeated simulation runs are CPU-bound.

### Run the aggregated baseline

Download the FAST’25 tool-agent trace:

Save this configuration as `planner-aggregated.yaml`

:

Run the prediction:

The command prints the summary and writes Planner decisions and metrics to
`planner-reports/aggregated/prediction.json`

.

### Run the disaggregated comparison

Copy the baseline, then replace its `engine`

mapping with separate prefill and decode roles:

Also replace the `planner`

mapping with role-specific minimums:

Save the result as `planner-disaggregated.yaml`

, then run it:

Compare request metrics, scaling events, and cumulative GPU time between the two
`prediction.json`

files.