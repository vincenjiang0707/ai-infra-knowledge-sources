# [Issue #433] [nv_dev][SM120] fp8_fp4_mqa_logits fp8 path returns nondeterministic in-window wrong results for head_dim 32/64 — read-side swizzle mode doesn't match the TMA descriptors

source: https://github.com/deepseek-ai/DeepGEMM/issues/433
state: open | updated: 2026-09-16T08:56:31Z
labels: 

## 正文

The read side of the SM120 fp8 MQA-logits kernel un-swizzles shared memory with a hardcoded 128-byte pattern, while the TMA descriptors and the copy helper swizzle in head_dim-byte atoms (32B/64B/128B for D=32/64/128). For head_dim 32/64 the patterns do not match, every fragment load addresses outside its row, and the kernel returns in-window logits that are silently wrong and run-to-run nondeterministic. D=128 is the only head_dim where the hardcoded value matches, which is why the main DSA path works.

## Failure surface (384-config self-consistency scan, script in the gist)

Every enumerated `test_mqa_logits` config (arch 12), 20 repeat calls compared bitwise:

```
TOTAL=384 FAILS=189
  fmt:        all fp8 (0 mxfp4 failures)
  head_dim:   D=32: 94   D=64: 95   D=128: 0
  compressed: both (CMP=0: 95, CMP=1: 94)
```

The stock test fails at its first fp8 config (fp8/bf16/uncompressed+clean, SQ=128, SK=4096, H=16, D=32, CP=1) with `x_val=0.0, y_val=7.28125` at coord (0,125) — inside the row's `[0, 640)` window. The exact `0.0`s come from misaddressed reads of uninitialized shared memory (`relu(0)*w*sf`), not from missing writes.

## Root cause — three sites that must agree

```cpp
// host TMA descriptors (csrc/jit_kernels/impls/sm120_mqa_logits.hpp):
make_tma_2d_desc(q, head_dim, ..., swizzle_mode=head_dim);        // per-D  ✓
// TMA write side (kernel):
tma::copy<kHeadDim, BLOCK_Q * kNumHeads, kHeadDim>(...);           // per-D  ✓
// kernel read side (sm120_fp8_mqa_logits.cuh):
static constexpr uint32_t kSwizzleMode = 128;                      // hardcoded ✗
```

The fp8 row is head_dim bytes, so writes land swizzled in head_dim-byte atoms. `SwizzleContext<kSwizzleMode>` and the fragment loaders then un-swizzle with the 128B pattern; for D=32/64 the XOR bits touch addresses the write pattern never permuted, so reads cross row boundaries of the tile or fall into pipeline stages that have not been filled yet — hence nondeterministic content.

## Fix (one line) and validation

```cpp
- static constexpr uint32_t kSwizzleMode = 128;
+ static constexpr uint32_t kSwizzleMode = kHeadDim;
```

The fix direction is the reader side: the smem tile geometry is "one row = head_dim bytes", so the swizzle atom must equal the row width (a 128B atom would span four D=32 rows and change the TMA box geometry). All readers are parameterized on this constant, so one change covers them.

Validated on RTX 5090 D (CUDA 13.0, torch 2.11.0+cu130, nv_dev @ 2642b32):
- self-consistency scan: **189 → 0** failures
- full `test_mqa_logits` (20x bitwise self-consistency + accuracy vs reference + bench): **PASSED**, all 384 configs, fp8 up to 411 TFLOPS

## Why related kernels are unaffected

- `sm120_fp4_mqa_logits.cuh`: D=128 only (`DG_STATIC_ASSERT`), row = 64 bytes, constant 64 — matches.
- `sm120_fp8_paged_mqa_logits.cuh` / fp4 paged: dispatch asserts `head_dim == 128`; their constant 128 matches the only supported head_dim.
- Dense fp8 is the only instantiation where multiple row widths are allowed by the dispatch (`head_dim == 32 or 64 or 128`) and the constant diverges from them.

## Relation to #392

On our hardware fp8 D=128 passes self-consistency across all configs (20 reps, both compressed and uncompressed), so the out-of-window nondeterminism reported in #392 does not reproduce here — possibly driver/timing dependent (the kernel, clean kernel, launch path and test file are byte-identical between f8e8fb5 and 2642b32). The mxfp4 H=64 D=128 accuracy failure from #392 also no longer reproduces. The stock test at f8e8fb5 already enumerated fp8 D=32/64, so the SM120 test failures reported there very likely included the defect fixed here.

