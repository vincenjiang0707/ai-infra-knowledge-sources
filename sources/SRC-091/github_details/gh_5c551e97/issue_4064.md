# [Issue #4064] TurboQuant serde fails on vLLM fp8 KV cache — CompilationError: cannot cast uint8 to fp8e4nv, 0 bytes offloaded to L2

source: https://github.com/LMCache/LMCache/issues/4064
state: closed | updated: 2026-09-18T10:33:50Z
labels: stale

## 正文

With the TurboQuant serde on an L2 adapter and vLLM serving with --kv-cache-dtype fp8, every serialize task throws a Triton CompilationError and no KV is written to L2 — the SSD copy is silently empty while store requests report "completed." Serving with bf16/auto KV works, so the failure is specific to the fp8 (uint8-backed) KV path.

Environment

LMCache v0.5.1 (TurboQuant serde, MP server + fs L2 adapter)
vLLM 0.22.0 (V1), LMCacheMPConnector, kv_role=kv_both
Model: Qwen3-Coder-30B-A3B-Instruct-FP8 · GPU: RTX PRO 6000 (sm_120), CUDA 13.0
--kv-cache-dtype fp8; preset turboquant_k8v4 (also repros with 4bit_nc, 3bit_nc)
Config — L2 adapter: {"type":"fs","base_path":"…","serde":{"type":"turboquant","preset":"turboquant_k8v4","block_size":16,"max_workers":8}}

Steps: start MP server w/ turboquant L2 adapter → serve vLLM --kv-cache-dtype fp8 via LMCacheMPConnector → drive traffic past L1 → du -sb <L2 path> stays 0.

Expected: KV quantized and written to L2; restores dequantize back.
Actual: 0 bytes on L2; all serialize/store tasks fail; l2_store_completed_requests_total increments but …_objects_chunks_total/on-disk bytes = 0 (failure swallowed).

Log

LMCache ERROR: Serde task 0 (SERIALIZE) failed        (async_processor.py:196)
  File ".../serde/turboquant/turboquant.py", line 641, in serialize
    triton_turboquant_store(key, value, ...)
  File ".../serde/turboquant/store_kernel.py", line 387, in triton_turboquant_store
    _tq_fused_store_fp8[grid](k_flat, v_flat, ...)
triton.compiler.errors.CompilationError: at 45:56:
AssertionError: cannot cast uint8[constexpr[128]] to <['128'], fp8e4nv>
LMCache WARNING: Store task 0 to adapter 0 failed for keys: [...]


## 评论 (4)

### lcheng321 · 2026-07-11

Taking this one. Looks like store_kernel.py value-casts uint8-backed fp8 to fp8e4nv instead of bitcasting like the decode side does; fixing it now with a roundtrip regression test and will open a PR shortly.

### lcheng321 · 2026-07-15

fixed in https://github.com/LMCache/LMCache/pull/4118

### lcheng321 · 2026-07-16

@rohit-metrum-ai fix is up in #4118, reproduced and verified on my end. Mind giving it a try on your setup too?

### github-actions[bot] · 2026-09-15

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.
