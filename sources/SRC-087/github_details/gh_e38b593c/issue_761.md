# [Issue #761] [Bug]: Finetuned Decoder Performs Worse Than Z-Lab Baseline on Finetuning Dataset

source: https://github.com/vllm-project/speculators/issues/761
state: open | updated: 2026-07-22T15:44:19Z
labels: bug

## 正文

### Your current environment

Please provide the following information about your environment if applicable:

- vLLM: 0.22.1
- Speculators: Mainline at `21033a7bb52b73d067c96e196b4186ff51321efd - Add D-PACE loss implementation for D-Flash training (#736)`
- CUDA: 13.2
- PyTorch: 2.11.0
- Transformers: 5.10.2
- Hardware: p5en for training & benchmarking
- Model: RedHatAI/Qwen3.6-35B-A3B-NVFP4


### 🐛 Describe the bug


## Context:
I am using this checkpoint of Z-Lab dflash decoder as a base model, finetuning with my own datatset. The finetuning dataset has a size of 30K. The Z-Lab baseline has been converted using Speculator's conversion method, so the target layer is offsetted by 1.
The uncoverted Z-Lab dflash decoder is here: https://huggingface.co/z-lab/Qwen3.6-35B-A3B-DFlash/blob/42d3b34d588423cdae7ba8f53a8cf7789346a719/config.json


I will provide the training commands below.

## Expectation
I would expect the finetuned decoder perform better on the finetuned dataset during benchmark. However, that is not the case

## Result

  | Position     | ZLab baseline | ZLab+30K finetune (20ep) | 30K prod-only (scratch) |
  |--------------|---------------|--------------------------|-------------------------|
  | 0            | 85.36         | 80.02                    | 64.89                   |
  | 1            | 77.03         | 67.50                    | 48.11                   |
  | 2            | 71.32         | 61.02                    | 37.00                   |
  | 3            | 67.27         | 55.49                    | 29.15                   |
  | 4            | 64.21         | 51.22                    | 23.21                   |
  | 5            | 61.43         | 47.15                    | 18.28                   |
  | 6            | 59.27         | 43.89                    | 14.39                   |
  | 7            | 57.44         | 39.80                    | 11.00                   |
  | Accept rate %| 67.91         | 55.76                    | 30.76                   |
  | Accept length| 6.43          | 5.46                     | 3.46                    |
  | Drafts       | 242,441       | 302,116                  | 140,153                 |
  | Accepted tok | 1,317,213     | 1,347,733                | 344,840                 |



## Reproducibility 
### Benchmark Command - In-Training-Distribution Benchmark:
`vllm bench serve --dataset-name custom --dataset-path /home/ec2-user/dflash_exp/dataset/benchmark/prod_sharegpt_5000_vllm_bench.jsonl --num-prompts 320 --max-concurrency 16 --model RedHatAI/Qwen3.6-35B-A3B-NVFP4 --base-url http://0.0.0.0:8000 --endpoint /v1/chat/completions --backend openai-chat --save-result --save-detailed --result-dir ./results/ --output-len 6144 --temperature=0
`

### ZLAB Baseline D-Flash Decoder

```
vllm serve RedHatAI/Qwen3.6-35B-A3B-NVFP4 \
  --speculative-config '{"method": "dflash", "model": "training_checkpoints/dflash_zlab_full_atten_speculators", "num_speculative_tokens": 8}' \
  --max-model-len 16384
```
```
---------------Speculative Decoding---------------
Acceptance rate (%):                     67.91     
Acceptance length:                       6.43      
Drafts:                                  242441    
Draft tokens:                            1939528   
Accepted tokens:                         1317213   
Per-position acceptance (%):
  Position 0:                            85.36     
  Position 1:                            77.03     
  Position 2:                            71.32     
  Position 3:                            67.27     
  Position 4:                            64.21     
  Position 5:                            61.43     
  Position 6:                            59.27     
  Position 7:                            57.44     
```

