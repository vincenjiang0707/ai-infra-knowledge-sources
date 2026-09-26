# [Issue #1105] [Performance] DFLASH windowed-attention backward — flash-attn-style Triton operator

source: https://github.com/vllm-project/speculators/issues/1105
state: closed | updated: 2026-09-10T12:18:41Z
labels: 

## 正文

### Proposal
This follows the "General Training Performance Improvements" initiative in the
Q3 Roadmap (#781, status: *Not Yet Started*) — this operator is a benchmarked
bottleneck fix for it.

A self-contained Triton operator for windowed-attention backward (flash-attention
style: two-pass online softmax + `atomic_add` for dK/dV). It respects the
anchor-block window and never materializes dense S/P. The integration diff is
available on request and will follow as a separate PR once the operator lands.

### Problem
The DFLASH draft attends each query only to an anchored block-windowed set of KV
blocks, but its backward currently goes through dense `flex_attention`,
materializing the full `[q_len, kv_len]` attention matrix. At production sizes the
dense backward needs ~69GB (OOM on 8×A800) and ignores the window structure.

### Benchmark (independent re-verification, 8×A800 SM80, torch 2.13.0+cu130)
| metric | dense flex backward | this operator |
|---|---|---|
| time | 419.2 ms | 184.7 ms (**2.3×**) |
| peak memory | ~69GB (OOM at prod size) | 5.6 GB (no dense materialization) |
| correctness | — | corr dq/dk/dv = 1.0000 (single- & cross-doc) |

(Additional BLOCK tuning: 997.8 → 137.4 ms, 7.26×.)
(Measured at a medium size that fits the dense baseline; at production size the
dense backward OOMs — that is the motivation.)

### Scope
- new file `windowed_attn_bwd.py` (~341 lines, imports only torch + triton)
- `DFlexAttnBwd` autograd wrapper; `non_causal` default aligned to production `False`
- integration intentionally NOT in this PR (follow-up): DFLASH decoder wiring,
  GQA-aware / amortized / 3-kernel-split variants, symmetric fused forward kernel

### Validation
- fwd+grad parity vs eager `flex_attention` (causal + non-causal, non-power-of-2 tail)
- A800 SM80

Is this the right direction for the DFLASH backward? Happy to split further or adjust scope.

## 评论 (1)

### Leslie360 · 2026-09-10

Withdrawing this proposal. Before writing any PR we benchmarked the compiled `flex_attention` backward at identical shapes: on the repo's supported torch range (verified 2.12.1) it beats the proposed operator by an order of magnitude — production shapes run in ~9 ms / ~8 GB versus the ~96 GB dense-materialization OOM of the eager reference. No custom kernel is needed. Thanks for the initiative slot (#781) — we'll bring a training-performance item that's actually missing.
