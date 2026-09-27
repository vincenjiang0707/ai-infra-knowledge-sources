# [Issue #1592] [Feature Request] Request for sm120 nvfp4 gemm support

source: https://github.com/tile-ai/tilelang/issues/1592
state: open | updated: 2026-09-27T02:35:22Z
labels: enhancement

## 正文

### Required prerequisites

- [x] I have searched the [Issue Tracker](https://github.com/tile-ai/tilelang/issues) that this hasn't already been reported. (comment there if it has.)

### Motivation

<!-- Please outline the motivation for the proposal.
Is your feature request related to a problem? E.g., "I'm always frustrated when [...]".
If this is related to another issue, please link here too. -->
Hello request for sm120 nvfp4 gemm support, I can provide the rtx-5090 gpus, contact me: 3633987847@qq.com


### Solution

_No response_

### Alternatives

_No response_

### Additional context

_No response_

## 评论 (1)

### ghostrider0470 · 2026-09-27

At Horizon Tech I've been working on SM120 NVFP4 for LLM inference on an RTX PRO 6000 Blackwell (96 GB, sm_120) and would like to contribute the parts that complement the new block-scaled GEMM support (#3237, #3257).

For serving, the new `T.gemm_blockscaled` path covers W4A4. Two gaps remain in practice: the small-M decode path, where most tokens are generated, and prefill on real checkpoints. Here is what I have, all written in TileLang against current `main`:

**1. W4A16 NVFP4 GEMM for decode (M = 1…1024)**
- FP4 weights are dequantized in registers from a fragment-ordered layout (~2 instructions per weight); activations stay BF16.
- vs Marlin (vLLM's NVFP4 W4A16), layer-weighted over the Qwen3.8-27B shapes: **3–4% faster at M = 1–32**, up to 7% at M = 96. It ties within +1–2% at M = 33–64 and 192–256, where Marlin is also near the tensor-core limit.
- At M = 1 a GEMV variant reaches ~96% of memory bandwidth on the widest layer.
- Correctness: 288/288 cases within tolerance vs a reference, deterministic, CUDA-graph replay tested.

**2. W4A4 prefill with two-pass residual activations**
- Activations are quantized in two NVFP4 passes (value + residual) to recover near-BF16 accuracy on the native `mxf4nvf4` tensor cores.
- ~960–1,036 TFLOPS on the same shapes: **3.1–4.0× faster than Marlin at 512–8,192 tokens**.
- Validated end-to-end with log-prob and paired-eval checks.

**3. A register-A speed-up for the #3257 path** (small, ready first): unroll the K atoms so the A fragment stays in registers (no local-memory spills), and load the scale factors once per atom instead of once per MMA. Outputs are unchanged.

End to end in vLLM (Qwen3.8-27B NVFP4, one RTX PRO 6000, MTP speculative decoding), single-stream decode went from 111.8 tok/s (NVFP4 + Marlin) to 143.3 tok/s with these kernels plus a few fused decode ops, quality-neutral in paired evals (GSM8K, MMLU-Pro; no significant change) and log-prob checks over ~108k tokens.

Plan, unless you'd prefer a different shape:
1. A PR with the register-A speed-up (it touches `gemm_mma_sm120.py`, so I'll rebase after #3284 and coordinate with #3081).
2. A PR adding the W4A16 decode GEMM, with tests gated on sm_120 and a benchmark vs Marlin.
3. A PR with the two-pass W4A4 prefill.

Questions before I open 2 and 3:
- Would you like these in the library (e.g. an SM120 W4A16 lowering or intrinsics) or as `examples/` + `maint/` benchmarks first?
- Is there any direction for small-M W4A16 on SM120 already in progress that I should build on?

I can run tests and benchmarks on sm_120 hardware for these PRs.

