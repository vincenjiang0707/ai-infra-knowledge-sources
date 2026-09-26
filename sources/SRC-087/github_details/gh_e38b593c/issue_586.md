# [Issue #586] [RFC]: Gemma4 MTP support

source: https://github.com/vllm-project/speculators/issues/586
state: open | updated: 2026-07-14T18:48:43Z
labels: RFC

## 正文

### Motivation.


We want to support **training Gemma4 MTP draft models** in speculators.

MTP finetuning already works for the Qwen-style architecture, as of: 1. the MTP algorithm, converter, and stitcher are merged (#452), and 2. MTP finetuning is wired into the shared training infrastructure with online/offline paths, and e2e
tests (#366). 

This RFC covers the Gemma4-specific delta on top of that MTP support. Gemma4's MTP drafter differs from the Qwen-style architecture in two ways the current stack cannot express:

1. The drafter shares the verifier's KV cache. Gemma4's MTP attention is
   query-only: it has no K/V projections and no KV cache of its own. At inference it
   borrows the verifier's last local and last global attention KV caches and cross-attends into them. 
2. A sparse LM head. The drafter does not use a flat draft-vocab
   LM head; it uses a centroid-masked (multi-level) head for efficient decoding.

Consequence for training:  Gemma4's drafter is not self-contained: its query-only attention has nothing to attend to
unless the verifier's KV tensors are supplied as training inputs, the same way hidden states are supplied today. There is currently no way to get those KV tensors out of the verifier and into the training process.

So Gemma4 MTP finetuning needs work on both sides of:
- vLLM: export the relevant verifier KV caches alongside hidden states.
- speculators: a Gemma-specific model definition, a data path that loads and aligns those KV tensors, and LM-head support.

This RFC proposes the speculators-side design and the shared data contract; the vLLM
KV-export mechanism is covered by the companion vLLM RFC.

### Proposed Change.


High-level: extend the offline-extraction data contract with verifier KV caches, add a Gemma4 MTP model definition that consumes them, and add multi-level LM-head support.

1. Shared data contract.
For Gemma4 we extend it with the two verifier KV caches the drafter shares:

```
{
  hidden_states:            [seq, n_layers, hidden]   
  token_ids:                [seq]                      
  verifier_kv_last_local:   [seq, kv_heads, head_dim] # new — K and V of the last sliding layer
  verifier_kv_last_global:  [seq, kv_heads, head_dim] # new — K and V of the last full layer
}
```

2. Gemma4 MTP variant. The Gemma4 variant provides a query-only attention module that consumes the injected verifier K/V instead of projecting/attending over its own sequence; the pre/post projection that fuses verifier hidden states with the drafter's token embedding.

3. Training data path. Extend the dataset/collation layer to load the verifier KV caches from the per-sample files, position-align them to the token sequence (the existing alignment check between stored tokens and training inputs must cover the KV tensors too), and route them into the Gemma draft model during the forward pass. This should reuse the existing per-algorithm argument-passing mechanism, so no changes to the core training loop are expected.

4. Multi-level LM head support. Represent the centroid-masked head in the Gemma variant and its training loss. Note the MTP code currently uses a flat LM head and explicitly disallows vocab reduction, so the multi-level head is a new capability.


### Any Other Things.

_No response_

## 评论 (2)

### Sridhar1030 · 2026-06-10

@Beichen-Ma are you working on this ? If not i am happy to contribute 


### Beichen-Ma · 2026-06-10

Yes, I am currently working on this.
