# [Issue #62] RuntimeError: npuSynchronizeDevice:torch_npu/csrc/core/npu/NPUStream.cpp:435 NPU function error: aclrtSynchronizeDevice, error code is 507046

source: https://github.com/Ascend/pytorch/issues/62
state: open | updated: 2025-09-02T06:32:58Z
labels: 

## 正文

[rank7]: Traceback (most recent call last):
[rank7]:   File "/home/wepsdl/conda/lib/python3.10/site-packages/llamafactory/launcher.py", line 23, in <module>
[rank7]:     launch()
[rank7]:   File "/home/wepsdl/conda/lib/python3.10/site-packages/llamafactory/launcher.py", line 19, in launch
[rank7]:     run_exp()
[rank7]:   File "/home/wepsdl/conda/lib/python3.10/site-packages/llamafactory/train/tuner.py", line 93, in run_exp
[rank7]:     _training_function(config={"args": args, "callbacks": callbacks})
[rank7]:   File "/home/wepsdl/conda/lib/python3.10/site-packages/llamafactory/train/tuner.py", line 67, in _training_function
[rank7]:     run_sft(model_args, data_args, training_args, finetuning_args, generating_args, callbacks)
[rank7]:   File "/home/wepsdl/conda/lib/python3.10/site-packages/llamafactory/train/sft/workflow.py", line 51, in run_sft
[rank7]:     dataset_module = get_dataset(template, model_args, data_args, training_args, stage="sft", **tokenizer_module)
[rank7]:   File "/home/wepsdl/conda/lib/python3.10/site-packages/llamafactory/data/loader.py", line 324, in get_dataset
[rank7]:     with training_args.main_process_first(desc="pre-process dataset"):
[rank7]:   File "/home/wepsdl/conda/lib/python3.10/contextlib.py", line 135, in __enter__
[rank7]:     return next(self.gen)
[rank7]:   File "/home/wepsdl/conda/lib/python3.10/site-packages/transformers/training_args.py", line 2496, in main_process_first
[rank7]:     dist.barrier()
[rank7]:   File "/home/wepsdl/conda/lib/python3.10/site-packages/torch/distributed/c10d_logger.py", line 75, in wrapper
[rank7]:     return func(*args, **kwargs)
[rank7]:   File "/home/wepsdl/conda/lib/python3.10/site-packages/torch/distributed/distributed_c10d.py", line 3690, in barrier
[rank7]:     work.wait()
[rank7]: RuntimeError: npuSynchronizeDevice:torch_npu/csrc/core/npu/NPUStream.cpp:435 NPU function error: aclrtSynchronizeDevice, error code is 507046
[rank7]: [ERROR] 2025-03-08-16:21:40 (PID:524, Device:7, RankID:7) ERR00100 PTA call acl api failed
[rank7]: [Error]: In the specified timeout waiting event, all tasks in the specified stream are not completed. 
[rank7]:         Rectify the fault based on the error information in the ascend log.
[rank7]: EE1002: [PID: 524] 2025-03-08-16:21:40.515.589 Stream synchronize timeout. rtDeviceSynchronize execute failed, reason=[stream sync timeout]
[rank7]:         Possible Cause: 1. The timeout interval may be improperly set.
[rank7]:         Solution: 1. Check whether the timeout interval is properly set. 2. Check whether the network is normal.
[rank7]:         TraceBack (most recent call last):
[rank7]:         wait for compute device to finish failed, runtime result = 507046.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]

## 评论 (6)

### yunyiyun · 2025-03-29

看下是不是所有卡都报该错误，如果是的，可以减少数据量，或者升级到最新版本，配置更长的超时时间，https://www.hiascend.com/document/detail/zh/Pytorch/600/apiref/Envvariables/Envir_020.html

如果部分卡超时，麻烦提供下详细的plog日志信息

### Pe4nutZz · 2025-05-13

> 看下是不是所有卡都报该错误，如果是的，可以减少数据量，或者升级到最新版本，配置更长的超时时间，https://www.hiascend.com/document/detail/zh/Pytorch/600/apiref/Envvariables/Envir_020.html
> 
> 如果部分卡超时，麻烦提供下详细的plog日志信息

超时时间如何设置

### yunyiyun · 2025-05-13

> > 看下是不是所有卡都报该错误，如果是的，可以减少数据量，或者升级到最新版本，配置更长的超时时间，https://www.hiascend.com/document/detail/zh/Pytorch/600/apiref/Envvariables/Envir_020.html
> > 如果部分卡超时，麻烦提供下详细的plog日志信息
> 
> 超时时间如何设置

https://www.hiascend.com/document/detail/zh/Pytorch/600/apiref/Envvariables/Envir_020.html
通过ACL_DEVICE_SYNC_TIMEOUT该环境变量配置设备同步的超时时间

### Pe4nutZz · 2025-05-14

> > > 看下是不是所有卡都报该错误，如果是的，可以减少数据量，或者升级到最新版本，配置更长的超时时间，https://www.hiascend.com/document/detail/zh/Pytorch/600/apiref/Envvariables/Envir_020.html
> > > 如果部分卡超时，麻烦提供下详细的plog日志信息
> > 
> > 
> > 超时时间如何设置
> 
> https://www.hiascend.com/document/detail/zh/Pytorch/600/apiref/Envvariables/Envir_020.html 通过ACL_DEVICE_SYNC_TIMEOUT该环境变量配置设备同步的超时时间

改大了也没啥用

### yunyiyun · 2025-05-14

> > > > 看下是不是所有卡都报该错误，如果是的，可以减少数据量，或者升级到最新版本，配置更长的超时时间，https://www.hiascend.com/document/detail/zh/Pytorch/600/apiref/Envvariables/Envir_020.html
> > > > 如果部分卡超时，麻烦提供下详细的plog日志信息
> > > 
> > > 
> > > 超时时间如何设置
> > 
> > 
> > https://www.hiascend.com/document/detail/zh/Pytorch/600/apiref/Envvariables/Envir_020.html 通过ACL_DEVICE_SYNC_TIMEOUT该环境变量配置设备同步的超时时间
> 
> 改大了也没啥用

1、首先确认你的版本是否支持该环境变量，需要使用6.0.0及之后的torch_npu和配套的cann，可以通过调用torch_npu.npu.synchronize()，配置info级别的plog日志（export ASCEND_GLOBAL_LOG_LEVEL=1），观察是否调用aclrtSynchronizeDeviceWithTimeout判断是否支持该环境变量，或者如果是同步超时报错，报错的接口会显示aclrtSynchronizeDeviceWithTimeout而不是aclrtSynchronizeDevice

2、如果环境变量生效依旧无法解决，可以参考官网维护模块进行定位解决，或者提供使用的芯片，cann，torch_npu版本以及详细日志信息便于进一步定位分析
日志参考 https://www.hiascend.com/document/detail/zh/canncommercial/81RC1/developmentguide/maintenref/logreference/logreference_0001.html
故障处理
https://www.hiascend.com/document/detail/zh/canncommercial/81RC1/developmentguide/maintenref/troubleshooting/troubleshooting_0001.html

### apoot9999 · 2025-09-02

试试改HCCL_EXEC_TIMEOUT，默认1800（半小时），调大点试试
