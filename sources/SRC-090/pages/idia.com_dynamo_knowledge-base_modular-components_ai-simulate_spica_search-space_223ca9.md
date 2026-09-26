source: https://docs.nvidia.com/dynamo/knowledge-base/modular-components/ai-simulate/spica/search-space
lastmod: 2026-09-24T19:58:16.636Z

# Spica Search Space

**Experimental.** Spica is intended for evaluation and feedback, not production capacity
planning. Its API, configuration schema, search results, and deployment output may change
without a standard deprecation period. Spica provides no SLA, accuracy, or configuration
optimality guarantees.

A `SearchSpace`

(the `search_space:`

block of a `SmartSearchConfig`

YAML) is the input
to one smart-sweep run: the knobs to **explore**, plus the **pinned** context (model,
hardware, GPU budget, and the engine/router/kv-manager/planner scalars). The optimizer
runs one Vizier study per `deployment_mode`

branch and ranks candidates across branches.

This document is the reference for **every knob**: its type, default, whether it is
searched or pinned, and its allowed choices. Source of truth:
`aisimulate/src/aisimulate/spica/config.py`

(`SearchSpace`

, `SEARCH_CHOICES`

, `COMPOSITE_DICT_KEYS`

, `COMPOSITE_REQUIRED_KEYS`

).

## Kinds of knob

There are four kinds of knob:

**Atomic list knob**— a list whose entries must be a non-empty subset of that knob’s`SEARCH_CHOICES`

. One element pins; many search.**Pinned scalar**— a plain value; never enters the sweep.**Composite knob**— bundles several coupled*unrolled*planner/predictor fields behind a named preset; each list entry is a preset id**or**a self-contained dict.— the parallel shape + replica count. Left`parallel_configs`

