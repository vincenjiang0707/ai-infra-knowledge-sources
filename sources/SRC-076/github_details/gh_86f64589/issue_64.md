# [Issue #64] Bug: `triton_ui.py` broken after ModelConfig change in #56

source: https://github.com/meta-pytorch/KernelAgent/issues/64
state: closed | updated: 2025-12-18T00:16:14Z
labels: bug

## 正文

### 🐛 Describe the bug

PR #56 changed `ModelConfig.provider_class` to `ModelConfig.provider_classes` (list), but `scripts/triton_ui.py` wasn't updated.

## Error

```
AttributeError: 'ModelConfig' object has no attribute 'provider_class'
```

## Location

`scripts/triton_ui.py` line 75

## Fix

```python
# Before:
self._model_to_provider = {
    cfg.name: cfg.provider_class for cfg in get_available_models()
}

# After:
self._model_to_provider = {
    cfg.name: cfg.provider_classes[0] for cfg in get_available_models()
}
```

### Platform and Version

main branch 

## 评论 (1)

### Jack-Khuu · 2025-12-16

Nice catch, I'll push something out; it'll need some other changes too since just [0] isn't enough
