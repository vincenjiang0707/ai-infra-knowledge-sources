# [Issue #1429] paddleocr-vl进行sft训练时报错ValueError: PaddleRecall error(102): LossNan. Loss contains inf or nan values, its value is nan

source: https://github.com/PaddlePaddle/ERNIE/issues/1429
state: open | updated: 2026-01-22T06:52:12Z
labels: 

## 正文

原来用A100-80GB训练，后改用Ada6000-48GB后训练第一步时出现以下报错，和A100训练时同样的数据集和配置文件，请问是什么原因呢？
[2026-01-19 17:43:11,367] [    INFO] - loss: 22.995561599731445, loss_cur_dp: 22.995561599731445, learning_rate: 1.666667e-06, global_step: 1, mem_allocated_gb: 13.636426, max_mem_allocated_gb: 19.670876, mem_reserved_gb: 33.954417, max_mem_reserved_gb: 45.060626, loss_scale: 32770.000000, global_runtime: 104.895400, global_samples_per_second: 0.610100, global_steps_per_second: 0.009500, tokens_trained_current_step: 524288, timestamp: 1768815791366, TFLOPS_per_sec_per_card: 23.853000, tokens_per_sec_per_card: 4980.700000, tokens_per_sec_per_card_average: 4980.700000, progress_or_epoch: 0.007700, data_id: 7, src_id: 0, data_type: 0
Traceback (most recent call last):
  File "/hy-tmp/ERNIE-release-v1.5/erniekit/launcher.py", line 58, in <module>
    launch()
  File "/hy-tmp/ERNIE-release-v1.5/erniekit/launcher.py", line 46, in launch
    run_tuner()
  File "/hy-tmp/ERNIE-release-v1.5/erniekit/train/tuner.py", line 82, in run_tuner
    _training_function(config={"args": args})
  File "/hy-tmp/ERNIE-release-v1.5/erniekit/train/tuner.py", line 64, in _training_function
    run_ocr_vl_sft(
  File "/hy-tmp/ERNIE-release-v1.5/erniekit/train/ocr_vl_sft/workflow.py", line 734, in run_ocr_vl_sft
    train_result = trainer.train(resume_from_checkpoint=checkpoint)
  File "/hy-tmp/ERNIE-release-v1.5/erniekit/train/ocr_vl_sft/trainer.py", line 362, in train
    return self._inner_training_loop(
  File "/hy-tmp/ERNIE-release-v1.5/erniekit/train/ocr_vl_sft/trainer.py", line 627, in _inner_training_loop
    self._check_loss_valid(tr_loss)
  File "/usr/local/miniconda3/envs/paddleocr-vl/lib/python3.10/site-packages/paddleformers/trainer/trainer.py", line 1773, in _check_loss_valid
    raise ValueError(f"{err_msg}. Loss contains inf or nan values, its value is {loss_value}")
ValueError: PaddleRecall error(102): LossNan. Loss contains inf or nan values, its value is nan

配置文件

train_dataset_type: "erniekit"
eval_dataset_type: "erniekit"
train_dataset_path: "./0112train/merged_output.jsonl"
train_dataset_prob: "1.0"

max_seq_len: 8192
num_samples_each_epoch: 6000000
use_pic_id: False
sft_replace_ids: True
sft_image_normalize: True
sft_image_rescale: True
image_dtype: "float32"

model_name_or_path: ./PaddleOCR-VL

fine_tuning: Full

multimodal: True
use_flash_attention: True
use_sparse_flash_attn: True


stage: OCR-VL-SFT
seed: 23
do_train: True
distributed_dataloader: False
dataloader_num_workers: 8
prefetch_factor: 10

batch_size: 8
packing_size: 1
gradient_accumulation_steps: 8

packing: True
padding: False
num_train_epochs: 1
max_steps: 17
save_steps: 10
save_total_limit: 2
save_strategy: steps
logging_steps: 1
release_grads: True

logging_dir: ./0112PaddleOCR-VL-SFT-table/tensorboard_logs/
output_dir: ./0112PaddleOCR-VL-SFT-table
disable_tqdm: True


warmup_steps: 10
learning_rate: 5.0e-6
lr_scheduler_type: cosine
min_lr: 5.0e-7
layerwise_lr_decay_bound: 1.0
from_scratch: 0


weight_decay: 0.1
adam_epsilon: 1.0e-8
adam_beta1: 0.9
adam_beta2: 0.95


tensor_parallel_degree: 1

pipeline_parallel_degree: 1
sharding_parallel_degree: 1

sharding: stage1

sequence_parallel: False
pipeline_parallel_config: enable_delay_scale_loss enable_release_grads disable_partial_send_recv
recompute: True
recompute_granularity: "full"
recompute_use_reentrant: True

compute_type: bf16

fp16_opt_level: O2
disable_ckpt_quant: True


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

convert_from_hf: True
save_to_hf: True


后面试着把compute_type由bf16改成fp16时训练学习率一直是0

## 评论 (3)

### a31413510 · 2026-01-20

麻烦提供一下训练脚本和训练配置

### HWChatGPT4 · 2026-01-20

> 麻烦提供一下训练脚本和训练配置

训练显卡：RTX Ada6000-48GB


训练脚本train.sh
```
CONFIG="./examples/configs/PaddleOCR-VL/sft/run_ocr_vl_sft_0112.yaml"
BASE_MODEL="./PaddleOCR-VL"
TRAIN_DATA="./0112train/merged_output.jsonl"
OUTPUT_DIR="./output_sft_$(date +%Y%m%d_%H%M%S)"

echo "配置文件: ${CONFIG}"
echo "基础模型: ${BASE_MODEL}"
echo "训练数据: ${TRAIN_DATA}"
echo "输出目录: ${OUTPUT_DIR}"

erniekit train \
    "${CONFIG}" \
    model_name_or_path="${BASE_MODEL}" \
    train_dataset_path="${TRAIN_DATA}" \
    output_dir="${OUTPUT_DIR}"

echo "✅ 训练成功完成！模型已保存至: ${OUTPUT_DIR}"
```

配置文件run_ocr_vl_sft_0112.yaml
```
train_dataset_type: "erniekit"
eval_dataset_type: "erniekit"
train_dataset_path: "./0112train/merged_output.jsonl"
train_dataset_prob: "1.0"

max_seq_len: 8192
num_samples_each_epoch: 6000000
use_pic_id: False
sft_replace_ids: True
sft_image_normalize: True
sft_image_rescale: True
image_dtype: "float32"

model_name_or_path: ./PaddleOCR-VL

fine_tuning: Full

multimodal: True
use_flash_attention: True
use_sparse_flash_attn: True

stage: OCR-VL-SFT
seed: 23
do_train: True
distributed_dataloader: False
dataloader_num_workers: 8
prefetch_factor: 10

batch_size: 8
packing_size: 1
gradient_accumulation_steps: 8

packing: True
padding: False
num_train_epochs: 1
max_steps: 17
save_steps: 10
save_total_limit: 2
save_strategy: steps
logging_steps: 1
release_grads: True

logging_dir: ./0112PaddleOCR-VL-SFT-table/tensorboard_logs/
output_dir: ./0112PaddleOCR-VL-SFT-table
disable_tqdm: True

warmup_steps: 10
learning_rate: 5.0e-6
lr_scheduler_type: cosine
min_lr: 5.0e-7
layerwise_lr_decay_bound: 1.0
from_scratch: 0

weight_decay: 0.1
adam_epsilon: 1.0e-8
adam_beta1: 0.9
adam_beta2: 0.95

tensor_parallel_degree: 1

pipeline_parallel_degree: 1
sharding_parallel_degree: 1

sharding: stage1

sequence_parallel: False
pipeline_parallel_config: enable_delay_scale_loss enable_release_grads disable_partial_send_recv
recompute: True
recompute_granularity: "full"
recompute_use_reentrant: True

compute_type: bf16

fp16_opt_level: O2
disable_ckpt_quant: True

amp_custom_white_list:

lookup_table
lookup_table_v2
flash_attn
matmul
matmul_v2
fused_gemm_epilogue
amp_custom_black_list:
reduce_sum
softmax_with_cross_entropy
c_softmax_with_cross_entropy
elementwise_div
sin
cos
unified_checkpoint: True
convert_from_hf: True
save_to_hf: True
```

 

### forBlank · 2026-01-22

@HWChatGPT4 我们没有在 Ada6000-48GB 上测试过 SFT。Loss 出现 NaN 可能是框架不同导致的算子精度问题。
