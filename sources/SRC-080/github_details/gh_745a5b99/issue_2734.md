# [Issue #2734] GPTQModifier hangs on multi-rank with sharded MoE experts (dist.reduce/broadcast on disjoint module sets)

source: https://github.com/vllm-project/llm-compressor/issues/2734
state: closed | updated: 2026-09-13T23:35:46Z
labels: stale

## 正文

## Summary

`GPTQModifier._reduce_hessian_to_target_rank` and `_broadcast_quantized_params` enqueue `dist.reduce` / `dist.broadcast` calls per module in the rank-local `module_list`. When the model is sharded such that **some modules exist on only one rank** (the canonical case: decoupled MoE expert sharding in DeepSeek-V4-Flash where each rank owns `n_routed_experts // world_size` experts), the per-rank `module_list` diverges, ranks call collectives on disjoint module subsets, and NCCL hangs (eventually timing out — or never timing out if `NCCL_TIMEOUT` is high enough).

The bug is latent for any sharding model that produces uniform `module_list` across ranks (e.g. HF `accelerate` auto-offload, where every rank holds the same module set, just with disk spill). It bites the moment a sharding strategy produces disjoint module sets.

## Affected versions

- `llmcompressor` `kylesayrs/transformers-v5` branch HEAD `f2aa32e2bde1941182d8f8a348837574969335e6` (verified on Hopper SM 9.0a / H200, multi-rank torchrun with `n_routed_experts=256`, `world_size=8`, `n_local_experts=32`).
- Code path: `src/llmcompressor/modifiers/gptq/base.py` lines 323 (`_reduce_hessian_to_target_rank`) and 350 (`_broadcast_quantized_params`).

## Reproduction

Architecture: DeepSeek-V4-Flash (256 routed experts × 43 main MoE layers + 1 MTP MoE layer, 568 GB BF16).

Sharding: each rank holds `experts[rank * 32 : (rank+1) * 32]` (the rest are `None` placeholders in the `nn.ModuleList`). `named_modules()` enumerates only the non-None children → per-rank counts:

```
[shard-invariant] OK — 43 main MoE layers + 1 MTP layer(s), 11264 total
(layer,expert) tuples, disjoint across 8 ranks
(per-rank counts: [1408, 1408, 1408, 1408, 1408, 1408, 1408, 1408])
```

Recipe (W4A16 routed experts + FP8_BLOCK attention, weight-only):

```python
from llmcompressor.modifiers.quantization import GPTQModifier
GPTQModifier(
    config_groups={
        "attention": QuantizationScheme(
            targets=[r"re:.*\.attn\.(wq_a|wq_b|wkv|wo_a|wo_b)$"], weights=FP8_BLOCK),
        "experts": QuantizationScheme(
            targets=[r"re:.*\.ffn\.experts\.\d+\.(w1|w2|w3)$"], weights=W4A16),
    },
)
```

Launch:

```bash
torchrun --nproc-per-node=8 quantize.py --samples 8 --batch-size 1 --max-seq-len 128
```

**Without the patch:** the run completes calibration on the first subgraph (layer 0 forward + Hessian build), reaches `compress_module_list`, calls `_reduce_hessian_to_target_rank`, and hangs at `dist.reduce` on the first sharded module — rank 0 has experts 0..31 in its `module_list`, rank 1 has experts 32..63, and `dist.reduce(hessians[expert_0], dst=...)` from rank 0 has no matching call from rank 1.

**With the patch:** subgraph 6 (layer 5 quantization in our dry-run setup) progresses through all 32 experts × 3 weights per rank, and the run continues to subgraph 7.

## Proposed fix (concept)

Expose a per-module "replication group" attribute on the quantization
config. Gate `_reduce_hessian_to_target_rank` and
`_broadcast_quantized_params` on it: only modules in the full-rank
replication group participate in cross-rank collectives.

## Workaround (inline)

Three patches applied at script-startup time:

