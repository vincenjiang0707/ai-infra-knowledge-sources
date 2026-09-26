# [Issue #4532] CAKE kernel candidates for MiniMax-H3 on B300 and RTX 5090

source: https://github.com/flashinfer-ai/flashinfer/issues/4532
state: open | updated: 2026-09-25T05:44:28Z
labels: needs-triage

## 正文

# CAKE kernel candidates for MiniMax-H3 on B300 and RTX 5090

Thank you for inviting customized kernel challenges in the CAKE tracker. We have
a MiniMax-H3 FL2VA runtime based on Sol Engine and SGLang and would like to ask
whether any of the standalone kernels below would be useful CAKE challenges.

These are independent candidates rather than a request for the CAKE team to
implement all of them. We will take care of Sol Engine/SGLang integration,
collectives, quantized checkpoints, calibration, end-to-end validation, and
deployment.

The two targets are:

- NVIDIA B300 / SM103a, with Ulysses SP1/SP2/SP4/SP8;
- NVIDIA RTX 5090 / SM120, quantized execution and SP1 only.

## B300 / SM103a candidates

Common H3 dimensions:

- hidden size: 5,376
- heads: 56
- head dimension: 128
- attention inner dimension: 7,168
- FFN dimension: 14,336
- supported Ulysses degree `P`: 1, 2, 4, or 8
- heads per rank after all-to-all: `56 / P` = 56, 28, 14, or 7
- non-causal packed-varlen attention
- batch size: 1

For B300, we are interested in separate shape specializations for SP1, SP2,
SP4, and SP8.

Nominal `M` values for our main 768p duration buckets are:

| Duration | Global packed rows `T` | SP1 `M` | SP2 `M` | SP4 `M` | SP8 `M` |
|---:|---:|---:|---:|---:|---:|
| 4 s | 33,472 | 33,472 | 16,736 | 8,368 | 4,184 |
| 5 s | 38,592 | 38,592 | 19,296 | 9,648 | 4,824 |
| 6 s | 48,768 | 48,768 | 24,384 | 12,192 | 6,096 |
| 8 s | 58,944 | 58,944 | 29,472 | 14,736 | 7,368 |
| 10 s | 74,240 | 74,240 | 37,120 | 18,560 | 9,280 |
| 15 s | 109,952 | 109,952 | 54,976 | 27,488 | 13,744 |

Prompt length makes `M` slightly dynamic, so kernels need tail handling around
these values. We can provide exact tensor traces and a PyTorch reference for each
operator below.

## 1. Fused BF16 pre-attention kernel — highest priority

Reference operation:

```text
x [M, 5376]
  -> RMSNorm
  -> indexed AdaLN scale/shift
  -> BF16 QKV GEMM [M, 5376] x [5376, 21504]
  -> Q/K RMSNorm over D=128
  -> 3-D RoPE on Q/K
  -> destination-major BF16 QKV
       [P, M, 56/P, 3, 128]
```

The output is only a send buffer; NCCL all-to-all is outside the kernel. The goal
is to avoid writing normalized x, modulated x, ordinary QKV, normalized Q/K, and
RoPE Q/K to HBM. `P` may be implemented as four compile-time specializations
instead of one dynamic kernel if that produces better code.

## 2. Fused low-precision pre-attention kernels

Same operation and output layout as kernel 1, with two independent variants:

```text
A. MXFP8/FP8 QKV GEMM
   -> BF16 Q/K RMSNorm + RoPE
   -> destination-major E4M3 QKV + scales

B. NVFP4 W4A4 QKV GEMM
   -> BF16 Q/K RMSNorm + RoPE
   -> destination-major NVFP4 QKV + block scales
```

An additional NVFP4-GEMM-to-E4M3-output variant is useful if the matching NVFP4
attention kernel is not accurate enough.

We will provide prepacked weights and scale tensors. The kernel does not need to
create or calibrate quantized weights.

