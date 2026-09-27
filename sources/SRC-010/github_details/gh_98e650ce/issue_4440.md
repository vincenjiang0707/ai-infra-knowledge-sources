# [Issue #4440] [Bug] MXFP4 Bug

source: https://github.com/InternLM/lmdeploy/issues/4440
state: open | updated: 2026-03-21T05:49:40Z
labels: 

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

## MXFP4 model loading fails: `export_weight` assertion doesn't include `e2m1` weight type

### Environment

- lmdeploy 0.12.2+cu128 (Windows, Python 3.12)
- Model quantized with llmcompressor 0.10.0.1 using `QuantizationModifier(scheme="MXFP4A16")`

### Description

TurboMind cannot load MXFP4 models produced by llmcompressor. The converter sets `weight_type='e2m1'` globally for MXFP4 models, but `export_weight()` doesn't include `'e2m1'` in its allowed types, causing an assertion failure when processing non-quantized layers (e.g. RMSNorm weights).

### Steps to reproduce

1. Quantize any model with llmcompressor MXFP4A16:
```python
from llmcompressor import oneshot
from llmcompressor.modifiers.quantization import QuantizationModifier

recipe = [QuantizationModifier(targets=["Linear"], scheme="MXFP4A16", ignore=["lm_head"])]
oneshot(model=model, dataset=ds, recipe=recipe, ...)
model.save_pretrained(output_dir)
```

2. Patch `config.json` so lmdeploy routes to its mxfp4 path (llmcompressor saves `quant_method: "compressed-tensors"`, but lmdeploy requires `quant_method: "mxfp4"`).

3. Load with TurboMind:
```python
from lmdeploy import pipeline, TurbomindEngineConfig
pipe = pipeline(output_dir, backend_config=TurbomindEngineConfig(model_format="mxfp4"))
```

### Error

```
File "lmdeploy/turbomind/deploy/target_model/base.py", line 146, in export_weight
    assert weight_type in ['float16', 'bfloat16', 'int4', 'fp8']
AssertionError
```

Stack trace shows it fails on `layers.{i}.attention_norm.weight` — a norm layer that should remain in float, not e2m1.

### Root cause

In `converter.py` lines 86–88, `model_format == 'mxfp4'` sets `weight_type = 'e2m1'` **globally** for all layers. This flows into `export_weight()` (`base.py:146`) which only allows `['float16', 'bfloat16', 'int4', 'fp8']`. The `'e2m1'` type is missing from this list.

Additionally, there's no logic to differentiate between quantized Linear weights (which should be e2m1) and non-quantized norm/embedding weights (which should remain float). Compare with the `GptOssForCausalLM` special case at `converter.py:91–93` which resets `weight_type = dtype` — suggesting this differentiation is needed but not generalized.

### Secondary issue

There is also a routing problem: llmcompressor saves MXFP4 models with `quant_method: "compressed-tensors"` and `format: "mxfp4-pack-quantized"` in the quantization config. lmdeploy's compressed-tensors path (`converter.py:149`) only accepts `format == 'pack-quantized'`, rejecting `mxfp4-pack-quantized`. This means the model can't load through *either* path without manually patching `config.json`.

### Reproduction

I ran a benchmarking script after successfully converting a model using llmcompressor.

### Environment

```Shell
Windows 10, RTX 4090, Python 3.12, torch 2.9.0, lmdeploy 0.12.2, compressed-tensors 0.14.0.1, llmcompressor 0.10.0.1, cuda 12.8.1, transformers 4.57.6, triton-windows 3.5.0.post21
```

### Error traceback

```Shell

```

## 评论 (1)

### lvhan028 · 2026-03-21

Support for models released by LLMCompressor is included in our roadmap. LMDeploy introduced support for LLMCompressor-int4 quantized models earlier this year, and we plan to extend this support to the remaining models in the future.
