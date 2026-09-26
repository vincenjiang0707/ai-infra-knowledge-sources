source: https://docs.nvidia.com/dynamo/zh-CN/reference/components/mocker-cli-reference
lastmod: 2026-09-23T23:30:39.914Z

# Mocker CLI Reference

Command-line flags for the python -m dynamo.mocker simulated worker.

`python -m dynamo.mocker`

launches a simulated Dynamo worker that registers with the frontend,
publishes KV events, and exercises the router and planner paths without a GPU. This page is the flag
reference. For the deployment workflow and local/Kubernetes launch recipes, see
[Simulate a Kubernetes Deployment](https://docs.nvidia.com/dynamo/kubernetes/operations/dynosim/live-simulation-with-mocker) or
[Simulate a Local Deployment](https://docs.nvidia.com/dynamo/cli/operations/dynosim/mocker-live-simulation); for the engine internals these flags
configure, see [Mocker Engine Architecture](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/mocker/mocker-engine-architecture).

The same engine settings apply to [DynoSim Runs](https://docs.nvidia.com/dynamo/cli/operations/dynosim/simulation-runs): `python -m dynamo.replay`

reuses the mocker engine and accepts these values as JSON through `--extra-engine-args`

,
`--prefill-engine-args`

, and `--decode-engine-args`

rather than as individual flags.

## Core and model

HuggingFace model ID or local path for the tokenizer.

Model name used in API responses.

Dynamo endpoint string. Defaults are namespace-dependent, and prefill workers use a different default endpoint than aggregated or decode workers.

Engine simulation type.

Allowed values: vllm sglangPath to a JSON file with mocker configuration. Overrides individual CLI arguments.

## KV cache

Number of KV cache blocks.

Tokens per KV cache block. For `sglang`

, when omitted, the effective page/block size defaults to 1
or to `--sglang-page-size`

when provided.

Enable prefix caching. Pass `--no-enable-prefix-caching`

to disable.

KV cache dtype for the bytes-per-token computation.

KV cache bytes per token. Overrides the auto-computation.

## Scheduling

Maximum concurrent sequences.

Maximum tokens per batch.

Enable chunked prefill. Pass `--no-enable-chunked-prefill`

to disable.

Decode eviction policy under memory pressure. `lifo`

is vLLM v1 style.

## Timing

Timing speedup factor applied to simulated prefill and decode durations.

Decode-only speedup multiplier, for example for Eagle speculation.

Simulated startup delay, in seconds.

## Data parallelism and workers

Number of DP replicas.

Workers per process. Prefer this over launching many separate mocker processes: all workers share one tokio runtime and thread pool.

Delay between worker launches, in seconds. `0`

disables; `-1`

enables auto mode.

## Performance modeling

Path to either a mocker-format `.npz`

file or a profiler results directory.

JSON config for emitting reasoning token spans, with `start_thinking_token_id`

,
`end_thinking_token_id`

, and `thinking_ratio`

.

## AIC performance model

Opt-in flags for the NVIDIA AI Configurator (AIC) latency model. Default mocker runs do not use AIC.
For the timing-model design, see [Mocker Engine Architecture](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/mocker/mocker-engine-architecture#performance-model).

Use the AIC SDK for latency prediction instead of the interpolated or polynomial models. Opt-in
only: default mocker and DynoSim run paths do not use AIC. Requires `aiconfigurator`

installed and
usable AIC systems/perf data for the requested `system/backend/version`

tuple.

AIC system name, for example `h200_sxm`

. Used with `--aic-perf-model`

.

AIC backend engine version, for example `0.12.0`

for vLLM. When unset, uses the default version for
the backend.

Tensor-parallel size for AIC latency prediction. Affects only AIC performance-model lookups, not mocker scheduling.

Mixture-of-Experts tensor-parallel size for AIC latency prediction. Required by some MoE models.

Mixture-of-Experts expert-parallel size for AIC latency prediction. Required by some MoE models.

Attention data-parallel size for AIC latency prediction. Required by some MoE models.

## Disaggregation

Worker mode.

Allowed values: agg prefill decodeComma-separated rendezvous base ports, one per worker in disaggregated mode.

KV cache transfer bandwidth in GB/s. Set to `0`

to disable.

## Event and request transport

Event transport.

Allowed values: nats zmqRequest transport.

Allowed values: nats tcpDiscovery backend.

Allowed values: kubernetes etcd file memComma-separated ZMQ PUB base ports for KV event publishing, one per worker.

Comma-separated ZMQ ROUTER base ports for gap recovery, one per worker.

## SGLang-specific

Apply only when `--engine-type sglang`

.

SGLang scheduling policy. `fifo`

/`fcfs`

is the default; `lpm`

is longest prefix match.

SGLang radix-cache page size in tokens. Also becomes the effective block size when
`--engine-type sglang`

and `--block-size`

is omitted.

SGLang max prefill-token budget per batch.

SGLang chunked-prefill chunk size.

SGLang admission-budget cap for max new tokens.

SGLang schedule conservativeness factor.