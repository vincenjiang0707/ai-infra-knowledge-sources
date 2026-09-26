# [Issue #1392] TypeError: (InvalidType) Type promotion only support calculations between floating-point numbers and between complex and real numbers. But got different data type x: int64, y: int32. (at /paddle/paddle/phi/common/type_promotion.h:228)

source: https://github.com/PaddlePaddle/ERNIE/issues/1392
state: open | updated: 2026-01-23T03:08:43Z
labels: 

## 正文

[环境]
paddlepaddle-gpu==3.2.0
erniekit==0.0.0         /home/aistudio/ERNIE

[运行]
erniekit train ERNIE/examples/configs/ERNIE-4.5-21B-A3B/sft/run_sft_lora_8k.yaml

[报错]
Traceback (most recent call last):
  File "/home/ERNIE-develop/erniekit/launcher.py", line 46, in <module>
    launch()
  File "/home/ERNIE-develop/erniekit/launcher.py", line 34, in launch
    run_tuner()
  File "/home/ERNIE-develop/erniekit/train/tuner.py", line 65, in run_tuner
    _training_function(config={"args": args})
  File "/home/ERNIE-develop/erniekit/train/tuner.py", line 49, in _training_function
    run_sft(model_args, data_args, generating_args, finetuning_args)
  File "/home/ERNIE-develop/erniekit/train/sft/workflow.py", line 532, in run_sft
    train_result = trainer.train(resume_from_checkpoint=last_checkpoint)
  File "/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddleformers/trainer/trainer.py", line 1172, in train
    return self._inner_training_loop(
  File "/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddleformers/trainer/trainer.py", line 1424, in _inner_training_loop
    tr_loss_step = self.training_step(model, inputs, step_control=step_control)
  File "/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddleformers/trainer/trainer.py", line 2782, in training_step
    loss = self.compute_loss(model, inputs)
  File "/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddleformers/trainer/trainer.py", line 2722, in compute_loss
    outputs = model(**inputs)
  File "/home/aistudio/external-libraries/lib/python3.10/site-packages/paddle/nn/layer/layers.py", line 1576, in __call__
    return self.forward(*inputs, **kwargs)
  File "/home/ERNIE-develop/ernie/modeling_moe.py", line 1917, in forward
    outputs = self.ernie(
  File "/home/aistudio/external-libraries/lib/python3.10/site-packages/paddle/nn/layer/layers.py", line 1576, in __call__
    return self.forward(*inputs, **kwargs)
  File "/home/ERNIE-develop/ernie/modeling_moe.py", line 1379, in forward
    layer_outputs = self.recompute_training(
  File "/home/ERNIE-develop/ernie/modeling_moe.py", line 1252, in recompute_training
    hidden_states = recompute(
  File "/home/aistudio/external-libraries/lib/python3.10/site-packages/paddle/distributed/fleet/utils/__init__.py", line 150, in recompute
    return fleet.recompute.recompute(function, *args, **kwargs)
  File "/home/aistudio/external-libraries/lib/python3.10/site-packages/paddle/distributed/fleet/recompute/recompute.py", line 715, in recompute
    return RecomputeFunction.apply(
  File "/home/aistudio/external-libraries/lib/python3.10/site-packages/paddle/distributed/fleet/recompute/recompute.py", line 238, in forward
    outputs = run_function(*args, **kwargs)
  File "/home/ERNIE-develop/ernie/modeling_moe.py", line 1248, in custom_forward
    return module(*inputs, output_gate_logits=False)
  File "/home/aistudio/external-libraries/lib/python3.10/site-packages/paddle/nn/layer/layers.py", line 1576, in __call__
    return self.forward(*inputs, **kwargs)
  File "/home/ERNIE-develop/ernie/modeling_moe.py", line 732, in forward
    hidden_states, _, router_loss, gate_logits = self.mlp(
  File "/home/aistudio/external-libraries/lib/python3.10/site-packages/paddle/nn/layer/layers.py", line 1576, in __call__
    return self.forward(*inputs, **kwargs)
  File "/home/ERNIE-develop/ernie/moe/moe_all_gather_layer.py", line 1122, in forward
    AlltoAllSmart.apply(
  File "/home/ERNIE-develop/ernie/moe/moe_all_gather_layer.py", line 406, in forward
    distributed_input_to_alltoall_out = paddle.maximum(
  File "/home/aistudio/external-libraries/lib/python3.10/site-packages/paddle/base/dygraph/generated_tensor_methods_patch.py", line 73, in _maximum
    return _C_ops.maximum(*args, **kwargs)
TypeError: (InvalidType) Type promotion only support calculations between floating-point numbers and between complex and real numbers. But got different data type x: int64, y: int32. (at /paddle/paddle/phi/common/type_promotion.h:228)

LAUNCH INFO 2025-12-05 03:28:16,962 Pod failed
LAUNCH ERROR 2025-12-05 03:28:16,962 Container failed !!!
Container rank 0 status failed cmd ['/opt/conda/envs/python35-paddle120-env/bin/python', '-u', '/home/ERNIE-develop/erniekit/launcher.py', 'train', 'ERNIE/examples/configs/ERNIE-4.5-21B-A3B/sft/run_sft_lora_8k.yaml'] code 1 log erniekit_dist_log/workerlog.0
LAUNCH INFO 2025-12-05 03:28:16,962 ------------------------- ERROR LOG DETAIL -------------------------
ers/trainer/trainer.py", line 1424, in _inner_training_loop
    tr_loss_step = self.training_step(model, inputs, step_control=step_control)
  File "/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddleformers/trainer/trainer.py", line 2782, in training_step
    loss = self.compute_loss(model, inputs)
  File "/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddleformers/trainer/trainer.py", line 2722, in compute_loss
    outputs = model(**inputs)
  File "/home/aistudio/external-libraries/lib/python3.10/site-packages/paddle/nn/layer/layers.py", line 1576, in __call__
    return self.forward(*inputs, **kwargs)
  File "/home/ERNIE-develop/ernie/modeling_moe.py", line 1917, in forward
    outputs = self.ernie(
  File "/home/aistudio/external-libraries/lib/python3.10/site-packages/paddle/nn/layer/layers.py", line 1576, in __call__
    return self.forward(*inputs, **kwargs)
  File "/home/ERNIE-develop/ernie/modeling_moe.py", line 1379, in forward
    layer_outputs = self.recompute_training(
  File "/home/ERNIE-develop/ernie/modeling_moe.py", line 1252, in recompute_training
    hidden_states = recompute(
  File "/home/aistudio/external-libraries/lib/python3.10/site-packages/paddle/distributed/fleet/utils/__init__.py", line 150, in recompute
    return fleet.recompute.recompute(function, *args, **kwargs)
  File "/home/aistudio/external-libraries/lib/python3.10/site-packages/paddle/distributed/fleet/recompute/recompute.py", line 715, in recompute
    return RecomputeFunction.apply(
  File "/home/aistudio/external-libraries/lib/python3.10/site-packages/paddle/distributed/fleet/recompute/recompute.py", line 238, in forward
    outputs = run_function(*args, **kwargs)
  File "/home/ERNIE-develop/ernie/modeling_moe.py", line 1248, in custom_forward
    return module(*inputs, output_gate_logits=False)
  File "/home/aistudio/external-libraries/lib/python3.10/site-packages/paddle/nn/layer/layers.py", line 1576, in __call__
    return self.forward(*inputs, **kwargs)
  File "/home/ERNIE-develop/ernie/modeling_moe.py", line 732, in forward
    hidden_states, _, router_loss, gate_logits = self.mlp(
  File "/home/aistudio/external-libraries/lib/python3.10/site-packages/paddle/nn/layer/layers.py", line 1576, in __call__
    return self.forward(*inputs, **kwargs)
  File "/home/ERNIE-develop/ernie/moe/moe_all_gather_layer.py", line 1122, in forward
    AlltoAllSmart.apply(
  File "/home/ERNIE-develop/ernie/moe/moe_all_gather_layer.py", line 406, in forward
    distributed_input_to_alltoall_out = paddle.maximum(
  File "/home/aistudio/external-libraries/lib/python3.10/site-packages/paddle/base/dygraph/generated_tensor_methods_patch.py", line 73, in _maximum
    return _C_ops.maximum(*args, **kwargs)
TypeError: (InvalidType) Type promotion only support calculations between floating-point numbers and between complex and real numbers. But got different data type x: int64, y: int32. (at /paddle/paddle/phi/common/type_promotion.h:228)

## 评论 (1)

### Jonathans575 · 2026-01-23

镜像已升级更新，麻烦重拉任务尝试
