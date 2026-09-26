# [Issue #56] torch.nn.MaxPool1d 类似算子的支持

source: https://github.com/Ascend/pytorch/issues/56
state: open | updated: 2026-06-16T19:58:48Z
labels: 

## 正文

目前迁移模型到Ascend平台训练需要使用到一位最大池化操作，Ascend平台的pytorch(v2.3.1, v2.4.0)似乎还不支持MaxPool操作？以及我需要使用何种算子来平替这项操作。

![image](https://github.com/user-attachments/assets/228da721-b4e2-4d3c-9e29-5e36d442670a)

```
data/home/xxxxxxx/anaconda3/envs/Multi-Mods/lib/python3.9/site-packages/torch_npu/utils/path_manager.py:82: UserWarning: Warning: The /usr/local/Ascend/ascend-toolkit/7.0.1.5/aarch64-linux/ascend_toolkit_install.info owner does not match the current user.
  warnings.warn(f"Warning: The {path} owner does not match the current user.")
train process.
Run model on npu
[W compiler_depend.ts:615] Warning: expandable_segments currently defaults to false. You can enable this feature by `export PYTORCH_NPU_ALLOC_CONF = expandable_segments:True`. (function operator())
[W compiler_depend.ts:181] Warning: 0Failed to find function aclrtCreateEventExWithFlag (function operator())
Traceback (most recent call last):
  File "/data/home/xxxxxx/Multi-Mods/train/train_models.py", line 223, in <module>
    y = train_model(new_model, optimizer, loss_fun, train_data, args.save, test_data)
  File "/data/home/xxxxxx/Multi-Mods/train/train_models.py", line 147, in train_model
    loss.backward()
  File "/data/home/xxxxxx/anaconda3/envs/Multi-Mods/lib/python3.9/site-packages/torch/_tensor.py", line 525, in backward
    torch.autograd.backward(
  File "/data/home/xxxxxx/anaconda3/envs/Multi-Mods/lib/python3.9/site-packages/torch/autograd/__init__.py", line 267, in backward
    _engine_run_backward(
  File "/data/home/xxxxxxxx/anaconda3/envs/Multi-Mods/lib/python3.9/site-packages/torch/autograd/graph.py", line 744, in _engine_run_backward
    return Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
RuntimeError: InnerRun:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:194 OPS function error: MaxPoolGradWithArgmaxV1, error code is 500002
[ERROR] 2024-12-19-12:06:38 (PID:1940485, Device:0, RankID:-1) ERR01100 OPS call acl api failed
[Error]: A GE error occurs in the system.
        Rectify the fault based on the error information in the ascend log.
EZ3003: No supported Ops kernel and engine are found for [MaxPoolGradWithArgmaxV180], optype [MaxPoolGradWithArgmaxV1].
        Possible Cause: The operator is not supported by the system. Therefore, no hit is found in any operator information library.
        Solution: 1. Check that the OPP component is installed properly. 2. Submit an issue to request for the support of this operator type.
        TraceBack (most recent call last):
        build graph failed, graph id:79, ret:-1[FUNC:BuildModelWithGraphId][FILE:ge_generator.cc][LINE:1615]
        [Build][SingleOpModel]call ge interface generator.BuildSingleOpModel failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        [Build][Op]Fail to build op model[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
        build op model failed, result = 500002[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
```

## 评论 (2)

### yunyiyun · 2025-02-05

对于不支持的可以尝试放到cpu上计算；另外当前可以使用训练芯片看下是否支持。

### So-cean · 2026-06-16

torch.nn.MaxPool2d支持也有问题。torchnpu2.6，cann 8.2rc2。 910b3
