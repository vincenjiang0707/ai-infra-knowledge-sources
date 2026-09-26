# [Issue #301] [Bug] JIT cache lacks cross-process synchronization, can cause failures under multi-process parallelism

source: https://github.com/deepseek-ai/DeepGEMM/issues/301
state: open | updated: 2026-04-11T16:39:30Z
labels: 

## 正文

## Description

`Compiler::build()` in `csrc/jit/compiler.hpp` does not synchronize across processes. When multiple processes target the same kernel (same signature hash, same cache directory), they can race on writing and reading `kernel.cu` and `kernel.cubin`, potentially causing:

- `CUDA driver error: 301 (CUDA_ERROR_FILE_NOT_FOUND, file not found)`
- `NVCC compilation failed: cc1plus: fatal error: .../kernel.cu: No such file or directory`

This was observed downstream in vllm-project/vllm#39057, where a user running DeepSeek-V3.2 with `-dp 8 --enable-expert-parallel` (8x H200, cache on a network filesystem) hit both errors during startup. The lack of locking in `build()` is a plausible explanation and seems worth fixing regardless.

cc @jxdn

## Initial code analysis

Multiple processes with the same kernel signature will compute the same `dir_path`:

```cpp
const auto dir_path = cache_dir_path / "cache" /
    fmt::format("kernel.{}.{}", name, get_hex_digest(kernel_signature));
```

With no locking, im guessing the following can happen concurrently:

1. Both processes call `make_dirs(dir_path)` and enter `compile()`
2. Both call `put(code_path, code)` which atomically renames a temp file to `dir_path/kernel.cu` — one process's write replaces the other's
3. For `NVCCCompiler`, NVCC is invoked as an external subprocess that reads `kernel.cu` from disk (line 214). If another process replaces or is mid-replace of that file, NVCC can fail with "file not found"
4. Similarly, both processes race on `rename(tmp_cubin, kernel.cubin)`

`NVRTCCompiler` compiles from an in-memory string so it avoids the `kernel.cu` read race, but still shares the cubin output path.

## What isnt verified

~~ - I haven't reproduced this in a controlled test — the downstream report is the only data point~~ I was able to verify this last night
- The network filesystem (`/hpfs/...`) could be a contributing factor (e.g. NFS caching behavior), independent of the race
~~- A corrupted or stale cache from a prior run could also produce similar errors~~  Accounted for in my test / setup in #302 

## Environment (from the downstream report)

- DeepGEMM at commit 477618c (pinned by vLLM)
- vLLM 0.19.1rc1.dev44
- 8x NVIDIA H200, CUDA 12.8, RHEL 9.4
- Cache directory on a shared/network filesystem (`/hpfs/...`)

## Suggested fix

Add a per-kernel file lock (`flock()`) around the compilation step in `build()` with a double-checked locking pattern:

```cpp
// Fast path — already compiled in this process
if (const auto& runtime = kernel_runtime_cache->get(dir_path); runtime != nullptr)
    return runtime;

// Acquire cross-process lock
FileLock lock(lock_path);  // RAII wrapper around flock(LOCK_EX)

// Re-check after acquiring lock — another process may have compiled it
if (const auto& runtime = kernel_runtime_cache->get(dir_path); runtime != nullptr)
    return runtime;

// Only now compile...
```

This would have zero overhead during steady-state inference (the in-process cache returns before reaching the lock) and only serializes compilation of the *same* kernel across processes — different kernels still compile in parallel.

Will try to reproduce and create a fix.

## 评论 (1)

### Gregory-Pereira · 2026-04-11

>What isnt verified
> - I haven't reproduced this in a controlled test — the downstream report is the only data point I was able to verify this last night
> - The network filesystem (/hpfs/...) could be a contributing factor (e.g. NFS caching behavior), independent of the race
> - A corrupted or stale cache from a prior run could also produce similar errors Accounted for in my test / setup in https://github.com/deepseek-ai/DeepGEMM/pull/302

I was able to verify this in my process of testing 302, also got:

