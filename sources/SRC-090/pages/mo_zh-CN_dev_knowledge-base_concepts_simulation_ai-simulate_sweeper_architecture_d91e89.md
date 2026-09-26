source: https://docs.nvidia.com/dynamo/zh-CN/dev/knowledge-base/concepts/simulation/ai-simulate/sweeper/architecture
lastmod: 2026-09-24T19:58:16.636Z

# Sweeper Architecture

Backend-neutral search, provider materialization, and replay execution

**Experimental.** Sweeper’s API, configuration schema, search results, and deployment output may
change without a standard deprecation period.

A `SmartSearchConfig`

combines backend knobs, optional adapter search spaces, a workload, an
optimization goal, and sweep run control. A `Sweeper`

composes that configuration with an injected
replay runtime.

## Ownership

## Sweep Flow

Provider code runs in the main process. Worker tasks receive only a serializable `ReplaySpec`

; they
do not import or pickle provider objects. Each worker creates one runner and reuses it for candidate
replays.

## Provider Preparation

A provider implements two operations:

`generate_search_space(search_spec, context)`

validates the complete adapter-owned search space and returns branch-specific parameters plus reusable prepared state.`materialize_replay(plan, selection, context)`

turns one namespaced selection into an`AdapterReplaySpec`

with concrete configuration and optional runtime hooks.

Sweeper namespaces provider parameters as `adapter::<adapter name>::<local parameter>`

. This avoids
collisions without adding feature-specific fields to the core schema.

## Replay and Failure Semantics

Before execution, `RunnerCapabilities`

verifies the replay-spec version, backend/topology pair, and
every runtime hook. Unsupported combinations fail before the optimizer spends trials on them.

Optimizer ask/tell stays in the main process. Exact repeated suggestions use a run-local result cache. Candidate build failures, replay failures, GPU-budget violations, and timeouts become infeasible trials. Parallel evaluation uses spawned worker processes and worker-sized waves; a timed-out pool is terminated and replaced.