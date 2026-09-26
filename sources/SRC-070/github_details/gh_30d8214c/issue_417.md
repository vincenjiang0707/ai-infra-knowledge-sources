# [Issue #417] [Regression] 8b1392b removes SM12x pure-fp8 1d1d kernels and aliases fp8_gemm_nt to the fp4 dispatcher (silent corruption on GB10)

source: https://github.com/deepseek-ai/DeepGEMM/issues/417
state: open | updated: 2026-09-16T10:32:14Z
labels: 

## 正文

## Summary

Between `a6b593d` and `8b1392b` on `nv_dev`, the SM12x pure-fp8 path regressed.

Verified diff (`git diff a6b593d..8b1392b`):

- **Removed**: `csrc/jit_kernels/impls/sm100_fp8_gemm_1d1d.hpp` (−416) and
  `deep_gemm/include/deep_gemm/impls/sm100_fp8_gemm_1d1d.cuh` (−567) — the
  pure-fp8 1d1d kernels.
- `fp8_fp4_mqa_logits` dispatch rewritten: generic `smxx_fp8_mqa_logits`
  → per-arch `sm90_fp8_mqa_logits` / `sm100_mqa_logits` / `sm120_mqa_logits`.
- NOTE (correction of the earlier draft): the `fp8_gemm_nt = fp8_fp4_gemm_nt`
  alias is **not** new — it exists in `a6b593d` already (`gemm.hpp:792`).
  The regression is the 1d1d kernel removal, not the alias.

## Impact (measured on 2x DGX Spark, GB10 / sm_121a)

With `--linear-backend deep_gemm` (DeepSeek-V4-Flash FP8 linear + MLA),
fp8xfp8 inputs on SM12x run the combined `sm120_fp8_fp4_gemm_1d1d` kernel,
which misreads fp8 weights as fp4: **silent numerical corruption**. Greedy
France output degenerates (`' Septy Septy…'`) and DSpark draft acceptance
collapses, dropping decode from ~25.8 tok/s (b12x linear baseline) to
~4.4 tok/s.

`a6b593d` (the last good commit, frozen by eugr/spark-vllm-docker and used
by vLLM v0.25.1) serves correctly.

## Request

Restore the pure-fp8 1d1d kernels on `nv_dev` (or route fp8xfp8 on SM12x
back to a pure-fp8 kernel) so the fp8 path is correct again. vLLM's cmake
pin is currently `8b1392b`; we have opened a vLLM PR
([#53680](https://github.com/vllm-project/vllm/pull/53680)) to pin back to
`a6b593d` in the interim.


## 评论 (4)

### maci0 · 2026-08-26

Status update: with the a6b593d wheel, the SM12x fp8 einsum path (fp8_einsum "bhr,hdr->bhd", DSV4 o_proj) now passes DeepGEMM's host layout checks and launches on sm_121a with finite output at T=10 / T=96 / T=8192 (real DeepSeek-V4-Flash-0731 shapes). The remaining blocker for the full `fp8_gemm_nt` 1d1d path is the JIT toolchain: stock CUDA 13.0/13.3 ptxas rejects tcgen05.mma for sm_12x targets, and the NVRTC cubin route is rejected by the driver (CUDA_ERROR_INVALID_IMAGE). We are evaluating the driver-JIT PTX route (nvrtcGetPTX + cuModuleLoadDataEx) and will open a PR with the fix.

### maci0 · 2026-08-26

The restore is now proposed in #419 (pure-fp8 1d1d kernel + header fixes: the a6b593d TU cannot compile as-is — math.cuh/cuda_bf16.h were missing from the include chain; the NVRTC frontend compiles it to PTX once fixed). Note the GB10 JIT toolchain gap still blocks runtime assembly of the tcgen05 instructions on stock CUDA 13.x (ptxas rejects tcgen05 for sm_121a; NVRTC cubin and driver-JIT PTX are both rejected by the driver) — the kernel needs build-time compilation or a fixed toolchain, same as the golden stack does today.

### lucifer1004 · 2026-09-16

In #447 the SM12x dispatch is dtype-driven end to end: `fp8_gemm_nt` enters a unified fp8/fp4 dispatcher, but the actual operand dtypes select the instantiation — fp8×fp8 compiles the 1D1D kernel with `kIsFP4=false` (native pure-fp8; SF granularity, swizzle modes and MMA kind all follow the fp8 path). There is no fp8-as-fp4 reinterpretation anywhere, so the silent-corruption mode is gone.

The reverse direction is loud rather than silent: combos with no SM120 implementation (e.g. K-grouped FP4 NT) hit `DG_HOST_UNREACHABLE` with an explicit message, covered by rejection tests (`test_sm120_k_grouped_fp4_unsupported_rejection`, `test_sm120_native_rejections.py`). Pure-fp8 correctness is covered by the dense fp8 suites and the `fmt=(False,False)` SF-branch regressions.


### maci0 · 2026-09-16

Thanks, that matches what we measure. We built `vllm-project/DeepGEMM@ad1f1726` on 2x GB10 (sm_121) and the dtype-driven instantiation is what we see: fp8 x fp8 selects the 1D1D kernel with `kIsFP4=false`, and with packed ue8m0 scale factors the result is exact against a dequantised reference (relative error 0) at 1x128x256 and 7x512x4096.

One failure mode we hit on that commit, which is a different mechanism from the fp8-as-fp4 alias and is worth checking against #447. A float32 SF with `disable_ue8m0_cast=True` is read by the SM120 kernel as packed ue8m0, because `layout.hpp:38/42` keep a float SF in the SM90 float layout whenever that flag is set, and the flag's clause only ever fires on arch 10/12. So the raw fp32 bytes are read as exponents (`0xFF` is `2^128`, which is the NaN) and `max_abs_err` is inf or ~1e30; the NaN fraction is allocator-dependent (1/128 = 0.781% at 1x128x256, matching the number we reported here earlier). For SFB the TMA descriptor is sized from `n` rather than `n / gran_mn`, so it reads past the tensor, which is probably the `Xid 43` seen on that path. `f9d0e2361` (#9) added `DG_HOST_ASSERT(sfa.scalar_type() == torch::kInt and sfb.scalar_type() == torch::kInt)` after the transform and that turns it into a clean rejection. If #447 carries the same guard plus the `test_sm120_native_rejections.py` cases you mention, I would expect the silent mode to be closed on both sides.

We can run #447's SM120 path on sm_121 when it is at a buildable commit, including the DSv4.1 sparse MQA and fp8 einsum paths, since that is the stack we serve (DeepSeek-V4-Flash-0731, TP=2). Say the word and we will post the results here.

Two questions, since #447 changes what is needed around it:

1. Should #417 be closed, given #447 makes the alias-driven corruption impossible by construction? We are happy either way; we just do not want to leave a stale report open if it is resolved.
2. What about #419 (restoring the SM100 pure-fp8 1d1d kernel plus the missing header includes in the a6b593d TU)? If #447 brings a native SM120 fp8 path into nv_dev, that port looks moot for SM12x, and the SM100 side may not need it either. If so, we would rather close it than leave two overlapping proposals.

For context on why we care about the nv_dev arm specifically: our image pins nv_dev at `a6b593d` (eugr's freeze, taken because 8b1392b dropped the pure-fp8 1d1d kernels), and we carry local ports on top. Landing #447 would let us drop that freeze and follow nv_dev.