**A — `Observer.synchronize` no-op when `world_size > 1`** (defensive; same disjoint-set hazard via `QuantizationMixin.sync_activation_observers` line 285 of `quantization/mixin.py` — fires for activation-quantization recipes; weight-only GPTQ doesn't trigger it directly but defensive coverage is cheap):

```python
import llmcompressor.observers.base as _obs_base
import llmcompressor.observers.moving_base as _obs_moving
_obs_base.Observer.synchronize = lambda self: []
_obs_moving.MovingAverageObserverBase.synchronize = lambda self: []
```

**B — `_reduce_hessian_to_target_rank` pre-filters `module_list` to exclude sharded modules:**

```python
import llmcompressor.modifiers.gptq.base as _gptq
import re
EXPERT_NAME_RE = re.compile(r"\.ffn\.experts\.\d+\.")
_orig = _gptq.GPTQModifier._reduce_hessian_to_target_rank

def _patched(self, module_list, module_to_rank):
    replicated = [m for m in module_list
                  if not EXPERT_NAME_RE.search(self._module_names.get(m, ""))]
    return _orig(self, replicated, module_to_rank)

_gptq.GPTQModifier._reduce_hessian_to_target_rank = _patched
```

**C — `_broadcast_quantized_params` same pre-filter.** (Identical pattern.)

Empirical confirmation on H200 8× p5en today: 8-rank GPTQ multi-rank dry-run reaches subgraph 6/45 cleanly with patches active. Log line `[patch B] skipped reduce for 48 sharded modules; reducing 4 replicated` confirms the filter fires on the expected ratios.

A sharding-invariant assertion is also wise — walks `named_modules()`, all-gathers `(layer_id, expert_id)` tuples across ranks, asserts disjointness before the patches take effect — protects against accidental replication corrupting the Hessian.

## Why this matters

DeepSeek-V3 / V4 routed-expert models are the headline use case for `llmcompressor` GPTQ multi-rank calibration. The `device_map="auto_offload"` path (HF accelerate) is the only currently-validated path; for very large MoE models with insufficient system RAM to spill the full model on every rank, **decoupled expert sharding is the obvious memory strategy** (`8 × 568 GB = 4.5 TB` of CPU RAM is not on every box). The library should support this sharding pattern out of the box.

## Related

- #2735 — DSv4 example drops MTP layer (related)
- #2736 — `compress_module_list` line 304 synchronous device→host stall (downstream of this issue's patches)

cc @kylesayrs

## 评论 (5)

### pasta-paul · 2026-05-20

Confirming the same disjoint-module-set hazard reproduces in the **observer-sync path**, not just the GPTQ-Hessian path — and on a **weight-only RTN recipe** (NVFP4 experts + FP8_BLOCK attention) where there is no Hessian and no cross-rank Hessian reduce.

## Reproducer (NVFP4 + FP8_BLOCK, weight-only, 4-rank torchrun on B300 SM 10.0a)

Recipe:
```python
QuantizationModifier(
    config_groups={
        "attention": QuantizationScheme(
            targets=[r"re:.*\.attn\.(wq_a|wq_b|wkv|wo_a|wo_b)$",
                     r"re:.*mtp\.\d+\.(e_proj|h_proj)$"],
            format="float-quantized", **FP8_BLOCK),
        "experts": QuantizationScheme(
            targets=[r"re:.*\.ffn\.experts\.\d+\.(w1|w2|w3)$"],
            format="nvfp4-pack-quantized", **NVFP4),
    },
)
```

Sharding: 256 routed experts × 8 ranks → each rank owns `n_routed_experts // world_size = 32` experts; non-owned slots are `None` in the `nn.ModuleList`. `match_named_modules` therefore enumerates a disjoint module set per rank.

## Where it hangs

Without the patches, the 4-rank dryrun hangs at subgraph 6/45. py-spy across all 4 ranks shows everyone stuck inside `sync_activation_observers` → `update_offload_parameter` → `update_offload` → `__torch_function__`. The relevant `dist.all_reduce` calls live in `Observer.synchronize`:

- `llmcompressor/observers/base.py:138-160` (static min/max reduce with `ReduceOp.MIN`/`MAX`)
- `llmcompressor/observers/moving_base.py:102-125` (moving-average reduce with `ReduceOp.AVG`)

`mixin.sync_activation_observers` (`llmcompressor/modifiers/quantization/quantization/mixin.py:296`) iterates matched modules and calls `observer.synchronize()` per match, then `wait_for_comms(pending_comms)`. With expert sharding, each rank's match list is disjoint → ranks call `dist.all_reduce` on different module identities → NCCL desync. Same root cause as the GPTQ-Hessian path described in this issue, one level up the call stack (the observer layer, called by both GPTQ and weight-only RTN paths).

## Workaround (in-repo monkey-patch)

```python
import llmcompressor.observers.base as _obs_base
import llmcompressor.observers.moving_base as _obs_moving
_obs_base.Observer.synchronize = lambda self: []
_obs_moving.MovingAverageObserverBase.synchronize = lambda self: []
```

Applied after `apply_dist_state()`, before `oneshot()` is called.

## A/B verification that the workaround is sound for RTN recipes

I ran the same recipe on (a) 1-rank with the patch, (b) 4-rank with the patch. Compared `weight_scale` tensors at layer 5 for shared modules (attention) and one rank-owned module (expert 0). Result:

| | 1-rank |mean\| | 4-rank |mean\| | ratio |
|---|---|---|---|
| layer 5 expert 0 w1.weight_scale | 1.778e+02 | 1.778e+02 | 1.000 |
| layer 5 expert 0 w2.weight_scale | 1.751e+02 | 1.751e+02 | 1.000 |
| layer 5 expert 0 w3.weight_scale | 1.794e+02 | 1.794e+02 | 1.000 |
| layer 5 attn.{wq_a,wq_b,wkv,wo_a,wo_b}.weight_scale | (identical shape/dtype/min/max/mean across all 5) | | 1.000 |

This is exact because NVFP4 + FP8_BLOCK as configured here are RTN-style — scales are derived from the weight tensors themselves, not from activation observer stats. The observers exist but their cross-rank sync doesn't affect the resulting scale tensors. **For activation-quantized recipes** (W4A8, dynamic-input W8A8) the no-op patch would lose cross-rank sample averaging — different decision.

## Implications for the fix design proposed in this issue

The "replication-group attribute on the quantization config" design discussed here generalizes cleanly to both the GPTQ-Hessian path and the observer-sync path — both call collectives per-matched-module, both crash on disjoint sets. Gating both paths on the same attribute is one change.

For the observer-sync path specifically, an even smaller fix is to skip `Observer.synchronize`'s `dist.all_reduce` when the observer's owning module isn't present on all ranks (auto-detect via an initial `all_gather` of "do you own this module name?" booleans). But that's more invasive in `Observer.__init__` plumbing. The explicit attribute is the right balance.

Happy to follow up with a draft PR if helpful.

### pasta-paul · 2026-05-27

> **Disclosure:** this comment was generated with AI assistance.

**Branch-state update — pinned SHA is stale.** When this issue was filed (2026-05-20) the citation was `kylesayrs/transformers-v5` HEAD `f2aa32e2`. As of 2026-05-26 the branch is at `7e2c6bfe` — **56 commits ahead, 18 behind, status: diverged**. GPTQ-relevant landings during that window include #2670 (modifier-level ActivationOrdering for all weight strategies) and #2682 (use modules list for sequential epoch end).

The disjoint-`module_list` issue is architectural — `dist.reduce` / `dist.broadcast` against a per-rank list that diverges across ranks under decoupled MoE sharding — so it should reproduce on current HEAD unless one of the post-pin commits changed how `module_list` is constructed. We haven't re-verified against `7e2c6bfe`. Will refresh the repro on current HEAD and update; flagging here so reviewers don't burn cycles checking the stale line numbers.

### Tobi-Adesoye · 2026-06-15

@pasta-paul This NCCL desynchronization is classic when applying traditional weight modifiers to distributed MoE setups. Because standard quantization observers run loops over identical execution graphs across ranks, they assume homogeneous module boundaries. With disjoint sharded experts, Rank A is running an observer sync step on an expert ID that Rank B doesn't even have in its memory map, causing the global synchronization primitive to hang indefinitely.

The solution requires decoupling the layer-wise tracking from the physical model graph entirely—managing variance and quantization scaling factors via an isolated, stateless mathematical hook rather than relying on global in-place module observation passes.

### github-actions[bot] · 2026-09-13

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!

### kylesayrs · 2026-09-13

Closing, tensor/expert parallel is not supported, only data parallel is supported.
