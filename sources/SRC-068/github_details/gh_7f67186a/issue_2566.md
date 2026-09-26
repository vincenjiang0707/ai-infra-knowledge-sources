# [Issue #2566] FLASH_ATTENTION_CUTE_DSL_CACHE_ENABLED=1 causes cudaErrorInvalidDeviceFunction on cross-process load

source: https://github.com/Dao-AILab/flash-attention/issues/2566
state: open | updated: 2026-07-24T06:06:03Z
labels: 

## 正文

**Title:** `FLASH_ATTENTION_CUTE_DSL_CACHE_ENABLED=1` causes `cudaErrorInvalidDeviceFunction` on cross-process load

## Summary

Enabling the cute DSL persistent JIT cache (`FLASH_ATTENTION_CUTE_DSL_CACHE_ENABLED=1` + `FLASH_ATTENTION_CUTE_DSL_CACHE_DIR=<path>`) causes the next process to crash on its first attention call with:

```
RuntimeError: CUDA Error: cudaErrorInvalidDeviceFunction
  in _flash_attn_fwd.compile_cache[compile_key](...)
```

The cache key in `flash_attn/cute/cache_utils.py` doesn't fully disambiguate compiled artifacts. A `.cubin` cached by one process is loaded into a different process's `compile_cache` dict for a slightly different call site, then handed to CUDA's launch, which rejects it.

Within a single process the in-memory cache works correctly — same process's compiled kernels match their use sites. The bug is specifically in cross-process reuse of the disk-cached artifacts.

## Environment

- flash-attention: `Dao-AILab/flash-attention@<recent HEAD>` (also reproducible with `RandNMR73/flash-attention@fa4-compile`, fork SHA `71677f5f`)
- torch: 2.11.0+cu128
- CUDA: 12.9.1
- Python: 3.12.13
- GPU: NVIDIA GB200 (sm_100)
- nvidia-cutlass-dsl: bundled with torch wheel
- Workload: LTX-2 video diffusion (FastVideo), bidirectional self-attention via `flash_attn.cute`

## Reproduce

1. Set `FLASH_ATTENTION_CUTE_DSL_CACHE_ENABLED=1` and `FLASH_ATTENTION_CUTE_DSL_CACHE_DIR=/persistent/path` in the container env.
2. Start a Python process that exercises `flash_attn.cute` over multiple attention shapes (we hit it on first call after a warmup pass with stage-1 + stage-2 latent shapes).
3. Let the process terminate gracefully so the cache flushes to disk (`/persistent/path` populated with cubin files).
4. Start a fresh process with the same env vars.
5. On the first `flash_attn.cute` call after `compile_cache` has loaded from disk, observe `cudaErrorInvalidDeviceFunction`.

## Logs

```
[1;36m(Worker pid=319)[0;0m ERROR 05-14 13:37:55.812 [multiproc_executor.py:537]     out, lse = _flash_attn_fwd(
[1;36m(Worker pid=319)[0;0m ERROR 05-14 13:37:55.812 [multiproc_executor.py:537]                ^^^^^^^^^^^^^^^^
[1;36m(Worker pid=319)[0;0m ERROR 05-14 13:37:55.812 [multiproc_executor.py:537]     _flash_attn_fwd.compile_cache[compile_key](
[1;36m(Worker pid=319)[0;0m ERROR 05-14 13:37:55.812 [multiproc_executor.py:537] RuntimeError: CUDA Error: cudaErrorInvalidDeviceFunction
```

## Suspected cause

The cache key in `flash_attn/cute/cache_utils.py:_compute_source_fingerprint` hashes Python source content + cutlass/tvm_ffi versions, but the actual compiled kernel binary depends on additional runtime context that isn't captured in the key:
- The exact call-site argument shapes (the JIT specializes per shape).
- Possibly device-specific JIT artifacts that are bound to driver instance / module state.

When process B loads process A's cached cubin under a key collision and hands it to CUDA, the kernel's expected device function signature doesn't match the launch site, and the driver returns `cudaErrorInvalidDeviceFunction`.

## Workaround

Leave `FLASH_ATTENTION_CUTE_DSL_CACHE_ENABLED` unset (default off). The in-process JIT cache still works fine; only the cross-process persistence path is affected.

## Expected fix

Either:
- Tighten the cache key to include per-call-site signature (input shape tuple, dtype, head_dim, etc.) so cross-process loads never resolve to a wrong cubin.
- Validate the loaded artifact against the call site before invoking it (e.g., re-check kernel symbol metadata) and fall through to JIT-recompile on mismatch.

## 评论 (1)

### hebo1221 · 2026-07-24

I could not reproduce this on current `main` (`b54df166ebb69b896892826014759d09b9c3c9c6`) on GB10 / SM121, but this result may still be architecture-specific because the report is from GB200 / SM100.

Environment:
- PyTorch `2.13.0+cu130` / CUDA `13.0`
- nvidia-cutlass-dsl `4.6.0.dev0`
- tvm-ffi `0.1.13rc1`

I used a brand-new dedicated cache directory and launched the same BF16 forward+backward repository test in two separate pytest processes (`batch=2`, `seqlen=128`, `heads=4`, `head_dim=64`). Process 1 logged cache misses and exported four objects (`fwd`, `bwd_pre`, `bwd`, `bwd_post`). Process 2 explicitly logged `Loading compiled function from disk` for the same four object hashes, then completed successfully: `1 passed`.

So cross-process persistence itself works for this SM121/current-DLS combination, and the current compile keys do include `arch` plus the relevant static kernel configuration. Could you retest current `main` on SM100 and, if it still fails, share:

1. `FA_LOG_LEVEL=1` output showing the exact object hash loaded immediately before the failure;
2. whether the persistent directory is shared by different GPU architectures, CUTLASS DSL builds, or container images;
3. the two attention calls that produce the colliding key (including strides/broadcasted dimensions, not only shapes)?

That should distinguish an SM100 AOT-loader problem from an actual key omission without guessing at a fix.
