# 2026-07-14-vllm-tilert-pd

source: https://vllm.ai/blog/2026-07-14-vllm-tilert-pd

# vLLM x TileRT: Specialized Decode for Latency-Critical Serving

Disaggregated serving, which separates the compute-bound prefill phase from the memory-bandwidth-bound decode phase, has become an increasingly standard pattern for serving large language models at scale, and vLLM supports it through a first-class connector interface.

That architectural shift carries a benefit that is easy to overlook: once prefill and decode are separated, **the decode side becomes pluggable**. Different serving regimes reward different engine designs. The prefill pool, the scheduler, the caching layer, and the serving API stay exactly where they are, while the decode pool becomes a deliberate choice.

Today, we are introducing exactly such a choice: **vLLM prefill paired with TileRT decode**, integrated through vLLM V1's public connector interface and shipping with TileRT 0.1.5. For latency-critical workloads, this pairing delivers **TileRT's native per-user decode speed**, while everything else about the deployment remains stock vLLM.

## Why a second decode option?

vLLM's native decode is, and remains, the right default: it is built for high-throughput batched serving across a huge range of models and hardware. But there is a growing class of workloads, e.g., agentic loops, interactive coding assistants, real-time voice, where the metric that matters is not aggregate throughput but how fast tokens reach each individual user. These workloads are latency-bound, and they call for a decode engine designed from the ground up for exactly that regime. Native decode and TileRT target different points on the same throughput–latency frontier, which is why they compose.

TileRT is such an engine: a new inference runtime built around the single goal of pushing per-user decode speed toward the limits of the hardware. We have written elsewhere about why we believe [speed is becoming its own scaling dimension](https://www.tilert.ai/blog/speed-as-the-next-scaling-law.html).

This post is not about the engine, though. It is about a more practical question: can you adopt a specialized decode engine **without giving up the ecosystem you depend on**, e.g., OpenAI-compatible APIs, scheduling, prefix caching, tool calling, and the operational maturity of vLLM?

This integration is designed to make that trade-off as small as possible:

**Prefill is vLLM.**Scheduling, chunked prefill, prefix caching — untouched.**The serving surface is vLLM.**Same APIs, same request format, same tooling.**Only decode changes, and only for the traffic you send there.**The TileRT-paired stack runs alongside your existing vLLM deployment; each workload picks its endpoint.

## Architecture: coexistence by design

The core design principle is **zero changes to vLLM**: no fork, no patches, no wrapped internal workers. The integration lives entirely behind vLLM V1's public extensibility surface: a `KVConnectorBase_V1`

implementation, composed under `MultiConnector`

and loaded through the standard `kv_connector_module_path`

mechanism. This matters beyond engineering aesthetics: adding a TileRT decode pool cannot destabilize a vLLM deployment you already run, and upgrading vLLM does not mean re-porting a fork.

**Routing.** A lightweight router fronts the TileRT pool. For each request it sets `max_tokens=1`

(vLLM performs the prefill and emits the first token) and attaches the target decode node in the standard pass-through field: `kv_transfer_params = {"tilert_host": ..., "tilert_ctrl_port": ...}`

. Traffic for the native pool flows through the usual disaggregation proxy, unmodified.

**Claim filtering.** The TileRT connector claims only requests carrying the mark and is a strict no-op for everything else, so the two decode pools can share one prefill instance (even a single forward batch): adopting TileRT for some traffic changes nothing for the rest.

**A pure producer.** The connector acts as a `kv_producer`

only, it never touches scheduling or sampling; it extracts and ships state after prefill. In every other respect the prefill instance is a stock vLLM server.

## How the handoff works

For cross-engine disaggregation to be practical, three things have to be true: the transfer must be fast, it must not slow the prefill node down, and the decode engine must pick up exactly where prefill left off.

**Data plane.** After prefill, the request's attention state (compressed KV, the sparse-attention index caches, and a small amount of metadata) moves to the decode node as RDMA one-sided writes into pre-registered GPU buffers, with either Mooncake or NIXL as the transfer engine. No intermediate serialization, no staging through host memory. The handoff protocol itself is independent of the underlying transfer engine, whose job is only to move bytes.

**Fully overlapped with prefill.** State extraction happens inside the forward window: the request's state is copied to a staging buffer before its cache blocks can be recycled, and a background sender performs the actual network transfer. A request bound for TileRT never blocks the next prefill iteration, including for native-pool requests sharing the same batch.

**Injection into a live engine.** On arrival, the state is converted to TileRT's native layout and injected directly into a running engine; decoding begins immediately, with multi-token speculative decoding active from the first step.

## Evaluation

## Choosing your decode pool

Route to **TileRT decode** when per-user token speed is the binding constraint, e.g., interactive agents, real-time assistants, latency-SLO inference, and the model is one TileRT supports.

Stay on **native vLLM decode** for maximum aggregate throughput, high-concurrency batching, and the long tail of models and features that general-purpose decode covers.

Both stacks expose the same OpenAI-compatible surface, so moving a workload between them is a routing change, not a client change.

**Current limitations.** In this release a TileRT decode node serves one in-flight request at a time, with the router providing gated dispatch and back-pressure. Model coverage in this release is GLM-5/5.1 and DeepSeek-V3.2, with more to come.

## Getting started

TileRT 0.1.5 is available on [PyPI](https://pypi.org/project/tilert/) (`pip install tilert`

; Python 3.12, CUDA 13 wheels) and the [TileRT repository](https://github.com/tile-ai/TileRT). Install it on both the prefill and decode nodes; the prefill side needs it for the connector plugin.

To run the TileRT pool and a native vLLM decode pool behind one shared prefill instance, compose both connectors under `MultiConnector`

. The configuration we validated runs NIXL end to end (vLLM's standard `NixlConnector`

for the native pool, the TileRT connector in NIXL mode for the TileRT pool), so the shared prefill uses a single transfer library; only the prefill's `--kv-transfer-config`

changes.

## Looking ahead

We think disaggregation is quietly changing what an inference stack is: less a single engine, and more a composition of specialized engines behind a shared serving layer. vLLM's connector interface is what makes that composition possible today, and this integration is one concrete example. It is also why an engine like TileRT can afford to specialize this deeply: with the serving layer shared and the interfaces open, going deep on one dimension no longer means rebuilding everything else.

We would love feedback from the community: on the integration surface, on the workloads where this helps, and on which models to support next.

## Acknowledgements

We thank the vLLM community for designing the V1 connector interface that made a zero-modification integration possible, and the Mooncake and NIXL projects for the RDMA transfer engines. We also appreciate [Inferact Inc.](https://inferact.ai/) for the collaboration to improve vLLM-TileRT integration.
