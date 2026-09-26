# [Issue #3978] [RFC] Oracle #8 for the quality fuzzers: device-memory canaries (red zones + asset snapshots + scattered sentinels) — the OOB-write class that passes all 7 existing oracles

source: https://github.com/flashinfer-ai/flashinfer/issues/3978
state: open | updated: 2026-09-19T17:50:47Z
labels: needs-triage

## 正文

## Motivation: the 7-oracle kit has a demonstrated blind spot

#3957 survived every oracle the quality fuzzers run today (numeric-vs-reference, NaN, determinism CRC, output-poison, tactic sweep, autotune-ON, device-state probe): a kernel that computes the **right answer** into its own output while **writing out of bounds elsewhere** passes all seven. The corruption only became visible ~45 configs later, when the stray writes happened to land on another backend's long-lived gather-index tensors — by then the failing test id pointed at an innocent victim, and the 2026-06-09 triage had already once written the whole thing off as an unexplained "whole-process abort".

During the #3957 hunt we prototyped a **device-memory canary probe** (384 checksummed sentinel tensors interleaved with freed gaps, verified after every config at native speed) — it bracketed the writer to a single config **on its first run**, where compute-sanitizer was unusable (~65× slowdown on CuteDSL workloads because every freshly-JIT'd cubin gets SASS-instrumented; and under the default caching allocator memcheck is structurally blind to intra-pool OOB anyway, since the whole segment is one valid allocation).

Proposal: promote this from a one-off debug script into **oracle #8 of the shared quality-fuzzer kit** (#3605), as an upgrade of the existing device-state probe.

## Design: three complementary pieces

| Piece | Mechanism | Catches | Character |
|---|---|---|---|
| **Red zones** | Allocate fuzzer-owned output buffers with guard margins filled with a known pattern; verify after each call | Near-boundary overruns: tile overhang, padding write-through, cluster-padding CTAs (the #3957 class fires exactly here — the epilogue wrote at `out[token, N]` ≡ one row past the slice) | **Deterministic**, names the overrun buffer |
| **Asset snapshots** | Checksum known long-lived device tensors (e.g. `_TRTLLM_PERMUTE_CACHE` index tensors) after each config | "Victim-class" corruption of persistent state — the exact #3957 manifestation | **Deterministic** for known assets |
| **Scattered canaries** | N seeded sentinel tensors interleaved with freed gaps across the pool; verify after each config | Wild pool-relative writes with no predictable victim | **Probabilistic** (density = knob); a net, not a proof of absence |

Honest scope note: stray addresses that are truly random 64-bit values hit unmapped VA and fault on their own — canaries add nothing there. Their value is precisely the observed dominant class: **pool-relative** bad addresses (`base + wrong offset`, stale pointers), which land in mapped memory and corrupt silently. #3957 ran 45+ configs without a single fault — that class is real and otherwise invisible.

## Rollout

1. Shared helper `tests/test_helpers/device_canary.py` (sibling of `fuzz_ledger.py`, same one-concept-for-all-fuzzers pattern): `arm(density)`, `verify(tag)`, plus a pytest-plugin wrapper for whole-file bracketing runs.
2. Wire into the unified MoE fuzzer and the scaled-GEMM fuzzer (#3539, now merged) as an **upgrade of check #7** (device-state probe) — not a new checklist item for reviewers.
3. **Default-ON in the fuzzers only** (not the general test suite): cost is ~50 MB + a few ms of device reductions per config; canaries have no legitimate writers, and verification happens after synchronize, outside any CUDA-graph capture (guard with `is_current_stream_capturing`). General-suite adoption can be revisited once SNR is proven.
4. Document the probabilistic nature and the density knob; on a trip, the deterministic follow-up is per-phase verification (the #3957 hunt's per-tactic monkeypatch localized the writer to a single `(runner, tactic)`).

## Prior art

- `compute-sanitizer --padding` (cudaMalloc-granularity red zones) — same concept, ~65× cost on JIT-heavy workloads; this proposal is the always-on cheap version.
- ASan redzones on the host side.
- Validation case: #3957 (first-run bracket) — any implementation must be able to catch it before the fix lands, and stays as the regression example after.

Refs: #3605 (release-quality plan), #3957 (motivating bug + live validation), #3958 (MoE fuzzer enablement; the debug knobs used in the hunt), #3539 (GEMM fuzzer, merged).


## 评论 (2)

### 0z5a · 2026-09-19

Hi @YangXu1990uiuc , I’d like to take a narrow first slice of Oracle #8: the reusable red-zone/canary helper plus fault-injection regression coverage.

### 0z5a · 2026-09-19

The portable red-zone sub-scope of this RFC is implemented in #5344 (base `dc04f50c9aa3eabcdaa5feb0934edb3d85e9529a`).

Design: one owning allocation per guarded buffer — `[prefix guard 0xA5][alignment pad][payload][suffix guard 0x5A][slack]` — with the payload a view of that same storage and `payload.data_ptr() % alignment == 0` by construction, so no dangling pointer is ever handed to a kernel. Guards are compared as bytes, never through float equality, so a NaN payload cannot produce a false positive. Fault injection writes through views of the owner: it can cross the payload's logical boundary but never leaves the owning allocation, and both the guard size and the payload size are checked before the write. Non-contiguous, nonzero-storage-offset, larger-storage-alias and non-strided templates are rejected explicitly. Real integration is an existing `out=` point, `flashinfer.silu_and_mul(x, out=buffer.payload, enable_pdl=False)`, exercised at `hidden=512` and `hidden=3420`.

Measured on an L20 (SM89, torch 2.13/CUDA 13 runtime):

```
CUDA_VISIBLE_DEVICES=<n> python -m pytest -q tests/utils/test_guard_zone.py tests/utils/test_guard_zone_kernel.py
# 73 passed, 2 skipped
CUDA_VISIBLE_DEVICES=<n>,<m> python -m pytest -q tests/utils/test_guard_zone.py
# 69 passed, 0 skipped
```

The two skipped-on-one-device cases are the per-device and same-process cross-device attribution tests; both pass with two devices visible.

Coverage includes: correct payload write leaves guards intact; prefix and suffix injection report the exact region and offset (including a boundary-straddling store); "payload correct but guard corrupted" fails independently of `allclose`, on both the helper and the real kernel; multi-dtype including a NaN payload; odd shapes and alignments; unsupported stride/alias rejection with a positive control; corruption split across a side stream so verification cannot jump ahead; CUDA-graph replay with stable addresses and no reset after corruption; allocation/release cycles without leaks; and the real `silu_and_mul` output buffer.

Honest detection boundary, also stated in the PR: unchanged guards only prove that *those guarded bytes* were not written. Writes far from the payload, writes of the value already present, and write-then-restore are invisible; an underflow smaller than the alignment pad is not observed; and this says nothing about arbitrary cross-device corruption. It complements `compute-sanitizer --mode memcheck`, it does not replace it, and it does not claim to reproduce the original SM100 report.

