source: https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/simulation/ai-simulate/sweeper/router-end-to-end-latency-sweep
lastmod: 2026-09-24T19:58:16.636Z

Router End-to-End Latency Sweep


Router End-to-End Latency Sweep

Experimental Sweeper search over KV router settings for MiniMax-M2.5 on B200 GPUs

**Experimental.** These replay results characterize one software snapshot and workload. Do not
treat them as production capacity guidance or a performance commitment. Sweeper’s search behavior
and output may change without a standard deprecation period.

This experiment reproduced the DynoSim router experiment, then used Sweeper’s smart sweep to find the KV-router configuration that minimized mean end-to-end latency on the Mooncake toolagent trace and validated the winner against the default-router baseline on the full trace.

## Setup

The deployment is **fixed** (pinned `parallel_configs`

, fixed engine batching, fixed
concurrency) so any change in e2e latency is attributable to the **router** alone.

## Sweep config

The experiment searched with `Sweeper.run`

(Vizier GP-bandit) and
`goal.target = e2e_latency`

. It ran on a 2k-request subset with the same long-context mix, then
validated the winner on the full trace. The configuration below documents the retired
`aisimulate==0.1.0.dev1`

API and is not accepted by AISimulate 0.12.0.

## Result — full trace, c=32 (the validation)

`*`

round_robin numbers are from the 2k subset (worst on every latency metric; not re-run full).

**Optimized vs default kv_router (full trace):** e2e **−3.6%**, TTFT **−14%**, TPOT **−27%**,
throughput **+3.6%**, prefix reuse **+12%** (0.494 → 0.554).

**Winning config:** `kv_router`

, ** overlap_score_credit=1.0**,

**,**

`prefill_load_scale=32`

**.**

`router_temperature=0.0`

### Why `prefill_load_scale`

matters most (and where it saturates)

`prefill_load_scale`

was best at the original ceiling (4.0), so the search space was extended
to 32. Higher values keep helping but **saturate around 16–32** (2k subset, overlap=1.0, temp=0):

Going beyond 32 (64/128) is expected to give negligible further gain.

## All searched configurations (2k-subset search)

Every distinct config the Vizier sweep evaluated (2k subset, c=32), best mean-e2e first.
`n`

= how many of the 48 trials landed on it (Vizier concentrates samples on the optimum).
`round_robin`

ignores the kv-router weights (shown as —).

## Takeaways

**kv_router ≫ round_robin**for e2e/TTFT (cache-affine placement → higher prefix reuse → less prefill recompute → lower TTFT), matching the DynoSim blog direction.here: pushing it up (to ~16–32) spreads prefill load off hot workers, cutting both TTFT and (notably) TPOT. It saturates ~16–32.`prefill_load_scale`

is the dominant router knob(its hard max) and`overlap_score_credit=1.0`

(fully deterministic, cache-affine routing) are best.`router_temperature=0.0`

- The smart sweep cut mean e2e
**−3.6%**and TPOT**−27%**over the default kv_router with no change to the deployment — purely router tuning.

## Reproduction Status

These results are historical and cannot be reproduced exactly. The experiment used
`aisimulate==0.1.0.dev1`

; that wheel did not include the example runner, and the experiment
configuration was not published.

The original validation ran the winning router configuration against the full trace with
`dynamo.replay.run_trace_replay`

. It required the AI Configurator performance model and the
`aic-forward-pass`

binding. The Router adapter validated the configured search choices before
the study started.