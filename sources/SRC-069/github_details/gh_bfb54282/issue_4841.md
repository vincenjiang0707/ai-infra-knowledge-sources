# [Issue #4841] [SM120] trtllm cutlass fused-MoE: autotuned (non-default) tactics intermittently corrupt generation under CUDA-graph serving; 14/60 tactics presented on NVFP4 cannot run at all

source: https://github.com/flashinfer-ai/flashinfer/issues/4841
state: closed | updated: 2026-09-25T22:05:33Z
labels: bug, needs-triage, model: qwen3.5 / 3.6 / 3.8, op: moe

## 正文

## Summary

On SM120 (RTX PRO 6000 Blackwell Workstation), serving `RadixArk/Qwen3.8-Flash-Next-NVFP4` through SGLang with FlashInfer **0.6.18** and autotuning enabled, generations intermittently collapse into a run of `!` (token id 0) at a rate of ~4–19% of 1024-token generations, varying per boot. With `trtllm::fused_moe::gemm1/gemm2` excluded from autotuning (all other ops still tuned), the rate is 0/36. I ran a ~15-arm bisection trying to isolate a mergeable fix and could not — but the elimination matrix is now strong enough that I believe this needs someone with kernel-level visibility into the trtllm-gen/cutlass grouped-GEMM path under CUDA-graph replay. Everything below is reproducible; harnesses: https://gist.github.com/SSHdotCodes/8abd7f719194c55b841b83c8c819666a

Related: my earlier report of the same class on 0.6.17 in sgl-project/sglang#34629 (0.6.17 was 36/36 corrupt; 0.6.18 improved to ~5/36 — the occupancy pre-filter now removes some unrunnable tactics from profiling — but did not fix it).

## Environment

- RTX PRO 6000 Blackwell Workstation Edition (SM120, 96 GB), driver 595.84
- flashinfer-python/cubin 0.6.18, jit-cache 0.6.18+cu130, torch 2.13.0+cu130
- SGLang nightly `d91c3682` + the Qwen3.8-Flash-Next overlay, `--moe-runner-backend flashinfer_cutlass`, NVFP4 (`modelopt_fp4`), NEXTN MTP spec decoding, decode inside CUDA graphs
- Two fused-MoE instantiations in serving, both 512 experts / top-10 / hidden 2560 / intermediate 640:
  - target: packed int64 NVFP4 weights, BF16 activations in (in-kernel quant), `g1c=20 g2c=40`
  - MTP draft: unpacked weights, `g1c=9 g2c=9`

## Corruption phenomenology (in serving)

- Only when fused-MoE ops are autotuned: full autotune = 5/36, 2/48, 7/48, 3/48, 9/48 corrupt across boots; `--flashinfer-autotune-skip-ops trtllm::fused_moe::gemm1 trtllm::fused_moe::gemm2` = 0/36; full disable = 0/36.
- **Per-boot tactic lottery**: tuning picks different winners per boot for the same buckets — observed `(gemm1,gemm2)` = (17,57), (16,56), (16,57) on consecutive boots — and every autotuned boot corrupts regardless of which healthy pair won.
- Collapse positions are **content-anchored and stable across boots** at temp 0 (e.g. one prompt reliably collapses near char 42, another near char 19), and corrupt generations **cluster in time** then recover — consistent with a state (KV/SSM pool) getting poisoned by a rare bad computation and later overwritten.
- All the autotune speed win on this model comes from these MoE tactics: median decode 173.5 tok/s (autotune on) vs 155.6 (MoE ops skipped, everything else tuned) vs 158.4 (autotune off).

## What I ruled out (each arm in the gist, all on 0.6.18)