## Scope / timing

`main` is unaffected (no SM120 support yet). When nv_dev next syncs to main, this would otherwise ship with the first official SM120 release: any fp8 DSA/MQA geometry with head_dim 32/64 on 5090-class hardware would silently corrupt logits.

Scan script and raw logs: https://gist.github.com/aganhui/f783450b212217284c062c3b46300649

PR incoming (base nv_dev). Happy to run further validation on this 5090 D if useful.


## 评论 (4)

### aganhui · 2026-09-10

Cross-arch note: the sibling kernels derive this value instead of hardcoding it — SM90 uses `to_swizzle_cute_type<kHeadDim>()` (sm90_fp8_mqa_logits.cuh:259,262), SM100 uses `kQKSwizzleMode = kHeadDim / kPackFactor` (sm100_mqa_logits.cuh:308). SM120 is the only instantiation with a hardcoded literal, and the only one whose dispatch allows multiple row widths (D=32/64/128). The proposed fix brings it in line with the other two arches.

### aganhui · 2026-09-10

Correction to the original report (thanks to ds-review-bot's check on #434): the sentence above — "sm120_fp8_paged_mqa_logits.cuh / fp4 paged: dispatch asserts head_dim == 128" — is wrong about the **fp8** paged variant. The `DG_HOST_ASSERT(head_dim == 128)` belongs to `sm120_fp4_paged_mqa_logits` (csrc/jit_kernels/impls/sm120_mqa_logits.hpp:586) only; `sm120_fp8_paged_mqa_logits` has no head_dim restriction and passes swizzle_mode = head_dim in its descriptors, so the fp8 paged kernel has the same swizzle mismatch for D=32/64.

Empirically on the 5090 D (targeted repro, small configs — the full paged suite does not fit in 32 GB): fp8 paged accuracy diff vs reference is **0.83 (D=32) / 0.72 (D=64)**, while self-consistency *passes* — the paged pipeline's misreads land on deterministically-stale shared memory, so the corruption is bit-stable across runs and only accuracy comparison exposes it. The fix in #434 now covers both fp8 variants (dense + paged); post-fix diffs are ~1e-3 across D=32/64/128.

The fp4 dense/paged kernels are indeed head_dim-128-only, so that part of the original report stands.

### aganhui · 2026-09-11

Update: the same bug and an essentially identical fix were already posted as **#379** by leavelet (7/15, covering dense + paged, bot-approved) — we missed that open PR before filing this report.

This issue remains useful as the documentation/evidence layer for that fix: the 189-config failure surface, the two distinct manifestations (nondeterministic in-window garbage in the dense kernel vs **deterministically-wrong values in the paged kernel**, where self-consistency passes and only accuracy-vs-reference exposes it), the cross-arch derivation analysis (SM90/SM100 derive this value; SM120 was the only generation with a hardcoded literal), and the likely explanation for the SM120 self-consistency/accuracy symptoms reported in #392 back in July.

Our validation data on a 5090 D (384-config scan 189→0 with this fix, paged accuracy 0.83/0.72 → ~1e-3) has been posted to #379 to help it get merged.

### lucifer1004 · 2026-09-16

Confirmed root cause (read-side hardcoded 128B unswizzle vs per-head_dim TMA swizzle atoms).

In #447 the SM120 fp8 MQA-logits kernel was rewritten: the read side is parameterized by the same value the host puts in the descriptors — `kSwizzleMode = kHeadDim`, with all fragment loads going through `SwizzleContext<kSwizzleMode>`; no hardcoded 128 remains. The host accepts fp8 head_dim 32/64/128 (`csrc/jit_kernels/impls/sm120_mqa_logits.hpp`).

Coverage: `test_sm120_dense_mqa_contract` parametrizes fp8 × head_dim {32, 64, 128} × heads {16, 32, 64}, including long-KV and CUDA-graph replay; paged fp8 at head_dim 32/64 is covered by `test_sm120_paged_mqa_metadata_graph`. All pass on sm_120a.

