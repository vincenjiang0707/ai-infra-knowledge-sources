# [Issue #49] 昇腾310p LLM推理报错：RuntimeError: copy_d2d:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:104 NPU function error: 

source: https://github.com/Ascend/pytorch/issues/49
state: closed | updated: 2024-11-08T08:16:48Z
labels: 

## 正文

一、问题现象（附报错日志上下文）：
RuntimeError: copy_d2d:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:104 NPU function error: c10_npu::acl::AclrtSynchronizeStreamWithTimeout(copy_stream), error code is 507013
[ERROR] 2024-09-04-02:09:03 (PID:2526494, Device:1, RankID:-1) ERR00100 PTA call acl api failed
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EI9999: Inner Error!
        The error from device(1), serial number is 13. there is a sdma error, sdma channel is 0, the channel exist the following problems: The SMMU returns a Terminate error during page table translation.. the value of CQE status is 2. the description of CQE status: When the SQE translates a page table, the SMMU returns a Terminate error.it's config include: setting1=0xc000080880e0000, setting2=0xff009000ff004c, setting3=0, sq base addr=0x800d00801003d000[FUNC:ProcessSdmaErrorInfo][FILE:device_error_proc.cc][LINE:704]
EI9999: 2024-09-04-02:09:03.196.977  Memory async copy failed, device_id=1, stream_id=3, task_id=703, flip_num=0, copy_type=2, memcpy_type=0, copy_data_type=0, length=40960[FUNC:GetError][FILE:stream.cc][LINE:1082]
        TraceBack (most recent call last):
        rtStreamSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
        synchronize stream failed, runtime result = 507013[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]


DEVICE[1] PID[2526494]: 
EXCEPTION STREAM:
  Exception info:TGID=2526494, model id=65535, stream id=3, stream phase=3
  Message info[0]:RTS_HWTS: hwts sdma error, slot_id=29, stream_id=3
    Other info[0]:time=2024-09-04-02:08:53.201.667, function=int_process_hwts_sdma_error, line=2070, error code=0x20b
[W compiler_depend.ts:409] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronize execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: 2024-09-04-02:09:03.218.111  wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeUsedDevices)
[W compiler_depend.ts:392] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronize execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: 2024-09-04-02:09:03.220.229  wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeDevice)
[W compiler_depend.ts:392] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronize execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: 2024-09-04-02:09:03.222.326  wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeDevice)
[W compiler_depend.ts:392] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronize execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: 2024-09-04-02:09:03.224.399  wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeDevice)
[W compiler_depend.ts:392] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronize execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: 2024-09-04-02:09:03.226.481  wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeDevice)
[W compiler_depend.ts:392] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronize execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: 2024-09-04-02:09:03.228.566  wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeDevice)
[W compiler_depend.ts:392] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronize execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: 2024-09-04-02:09:03.230.811  wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeDevice)
[W compiler_depend.ts:392] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronize execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: 2024-09-04-02:09:03.233.321  wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeDevice)
[W compiler_depend.ts:392] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronize execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: 2024-09-04-02:09:03.235.839  wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeDevice)


二、软件版本:
-- CANN 版本 (e.g., CANN 3.0.x，5.x.x): CANN 8.0.RC2
--Tensorflow/Pytorch/MindSpore 版本: pytorch 2.1.0     torch_npu2.1.0.post6  
--Python 版本 (e.g., Python 3.7.5):Python 3.10.14
--操作系统版本 (e.g., Ubuntu 18.04): Ubuntu 20.04.5 LTS (Focal Fossa)
三、测试步骤：

```
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation.utils import GenerationConfig
tokenizer = AutoTokenizer.from_pretrained("/baichuan-2-chat-pytorch-7b", use_fast=False, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("/baichuan-2-chat-pytorch-7b", device_map="auto", torch_dtype=torch.bfloat16, trust_remote_code=True)
model.generation_config = GenerationConfig.from_pretrained("/baichuan-2-chat-pytorch-7b")
messages = []
messages.append({"role": "user", "content": "介绍一下自己。"})
response = model.chat(tokenizer, messages)
print(response)

模型能加载进来，但是推理会报错。
```


四、日志信息:
ascend/log/debug/plog/plog-2514126_20240904013504490.log   日志见附件
[plog-2514126_20240904013504490.log](https://github.com/user-attachments/files/16860247/plog-2514126_20240904013504490.log)


## 评论 (0)
