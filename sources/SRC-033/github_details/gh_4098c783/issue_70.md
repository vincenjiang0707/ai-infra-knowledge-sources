# [Issue #70] 双卡运行timm训练报错

source: https://github.com/Ascend/pytorch/issues/70
state: open | updated: 2025-07-03T03:54:33Z
labels: 

## 正文

一、问题现象（附报错日志上下文）：
按照官方example：https://ascend.github.io/docs/sources/timm/quick_start.html
进行timm训练报错，单卡没问题，双卡会报错，如下：

```
Training in distributed mode with multiple processes, 1 device per process.Process 0, total 2, device npu:0.
Training in distributed mode with multiple processes, 1 device per process.Process 1, total 2, device npu:1.
Model seresnet34 created, param count:21960416
Data processing configuration for current model + dataset:
        input_size: (3, 224, 224)
        interpolation: bicubic
        mean: (0.485, 0.456, 0.406)
        std: (0.229, 0.224, 0.225)
        crop_pct: 0.875
        crop_mode: center
npu:0 Model is on device: npu:0
Created SGD (sgd) optimizer: lr: 0.4, momentum: 0.9, dampening: 0, weight_decay: 2e-05, nesterov: True, maximize: False, foreach: None, differentiable: False
AMP not enabled. Training in torch.float32.
Using native Torch DistributedDataParallel.
npu:0 2 Model is on device: npu:0
npu:1 Model is on device: npu:1
npu:1 2 Model is on device: npu:1
Traceback (most recent call last):
  File "/home/ma-user/work/mobilenetv5/train.py", line 1376, in <module>
Traceback (most recent call last):
  File "/home/ma-user/work/mobilenetv5/train.py", line 1376, in <module>
    main()
  File "/home/ma-user/work/mobilenetv5/train.py", line 659, in main
    main()
  File "/home/ma-user/work/mobilenetv5/train.py", line 659, in main
    model = NativeDDP(model, device_ids=[device], broadcast_buffers=not args.no_ddp_bb)
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/torch/nn/parallel/distributed.py", line 795, in __init__
    model = NativeDDP(model, device_ids=[device], broadcast_buffers=not args.no_ddp_bb)
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/torch/nn/parallel/distributed.py", line 795, in __init__
    _verify_param_shape_across_processes(self.process_group, parameters)
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/torch/distributed/utils.py", line 265, in _verify_param_shape_across_processes
    return dist._verify_params_across_processes(process_group, tensors, logger)
RuntimeError:     DDP expects same model across all ranks, but Rank 0 has 174 params, while rank 1 has inconsistent 0 params._verify_param_shape_across_processes(self.process_group, parameters)

  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/torch/distributed/utils.py", line 265, in _verify_param_shape_across_processes
    return dist._verify_params_across_processes(process_group, tensors, logger)
RuntimeError: DDP expects same model across all ranks, but Rank 1 has 174 params, while rank 1 has inconsistent 0 params.
[ERROR] 2025-07-02-12:55:54 (PID:1922331, Device:0, RankID:-1) ERR99999 UNKNOWN application exception
[2025-07-02 12:56:00,762] torch.distributed.elastic.multiprocessing.api: [WARNING] Sending process 1922332 closing signal SIGTERM
[2025-07-02 12:56:04,482] torch.distributed.elastic.multiprocessing.api: [ERROR] failed (exitcode: 1) local_rank: 0 (pid: 1922331) of binary: /home/ma-user/anaconda3/envs/PyTorch-2.1.0/bin/python3.1
Traceback (most recent call last):
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/bin/torchrun", line 8, in <module>
    sys.exit(main())
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 346, in wrapper
    return f(*args, **kwargs)
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/torch/distributed/run.py", line 806, in main
    run(args)
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/torch/distributed/run.py", line 797, in run
    elastic_launch(
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/torch/distributed/launcher/api.py", line 134, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/torch/distributed/launcher/api.py", line 264, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
============================================================
train.py FAILED
------------------------------------------------------------
Failures:
  <NO_OTHER_FAILURES>
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2025-07-02_12:56:00
  host      : notebook-007639f6-635f-4b82-87f4-fb0622e29c33.notebook-007639f6-635f-4b82-87f4-fb0622e29c33-distributed.default.svc.cluster.local
  rank      : 0 (local_rank: 0)
  exitcode  : 1 (pid: 1922331)
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
(PyTorch-2.1.0) [ma-user mobilenetv5]$/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 30 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
```

二、软件版本:
-- CANN 版本 (e.g., CANN 3.0.x，5.x.x):  cann_8.0.0
--Tensorflow/Pytorch/MindSpore 版本: pytorch_2.1.0
--Python 版本 (e.g., Python 3.7.5): py_3.10
-- MindStudio版本 (e.g., MindStudio 2.0.0 (beta3)): NA
--操作系统版本 (e.g., Ubuntu 18.04): euler_2.10.11-aarch64

三、测试步骤：
num_npus=2
./distributed_train.sh $num_npus path/to/dataset/ImageNet-1000 \
    --device npu \
    --model seresnet34 \
    --sched cosine \
    --epochs 150 \
    --warmup-epochs 5 \
    --lr 0.4 \
    --reprob 0.5 \
    --remode pixel \
    --batch-size 32 \
    --amp -j 4


四、日志信息:
如上
请根据自己的运行环境参考以下方式搜集日志信息，如果涉及到算子开发相关的问题，建议也提供UT/ST测试和单算子集成测试相关的日志。


## 评论 (1)

### iamhankai · 2025-07-03

改用这个版本timm可以解决：
[https://github.com/huggingface/pytorch-image-models/pull/2102/commits/7333040c754571b384d3a1a04330c114f914d5f8](https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fhuggingface%2Fpytorch-image-models%2Fpull%2F2102%2Fcommits%2F7333040c754571b384d3a1a04330c114f914d5f8)
