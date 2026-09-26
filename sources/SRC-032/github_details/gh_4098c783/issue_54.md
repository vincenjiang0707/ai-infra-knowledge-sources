# [Issue #54] 环境变量设置HCCL_EXEC_TIMEOUT=0不生效

source: https://github.com/Ascend/pytorch/issues/54
state: open | updated: 2026-01-14T03:17:01Z
labels: 

## 正文

我在昇腾910B2 4卡上使用lmdeploy启动Qwen1.5-72B模型，大概模型启动30分钟后服务就挂掉，查看可能和HCCL_EXEC_TIMEOUT有关，我把HCCL_EXEC_TIMEOUT设置成0，但是不生效，30分钟后还是有问题。

**错误日志:**
2024-10-21 10:09:43,821 - lmdeploy - INFO - model_weight_loader.py:152 - rank[2] loading weights - "model-00031-of-00038.safetensors"
2024-10-21 10:09:44,080 - lmdeploy - INFO - model_weight_loader.py:152 - rank[1] loading weights - "model-00016-of-00038.safetensors"
/usr/local/python3.10.5/lib/python3.10/site-packages/torch_npu/distributed/distributed_c10d.py:93: UserWarning: HCCL doesn't support gather at the moment. Implemented with allgather instead.
  warnings.warn("HCCL doesn't support gather at the moment. Implemented with allgather instead.")
HINT:    Please open http://0.0.0.0:23333 in a browser for detailed api usage!!!
HINT:    Please open http://0.0.0.0:23333 in a browser for detailed api usage!!!
HINT:    Please open http://0.0.0.0:23333 in a browser for detailed api usage!!!
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:23333 (Press CTRL+C to quit)
/usr/local/python3.10.5/lib/python3.10/site-packages/torch_npu/utils/storage.py:38: UserWarning: TypedStorage is deprecated. It will be removed in the future and UntypedStorage will be the only storage class. This should only matter to you if you are using storages directly.  To access UntypedStorage directly, use tensor.untyped_storage() instead of tensor.storage()
  if self.device.type != 'cpu':
