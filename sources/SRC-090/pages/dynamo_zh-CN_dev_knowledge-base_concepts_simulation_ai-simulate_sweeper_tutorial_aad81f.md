source: https://docs.nvidia.com/dynamo/zh-CN/dev/knowledge-base/concepts/simulation/ai-simulate/sweeper/tutorial
lastmod: 2026-09-24T19:58:16.636Z

# Sweeper Tutorial

Configure, execute, and inspect a replay-backed search

**Experimental.** Sweeper’s API and search behavior may change without a standard deprecation
period.

## 1. Define the Backend Search

Choose a model, hardware system, deployment modes, backends, and GPU budget:

Sweeper enumerates legal parallel configurations, removes unsupported runner topologies, and adds the active engine-role knobs to the optimizer study.

## 2. Define One Workload and Goal

Every candidate is evaluated against this workload. See [Traffic](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/ai-simulate/sweeper/traffic) for trace and
closed-loop alternatives, and [Optimization Goals](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/ai-simulate/sweeper/optimization-goals) for SLA and Pareto modes.

## 3. Control the Sweep

Each round is a barrier: the sampler asks for unique candidates, replay evaluates them, and then
the scores are reported back together. `parallel_evals`

controls replay worker fan-out.

## 4. Add Optional Feature Search

An installed or injected provider owns the schema below its adapter name:

The provider receives the complete `search_space`

mapping. It does not receive a preselected
concrete feature configuration.

## 5. Run and Inspect

The same `Sweeper`

instance can run multiple configurations. Studies, caches, and process pools are
new for every call.