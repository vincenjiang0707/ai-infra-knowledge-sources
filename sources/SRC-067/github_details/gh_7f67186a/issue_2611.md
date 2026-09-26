# [Issue #2611] [FA4] cute varlen backward: int32 overflow in `_bwd_preprocess` corrupts `dQ/dK/dV` when `dout` has a large outer stride

source: https://github.com/Dao-AILab/flash-attention/issues/2611
state: closed | updated: 2026-06-01T02:29:41Z
labels: 

## 正文

### Summary

In `flash_attn.cute.flash_attn_varlen_func` backward, when `dout` is
non-contiguous and any `cu_seqlens[k] * dout.stride(0) >= 2**31`, the cute
kernel `_bwd_preprocess` indexes `dout` with a wrapped 32-bit offset. The
backward either silently corrupts `dQ/dK/dV` or terminates with
`cudaErrorIllegalAddress`. Forward is unaffected.

### Root cause

In `cutlass.cute.crd2idx` (reached via FA4 backward's per-segment
`domain_offset` on `dout`), `coord[0] * stride[0]` is accumulated in i32.
On overflow it sign-extends to i64 and is added to the tensor pointer,
sending the kernel ~2 GiB before the real base.

Verified sample (in-kernel probe, real training step):

```
dout.shape  = (410923, 16, 96)
dout.stride = (9728, 96, 1)        # view of cat([attn_flat, mlp], dim=1)

coord            = (225304, _, _)
true_offset      = 225304 * 9728 = 2_191_757_312
off_signed_i32   = -2_103_209_984              # = true_offset - 2**32
off_unsigned_i64 = 18_446_744_071_606_341_632  # sign-extended i32
```

### Real-world trigger

Any block that cats attn output with another feature before a linear:

```python
attn_out  = flash_attn_varlen_func(q, k, v, cu, cu, mx, mx)   # [N, H, D]
stream    = torch.cat([attn_out.reshape(N, H*D), mlp_out], dim=1)
linear(stream).sum().backward()
# cat-bwd → grad of attn_flat is a stride-view with stride[0] = H*D + M.
# Reshape to [N, H, D] → dout stride (H*D + M, D, 1).
```

For `H=16, D=96, M=8192` → `stride[0] = 9728`, wrap threshold is just
`2**31 / 9728 ≈ 220_753` tokens, easily hit by packed-sequence training.

### Environment

- `flash-attention` @ `6c4f74f` (2026-05-25)
- `nvidia-cutlass-dsl` 4.5.0, PyTorch 2.10.0+cu130, CUDA 13.0
- GPU: NVIDIA B300 SXM6 (also reproduces on B200)

### Minimal repro

Single self-contained script (depends only on `torch` + `flash_attn.cute`).
Two tests, identical `(q, k, v)` and numerical `dout`, same kernel — they
differ **only** in `cu_seqlens`:

| Test | `cu_seqlens` | Expected | Observed |
|------|---|---|---|
| `test_no_overflow_single_segment` | `[0, 410_923]` (only coord is 0) | PASS | PASS — `dQ rel_err=5e-3, dK=dV=0` |
| `test_overflow_multi_segment`     | `[0, 225_304, 410_923]` (225 304 × 9 728 > 2³¹) | FAIL | FAIL — **`cudaErrorIllegalAddress`** |

Run (≥30 GiB free VRAM, Hopper/Blackwell):

```bash
python test_bwd_preprocess_i32_overflow.py
# or
pytest -xvs test_bwd_preprocess_i32_overflow.py
```

Observed output of the failing test:

```
--- repro: multi-segment, offset crosses 2**31 ---
  cu_seqlens          = [0, 225304, 410923]
  stride[0]           = 9728
  max_off * stride[0] = 2191757312  (i32 wrap @ 2147483648)  →  WRAP EXPECTED
  FA4(view-dout) FAILED: AcceleratorError: CUDA error: an illegal memory access was encountered
  → i32-wrapped pointer reads OOB. BUG REPRODUCED.
```

<details>
<summary><b>Full repro script</b> — <code>test_bwd_preprocess_i32_overflow.py</code> (click to expand)</summary>

