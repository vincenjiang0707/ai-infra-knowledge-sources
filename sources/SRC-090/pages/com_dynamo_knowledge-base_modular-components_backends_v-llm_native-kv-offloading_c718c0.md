source: https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/native-kv-offloading
lastmod: 2026-09-24T19:58:16.636Z

# Native KV Offloading

vLLM’s OffloadingConnector with KV-aware routing in Dynamo

This guide shows how to run vLLM’s native CPU KV cache offloading
(`OffloadingConnector`

) with Dynamo’s KV router. For Dynamo-side offloading
backends such as KVBM, LMCache, and FlexKV, see
[KV Cache Offloading](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/kv-cache-offloading).

## Support Matrix

Status legend: ✅ validated end to end · ⚠️ available but not yet validated end to end · 🚧 Dynamo integration in progress · ❌ not yet supported.

## Requirements

Router-visible CPU offloading requires **vLLM v0.24.0 or later** and **Dynamo 1.3.0 or later**.

- vLLM v0.24.0 adds self-describing KV events for the
`OffloadingConnector`

, opt-in via`"self_describing_kv_events": true`

. Earlier versions publish placeholder CPU events with no token payload, which the router cannot index. - Dynamo 1.3.0 maps vLLM’s
`medium=CPU`

events to the router’s host tier and adds`--router-host-cache-hit-weight`

.

Three settings are required, and none is on by default:

- On every worker, enable KV event publishing with
`--kv-events-config`

—`--router-mode kv`

on the frontend does not enable it (see[KV-Aware Routing](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/overview#feature-support-matrix)). - On every worker, set
`"self_describing_kv_events": true`

inside`kv_connector_extra_config`

. - On the frontend, select event-driven KV routing with
`--router-mode kv`

.

Prefix caching must stay enabled on the workers; `python -m dynamo.vllm`

enables it by default.

## Setup

**vLLM workers** — native CPU offloading with router-usable events:

Launch additional workers with their own `CUDA_VISIBLE_DEVICES`

and a unique `--kv-events-config`

endpoint port per worker on the same host (for example `tcp://*:20081`

).

**Dynamo frontend** — event-driven KV routing:

The router tuning flags are optional; see [Configuration](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/native-kv-offloading#configuration).

The `--kv-transfer-config`

and `--kv-events-config`

JSON is vLLM-native — Dynamo passes engine flags through unchanged. `cpu_bytes_to_use`

(16 GiB in this example) is the total pinned host memory for the CPU tier, shared across the engine’s workers rather than per rank.

## Configuration

These are the main settings for the common CPU-offloading path. For all
connector options, see
[vLLM’s KV offloading guide](https://docs.vllm.ai/en/latest/features/kv_offloading_usage/).

**Worker side ( kv_connector_extra_config keys):**

**Frontend side (Dynamo router):**

Tune these values for your workload only after [verifying](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/native-kv-offloading#verification) that
CPU-tier events reach the router. See
[Configuration and Tuning](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/configuration-and-tuning)
for the full router reference.

## How Routing Works

vLLM copies sealed GPU KV blocks to pinned CPU memory. Dynamo adds:

**Tier-aware KV routing.**The router credits CPU-tier prefix overlap when choosing a worker, weighted by`--router-host-cache-hit-weight`

.**Event relay.**Each worker relays vLLM’s GPU and CPU KV events from the local ZMQ publisher to the Dynamo event plane.

The GPU and CPU copies then evict independently:

Without this event wiring, offloading still works inside each worker, but the router treats CPU-resident prefixes as cache misses.

## Verification

Check that the router applies KV events:

The `event_type="stored",status="ok"`

counter should increase as requests run.

To confirm CPU-tier routing, run the frontend with debug logging and repeat a long prefix after it has been offloaded:

A line like this confirms that the router consulted the CPU tier:

## Troubleshooting

## Further Reading

[Offloading Support Matrix](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/offloading-support-matrix)— cross-framework support matrix for KV routing with offloading[vLLM KV offloading guide](https://docs.vllm.ai/en/latest/features/kv_offloading_usage/)— connector configuration reference[Configuration and Tuning](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/configuration-and-tuning)— full router flag reference, including lower-tier cache-hit weights[Router Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/router-guide)— routing modes and deployment matrix[KV Cache Offloading](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/v-llm/kv-cache-offloading)— KVBM, LMCache, and FlexKV offloading backends for vLLM[Using HiCache](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/sg-lang/hi-cache)— the SGLang counterpart: tier-aware routing with HiCache