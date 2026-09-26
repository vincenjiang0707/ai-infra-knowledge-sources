# [Issue #613] [Bug]: RedHatAI/Qwen3.6-35B-A3B-NVFP4 - Dflash - Very Low Acceptance Despite Good Validation Metrics

source: https://github.com/vllm-project/speculators/issues/613
state: closed | updated: 2026-07-21T03:50:19Z
labels: bug

## 正文

### Your current environment

Please provide the following information about your environment if applicable:

- vLLM: 0.22.1 for Hidden State Extraction + Inference Benchmark 
- Speculators: Mainline `b6bccf38525971b7b9721a47d69e434fbce31391` as of 06/13/2025
- CUDA: 13.2
- PyTorch: 2.11.0
- Transformers: 5.10.2
- Hardware: p4de for benchmark, p5en for training
- Model: RedHatAI/Qwen3.6-35B-A3B-NVFP4


### 🐛 Describe the bug

# Overview:
Benchmarking with a subset of training data yields very low acceptance rate. 
Training data is 130K worth of at most 10240 context size of internal domain-specific prompts. 
Even when I invoke with a singular prompt (still in training distribution), the acceptance rate is very low.

Training's validation metrics seem fine and no anomalies. 

### Low Acceptance Rate:
```
(APIServer pid=1874323) INFO:     Started server process [1874323]
(APIServer pid=1874323) INFO:     Waiting for application startup.
(APIServer pid=1874323) INFO:     Application startup complete.
(Worker_TP0 pid=1875538) WARNING 06-16 19:27:42 [jit_monitor.py:103] Triton kernel JIT compilation during inference: _zero_kv_blocks_kernel. This causes a latency spike; consider extending warmup to cover this shape/config.
(Worker_TP0 pid=1875538) WARNING 06-16 19:27:42 [jit_monitor.py:103] Triton kernel JIT compilation during inference: _compute_slot_mapping_kernel. This causes a latency spike; consider extending warmup to cover this shape/config.
(Worker_TP0 pid=1875538) WARNING 06-16 19:27:42 [jit_monitor.py:103] Triton kernel JIT compilation during inference: eagle_prepare_next_token_padded_kernel. This causes a latency spike; consider extending warmup to cover this shape/config.
(Worker_TP0 pid=1875538) WARNING 06-16 19:27:42 [jit_monitor.py:103] Triton kernel JIT compilation during inference: copy_and_expand_dflash_inputs_kernel. This causes a latency spike; consider extending warmup to cover this shape/config.
(Worker_TP0 pid=1875538) WARNING 06-16 19:27:42 [jit_monitor.py:103] Triton kernel JIT compilation during inference: rejection_greedy_sample_kernel. This causes a latency spike; consider extending warmup to cover this shape/config.
(Worker_TP0 pid=1875538) WARNING 06-16 19:27:42 [jit_monitor.py:103] Triton kernel JIT compilation during inference: eagle_prepare_inputs_padded_kernel. This causes a latency spike; consider extending warmup to cover this shape/config.
(APIServer pid=1874323) INFO 06-16 19:27:45 [loggers.py:271] Engine 000: Avg prompt throughput: 390.7 tokens/s, Avg generation throughput: 28.9 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.8%, Prefix cache hit rate: 0.0%
(APIServer pid=1874323) INFO 06-16 19:27:45 [metrics.py:101] SpecDecoding metrics: Mean acceptance length: 1.23, Accepted throughput: 0.22 tokens/s, Drafted throughput: 7.73 tokens/s, Accepted: 54 tokens, Drafted: 1872 tokens, Per-position acceptance rate: 0.231, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, Avg Draft acceptance rate: 2.9%
(APIServer pid=1874323) INFO 06-16 19:27:55 [loggers.py:271] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 86.8 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.8%, Prefix cache hit rate: 0.0%
(APIServer pid=1874323) INFO 06-16 19:27:55 [metrics.py:101] SpecDecoding metrics: Mean acceptance length: 1.14, Accepted throughput: 10.60 tokens/s, Drafted throughput: 609.61 tokens/s, Accepted: 106 tokens, Drafted: 6096 tokens, Per-position acceptance rate: 0.139, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, Avg Draft acceptance rate: 1.7%
(APIServer pid=1874323) INFO 06-16 19:28:05 [loggers.py:271] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 81.7 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.9%, Prefix cache hit rate: 0.0%
(APIServer pid=1874323) INFO 06-16 19:28:05 [metrics.py:101] SpecDecoding metrics: Mean acceptance length: 1.12, Accepted throughput: 8.80 tokens/s, Drafted throughput: 583.12 tokens/s, Accepted: 88 tokens, Drafted: 5832 tokens, Per-position acceptance rate: 0.121, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, Avg Draft acceptance rate: 1.5%
(APIServer pid=1874323) INFO 06-16 19:28:15 [loggers.py:271] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 76.9 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.9%, Prefix cache hit rate: 0.0%
(APIServer pid=1874323) INFO 06-16 19:28:15 [metrics.py:101] SpecDecoding metrics: Mean acceptance length: 1.10, Accepted throughput: 7.10 tokens/s, Drafted throughput: 558.37 tokens/s, Accepted: 71 tokens, Drafted: 5584 tokens, Per-position acceptance rate: 0.102, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, Avg Draft acceptance rate: 1.3%
(APIServer pid=1874323) INFO 06-16 19:28:25 [loggers.py:271] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 72.5 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.9%, Prefix cache hit rate: 0.0%
(APIServer pid=1874323) INFO 06-16 19:28:25 [metrics.py:101] SpecDecoding metrics: Mean acceptance length: 1.09, Accepted throughput: 5.70 tokens/s, Drafted throughput: 534.38 tokens/s, Accepted: 57 tokens, Drafted: 5344 tokens, Per-position acceptance rate: 0.085, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, Avg Draft acceptance rate: 1.1%
```


### Serve Command:
```
vllm serve RedHatAI/Qwen3.6-35B-A3B-NVFP4 \
  --speculative-config '{"method": "dflash", "model": "/home/ec2-user/temp_quick_eagle3/dflash_internal_qw36_130K_epoch7", "num_speculative_tokens": 8}' \
  --attention-backend flash_attn \
  --max-num-batched-tokens 32768 -tp 2
```

### Invocation Script:
```
import json, requests

with open("internal_prod_sharegpt_640.jsonl", encoding="utf-8") as f:
    conv = json.loads(f.readline())["conversations"]

# keep only system + user (drop the assistant turn — that's what we want generated)
messages = [m for m in conv if m["role"] in ("system", "user")]

resp = requests.post("http://localhost:8000/v1/chat/completions", json={
    "model": "RedHatAI/Qwen3.6-35B-A3B-NVFP4",
    "messages": messages,
    "max_tokens": 10240,
    "temperature": 0,
})
print(resp.json()["choices"][0]["message"]["content"])
```

## Offline Training

### Data Prep
```
python speculators/scripts/prepare_data.py \
  --model RedHatAI/Qwen3.6-35B-A3B-NVFP4 \
  --data dataset/internal_prod_sharegpt.jsonl \
  --output ./dataset_prepped/dflash_qwen36_A3B_internal \
  --seq-length 10240 \
  --num-preprocessing-workers 10 \
  --overwrite
```

#### Input parsing seems correct to include both `<think>` and `<output>`
<img width="585" height="48" alt="Image" src="https://github.com/user-attachments/assets/749f7f90-ed44-4c38-b5c8-77522b46effb" />
<img width="157" height="34" alt="Image" src="https://github.com/user-attachments/assets/dd95a523-dc35-48a9-8a43-1b1365e5e3b8" />


