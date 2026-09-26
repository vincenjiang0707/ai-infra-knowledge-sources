source: https://docs.nvidia.com/dynamo/zh-CN/dev/knowledge-base/concepts/simulation/ai-simulate/sweeper/quickstart
lastmod: 2026-09-24T19:58:16.636Z

# Sweeper Quickstart

Run a backend-neutral sweep with an injected replay runtime

**Experimental.** Sweeper is intended for evaluation and feedback, not production capacity
planning.

Install AISimulate:

Sweeper requires a `RunnerFactory`

supplied by the application that owns replay execution:

Set `sweep.parallel_evals`

above one to use spawned worker processes. Scripts using that mode must
guard their entrypoint with `if __name__ == "__main__":`

.

Next, read the [Tutorial](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/ai-simulate/sweeper/tutorial) for the complete configuration flow or [Sweep Configuration
Providers](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/ai-simulate/sweeper/sweep-configuration-providers) to add feature-specific search dimensions.