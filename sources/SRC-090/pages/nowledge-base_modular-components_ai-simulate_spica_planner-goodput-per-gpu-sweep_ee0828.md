source: https://docs.nvidia.com/dynamo/knowledge-base/modular-components/ai-simulate/spica/planner-goodput-per-gpu-sweep
lastmod: 2026-09-24T19:58:16.636Z

Planner Goodput-per-GPU Sweep


Planner Goodput-per-GPU Sweep

Experimental Spica search over Planner policies for MiniMax-M2.5 on B200 GPUs

**Experimental.** These replay results characterize one software snapshot and workload. Do not
treat them as production capacity guidance or a performance commitment. Spica’s search behavior
and output may change without a standard deprecation period.

Enable the planner (SLA mode) on the same deployment as the
[router experiment](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/ai-simulate/spica/router-end-to-end-latency-sweep), then use Spica’s smart sweep to **find the
planner configuration that maximizes goodput-per-GPU** on the Mooncake toolagent trace, and
compare against the static deployment and the default planner.

## Setup

### Why open-loop (not closed-loop)

A planner experiment must be **open-loop**. In closed-loop (fixed N in flight) the throughput
is *concurrency-bound* — fewer workers serve the same N concurrent requests **slower**, so
scaling down lowers throughput (hence goodput) roughly as fast as it lowers GPU count, and
goodput-per-GPU does **not** improve (the optimum degenerates to “stay at max workers”). In
open-loop the throughput is *arrival-bound* (fixed total tokens over the trace’s ~59 min), so
adding workers does **not** raise throughput — it only lowers latency. The planner can then
scale **down** in lulls without losing goodput, and goodput-per-GPU improves. That is the
regime where the planner has value.

## Baselines (open-loop, full trace)

The default planner already gives **2.3×** the static goodput-per-GPU — same goodput, but it
scales the fleet to an average of ~13.5 GPUs instead of pinning 32.

## Sweep config

`run_smart_search`

, `goal.target = goodput_per_gpu`

. Deployment + router + workload + SLA
fixed; only the planner knobs swept (full trace, open-loop):

## Result — goodput-per-GPU by planner-policy family

The dominant factor is the **scaling-policy family** (48 trials → 19 distinct configs):

**Best:** `load_180_10`

→ **goodput/gpu ≈ 121** (avg_gpu 8.3, goodput 999).

**Static 37.6 → default planner 87.7 → optimized planner ≈ 121** — the tuned planner is
**3.2× static** and **+38% over the default planner**.

## All searched configurations (full-trace sweep)

Every distinct planner config the Vizier sweep evaluated (48 trials → 19 distinct), best
goodput-per-GPU first. `load_scaling_down_sensitivity`

70/80/90 = aggressive/default/conservative;
`max_num_fpm_samples`

is the FPM budget (small=32, default=64, large/fine=128) and **only affects
the predictive throughput-scaling policies** — for the `load_*`

policies it is inert (so its
spread within the `load_180_10`

family is noise).

## Takeaways

**Reactive load scaling ≫ hybrid ≫ predictive throughput scaling**for goodput-per-GPU. Predictive throughput scaling*over-provisions*(it pre-scales to avoid SLA misses → avg_gpu ~20 → worst goodput/gpu); reactive load scaling tracks the actual load and scales down hard (avg_gpu ~8).- The optimizer drives latency
**to the SLA edge**to minimize GPUs: the best`load_*`

config runs TPOT ~78 ms (near the 50 ms ITL bound) and TTFT ~1100 ms (under the 2000 ms bound), letting goodput dip to ~1000 while avg_gpu drops to ~8 → goodput/gpu peaks. The conservative predictive policies keep latency low but waste GPUs. **Caveat:**`load_*`

policies don’t use`planner_fpm_sampling`

(it only affects predictive throughput scaling), so the`sens`

/`fpm`

spread*within*the`load_180_10`

family (117–121) is mostly mocker noise (~5%). The robust conclusion is the**policy family**(`load_180_10`

), not a precise`sens`

/`fpm`

setting.

## Reproduce

Notes: the planner path needs the `aic-forward-pass`

binding; a per-throughput-interval
load-predictor sub-sweep runs first (forecast-loss winner pinned per interval). Static and
default-planner baselines are run via `dynamo.replay.run_trace_replay`

(static: no
`planner_config`

; planner: `planner_config`

+ the SLA). Same deployment as
[Router End-to-End Latency Sweep](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/ai-simulate/spica/router-end-to-end-latency-sweep).