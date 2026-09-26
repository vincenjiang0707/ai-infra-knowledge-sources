# [Issue #2331] [BUG] NaN error when quantizing Qwen3 model with AWQ

source: https://github.com/ModelCloud/GPTQModel/issues/2331
state: closed | updated: 2026-01-08T11:04:31Z
labels: bug

## 正文

# [BUG] NaN error when quantizing Qwen3 model with AWQ

## Software Info

**OS/Version**: Linux 5.15.0-78-generic  
**Python Version**: Python 3.12  
**GPU**: NVIDIA GeForce RTX 5090, Driver 580.76.05, 32GB VRAM

```
gptqmodel: 5.6.12
torch: 2.9.0+cu128
transformers: 4.57.3
accelerate: 1.12.0
```

## Description

AWQ quantization fails on Qwen3-8B-Base model with NaN errors. The error occurs in `_compute_best_scale` method where all 20 ratio loss calculations produce NaN values, causing `best_ratio` to remain -1 and raise an exception.

## To Reproduce

```python
from gptqmodel import GPTQModel, QuantizeConfig
from gptqmodel.quantization.config import METHOD, FORMAT
from transformers import AutoTokenizer
from datasets import load_dataset

model_path = "/path/to/Qwen3-8B-Base"

quant_config = QuantizeConfig(
    bits=4,
    group_size=128,
    quant_method=METHOD.AWQ,
    format=FORMAT.LLM_AWQ,
)

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = GPTQModel.load(model_path, quant_config, device_map="auto", trust_remote_code=True)

# Load calibration data (WikiText-2)
dataset = load_dataset("wikitext", "wikitext-2-raw-v1", split="train")
calibration_dataset = [item["text"] for item in dataset if len(item["text"].strip()) > 10][:256]

model.quantize(calibration_dataset, batch_size=1)  # Fails here
```

## Error Message

```
DEBUG [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan]
❌ AWQ Quantization Failure: 3 of 35

Traceback (most recent call last):
  File "...", line 197, in main
    model.quantize(...)
  File ".../gptqmodel/models/base.py", line 678, in quantize
    result = module_looper.loop(...)
  File ".../gptqmodel/looper/awq_processor.py", line 498, in _quantize_layer
    self._search_best_scale(layer_module_ref, **layer)
  File ".../gptqmodel/looper/awq_processor.py", line 683, in _search_best_scale
    best_scales, loss = self._compute_best_scale(...)
  File ".../gptqmodel/looper/awq_processor.py", line 941, in _compute_best_scale
    raise Exception
Exception
```

## Root Cause

Three numerical stability issues in `awq_processor.py`:

1. **Line 641**: `w_mean` can be zero when some weight channels are all zeros, causing issues in `w_mean.pow(1 - ratio)`.

2. **Line 667**: `x_mean` can be zero when some activation channels are all zeros (sparse activations), causing issues in `x_mean.pow(ratio)`.

3. **Line 904**: Scale normalization is unstable:
   ```python
   scales = scales / (scales.max() * scales.min()).sqrt()
   ```
   When `scales.min()` is close to zero (e.g., clamped to `1e-4`), `scales.max() * scales.min()` can be very small, leading to NaN.

## Suggested Fix

### Fix 1: Add minimum protection for `w_mean` (after line 641)
```python
w_mean = (w_sum / row_count).to(weight_dtype)
w_mean = w_mean.clamp(min=1e-8)
```

### Fix 2: Add minimum protection for `x_mean` (after line 667)
```python
x_mean = (x_sum / num_elements).to(inp.dtype)
x_mean = x_mean.clamp(min=1e-8)
```

### Fix 3: Improve scale normalization stability (replace line 904)
```python
scale_max = scales.max()
scale_min = scales.min()
scale_product = scale_max * scale_min
if scale_product < 1e-8 or scale_max < 1e-6:
    scale_norm = scale_max if scale_max > 1e-6 else 1.0
else:
    scale_norm = scale_product.sqrt()
scales = scales / scale_norm
```

## Expected Behavior

AWQ quantization should complete successfully for Qwen3 models.

## Model/Datasets

- **Model**: Qwen3-8B-Base (available on HuggingFace)
- **Calibration Dataset**: WikiText-2

## Additional Notes

- GPTQ quantization works fine on the same model, indicating the issue is specific to AWQ.
- Qwen3 has `q_norm` and `k_norm` layers in attention, which may cause unusual activation distributions.
- I've tested the fixes locally and quantization completes successfully. I can submit a PR if needed.

## 评论 (5)

### 13pathak · 2026-01-06

Opened a PR for this issue. Hope the author accepts it asap. https://github.com/ModelCloud/GPTQModel/pull/2332

### Qubitium · 2026-01-07

@12345txy @13pathak Thanks for reporting this bug. Proposed fix in this issue and PR #2332 may not fix the core issue and only hides it based on early testing of this model. Most likely an internal gptqmodel regresssion in awq processing and not anything specific to special activations causing `NaN`. We should have more findings later today.

### Qubitium · 2026-01-08

Fix for this bug is going be tracked in https://github.com/ModelCloud/GPTQModel/pull/2335


### Qubitium · 2026-01-08

Note that this issue is directly related to new issue I have created: https://github.com/ModelCloud/GPTQModel/issues/2336

### Qubitium · 2026-01-08

@12345txy Fixed. Please verify with `main`. 
