# [Issue #3605] [RFC] FlashInfer Release-Quality Action Plan

source: https://github.com/flashinfer-ai/flashinfer/issues/3605
state: open | updated: 2026-09-20T02:51:09Z
labels: op: moe

## 正文

# FlashInfer Release-Quality Action Plan

*Owner: Yang Xu · written for community review — feedback welcome.*

> **Status update 2026-09-06.** Both harnesses are merged and gate CI by default; the MoE fuzzer has
> since caught two more real bugs; Stream 0 landed a per-unit timeout runner. Sampling and Attention
> are still unstarted (contributors wanted — see §3); Norm/RoPE is being picked up by @0z5a. Changes
> from the June text are marked *(updated)*. Running tally of harness-found bugs added at the end of §3.

## TL;DR

Recent release-quality gaps cluster in low-precision and MoE, and reached users mainly because the
test signal was too weak to gate on and architecture coverage was thin. The plan: port one proven
test kit — 7 invariant oracles + an authoritative reference + adversarial inputs — op by op, run it
on a trustworthy, gating CI signal, and back it with complementary tiers (perf, compute-sanitizer,
framework-integration). Two harnesses (MoE, scaled GEMM) are already built and each found real bugs
soon after landing; the rest are net-new. Then re-audit what still escapes and repeat the loop.

## Why this doc exists

Downstream serving frameworks and users have flagged gaps in FlashInfer's recent release quality,
and the pattern is visible directly in our own issue tracker — e.g. attention quality regressions
(#1645), BF16 MoE stability (#3364), hangs (#3329), and MoE perf (#3521).

This plan lays out, grounded in that history: **what's broken, why it escapes today's tests, what
we're building to catch it before release, and — issue by issue — how much of the historical bug
stream each piece addresses.** The catch-rate figures are forward-looking estimates — from reviewing
past issues one at a time and judging what each harness will catch once fully built out, across
backends/dtypes/architectures — not a measurement of today's coverage, and are given as ranges.

## Precedent — a proven playbook, not a bet

The design here is borrowed from cuDNN, where it already worked. After cuDNN shipped
`test_mhas_v2` — a single consolidated attention fuzzer (one strong harness, an authoritative
reference, adversarial inputs), the direct model for the design below — attention-related bug
reports dropped substantially and the time from kernel-completion to end-to-end convergence
shortened (far fewer silent-correctness round-trips). We are porting that working system to
FlashInfer, op by op. The sharpest techniques carry over directly:

- **sparse + exact-grid inputs** so structural bugs aren't averaged away (a low-precision analog of
  the sparse-integer trick);
- **an authoritative reference recipe** as the single source of truth;
- **output-buffer poison** for the uninitialized / padding-leak class;
- **per-backend determinism (CRC) + a device-state probe** after each config;
- **compute-sanitizer racecheck + SASS forensics** for Heisenbugs (§4).

The point: this is a portable system, not a one-off. It is now validated on **two** ops (MoE and
scaled GEMM, §3) — and in both cases it found real bugs shortly after landing.

## 1. Diagnosis — why bugs reach users today

From a census of 2026-H1 issues (~131 bug issues, 161 merged fix-PRs):

1. **The dominant clusters are low-precision and MoE.** MoE alone ≈ 31% of bug issues; the
   low-precision FP4/FP8/MXFP8 GEMM+MoE cluster ≈ 36%; attention/KV is another large slice.
2. **~60% of fixes land in the Python dispatch / validation / marshaling layer, not deep in the
   kernel** — i.e. most bugs are integration and contract bugs, not exotic math.
3. **The test signal was too weak to gate on.** Some classes — notably hangs and timeouts — could
   pass without surfacing, and the suites that did run were too gentle to fail on real bugs (point
   4). Together these let bugs reach users even on paths CI nominally exercised. Strengthening the
   signal so a real bug reliably turns the build red is the highest-leverage fix and is in progress.
4. **Existing low-precision tests are gentle:** fixed shape grids, loose `cosine > 0.97`, a single
   autotune mode, no edge inputs / output-poison / determinism / device-state checks.

The takeaway that shapes everything below: **the same ~7 failure classes recur across every op**
(§2). So we don't need 7 unrelated test efforts — we need **one invariant "kit"** (no-crash,
reference-numeric, determinism, output-poison, autotune sweep + real-path, device-state probe)
applied per op, where the only per-op work is the **authoritative reference** and the **input
model**. That kit is now proven on two ops; it generalizes.

## 2. The recurring bug classes (and the oracle that catches each)

