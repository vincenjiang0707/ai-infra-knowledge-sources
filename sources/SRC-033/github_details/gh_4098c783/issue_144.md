# [Issue #144] torch_npu 2.10 + CANN 9.0 on soc_version 104: torch.nn.functional.linear fails with MatMul/TransData

source: https://github.com/Ascend/pytorch/issues/144
state: open | updated: 2026-06-08T20:04:46Z
labels: 

## 正文

### Current environment

We are trying to run Qwen3-0.6B on Ascend 910B with `soc_version == 104`.

Relevant environment from the container:

```text
OS: openEuler 24.03 (LTS-SP2) (aarch64)
Python: 3.11.15
PyTorch: 2.10.0+cpu
torch_npu: 2.10.0
CANN: 9.0.0
vLLM: 0.20.2
vLLM Ascend image: quay.io/ascend/vllm-ascend:v0.20.2rc1 based local image
NPU: 910B 32GB
npu-smi: 25.5.2
torch_npu.npu.get_soc_version(): 104
```

`npu-smi` shows 910B devices:

```text
+------------------------------------------------------------------------------------------------+
| npu-smi 25.5.2                   Version: 25.5.2                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B                | OK            | 70.3        38                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           1103 / 13552      0    / 32768         |
+===========================+===============+====================================================+
| 1     910B                | OK            | 68.9        38                0    / 0             |
| 0                         | 0000:81:00.0  | 0           1483 / 15665      0    / 32768         |
+===========================+===============+====================================================+
| 2     910B                | OK            | 70.7        39                0    / 0             |
| 0                         | 0000:41:00.0  | 0           2803 / 15665      0    / 32768         |
+===========================+===============+====================================================+
| 3     910B                | OK            | 67.6        36                0    / 0             |
| 0                         | 0000:01:00.0  | 0           3184 / 15563      0    / 32768         |
+===========================+===============+====================================================+
| 4     910B                | OK            | 72.1        52                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           1071 / 13526      0    / 32768         |
+===========================+===============+====================================================+
| 5     910B                | OK            | 68.3        37                0    / 0             |
| 0                         | 0000:82:00.0  | 0           1408 / 15665      0    / 32768         |
+===========================+===============+====================================================+
| 6     910B                | OK            | 70.0        43                0    / 0             |
| 0                         | 0000:42:00.0  | 0           2277 / 15665      0    / 32768         |
+===========================+===============+====================================================+
| 7     910B                | OK            | 68.5        36                0    / 0             |
| 0                         | 0000:02:00.0  | 0           3818 / 15589      0    / 32768         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 0                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 2                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 3                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 4                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 5                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 6                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 7                                                            |
+===========================+===============+====================================================+
```

### What happened

On upstream vLLM Ascend, the first error is:

```text
RuntimeError: Can not support soc_version: 104.
```

This matches the currently open issue https://github.com/vllm-project/vllm-ascend/issues/6796.

For debugging only, I temporarily treated `soc_version == 104` as `AscendDeviceType.A2` in `vllm_ascend/utils.py` to get past the device-type guard. After that, Qwen3-0.6B can get further, but it fails during the first dummy/profile forward in `qkv_proj`, eventually reaching `torch.nn.functional.linear`.

The important part is that this is not only a vLLM model-startup failure: a minimal standalone PyTorch `torch.nn.functional.linear` repro also fails on NPU with `soc_version 104`.

### Minimal repro

```python
import os
os.environ.setdefault("ASCEND_RT_VISIBLE_DEVICES", "0")
os.environ.setdefault("ASCEND_LAUNCH_BLOCKING", "1")

import torch
import torch_npu

torch.npu.set_device(0)
print("torch", torch.__version__)
print("torch_npu", torch_npu.__version__)
print("soc_version", torch_npu.npu.get_soc_version())

x = torch.ones((1, 1024), dtype=torch.float16).to("npu:0")
w = torch.ones((2048, 1024), dtype=torch.float16).to("npu:0")
y = torch.nn.functional.linear(x, w)
torch.npu.synchronize()
print(y.shape, y[0, 0].float().cpu())
```

Run command:

```bash
ASCEND_RT_VISIBLE_DEVICES=0 ASCEND_LAUNCH_BLOCKING=1 python3 /tmp/repro_matmul_uncaught.py
```

### Minimal repro error log

```text
torch 2.10.0+cpu
torch_npu 2.10.0
soc_version 104
Traceback (most recent call last):
  File "/tmp/repro_matmul_uncaught.py", line 14, in <module>
    y = torch.nn.functional.linear(x, w)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: InnerRun:../torch_npu/csrc/framework/OpParamMaker.cpp:240 OPS function error: MatMul, error code is 500002
[ERROR] 2026-06-08-19:41:31 (PID:8818, Device:0, RankID:-1) ERR01100 OPS call acl api failed
[Error]: A GE error occurs in the system.
        Rectify the fault based on the error information in the ascend log.
[PID: 8818] 2026-06-08-19:41:31.081.721 Unsupported_Operator(EZ3002): Optype [TransData] of Ops kernel [DNN_VM_HOST_CPU_OP_STORE] is unsupported. Reason: Transdata op, groups should be greater than 1, but now is 1.
        Possible Cause: The operator type is unsupported in the operator information library due to specification mismatch.
        Solution: Submit an issue to request for support at https://gitee.com/ascend, or remove this type of operators from your model.
        TraceBack (most recent call last):
        Optype [TransData] of Ops kernel [aicpu_ascend_kernel] is unsupported. Reason: Transdata op, groups should be greater than 1, but now is 1.
        No supported Ops kernel and engine are found for [trans_TransData_0], optype [TransData].
        Failed to select engine for [trans_TransData_0][TransData].[FUNC:operator()][FILE:engine_place.cc][LINE:152]
        RunAllSubgraphs failed, graph=online.[FUNC:RunAllSubgraphs][FILE:engine_place.cc][LINE:125]
        build graph failed, graph id:0, ret:4294967295[FUNC:BuildModelWithGraphId][FILE:ge_generator.cc][LINE:1603]
        [Build][SingleOpModel]call ge interface generator.BuildSingleOpModel failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:148]
        [Build][Op]Fail to build op model[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:132]
        build op model failed, result = 500002[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:132]
```

