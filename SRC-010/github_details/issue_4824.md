# [Issue #4824] [Feature] DeepSeek-V4 MoE is Blackwell-only via DeepGEMM — is a non-Blackwell path wanted?

source: https://github.com/InternLM/lmdeploy/issues/4824
state: open | updated: 2026-09-01T04:27:52Z
labels: 

## 正文

### Motivation

DeepSeek-V4 currently reaches only one MoE path in the PyTorch engine: `DeepseekV4MoE` constructs `FusedMoEV4FP4` unconditionally (`lmdeploy/pytorch/models/deepseek_v4.py:633`), which resolves to `TritonFusedMoEV4FP4Builder` and ultimately to DeepGEMM's `m_grouped_fp8_fp4_gemm_nt_contiguous`. That kernel accepts packed FP4 expert weights only on `arch_major == 10`, as the implementation's own docstring notes — so the model is effectively Blackwell-only, and even SM90 is excluded.

That is a reasonable place to start, but it leaves out the hardware most self-hosted deployments in this ecosystem actually have. It also sits oddly next to LMDeploy's own position on old GPUs: TurboMind's MXFP4 support is advertised as working "on NVIDIA GPUs starting from V100". The model file itself carries no architecture gate; the restriction lives entirely in which MoE implementation gets selected.

I would like to know whether a non-Blackwell MoE path for DeepSeek-V4 is something the project wants. If it is, I am in a position to help with the part that is usually hardest to arrange — real hardware and measurements.

### What I have

I have DeepSeek-V4-Flash-0731 serving on 8x A800 (SM80) through a different engine, using the **stock checkpoint with no conversion step** — the published e2m1 weights and e8m0 block scales are read as-is, decoded by a Marlin W4A16 kernel instead of DeepGEMM:

- **GSM8K 96.44%** (1272/1319, greedy, thinking off). The DeepSeek official API scores 96.29% on the same questions and grader, at the same 129 tokens/question — so the serving path costs nothing measurable in quality.
- 105.7 tok/s single-stream with speculative decoding; 330 tok/s aggregate at 16 concurrent
- needle-in-a-haystack clean across 4K / 32K / 128K x three needle depths
- prefill 19 s at 64K, 64 s at 218K; a repeat of the same 218K prompt returns in 0.87 s on a prefix-cache hit
- 1M context ceiling, fp8 KV cache

The point I'd draw from that: a Marlin-family W4A16 GEMM reproduces the published model on Ampere with no accuracy left on the table. There is nothing exotic needed for these weights.

The machine, in case it is useful to know what a contribution here would be validated on — 8x **A800-SXM4-80GB**, NVLink fully connected (NV8 between every pair), driver 590.44.01, 640 GB of GPU memory in one node. It is a dedicated box, not a shared slice, so I can hold a model resident and run whatever matrix is useful rather than working around a queue. If the answer to the question below is yes, testing on real SM80 silicon is the part I can cover — that is usually the awkward half of supporting hardware the maintainers do not have.

The relevant finding for LMDeploy: **DeepSeek's published FP4 experts do not need Blackwell.** A Marlin-family W4A16 GEMM decodes e2m1 with plain bit manipulation and runs on SM80 upward. The Blackwell requirement comes from DeepGEMM specifically, not from the weight format.

### The gap, as far as I can see

`lmdeploy/pytorch/kernels/cuda/` has `fused_moe`, `blocked_fp8`, `w8a8` and `v4_fp4`, but no Marlin-family kernel, so there is currently nothing to fall back to for packed 4-bit experts. The two options I can see:

1. **Dequantise the FP4 experts to BF16 at load and use the generic fused MoE.** Small change, but the expert weights grow roughly 4x — for V4-Flash that does not fit on 8x80GB, so it is not a real option at this scale.
2. **Bring in a Marlin-style W4A16 grouped GEMM** and select it when the FP4 path is unavailable. This is the one that actually works, and it is a substantial piece of kernel work.

### What I am asking

Is (2) something LMDeploy wants? I am not asking anyone to take on Ampere maintenance — I am asking whether a contribution in that direction would be welcome, before I spend days on a kernel port that might not have a home. If it is welcome I would rather do it in the open with the maintainers' guidance on where the pieces belong, and I can carry the A800 testing.

