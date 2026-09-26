# [Issue #140] 算子launch线程数量有误，全部由acl_thread进行算子下发

source: https://github.com/Ascend/pytorch/issues/140
state: open | updated: 2026-06-09T12:09:00Z
labels: 

## 正文

我是在C++进行大模型推理框架的开发，问题是在本地拉起多个线程，每个线程绑定一个NPU Stream进行算子的launch，本意是想多线程并发launch NPU算子，但是经过profile发现最终会有单个线程acl_thread进行统一的launch。然后在GPU上是能够正常拉起多个线程进行算子的下发，这是torch_npu这边规定的吗，还是其他原因？

环境：
910B3 单卡
torch: 2.9.0+cpu
torch_npu: 2.9.0
CANN：8.5.0


## 评论 (1)

### yunyiyun · 2026-06-09

torch_npu默认开启taskqueue，一个device对应一个taskqueue，taskqueue开启时可以有多个线程enqueue，但是只有一个线程dequeue，就是你看到的acl_thread线程，你可以关闭taskqueue，这样就能看到多个线程下发

https://www.hiascend.com/document/detail/zh/Pytorch/2600/comref/Envvariables/docs/zh/environment_variable_reference/TASK_QUEUE_ENABLE.md
