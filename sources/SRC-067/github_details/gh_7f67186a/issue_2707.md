# [Issue #2707] Is there a plan for MXFP8 support?

source: https://github.com/Dao-AILab/flash-attention/issues/2707
state: open | updated: 2026-07-15T22:53:05Z
labels: 

## 正文

Hi,

Seems MXFP8 is not supported according to [benchmark_flash_attention_fp8.py](https://github.com/Dao-AILab/flash-attention/blob/main/flash_attn/cute/benchmark_flash_attention_fp8.py).

Thanks!

## 评论 (2)

### tridao · 2026-07-14

Prob for the forward. It's not yet clear how to properly quantize V if you don't want to leak information to future tokens (e.g. quantizing 32 tokens require the max, which means token i is sending information to token i+1).
I could imagine doing mxfp8 for Q @ K (quantizing along the headdim) and bf16 for P @ V.

### goldhuang · 2026-07-15

@tridao Is it clear for sequence-to-sequence diffusion model?
