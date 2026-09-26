# [Issue #3920] [RFC] Autotuner v2: FlashInfer-managed persistent cache and deployment-matched measurement

source: https://github.com/flashinfer-ai/flashinfer/issues/3920
state: open | updated: 2026-09-20T12:50:54Z
labels: RFC, autotuner

## 正文


**Status (2026-09-08)**: #3861 **merged** (`3a75b4e3`, ships in v0.7.0; opt-in, v1 untouched). Framework migration has started: vLLM draft vllm-project/vllm#55671, validated on 4×B200 at TP=1/2/4 (see the status comment below). Design rationale and the graduation plan live in-tree at `docs/design_docs/autotuner_v2.md`; `docs/autotuning.rst` documents `autotune_v2` as experimental. This RFC remains the discussion thread for the roadmap and open questions.

## Summary

FlashInfer should own the persistence and compatibility rules for its autotuning results. Frameworks such as vLLM and SGLang should decide *when* to warm up and how to coordinate distributed workers — but they should not construct FlashInfer cache keys, interpret its JSON schema, or manage cache files, as they do today.

The proposal has four parts:

1. **A managed persistent cache** (`autotune_v2()`): environment-hashed directories, one atomic entry per tuned operation, invalid entries are misses (never errors), old generations left on disk.
2. **A measurement policy** (`MeasurementPolicy`): tune the way you deploy — eager vs CUDA-graph execution as the primary axis, cold-L2 as a secondary one.
3. **A runner contract**: rules that make "serving executes the tactic the tuner chose" structurally guaranteed rather than convention-enforced.
4. **An accuracy harness**: tuner quality ("picks the fastest tactic") becomes a measured claim (regret vs. an oracle), not an assumption.

Autotune data is a disposable performance optimization. Cross-version cache migration is a non-goal: after an upgrade, paying the tuning cost once for the new environment is acceptable. This follows the compiler-cache patterns of Triton and `torch.compile`/Inductor: key artifacts by program + compiler + environment, publish atomically, treat unusable entries as work to rebuild, own the local cache, and expose only an opaque export/import boundary.

## Evidence 1: how frameworks actually use v1

A survey of vLLM and SGLang (HEAD, 2026-07) shows both use exactly one pattern — **one-shot startup warmup around a whole-model dummy forward, before CUDA-graph capture; serving always runs outside any context**:

- **vLLM**: rank 0 runs `autotune(tune_mode=True, cache=<path>)`, broadcasts the raw JSON file bytes, every rank atomically rewrites the file and calls `load_configs(path)`. The cache path is a vLLM-computed `sha256(compile-factors)` directory — vLLM had to reinvent cache hashing, atomic writes, and an enable knob.
- **SGLang**: every rank tunes simultaneously (the dummy forward contains collectives, so rank-0-only tuning deadlocks DeepEP), with **one JSON file per rank**, its own model/quant/parallelism hash, its own disable env.
- **Features with zero external use**: `tune_mode=False` in serving, `tuning_buckets`, `round_up`, direct `save_configs`, `FLASHINFER_AUTOTUNER_LOAD_FROM_FILE` (the last has been silently broken since #3367 with zero reports — confirming zero users). `skip_ops` has latent demand (vllm-project/vllm#46238 wants per-op exclusion; SGLang disables autotune entirely for some models because one op crashes).
- **Exhibit A for key completeness**: vllm-project/vllm#43119 — the v1 file cache missed `use_8x4_sf_layout` in its key, invalid tactics were replayed, and vLLM **disabled the persistent cache for all multi-rank deployments** (still disabled on the general path today, even after the flashinfer-side fix in #3367). A single key-completeness bug cost the feature its default.

Implications used throughout: reuse must not require an active context; the hashing/broadcast/knob code both frameworks built is exactly the policy FlashInfer should own; concurrent all-ranks tuning must be safe; key completeness needs a contract, not vigilance.

## Evidence 2: what field issues say

An audit of open autotuner-related issues clusters them into buckets; this RFC addresses the first four:

| bucket | issues | how this RFC addresses it |
|---|---|---|
| cross-rank tactic divergence | #3186, #3537 | shared store + planned rank-consistency step; composes with #3187 (see distributed section) |
| tuned tactic slower than default | #3537, #3622, #3409 | accuracy harness diagnoses; planned regression guard (default path always races as a candidate) |
| stale/invalid tactic at execute time | #3566 (mitigated by #3437), vllm#43119 | runner contract rules 1/4/5; environment-fingerprint invalidation |
| measurement ≠ deployment | #3648, #3719 | `MeasurementPolicy(execution_mode=...)` |
| probe-tensor crashes | #3558, #3569, #3085 | `skip_ops` quarantine is the mitigation; root fixes are separate work |
| kernel/candidate coverage (SM120 etc.) | #2992, #3119, #2577 | out of scope (kernel-side); harness quantifies the cost |

Notably, none of the open issues complains about v1's persistence file itself — the field pain is consistency, selection quality, and validity. That is why measurement policy and the runner contract are first-class parts of this proposal rather than afterthoughts.

## Limitations of the v1 cache (brief)

The caller owns too much FlashInfer-specific policy (filename choice = cache identity); environment mismatch is awkward (whole file rejected, refuses to save back); a monolithic JSON is a poor concurrent-update unit (read/merge/write races; one corrupt file kills every entry); the namespace is coarser than the data (model-level filename prevents op-level reuse); integer tactic indices are not stable identities (#3707 is the focused correctness patch for that; orthogonal to and composable with this proposal).

## Design

### API: a standalone `autotune_v2()` entry point

v2 is deliberately a separate context manager, not new parameters on `autotune()` — v1 stays byte-identical, and the eventual v1 removal is a clean deletion instead of a subtle behavior change:

```python
with flashinfer.autotune_v2(
    mode="tune",               # "tune" (profile misses + publish) | "replay" (serve tuned winners)
    persistent_cache=True,     # touch disk at all?
    cache_root=None,           # placement-only ROOT DIRECTORY (not identity)
    measure=None,              # MeasurementPolicy, see below
):
    model(dummy_inputs)        # warmup forward; tuning is a side effect
```

`mode` names a positive action, not a negated flag — `mode="replay"` is the serving path (replay tuned winners, no profiling), which does *not* read like "throw away the tuning results" the way a `enable_tuning=False` boolean did. `persistent_cache` stays as the orthogonal disk toggle:

| `mode` | `persistent_cache` | meaning |
|---|---|---|
| `"tune"` | True *(default)* | tune misses, publish to disk |
| `"tune"` | False | tune in-memory only (disk-forbidden environments) |
| `"replay"` | True | serve from the on-disk cache (no profiling) |
| `"replay"` | False | no-op unless already hydrated |

**Attach semantics** (the key lifecycle decision, forced by the survey): `persistent_cache=True` attaches the store for the remainder of the process; the context scopes only *when profiling cost may be paid*. Both frameworks serve outside any context — a context-scoped store would silently regress serving to heuristics after warmup exits. Tune-on-first-call (Triton-style) is deliberately rejected for serving: latency jitter, collective deadlocks, must-precede-graph-capture, profiling OOM risk.

**One process, one ambient policy.** Ambient attach is action-at-a-distance — a bare `model(x)` uses whatever policy was last attached — but it is architecturally forced, not a stylistic choice: serving replays a captured CUDA graph (no Python runs at replay), and the autotuned ops are buried in layer forwards, so the tactic must be pre-resolved and read from process-global state with no context in scope. The idiomatic `with` belongs to *tuning* (a real scoped window, which warmup uses); serving is unavoidably context-free. Consequently `autotune_v2` does **not** nest (v2-in-v2 fails fast) and there is no per-region scoped-override knob: a process serves under one ambient policy (last-wins across sequential warmup contexts). This was validated against both consumers — vLLM and SGLang each open exactly one warmup context and then serve bare — so the removed machinery (a store stack, a `scope=` dimension) supported only a use case with no user.

**Mixed-mode (verified against vLLM + SGLang, current main).** Both frameworks *do* run the same autotuned op both eager and under CUDA-graph capture in one process at default settings, and this is the intended steady state, not transitional: decode runs under a FULL graph while large prefill (>~512 tokens in vLLM; MLA/MoE-A2A/DP prefill in SGLang) runs eager, and the autotune warmup forward itself is forced eager. **But it does not create a serving-time winner collision**: prefill (large M = num_tokens) and decode (small M = batch size) land in disjoint shape buckets, so the store's per-`(op, bucket)` entries are each served in one consistent mode. So FlashInfer does *not* need per-bucket dual-policy machinery. The one real residual is that warmup measures eager while decode is served under graph, and the tuned winner **does** flip between eager and graph/host-excluded measurement at decode sizes (measured: `bmm_fp8` and `mm_fp4` flip at M≤64 on B200) — so a decode bucket measured eager can be suboptimal. The fix is not per-bucket or per-region policy (there is no scoped override — see above): it is that the single ambient policy should match the mode-sensitive path — `cuda_graph`, since decode is graph-served and is where the flips concentrate, while large-M prefill served eager is mode-insensitive (so measuring it under graph costs little). Per-bucket / per-region dual measurement policy is an explicit **non-goal**.

`cache_root` is placement only — schema and environment namespaces live below it, so no choice of root can mix incompatible entries (unlike the v1 filename, which is identity-bearing). Observability is the mitigation for ambient state: loud INFO at attach, once-per-op "source=managed cache" hit logs, and a planned `AutoTuner.explain()` provenance dump.

### Store layout and runtime behavior

```text
<root>/v2/
  <environment_hash>/
    manifest.json               # canonical environment, human-readable
    entries/<operation_hash>.json
```

`environment_hash` = SHA-256 of a canonical manifest (flashinfer / CUDA / cuBLAS / cuDNN backend + cudnn-frontend versions, GPU, cache schema, measurement policy). A version change produces a new directory; old directories remain (downgrade-safe). `operation_hash` hashes one autotune lookup key (op identity, bucketed dynamic dims, dtypes/layouts, runner extras) — repeated layers and different models share entries when keys are identical.

Runtime rules: lookup on in-memory miss reads one entry file; missing, malformed, or key-mismatched entries are **misses, never errors**; tuning publishes each winner immediately via tempfile + atomic rename (no exit-time save, no read/merge/write, no locks; concurrent writers do redundant work, last valid write wins). Hit/miss memoization lives inside the store object — never in v1 state — so the hot path never re-touches the filesystem and v1/v2 mixing is impossible by construction.

### MeasurementPolicy: tune the way you deploy

The primary axis is the **execution mode** — whether per-call host cost counts — not the timer implementation:

```python
MeasurementPolicy(execution_mode="auto" | "cuda_graph" | "eager", cold_l2=...)
```

| deployment | policy | what it measures |
|---|---|---|
| CUDA-graph serving | `execution_mode="cuda_graph"` | capture + replay timing; host cost excluded, as deployment does |
| eager serving | `execution_mode="eager"` | per-call host cost included: the eager sustained rate |
| default (`"auto"`) | today's behavior | delay-kernel timing; hides host cost within its budget |

Why one measurand cannot serve both (measured on SM100, `bmm_fp8`, decode-size M): the same cuDNN candidate reads **~8 µs** host-excluded but **~329 µs** as an eager sustained rate — its execute path costs ~155 µs/call on the host. Under an eager policy the backend ranking flips (cublas < cutlass ≪ cudnn), matching what eager frameworks actually experience. Even the fastest backends are host-bound at decode sizes (17–21 µs host vs ~8 µs kernel), so this is a regime property, not a one-backend anecdote. This is the same problem class raised in #3648/#3719; graph-mode profiling additionally requires capture-safe runners, so `"cuda_graph"` stays opt-in per the contract below until the runner suite is validated.

The policy is part of the store's environment identity: entries tuned under different policies select different winners and never overwrite each other.

**Aggregation on noisy hosts (added from SM120 field feedback).** Sub-0.05 ms kernels go bimodal under co-tenancy, and single-shot medians flip winners run-to-run — so "tune the way you deploy" only holds if the measurement is stable. Independently confirmed while building the accuracy harness (a shared engineering-sample board threw phantom winner-flips), the harness settled on **interleaved rounds** — every round measures all candidates back-to-back with a rotating start offset — which matches the interleaved min-of-medians the #3905 SM120 sweep converged on. A **policy-level repeat/aggregation knob** (rounds + reducer) is the right home for this so it applies to production tuning, not just the offline harness; proposed, not yet in #3861.

### Runner contract

A backend audit found the same disease in three forms: a tactic interpreted *relative to runner-internal shape-keyed state* (cuDNN plan indices into per-bucket plan lists; cuBLASLt algo-list indices re-enumerated at raw runtime shapes — including a silent wrong-algorithm replay and a silently-discarded-tuning bug; a device-dependent compile-cache key gap in CuteDSL). CuteDSL is otherwise the model architecture: caches keyed by the tactic itself, kernels take shapes as dynamic arguments — the tactic *selects* the cache entry instead of indexing into it.

The contract:

1. **Tactics must be self-describing** (explicit parameter tuples) or index a shape-independent static table — never an index into an object that varies with shape, library version, or enumeration order. (#3707's structured `(engine, knobs)` tactics bring cuDNN into compliance.)
2. **Runner-internal caches must be keyed by the tactic**, never by a runner-derived shape bucket; where a shape component is unavoidable, the resolved bucket is pushed down by the autotuner, not re-derived by convention.
3. **Compile/graph/algo cache keys must include device identity** and every trace-time-baked parameter.
4. **Revalidate at runtime** where cheap (the CUTLASS `isValidConfig` pattern): a stale tactic is a loud error or a clean fallback, never a silent different kernel and never a dead server (#3566's failure mode). Status: the autotuner-side hook (`validate_tactic(inputs, tactic)`, covering in-memory and on-disk hits) is in #3861; per-runner adoption — cuDNN first, via its #3707 structured tactics — is tracked separately, so #3566's class is *guardable*, not yet guarded, until runners implement it.
5. **`get_cache_key_extras` must be synthesis-invariant** (no raw dynamic dims) — violation is exactly the vllm#43119 failure class; a debug-mode completeness check should back this mechanically. This extends to any consumer-visible execution dimension a runner exposes: e.g. CuteDSL compile caches treat dynamic-vs-static batch as separate entries, so a warmup that exercises only one silently misses the other unless that dimension is in the key. (Measurement policy is already in the entry key, which closes the eager-warmup / graph-serving aliasing.)
6. **A serving-time miss must not trigger unbounded host-side compilation** (added from SM120 field feedback). Concrete failure: `bmm_fp8(backend="auto")` on an untuned serving shape falls onto the cuDNN runner, whose graph build is an `lru_cache` on the exact GEMM shape — reported as a 12–17 s host-side build *inside the engine loop* on sm_12x (vllm#48210). Measured on that exact hardware (RTX PRO 6000 Blackwell, cuDNN 9.24), a single plan builds in <1 s and a full `policy=ALL` enumeration is ~3 s, so the 12–17 s is per-shape *accumulation* (~325 ms/shape × dozens of distinct serving shapes). The common in-bucket case is already collapsed by cuDNN override-shape support (#2790 lineage — build once per bucket, execute real M via `override_shapes`); this contract rule is specifically the **out-of-bucket** residual — a serving shape outside every tuned bucket still cold-builds in the engine loop. Two candidate rules, either of which closes the class: the fallback (`tactic=-1`) path must be cheap, **or** runners declare an init-cost class so `auto` skips lazy-heavyweight backends outside a tuning context. This is a runner-contract addition (proposed, not in #3861); the default-candidate coverage guard only races `-1` *during* tuning and does not by itself bound serving-time compilation.

### Accuracy quantification

"v2 selects better tactics than v1" must be a measured claim. The harness: for a grid of (op, real-model N/K, M sweep), measure **every** valid candidate under deployment-faithful conditions at high repetition to obtain an oracle; then simulate tuner selections at production settings under each policy and score:

1. **Regret** — `(t(chosen) − t(oracle_best)) / t(oracle_best)` (headline metric; top-1 alone over-penalizes near-ties);
2. **Top-1 agreement** and rank correlation (noise vs bias diagnosis);
3. **Winner-flip rate** across repeated tuning runs;
4. **Replay fidelity** — does serving execute what the tuner chose (v1 has measured violations; the contract makes this structurally 100%);
5. **Bucket-transfer regret** — regret at off-representative M inside a bucket (decides round-up and bucket density with data).

The oracle sweep is expensive (hours of GPU for a few ops) and runs as a periodic quality gate, not per-PR. One methodological note from building it: candidates must be measured interleaved, not phase-separated, or thermal/clock drift between phases manufactures phantom regret; the sweep records the SM clock per round and clocks are deliberately **not** locked — deployments run floating clocks, and the lab should measure what the field runs.

**Validated on production silicon.** On a full-power B200 (183 GB / 1000 W, all-release stack) across `bmm_fp8` / `mm_fp4` / `cutlass_fused_moe`: on-diagonal regret (policy matches deployment) is ≈ 0, off-diagonal is catastrophic (>1000%), and v1's delay-kernel measurement is mediocre on both — the deployment-match thesis as a measured matrix. Two lessons the clock instrumentation earned: (1) an engineering-sample board threw **43–96% "MoE regret"** that was pure thermal artifact — the 64-expert GEMM collapsed its clock 1965→120 MHz mid-sweep, so `clk_ratio < ~0.9` must invalidate a row; (2) at *balanced* routing, MoE tactic selection is already ≈ 0% regret — which does **not** contradict #3622, because that regression is driven by *skewed* routing / effective per-expert M that a balanced probe cannot exercise. Representative-probe construction (the op-level track) is where that gap closes.

## Distributed story

Persistence and distributed orchestration remain separate responsibilities.

- **Shared filesystem: solved with zero framework code.** The per-entry atomic store makes all-ranks-tune-simultaneously (SGLang's default, and required whenever the dummy forward contains collectives) safe: concurrent publishes are redundant work and the last valid write wins. Per-rank cache files and framework hash directories become unnecessary. Precision on convergence: the *store* converges (and with it every later process/restart); ranks' in-session in-memory winners may still diverge until the finalize step below runs — `autotune_v2_reload()` (implemented in #3861): after a post-tuning barrier, every rank drops its locally-measured winners and re-reads the store's canonical entries, making all homogeneous ranks serve byte-identical tactics.
- **In-session rank consistency**: #3186 shows divergent per-rank tactic choices deadlocking NCCL symmetric-memory allocation *during* tuning. #3187 (all-reduce of measured times before argmin) fixes the in-session window; on top of the store we plan a **finalize step** (tune → barrier → reload winners from the shared store) guaranteeing byte-identical tactics afterwards, including across restarts. The two compose.
- **Heterogeneous ranks (expert parallelism)** — raised by @ima-helikoptaaa below: under EP, ranks legitimately tune *different* shape sets, so "byte-identical tactics" is the wrong invariant; the load-bearing one is **every rank issues the same number of per-tactic collectives per tuning pass**. v1's leader-only file breaks it on the *second* start (leader hits and skips, others miss and profile → the all-reduce count diverges → deadlock). The per-rank atomic store removes the reported cause by construction: each rank publishes its own keys, so a steady-state warm start has every rank hit and issue zero collectives. It does **not** yet enforce the invariant for a *partially* warm store (a rank with a new shape, or one that crashed before publishing). Planned hardening, in the process-group path only: all-reduce(MAX) the per-`choose_one` miss bit so every rank enters the tactic loop together (warm ranks re-profile that profile), plus a debug check that all-reduces the tactic count per profile and fails loudly instead of hanging. Tracked as roadmap item 8.
- **No shared filesystem** (multi-node, node-local roots): a small opaque boundary — `export()` produces bytes, the framework broadcasts them (never parses), `install()` verifies the environment fingerprint and publishes locally. Heterogeneous ranks must tune separately; a fingerprint mismatch refuses loudly. This is a distribution boundary, not a cache-management API; scheduling policy (leader-only vs all-ranks) stays with the framework.

## Roadmap

1. ~~Managed store + `autotune_v2()` opt-in~~ (**done** — #3861: store, env-hash isolation, atomic publish-on-tune, attach semantics, `MeasurementPolicy`, observability, GPU-free test suite covering both frameworks' consumption patterns)
2. ~~**Default-candidate coverage**~~ (**done** — in #3861: inside `autotune_v2` contexts the default path `(runners[0], -1)` always races as a candidate, so a tuned-and-persisted selection cannot lose to not tuning *at the probe inputs*. It is deliberately not claimed as a full regression guard: when the synthetic probe misrepresents serving — routing distribution / EP-sharded M, the #3622/#3537 class — the comparison itself is off; representative probe construction is op-level work on a separate track, and a paired default-vs-winner A/B with margin is a possible strengthening)
3. ~~**Rank-consistency finalize step**~~ (**done** — in #3861: `autotune_v2_reload()`, composing with #3187; see the distributed section)
4. **Opaque export/install** for multi-node distribution
5. **cuDNN plan sidecar** (after #3707): serialize the winning plan next to the entry, skip plan-list enumeration on load
6. **Framework migration** (**in progress**): vLLM — vllm-project/vllm#55671 (draft; capability-probed so it is a no-op until vLLM's pin moves to v0.7.0; every rank tunes into the shared store, `set_autotune_process_group` kept, `barrier → autotune_v2_reload() → barrier` finalize; deletes the leader-read/broadcast/atomic-write/`load_configs`/`save_configs` block for both the generic pass and the SM120 sparse-MLA pass). B200 result: cold tuning windows 55–159 s collapse to 1–2 s on warm restart with entry counts unchanged, all ranks publish and hit, reload runs on every rank (TP2, TP4, incl. the fused-MoE path). SGLang — not started. Deprecation of the v1 path-based API follows the graduation plan below (removal never deletes user files).
7. **Graduation** (`docs/design_docs/autotuner_v2.md` §4, landed with #3861, following @aleozlx's comment below): `autotune_v2` is a **transitional name** — at graduation `autotune()` becomes the v2 implementation, `autotune_v2` a deprecated alias, and `autotune(cache=<path>)` / `save_configs` / `load_configs` thin shims onto the managed store (`cache=` honored as placement only). Gates: (1) vLLM and SGLang migrated *and released*; (2) `validate_tactic` adopted by ≥1 runner — met by the three dense-BF16 GEMM runners, cuDNN still pending; (3) `execution_mode` default resolved (open question 1); (4) harness regret ≤ v1 on ≥2 architectures (B200 done, SM120 none). Removal of the shims/alias waits for the next major.
8. **Collective-count invariant under heterogeneous EP** (see the distributed section): miss-bit all-reduce(MAX) when a tune group is set + debug tactic-count check.

## Non-goals

Migration across incompatible environments; GC/size limits/pruning; a remote cache service; distributed locks or cross-job single-flight; **tuning of communication / multi-GPU collective ops** (v1 does not tune them either — collective tuning needs lockstep candidate enumeration, MAX-reduction, and one group-level decision, plus topology fields in the manifest; deferred until a concrete comm op wants tuning).

## Open questions

1. **Default execution mode**: `"auto"` currently preserves today's behavior. Flipping the default to `"cuda_graph"` (the dominant serving mode) requires the capture-safety contract validated across the op suite first. SGLang input (Brayden): decode is always CUDA-graph and prefill is moving there too, so eager-tuning accuracy is low-value for them — this strengthens the case for `"cuda_graph"` being the eventual default.
2. **Cold-L2 default**: currently off (inherits the op default). Field ask (Brayden) is cold-L2 **on by default**, since serving is cold more often than warm; the blocker is transient tuning memory (rotating buffers — already reduced to a single flush buffer on the CUPTI path). Candidate default-flip once the memory cost is bounded per op.
3. **Policy-level aggregation knob**: rounds + reducer (interleaved min-of-medians), so stable tactic ordering on co-tenant / noisy hosts is a production-tuning property, not just an offline-harness one (see MeasurementPolicy).
4. **Export/install surface**: exact spelling and whether a convenience `sync_across(process_group)` helper (following #3187's explicit-group precedent) is worth adding on top. Note (Brayden): SGLang intends single-rank-tune-then-broadcast for DP/TP — with a shared FS the store already gives this for free (one writer, all readers); export/install covers the no-shared-FS case.
5. **Bucket policy**: round-up vs round-down defaults, informed by bucket-transfer regret data rather than intuition (also raised in #3537's bucket-alignment discussion).
6. **Heuristic-competitive default** (Brayden): for well-behaved ops (e.g. CuteDSL NVFP4 GEMM) the un-tuned heuristic is already within noise, so autotuning's compile/tune cost buys little — the persistent store amortizes that one-time cost, and the accuracy harness's regret-of-`tactic=-1`-vs-oracle is exactly the metric to certify "safe to skip tuning here."

## Acknowledgments

This proposal incorporates feedback and examples from the vLLM team (opaque artifact boundary), Lee Nau (@leejnau) and the SGLang community (CUDA-graph lifecycle and capture safety), Brayden Zhong (@b8zhong) (#3648, #3719; cold-L2 default, single-rank broadcast, heuristic-competitive defaults, CUDA-graph-dominant deployment), @waynehacking8 (SM120 serving-time compilation bound, noisy-host aggregation, execution-mode cache keying), Po-Han Huang (@nvpohanh) and Albert Cheng (@qiching) (graph-profiling direction and capture-safe-runner requirements), Brian Ryu (@bkryu) (cold-L2 mismatch), Alex Yang (@aleozlx) and #3768 contributors (candidate quality, redundant compilation, and the graduation plan), @ima-helikoptaaa (heterogeneous-EP collective-count failure mode), and Yanqin Zhai (legacy-cache invalidation, #3707).

---
🤖 Drafted with [Claude Code](https://claude.com/claude-code); design and measurements by the FlashInfer autotuner v2 effort.









## 评论 (9)

### waynehacking8 · 2026-07-11

Feedback from the consumer-Blackwell corner (RTX PRO 6000 / SM120, single-GPU serving).

The sharpest v1 pain I see in the wild right now is what happens at serving time for shapes the warmup never tuned. Concrete case from this week: vLLM routes per-tensor fp8 linears through bmm_fp8(backend="auto"), and once warmup has cached tuned buckets, a novel (batch, seqlen) at serving either falls back or lands on the cudnn runner, whose graph build is an lru_cache keyed on the exact gemm shape -- a 12-17s host-side build inside the engine loop on sm_12x (vllm-project/vllm#48210, reporter's py-spy plus our source trace). The runner contract feels like the right place to close that whole class: a serving-time miss should be structurally barred from unbounded host-side compilation, either by requiring tactic=-1 paths to be cheap or by having runners declare an init-cost class so auto skips lazy-heavyweight backends outside tuning contexts.

On MeasurementPolicy: deployment-matched measurement is the right call, and one thing worth folding in from benchmarking on a shared SM120 box is aggregation strategy. Sub-0.05ms kernels go bimodal under co-tenancy and single-shot medians flip winners run to run; we settled on interleaved min-of-medians across 5 rounds to get stable orderings (that's what the #3905 SM120 sweep used). A policy-level repeat/aggregation knob would make tune-the-way-you-deploy hold on noisy hosts, not just clean CI boxes.

On cache keying: cute-dsl compile caches already treat dynamic-vs-static batch as separate entries, so a warmup that only exercises one silently misses the other. From the #3861 diff the measurement fields (execution mode, cold-L2) look like they're folded into the entry key, which closes the eager-warmup/graph-serving aliasing -- just flagging that the same needs to hold for any consumer-visible execution-mode dimension a runner exposes.

### b8zhong · 2026-07-13

Whenever possible, I also think 

- For **relatively straightforward cases**, it would be very nice to make sure that the non-autotuned perf can be ~5% of the non-autotuned perf. As in many cases, the compilation and autotune time will be too long. For example for cute-dsl NVFP4 GEMM, disabling the autotune has nearly no perf loss, as the heuristic is well built
- SGLang (ideally) will broadcast a single rank tuning result (in DP and TP cases). The only reason we didn't yet is an oversight from our part
- Ideally, cold L2 should be on by default. If it has high memory consumption or causes some sort of other issue, it should be fixed.
- Eager autotuner performance is not very important to SGLang. In decode, we will always use CUDA graph, and for prefill, we plan to adopt CUDA graph for most cases anyway.

### YangXu1990uiuc · 2026-07-24

Thanks @waynehacking8 — all three land, and I've folded them into the RFC:

1. **Serving-time miss → unbounded host compilation** (your `bmm_fp8`/cuDNN 12–17 s `lru_cache` build inside the engine loop, vllm#48210). You're right that this is a *runner-contract* problem, and that the default-candidate guard doesn't cover it — that guard only races `tactic=-1` *during* tuning; it does nothing to bound a lazy-heavyweight backend on an untuned serving shape. Added as a new contract rule: a serving-time miss must not trigger unbounded host-side compilation, via either a cheap `tactic=-1` path or a runner-declared init-cost class so `auto` skips lazy-heavyweight backends outside a tuning context. (Proposed; not in #3861.)
2. **Noisy-host aggregation.** This matches what building the accuracy harness independently forced — a shared engineering-sample board threw phantom winner-flips, and the fix was interleaved rounds (all candidates back-to-back, rotating offset), which is the same shape as your interleaved min-of-medians in the #3905 SM120 sweep. I've made a **policy-level repeat/aggregation knob** an explicit open question so it applies to production tuning, not just the offline harness — thanks for the #3905 datapoint.
3. **Execution-mode cache keying** (dynamic-vs-static batch as separate CuteDSL compile entries). Agreed — measurement policy is already in the entry key, and I extended contract rule 5 to say the same must hold for any consumer-visible execution dimension a runner exposes, backed by the debug-mode key-completeness check.

If you're able to run the accuracy harness on the RTX PRO 6000 (`benchmarks/bench_autotuner_accuracy.py`, tag `perf-val-latest`), SM120 numbers would be genuinely new — we have no consumer-Blackwell data yet.


### YangXu1990uiuc · 2026-07-24

Thanks @b8zhong — folded all four into the RFC:

- **Heuristic-competitive default** (CuteDSL NVFP4 GEMM within noise un-tuned): agreed this is the target for well-behaved ops. Two things help — the persistent store amortizes the one-time compile/tune cost, and the harness's *regret-of-`tactic=-1`-vs-oracle* is exactly the metric to certify "safe to skip tuning here" per op. Added as an open question.
- **Single-rank-tune-then-broadcast (DP/TP)**: with a shared filesystem the managed store already gives this for free — one writer, all readers, no broadcast code — which is the "delete your per-rank cache logic" path in the migration drafts. `export()`/`install()` covers the no-shared-FS case. Noted against the distributed section.
- **Cold-L2 on by default**: added as an open question. The one blocker is transient tuning memory (rotating buffers), already reduced to a single flush buffer on the CUPTI path — candidate default-flip once the per-op memory cost is bounded.
- **Eager accuracy is low-value (decode + prefill both CUDA-graph)**: very useful signal — this strengthens the case for `execution_mode="cuda_graph"` being the eventual default (open question 1), gated only on validating capture-safety across the op suite.


### YangXu1990uiuc · 2026-07-24

Follow-up on the 12–17 s build, @waynehacking8 — I measured it on your exact hardware (RTX PRO 6000 Blackwell Server Edition, sm120, cuDNN 9.24):

```
[single] override cache_m=256 COLD  =  3061 ms   # one bucket graph, policy=ALL (all engines)
[single] exact     M=200      COLD  =   672 ms   # a single plan build is <1s
[accum ] 20 distinct exact-shape cold builds = 6.50 s  (~325 ms/shape steady state)
```

So the 12–17 s isn't one pathological build — a single plan builds in <1 s, and the full `policy=ALL` enumeration for a shape is ~3 s. The 12–17 s is **per-shape accumulation**: ~325 ms/shape × the ~40–50 distinct `(batch, seqlen)` shapes a serving run hits before the `lru_cache` saturates. 20 shapes already cost 6.5 s here.

The good news is that this is largely **already addressed**, by a line of work that isn't the autotuner: cuDNN **override-shape** support (#2790 and its follow-ups — the cuDNN-GEMM-runner side, mostly @Yanqinz). When `is_override_shape_enabled` (cuDNN 9.x), the fp8 cuDNN runner builds **one graph per tuning bucket** (`cache_m`) and feeds the real M at execute time via `override_shapes` — so N distinct serving shapes within a bucket reuse a single graph instead of building N. That collapses exactly the accumulation you hit. If you were on the exact-shape path (`build_cudnn_gemm_fp8_graph(a.shape…)`), it's because override-shape wasn't active — either an older cuDNN without the capability, or a flashinfer predating the wiring. Which flashinfer + cuDNN versions were you on for vllm#48210? On a recent pair the per-shape accumulation should already be gone.

Where the autotuner-v2 runner contract still adds something is the **out-of-bucket** tail: a serving shape outside every tuned bucket still falls to a cold build, and the proposed rule (cheap fallback / init-cost-aware backend skipping outside tuning contexts) is the structural backstop for that residual — but the common in-bucket case is an override-shape win, not a v2 one. Thanks for the sharp report; it made a clean measurement worth doing.


### aleozlx · 2026-08-04

### On roadmap item 6 — the graduation plan needs to name the end state

Item 6 currently reads:

> **Framework migration**: vLLM and SGLang delete their hashing/broadcast/per-rank-file/knob code; deprecate the v1 path-based API afterwards (removal never deletes user files)

That fixes the *ordering* but leaves the *end state* unnamed, and two things in #3861 make it worth pinning down now rather than later:

- `framework_patches/vllm_autotune_v2.patch` asks downstream to adopt the symbol `autotune_v2` **by name**. If graduation later renames it, vLLM and SGLang touch the same call site twice. If graduation *doesn't* rename it, `_v2` becomes permanent public API surface and the next iteration is structurally forced to be `autotune_v3`.
- #3861 doesn't touch `docs/autotuning.rst` (419 lines documenting `autotune(cache=path)` / `save_configs` / `load_configs` as *the* public API), so on merge the shipped docs describe v1 only and v2 is publicly undocumented. Nothing in-tree ever forces the reckoning.

Proposed expansion of item 6, in three parts:

**a) State that `autotune_v2` is a transitional name.** At graduation, `autotune()` *becomes* the v2 implementation and `autotune_v2` becomes a deprecated alias of it. The version number never survives into the stable API. This costs one sentence today and is precisely what lets the frameworks adopt the name without fear of a second migration.

**b) Name the graduation gates.** "Deprecate afterwards" currently hides at least four:

1. vLLM and SGLang migrated **and released** (item 6 as written);
2. `validate_tactic` adopted by at least one runner (cuDNN, via #3707) — otherwise graduation ships a contract this RFC itself describes as "guardable, not yet guarded";
3. `execution_mode` default resolved (open question 1) — if `"auto"` → `"cuda_graph"` flips *after* graduation, that is a second silent tactic-selection change arriving under the final name;
4. accuracy-harness regret ≤ v1 on ≥2 architectures (production B200 today; SM120 explicitly has no data yet).

**c) Version-policy constraint.** Under the right-shifted scheme in `CLAUDE.md`, *removing* `autotune(cache=<path>)` / `save_configs` / `load_configs` is an incompatible API change → **major** bump. So removal is deferred to 1.0 whether or not that is stated, and the same rule applies to eventually dropping the `autotune_v2` alias. A cheaper end state that isn't blocked on a major: keep the v1 spellings as thin shims forwarding to the managed store, honoring `cache=<path>` as placement only. That collapses the two-autotuner surface without waiting for a removal window.

---

One clarification while I'm here, since it has come up as the reason v2 can't simply replace v1: **"the format may be different" is not load-bearing.** Autotune caches are already per-version disposable — `_collect_metadata()` stamps `flashinfer_version` and `_classify_metadata_mismatches` treats a mismatch as *hard* (`load_configs` ignores the file, `save_configs` refuses to write back), so a v1 file is dead on the first patch bump regardless of what v2 does. The on-disk format difference resolves itself.

What actually argues for a separate entry point is (i) the **call-site signature** — v1's `cache=<file path>` is identity-bearing, v2's `cache_root` is a placement-only directory, so an in-place swap silently redefines an argument downstream code already passes — and (ii) the **lifetime change**, context-scoped tuning in v1 vs process-lifetime attach in v2, which changes behavior *after* the `with` block exits. Both are migration-window problems, which is exactly why the window deserves a documented end.

Happy to send the above as a design doc under `docs/design_docs/` if that's the preferred home for it.

🤖 Drafted with [Claude Code](https://claude.com/claude-code)


### ima-helikoptaaa · 2026-08-31

 @YangXu1990uiuc 

Sharing a failure mode that seems relevant to the distributed-consistency pillar, in case it is useful for v2.

Setup: 4x RTX PRO 6000 (sm120), TP4, an NVFP4 fused MoE with expert parallelism, on vLLM. vLLM does the file-broadcast dance the RFC wants to retire: rank 0 reads the persisted cache, broadcasts it, every rank writes and loads it, then tuning runs with set_autotune_process_group set (#3187).

It deadlocks on the second start, never the first. A cold start tunes in lockstep and the leader saves, but the leader only saves its own configs, so the file holds only rank 0's MoE shapes. On the next start every rank loads that file, and because ranks are heterogeneous under EP (different local experts, so different gemm shapes) rank 0 hits and takes the skip path while the others miss and profile. Rank 0 fires zero per-tactic all-reduces and races ahead into the model output all-reduce, the others block in _profile_single_kernel on an all-reduce that never comes. py-spy shows exactly that split, and deleting the cache to force a cold run fixes it.

Worth separating from #3187: that made ranks which all profile agree on a tactic. Here a rank skips profiling entirely, so what breaks is the count of collective calls, not the choice. The invariant that has to hold is that every rank issues the same number of per-tactic all-reduces per tuning pass, regardless of whether their shapes match.

Where it touches v2: the distributed-consistency section reads as homogeneous ranks converging on byte-identical tactics, but under EP the ranks genuinely differ. A per-rank atomic store plus a reload finalize looks like it would fix the persistence side cleanly, I just could not tell whether it also holds the collective-count invariant when the store is partially warm and the ranks do not share a shape set. If it does, might be worth stating explicitly, since this is the exact edge that bites the broadcast-the-file approach today. If not, the heterogeneous-EP case may need its own handling.

Happy to share the py-spy dumps or a minimal repro.

### YangXu1990uiuc · 2026-09-08

### Status update (2026-09-08): #3861 merged, vLLM migration draft validated on B200

- **#3861 merged** as `3a75b4e3`, ships in v0.7.0. Opt-in, `autotune()` behavior unchanged. The design rationale, runner contract and graduation plan are now in-tree: `docs/design_docs/autotuner_v2.md`; `docs/autotuning.rst` documents `autotune_v2` as experimental.
- **vLLM migration**: vllm-project/vllm#55671 (draft). Capability-probed (`hasattr(flashinfer, "autotune_v2")`), so it is a no-op until vLLM's pin moves off 0.6.18. Every rank tunes into one shared store; `set_autotune_process_group` is kept; `barrier → autotune_v2_reload() → barrier` after tuning. It deletes the leader-read / `broadcast_object` / atomic-write / `load_configs` / `save_configs` block for both the generic pass and the SM120 sparse-MLA pass. SGLang not started.
- **B200 validation** (4× B200, `nvidia/Qwen3-8B-FP8`, `nvidia/Qwen3-8B-FP4`, `nvidia/Qwen3-30B-A3B-FP4`; cold = fresh store, warm = restart against it):

| case | cold startup / tuning window | warm startup / tuning window | entries (unchanged on warm) | `autotune_v2_reload()` per rank |
|---|---|---|---|---|
| FP8 dense TP1 | 415.8 s / 159 s | 120.2 s / 1 s | 88 (cuBLAS 46 · cuDNN 33 · CUTLASS 9) | – |
| FP8 dense TP2 | 410.7 s / 128 s | 165.3 s / 1 s | 88 | 2/2 |
| NVFP4 MoE TP2 | 761.2 s (incl. first JIT) / 130 s | 195.4 s / 2 s | 66 | 2/2 |
| NVFP4 MoE TP4 | 320.5 s / 58 s | 195.3 s / 2 s | 66 | 4/4 |

Every rank publishes and no rank hangs (incl. the fused-MoE path, whose per-tactic collectives are the #3186 hazard); on restart every rank hits the store and the tuning window collapses to 1–2 s; outputs identical cold vs warm; zero errors. Legacy path (pinned 0.6.18) re-run on the same model: unchanged behavior, single-GPU startup at parity — expected, since the measurement policy is unchanged; the payoff is multi-rank persistence and the deleted framework plumbing.

Two vLLM-side facts worth knowing when reading v2 coverage: with vLLM's default NVFP4 kernel (`FlashInferCuteDslNvFp4LinearKernel`) `kernel_warmup` auto-adds `skip_ops={"fp4_gemm"}`, so a dense NVFP4 model tunes and persists nothing under either v1 or v2; and on Hopper vLLM routes FP8 linears to its CUTLASS kernel, so no FlashInfer op is autotuned there at all.

---

@aleozlx — thanks, all four points are adopted. #3861 landed your proposal as `docs/design_docs/autotuner_v2.md` §4: `autotune_v2` is a transitional name; at graduation `autotune()` becomes the v2 implementation, `autotune_v2` a deprecated alias, and the v1 spellings thin shims onto the managed store (`cache=` as placement only), so no framework call site is touched twice and removal is deferred to the next major without blocking graduation. Gate status today: (1) vLLM draft open, SGLang not started; (2) `validate_tactic` is implemented by the three dense-BF16 GEMM runners — cuDNN adoption still pending; (3) `execution_mode` default still `"auto"` (open question 1); (4) B200 data only. Agreed on the "format may be different" point — it was never the argument; the call-site signature and lifetime change are, and both now have a documented end. The root-level `framework_patches/` file was dropped from the PR; the migration lives in the vLLM PR.

@ima-helikoptaaa — thank you, this is the sharpest description of the failure I've seen, and you're right to separate it from #3187: what breaks is the *count* of collectives, not the choice. Where v2 stands against it:

- The reported root cause goes away by construction: every rank publishes its **own** keys to the store, so after a cold start the store holds all ranks' EP-local shapes, and on the second start every rank hits and issues zero per-tactic collectives. The v1 leader-only save is exactly what v2 retires. (The B200 MoE TP2/TP4 cold→warm runs above exercise this mechanism, though without EP.)
- What v2 does **not** yet enforce is the count invariant for a *partially* warm store under heterogeneous ranks — a rank seeing a new shape, or one that crashed before publishing — where one rank misses and profiles while others hit and skip. #3187's docstring pushes "identical starting caches" onto the caller; under EP that assumption is exactly what fails.
- Proposed hardening, process-group path only (added as roadmap item 8): all-reduce(MAX) the per-`choose_one` miss bit so every rank enters the tactic loop together (warm ranks re-profile that one profile, a bounded cost), plus a debug-mode check that all-reduces the tactic count per profile and raises instead of hanging. I've stated the invariant explicitly in the distributed section.

A minimal repro (or the py-spy dumps) would be very welcome — it would become the regression test for item 8.

<!-- note to self: claude::28440023-66ee-410c-a0aa-234997e886d7 — "Autotuner v2 report review" · cwd /home/scratch.yanxu_libs/flashinfer · workspace /home/scratch.yanxu_gpu/vllm_v2_val -->


### jmeadlock · 2026-09-20

A single-GPU datapoint for the "tune the way you deploy" pillar and for #4433's near-tied-argmin mechanism, showing up in `trtllm_fp4_block_scale_moe` rather than cuTile GEMM. FlashInfer `0.6.18.post1`, SM103 (DGX Station GB300), driver 595.91, CUDA 13.0, vLLM `v0.29.1rc1.dev347`. Receipts — four `autotune_configs.json` with sha256, per-window JSON, boot logs, launch scripts — are public: [J-M-Recipes, 2026-09-19 bundle](https://github.com/J-M-Recipes/recipes/tree/main/recipes/dgx-station-gb300/deepseek-v4.1-flash-vllm-uva-dspark/results/2026-09-19-overnight-ksched-nightly-adaptive).

**Setup.** DeepSeek-V4.1-Flash (MXFP4 routed experts, 384 experts / top-6), one GB300, part of the expert weights in Grace memory over UVA, DSpark speculative decode k=5. Same image, same flags, same model on every boot; the only variable is how the autotune cache was populated. Every number is a same-window pair against an unchanged reference container (single-stream prose, T=0, 192 tokens, three runs per boot, all within ±0.5 tok/s).

**1. Two live tunes of the same 191-entry key set chose different tactics, and the difference is 9% at serving time.**
Two fresh processes tuned from empty into the same hash dir: **86/191 entries differ** — 27/42 `trtllm_fp4_block_scale_moe` (`MoERunner`) entries and 58/147 `mxfp8_gemm` entries. Loaded back into fresh processes (hash hit, `Loaded 189 configs`, 0 new), set A serves **172.1 / 172.3 tok/s** and set B serves **187.8 / 187.9 tok/s** (two boots each). Set A also has a −15% / −17% hole at 4 and 12 concurrent streams that set B does not. The M=1 decode MoE key is one of the entries that differs — `MoERunner` tactic `[16, 70]` in A vs `[8, 52]` in B for `((1,0),(0,),(1,6),(1,6),(1,5120),(1,160),(0,),(0,))` — so the kernel every single-stream decode step runs was ranked differently by two tunes on the same silicon. Greedy tokens: identical between a tune and its own loaded cache (16/16 text prompts), 4/18 between the two sets.

| cache state | C1 tok/s | vs 172 reference |
|---|---|---|
| set A loaded (two boots) | 172.1 / 172.3 | 0% |
| set B loaded (two boots) | 187.8 / 187.9 | **+9.2%** |
| set C loaded (different KV dtype → different key set; one boot) | 183.3 | +6.5% |
| live tune, process that produced A | 183.9 | +6.9% |
| live tune, process that produced B | 195.7 | +13.7% |
| live tune, process that produced C | 193.7 | +12.6% |
| **hook-off** config (fewer/different shapes): set D loaded | 90.5 | −0.9% vs its own live tune (91.3) |

**2. The process that ran the tune is faster than a fresh process loading that tune's own output — three of three pairs on the same config, −4 / −6 / −5.4%, token-identical — and a fourth pair on a simpler config shows only −0.9%.**
A: 183.9 live → 172.2 loaded (−6%). B: 195.7 → 187.8 (−4%). C: 193.7 → 183.3 (−5.4%). D (a config with fewer MoE kernel shapes — one routed MoE call per layer instead of two unfinalized calls plus a finalize): 91.3 → 90.5 (−0.9%, 17/18 parity). So the tax scales with which shapes are in the set, not a fixed per-process cost — which is consistent with a per-key lookup miss / fallback on some subset of keys rather than a global effect. Greedy outputs match between a tune and its loaded cache on 16/16 text prompts (17/18 incl. a tool prompt that jitters on the reference as well), so the loaded process appears to execute the same tactics — it is just slower. No explanation from our side; candidates are a lookup miss that falls back to a default tactic for some key that happens to be numerically identical, or state only a live tune leaves behind (JIT / warm paths). This is exactly what the v2 runner contract ("serving executes the tactic the tuner chose, structurally guaranteed") would make either impossible or visible.

**3. The tuning environment did not match deployment.** vLLM tunes eager before CUDA-graph capture and serves inside graphs; the RFC's eager-vs-graph `MeasurementPolicy` axis is the variable I could not control here.

**4. Small practical note:** `--kv-cache-dtype` enters the kernel-shape hash (fp8 vs nvfp4 DS-MLA), so a pinned cache silently stops applying when an engine default changes underneath it (vLLM #56935 flipped the SM100 default). A cache that logs *why* it did not match would have saved a boot.

What this data asks of v2: (a) a tolerance band + deterministic tiebreak in the MoE runner ranking, as #4459 did for cuTile — 9% between two saves is a serving-speed lottery on every cold start; (b) export carrying the *measured latencies* next to the chosen tactic, so a loaded cache can be validated by a quick re-measure instead of trusted; (c) a per-key "tactic executed" log at serving time so observation 2 can be diagnosed.

Happy to run `autotune_v2` from #3861 on this box against the same reference container if someone points a build at me; the harness is one script and the reference is kept.

---
Milo (James Meadlock's agent) drafted from the receipts; James reviewed.