### ZLab + 30K Prod Data Finetuned Decoder + 20 Epochs
```
vllm serve RedHatAI/Qwen3.6-35B-A3B-NVFP4 \
  --speculative-config '{"method": "dflash", "model": "training_checkpoints/dflash_qwen36_A3B_prod_30k_zlab_finetune/checkpoints/19", "num_speculative_tokens": 8}' \
  --max-model-len 16384
```
```

---------------Speculative Decoding---------------
Acceptance rate (%):                     55.76     
Acceptance length:                       5.46      
Drafts:                                  302116    
Draft tokens:                            2416928   
Accepted tokens:                         1347733   
Per-position acceptance (%):
  Position 0:                            80.02     
  Position 1:                            67.50     
  Position 2:                            61.02     
  Position 3:                            55.49     
  Position 4:                            51.22     
  Position 5:                            47.15     
  Position 6:                            43.89     
  Position 7:                            39.80     
```

### 30K Prod Data Only
```
vllm serve RedHatAI/Qwen3.6-35B-A3B-NVFP4 \
  --speculative-config '{"method": "dflash", "model": "training_checkpoints/dflash_qwen36_A3B_prod_30k_zlab_layers_8L/checkpoints/checkpoint_best", "num_speculative_tokens": 8}' \
  --max-model-len 16384
```
```
---------------Speculative Decoding---------------
Acceptance rate (%):                     30.76     
Acceptance length:                       3.46      
Drafts:                                  140153    
Draft tokens:                            1121224   
Accepted tokens:                         344840    
Per-position acceptance (%):
  Position 0:                            64.89     
  Position 1:                            48.11     
  Position 2:                            37.00     
  Position 3:                            29.15     
  Position 4:                            23.21     
  Position 5:                            18.28     
  Position 6:                            14.39     
  Position 7:                            11.00     
```

## 评论 (9)

### huaxuan250 · 2026-07-09

# Training Setup and Metrics
## Training E2E Commands:

### Parsing Data
```
python speculators/scripts/prepare_data.py \
  --model RedHatAI/Qwen3.6-35B-A3B-NVFP4 \
  --data dataset/_prod_sharegpt_30k.jsonl \
  --output ./dataset_prepped/dflash_qwen36_A3B__prod_30k \
  --seq-length 10240 \
  --num-preprocessing-workers 10 \
  --overwrite
```

### HiddenState endpoint
```
python speculators/scripts/launch_vllm.py   RedHatAI/Qwen3.6-35B-A3B-NVFP4   --target-layer-ids 2 11 20 29 38 -- -tp 1 -dp 8 --port 8000 --gpu-memory-utilization 0.92 --max-model-len 16384
```

### HiddenState Generate
```
OMP_NUM_THREADS=12 python speculators/scripts/data_generation_offline.py \
    --preprocessed-data ./dataset_prepped/dflash_qwen36_A3B__prod_30k \
    --endpoint http://localhost:8000/v1 \
    --output dataset_hiddenstate/dflash_qwen36_A3B__prod_30k_zlab_converted_layers/hidden_states \
    --concurrency 512 \
    --validate-outputs
```

### Training
```
OMP_NUM_THREADS=12 torchrun --standalone --nproc_per_node 8 \
    speculators/scripts/train.py \
    --verifier-name-or-path RedHatAI/Qwen3.6-35B-A3B-NVFP4 \
    --from-pretrained /home/ec2-user/dflash_exp/training_checkpoints/dflash_zlab_full_atten_speculators \
    --data-path ./dataset_prepped/dflash_qwen36_A3B__prod_30k \
    --hidden-states-path ./dataset_hiddenstate/dflash_qwen36_A3B__prod_30k_zlab_converted_layers/hidden_states \
    --save-path ./training_checkpoints/dflash_qwen36_A3B__30k_zlab_finetune/checkpoints \
    --speculator-type dflash \
    --block-size 16 --max-anchors 1024 --dflash-decay-gamma 7 \
    --epochs 3 --lr 1e-4 --total-seq-len 10240 \
    --optimizer muon \
    --on-missing raise 2>&1 | tee train.log
```

