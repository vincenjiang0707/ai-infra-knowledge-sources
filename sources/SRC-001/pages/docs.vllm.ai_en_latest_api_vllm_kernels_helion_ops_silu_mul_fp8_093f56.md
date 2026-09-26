source: https://docs.vllm.ai/en/latest/api/vllm/kernels/helion/ops/silu_mul_fp8/
lastmod: 2026-09-24

Pick the best pre-tuned config for the given input shape.

## Selection strategy

- Find the closest intermediate_size among available configs (exact match preferred).
- Among the num_tokens values tuned for that intermediate_size, pick the smallest num_tokens >= the input's num_tokens. If the input is larger than all available num_tokens, fall back to the largest.

## Source code in `vllm/kernels/helion/ops/silu_mul_fp8.py`


| def pick_silu_mul_fp8_config(
args: tuple[Any, ...], config_keys: list[CaseKey]
) -> CaseKey | None:
"""Pick the best pre-tuned config for the given input shape.
Selection strategy:
1. Find the closest intermediate_size among available configs
(exact match preferred).
2. Among the num_tokens values tuned for that intermediate_size, pick
the smallest num_tokens >= the input's num_tokens. If the input is
larger than all available num_tokens, fall back to the largest.
"""
if not config_keys:
return None
input_tensor, _scale = args
intermediate_size = int(input_tensor.shape[-1]) // 2
num_tokens = int(input_tensor.view(-1, input_tensor.shape[-1]).shape[0])
cache_key = (num_tokens, intermediate_size)
cached = _pick_cache.get(cache_key)
if cached is not None:
return cached
by_isize: dict[int, list[int]] = {}
for k in config_keys:
if k.is_default():
continue
by_isize.setdefault(k["intermediate"], []).append(k["numtokens"])
if not by_isize:
return None
best_isize = min(by_isize, key=lambda s: abs(s - intermediate_size))
available = sorted(by_isize[best_isize])
best_ntokens = next((n for n in available if n >= num_tokens), available[-1])
result = CaseKey({"intermediate": best_isize, "numtokens": best_ntokens})
_pick_cache[cache_key] = result
return result
|