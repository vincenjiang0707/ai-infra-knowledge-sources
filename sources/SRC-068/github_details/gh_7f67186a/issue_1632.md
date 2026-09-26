# [Issue #1632] Clarification on autotune using the triton backend for amd cards

source: https://github.com/Dao-AILab/flash-attention/issues/1632
state: open | updated: 2026-07-28T20:24:03Z
labels: 

## 正文

Under the **getting started** section for amd cards it is said that for enabling auto tune and giving better performance one can use this `FLASH_ATTENTION_TRITON_AMD_AUTOTUNE="TRUE"` flag. 
This flag got me an error and so I looked at the code and found: 
```python
def get_autotune_configs():
    if AUTOTUNE:
        if is_cdna():
            autotune_configs, autotune_keys = get_cdna_autotune_configs()
            fwd_auto_tune_configs, fwd_autotune_keys= autotune_configs, autotune_keys
            reduce_auto_tune_configs, reduce_autotune_keys = autotune_configs, autotune_keys
            return (fwd_auto_tune_configs, fwd_autotune_keys), (reduce_auto_tune_configs, reduce_autotune_keys)
        else:
            raise ValueError("Unknown Device Type")
```
Because it is listed under the triton backend section that claims it should support cdna as well as rdna cards, I am now wondering is there an issue with the code or is this feature only available for cdna cards, if so it would be nice to mention that because it could lead to confusion. 

## 评论 (2)

### feffy380 · 2025-08-17

It's a bit misleading to call it "auto tuning" only to find out it's a set of hardcoded configs for 2 or 3 CDNA cards.

### Ragua1 · 2026-07-28

The AMD Triton backend was moved into [ROCm/aiter](https://github.com/ROCm/aiter) by #2230 (`3f94643`, merged 2026-03-12). `main` no longer ships `flash_attn/flash_attn_triton_amd/` — that path is gone — and instead consumes the kernels through the `third_party/aiter` submodule. In that version `get_fwd_decode_configs()` branches on both `arch.is_rdna` and `arch.is_cdna` and no longer raises, and `RDNA_ARCHS` lists gfx1030/1100/1101/1102/1150/1151/1200/1201. So autotune on `main` really is supported on RDNA, and @feffy380's "hardcoded configs for 2 or 3 CDNA cards" no longer describes it.

The catch is the release channel. The newest PyPI version is still `2.8.3.post1` (uploaded 2026-06-11), and despite the date it is a `.post` re-packaging of the v2.8.3 tag from August 2025 — pre-migration. It still contains the old `flash_attn_triton_amd/`, so it still raises. Reproduced on `2.8.3.post1` with torch 2.10.0+rocm7.14 on gfx1101: `ValueError("Unknown Device Type")` from `fwd_decode.py:34`, because that module branched on `is_cdna()` only while `fwd_prefill.py` already handled `is_rdna()`.

**Workaround on any released version: `FLASH_ATTENTION_TRITON_AMD_AUTOTUNE=FALSE`.** 
The non-autotune fallback config works fine on RDNA — you lose the tuning, not the backend.

And a small doc suggestion, which is what this issue originally asked for: the README still says *"For peak throughput, enable `FLASH_ATTENTION_TRITON_AMD_AUTOTUNE="TRUE"` to search for optimal settings"* with no version caveat. That is true for `main` but not for anything installable from PyPI today, which is exactly the confusion reported here. A sentence saying the Triton AMD backend on `main` comes from the `third_party/aiter` submodule, and that released wheels predate it, would save the next person the same trip.
