# [Issue #43] Met error when distributed training

source: https://github.com/Ascend/pytorch/issues/43
state: open | updated: 2024-07-24T07:59:56Z
labels: 

## 正文

worker-1:   File "loader.py", line 163, in get_dataset
worker-1:     with training_args.main_process_first(desc="pre-process dataset"):
worker-1:   File "/usr/local/python3.10.12/lib/python3.10/contextlib.py", line 142, in __exit__
worker-1:     next(self.gen)
worker-1:   File "/usr/local/python3.10.12/lib/python3.10/site-packages/transformers/training_args.py", line 2363, in main_process_first
worker-1:     dist.barrier()
worker-1:   File "/usr/local/python3.10.12/lib/python3.10/site-packages/torch/distributed/c10d_logger.py", line 47, in wrapper
worker-1:     return func(*args, **kwargs)
worker-1:   File "/usr/local/python3.10.12/lib/python3.10/site-packages/torch/distributed/distributed_c10d.py", line 3703, in barrier
worker-1:     work.wait()
worker-1: RuntimeError: npuSynchronizeDevice:torch_npu/csrc/core/npu/NPUStream.cpp:363 NPU error, error code is 107020
worker-1: [ERROR] 2024-07-03-11:28:40 (PID:639, Device:0, RankID:16) ERR00100 PTA call acl api failed.
worker-1: EI9999: Inner Error!
worker-1: EI9999: 2024-07-03-11:28:40.419.527  The error from device(chipId:0, dieId:0), serial number is 1, hccl fftsplus task timeout occurred during task execution, stream_id:4, sq_id:4, task_id:5, stuck notify num:7, timeout:1836.[FUNC:ProcessStarsHcclFftsPlusTimeoutErrorInfo][FILE:device_error_proc.cc][LINE:1389]
worker-1:         TraceBack (most recent call last):
worker-1:         The 0 stuck notify wait context info:(context_id=2, notify_id=7).[FUNC:ProcessStarsHcclFftsPlusTimeoutErrorInfo][FILE:device_error_proc.cc][LINE:1396]
worker-1:         The 1 stuck notify wait context info:(context_id=4, notify_id=9).[FUNC:ProcessStarsHcclFftsPlusTimeoutErrorInfo][FILE:device_error_proc.cc][LINE:1396]
worker-1:         The 2 stuck notify wait context info:(context_id=6, notify_id=17).[FUNC:ProcessStarsHcclFftsPlusTimeoutErrorInfo][FILE:device_error_proc.cc][LINE:1396]
worker-1:         The 3 stuck notify wait context info:(context_id=8, notify_id=11).[FUNC:ProcessStarsHcclFftsPlusTimeoutErrorInfo][FILE:device_error_proc.cc][LINE:1396]
worker-1:         The 4 stuck notify wait context info:(context_id=10, notify_id=16).[FUNC:ProcessStarsHcclFftsPlusTimeoutErrorInfo][FILE:device_error_proc.cc][LINE:1396]
worker-1:         The 5 stuck notify wait context info:(context_id=12, notify_id=14).[FUNC:ProcessStarsHcclFftsPlusTimeoutErrorInfo][FILE:device_error_proc.cc][LINE:1396]
worker-1:         The 6 stuck notify wait context info:(context_id=14, notify_id=19).[FUNC:ProcessStarsHcclFftsPlusTimeoutErrorInfo][FILE:device_error_proc.cc][LINE:1396]
worker-1:         The error from device(chipId:0, dieId:0), serial number is 2, event wait timeout occurred during task execution, stream_id:2, sq_id:2, task_id:5, event_id=3, timeout=1868.[FUNC:ProcessStarsWaitTimeoutErrorInfo][FILE:device_error_proc.cc][LINE:1344]
worker-1:         Task execute failed, device_id=0, stream_id=2, task_id=5, flip_num=0, task_type=3(EVENT_WAIT).[FUNC:GetError][FILE:stream.cc][LINE:1512]
worker-1:         fftsplus task execute failed, dev_id=0, stream_id=4, task_id=5, context_id=2, thread_id=0, err_type=13[hccl fftsplus timeout][FUNC:GetError][FILE:stream.cc][LINE:1512]
worker-1:         fftsplus task execute failed, dev_id=0, stream_id=4, task_id=5, context_id=4, thread_id=0, err_type=13[hccl fftsplus timeout][FUNC:GetError][FILE:stream.cc][LINE:1512]
worker-1:         fftsplus task execute failed, dev_id=0, stream_id=4, task_id=5, context_id=6, thread_id=0, err_type=13[hccl fftsplus timeout][FUNC:GetError][FILE:stream.cc][LINE:1512]
worker-1:         fftsplus task execute failed, dev_id=0, stream_id=4, task_id=5, context_id=8, thread_id=0, err_type=13[hccl fftsplus timeout][FUNC:GetError][FILE:stream.cc][LINE:1512]
worker-1:         fftsplus task execute failed, dev_id=0, stream_id=4, task_id=5, context_id=10, thread_id=0, err_type=13[hccl fftsplus timeout][FUNC:GetError][FILE:stream.cc][LINE:1512]
worker-1:         fftsplus task execute failed, dev_id=0, stream_id=4, task_id=5, context_id=12, thread_id=0, err_type=13[hccl fftsplus timeout][FUNC:GetError][FILE:stream.cc][LINE:1512]
worker-1:         fftsplus task execute failed, dev_id=0, stream_id=4, task_id=5, context_id=14, thread_id=0, err_type=13[hccl fftsplus timeout][FUNC:GetError][FILE:stream.cc][LINE:1512]
worker-1:         rtDeviceSynchronize execute failed, reason=[task timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
worker-1:         wait for compute device to finish failed, runtime result = 107020.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
worker-1: 
worker-1: [W NPUStream.cpp:382] Warning: NPU warning, error code is 107020[Error]: .
worker-1: EH9999: Inner Error!
worker-1:         rtDeviceSynchronize execute failed, reason=[task timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
worker-1: EH9999: 2024-07-03-11:28:40.447.909  wait for compute device to finish failed, runtime result = 107020.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
worker-1:         TraceBack (most recent call last):
worker-1:  (function npuSynchronizeUsedDevices)
worker-1: [W NPUStream.cpp:365] Warning: NPU warning, error code is 107020[Error]: .
worker-1: EH9999: Inner Error!
worker-1:         rtDeviceSynchronize execute failed, reason=[task timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
worker-1: EH9999: 2024-07-03-11:28:40.449.765  wait for compute device to finish failed, runtime result = 107020.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
worker-1:         TraceBack (most recent call last):
worker-1:  (function npuSynchronizeDevice)
worker-1: [W NPUStream.cpp:365] Warning: NPU warning, error code is 107020[Error]: .
worker-1: EH9999: Inner Error!
worker-1:         rtDeviceSynchronize execute failed, reason=[task timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
worker-1: EH9999: 2024-07-03-11:28:40.450.757  wait for compute device to finish failed, runtime result = 107020.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
worker-1:         TraceBack (most recent call last):
worker-1:  (function npuSynchronizeDevice)
worker-1: [W NPUStream.cpp:365] Warning: NPU warning, error code is 107020[Error]: .
worker-1: EH9999: Inner Error!
worker-1:         rtDeviceSynchronize execute failed, reason=[task timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
worker-1: EH9999: 2024-07-03-11:28:40.451.641  wait for compute device to finish failed, runtime result = 107020.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
worker-1:         TraceBack (most recent call last):
worker-1:  (function npuSynchronizeDevice)
worker-1: [W NPUStream.cpp:365] Warning: NPU warning, error code is 107020[Error]: .
worker-1: EH9999: Inner Error!
worker-1:         rtDeviceSynchronize execute failed, reason=[task timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
worker-1: EH9999: 2024-07-03-11:28:40.452.478  wait for compute device to finish failed, runtime result = 107020.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
worker-1:         TraceBack (most recent call last):
worker-1:  (function npuSynchronizeDevice)
worker-1: [W NPUStream.cpp:365] Warning: NPU warning, error code is 107020[Error]: .
worker-1: EH9999: Inner Error!
worker-1:         rtDeviceSynchronize execute failed, reason=[task timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
worker-1: EH9999: 2024-07-03-11:28:40.453.317  wait for compute device to finish failed, runtime result = 107020.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
worker-1:         TraceBack (most recent call last):
worker-1:  (function npuSynchronizeDevice)
worker-1: [W NPUStream.cpp:365] Warning: NPU warning, error code is 107020[Error]: .
worker-1: EH9999: Inner Error!
worker-1:         rtDeviceSynchronize execute failed, reason=[task timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
worker-1: EH9999: 2024-07-03-11:28:40.454.154  wait for compute device to finish failed, runtime result = 107020.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
worker-1:         TraceBack (most recent call last):
worker-1:  (function npuSynchronizeDevice)
worker-1: [W NPUStream.cpp:365] Warning: NPU warning, error code is 107020[Error]: .
worker-1: EH9999: Inner Error!
worker-1:         rtDeviceSynchronize execute failed, reason=[task timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
worker-1: EH9999: 2024-07-03-11:28:40.454.978  wait for compute device to finish failed, runtime result = 107020.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
worker-1:         TraceBack (most recent call last):
worker-1:  (function npuSynchronizeDevice)
worker-1: [W NPUStream.cpp:365] Warning: NPU warning, error code is 107020[Error]: .
worker-1: EH9999: Inner Error!
worker-1:         rtDeviceSynchronize execute failed, reason=[task timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
worker-1: EH9999: 2024-07-03-11:28:40.455.800  wait for compute device to finish failed, runtime result = 107020.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
worker-1:         TraceBack (most recent call last):
worker-1:  (function npuSynchronizeDevice)
worker-1: Inner error, see details in Ascend logs.Inner error, see details in Ascend logs.Inner error, see details in Ascend logs.Inner error, see details in Ascend logs.Inner error, see details in Ascend logs.Inner error, see details in Ascend logs.Inner error, see details in Ascend logs.256



above the error log, anyone know what the problem is? I train a 1.5B model and training data is large to about 100G, and setting streaming=True or False still gets this error. I train on 3 nodes and each 8x910B. 
If I reduce the training data to very little like 5G, this error won't appear. But I need train on more data.

## 评论 (1)

### yunyiyun · 2024-07-24

Try to configure HCCL_EXEC_TIMEOUT to be larger
https://www.hiascend.com/document/detail/zh/canncommercial/80RC2/apiref/envvar/envref_07_0075.html
