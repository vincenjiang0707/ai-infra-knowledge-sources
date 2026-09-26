# [Issue #3108] [Checkpoint Submission] Qwen3.5-9B FP8-block + NVFP4

source: https://github.com/vllm-project/llm-compressor/issues/3108
state: closed | updated: 2026-08-31T14:24:09Z
labels: 

## 正文

Submission for #3088 (Qwen3.5-9B, priority 1, missing FP8 Block and NVFP4). The submission form linked there (`issues/new?template=submit-checkpoint.yml`) currently 404s because the template is not on main, so this is a plain issue carrying the same fields.

## Checkpoints

- FP8 Block: https://huggingface.co/RishabhSinha/Qwen3.5-9B-FP8-block
- NVFP4: https://huggingface.co/RishabhSinha/Qwen3.5-9B-NVFP4

## Base model

[Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B)

## Method

- llm-compressor `0.13.1.dev51+g50d0a1c75`, compressed-tensors `0.18.1.dev21+g8c0fa69`
- transformers 5.16.1, torch 2.11.0+cu128, 1x L40S
- Full recipes embedded in each model card:
  - FP8-block: data-free, RedHatAI-family ignore list (lm_head plus the visual and linear_attn modules), MTP tensors carried over into the checkpoint via `save_mtp_tensors_to_checkpoint`
  - NVFP4: calibrated, 256 samples x 4096 max seq len, Open-Platypus

## Validation

- Greedy sanity generations on both checkpoints
- FP8-block loads and runs natively on vLLM 0.24: `TritonFp8BlockScaledMMKernel` selected for the block-scaled GEMMs, GDN kernels engaged
- lm-eval results pending; will post them in this thread


## 评论 (0)