If the answer is that DeepSeek-V4 is intentionally Blackwell-only for now, that is a legitimate scope decision and I would rather hear it plainly than guess from the code.

### Related resources

- `lmdeploy/pytorch/models/deepseek_v4.py:633` — unconditional `FusedMoEV4FP4`
- `lmdeploy/pytorch/backends/cuda/moe/v4_fp4.py:106` — "DeepGEMM's grouped FP8xFP4 kernels accept packed FP4 expert weights only on arch_major == 10"
- #4658 — TurboMind support for the same model (different backend, related question)


## 评论 (9)

### Hakureirm · 2026-08-04

Following up with something I got wrong in the original post.

I said a Marlin port would be a few days of work. Having now read how the reference implementation is actually built, that estimate was too optimistic and I'd rather correct it before anyone plans around it. SGLang's MXFP4 Marlin path is a JIT-compiled CUDA extension (`load_jit` over C++ sources), not a Triton kernel — so bringing it over is not lifting one kernel file, it means carrying a CUDA source tree and its build path into a codebase whose GPU kernels are predominantly Triton. That is weeks, not days, and it is a maintenance surface someone has to own afterwards.

That changes what I think is worth proposing. Rather than porting Marlin wholesale, the narrower question is whether a Triton W4A16 grouped GEMM for e2m1 + e8m0 block scales would be welcome — the same decode logic, written natively in the style of the kernels already in `lmdeploy/pytorch/kernels/cuda/`. That is a self-contained piece of work, it fits the existing build, and `fused_moe.py` already has the grouped-expert plumbing around it.

I can prototype that and report numbers on 8x A800 either way. Still asking the same question first: is a non-Blackwell MoE path for DeepSeek-V4 something the project wants? Nothing here is urgent for me — I have the model serving on this hardware through another engine, so I'm asking about direction, not unblocking myself.

### Hakureirm · 2026-08-04

Confirmed the blocker on real hardware rather than by reading the code. On 8x A800 (SM 8.0) with `lmdeploy 0.15.0` and `deep_gemm 0.1.4.post1`:

```
>>> deep_gemm.m_grouped_fp8_fp4_gemm_nt_contiguous(aq, (w, scales), out, idx)
RuntimeError: Assertion error (deepgemm/csrc/.../utils/layout.hpp:57):
    ab.scalar_type() == kPackedFP4 and arch_major == 10
```

So the restriction is a hard assertion inside DeepGEMM, not a dispatch preference — the kernel refuses on anything below Blackwell regardless of how the weights are presented. I tried passing the e8m0 scales as a `uint8` view and as `float32`; same assertion both ways. (Before that it fails even earlier, in DLPack conversion: `Unsupported DLDataType for torch conversion: float8_e8m0fnu`.)

`TritonFusedMoEV4FP4Builder` resolves fine on SM80 and `lmdeploy` imports cleanly — the model gets all the way to the GEMM before anything complains. That is the whole gap.

Which puts the question in a narrower place than my first post did: everything except the expert GEMM already works on Ampere. What is missing is one W4A16 grouped GEMM over e2m1 weights with e8m0 block scales. Still asking whether that is something the project wants before I build it.

### grimoire · 2026-08-20

https://github.com/InternLM/lmdeploy/blob/main/lmdeploy/pytorch/kernels/cuda/v4_fp4_fused_moe.py
https://github.com/InternLM/lmdeploy/blob/main/lmdeploy/pytorch/kernels/cuda/v4_fp4_grouped_gemm.py

we have implment custom triton kernel to support nvfp4 moe on non-blackwell device. The kernel has been tested on Hopper device, and I guess it should be able to work on ampere, but the performance has not be tuned.

### Hakureirm · 2026-08-20

Thank you — that answers the question, and better than I hoped: the work is already
done rather than merely welcome.

I have the SM80 hardware, so I ran it rather than guessing. On A800 (sm80, Triton
3.7.1) the kernel does not compile at all — it is not a tuning gap:

```
ValueError: type fp8e4nv not supported in this architecture.
            The supported fp8 dtypes are ('fp8e4b15', 'fp8e5')
```

This covers both files you linked: `v4_fp4_grouped_gemm.py` routes both its
contiguous and masked entry points through `fused_moe_v4_fp4_kernel_launcher`, so
there is one Triton kernel behind them.