### Candidate 2 implementation tracking

- [ ] https://github.com/flashinfer-ai/flashinfer/pull/5060 — Variant A: MXFP8 pre-attention for B200 (`sm_100a`) and B300 (`sm_103a`). Implementation and validation are complete; the PR is open for review.


## 3. Packed-varlen FlashAttention-4 kernels

Input after our existing Ulysses all-to-all:

```text
Q/K/V: [T, 56/P, 128]
cu_seqlens: int32
causal: false
output: BF16 [T, 56/P, 128]
```

Nominal `T` centers are 33,472, 38,592, 48,768, 58,944, 74,240, and
109,952. Requested standalone variants:

```text
A. BF16 FA4
B. E4M3 FP8 FA4 with explicit descales
C. experimental block-scaled NVFP4 FA4
```

For C, we would be interested in a genuine low-precision Tensor Core implementation
rather than NVFP4 storage followed by BF16 matmuls. Softmax remains FP32. It would
be helpful to report the actual QK and PV MMA dtypes separately; a hybrid
NVFP4-QK / FP8-or-BF16-PV candidate would also be useful.

## 4. Direct-layout attention output projection

Reference operation:

```text
inverse-Ulysses receive layout [P, M, 56/P, 128]
  -> read without a standalone unpack/transpose
  -> O GEMM [M, 7168] x [7168, 5376]
  -> indexed gate * output + residual
  -> BF16 [M, 5376]
```

Requested GEMM variants: BF16, MXFP8/FP8, and NVFP4 W4A4. The collective itself
is outside the kernel.

## 5. Fused RMSNorm + AdaLN + FC1 + SwiGLU

Reference operation:

```text
x [M, 5376]
  -> RMSNorm
  -> indexed AdaLN scale/shift
  -> FC1 [M, 5376] x [5376, 28672]
  -> split gate/up
  -> SiLU(gate) * up
  -> BF16 [M, 14336]
```

Requested GEMM variants: BF16, MXFP8/FP8, and NVFP4 W4A4.

## 6. Persistent full MLP candidate

Reference operation:

```text
RMSNorm + indexed AdaLN
  -> FC1 [M, 5376] x [5376, 28672]
  -> SwiGLU
  -> FC2 [M, 14336] x [14336, 5376]
  -> indexed gate * output + residual
  -> BF16 [M, 5376]
```

Requested variants: BF16, MXFP8/FP8, and NVFP4 W4A4. This is only worth keeping
if it beats kernel 5 plus a tuned standalone FC2 GEMM; CAKE does not need to solve
that scheduling decision outside the kernel benchmark.

## 7. Quantize-and-pack helper kernels

These are useful fallbacks when the GEMM epilogue cannot write the communication
layout directly:

```text
BF16 Q/K/V [M, 56, 128]
  -> destination-major E4M3 + scales [P, M, 56/P, 3, 128]

BF16 Q/K/V [M, 56, 128]
  -> destination-major NVFP4 + block scales [P, M, 56/P, 3, 128]
```

Quantization and relayout should happen in one HBM pass.

## RTX 5090 / SM120 quantized SP1 candidates

If CAKE currently supports SM120, we would also appreciate considering a smaller
set of single-GPU kernels for the quantized H3 FL2VA path on RTX 5090. This target
uses SP1 only, so there is no Ulysses layout or collective in these kernels.

For SP1, `M = T`; the nominal M values are 33,472, 38,592, 48,768, 58,944,
74,240, and 109,952 for 4/5/6/8/10/15 seconds. We are interested in two quantized
GEMM formats:

- W8A8 E4M3 FP8;
- NVIDIA-compatible block-scaled NVFP4 W4A4.

BF16 is used as the numerical reference but does not need a separately tuned 5090
kernel in this request.

### 5090-K1. Quantized fused pre-attention

