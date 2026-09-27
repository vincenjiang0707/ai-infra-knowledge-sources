# [Issue #5288] [MP] Model sparse presence domains across kernel groups

source: https://github.com/LMCache/LMCache/issues/5288
state: open | updated: 2026-09-26T10:46:40Z
labels: 

## 正文

## Background

The MP transfer path currently uses one presence decision per object-group chunk. An object group may contain multiple kernel groups, while `all_null_chunk_masks()` marks the object absent only when every block ID represented by that object equals the configured null sentinel.

This assumes all kernel groups in one object share a presence domain. If a future connector places independently sparse kernel groups in the same object, one group can be absent while another is present for the same chunk. The object-level mask then cannot describe both groups safely.

This came up while reviewing #5132. The current consumers do not trigger the divergent case:

- vLLM's historical block `0` sentinel is an allocated null block.
- ATOM's native STATE image is indivisible, so every STATE ordinal has the same absent prefix and the same present checkpoint endpoint.

## Design question

LMCache should make the shared-presence assumption explicit or represent independent presence. Two possible approaches are:

1. Add an explicit presence-domain identity to group registration/object-group construction and only combine kernel groups that share it.
2. Carry per-kernel-group presence masks through staging and the transfer implementation.

This needs to account for object-key/layout compatibility, `separate_object_groups=False`, store reservation/commit behavior, retrieve lookup semantics, and GPU block-ID staging.

## Suggested regression coverage

Add a case where two candidate kernel groups disagree on nullness for the same chunk and verify the selected design either separates them into different objects or skips the absent group without staging/dereferencing its sentinel.


## 评论 (1)

### neevmodh · 2026-09-26

This is a good forward-looking catch — flagging a latent assumption before it becomes a real bug is exactly the kind of review that prevents a much harder debugging session down the line.

I don't have enough context on the object-group/kernel-group staging internals (or the discussion in #5132) to responsibly weigh in on approach 1 vs 2 here — the tradeoff space you outlined (object-key/layout compatibility, `separate_object_groups=False`, store/retrieve semantics, GPU block-ID staging) needs someone who's worked in that code directly. I don't want to add noise with an uninformed opinion on an architectural decision with this much surface area. Following for the resolution — happy to help with the regression coverage you outlined once a direction is picked, since writing the two-kernel-groups-disagree test case is more mechanical once the design lands.
