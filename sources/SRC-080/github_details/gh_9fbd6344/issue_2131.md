# [Issue #2131] fold_weight crashes with AttributeError: 'NoneType' object has no attribute 'data' on Megatron models with tied word embeddings

source: https://github.com/NVIDIA/Model-Optimizer/issues/2131
state: closed | updated: 2026-08-28T08:10:10Z
labels: bug

## 正文

## Describe the bug

On Megatron-Core models with tied word embeddings
(`share_embeddings_and_output_weights=True`), the `output_layer` stores
`weight = None` and borrows the embedding weight at forward time
(`skip_weight_param_allocation=True`). ModelOpt still attaches an
`output_layer.weight_quantizer` to it, so `mtq.fold_weight` matches the pair and
dereferences the `None` weight:

```
modelopt/torch/quantization/nn/modules/quant_module.py, in fold_weight
    weight.data.copy_(attr(weight.float()).to(weight.dtype))
AttributeError: 'NoneType' object has no attribute 'data'
```

`QuantModule.fold_weight` selects pairs on the `*_weight_quantizer` name and
`fake_quant` alone, and `_fold_weight_quantizer` accesses `weight.data` with no
`None` guard (still the case on current `main`):

https://github.com/NVIDIA/TensorRT-Model-Optimizer/blob/6b02f528bbc46b5ed474fade47add23f6810f0f3/modelopt/torch/quantization/nn/modules/quant_module.py#L144-L145

Normal QAT forwards never hit this because the Megatron plugin quantizes the weight
*argument* passed to the linear functional, not the stored `module.weight`;
`fold_weight` is the first path that reads the stored attribute, which is genuinely
`None` on the tied layer. (HF models tie via a shared tensor instead of `None`, so
only Megatron is affected.) There is no workaround from outside: `mtq.fold_weight`
walks every `QuantModule`, and per-module `fold_weight()` can't skip one pair.

## Steps/Code to reproduce bug

```python
import modelopt.torch.quantization as mtq
from megatron.core.models.gpt import GPTModel

# Any GPTModel with tied embeddings, e.g. Qwen3-0.6B:
# output_layer.weight is None (borrowed from the embedding at forward time).
model = GPTModel(..., share_embeddings_and_output_weights=True)
model = mtq.quantize(model, mtq.NVFP4_DEFAULT_CFG, forward_loop)

mtq.fold_weight(model)  # AttributeError: 'NoneType' object has no attribute 'data'
```

Hit in practice in NeMo-RL quantization-aware GRPO (Megatron backend, Qwen3-0.6B);
https://github.com/NVIDIA-NeMo/RL/pull/3441 currently reimplements the per-pair fold
with a `None` guard as a workaround.

## Expected behavior

`fold_weight` skips pairs whose weight is not a tensor:

```python
weight = getattr(self, weight_name)
if not isinstance(weight, torch.Tensor):
    continue  # e.g. Megatron tied-embedding output_layer: weight = None
self._fold_weight_quantizer(attr, (weight,), keep_attrs)
```

Skipping is correct: the tied `output_layer` has no stored weight, and the tensor it
borrows belongs to the embedding module, whose own pair is folded on that module.

## System information

- ModelOpt: 0.46.0.dev86 (also present on `main` @ 6b02f52)
- Model: Megatron-Core `GPTModel` with `share_embeddings_and_output_weights=True` (Qwen3-0.6B)
- Quant config: NVFP4 defaults; crash is independent of format

## 评论 (1)

### kevalmorabia97 · 2026-08-28

Fixed in #2140 