```text
x [M, 5376]
  -> RMSNorm + indexed AdaLN
  -> FP8 or NVFP4 QKV GEMM [M, 5376] x [5376, 21504]
  -> BF16 Q/K RMSNorm + 3-D RoPE
  -> Q/K/V [M, 56, 128]
```

Useful output variants would be BF16, E4M3 plus scales, and NVFP4 plus block
scales, so that we can connect the best one to the corresponding attention path.

### 5090-K2. Quantized packed-varlen FA4

```text
Q/K/V [T, 56, 128]
cu_seqlens: int32
causal: false
output: BF16 [T, 56, 128]
```

The requested candidates are E4M3 FP8 FA4 and experimental block-scaled NVFP4
FA4. Softmax should remain FP32. For the NVFP4 candidate, it would be helpful to
report the QK and PV MMA dtypes separately and include a hybrid NVFP4-QK /
FP8-or-BF16-PV result if it is more accurate or faster.

### 5090-K3. Quantized attention output projection

```text
attention output [M, 7168]
  -> FP8 or NVFP4 O GEMM [M, 7168] x [7168, 5376]
  -> indexed gate * output + residual
  -> BF16 [M, 5376]
```

### 5090-K4. Quantized FC1 + SwiGLU

```text
x [M, 5376]
  -> RMSNorm + indexed AdaLN
  -> FP8 or NVFP4 FC1 [M, 5376] x [5376, 28672]
  -> SwiGLU
  -> BF16 [M, 14336]
```

### 5090-K5. Quantized persistent full MLP candidate

```text
RMSNorm + indexed AdaLN
  -> FP8 or NVFP4 FC1
  -> SwiGLU
  -> FP8 or NVFP4 FC2 [M, 14336] x [14336, 5376]
  -> indexed gate * output + residual
  -> BF16 [M, 5376]
```

As with the B300 candidates, this full MLP would only be useful if it outperforms
the fused FC1 + SwiGLU kernel followed by a tuned standalone FC2 kernel. We will
provide prepacked quantized weights and scales; weight conversion and calibration
are not part of the kernel request.

For RTX 5090, our preferred starting point would be **5090-K4 NVFP4 FC1 +
SwiGLU**, followed by 5090-K1 and the FP8/NVFP4 attention candidates.

## Integration

For any selected candidate, a FlashInfer-compatible kernel implementation and
basic benchmark results would be very helpful. We will handle the Sol
Engine/SGLang integration and end-to-end evaluation.


## 评论 (16)

### yyihuang · 2026-08-15

@Kim2026-dev Thank you for proposing this detailed CAKE kernel request! We have moved it into this sub-issue so we can track it independently.

### Edenzzzz · 2026-08-18

hi @Kim2026-dev I'm the author of the nvfp4 attn on B300. I would not recommend quantization all of QKV to NVFP4 on B300, as group-wise P quantization stalls softmax significantly, unless we want to dequantize V before GEMM like Inkling does. It's better to quantize QK to NVFP4 and V to FP8, then pack it with uint8 `[P, M, H/P, 2D]`. 
I'm also working on an agent for kernels project and will try some of these tickets soon.

<img width="1800" height="750" alt="Image" src="https://github.com/user-attachments/assets/8e2821bc-58a5-411f-91d4-0482703f299b" />



### LiquidMovz · 2026-08-18

@yyihuang @Kim2026-dev — Chase (ADAPT). We write custom Blackwell kernels (B200, B300, RTX PRO 6000). We can take a first kernel off this list.

Reading the issue as current; please correct anything that moved:

- Preferred start you named: **5090-K4 NVFP4 FC1+SwiGLU**, then 5090-K1, then the FP8/NVFP4 attention candidates
- B300 / SM103a list still live (Ulysses SP1/2/4/8)
- @Edenzzzz note: do not quantize all QKV to NVFP4 on B300; QK NVFP4 + V FP8, pack `uint8 [P, M, H/P, 2D]`

