# [Issue #66] RuntimeError: operator():build/CMakeFiles/torch_npu.dir/compiler_depend.ts:25 NPU function error: c10_npu::acl::AclrtSynchronizeStreamWithTimeout(copy_stream)\

source: https://github.com/Ascend/pytorch/issues/66
state: open | updated: 2025-10-09T02:40:00Z
labels: 

## 正文

问题现象：
```
Traceback (most recent call last):
  File "/home/ma-user/work/zhongyunde/test/llama149/testLlame_new.py", line 30, in <module>
    generate_ids = model.generate(inputs.input_ids, max_length=512)
  File "/home/ma-user/work/zhongyunde/source/backup/venv/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
  File "/home/ma-user/work/zhongyunde/source/backup/venv/lib/python3.10/site-packages/transformers/generation/utils.py", line 2026, in generate
    result = self._sample(
  File "/home/ma-user/work/zhongyunde/source/backup/venv/lib/python3.10/site-packages/transformers/generation/utils.py", line 2975, in _sample
    while self._has_unfinished_sequences(
  File "/home/ma-user/work/zhongyunde/source/backup/venv/lib/python3.10/site-packages/transformers/generation/utils.py", line 2210, in _has_unfinished_sequences
    elif this_peer_finished:
RuntimeError: operator():build/CMakeFiles/torch_npu.dir/compiler_depend.ts:25 NPU function error: c10_npu::acl::AclrtSynchronizeStreamWithTimeout(copy_stream), error code is 507035
[ERROR] 2025-04-29-18:46:11 (PID:1066924, Device:1, RankID:-1) ERR00100 PTA call acl api failed
[Error]: The vector core execution is abnormal. 
        Rectify the fault based on the error information in the ascend log.
EZ9999: Inner Error!
EZ9999: [PID: 1066924] 2025-04-29-18:46:11.009.260 The error from device(chipId:5, dieId:0), serial number is 65, there is an aivec error exception, core id is 4, error code = 0x800000, dump info: pc start: 0x1242001e0710, current: 0x1242001e0cec, vec error info: 0x420db1170c, mte error info: 0x8303000434, ifu error info: 0x546b90ee02d80, ccu error info: 0x40e23eed1a000a1b, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x12424040a800.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_proc.cc][LINE:1409]
        TraceBack (most recent call last):
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x3000434, fixp_error1 info: 0x83 fsmId:0, tslot:1, thread:0, ctxid:0, blk:0, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_proc.cc][LINE:1421]
       Kernel task happen error, retCode=0x31, [vector core exception].[FUNC:PreCheckTaskErr][FILE:davinci_kernel_task.cc][LINE:1286]
       AIV Kernel happen error, retCode=0x31.[FUNC:GetError][FILE:stream.cc][LINE:1079]
       Aicore kernel execute failed, device_id=1, stream_id=2, report_stream_id=2, task_id=42, flip_num=0, fault kernel_name=ConcatD_0d745295987e1c668b2ec8b2844aeada_high_performance_3000001, fault kernel info ext=none, program id=53, hash=8442900821206759504.[FUNC:GetError][FILE:stream.cc][LINE:1079]
       [AIC_INFO] after execute:args print end[FUNC:GetError][FILE:stream.cc][LINE:1079]
       rtStreamSynchronizeWithTimeout execute failed, reason=[vector core exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
       synchronize stream failed, runtime result = 507035[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]

[INFO] TORCHAIR [concrete_graph/session.cpp:98] Start to synchronize device in Finalize.
[ERROR] TORCHAIR [concrete_graph/session.cpp:101] ACL synchronize device failed in Finalize, return 507011
[DEBUG] TORCHAIR [concrete_graph/session.cpp:127] After torchair finalize, got context pointer: 0xaaaafee661b0
[W compiler_depend.ts:487] Warning: NPU warning, error code is 507035[Error]: 
[Error]: The vector core execution is abnormal. 
        Rectify the fault based on the error information in the ascend log.
EZ9999: Inner Error!
EZ9999: [PID: 1066924] 2025-04-29-18:46:11.026.847 The error from device(chipId:4, dieId:0), serial number is 53, there is an aivec error exception, core id is 21, error code = 0x800000, dump info: pc start: 0x1240c0020000, current: 0x1240c0020250, vec error info: 0x591615270d, mte error info: 0x800300388e, ifu error info: 0x2124380580800, ccu error info: 0x7dd328ab00000000, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x1240c006a878.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_proc.cc][LINE:1409]
        TraceBack (most recent call last):
       The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x300388e, fixp_error1 info: 0x80 fsmId:0, tslot:3, thread:0, ctxid:0, blk:0, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_proc.cc][LINE:1421]
       Op execute failed. origin_op_name [Greater], op_name [Greater], error_info: task_id 2, stream_id 5, tid 1066924, device_id 0, retcode 0x7bc83[FUNC:ErrorTrackingCallback][FILE:error_tracking.cc][LINE:114]
       Aicore kernel execute failed, device_id=0, stream_id=5, report_stream_id=2, task_id=2, flip_num=0, fault kernel_name=te_greater_c87b4e35adc1e58d7047014c98476f6d74dd012ef22efd1f1c93482e181551fe2487f8709dcda93ee62e53b922adf8008eab9333cff99835ffe8fce41feface9_static_bin, fault kernel info ext=te_greater_c87b4e35adc1e58d7047014c98476f6d74dd012ef22efd1f1c93482e181551fe__kernel0, program id=14, hash=2660134322332982280.[FUNC:GetError][FILE:stream.cc][LINE:1079]
       [AIC_INFO] after execute:args print end[FUNC:GetError][FILE:stream.cc][LINE:1079]
       rtDeviceSynchronize execute failed, reason=[the model stream execute failed][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
       wait for compute device to finish failed, runtime result = 507011.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
       rtDeviceSynchronizeWithTimeout execute failed, reason=[vector core exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
       wait for compute device to finish failed, runtime result = 507035.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
 (function npuSynchronizeUsedDevices)
[W compiler_depend.ts:122] Warning: NPU warning, error code is 507035[Error]: 
[Error]: The vector core execution is abnormal. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[vector core exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 1066924] 2025-04-29-18:46:11.184.465 wait for compute device to finish failed, runtime result = 507035.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function empty_cache)
[W compiler_depend.ts:469] Warning: NPU warning, error code is 507035[Error]: 
[Error]: The vector core execution is abnormal. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[vector core exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 1066924] 2025-04-29-18:46:11.185.937 wait for compute device to finish failed, runtime result = 507035.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeDevice)
[W compiler_depend.ts:122] Warning: NPU warning, error code is 507035[Error]: 
[Error]: The vector core execution is abnormal. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[vector core exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 1066924] 2025-04-29-18:46:11.187.327 wait for compute device to finish failed, runtime result = 507035.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function empty_cache)
[W compiler_depend.ts:469] Warning: NPU warning, error code is 507035[Error]: 
[Error]: The vector core execution is abnormal. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[vector core exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 1066924] 2025-04-29-18:46:11.188.620 wait for compute device to finish failed, runtime result = 507035.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeDevice)
[W compiler_depend.ts:122] Warning: NPU warning, error code is 507035[Error]: 
[Error]: The vector core execution is abnormal. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[vector core exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 1066924] 2025-04-29-18:46:11.190.000 wait for compute device to finish failed, runtime result = 507035.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function empty_cache)
[W compiler_depend.ts:469] Warning: NPU warning, error code is 507035[Error]: 
[Error]: The vector core execution is abnormal. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[vector core exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 1066924] 2025-04-29-18:46:11.191.317 wait for compute device to finish failed, runtime result = 507035.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeDevice)
[W compiler_depend.ts:122] Warning: NPU warning, error code is 507035[Error]: 
[Error]: The vector core execution is abnormal. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[vector core exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 1066924] 2025-04-29-18:46:11.192.638 wait for compute device to finish failed, runtime result = 507035.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function empty_cache)
[W compiler_depend.ts:469] Warning: NPU warning, error code is 507035[Error]: 
[Error]: The vector core execution is abnormal. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[vector core exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 1066924] 2025-04-29-18:46:11.193.895 wait for compute device to finish failed, runtime result = 507035.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeDevice)
[INFO] TORCHAIR [memory/Allocator.cpp:110] [MemoryTrace] FreeFeatureMemory: Try to Free memory, size = 786944, and addr = 0x124041201e00 , use count = 1
[INFO] TORCHAIR [memory/Allocator.cpp:88] [MemoryTrace] FreePoolMemory: Try to Free memory, size = 786944, and addr = 0x124041201e00 , use count = 1
[DEBUG] TORCHAIR [memory/Allocator.cpp:42] [MemoryTrace] Try to free the mem_block, mem_block = 0xaaab1c06b400, NPUCachingAllocator block = 0xaaab19bb5160, device_ptr = 0x124041201e00, size = 786944
[DEBUG] TORCHAIR [memory/Allocator.cpp:51] [MemoryTrace]Free the mem_block success.
[INFO] TORCHAIR [memory/Allocator.cpp:99] [MemoryTrace] FreePoolMemory: Free memory success, block use count = 0 , memory pool size = 0
[DEBUG] TORCHAIR [memory/Allocator.cpp:42] [MemoryTrace] Try to free the mem_block, mem_block = 0xaaab1c22c570, NPUCachingAllocator block = 0xaaab1d340160, device_ptr = 0x124041200000, size = 7680
[DEBUG] TORCHAIR [memory/Allocator.cpp:51] [MemoryTrace]Free the mem_block success.
```