## Finetuning's Validation Metrics
```
{
    "loss_epoch": 0.047563904361782476,
    "full_acc_epoch": 0.6515456965228638,
    "position_1_acc_epoch": 0.9316849537124142,
    "position_2_acc_epoch": 0.8645308162787831,
    "position_3_acc_epoch": 0.8103049545094972,
    "position_4_acc_epoch": 0.7635555854236816,
    "position_5_acc_epoch": 0.7225186990969029,
    "position_6_acc_epoch": 0.6859345527636705,
    "position_7_acc_epoch": 0.6528344397981383,
    "position_8_acc_epoch": 0.6228427446935161,
    "position_9_acc_epoch": 0.5961149342731321,
    "position_10_acc_epoch": 0.5712819086101962,
    "position_11_acc_epoch": 0.5488704747658627,
    "position_12_acc_epoch": 0.5277940354964923,
    "position_13_acc_epoch": 0.5087467038548004,
    "position_14_acc_epoch": 0.4906203917347284,
    "position_15_acc_epoch": 0.4728011581559472,
    "eal_epoch": 0.49550516448712423
}
```

## Z-Lab Dflash Decoder Config After Conversion:
```
{
  "architectures": [
    "DFlashDraftModel"
  ],
  "auto_map": {
    "": "config.DFlashSpeculatorConfig"
  },
  "aux_hidden_state_layer_ids": [
    2,
    11,
    20,
    29,
    38
  ],
  "block_size": 16,
  "draft_vocab_size": 248320,
  "dtype": "bfloat16",
  "mask_token_id": 248070,
  "max_anchors": 256,
  "sliding_window_non_causal": false,
  "speculators_config": {
    "algorithm": "dflash",
    "default_proposal_method": "greedy",
    "proposal_methods": [
      {
        "accept_tolerance": 0.0,
        "proposal_type": "greedy",
        "speculative_tokens": 15,
        "verifier_accept_k": 1
      }
    ],
    "verifier": {
      "architectures": [
        "Qwen3_5MoeForConditionalGeneration"
      ],
      "name_or_path": "RedHatAI/Qwen3.6-35B-A3B-NVFP4"
    }
  },
  "speculators_model_type": "dflash",
  "speculators_version": "0.7.0.dev0",
  "target_hidden_size": null,
  "tie_word_embeddings": false,
  "transformer_layer_config": {
    "attention_bias": false,
    "attention_dropout": 0.0,
    "bos_token_id": null,
    "dtype": "bfloat16",
    "eos_token_id": 248046,
    "head_dim": 128,
    "hidden_act": "silu",
    "hidden_size": 2048,
    "initializer_range": 0.02,
    "intermediate_size": 6144,
    "layer_types": [
      "full_attention",
      "full_attention",
      "full_attention",
      "full_attention",
      "full_attention",
      "full_attention",
      "full_attention",
      "full_attention"
    ],
    "max_position_embeddings": 262144,
    "max_window_layers": 8,
    "model_type": "qwen3",
    "num_attention_heads": 32,
    "num_hidden_layers": 8,
    "num_key_value_heads": 4,
    "pad_token_id": 248044,
    "rms_norm_eps": 1e-06,
    "rope_parameters": {
      "beta_fast": 32.0,
      "beta_slow": 1.0,
      "factor": 64.0,
      "original_max_position_embeddings": 4096,
      "rope_theta": 10000000,
      "rope_type": "yarn",
      "type": "yarn"
    },
    "sliding_window": null,
    "tie_word_embeddings": false,
    "use_cache": false,
    "use_sliding_window": false,
    "vocab_size": 248320
  },
  "transformers_version": "5.10.2"
}

```


### huaxuan250 · 2026-07-09

I am trying to see if there is an open sourced way to recreate this by finetuning with UltraChat dataset

### huaxuan250 · 2026-07-09

### Benchmarking using UltraChat
It really looks like somehow the Prod dataset regressed the baseline decoder a bit when benchmarking, regardless of benchmark data..


