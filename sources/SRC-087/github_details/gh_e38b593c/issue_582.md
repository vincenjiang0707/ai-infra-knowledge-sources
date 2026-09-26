# [Issue #582] [RFC]: Add Training Support for Orthrus

source: https://github.com/vllm-project/speculators/issues/582
state: closed | updated: 2026-07-01T13:47:31Z
labels: RFC

## 正文

### Motivation.

I would like to propose adding training support for **Orthrus**, a new speculative / parallel decoding method:

* Paper: https://huggingface.co/papers/2605.12825
* Model collection: https://huggingface.co/collections/chiennv/orthrus
* Reference implementation: https://github.com/chiennv2000/orthrus

Orthrus looks promising because it keeps the base LLM frozen and trains a lightweight diffusion-style module for parallel token generation. According to the paper/model card, it supports lossless generation, shares the target model’s KV cache, and introduces only `O(1)` cache overhead.

I think this could be a valuable addition to `speculators`, complementary to DFlash and EAGLE-style methods.

 Orthrus may have some practical advantages:

* It does not rely on a fully separate autoregressive draft model.
* It shares KV cache with the target model, which may reduce memory overhead.
* It may be more suitable for long-context and high-concurrency serving.
* The trainable part is lightweight, while the base model remains frozen.
* It provides a different trade-off between parallel generation, memory usage, and verification cost.

### Proposed Change.

A possible initial scope could be:

1. Add an `orthrus` training algorithm.
2. Support Qwen3 models first, since public Orthrus checkpoints already exist.
3. Save trained Orthrus modules in a format that can later be used by vLLM.
4. Add benchmarks comparing Orthrus with DFlash / EAGLE under both low- and high-concurrency settings.

### Any Other Things.

Open questions:

* Would the maintainers be interested in Orthrus training support?
* Should Orthrus be implemented as a new algorithm type, or as a more general attached-speculator module?
* What artifact format would be best for future vLLM integration?

Thanks!

## 评论 (8)

### fynnsu · 2026-06-10

@HaizhouPeng Thanks for the RFC! We've started evaluating Orthrus internally. We're trying to determine whether the overhead of running what is essentially a full size draft model, can perform well compared to lighter weight drafters. I'll try to update once we have more concrete results.

On top of that, I have some concerns about our ability to scale the training workloads in speculators to larger models like this. Although only a few parameters are active, the costs of training a model with (for example) 36 layers are a lot higher (in terms of VRAM and runtime) and this isn't something the speculators library is currently optimized for. It is likely that if we add this as described in the paper, it would only be possible to train it on small models (e.g. 8B or less), while larger models hit OOM errors.

### HaizhouPeng · 2026-06-11

@fynnsu Thanks for the update! I really appreciate your team looking into Orthrus internally. The concerns about overhead and training scalability make sense, and I’m looking forward to any concrete results or observations you can share later. Thanks again! 🎉

### weifanjiang · 2026-06-18

@HaizhouPeng We compared request-serving latency for a proxy Orthrus-style workflow and DFlash under different request rates, and wanted to share some preliminary results.

Method:
- Since we have not implemented Orthrus training yet, we constructed a synthetic Orthrus-style checkpoint that matches the forward-pass workflow shown in Figure 1 of the paper. The checkpoint has 36 attention-only layers, matching the Qwen3-8B verifier depth, and reuses the verifier KV cache, MLP, norm, and LM head. This checkpoint was not trained on real data.
- We set draft size to 31 (corresponding to block size 32 if including the anchor) and synthetic acceptance length to 9.43, which is averaged from 4 datasets reported in figure 4 of the paper.
- For comparison, we include DFlash with five layers. We set draft size to 31 and synthetic acceptance length to 6.85, also averaged from 4 reported datasets in figure 4.
- We used a synthetic serving workload with 256 input tokens and 2048 output tokens per request, and profiled per-request latency as a function of request rate using GuideLLM. All experiments were run on a single A100.

In this synthetic setting, DFlash achieves lower latency than the Orthrus-style proxy. Although Orthrus has a higher synthetic accepted length, the additional attention computation appears to dominate in this setup. That said, these results are preliminary latency evidence rather than a definitive Orthrus evaluation.  Our experiment uses synthetic acceptance lengths on untrained checkpoints. Also, this setting differs from Figure 4 of the paper, which focuses on long-context scenarios of 16K+ tokens.

<img width="1824" height="1398" alt="Image" src="https://github.com/user-attachments/assets/c9081099-8096-405e-8997-b08fb52a2fe2" />

### fynnsu · 2026-06-18

Thanks @weifanjiang! 

@HaizhouPeng given these results, and the technical challenges introduced by training an Orthrus model, we can't prioritize this work right now. If you're still interested in seeing this implemented and have the bandwidth to work on it yourself, we can help you with the planning and reviews. 

### HaizhouPeng · 2026-06-19

@weifanjiang @fynnsu Thank you for the detailed analysis and preliminary latency evaluation. This is very helpful. Given these results and the fact that Orthrus training support is not currently implemented, I think it is reasonable to close this RFC for now. Thanks again for taking the time to investigate and share the results.

### chiennv2000 · 2026-06-24

Hi @HaizhouPeng and folks, orthrus author here. Thanks for taking the time to this. We've been busy over the last few weeks, but we are planning to release Qwen 3.5/Gemma support very soon, followed by the full training code release. I will reach out again once everything is available. @HaizhouPeng , is there an email address I can reach you at?

### HaizhouPeng · 2026-06-25

@chiennv2000 I will send you emails privately, and you can use the email address

### jamesunnc · 2026-07-01

Looking forward to qwen3.5 support!
