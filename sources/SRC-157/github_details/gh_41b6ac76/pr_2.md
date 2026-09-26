# [PR #2] Profiling additions: application replay for residency-dependent kernels, divergent-barrier diagnosis, SASS counters helper

source: https://github.com/mit-han-lab/ncu-report-skill/pull/2
state: closed | updated: 2026-09-04T14:53:29Z
labels: 

## 正文

Practical additions from profiling a recurrent batched GEMV on GB200 (CUDA 13.3, ncu 2026.2.1), where the default recipes gave misleading answers in three places. Everything here was verified on hardware; the measurement record is in https://github.com/youngjun-ii/gpu_perf (`recurrent_gemv/JOURNAL.md`, entries 5 and 6).

**Collection (`03-collection.md`, `09-common-issues.md`, `SKILL.md` step 3)**
- Recipe 4b: kernels whose speed depends on state left by earlier launches (L2 residency across steps, persistent kernels) must be profiled with `--replay-mode application --cache-control none`. Kernel replay restores memory and flushes L2 between passes: a 16.8 MB matrix that is L2-resident in the timing loop showed 1.5 % L2 hit and all-DRAM reads under kernel replay, 93 % hit and 0 DRAM bytes under application replay.
- Persistent/cooperative kernels launch once, so `-s 2 -c 1` profiles nothing (`No kernels were profiled`); use `-s 0`.

**Diagnosis (`06-diagnosis-playbook.md`, `05-analysis-dimensions.md`)**
- Pattern I.1: a barrier far slower than its isolated cost. `cooperative_groups::grid_group::sync()` measured 1.8 µs alone and 14 µs extra per step inside a real kernel. Its non-aligned `barrier.sync` gets a `BRA.DIV` + `WARPSYNC.COLLECTIVE` + `BAR.SYNC.DEFER_BLOCKING` fallback and the warp is not reconverged first; cg's own master warp arrives split every step. Diagnosed from the SASS source view (average threads at the `BRA.DIV`, execution counts on the collective block) and confirmed by reproducing it with `asm("barrier.sync 0;")` in a hand-rolled barrier. The fix is a barrier built around the aligned `__syncthreads()`.
- Pattern I.2: inter-CTA handoff cost that does not respond to contention, scope or placement (two dependent L2 round trips plus a release fence); polling-storm pitfall; NCCL-LL tagged data as the fix (1.1 → 0.5 µs per step).
- Stall samples of a barrier land on the instruction after the `BAR.SYNC`; stall ratios × instructions per warp as a cycle budget that must add up to the measured duration; ablation bit masks and iteration scaling as profiling methods.

**Helper (`helpers/sass_source_counters.py`)**
Per-instruction table via `ncu --import --page source --print-source sass --csv`: top stall PCs, every divergent branch with its average thread count, execution counts on `BAR.SYNC` / `BRA.DIV` / `WARPSYNC` / `COLLECTIVE` / `MEMBAR` / `ATOM` / `CCTL`, and an instruction-by-instruction diff between two reports of the same binary. Flags the split-warp barrier case explicitly. Tested against reports from ncu 2026.2.1.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## 评论 (1)

### youngjun-ii · 2026-09-04

Opened against the wrong repository by mistake, closing. Apologies for the noise.