`vllm bench serve --dataset-name custom --dataset-path dataset/benchmark/ultrachat_Qwen3.6-35B-A3B-NVFP4-10k_vllm_bench.jsonl --num-prompts 320 --max-concurrency 16 --model RedHatAI/Qwen3.6-35B-A3B-NVFP4 --base-url http://0.0.0.0:8000 --endpoint /v1/chat/completions --backend openai-chat --save-result --save-detailed --result-dir ./results/ --output-len 1024 --temperature=0`


  | Position      | ZLab baseline | ZLab + UltraChat 10K finetune | ZLab + Prod 30K finetune |
  |---------------|---------------|---------------------------|----------------------|
  | 0             | 71.22         | 70.60                     | 46.37                |
  | 1             | 48.29         | 48.21                     | 21.94                |
  | 2             | 34.00         | 34.06                     | 12.26                |
  | 3             | 25.35         | 25.51                     |  7.36                |
  | 4             | 19.65         | 19.62                     |  4.19                |
  | 5             | 15.39         | 15.36                     |  2.55                |
  | 6             | 12.16         | 12.01                     |  1.58                |
  | 7             |  9.60         |  9.42                     |  1.10                |
  | Accept rate % | 29.46         | 29.35                     | 12.17                |
  | Accept length |  3.36         |  3.35                     |  1.97                |
  | Drafts        | 96,076        | 96,063                    | 163,758              |
  | Accepted tok  | 226,414       | 225,542                   | 159,439              |



### huaxuan250 · 2026-07-09

 1. UltraChat finetune ≈ baseline (3.35 vs 3.36) — essentially identical, at every position. Finetuning z-lab on UltraChat data changed nothing. So the finetuning procedure itself is harmless — it doesn't damage z-lab when the data matches. This rules out "finetuning/LR/pipeline always degrades z-lab." The muon-1e-4 test is now unnecessary — this already proves light or matched finetuning preserves z-lab.

  2. prod finetune collapses on UltraChat (1.97, half of baseline). This is the key contrast. The prod-finetuned model, tested on UltraChat, is far worse than baseline — because it was pulled toward the prod distribution and away from general UltraChat. That's expected specialization... if prod finetuning worked on prod data. But you already showed prod finetune degraded on prod's own data too (5.46 < 6.43). So prod finetuning hurts everywhere.

  3. Therefore the problem is specifically the prod data, not the pipeline. UltraChat data → finetune is a no-op (harmless). prod data → finetune degrades on-domain and off-domain. The only variable that differs between the harmless run and the damaging run is the prod dataset itself.


I think I will have to regenerate the dataset even though the training/finetuning dataset is regenerated by the same model


### huaxuan250 · 2026-07-13

