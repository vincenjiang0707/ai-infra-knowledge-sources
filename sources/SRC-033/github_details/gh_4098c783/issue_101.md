# [Issue #101] SFTTrainer Out of Memory: Full-parameter fine-tuning on 8*910B (64G) for long context model Qwen3-4B-Instruct-2507.

source: https://github.com/Ascend/pytorch/issues/101
state: open | updated: 2026-01-21T04:16:32Z
labels: 

## 正文

Qwen3-4B-Instruct-2507 supports 256K token context. When I fine-tunes this model by using SFTTrainer with one training args of max_length=256K and DeepSpeed (Accelerate), OOM errors still occur during training. The deepspeed configuration is as follows:
```json
{
  "train_batch_size": "auto",
  "gradient_accumulation_steps": 2,
  "fp16": { "enabled": false },
  "bf16": { "enabled": true },
  "zero_optimization": {
    "stage": 3,
    "offload_optimizer": { "device": "cpu" },
    "offload_param": { "device": "cpu" },
    "contiguous_gradients": true,
    "overlap_comm": true,
    "allgather_bucket_size": 2e8,
    "reduce_bucket_size": 2e8,
    "stage3_prefetch_bucket_size": 2e8,
    "stage3_param_persistence_threshold": "auto",
    "stage3_max_live_parameters": 1e9,
    "stage3_max_reuse_distance": 1e9,
    "stage3_gather_16bit_weights_on_model_save": true
  },
  "activation_checkpointing": {
    "partition_activations": true,
    "cpu_checkpointing": false,
    "contiguous_memory_optimization": false,
    "number_checkpoints": null,
    "synchronize_checkpoint_boundary": false,
    "profile": false
  },
  "pipeline": {
    "pipeline_parallel_size": 1
  },
  "wall_clock_breakdown": false,
  "gradient_clipping": 1.0
}
```

The accelerate configuration is as follows:
```
compute_environment: LOCAL_MACHINE
debug: false
deepspeed_config:
  deepspeed_config_file: /path/to/deepspeed.json
  zero3_init_flag: false
distributed_type: DEEPSPEED
downcast_bf16: 'no'
enable_cpu_affinity: false
machine_rank: 0
main_training_function: main
num_machines: 1
num_processes: 8
rdzv_backend: static
same_network: true
tpu_env: []
tpu_use_cluster: false
tpu_use_sudo: false
use_cpu: false
```

I wonder if it is possible to train a long context model on an 8*910B (64G) machine. Thx!

## 评论 (1)

### fvfc-stpgh · 2026-01-21

Thank you for your feedback on this model training issue. Here are some suggestions for model optimization: https://www.hiascend.com/document/detail/zh/Pytorch/730/ptmoddevg/trainingmigrguide/PT_LMTMOG_0002.html.
To address the OOM issue, you can refer to this document: https://www.hiascend.com/document/detail/zh/Pytorch/730/ptmoddevg/Frameworkfeatures/docs/zh/framework_feature_guide_pytorch/virtual_memory.md.
Currently, our team has not conducted formal verification or optimization for training this model with DeepSpeed. For more targeted solutions, we suggest reaching out to the DeepSpeed official issues: https://github.com/microsoft/DeepSpeed/issues.