```python
# SPDX-License-Identifier: BSD-3-Clause
"""
Repro: FA4 (cute) varlen backward — int32 overflow in `_bwd_preprocess`.

When `dout` flowing into `flash_attn.cute.flash_attn_varlen_func`'s backward
is non-contiguous and `cu_seqlens[k] * dout.stride(0) >= 2**31`, the cute
kernel `_bwd_preprocess` indexes `dout` with a wrapped i32 offset — silently
corrupts `dQ/dK/dV` or raises `cudaErrorIllegalAddress`.

Trigger from a real `cat([attn_flat, mlp], dim=1) → linear → loss.backward()`
chain. With H=16, D=96, M=8192 → stride[0] = 1536+8192 = 9728, the wrap
threshold is just 2**31 / 9728 ≈ 220_753 tokens.

Two tests differ ONLY in `cu_seqlens`:
  * test_no_overflow_single_segment  : cu=[0, N]              → PASS
  * test_overflow_multi_segment      : cu=[0, 225_304, N]     → FAIL
    (225_304 × 9_728 = 2_191_757_312 > 2**31)

Run (≥30 GiB free VRAM on Hopper/Blackwell):
    python test_bwd_preprocess_i32_overflow.py
    pytest -xvs test_bwd_preprocess_i32_overflow.py
"""

from __future__ import annotations

import sys
import traceback

import pytest
import torch


# Config taken from a real training log so the wrap predicate is reproduced
# exactly. BUG_OFFSET = 225_304 is one of the per-batch coords printed by an
# in-kernel probe; 225_304 × 9_728 = 2_191_757_312 > 2**31.
TOTAL_Q, NUM_HEADS, HEAD_DIM = 410_923, 16, 96
ATTN_DIM   = NUM_HEADS * HEAD_DIM         # = 1536
MLP_DIM    = 8_192
STREAM_DIM = ATTN_DIM + MLP_DIM           # = 9728  (outer stride after cat)
BUG_OFFSET = 225_304
DTYPE      = torch.bfloat16
SEED       = 0
REL_TOL    = 1e-2                          # bf16 noise floor; bug → O(1)
MIN_FREE_VRAM_BYTES = 30 * (1024 ** 3)


def _check_env():
    if not torch.cuda.is_available():
        return "CUDA GPU required."
    try:
        from flash_attn.cute import flash_attn_varlen_func  # noqa: F401
    except Exception as e:
        return f"flash-attn 4.x cute backend not importable: {e!r}"
    free, _ = torch.cuda.mem_get_info()
    if free < MIN_FREE_VRAM_BYTES:
        return f"insufficient free VRAM: {free / 2**30:.1f} GiB < 30 GiB."
    return None


_SKIP = _check_env()
pytestmark = pytest.mark.skipif(_SKIP is not None, reason=_SKIP or "")


def _randn(*shape, seed):
    g = torch.Generator(device="cuda").manual_seed(seed)
    return torch.randn(*shape, device="cuda", dtype=DTYPE, generator=g) * 0.1


def _make_qkv():
    g = torch.Generator(device="cuda").manual_seed(SEED)
    qkv = torch.randn(3, TOTAL_Q, NUM_HEADS, HEAD_DIM,
                      device="cuda", dtype=DTYPE, generator=g) * 0.1
    return qkv[0], qkv[1], qkv[2]


def _fa4_bwd(q0, k0, v0, dout, cu, mx):
    """One FA4 varlen backward; returns (dq, dk, dv) detached."""
    from flash_attn.cute import flash_attn_varlen_func as fa4
    q = q0.detach().clone().requires_grad_()
    k = k0.detach().clone().requires_grad_()
    v = v0.detach().clone().requires_grad_()
    ret = fa4(q, k, v, cu_seqlens_q=cu, cu_seqlens_k=cu,
              max_seqlen_q=mx, max_seqlen_k=mx, causal=False)
    out = ret[0] if isinstance(ret, tuple) else ret
    dq, dk, dv = torch.autograd.grad(out, [q, k, v], dout)
    return dq.detach(), dk.detach(), dv.detach()


def _capture_view_dout(q, k, v, cu, mx):
    """Run `attn → cat([attn_flat, mlp], dim=1) → matmul → sum.backward()`
    and return the captured view-stride dout with shape [N, H, D] and
    stride (STREAM_DIM, HEAD_DIM, 1) — exactly the layout FA4 sees in the
    buggy real-world path. The in-chain backward gets a *contiguous* dout
    so it doesn't crash; we replay the captured view-dout ourselves.
    """
    from flash_attn.cute import flash_attn_varlen_func as fa4
    qx = q.detach().clone().requires_grad_()
    kx = k.detach().clone().requires_grad_()
    vx = v.detach().clone().requires_grad_()
    mlp = _randn(TOTAL_Q, MLP_DIM, seed=SEED + 1)
    w2  = _randn(STREAM_DIM, 1,    seed=SEED + 2)   # 1-column → minimal mem

    ret  = fa4(qx, kx, vx, cu_seqlens_q=cu, cu_seqlens_k=cu,
               max_seqlen_q=mx, max_seqlen_k=mx, causal=False)
    attn = ret[0] if isinstance(ret, tuple) else ret
    attn_flat = attn.reshape(TOTAL_Q, ATTN_DIM)

    captured = {}

    def _hook(g):
        # `clone(memory_format=preserve_format)` only handles
        # contiguous/channels_last — use empty_strided+copy_ to preserve
        # the arbitrary stride for our replay.
        buf = torch.empty_strided(g.shape, g.stride(),
                                  dtype=g.dtype, device=g.device)
        buf.copy_(g)
        captured["g"] = buf
        return g.contiguous()                       # keep in-chain bwd safe

    attn_flat.register_hook(_hook)
    ((torch.cat([attn_flat, mlp], dim=1) @ w2).sum()).backward()

    g_flat = captured["g"]
    assert g_flat.shape == (TOTAL_Q, ATTN_DIM) and g_flat.stride() == (STREAM_DIM, 1)
    dout_view = g_flat.reshape(TOTAL_Q, NUM_HEADS, HEAD_DIM)
    assert dout_view.stride() == (STREAM_DIM, HEAD_DIM, 1) and not dout_view.is_contiguous()

    del qx, kx, vx, mlp, w2, attn, attn_flat, ret, g_flat
    torch.cuda.empty_cache()
    return dout_view


def _rel_err(a, b):
    return ((a.float() - b.float()).abs().max()
            / b.float().abs().max().clamp_min(1e-30)).item()


def _run_one(cu_list, label):
    """Build inputs, capture view-dout, run FA4 bwd twice (view vs contig).
    Returns (eq, ek, ev) rel-errs. A CUDA illegal-access in the view call is
    the strongest form of the bug — reported as inf rel-errs.
    """
    q, k, v = _make_qkv()
    cu = torch.tensor(cu_list, device="cuda", dtype=torch.int32)
    mx = int((cu[1:] - cu[:-1]).max().item())
    max_off = max(cu_list[:-1])

    header = (
        f"\n--- {label} ---\n"
        f"  cu_seqlens          = {cu_list}\n"
        f"  stride[0]           = {STREAM_DIM}\n"
        f"  max_off * stride[0] = {max_off * STREAM_DIM}"
        f"  (i32 wrap @ {2**31})  →  "
        f"{'WRAP EXPECTED' if max_off * STREAM_DIM >= 2**31 else 'no wrap'}\n"
    )

    dout_view = _capture_view_dout(q, k, v, cu, mx)

    # Run contig FIRST — if the view call later poisons the context, we
    # already have the reference safely on CPU.
    dq_c, dk_c, dv_c = (t.cpu() for t in _fa4_bwd(q, k, v, dout_view.contiguous(), cu, mx))
    torch.cuda.synchronize()

    try:
        dq_v, dk_v, dv_v = _fa4_bwd(q, k, v, dout_view, cu, mx)
        torch.cuda.synchronize()
    except Exception as e:
        print(header + f"  FA4(view-dout) FAILED: {type(e).__name__}: {e}\n"
                       f"  → i32-wrapped pointer reads OOB. BUG REPRODUCED.",
              flush=True)
        return float("inf"), float("inf"), float("inf")

    eq = _rel_err(dq_v, dq_c.cuda())
    ek = _rel_err(dk_v, dk_c.cuda())
    ev = _rel_err(dv_v, dv_c.cuda())
    print(header + f"  rel_err vs FA4-contig:  dQ={eq:.3e}  dK={ek:.3e}  dV={ev:.3e}",
          flush=True)
    return eq, ek, ev


def test_no_overflow_single_segment():
    """Control: cu=[0, N], only segment-start coord is 0, no wrap. EXPECT PASS."""
    eq, ek, ev = _run_one([0, TOTAL_Q], "control: single-segment, no wrap")
    assert eq < REL_TOL and ek < REL_TOL and ev < REL_TOL, \
        f"control failed (env broken?): dQ={eq:.2e} dK={ek:.2e} dV={ev:.2e}"


def test_overflow_multi_segment():
    """Repro: cu=[0, 225_304, N]. 225_304 × 9_728 > 2**31 → bug fires. EXPECT FAIL."""
    assert BUG_OFFSET * STREAM_DIM >= 2**31, "BUG_OFFSET doesn't satisfy wrap predicate"
    eq, ek, ev = _run_one([0, BUG_OFFSET, TOTAL_Q],
                          "repro: multi-segment, offset crosses 2**31")
    assert eq < REL_TOL and ek < REL_TOL and ev < REL_TOL, \
        f"BUG REPRODUCED: i32 wrap corrupts grads. dQ={eq:.2e} dK={ek:.2e} dV={ev:.2e}"


def _run(name, fn):
    print(f"\n========== {name} ==========", flush=True)
    try:
        fn(); print(f"[{name}] PASS", flush=True); return True
    except AssertionError as e:
        print(f"[{name}] FAIL: {e}", flush=True); return False
    except Exception:
        traceback.print_exc(); return False


if __name__ == "__main__":
    if _SKIP is not None:
        print(f"SKIP: {_SKIP}", flush=True); sys.exit(0)
    print(f"Repro: total_q={TOTAL_Q} H={NUM_HEADS} D={HEAD_DIM} "
          f"stream_dim={STREAM_DIM}  wrap @ cu_seqlens[k] >= "
          f"{2**31 // STREAM_DIM + 1}", flush=True)
    r1 = _run("test_no_overflow_single_segment", test_no_overflow_single_segment)
    r2 = _run("test_overflow_multi_segment",     test_overflow_multi_segment)
    print(f"\nexpected (bug active):  PASS, FAIL\n"
          f"actual:                 {'PASS' if r1 else 'FAIL'}, "
          f"{'PASS' if r2 else 'FAIL'}", flush=True)
    sys.exit(0 if r1 else 2)
```

