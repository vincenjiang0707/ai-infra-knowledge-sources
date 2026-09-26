# [Issue #166] ProcessGroupHCCL creation fails with fftsplus SDMA device error (507049) when another process uses CaMem sleep mode on the same NPU

source: https://github.com/Ascend/pytorch/issues/166
state: open | updated: 2026-08-31T03:14:51Z
labels: 

## 正文

---

## 环境

| 项 | 值 |
|---|---|
| 硬件 | Atlas 800T A2,910B3 × 8(单机) |
| 驱动/HDK | 25.5.1 |
| CANN | 9.0.1(容器内置) |
| torch | 2.10.0+cpu |
| torch_npu | 2.10.0.post2 |
| vLLM-Ascend | 0.23.0rc2 |

## 复现步骤

最小化场景:两个进程共占同一张 NPU 卡,一个进程启用了 vLLM-Ascend 的 `enable_sleep_mode`(CaMemAllocator),另一个进程在该卡上创建 HCCL 进程组:

```python
# 进程 A(vLLM-Ascend 推理引擎,enable_sleep_mode=True,已执行 /sleep)
# 此进程持有 CaMem 内存池,权重已下架到 CPU(storage resize 为零)

# 进程 B(训练进程,同卡):
import torch, torch_npu, torch.distributed as dist
dist.init_process_group(backend="hccl")           # 默认组正常
group = dist.new_group(backend="hccl")             # ← 此处触发设备故障
```

实际框架中的调用链(完整栈):

```
areal/v2/weight_update/nccl_group.py:134 init_weights_update_group
→ init_custom_process_group(backend="hccl", world_size=N, ...)
→ torch_npu/distributed/distributed_c10d.py:645 _patched_new_process_group_helper
→ ProcessGroupHCCL.cpp:1064
→ AclrtSetOpWaitTimeout(kOpWaitTimeout)
→ error code 507049
```

设备侧详细错误:

```
EE9999[PID: 43311] The error from device(chipId:1, dieId:0), serial number is 6.
there is a fftsplus sdma error, sdma channel is 2,
sdmaState=0x6, sdmaTslotid=0x4, sdmaCxtid=0x1, sdmaThreadid=0x0,
irqStatus=0x0, cqeStatus=0x70000.
[FUNC:ProcessCoreErrors][FILE:device_error_proc.cc][LINE:1714]
```

<img width="1406" height="433" alt="Image" src="https://github.com/user-attachments/assets/371b6a98-1846-49aa-bfd1-b5dc91f5183d" />

上层表现:

```
RuntimeError: npuSynchronizeDevice:../torch_npu/csrc/core/npu/NPUStream.cpp:576
NPU function error: AclrtSynchronizeDeviceWithTimeout, error code is 507049
wait for compute device to finish failed, runtime result = 507049
```

<img width="1385" height="491" alt="Image" src="https://github.com/user-attachments/assets/9a375937-4915-4700-9d64-d2dd81d604e9" />

## 关键对照

| 场景 | 结果 |
|---|---|
| **分离模式**(vLLM 和训练器各占不同卡,同一段建组代码) | ✅ 全部通过,连续 20+ 次建组零失败 |
| **共卡模式**(vLLM 启用 CaMem sleep,训练器同卡建组) | ❌ 100% 复现(三次干净容器重启后仍复现) |
| 共卡模式下训练器先恢复权重再建组 | ❌ 仍复现(同秒故障) |
| 共卡模式下改用 gloo 后端建组 | ❌ 仍复现(说明不是 HCCL 特定问题,是 CaMem×设备计算的通用交互) |

这强烈指向:**HCCL 通信域初始化与 CaMemAllocator 的设备内存池状态之间存在设备级交互问题**(SDMA 通道在已被另一进程腾挪过的内存映射上执行 DMA 时触发故障)。

## 期望

1. 请确认这是否为已知问题(驱动/固件版本相关);
2. 如果是 HCCL 通信域创建与 CaMem 内存池的已知不兼容,是否有推荐的工作顺序(如先建域再启用 sleep)?
3. 如果是新问题,请转交驱动/固件团队分析 SDMA channel 2 的 `sdmaState=0x6 / cqeStatus=0x70000` 状态含义;
4. gloo 后端也触发同款故障,说明这不是 HCCL 特定问题——可能是 CaMem 内存池状态与任何设备侧计算/同步操作的交互。请确认 CaMem sleep 后设备是否需要特定的恢复序列才能安全执行后续操作。

## 补充信息

