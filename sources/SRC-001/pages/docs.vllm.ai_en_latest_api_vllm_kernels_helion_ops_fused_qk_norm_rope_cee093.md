source: https://docs.vllm.ai/en/latest/api/vllm/kernels/helion/ops/fused_qk_norm_rope/
lastmod: 2026-09-24

Pick the best pre-tuned config for the given input shape.

## Selection strategy

- Find the closest q_heads among available configs (exact match preferred).
- Find the closest kv_heads among available configs (exact match preferred).
- Among the num_tokens values tuned for that q_heads and q_heads, pick the smallest num_tokens >= the input's num_tokens. If the input is larger than all available num_tokens, fall back to the largest.

## Source code in `vllm/kernels/helion/ops/fused_qk_norm_rope.py`


| def pick_config(args: tuple[Any, ...], config_keys: list[CaseKey]) -> CaseKey | None:
"""Pick the best pre-tuned config for the given input shape.
Selection strategy:
1. Find the closest q_heads among available configs
(exact match preferred).
2. Find the closest kv_heads among available configs
(exact match preferred).
3. Among the num_tokens values tuned for that q_heads and q_heads, pick
the smallest num_tokens >= the input's num_tokens. If the input is
larger than all available num_tokens, fall back to the largest.
"""
if not config_keys:
return None
qkv, q_heads, kv_heads, *_ = args
num_tokens = qkv.shape[0]
cache_key = (num_tokens, q_heads, kv_heads)
cached = _pick_cache.get(cache_key)
if cached is not None:
return cached
configs: dict[int, dict[int, list[int]]] = {}
for key in config_keys:
if key.is_default():
continue
configs.setdefault(key["q_heads"], {}).setdefault(key["kv_heads"], []).append(
key["num_tokens"]
)
if not configs:
return None
best_q_heads = min(configs, key=lambda s: abs(s - q_heads))
best_kv_heads = min(configs[best_q_heads], key=lambda s: abs(s - kv_heads))
available_num_tokens = sorted(configs[best_q_heads][best_kv_heads])
best_num_tokens = next(
(n for n in available_num_tokens if n >= num_tokens), available_num_tokens[-1]
)
result = CaseKey(
{
"q_heads": best_q_heads,
"kv_heads": best_kv_heads,
"num_tokens": best_num_tokens,
}
)
_pick_cache[cache_key] = result
return result
|