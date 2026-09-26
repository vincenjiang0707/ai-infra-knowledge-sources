# [Issue #14] OOM question

source: https://github.com/FasterDecoding/Medusa/issues/14
state: closed | updated: 2023-09-15T01:19:58Z
labels: 

## 正文

Hi, I am very interested in your work, but when I tried to replicate it using four RTX 3090 graphics cards, I encountered an Out of Memory (OOM) issue. This is the script I am using.

`CUDA_VISIBLE_DEVICES=0,1,2,3
torchrun --nproc_per_node=4 medusa/train/train.py --model_name_or_path ~/Medusa-main/models/lmsys_vicuna-7b-v1.5 \
    --data_path ShareGPT_Vicuna_unfiltered/ShareGPT_V4.3_unfiltered_cleaned_split.json \
    --bf16 True \
    --output_dir test \
    --num_train_epochs 1 \
    --per_device_train_batch_size 4 \
    --per_device_eval_batch_size 8 \
    --gradient_accumulation_steps 8 \
    --evaluation_strategy "no" \
    --save_strategy "no" \
    --learning_rate 1e-3 \
    --weight_decay 0.0 \
    --warmup_ratio 0.1 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --tf32 True \
    --model_max_length 2048 \
    --lazy_preprocess True \
    --medusa_num_heads 3 \
    --medusa_num_layers 1 \`

I would like to know when you say you can train on four GPUs, what GPUs are they? thanks!

## 评论 (2)

### ctlllll · 2023-09-14

We used A100-80G for training. For RTX 3090, you may need to use a smaller batch size (e.g., bs=1). If it still cannot fit into a single GPU, you may want to try either a quantized base model (use `load_in_8bit` or `load_in_4bit`), or FSDP :)

### helldog-star · 2023-09-15

> We used A100-80G for training. For RTX 3090, you may need to use a smaller batch size (e.g., bs=1). If it still cannot fit into a single GPU, you may want to try either a quantized base model (use `load_in_8bit` or `load_in_4bit`), or FSDP :)

Thanks! I use a batch size of 1, and that works!