```
Loading safetensors checkpoint shards:  95% Completed | 155/163 [16:21<00:14,  1.77s/it]
(Worker_DP0_EP0 pid=491) 
Loading safetensors checkpoint shards:  97% Completed | 158/163 [16:22<00:05,  1.08s/it]
(Worker_DP0_EP0 pid=491) 
Loading safetensors checkpoint shards:  98% Completed | 160/163 [16:22<00:02,  1.18it/s]
(Worker_DP0_EP0 pid=491) 
Loading safetensors checkpoint shards:  99% Completed | 161/163 [16:33<00:04,  2.47s/it]
(Worker_DP0_EP0 pid=491) 
Loading safetensors checkpoint shards: 100% Completed | 163/163 [16:33<00:00,  6.09s/it]
(Worker_DP0_EP0 pid=491) 
(Worker_DP0_EP0 pid=491) INFO 04-11 14:49:48 [default_loader.py:384] Loading weights took 993.09 seconds
(Worker_DP0_EP0 pid=491) INFO 04-11 14:49:55 [fp8.py:577] Using MoEPrepareAndFinalizeNaiveDPEPModular
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871] WorkerProc failed to start.
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871] Traceback (most recent call last):
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 840, in worker_main
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     worker = WorkerProc(*args, **kwargs)
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return func(*args, **kwargs)
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 627, in __init__
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     self.worker.load_model()
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/worker/gpu_worker.py", line 323, in load_model
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     self.model_runner.load_model(load_dummy_weights=load_dummy_weights)
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return func(*args, **kwargs)
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/worker/gpu_model_runner.py", line 4751, in load_model
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     self.model = model_loader.load_model(
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]                  ^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return func(*args, **kwargs)
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/model_loader/base_loader.py", line 81, in load_model
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     process_weights_after_loading(model, model_config, target_device)
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/model_loader/utils.py", line 118, in process_weights_after_loading
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     module.process_weights_after_loading(model_config.dtype)
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/attention/mla_attention.py", line 747, in process_weights_after_loading
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     kv_b_proj_weight = get_and_maybe_dequant_weights(
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/quant_utils.py", line 390, in get_and_maybe_dequant_weights
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     dequant_weights = layer.quant_method.apply(layer, eye, bias=None).to(out_dtype)
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/fp8.py", line 489, in apply
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return self.w8a8_block_fp8_linear.apply(
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 414, in apply
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     output = self._run_flashinfer(input_2d, weight, weight_scale)
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 544, in _run_flashinfer
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     output = torch.ops.vllm.flashinfer_fp8_blockscale_gemm(
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm/lib64/python3.12/site-packages/torch/_ops.py", line 1209, in __call__
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return self._op(*args, **kwargs)
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 318, in _flashinfer_fp8_blockscale_gemm_impl
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return torch.cond(
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm/lib64/python3.12/site-packages/torch/_higher_order_ops/cond.py", line 186, in cond
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return false_fn(*operands)
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 300, in run_deepgemm
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     fp8_gemm_nt(
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/utils/deep_gemm.py", line 226, in fp8_gemm_nt
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return _fp8_gemm_nt_impl(*args, disable_ue8m0_cast=not use_ue8m0, **kwargs)
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_EP2 pid=492) ERROR 04-11 14:49:58 [multiproc_executor.py:871] RuntimeError: Assertion error (csrc/apis/../jit_kernels/impls/../../jit/kernel_runtime.hpp:45): exit_code == 0
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871] WorkerProc failed to start.
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871] Traceback (most recent call last):
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 840, in worker_main
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     worker = WorkerProc(*args, **kwargs)
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return func(*args, **kwargs)
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 627, in __init__
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     self.worker.load_model()
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/worker/gpu_worker.py", line 323, in load_model
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     self.model_runner.load_model(load_dummy_weights=load_dummy_weights)
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return func(*args, **kwargs)
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/worker/gpu_model_runner.py", line 4751, in load_model
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     self.model = model_loader.load_model(
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]                  ^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return func(*args, **kwargs)
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/model_loader/base_loader.py", line 81, in load_model
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     process_weights_after_loading(model, model_config, target_device)
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/model_loader/utils.py", line 118, in process_weights_after_loading
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     module.process_weights_after_loading(model_config.dtype)
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/attention/mla_attention.py", line 747, in process_weights_after_loading
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     kv_b_proj_weight = get_and_maybe_dequant_weights(
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/quant_utils.py", line 390, in get_and_maybe_dequant_weights
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     dequant_weights = layer.quant_method.apply(layer, eye, bias=None).to(out_dtype)
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/fp8.py", line 489, in apply
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return self.w8a8_block_fp8_linear.apply(
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 414, in apply
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     output = self._run_flashinfer(input_2d, weight, weight_scale)
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 544, in _run_flashinfer
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     output = torch.ops.vllm.flashinfer_fp8_blockscale_gemm(
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm/lib64/python3.12/site-packages/torch/_ops.py", line 1209, in __call__
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return self._op(*args, **kwargs)
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 318, in _flashinfer_fp8_blockscale_gemm_impl
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return torch.cond(
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm/lib64/python3.12/site-packages/torch/_higher_order_ops/cond.py", line 186, in cond
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return false_fn(*operands)
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 300, in run_deepgemm
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     fp8_gemm_nt(
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/utils/deep_gemm.py", line 226, in fp8_gemm_nt
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return _fp8_gemm_nt_impl(*args, disable_ue8m0_cast=not use_ue8m0, **kwargs)
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_EP1 pid=494) ERROR 04-11 14:49:58 [multiproc_executor.py:871] RuntimeError: Assertion error (csrc/apis/../jit_kernels/impls/../../jit/kernel_runtime.hpp:45): exit_code == 0
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871] WorkerProc failed to start.
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871] Traceback (most recent call last):
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 840, in worker_main
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     worker = WorkerProc(*args, **kwargs)
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return func(*args, **kwargs)
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 627, in __init__
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     self.worker.load_model()
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/worker/gpu_worker.py", line 323, in load_model
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     self.model_runner.load_model(load_dummy_weights=load_dummy_weights)
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return func(*args, **kwargs)
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/worker/gpu_model_runner.py", line 4751, in load_model
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     self.model = model_loader.load_model(
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]                  ^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return func(*args, **kwargs)
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/model_loader/base_loader.py", line 81, in load_model
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     process_weights_after_loading(model, model_config, target_device)
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/model_loader/utils.py", line 118, in process_weights_after_loading
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     module.process_weights_after_loading(model_config.dtype)
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/attention/mla_attention.py", line 747, in process_weights_after_loading
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     kv_b_proj_weight = get_and_maybe_dequant_weights(
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/quant_utils.py", line 390, in get_and_maybe_dequant_weights
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     dequant_weights = layer.quant_method.apply(layer, eye, bias=None).to(out_dtype)
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/fp8.py", line 489, in apply
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return self.w8a8_block_fp8_linear.apply(
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 414, in apply
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     output = self._run_flashinfer(input_2d, weight, weight_scale)
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 544, in _run_flashinfer
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     output = torch.ops.vllm.flashinfer_fp8_blockscale_gemm(
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm/lib64/python3.12/site-packages/torch/_ops.py", line 1209, in __call__
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return self._op(*args, **kwargs)
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 318, in _flashinfer_fp8_blockscale_gemm_impl
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return torch.cond(
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm/lib64/python3.12/site-packages/torch/_higher_order_ops/cond.py", line 186, in cond
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return false_fn(*operands)
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 300, in run_deepgemm
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     fp8_gemm_nt(
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/utils/deep_gemm.py", line 226, in fp8_gemm_nt
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return _fp8_gemm_nt_impl(*args, disable_ue8m0_cast=not use_ue8m0, **kwargs)
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_EP3 pid=490) ERROR 04-11 14:49:58 [multiproc_executor.py:871] RuntimeError: Assertion error (csrc/apis/../jit_kernels/impls/../../jit/kernel_runtime.hpp:45): exit_code == 0
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871] WorkerProc failed to start.
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871] Traceback (most recent call last):
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 840, in worker_main
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     worker = WorkerProc(*args, **kwargs)
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return func(*args, **kwargs)
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 627, in __init__
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     self.worker.load_model()
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/worker/gpu_worker.py", line 323, in load_model
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     self.model_runner.load_model(load_dummy_weights=load_dummy_weights)
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return func(*args, **kwargs)
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/worker/gpu_model_runner.py", line 4751, in load_model
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     self.model = model_loader.load_model(
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]                  ^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return func(*args, **kwargs)
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/model_loader/base_loader.py", line 81, in load_model
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     process_weights_after_loading(model, model_config, target_device)
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/model_loader/utils.py", line 118, in process_weights_after_loading
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     module.process_weights_after_loading(model_config.dtype)
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/attention/mla_attention.py", line 747, in process_weights_after_loading
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     kv_b_proj_weight = get_and_maybe_dequant_weights(
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/quant_utils.py", line 390, in get_and_maybe_dequant_weights
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     dequant_weights = layer.quant_method.apply(layer, eye, bias=None).to(out_dtype)
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/fp8.py", line 489, in apply
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return self.w8a8_block_fp8_linear.apply(
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 414, in apply
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     output = self._run_flashinfer(input_2d, weight, weight_scale)
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 544, in _run_flashinfer
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     output = torch.ops.vllm.flashinfer_fp8_blockscale_gemm(
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm/lib64/python3.12/site-packages/torch/_ops.py", line 1209, in __call__
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return self._op(*args, **kwargs)
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 318, in _flashinfer_fp8_blockscale_gemm_impl
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return torch.cond(
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm/lib64/python3.12/site-packages/torch/_higher_order_ops/cond.py", line 186, in cond
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return false_fn(*operands)
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 300, in run_deepgemm
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     fp8_gemm_nt(
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/utils/deep_gemm.py", line 226, in fp8_gemm_nt
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return _fp8_gemm_nt_impl(*args, disable_ue8m0_cast=not use_ue8m0, **kwargs)
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP6_EP6 pid=489) ERROR 04-11 14:49:58 [multiproc_executor.py:871] RuntimeError: Assertion error (csrc/apis/../jit_kernels/impls/../../jit/kernel_runtime.hpp:45): exit_code == 0
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871] WorkerProc failed to start.
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871] Traceback (most recent call last):
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 840, in worker_main
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     worker = WorkerProc(*args, **kwargs)
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return func(*args, **kwargs)
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 627, in __init__
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     self.worker.load_model()
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/worker/gpu_worker.py", line 323, in load_model
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     self.model_runner.load_model(load_dummy_weights=load_dummy_weights)
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return func(*args, **kwargs)
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/worker/gpu_model_runner.py", line 4751, in load_model
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     self.model = model_loader.load_model(
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]                  ^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return func(*args, **kwargs)
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/model_loader/base_loader.py", line 81, in load_model
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     process_weights_after_loading(model, model_config, target_device)
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/model_loader/utils.py", line 118, in process_weights_after_loading
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     module.process_weights_after_loading(model_config.dtype)
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/attention/mla_attention.py", line 747, in process_weights_after_loading
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     kv_b_proj_weight = get_and_maybe_dequant_weights(
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/quant_utils.py", line 390, in get_and_maybe_dequant_weights
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     dequant_weights = layer.quant_method.apply(layer, eye, bias=None).to(out_dtype)
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/fp8.py", line 489, in apply
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return self.w8a8_block_fp8_linear.apply(
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 414, in apply
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     output = self._run_flashinfer(input_2d, weight, weight_scale)
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 544, in _run_flashinfer
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     output = torch.ops.vllm.flashinfer_fp8_blockscale_gemm(
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm/lib64/python3.12/site-packages/torch/_ops.py", line 1209, in __call__
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return self._op(*args, **kwargs)
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 318, in _flashinfer_fp8_blockscale_gemm_impl
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return torch.cond(
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm/lib64/python3.12/site-packages/torch/_higher_order_ops/cond.py", line 186, in cond
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return false_fn(*operands)
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 300, in run_deepgemm
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     fp8_gemm_nt(
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/utils/deep_gemm.py", line 226, in fp8_gemm_nt
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return _fp8_gemm_nt_impl(*args, disable_ue8m0_cast=not use_ue8m0, **kwargs)
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP5_EP5 pid=493) ERROR 04-11 14:49:58 [multiproc_executor.py:871] RuntimeError: Assertion error (csrc/apis/../jit_kernels/impls/../../jit/kernel_runtime.hpp:45): exit_code == 0
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871] WorkerProc failed to start.
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871] Traceback (most recent call last):
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 840, in worker_main
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     worker = WorkerProc(*args, **kwargs)
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return func(*args, **kwargs)
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 627, in __init__
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     self.worker.load_model()
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/worker/gpu_worker.py", line 323, in load_model
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     self.model_runner.load_model(load_dummy_weights=load_dummy_weights)
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return func(*args, **kwargs)
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/worker/gpu_model_runner.py", line 4751, in load_model
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     self.model = model_loader.load_model(
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]                  ^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return func(*args, **kwargs)
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/model_loader/base_loader.py", line 81, in load_model
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     process_weights_after_loading(model, model_config, target_device)
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/model_loader/utils.py", line 118, in process_weights_after_loading
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     module.process_weights_after_loading(model_config.dtype)
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/attention/mla_attention.py", line 747, in process_weights_after_loading
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     kv_b_proj_weight = get_and_maybe_dequant_weights(
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/quant_utils.py", line 390, in get_and_maybe_dequant_weights
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     dequant_weights = layer.quant_method.apply(layer, eye, bias=None).to(out_dtype)
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/fp8.py", line 489, in apply
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return self.w8a8_block_fp8_linear.apply(
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 414, in apply
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     output = self._run_flashinfer(input_2d, weight, weight_scale)
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 544, in _run_flashinfer
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     output = torch.ops.vllm.flashinfer_fp8_blockscale_gemm(
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm/lib64/python3.12/site-packages/torch/_ops.py", line 1209, in __call__
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return self._op(*args, **kwargs)
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 318, in _flashinfer_fp8_blockscale_gemm_impl
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return torch.cond(
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm/lib64/python3.12/site-packages/torch/_higher_order_ops/cond.py", line 186, in cond
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return false_fn(*operands)
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 300, in run_deepgemm
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     fp8_gemm_nt(
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/utils/deep_gemm.py", line 226, in fp8_gemm_nt
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return _fp8_gemm_nt_impl(*args, disable_ue8m0_cast=not use_ue8m0, **kwargs)
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP4_EP4 pid=488) ERROR 04-11 14:49:58 [multiproc_executor.py:871] RuntimeError: Assertion error (csrc/apis/../jit_kernels/impls/../../jit/kernel_runtime.hpp:45): exit_code == 0
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871] WorkerProc failed to start.
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871] Traceback (most recent call last):
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 840, in worker_main
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     worker = WorkerProc(*args, **kwargs)
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return func(*args, **kwargs)
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 627, in __init__
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     self.worker.load_model()
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/worker/gpu_worker.py", line 323, in load_model
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     self.model_runner.load_model(load_dummy_weights=load_dummy_weights)
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return func(*args, **kwargs)
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/worker/gpu_model_runner.py", line 4751, in load_model
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     self.model = model_loader.load_model(
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]                  ^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return func(*args, **kwargs)
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/model_loader/base_loader.py", line 81, in load_model
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     process_weights_after_loading(model, model_config, target_device)
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/model_loader/utils.py", line 118, in process_weights_after_loading
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     module.process_weights_after_loading(model_config.dtype)
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/attention/mla_attention.py", line 747, in process_weights_after_loading
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     kv_b_proj_weight = get_and_maybe_dequant_weights(
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/quant_utils.py", line 390, in get_and_maybe_dequant_weights
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     dequant_weights = layer.quant_method.apply(layer, eye, bias=None).to(out_dtype)
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/fp8.py", line 489, in apply
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return self.w8a8_block_fp8_linear.apply(
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 414, in apply
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     output = self._run_flashinfer(input_2d, weight, weight_scale)
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 544, in _run_flashinfer
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     output = torch.ops.vllm.flashinfer_fp8_blockscale_gemm(
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm/lib64/python3.12/site-packages/torch/_ops.py", line 1209, in __call__
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return self._op(*args, **kwargs)
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 318, in _flashinfer_fp8_blockscale_gemm_impl
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return torch.cond(
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm/lib64/python3.12/site-packages/torch/_higher_order_ops/cond.py", line 186, in cond
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return false_fn(*operands)
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 300, in run_deepgemm
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     fp8_gemm_nt(
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/utils/deep_gemm.py", line 226, in fp8_gemm_nt
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return _fp8_gemm_nt_impl(*args, disable_ue8m0_cast=not use_ue8m0, **kwargs)
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP7_EP7 pid=495) ERROR 04-11 14:49:58 [multiproc_executor.py:871] RuntimeError: Assertion error (csrc/apis/../jit_kernels/impls/../../jit/kernel_runtime.hpp:45): exit_code == 0
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871] WorkerProc failed to start.
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871] Traceback (most recent call last):
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 840, in worker_main
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     worker = WorkerProc(*args, **kwargs)
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return func(*args, **kwargs)
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 627, in __init__
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     self.worker.load_model()
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/worker/gpu_worker.py", line 323, in load_model
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     self.model_runner.load_model(load_dummy_weights=load_dummy_weights)
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return func(*args, **kwargs)
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/v1/worker/gpu_model_runner.py", line 4751, in load_model
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     self.model = model_loader.load_model(
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]                  ^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return func(*args, **kwargs)
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/model_loader/base_loader.py", line 81, in load_model
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     process_weights_after_loading(model, model_config, target_device)
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/model_loader/utils.py", line 118, in process_weights_after_loading
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     module.process_weights_after_loading(model_config.dtype)
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/attention/mla_attention.py", line 747, in process_weights_after_loading
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     kv_b_proj_weight = get_and_maybe_dequant_weights(
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/quant_utils.py", line 390, in get_and_maybe_dequant_weights
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     dequant_weights = layer.quant_method.apply(layer, eye, bias=None).to(out_dtype)
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/fp8.py", line 489, in apply
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return self.w8a8_block_fp8_linear.apply(
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 414, in apply
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     output = self._run_flashinfer(input_2d, weight, weight_scale)
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 544, in _run_flashinfer
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     output = torch.ops.vllm.flashinfer_fp8_blockscale_gemm(
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm/lib64/python3.12/site-packages/torch/_ops.py", line 1209, in __call__
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return self._op(*args, **kwargs)
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 318, in _flashinfer_fp8_blockscale_gemm_impl
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return torch.cond(
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm/lib64/python3.12/site-packages/torch/_higher_order_ops/cond.py", line 186, in cond
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return false_fn(*operands)
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/model_executor/layers/quantization/utils/fp8_utils.py", line 300, in run_deepgemm
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     fp8_gemm_nt(
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]   File "/opt/vllm-source/vllm/utils/deep_gemm.py", line 226, in fp8_gemm_nt
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]     return _fp8_gemm_nt_impl(*args, disable_ue8m0_cast=not use_ue8m0, **kwargs)
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_EP0 pid=491) ERROR 04-11 14:49:58 [multiproc_executor.py:871] RuntimeError: Assertion error (csrc/apis/../jit_kernels/impls/../../jit/kernel_runtime.hpp:45): exit_code == 0
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108] EngineCore failed to start.
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108] Traceback (most recent call last):
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]   File "/opt/vllm-source/vllm/v1/engine/core.py", line 1074, in run_engine_core
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]   File "/opt/vllm-source/vllm/v1/engine/core.py", line 1609, in __init__
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]     super().__init__(
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]     return func(*args, **kwargs)
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]   File "/opt/vllm-source/vllm/v1/engine/core.py", line 848, in __init__
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]     super().__init__(
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]   File "/opt/vllm-source/vllm/v1/engine/core.py", line 114, in __init__
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]     self.model_executor = executor_class(vllm_config)
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 105, in __init__
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]     super().__init__(vllm_config)
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]     return func(*args, **kwargs)
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]   File "/opt/vllm-source/vllm/v1/executor/abstract.py", line 109, in __init__
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]     self._init_executor()
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 208, in _init_executor
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 750, in wait_for_ready
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108]     raise e from None
(EngineCore_DP1 pid=416) ERROR 04-11 14:49:59 [core.py:1108] Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
(EngineCore_DP1 pid=416) Process EngineCore_DP1:
(EngineCore_DP1 pid=416) Traceback (most recent call last):
(EngineCore_DP1 pid=416)   File "/usr/lib64/python3.12/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP1 pid=416)     self.run()
(EngineCore_DP1 pid=416)   File "/usr/lib64/python3.12/multiprocessing/process.py", line 108, in run
(EngineCore_DP1 pid=416)     self._target(*self._args, **self._kwargs)
(EngineCore_DP1 pid=416)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 1112, in run_engine_core
(EngineCore_DP1 pid=416)     raise e
(EngineCore_DP1 pid=416)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 1074, in run_engine_core
(EngineCore_DP1 pid=416)     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_DP1 pid=416)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP1 pid=416)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 1609, in __init__
(EngineCore_DP1 pid=416)     super().__init__(
(EngineCore_DP1 pid=416)   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore_DP1 pid=416)     return func(*args, **kwargs)
(EngineCore_DP1 pid=416)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP1 pid=416)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 848, in __init__
(EngineCore_DP1 pid=416)     super().__init__(
(EngineCore_DP1 pid=416)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 114, in __init__
(EngineCore_DP1 pid=416)     self.model_executor = executor_class(vllm_config)
(EngineCore_DP1 pid=416)                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP1 pid=416)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 105, in __init__
(EngineCore_DP1 pid=416)     super().__init__(vllm_config)
(EngineCore_DP1 pid=416)   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore_DP1 pid=416)     return func(*args, **kwargs)
(EngineCore_DP1 pid=416)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP1 pid=416)   File "/opt/vllm-source/vllm/v1/executor/abstract.py", line 109, in __init__
(EngineCore_DP1 pid=416)     self._init_executor()
(EngineCore_DP1 pid=416)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 208, in _init_executor
(EngineCore_DP1 pid=416)     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_DP1 pid=416)                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP1 pid=416)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 750, in wait_for_ready
(EngineCore_DP1 pid=416)     raise e from None
(EngineCore_DP1 pid=416) Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
/usr/lib64/python3.12/multiprocessing/resource_tracker.py:279: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
(EngineCore_DP3 pid=422) Process EngineCore_DP3:
(EngineCore_DP3 pid=422) Traceback (most recent call last):
(EngineCore_DP3 pid=422)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 208, in _init_executor
(EngineCore_DP3 pid=422)     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_DP3 pid=422)                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP3 pid=422)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 750, in wait_for_ready
(EngineCore_DP3 pid=422)     raise e from None
(EngineCore_DP3 pid=422) Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
(EngineCore_DP3 pid=422) 
(EngineCore_DP3 pid=422) During handling of the above exception, another exception occurred:
(EngineCore_DP3 pid=422) 
(EngineCore_DP3 pid=422) Traceback (most recent call last):
(EngineCore_DP3 pid=422)   File "/usr/lib64/python3.12/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP3 pid=422)     self.run()
(EngineCore_DP3 pid=422)   File "/usr/lib64/python3.12/multiprocessing/process.py", line 108, in run
(EngineCore_DP3 pid=422)     self._target(*self._args, **self._kwargs)
(EngineCore_DP3 pid=422)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 1074, in run_engine_core
(EngineCore_DP3 pid=422)     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_DP3 pid=422)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP3 pid=422)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 1609, in __init__
(EngineCore_DP3 pid=422)     super().__init__(
(EngineCore_DP3 pid=422)   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore_DP3 pid=422)     return func(*args, **kwargs)
(EngineCore_DP3 pid=422)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP3 pid=422)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 848, in __init__
(EngineCore_DP3 pid=422)     super().__init__(
(EngineCore_DP3 pid=422)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 114, in __init__
(EngineCore_DP3 pid=422)     self.model_executor = executor_class(vllm_config)
(EngineCore_DP3 pid=422)                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP3 pid=422)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 105, in __init__
(EngineCore_DP3 pid=422)     super().__init__(vllm_config)
(EngineCore_DP3 pid=422)   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore_DP3 pid=422)     return func(*args, **kwargs)
(EngineCore_DP3 pid=422)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP3 pid=422)   File "/opt/vllm-source/vllm/v1/executor/abstract.py", line 109, in __init__
(EngineCore_DP3 pid=422)     self._init_executor()
(EngineCore_DP3 pid=422)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 252, in _init_executor
(EngineCore_DP3 pid=422)     self._ensure_worker_termination([uw.proc for uw in unready_workers])
(EngineCore_DP3 pid=422)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 434, in _ensure_worker_termination
(EngineCore_DP3 pid=422)     if wait_for_termination(active_procs(), 4):
(EngineCore_DP3 pid=422)        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP3 pid=422)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 428, in wait_for_termination
(EngineCore_DP3 pid=422)     time.sleep(0.1)
(EngineCore_DP3 pid=422)   File "/opt/vllm-source/vllm/entrypoints/openai/api_server.py", line 570, in signal_handler
(EngineCore_DP3 pid=422)     raise KeyboardInterrupt("terminated")
(EngineCore_DP3 pid=422) KeyboardInterrupt: terminated
/usr/lib64/python3.12/multiprocessing/resource_tracker.py:279: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
(EngineCore_DP2 pid=419) Process EngineCore_DP2:
(EngineCore_DP2 pid=419) Traceback (most recent call last):
(EngineCore_DP2 pid=419)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 208, in _init_executor
(EngineCore_DP2 pid=419)     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_DP2 pid=419)                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP2 pid=419)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 750, in wait_for_ready
(EngineCore_DP2 pid=419)     raise e from None
(EngineCore_DP2 pid=419) Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
(EngineCore_DP2 pid=419) 
(EngineCore_DP2 pid=419) During handling of the above exception, another exception occurred:
(EngineCore_DP2 pid=419) 
(EngineCore_DP2 pid=419) Traceback (most recent call last):
(EngineCore_DP2 pid=419)   File "/usr/lib64/python3.12/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP2 pid=419)     self.run()
(EngineCore_DP2 pid=419)   File "/usr/lib64/python3.12/multiprocessing/process.py", line 108, in run
(EngineCore_DP2 pid=419)     self._target(*self._args, **self._kwargs)
(EngineCore_DP2 pid=419)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 1074, in run_engine_core
(EngineCore_DP2 pid=419)     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_DP2 pid=419)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP2 pid=419)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 1609, in __init__
(EngineCore_DP2 pid=419)     super().__init__(
(EngineCore_DP2 pid=419)   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore_DP2 pid=419)     return func(*args, **kwargs)
(EngineCore_DP2 pid=419)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP2 pid=419)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 848, in __init__
(EngineCore_DP2 pid=419)     super().__init__(
(EngineCore_DP2 pid=419)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 114, in __init__
(EngineCore_DP2 pid=419)     self.model_executor = executor_class(vllm_config)
(EngineCore_DP2 pid=419)                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP2 pid=419)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 105, in __init__
(EngineCore_DP2 pid=419)     super().__init__(vllm_config)
(EngineCore_DP2 pid=419)   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore_DP2 pid=419)     return func(*args, **kwargs)
(EngineCore_DP2 pid=419)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP2 pid=419)   File "/opt/vllm-source/vllm/v1/executor/abstract.py", line 109, in __init__
(EngineCore_DP2 pid=419)     self._init_executor()
(EngineCore_DP2 pid=419)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 252, in _init_executor
(EngineCore_DP2 pid=419)     self._ensure_worker_termination([uw.proc for uw in unready_workers])
(EngineCore_DP2 pid=419)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 434, in _ensure_worker_termination
(EngineCore_DP2 pid=419)     if wait_for_termination(active_procs(), 4):
(EngineCore_DP2 pid=419)        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP2 pid=419)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 428, in wait_for_termination
(EngineCore_DP2 pid=419)     time.sleep(0.1)
(EngineCore_DP2 pid=419)   File "/opt/vllm-source/vllm/entrypoints/openai/api_server.py", line 570, in signal_handler
(EngineCore_DP2 pid=419)     raise KeyboardInterrupt("terminated")
(EngineCore_DP2 pid=419) KeyboardInterrupt: terminated
/usr/lib64/python3.12/multiprocessing/resource_tracker.py:279: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
(EngineCore_DP6 pid=431) Process EngineCore_DP6:
(EngineCore_DP6 pid=431) Traceback (most recent call last):
(EngineCore_DP6 pid=431)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 208, in _init_executor
(EngineCore_DP6 pid=431)     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_DP6 pid=431)                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP6 pid=431)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 750, in wait_for_ready
(EngineCore_DP6 pid=431)     raise e from None
(EngineCore_DP6 pid=431) Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
(EngineCore_DP6 pid=431) 
(EngineCore_DP6 pid=431) During handling of the above exception, another exception occurred:
(EngineCore_DP6 pid=431) 
(EngineCore_DP6 pid=431) Traceback (most recent call last):
(EngineCore_DP6 pid=431)   File "/usr/lib64/python3.12/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP6 pid=431)     self.run()
(EngineCore_DP6 pid=431)   File "/usr/lib64/python3.12/multiprocessing/process.py", line 108, in run
(EngineCore_DP6 pid=431)     self._target(*self._args, **self._kwargs)
(EngineCore_DP6 pid=431)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 1074, in run_engine_core
(EngineCore_DP6 pid=431)     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_DP6 pid=431)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP6 pid=431)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 1609, in __init__
(EngineCore_DP6 pid=431)     super().__init__(
(EngineCore_DP6 pid=431)   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore_DP6 pid=431)     return func(*args, **kwargs)
(EngineCore_DP6 pid=431)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP6 pid=431)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 848, in __init__
(EngineCore_DP6 pid=431)     super().__init__(
(EngineCore_DP6 pid=431)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 114, in __init__
(EngineCore_DP6 pid=431)     self.model_executor = executor_class(vllm_config)
(EngineCore_DP6 pid=431)                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP6 pid=431)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 105, in __init__
(EngineCore_DP6 pid=431)     super().__init__(vllm_config)
(EngineCore_DP6 pid=431)   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore_DP6 pid=431)     return func(*args, **kwargs)
(EngineCore_DP6 pid=431)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP6 pid=431)   File "/opt/vllm-source/vllm/v1/executor/abstract.py", line 109, in __init__
(EngineCore_DP6 pid=431)     self._init_executor()
(EngineCore_DP6 pid=431)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 252, in _init_executor
(EngineCore_DP6 pid=431)     self._ensure_worker_termination([uw.proc for uw in unready_workers])
(EngineCore_DP6 pid=431)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 434, in _ensure_worker_termination
(EngineCore_DP6 pid=431)     if wait_for_termination(active_procs(), 4):
(EngineCore_DP6 pid=431)        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP6 pid=431)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 428, in wait_for_termination
(EngineCore_DP6 pid=431)     time.sleep(0.1)
(EngineCore_DP6 pid=431)   File "/opt/vllm-source/vllm/entrypoints/openai/api_server.py", line 570, in signal_handler
(EngineCore_DP6 pid=431)     raise KeyboardInterrupt("terminated")
(EngineCore_DP6 pid=431) KeyboardInterrupt: terminated
/usr/lib64/python3.12/multiprocessing/resource_tracker.py:279: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
(EngineCore_DP5 pid=428) Process EngineCore_DP5:
(EngineCore_DP5 pid=428) Traceback (most recent call last):
(EngineCore_DP5 pid=428)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 208, in _init_executor
(EngineCore_DP5 pid=428)     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_DP5 pid=428)                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP5 pid=428)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 750, in wait_for_ready
(EngineCore_DP5 pid=428)     raise e from None
(EngineCore_DP5 pid=428) Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
(EngineCore_DP5 pid=428) 
(EngineCore_DP5 pid=428) During handling of the above exception, another exception occurred:
(EngineCore_DP5 pid=428) 
(EngineCore_DP5 pid=428) Traceback (most recent call last):
(EngineCore_DP5 pid=428)   File "/usr/lib64/python3.12/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP5 pid=428)     self.run()
(EngineCore_DP5 pid=428)   File "/usr/lib64/python3.12/multiprocessing/process.py", line 108, in run
(EngineCore_DP5 pid=428)     self._target(*self._args, **self._kwargs)
(EngineCore_DP5 pid=428)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 1074, in run_engine_core
(EngineCore_DP5 pid=428)     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_DP5 pid=428)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP5 pid=428)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 1609, in __init__
(EngineCore_DP5 pid=428)     super().__init__(
(EngineCore_DP5 pid=428)   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore_DP5 pid=428)     return func(*args, **kwargs)
(EngineCore_DP5 pid=428)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP5 pid=428)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 848, in __init__
(EngineCore_DP5 pid=428)     super().__init__(
(EngineCore_DP5 pid=428)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 114, in __init__
(EngineCore_DP5 pid=428)     self.model_executor = executor_class(vllm_config)
(EngineCore_DP5 pid=428)                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP5 pid=428)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 105, in __init__
(EngineCore_DP5 pid=428)     super().__init__(vllm_config)
(EngineCore_DP5 pid=428)   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore_DP5 pid=428)     return func(*args, **kwargs)
(EngineCore_DP5 pid=428)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP5 pid=428)   File "/opt/vllm-source/vllm/v1/executor/abstract.py", line 109, in __init__
(EngineCore_DP5 pid=428)     self._init_executor()
(EngineCore_DP5 pid=428)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 252, in _init_executor
(EngineCore_DP5 pid=428)     self._ensure_worker_termination([uw.proc for uw in unready_workers])
(EngineCore_DP5 pid=428)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 434, in _ensure_worker_termination
(EngineCore_DP5 pid=428)     if wait_for_termination(active_procs(), 4):
(EngineCore_DP5 pid=428)        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP5 pid=428)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 428, in wait_for_termination
(EngineCore_DP5 pid=428)     time.sleep(0.1)
(EngineCore_DP5 pid=428)   File "/opt/vllm-source/vllm/entrypoints/openai/api_server.py", line 570, in signal_handler
(EngineCore_DP5 pid=428)     raise KeyboardInterrupt("terminated")
(EngineCore_DP5 pid=428) KeyboardInterrupt: terminated
/usr/lib64/python3.12/multiprocessing/resource_tracker.py:279: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
(EngineCore_DP4 pid=425) Process EngineCore_DP4:
(EngineCore_DP4 pid=425) Traceback (most recent call last):
(EngineCore_DP4 pid=425)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 208, in _init_executor
(EngineCore_DP4 pid=425)     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_DP4 pid=425)                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP4 pid=425)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 750, in wait_for_ready
(EngineCore_DP4 pid=425)     raise e from None
(EngineCore_DP4 pid=425) Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
(EngineCore_DP4 pid=425) 
(EngineCore_DP4 pid=425) During handling of the above exception, another exception occurred:
(EngineCore_DP4 pid=425) 
(EngineCore_DP4 pid=425) Traceback (most recent call last):
(EngineCore_DP4 pid=425)   File "/usr/lib64/python3.12/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP4 pid=425)     self.run()
(EngineCore_DP4 pid=425)   File "/usr/lib64/python3.12/multiprocessing/process.py", line 108, in run
(EngineCore_DP4 pid=425)     self._target(*self._args, **self._kwargs)
(EngineCore_DP4 pid=425)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 1074, in run_engine_core
(EngineCore_DP4 pid=425)     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_DP4 pid=425)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP4 pid=425)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 1609, in __init__
(EngineCore_DP4 pid=425)     super().__init__(
(EngineCore_DP4 pid=425)   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore_DP4 pid=425)     return func(*args, **kwargs)
(EngineCore_DP4 pid=425)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP4 pid=425)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 848, in __init__
(EngineCore_DP4 pid=425)     super().__init__(
(EngineCore_DP4 pid=425)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 114, in __init__
(EngineCore_DP4 pid=425)     self.model_executor = executor_class(vllm_config)
(EngineCore_DP4 pid=425)                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP4 pid=425)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 105, in __init__
(EngineCore_DP4 pid=425)     super().__init__(vllm_config)
(EngineCore_DP4 pid=425)   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore_DP4 pid=425)     return func(*args, **kwargs)
(EngineCore_DP4 pid=425)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP4 pid=425)   File "/opt/vllm-source/vllm/v1/executor/abstract.py", line 109, in __init__
(EngineCore_DP4 pid=425)     self._init_executor()
(EngineCore_DP4 pid=425)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 252, in _init_executor
(EngineCore_DP4 pid=425)     self._ensure_worker_termination([uw.proc for uw in unready_workers])
(EngineCore_DP4 pid=425)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 434, in _ensure_worker_termination
(EngineCore_DP4 pid=425)     if wait_for_termination(active_procs(), 4):
(EngineCore_DP4 pid=425)        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP4 pid=425)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 428, in wait_for_termination
(EngineCore_DP4 pid=425)     time.sleep(0.1)
(EngineCore_DP4 pid=425)   File "/opt/vllm-source/vllm/entrypoints/openai/api_server.py", line 570, in signal_handler
(EngineCore_DP4 pid=425)     raise KeyboardInterrupt("terminated")
(EngineCore_DP4 pid=425) KeyboardInterrupt: terminated
/usr/lib64/python3.12/multiprocessing/resource_tracker.py:279: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
(EngineCore_DP7 pid=434) Process EngineCore_DP7:
(EngineCore_DP7 pid=434) Traceback (most recent call last):
(EngineCore_DP7 pid=434)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 208, in _init_executor
(EngineCore_DP7 pid=434)     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_DP7 pid=434)                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP7 pid=434)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 750, in wait_for_ready
(EngineCore_DP7 pid=434)     raise e from None
(EngineCore_DP7 pid=434) Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
(EngineCore_DP7 pid=434) 
(EngineCore_DP7 pid=434) During handling of the above exception, another exception occurred:
(EngineCore_DP7 pid=434) 
(EngineCore_DP7 pid=434) Traceback (most recent call last):
(EngineCore_DP7 pid=434)   File "/usr/lib64/python3.12/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP7 pid=434)     self.run()
(EngineCore_DP7 pid=434)   File "/usr/lib64/python3.12/multiprocessing/process.py", line 108, in run
(EngineCore_DP7 pid=434)     self._target(*self._args, **self._kwargs)
(EngineCore_DP7 pid=434)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 1074, in run_engine_core
(EngineCore_DP7 pid=434)     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_DP7 pid=434)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP7 pid=434)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 1609, in __init__
(EngineCore_DP7 pid=434)     super().__init__(
(EngineCore_DP7 pid=434)   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore_DP7 pid=434)     return func(*args, **kwargs)
(EngineCore_DP7 pid=434)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP7 pid=434)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 848, in __init__
(EngineCore_DP7 pid=434)     super().__init__(
(EngineCore_DP7 pid=434)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 114, in __init__
(EngineCore_DP7 pid=434)     self.model_executor = executor_class(vllm_config)
(EngineCore_DP7 pid=434)                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP7 pid=434)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 105, in __init__
(EngineCore_DP7 pid=434)     super().__init__(vllm_config)
(EngineCore_DP7 pid=434)   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore_DP7 pid=434)     return func(*args, **kwargs)
(EngineCore_DP7 pid=434)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP7 pid=434)   File "/opt/vllm-source/vllm/v1/executor/abstract.py", line 109, in __init__
(EngineCore_DP7 pid=434)     self._init_executor()
(EngineCore_DP7 pid=434)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 252, in _init_executor
(EngineCore_DP7 pid=434)     self._ensure_worker_termination([uw.proc for uw in unready_workers])
(EngineCore_DP7 pid=434)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 434, in _ensure_worker_termination
(EngineCore_DP7 pid=434)     if wait_for_termination(active_procs(), 4):
(EngineCore_DP7 pid=434)        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP7 pid=434)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 428, in wait_for_termination
(EngineCore_DP7 pid=434)     time.sleep(0.1)
(EngineCore_DP7 pid=434)   File "/opt/vllm-source/vllm/entrypoints/openai/api_server.py", line 570, in signal_handler
(EngineCore_DP7 pid=434)     raise KeyboardInterrupt("terminated")
(EngineCore_DP7 pid=434) KeyboardInterrupt: terminated
/usr/lib64/python3.12/multiprocessing/resource_tracker.py:279: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
(EngineCore_DP0 pid=415) Process EngineCore_DP0:
(EngineCore_DP0 pid=415) Traceback (most recent call last):
(EngineCore_DP0 pid=415)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 208, in _init_executor
(EngineCore_DP0 pid=415)     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_DP0 pid=415)                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=415)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 750, in wait_for_ready
(EngineCore_DP0 pid=415)     raise e from None
(EngineCore_DP0 pid=415) Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
(EngineCore_DP0 pid=415) 
(EngineCore_DP0 pid=415) During handling of the above exception, another exception occurred:
(EngineCore_DP0 pid=415) 
(EngineCore_DP0 pid=415) Traceback (most recent call last):
(EngineCore_DP0 pid=415)   File "/usr/lib64/python3.12/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP0 pid=415)     self.run()
(EngineCore_DP0 pid=415)   File "/usr/lib64/python3.12/multiprocessing/process.py", line 108, in run
(EngineCore_DP0 pid=415)     self._target(*self._args, **self._kwargs)
(EngineCore_DP0 pid=415)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 1074, in run_engine_core
(EngineCore_DP0 pid=415)     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=415)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=415)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 1609, in __init__
(EngineCore_DP0 pid=415)     super().__init__(
(EngineCore_DP0 pid=415)   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore_DP0 pid=415)     return func(*args, **kwargs)
(EngineCore_DP0 pid=415)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=415)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 848, in __init__
(EngineCore_DP0 pid=415)     super().__init__(
(EngineCore_DP0 pid=415)   File "/opt/vllm-source/vllm/v1/engine/core.py", line 114, in __init__
(EngineCore_DP0 pid=415)     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=415)                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=415)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 105, in __init__
(EngineCore_DP0 pid=415)     super().__init__(vllm_config)
(EngineCore_DP0 pid=415)   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore_DP0 pid=415)     return func(*args, **kwargs)
(EngineCore_DP0 pid=415)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=415)   File "/opt/vllm-source/vllm/v1/executor/abstract.py", line 109, in __init__
(EngineCore_DP0 pid=415)     self._init_executor()
(EngineCore_DP0 pid=415)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 252, in _init_executor
(EngineCore_DP0 pid=415)     self._ensure_worker_termination([uw.proc for uw in unready_workers])
(EngineCore_DP0 pid=415)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 434, in _ensure_worker_termination
(EngineCore_DP0 pid=415)     if wait_for_termination(active_procs(), 4):
(EngineCore_DP0 pid=415)        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=415)   File "/opt/vllm-source/vllm/v1/executor/multiproc_executor.py", line 428, in wait_for_termination
(EngineCore_DP0 pid=415)     time.sleep(0.1)
(EngineCore_DP0 pid=415)   File "/opt/vllm-source/vllm/entrypoints/openai/api_server.py", line 570, in signal_handler
(EngineCore_DP0 pid=415)     raise KeyboardInterrupt("terminated")
(EngineCore_DP0 pid=415) KeyboardInterrupt: terminated
(APIServer pid=8) INFO 04-11 14:50:00 [coordinator.py:189] DP Coordinator process exiting
/usr/lib64/python3.12/multiprocessing/resource_tracker.py:279: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
(APIServer pid=8) Traceback (most recent call last):
(APIServer pid=8)   File "<frozen runpy>", line 198, in _run_module_as_main
(APIServer pid=8)   File "<frozen runpy>", line 88, in _run_code
(APIServer pid=8)   File "/opt/vllm-source/vllm/entrypoints/openai/api_server.py", line 724, in <module>
(APIServer pid=8)     uvloop.run(run_server(args))
(APIServer pid=8)   File "/opt/vllm/lib64/python3.12/site-packages/uvloop/__init__.py", line 96, in run
(APIServer pid=8)     return __asyncio.run(
(APIServer pid=8)            ^^^^^^^^^^^^^^
(APIServer pid=8)   File "/usr/lib64/python3.12/asyncio/runners.py", line 195, in run
(APIServer pid=8)     return runner.run(main)
(APIServer pid=8)            ^^^^^^^^^^^^^^^^
(APIServer pid=8)   File "/usr/lib64/python3.12/asyncio/runners.py", line 118, in run
(APIServer pid=8)     return self._loop.run_until_complete(task)
(APIServer pid=8)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=8)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=8)   File "/opt/vllm/lib64/python3.12/site-packages/uvloop/__init__.py", line 48, in wrapper
(APIServer pid=8)     return await main
(APIServer pid=8)            ^^^^^^^^^^
(APIServer pid=8)   File "/opt/vllm-source/vllm/entrypoints/openai/api_server.py", line 684, in run_server
(APIServer pid=8)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=8)   File "/opt/vllm-source/vllm/entrypoints/openai/api_server.py", line 698, in run_server_worker
(APIServer pid=8)     async with build_async_engine_client(
(APIServer pid=8)                ^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=8)   File "/usr/lib64/python3.12/contextlib.py", line 210, in __aenter__
(APIServer pid=8)     return await anext(self.gen)
(APIServer pid=8)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=8)   File "/opt/vllm-source/vllm/entrypoints/openai/api_server.py", line 100, in build_async_engine_client
(APIServer pid=8)     async with build_async_engine_client_from_engine_args(
(APIServer pid=8)                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=8)   File "/usr/lib64/python3.12/contextlib.py", line 210, in __aenter__
(APIServer pid=8)     return await anext(self.gen)
(APIServer pid=8)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=8)   File "/opt/vllm-source/vllm/entrypoints/openai/api_server.py", line 136, in build_async_engine_client_from_engine_args
(APIServer pid=8)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=8)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=8)   File "/opt/vllm-source/vllm/v1/engine/async_llm.py", line 225, in from_vllm_config
(APIServer pid=8)     return cls(
(APIServer pid=8)            ^^^^
(APIServer pid=8)   File "/opt/vllm-source/vllm/v1/engine/async_llm.py", line 154, in __init__
(APIServer pid=8)     self.engine_core = EngineCoreClient.make_async_mp_client(
(APIServer pid=8)                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=8)   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(APIServer pid=8)     return func(*args, **kwargs)
(APIServer pid=8)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=8)   File "/opt/vllm-source/vllm/v1/engine/core_client.py", line 128, in make_async_mp_client
(APIServer pid=8)     return DPLBAsyncMPClient(*client_args)
(APIServer pid=8)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=8)   File "/opt/vllm-source/vllm/v1/engine/core_client.py", line 1307, in __init__
(APIServer pid=8)     super().__init__(
(APIServer pid=8)   File "/opt/vllm-source/vllm/v1/engine/core_client.py", line 1124, in __init__
(APIServer pid=8)     super().__init__(
(APIServer pid=8)   File "/opt/vllm-source/vllm/tracing/otel.py", line 178, in sync_wrapper
(APIServer pid=8)     return func(*args, **kwargs)
(APIServer pid=8)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=8)   File "/opt/vllm-source/vllm/v1/engine/core_client.py", line 872, in __init__
(APIServer pid=8)     super().__init__(
(APIServer pid=8)   File "/opt/vllm-source/vllm/v1/engine/core_client.py", line 534, in __init__
(APIServer pid=8)     with launch_core_engines(
(APIServer pid=8)          ^^^^^^^^^^^^^^^^^^^^
(APIServer pid=8)   File "/usr/lib64/python3.12/contextlib.py", line 144, in __exit__
(APIServer pid=8)     next(self.gen)
(APIServer pid=8)   File "/opt/vllm-source/vllm/v1/engine/utils.py", line 1073, in launch_core_engines
(APIServer pid=8)     wait_for_engine_startup(
(APIServer pid=8)   File "/opt/vllm-source/vllm/v1/engine/utils.py", line 1132, in wait_for_engine_startup
(APIServer pid=8)     raise RuntimeError(
(APIServer pid=8) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {'EngineCore_DP1': 1}
=== FAIL: vLLM process died during startup ===
=== Dumping JIT cache state ===
/tmp/deep_gemm_cache/locks/kernel.sm90_fp8_gemm_1d2d.371756703f6a0c121d20ad6a4d46139e.lock
/tmp/deep_gemm_cache/cache/kernel.sm90_fp8_gemm_1d2d.371756703f6a0c121d20ad6a4d46139e/kernel.cu
/tmp/deep_gemm_cache/cache/kernel.sm90_fp8_gemm_1d2d.371756703f6a0c121d20ad6a4d46139e/kernel.cubin
total 0
drwxr-xr-x 2 vllm root 85 Apr 11 14:49 .
drwxr-xr-x 5 vllm root 59 Apr 11 14:49 ..
-rw-r--r-- 1 vllm root  0 Apr 11 14:49 kernel.sm90_fp8_gemm_1d2d.371756703f6a0c121d20ad6a4d46139e.lock
```

Also I was able to account for purging the cache, see comments in #302 