- 故障芯片不固定(另一轮在 chipId:0 复现过同款);
- 故障在进程组创建的**同一秒**发生(非超时后崩溃——但也观察到一次 5 分钟等待后崩溃的变体);
- 容器内无 Transformer Engine、无 apex(纯 MindSpeed + Megatron-Bridge 环境);
- 完整的 vLLM-Ascend sleep 配置:`enable_sleep_mode: true` + `weight_nz_mode: 0` + `VLLM_SERVER_DEV_MODE=1`。

## 完整日志摘录

<details>
<summary>点击展开:从传输计划构建到 SDMA 故障的完整日志(已去除终端颜色码,IP 已隐去)</summary>

```text
# —— 对照侧:推理 worker(vLLM-Ascend,enable_sleep_mode)建组成功 ——
2026-08-31 01:43:41.286 INFO transfer_plan.py:268 -- Built communication plan with 1240 operations for 310 common parameters
2026-08-31 01:43:41.287 INFO transfer_plan.py:671 -- Rank[0] (inference) local plan has 620 operations grouped by 2 opposite ranks: [2, 3], global operations across all ranks: 1240
20260831-01:43:41.288 NCCLGroup INFO: init custom process group for inference: master_address=<redacted>, master_port=29508, rank=0, world_size=4, group_name=awex_actor-rollout, backend=hccl, current device id 0
20260831-01:43:41.368 NCCLGroup INFO: Initialized custom process group   ← 推理侧成功

# —— 故障侧:训练 worker 同一秒在同一卡上建组,触发设备故障 ——
20260831-01:43:41.474 TrainWorker ERROR: Error in engine thread when running init_weights_update_group: Failed to initialize custom process group: ProcessGroupHCCL:../torch_npu/csrc/distributed/ProcessGroupHCCL.cpp:1064 NPU function error: c10_npu::acl::AclrtSetOpWaitTimeout(kOpWaitTimeout), error code is 507049
[ERROR] 2026-08-31-01:43:41 (PID:93858, Device:0, RankID:0) ERR00100 PTA call acl api failed
EE9999: Inner Error!
EE9999[PID: 93858] 2026-08-31-01:43:40.988.733 (EE9999): The error from device(chipId:0, dieId:0), serial number is 16. there is a fftsplus sdma error, sdma channel is 4, sdmaState=0x6, sdmaTslotid=0x6, sdmaCxtid=0x1, sdmaThreadid=0x0, irqStatus=0x0, cqeStatus=0x70000.[FUNC:ProcessCoreErrors][FILE:device_error_proc.cc][LINE:1714]
        TraceBack (most recent call last):
        Failed to submit TaskTimeoutSetTask, retCode=0x715006c[FUNC:SetTimeoutConfigTaskSubmit][FILE:runtime.cc][LINE:4906]
        Failed to exe SetTimeoutConfigTaskSubmit, retCode=0x715006c.[FUNC:SetTimeoutConfig][FILE:runtime.cc][LINE:4994]
        rtSetOpWaitTimeOut execution failed, reason=fftsplus exception[FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:65]
        [Call][Rts]call rts api [rtSetOpWaitTimeOut] failed, retCode is 507049[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:148]

Traceback (most recent call last):
  File "/workspace/AReaL/areal/v2/weight_update/nccl_group.py", line 134, in init_weights_update_group
    group = init_custom_process_group(
  File "/workspace/AReaL/areal/v2/weight_update/nccl_group.py", line 78, in init_custom_process_group
    pg, _ = _new_process_group_helper(
  File "/usr/local/python3.11.15/lib/python3.11/site-packages/torch_npu/distributed/distributed_c10d.py", line 645, in _patched_new_process_group_helper
    backend_class = creator_fn(dist_backend_opts, backend_options)
  File "/usr/local/python3.11.15/lib/python3.11/site-packages/torch_npu/__init__.py", line 252, in _new_process_group_hccl_helper
    return torch_npu._C._distributed_c10d.ProcessGroupHCCL(store, group_rank, group_size, pg_options)
RuntimeError: ProcessGroupHCCL:../torch_npu/csrc/distributed/ProcessGroupHCCL.cpp:1064 NPU function error: c10_npu::acl::AclrtSetOpWaitTimeout(kOpWaitTimeout), error code is 507049
```

</details>

---

*在做AReaL2.1昇腾适配时，在单机 8×910B3 上做共卡训练×推理的权重同步时发现此问题。分离模式已在同硬件上完整验证(20 步零失败,权重同步 94ms/步),共卡模式被此设备故障阻塞。*

---


## 评论 (1)

### ascend-robot · 2026-08-31

Hello,

This repo is only a mirror with no active development or maintenance.
All bug reports, questions and code contributions should be submitted via the original repository link below.
Thanks for your interest!

Original Repository Link: https://gitcode.com/Ascend/pytorch
