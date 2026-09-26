# [Issue #738] [Bug]: Acceptance Rate Drops Much Quicker Along Posititions for Dflash

source: https://github.com/vllm-project/speculators/issues/738
state: open | updated: 2026-07-09T03:27:11Z
labels: bug

## 正文

### Your current environment

Please provide the following information about your environment if applicable:

- vLLM: 0.22.1 for Hidden State Extraction + Inference Benchmark 
- Speculators: Mainline `eb98a29eabc1d79d531d643424cf499bbb25a7f7` as of 07/01/2025
- CUDA: 13.2
- PyTorch: 2.11.0
- Transformers: 5.10.2
- Hardware: p4de for benchmark, p5en for training
- Model: RedHatAI/Qwen3.6-35B-A3B-NVFP4


### 🐛 Describe the bug

# Overview
## Continuation of this issue:
https://github.com/vllm-project/speculators/issues/613

## Fixes Applied:
### Training ignores `partial_rotary_factor`
Suggested by this comment: https://github.com/vllm-project/speculators/issues/613#issuecomment-4856024440
### Hidden State Extraction is fixed:
This branch of Vllm is used for extracting hidden state extraction: https://github.com/vllm-project/vllm/pull/46301
### The combination of the above 2 gave good Ultrachat-trained decoders:
https://github.com/vllm-project/speculators/issues/613#issuecomment-4859229999
https://github.com/vllm-project/speculators/issues/613#issuecomment-4860252673

## Persistent Issue:
### Trained with Prod data yield sub-optimal In-Distribution Benchmark Performance
Details here: https://github.com/vllm-project/speculators/issues/613#issuecomment-4908637925


It looks like: 
Our validation metrics are fine, pos1 token acceptance is on par with the Z-Lab baseline, but subsequent acceptance rate drops very very quickly.
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

I wonder could this be the effect of the lack of partial `partial_rotary_factor`?


## 评论 (4)

### huaxuan250 · 2026-07-07

The training command for the above self-trained decoder
The gamma should be default to 4.0 because I didn't have `--dflash-decay-gamma` set
```
speculators/scripts/train.py --verifier-name-or-path RedHatAI/Qwen3.6-35B-A3B-NVFP4 --data-path ./dataset_prepped/dflash_qwen36_A3B_garp_prod --hidden-states-path /mnt/local/hidden_states/dflash_qwen36_A3B_garp/hidden_states --save-path ./training_checkpoints/dflash_qwen36_A3B_garp_full_attn/checkpoints --speculator-type dflash --block-size 16 --max-anchors 2048 --num-layers 8 --target-layer-ids 1 10 19 28 37 --epochs 5 --lr 5e-4 --total-seq-len 10240 --optimizer muon --on-missing raise

```

### fynnsu · 2026-07-08

#733 seems to fix the partial rotary factor issue. Maybe see if that resolves your issue?

### huaxuan250 · 2026-07-08

@fynnsu will try it first after the current iteration of training finishes
Interestingly, the Z-Lab's decoder (this is the checkpoint I am using: https://huggingface.co/z-lab/Qwen3.6-35B-A3B-DFlash/blob/31977fbe13a86e8b961774f773058175676d89b8/config.json) seems to have a very different layout for the positional embeddings

Reminder for myself: Finetuned Decoder achived worse performance than Z-Lab base on finetune dataset

### huaxuan250 · 2026-07-09

Reminder for myself: Finetuned Decoder achieved worse performance than Z-Lab base decoder on finetune dataset