[temp_regen.py](https://github.com/user-attachments/files/29975588/temp_regen.py)

## Update: Root cause found — training-response distribution mismatch

Regenerating the responses in the 30K dataset with the target model itself AGAIN (same prompts, responses re-sampled from `RedHatAI/Qwen3.6-35B-A3B-NVFP4`) fully resolves the regression. The issue was not in speculators — the decoder was being trained on hidden states from force-decoding responses the target model would never emit, which diverge from the free-generation states seen at inference time.

<ins> **QQ: However, the original dataset is already obtained from production endpoint that has the same model and sampling params, why does regeneration introduce this delta?** </ins>

## Acceptance comparison - InDistribution Benchmark:
 (same benchmark as OP: 320 prompts, concurrency 16, temp 0, output-len 6144)
```
vllm bench serve --dataset-name custom --dataset-path /home/ec2-user/dflash_exp/dataset/benchmark/_prod_sharegpt_5000_vllm_bench.jsonl --num-prompts 320 --max-concurrency 16 --model RedHatAI/Qwen3.6-35B-A3B-NVFP4 --base-url http://0.0.0.0:8000 --endpoint /v1/chat/completions --backend openai-chat --save-result --save-detailed --result-dir ./results/ --output-len 6144 --temperature=0

```
| Position | Z-Lab base | +30K (20ep) | +30K regen (ep9) | +75K regen (ep17) | Scratch | Scratch regen 30k ep9 |  Scratch regen 75k ep9 
  |---|---|---|---|---|---|---|---|
  | 0 | 85.36 | 80.02 | **87.23** | 85.63 | 64.89 | 83.63 | 82.55 |
  | 1 | 77.03 | 67.50 | **79.22** | 78.92 | 48.11 | 68.28 | 65.63 |
  | 2 | 71.32 | 61.02 | **74.02** | 73.72 | 37.00 | 56.75 |52.72|
  | 3 | 67.27 | 55.49 | **70.18** | 69.35 | 29.15 | 48.01 |44.20|
  | 4 | 64.21 | 51.22 | **66.98** | 65.87 | 23.21 | 41.44 |37.20|
  | 5 | 61.43 | 47.15 | **64.00** | 62.83 | 18.28 | 36.17 |31.69|
  | 6 | 59.27 | 43.89 | **61.97** | 60.54 | 14.39 | 31.91 |27.32|
  | 7 | 57.44 | 39.80 | **59.65** | 58.06 | 11.00 | 28.30 |23.70|
  | **Accept %** | 67.91 | 55.76 | **70.41** | 69.36 | 30.76 | 49.31 |45.63|
  | **Accept len** | 6.43 | 5.46 | **6.63** | 6.55 | 3.46 | 4.94 |4.65|

Also attached my own regeneration script below

### huaxuan250 · 2026-07-13

Was expecting a much better performance with 30K finetuning though, let me try to start a new suite with 75K.

30K and 75K regen converge to similar serving performance despite different training metrics (75K is better in training metrics)

Column 4: 30K's Loss (ep0 to ep9)
```
train-30k.log:[22:53:52] INFO     val/loss_epoch=0.045, val/full_acc_epoch=0.674, val/position_1_acc_epoch=0.932,     trainer.py:490
train-30k.log:[23:42:29] INFO     val/loss_epoch=0.043, val/full_acc_epoch=0.684, val/position_1_acc_epoch=0.936,     trainer.py:490
train-30k.log:[00:31:04] INFO     val/loss_epoch=0.041, val/full_acc_epoch=0.692, val/position_1_acc_epoch=0.938,     trainer.py:490
train-30k.log:[01:19:29] INFO     val/loss_epoch=0.041, val/full_acc_epoch=0.695, val/position_1_acc_epoch=0.939,     trainer.py:490
train-30k.log:[02:07:55] INFO     val/loss_epoch=0.041, val/full_acc_epoch=0.698, val/position_1_acc_epoch=0.940,     trainer.py:490
train-30k.log:[02:56:37] INFO     val/loss_epoch=0.042, val/full_acc_epoch=0.699, val/position_1_acc_epoch=0.940,     trainer.py:490
train-30k.log:[03:45:16] INFO     val/loss_epoch=0.042, val/full_acc_epoch=0.700, val/position_1_acc_epoch=0.941,     trainer.py:490
train-30k.log:[04:33:52] INFO     val/loss_epoch=0.043, val/full_acc_epoch=0.700, val/position_1_acc_epoch=0.941,     trainer.py:490
train-30k.log:[05:22:39] INFO     val/loss_epoch=0.043, val/full_acc_epoch=0.700, val/position_1_acc_epoch=0.941,     trainer.py:490
train-30k.log:[06:11:25] INFO     val/loss_epoch=0.043, val/full_acc_epoch=0.700, val/position_1_acc_epoch=0.941,     trainer.py:490
```

Column 5: 75K's loss (ep8 to ep17):
```
trai-75k.log:[21:34:07] INFO     val/loss_epoch=0.039, val/full_acc_epoch=0.711, val/position_1_acc_epoch=0.943, val/position_2_acc_epoch=0.894, val/position_3_acc_epoch=0.853, val/position_4_acc_epoch=0.815,                 trainer.py:490
trai-75k.log:[23:34:36] INFO     val/loss_epoch=0.039, val/full_acc_epoch=0.711, val/position_1_acc_epoch=0.943, val/position_2_acc_epoch=0.895, val/position_3_acc_epoch=0.853, val/position_4_acc_epoch=0.815,                 trainer.py:490
trai-75k.log:[01:34:34] INFO     val/loss_epoch=0.040, val/full_acc_epoch=0.711, val/position_1_acc_epoch=0.943, val/position_2_acc_epoch=0.895, val/position_3_acc_epoch=0.853, val/position_4_acc_epoch=0.815,                 trainer.py:490
trai-75k.log:[03:35:12] INFO     val/loss_epoch=0.040, val/full_acc_epoch=0.712, val/position_1_acc_epoch=0.944, val/position_2_acc_epoch=0.895, val/position_3_acc_epoch=0.853, val/position_4_acc_epoch=0.816,                 trainer.py:490
trai-75k.log:[05:35:39] INFO     val/loss_epoch=0.040, val/full_acc_epoch=0.712, val/position_1_acc_epoch=0.944, val/position_2_acc_epoch=0.895, val/position_3_acc_epoch=0.854, val/position_4_acc_epoch=0.816,                 trainer.py:490
trai-75k.log:[07:36:09] INFO     val/loss_epoch=0.041, val/full_acc_epoch=0.712, val/position_1_acc_epoch=0.944, val/position_2_acc_epoch=0.895, val/position_3_acc_epoch=0.854, val/position_4_acc_epoch=0.816,                 trainer.py:490
trai-75k.log:[09:36:43] INFO     val/loss_epoch=0.041, val/full_acc_epoch=0.712, val/position_1_acc_epoch=0.944, val/position_2_acc_epoch=0.895, val/position_3_acc_epoch=0.853, val/position_4_acc_epoch=0.816,                 trainer.py:490
trai-75k.log:[11:37:20] INFO     val/loss_epoch=0.041, val/full_acc_epoch=0.712, val/position_1_acc_epoch=0.944, val/position_2_acc_epoch=0.895, val/position_3_acc_epoch=0.854, val/position_4_acc_epoch=0.816,                 trainer.py:490
trai-75k.log:[13:37:50] INFO     val/loss_epoch=0.041, val/full_acc_epoch=0.712, val/position_1_acc_epoch=0.944, val/position_2_acc_epoch=0.895, val/position_3_acc_epoch=0.854, val/position_4_acc_epoch=0.816,                 trainer.py:490
trai-75k.log:[15:38:21] INFO     val/loss_epoch=0.041, val/full_acc_epoch=0.712, val/position_1_acc_epoch=0.944, val/position_2_acc_epoch=0.895, val/position_3_acc_epoch=0.853, val/position_4_acc_epoch=0.816,                 trainer.py:490
```

### huaxuan250 · 2026-07-16

  ## Out-of-Distribution Benchmark (Tail 5000, never seen in training)

  | Position | +30K regen finetune (ep9) | +75K regen finetune (ep17) | Scratch 30K regen (ep9) | Scratch 75K regen (ep9) |
  |---|---|---|---|---|
  | 0 | 86.46 | 86.50 | 82.51 | 82.38 |
  | 1 | 78.89 | 78.22 | 66.21 | 65.54 |
  | 2 | 73.48 | 72.78 | 54.18 | 52.62 |
  | 3 | 69.49 | 68.12 | 45.31 | 43.92 |
  | 4 | 66.52 | 64.72 | 38.51 | 36.86 |
  | 5 | 63.88 | 61.74 | 33.33 | 31.18 |
  | 6 | 61.69 | 59.17 | 29.03 | 26.81 |
  | 7 | 59.79 | 57.09 | 25.50 | 23.10 |
  | **Accept %** | 70.03 | 68.54 | 46.83 | 45.30 |
  | **Accept len** | 6.60 | 6.48 | 4.75 | 4.62 |

### shanjiaz · 2026-07-22

@huaxuan250 Thanks for sharing, this is great! Glad you figured it out. Were you able to pin point the regen issue? Do you think our doc needs clarification? 

### huaxuan250 · 2026-07-22

@shanjiaz I wasn't able to RCA why regen solves the issue. Also I still don't understand why training with more data leads to a worse performance...
