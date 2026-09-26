# [Issue #163] [Bug]: NPU 环境下 Dynamo 处理零参数 id() 时抛出 IndexError 而非 TypeError，与 PyTorch 原生行为不一致，影响设备测试解耦

source: https://github.com/Ascend/pytorch/issues/163
state: open | updated: 2026-08-13T06:36:06Z
labels: 

## 正文



## 环境信息
环境问题如下


```
### Environment
| Item | Version |
|------|---------|
| CANN | 9.1.0 |
| PyTorch | 2.14.0+gitee7bc39 |
| torch_npu | 2.14.0+gitee7bc39 |
```

社区用例：
https://github.com/pytorch/pytorch/blob/main/test/dynamo/test_id.py

<img width="622" height="341" alt="Image" src="https://github.com/user-attachments/assets/7a7e3ae9-0855-49bf-a498-925700807b51" />




## 报错信息


           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/npu-env/pytorch/torch/_dynamo/variables/builtin.py", line 1388, in builtin_dispatch
    rv = handler(tx, args, kwargs)
         ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/npu-env/pytorch/torch/_dynamo/variables/builtin.py", line 1262, in call_self_handler
    return self_handler(tx, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/miniconda/envs/npu/lib/python3.12/site-packages/torch_npu/utils/_dynamo.py", line 290, in _wrap_call_id
    args[0], torch._dynamo.variables.streams.EventVariable
    ~~~~^^^
IndexError: tuple index out of range

from user code:
   File "/workspace/dcp-work-dcp-tc/pytorch/test/dynamo/test_id.py", line 453, in wrapper
    return fn(x)
           ^^^^^
  File "/workspace/dcp-work-dcp-tc/pytorch/test/dynamo/test_id.py", line 443, in fn0
    return id()
           ^^^^

Set TORCHDYNAMO_VERBOSE=1 for the internal stack trace (please do this especially if you're reporting a bug to PyTorch). For even more developer context, set TORCH_LOGS="+dynamo"


To execute this test, run the following from the base repo dir:
    python test/dynamo/test_id.py IdTests.test_id_wrong_arg_count

This message can be suppressed by setting PYTORCH_PRINT_REPRO_ON_FAILURE=0


```


## 期望
和pytorch抛的异常一致

## 评论 (1)

### ascend-robot · 2026-08-13

Hello,

This repo is only a mirror with no active development or maintenance.
All bug reports, questions and code contributions should be submitted via the original repository link below.
Thanks for your interest!

Original Repository Link: https://gitcode.com/Ascend/pytorch