('Warning: torch.save with "_use_new_zipfile_serialization = False" is not recommended for npu tensor, which may bring unexpected errors and hopefully set "_use_new_zipfile_serialization = True"', 'if it is necessary to use this, please convert the npu tensor to cpu tensor for saving')
/opt/lmdeploy/lmdeploy/pytorch/engine/logits_process.py:333: UserWarning: AutoNonVariableTypeMode is deprecated and will be removed in 1.10 release. For kernel implementations please use AutoDispatchBelowADInplaceOrView instead, If you are looking for a user facing API to enable running your inference-only workload, please use c10::InferenceMode. Using AutoDispatchBelowADInplaceOrView in user code is under risk of producing silent wrong result in some edge cases. See Note [AutoDispatchBelowAutograd] for more details. (Triggered internally at build/CMakeFiles/torch_npu.dir/compiler_depend.ts:74.)
  stop_words = torch.where(self.ignore_eos[:, None], stop_words, -1)
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:671: ImportWarning: TEMetaPathLoader.exec_module() not found; falling back to load_module()
INFO:     10.17.2.84:39286 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO:     10.17.2.84:57256 - "POST /v1/chat/completions HTTP/1.1" 200 OK
EI9999: Inner Error!
EI9999: 2024-10-21-10:42:00.204.495  The error from device(chipId:2, dieId:0), serial number is 9, hccl fftsplus task timeout occurred during task execution, stream_id:5, sq_id:5, task_id:38827, stuck notify num:1, timeout:30min(default).[FUNC:ProcessStarsHcclFftsPlusTimeoutErrorInfo][FILE:device_error_proc.cc][LINE:1435]
        TraceBack (most recent call last):
        The 0 stuck notify wait context info:(context_id=1, notify_id=16).[FUNC:ProcessStarsHcclFftsPlusTimeoutErrorInfo][FILE:device_error_proc.cc][LINE:1449]
        The error from device(chipId:2, dieId:0), serial number is 10, event wait timeout occurred during task execution, stream_id:4, sq_id:4, task_id:42015, event_id=970, timeout=1868.[FUNC:ProcessStarsWaitTimeoutErrorInfo][FILE:device_error_proc.cc][LINE:1395]
        Task execute failed, device_id=2, stream_id=4, task_id=42015, flip_num=3, task_type=3(EVENT_WAIT).[FUNC:GetError][FILE:stream.cc][LINE:1082]
        rtStreamSynchronizeWithTimeout execute failed, reason=[task timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
        synchronize stream failed, runtime result = 107020[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]

2024-10-21 10:42:00,218 - lmdeploy - ERROR - model_agent.py:489 - Rank[2] failed.
Traceback (most recent call last):
  File "/opt/lmdeploy/lmdeploy/pytorch/engine/model_agent.py", line 486, in _start_tp_process
    func(rank, *args, **kwargs)
  File "/opt/lmdeploy/lmdeploy/pytorch/engine/model_agent.py", line 439, in _tp_model_loop
    inputs, swap_in_map, swap_out_map, exit_flag = _broadcast_inputs(
  File "/opt/lmdeploy/lmdeploy/pytorch/engine/model_agent.py", line 404, in _broadcast_inputs
    dist.broadcast_object_list(inputs)
  File "/usr/local/python3.10.5/lib/python3.10/site-packages/torch/distributed/c10d_logger.py", line 47, in wrapper
    return func(*args, **kwargs)
  File "/usr/local/python3.10.5/lib/python3.10/site-packages/torch/distributed/distributed_c10d.py", line 2615, in broadcast_object_list
    torch.sum(object_sizes_tensor).item(),  # type: ignore[arg-type]
RuntimeError: ACL stream synchronize failed.
EI9999: Inner Error!
EI9999: 2024-10-21-10:42:00.358.410  The error from device(chipId:3, dieId:0), serial number is 9, hccl fftsplus task timeout occurred during task execution, stream_id:5, sq_id:5, task_id:38827, stuck notify num:1, timeout:30min(default).[FUNC:ProcessStarsHcclFftsPlusTimeoutErrorInfo][FILE:device_error_proc.cc][LINE:1435]
        TraceBack (most recent call last):
        The 0 stuck notify wait context info:(context_id=1, notify_id=9).[FUNC:ProcessStarsHcclFftsPlusTimeoutErrorInfo][FILE:device_error_proc.cc][LINE:1449]
        The error from device(chipId:3, dieId:0), serial number is 10, event wait timeout occurred during task execution, stream_id:4, sq_id:4, task_id:42015, event_id=970, timeout=1868.[FUNC:ProcessStarsWaitTimeoutErrorInfo][FILE:device_error_proc.cc][LINE:1395]
        Task execute failed, device_id=3, stream_id=4, task_id=42015, flip_num=3, task_type=3(EVENT_WAIT).[FUNC:GetError][FILE:stream.cc][LINE:1082]
        rtStreamSynchronizeWithTimeout execute failed, reason=[task timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
        synchronize stream failed, runtime result = 107020[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]

2024-10-21 10:42:00,372 - lmdeploy - ERROR - model_agent.py:489 - Rank[3] failed.
Traceback (most recent call last):
  File "/opt/lmdeploy/lmdeploy/pytorch/engine/model_agent.py", line 486, in _start_tp_process
    func(rank, *args, **kwargs)
  File "/opt/lmdeploy/lmdeploy/pytorch/engine/model_agent.py", line 439, in _tp_model_loop
    inputs, swap_in_map, swap_out_map, exit_flag = _broadcast_inputs(
  File "/opt/lmdeploy/lmdeploy/pytorch/engine/model_agent.py", line 404, in _broadcast_inputs
    dist.broadcast_object_list(inputs)
  File "/usr/local/python3.10.5/lib/python3.10/site-packages/torch/distributed/c10d_logger.py", line 47, in wrapper
    return func(*args, **kwargs)
  File "/usr/local/python3.10.5/lib/python3.10/site-packages/torch/distributed/distributed_c10d.py", line 2615, in broadcast_object_list
    torch.sum(object_sizes_tensor).item(),  # type: ignore[arg-type]
RuntimeError: ACL stream synchronize failed.
EI9999: Inner Error!
EI9999: 2024-10-21-10:42:00.428.572  The error from device(chipId:1, dieId:0), serial number is 9, hccl fftsplus task timeout occurred during task execution, stream_id:5, sq_id:5, task_id:38827, stuck notify num:1, timeout:30min(default).[FUNC:ProcessStarsHcclFftsPlusTimeoutErrorInfo][FILE:device_error_proc.cc][LINE:1435]
        TraceBack (most recent call last):
        The 0 stuck notify wait context info:(context_id=1, notify_id=10).[FUNC:ProcessStarsHcclFftsPlusTimeoutErrorInfo][FILE:device_error_proc.cc][LINE:1449]
        The error from device(chipId:1, dieId:0), serial number is 10, event wait timeout occurred during task execution, stream_id:4, sq_id:4, task_id:42015, event_id=970, timeout=1868.[FUNC:ProcessStarsWaitTimeoutErrorInfo][FILE:device_error_proc.cc][LINE:1395]
        Task execute failed, device_id=1, stream_id=4, task_id=42015, flip_num=3, task_type=3(EVENT_WAIT).[FUNC:GetError][FILE:stream.cc][LINE:1082]
        rtStreamSynchronizeWithTimeout execute failed, reason=[task timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
        synchronize stream failed, runtime result = 107020[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]

2024-10-21 10:42:00,443 - lmdeploy - ERROR - model_agent.py:489 - Rank[1] failed.
Traceback (most recent call last):
  File "/opt/lmdeploy/lmdeploy/pytorch/engine/model_agent.py", line 486, in _start_tp_process
    func(rank, *args, **kwargs)
  File "/opt/lmdeploy/lmdeploy/pytorch/engine/model_agent.py", line 439, in _tp_model_loop
    inputs, swap_in_map, swap_out_map, exit_flag = _broadcast_inputs(
  File "/opt/lmdeploy/lmdeploy/pytorch/engine/model_agent.py", line 404, in _broadcast_inputs
    dist.broadcast_object_list(inputs)
  File "/usr/local/python3.10.5/lib/python3.10/site-packages/torch/distributed/c10d_logger.py", line 47, in wrapper
    return func(*args, **kwargs)
  File "/usr/local/python3.10.5/lib/python3.10/site-packages/torch/distributed/distributed_c10d.py", line 2615, in broadcast_object_list
    torch.sum(object_sizes_tensor).item(),  # type: ignore[arg-type]
RuntimeError: ACL stream synchronize failed.

## 评论 (2)

### yunyiyun · 2024-12-18

HCCL_EXEC_TIMEOUT配置时请配置大于0的数据，如果配置成0依旧是默认时间

### baihongyu19 · 2026-01-14

这个问题解决了吗？我也出现了