The cause is the decode path, not anything about the weights. After the `prmt.b32`
LUT the nibbles become fp8 bytes via `.to(tl.float8e4nv, bitcast=True)`
(`v4_fp4_fused_moe.py:147-154`), and both `tl.dot` operands are fp8e4nv (`:175`).
Triton's NVIDIA backend gates that type by architecture:

```python
# triton 3.7.1, triton/backends/nvidia/compiler.py:191-195
supported_fp8_dtypes = set(CUDAOptions.supported_fp8_dtypes)   # ('fp8e5', 'fp8e4b15')
if capability >= 89:
    supported_fp8_dtypes.add("fp8e4nv")
```

sm80 is capability 80, so it never gets fp8e4nv.

Two details that decide how big the Ampere fix actually is, both measured rather than
reasoned:

**1. The obvious workaround does not apply.** What is rejected is the type itself,
not merely its use as a dot operand — a plain bitcast that never reaches a `tl.dot`
fails identically. So "upcast to fp16 before the dot" is not available as written.

**2. The activation pointer cannot even be loaded.** `tl.load` on a
`torch.float8_e4m3fn` pointer fails with the same error; the same bytes viewed as
`uint8` load fine. So the activations have to be `.view(torch.uint8)`'d at the call
site as well, not just handled differently inside the kernel.

| probe on A800 (sm80) | result |
|---|---|
| `tl.load` an fp8e4nv pointer, no dot | fails |
| same bytes as a `uint8` pointer | passes |
| `fp8e4nv` bitcast + convert, no dot | fails |
| `tl.dot(fp8e4nv, fp8e4nv)` | fails |
| `tl.dot(fp8e5, fp8e5)` | passes, max deviation 0 |

So an Ampere path has to avoid the type entirely and land the dot on fp16, which
Ampere does have tensor cores for. Worth flagging that this is not a one-line change:
the decode is byte-granular by design — `LUT_LO`/`LUT_HI` (`:106-107`) are two int32
words holding the eight e2m1 magnitudes as e4m3 *bytes*, which is exactly what makes
the single `prmt.b32` work. Producing fp16 needs either two `prmt` passes to assemble
the halves, or an arithmetic decode in place of the table.

One thing that argues there is nothing to lose by doing that: `fp8e4b15`, the other
type sm80 accepts, is not a real fp8 path anyway. Triton upcasts it to fp16 before
the dot regardless of architecture, because there is no fp8e4b15 type in MLIR
(`triton/language/semantic.py:1504-1511`) — and on capability >= 90 it additionally
warns that it is deprecated and slow. So on Ampere there is no fp8 tensor-core path
being given up here; fp16 is the honest target rather than a fallback.

As a control, the same script with the same synthetic inputs compiles and runs on
capability (12,0): 2048/2048 non-zero outputs. That is what makes the sm80 result an
architecture conclusion rather than a malformed harness on my side.

The probe leaves your file byte-identical — it only stubs the four lmdeploy-internal
imports and feeds synthetic inputs shaped by your own launcher asserts. Happy to post
it here if useful.

If you are open to it, I would like to build the fp16 variant and send it to you as a
PR. What I have in mind keeps your kernel rather than replacing it:

- keep the structure, the int32 load and the `prmt` decode; change only where the
  decoded values land — fp16 instead of fp8 bytes, so the dot runs on tensor cores
  Ampere actually has;
- take the activations in as `uint8` and decode e4m3 with integer ops, since the fp8
  pointer cannot cross the kernel boundary on sm80 at all;
- gate it on capability so that nothing changes at >= 89 — your current path stays
  byte-for-byte as it is, and the fp16 decode is selected only below that;
- validate on the 8x A800-SXM4-80GB box, which is dedicated rather than a shared
  slice, so I can hold a model resident and run whatever matrix is useful, including
  the accuracy comparison against the Blackwell path rather than just "it compiles".

Would you take that as a PR? It is your kernel and your maintenance burden afterwards,
so I would rather ask than show up with one unannounced.

One caveat on what I did **not** measure: no performance numbers. Six of the eight
GPUs are busy with a training run, and timings taken in that state would not be worth
reporting. Compilation and correctness are unaffected by that, which is why those are
the only claims above.


### grimoire · 2026-08-20