| # | Bug class | Representative examples (any op) | Oracle that catches it |
|---|---|---|---|
| C1 | Numerical wrong-output / accuracy | MoE #3197, #2822; GEMM #3103; fp8 #2431; sampling #2320 | numeric vs authoritative reference + sparse exact-grid inputs |
| C2 | NaN / Inf where ref is finite | #2595 (cutlass fp8), #1646 (cutlass MoE), sampling #2402 | reference-aware no-NaN |
| C3 | Crash / IMA / device-assert | MoE #3427, #2776; GEMM #2516, #3085 | no-crash + device-state probe (+ compute-sanitizer, §4) |
| C4 | Uninitialized / padding-leak into real output | mm_fp4 #2861 | output-buffer poison |
| C5 | Determinism / intermittent | sampling #3470, #2284; intermittent MoE NaN | per-backend CRC determinism + N-run stress (§4) |
| C6 | Autotune: tactic / profiling / cache | MoE #3168, #3197; bmm_fp8 #3085 | tactic sweep + autotune-ON real path + cache-coherence |
| C7 | Arch coverage / dispatch / marshaling | MoE #3466 (missing SM103 cubin), #3359; mm_fp4 #2577 | arch axis in matrix + build-manifest oracle |

These seven are the engine. Each op below is just *which classes dominate + what the reference is.*

## 3. Per-op map — status, dominant classes, and projected catch

Denominator throughout = **bug issues only** (feature requests / RFEs excluded entirely).