| hypothesis | test | result |
|---|---|---|
| tactic numerically wrong at some (M, routing) | eager sweep, every tactic × M∈{1..4096} × {uniform, all-same-expert, max-spread} × seeds, vs default-tactic output | clean (only the 14 hard-throwing tactics below) |
| bad tactic *pair* interaction | all healthy (t1,t2) pairs × M∈{1,8,192,4096} | 0/1920 |
| wrong under CUDA-graph capture/replay | per-tactic capture + replay×3 vs eager | 0/184 |
| rare per-call trigger | frozen winning pair in a captured graph, 300–600k replays, Zipf + pathological routing mutated per replay, incl. a full pretune first and periodic prefill-shaped churn | clean at ~17k replays/s |
| tuning-phase poisoning (broken tactics executing during profiling) | direct `run_gemm_profile` probe per broken tactic | they throw host-side in the profile path too; never launch |
| kernel reads uninitialized workspace | NaN-fill the allocator's free blocks before every call, all tactics | 0/576 |
| PDL launch race | serving with `enable_pdl=False`, autotune on | still corrupt (3/48) |
| per-call internal workspace aliasing across graph captures | dedicated persistent `workspace_buffer` passed to every call (per the API doc) | still corrupt (9/48) |
| MoE output wrong in vivo | in-server guard: recompute sampled calls with the default pair on identical inputs and compare (rel-L2 gate 0.15), decode-sized and prefill-sized eager calls, through corrupt generations | zero divergences (~30k+ comparisons). Note decode itself replays inside CUDA graphs where a Python-level guard cannot run — eager coverage only. |

So: numerically-correct-in-isolation tactics, executing inside captured decode graphs, intermittently produce a deterministic, content-anchored corruption in full serving — and only when they are non-default.

## Two concrete smaller defects found along the way

1. **`get_valid_tactics` presents unrunnable tactics on SM120.** For the NVFP4 config above, 14/60 tactics (gemm1 {4,5,14,15}, gemm2 {24,25,32,33,34,35,44,45,54,55}) throw in *both* the profile path and the real path: `Unsupported tile shape config 128128256 / 256128128 for MoE gemm` (`moe_gemm_template_dispatch_tma_ws.h:512`) and `Failed to initialize cutlass TMA WS grouped gemm. Error: Error Internal` (tactics 32/33). `get_tactic_occupancy` reports them runnable, and the NVFP4 path never reaches `get_valid_tactics_for_shape` (that filter is gated on `use_w4_group_scaling`, which is False for NVFP4). They are skipped by exception during profiling, but they add noise, waste tuning time, and pollute failed-tactic stats.
2. **Tactic selection is unstable boot-to-boot** (latency-only ranking under serving memory pressure), which makes field reports of this bug look flaky and hard to correlate.

## Repro (serving level, deterministic enough)

