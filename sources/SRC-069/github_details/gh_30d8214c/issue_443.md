# [Issue #443] DeepGEMM JIT: CUDA 800 (NOT_PERMITTED) at jit/handle.hpp:154 kills vLLM engine on first long-context request

source: https://github.com/deepseek-ai/DeepGEMM/issues/443
state: open | updated: 2026-09-16T08:56:37Z
labels: 

## 正文

 ## Environment

GB10 (DGX Spark, sm_121a), CUDA 13.2, driver 595.x
vLLM local build v0.25.2.dev0+g752a3a504.d20260714, TP=2, CUDA graphs FULL_AND_PIECEWISE (lazy capture), chunked prefill + prefix caching, MTP-6 spec decode
Model: DeepSeek-V4-Flash (hybrid mamba+MLA+sparse indexer MoE), fp8 weights, nvfp4_ds_mla KV
DeepGEMM: vendored, offline-nvcc JIT (DG_JIT_USE_NVRTC=0), persistent cache, PDL enabled (set_pdl(True))


## Error (first decode step after a 287k-token prefill):
```
RuntimeError: CUDA driver error
(/workspace/.deps/deepgemm-src/csrc/apis/../jit_kernels/impls/../../jit/handle.hpp:154):
800 (CUDA_ERROR_NOT_PERMITTED, operation not permitted)
→ EngineDeadError → API server exit
```

## Call path
deepseek_v4/attention.py → flashinfer_sparse.py:606 _o_proj → ops/o_proj.py fp8_einsum("bhr,hdr->bhd") → DeepGEMM JIT

### Trigger
First-ever execution of the sparse o_proj einsum path: a ~287k-token request (2 concurrent, 124k/125k prefix-cache hits) after 29 h uptime with only short-context traffic. Prefill itself succeeded (286,720 tokens computed, KV 10% used). Boot-time DeepGEMM warmup (1,762 kernels) does not cover this path/shape.

## Suspected cause
The nvcc compile step succeeds; the failure is at the driver call in handle.hpp:154 (module load or PDL-attributed launch). JIT module load / PDL launch is prohibited while any stream in the context is capturing — and vLLM lazily captures a new decode graph exactly when a new batch shape appears, so a first-time JIT compile can land inside a capture window.

- Error 800 = operation not permitted (not OOM, not invalid handle)
- Intermittent by nature: after restart, six long-context runs (64k–509k tokens, incl. 2-concurrent 255k) all passed; the compiled shape is then cached and never hits the JIT path again

## Question
Which driver call is at jit/handle.hpp:154 in the current jit_kernels/impls layout — module load or PDL launch? And is there a recommended capture-safe pattern (e.g., defer load while cudaStreamIsCapturing, or retry-once-on-800)?

## Proposed fix
Defer cuModuleLoadData until capture ends (queue + load after cudaStreamEndCapture), or retry once on 800. A set_pdl(False) toggle would also be a useful operator workaround. Happy to test a patched build and provide the full crash log.

## 评论 (1)

### lucifer1004 · 2026-09-16

The failing path no longer exists on the #447 branch: the old in-tree JIT (`csrc/jit/handle.hpp`, the NVRTC/module-load machinery) was replaced wholesale by DeepJIT — offline `nvcc` is the only compile backend, libraries are loaded via a lazily-dlopened `libcuda`, and the CUDA context is explicitly established before any driver API call (the standard remedy class for `CUDA_ERROR_NOT_PERMITTED` on first driver-API touch).

Verified the analogous scenario on a GB10 (sm_121a): fresh JIT cache, offline nvcc, PDL enabled, ~72 GiB of VRAM deliberately pinned first to simulate the post-long-prefill state, then first-ever compile+launch of the sparse o_proj fp8 einsum `bhr,hdr->bhd` at the issue's shape (b=2, h=32, r=128, d=7168) plus two more fresh shapes — all compile and run cleanly, numerics match the eager reference, two independent rounds. No CUDA error.

Caveat: this is an analogous-scenario verification (the exact failing code is gone, so a literal before/after on the same file is impossible); if you still see an 800 on this branch, a driver-API trace would pinpoint the new call site.

