# [Issue #5151] [Bug] MP server: lookup reports full hit but restored KV context is wrong for long prefixes (breaks between 114 and 128 chunks)

source: https://github.com/LMCache/LMCache/issues/5151
state: closed | updated: 2026-09-20T03:42:32Z
labels: bug

## 正文

## Summary

In multiprocess (MP) mode, a prompt that was previously stored is looked up and
reported as a full hit (lookup_requested == lookup_hit == expected tokens,
per-rank h2d transfers observed), yet the restored KV context produces a
greedy continuation that is **unrelated** to the continuation produced by the
same engine's own cold computation of the same prompt (common prefix:
1 char of 2045). At shorter lengths the identical flow is byte-verbatim.

The failure is same-instance and same-process: engine computes prompt P cold
(stores it), waits until stores fully settle, resets the engine-local prefix
cache, then recomputes P — the second pass reports a full external hit and
finishes fast (TTFT 0.74 s vs 60.3 s cold), but the output diverges from
char ~1. This rules out cross-instance numerics, producer identity, and
client-side effects.

**Bracket** (same-instance flow, verbatim vs broken):

| prompt tokens | chunks | result |
|---|---|---|
| 32 768 | 41 | verbatim (agree 1540/1540) |
| 65 536 | 83 | verbatim (cross-instance as well) |
| 90 112 | 114 | **verbatim** (agree 2522/2522, hit counter exact) |
| 100 352 | 128 | **BROKEN** (agree 1/2045, hit counter reports full) |

Breakpoint is inside **(114, 128] chunks**. We have not bisected further.

## Environment

- LMCache: frozen build `v0.5.6.dev7 (ge5078730)`, MP server
  (`lmcache server --chunk-size 784 --separate-object-groups`) +
  `LMCacheMPConnector` on vLLM engines (KV connector V1).
- vLLM: v1.5.0-based build, TP4.
- Model: Qwen3.8-27B-FP8, hybrid GDN + full attention, 784-token hybrid KV
  chunk (64 layers).
- Realm: L1 40 GiB host memory + `fs_native` L2 (write-through). Failure
  reproduces with the working set far below the L1 watermark — no eviction
  involved.

## Reproduction (same-instance, no confounds)

1. Launch one TP4 engine against a fresh MP server.
2. Send prompt P (100352 frozen token ids, `temperature=0`, `seed` fixed,
   512 output tokens) — cold compute, ~60 s TTFT. Wait until `Stored 784`
   lines stabilize (128 chunks × 4 ranks).
3. `POST /reset_prefix_cache` (engine-local APC only).
4. Re-send the identical P.
5. Observe: `lmcache_mp_lookup_hit_l1_tokens_total` delta == 100352
   (hit_l2 == 0), engine `external_prefix_cache_hits_total` delta == 100351,
   per-rank h2d bytes > 0 — and the output agrees with step 2's output on
   **1 of 2045 characters**.

Control at 32768 (41 chunks): same flow, output **verbatim**, hit counter
exact (32144).

Script: `tier_diag_selfhit.py` (archive available on request); raw evidence:
`results-tiered/diag-acceptance.json` and the phase acceptance with the
cross-instance variant of the same signature
(`results-tiered/phase-b-partial-acceptance.json`, `L100352/l1/rep0`).

## Additional observations

- **h2d volume mismatch**: at the 100352 hit, total h2d staging bytes were
  ~6.8 GiB across 4 ranks where a full 100351-token restore implies ~26 GiB
  at this model's ~262,144 B/token (4-rank combined). The counters say "full
  hit" while the transferred volume says ~quarter — suggesting the lookup
  counted tokens/chunks it did not actually transfer, or assembled the
  context from a subset.
- Off-by-one: external hits 100351 vs expected 100352 at the boundary length.
- Stores were fully settled before the lookup (line-count + object-count
  stability gate), so this is not an in-flight-store race visible from our
  side. We cannot rule out a store-side metadata/counting race that the
  settle window hides.
- Not eviction: the 26 GiB working set fits the 40 GiB L1 with the 0.8
  watermark, and the realm object census after the store shows it resident.
- Impact: silent wrong-context serving — for any prefix ≥ the break point the
  engine returns fast, confidently wrong continuations. This makes tiered
  caching unusable beyond ~83 chunks on this build and is why our phase
  marked all ≥100352 rows NOT_RUN.

## Ask

- Pointers to the MP lookup/reassembly path for multi-chunk prefixes
  (chunk hashing, hit accounting vs transfer accounting) would help us bisect
  further — the (114, 128] bracket already suggests a threshold near 2^7
  chunks or a per-prefix chunk-count limit.
- We can run any requested bisection on this hardware within a day.


## 评论 (10)

### kezboard233 · 2026-09-17

Additional bisection (same-instance flow as in the report):

| prompt tokens | chunks | result |
|---|---|---|
| 90 112 | 114 | verbatim (agree 2522/2522), hit counter exact |
| 94 864 | 121 | **broken, soft**: verbatim false, agree 1463/1962 (74.6%), hit counter off by one (94 863) |
| 100 352 | 128 | broken, hard: agree 1/2045, hit counter off by one |

So the breakpoint is inside **(114, 121] chunks**, and the corruption appears to be *progressive*: at 121 chunks the continuation still agrees for ~75% before diverging, at 128 chunks it diverges from ~char 1. The off-by-one in the external-hit counter appears only in broken runs (89376 exact at 114 chunks vs 94863/100351 at 121/128). Hope the threshold hint (just above 114 chunks ≈ just under 90 KiB of 784-token chunks) narrows the suspect code path.

### kezboard233 · 2026-09-17

