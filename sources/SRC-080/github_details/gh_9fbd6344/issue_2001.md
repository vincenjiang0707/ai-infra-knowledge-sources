# [Issue #2001] Public preset `quant_cfg` changed from dict to list in 0.44 (breaking, undocumented?)

source: https://github.com/NVIDIA/Model-Optimizer/issues/2001
state: open | updated: 2026-08-02T22:08:50Z
labels: 

## 正文

## Summary

Between `nvidia-modelopt` 0.43 and 0.44, the `quant_cfg` field in the public quantization preset configs (e.g. `FP8_DEFAULT_CFG`, `INT8_DEFAULT_CFG`, `NVFP4_DEFAULT_CFG`) changed from a `dict` to a `list`. The internal `modelopt.torch.quantization.config._default_disabled_quantizer_cfg` changed the same way.

Downstream code that composes a `quant_cfg` by dict-merging these presets/fragments (a natural pattern) now breaks with `TypeError: 'list' object is not a mapping`. I couldn't find this called out in the changelog / migration notes — is it intentional, and is there a recommended migration path?

## Environment

- `nvidia-modelopt`: 0.45.0 (also reproduces on 0.44.0; works on 0.43.0)
- `torch`: 2.14.0.dev20260704+cu130 (the objects involved are plain Python, so this is torch-independent)
- python: 3.12

## Minimal reproducer (modelopt only)

```python
import modelopt.torch.quantization as mtq

# `quant_cfg` in the public preset configs is a dict on <=0.43 and a list on >=0.44:
print(type(mtq.FP8_DEFAULT_CFG["quant_cfg"]))             # 0.43: <class 'dict'> | 0.44+: <class 'list'>
print(type(mtq.config._default_disabled_quantizer_cfg))   # 0.43: <class 'dict'> | 0.44+: <class 'list'>

# Code that composes a quant_cfg by dict-merging these now raises:
base = {"*weight_quantizer": {"fake_quant": False}}
merged = {**base, **mtq.config._default_disabled_quantizer_cfg}
# TypeError: 'list' object is not a mapping
```

## Note

`mtq.quantize(model, quant_cfg=<dict>, ...)` still accepts the old dict-style `quant_cfg` on 0.45, so the documented quantize path itself is intact — the break is specifically for code that reads/merges the preset `quant_cfg` objects (or the `_default_disabled_quantizer_cfg` fragment) as mappings.

## Questions

1. Is the `dict` → `list` change to preset `quant_cfg` intentional and stable going forward?
2. Is there a supported/public way to obtain the "default disabled quantizers" fragment (i.e. a replacement for `config._default_disabled_quantizer_cfg`)?
3. Any migration guidance for merging user overrides into a preset `quant_cfg` under the new list format?

Context: this surfaced in 🤗 [diffusers](https://github.com/huggingface/diffusers), whose ModelOpt integration composes `quant_cfg` from these fragments.


## 评论 (7)

### jenchen13 · 2026-07-21

Hi @sayakpaul , the change of `quant_cfg` from from dict to list was in the 0.44 CHANGELOT.rst
```
Backward Breaking Changes

The quant_cfg field in quantization configs is now an ordered list of QuantizerCfgEntry dicts instead of a flat dictionary. 
...
```
We also have documentation on the new list-based `quant_cfg` in [the docs](https://nvidia.github.io/Model-Optimizer/guides/_quant_cfg.html). The change was motivated to improve granularity and ordering in quant configs -- for example now the last config entry wins: "If two entries both match *weight_quantizer and both carry a cfg, the second entry does not inherit the first entry’s settings — it replaces them entirely." 

### shengliangxu · 2026-07-21

Thanks @sayakpaul for reporting. Thanks @jenchen13 for following up.

The change was more than an improvement, it was to fix the semantic. The old dict format is ambiguous when multiple config wildcard items config the same parameter because dict keys are unordered. The list defines a clear ordering and make the semantic deterministic.

However we still accept dict configs for backward compatibility as much as possible by normalizing to list. But old style dict manipulation code will break because of the change of type.

### sayakpaul · 2026-07-22

Would it be possible to open a PR to Diffusers to fix this?

### shengliangxu · 2026-07-23

Thanks @sayakpaul , absolutely, I'll submit a PR to fix it soon.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: f8f01121d056bb252d7ea9fae13de5f778f4259c9a7714c6919e3160b84eb65e

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 50577401eef36c5af61dda029f69a821312a24c2912316f9dc5596a398115b44

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 4642a6dbc968c3329a33f75907f59ae879a3faa220dc830429a3a927c67ad94c

Release follow-up: this open ModelOpt issue needs release relevance confirmed. Link its planned fix/validation, or confirm it is not a v0.46.0 blocker.
