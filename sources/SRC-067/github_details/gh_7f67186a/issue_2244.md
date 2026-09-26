# [Issue #2244] FA3 deterministic=True gives non-deterministic gradients in backward (flash_attn_func / flash_attn_qkvpacked_func)

source: https://github.com/Dao-AILab/flash-attention/issues/2244
state: open | updated: 2026-09-21T20:48:27Z
labels: 

## 正文

Hi FlashAttention team,

I am testing FlashAttention3 APIs to verify whether deterministic=True guarantees deterministic computation (bitwise reproducibility across multiple runs).

I found that while the forward outputs are deterministic, the backward gradients are still non-deterministic (bitwise mismatch), even when deterministic=True.

This happens consistently on my environment and can be reproduced with a minimal single-op test.

```log
[Test] flash_attn_qkvpacked_func FWD+BWD deterministic=True
[Forward Output Compare]  {'all_equal': True, 'max_abs_diff': 0.0, 'unequal_count': 0, 'total_runs': 30}
[Backward Grad Compare]   {'all_equal': False, 'max_abs_diff': 0.0001220703125, 'unequal_count': 29, 'total_runs': 30}
````

```log
[Test] flash_attn_func FWD+BWD deterministic=True
[Forward Output Compare]      {'all_equal': True, 'max_abs_diff': 0.0, 'unequal_count': 0, 'total_runs': 30}
[Backward Grad Q Compare]     {'all_equal': False, 'max_abs_diff': 0.0001220703125, 'unequal_count': 29, 'total_runs': 30}
[Backward Grad K Compare]     {'all_equal': True, 'max_abs_diff': 0.0, 'unequal_count': 0, 'total_runs': 30}
[Backward Grad V Compare]     {'all_equal': True, 'max_abs_diff': 0.0, 'unequal_count': 0, 'total_runs': 30}
````

So it seems:

- dq is non-deterministic
- dk and dv are deterministic (at least for this test shape)
- forward is deterministic


Minimal Reproduction Script:
```python
import torch
import numpy as np

from flash_attn_interface import flash_attn_func, flash_attn_qkvpacked_func


def set_seed(seed=0):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)


def compare_tensor_list(tensors):
    ref = tensors[0]
    all_equal = True
    max_diff = 0.0
    unequal_count = 0

    for t in tensors[1:]:
        if not torch.equal(ref, t):
            all_equal = False
            unequal_count += 1
        max_diff = max(max_diff, (ref - t).abs().max().item())

    return {
        "all_equal": all_equal,
        "max_abs_diff": max_diff,
        "unequal_count": unequal_count,
        "total_runs": len(tensors),
    }


def test_flash_attn_qkvpacked_fwd_bwd(deterministic=True, runs=30, dtype=torch.float16):
    print("\n===========================================")
    print(f"[Test] flash_attn_qkvpacked_func FWD+BWD deterministic={deterministic}")
    print("===========================================")

    set_seed(123)

    B, S, H, D = 2, 512, 8, 64
    qkv_base = torch.randn(B, S, 3, H, D, device="cuda", dtype=dtype)
    dout_base = torch.randn(B, S, H, D, device="cuda", dtype=dtype)

    out_list = []
    grad_list = []

    torch.cuda.synchronize()

    for _ in range(runs):
        qkv = qkv_base.clone().detach().requires_grad_(True)

        out = flash_attn_qkvpacked_func(
            qkv,
            causal=False,
            deterministic=deterministic,
        )

        out.backward(dout_base)

        out_list.append(out.detach().clone())
        grad_list.append(qkv.grad.detach().clone())

        torch.cuda.synchronize()

    print("[Forward Output Compare] ", compare_tensor_list(out_list))
    print("[Backward Grad Compare] ", compare_tensor_list(grad_list))


def test_flash_attn_func_fwd_bwd(deterministic=True, runs=30, dtype=torch.float16):
    print("\n===========================================")
    print(f"[Test] flash_attn_func FWD+BWD deterministic={deterministic}")
    print("===========================================")

    set_seed(456)

    B, S, H, D = 2, 1024, 12, 64

    q_base = torch.randn(B, S, H, D, device="cuda", dtype=dtype)
    k_base = torch.randn(B, S, H, D, device="cuda", dtype=dtype)
    v_base = torch.randn(B, S, H, D, device="cuda", dtype=dtype)

    dout_base = torch.randn(B, S, H, D, device="cuda", dtype=dtype)

    out_list = []
    gq_list, gk_list, gv_list = [], [], []

    torch.cuda.synchronize()

    for _ in range(runs):
        q = q_base.clone().detach().requires_grad_(True)
        k = k_base.clone().detach().requires_grad_(True)
        v = v_base.clone().detach().requires_grad_(True)

        out = flash_attn_func(
            q, k, v,
            causal=True,
            deterministic=deterministic,
        )

        out.backward(dout_base)

        out_list.append(out.detach().clone())
        gq_list.append(q.grad.detach().clone())
        gk_list.append(k.grad.detach().clone())
        gv_list.append(v.grad.detach().clone())

        torch.cuda.synchronize()

    print("[Forward Output Compare] ", compare_tensor_list(out_list))
    print("[Backward Grad Q Compare] ", compare_tensor_list(gq_list))
    print("[Backward Grad K Compare] ", compare_tensor_list(gk_list))
    print("[Backward Grad V Compare] ", compare_tensor_list(gv_list))


if __name__ == "__main__":
    assert torch.cuda.is_available()
    test_flash_attn_qkvpacked_fwd_bwd(deterministic=True)
    test_flash_attn_func_fwd_bwd(deterministic=True)
```


