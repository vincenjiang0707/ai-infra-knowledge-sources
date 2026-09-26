# [Issue #2209] Per-expert weight_quantizer._amax fails Megatron validate_sharding_integrity on topology reshard (TEGroupedMLP NVFP4)

source: https://github.com/NVIDIA/Model-Optimizer/issues/2209
state: closed | updated: 2026-09-15T14:43:34Z
labels: 

## 正文

### Bug

Megatron distributed-checkpoint `validate_sharding_integrity` rejects the per-expert MoE `weight_quantizer._amax` tensor introduced by #1550 ("Support per expert weight quantizer in TEGroupedMLP") when the quantized checkpoint is saved and then reloaded under a different parallel topology (or is an older golden checkpoint):

```
megatron.core.dist_checkpointing.core.CheckpointingException: Invalid sharding pattern validation.
Invalid access pattern for ShardedTensor(
  key='decoder.layers.1.mlp.experts.experts.16.linear_fc1.weight_quantizer._amax',
  dtype=torch.bfloat16, local_shape=(1,), global_shape=(1,))
```

The per-expert scalar `_amax` is registered with `global_shape=(1,)` and no expert-axis identity, so multiple experts/ranks resolve to the same global offset and integrity validation fails. On multi-rank saves the first failure is followed by secondary `ncclRemoteError: remote process exited prematurely` on other ranks.

The `_global_amax` variant already rides with a global expert identity (see `modelopt/torch/quantization/plugins/megatron.py`), but the plain per-expert `weight_quantizer._amax` does not appear to get the same treatment on reshard.

### Where it reproduces (nmm-sandbox CW-DFW L0)

- `examples/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16/megatron_lm_qad_regression.yaml` — quantize saves then train/eval reloads `/scratchspace/golden_curve_qad/te/nano30b_nvfp4_quant` (TP=4 ETP=1 EP=8), fails on load.
- `services/megatron-lm/quantize/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16.yaml` — NVFP4 PTQ save/load, same `_amax` validation failure + downstream NCCL fallout.

Both were green before the per-expert-quantizer change and have been failing since; they are now quarantined (allow-to-fail) in nmm-sandbox CI pending this fix.

### Suggested direction

Give the per-expert `weight_quantizer._amax` sharded tensors a correct global expert identity (matching the `_global_amax` handling) so they reshard across TP/EP/ETP topology, or exclude the scalar per-expert `_amax` from `validate_sharding_integrity`. Related in-flight work: #1553 (NVFP4 `_global_amax` TP/EP sync — adjacent but touches calibration, not the checkpoint sharding metadata).

_Filed from nmm-sandbox pipeline #63140716 (CW-DFW). Introduced by #1550._


## 评论 (3)

### mohityadav8 · 2026-08-28

@kevalmorabia97 @jenchen13 can i work in this issue ?

### jenchen13 · 2026-09-04

I have a fix for this in https://github.com/NVIDIA/Model-Optimizer/pull/2319

### jenchen13 · 2026-09-15

this has been fixed by #2319 