**empty**it is*derived*by KV-feasible enumeration (see[Parallel configs](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/ai-simulate/spica/search-space#parallel-configs-derived)); provide a list of dicts to pin one or search a custom menu.

`_validate_search_choices`

enforces list knobs are non-empty and every entry is legal.

## Deployment

`deployment_mode`

is the only knob that branches the sweep (agg / disagg have structurally
different parallel configs); `backend`

is a *searched knob within each branch*, not a
separate study. `min_gpu_budget`

is validated against `gpu_budget`

by `_validate_gpu_budget`

.

## Prefill engine (disagg branch)

## Decode engine (disagg branch)

## Agg engine (agg branch)

## KV manager (G2 host offload)

All fields are pinned. The current Spica schema configures only G2 host offload;
it does not expose G3 or G4 tiers. Offload is **off by default**
(`num_g2_blocks = 0`

). When G2 is enabled, `kv_bytes_per_token`

is required so
replay cannot silently disable offload if model metadata is private or
unavailable. In disaggregated deployments, these settings are applied only to
prefill workers; decode workers do not receive a second local offload tier.

## Router

KV-router weights are ignored under `round_robin`

. When `router_mode`

is pinned to
`["round_robin"]`

, the search-space builder removes all dependent router knobs from the
Vizier study. A mixed `["kv_router", "round_robin"]`

study retains them because they are
active for its KV-router trials.

`host_cache_hit_weight`

and `disk_cache_hit_weight`

are emitted as router scoring
weights when G2 offload is enabled. With offload off (the default
`num_g2_blocks = 0`

), they are dropped from the search to avoid dead dimensions.
The current Spica surface does not configure a disk tier, so
`disk_cache_hit_weight`

does not tune disk capacity or disk offload.

## Admission control (pinned)

For a search that includes `kv_router`

, these fields are reserved but currently rejected
when set: Dynamo’s replay API does not accept admission-control configuration, so scoring
them would diverge from the generated frontend. Leave them at their defaults until replay
support is available. They remain inert under a round-robin-only search.

## Planner composites

Composite knobs. Each list entry is a preset id (string) **or** a dict; one entry pins,
several search; presets and dicts can be mixed. Choices below are the preset ids; the
preset → field expansions are in [Composite presets](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/ai-simulate/spica/search-space#composite-presets).

When every configured `planner_scaling_policy`

disables both throughput and load scaling
(for example `["disabled"]`

), the search-space builder removes `planner_fpm_sampling`

and
`planner_load_sensitivity`

from the Vizier study. Mixed studies retain them for policies that
enable the planner.

## Load predictor

`load_predictor_candidates`

is the forecaster for predictive throughput scaling. It is
**not** part of the main Vizier study: a separate forecast-loss sub-sweep
(`sweep_load_predictor`

) scores every entry against the trace by one-step-ahead loss and
pins the per-interval winner into the main sweep. Triggered only when some
`planner_scaling_policy`

candidate enables throughput scaling; for a static (non-trace)
workload it short-circuits to `constant_last`

for every interval.

## How the sweep uses these (branches & backend)

The sweep runs **one Vizier study per deployment_mode**.

**: listing multiple backends searches them**

`backend`

is a searched knob,
not a branch*together*within each mode’s study, and the cross-branch merge picks the global best —

`rank()`

for a single-objective goal, or
`pareto_front()`

(the non-dominated set) under a `pareto`

goal. The parallel-config pool is the **union**of every backend’s KV-feasible configs. Backend is selected first and the latent shape request is projected only onto configs that backend supports. A backend with no perf DB / no viable config for a mode is dropped; a

**mode**for which no backend is viable is

**skipped with a warning**(a viable mode still runs); only if

*no*mode is viable does the run error. A

*pinned*config legal for no backend is a hard error (fail fast).

Replay capability is part of viability: TRT-LLM is excluded from disaggregated branches because Dynamo replay currently rejects TRT-LLM disaggregation. It remains searchable in aggregate branches.

The planner’s `optimization_target`

is derived from the sweep **goal**, not from
`planner_scaling_policy`

(see `OptimizationTarget.planner_optimization_target`

):
`throughput`

/`throughput_per_gpu`

/`throughput_per_user`

→ `"throughput"`

, `e2e_latency`

→
`"latency"`

, `goodput`

/`goodput_per_gpu`

→ `"sla"`

, `pareto`

→ `"throughput"`

. The policy
only decides *which* scaling loops run and their intervals.

**Predictive throughput scaling needs an SLA**, so it only works under a goodput sweep
(`optimization_target="sla"`

). For a `throughput`

/`e2e_latency`

/`pareto`

sweep,
`filter_scaling_policies(allow_throughput=False)`

**drops** every throughput-scaling entry
(`throughput_*`

, `hybrid_*`

, or any dict with `enable_throughput_scaling: true`

); only
`disabled`

/ `load_*`

survive. Listing *only* throughput-scaling policies for a non-SLA
sweep errors (nothing left to search). Both scaling flags false ⇒ planner off (static
replica count, same as `disabled`

).

An e2e-only goodput SLA can be replay-scored, but it cannot seed the planner’s ttft/itl SLA
target. In that case the main sweep drops every planner-scaling entry (throughput, load, and
hybrid) and keeps only static policies such as `disabled`

; if nothing static remains, it raises a
clear config error.

## Composite presets

A composite dict entry **replaces** the preset expansion (no partial / merge). Required keys
are enforced at load by `_validate_search_choices`

against `COMPOSITE_REQUIRED_KEYS`

: the
three **planner** composites must provide *all* their unrolled fields; a
`load_predictor_candidates`

dict needs at least `load_predictor`

(the family), with family
params defaulting per family. Unknown keys are rejected. Value *legality* (perfect-square fpm
bucket, positive intervals, `load_scaling_down_sensitivity`

in 0–100, …) is validated
downstream by Dynamo’s `PlannerConfig`

.

`planner_scaling_policy`


Decoded by `SCALING_POLICIES`

in `aisimulate/src/aisimulate/spica/planner.py`

.

Dict keys (all required): `enable_throughput_scaling`

, `enable_load_scaling`

,
`throughput_adjustment_interval_seconds`

, `load_adjustment_interval_seconds`

.

`planner_fpm_sampling`


Decoded by `FPM_SAMPLING`

.

Dict keys (all required): `max_num_fpm_samples`

, `fpm_sample_bucket_size`

(a perfect square,
checked downstream).

`planner_load_sensitivity`


Decoded by `LOAD_SENSITIVITY`

.

Dict keys (all required): `load_scaling_down_sensitivity`

(0–100), `load_min_observations`

.

`load_predictor_candidates`


Decoded by `LOAD_PREDICTOR_PRESETS`

in
`aisimulate/src/aisimulate/spica/load_predictor_sweep.py`

.

Dict keys: `load_predictor`

(required; one of `constant`

/ `arima`

/ `prophet`

/ `kalman`

),
`load_predictor_log1p`

, `prophet_window_size`

(prophet), and
`kalman_q_level`

/ `kalman_q_trend`

/ `kalman_r`

/ `kalman_min_points`

(kalman). Omitted
family fields take the planner defaults (`prophet_window_size`

=50, `kalman_q_level`

=1.0,
`kalman_q_trend`

=0.1, `kalman_r`

=10.0, `kalman_min_points`

=5).

## Parallel configs (derived)

Left empty, `parallel_configs`

is **enumerated** by `parallel_configs_for`

(`aisimulate/src/aisimulate/spica/model_hw.py`

) on top of `enumerate_parallel_configs`

/
`enumerate_disagg_configs`

(`aisimulate/src/aisimulate/spica/parallel_enum.py`

). Per `(model, hardware, gpu_budget, backend)`

:

**GPUs per worker**is drawn from the ladder`{1, 2, 4, 8, 16}`

(`_DEFAULT_GPUS_PER_WORKER`

), capped at`gpu_budget`

. A worker spans`tp * pp * dp`

GPUs with`pp`

pinned to 1, so`gpus_per_worker = tp * dp`

.**Dense models**use plain TP only:`{tp: g, dp: 1, moe_tp: 1, moe_ep: 1}`

.**MoE models**scan`tp / dp / moe_tp / moe_ep`

over`{1, 2, 4, 8, …}`

subject to the MoE width constraint`tp * attention_dp == moe_tp * moe_ep`

(here`dp`

=`attention_dp`

), and keep only these four pure patterns:**TEP**— attention-TP + expert-EP:`tp > 1`

,`dp == 1`

,`moe_tp == 1`

,`moe_ep > 1`

.**DEP**— attention-DP + expert-EP:`tp == 1`

,`dp > 1`

,`moe_tp == 1`

,`moe_ep > 1`

.**TP**—`tp > 1`

,`dp == 1`

,`moe_tp > 1`

,`moe_ep == 1`

.**DTP**—`tp == 1`

,`dp > 1`

,`moe_tp > 1`

,`moe_ep == 1`

. MoE tensor parallelism is scanned for every MoE model; backend filters below can still remove unsupported combinations.

**Backend filters**(mirroring AI Configurator’s`enumerate_parallel_config`

):`trtllm`

forbids`tp > 1 & attention_dp > 1`

.`sglang`

EP-only MoE backends (wideep /`deepep_moe`

/`megamoe`

) force`moe_tp == 1`

.`vllm`

forbids`moe_tp > 1 & moe_ep > 1`

. Large MoE that a node can’t hold (`gpus_per_node * vram_per_gpu < 2 * weight_bytes`

) auto-enables multi-node wideEP.

**KV feasibility**(`aisimulate.spica.kv_estimate.feasible_shape_tokens`

, via`aiconfigurator_core.sdk.memory.estimate_kv_cache`

): a shape is kept iff its total KV capacity in tokens (after quantized weights + activation reservations) holds at least one longest sequence —`total_kv_size_tokens > max_seq_len`

, where`max_seq_len`

=`context_length`

if set, else the model’s max context. This is per-shape (TEP / DEP / TP differ at the same GPU count) and uses the real (often FP8) weights. The estimator raises`NoPerfDatabase`

for a target with no perf DB, and branch enumeration removes that backend. Spica does not use the naive fallback. If no shape is feasible within budget,`NoViableParallelConfig`

is raised for that branch.**Replicas**fill the budget: for each kept worker shape, replica counts`r ∈ 1..(gpu_budget // g)`

such that`g * r`

lies in`[min_gpu_budget, gpu_budget]`

.**disagg**enumerates prefill × decode**independently**(each role its own shape + replica count) and pairs them so`prefill.total_gpus + decode.total_gpus`

fits the budget; prefill/decode throughput rate-matching is applied downstream at replay.

### Parallel search projection

Vizier searches model-visible latent dimensions and projects every suggestion onto the valid
parallel-config pool. There is no opaque config-index path. These dimensions are **internal
Vizier parameters**, not fields accepted under `search_space:`

. Users constrain them through
the model, hardware, backend, GPU budget, context length, and optional `parallel_configs`

pool.

#### Internal Vizier parameters

The projector defines up to three aggregate features, plus `agg_ffn_mode`

when the valid pool
contains MoE TP or EP:

It defines up to six disaggregated features, plus one FFN-mode feature per role when the valid pool contains MoE TP or EP:

Here `prefill_total_gpus = prefill_gpus_per_engine * prefill_replicas`

, with the analogous
definition for decode. A one-GPU shape is canonicalized as attention `tp`

and FFN `tp`

.
`*_ffn_mode`

is omitted when the pool has no MoE shape. Any single-valued feature is also
omitted from Vizier and injected as a constant. A one-config pool bypasses projection entirely.

The geometric-center default for an engine-size dimension is the feasible value closest in
log space to `sqrt(min_size * max_size)`

; a tie picks the smaller value. For example,
`{1, 2, 4, 8, 16}`

defaults to `4`

. The ranges and defaults are rebuilt for every deployment
mode from that branch’s union of valid configs across its viable backends. With multiple
backends, a value may therefore exist in the study-wide range but not for the backend selected
by a particular trial. Projection handles that case instead of marking the trial infeasible.

#### Projection onto a valid config

For latent request `z`

and its selected backend, `ParallelConfigProjector.project`

applies the
following deterministic steps:

-
**Backend filter.**Remove every config that is not legal and KV-feasible for the selected backend. GPU-budget and shape validity were already enforced when this pool was built. -
**Mode match.**For every remaining config, count mismatches across all requested attention and FFN modes. Keep only configs with the minimum mismatch count. Consequently, an exact mode combination always wins over a numerically closer config with a different mode. If no config realizes all requested modes, the least-mismatched mode combination is used and trial metadata records`mode_projected: true`

. -
**Numeric distance.**Among the mode survivors, minimize the sum of squared normalized deltas over`used_gpu_ratio`

,`prefill_gpu_share`

when applicable, and every per-engine GPU target. Ratios and shares use their linear value; engine sizes use`log2(size)`

. Each delta is divided by that feature’s min-to-max span**within the selected backend’s pool**:A feature with zero span for that backend contributes zero. All non-constant numeric features otherwise have equal weight after normalization.

-
**Stable tie-break.**Equal distances use a deterministic lexicographic shape-and-replica key, so projection never depends on evaluation history.

Replica count, concrete `tp`

/ `attention_dp`

/ `moe_tp`

/ `moe_ep`

, and total GPU usage are
not independent Vizier knobs. They come from the selected valid config. This preserves useful
numeric and categorical structure for Vizier while guaranteeing replay never receives an
illegal parallel combination.

For example, consider a 32-GPU disagg branch containing these two valid configs for one backend:

A request for A’s numeric values (`used_gpu_ratio=0.5`

, `prefill_gpu_share=0.5`

, engine sizes
`4 + 8`

), the modes shared by both configs, but decode FFN mode `tp`

projects to B. Mode
matching removes A before numeric distance is considered, so B’s actual ratios become `0.875`

and `0.143`

; its concrete replica counts `1 + 3`

are carried into replay.

Requested features, actual features, numeric distance, whether a mode fallback occurred, and
the full selected parallel config are recorded in Vizier trial metadata under
`spica_projection`

.

Different latent requests may project to the same full sample. Spica reuses the successful
replay result and makes bounded replacement asks; only unique successful samples count toward
`candidates_per_round`

. After `11 * candidates_per_round`

attempts, the branch may stop early.
Projection never changes to the nearest *untested* config, which would make it
history-dependent.

**Derived, not settable:** `strategy`

(`tp`

/ `tep`

/ `dep`

/ `dtp`

, computed by
`ParallelShape.strategy`

; it also has a `mixed`

fallback that enumeration never emits) and
`used_gpus`

(`gpus_per_worker × replicas`

, summed across roles for disagg).

### Pinning `parallel_configs`


Provide a list of dicts to **pin** (one entry) or search a **custom menu** (several entries).
A pinned config is kept for whichever backends it is legal + feasible on (errors if none).
`_validate_parallel_configs`

requires `deployment_mode`

to list **exactly one mode** when
`parallel_configs`

is non-empty.

With projection, one entry bypasses all parallel Vizier dimensions and projection; several entries form the complete projection pool, so the sampler can never leave the user’s menu. The YAML schema is unchanged.

**agg**entry — a flat shape dict:`tp`

(required),`attention_dp`

,`moe_tp`

,`moe_ep`

,`pp`

,`replicas`

. Omitted dims default to`1`

;`replicas`

defaults to`1`

. Dense models can write just`{tp: N}`

.**disagg**entry — nests two shape dicts:`{prefill: <shape>, decode: <shape>}`

, each with its own`replicas`

.

Each pinned shape is validated against the same rules the enumerator applies — MoE width
(`tp × attention_dp == moe_tp × moe_ep`

), `gpus_per_worker ∈ {1, 2, 4, 8, 16}`

, backend
filters, KV feasibility for the model’s max sequence, `used_gpus ≤ gpu_budget`

. Structural +
single-mode checks run at config load; full legality / KV-feasibility when branches are
enumerated. An illegal pin is rejected before replay.

## Examples

Pin a single deployment (one candidate — handy for a targeted re-evaluation):

Search presets but pin one composite field with a dict (custom 240 s interval):

Pin a disagg parallel config (prefill TEP, decode DEP):

## Validation summary

**List knob**— non-empty; string entries must be a listed`SEARCH_CHOICES`

value (`_validate_search_choices`

).**Composite dict**— no unknown keys, and the required keys are present (all unrolled fields for the planner composites; at least`load_predictor`

for`load_predictor_candidates`

). Value legality is checked downstream by Dynamo’s`PlannerConfig`

.—`gpu_budget`

/`min_gpu_budget`

`0 < min_gpu_budget <= gpu_budget`

(`_validate_gpu_budget`

).— structural + single-mode at config load (`parallel_configs`

`_validate_parallel_configs`

); full legality / KV-feasibility when branches are enumerated.