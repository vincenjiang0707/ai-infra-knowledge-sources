# [Issue #67] setDevice 报错

source: https://github.com/Ascend/pytorch/issues/67
state: open | updated: 2025-07-04T01:27:44Z
labels: 

## 正文

这和 torch 的使用方法不一致吗？这个 setDevice 是怎么用的？

```bash
>>> os.environ['ASCEND_RT_VISIBLE_DEVICES'] = '1'
>>> torch_npu._C._npu_setDevice(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: Initialize:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:146 NPU function error: c10_npu::SetDevice(device_id_), error code is 507033
[ERROR] 2025-06-24-11:20:49 (PID:528886, Device:-1, RankID:-1) ERR00100 PTA call acl api failed
[Error]: Failed to start the device. 
        Rectify the fault based on the error information in the ascend log.
EL0003: [PID: 528886] 2025-06-24-11:20:41.662.506 The argument is invalid.
        Solution: Try again with a valid argument.
        TraceBack (most recent call last):
        Failed to open device, retCode=0x7020014, deviceId=0.[FUNC:InitRawDriver][FILE:raw_device.cc][LINE:126]
        Failed to init RawDriver, device_id=0, retCode=0x7020014[FUNC:Init][FILE:raw_device.cc][LINE:323]
        Check param failed, dev can not be NULL![FUNC:DeviceRetain][FILE:runtime.cc][LINE:3631]
        Check param failed, dev can not be NULL![FUNC:PrimaryContextRetain][FILE:runtime.cc][LINE:3330]
        Check param failed, ctx can not be NULL![FUNC:PrimaryContextRetain][FILE:runtime.cc][LINE:3360]
        Check param failed, context can not be null.[FUNC:NewDevice][FILE:api_impl.cc][LINE:3000]
        New device failed, retCode=0x7010006[FUNC:SetDevice][FILE:api_impl.cc][LINE:3024]
        rtSetDevice execute failed, reason=[device retain error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
        open device 0 failed, runtime result = 507033.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        ctx is NULL![FUNC:GetDevErrMsg][FILE:api_impl.cc][LINE:5925]
        The argument is invalid.Reason: rtGetDevMsg execute failed, reason=[context pointer null]
```

## 评论 (2)

### FieeFlip · 2025-06-24

@yan-yhy 

### yunyiyun · 2025-07-04

ASCEND_RT_VISIBLE_DEVICES在import torch_npu之前进行配置，
或者更新到即将发布的最新的torch_npu版本