1. SGLang, Qwen3.8-Flash-Next NVFP4 on SM120, `--moe-runner-backend flashinfer_cutlass`, spec decoding on, autotune enabled.
2. Generate 36–48 × 1024-token completions (three prompt families in the gist's setup; temp 0 is fine).
3. Expect ~4–19% of generations to collapse into `!` runs; with the two fused-MoE ops in `skip_ops`, expect 0.

I'm happy to run candidate fixes or instrumented builds on this card — the serving repro takes ~15 minutes end-to-end, and the harness suite in the gist covers the isolation side. Mitigation we ship meanwhile: `--disable-flashinfer-autotune` (or skipping the two fused-MoE ops, which measures speed-equivalent to full disable on this model).


## 评论 (3)

### SSHdotCodes · 2026-08-31

## Root cause found — not in FlashInfer. Closing the corruption half of this issue.

After a full-day forensic session on the same RTX PRO 6000 I can now answer what the elimination matrix above could not: **the intermittent generation corruption is not caused by the trtllm cutlass fused-MoE tactics at all.** It is sgl-project/sglang#36537, i.e. the QSA sparse-decode **FA4 cute varlen fallback on SM120**, fixed upstream by sgl-project/sglang#36806 ("route exact SM120 to FlashInfer sparse decode", merged 2026-08-28). My serving stack predated that fix and routed SM120 decode to the FA4 fallback.

### Why it looked exactly like an autotune bug

- The FA4-fallback defect is data-dependent: it fires on particular sparse-attention gather patterns. At temperature 0, which gather patterns occur is a deterministic function of the hidden states.
- Autotuned (non-default) MoE tactics change floating-point **summation order**, so hidden states differ from the default tactic's at the bit level. That noise occasionally flips a borderline indexer top-k selection, which changes the gather pattern — and some patterns trigger the FA4 defect.
- Hence every signature that pointed at autotune: corruption "regardless of which healthy pair won" (any tactic ≠ default perturbs the bits), per-boot tactic lottery, content-anchored collapse positions (specific token positions produce the borderline scores), 0% with `--disable-flashinfer-autotune` (one fixed trajectory that happens to avoid the trigger), and total immunity in isolation (the defect lives in a different kernel entirely).
- The trigger is also sensitive to *any* perturbation, not just tactics: adding ~700 small captured ops per decode step took corruption from 12.5% to 100% of generations; disabling the overlap scheduler took it to 41.7% — all with identical MoE numerics.

### The verification data (all on SM120, FlashInfer 0.6.18, same serving stack as the report)

| arm | decode attention | result |
|---|---|---|
| graphs + autotune ON | FA4 varlen fallback | 3/24 corrupt (12.5%), and 5–19% historically |
| graphs + autotune ON + instrumentation | FA4 varlen fallback | 15/15 corrupt |
| eager (`--disable-cuda-graph`), autotune ON **or OFF** | FA4 varlen fallback | 50–100% corrupt (autotune-independent — the key exoneration datapoint) |
| graphs + autotune ON | trtllm-gen paged decode (#36806 routing) | **0/24 at identical tok/s** |
| graphs + autotune ON + the corruption-amplifying instrumentation | trtllm-gen paged decode | **0/12, device-level NaN counters all zero** |
| eager, autotune OFF | trtllm-gen paged decode | 0/6 |

Device-level forensics of the fallback's corruption, for anyone chasing similar reports: the poison is a full hidden-state row of uniform bf16 `0x7fff` (= fp32 `0x7FFFFFFF` read as float) appearing *between* MoE calls — MoE inputs go NaN while MoE outputs remain bit-correct on every check. In-graph tripwires recorded `n_origin = 0` (the fused-MoE op never turned a clean input into a bad output) across every corrupt generation.

So: the fused-MoE tactics were guilty of nothing but being fast in a different bit pattern. `--disable-flashinfer-autotune` is not needed on this stack once sglang#36806's routing is in place — autotune is back on in my production deployment with 0 corruption across 40+ validation generations and full tuned speed.

### What remains of this issue (real, and smaller)

Defect 2 from the report stands and is FlashInfer's: `queryOccupancyForConfig` returns 1 unconditionally for every TMA warp-specialized config, so `get_valid_tactics` presents 14/60 tactics on SM120 NVFP4 that the dispatch rejects (`Unsupported tile shape config 128128256 / 256128128`, plus two cutlass-init failures). They throw during every profiling pass — noise, wasted tuning time, polluted failed-tactic stats. I am submitting a PR that probes the TMA WS dispatch in workspace-query mode (the same graceful-skip idiom `calcMaxWorkspaceSize` already uses) so those configs report occupancy 0 and are filtered before profiling.

### SSHdotCodes · 2026-08-31

PR for the tactic-presentation defect is up: #4847 — verified on this card via a JIT rebuild: the 12 dispatch-rejected tactics now report occupancy 0 and disappear from profiling; surviving tactics numerically unchanged.

### SSHdotCodes · 2026-09-25

Closing: both parts are resolved. The generation corruption was not in FlashInfer; the root cause was fixed by sgl-project/sglang#36806 (see above). The dispatch-rejected tactics are fixed by #4847 (merged 2026-09-12).
