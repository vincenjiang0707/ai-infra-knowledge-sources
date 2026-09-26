source: https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/ai-simulate/sweeper/results
lastmod: 2026-09-24T19:58:16.636Z

# Sweeper Results

**Experimental.** Sweeper’s replay and result contracts may change without a standard deprecation
period.

Sweeper materializes every optimizer suggestion in the main process. It unrolls the backend
selection, asks each configured provider for its concrete adapter configuration and runtime hooks,
then constructs a `ReplaySpec`

.

## Replay Specification

`ReplaySpec`

version 1 contains:

- a
`BackendDeploymentSpec`

with topology, backend version, engine arguments, and worker counts; - the validated workload and optimization goal;
- concrete concurrency when KV-load search derives it;
- concrete adapter configurations and their runtime hooks.

`RunnerCapabilities.require_compatible`

checks the version, backend/topology pair, and hooks before
execution. `canonical_json`

creates deterministic strict JSON and rejects non-finite values.

## Candidate Output

For a scalar goal, `Sweeper.run`

returns feasible `Candidate`

objects sorted best-first. Each
candidate contains:

For `goal.target: pareto`

, the result contains only non-dominated candidates and preserves each
objective’s natural direction.

Exact repeated suggestions reuse a result from the current `run`

call. The cache does not persist
between calls, even when the same `Sweeper`

instance is reused.