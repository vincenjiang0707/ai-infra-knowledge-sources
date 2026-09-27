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

## 评论 (12)

### jwpark33 · 2026-04-26

@HDCharles  I'd like to contribute to this! Can I be assigned to work on this ?

### HDCharles · 2026-04-28

yes @jwpark33 it looks like there are a few open PRs after you requested to be assigned, feel free to use them as a jumping off point or collaborate those submitters.

### jayakumarpujar · 2026-04-28

@HDCharles Moving the design discussion here as suggested in #2659.

I want to add few points into the PR thread:

**Validated end-to-end on Colab T4** (`facebook/opt-125m` W4A16):
- 8 prompts, 95 tokens: `mean_kld = 0.202843`
- sanity check (same model both sides): exactly `0.0`
- WikiText-2 (64 samples, 6106 tokens): `mean_kld = 0.154366`
- per-prompt KLD range 0.17 - 0.23 (consistent across prompts)
- 26 unit tests passing
- Total wall-clock for notebook flow: ~10 min on T4

**Implementation specifics worth flagging:**
- Hook captures `LogitsProcessor.forward(lm_head, hidden_states)`'s `inputs[1]`
- Worker fns are module-level + state is stashed on `model.__kld_captures__` to survive vLLM v1's spawn-based worker isolation
- `VLLM_ALLOW_INSECURE_SERIALIZATION=1` is required (v1 serializer rejects function objects; pickle fallback is needed for module-level fns)
- `_teardown_llm` calls `destroy_model_parallel` + `destroy_distributed_environment` + `gc.collect` + `cuda.empty_cache` between models - `del llm` alone OOMs on the second load

**What rework toward `ExtractHiddenStatesProposer` would look like** (from reading `vllm/v1/spec_decode/extract_hidden_states.py`):
- `speculative_config.method = "extract_hidden_states"`
- `eagle_aux_hidden_state_layer_ids` set per architecture
- `ExtractHiddenStatesModel` writes hidden states into the KV cache via `CacheOnlyAttentionLayer`, retrieved through the KV connector
- Per-architecture work: each new model family needs its layer IDs mapped (Llama, OPT, Mistral, Qwen, Gemma, ...)

**Honest gap on the eager cost:** I don't have a head-to-head benchmark because I never built the spec-decode version. For an offline tool run once per quantization scheme on a single GPU, ~10 min on opt-125m on T4 is tractable, but I can't put a number on what we'd save with graphs preserved. If you have a rough estimate from your own benchmarking work that would be useful.

**Decision points I'd like your call on:**

1. Does an offline eval tool justify accepting the eager cost in exchange for not touching vLLM internals or per-architecture layer-ID configs?

2. If yes, the hook path is essentially done (PR #2659) modulo whatever review feedback you have on the actual code.

3. If no, I'm happy to rework toward `ExtractHiddenStatesProposer`. Two things would help me get unblocked:
   - Is the spec-decode interface considered stable enough for an external eval tool to depend on, or should this live closer to vLLM core?
   - Where should the per-architecture layer-ID mapping table live - `llmcompressor.evaluation` or somewhere else?

I'll wait for your direction before doing more work on the PR.

### HDCharles · 2026-04-28

to be clear, neither approach requires internal changes in vllm. thats not the actual tradeoff

the major tradeoff seems to be using eager + hooks vs hidden_states_extractor

the concerns i have with hooks are as follows
1) eager is going to be slower
2) vllm is complicated and inserting random hooks seems fragile and prone to break across vllm versions. using hidden states extraction (the method we landed on when discussing how to extract hidden states from vllm) has less long term risk.
3) are these hooks going to work in TP implementations?

I also think its probably better to write to disk rather than store on cpu, making the baseline method be as easy to run as possible is ideal and improving latecy with additional hardware can be a followup.

### jayakumarpujar · 2026-04-28

Thanks for the clear breakdown @HDCharles - all three concerns make sense and I agree with the direction.

To answer point 3: hooks do **not** work under TP. Our current implementation already raises `ValueError` for `tensor_parallel_size != 1` precisely because the `lm_head` weight is sharded across ranks and the hook-based capture breaks. So TP support would require the proper `hidden_states_extractor` path anyway.

We'll pivot to:
- `hidden_states_extractor` for hidden state capture (no eager, no hooks)
- Write hidden states to disk (safetensors) between runs
- Load only `lm_head` weights from checkpoint offline for KLD computation

I see PR #2663 by @rpathade is already heading in this direction.

### HDCharles · 2026-04-29

@jayakumarpujar I was considering making a followup about doing this as fast as possible and keeping everything on the gpu for situations where you can run both models at the same time. I had not actually figured out the details for that approach and as of now, I'm not aware of a way to keep the hidden states/logits on the gpu in that scenario without using hooks.

That use case seems a much clearer fit for your approach at a high level. It seems like you could maybe directly extract the logits after the logits processor (wondering if that would solve the TP issue) for both models and compute kld on the fly.

If you want i can make a separate issue for that and assign you.

### jayakumarpujar · 2026-04-29

Yes,  @HDCharles 
please go ahead and open the separate issue and assign me.

The logits-after-`LogitsProcessor` idea is interesting for the TP case. Instead of capturing `inputs[1]` (pre-projection hidden states), capturing the output of `LogitsProcessor` directly gives full logits - no `lm_head` projection needed offline, and the TP gather already happened inside vLLM before the output is returned. That would sidestep the sharded weight problem entirely. Only downside is logits are ~30x larger than hidden states, but if both models fit on GPU simultaneously the bottleneck shifts from disk I/O to compute, so the size tradeoff may be acceptable.

Happy to explore both options (hidden states + offline projection vs direct logit capture) once the issue is up.

### HDCharles · 2026-05-04

@jwpark33 any progress?

### rpathade · 2026-05-05

@HDCharles can you assign this to me please?


### jwpark33 · 2026-05-05

@HDCharles Sorry for the confusion. I misunderstood the ownership status and thought this was already being handled by someone else before it was assigned to me.

Since it looks like someone else is already working on this now, I’ll step back here. I’d be happy to contribute to another issue if there’s anything else I can help with.

### github-actions[bot] · 2026-08-03

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!

### github-actions[bot] · 2026-09-02

This issue has been automatically closed due to inactivity. Please feel free to reopen if you feel it is still relevant. Thank you!
