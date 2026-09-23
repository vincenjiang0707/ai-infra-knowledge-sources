source: https://docs.vllm.ai/en/latest/api/vllm/kernels/helion/ops/dynamic_per_token_scaled_fp8_quant/
lastmod: 2026-09-23

Pick the best pre-tuned config for the given input shape.

## Selection strategy

- Find the closest hidden_size among available configs (exact match preferred).
- Among the num_tokens values tuned for that hidden_size, pick the smallest num_tokens >= the input's num_tokens. If the input is larger than all available num_tokens, fall back to the largest.

## Source code in `vllm/kernels/helion/ops/dynamic_per_token_scaled_fp8_quant.py`


| def pick_config(args: tuple[Any, ...], config_keys: list[CaseKey]) -> CaseKey | None:
"""Pick the best pre-tuned config for the given input shape.
Selection strategy:
1. Find the closest hidden_size among available configs
(exact match preferred).
2. Among the num_tokens values tuned for that hidden_size, pick
the smallest num_tokens >= the input's num_tokens. If the input is
larger than all available num_tokens, fall back to the largest.
"""
if not config_keys:
return None
_, input, *_ = args
num_tokens, hidden_size = input.shape
cache_key = (num_tokens, hidden_size)
cached = _pick_cache.get(cache_key)
if cached is not None:
return cached
configs: dict[int, list[int]] = {}
for key in config_keys:
if key.is_default():
continue
configs.setdefault(key["hidden_size"], []).append(key["num_tokens"])
if not configs:
return None
best_hidden_size = min(configs, key=lambda s: abs(s - hidden_size))
available_num_tokens = sorted(configs[best_hidden_size])
best_num_tokens = next(
(n for n in available_num_tokens if n >= num_tokens), available_num_tokens[-1]
)
result = CaseKey({"hidden_size": best_hidden_size, "num_tokens": best_num_tokens})
_pick_cache[cache_key] = result
return result
|