# [Issue #3023] [Bug] AutoRoundModifier: input_capture_hook accumulates GPU memory during optimization when gradient_accumulate_steps > 1

source: https://github.com/vllm-project/llm-compressor/issues/3023
state: closed | updated: 2026-08-18T17:30:14Z
labels: 

## 正文

# [Bug] AutoRoundModifier: input_capture_hook accumulates GPU memory during optimization when gradient_accumulate_steps > 1

## Environment

- llm-compressor: current main (1677fece)
- auto-round: latest
- PyTorch: 2.x, CUDA
- Hardware tested: 8 × RTX 5880 (44 GB), `Qwen/Qwen3.5-35B-A3B` (MoE)

## Bug Description

`AutoRoundModifier` registers `input_capture_hook` as a `forward_pre` hook on
all decoding layers in `on_calibration_start()`.  This hook is **never disabled
before the SignSGD optimization loop**, so every mini-batch forward pass during
optimization also triggers it.

With `gradient_accumulate_steps=N`, the hook appends N copies of
`(args, kwargs)` — each containing the full `hidden_states` tensor — into
`_all_module_input` per outer iteration.  These tensors are not released until
`post_autoround_cleanup()` calls `_all_module_input.clear()` after the entire
optimization run for that layer finishes.

## Reproduction

```python
from llmcompressor import oneshot
from llmcompressor.modifiers.autoround import AutoRoundModifier

# Monitor torch.cuda.memory_allocated() during calibration:
# it grows by ~gradient_accumulate_steps × hidden_states_bytes each outer iteration.

recipe = AutoRoundModifier(
    iters=200,
    batch_size=1,
    gradient_accumulate_steps=8,  # paper default — triggers the bug
    scheme="W4A16",
)
oneshot(model="<any model>", recipe=recipe, dataset="<calibration data>")
```

## Measured Impact

On `Qwen/Qwen3.5-35B-A3B` (hidden_size=2048, seq_len=6144, bf16):

| Parameter | Value |
|---|---|
| `gradient_accumulate_steps` | 8 |
| `hidden_states` size per sample | 24 MB |
| Memory growth per outer iter | **+204 MB** |
| Total accumulation at ITERS=200 | **~40 GB** |
| Result | OOM on 44 GB GPUs |

```
[MEM-ITER]   1  Δalloc=+204.4MB  alloc=13234MB
[MEM-ITER]   2  Δalloc=+204.4MB  alloc=13438MB
[MEM-ITER]   3  Δalloc=+204.4MB  alloc=13642MB
...
```

## Root Cause

```
on_calibration_start()
  → register_hook(module, input_capture_hook, "forward_pre")

apply_autoround()
  → ar.quantize_block(block, inputs=ar_inputs, ...)     # ITERS optimization steps
      → for each outer iter:
          for each mini-batch (gradient_accumulate_steps times):
            BlockForwardRunner.forward()
              → decoding_layer.forward()                # triggers forward_pre hook!
                  → input_capture_hook()
                      → _all_module_input[name].append((args, kwargs))
                                                 ↑
                                    hidden_states kept alive
```

The hook was intended only for the calibration pass but fires during optimization too.

## Proposed Fix

The fix requires distinguishing two states that look identical from the dict alone:
**"this layer has never been seen"** (calibration phase, hook should capture) vs
**"this layer's inputs were already consumed by apply_autoround()"** (optimization
phase, hook should be a no-op).

Checking `if name not in _all_module_input` does not work: after `pop()` the key
is absent, so the calibration-phase first fire is also blocked — causing `KeyError`
when the next layer's inputs are requested.

The correct approach is a separate "consumed" tracking structure alongside
`_all_module_input` so that the hook can distinguish the two cases.  The fix
touches only `AutoRoundModifier` in `base.py` and produces a diff of ~+17/-4 lines
against `main`.

## Verification

After fix, on the same setup:

```
[MEM-ITER]   1  Δalloc=+0.0MB  alloc=11276MB
[MEM-ITER]   2  Δalloc=+0.0MB  alloc=11276MB
[MEM-ITER]   3  Δalloc=+0.0MB  alloc=11276MB
...
[MEM-PTR] iter=2: 2 new tensors (+48.0MB new, -48.0MB freed)  ← legitimate pred/ref, freed same iter
```

Memory is completely flat across all 8 ranks for 20 iterations.

## PR Ready

I have a clean fix on branch `fix/autoround-input-capture-hook-leak` (forked from
`vllm-project/llm-compressor` at `1677fece`) with a single-file diff of
+17/-4 lines against `main`.  Happy to submit a PR once the approach is confirmed.

## 评论 (1)

### yiliu30 · 2026-08-12

Hi @xesdiny, thanks for raising this issue! I have assigned it to you, and let's discuss the fix details in the PR.
