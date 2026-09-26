# [Issue #34] 训练成功，但是推理服务报错

source: https://github.com/Ascend/pytorch/issues/34
state: open | updated: 2025-10-14T06:29:30Z
labels: 

## 正文

torch-npu  2.2 版本。模型llama 7b 
[ma-user LLaMA-Factory]$npu-smi info
+------------------------------------------------------------------------------------------------+
| npu-smi 23.0.rc2                 Version: 23.0.rc2                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B                | OK            | 70.8        36                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           2187 / 15137      1    / 32768         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 0                                                            |
+===========================+===============+====================================================+

packages/transformers/generation/logits_process.py:1591: UserWarning: AutoNonVariableTypeMode is deprecated and will be removed in 1.10 release. For kernel implementations please use AutoDispatchBelowADInplaceOrView instead, If you are looking for a user facing API to enable running your inference-only workload, please use c10::InferenceMode. Using AutoDispatchBelowADInplaceOrView in user code is under risk of producing silent wrong result in some edge cases. See Note [AutoDispatchBelowAutograd] for more details. (Triggered internally at torch_npu/csrc/aten/common/TensorFactories.cpp:74.)
scores_processed = torch.where(scores != scores, 0.0, scores)
E39999: Inner Error!
E39999: 2024-05-21-12:06:49.978.985 An exception occurred during AICPU execution, stream_id:56, task_id:3319, errcode:21008, msg:inner error[FUNC:ProcessAicpuErrorInfo][FILE:device_error_proc.cc][LINE:730]
TraceBack (most recent call last):
Kernel task happen error, retCode=0x2a, [aicpu exception].[FUNC:PreCheckTaskErr][FILE:task_info.cc][LINE:1776]
Aicpu kernel execute failed, device_id=0, stream_id=56, task_id=3319, errorCode=2a.[FUNC:PrintAicpuErrorInfo][FILE:task_info.cc][LINE:1579]
Aicpu kernel execute failed, device_id=0, stream_id=56, task_id=3319, fault op_name=[FUNC:GetError][FILE:stream.cc][LINE:1512]
rtStreamSynchronize execute failed, reason=[aicpu exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
synchronize stream failed, runtime result = 507018[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]

DEVICE[0] PID[308274]:
EXCEPTION TASK:
Exception info:TGID=2533077, model id=65535, stream id=56, stream phase=3, task id=3319, task type=aicpu kernel, recently received task id=3323, recently send task id=3318, task phase=RUN
Message info[0]:aicpu=0,slot_id=0,report_mailbox_flag=0x5a5a5a5a,state=0x5210
Other info[0]:time=2024-05-21-12:06:49.250.837, function=proc_aicpu_task_done, line=970, error code=0x2a
Exception in thread Thread-8:
Traceback (most recent call last):
File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/threading.py", line 980, in _bootstrap_inner
self.run()
File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/threading.py", line 917, in run
self._target(*self._args, **self._kwargs)
File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context
return func(*args, **kwargs)
File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/transformers/generation/utils.py", line 1736, in generate
result = self._sample(
File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/transformers/generation/utils.py", line 2426, in _sample
streamer.put(next_tokens.cpu())
RuntimeError: ACL stream synchronize failed, error code:507018

## 评论 (4)

### yunyiyun · 2024-05-23

模型问题可以在这个仓提问 https://gitee.com/ascend/ModelLink

### yhfgyyf · 2024-06-14

> torch-npu 2.2 版本。模型llama 7b [ma-user LLaMA-Factory]$npu-smi info +------------------------------------------------------------------------------------------------+ | npu-smi 23.0.rc2 Version: 23.0.rc2 | +---------------------------+---------------+----------------------------------------------------+ | NPU Name | Health | Power(W) Temp(C) Hugepages-Usage(page)| | Chip | Bus-Id | AICore(%) Memory-Usage(MB) HBM-Usage(MB) | +===========================+===============+====================================================+ | 0 910B | OK | 70.8 36 0 / 0 | | 0 | 0000:C1:00.0 | 0 2187 / 15137 1 / 32768 | +===========================+===============+====================================================+ +---------------------------+---------------+----------------------------------------------------+ | NPU Chip | Process id | Process name | Process memory(MB) | +===========================+===============+====================================================+ | No running processes found in NPU 0 | +===========================+===============+====================================================+
> 
> packages/transformers/generation/logits_process.py:1591: UserWarning: AutoNonVariableTypeMode is deprecated and will be removed in 1.10 release. For kernel implementations please use AutoDispatchBelowADInplaceOrView instead, If you are looking for a user facing API to enable running your inference-only workload, please use c10::InferenceMode. Using AutoDispatchBelowADInplaceOrView in user code is under risk of producing silent wrong result in some edge cases. See Note [AutoDispatchBelowAutograd] for more details. (Triggered internally at torch_npu/csrc/aten/common/TensorFactories.cpp:74.) scores_processed = torch.where(scores != scores, 0.0, scores) E39999: Inner Error! E39999: 2024-05-21-12:06:49.978.985 An exception occurred during AICPU execution, stream_id:56, task_id:3319, errcode:21008, msg:inner error[FUNC:ProcessAicpuErrorInfo][FILE:device_error_proc.cc][LINE:730] TraceBack (most recent call last): Kernel task happen error, retCode=0x2a, [aicpu exception].[FUNC:PreCheckTaskErr][FILE:task_info.cc][LINE:1776] Aicpu kernel execute failed, device_id=0, stream_id=56, task_id=3319, errorCode=2a.[FUNC:PrintAicpuErrorInfo][FILE:task_info.cc][LINE:1579] Aicpu kernel execute failed, device_id=0, stream_id=56, task_id=3319, fault op_name=[FUNC:GetError][FILE:stream.cc][LINE:1512] rtStreamSynchronize execute failed, reason=[aicpu exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53] synchronize stream failed, runtime result = 507018[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
> 
> DEVICE[0] PID[308274]: EXCEPTION TASK: Exception info:TGID=2533077, model id=65535, stream id=56, stream phase=3, task id=3319, task type=aicpu kernel, recently received task id=3323, recently send task id=3318, task phase=RUN Message info[0]:aicpu=0,slot_id=0,report_mailbox_flag=0x5a5a5a5a,state=0x5210 Other info[0]:time=2024-05-21-12:06:49.250.837, function=proc_aicpu_task_done, line=970, error code=0x2a Exception in thread Thread-8: Traceback (most recent call last): File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/threading.py", line 980, in _bootstrap_inner self.run() File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/threading.py", line 917, in run self._target(*self._args, **self._kwargs) File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs) File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/transformers/generation/utils.py", line 1736, in generate result = self._sample( File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/transformers/generation/utils.py", line 2426, in _sample streamer.put(next_tokens.cpu()) RuntimeError: ACL stream synchronize failed, error code:507018

我也有这个问题，910Apro训练没有问题，推理报错

### Shlysz · 2025-10-03

你好我也有这个问题，最后是怎么解决的

### yunyiyun · 2025-10-14

可以参考资料排查aicpu算子报错
https://www.hiascend.com/document/detail/zh/canncommercial/82RC1/maintenref/troubleshooting/troubleshooting_0151.html
