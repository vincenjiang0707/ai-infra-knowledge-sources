source: https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/ai-simulate/sweeper/glm-5-fp-8-pareto-sweep
lastmod: 2026-09-24T19:58:16.636Z

GLM-5-FP8 Disaggregated Pareto Sweep


GLM-5-FP8 Disaggregated Pareto Sweep

Experimental Sweeper search for a GLM-5-FP8 Pareto frontier on B200 GPUs

**Experimental.** These replay results characterize one software snapshot and workload. Do not
treat them as production capacity guidance or a performance commitment. Sweeper’s search behavior
and output may change without a standard deprecation period.

This replay-backed sweep targets the InferenceX/SemiAnalysis (SA) **GLM-5-FP8 / B200 /
Dynamo with SGLang / 1k-1k / disaggregated** frontier. It tests whether Sweeper can discover competitive
deployment mappings without pinning the parallel shape or replica count.

## Setup

`kv_load_ratio=1`

means the candidate’s estimated decode KV capacity divided by
`isl + floor(osl / 2)`

; `0`

maps to concurrency 1. This makes traffic pressure comparable
across candidates with different decode shapes and replica counts.

## Latest replay baseline

The replay baseline uses SA’s per-concurrency deployment mappings with the fixed AI Configurator and Dynamo mocker stack, block size 64, FP8 KV cache, and 10 requests per concurrency unit. It is the correct software baseline for this sweep; the earlier pre-fix replay curve is no longer used.

Hypervolume uses reference point `(0, 0)`

. Sweeper reaches **113.5%** of the latest replay
baseline’s hypervolume by finding deployment mappings beyond the fixed SA mapping schedule.

## Search encoding

Parallel search uses the default structured projection. Vizier models:

- total used-GPU ratio;
- prefill GPU share;
- prefill and decode GPUs-per-engine targets;
- per-role attention mode (
`tp`

or`dp`

); - per-role MoE FFN mode (
`tp`

or`ep`

).

Each suggestion is projected onto the nearest backend-compatible, KV-feasible enumerated
configuration. Replica counts and concrete TP / DP / MoE-TP / MoE-EP fields are derived from
that valid target. `parallel_configs: []`

requests the full enumerated pool; a user can still
provide one config as a strict pin or several configs as a custom projection pool.

## Configuration

The experiment used the following configuration shape. It documents the retired
`aisimulate==0.1.0.dev1`

API and is not accepted by AISimulate 0.12.0:

## Result

The 80-round run completed 640 successful unique samples from 670 attempts in 12:06:56:

- 22 candidates were rejected by KV-capacity prechecks;
- 8 replay evaluations exceeded the 600-second limit;
- 0 replay evaluations crashed;
- 155 distinct concrete parallel mappings were evaluated.

The highest-throughput point reached **1788.4 output tok/s/GPU** at **23.56 tok/s/user**:

Representative non-dominated points:


The exact Pareto filter returns 204 points because continuous load values produce many tiny tradeoffs along otherwise flat regions. The representative table and plot retain the useful shape of the frontier without treating those near-duplicates as different deployment choices.

## Convergence

For this workload, 50-55 rounds is the practical quality/runtime point. The final 27 rounds after round 53 consumed about 4 hours 39 minutes for 1.05% additional hypervolume.

## Reproduction Status

The packaged dependencies support this configuration’s KV-capacity and candidate-concurrency
calculations. These results are historical and cannot be reproduced exactly. The experiment used
`aisimulate==0.1.0.dev1`

; that wheel did not include the example runner, and the experiment
configuration was not published. Recreating the frontier also requires AI Configurator
performance database coverage for B200/SGLang/GLM-5-FP8 and the Replay behavior from the original
runtime snapshot.

The original run required the `aic-forward-pass`

binding. Dynamo’s attention-DP KV-capacity
calculation multiplied per-rank capacity by attention DP and replicas before passing engine
capacity to Replay.