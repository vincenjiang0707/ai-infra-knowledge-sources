# [Issue #72] fsdp 模型保存问题,仅在多节点会出现这种情况，在单机八卡测试没有问题

source: https://github.com/Ascend/pytorch/issues/72
state: open | updated: 2025-07-19T01:52:50Z
labels: 

## 正文

Entering the ``_unshard_fsdp_state_params`` context but _unshard_params_ctx[module] is not None.
Entering the ``_unshard_fsdp_state_params`` context but _unshard_params_ctx[module] is not None.
npuSynchronizeDevice:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:506 NPU function error: AclrtSynchronizeDeviceWithTimeout, error code is 107020
[ERROR] 2025-07-13-21:24:03 (PID:474, Device:2, RankID:2) ERR00100 PTA call acl api failed.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[task timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 474] 2025-07-13-21:24:03.362.493 wait for compute device to finish failed, runtime result = 107020.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):

npuSynchronizeDevice:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:506 NPU function error: AclrtSynchronizeDeviceWithTimeout, error code is 107020
[ERROR] 2025-07-13-21:24:03 (PID:475, Device:3, RankID:3) ERR00100 PTA call acl api failed.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[task timeout][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 475] 2025-07-13-21:24:03.363.017 wait for compute device to finish failed, runtime result = 107020.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):


## 评论 (1)

### yunyiyun · 2025-07-19

当前提供的信息显示任务超时，可能由于数据量太大导致在一定时间没有计算完成，可以尝试调整设备超时时间或者改小数据看下是否报错（调整设备超时需要torch_npu 6.0.0及之后的版本才支持）
https://www.hiascend.com/document/detail/zh/Pytorch/700/comref/Envvariables/Envir_027.html
或者检查下多节点中是否有其他节点已经报错或者代码卡住导致任务没有完成
