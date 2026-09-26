source: https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/ai-simulate/sweeper/configuration
lastmod: 2026-09-24T19:58:16.636Z

# Sweeper Configuration

Core fields and optional adapter-owned search spaces

**Experimental.**Sweeper’s configuration schema may change without a standard deprecation period.

`SmartSearchConfig.search_space`

contains backend and deployment fields. Optional feature-specific
search spaces are mappings under `SmartSearchConfig.adapters`

.

## Top-Level Shape

The adapter value is a search space, not one concrete runtime configuration. Its provider validates the whole mapping, contributes optimizer dimensions, and later materializes one concrete adapter configuration for each candidate.

## Backend Fields

Each engine role also has lists for `max_num_batched_tokens`

and `max_num_seqs`

, plus pinned block
size, GPU-memory-utilization, and prefix-caching fields. A one-item list pins a searched field.

## Pinned Parallel Configurations

Pinning `parallel_configs`

requires exactly one deployment mode. An aggregated entry is one shape:

A disaggregated entry contains `prefill`

and `decode`

shapes. Every pinned shape must be legal,
KV-feasible, and supported by at least one selected backend.

## Provider Selection

Adapter names are provider entry-point names. A provider can be installed through the
`aisimulate.sweep_config_providers`

entry-point group or injected into the `Sweeper`

constructor:

Sweeper loads only names present under `adapters`

. See [Sweep Configuration
Providers](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/ai-simulate/sweeper/sweep-configuration-providers) for the complete ABI.

## Sampler Algorithm Override

The experimental `AISIMULATE_SWEEPER_VIZIER_ALGO`

environment variable overrides the Vizier
algorithm. For example, set it to `RANDOM_SEARCH`

to bypass the default GP-bandit designer.
`SPICA_VIZIER_ALGO`

remains a deprecated fallback during migration; when both are set, the
AISimulate variable takes precedence.

## Removed KVBM Fields

Sweeper rejects the old KVBM block-count, transfer-bandwidth, offload-batch-size, and cache-hit fields. The AISimulate engine and replay path do not support them, and they have no adapter migration.