### vLLM repro command

Qwen3-0.6B is mounted at `/model`.

```bash
export ASCEND_RT_VISIBLE_DEVICES=0
export TASK_QUEUE_ENABLE=1
export HCCL_OP_EXPANSION_MODE=AIV
export ASCEND_LAUNCH_BLOCKING=1

python3 -m vllm.entrypoints.openai.api_server \
  --model /model \
  --dtype float16 \
  --port 18002 \
  --host 0.0.0.0 \
  --reasoning-parser qwen3 \
  --served-model-name qwen3-0.6b \
  --enable-prefix-caching \
  --trust-remote-code \
  --tensor-parallel-size 1 \
  --gpu-memory-utilization 0.75 \
  --max-model-len 2048 \
  --enforce-eager
```

Notes:

- The Docker container maps all NPU devices (`/dev/davinci0` through `/dev/davinci7`) and selects NPU0 with `ASCEND_RT_VISIBLE_DEVICES=0` inside the container.
- BF16 is not used here; this repro uses `float16`.
- `Gloo Rank 0 is connected to 0 peer ranks` appears with `world_size=1`, which seems expected and unrelated.

### vLLM error log

```text
EngineCore failed to start during profile_run / _dummy_run.

Traceback reaches:

  File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3.py", line 228, in forward
    hidden_states = self.self_attn(
  File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/worker/patch_qwen3vl.py", line 36, in forward_with_split_qkv_rmsnorm_mrope
    qkv, _ = self.qkv_proj(hidden_states)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/linear.py", line 199, in forward
    return super().forward(input_)
  File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 587, in forward
    output_parallel = self.quant_method.apply(self, input_, bias)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/linear.py", line 90, in apply
    return torch.ops.vllm.unquantized_gemm(x, layer.weight, bias)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/linear.py", line 52, in unquantized_gemm
    return torch.nn.functional.linear(x, weight, bias)

RuntimeError: Sync:../torch_npu/csrc/framework/OpCommand.cpp:340 NPU function error: c10_npu::acl::AclrtSynchronizeStreamWithTimeout(stream), error code is 507018
[ERROR] 2026-06-08-19:04:04 (PID:4179, Device:0, RankID:-1) ERR00100 PTA call acl api failed
[Error]: The aicpu execution is abnormal.
E39999: Inner Error!
E39999[PID: 4179] 2026-06-08-19:04:04.698.981 (E39999):  Kernel task happen error, retCode=0x2a, [aicpu exception].[FUNC:PreCheckTaskErr][FILE:davinci_kernel_task.cc][LINE:1729]
TraceBack (most recent call last):
Aicpu kernel execute failed, device_id=0, stream_id=15, task_id=265, soName=libtf_kernels.so, funcName=TFOperateAPI, kernelName=MatMul, errorCode=0x2a.[FUNC:PrintAicpuErrorInfo][FILE:davinci_kernel_task.cc][LINE:1435]
Aicpu kernel execute failed, device_id=0,stream_id=15,task_id=265, soName=libtf_kernels.so, funcName=TFOperateAPI, kernelName=MatMul[FUNC:PrintAicpuErrorInfo][FILE:davinci_kernel_task.cc][LINE:1460]
An exception occurred during AICPU execution, stream_id:15, task_id:265, errcode:5, msg:aicpu execute failed[FUNC:ProcessAicpuErrorInfo][FILE:device_error_proc.cc][LINE:878]
rtStreamSynchronizeWithTimeout execution failed, reason=aicpu exception[FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:65]
```

### Additional observation

Before reaching the MatMul error, I also saw an Ascend RoPE/update path issue when debugging Qwen3:

```text
Unsupported_Operator(EZ3003): No supported Ops kernel and engine are found for [AsStrided12], optype [AsStrided]
```

This was triggered by `vllm_ascend/ops/rotary_embedding.py:update_cos_sin` at the slice assignment:

```python
_cos[:, :num_tokens] = ...
```

For debugging, I bypassed that slice assignment and then the startup moved forward to the MatMul failure above. I mention this only as supporting evidence that `soc_version=104` seems to be going through unsupported or wrong operator paths when treated as A2.

### Expected behavior

- Please clarify whether `soc_version == 104` is supposed to be supported by vLLM Ascend / torch_npu / CANN 9.0 on 910B.
- If it should be supported, `torch.nn.functional.linear` with a small FP16 matrix should work on NPU.
- If it is not supported, vLLM Ascend should document this and avoid recommending workarounds that simply map 104 to A2, because later operator selection still fails.

### Related issue

- https://github.com/vllm-project/vllm-ascend/issues/6796


## 评论 (1)

### wakaka6 · 2026-06-08

Cross-linking the vLLM Ascend issue where this was first isolated from Qwen3 startup: https://github.com/vllm-project/vllm-ascend/issues/10206

The key signal is the standalone `torch.nn.functional.linear` repro above; vLLM is just where the failure first surfaced.
