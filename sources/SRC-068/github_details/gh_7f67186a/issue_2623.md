# [Issue #2623] [CuTe/SM90] Block-sparse backward returns silently-wrong gradients for head_dim=64 (forward is exact)

source: https://github.com/Dao-AILab/flash-attention/issues/2623
state: closed | updated: 2026-06-05T03:00:35Z
labels: 

## 正文

### Summary

On SM90 (H200), `flash_attn.cute.flash_attn_func` with the block-sparse interface
(`full_block_*` / `mask_block_*` produced by `compute_block_sparsity`) gives a **correct
forward** but **silently wrong backward gradients** for `head_dim = 64`. There is **no
error or NaN** — `dQ`/`dK`/`dV` are finite but off by ~**150–700×** versus the same
attention pattern run without block-sparsity. Training through the block-sparse backward
therefore silently diverges (loss → NaN after a few steps, faster with more block-sparse
layers).

This looks related to #2429 (SM90 block-sparse fwd/bwd `tile_n` mismatch), but that issue is
about `128 < head_dim ≤ 192` raising a `ValueError` (`sparse_block_size[1]=96 to match tile_n`).
The `head_dim = 64` case below does **not** raise — it returns wrong gradients silently, which
is arguably more dangerous since there's no signal that anything is wrong.

### Repro (self-contained)

The block-sparse spec is a plain **causal** pattern, so it must equal `causal=True`. The
**forward matches exactly** (`max|d| = 0.0`, proving the block list is correct); only the
**backward** is wrong.

```python
import torch
from flash_attn.cute import flash_attn_func
from flash_attn.cute.compute_block_sparsity import compute_block_sparsity

dev = "cuda"
B, H, D, T = 1, 8, 64, 768          # head_dim = 64
tile_m, tile_n = 192, 128           # required tiles for head_dim=64 on SM90
torch.manual_seed(0)
base = [torch.randn(B, T, H, D, device=dev, dtype=torch.bfloat16) for _ in range(3)]

def causal(b, h, q_idx, kv_idx, seqlen, aux):   # 6-arg cute mask_mod
    return kv_idx <= q_idx

_, bs = compute_block_sparsity(tile_m, tile_n, B, H, T, T, causal, None, dev,
                               compute_full_blocks=True)

def run(block_sparse):
    q, k, v = [t.clone().requires_grad_(True) for t in base]
    if block_sparse:
        o = flash_attn_func(q, k, v, causal=False, mask_mod=causal,
                            full_block_cnt=bs.full_block_cnt, full_block_idx=bs.full_block_idx,
                            mask_block_cnt=bs.mask_block_cnt, mask_block_idx=bs.mask_block_idx,
                            block_size=(tile_m, tile_n))
    else:
        o = flash_attn_func(q, k, v, causal=True)
    o = o[0] if isinstance(o, tuple) else o
    (o.float() * torch.randn_like(o).float()).sum().backward()
    return o.detach(), q.grad, k.grad, v.grad

torch.manual_seed(1); ob, qb, kb, vb = run(True)    # block-sparse causal
torch.manual_seed(1); od, qd, kd, vd = run(False)   # dense causal reference

print("forward  max|d| :", (ob.float() - od.float()).abs().max().item())
for n, a, b in [("dQ", qb, qd), ("dK", kb, kd), ("dV", vb, vd)]:
    rel = (a.float() - b.float()).abs().max().item() / (b.float().abs().max().item() + 1e-6)
    print(f"backward {n} rel-err:", round(rel, 1))
```

Output on H200 (SM90):

```
forward  max|d| : 0.0
backward dQ rel-err: 743.6
backward dK rel-err: 493.5
backward dV rel-err: 154.4
```

### Expected

Block-sparse backward gradients should match the equivalent non-block-sparse attention
(here `causal=True`) to bf16 tolerance, just as the forward does.

### Environment

- `flash-attn-4` 4.0.0b5
- `nvidia-cutlass-dsl` 4.4.2
- torch 2.10.0+cu128, CUDA 12.8
- GPU: NVIDIA H200 (SM90, compute capability 9.0)

### Notes

Possibly the same fwd/bwd `tile_n` mismatch root cause as #2429, but at `head_dim = 64` it
manifests as **silently-wrong gradients** rather than a `ValueError`. The forward block-sparse
path is correct and gives a real prefill speedup, so this only affects training through the
block-sparse path.


## 评论 (7)

### vaderyang · 2026-06-04

Additional data + likely root cause.