Third bisection point: 92 416 tokens (117 chunks) is **verbatim** (agree 2060/2060, external-hit counter exact at 91 728 = 117×784). Updated bracket: **(117, 121] chunks** — a 4-chunk window between 92 416 and 94 864 tokens. The same repro () flips between healthy and broken inside this window, so it should reproduce directly.

### kezboard233 · 2026-09-17

Correlation with in-flight PR #5150 (packed uint32 token ids): that PR reworks exactly the modules on this failure path — `modules/lookup.py`, `token_hasher.py`, `token_codec.py`, `cache_control/key_resolver.py`, `lmcache_driven_transfer.py` — plus a new `test_lookup_outcome_attribution.py`. Two notes:

1. Our frozen build (ge5078730, Sep 14) **predates** #5150, so the fidelity bug exists before it; this is not a #5150 regression.
2. If #5150 reworks chunk hashing/lookup assembly, running its branch against our one-script repro (`tier_diag_selfhit.py`, flips healthy/broken inside the (117, 121]-chunk window in ~10 minutes on one TP4 engine) would be a fast check for both "does it fix the corruption" and "does the packed-buffer change preserve long-prefix fidelity".

Happy to run that validation on our hardware if useful.

### kezboard233 · 2026-09-17

Validation result: we applied #5150's Python-layer changes (lookup.py, token_hasher.py, token_codec.py, key_resolver.py, lmcache_driven_transfer.py, session.py, engine_context.py, the vllm MP connectors/adapter, custom_types) onto our frozen build via patch, and re-ran the same-instance repro at 100 352 tokens (128 chunks):

**still broken** — verbatim false, agree 0/2343, external-hit counter off by one (100 351), TTFT 0.63 s.

So the corruption is not fixed by #5150's current Python changes on our base. Caveats: our build is ge5078730 (Sep 14) with the PR files applied as an overlay (one hunk applied with a 3-line offset), and any hypothetical fix requiring non-Python parts wouldn't be covered. The failure keeps its exact signature, which should still make it findable: full hit counters + per-rank h2d transfers + output unrelated to the cold reference, breakpoint (117, 121] chunks, off-by-one external-hit counter in broken runs only.

### kezboard233 · 2026-09-17

One more data point narrowing the mechanism (from re-examining our logs):

- The MP-side store completes fully and cleanly: 512 `Stored 784` lines (128 chunks × 4 ranks), no eviction lines, allocator never exhausted (40 GiB L1, 26 GiB working set).
- The retrieve claims the full 100 352 tokens in ~12 ms, and the h2d byte volume is *proportionally normal* (~26% of host-side layout bytes, same ratio as healthy 32K/64K runs — our earlier 6.8 GiB 'shortfall' was a miscalibration, the host layout carries ~3.8x the GPU KV volume).
- Yet the restored context is wrong, and **progressively** so: 121 chunks -> continuation agrees 74.6% before diverging; 128 chunks -> diverges from ~char 1. The off-by-one external-hit counter appears only in broken runs.

Working hypothesis: above ~120 chunks the async d2h store pipeline overruns -- later chunks reuse/overwrite pinned staging buffers before earlier async writes complete, so the tail of a long prefix is stored with interleaved/garbage content while bookkeeping still records every chunk as stored. That would explain progressive corruption, intact counters, normal transfer volume, and a store that 'settles' cleanly.

Testable on your side by checksumming resident L1 objects after a 128-chunk store (POST /cache/checksums) versus a freshly recomputed reference, or by serializing the store pipeline above 120 chunks. Our repro flips healthy/broken inside the (117, 121]-chunk window in ~10 min on one TP4 engine if you want a live demo.

### chunxiaozheng · 2026-09-18

@kezboard233 I have a general understanding of the cause of this issue, and I can come and fix it.

### chunxiaozheng · 2026-09-19

@kezboard233 Could you try #5249 in your environment with the original reproducer and check whether it resolves the output mismatch? I haven’t reproduced the divergence locally yet, so your validation would help confirm whether this is the cause of this issue.

### kezboard233 · 2026-09-19

Validation update: [PR #5249 fixes both reported failure points](https://github.com/LMCache/LMCache/pull/5249#issuecomment-5743040089) — the 100352 hard failure and the 94864 soft failure (the patched runs match the same-process cold reference verbatim; base reproduces deterministically, see the matrix there).

Also correcting two errors in this thread's bisection data (my own records, not the upstream build): the healthy 114-chunk run had **90112 input tokens** (89376 was the external-hit count, not the input length), and 94864 is **121** chunks (not 120). The healthy points all carried a partial tail chunk while both broken points were exact chunk multiples, so the "(117, 121] chunks" threshold framing should be read as an exact-multiple-full-hit boundary effect rather than a length threshold — see the #5249 comment for details. We have not tested shorter exact-multiple inputs.

### chunxiaozheng · 2026-09-20

> Validation update: [PR #5249 fixes both reported failure points](https://github.com/LMCache/LMCache/pull/5249#issuecomment-5743040089) — the 100352 hard failure and the 94864 soft failure (the patched runs match the same-process cold reference verbatim; base reproduces deterministically, see the matrix there).
> 
> Also correcting two errors in this thread's bisection data (my own records, not the upstream build): the healthy 114-chunk run had **90112 input tokens** (89376 was the external-hit count, not the input length), and 94864 is **121** chunks (not 120). The healthy points all carried a partial tail chunk while both broken points were exact chunk multiples, so the "(117, 121] chunks" threshold framing should be read as an exact-multiple-full-hit boundary effect rather than a length threshold — see the [#5249](https://github.com/LMCache/LMCache/pull/5249) comment for details. We have not tested shorter exact-multiple inputs.

@kezboard233 Thanks for the detailed feedback and validation! This is very helpful! 👍 

### chunxiaozheng · 2026-09-20

#5249 has fixed current issue.
