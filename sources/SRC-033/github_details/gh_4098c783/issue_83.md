# [Issue #83] not support uinit64 yet?

source: https://github.com/Ascend/pytorch/issues/83
state: open | updated: 2025-10-14T06:19:18Z
labels: 

## 正文

when I run Qwen3-Next-80B-A3B-Instruct ,  got error below 
[2025-09-13 05:28:15 TP4] Scheduler hit an exception: Traceback (most recent call last):
  File "/workspace/sglang/python/sglang/srt/managers/scheduler.py", line 2615, in run_scheduler_process
    scheduler = Scheduler(
                ^^^^^^^^^^
  File "/workspace/sglang/python/sglang/srt/managers/scheduler.py", line 333, in __init__
    self.tp_worker = TpWorkerClass(
                     ^^^^^^^^^^^^^^
  File "/workspace/sglang/python/sglang/srt/managers/tp_worker_overlap_thread.py", line 73, in __init__
    self.worker = TpModelWorker(
                  ^^^^^^^^^^^^^^
  File "/workspace/sglang/python/sglang/srt/managers/tp_worker.py", line 96, in __init__
    self.model_runner = ModelRunner(
                        ^^^^^^^^^^^^
  File "/workspace/sglang/python/sglang/srt/model_executor/model_runner.py", line 259, in __init__
    self.initialize(min_per_gpu_memory)
  File "/workspace/sglang/python/sglang/srt/model_executor/model_runner.py", line 388, in initialize
    self.init_memory_pool(
  File "/workspace/sglang/python/sglang/srt/model_executor/model_runner.py", line 1587, in init_memory_pool
    self.token_to_kv_pool = MHATokenToKVPool(
                            ^^^^^^^^^^^^^^^^^
  File "/workspace/sglang/python/sglang/srt/mem_cache/memory_pool.py", line 435, in __init__
    self._create_buffers()
  File "/workspace/sglang/python/sglang/srt/mem_cache/memory_pool.py", line 477, in _create_buffers
    self.data_ptrs = torch.cat([self.k_data_ptrs, self.v_data_ptrs], dim=0)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: cat:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:265 NPU function error: call aclnnCat failed, error code is 161002
[ERROR] 2025-09-13-05:28:15 (PID:55172, Device:4, RankID:-1) ERR00100 PTA call acl api failed.
EZ1001: [PID: 55172] 2025-09-13-05:28:15.526.256 tensor 0 not implemented for DT_UINT64, should be in dtype support list [DT_FLOAT,DT_INT32,DT_INT64,DT_FLOAT16,DT_INT16,DT_INT8,DT_UINT8,DT_DOUBLE,DT_COMPLEX64,DT_BFLOAT16,DT_BOOL,].

ascendd not support uinit64 yet?

## 评论 (1)

### yunyiyun · 2025-10-14

This op dose not support uinit64
https://www.hiascend.com/document/detail/zh/canncommercial/82RC1/API/aolapi/context/aclnnCat.md

