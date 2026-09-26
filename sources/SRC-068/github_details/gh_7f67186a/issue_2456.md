# [Issue #2456] [RFC] FA4 — head_dim=256 & head_dim=512

source: https://github.com/Dao-AILab/flash-attention/issues/2456
state: open | updated: 2026-09-18T21:13:52Z
labels: 

## 正文

## Overview

This document tracks the roadmap for large head dimension support (`head_dim=256`, `head_dim=512`) in FA4 (the CuTe DSL-based implementation in `flash_attn/cute/`). The work targets Blackwell (SM100/SM110) GPUs using 2CTA instructions.

### Tracking PRs

**Merged (upstream `main`):**
- [#2412](https://github.com/Dao-AILab/flash-attention/pull/2412) — [FA4][CuTe DSL] Add head_dim=256 support (forward + backward, SM100) — commit `27b4eb9`
- [#2487](https://github.com/Dao-AILab/flash-attention/pull/2487) — [Cute,hd256] Post-merge cleanup: dead code, duplicate imports — commit `b21e204`

**Ready (pushed to `Johnsonms/flash-attention`, PRs to be opened):**

| Branch | Tip | Base |
|---|---|---|
| `Johnsonms/exp2-emu-hd256-v2`          | `b97ca5d` | `main` |
| `Johnsonms/paged-kv-hd256-v2`          | `0b2c01b` | `main` |


All four rebased onto post-merge `main` (after #2412 + #2487) on 2026-04-23 by cherry-picking each branch's novel commit. `exp2-emu-v2` is independent; the other three form a stack. Each commit body is a PR-ready description. `HD256_SEQUSED_K_PR.md` and `HD256_PERSISTENT_CLUSTER_PR.md` are also committed in-tree on their respective branches. All four pass the correctness smoke set and a 3-run forward benchmark on B200.

---

## Status Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Done / merged upstream |
| 🚢 | Ready — branch pushed, validated, PR pending |
| 🔨 | Code complete, not yet on a named branch |
| 📋 | Planned |
| 💡 | Exploratory |

---

## Phase 1 — Core head_dim=256 (SM100 Blackwell)

| Feature | Status | Notes |
|---------|--------|-------|
| Forward kernel (2CTA, SM100) | ✅ | #2412 |
| Backward kernel (2CTA, SM100) | ✅ | #2412 |
| Interface integration (`flash_attn_func`) | ✅ | Auto-dispatch on SM100, #2412 |
| Post-merge cleanup (dead code / dup imports) | ✅ | #2487 |
| `pack_gqa` support | 🔨 | Code complete; see `AI/PACK_GQA_NOTES.md` for kernel behavior + 66× MLA-decode measurement |
| FP8 input (FP8 tensor core MMA) | 🔨 | Implementation ready, perf to be improved |

---

## Phase 2 — hd256 Follow-ups (Ready for PR)

The four v2 branches listed above land incrementally on post-merge main.

| Feature | Status | Branch | Notes |
|---------|--------|--------|-------|
| exp2 FMA emulation (softmax SFU→FMA) | 🚢 | `exp2-emu-hd256-v2` | Replaces 3-of-4 SFU `exp2` with packed FMA polynomial. Long-seqlen fwd win (~+2–5% at ≥16k); see perf table below. Independent of the stack. |
| TMA paged KV (page_size = tile_n = 128) | 🚢 | `paged-kv-hd256-v2` | Reuses dense TMA load path via page-table remap. +6 paged tests pass. Within ±0.3% of main on dense path. |
| `seqused_k` + `seqused_k==0` early return | 🚢 | `seqused-k-hd256-v2` | Per-batch KV lengths (needed for MLA-style decode). Stacked on paged-kv-v2. Reproducible +4–7% at long-seqlen non-causal — treated as compiler-driven artifact, not a claimed optimization (SASS investigation pending). |
| Persistent + cluster-aware tile scheduler | 🚢 | `persistent-cluster-hd256-v2` | Gated on `seqlen_k ≤ 2048`. At 8 Q-heads seqlen=1024: +10–25%. At 32 Q-heads: ~0% (launch amortization already saturated). Framed as "no regression at any config, win at decode-style small-batch / few-head". |

Operational notes:
- Stacked PRs should set GitHub base = previous v2 branch (not `main`) so the diff shows only the incremental change.
- After amending any branch in the stack, cascade-rebase downstream branches and force-push (git skips already-applied commits by patch-id).

---

## Phase 3 — Further Optimization & Coverage

| Feature | Status | Notes |
|---------|--------|-------|
| Short-sequence perf vs TRT-LLM | 📋 | Partially addressed by `persistent-cluster-v2` at small head counts; broader benchmark-driven tuning still open |
| `varlen` / packed sequence support (hd256) | 📋 | Not yet branched |
| SM103x specific optimizations | 💡 | Pending SM103 hardware access |

---

## Phase 4 — Extended head_dim Support

| Feature | Status | Notes |
|---------|--------|-------|
| `head_dim=192` (SM100, symmetric) | 📋 | |
| `head_dim=384` (SM100, symmetric) | 📋 | |
| `head_dim=512` (SM100, symmetric) | 📋 | |
| SM103 support | 💡 | Pending hardware access |

> Asymmetric `head_dim_qk` / `head_dim_v` (MLA-style, e.g. `dqk=192 / dv=512`) is out of scope for this RFC — tracked separately.

---

## Performance Snapshot

> head_dim=256, Blackwell B200, bf16, 8 Q-heads, batch auto-sized to ~32k tokens.
> Avg of 3 runs with GPU clocks locked at 1965 MHz.
> MFU based on B200 peak 2.25 PFLOPS BF16.

### Forward (TFLOPS / MFU%)

| | 1k | 2k | 4k | 8k | 16k | 32k | 64k | 96k | 128k |
|--------|------|------|------|------|------|------|------|------|------|
| Non-Causal | 950/42% | 1280/57% | 1477/66% | 1594/71% | 1663/74% | 1709/76% | 1562/69% | 1539/68% | 1481/66% |
| Causal | 584/26% | 897/40% | 1191/53% | 1385/62% | 1505/67% | 1589/71% | 1594/71% | 1449/64% | 1457/65% |

### Backward (TFLOPS / MFU%)

| | 1k | 2k | 4k | 8k | 16k | 32k | 64k | 96k | 128k |
|--------|------|------|------|------|------|------|------|------|------|
| Non-Causal | 333/15% | 523/23% | 735/33% | 932/41% | 1030/46% | 964/43% | 912/41% | 938/42% | 942/42% |
| Causal | 182/8% | 311/14% | 483/21% | 665/30% | 809/36% | 879/39% | 894/40% | 860/38% | 881/39% |

### exp2 Emulation Impact (`exp2-emu-hd256-v2`)

> Comparing base (`b6aa1da`) vs exp2 (`1eba49a`), avg 3 runs, locked clocks @ 1965 MHz.

#### Forward

| | 1k | 2k | 4k | 8k | 16k | 32k | 64k | 96k | 128k |
|--------|------|------|------|------|------|------|------|------|------|
| Non-Causal base | 945 | 1290 | 1482 | 1585 | 1642 | 1671 | 1552 | 1505 | 1443 |
| Non-Causal exp2 | 950 | 1280 | 1477 | 1594 | 1663 | 1709 | 1562 | 1539 | 1481 |
| **Δ** | +0.5% | -0.7% | -0.4% | +0.5% | +1.3% | +2.3% | +0.6% | +2.3% | +2.6% |
| Causal base | 583 | 893 | 1179 | 1363 | 1482 | 1557 | 1607 | 1421 | 1387 |
| Causal exp2 | 584 | 897 | 1191 | 1385 | 1505 | 1589 | 1594 | 1449 | 1457 |
| **Δ** | +0.1% | +0.5% | +1.0% | +1.6% | +1.6% | +2.0% | -0.8% | +1.9% | +5.0% |

#### Backward

| | 1k | 2k | 4k | 8k | 16k | 32k | 64k | 96k | 128k |
|--------|------|------|------|------|------|------|------|------|------|
| Non-Causal base | 332 | 521 | 733 | 928 | 1013 | 929 | 918 | 931 | 936 |
| Non-Causal exp2 | 333 | 523 | 735 | 932 | 1030 | 964 | 912 | 938 | 942 |
| **Δ** | +0.4% | +0.3% | +0.2% | +0.4% | +1.6% | +3.8% | -0.7% | +0.7% | +0.6% |
| Causal base | 182 | 310 | 482 | 663 | 807 | 875 | 879 | 864 | 865 |
| Causal exp2 | 182 | 311 | 483 | 665 | 809 | 879 | 894 | 860 | 881 |
| **Δ** | +0.2% | +0.3% | +0.1% | +0.3% | +0.2% | +0.4% | +1.7% | -0.5% | +1.8% |

---

## References

- `AI/HD256_SEQUSED_K_PR.md` — PR description for `seqused-k-hd256-v2` (committed in-branch).
- `AI/HD256_PERSISTENT_CLUSTER_PR.md` — PR description for `persistent-cluster-hd256-v2` (committed in-branch).
- `AI/PACK_GQA_NOTES.md` — pack_gqa kernel behavior, interface guards, 66× MLA-decode measurement.
- `AI/DEBUG_2CTA.md` — 2CTA kernel hang/deadlock debugging.
- `AI/CLC_TRACE_DEBUG.md` — CLC scheduling visualization.

Cc: @tzadouri @tridao


## 评论 (3)

### Johnsonms · 2026-05-20

https://github.com/Dao-AILab/flash-attention/issues/2576

### Johnsonms · 2026-09-14

https://github.com/Dao-AILab/flash-attention/pull/2810

### sudhakarsingh27 · 2026-09-18

https://github.com/Dao-AILab/flash-attention/pull/2891 proposes enabling `seqused_q/k` for backward for d256 in SM100. Could you take a look @Johnsonms? 
