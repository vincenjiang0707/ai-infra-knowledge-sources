# [Issue #1633] [Bug] NVFP4 W4A4 export: per-block weight_scale contains NaN bytes from unclamped FP32 → FP8 E4M3 cast

source: https://github.com/NVIDIA/Model-Optimizer/issues/1633
state: open | updated: 2026-06-05T18:29:47Z
labels: bug, torch.quantization, triaged, auto-fixable

## 正文

**Before submitting an issue, please make sure it hasn't been already addressed by searching through the [existing and past issues](https://github.com/NVIDIA/Model-Optimizer/issues?q=is%3Aissue).**

Searched issues for `NaN weight_scale`, `NaN FP4`, `FP8 cast NaN`, `float8_e4m3fn cast` — no prior reports.

## Describe the bug

**Context:** Discovered while quantizing **Qwen/Qwen3-Omni-30B-A3B-Instruct** to NVFP4 W4A4 with **`nvidia-modelopt==0.44.0`** on an **NVIDIA RTX PRO 6000 Blackwell Workstation Edition** (sm_120, 96 GiB) calibration box, for downstream FP4 inference. Calibration scope started narrow (MoE experts only) and was widened layer-by-layer; the behavior below first appeared the moment `o_proj` joined the FP4 surface.

ModelOpt's NVFP4 quantizer computes a per-block `weight_scale` in FP32 (as `amax / (NVFP4_max * fp8_max)` after the global-scale division), then casts to `torch.float8_e4m3fn` before serializing to disk. PyTorch's `to(torch.float8_e4m3fn)` saturates correctly for inputs at and near the FP8 E4M3 max of 448, but for inputs sufficiently far above max it emits NaN bytes (E4M3 encoding `0x7F` / `0xFF`) rather than the max byte. As a result, NVFP4 W4A4 checkpoints exported with stock ModelOpt 0.44 can contain literal NaN bytes in per-block `weight_scale`. Downstream inference engines reading the safetensors then see `weight_scale[i] = NaN`, the NaN propagates through the FP4 GEMM, and the served model output collapses to garbage.

This is an inconsistency between two parallel code paths in `nvfp4_tensor.py`. One path clamps before the FP8 cast; the other does not:

- `modelopt/torch/quantization/qtensor/nvfp4_tensor.py:131-134` (0.44.0) — clamps:
  ```python
  per_block_scale = (
      (per_block_scale * 448.0 / per_block_scale_max)
      .clamp_(max=448.0)
      .to(torch.float8_e4m3fn)
  )
  ```
- `modelopt/torch/quantization/qtensor/nvfp4_tensor.py:173-176` (0.44.0) — does not clamp:
  ```python
  per_block_scale[per_block_scale == 0] = 1.0
  if not keep_high_precision:
      per_block_scale = per_block_scale.to(torch.float8_e4m3fn)
  ```

The line-133 site establishes the intended pattern: finite FP8 bytes only. The line-176 site, when reached with per-block scales above 448, emits the FP8 E4M3 NaN encoding instead.

**Impact:** affects NVFP4 W4A4 checkpoint exports that reach the line-176 path with per-block scales above 448. The case we hit:
- Qwen3-Omni-30B-A3B-Instruct NVFP4 W4A4 full-thinker export (a handful of NaN bytes across `o_proj` layers, more once experts/MoE projections join the FP4 surface).
- Confirmed calibration-side rather than inference-side by byte-editing the on-disk NaN bytes to the FP8 max byte (`0x7E`) and observing coherent downstream inference output.

**Question for the maintainers:** is the line-176 omission of the clamp intentional (e.g., the `keep_high_precision=False` path is expected to be reached only with inputs already capped at 448 upstream), or is it a bug? If intentional, what's the upstream invariant we're missing in the Qwen3-Omni W4A4 calibration that's letting >448 values reach this code path? If a bug, the one-line fix shown in *Expected behavior* below matches the line-133 sibling.

### Steps/Code to reproduce bug

**Minimal repro of the underlying PyTorch behavior ModelOpt is exposed to** (no ModelOpt install required, no GPU required — pure CPU torch):

