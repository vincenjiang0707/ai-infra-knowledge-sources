# [Issue #4249] Why is the context axis required for expert sharding when `shard_exp_on_fsdp` is enabled?

source: https://github.com/AI-Hypercomputer/maxtext/issues/4249
state: closed | updated: 2026-07-13T16:59:00Z
labels: feature request

## 正文

### Feature or Model Request

_No response_

### Additional Context

_No response_

## 评论 (4)

### NuojCheng · 2026-06-24

Could you elaborate which lines of code and what errors you met? I don't think context axis is required for the `shard_exp_on_fsdp` flag.

### pathfinder-pf · 2026-06-25

https://github.com/AI-Hypercomputer/maxtext/blob/main/src/maxtext/configs/base.yml#L551 this line

### NuojCheng · 2026-06-25

In MaxText, the `context` axis acts like FSDP to shard weight tensors. Because of this, context always shards the same dimensions as fsdp for weights and optimizer states. With the flag shard_exp_on_fsdp, this pattern is kept.

Alternatively, if you don't want the context axis to shard the expert dimension, you can define custom logical sharding rules. See the [documentation](https://maxtext.readthedocs.io/en/maxtext-v0.2.3/guides/optimization/custom_mesh_and_rule.html) for details.

### NuojCheng · 2026-07-13

Please let us know if there are any further questions. Close for now.