We are interested in non-Blackwell support, but a MoE-only SM80 fallback is not sufficient for the current LMDeploy V4 runtime: the attention backend and FP8 cache packing also require SM90/SM100 functionality. 

### Hakureirm · 2026-08-21

First, a correction to my opening post that I should not leave standing. I wrote
GSM8K 96.44% and said the official API scores 96.29% on the same questions. Those
two numbers are from different runs. Paired as they were actually measured it is
96.44% against the API's 96.7% — so slightly *below* rather than slightly above.
Three questions, inside the concurrency noise, and it does not change the point I
was making about serving quality; but I stated the comparison the flattering way
round, and that is worth fixing before I ask you for anything.

On the substance: you are right, and a MoE-only fallback would not have made V4 run
on SM80. I went and measured the rest of the runtime rather than take it or dispute
it. The shape that came back is narrower than "also requires SM90/SM100" — most of
it is **one Triton type gate**, hit in more than one place.

Same probes on four architectures, your kernels byte-identical (only the
lmdeploy-internal imports stubbed), synthetic inputs shaped by their own asserts:

| probe | A800 sm80 | H100 sm90 | B200 sm100 | RTX 5090 sm120 |
|---|---|---|---|---|
| `fp8e4nv` bitcast, no dot | fails | pass | pass | pass |
| `tl.dot(fp8e4nv, fp8e4nv)` | fails | pass | pass | pass |
| `tl.dot(fp8e5, fp8e5)` | pass | pass | pass | pass |
| `v4_fp4_fused_moe` — MoE GEMM | fails | pass | pass | pass |
| `pack_window_tokens_fp8` — FP8 cache packing | fails | pass | pass | pass |

sm80 is the only architecture that fails anything, and both kernels fail on the same
thing: `fp8e4nv` enters Triton's supported set only at capability >= 89
(`triton/backends/nvidia/compiler.py`, same line in 3.6.0 and 3.7.1, both inside
your `triton<=3.7.1,>=3.0.0` pin). Incidentally this also confirms your "tested on
Hopper" from the outside — the MoE kernel runs clean on H100 and B200.

So your FP8 cache packing is the same gate rather than a separate problem:
`v4_pack_window.py:81` is `(tile_vals / scale_inv).to(tl.float8e4nv)`. It is not the
same *fix*, though, and I want to be honest about that rather than fold it into one
bullet: the MoE kernel only needs its decoded values to land somewhere else, while
pack_window genuinely has to produce e4m3 bytes, so that one wants the byte pattern
synthesised with integer ops. Two kernels, one blocker, two different amounts of
work.

I also probed `ds_index.fp8_index`, on the theory that the indexer's non-DeepGEMM
branch might be a way in. **It is not, and I would rather report that than leave you
to find it:** `configurations/deepseek_v4.py` allocates `v4_index_kv_r4` as packed
`torch.uint8` unconditionally, so `v4_indexer.py`'s `dtype == torch.uint8` test is
always true for V4 and the DeepGEMM path is the only one it takes. The `fp8_index`
branch is there for the legacy split cache layout, not for V4. Mentioning it only so
you know it was checked and is not a route I am proposing.

That leaves the indexer's DeepGEMM scoring and FlashMLA as the two real gaps, rather
than four separate ones. On those, one data point rather than an argument: the 8x
A800 deployment behind my first post does not take the FlashMLA sparse-decode path
at all — that gate was changed to select by which architectures actually carry the
kernel — and the image it serves from does not have `flash_mla` installed. So SM80
substitutes exist; they are in a different engine, which is a much smaller claim
than "the attention backend requires SM90", but also a much smaller claim than "so
port them", and I am not pretending otherwise.

What I would like to do, if you will have it, is the `fp8e4nv` work: the MoE GEMM
and the cache packing, decoding to fp16/bf16 rather than routing through a type
Ampere's Triton will not instantiate, gated on capability so nothing changes at
>= 89. I can show that rather than assert it — the H100 and B200 columns above are
already the before-picture, and validation would be on the A800 box against the
Blackwell path rather than "it compiles".

The indexer scoring and FlashMLA I would not start on without hearing from you.
Those are architecture calls about what you want to carry afterwards, and they are
yours to make, not mine to present you with.

The probes are one file that copies your kernels in unmodified; happy to post it.