**Also affects `head_dim=128`** (so it's not `head_dim=64`-specific): the same repro with `D=128`, `block_size=(128,128)` gives forward `max|d|=0.0` but backward `dQ` rel-err ≈ 684 (dK/dV similar). Block-sparse backward is wrong across head dims on SM90, not just 64.

**Likely root cause — the backward needs a transposed mask that the public API can't supply.**

`get_block_sparse_expected_shapes_bwd` / `normalize_block_sparse_config_bwd` show the backward expects a **Q-direction (transposed)** block mask: per-KV-block lists of Q-blocks, shape `[B, H, n_kv_blocks, n_q_blocks]`, with `sparse_block_size_q = subtile_factor * m_block_size`. The docstring even hints: *"Backward expects Q-direction block-sparse tensors … Regenerate the backward BlockMask with BLOCK_SIZE=(subtile_factor*m_block_size, n_block_size)."*

But the public `flash_attn_func` only accepts the **forward (M-direction)** mask (`full_block_cnt/idx`, `mask_block_cnt/idx` = per-Q-block lists of KV-blocks), and `FlashAttnFunc.forward` saves only `(q, k, v, out, lse)` for backward — there is no parameter or saved tensor for the transposed backward mask. So `FlashAttnFunc.backward` ends up feeding the forward (M-direction) mask into the backward, which interprets it as the N-direction mask → reads the wrong blocks → silently-wrong gradients (no shape error here because the index tensor is near-square).

Net: block-sparse **training** via the public `flash_attn_func` looks unsupported in 4.0.0b5 — the forward mask is correct (and gives a real prefill speedup) but the API exposes no way to pass the transposed backward mask the bwd kernel requires. The lower-level `_flash_attn_bwd` does take a `block_sparse_tensors` arg, so a fix could thread a separate (transposed) backward mask through `FlashAttnFunc`, or have it auto-transpose the forward mask.

Env: `head_dim` 64 & 128, SM90 (H200), `flash-attn-4` 4.0.0b5, `nvidia-cutlass-dsl` 4.4.2, torch 2.10.0+cu128.


### reubenconducts · 2026-06-04

The `flash_attn_func` API was changed in https://github.com/Dao-AILab/flash-attention/pull/2506. The user must pass in `block_sparse_tensors` for forward and additionally `block_sparse_tensors_bwd` to be used in backward. I've yet to add backward-transposed tensors to `compute_block_sparsity`, though. 

### vaderyang · 2026-06-04

Thanks @reubenconducts — confirming the transposed-bwd-mask diagnosis, and reporting a **second, separate bug** that will still bite `head_dim=64` even once `block_sparse_tensors_bwd` is wired up.

**1. Working fix on 4.0.0b5 (no `block_sparse_tensors_bwd` param yet) via the lower-level path.** Calling `_flash_attn_fwd` / `_flash_attn_bwd` directly and threading a separate transposed mask makes the gradients correct:

- Force the **forward** tile to `(128,128)` (via `tile_mn`) instead of the `head_dim=64` default `(192,128)`, so the forward q-block matches the backward's `sparse_block_size_q = subtile_factor(2) * m_block_size(64) = 128`. With aligned granularity the **backward Q-direction mask is the pure transpose of the forward M-direction selection** (per-KV-block lists of Q-blocks), and `mask_mod=causal` reconstructs the diagonal in both directions — no separate data-dependent backward mask builder needed.
- Forward: `_flash_attn_fwd(q,k,v, tile_mn=(128,128), mask_mod=causal, block_sparse_tensors=fwd_bs, return_lse=True)`.
- Backward: `_flash_attn_bwd(q,k,v,out,dout,lse, mask_mod=causal, block_sparse_tensors=bwd_bs)` where `bwd_bs` is the transpose of `fwd_bs` (block_size `(128,128)`).

Result on SM90/H200: dq/dk/dv rel-err **~3e-3** (bf16 noise) vs an SDPA reference over the identical token mask, across several shapes (T=768–4096) and a degenerate `top_k=all == dense causal` check. (Before: dq/dk/dv off by 190–3039×.)

**2. The second bug — `AtomLayoutMdQ` vs the forced `m_block_size=64` for `head_dim<=64` block-sparse backward.**

`_flash_attn_bwd` forces `m_block_size = 64` for SM90 block-sparse:
```python
if arch // 10 == 9 and use_block_sparsity:
    m_block_size = 64
    dQ_swapAB = False
```
but `_tile_size_bwd_sm90(head_dim<=64)` returns `AtomLayoutMdQ=2` (tuned for the dense `m_block_size=128`). The dQ MMA tiler M is then `m_block_size // AtomLayoutMdQ = 64 // 2 = 32`, which is **< the 64 WGMMA M-mode minimum**, so both the main bwd kernel (`flash_bwd_sm90._get_tiled_mma`) and the dQ postprocess (`flash_bwd_postprocess._get_tiled_mma`) raise:
```
OpError: expects the M-mode to be 64, but got 32
```
So even with a correct transposed backward mask, `head_dim=64` block-sparse backward won't compile on SM90 until `AtomLayoutMdQ` is adjusted.

**Minimal upstream fix:** when `arch//10==9 and use_block_sparsity and head_dim <= 64`, also set `AtomLayoutMdQ = 1` (tiler M = `64 // 1 = 64`; the dQ N-tiler stays clean: `head_dim // (num_wg_mma // 1) = 64 // 2 = 32`). Dense `head_dim=64` (`m_block_size=128`) must keep `AtomLayoutMdQ=2`, so the override has to be conditional on `use_block_sparsity` — patching `_tile_size_bwd_sm90` unconditionally breaks dense (its WGMMA M-mode then becomes 128). I validated this exact change (gated to in-flight block-sparse backward) against the dense path: dense backward is unchanged and block-sparse backward becomes correct.

`head_dim=128` block-sparse backward is unaffected by bug #2 (its `m_block_size=64` is native and `AtomLayoutMdQ=1` already), so once `block_sparse_tensors_bwd` lands it should work there without the `AtomLayoutMdQ` change.

Env: SM90 (H200), `flash-attn-4` 4.0.0b5, `nvidia-cutlass-dsl` 4.4.2, torch 2.10.0+cu128.


### Johnsonms · 2026-06-04

Thanks @vaderyang , I will check it today and cycle back to you later

### Johnsonms · 2026-06-04

Thank @vaderyang  again for the detailed reproduction and investigation.

I've verified the issue on H100 (SM90). The problem is reproducible in **FlashAttention 4.0.0b5**, but it has already been fixed in **4.0.0b11** (released on 2026-04-28) and all subsequent versions.

**Root cause**

The issue is not caused by the tile-mismatch hypothesis.

In **4.0.0b5**, `FlashAttnFunc.backward` in `flash_attn/cute/interface.py` did not save or forward `mask_mod` or the block-sparse tensors when invoking `_flash_attn_bwd`. As a result, the forward pass correctly applied the block-sparse causal pattern, while the backward pass effectively executed as if the attention were dense and unmasked.

This caused gradients to be computed against a different function than the one used during the forward pass, producing finite but significantly incorrect values (approximately 150–700× off).

**Fixes**

* **#2485**: Propagated `mask_mod`, `score_mod`, and `aux_tensors` through the autograd context.
* **#2506**: Added `ctx.block_sparse_tensors_bwd` and forwarded the block-sparse tensors to the backward kernel.

Both fixes first appear in **fa4-v4.0.0.beta11** (verified via `git tag --contains`). The affected range is **4.0.0b5–4.0.0b10**.

**Validation on current main (4.0.0b17.dev)**

Compared against a float32 SDPA reference:

* Causal block-sparse (your exact pattern):

  * Forward relative error: **2.2e-3**
  * dQ / dK / dV relative error: **≤ 5e-3**

* Sliding-window non-causal block-sparse:

  * Forward relative error: **2.1e-3**
  * dQ / dK / dV relative error: **≤ 6e-3**

Additionally:

* `bsp_out` vs. dense-causal: **3.42** (non-zero), confirming that the block-sparse path is actively being exercised.

All results are well within expected BF16 tolerance.

**Recommended fix**

```bash
pip install -U "flash-attn-4>=4.0.0b11"
```

Please let us know if you can still reproduce the issue after upgrading. Otherwise, I'll consider this resolved and close the issue.


### vaderyang · 2026-06-05

Confirmed fixed — thanks for the quick and thorough investigation, @Johnsonms.

I upgraded to **4.0.0b11** (with **quack-kernels 0.5.0**) and verified first-hand that the **public** API path is correct for `head_dim=64`:

```python
out = flash_attn_func(
    q, k, v, softmax_scale=scale, causal=False, mask_mod=causal_mask_mod,
    block_sparse_tensors=fwd_bs,        # M-direction (per-q-block -> kv-blocks)
    block_sparse_tensors_bwd=bwd_bs,    # Q-direction = transpose of fwd selection
)
out.backward(dout)
```

vs a float32 SDPA reference over the identical token mask, across a few shapes (T=768/2048/4096, causal + sink/local/top-k block-sparse):

* forward rel-err ≈ **2e-3**
* dQ / dK / dV rel-err ≈ **3–5e-3**

All within BF16 tolerance, with **no workarounds** — no lower-level calls, no tile overrides.

**Retracting my "second bug" (the `AtomLayoutMdQ` / `m_block_size=64` tiler note).** That `OpError: expects the M-mode to be 64, but got 32` was an artifact of my **b5 workaround**: since b5's public `FlashAttnFunc` didn't accept a backward mask, I was threading a transposed mask through the lower-level `_flash_attn_bwd` directly with a forced `tile_mn=(128,128)`, and b5's bwd config (`AtomLayoutMdQ=2` with the forced `m_block_size=64`) produced the 32-wide tiler. On b11 this doesn't arise: `_tile_size_{fwd,bwd}_sm90` now take `sparse_block_size_q` and align the tiles natively, so the public path just works. So it's **not** a live upstream bug — apologies for the noise.

One note for anyone still on the b5–b10 range hitting this: upgrading also requires **`quack-kernels>=0.4.0`** — with the b5-era `quack-kernels==0.3.5`, the b11 backward fails with `get_smem_store_C() missing 1 required positional argument: 'arch'` (the bwd kernel calls the newer `quack.copy_utils` signature).

Resolved on my end — feel free to close. Thanks again!


### Johnsonms · 2026-06-05

Great, Thanks @vaderyang
