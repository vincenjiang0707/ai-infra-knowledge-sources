# [Issue #2646] cheap KLD metric

source: https://github.com/vllm-project/llm-compressor/issues/2646
state: closed | updated: 2026-09-02T20:06:17Z
labels: enhancement, good first issue, stale

## 正文

# Background

[KL Divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence) is a useful metric for measuring the similarity between two model's output distributions (i.e. to see how similar a quantized model is compared to a non quantized model). It requires extracting the output probabilities for two models and then comparing them.

In vllm its hard to extract logprobs. As an example, extracting full vocab logprobs for 10 tokens with llama-3-8B takes 1.1 tokens/sec, making a wikitext kl-divergence calculation take ~64 hours

https://gist.github.com/HDCharles/030a3c5d7439680afdbebd935758366d

Most of this time is spent transferring the massive tensor to disk. you could get around this by taking fewer logprobs, but the tail tends to dominate the logprobs calculation unless you're using a temperature way below the common .7-1.0 temperature used for most generation. 

so approximation won't work and the normal method won't work, we need a different approach.

# Approach

the primary issue is the amount of data that we need to extract from within vllm, one thing we can do to reduce this is extract a step before the logprobs have been generated. While the vocab size is 120k, the hidden dimension is just 4096 and can be used to generate the full logprobs. Using this would theoretically reduce our transfer time and storage size by a factor of ~30x.

Getting this data is also tricky but
in https://vllm.ai/blog/extract-hidden-states a method for extracting hidden states was developed for training speculative decoding models that require hidden state information.

From here we can theoretically do the following, run both models on vllm, extract the hidden state information before the lm_head, then to calculate KLDivergence, populate the lm_head (which is usually the same for both models, but could be 2 lm_heads if they differ), load the tokens in batches, uses lm_head to calculate the logprobs, and from there calculates kl-divergence.

This has the benefit of using existing vllm compoenents, saving on storage, and being fast.

# Task

Create a tool/script to quickly and efficiently calculate kl divergence using the approach above.
Test it, figure out how easy it is to generalize to different model architectures....etc

## 评论 (0)
