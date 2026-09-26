# [Issue #286] Training loss does not decrease

source: https://github.com/SafeAILab/EAGLE/issues/286
state: open | updated: 2025-09-03T08:41:04Z
labels: 

## 正文

 when I use the **ultra_chat 200k** data (without regenerating the assistant data from the target model) to train the llama3.1-8b-instruct model, the **training acc is only around 35%** and **loss around 20**. I used 16xh100 and train_micro_batch_size_per_gpu=1 / gradient_accumulation_steps=2. It was found that the loss_mask generation method did not match the tokenizer. This problem has been fixed. Now it is ensured that the token after assistant is set to 1.  Anyone can help on this issue. Thanks a lot. 


Training Code:
commit : **e0d1b454ed4c2ead0aa1ef17fee1958b15965609**
**EAGLE/eagle/traineagle3**

training script:


```
torchrun \
    --nnodes 2\
    --nproc_per_node=8 \
    --node_rank 0 \
    --master_addr 127.0.0.1 \
    --master_port 8081 \
        main.py \
        --basepath $model_path \
        --trainpath $train_data_set \
        --testpath $test_data_set \
        --savedir $savedir \
        --deepspeed_config ds_config.json
```



config.json
```
{
  "architectures": [
    "LlamaForCausalLM"
  ],
  "bos_token_id": 128000,
  "eos_token_id": [
    128001,
    128008,
    128009
  ],
  "hidden_act": "silu",
  "hidden_size": 4096,
  "initializer_range": 0.02,
  "intermediate_size": 14336,
  "max_position_embeddings": 2048,
  "model_type": "llama",
  "num_attention_heads": 32,
  "num_key_value_heads": 8,
  "num_hidden_layers": 1,
  "pad_token_id": 128009,
  "rms_norm_eps": 1e-05,
  "tie_word_embeddings": false,
  "torch_dtype": "bfloat16",
  "transformers_version": "4.28.1",
  "use_cache": true,
  "vocab_size": 128256,
  "draft_vocab_size": 32000
}
```


ds_config.json :
```
{
    "bf16": {
        "enabled": "true",
        "auto_cast": "true"
    },
    "optimizer": {
        "type": "AdamW",
        "params": {
            "lr": 5e-5,
            "weight_decay": 0.0,
            "adam_w_mode": true,
            "betas": [
                    0.9,
                    0.95
                  ]
        }
    },
    "scheduler": {
        "type": "WarmupDecayLR",
        "params": {
            "warmup_min_lr": 5e-7,
            "warmup_max_lr": 5e-5,
            "warmup_num_steps": 5000,
            "total_num_steps": 230000
        }
    },
    "zero_optimization": {
        "stage": 2,
        "stage3_gather_16bit_weights_on_model_save": true,
        "allgather_partitions": true,
        "allgather_bucket_size": 2e8,
        "overlap_comm": true,
        "reduce_scatter": true,
        "reduce_bucket_size": 2e8,
        "contiguous_gradients": true
    },
    "gradient_accumulation_steps": 2,
    "gradient_clipping": 0.5,
    "steps_per_print": 1,
    "train_micro_batch_size_per_gpu": 1,
    "wall_clock_breakdown": false
}


```


## 评论 (3)

### fan-niu · 2025-08-21

For quick verification, I used 1024 data for training and expected 100 rounds of overfitting experiments. When I increased max_lr=1e-2 and min_lr=5e-4, I still only got the following acc on 100 epoch

Train Epoch [100/100], position 0,  Acc: 0.61
Train Epoch [100/100], position 1,  Acc: 0.30
Train Epoch [100/100], position 2,  Acc: 0.21
Train Epoch [100/100], position 3,  Acc: 0.16
Train Epoch [100/100], position 4,  Acc: 0.12
Train Epoch [100/100], position 5,  Acc: 0.10
Train Epoch [100/100], position 6,  Acc: 0.07
Train Epoch [100/100], position 0, pLoss: 1.60
Train Epoch [100/100], position 1, pLoss: 2.34
Train Epoch [100/100], position 2, pLoss: 2.69
Train Epoch [100/100], position 3, pLoss: 2.92
Train Epoch [100/100], position 4, pLoss: 3.10
Train Epoch [100/100], position 5, pLoss: 3.26
Train Epoch [100/100], position 6, pLoss: 3.41

### Mewo518 · 2025-08-25

I have also encountered this problem. Is there any expert who can help me solve this problem.

<img width="1668" height="318" alt="Image" src="https://github.com/user-attachments/assets/d5eeaa63-36ad-4b36-b61e-94ec8ba412eb" />

### KerwinKai · 2025-09-03

Refer to: https://github.com/SafeAILab/EAGLE/pull/274
