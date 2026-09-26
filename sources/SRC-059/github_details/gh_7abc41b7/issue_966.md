# [Issue #966] 🚀[Fine-tuning] ERNIE-4.5-MoE Megatron Training Implementation and Best Practices👋

source: https://github.com/PaddlePaddle/ERNIE/issues/966
state: closed | updated: 2025-10-02T12:01:01Z
labels: 

## 正文

Thanks to the open-sourcing of the ERNIE-4.5 series—this is truly exciting.

We have added Megatron training support for both ERNIE-4.5 and ERNIE-4.5-MoE (CPT/SFT/DPO). For best practices, please refer to this PR: https://github.com/modelscope/ms-swift/pull/4757


Training shell:
```shell
# 4 * 51GiB, 16s/it
CUDA_VISIBLE_DEVICES=0,1,2,3 \
megatron sft \
    --load ERNIE-4.5-21B-A3B-PT-mcore \
    --dataset 'AI-ModelScope/alpaca-gpt4-data-zh#500' \
              'AI-ModelScope/alpaca-gpt4-data-en#500' \
              'swift/self-cognition#500' \
    --expert_model_parallel_size 4 \
    --moe_grouped_gemm true \
    --moe_shared_expert_overlap true \
    --moe_aux_loss_coeff 0.01 \
    --micro_batch_size 4 \
    --global_batch_size 16 \
    --recompute_granularity full \
    --recompute_method uniform \
    --recompute_num_layers 1 \
    --finetune true \
    --cross_entropy_loss_fusion true \
    --lr 1e-5 \
    --lr_warmup_fraction 0.05 \
    --min_lr 1e-6 \
    --save megatron_output/ERNIE-4.5-21B-A3B-PT \
    --eval_interval 100 \
    --save_interval 100 \
    --max_length 2048 \
    --max_epochs 1 \
    --num_workers 8 \
    --dataset_num_proc 8 \
    --no_save_optim true \
    --no_save_rng true \
    --sequence_parallel true \
    --optimizer_cpu_offload true \
    --use_precision_aware_optimizer true \
    --attention_backend flash \
    --model_author swift \
    --model_name swift-robot
```

Training GPU memory usage:
![image](https://github.com/user-attachments/assets/734a9183-0148-4f09-bb1c-baa791ce6ed2)

Training log:
![image](https://github.com/user-attachments/assets/45fdc5d8-4b15-409f-a696-15f6dda13337)


Results:
![image](https://github.com/user-attachments/assets/cc55b412-935a-47e6-9ae3-2dd6b6d77b55)


## 评论 (2)

### lugimzzz · 2025-07-03

We're thrilled to see ERNIE model support integrated into MS-SWIFT! Thank you for making our model accessible through your excellent framework. Great work! 👏

### nepeplwu · 2025-10-02

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_