## 评论 (3)

### NJX-njx · 2026-03-14

I'll try to reproduce this and investigate why deterministic=True still yields non-deterministic dq in backward. Will report findings and propose a fix or (if impossible) document the limitation precisely.

### NJX-njx · 2026-03-29

I'd like to look into this. The issue was reported against FA3 (hopper/), but I'll audit the same deterministic path in FA4 (\) — specifically the \ cluster-wide reduction in \ and the corresponding backward kernels — to determine if the same non-determinism exists there and submit a fix.

### LiRunGuo · 2026-09-21

I tried to reproduce this on current main (edb5c76) and could not.

Setup: H200 (SM90), CUDA 12.8 nvcc, torch 2.11.0+cu128. FA3 built from `hopper/` (hdim 64/128, fp16/bf16).

Test: `flash_attn_func(..., deterministic=True)` forward+backward, with dQ/dK/dV compared bitwise against the first run. Six configs:
- your two shapes: fp16, B2 S1024 H12 D64 and B2 S512 H8 D64, non-causal;
- bf16 D128 S2048, causal and non-causal;
- GQA 16/2 at D128 non-causal and D64 causal (this exercises the dK/dV semaphore path).

Results: all bitwise identical over
- 30 runs on an idle GPU,
- 200 runs on an idle GPU,
- 200 runs on a GPU kept at ~97% utilization by other jobs (to perturb timing).

One note from reading the code. `hopper/mainloop_bwd_sm90_tma_gmma_ws.hpp` (dQ) and `hopper/epilogue_bwd.hpp` (GQA dK/dV) call `tma_store_wait<>()`, which is `cp.async.bulk.wait_group.read`, before `Barrier::arrive_inc`. That only guarantees the smem source has been read, not that the bulk reduce-add has landed in gmem. FA4's SM90 backward uses a non-`.read` wait in deterministic mode (#2510). So the ordering could in principle be weaker than intended, but I couldn't observe any effect on this setup, and I didn't want to propose a fix without a repro.

Could you share your GPU model, CUDA/driver version, and the FA3 commit or wheel you used? That would help decide whether this is still live.