To write 5090-K4 we still need from you:

1. Confirm 5090-K4 NVFP4 is still first after that QK/V note
2. CUDA / driver / FlashInfer / SGLang / Sol Engine pins
3. The PyTorch reference + tensor traces you offered, for two M buckets (6s and 10s is enough)
4. Prepacked NVFP4 FC1 weights + the scale layout
5. Current us on 5090 for that op, and the accuracy gate vs BF16
6. When you want a benchable cubin
7. Off-thread contact if you prefer that to the issue
8. Who signs off on the list (and who Kim2026-dev is), if that is not you

We write the kernel. You keep Sol Engine / SGLang integration.

### yyihuang · 2026-09-25

@Kim2026-dev Update for this request: [feat(cake_diffusion): add SM103a BF16 pre-attention](https://github.com/flashinfer-ai/flashinfer/pull/4690) was merged on 2026-09-11 (UTC).

Candidate 1: the fused BF16 MiniMax-H3 pre-attention operator is merged for SM103a.

- Fuses input RMSNorm, indexed AdaLN, QKV projection, per-head Q/K RMSNorm, partial 3-D RoPE, and destination-major packing.
- Writes caller-owned Ulysses send buffers for P=1/2/4/8; the collective stays outside the operator.


### yyihuang · 2026-09-25

@Kim2026-dev Update for this request: [feat(cake_kernel): add MiniMax-H3 MXFP8 pre-attention for SM100a/SM103a](https://github.com/flashinfer-ai/flashinfer/pull/5060) was merged on 2026-09-09 (UTC).

Candidate 2A: MXFP8 MiniMax-H3 pre-attention is merged for SM100a and SM103a.

- The prepared MiniMaxH3Mxfp8PreAttention operation combines generated norm/AdaLN/quantization and norm/RoPE/packing stages with the prepacked MXFP8 QKV GEMM.
- Produces destination-major E4M3 QKV with UE8M0 scales and supports prepared CUDA Graph replay with caller-owned buffers.


### yyihuang · 2026-09-25

@Kim2026-dev Update for this request: [feat(cake_diffusion): add SM100a support to MiniMax-H3 BF16 pre-attention](https://github.com/flashinfer-ai/flashinfer/pull/5137) was merged on 2026-09-11 (UTC).

The BF16 pre-attention operator from #4690 now also supports SM100a (B200).

- Retains SM103a support and the existing precise-math API; the JIT module includes both native targets.
- The operation still fuses the pre-attention chain into the destination-major output layout; CUDA 12.9 remains the minimum.


### yyihuang · 2026-09-25

@Kim2026-dev Update for this request: [feat(cake_minimax_h3): SM120 FP8/NVFP4 fused MiniMax-H3 pre-attention (RTX 5090 / RTX PRO 6000)](https://github.com/flashinfer-ai/flashinfer/pull/5493) was merged on 2026-09-23 (UTC).

Candidate 5090-K1: FP8 and NVFP4 fused pre-attention is merged for SM120a (RTX 5090 / RTX PRO 6000 Blackwell).

- Adds minimax_h3_fp8_pre_attention and minimax_h3_nvfp4_pre_attention.
- Combines RMSNorm/AdaLN/activation quantization with QKV GEMM and a fused Q/K RMSNorm + 3-D RoPE epilogue; supports BF16, E4M3 or NVFP4 Q/K/V outputs.


### yyihuang · 2026-09-25

@Kim2026-dev Update for this request: [feat(cake_backend): add MiniMax-H3 NVFP4 (W4A4) pre-attention for SM100a/SM103a](https://github.com/flashinfer-ai/flashinfer/pull/5496) was merged on 2026-09-24 (UTC).

Candidate 2B: NVFP4 W4A4 MiniMax-H3 pre-attention is merged for SM100a and SM103a.

- Adds the prepared MiniMaxH3Nvfp4PreAttention operation: norm + AdaLN + NVFP4 activation quantization, mm_fp4 QKV GEMM, then Q/K RMSNorm + RoPE + destination-major NVFP4 packing.
- Uses E2M1 values with swizzled E4M3 block scales and caller-owned prepared buffers.

This is the segmented three-launch delivery; later pack-pipeline and GEMM-epilogue-fusion PRs are separate updates.


### yyihuang · 2026-09-25

@Kim2026-dev Update for this request: [feat(cake_minimax_h3): experimental MiniMax-H3 packed-varlen BF16 + NVFP4 attention (SM100/SM103)](https://github.com/flashinfer-ai/flashinfer/pull/5499) was merged on 2026-09-24 (UTC).

Candidates 3A/3C: experimental packed-varlen MiniMax-H3 attention is merged for SM100/SM103.

- Adds minimax_h3_varlen_attention for BF16 and minimax_h3_varlen_nvfp4_attention for quantized attention.
- Supports noncausal THD inputs with cu_seqlens, including empty/tail segments. The NVFP4 path uses NVFP4 QK MMA and defaults to FP8 PV MMA; an FP4 PV mode is also exposed.

This delivers the Blackwell packed-varlen candidates; it does not imply that the separate SM120 attention candidates have landed.


### yyihuang · 2026-09-25

@Kim2026-dev Update for this request: [feat(cake_diffusion): add MiniMax-H3 fused RMSNorm + AdaLN + FC1 + SwiGLU for SM100 and SM103](https://github.com/flashinfer-ai/flashinfer/pull/5491) was merged on 2026-09-23 (UTC).

Candidate 5: fused RMSNorm + indexed AdaLN + FC1 + SwiGLU is merged for SM100/SM103.

- Adds BF16, MXFP8 and NVFP4 variants in flashinfer.diffusion_ops.
- The norm/quantization stage feeds a generated FC1 GEMM with fused SwiGLU, returning BF16 output in two launches per call.

This is the FC1/prologue operator, not the full FC1 + FC2 MLP requested as a separate candidate.


### yyihuang · 2026-09-25

@Kim2026-dev Update for this request: [perf(cake_diffusion): 256-column quantized GEMM tiles for the MiniMax-H3 fused FC1 + SwiGLU on SM100 and SM103](https://github.com/flashinfer-ai/flashinfer/pull/5506) was merged on 2026-09-24 (UTC).

A performance update to the quantized FC1 + SwiGLU operators from #5491 is merged.

- MXFP8 and NVFP4 GEMM cores use wider 256-column CTA-pair output tiles and 128-byte TMA scale-factor rows.
- The regenerated operators preserve the previous output numerics; BF16 and the norm/quantization kernels are unchanged.


### yyihuang · 2026-09-25

@Kim2026-dev Update for this request: [perf(cake_diffusion): 256x448 GEMM tile for the MiniMax-H3 FC1+SwiGLU NVFP4 operator (SM100a/SM103a)](https://github.com/flashinfer-ai/flashinfer/pull/5513) was merged on 2026-09-24 (UTC).

The next NVFP4 FC1 + SwiGLU performance update is merged for SM100a/SM103a.

- Uses a 256x448 CTA-pair GEMM tile, alternating TMEM scale windows and a packed BF16 drain.
- The BF16 and MXFP8 kernels remain unchanged.

Integration note: re-prepare NVFP4 weights with the updated prepare_fc1_weight_nvfp4 helper. The scale layout changed to 128 combined 224-row sub-tiles, so buffers prepared for the previous layout must not be reused.


### yyihuang · 2026-09-25

@Kim2026-dev Update for this request: [feat(cake_backend): MiniMax-H3 one-pass QKV quantize-and-pack helpers (NVFP4 + MXFP8, SM100a/SM103a)](https://github.com/flashinfer-ai/flashinfer/pull/5527) was merged on 2026-09-24 (UTC).

Candidate 7: the one-pass QKV quantize-and-pack helpers are merged for SM100a/SM103a.

- MiniMaxH3QkvQuantizePack reads BF16 Q/K/V and writes destination-major Ulysses send buffers for P=1/2/4/8.
- Supports NVFP4/E4M3 block-16 scales and MXFP8/UE8M0 block-32 scales, combining quantization and relayout in one HBM pass. Outputs match the segmented quantize-and-pack recipes byte for byte.


### yyihuang · 2026-09-25

@Kim2026-dev Update for this request: [feat(cake_minimax_h3): SM120 FP8/NVFP4 fused MiniMax-H3 attention output projection with indexed gate + residual (RTX 5090 / RTX PRO 6000)](https://github.com/flashinfer-ai/flashinfer/pull/5524) was merged on 2026-09-25 (UTC).

Candidate 5090-K3: fused attention output projection is merged for SM120a (RTX 5090 / RTX PRO 6000 Blackwell).

- FP8 and NVFP4 variants combine activation quantization, the 7168-to-5376 output GEMM, indexed gating and residual addition.
- The generated operator writes BF16 output in one kernel launch, avoiding the separate projection/gate/residual chain.

This update covers the SM120 output-projection candidate; the separate SM100/SM103 direct-layout implementation is tracked in its own PR.


### yyihuang · 2026-09-25

@Kim2026-dev [PR #5539](https://github.com/flashinfer-ai/flashinfer/pull/5539) was merged on 2026-09-25 (UTC), delivering the FP8 portion of candidate **5090-K2**.

- Adds `flashinfer.diffusion_ops.minimax_h3_sm120_varlen_attention_fp8` for SM120 / GB202 (RTX 5090 and RTX PRO 6000 Blackwell): noncausal packed-varlen attention over BF16 `[T, 56, 128]` inputs and `int32 cu_seqlens`, with BF16 output.
- Performs statistics, FP8 quantization and attention in four launches. QK and PV use FP8 Tensor Core MMA, with FP32 softmax; supports ragged and empty segments and caches the segment plan/workspace.
- Reports correctness and complete-operator benchmarks on both boards, including the six requested production token counts. For the single-segment production rows, the reported speedups over the fastest tested FlashInfer BF16 route are 1.82–1.87x on RTX PRO 6000 and 1.93–1.97x on RTX 5090, including quantization overhead.

The experimental NVFP4 variant was evaluated but was not shipped because of the measured accuracy tradeoff. This merge therefore covers FP8, not the NVFP4 portion of candidate 5090-K2.


### yyihuang · 2026-09-25

@Kim2026-dev [PR #5521](https://github.com/flashinfer-ai/flashinfer/pull/5521) was merged on 2026-09-25 (UTC), delivering **candidate 5090-K4: FP8 and NVFP4 fused FC1 + SwiGLU** for SM120 / GB202 (RTX 5090 and RTX PRO 6000 Blackwell).

- Fuses RMSNorm, indexed AdaLN, activation quantization, FC1 (5376 to 28672), and SwiGLU into two kernel launches, producing BF16 `[M, 14336]` output.
- Provides FP8 weight preparation and the FP8 operator; the NVFP4 preparation/operator APIs select the SM120-specific implementation. Prepared weight layouts are architecture-specific.
- Reports complete-operator benchmarks across all six requested M values (33472 through 109952). Compared with the fastest tested segmented chain of the same precision, reported speedups are NVFP4 1.52–1.53x and FP8 2.68–2.71x on RTX PRO 6000; NVFP4 1.45–1.49x and FP8 1.57–1.59x on RTX 5090. Reported peak memory is 1.8–5.2 GiB versus 3.9–12.1 GiB for the segmented chain.

Both FP8 and NVFP4 FC1 + SwiGLU variants are included in this merge. The separate persistent full-MLP candidate 5090-K5 and NVFP4 attention candidate 5090-K2 are not part of this PR.

