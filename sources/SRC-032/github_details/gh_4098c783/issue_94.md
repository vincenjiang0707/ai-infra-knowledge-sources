# [Issue #94] LinearOperation CreateOperation failed

source: https://github.com/Ascend/pytorch/issues/94
state: open | updated: 2026-06-12T05:52:45Z
labels: 

## 正文

## 版本
+ CANN：8.3.RC2
+ torch_npu：2.7.1
+ npu驱动（Ascend HDK）：24.1.rc2
+ 操作系统：BigCloud Enterprise Linux For Euler 21.10 LTS，aarch64
+ 推理卡：Ascend 310P3

使用的quay.io/ascend/vllm-ascend/v0.11.0-310p-openeuler docker镜像

```bash
[root@bbefe1f368bf workspace]# npu-smi info
+--------------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc2                                 Version: 24.1.rc2                                     |
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Name                  | Health          | Power(W)     Temp(C)           Hugepages-Usage(page) |
| Chip    Device                | Bus-Id          | AICore(%)    Memory-Usage(MB)                        |
+===============================+=================+======================================================+
| 1792    310P3                 | OK              | NA           36                0     / 0             |
| 0       0                     | 0000:07:00.0    | 0            1821 / 44280                            |
+-------------------------------+-----------------+------------------------------------------------------+
| 1792    310P3                 | OK              | NA           36                0     / 0             |
| 1       1                     | 0000:07:00.0    | 0            1041 / 43693                            |
+===============================+=================+======================================================+
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Chip                  | Process id      | Process name             | Process memory(MB)        |
+===============================+=================+======================================================+
| No running processes found in NPU 1792                                                                 |
+===============================+=================+======================================================+
```

## 问题代码

```python
import torch
import torch_npu

print(torch.npu.is_available())
print(torch.npu.device_count())

x = torch.randn(2, 2).npu()
w = torch.randn(2, 2).npu()
c = torch.zeros(2, 2).npu()

torch_npu._npu_matmul_add_fp32(x, w, c)
print("Minimal test passed!")
```

## 错误异常
```bash
[root@bbefe1f368bf workspace]# python torch_sample.py
True
2
Traceback (most recent call last):
  File "/workspace/torch_sample.py", line 13, in <module>
    torch_npu._npu_matmul_add_fp32(x, w, c)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/op_plugin/atb/_atb_ops.py", line 96, in wrapper
    return api_func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/op_plugin/atb/_atb_ops.py", line 104, in generated_function
    return getattr(torch.ops.atb, api_name)(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
    return self._op(*args, **(kwargs or {}))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: LinearOperation CreateOperation failed!
[ERROR] 2025-12-18-11:35:06 (PID:1700, Device:0, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```

请问LinearOperation CreateOperation failed怎么解决

## 评论 (2)

### jxj9049 · 2025-12-19

This interface is only an example for library use and is not intended for external use. It currently does not support any machine models.

### Michael-24 · 2026-06-12

310p模型 qwen3-tts 模型的时候 也遇到 这个报错:
LinearOperation CreateOperation failed 🥹
