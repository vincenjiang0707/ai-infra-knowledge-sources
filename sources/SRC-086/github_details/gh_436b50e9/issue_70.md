# [Issue #70] Training Medusa heads

source: https://github.com/FasterDecoding/Medusa/issues/70
state: open | updated: 2025-08-02T00:08:00Z
labels: 

## 正文

I am trying to train Medusa heads (first on the dataset provided as example, than on my own, much smaller dataset). 
I am working on Azure Compute Instance where I have V100s (up to 8).

I am able to run inference even on instance with one GPU successfully (I guess that means I can load model into GPU? btw when I use instances with multiple GPUs I get errors that tensors are not on the same device).

Currently I'm trying to run training script on instance with 2 GPUs (I changed it to 2 nodes, not to use `bf16` since I don't have Ampere GPUs, reduced everything that I can and added `load_in_4bit`:

`torchrun --nproc_per_node=2 medusa/train/train.py --model_name_or_path lmsys/vicuna-7b-v1.3 \
    --data_path ShareGPT_Vicuna_unfiltered/ShareGPT_V4.3_unfiltered_cleaned_split.json \
    --bf16 False \
    --output_dir test \
    --num_train_epochs 1 \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 2 \
    --evaluation_strategy "no" \
    --save_strategy "no" \
    --learning_rate 1e-3 \
    --weight_decay 0.0 \
    --warmup_ratio 0.1 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --tf32 False \
    --model_max_length 512 \
    --lazy_preprocess True \
    --medusa_num_heads 3 \
    --medusa_num_layers 1 \
    --load_in_4bit True`


I have torch version 2.1.2+cu121 and CUDA 12.2. 

When I run the training script I get this:

`RuntimeError: cutlassF: no kernel found to launch!`
`torch.distributed.elastic.multiprocessing.errors.ChildFailedError: `


What am I doing wrong?

## 评论 (6)

### morganmcg1 · 2024-01-23

I see the train file is now called `train_legacy.py`, maybe changing `train.py` to `train_legacy.py` might help?

### ctlllll · 2024-01-24

Thanks for your interest! We have a legacy minimal training code for Medusa-1 in the old branch https://github.com/FasterDecoding/Medusa/tree/v0.1_backup, and some updated recipes available in a separate fork of axolotl (https://github.com/FasterDecoding/Medusa#training).

### mmilunovic-mdcs · 2024-02-05

Hey 😄 axolotl doesn't work for me for some weird reason. 

I'm trying to run a legacy training script. I reduced everything that I could (except sequence length). 

`torchrun --nproc_per_node=4 medusa/train/train_legacy.py --model_name_or_path lmsys/vicuna-7b-v1.3 \
    --data_path ShareGPT_Vicuna_unfiltered/ShareGPT_V4.3_unfiltered_cleaned_split.json \
    --bf16 False \
    --output_dir test \
    --num_train_epochs 1 \
    --per_device_train_batch_size 2 \
    --per_device_eval_batch_size 2 \
    --gradient_accumulation_steps 2 \
    --evaluation_strategy "no" \
    --save_strategy "no" \
    --learning_rate 1e-3 \
    --weight_decay 0.0 \
    --warmup_ratio 0.1 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --tf32 False \
    --model_max_length 2048 \
    --lazy_preprocess True \
    --medusa_num_heads 3 \
    --medusa_num_layers 1`


And I am still getting CUDA OOM on Azure instance with 4xV100 GPUs...
What takes up this much memory? 

### junphine · 2024-03-15

medusa_logits = logits[i, :, : -(2 + i)].contiguous()
medusa_labels = labels[..., 2 + i :].contiguous()

Why use 2 as start gap for logits and label align？

### callanwu · 2024-04-01

> medusa_logits = logits[i, :, : -(2 + i)].contiguous() medusa_labels = labels[..., 2 + i :].contiguous()
> 
> Why use 2 as start gap for logits and label align？

In conventional language modeling tasks, the objective is to predict the $x+1$-th token given a sequence of $x$ tokens. However, in the Medusa architecture, the training objective for the $i$-th head is to predict the $x+1+i$-th token, given a sequence of x tokens. Thus, in this framework, the initial loop corresponds to a prediction offset of $+2$, and as the loop iterates over different heads, the position of the token to be predicted continually increases.

https://github.com/FasterDecoding/Medusa/blob/5e980538695096e7e372c1e27a6bcf142bfeab11/medusa/train/train_legacy.py#L72-L81

### ksajan · 2024-08-25

@mmilunovic-mdcs Were you able to get this working I am not even able to follow any of the training examples given. Both legacy and new are giving me the same error that is Module not found huggingface_hub.error not found even though its present. No clue why. 
