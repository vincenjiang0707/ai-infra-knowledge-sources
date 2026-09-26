# [Issue #1430] ocr_v_sft采用lora训练后，测试模型报错

source: https://github.com/PaddlePaddle/ERNIE/issues/1430
state: open | updated: 2026-01-22T07:05:03Z
labels: 

## 正文

感谢伟大工程。
1、采用lora训练需要修改erniekit\train\ocr_vl_sft\pretraining_trainer.py的文件保存
`
def save_model(self, output_dir=None, merge_tensor_parallel=False):
        """
        Saves the model and associated configuration files to the specified directory.

        Args:
            output_dir (str, optional): Directory to save the model. Defaults to None.

        Returns:
            None

        Raises:
            None

        """
        super().save_model(output_dir,merge_tensor_parallel)
        if self.args.should_save:
            with open(
                os.path.join(output_dir, "static_name_to_dyg_name.json"), "w"
            ) as of:
                of.write(json.dumps(self.static_name_to_dyg_name))
`
2、配置文件为
`
### data
train_dataset_type: "erniekit"
eval_dataset_type: "erniekit"
train_dataset_path: "./train/train.jsonl"
train_dataset_prob: "1.0"
eval_dataset_path: "./train/val.jsonl"
eval_dataset_prob: "1.0"
max_seq_len: 16384
num_samples_each_epoch: 6000000
use_pic_id: False
sft_replace_ids: True
sft_image_normalize: True
sft_image_rescale: True
image_dtype: "float32"

### model
# model_name_or_path: PaddlePaddle/PaddleOCR-VL
model_name_or_path: "./pretrainmodel"
fine_tuning: LoRA
lora_rank: 32
fuse_rope: True
multimodal: True
use_flash_attention: True
use_sparse_flash_attn: True

### finetuning
# base
stage: OCR-VL-SFT
seed: 23
do_train: True
# do_eval: True
distributed_dataloader: False
dataloader_num_workers: 16
prefetch_factor: 10
batch_size: 20
packing_size: 8
packing: True
padding: False
num_train_epochs: 75
max_steps: 130000
# eval_batch_size: 8
# eval_iters: 50
# eval_steps: 100
# evaluation_strategy: steps
save_steps: 5000
save_total_limit: 5
save_strategy: steps
logging_steps: 5
release_grads: True
gradient_accumulation_steps: 8
logging_dir: ./PaddleOCR-VL-SFT-lora/tensorboard_logs/
output_dir: ./PaddleOCR-VL-SFT-lora
disable_tqdm: True

# train
warmup_steps: 10
learning_rate: 1.0e-4
lr_scheduler_type: cosine
min_lr: 1.0e-5
layerwise_lr_decay_bound: 1.0
from_scratch: 0

# optimizer
weight_decay: 0.1
adam_epsilon: 1.0e-8
adam_beta1: 0.9
adam_beta2: 0.95

# performance
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
# amp_master_grad: True
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
# unified_checkpoint_config: async_save
convert_from_hf: True
save_to_hf: True
`
3、训练保存的模型文件

<img width="502" height="722" alt="Image" src="https://github.com/user-attachments/assets/f89a1f7e-2d0a-4272-8bca-b0d99559fc6e" />
4、采用如下进行测试
`import json
import os
import shutil
from pathlib import Path
import paddle
from paddlex import create_model
import time

def batch_process_ocr(val_path, model_dir, output_folder="./output", batch_size=8):
    """批量处理OCR检测"""
    
    # 1. 加载数据
    with open(val_path, 'r') as f:
        samples = [json.loads(line) for line in f]
    
    print(f"加载 {len(samples)} 个样本")
    
    # 2. 准备batch数据
    batch_data = []
    for i, sample in enumerate(samples):
        sample['image'] = sample['image_info'][0]['image_url']
        sample['query'] = "OCR:"
        
        if os.path.exists(Path(sample['image'])):
            batch_data.append(sample)
        else:
            print(f"文件不存在: {sample['image']}")
    
    print(f"有效样本: {len(batch_data)} 个")
    
    # 3. 初始化模型
    model = create_model("PaddleOCR-VL-0.9B", model_dir=model_dir)
    os.makedirs(output_folder, exist_ok=True)
    
    # 4. Batch处理
    start = time.time()
    results, incorrect = [], 0
    
    for i in range(0, len(batch_data), batch_size):
        batch = batch_data[i:i + batch_size]
        
        # 批量预测
        batch_responses = []
        for sample in batch:
            try:
                res = next(model.predict(sample, max_new_tokens=2048, use_cache=True))
                batch_responses.append(res['result'])
            except Exception as e:
                print(f"预测失败: {e}")
                batch_responses.append("")
        
        # 处理结果
        for j, sample in enumerate(batch):
            if batch_responses[j]:  # 只处理成功预测的
                sample['response'] = batch_responses[j]
                gt_text = sample['text_info'][1]['text']
                print(sample['response'],",",gt_text)
                if gt_text != batch_responses[j]:
                    incorrect += 1
                    filename = Path(sample['image']).stem
                    dest = os.path.join(output_folder, f"{sample['response']}_{gt_text}.png")
                    shutil.copy2(sample['image'], dest)
                
                results.append(sample)
    
    # 5. 保存结果
    # with open("ocr_vl_sft-test_Bengali_response.jsonl", 'w') as f:
    #     for r in results:
    #         f.write(json.dumps(r, ensure_ascii=False) + '\n')
    
    # 6. 输出统计
    elapsed = time.time() - start
    print(f"\n总样本: {len(samples)} | 成功处理: {len(results)}")
    print(f"错误数: {incorrect} | 错误率: {incorrect/len(results):.4f}")
    print(f"耗时: {elapsed:.1f}秒 | 速度: {len(results)/elapsed:.1f} 样本/秒")

if __name__ == "__main__":
    batch_process_ocr(
        "./train/val.jsonl",
        # "./PaddleOCR-VL-SFT-Bengali/checkpoint-12800",
        "./PaddleOCR-VL-SFT-lora/checkpoint-10000/",
        batch_size=64
    )`
后进行报错

<img width="771" height="255" alt="Image" src="https://github.com/user-attachments/assets/0b67ea90-930d-4ed2-8a31-9aa686f3f37c" />


## 评论 (1)

### forBlank · 2026-01-22

ERNIEkit 1.4 不支持 PaddleOCR-VL LoRA，建议使用 PaddleFormers 1.0，可以参考 [PaddleFormers & PaddleOCR-VL Best Practices](https://github.com/PaddlePaddle/PaddleFormers/tree/release/v1.0/examples/best_practices/PaddleOCR-VL)