| Op | Harness status | Dominant classes | Representative issues | Projected full-catch |
|---|---|---|---|---|
| **MoE** | ✅ merged, **gating by default** (#4475, 2026-08-19); curated seeds + activation-matrix drift check (#4805) *(updated)* | C1, C3, C6, C7 | #3197, #2822, #1646, #3427, #2776, #3168, #3466, #3359 | ~half of in-scope, audited · **4 real bugs found so far** (tally below) |
| **Scaled GEMM / BMM** | ✅ merged (#3539, 2026-07-14), gating on the H100 lane *(updated)* | C1/C2, C4, C3/C6, C7 | #3103, #2595, #2861, #3085, #2516, #2577 | comparable to MoE; simpler (no routing) · **2 real findings**, ledger holds 1 open entry |
| **Sampling** | to build — **unstarted, contributor wanted** | C1, C2, C5 | #3470, #2320, #384, #2402, #2284 | high — small, correctness-dominated surface |
| **Attention / MLA** | to build (largest effort); a POC reject-or-correct paged-prefill fuzzer exists in #4015 (stalled since July) and already found + fixed one bug (#4014) — **contributor wanted** *(updated)* | C1, C4, C3/C7 | #1645, #2208, #2409, #2408, #1971 | moderate — see note |
| **Norm / RoPE** | to build (cheapest) — **in progress: @0z5a** is taking the rmsnorm output-contract slice first *(updated)* | C1/overflow, dispatch | #3005, #2271, #730, #194 | moderate, low effort |

*Attention note: the C1/C4 quality-and-correctness bugs (including the #1645 attention quality
regression) are catchable; the limiter is attention's larger share of perf and
framework-triggered bugs, which are covered by the complementary tiers in §4 rather than the
single-op harness.*

Two harnesses are done and gating; the rest are net-new work in the same style.

**MoE harness (DONE — merged, default-ON).** Drives the real unified MoE API with all 7 oracles, a brutal config
space (non-pow2 / odd-token / EP-shard / routing-skew, memory-budgeted for parallel CI), a
known-failure ledger, and an autotune cache-coherence scenario. It found **2 real bugs in the new
API shortly after landing**: an EP-shard case producing all-zero output (#3547) and a calibrated
scale silently inflating output (#3548). *(updated)* Since then it went default-ON in CI with the
subsumed legacy UTs pruned (#4475), gained curated seeds for the CUTLASS / b12x backends plus a
CPU check that the documented activation matrix matches the runner declarations (#4805), and
caught two more real bugs: a cross-call device-state corruption from an unpredicated finalize
epilogue (#3957, fixed by #4186) and MxFP8 weight scales missing the 128x4 interleave after the
row shuffle (#4087, fix #4093 open).

**Scaled GEMM / BMM harness (DONE — merged #3539).** One fuzzer over the whole scaled-GEMM family
(bf16 / fp8 / mxfp8 / nvfp4 / mxfp4, `mm` + `bmm`) on the same 7-oracle kit, plus a **cross-backend
convention auditor** (each API declares its scale convention; backends sharing a convention must
agree numerically). It already surfaced real issues: a cuDNN bf16→fp16 miscompute on Hopper for
non-power-of-2 M in one cuDNN point release (now guarded inside the FlashInfer API), and a
both-backend `bmm_mxfp8` batched scale-factor bug (#3604). **This is the key generalization
datapoint** — the MoE playbook ported to a second op and immediately caught bugs, with only the
reference + input model written fresh.

**Harness-found bugs — running tally** *(new)*. This is the only measured (not projected) catch
data in the plan; kept current as fixes land.

| # | Found by | Class | Status |
|---|---|---|---|
| #3547 EP-shard all-zero output | MoE | C1 | ✅ fixed |
| #3548 activation global_scale silently ignored | MoE | C1 | open (fix #3592 closed unmerged) |
| #3957 cross-call device-state corruption, CuTe finalize N-tile overrun | MoE | C3 | ✅ fixed (#4186) |
| #4087 MxFP8 weight-scale interleave missing after row shuffle | MoE | C1 | open (fix #4093) |
| cuDNN bf16→fp16 miscompute, non-pow2 M, Hopper | GEMM | C1 | ✅ guarded in API |
| #3604 bmm_mxfp8 garbage for b>1, M%128≠0 (cuDNN + CUTLASS) | GEMM | C1/C3 | open (fix #3666); ledgered, crash-capable on cu129 |
| #4014 cuDNN attention scale missing from graph-cache key | Attention POC (#4015) | C6-like | ✅ fixed |

**Why catch-rate climbs over time.** The gap between *caught outright* and *at least flagged* is
mostly shape-luck and intermittence — both are sampling problems. Retiring the now-subsumed per-op
tests frees CI capacity to fuzz several× longer, and the fuzzers are fully seed-deterministic so any
catch reproduces from the test id alone. Curated production shapes (for shape-luck) and N-run stress
(for intermittence) buy that conversion more cheaply than brute-force time. Neither helps the
tolerance-floor cases (an oracle-strength problem the Phase 2 re-audit loop would prioritize) nor
the no-oracle-exists cases (needs the
build-manifest oracle).

## 4. Force-multipliers — the complementary tiers

A correctness net can't see everything. Alongside one hard precondition (A), we run three
complementary tiers (B–D) that close most of what it structurally can't — these are part of the same
release-quality program, not a separate workstream:

**(A) A robust, gating CI signal + broader architecture coverage — the #1 lever.** Beyond the gentle
test content already diagnosed in §1, two infra gaps let bugs through, and both are being closed:

- **Signal robustness / SNR.** CI must reliably catch hangs and timeouts and turn them red, and the
  low-precision suites must PR-gate (not nightly-only) so a real failure blocks the build rather than
  passing silently. This directly closes the **hang class** (#769, #3329, #2933-class) — exactly the
  mode a weak timeout signal hid; a per-test timeout + N-run stress make hangs deterministically red.
  *(updated)* **Landed:** the unit-test runner now shards with per-unit timeout budgets and a
  timeout policy, replacing the 7200 s per-file cap (#4141, #4359). Both fuzzers are default-ON.
  **Caveat that explains most of the theoretical-vs-actual catch gap:** public PR CI has no Blackwell
  runner (T4 / A10G / H100 only), so the fuzzers gate pre-merge on SM90 only; the Blackwell-only
  backends — most of the MoE surface — are gated post-merge by the internal daily runs. Until a
  Blackwell lane exists pre-merge, "gating" for those backends means "red the next day".
- **Architecture coverage.** Historically thin, and several escapes were arch-specific (#3466 missing
  SM103 cubin, #2577 SM120 all-backends-fail, #3359) — this is being actively broadened. Every test
  axis (and the build-manifest check in Stream 2) should span the full supported SM range.

Until the signal is both robust and demanding, the catch-rates here stay theoretical — no oracle
improvement substitutes for a gate that actually fires.

**(B) Perf-regression tracking** (in progress; no in-tree evidence yet as of 2026-09-06) closes the perf class we exclude from the correctness
harnesses by design (#3521, #3537, #2992, #2671, #2859, #1753 — perf is ≈10–15% of issues).

**(C) A compute-sanitizer weekly wrap** around the same fuzz configs catches the race / IMA /
device-corruption class that single-run correctness misses, and — key — turns **Heisenbugs into
deterministic failures** (#3168, #3427, #3085, intermittent-NaN class, #2776). Near-zero to build —
the same tests, just wrapped — and run on a weekly cadence since the sanitizer is slow. *(updated)*
Internal QA already runs suites under compute-sanitizer (tests started needing sanitizer-aware skips,
#4493); there is no in-tree workflow yet. (A proven
technique — the same racecheck / SASS forensics approach root-caused a Blackwell matmul buffer-race
in cuDNN; it transfers directly.)

**(D) Framework-integration tests** (drop a new FlashInfer into known-good vLLM / SGLang and run
their suites — in progress; no in-tree evidence yet; see @ormandj's SM120 TP2 findings below for
concrete Tier D / C7 gate candidates, #3930 still open) reproduce the framework-glue / dispatch-triggered class single-op
harnesses can't: a real kernel bug that only surfaces through a live dispatch + concurrency sequence
(#3427, #3390, #3329, the framework-observed side of #1645). It also catches higher-level
integration / regression bugs (API-contract drift, end-to-end accuracy) no kernel-level oracle sees;
if the integration matrix includes multi-GPU TP/EP, it reaches into the multi-rank class otherwise
structurally out of scope.

**How much this catches.** With the harnesses gating in CI plus the three tiers, the
program would have *touched* (some tier flags it) **a large majority** of historical bug issues. The
share that would *reliably gate the build red* — deterministically block a release, not just
flag-when-lucky — is a smaller core, which the roadmap's curated shapes + N-run stress + longer fuzz
steadily grow. The irreducible remainder is structural: **multi-node / multi-rank collectives**
beyond the integration matrix (e.g. #3530, #3279) and **build / packaging / air-gapped artifacts**
(#3466-class). For context, today's effective pre-release catch on the dominant low-precision/MoE
class was near-zero — under a signal too weak to gate on.

## 5. Plan of record

**Phase 0 — land what's done.** MoE harness → merged; Scaled GEMM/BMM harness (PR #3539) → merged
2026-07-14; verify-to-close the harness-found findings as their fixes land (the known-failure ledger
auto-flags each fix). *(done; 3 findings still open, see tally in §3)*

**Phase 1**

- **Stream 0 — make the CI signal trustworthy + gating.** Strengthen the signal so hangs/timeouts
  surface; confirm the low-precision suites PR-gate (not nightly-only); triage what newly surfaces.
  Highest leverage; unblocks everything else. *(updated: per-unit timeout runner landed, fuzzers
  default-ON with legacy UTs pruned; remaining = a pre-merge Blackwell lane, see Tier A.)*
- **Stream 1 — replicate the pattern, one tester at a time** (concrete testers, no premature
  abstraction). Scaled GEMM is **done** (the simplest port — no routing — already finding bugs).
  Remaining, in the proven style: **(a) Sampling** (cheap, high-yield, distributional reference;
  **unassigned**) → **(b) Norm/RoPE** (cheap; **@0z5a**, starting with the rmsnorm output-contract
  slice) → **(c) Attention/MLA** (largest; online-softmax-aware reference + mask/padding poison;
  directly targets the #1645 quality-regression class; POC in #4015, **unassigned**). Extract a
  shared invariant-kit only after a third tester reveals the real common shape — the ledger
  (`tests/test_helpers/fuzz_ledger.py`) is the first piece already shared by both fuzzers.
- **Stream 2 — complementary tiers.** Perf-regression tracking (in progress) + framework-integration
  tests (in progress) + a compute-sanitizer weekly wrap + a **build-manifest / arch-coverage check**
  (every advertised backend×quant×arch actually instantiates a kernel — closes the missing-cubin
  class).

**Phase 2 — re-audit and iterate.** This is a loop, not a one-shot. Once Phase 1 is in place
(harnesses + a trustworthy, gating signal + the complementary tiers), re-measure the bug-escape
stream against the now-stronger gate: what still reaches users? Feed that back into the same
diagnose → build → gate cycle, each pass targeting the next-largest remaining escape class — e.g.
deepening whichever oracle the re-audit shows is still too weak (a current candidate: the
cross-backend reference on quantized modes). The re-audit sets the priority, not up-front guesswork.

## Appendix — method & provenance

- **Catch-rate figures** are issue-by-issue estimates given as ranges; non-MoE per-op figures are
  projections by analogy that become measured as each harness lands.
- **Issue IDs** in §2–§3 were verified against `flashinfer-ai/flashinfer` (open/closed + titles).
- **Harnesses in-tree:** unified MoE API fuzzer `tests/moe/test_unified_moe_fuzz.py` (merged,
  default-ON); unified Scaled GEMM/BMM fuzzer + convention auditor `tests/gemm/test_unified_gemm_fuzz.py`
  (merged #3539); shared known-failure ledger `tests/test_helpers/fuzz_ledger.py`.
- **Distinction that matters for reading the numbers:** *touched* (some tier flags the issue) is a
  larger set than *reliably gates red* (deterministically blocks the release). The roadmap converts
  the former into the latter over time; the structural remainder (multi-node collectives + packaging)
  stays out of scope for kernel-level testing.

<!-- note to self: claude::d6f47b32-e07c-43ec-9755-cd807049d528 — "tracker #3605 status refresh 2026-09-06"
cwd /home/scratch.yanxu_libs/flashinfer -->


## 评论 (12)

### leonardHONG · 2026-06-16

Hi — once the fuzzer/API harness lands, is there any clean slice here I could help with? Happy to pick up whatever would be useful.


### ormandj · 2026-07-14

Three current SM120 TP2 integration findings map directly to Tier D/C7:

- vllm-project/vllm#48303: the FlashInfer CUTLASS MXFP4 backend existed, but DeepSeek-family weight conversion was missing, so explicit selection failed during worker initialization. The focused fix has controlled end-to-end A/B data.
- #3930 / #3676: loaded-library substring matching selected TileLang’s `libcudart_stub.so`, so communication-workspace initialization failed. Filename-based matching plus the anchored matcher/collision tests supplied on #3930 fixes the reproduced initialization path; this is not a performance claim.
- vllm-project/vllm#48054: vLLM uses a 0.6.14-only sparse-MLA signature while pinning FlashInfer 0.6.13. Python 0.6.14 is on PyPI; cubin 0.6.14 is only on FlashInfer’s index; JIT-cache 0.6.14 is on the official cu129/cu130 indexes; no cu133 index is published.

Suggested Tier D/C7 gate: assert the selected backend, start the TP2 workspace with loaded look-alike libraries, execute semantic requests, and record exact Python/cubin/JIT-cache versions and source indexes.


### 0z5a · 2026-09-06

Thanks @YangXu1990uiuc for [confirming this slice](https://github.com/flashinfer-ai/flashinfer/issues/3605#issuecomment-5564614029). **The first RMSNorm output-buffer contract PR is open: #4994**, head `92da53c4c4b9a2a5d261650b401dd891904ba0b5`. This updates my earlier local-only preparation status.

It adds 80 deterministic cases inside the already CI-invoked `tests/utils/test_norm.py`: FP16/BF16, 2D/3D inputs, an odd 2D hidden size, dense/offset-and-row-padded buffers, and zero/tiny/sparse/alternating/large-but-finite inputs. It reuses the existing FP32 reference and checks poisoned-output overwrite, exact repeatability after changing poison, input/weight preservation, return-buffer identity and untouched output padding.

The exact patch passed on L20/SM89 through both actual dispatch paths: **CuTe 80 passed; forced CUDA 80 passed**, zero failures/errors/skips in each JUnit result. The worker verified the requested path and pinned source/submodule hashes before execution. Runtime: Torch 2.13.0+cu130, CUDA 13.0, CUTLASS DSL 4.6.2, TVM FFI 0.1.11. Full `pre-commit run --all-files` passed.

This is test-only correctness coverage on one architecture, not a kernel-defect or performance claim. It does not add a backend, duplicate the existing Triton/RoPE/reduction/FP8-clamp implementations, or complete the full Norm/RoPE or seven-oracle program. PDL, quantized variants, other architectures and the wider fuzzer remain outside this first PR.

AI-assisted test implementation; the repository PR template and executed-validation limitations are preserved. Upstream maintainer review and GPU CI remain pending.

### YangXu1990uiuc · 2026-09-07

> Hi [@YangXu1990uiuc](https://github.com/YangXu1990uiuc) — could I take a bounded test-only slice of the Norm/RoPE stream: caller-owned output correctness for the existing public `flashinfer.norm.rmsnorm` API?
> 
> I checked main `6c14bbd5ff34210404d5d4b5f6ff3b4b2527f59f`, its existing shape/stride and trace-reference tests, and the relevant open work including Triton coverage [#4060](https://github.com/flashinfer-ai/flashinfer/pull/4060), RoPE bounds [#4349](https://github.com/flashinfer-ai/flashinfer/pull/4349), RMSNorm reduction optimization [#2519](https://github.com/flashinfer-ai/flashinfer/pull/2519), and Spark follow-ups [#4877](https://github.com/flashinfer-ai/flashinfer/pull/4877). The proposed scope does not add a backend or duplicate those implementations, the FP8 clamp work, or a repo-wide harness.
> 
> The local preparation adds 80 deterministic cases inside the already CI-invoked `tests/utils/test_norm.py`: FP16/BF16, 2D/3D inputs, an odd 2D hidden size, dense/offset-and-row-padded buffers, and zero/tiny/sparse/alternating/large-but-finite inputs. It reuses the existing FP32 reference and checks both poisoned-output overwrite and exact repeatability after changing the poison, input/weight preservation, return-buffer identity, and untouched output padding. Applicable pre-commit hooks and syntax checks pass. **No kernel defect or GPU pass is claimed yet.**
> 
> GPU preparation is underway for explicit CuTe-DSL and forced legacy-CUDA dispatch on an L20/SM89, with pinned source/submodule hashes and no silent fallback counted as the requested backend. PDL, other architectures, quantized variants, performance, and completion of the full seven-oracle program remain outside this first slice.
> 
> Is someone already covering this particular boundary, or would a small assigned subtask / integration into an existing effort be useful? I will keep the patch local pending coordination. This preparation uses AI assistance; any submission will keep the repository PR template and report the actual executed validation, including limitations.
> 
> Validation update (September 6): the exact 80-case patch passed on L20/SM89 through both actual dispatch paths: CuTe **80 passed**, forced CUDA **80 passed**, with zero failures/errors/skips in each JUnit result. The test worker checked that the requested path was selected and verified all source/submodule hashes before execution. Runtime: Torch 2.13.0+cu130, CUDA 13.0, CUTLASS DSL 4.6.2, TVM FFI 0.1.11. The full `pre-commit run --all-files` also passed. This is correctness coverage for this API boundary on one architecture, not a performance or kernel-defect claim; the patch remains local while coordination is pending.

Hi @0z5a thank you for volunteering for this part! I don't think anybody is working on this right now, feel free to take it!

### YangXu1990uiuc · 2026-09-07

Status refresh posted in the body (§3 table, new "harness-found bugs" tally, Tier A / Stream 0 updates; changes marked *(updated)*).

@leonardHONG — sorry for the slow reply to your June offer. Both fuzzers are now merged and gating, so the pattern to copy is concrete: `tests/gemm/test_unified_gemm_fuzz.py` is the simplest port (adapters + a canonical reference + the shared ledger in `tests/test_helpers/fuzz_ledger.py`). Two slices are open and unassigned:

- **Sampling** (Stream 1a): small surface, correctness-dominated; the novel part is a distributional reference (exact CDF / chi-square against `torch.multinomial`-style ground truth) plus the -inf / duplicate-logit / top-k=vocab edge inputs. Cheapest of the two.
- **Attention / MLA** (Stream 1c): largest; online-softmax-aware reference + mask/padding poison. #4015 is a stalled POC of the reject-or-correct fuzzer for paged prefill you could start from rather than from scratch.

Norm/RoPE is being taken by @0z5a. If either of the above interests you, say which and I will write up the concrete first slice (oracle list, input model, done criteria) the same way.


### leonardHONG · 2026-09-08

Thanks for the follow-up! No worries about the delay.

I’d be interested in taking the Attention / MLA slice. I can start from #4015 and build from there.

A concrete first slice with the oracle list, input model, and done criteria would be really helpful. Thanks!


### YangXu1990uiuc · 2026-09-08

@leonardHONG great — here is a concrete first slice. It is deliberately **MLA**, not the paged-prefill fuzzer: #4015 (paged attention) is moving daily and would collide with you; the Batch MLA wrapper just got its backend isolation in #4697 and has **no reject-or-correct harness yet**, so it is the same job on a fresh, stable surface.

## Slice: reject-or-correct fuzzer for `flashinfer.mla.BatchMLAPagedAttentionWrapper`

**Property (the whole point):** for ANY input — valid, malformed, or value-corrupted — a call either raises a clean, actionable error, or returns results matching an independent fp32 oracle. Silent garbage always fails the suite.

**Template to copy:** `tests/experimental/test_paged_attention_fuzzer.py` + `test_paged_attention_prototype.py` (`make_problem` / `run_unified` / `_run_and_check` / mutation table / `KNOWN_GAP_MUTATIONS` pattern) and the shared ledger `tests/test_helpers/fuzz_ledger.py`. Design doc for the target: `docs/design_docs/batch_mla_backend_architecture.md`; existing tests: `tests/attention/test_mla_wrapper.py`, `test_deepseek_mla.py`.

**Oracles (all 7, in this order):**
1. no-crash + clean error: every rejection is `ValueError`/`TypeError` with a non-empty message that names the fix.
2. numeric vs an independent fp32 reference: q = `[q_nope | q_pe]`, k = `[ckv | kpe]` gathered by page table, v = `ckv`; causal and non-causal; compare `out` and, when requested, `lse`.
3. reference-aware no-NaN/Inf.
4. determinism: two runs of the same config, byte-identical (CRC) per backend.
5. output poison: pre-fill caller-owned `out`/`lse` with NaN; every element the contract covers must be overwritten, nothing outside it touched.
6. plan/run contract drift: run options that disagree with the plan (`lse_mode`, dtype, split vs packed) must be rejected, not silently coerced.
7. device-state probe after each config (a small independent kernel + sync) so a stray write is attributed to the config that made it.

**Input model (axes to sample):** `head_dim_ckv=512`, `head_dim_kpe=64` (that is the MLA shape; the CUTLASS backend hard-requires it); `num_heads ∈ {16, 32, 64, 128}`; `page_size ∈ {1, 16, 32, 64}` (CUTLASS: ≤128 and divides 128); `q_len ∈ {1, 8, 33}`, `kv_len ∈ [64, 4096]` ragged per request; `batch ∈ [1, 8]`; dtypes bf16/fp16, plus fp8-e4m3 KV on fa2/fa3 SM90 with the per-tensor `kpe_scale`/`ckv_scale` contract; metadata `MLAPlanMetadata.csr(...)` vs `.dense(...)`; query/KV `packed` vs `split`; `lse_mode ∈ {none, base2, basee}` (LSE base is an oracle axis, not an assumption — see #4663 for why); backends `fa2`, `fa3`, `cutlass` (SM100/103 only, non-causal, exactly 128 heads), and `auto`. Declare per backend only what you machine-check.

**Mutations (each either rejected cleanly or still correct):** non-monotonic / non-zero-start `qo_indptr`; `kv_indptr` not matching `kv_indices` length; `kv_len_arr` exceeding page capacity; under-claimed batch dims; wrong dtype / device / rank on any metadata tensor; over-allocated `kv_indices` tail filled with a NaN page; split query given to a packed-only backend; `lse_mode` mismatch plan vs run; wrong-shape/dtype `out`/`lse` buffers; CUDA-graph re-plan with a changed batch size (must be rejected). Out-of-pool page-id **values** are a documented trusted input — mark that mutation `xfail` like we do, don't drop it.

**Done criteria:**
- `tests/attention/test_mla_paged_attention_fuzz.py` (MLA is stable → `tests/attention/`), default-ON, `FLASHINFER_MLA_FUZZ_NUM_TESTS` (default ~150), `FLASHINFER_MLA_FUZZ_ONLY_SEED` for one-seed repro, every failure prints its repro command.
- Known failures go through `FuzzLedger` with the issue number, never through `skip`.
- Green on H100 (fa2/fa3) and one SM100 box (fa2/cutlass) in the PR description with counts.
- Anything real it finds is filed as an issue with the seed and added to the tally in this tracker.

If you want, open a draft PR early with just `make_problem` + the reference + one backend and I will review the oracle before you fan out across axes.


### leonardHONG · 2026-09-09

Thanks for the detailed write-up! I’d be happy to take this on. I have access to a Hopper GPU and can validate fa2/fa3 there, but I don’t currently have access to an SM100 GPU. Would someone be able to help with the SM100 validation?

I’ll start with a draft PR covering `make_problem`, the fp32 reference, and one backend so you can review the oracle before I expand the coverage.

### JulianZJN · 2026-09-09

Hi @YangXu1990uiuc — I'd like to take the Sampling / Stream 1a slice, keeping it separate from the ongoing MLA and Norm/RoPE work.

For the first test-only PR, I propose the existing probability sampling, top-k and top-p APIs: an independent filtered-distribution reference; deterministic support/degenerate-case invariants; a bounded distributional check with an explicit false-positive budget; adversarial zero-probability, duplicate-value and k=vocab cases; and single-seed replay using the existing FuzzLedger pattern. I will preserve the existing sampling tests rather than replace them or introduce a repository-wide harness. Same-seed equality will only be asserted within a documented deterministic path, not between unrelated RNG implementations. Undefined invalid-input behavior will not be assigned a new contract by the tests.

I have RTX 4090 / SM89 resources for initial validation. This is not a claim of Hopper/Blackwell coverage or of a discovered kernel defect. Could you confirm the preferred first-slice API list and CI budget, or point me to any overlapping Sampling work not yet linked here?

### JulianZJN · 2026-09-19

@YangXu1990uiuc Sampling / Stream 1a is up as #5341. Same shape as the GEMM fuzzer (seeded cases, shared ledger, single-seed repro), with a float64 reference for top-k / top-p / joint / top_k_first and a small χ² check with a fixed false-positive budget.

One for the harness-found tally: per-request `top_k` (and `min_p`) with `indices` reads the threshold by output position instead of by probs row, and out of bounds when `len(indices) > probs.size(0)`. Issue #5339, fix in #5340.

Validated on SM89 only. Next slice I'd suggest is `min_p` plus the logits entry points once the fix is in; happy to take it.


### 0z5a · 2026-09-19

The Sampling side of the quality-fuzzing plan is up as a **draft** in #5346 (base `dc04f50c9aa3eabcdaa5feb0934edb3d85e9529a`), because the CPU layer is green while the GPU layer is not yet.

Two production defects fell out of building the independent oracle, both about per-row filter parameters under `indices`:

- `TopKSamplingFromProbKernel` read `top_k_arr[bx]` and `MinPSamplingFromProbKernel` read `min_p_arr[bx]`, while the launcher validates that tensor against `probs.size(0)` (unique rows). Whenever `indices` reuses rows, that is an out-of-bounds device read and the wrong row's parameter; both now key on `row_idx`, as the top-p and joint kernels already did.
- The shims always materialised the per-row `top_k` tensor as `int32`, while the C++ side reads that buffer as the output `IdType`. With int64 `indices` the int32 buffer was read as int64: garbage `k` (filtering silently disabled) plus an OOB read. It is now materialised in the output dtype.

Suite shape: contract table per API with the source line each fact came from; an independent CPU oracle that implements softmax and the filters itself (`top_k_first` and `joint` get separate references); a deterministic layer (one-hot/unique candidates, fixed `seed`+`offset` replay); and a distribution layer with a pre-declared budget (`K = 44`, `alpha = 0.01`, `N = 200000`, half width 0.004765) calibrated against pure reference sampling — 0/30 false positives, power 0.833 at 1.0x half width and 1.000 at 2.0x. Failures dump seed/offset, input rule, filter order, thresholds, indices, reference support and observed frequencies.

```
python -m pytest -q tests/sampling/test_sampling_contract_cpu.py     # 12 passed
```

GPU layer, first live run on the L20, one GPU, shard 0/4: `25 failed, 3 skipped`. Two classes: the harness itself indexes a CUDA tensor with a CPU index tensor (`singular.repeat(case.calls)[rows]`), and the first `illegal memory access` lands in `struct/keying/top_k_int64` — exactly the int64-indices scenario fixed above — after which the poisoned context fails the remaining cases. Whether the kernel still reads out of bounds on some path or the harness feeds an invalid input is not attributed yet; the next step is a single-case run with `CUDA_LAUNCH_BLOCKING=1` against both the patched and unpatched trees, and I will update the PR with the result.


### 0z5a · 2026-09-20

Attribution follow-up for the GPU-layer failure reported above, since it changes who owns it.

The `struct/keying/top_k_int64` case was run alone with `CUDA_LAUNCH_BLOCKING=1` twice: once on the patched tree and once on a clean worktree of the base commit `dc04f50c` with no patch applied. Both fail identically:

```
RuntimeError: Check failed: (status == cudaSuccess) is false:
TopKSamplingFromProbs failed with error code an illegal memory access was encountered
csrc/sampling.cu:225
```

So that out-of-bounds read is **pre-existing upstream behaviour**, not something the two fixes in #5346 introduce or claim to fix. The two fixes there are the per-row parameter keying (`top_k_arr[bx]`/`min_p_arr[bx]` → `row_idx`) and materialising the per-row top-k buffer in the output dtype; this case still trips the launcher check on both trees, so it needs a separate look at what else is indexed out of range when `indices` is int64. The suite keeps it as a known-failing case rather than dropping or xfailing it silently.

Two things I cannot decide on this machine (L20, SM89), both queued for an SM90+ box:

- whether the OOB is SM89-specific or reproduces on Hopper;
- whether the remaining failures after the context is poisoned hide any additional distinct defect.

They are in `h100-test/flashinfer-a1-20260920/` together with the SM90/SM100 items from the other PRs.

