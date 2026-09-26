# [Issue #560] Support for T5

source: https://github.com/AI-Hypercomputer/maxtext/issues/560
state: closed | updated: 2026-04-28T17:56:26Z
labels: feature request

## 正文

Do you have plans to support encoder-decoder models like T5? It will be great to have T5 with flash attention 😃

## 评论 (7)

### rwitten · 2024-03-27

What specific model would you like supported? We would only take this on if we saw sufficient interest (but in practice we see heavy movement towards decoder-only models).

### kishorenc · 2024-03-27

Decoder only models are great for generative use cases but T5 family is the work horse for many discriminative tasks. For example, the flan-t5-base model has 2M downloads on [Huggingface](https://huggingface.co/google/flan-t5-base) in the last month. Support for flan-t5 will add a huge value to the community.

### versae · 2024-04-08

It'd be great to have T5 models here as well.

### emergenz · 2024-04-12

I'm going to try to turn MaxText into encoder-decoder anyway, so native support is of course also appreciated :)

### emergenz · 2024-07-16

https://github.com/p-doom/maxtext/tree/colab_temp

We finally came around to implement encoder-decoder models in our maxtext fork. The synthetic data pipeline seems to work. Will add support for the real data pipeline later today.

### emergenz · 2024-07-16

okay I was a bit too fast, still have to fix a few things.

### sarunsingla11722 · 2026-04-28

As an effort we are cleaning any stale issues. Please feel free to reopen if still required. 