### Hidden State Generation
```
# vllm env
python speculators/scripts/launch_vllm.py   RedHatAI/Qwen3.6-35B-A3B-NVFP4   --target-layer-ids 1 10 19 28 37   -- -tp 1 -dp 8 --port 8000 --gpu-memory-utilization 0.90 --max-model-len 16384
# speculators venv
OMP_NUM_THREADS=8 python speculators/scripts/data_generation_offline.py \
    --preprocessed-data ./dataset_prepped/dflash_qwen36_A3B_internal \
    --endpoint http://localhost:8000/v1 \
    --output /mnt/local/hidden_states/dflash_qwen36_A3B_internal/hidden_states \
    --concurrency 512 \
    --validate-outputs
```

### Training
```
tmux new -s train
OMP_NUM_THREADS=12 torchrun --standalone --nproc_per_node 8 \
  speculators/scripts/train.py \
  --verifier-name-or-path RedHatAI/Qwen3.6-35B-A3B-NVFP4 \
  --data-path ./dataset_prepped/dflash_qwen36_A3B_internal \
  --hidden-states-path /mnt/local/hidden_states/dflash_qwen36_A3B_internal/hidden_states \
  --save-path ./training_checkpoints/dflash_qwen36_A3B_internal/checkpoints \
  --speculator-type dflash \
  --block-size 16 --max-anchors 1024 --num-layers 8 \
  --target-layer-ids 1 10 19 28 37 \
  --epochs 10 --lr 5e-4 --total-seq-len 10240 \
  --on-missing raise 2>&1 | tee train.log
```

#### Best checkpoint's validation metrics:
```
{
    "loss_epoch": 0.20828166703736656,
    "full_acc_epoch": 0.6475686844258086,
    "position_1_acc_epoch": 0.930225407289326,
    "position_2_acc_epoch": 0.865268385819868,
    "position_3_acc_epoch": 0.8119856137293102,
    "position_4_acc_epoch": 0.7652921036036926,
    "position_5_acc_epoch": 0.7236637749946657,
    "position_6_acc_epoch": 0.6858766795461503,
    "position_7_acc_epoch": 0.6515784202588509,
    "position_8_acc_epoch": 0.6203273317461415,
    "position_9_acc_epoch": 0.5919495058879333,
    "position_10_acc_epoch": 0.5658542707436369,
    "position_11_acc_epoch": 0.5417433506587572,
    "position_12_acc_epoch": 0.5195169016655342,
    "position_13_acc_epoch": 0.4987566168952847,
    "position_14_acc_epoch": 0.4789171224935629,
    "position_15_acc_epoch": 0.4597529435631282
}
```

## 评论 (31)

### huaxuan250 · 2026-06-16

The layer choice is inspired and consistent with `z-lab/Qwen3.6-35B-A3B-DFlash`, which has an good performance lift:
```
vllm serve RedHatAI/Qwen3.6-35B-A3B-NVFP4 \
  --speculative-config '{"method": "dflash", "model": "z-lab/Qwen3.6-35B-A3B-DFlash", "num_speculative_tokens": 8}' \
  --attention-backend flash_attn \
  --max-num-batched-tokens 32768 -tp 2
```
```
============ Serving Benchmark Result ============
Successful requests:                     640       
Failed requests:                         0         
Maximum request concurrency:             32        
Benchmark duration (s):                  733.86    
Total input tokens:                      1871273   
Total generated tokens:                  2132038   
Request throughput (req/s):              0.87      
Output token throughput (tok/s):         2905.22   
Peak output token throughput (tok/s):    800.00    
Peak concurrent requests:                36.00     
Total token throughput (tok/s):          5455.11   
---------------Time to First Token----------------
Mean TTFT (ms):                          385.79    
Median TTFT (ms):                        242.52    
P99 TTFT (ms):                           3881.40   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          11.46     
Median TPOT (ms):                        11.77     
P99 TPOT (ms):                           14.44     
---------------Inter-token Latency----------------
Mean ITL (ms):                           50.97     
Median ITL (ms):                         47.40     
P99 ITL (ms):                            157.48    
---------------Speculative Decoding---------------
Acceptance rate (%):                     47.16     
Acceptance length:                       4.77      
Drafts:                                  446819    
Draft tokens:                            3574552   
Accepted tokens:                         1685779   
Per-position acceptance (%):
  Position 0:                            82.27     
  Position 1:                            66.16     
  Position 2:                            54.24     
  Position 3:                            45.65     
  Position 4:                            38.99     
  Position 5:                            33.89     
  Position 6:                            29.75     
  Position 7:                            26.34     
==================================================

```

### huaxuan250 · 2026-06-16

### My config.json
```
{
  "architectures": [
    "DFlashDraftModel"
  ],
  "auto_map": {
    "": "config.DFlashSpeculatorConfig"
  },
  "aux_hidden_state_layer_ids": [
    1,
    10,
    19,
    28,
    37
  ],
  "block_size": 16,
  "draft_vocab_size": 248320,
  "dtype": "bfloat16",
  "mask_token_id": 248077,
  "max_anchors": 1024,
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
      "architectures": [],
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
    "bos_token_id": 1,
    "eos_token_id": 2,
    "head_dim": 256,
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
    "mlp_bias": false,
    "model_type": "llama",
    "num_attention_heads": 16,
    "num_hidden_layers": 8,
    "num_key_value_heads": 2,
    "pad_token_id": null,
    "pretraining_tp": 1,
    "rms_norm_eps": 1e-06,
    "rope_parameters": {
      "partial_rotary_factor": 0.25,
      "rope_theta": 10000000,
      "rope_type": "default"
    },
    "sliding_window": 2048,
    "tie_word_embeddings": false,
    "use_cache": true,
    "vocab_size": 248320
  },
  "transformers_version": "5.10.2"
}

```

### Z-Lab Config.json
```
{
  "architectures": [
    "DFlashDraftModel"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "auto_map": {
    "AutoModel": "dflash.DFlashDraftModel"
  },
  "block_size": 16,
  "dflash_config": {
    "mask_token_id": 248070,
    "target_layer_ids": [
      1,
      10,
      19,
      28,
      37
    ]
  },
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
  "num_target_layers": 40,
  "pad_token_id": 248044,
  "rms_norm_eps": 1e-06,
  "rope_scaling": {
    "beta_fast": 32.0,
    "beta_slow": 1.0,
    "factor": 64.0,
    "original_max_position_embeddings": 4096,
    "rope_type": "yarn",
    "type": "yarn"
  },
  "rope_theta": 10000000,
  "sliding_window": null,
  "tie_word_embeddings": false,
  "transformers_version": "4.57.1",
  "use_cache": false,
  "use_sliding_window": false,
  "vocab_size": 248320
}
```

### huaxuan250 · 2026-06-16

I CCed a hidden state check script, attached below.
I sampled 1000 hs safetensors, dont seem to have any NaN or INF
```
found 127822 files under /mnt/local/hidden_states/dflash_qwen36_A3B_garp/hidden_states
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
  header 1000/127822  (0 fails so far)
  ......
  header 127000/127822  (0 fails so far)
header sweep done in 5.5s — 0 failed

deep-scanning 1000 files...
  deep 100/1000  (0 fails so far)
  ......
  deep 1000/1000  (0 fails so far)
deep scan done in 241.6s — 0 failed
```

