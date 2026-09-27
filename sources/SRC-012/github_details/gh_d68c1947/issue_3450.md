# [Issue #3450] [Feature Request] Integrate DFlash Speculative Decoding

source: https://github.com/mlc-ai/mlc-llm/issues/3450
state: open | updated: 2026-03-27T15:50:35Z
labels: feature request

## 正文

## 🚀 Feature

Integrate [[DFlash speculative decoding](https://arxiv.org/abs/2602.06036)](https://arxiv.org/abs/2602.06036) into MLC LLM

## Motivation

DFlash is a new speculative decoding method where the speculator is a diffusion-based LM which shares a KV cache with the original model. It has a  higher acceptance rates and a more unified architecture.

Instead of the draft model guessing tokens one by one (which creates a sequential bottleneck), DFlash generates an entire block of tokens all at once in a single forward pass. It does this by hooking into the target model's hidden states (KV injection), letting a tiny diffusion adapter see the target's context, increasing draft accuracy.

## Alternatives

- Standard Autoregressive Drafting (like EAGLE-3): While EAGLE is great, the drafter is still spitting out tokens sequentially. Drafting a long sequence still takes linear time, limiting how fast we can actually go. DFlash handles the whole block in constant time.
- Medusa / Multi-Head: These give awesome parallel drafting, but they usually require messing with the base model's architecture and dealing with complex tree attention. DFlash lets us keep the target model completely frozen.

## Additional context

- The paper shows massive speedups—up to 6x lossless acceleration on models like Qwen3.
- It is already merged into SGLang and vLLM is reportedly working on it too.
- To get this working, we're going to need to tweak `MLCEngine`. Specifically, we need a clean way to route the target model's hidden state embeddings into the drafting phase, and we need to update the speculative loop so it can take a full block of tokens simultaneously instead of looping sequentially.
- I am currently building this out in a fork and would love to merge it upstream when it's ready. I'd love to get the maintainers' thoughts on the best way to handle routing those hidden states in C++ without breaking the existing Model interface abstractions before opening the PR

## 评论 (1)

### JiwaniZakir · 2026-03-27

The core integration challenge here is that MLC LLM's existing speculative decoding pipeline (likely in `serve/draft_executor` or the engine's speculative loop in `cpp/serve/`) assumes token-by-token autoregressive draft generation, so the batch-token draft path DFlash requires would need a parallel code branch rather than a loop modification. The more significant hurdle is KV injection: MLC's `Model` interface (defined in `cpp/serve/model.h`) currently exposes logits and KV cache state but not intermediate hidden states, so surfacing those embeddings to the diffusion adapter without breaking the existing abstraction would likely require adding a hidden-state output variant to `ModelWorkspace` or a new engine-level callback hook. The SGLang implementation's approach to this boundary—whether they expose hidden states at the model API level or handle it entirely within the attention kernel—would be worth examining as a reference point before settling on the C++ interface design for MLC.
