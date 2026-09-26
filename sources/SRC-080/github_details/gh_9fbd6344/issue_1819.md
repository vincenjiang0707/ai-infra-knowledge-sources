# [Issue #1819] distill.py fails with AttributeError: DistillQwen3VLModel has no attribute 'output_layer' when using Qwen3.5-0.8B as student/teacher

source: https://github.com/NVIDIA/Model-Optimizer/issues/1819
state: open | updated: 2026-06-25T08:41:10Z
labels: feature request

## 正文

branch: dkorzekwa/claude_qwen35_distill (create a few days ago from modelopt main)
container: nemo_26_06

Steps to reproduce

```
PYTHONPATH=/workspace/Model-Optimizer:$PYTHONPATH \
torchrun --nnodes 1 --nproc_per_node 1 \
    examples/megatron_bridge/distill.py \
    --tp_size 1 \
    --teacher_hf_path /workspace/hf_models/Qwen/Qwen3.5-0.8B \
    --student_hf_path /workspace/hf_models/Qwen/Qwen3.5-0.8B \
    --student_hf_model /workspace/hf_models/Qwen/Qwen3.5-0.8B \
    --use_mock_data \
    --seq_length 512 --mbs 1 --gbs 8 --train_iters 10 \
    --kd_loss_scale 1.0 \
    --output_dir /tmp/distill_test \
    --hf_export_path /tmp/distill_test/hf
```

Error
AttributeError: DistillQwen3VLModel has no attribute `output_layer`

Full traceback location:
- modelopt/torch/distill/mode.py:189 → _convert_for_kd
- modelopt/torch/distill/distillation_model.py:88 → self.get_submodule(student_layer_name)

## 评论 (1)

### kevalmorabia97 · 2026-06-25

VLM Distillation is not yet supported. I'm working on supporting it where we can distill language model from VLM teacher to VLM student using text-only data as initial support 