```python
import torch

print(f"FP8 E4M3 max: {torch.finfo(torch.float8_e4m3fn).max}")
print("FP32 -> FP8 E4M3 cast bytes for various inputs:")
for v in [100.0, 448.0, 449.0, 500.0, 1000.0, 5000.0]:
    s = torch.tensor([v], dtype=torch.float32).to(torch.float8_e4m3fn)
    b = s.view(torch.uint8).item()
    nan = torch.isnan(s).item()
    print(f"  fp32={v:>8.1f}  ->  byte=0x{b:02X}  isnan={nan}")
```

Output (PyTorch 2.12.0):

```
FP8 E4M3 max: 448.0
FP32 -> FP8 E4M3 cast bytes for various inputs:
  fp32=   100.0  ->  byte=0x6C  isnan=False
  fp32=   448.0  ->  byte=0x7E  isnan=False
  fp32=   449.0  ->  byte=0x7E  isnan=False
  fp32=   500.0  ->  byte=0x7F  isnan=True    <-- NaN emitted
  fp32=  1000.0  ->  byte=0x7F  isnan=True
  fp32=  5000.0  ->  byte=0x7F  isnan=True
```

PyTorch saturates correctly for values near max (`449 -> 448`), but for any input significantly above max it emits the FP8 E4M3 NaN encoding (`0x7F`) instead of clamping. This is the byte that lands on disk in a `weight_scale` safetensor.

**Reproducing in ModelOpt 0.44.0 source:**

The site we traced the NaN bytes to is `modelopt/torch/quantization/qtensor/nvfp4_tensor.py:176`, quoted above. Adding `.clamp_(max=448.0)` immediately before that cast — matching the sibling site at line 133 — produced clean exports (0 NaN bytes verified by byte-scan) and recovered coherent inference output downstream.

There are additional `.to(torch.float8_e4m3fn)` calls in `modelopt/torch/export/quant_utils.py` (lines ~859, 860, 878, 894, 897, 903 in 0.44.0) that operate on `weight / weights_scaling_factor`. Those cast the *dequantized weight tensor* rather than `weight_scale`, so they're a different code path with a different value distribution — we did not observe them producing NaN bytes in our W4A4 export. Noting them in case the same unclamped-cast pattern warrants a broader audit.

**End-to-end repro** (heavier — full Qwen3-Omni 30B-A3B-Instruct NVFP4 W4A4 calibration):

- Run a per-tensor NVFP4 W4A4 calibration covering `o_proj` (or a wider thinker scope) on Qwen3-Omni 30B-A3B-Instruct with vanilla `nvidia-modelopt==0.44.0`. Calibration data: ~128 short prompts is enough.
- Inspect the resulting `*.weight_scale` tensors:
  ```python
  import safetensors.torch
  from glob import glob
  for f in glob("path/to/export/*.safetensors"):
      st = safetensors.torch.load_file(f)
      for k, v in st.items():
          if k.endswith(".weight_scale") and v.dtype == torch.float8_e4m3fn:
              n = int(torch.isnan(v).sum().item())
              if n:
                  print(f"{f}::{k}: {n} NaN bytes (shape={v.shape})")
  ```
- For our `o_proj`-inclusive export (Qwen3-Omni, mse calibration), this prints 4 NaN bytes spread across `o_proj` layers 4 and 9 of the thinker. Once experts are added to the FP4 surface, the count grows.

Two public reproducer checkpoints on Hugging Face Hub, kept for this purpose (the `-preview` suffix denotes a known-bad export):

