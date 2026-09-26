# [Issue #99] torch_npu2.7.1 和CANN 8.3.RC1不兼容

source: https://github.com/Ascend/pytorch/issues/99
state: open | updated: 2026-03-30T03:06:59Z
labels: 

## 正文

按照readme安装了2.7.1版本的torch_npu和CANN 8.3.RC1，在执行时报错
Traceback (most recent call last):
   File "/usr/local/python3/lib/python3.11/site-packages/torch_npu/op_plugin/atb/_atb_ops.py", line 66, in <module>
     torch.ops.load_library(atb_so_path)
   File "/usr/local/python3/lib/python3.11/site-packages/torch/_ops.py", line 1392, in load_library
     ctypes.CDLL(path)
   File "/usr/local/python3/lib/python3.11/ctypes/__init__.py", line 376, in __init__
     self._handle = _dlopen(self._name, mode)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^
 OSError: /home/mtp/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib/libtbe_adapter.so: undefined symbol: _ZN3Mki2DlC1ERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEb
 
 The above exception was the direct cause of the following exception:
 
 Traceback (most recent call last):
   File "/usr/local/python3/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 571, in worker_main
     worker = WorkerProc(*args, **kwargs)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
   File "/usr/local/python3/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 405, in __init__
     wrapper.init_worker(all_kwargs)
   File "/usr/local/python3/lib/python3.11/site-packages/vllm/worker/worker_base.py", line 248, in init_worker
     self.worker = worker_class(**kwargs)
                   ^^^^^^^^^^^^^^^^^^^^^^
   File "/usr/local/python3/lib/python3.11/site-packages/vllm_ascend/worker/worker_v1.py", line 88, in __init__
     _register_atb_extensions()
   File "/usr/local/python3/lib/python3.11/site-packages/torch_npu/op_plugin/atb/_atb_ops.py", line 86, in      _register_atb_extensions
     raise NNAL_EX from GLOBAL_E
   File "/usr/local/python3/lib/python3.11/site-packages/torch_npu/op_plugin/atb/_atb_ops.py", line 66, in <module>
     torch.ops.load_library(atb_so_path)
   File "/usr/local/python3/lib/python3.11/site-packages/torch/_ops.py", line 1392, in load_library
     ctypes.CDLL(path)
   File "/usr/local/python3/lib/python3.11/ctypes/__init__.py", line 376, in __init__
     self._handle = _dlopen(self._name, mode)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^
 OSError: [Errno None] Please check the version of the NNAL package. An undefined symbol was found, which may be caused by a version mismatch between NNAL and torch_npu.

## 评论 (4)

### yunyiyun · 2026-01-07

请根据报错提示，安装对应配套的nnal包

### ljljkatakuli · 2026-01-07

Ascend-cann-nnal_8.3.RC1_linux-aarch64.run  我已经安装了这个版本的cann-nnal，理论上应该是适配的，但还是报这个错，也试过torch_npu==2.7.1.post1，依然报一样的错



### yunyiyun · 2026-01-07

您这边检查下是否正确安装，环境变量是否正取配置，
或者重新安装下相关的配套包，记得保持环境的干净，防止残留文件影响

### immengzi · 2026-03-30

同样的问题。CANN 8.5.0，torch npu 2.8.0post2

```sh
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68] EngineCore failed to start.
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68] Traceback (most recent call last):
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]   File "/usr/local/lib64/python3.11/site-packages/torch_npu/op_plugin/atb/_atb_ops.py", line 66, in <module>
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]     torch.ops.load_library(atb_so_path)
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]   File "/usr/local/lib64/python3.11/site-packages/torch/_ops.py", line 1478, in load_library
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]     ctypes.CDLL(path)
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]   File "/usr/lib64/python3.11/ctypes/__init__.py", line 376, in __init__
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]     self._handle = _dlopen(self._name, mode)
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]                    ^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68] OSError: /usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib/libtbe_adapter.so: undefined symbol: _ZN3Mki2DlC1ERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEb
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68] The above exception was the direct cause of the following exception:
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68] Traceback (most recent call last):
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]   File "/root/vllm-ascend/vllm_ascend/patch/platform/patch_core.py", line 59, in run_engine_core
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]   File "/root/vllm/vllm/v1/engine/core.py", line 637, in __init__
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]     super().__init__(
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]   File "/root/vllm/vllm/v1/engine/core.py", line 102, in __init__
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]   File "/root/vllm/vllm/v1/executor/abstract.py", line 101, in __init__
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]     self._init_executor()
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]   File "/root/vllm/vllm/v1/executor/uniproc_executor.py", line 46, in _init_executor
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]     self.driver_worker.init_worker(all_kwargs=[kwargs])
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]   File "/root/vllm/vllm/v1/worker/worker_base.py", line 313, in init_worker
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]     self.worker = worker_class(**kwargs)
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]                   ^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]   File "/root/vllm-ascend/vllm_ascend/worker/worker.py", line 115, in __init__
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]     _register_atb_extensions()
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]   File "/usr/local/lib64/python3.11/site-packages/torch_npu/op_plugin/atb/_atb_ops.py", line 86, in _register_atb_extensions
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]     raise NNAL_EX from GLOBAL_E
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]   File "/usr/local/lib64/python3.11/site-packages/torch_npu/op_plugin/atb/_atb_ops.py", line 66, in <module>
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]     torch.ops.load_library(atb_so_path)
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]   File "/usr/local/lib64/python3.11/site-packages/torch/_ops.py", line 1478, in load_library
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]     ctypes.CDLL(path)
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]   File "/usr/lib64/python3.11/ctypes/__init__.py", line 376, in __init__
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]     self._handle = _dlopen(self._name, mode)
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68]                    ^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=1228) ERROR 03-30 03:00:55 [patch_core.py:68] OSError: [Errno None] Please check the version of the NNAL package. An undefined symbol was found, which may be caused by a version mismatch between NNAL and torch_npu.
```
