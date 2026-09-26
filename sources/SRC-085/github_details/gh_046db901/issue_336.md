# [Issue #336] Discussion on EA Layer KV Cache Consistency: Potential Attention Pollution or Intentional Design Choice?

source: https://github.com/SafeAILab/EAGLE/issues/336
state: closed | updated: 2026-06-03T10:52:57Z
labels: 

## 正文

# Description
I've been deep-diving into the EAGLE implementation and found a potential inconsistency in how the EA Layer manages its KV Cache (stable_kv) and tree_mask between consecutive drafting rounds.

## The Core Logic Conflict

1. Base Model Pruning: In update_inference_inputs, the Base Model's KV Cache is correctly pruned to match the accepted path length (L).
2. Small Model Retention: However, the EA Layer's stable_kv is not pruned. If the previous drafting round generated a tree of 64 nodes but only 5 were accepted, stable_kv still physically contains 64 entries.
3. Logical Mask Reset: In topK_genrate, the tree_mask is reset. This reset is perfectly reasonable and necessary because we are starting a new drafting round with a new root.

## The Problem:The "Ghost" Attention
The combination of these steps leads to a mathematical inconsistency:

- In the previous round, the tree_mask acted as a "shield" that prevented nodes from seeing tokens in other branches.
- Once the tree_mask is reset for the new round, this shield disappears.
- Because the stable_kv was never pruned, the new queries in the current round will physically attend to all 64 entries (including the 59 rejected "zombie" nodes).
- This results in Attention Pollution: the new hidden states are computed as a weighted sum that includes information from rejected futures, which violates causal consistency.

## My Concern
I am not sure if this is a minor bug or an intentional design trade-off. Specifically:

1. Is it a Design Choice? Perhaps the computational overhead of pruning the EA Layer's cache outweighs the accuracy gains? Do the Top-K results remain stable enough even with "polluted" attention from rejected branches?
2. Is it a Potential Bug? Even if the position_id remains consistent (as nodes in the same layer share the same ID), the attention mechanism still aggregates values from the un-pruned entries. This could lead to distribution shifts, especially in Sampling mode.


Could you clarify if there's a hidden rationale behind keeping the full stable_kv unpruned? If it is a performance-driven design, have you observed any significant impact on the acceptance rate due to this "context noise"?

## 评论 (1)

### yunzz · 2026-05-14

I would like to update this issue as I have investigated the source code further and clarified my misunderstanding. The concern about "Attention Pollution" is actually addressed by a very clever Incremental Prefill design in the EA Layer.
The confusion stemmed from the distinction between the temporary past_key_values (used during the recursive tree generation) and the persistent self.stable_kv (the "ground truth" cache for the EA Layer).
Causal Consistency: Since the "rejected" branches from the previous round were never committed to self.stable_kv, and the new drafting phase starts fresh from the newly updated stable_kv, there is no "ghost attention" or pollution. The identity mask used for the new root is correct because it only applies to the newly added verified tokens.
Conclusion: 
The implementation is mathematically sound. The EA Layer doesn't need explicit pruning like the Base Model because it uses this offset-based incremental update to synchronize its state with the verified prefix.

I'm closing this issue as the logic is clear now. Hope this helps anyone else digging into the EA Layer's KV management!
