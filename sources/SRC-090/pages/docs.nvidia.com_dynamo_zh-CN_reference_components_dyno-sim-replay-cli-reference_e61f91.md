source: https://docs.nvidia.com/dynamo/zh-CN/reference/components/dyno-sim-replay-cli-reference
lastmod: 2026-09-23T23:30:39.914Z

# DynoSim Replay CLI Reference

Flags, engine-args JSON fields, constraints, and report schema for python -m dynamo.replay.

`python -m dynamo.replay`

runs one workload through one simulated Dynamo configuration and emits an
AIPerf-style report. This page is the flag and schema reference. For the workflow — input formats,
run modes, and when to use DynoSim versus AIPerf — see [DynoSim Runs](https://docs.nvidia.com/dynamo/cli/operations/dynosim/simulation-runs); for
searching many configurations, see [DynoSim Sweeps](https://docs.nvidia.com/dynamo/cli/operations/dynosim/simulation-sweeps).

The command reuses the mocker engine, so engine behavior is configured through JSON passed to
`--extra-engine-args`

(or the staged `--prefill-engine-args`

/ `--decode-engine-args`

) rather than
individual flags. For the underlying engine settings, see the
[Mocker CLI Reference](https://docs.nvidia.com/dynamo/reference/components/mocker-cli-reference).

`python -m dynamo.replay`

requires exactly one of: positional trace files, or all of
`--input-tokens`

, `--output-tokens`

, and `--request-count`

. The `dynamo`

format accepts one or more
trace shards. Every other trace format requires exactly one file.

## Workload input

Input trace path. The `dynamo`

format accepts one or more JSONL or JSONL.GZ shards. Other formats
accept one JSONL file. Mutually exclusive with the synthetic-workload flags below.

Synthetic per-request input length. Required (with `--output-tokens`

and `--request-count`

) when no
trace file is given.

Synthetic per-request output length.

Number of synthetic requests. When `--turns-per-session > 1`

, this is interpreted as the number of
sessions, and total completed requests become `request_count * turns_per_session`

.

Trace parser.

Allowed values: mooncake mooncake-delta agentic_mooncake applied_compute_agentic dynamoHow many tokens each `hash_id`

in the dataset represents. Trace-file runs only; separate from the
engine `block_size`

. Public Mooncake/toolagent traces use `512`

. Dynamo request traces embed this
value; replay derives it when the flag is omitted and rejects an explicit mismatch.

The `mooncake-delta`

, `agentic_mooncake`

, and `dynamo`

formats were added after Dynamo v1.2.1.
The `ai-dynamo`

1.2.x wheels on PyPI accept only `mooncake`

and
`applied_compute_agentic`

.

### Synthetic workload shaping

Apply only to synthetic (non-trace) runs.

Synthetic arrival spacing between requests, in milliseconds.

Number of turns in each synthetic session.

Fraction of prompt blocks shared inside a prefix group.

Number of shared-prefix groups. `0`

disables grouping.

Constant delay applied after each completed turn before the next turn in the same session becomes eligible.

## Trace file schema

Mooncake-style JSONL traces contain one request per line. A basic row accepts:

Example:

Rows without `session_id`

are independent requests. Priority fields affect only pending requests
when `--router-mode kv_router`

is active; they do not change round-robin routing or execution order
inside a selected engine.

### Multi-turn sessions

Use the same `session_id`

for every turn in one session. Turn `n+1`

waits for turn `n`

to complete,
then applies `delay`

, `delay_ms`

, or the timestamp delta between consecutive rows.

### Agentic Mooncake traces

Set `--trace-format agentic_mooncake`

to model request-level dependencies. Each row requires a stable
`request_id`

and can include:

Rows without `wait_for`

use their timestamp as the start time. Rows with dependencies wait for all
listed requests and then apply `delay + tool_wait_ms`

.

Agentic Mooncake is an input format for externally authored Mooncake-compatible traces. It is not an intermediate representation for Dynamo request traces.

### Dynamo request traces

Set `--trace-format dynamo`

to read one or more `dynamo.request.trace.v1`

JSONL or JSONL.GZ shards.
DynoSim reads the original records directly and does not create an intermediate Mooncake file. It
derives and validates the trace block size across all shards.

Rows without `agent_context`

use the standard request model. If every request contains
`agent_context`

, DynoSim reconstructs the agent-aware model, including session dependencies and tool
waits. A replay cannot mix context-free and agent-aware request rows. For the complete capture schema,
see [Observe a Local Deployment](https://docs.nvidia.com/dynamo/cli/operations/observability#capture-and-replay-requests).

`--trace-block-size`

defines how many tokens each trace `hash_id`

represents. It is independent from
the simulated engine `block_size`

.

## Execution

Offline mode drives the mocker engine core directly with no workers, NATS, etcd, or frontend. Online mode launches the mock workers against the live runtime path.

Allowed values: offline onlineRouting strategy. `kv_router`

uses the shared local scheduler and an in-process KV indexer.

Number of aggregated workers.

Prefill worker pool size for offline disaggregated simulation.

Decode worker pool size for offline disaggregated simulation.

Closed-loop concurrency cap. Ignores first-turn trace arrival timing and keeps a fixed number of requests in flight. Works with both trace-file and synthetic workloads.

Compresses or stretches the trace arrival process. Affects trace timestamps, not worker compute speed. Larger values make arrivals happen sooner.

Output report path. When omitted, writes a timestamped `dynamo_replay_report_*.json`

in the current
working directory.

## Engine and router JSON

These flags take JSON strings. Engine settings such as `block_size`

, `engine_type`

, `dp_size`

,
`speedup_ratio`

, and `decode_speedup_ratio`

belong here, not as top-level flags. Unspecified fields
fall back to `MockEngineArgs::default()`

and `KvRouterConfig::default()`

.

Aggregated engine configuration. Accepts a partial JSON object.

Prefill worker configuration for offline disaggregated runs. Must set `worker_type: "prefill"`

.

Decode worker configuration for offline disaggregated runs. Must set `worker_type: "decode"`

.

KV-router policy tuning, for example `{"router_queue_policy":"fcfs"}`

or
`{"router_prefill_load_model":"aic"}`

. Accepts a partial JSON object.

Startup-only policy-family and cache-bucket queue YAML. Overrides `router_policy_config`

inside
`--router-config`

. When omitted, DynoSim checks `DYN_ROUTER_POLICY_CONFIG`

.

Exact model profile to select from `--router-policy-config`

. When omitted, the YAML root profile is
used.

Requests can set `policy_class`

in Mooncake JSONL rows. A recognized policy family combines with the
router-observed uncached Input Sequence Length (ISL) bucket to select a physical queue. An exact
explicit class bypasses cache bucketing. Missing, unknown, and ordinary physical-class names use the
selected profile’s `default_policy_family`

. For the YAML schema and queue behavior, see
[Router Configuration](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/router/configuration-and-tuning#policy-class-queues).

### Engine-timing AIC fields (engine-args JSON)

Set inside `--extra-engine-args`

(or the staged prefill/decode engine args) to drive the simulated
worker’s own timing model from AIC. This is the engine-timing AIC surface, distinct from the
router-side `--aic-*`

flags below.

Backend the analytical model emulates. Enables the AIC perf model; should match `engine_type`

.

GPU SKU for the perf model, for example `h200_sxm`

, `h100_sxm`

, `b200`

.

HuggingFace model identifier used by the perf model. Equivalent of `--model-path`

in
`dynamo.mocker`

.

Tensor-parallel size of each engine replica.

Speculative-decode depth for AIC-backed MTP runs. In disagg, set on the decode engine args.

Conditional draft-token accept rates for the mocker burst sampler, for example `"1,1"`

with
`aic_nextn=2`

accepts up to three visible tokens per decode forward.

Simulated seconds between a planner scale-up decision and the new worker becoming active. Unset or
`0`

means workers activate instantly.

## Router-side AIC prompt-load flags

Top-level flags used only for router-side prompt-load modeling, together with
`router_prefill_load_model: "aic"`

in `--router-config`

. Engine timing AIC still belongs in the
engine-args JSON above. Both surfaces accept the MoE parallelism fields; for Kimi-style TP-only MoE
configs, set `--aic-moe-tp-size`

equal to `--aic-tp-size`

, with `--aic-moe-ep-size 1`

and
`--aic-attention-dp-size 1`

.

Backend for the router-side perf model.

Allowed values: vllm sglang trtllmGPU SKU for the router-side perf model, for example `h200_sxm`

.

AIC backend engine version. When unset, uses the default version for the backend.

HuggingFace model identifier for the router-side perf model.

Tensor-parallel size for router-side latency prediction.

Mixture-of-Experts tensor-parallel size. Required by some MoE models.

Mixture-of-Experts expert-parallel size. Required by some MoE models.

Attention data-parallel size. Required by some MoE models.

## Constraints

DynoSim validates these before running and fails immediately on any violation.

Shared constraints:

`extra_engine_args.engine_type`

must be`vllm`

,`sglang`

, or`trtllm`

- aggregated simulation requires the existing aggregated args path
- disaggregated simulation requires both
`prefill_engine_args`

and`decode_engine_args`

- disaggregated simulation requires
`router_mode=kv_router`

`dp_size`

must be`1`

- disaggregated simulation requires matching
`block_size`

in`prefill_engine_args`

and`decode_engine_args`


Additional offline constraints:

- offline
`kv_router`

requires`num_workers > 1`

- single-worker offline mode is a dedicated fast path for
`vllm`

,`sglang`

, and`trtllm`

; it supports flat request runs and workload-driven multi-turn runs - offline disaggregated simulation is a separate two-stage runtime with prefill and decode worker pools

Additional online constraints:

- the current live simulation path is also limited to aggregated workers

## Report schema

The report — and the equivalent Python APIs `dynamo.replay.run_trace_replay(...)`

and
`dynamo.replay.run_synthetic_trace_replay(...)`

— contains:

- request counts
- input and output token totals
- virtual duration and wall-clock runtime
- request and token throughput
- prefix cache reuse ratio
- TTFT, TTST, TPOT, ITL, and end-to-end latency summaries
- output-token-throughput-per-user summaries