软件版本：（46，30188）
```
-- CANN 版本:  8.0.RC3 
-- Tensorflow/Pytorch/MindSpore 版本: torch 2.1.0/2.1.0.post10 2.1.0.post10
-- Python 版本 ：Python 3.10.0  （source /home/ma-user/work/zhongyunde/source/backup/venv/bin/activate）
-- MindStudio版本 (e.g., MindStudio 2.0.0 (beta3)): NA 
-- 操作系统版本 (e.g., Ubuntu 18.04): Linux version 4.19.90-vhulk2211.3.0.h1543.eulerosv2r10.aarch64 (cat /proc/version)
```

测试步骤：试图采用图模式方式编译
> (venv) (llama_py39) (MindSpore) [ma-user llama149]$python testLlame_new.py
> 参考：https://www.hiascend.com/document/detail/zh/Pytorch/60RC1/modthirdparty/torchairuseguide/torchair_0006.html
```
from transformers import LlamaForCausalLM, AutoTokenizer
import torch
import torch_npu
import time
import torchair as tng

torch.set_printoptions(profile="full")
# torch.npu.set_compile_mode(jit_compile=True)
device="npu:1"

__spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"

#下载好的hf模型地址
hf_model_path = 'models--daryl149--llama-2-7b-hf'
model = LlamaForCausalLM.from_pretrained(hf_model_path, device_map=device)

npu_backend = tng.get_npu_backend()
model.forward = torch.compile(model.forward, backend=npu_backend, dynamic=False)
#model = torch.compile(model, backend=npu_backend, dynamic=False)

tokenizer = AutoTokenizer.from_pretrained(hf_model_path)

#print(model)

prompt = "Hey, are you conscious? Can you talk to me?"
inputs = tokenizer(prompt, return_tensors="pt").to(device)

# Generate
time_start = time.time()
generate_ids = model.generate(inputs.input_ids, max_length=512)
time_end = time.time()
#res = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
print("time cost:", time_end-time_start)
```

补充说明：
a) 上述用例 model.forward = torch.compile(model.forward, backend=npu_backend, dynamic=False) 改为 model = torch.compile(model, backend=npu_backend, dynamic=False) 时编译本身正确，但图模式没有生效
b) 已经使用固定的device="npu:1", 参考 https://gitee.com/ascend/pytorch/issues/IAOOZ0

## 评论 (2)

### yunyiyun · 2025-07-19

如果使用device='npu:0'还报错吗

### JiabinXue · 2025-10-09

遇到了同样的问题，希望推理qwen2.5-32B model,如果设置npu:0在64G显存下无法加载，会出现OOM，但是如果设置auto，则会出现上述错误，后续这个问题有解决吗？

