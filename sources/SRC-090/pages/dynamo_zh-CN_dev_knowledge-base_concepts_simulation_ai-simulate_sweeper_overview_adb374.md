source: https://docs.nvidia.com/dynamo/zh-CN/dev/knowledge-base/concepts/simulation/ai-simulate/sweeper/overview
lastmod: 2026-09-24T19:58:16.636Z

# Sweeper

Experimental backend-neutral configuration search

**Experimental.** Sweeper is intended for evaluation and feedback, not production capacity
planning. Its API, configuration schema, search behavior, and output may change without a
standard deprecation period.

Sweeper searches deployment configurations with a black-box optimizer. It turns every suggestion
into a versioned `ReplaySpec`

, sends that specification to an injected `RunnerFactory`

, and returns
ranked candidates or a Pareto front.

The `aisimulate`

package owns only backend-neutral simulation behavior. Optional feature packages
can register a `SweepConfigProvider`

that contributes search dimensions and materializes its part
of a replay. Sweeper imports a provider only when its adapter name appears in the configuration.

## Start Here

[Quickstart](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/ai-simulate/sweeper/quickstart)runs a small backend-neutral sweep.[Tutorial](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/ai-simulate/sweeper/tutorial)explains a complete sweep configuration.[Architecture](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/ai-simulate/sweeper/architecture)shows the provider, replay, and worker boundaries.[Configuration](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/ai-simulate/sweeper/configuration)describes core and adapter-owned search spaces.[Traffic](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/ai-simulate/sweeper/traffic)defines trace, request-rate, concurrency, and KV-load workloads.[Optimization Goals](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/ai-simulate/sweeper/optimization-goals)defines scalar and Pareto objectives.[Results](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/ai-simulate/sweeper/results)describes`ReplaySpec`

and`Candidate`

output.[Sweep Configuration Providers](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/ai-simulate/sweeper/sweep-configuration-providers)documents the extension ABI.

## Python Entry Point

`Sweeper`

is the only public execution interface. Supply a replay runtime explicitly:

For the public YAML contract and stack discovery, use `aisimulate recommend --config recommendation.yaml`

. The `Sweeper`

class remains available for callers that need the legacy Python
SDK configuration and an explicitly injected runtime.

## Compatibility

- A provider is imported only when its adapter name appears under
`adapters`

. - The runner advertises supported
`ReplaySpec`

versions, backend/topology pairs, and runtime hooks before a study starts. - Every
`Sweeper.run`

call owns fresh optimizer studies, result caches, runners, and worker pools. - KVBM search fields are rejected. The AISimulate engine and replay path do not support those fields and provide no adapter migration for the old host or disk offload settings.