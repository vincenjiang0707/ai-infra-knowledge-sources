# [Issue #782] RFC: Add DeLS-Spec (Decoupled Long-Short Contexts) speculator

source: https://github.com/vllm-project/speculators/issues/782
state: open | updated: 2026-07-22T07:40:22Z
labels: 

## 正文

## Summary

Implement the DeLS-Spec speculative decoding method from [DeLS-Spec: Decoupled Long-Short Contexts for Parallel Speculative Drafting](https://arxiv.org/abs/2607.07409) (Zheng & Li, July 2026).

## Method

DeLS-Spec extends DFlash-style block-parallel drafting by adding a lightweight **local head** (short-context expert) alongside the DFlash model (long-context expert). Key properties:

- **GRU-based local head**: Captures intra-block causal dependencies that DFlash's position-wise parallel predictions miss
- **Independent training**: The local head trains with standard NTP loss on plain text — no target model hidden states, no joint optimization with DFlash
- **Product-of-experts fusion**: At inference, logits are combined: `l = l_DFlash + α·l_local − β·l_prior`
- **Extremely low training cost**: Only the small GRU + projection layers are trained; embeddings are frozen from the verifier

## Architecture

| Component | Details |
|-----------|---------|
| Input | Frozen verifier embeddings (shared) |
| Sequential head | GRU (configurable hidden size, default 1024) |
| Projection | Low-rank linear → vocab (default rank 256) |
| Variants | `rnn` (GRU) or `markov` (bigram lookup) |
| Trainable params | ~22M (vs ~489M total with frozen embeddings) |

## Relationship to existing methods

- **vs DFlash**: DeLS-Spec adds intra-block causality without modifying DFlash
- **vs DSpark**: DSpark trains jointly with DFlash and uses DFlash backbone hidden states; DeLS-Spec trains independently and uses only frozen verifier embeddings
- **vs Domino**: Similar goal (add causality to block-parallel drafting) but Domino requires retraining from scratch

## Results (from paper)

Evaluated on Qwen3 models across math, code, and dialogue benchmarks. DeLS-Spec consistently improves both decoding speedup and average acceptance length over standalone DFlash.

## Implementation scope

- [x] `speculators` model implementation (`DelsSpecDraftModel`, `DelsSpecSpeculatorConfig`)
- [x] Training integration (CLI args, registry)
- [x] Smoke training validates learning signal
- [ ] vLLM inference integration (requires DFlash proposer modification for logit fusion — separate PR)
- [ ] Full-scale training evaluation

## 评论 (1)

### HaizhouPeng · 2026-07-22

++++

