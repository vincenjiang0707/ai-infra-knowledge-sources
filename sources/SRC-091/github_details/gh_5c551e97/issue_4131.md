# [Issue #4131] [Bug] enable_blending with LMCacheConnectorV1 crashes at startup: VLLMModelTracker.register_model is never called

source: https://github.com/LMCache/LMCache/issues/4131
state: open | updated: 2026-09-19T01:44:44Z
labels: stale

## 正文

## Summary

Enabling CacheBlend (`enable_blending: true`) with the vLLM V1 connector (`LMCacheConnectorV1`) crashes the engine at startup:

```
ValueError: vllm model for vllm-instance not found.
```

Root cause: `LMCBlenderBuilder.get_or_create()` calls `VLLMModelTracker.get_model(ENGINE_NAME)`, but **nothing in the current tree ever calls `VLLMModelTracker.register_model()`** — grepping the repo shows the only references are in `lmcache/v1/compute/models/utils.py` (definition) and `lmcache/v1/compute/blend/utils.py` (the `get_model` call). The registration call appears to be a leftover from the old `lmcache_vllm` fork era.

## Environment

- LMCache: main @ `668a1fd`, built from source
- vLLM: 0.19.1 (official `vllm/vllm-openai:latest-cu130-ubuntu2404` image, aarch64 / GB10)
- Model: Llama-3.1-8B-Instruct, `--enforce-eager --no-enable-prefix-caching`

## Reproduction

```yaml
# lmcache config
chunk_size: 256
local_cpu: true
max_local_cpu_size: 32
enable_blending: true
use_layerwise: true
blend_special_str: " # #"
blend_check_layers: [1]
blend_recompute_ratios: [0.15]
```

```
vllm serve meta-llama/Llama-3.1-8B-Instruct \
  --kv-transfer-config '{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_both"}' ...
```

EngineCore dies during `_initialize_kv_caches` → `LMCacheConnectorV1Impl.__init__` → `LMCBlenderBuilder.get_or_create` → `VLLMModelTracker.get_model` raises.

## Workaround that made blending work for us

A tiny vLLM general plugin that wraps `GPUModelRunner.load_model` and registers the model right after load:

```python
# entry point group "vllm.general_plugins"
def register():
    import importlib
    for mod in ("vllm.v1.worker.gpu_model_runner", "vllm.v1.worker.gpu.model_runner"):
        try:
            cls = importlib.import_module(mod).GPUModelRunner
        except Exception:
            continue
        orig = cls.load_model
        def load_model(self, *a, _orig=orig, **kw):
            out = _orig(self, *a, **kw)
            from lmcache.v1.compute.models.utils import VLLMModelTracker
            VLLMModelTracker.register_model("vllm-instance", self.model)
            return out
        cls.load_model = load_model
```

(Note vLLM 0.19 has two runner modules — the default flat `gpu_model_runner.py` and the V2 `gpu/model_runner.py` — so both need the hook.)

## Additional friction points hit on the same path (worth doc fixes at least)

1. `blend_check_layers` / `blend_recompute_ratios` default to `None`; with blending enabled, `process_qkv` crashes with `TypeError: argument of type 'NoneType' is not iterable`. Either give working defaults or validate at config load.
2. The default `blend_special_str: " # # "` (trailing space) never matches in-stream tokens for Llama-3 BPE: `encode(" # # ")[1:]` = `[' #', ' #', ' ']`, but in a real prompt the trailing space merges into the next word (`' all'` etc.), so `SegmentTokenDatabase._fast_split_by_subtensor` finds **zero separators** and every lookup misses. Using `" # #"` (no trailing space, `[674, 674]`) works. Also, the *first* document of a prompt tokenizes without a leading space, so its segment hash differs from the same document appearing mid-prompt — prepending a fixed dummy segment (`"docs:" + SEP`) restores position-invariant reuse.
3. Setting `blend_special_str` via env var strips the meaningful leading/trailing whitespace — it only works via `LMCACHE_CONFIG_FILE` yaml.

Happy to turn the workaround into a PR if you can advise where the registration should live properly (connector init? runner wrapper?).


## 评论 (2)

### ApostaC · 2026-07-20

Hi @matu79go , this part of the code is deprecated. We are working on releasing the new version of cacheblend these days. Thanks for your interest!

### github-actions[bot] · 2026-09-19

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.
