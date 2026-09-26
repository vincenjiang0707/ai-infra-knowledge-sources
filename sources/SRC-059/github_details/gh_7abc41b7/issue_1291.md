# [Issue #1291] ModuleNotFoundError: No module named 'data_processor.steps'

source: https://github.com/PaddlePaddle/ERNIE/issues/1291
state: closed | updated: 2026-01-07T12:02:04Z
labels: 

## 正文

ernie训练出错

/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddle/utils/cpp_extension/extension_utils.py:717: UserWarning: No ccache found. Please be aware that recompiling all source files may be required. You can download and install ccache from: https://github.com/ccache/ccache/blob/master/doc/INSTALL.md
  warnings.warn(warning_message)
/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/_distutils_hack/__init__.py:30: UserWarning: Setuptools is replacing distutils. Support for replacing an already imported distutils is deprecated. In the future, this condition will fail. Register concerns at https://github.com/pypa/setuptools/issues/new?template=distutils-deprecation.yml
  warnings.warn(
None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
W0926 09:53:56.741303 90879 gpu_resources.cc:114] Please NOTE: device: 0, GPU Compute Capability: 8.0, Driver API Version: 12.8, Runtime API Version: 12.6
Traceback (most recent call last):
  File "/opt/conda/envs/python35-paddle120-env/bin/erniekit", line 33, in <module>
    sys.exit(load_entry_point('erniekit', 'console_scripts', 'erniekit')())
  File "/home/aistudio/ERNIE/erniekit/cli.py", line 72, in main
    from . import launcher
  File "/home/aistudio/ERNIE/erniekit/launcher.py", line 20, in <module>
    from erniekit.train.tuner import run_tuner
  File "/home/aistudio/ERNIE/erniekit/train/tuner.py", line 22, in <module>
    from .vl_sft import run_vl_sft
  File "/home/aistudio/ERNIE/erniekit/train/vl_sft/__init__.py", line 15, in <module>
    from .workflow import run_vl_sft
  File "/home/aistudio/ERNIE/erniekit/train/vl_sft/workflow.py", line 55, in <module>
    from data_processor.steps.end2end_processing import (
ModuleNotFoundError: No module named 'data_processor.steps'

下面是下载模型以及配置脚本相关

aistudio download --model PaddlePaddle/ERNIE-4.5-0.3B-Paddle --local_dir baidu/ERNIE-4.5-0.3B-Paddle

erniekit train examples/configs/ERNIE-4.5-0.3B/sft/run_sft_8k.yaml



### data
train_dataset_type: "erniekit"
eval_dataset_type: "erniekit"
train_dataset_path: "/home/aistudio/data/data348854/train-1000.jsonl"
train_dataset_prob: "1.0"
eval_dataset_path: "/home/aistudio/data/data348854/test-200.jsonl"
eval_dataset_prob: "1.0"
max_seq_len: 8192
num_samples_each_epoch: 6000000

### model
model_name_or_path: baidu/ERNIE-4.5-0.3B-Paddle
fine_tuning: Full
fuse_rope: True
use_sparse_head_and_loss_fn: True

### finetuning
# base
stage: SFT
seed: 23
do_train: True
do_eval: True
distributed_dataloader: False
dataloader_num_workers: 1
batch_size: 1
num_train_epochs: 1
max_steps: 100
max_evaluate_steps: 10000
eval_steps: 10000
evaluation_strategy: steps
save_steps: 10000000
save_total_limit: 5
save_strategy: steps
logging_steps: 1
release_grads: True
gradient_accumulation_steps: 8
logging_dir: ./vdl_log
output_dir: ./output
disable_tqdm: True

# train
warmup_steps: 20
learning_rate: 1.0e-5
lr_scheduler_type: cosine
min_lr: 1.0e-6
layerwise_lr_decay_bound: 1.0

# optimizer
weight_decay: 0.1
adam_epsilon: 1.0e-8
adam_beta1: 0.9
adam_beta2: 0.95
offload_optim: True

# performance
tensor_parallel_degree: 1
pipeline_parallel_degree: 1
sharding_parallel_degree: 1
sharding: stage1
sequence_parallel: True
pipeline_parallel_config: enable_delay_scale_loss enable_release_grads disable_partial_send_recv
recompute: False
recompute_use_reentrant: True
compute_type: bf16
fp16_opt_level: O2
disable_ckpt_quant: True
amp_master_grad: True
amp_custom_white_list:
  - lookup_table
  - lookup_table_v2
  - flash_attn
  - matmul
  - matmul_v2
  - fused_gemm_epilogue
amp_custom_black_list:
  - reduce_sum
  - softmax_with_cross_entropy
  - c_softmax_with_cross_entropy
  - elementwise_div
  - sin
  - cos
unified_checkpoint: True
unified_checkpoint_config: async_save


## 评论 (8)

### Jonathans575 · 2025-09-26

hello，你这是哪个分支的代码，什么方式安装的erniekit？
看起来是环境问题，和训练配置无关

### ZhijunLStudio · 2025-09-26

> hello，你这是哪个分支的代码，什么方式安装的erniekit？ 看起来是环境问题，和训练配置无关

今天早上新拉的
commit 8c94332492e07dfec206ddff50207682e3430b6b

安装方式为pip install -e .

### Jonathans575 · 2025-09-26

请检查下/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/data_processor是否存在，存在的话删掉再试一下

### ZhijunLStudio · 2025-09-26

没有这个文件

### Jonathans575 · 2025-09-26

麻烦重装一下erniekit试一下：
cd your_path_to_ERNIE
cd ..
pip uninstall erniekit
cd ERNIE
pip install -e .

我们也尝试复现一下

### ZhijunLStudio · 2025-09-27

重装之后报了这个错误
[2025-09-27 09:32:22,841] [   DEBUG] - world_size                    : 8
[2025-09-27 09:32:22,841] [   DEBUG] - zcc_ema_interval              : 1
[2025-09-27 09:32:22,841] [   DEBUG] - zcc_pipeline_hooks_capacity_usage: 0.6
[2025-09-27 09:32:22,841] [   DEBUG] - zcc_save_ema_coef             : None
[2025-09-27 09:32:22,841] [   DEBUG] - zcc_workers_num               : 3
[2025-09-27 09:32:22,841] [   DEBUG] - 
[2025-09-27 09:32:22,842] [    INFO] - Starting training from resume_from_checkpoint : None
W0927 09:32:22.843070  3484 nccl_comm_context.cc:70] ncclCommInitRankConfigMemOpt is not supported.
[2025-09-27 09:32:23,874] [    INFO] - [timelog] checkpoint loading time: 0.00s (2025-09-27 09:32:23) 
[2025-09-27 09:32:23,874] [    INFO] - ***** Running training *****
[2025-09-27 09:32:23,874] [    INFO] -   Num examples = 6,400
[2025-09-27 09:32:23,874] [    INFO] -   Num Epochs = 9223372036854775807
[2025-09-27 09:32:23,875] [    INFO] -   Instantaneous batch size per device = 1
[2025-09-27 09:32:23,875] [    INFO] -   Total train batch size (w. parallel, distributed & accumulation) = 64
[2025-09-27 09:32:23,875] [    INFO] -   Gradient Accumulation steps = 8
[2025-09-27 09:32:23,875] [    INFO] -   Total optimization steps = 100
[2025-09-27 09:32:23,875] [    INFO] -   Total num train samples = 6,400
[2025-09-27 09:32:23,876] [   DEBUG] -   Number of trainable parameters = 360,748,032 (per device)
[2025-09-27 09:32:23,895] [    INFO] - prepare SequenceDataset ...
[2025-09-27 09:32:27,045] [    INFO] - prepare SequenceDataset done: total number of examples is 6000000
W0927 09:32:28.693892  3484 multiply_fwd_func.cc:80] got different data type, run type promotion automatically, this may cause data type been changed.
Traceback (most recent call last):
  File "/home/aistudio/ERNIE/erniekit/launcher.py", line 46, in <module>
    launch()
  File "/home/aistudio/ERNIE/erniekit/launcher.py", line 34, in launch
    run_tuner()
  File "/home/aistudio/ERNIE/erniekit/train/tuner.py", line 65, in run_tuner
    _training_function(config={"args": args})
  File "/home/aistudio/ERNIE/erniekit/train/tuner.py", line 49, in _training_function
    run_sft(model_args, data_args, generating_args, finetuning_args)
  File "/home/aistudio/ERNIE/erniekit/train/sft/workflow.py", line 450, in run_sft
    train_result = trainer.train(resume_from_checkpoint=last_checkpoint)
  File "/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddleformers/trainer/trainer.py", line 1013, in train
    return self._inner_training_loop(
  File "/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddleformers/trainer/trainer.py", line 1262, in _inner_training_loop
    tr_loss_step = self.training_step(model, inputs, step_control=step_control)
  File "/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddleformers/trainer/trainer.py", line 2562, in training_step
    loss = self.compute_loss(model, inputs)
  File "/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddleformers/trainer/trainer.py", line 2502, in compute_loss
    outputs = model(**inputs)
  File "/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddle/nn/layer/layers.py", line 1571, in __call__
    return self.forward(*inputs, **kwargs)
  File "/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddle/distributed/parallel.py", line 571, in forward
    outputs = self._layers(*inputs, **kwargs)
  File "/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddle/nn/layer/layers.py", line 1571, in __call__
    return self.forward(*inputs, **kwargs)
  File "/home/aistudio/ERNIE/ernie/modeling_moe.py", line 1743, in forward
    return self.criterion(logits, labels, loss_mask, router_loss, mtp_logits)
  File "/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddle/nn/layer/layers.py", line 1571, in __call__
    return self.forward(*inputs, **kwargs)
  File "/home/aistudio/ERNIE/ernie/modeling_moe.py", line 1398, in forward
    res = super().forward(
  File "/home/aistudio/ERNIE/ernie/modeling.py", line 1321, in forward
    res = self.forward_impl(logits, masked_lm_labels, loss_mask)
  File "/home/aistudio/ERNIE/ernie/modeling.py", line 1440, in forward_impl
    masked_lm_loss = sb_loss_func(prediction_scores, masked_lm_labels)
  File "/home/aistudio/ERNIE/ernie/modeling.py", line 152, in wrapper
    return paddle.concat(outs, out_idx)
  File "/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddle/tensor/manipulation.py", line 1408, in concat
    return _C_ops.concat(input, axis)
ValueError: (InvalidArgument) concat(): argument 'x' (position 0) must be list of Tensors, but got empty list (at /paddle/paddle/fluid/pybind/eager_utils.cc:1393)

LAUNCH INFO 2025-09-27 09:32:31,869 Pod failed
LAUNCH ERROR 2025-09-27 09:32:31,869 Container failed !!!
Container rank 0 status failed cmd ['/opt/conda/envs/python35-paddle120-env/bin/python', '-u', '/home/aistudio/ERNIE/erniekit/launcher.py', 'train', 'examples/configs/ERNIE-4.5-0.3B/sft/yue_zh_sft_full.yaml'] code 1 log erniekit_dist_log/workerlog.0
LAUNCH INFO 2025-09-27 09:32:31,869 ------------------------- ERROR LOG DETAIL -------------------------
udio/ERNIE/erniekit/launcher.py", line 46, in <module>
    launch()
  File "/home/aistudio/ERNIE/erniekit/launcher.py", line 34, in launch
    run_tuner()
  File "/home/aistudio/ERNIE/erniekit/train/tuner.py", line 65, in run_tuner
    _training_function(config={"args": args})
  File "/home/aistudio/ERNIE/erniekit/train/tuner.py", line 49, in _training_function
    run_sft(model_args, data_args, generating_args, finetuning_args)
  File "/home/aistudio/ERNIE/erniekit/train/sft/workflow.py", line 450, in run_sft
    train_result = trainer.train(resume_from_checkpoint=last_checkpoint)
  File "/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddleformers/trainer/trainer.py", line 1013, in train
    return self._inner_training_loop(
  File "/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddleformers/trainer/trainer.py", line 1262, in _inner_training_loop
    tr_loss_step = self.training_step(model, inputs, step_control=step_control)
  File "/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddleformers/trainer/trainer.py", line 2562, in training_step
    loss = self.compute_loss(model, inputs)
  File "/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddleformers/trainer/trainer.py", line 2502, in compute_loss
    outputs = model(**inputs)
  File "/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddle/nn/layer/layers.py", line 1571, in __call__
    return self.forward(*inputs, **kwargs)
  File "/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddle/distributed/parallel.py", line 571, in forward
    outputs = self._layers(*inputs, **kwargs)
  File "/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddle/nn/layer/layers.py", line 1571, in __call__
    return self.forward(*inputs, **kwargs)
  File "/home/aistudio/ERNIE/ernie/modeling_moe.py", line 1743, in forward
    return self.criterion(logits, labels, loss_mask, router_loss, mtp_logits)
  File "/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddle/nn/layer/layers.py", line 1571, in __call__
    return self.forward(*inputs, **kwargs)
  File "/home/aistudio/ERNIE/ernie/modeling_moe.py", line 1398, in forward
    res = super().forward(
  File "/home/aistudio/ERNIE/ernie/modeling.py", line 1321, in forward
    res = self.forward_impl(logits, masked_lm_labels, loss_mask)
  File "/home/aistudio/ERNIE/ernie/modeling.py", line 1440, in forward_impl
    masked_lm_loss = sb_loss_func(prediction_scores, masked_lm_labels)
  File "/home/aistudio/ERNIE/ernie/modeling.py", line 152, in wrapper
    return paddle.concat(outs, out_idx)
  File "/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddle/tensor/manipulation.py", line 1408, in concat
    return _C_ops.concat(input, axis)
ValueError: (InvalidArgument) concat(): argument 'x' (position 0) must be list of Tensors, but got empty list (at /paddle/paddle/fluid/pybind/eager_utils.cc:1393)

LAUNCH INFO 2025-09-27 09:32:32,471 Exit code 1

### Jonathans575 · 2025-09-28

还是环境问题，develop和1.3分支需要paddle3.2，paddleformers>0.3
1.2分支及以下需要paddle3.1，paddleformers=0.2.4

### nepeplwu · 2026-01-07

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_
