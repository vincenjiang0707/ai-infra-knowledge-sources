# [Issue #2427] Support head_dim=512 for Gemma 4 global attention layers

source: https://github.com/Dao-AILab/flash-attention/issues/2427
state: open | updated: 2026-07-07T13:49:52Z
labels: 

## 正文

## Context

Google's **Gemma 4** (26B-A4B, released March 2026) introduces a hybrid attention design with two different head dimensions within the same model:

- **26 out of 30 layers**: sliding window attention with `head_dim=256` — works with FA2
- **4 out of 30 layers**: global attention with `head_dim=512` — **exceeds FA2's 256 limit**

This is the first widely-used open model (to my knowledge) that requires `head_dim=512` with multiple attention heads in production. Unlike the case in #801 (single head, head_dim=512), Gemma 4's global attention layers have `num_attention_heads=8` and `num_key_value_heads=4` with `head_dim=512`, so there is a real opportunity for FA2/FA3 speedup if the head_dim limit were raised.

## Request

Support `head_dim=512` in FlashAttention (FA2 and/or FA3/FA4).

### Model config details

```json
{
  "head_dim": 256,
  "global_head_dim": 512,
  "num_attention_heads": 8,
  "num_key_value_heads": 4,
  "sliding_window_pattern": 6,
  "num_hidden_layers": 30
}
```

Global attention layers at indices `[3, 9, 15, 21]`. Each has 8 query heads and 4 KV heads with `head_dim=512`.

## Current error

```
RuntimeError: FlashAttention only supports head dimensions up to 256
```

## Current workaround

Fall back to SDPA for **all 30 layers**, losing FA2 speedup even on the 26 layers that are FA2-compatible (head_dim=256).

HuggingFace Transformers could implement per-layer attention dispatch (FA2 for sliding layers, SDPA for global layers), but native FA support for head_dim=512 would be the ideal solution — it would benefit Gemma 4 and any future models adopting larger head dimensions.

## Related

- #801 — head_dim > 256 request (closed, was for single-head case)
- #2318 — FA4 Hopper now supports head_dim=256, head_dim=512 still unsupported
- HuggingFace Transformers issue: [huggingface/transformers#45201](https://github.com/huggingface/transformers/issues/45201) (per-layer attention workaround)

## Why this matters now

Gemma 4 is likely the first of several models to adopt hybrid head dimensions. As context windows grow and models mix local/global attention patterns, `head_dim > 256` for global layers may become common. Supporting 512 would future-proof FlashAttention for this architectural trend.

## 评论 (12)

### tridao · 2026-04-03

hdim fwd for 512 isn't too hard on Hopper (we kinda have it in FA3, not hard to port to FA4). 
On Blackwell might be harder, we have a PR on hdim 256, will merge that first.

### samuelazran · 2026-04-03

Thanks @tridao! Great to hear hdim 512 fwd is feasible on Hopper.

In the meantime, we're using a per-layer hybrid approach as a workaround: load the model with `attn_implementation="flash_attention_2"`, then give each of the 5 global layers (indices [5, 11, 17, 23, 29]) a shallow-copied config with `_attn_implementation="sdpa"`. This way the 25 sliding layers (hdim=256) get FA2 while the 5 global layers (hdim=512) fall back to SDPA. Clean, no forward() patching needed.

Looking forward to native hdim=512 support — happy to test when available.

### zhangtemplar · 2026-04-11

> Thanks [@tridao](https://github.com/tridao)! Great to hear hdim 512 fwd is feasible on Hopper.
> 
> In the meantime, we're using a per-layer hybrid approach as a workaround: load the model with `attn_implementation="flash_attention_2"`, then give each of the 5 global layers (indices [5, 11, 17, 23, 29]) a shallow-copied config with `_attn_implementation="sdpa"`. This way the 25 sliding layers (hdim=256) get FA2 while the 5 global layers (hdim=512) fall back to SDPA. Clean, no forward() patching needed.
> 
> Looking forward to native hdim=512 support — happy to test when available.

how did you do that, I tried similar algorithms but got error on attention mask shape didn't match:

```
[rank3]:   File "/home/%user/miniconda3/envs/rankagi_cpt/lib/python3.11/site-packages/transformers/models/gemma4/modeling_gemma4.py", line 792, in eager_attention_forward
[rank3]:     attn_weights = attn_weights + attention_mask
[rank3]:                    ~~~~~~~~~~~~~^~~~~~~~~~~~~~~~
[rank3]: RuntimeError: The size of tensor a (4096) must match the size of tensor b (8) at non-singleton dimension 2
```

### zzhhjjj · 2026-04-16

Vibe-coded a kernel optimized only for the Gemma 4 config. Contributions are welcome!
https://github.com/zzhhjjj/gemma-triton-flash-attn

### DefTruth · 2026-04-19

The Split-D idea in FFPA can extend the headdim up to 1024 and more! 
- https://github.com/xlite-dev/ffpa-attn

### kailashbuki · 2026-04-24

@tridao: Saw [this PR](https://github.com/Dao-AILab/flash-attention/pull/2467) from last week adding 512 head dimension support in FA3 — is this on your radar?

### ShuaiShao93 · 2026-06-13

any updates here?

### murthyrudra · 2026-06-29

any updates here?



### DWANG015 · 2026-06-30

any updates here?

### alex-ht · 2026-07-01

### Better Temporary Workaround for H100 (using `flex_attention`)
On H100, the default `flex_attention` also fails due to Triton SRAM OOM. The following patch forces smaller block sizes and makes it work reliably:

```python
_FLEX_KERNEL_OPTIONS = {
    "BLOCK_M": 16,
    "BLOCK_N": 16,
    "num_stages": 1,
    "num_warps": 4
}

def patch_flex_kernel_options():
    from transformers.modeling_utils import ALL_ATTENTION_FUNCTIONS
    from transformers.integrations.flex_attention import flex_attention_forward as _orig
    
    def _wrapped(module, query, key, value, attention_mask, **kwargs):
        kwargs.setdefault("kernel_options", _FLEX_KERNEL_OPTIONS)
        return _orig(module, query, key, value, attention_mask, **kwargs)
    
    ALL_ATTENTION_FUNCTIONS["flex_attention"] = _wrapped

# Apply patch before loading the model
patch_flex_kernel_options()
```

**Why it works**  
With `BLOCK_M=16` and `num_stages=1`, SRAM usage drops from ~263KB to ~80KB, well below H100’s 232KB limit.

**SRAM breakdown**:
- Q/K/V tiles: 16KB each
- Accumulator: 32KB
- **Total ≈ 80KB**

This patch only affects the `flex_attention` path and requires no source code changes.

### ggcr · 2026-07-01

Triton solution proposed by @zzhhjjj worked fine as a temporary fix while we wait for the official PR

### MiNeves00 · 2026-07-07

Any updates to the official PR support for models like Gemma4?
