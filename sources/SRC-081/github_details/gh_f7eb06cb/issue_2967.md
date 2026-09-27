# [Issue #2967] calibration_data_device="balanced" → CUDA illegal memory access at scale (long seqlen + many samples + multi-GPU); "cpu" works

source: https://github.com/ModelCloud/GPTQModel/issues/2967
state: closed | updated: 2026-07-23T23:00:46Z
labels: 

## 正文

## Describe the bug
Quantizing with `QuantizeConfig(..., calibration_data_device="balanced")` on 8 GPUs with **many long calibration samples** dies with `CUDA error: an illegal memory access was encountered`. Switching the same run to `calibration_data_device="cpu"` completes all layers, and keeping `balanced` but using **fewer samples** also completes. So it is specific to the `balanced` calibration-cache path (added in #2608) under load.

The failure is a memory *corruption*, not an OOM: it surfaces at a **shifting** layer/module (we saw `linear_attn.in_proj_qkv` @ layer 16, `mlp.gate_proj` @ layer 27, `self_attn.o_proj` @ layer 27 across otherwise-identical runs), and at crash time each GPU still has **60GB+ free** and host RAM is far from full and non-monotonic. The shifting surface + healthy memory is the classic signature of an out-of-bounds write whose damage is read later.

## Reproduction matrix (all else identical: 8×80GB GPUs, `device_map="auto"`)
| calibration_data_device | samples | seqlen | result |
|---|---|---|---|
| **balanced** | 128 | 65536 | **CUDA illegal memory access** (layer ~16–27, shifts run to run) |
| cpu | 128 | 65536 | ✅ completes all layers |
| balanced | 16 | 65536 | ✅ completes |
| balanced | 128 | 32768 | ✅ completes |

So it needs `balanced` **and** enough samples-per-device (128/8 = 16 vs 16/8 = 2) **and** long sequences (large per-sample tensors) together.

## Minimal reproducer
```python
import os, sys, torch
from gptqmodel import GPTQModel, QuantizeConfig
# python repro.py balanced  -> crashes ;  python repro.py cpu -> completes
MODEL = os.environ.get("MODEL", "/path/to/a/long-context/model")
CALIB_DEVICE = sys.argv[1] if len(sys.argv) > 1 else "balanced"
SAMPLES = int(os.environ.get("SAMPLES", "128"))   # 128 crashes; 16 completes
SEQLEN  = int(os.environ.get("SEQLEN", "65536"))  # 64k crashes; 32k completes
g = torch.Generator().manual_seed(0)
calib = [{"input_ids": torch.randint(0, 1000, (SEQLEN,), generator=g).tolist(),
          "attention_mask": [1]*SEQLEN} for _ in range(SAMPLES)]
qc = QuantizeConfig(bits=4, group_size=128, calibration_data_device=CALIB_DEVICE)
model = GPTQModel.load(MODEL, qc, device_map="auto")
model.quantize(calib, batch_size=1)
print(f"OK: calibration_data_device={CALIB_DEVICE} samples={SAMPLES} seqlen={SEQLEN}")
```
`MODEL` = any model that supports a 64k context. We hit it on Qwen3.6-27B (hybrid linear + full attention) on 8×A800; the failing path is GPTQModel's balanced cache handling, so it should be model-agnostic at this scale. (We first reproduced it with real tokenized calibration data via our own harness; the random-input script above reproduces the same conditions.)

## What we ruled out (to save you time)
- **Not a compute kernel int32 overflow**: the model's fla GDN ops (`chunk_gated_delta_rule`, `FusedRMSNormGated`), torch SDPA (head_dim 256), and torch conv all run standalone at 64k/128k with no error.
- **Not `compute_hessian_xtx`**: the isolated Hessian matmul at these shapes (up to ~1.3B elements) is fine.
- **Not OOM / not a leak**: 60GB+ free per GPU at crash; host RAM spikes then releases (non-monotonic).
- **Not an intra-device worker race**: forcing `cuda:per=1` still crashes (crash point just shifts).
- **Not an input/mask device mismatch**: `forward_batch_worker` correctly `move_to`s input, attention_mask, position_ids and kwargs to the replica device.

Remaining suspect is the balanced cross-device cache placement/consumption in `gptqmodel/looper/forward_executor.py` (the `is_balanced_mode` batch→device assignment and result-device routing) scaling with samples-per-device. We could not localize the exact line: **`compute-sanitizer memcheck` deadlocks** with the multi-device thread pool (GPU stuck at 0% util, no progress), and `CUDA_LAUNCH_BLOCKING=1` deadlocks the same way.

## Workaround
`calibration_data_device="cpu"` completes and produces a valid quant (slower, per-batch H2D).

## Environment
- GPTQModel 7.3.1
- torch 2.13.0+cu130, triton 3.7.1, transformers 5.14.1
- 8× A800 80GB, driver 580 / CUDA 13
- model: Qwen3.6-27B (hybrid linear + full attention)

Happy to run any targeted instrumentation you suggest (a sync/log point in the balanced forward loop) to pinpoint the exact op, since sanitizer won't attach cleanly.


## 评论 (4)

### Qubitium · 2026-07-23

@thomaslwang Very strange and thanks for tge detailed error dissection. Will take a look.

### Qubitium · 2026-07-23

@thomaslwang  What python version are you using?



### Qubitium · 2026-07-23

@thomaslwang  I am currently trying to reproduce this bug on 4xA100. Another point, can check your nvidia-smi log for any A800 ecc errors or other such error logs? Need to rule out gpu errors at this point. 

### Qubitium · 2026-07-23

@thomaslwang  Please pull and build from `main` and test the fix: https://github.com/ModelCloud/GPTQModel/pull/2969

The bug is `timing` related so I am still unable to reproduce as timing is different for every system but test the fix and let me know if it resolves your issue.

```
git clone ..
cd gptqmodel
pip install -v -e .
```