- [YihongJin/Qwen3-Omni-30B-A3B-Instruct-NVFP4-W4A4-experts-oproj-mse-preview](https://huggingface.co/YihongJin/Qwen3-Omni-30B-A3B-Instruct-NVFP4-W4A4-experts-oproj-mse-preview) — narrow scope (MoE experts + `o_proj`), 4 NaN bytes spread across `o_proj` layers 4 and 9. Smallest minimal repro.
- [YihongJin/Qwen3-Omni-30B-A3B-Instruct-NVFP4-W4A4-full-thinker-mse-preview](https://huggingface.co/YihongJin/Qwen3-Omni-30B-A3B-Instruct-NVFP4-W4A4-full-thinker-mse-preview) — full thinker scope, more NaN bytes; this is the one we ran end-to-end accuracy validation against in vllm-omni#4025.

### Expected behavior

The line-176 cast should match the line-133 contract: every byte written to disk for a `weight_scale` tensor is a finite FP8 E4M3 value (`0x00`–`0x7E` or `0x80`–`0xFE`), never the NaN encoding (`0x7F` / `0xFF`). The minimal fix is a one-line change at line 176 to clamp before the cast, matching the existing pattern at line 133:

```python
per_block_scale[per_block_scale == 0] = 1.0
if not keep_high_precision:
    per_block_scale = per_block_scale.clamp_(max=448.0).to(torch.float8_e4m3fn)  # add .clamp_
```

If a per-block scale ever needs to be larger than 448 (extreme outliers the global-scale division didn't normalize), that should be surfaced as a calibration warning, not silently emitted as a NaN byte that propagates through downstream FP4 GEMMs.

### Who can help?

Leaving blank — happy to defer to whoever owns `modelopt/torch/quantization/qtensor/nvfp4_tensor.py` and `modelopt/torch/export/quant_utils.py`. Glad to provide more reproducer artifacts (full Qwen3-Omni calibration logs, additional preview checkpoints, byte-level safetensor inspections) on request.

## System information

- Container used (if applicable): `vllm/vllm-openai:v0.21.0`
- OS: Ubuntu 22.04 (in container)
- CPU architecture: x86_64
- GPU name (e.g. H100, A100, L40S): bug is GPU-independent — it's a pure-PyTorch FP32 → FP8 cast in calibration export code. Reproduces deterministically on CPU. Original calibration that surfaced it was on NVIDIA RTX PRO 6000 Blackwell Workstation Edition (sm_120).
- GPU memory size: 96 GiB (not load-bearing for the bug)
- Number of GPUs: 1 (also not load-bearing)
- Library versions:
  - Python: 3.12
  - **ModelOpt version: 0.44.0** (the relevant pin)
  - CUDA: 12.4 (not load-bearing)
  - PyTorch: 2.5+ (any version with `torch.float8_e4m3fn`)
  - Transformers: 4.51.x
  - TensorRT-LLM: n/a (not used in our path)
  - ONNXRuntime: n/a
  - TensorRT: n/a
- Any other details that may help: end-to-end investigation timeline, accuracy validation, and a downstream-side mitigation are captured at vllm-project/vllm-omni#4025; happy to share the patched-ModelOpt diff and the calibration logs that produced the clean exports.


## 评论 (1)

### ChenhanYu · 2026-06-05

## Triage Analysis

| Field | Value |
|-------|-------|
| Classification | Bug |
| Severity | High |
| Complexity | Simple |
| Auto-fixable | Yes |

### Summary
The NVFP4 W4A4 export has an inconsistency where the static quantizer path in `get_weights_scaling_factor_from_quantizer` did not clamp per-block scales before casting to FP8 E4M3, causing NaN bytes when scales exceed 448. This has been fixed by introducing the `_cast_per_block_scale_to_fp8` helper function, but the issue documents the original problem and confirms the fix pattern.

### Root Cause / Approach
In the original ModelOpt 0.44.0 code, the static quantizer path (`get_weights_scaling_factor_from_quantizer`) performed the FP8 cast without clamping: `per_block_scale.to(torch.float8_e4m3fn)`. When per-block scale values exceeded 448 (e.g., due to zero-amax blocks being set to 1.0 then rescaled by a small `per_block_scale_max`), PyTorch's `to(torch.float8_e4m3fn)` produces NaN bytes (0x7F/0xFF) instead of saturating to max. The dynamic path already had the clamp. The fix (visible in the current code) extracts a `_cast_per_block_scale_to_fp8` helper that clamps to [2^-9, 448] before casting, and both paths now use it.

### Suggested Fix
The fix is already present in the current codebase: the `_cast_per_block_scale_to_fp8` helper function clamps values to `[2**-9, 448.0]` before casting to `torch.float8_e4m3fn`, and both the static path (with `per_block_scale_max` rescaling) and dynamic path use this helper. The issue can be closed as fixed. If running version 0.44.0, users should upgrade to the version containing this fix.

### Relevant Files
- `modelopt/torch/quantization/qtensor/nvfp4_tensor.py`
- `tests/unit/torch/quantization/test_nvfp4_tensor.py`
- `modelopt/torch/kernels/quantization/gemm/nvfp4_quant.py`
- `modelopt/torch/kernels/quantization/gemm/fp4_kernel.py`

---
_Auto-triaged by pensieve `/magic-triage`_
