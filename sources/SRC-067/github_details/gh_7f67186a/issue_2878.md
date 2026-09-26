# [Issue #2878] [FA4, Hopper, BWD] BWD Speed Regression on H200 when headdim=256

source: https://github.com/Dao-AILab/flash-attention/issues/2878
state: closed | updated: 2026-09-14T22:26:52Z
labels: 

## 正文

flash-attn-4    version:      4.0.0b24


Supposely, the runtime of bwd of FA4 should be nearly 500ms given the runtime of headdim=128. Unfortunately, it takes almost twice the runtime. 

```
batch_size: 1,  seq_len: 86000, head_size: 32, dim: 128
runtime of fwd of FA4 at bf16 precision in milliseconds: 88.88246 (88.88246, 88.88246).
---------------------------------------------------------------------
runtime of bwd of FA4 at bf16 precision in milliseconds: 246.29193 (246.29193, 246.29193).
---------------------------------------------------------------------
batch_size: 1,  seq_len: 86000, head_size: 32, dim: 256
runtime of fwd of FA4 at bf16 precision in milliseconds: 166.24957 (166.24957, 166.24957).
---------------------------------------------------------------------
runtime of bwd of FA4 at bf16 precision in milliseconds: 965.84863 (965.84863, 965.84863).
---------------------------------------------------------------------
```

To reproduce, run the following code on H200 under 4.0.0b24:

```
import torch
import triton
from flash_attn.cute.interface import flash_attn_varlen_func as FA4_Varlen

def benchmark(f, job_name:str):
    warmup=20
    rep=100
    ms = triton.testing.do_bench(f, warmup=warmup, rep=rep, quantiles=[0.2, 0.5, 0.8])
    print(f"runtime of {job_name} in milliseconds: {ms[1]:.5f} ({ms[0]:.5f}, {ms[2]:.5f}).")
    return ms[1]

def test_once_varlen(batch_size, seq_len, num_heads, dim):
    print(f"batch_size: {batch_size},  seq_len: {seq_len}, head_size: {num_heads}, dim: {dim}")
    q, k, v = get_tensors(batch_size, seq_len, num_heads, dim)
    device = "cuda"
    cu_q = torch.tensor([0, seq_len >> 1, seq_len], device=device, dtype=torch.int32)
    cu_k = torch.tensor([0, seq_len >> 1, seq_len], device=device, dtype=torch.int32)
    max_seqlen_q = int((cu_q[1:] - cu_q[:-1]).max())
    max_seqlen_k = int((cu_k[1:] - cu_k[:-1]).max())
    fa4_fwd_bf16 = lambda: FA4_Varlen(
        q[0], k[0], v[0],
        cu_seqlens_q=cu_q, cu_seqlens_k=cu_k,
        max_seqlen_q=max_seqlen_q, max_seqlen_k=max_seqlen_k,
    )
    runtime_fa4_fwd_bf16 = benchmark(fa4_fwd_bf16, "fwd of FA4 at bf16 precision")
    print("---------------------------------------------------------------------")

    out, _ = fa4_fwd_bf16()
    dout = torch.randn_like(out)
    fa4_bwd_bf16 = lambda: out.backward(dout, retain_graph=True)
    runtime_fa4_bwd_bf16 = benchmark(fa4_bwd_bf16, "bwd of FA4 at bf16 precision")
    print("---------------------------------------------------------------------")

    return runtime_fa4_fwd_bf16, runtime_fa4_bwd_bf16

def get_tensors(batch_size, seq_len, head_size, dim):
    torch.manual_seed(42)
    q = torch.randn((batch_size, seq_len, head_size, dim), dtype=torch.bfloat16, device="cuda", requires_grad=True)
    k = torch.randn((batch_size, seq_len, head_size, dim), dtype=torch.bfloat16, device="cuda", requires_grad=True)
    v = torch.randn((batch_size, seq_len, head_size, dim), dtype=torch.bfloat16, device="cuda", requires_grad=True)
    return q, k, v

if __name__ == "__main__":
    test_once_varlen(1, 86000, 32, 128)
    test_once_varlen(1, 86000, 32, 256)
```

## 评论 (1)

### SuperGoodGame · 2026-09-13

I'd like to take this one.

Reproduced on SM90 (8x H20Z, same silicon as H200). At your shape (varlen 86000, 32 heads): hdim128 bwd = 509 ms, hdim256 bwd = 1931 ms, 3.8x (you saw 3.9x). hdim256 bwd runs at ~300 TFLOP/s while the C++ FA3 hopper kernel gets ~480 on the same GPU; at hdim128 the two are at parity, so the gap is specific to this branch.

Root cause: the SM90 hdim256 `BwdConfig` is 64x64 with `num_stages_Q=1`, so TMA loads and WGMMA are serialized on every m-block. It cannot take a second stage because the DSL kernel always stages dQ through a 64 KB `sdQaccum` smem buffer. The C++ kernel skips that buffer for hdim256 (`dQacc_use_TMA = kHeadDim < 256`) and atomicAdds dQ from registers, which is what frees the smem for 64x80 + 2 stages there.

Plan:
1. Config change first: 64x48, `num_stages_Q=2`, `dKV_swapAB=True` for MHA. Measured +25% dense, +18% causal, +13% at your shape; numerics bit-identical to the current config; `test_flash_attn_output` d=256 MHA subset passes. GQA stays on the current config for now because `flash_bwd_postprocess` does not handle `dKV_swapAB` (GQA bwd at hdim 192 already fails on main for the same reason). This also fixes the current bwd crash for head_dim in (192, 256).
2. Then port the C++ hdim256 dQ path (no smem staging, sliced dQ MMA with register atomics) so 64x80 / 2-stage fits, aiming for FA3 parity.

PR for (1) coming first.