### Hakureirm · 2026-08-21

Follow-up: I built the two `fp8e4nv` kernels rather than leave the offer abstract, so
you can judge the size of it instead of my description of it.

| | `v4_fp4_fused_moe` | `pack_window_tokens_fp8` |
|---|---|---|
| >= 89, stock vs patched on the fp8 path | bit-identical | bit-identical |
| same GPU, new path vs fp8 path | bit-identical | bit-identical |
| A800 sm80, new path vs an sm120 fp8 reference | bit-identical | bit-identical |
| stock kernel on sm80 | still will not compile | still will not compile |

The first two rows were run on H100, B200 and RTX 5090; the third crosses machines.
"Bit-identical" rather than "close": every conversion involved is exact, and the
accumulator is fp32 on both paths either way.

**The MoE change is smaller than I expected.** All eight e2m1 magnitudes have a zero
low byte in fp16, so your single `prmt.b32` table lookup survives untouched — the
decoded byte is shifted up 8 and bitcast to fp16 instead of bitcast to fp8. The sign
step needs no change at all, since bit 7 of the byte is fp16's sign bit too. The
activations are converted host-side, which is lossless because fp16 represents every
e4m3 value. Roughly 30 lines, and `capability >= 89` keeps your path byte for byte.

**The cache packing is the more real piece**, as expected: it has to *produce* e4m3
bytes rather than land the arithmetic elsewhere, so that one builds the byte pattern
arithmetically (RNE, subnormals, overflow) and takes a `uint8` view of the same
buffer, since a store through an fp8 pointer is equally uncompilable below 89.

One thing from writing that encoder that may be worth your knowing independently of
this patch: **`torch` and Triton disagree about e4m3 overflow, and `torch` disagrees
with itself across versions.** Triton's `.to(tl.float8e4nv)` saturates to 0x7E;
`torch.Tensor.to(torch.float8_e4m3fn)` returns NaN on 2.11 and saturates on 2.13. I
first validated the encoder against torch and got the overflow semantics wrong in a
way that only showed up on the other machine. Anything comparing your fp8 paths
against a torch reference has the same trap in it.

What I have not done: no performance numbers, and no end-to-end V4 run. The
verification is against your launchers' own contracts with synthetic inputs, not the
model — V4 cannot serve on SM80 in LMDeploy until the indexer scoring and FlashMLA
are answered too, and those are still your call, not something I have quietly gone
ahead with.

Happy to open it as a PR whenever you say, or to leave it here if you would rather
not carry the second code path. Either answer is useful to me; the analysis was
worth having regardless.

It is on a branch rather than in a description, in case reading it is faster than
reading me: **[`Hakureirm/lmdeploy:sm80-fp8e4nv-decode`](https://github.com/InternLM/lmdeploy/compare/main...Hakureirm:lmdeploy:sm80-fp8e4nv-decode)**
— two files, +111/-14, one commit per kernel. No PR opened; say the word and I will
send it, or ignore the branch and nothing is owed either way.


### grimoire · 2026-08-24

We have not provided a non-FlashMLA fallback, If sparse attention in FlashMLA does not support sm80, other update are meaningless.

### Hakureirm · 2026-09-01

A useful data point rather than an argument, since this is your call and not mine:

SGLang treats sparse attention as a swappable backend rather than as FlashMLA —
`flashmla_sparse`, `flashmla_kv`, `flashmla_auto`, `fa3`, `tilelang`, `aiter` and
`trtllm` are all selectable for the same decode, and it auto-picks a non-FlashMLA one
where FlashMLA is not available (`tilelang`, in `nsa/tilelang_kernel.py`, is the one
that is a kernel rather than a Hopper library). Nothing about the model requires
FlashMLA specifically; the absence of a fallback is a property of the current V4
runtime rather than of sparse MLA.

Whether you want a second sparse path is a much bigger question than those two
kernels, and it is yours. I am not going to build one unasked, and I would want to
hear that you want it before spending the time. If the answer is no, that is a fine
answer and the branch can just sit there.

One practical note: `v4_fp4_fused_moe.py` moved to `moe/v4_fp4.py` in a96cb3f, so the
branch targets the old path. The kernel body is unchanged, so it is a rebase rather
than a rewrite — happy to do that if the answer ever becomes yes.