</details>

### User-side workaround

Force `dout` contiguous before FA4 backward:

```python
attn_out = flash_attn_varlen_func(q, k, v, cu, cu, mx, mx)
if attn_out.requires_grad:
    attn_out.register_hook(lambda g: g.contiguous() if not g.is_contiguous() else g)
```

After this fix our training loss recovered exactly to the pre-FA4 baseline.

### Suggested kernel-side fix

Widen the offset accumulator in `crd2idx` (or at FA4's `domain_offset` call
site for the per-segment `dout` slice) so that `coord[0] * stride[0]` is
computed in i64 before being added to the pointer.

Happy to test a candidate patch on the same hardware.


## 评论 (4)

### Johnsonms · 2026-06-01

Thanks @zhipenggong for catching up, will take a look soon

### jayhshah · 2026-06-01

It's probably this issue with cutlass 4.5.0 (https://github.com/NVIDIA/cutlass/issues/3208), can you upgrade to 4.5.2 and see if that fixes it?

### zhipenggong · 2026-06-01

Yes, it's fixed after upgrade to 4.5.2. Thank you very much for the help.

### Johnsonms · 2026-06-01

 I also confirm this on a GB300.

The dependency floor has already been bumped to `nvidia-cutlass-dsl>=4.5.2` on main in #2605, but the current published `flash-attn-4 4.0.0b15` wheel still allows older affected DSL versions. Until the next wheel is published, the workaround is:

```bash
pip install -U "nvidia-cutlass-dsl>=4.5.2"
```

