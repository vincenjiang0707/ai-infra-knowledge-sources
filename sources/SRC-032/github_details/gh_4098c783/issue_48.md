# [Issue #48] 在使用Ascend进行模型训练的时候遇到错误

source: https://github.com/Ascend/pytorch/issues/48
state: open | updated: 2025-05-13T11:58:17Z
labels: 

## 正文

训练数据量1.2M,采用16卡进行训练
已经设置
export HCCL_EXEC_TIMEOUT=17340

错误信息：
W NPUStream.cpp:409] Warning: NPU warning, error code is 507046[Error]: 
[Error]: In the specified timeout waiting event, all tasks in the specified stream are not completed. 
        Rectify the fault based on the error information in the ascend log.
EE1002: 2024-09-03-16:50:00.041.231 Stream synchronize timeout. rtDeviceSynchronize execute failed, reason=[stream sync timeout]
        Possible Cause: 1. The timeout interval may be improperly set.
        Solution: 1. Check whether the timeout interval is properly set. 2. Check whether the network is normal.
        TraceBack (most recent call last):
        wait for compute device to finish failed, runtime result = 507046.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
 (function npuSynchronizeUsedDevices)

## 评论 (2)

### yunyiyun · 2024-09-21

麻烦提供下详细plog日志
plog日志默认路径：/root/ascend/log
可以通过export ASCEND_GLOBAL_LOG_LEVEL=1配成INFO级别（0对应DEBUG级别，2对应WARN级别，3为默认的ERROR级别）。
对于分布式通信（hccl）问题，一般需要开启event日志 export ASCEND_GLOBAL_EVENT_ENABLE=1

### Pe4nutZz · 2025-05-13

这个问题解决了吗