[full_hs_check.py](https://github.com/user-attachments/files/29024725/full_hs_check.py)

### dsikka · 2026-06-17

Hi @huaxuan250 

Do you have your serving benchmark result for your trained speculator, like you generated for the ZLab model?

> The layer choice is inspired and consistent with `z-lab/Qwen3.6-35B-A3B-DFlash`, which has an good performance lift:
> 
> ```
> vllm serve RedHatAI/Qwen3.6-35B-A3B-NVFP4 \
>   --speculative-config '{"method": "dflash", "model": "z-lab/Qwen3.6-35B-A3B-DFlash", "num_speculative_tokens": 8}' \
>   --attention-backend flash_attn \
>   --max-num-batched-tokens 32768 -tp 2
> ```
> 
> ```
> ============ Serving Benchmark Result ============
> Successful requests:                     640       
> Failed requests:                         0         
> Maximum request concurrency:             32        
> Benchmark duration (s):                  733.86    
> Total input tokens:                      1871273   
> Total generated tokens:                  2132038   
> Request throughput (req/s):              0.87      
> Output token throughput (tok/s):         2905.22   
> Peak output token throughput (tok/s):    800.00    
> Peak concurrent requests:                36.00     
> Total token throughput (tok/s):          5455.11   
> ---------------Time to First Token----------------
> Mean TTFT (ms):                          385.79    
> Median TTFT (ms):                        242.52    
> P99 TTFT (ms):                           3881.40   
> -----Time per Output Token (excl. 1st token)------
> Mean TPOT (ms):                          11.46     
> Median TPOT (ms):                        11.77     
> P99 TPOT (ms):                           14.44     
> ---------------Inter-token Latency----------------
> Mean ITL (ms):                           50.97     
> Median ITL (ms):                         47.40     
> P99 ITL (ms):                            157.48    
> ---------------Speculative Decoding---------------
> Acceptance rate (%):                     47.16     
> Acceptance length:                       4.77      
> Drafts:                                  446819    
> Draft tokens:                            3574552   
> Accepted tokens:                         1685779   
> Per-position acceptance (%):
>   Position 0:                            82.27     
>   Position 1:                            66.16     
>   Position 2:                            54.24     
>   Position 3:                            45.65     
>   Position 4:                            38.99     
>   Position 5:                            33.89     
>   Position 6:                            29.75     
>   Position 7:                            26.34     
> ==================================================
> ```



### huaxuan250 · 2026-06-17

Hi @dsikka,
In a blink of eyes my instance where I do the benchmark is terminated overnight.
But I did the performance and it is consisnt with 
```
(APIServer pid=1874323) INFO 06-16 19:28:15 [metrics.py:101] SpecDecoding metrics: Mean acceptance length: 1.10, Accepted throughput: 7.10 tokens/s, Drafted throughput: 558.37 tokens/s, Accepted: 71 tokens, Drafted: 5584 tokens, Per-position acceptance rate: 0.102, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, Avg Draft acceptance rate: 1.3%
```

### huaxuan250 · 2026-06-18

# Dense Qwen/Qwen3.5-4B Model Verification

## TLDR: 1.05 / 15 tokens

### VLLM Serve CLI:
```
vllm serve Qwen/Qwen3.5-4B -tp 1 \
    --gpu-memory-utilization 0.9 \
    --reasoning-parser qwen3 \
    --max-num-batched-tokens 16384 \
    --max-num-seqs 128 \
    --speculative-config '{"model": "/home/ec2-user/dflash_exp/training_checkpoints/dflash_qwen35_4B_os/checkpoints/checkpoint_best", "num_speculative_tokens": 15, "method": "dflash"}'
```

### Singular In-Distribution Invoke
```
Mean acceptance length: 1.04, Accepted throughput: 2.20 tokens/s, Drafted throughput: 920.97 tokens/s, Accepted: 22 tokens, Drafted: 9210 tokens, Per-position acceptance rate: 0.036, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, Avg Draft acceptance rate: 0.2%

Mean acceptance length: 1.07, Accepted throughput: 0.11 tokens/s, Drafted throughput: 22.83 tokens/s, Accepted: 39 tokens, Drafted: 8220 tokens, Per-position acceptance rate: 0.071, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, Avg Draft acceptance rate: 0.5%
```


### Best Validation
```
{
    "loss_epoch": 0.5286458333333334,
    "full_acc_epoch": 0.39421222592339145,
    "position_1_acc_epoch": 0.8713057715923045,
    "position_2_acc_epoch": 0.764018114450391,
    "position_3_acc_epoch": 0.6569370264563408,
    "position_4_acc_epoch": 0.5653946985144189,
    "position_5_acc_epoch": 0.489174051162013,
    "position_6_acc_epoch": 0.4203824332843034,
    "position_7_acc_epoch": 0.3687233413573209,
    "position_8_acc_epoch": 0.3200543040176488,
    "position_9_acc_epoch": 0.2817321626459807,
    "position_10_acc_epoch": 0.24543975336130855,
    "position_11_acc_epoch": 0.2147775195799983,
    "position_12_acc_epoch": 0.1930962886062808,
    "position_13_acc_epoch": 0.16645632969232776,
    "position_14_acc_epoch": 0.15165296484170018,
    "position_15_acc_epoch": 0.13367032967032966
}
```



## Download Data From HF into JSONL
```
from datasets import load_dataset
import json

ds = load_dataset("inference-optimization/Qwen3.5-4B-responses", split="train")
role = {"human": "user", "gpt": "assistant"}

with open("out.jsonl", "w") as f:
    for row in ds:
        conv = [{"role": role.get(t["from"], t["from"]), "content": t["value"]}
                for t in row["conversations"]]
        f.write(json.dumps({"conversations": conv}, ensure_ascii=False) + "\n")

```

## Training E2E
```
python speculators/scripts/prepare_data.py \
  --model Qwen/Qwen3.5-4B \
  --data dataset/qwen35_4b_os.jsonl \
  --output ./dataset_prepped/dflash_qwen35_4B_os \
  --seq-length 12288 \
  --num-preprocessing-workers 10 \
  --overwrite

python speculators/scripts/launch_vllm.py   Qwen/Qwen3.5-4B   --target-layer-ids 1 8 15 22 29  -- -tp 1 -dp 8 --port 8000 --gpu-memory-utilization 0.90 --max-model-len 16384

OMP_NUM_THREADS=8 python speculators/scripts/data_generation_offline.py \
    --preprocessed-data ./dataset_prepped/dflash_qwen35_4B_os \
    --endpoint http://localhost:8000/v1 \
    --output /mnt/local/hidden_states/dflash_qwen35_4B_os/hidden_states \
    --concurrency 512 \
    --validate-outputs

OMP_NUM_THREADS=12 torchrun --standalone --nproc_per_node 8 \
  speculators/scripts/train.py \
  --verifier-name-or-path Qwen/Qwen3.5-4B \
  --data-path ./dataset_prepped/dflash_qwen35_4B_os \
  --hidden-states-path /mnt/local/hidden_states/dflash_qwen35_4B_os/hidden_states \
  --save-path ./training_checkpoints/dflash_qwen35_4B_os/checkpoints \
  --speculator-type dflash \
  --block-size 16 --max-anchors 1024 --num-layers 8 \
  --target-layer-ids 1 8 15 22 29 \
  --epochs 100 --lr 3e-4 --total-seq-len 10240 \
  --on-missing raise 2>&1 | tee train.log
```

### shanjiaz · 2026-06-18

@huaxuan250 Trained the model and was able to reproduce the issue. Took a look at the dataset, the regenerated dataset `inference-optimization/Qwen3.5-4B-responses` you used are consisted of very short sequences (< 500). Serving with unlimited `max-model-len` will have really poor acceptance rates. May I ask how you prepared for your training data, we've discovered that using verifier regenerated data with longer response (we use 8192) helps improve acceptance rate. Let us know if you have any more questions!

### huaxuan250 · 2026-06-18

> we've discovered that using verifier regenerated data with longer response (we use 8192)

@shanjiaz For Qwen3.6 A3B NVFP4, the training data's response max size is around 6144. The data is **not** regenerated but the full prompt-response is captured from prod traffic from the exact same target model.

Are you suggesting to regenerate the response on the training machine with the same sampling param? What kind of the difference will this make I wonder, and why

### shanjiaz · 2026-06-18

@huaxuan250 
1. Generally we've found that drafter trained on max sequence length 8192 for example, does well for prompts up to 8192. Acceptance rates usually drop when we generate beyond the training limit. I'm suspecting this could be the issue, you can verify by limiting the --max-model-len argument to your average response size and see if you get a better result during inference. We're remedying this issue with Sliding Window Attention, it's supported on speculators and vLLM support is in progress.
2. I'd also suggest regenerating the verifier responses for training. Since speculative decoding speedup depends on how closely the drafter matches the verifier's behavior, we've consistently observed that drafters trained on responses generated by their target verifier perform better than those trained on responses from other models. In your case, I'd recommend taking a dataset (we typically use Magpie + UltraChat), removing the assistant responses, and regenerating them with Qwen3.6-35B-A3B. We have [response regeneration](https://github.com/vllm-project/speculators/tree/main/scripts/response_regeneration) scripts that can help with this. After that, you could optionally fine-tune on your production data to incorporate domain-specific knowledge, though I wouldn't rely solely on production responses if they weren't generated by the target verifier.

### huaxuan250 · 2026-06-18

@shanjiaz 
> Acceptance rates usually drop when we generate beyond the training limit. I'm suspecting this could be the issue

For Qwen36 A3B NVFP4, the training dataset capped at 10240. I will try to cap the original serve config
```
vllm serve RedHatAI/Qwen3.6-35B-A3B-NVFP4 \
  --speculative-config '{"method": "dflash", "model": "/home/ec2-user/temp_quick_eagle3/dflash_internal_qw36_130K_epoch7", "num_speculative_tokens": 8}' \
  --attention-backend flash_attn \
  --max-num-batched-tokens 32768 -tp 2
```

> Since speculative decoding speedup depends on how closely the drafter matches the verifier's behavior, we've consistently observed that drafters trained on responses generated by their target verifier perform better than those trained on responses from other models. 

Just to point it out: Production prompt-response pair **is** from the exact same target model (Qwen3.6 A3B) with NVFP4 precision. 

In this case, I wonder what difference or benefits does regen make?

### huaxuan250 · 2026-06-18

I think the most important question and the smallest question is: 
```
A Qwen3.5 4B dflash decoder trained with data generated by Qwen3.5 4B, has terrible performance when invoking with in-training-distribution prompt, despite good validation metrics.
```

1 possible solution is to cap the serve max-model-len to be consistent with the training data.


### shanjiaz · 2026-06-18

@huaxuan250 I think the Qwen3.5 4B model is just not going to be good because it's trained on very short sequence with very small amount of data. For the dflash model you trained for Qwen3.6-35B-A3B, could you please trying serving with --max-model-len 4096 and see if you get better acceptance rates? Thanks!

### huaxuan250 · 2026-06-18

### Testing on reduced max-model-len
```
vllm serve RedHatAI/Qwen3.6-35B-A3B-NVFP4 \
  --speculative-config '{"method": "dflash", "model": "/home/ec2-user/dflash_exp/training_checkpoints/dflash_qwen36_A3B_internal/checkpoints/checkpoint_best", "num_speculative_tokens": 8}' \
  --attention-backend flash_attn \
  --max-model-len 6144 \
  -tp 2
```

```
(APIServer pid=1669325) INFO 06-18 17:27:38 [metrics.py:101] SpecDecoding metrics: Mean acceptance length: 1.11, Accepted throughput: 3.70 tokens/s, Drafted throughput: 263.98 tokens/s, Accepted: 37 tokens, Drafted: 2640 tokens, Per-position acceptance rate: 0.110, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, Avg Draft acceptance rate: 1.4%

(APIServer pid=1669325) INFO 06-18 17:27:18 [metrics.py:101] SpecDecoding metrics: Mean acceptance length: 1.17, Accepted throughput: 8.60 tokens/s, Drafted throughput: 411.15 tokens/s, Accepted: 86 tokens, Drafted: 4112 tokens, Per-position acceptance rate: 0.165, 0.002, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, Avg Draft acceptance rate: 2.1%
```

### huaxuan250 · 2026-06-18

# Dense Qwen/Qwen3.5-4B Model Verification using UltraChat

## TLDR: 1.2 / 15

### In-Distribution Invoke:
```
(APIServer pid=1950622) INFO 06-18 21:44:09 [metrics.py:101] SpecDecoding metrics: Mean acceptance length: 1.21, Accepted throughput: 14.30 tokens/s, Drafted throughput: 1036.48 tokens/s, Accepted: 143 tokens, Drafted: 10365 tokens, Per-position acceptance rate: 0.207, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, Avg Draft acceptance rate: 1.4%
(APIServer pid=1950622) INFO 06-18 21:44:19 [metrics.py:101] SpecDecoding metrics: Mean acceptance length: 1.20, Accepted throughput: 11.90 tokens/s, Drafted throughput: 881.97 tokens/s, Accepted: 119 tokens, Drafted: 8820 tokens, Per-position acceptance rate: 0.202, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, Avg Draft acceptance rate: 1.3%
(APIServer pid=1950622) INFO 06-18 21:45:59 [metrics.py:101] SpecDecoding metrics: Mean acceptance length: 1.23, Accepted throughput: 1.34 tokens/s, Drafted throughput: 88.50 tokens/s, Accepted: 134 tokens, Drafted: 8850 tokens, Per-position acceptance rate: 0.227, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, Avg Draft acceptance rate: 1.5%
(APIServer pid=1950622) INFO 06-18 21:46:09 [metrics.py:101] SpecDecoding metrics: Mean acceptance length: 1.23, Accepted throughput: 13.80 tokens/s, Drafted throughput: 887.97 tokens/s, Accepted: 138 tokens, Drafted: 8880 tokens, Per-position acceptance rate: 0.233, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, Avg Draft acceptance rate: 1.6%
```

### Validation metrics:
```
{
    "loss_epoch": 0.7000159438775511,
    "full_acc_epoch": 0.2554982810146134,
    "position_1_acc_epoch": 0.7321810379629492,
    "position_2_acc_epoch": 0.5513791083469395,
    "position_3_acc_epoch": 0.4374942337854046,
    "position_4_acc_epoch": 0.35374035976893375,
    "position_5_acc_epoch": 0.29140429311325555,
    "position_6_acc_epoch": 0.24347277055996167,
    "position_7_acc_epoch": 0.20560201712559603,
    "position_8_acc_epoch": 0.17667903645508168,
    "position_9_acc_epoch": 0.15582705921733003,
    "position_10_acc_epoch": 0.13847507008960475,
    "position_11_acc_epoch": 0.12474068075363796,
    "position_12_acc_epoch": 0.11511199673973102,
    "position_13_acc_epoch": 0.1068978539398623,
    "position_14_acc_epoch": 0.10065067456515375,
    "position_15_acc_epoch": 0.09567184497117232
}
```



## Recreation:
### Data Regen:
```
speculators/scripts/response_regeneration/run_all.sh \
  --model "Qwen/Qwen3.5-4B" \
  --dataset ultrachat \
  --dp-size 4 --tp-size 2 \
  --limit 10000
```

### Prep Data
```
python speculators/scripts/prepare_data.py \
  --model Qwen/Qwen3.5-4B \
  --data dataset/ultrachat_Qwen3.5-4B.jsonl \
  --output ./dataset_prepped/dflash_qwen35_4B_ultrachat \
  --seq-length 10240 \
  --num-preprocessing-workers 10 \
  --overwrite
```

### Hidden State Extraction
```
python speculators/scripts/launch_vllm.py   Qwen/Qwen3.5-4B   --target-layer-ids 1 8 15 22 29  -- -tp 1 -dp 8 --port 8000 --gpu-memory-utilization 0.90 --max-model-len 16384
```
```
OMP_NUM_THREADS=8 python speculators/scripts/data_generation_offline.py \
    --preprocessed-data ./dataset_prepped/dflash_qwen35_4B_ultrachat \
    --endpoint http://localhost:8000/v1 \
    --output /mnt/local/hidden_states/dflash_qwen35_4B_ultrachat/hidden_states \
    --concurrency 512 \
    --validate-outputs
```

### Training:
```
OMP_NUM_THREADS=12 torchrun --standalone --nproc_per_node 8 \
  speculators/scripts/train.py \
  --verifier-name-or-path Qwen/Qwen3.5-4B \
  --data-path ./dataset_prepped/dflash_qwen35_4B_ultrachat \
  --hidden-states-path /mnt/local/hidden_states/dflash_qwen35_4B_ultrachat/hidden_states \
  --save-path ./training_checkpoints/dflash_qwen35_4B_ultrachat/checkpoints \
  --speculator-type dflash \
  --block-size 16 --max-anchors 1024 --num-layers 8 \
  --target-layer-ids 1 8 15 22 29 \
  --epochs 100 --lr 3e-4 --total-seq-len 10240 \
  --on-missing raise 2>&1
```

### Serve Config:
```
vllm serve Qwen/Qwen3.5-4B -tp 1 \
    --gpu-memory-utilization 0.9 \
    --reasoning-parser qwen3 \
    --max-num-batched-tokens 16384 \
    --max-model-len 4096 \
    --speculative-config '{"model": "/home/ec2-user/dflash_exp/training_checkpoints/dflash_qwen35_4B_ultrachat/checkpoints/checkpoint_best", "num_speculative_tokens": 15, "method": "dflash"}'
```

### Temp Invoke:
```
import json, requests

PATH = "/home/ec2-user/dflash_exp/dataset/ultrachat_Qwen3.5-4B.jsonl"

with open(PATH) as f:
    row = json.loads(f.readline())

role_map = {"human": "user", "gpt": "assistant"}
messages = []
for t in row["conversations"]:
    src = t.get("from") or t.get("role")
    role = role_map.get(src, src)
    if role == "assistant":          # drop the existing answer
        continue
    messages.append({"role": role, "content": t.get("value") or t.get("content")})

resp = requests.post(
    "http://localhost:8000/v1/chat/completions",
    json={
        "model": "Qwen/Qwen3.5-4B",
        "messages": messages,
        "temperature": 0.7
    },
    timeout=600,
)
resp.raise_for_status()
print(resp.json()["choices"][0]["message"]["content"])
```

### huaxuan250 · 2026-06-18

https://github.com/vllm-project/speculators/issues/613#issuecomment-4746399014
Judging from all these symtoms, could this be related to reasoning and stuff?

### shanjiaz · 2026-06-19

@huaxuan250 Yes! There it is `--reasoning-parser qwen3`. Your model is trained without reasoning so should not turn reasoning on for inference!

### huaxuan250 · 2026-06-19

> There it is --reasoning-parser qwen3. Your model is trained without reasoning so should not turn reasoning on for inference!

@shanjiaz I think my Qwen3.5 Dense+UltraChat model is trained with reasoning.
The masking is able to extract both reasoning and output.
And the in-distribution benchmark also has reasoning enabled.

### Sample regenerated training data from ultrachat:
```
{
    "id": "sample_61",
    "conversations": [{
        "from": "human",
        "value": "What kind of collaborative work is expected of the Art Teacher at The School of Arts and Sciences?\nGenerate according to: The School of Arts and Sciences, at 3208 Thomasville Rd, Tallahassee, FL is seeking applications for a Kindergarten-8th grade Art Teacher to teach in a multi-aged classroom. Applicants should be able to plan and execute rigorous, teacher created, hands-on thematic and project based lessons. They will also implement and support instruction and assessment practices for a diverse group of students that reflect the Florida Standards and the principles of their Charter. Also, they will work collaboratively with a diverse group of school colleagues, parents, community members and others to support and implement the goals of the school. Portfolio assessment experience. Salary and benefits commensurate with education and experience; eligible for benefits.\nIf interested, please submit a resume and cover letter with SAST ART TEACHER in the subject line by May 11, 2018 to Eirin Lombardo, Principal at lombardoe@leonschools.net."
    }, {
        "from": "gpt",
        "value": "Thinking Process:\n\n1.  **Analyze the Request:**\n    *   **Question:** What kind of collaborative work is expected of the Art Teacher at The School of Arts and Sciences?\n    *   **Source Material:** A job advertisement for an Art Teacher at The School of Arts and Sciences (Tallahassee, FL).\n    *   **Task:** Generate an answer based *only* on the provided text.\n\n2.  **Scan the Source Text for Keywords:**\n    *   Keywords: \"collaboratively\", \"work\", \"collaborate\".\n    *   Relevant sentence: \"Also, they will work collaboratively with a diverse group of school colleagues, parents, community members and others to support and implement the goals of the school.\"\n\n3.  **Extract the Information:**\n    *   Who to work with: school colleagues, parents, community members, and others (a diverse group).\n    *   Purpose of the collaboration: To support and implement the goals of the school.\n\n4.  **Draft the Answer:**\n    *   Based on the text, the Art Teacher is expected to work collaboratively with a diverse group including school colleagues, parents, community members, and others.\n    *   The goal is to support and implement the goals of the school.\n\n5.  **Refine the Answer:**\n    *   Make it clear and concise, adhering strictly to the provided text.\n\n    *   *Draft:* According to the job description, the Art Teacher is expected to work collaboratively with a diverse group of people, including school colleagues, parents, community members, and others. This collaboration is aimed at supporting and implementing the goals of the school.\n\n6.  **Final Check:** Does this answer the prompt using *only* the provided text? Yes.\n\n7.  **Final Output Generation:** (Matches the refined draft).\n</think>\n\nBased on the job advertisement, the Art Teacher is expected to work collaboratively with a diverse group that includes school colleagues, parents, community members, and others. The purpose of this collaborative work is to support and implement the goals of the school."
    }],
    "metadata": {
        "idx": 61,
        "finish_reason": "stop",
        "latency_s": 3.853,
        "usage": {
            "prompt_tokens": 225,
            "total_tokens": 669,
            "completion_tokens": 444,
            "prompt_tokens_details": null
        },
        "endpoint": "http://127.0.0.1:8000/v1/chat/completions"
    }
}
```


### Masking output

<img width="1213" height="906" alt="Image" src="https://github.com/user-attachments/assets/72f26cd5-ef47-4bf1-b85e-851181e180ae" />
<img width="2040" height="323" alt="Image" src="https://github.com/user-attachments/assets/307a0800-ed58-47cf-86bc-3fad4620758a" />

### shanjiaz · 2026-06-22

@huaxuan250 Test ran on 5k data for qwen3.5-4b using this [fix](https://github.com/vllm-project/vllm/pull/46301). Results seem to be very reasonable, let me know! 

<img width="1350" height="326" alt="Image" src="https://github.com/user-attachments/assets/ae5d74df-a6e9-405c-adeb-e0ff5c09a97a" />

### huaxuan250 · 2026-06-29

I am going to patch this https://github.com/vllm-project/vllm/pull/46301 to my local vllm so the hidden state generated will have the right content. I will update in this thread as well

### shanjiaz · 2026-06-29

@huaxuan250 Thanks! Let us know.

### huaxuan250 · 2026-06-30

# 06/30/2026

## TLDR: Dont think the regenerated hidden state from that vLLM fixed the issue
### In-distribution Invoke
```
(APIServer pid=76938) INFO 06-30 18:16:28 [metrics.py:120] SpecDecoding metrics: Mean acceptance length: 1.34, Accepted throughput: 0.69 tokens/s, Drafted throughput: 30.29 tokens/s, Accepted: 49 tokens, Drafted: 2160 tokens, Per-position acceptance rate: 0.340, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, Avg Draft acceptance rate: 2.3%
(APIServer pid=76938) INFO 06-30 18:16:38 [metrics.py:120] SpecDecoding metrics: Mean acceptance length: 1.22, Accepted throughput: 5.70 tokens/s, Drafted throughput: 394.48tokens/s, Accepted: 57 tokens, Drafted: 3945 tokens, Per-position acceptance rate: 0.217, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000,0.000, 0.000, Avg Draft acceptance rate: 1.4%
(APIServer pid=76938) INFO 06-30 18:16:48 [metrics.py:120] SpecDecoding metrics: Mean acceptance length: 1.17, Accepted throughput: 4.50 tokens/s, Drafted throughput: 395.96tokens/s, Accepted: 45 tokens, Drafted: 3960 tokens, Per-position acceptance rate: 0.170, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000,0.000, 0.000, Avg Draft acceptance rate: 1.1%
(APIServer pid=76938) INFO 06-30 18:16:58 [metrics.py:120] SpecDecoding metrics: Mean acceptance length: 1.41, Accepted throughput: 0.70 tokens/s, Drafted throughput: 25.50 tokens/s, Accepted: 7 tokens, Drafted: 255 tokens, Per-position acceptance rate: 0.412, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, Avg Draft acceptance rate: 2.7%
(APIServer pid=76938) INFO 06-30 18:18:28 [metrics.py:120] SpecDecoding metrics: Mean acceptance length: 1.40, Accepted throughput: 0.11 tokens/s, Drafted throughput: 4.17 tokens/s, Accepted: 10 tokens, Drafted: 375 tokens, Per-position acceptance rate: 0.400, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, Avg Draft acceptance rate: 2.7%
(APIServer pid=76938) INFO 06-30 18:18:38 [metrics.py:120] SpecDecoding metrics: Mean acceptance length: 1.27, Accepted throughput: 7.10 tokens/s, Drafted throughput: 394.46tokens/s, Accepted: 71 tokens, Drafted: 3945 tokens, Per-position acceptance rate: 0.270, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000,0.000, 0.000, Avg Draft acceptance rate: 1.8%
(APIServer pid=76938) INFO 06-30 18:18:48 [metrics.py:120] SpecDecoding metrics: Mean acceptance length: 1.20, Accepted throughput: 5.40 tokens/s, Drafted throughput: 396.01tokens/s, Accepted: 54 tokens, Drafted: 3960 tokens, Per-position acceptance rate: 0.205, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000,0.000, 0.000, Avg Draft acceptance rate: 1.4%
```

### HumanEval Metrics:
`python speculators/scripts/evaluate/evaluate.py --target http://localhost:8000/v1 throughput --subsets "HumanEval"`
```
=== Speculative Decoding Acceptance Report ===

  Num drafts                       72730
  Num draft tokens               1090950
  Num accepted tokens              12234
  Acceptance length               1.1682

  Position                  Acceptance Rate
  ------------------------- ------------
  Position 0                      0.1623
  Position 1                      0.0055
  Position 2                      0.0004
  Position 3                      0.0000
  Position 4                      0.0000
  Position 5                      0.0000
  Position 6                      0.0000
  Position 7                      0.0000
  Position 8                      0.0000
  Position 9                      0.0000
  Position 10                     0.0000
  Position 11                     0.0000
  Position 12                     0.0000
  Position 13                     0.0000
  Position 14                     0.0000

[INFO] [HumanEval] Complete
```


### Validation
```
{
    "loss_epoch": 0.70671875,
    "full_acc_epoch": 0.25338556617473235,
    "position_1_acc_epoch": 0.729068623021523,
    "position_2_acc_epoch": 0.5486913527167195,
    "position_3_acc_epoch": 0.4348699402543771,
    "position_4_acc_epoch": 0.3514501167182019,
    "position_5_acc_epoch": 0.28905010257200214,
    "position_6_acc_epoch": 0.239627357752211,
    "position_7_acc_epoch": 0.20329885406167125,
    "position_8_acc_epoch": 0.17475381272147067,
    "position_9_acc_epoch": 0.15388287247375843,
    "position_10_acc_epoch": 0.13692924722336489,
    "position_11_acc_epoch": 0.12442043024711165,
    "position_12_acc_epoch": 0.1138726298484132,
    "position_13_acc_epoch": 0.1056717895681029,
    "position_14_acc_epoch": 0.09873946489770102,
    "position_15_acc_epoch": 0.0933852235497224
}
```


## vllm env for generating the hidden state:
```
(vllmFixHybrid) [ec2-user@ip-172-31-41-56 dflash_exp]$ uv pip show vllm
Using Python 3.12.13 environment at: /home/ec2-user/vllmFixHybrid
Name: vllm
Version: 0.1.dev17848+gfa9b98d1c.precompiled
Location: /home/ec2-user/vllmFixHybrid/lib/python3.12/site-packages
Editable project location: /home/ec2-user/vllm

(vllmFixHybrid) [ec2-user@ip-172-31-41-56 dflash_exp]$ cd /home/ec2-user/vllm
(vllmFixHybrid) [ec2-user@ip-172-31-41-56 vllm]$ git status
On branch fix/extract-hidden-states-hybrid-block-size
Your branch is up to date with 'origin/fix/extract-hidden-states-hybrid-block-size'.

nothing to commit, working tree clean
(vllmFixHybrid) [ec2-user@ip-172-31-41-56 vllm]$ 
```

## Same dataset & training as here: https://github.com/vllm-project/speculators/issues/613#issuecomment-4746399014

## Invocation Status
### Serving:
```
vllm serve Qwen/Qwen3.5-4B -tp 1 \
    --gpu-memory-utilization 0.9 \
    --reasoning-parser qwen3 \
    --max-num-batched-tokens 16384 \
    --max-model-len 4096 \
    --enforce-eager \
    --speculative-config '{"model": "/home/ec2-user/dflash_exp/training_checkpoints/dflash_qwen35_4B_ultrachat/checkpoints/checkpoint_best", "num_speculative_tokens": 15, "method": "dflash"}'
```

### Invoking
```
import json, requests

PATH = "/home/ec2-user/dflash_exp/dataset/ultrachat_Qwen3.5-4B.jsonl"

with open(PATH) as f:
    row = json.loads(f.readline())

role_map = {"human": "user", "gpt": "assistant"}
messages = []
for t in row["conversations"]:
    src = t.get("from") or t.get("role")
    role = role_map.get(src, src)
    if role == "assistant":          # drop the existing answer
        continue
    messages.append({"role": role, "content": t.get("value") or t.get("content")})

resp = requests.post(
    "http://localhost:8000/v1/chat/completions",
    json={
        "model": "Qwen/Qwen3.5-4B",
        "messages": messages,
        "temperature": 0.0
    },
    timeout=600,
)
resp.raise_for_status()
print(resp.json()["choices"][0]["message"]["content"])
```

### Model Response:
```
{
    'index': 0,
    'message': {
        'role': 'assistant',
        'content': '\n\nBased on the job posting, the Art Teacher is expected to work collaboratively with a diverse group of school colleagues, parents, community members, and others to support and implement the goals of the school.',
        'refusal': None,
        'annotations': None,
        'audio': None,
        'function_call': None,
        'tool_calls': [],
        'reasoning': 'Thinking Process:\n\n1.  **Analyze the Request:**\n    *   **Question:** What kind of collaborative work is expected of the Art Teacher at The School of Arts and Sciences?\n    *   **Source Material:** A job posting text for an Art Teacher position at The School of Arts and Sciences (Tallahassee, FL).\n    *   **Constraint:** Generate according to the provided text.\n\n2.  **Scan the Source Text for Keywords:**\n    *   Keywords: "collaborative", "work", "Art Teacher", "School of Arts and Sciences".\n    *   Relevant sentence: "Also, they will work collaboratively with a diverse group of school colleagues, parents, community members and others to support and implement the goals of the school."\n\n3.  **Extract the Information:**\n    *   Who: A diverse group of school colleagues, parents, community members, and others.\n    *   Purpose: To support and implement the goals of the school.\n    *   Context: Kindergarten-8th grade Art Teacher position.\n\n4.  **Draft the Answer:**\n    *   Based on the text, the Art Teacher is expected to work collaboratively with a diverse group of stakeholders.\n    *   These stakeholders include school colleagues, parents, community members, and others.\n    *   The goal of this collaboration is to support and implement the goals of the school.\n\n5.  **Refine the Answer:**\n    *   Make it concise and directly address the prompt using only the provided information.\n    *   *Draft:* The Art Teacher is expected to work collaboratively with a diverse group of school colleagues, parents, community members, and others. This collaboration is intended to support and implement the goals of the school.\n\n6.  **Final Review:** Does this accurately reflect the source text without adding external information? Yes.\n\n7.  **Final Output Generation:** (Matches the drafted answer).\n    *   "According to the job posting, the Art Teacher is expected to work collaboratively with a diverse group of school colleagues, parents, community members, and others to support and implement the goals of the school."\n\n    *   *Self-Correction on "Generate according to":* The prompt asks to "Generate according to". This usually means base the answer strictly on the provided text.\n\n    *   *Final Polish:* The Art Teacher is expected to work collaboratively with a diverse group of school colleagues, parents, community members, and others to support and implement the goals of the school.\n\n    *   *Wait, check for other collaborative aspects:* The text mentions "plan and execute rigorous, teacher created, hands-on thematic and project based lessons." This is more about instruction than collaboration. The text mentions "implement and support instruction and assessment practices for a diverse group of students." This is about student instruction. The specific "collaborative work" is explicitly defined in the sentence starting with "Also, they will work collaboratively..."\n\n    *   *Decision:* Stick to the explicit mention of collaboration.\n\n    *   *Final Answer Formulation:* Based on the text provided, the Art Teacher is expected to work collaboratively with a diverse group of school colleagues, parents, community members, and others to support and implement the goals of the school.cw\n'
    },
    'logprobs': None,
    'finish_reason': 'stop',
    'stop_reason': None,
    'token_ids': None,
    'routed_experts': None
}
```


### orestis-z · 2026-07-01

Hey @shanjiaz I can dig into this unless you're not actively doing that yourself.

### orestis-z · 2026-07-01

## Root Cause Analysis: RoPE `partial_rotary_factor` mismatch between training and inference

*Explored and written with [Claude Code](https://claude.ai/code)*

---

### Summary

The bug affects **all DFlash models trained on verifiers that use `partial_rotary_factor`** (Qwen3.5, Qwen3.6, Gemma4, etc.). The root cause is a train/inference mismatch in the rotary position embedding dimension.

### The mismatch chain

**1. Verifier config** (e.g. Qwen3.5-4B, Qwen3.6-35B-A3B) includes:
```
rope_parameters.partial_rotary_factor = 0.25
head_dim = 256
```

**2. `create_transformer_layer_config`** ([`scripts/train.py:151-170`](https://github.com/vllm-project/speculators/blob/main/scripts/train.py#L151-L170)) deep-copies the verifier's `rope_parameters` onto the draft config, including `partial_rotary_factor`. It strips `mrope_section`, `mrope_interleaved`, `type` — but **not** `partial_rotary_factor`.

**3. During training**, speculators uses `Qwen3RotaryEmbedding` (from `transformers.models.qwen3`), whose `compute_default_rope_parameters` computes:
```python
dim = getattr(config, "head_dim", None)  # → 256 (ignores partial_rotary_factor)
```
→ **Trains with 256-dim rotation** (100% of head)

**4. During inference** in vLLM, `get_rope` reads from the saved `rope_parameters`:
```python
partial_rotary_factor = rope_parameters.get("partial_rotary_factor", 1.0)  # → 0.25
rotary_dim = int(head_size * partial_rotary_factor)  # → 64
```
→ **Infers with 64-dim rotation** (25% of head)

**5. Additionally**, speculators' local `apply_rotary_pos_emb` applies rotation to the full Q/K tensor. The correct `Qwen3_5` version in transformers splits into `q_rot, q_pass = q[..., :rotary_dim], q[..., rotary_dim:]` and only rotates the first part.

### Verification

Script that reproduces the mismatch and confirms the fix: https://gist.github.com/orestis-z/3e3bd0e4b83e4084c383ba922b9b1586

```
Verifier: Qwen/Qwen3.5-4B
  [WITHOUT FIX]  Training rotary_dim=256, Inference rotary_dim=64 → MISMATCH (4x)
  [WITH FIX]     Training rotary_dim=256, Inference rotary_dim=256 → MATCH ✓

Verifier: RedHatAI/Qwen3.6-35B-A3B-NVFP4
  [WITHOUT FIX]  Training rotary_dim=256, Inference rotary_dim=64 → MISMATCH (4x)
  [WITH FIX]     Training rotary_dim=256, Inference rotary_dim=256 → MATCH ✓

Verifier: meta-llama/Llama-3.1-8B
  [WITHOUT FIX]  Training rotary_dim=128, Inference rotary_dim=128 → MATCH (no partial_rotary_factor)
  [WITH FIX]     Training rotary_dim=128, Inference rotary_dim=128 → MATCH ✓
```

### Why z-lab works

z-lab's config uses `head_dim=128` and **no `partial_rotary_factor`** (uses `rope_scaling` with yarn type instead). Both training and inference use full 128-dim rotation → consistent → 47% acceptance.

### Why this only affects Qwen3.5/Gemma4

Most models (Llama, Qwen3, Mistral, DeepSeek) don't set `partial_rotary_factor` or default it to `1.0`, making the mismatch invisible (`int(head_dim * 1.0) == head_dim`). Only Qwen3.5 (`0.25`) and Gemma4 (`0.5`) set it below 1.0, triggering a 4x or 2x RoPE dimension mismatch.

### Fix options

**Quick fix** — strip `partial_rotary_factor` from the draft config so both training and vLLM use full-dim rotation:

```python
# scripts/train.py:168
_MROPE_KEYS = ("mrope_section", "mrope_interleaved", "type", "partial_rotary_factor")
```

**Proper fix** — make training actually apply partial rotation (matching the verifier and vLLM):
1. Replace `Qwen3RotaryEmbedding` with a version that reads `partial_rotary_factor` from `rope_parameters` (like `Qwen3_5TextRotaryEmbedding` does)
2. Update `apply_rotary_pos_emb` to split Q/K into rotary/pass-through parts

The proper fix is better long-term — the draft model would use the same positional encoding as the verifier.

### huaxuan250 · 2026-07-01

Hi @orestis-z,
That quick fix is applicable to the Qwen3.5 Desne, check blow:
```
(APIServer pid=1129565) INFO 07-01 19:08:52 [metrics.py:120] SpecDecoding metrics: Mean acceptance length: 4.97, Accepted throughput: 11.47 tokens/s, Drafted throughput: 43.32 tokens/s, Accepted: 699 tokens, Drafted: 2640 tokens, Per-position acceptance rate: 0.830, 0.670, 0.562, 0.483, 0.398, 0.347, 0.256, 0.142, 0.097, 0.085, 0.040, 0.017, 0.017, 0.017, 0.011, Avg Draft acceptance rate: 26.5%
```

Testing out Qwen3.6 MOE

### huaxuan250 · 2026-07-01

Qwen3.6 MOE:
```
(APIServer pid=1332443) INFO 07-01 21:33:03 [metrics.py:120] SpecDecoding metrics: Mean acceptance length: 5.05, Accepted throughput: 3.07 tokens/s, Drafted throughput: 11.39 tokens/s, Accepted: 352 tokens, Drafted: 1305 tokens, Per-position acceptance rate: 0.897, 0.701, 0.575, 0.471, 0.333, 0.310, 0.230, 0.161, 0.138, 0.115, 0.046, 0.023, 0.023, 0.011, 0.011, Avg Draft acceptance rate: 27.0%
```

Looks pretty good, I will train a small sample of my producntion prompt and see if this can survive in long context length.

So looks like these combinations are the true fix:
1. Use this branch of vLLM to generate hidden state: `https://github.com/vllm-project/vllm/pull/46301`
2. Include `partial_rotary_factor` in _MROPE_KEYS = ("mrope_section", "mrope_interleaved", "type", "partial_rotary_factor") at `train.py`

### shanjiaz · 2026-07-01

Awesome! Will close this issue. @huaxuan250 please use sliding window attention when training for dflash. vLLM support has just landed. @orestis-z Thanks for looking into this!!!

### orestis-z · 2026-07-02

@shanjiaz should we merge a fix or leave it as it is (asking since issue is closed)?

One of the two:
- one-liner that strips `partial_rotary_factor` so both sides default to full rotation
- PR #568 makes training correctly handle partial rotation.

### shanjiaz · 2026-07-06

@orestis-z Sorry somehow missed this comment. Let's try to merge the PR that makes training correctly handle partial rotation?

### huaxuan250 · 2026-07-06

Thx a lot for the help @shanjiaz and @orestis-z 

### huaxuan250 · 2026-07-07

# 07/07/2026
## TLDR: Trained with internal domain data with the above fixes, validation metrics looks fine, but benchmark performance using the training data is not as good.
```
  ┌───────────┬───────────────────────────┬──────────────────────────┬────────────────┐
  │   step    │ self full_attn — training │ self full_attn — serving │ zlab — serving │
  ├───────────┼───────────────────────────┼──────────────────────────┼────────────────┤
  │ 1st token │ 93.7% (pos1)              │ 84.3% (pos0)             │ 84.0% (pos0)   │
  ├───────────┼───────────────────────────┼──────────────────────────┼────────────────┤
  │ 2nd token │ 87.4% (pos2)              │ 45.2% (pos1)             │ 75.1% (pos1)   │
  ├───────────┼───────────────────────────┼──────────────────────────┼────────────────┤
  │ 3rd token │ 82.2% (pos3)              │ 20.1% (pos2)             │ 69.5% (pos2)   │
  ├───────────┼───────────────────────────┼──────────────────────────┼────────────────┤
  │ 4th token │ 77.6% (pos4)              │ 11.6% (pos3)             │ 65.1% (pos3)   │
  └───────────┴───────────────────────────┴──────────────────────────┴────────────────┘

```

## Full workflow
### Benchmark Command: --temperature=0
```
vllm bench serve --dataset-name custom --dataset-path /home/ec2-user/dflash_exp/dataset/garp_prod_sharegpt_5000_vllm_bench.jsonl --num-prompts 320 --max-concurrency 16 --model RedHatAI/Qwen3.6-35B-A3B-NVFP4 --base-url http://0.0.0.0:8000 --endpoint /v1/chat/completions --backend openai-chat --save-result --save-detailed --result-dir ./results/ --output-len 6144 --temperature=0

```
### Z-Lab
#### Serving:
```
vllm serve RedHatAI/Qwen3.6-35B-A3B-NVFP4 \
  --speculative-config '{"method": "dflash", "model": "training_checkpoints/dflash_zlab_full_atten", "num_speculative_tokens": 8}' \
  --max-model-len 16384
```

#### Performance:
```
Acceptance rate (%):                     65.97     
Acceptance length:                       6.28      
Drafts:                                  255426    
Draft tokens:                            2043408   
Accepted tokens:                         1347987   
Per-position acceptance (%):
  Position 0:                            83.95     
  Position 1:                            75.11     
  Position 2:                            69.54     
  Position 3:                            65.11     
  Position 4:                            62.09     
  Position 5:                            59.36     
  Position 6:                            57.24     
  Position 7:                            55.33     
```
#### Config:
```
{
  "architectures": [
    "DFlashDraftModel"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "auto_map": {
    "AutoModel": "dflash.DFlashDraftModel"
  },
  "block_size": 16,
  "dflash_config": {
    "mask_token_id": 248070,
    "target_layer_ids": [
      1,
      10,
      19,
      28,
      37
    ]
  },
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
  "num_target_layers": 40,
  "pad_token_id": 248044,
  "rms_norm_eps": 1e-06,
  "rope_scaling": {
    "beta_fast": 32.0,
    "beta_slow": 1.0,
    "factor": 64.0,
    "original_max_position_embeddings": 4096,
    "rope_type": "yarn",
    "type": "yarn"
  },
  "rope_theta": 10000000,
  "sliding_window": null,
  "tie_word_embeddings": false,
  "transformers_version": "4.57.1",
  "use_cache": false,
  "use_sliding_window": false,
  "vocab_size": 248320
}

```

### Self-Trained with Domain Data
#### Serving:
```
vllm serve RedHatAI/Qwen3.6-35B-A3B-NVFP4 \
  --speculative-config '{"method": "dflash", "model": "training_checkpoints/dflash_qwen36_A3B_garp_full_attn/checkpoints/checkpoint_best", "num_speculative_tokens": 8}' \
  --max-model-len 16384
```

#### Performance:
```
-------------Speculative Decoding---------------
Acceptance rate (%):                     22.44     
Acceptance length:                       2.80      
Drafts:                                  367207    
Draft tokens:                            2937656   
Accepted tokens:                         659241    
Per-position acceptance (%):
  Position 0:                            84.27     
  Position 1:                            45.23     
  Position 2:                            20.06     
  Position 3:                            11.59     
  Position 4:                            7.81      
  Position 5:                            6.19      
  Position 6:                            3.24      
  Position 7:                            1.13      
```

#### Config:
```
{
  "architectures": [
    "DFlashDraftModel"
  ],
  "auto_map": {
    "": "config.DFlashSpeculatorConfig"
  },
  "aux_hidden_state_layer_ids": [
    1,
    10,
    19,
    28,
    37
  ],
  "block_size": 16,
  "draft_vocab_size": 248320,
  "dtype": "bfloat16",
  "mask_token_id": 248077,
  "max_anchors": 2048,
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
    "eos_token_id": null,
    "head_dim": 256,
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
    "max_window_layers": 28,
    "model_type": "qwen3",
    "num_attention_heads": 16,
    "num_hidden_layers": 8,
    "num_key_value_heads": 2,
    "pad_token_id": null,
    "rms_norm_eps": 1e-06,
    "rope_parameters": {
      "rope_theta": 10000000,
      "rope_type": "default"
    },
    "sliding_window": null,
    "tie_word_embeddings": false,
    "use_cache": true,
    "use_sliding_window": false,
    "vocab_size": 248320
  },
  "transformers_version": "5.10.2"
}
```
#### Validation metrics:
```
{
    "loss_epoch": 0.1909632375707714,
    "full_acc_epoch": 0.6596276429942887,
    "position_1_acc_epoch": 0.9370174994318367,
    "position_2_acc_epoch": 0.8737494432419424,
    "position_3_acc_epoch": 0.8218679103011343,
    "position_4_acc_epoch": 0.776408029464583,
    "position_5_acc_epoch": 0.7354383284646954,
    "position_6_acc_epoch": 0.6984372863340227,
    "position_7_acc_epoch": 0.6647190723923047,
    "position_8_acc_epoch": 0.6338067898470079,
    "position_9_acc_epoch": 0.6054288873706711,
    "position_10_acc_epoch": 0.579330671087469,
    "position_11_acc_epoch": 0.5552893307553768,
    "position_12_acc_epoch": 0.5329437330717098,
    "position_13_acc_epoch": 0.5120572639380102,
    "position_14_acc_epoch": 0.49224159262644546,
    "position_15_acc_epoch": 0.4728947225284691
}
```

### piekey1994 · 2026-07-21

Why have I removed the partial_rotary_factor, and training the dflash of qwen3.6-35ba3b is still ineffective, and the vllm is 0.25.1?
There is no problem in training qwen3-30ba3b.
