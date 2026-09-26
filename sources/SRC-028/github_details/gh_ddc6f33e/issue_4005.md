# [Issue #4005] MoE throughput regression: `activation_batch_moe` missing `'expert'` axis + `minimal_flash` not checkpointing MoE intermediates

source: https://github.com/AI-Hypercomputer/maxtext/issues/4005
state: closed | updated: 2026-05-28T16:55:36Z
labels: bug

## 正文

### Bug report


#### Problem

I found two independent bugs on `main` that cause a **2.6x throughput regression** for MoE
training on any config using `capacity_factor > 0` (einsum/dense_matmul path) with
expert-parallel sharding as the primary axis (e.g., single-node GPU with
`ici_expert_parallelism=-1`).

**Bug 1 — Missing expert axis (2.5x regression, PRs #3473 / #3606):**
`activation_batch_moe` in `base.yml` maps to `['data', 'fsdp', 'fsdp_transpose']` without
`'expert'`. On configs where `expert` is the only active physical mesh axis (all others
size 1), MoE activations become effectively unsharded. This was likely invisible in upstream
testing because TPU v5p-8 uses `fsdp` as the primary axis, and GPU tests used
`ici_expert_parallelism=1`.

**Bug 2 — Remat checkpoint mismatch (7% regression, PRs #3414 / #3505):**
Checkpoint annotations in `moe.py` were renamed from `mlpwi_*` to `moe_mlpwi_*`, but
`minimal_policy()` in `nnx_decoders.py` was not updated to include the new names. The
`minimal_flash` remat policy silently stops checkpointing MoE intermediates, causing
unnecessary recomputation. PR #3505 partially addressed this but only fixed `types.py`,
not `nnx_decoders.py`.

#### Benchmarks

All results on 1x MI325X node (8 GPUs), DeepSeek V2 Lite 16B, `per_device_batch_size=8`,
`ici_expert_parallelism=-1`, `capacity_factor=1.25`, `remat_policy=minimal_flash`:

| Configuration | TFLOP/s | vs Baseline | Description |
|---|---|---|---|
| [`rocm/maxtext` `release/v26.4`](https://github.com/rocm/maxtext/tree/release/v26.4) (baseline) | 318 | — | Before PRs #3473/#3414; most recent commit includes MoE fix |
| Current `main` (broken) | 120 | **2.6x slower** | Both bugs present |

Note: `release/v26.4` refers to the branch in [`rocm/maxtext`](https://github.com/rocm/maxtext),
which is AMD's fork of `AI-Hypercomputer/maxtext`. The most recent commit on that branch
already contains the MoE sharding fix, making it a known-good baseline.

#### Proposed fix options

I tested five approaches. All fix the primary sharding regression; they differ in how they
handle the remat checkpoint names.

| Option | TFLOP/s | vs Baseline | Sharding fix | Remat fix | Files changed |
|---|---|---|---|---|---|
| A | 324 | 1.02x | Revert `_moe` axis names in `moe.py` | Revert checkpoint names to `mlpwi_*` | `moe.py` |
| B | 361 | 1.13x | Add `'expert'` to `activation_batch_moe` in `base.yml` | Revert checkpoint names to `mlpwi_*` | `base.yml`, `moe.py` |
| B' | 336 | 1.06x | Add `'expert'` to `activation_batch_moe` in `base.yml` | Add `moe_mlpwi_*` to `minimal_policy()` | `base.yml`, `nnx_decoders.py` |
| **B''** | **360** | **1.13x** | **Add `'expert'` to `activation_batch_moe` in `base.yml`** | **Stack both names: inner `mlpwi_*` + outer `moe_mlpwi_*`** | **`base.yml`, `moe.py`** |
| C | 324 | 1.02x | Surgical: only restore `activation_batch` on masks/gate_logits | Revert checkpoint names to `mlpwi_*` | `moe.py` |

**Option A** (324 TFLOP/s): Revert all `_moe` axis names and checkpoint names in `moe.py`.
Full recovery. Discards the axis separation refactor from PRs #3473/#3606.

**Option B** (361 TFLOP/s): Add `'expert'` to `activation_batch_moe` in `base.yml` + revert
checkpoint names in `moe.py`. Best raw performance. Preserves code structure but MoE and
dense MLP share remat names, losing independent remat control from PR #3414.

**Option B'** (336 TFLOP/s): Add `'expert'` to `base.yml` + add `moe_mlpwi_*` names to
`minimal_policy()` in `nnx_decoders.py`. Preserves independent MoE remat control. 7% slower
than B because distinct checkpoint names on shared vs routed experts within MoE layers
prevent XLA from merging their remat schedules.

**Option B'' (recommended)** (360 TFLOP/s): Add `'expert'` to `base.yml` + stack both
checkpoint names in `moe.py` (inner `mlpwi_*` matched by `minimal_flash`, outer
`moe_mlpwi_*` for custom policies). Best performance AND independent MoE remat control.
No changes to `nnx_decoders.py`.

**Option C** (324 TFLOP/s): Only restore `activation_batch` on mask and gate_logit tensors
(pre-dispatch), keeping `activation_batch_moe` on dispatch/mlp axes (post-dispatch). Most
semantically precise but more surgical edits, and 10% slower than B/B''.

#### Notes for the shard_map path

The `shard_map` path (`sparse_matmul`, used when `capacity_factor <= 0`) handles expert
partitioning via `shard_map` itself, so adding `'expert'` to `activation_batch_moe` should
be harmless there — JAX ignores redundant sharding constraints inside `shard_map`. However,
this should be verified on TPU configs that use the shard_map path (e.g., DeepSeek V3 with
`capacity_factor=-1`).

cc @NuojCheng (PRs #3473, #3606) @abhinavgoel95 (PRs #3414, #3505)

### Logs/Output

_No response_

### Environment Information

_No response_

### Additional Context

_No response_

## 评论 (1)

### NuojCheng · 2026-05-28

Thank you for the investigation. Dense matmul in maxtext is only used for correctness verification and no longer for performance benchmarking, at least for TPU usages. The PR LGTM.
