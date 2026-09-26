# [Issue #2577] [Cute,Fwd,Sm100] FP8 precision degradation at KV tile boundaries due to rescale_threshold

source: https://github.com/Dao-AILab/flash-attention/issues/2577
state: open | updated: 2026-07-25T17:36:48Z
labels: 

## 正文

## Summary

FA4 FP8 (e4m3) forward pass on SM100 exhibits severe precision degradation (cosine similarity dropping to ~0.86) at KV sequence length tile boundaries (multiples of 128). The root cause is `rescale_threshold=4.0` interacting with `max_offset=8`, allowing intermediate P values up to 2^12 = 4096 which overflow FP8 e4m3 max (448).

## Environment

- GPU: NVIDIA B300 (SM100f)
- Flash Attention: main branch @ `4178915`
- FP8 support introduced in: `b65ae6b` (#2109)
- Test config: batch=1, q_seqlen=1, kv_seqlen=1~1023, num_heads=6 Q / 1 KV (GQA), head_dim=128, paged KV (page_size=128)

## Problem

When running FP8 paged decode attention, cosine similarity vs BF16 reference drops sharply at every 128-token boundary:
```
FA4 FP8 vs BF16 kv_seqlen=127: max_diff=0.032471  mean_diff=0.005810  cos_sim=0.99866372
FA4 FP8 vs BF16 kv_seqlen=128: max_diff=0.300781  mean_diff=0.047027  cos_sim=0.86276174
FA4 FP8 vs BF16 kv_seqlen=129: max_diff=0.302246  mean_diff=0.024087  cos_sim=0.95049518
FA4 FP8 vs BF16 kv_seqlen=130: max_diff=0.268127  mean_diff=0.038082  cos_sim=0.94660372
```

<img width="1800" height="750" alt="Image" src="https://github.com/user-attachments/assets/1155a325-9503-49ac-96b8-5384eeaf55ad" />

## Root Cause

In `flash_attn/cute/flash_fwd_sm100.py` (L2002-2005, as of `4178915`):

```python
rescale_threshold = (
    8.0 if const_expr(self.q_dtype.width == 16) else
    4.0 if const_expr(self.q_dtype.width == 8) else  # BUG
    0.0
)
```
Combined with max_offset = 8 (L1994), the effective exponent of P before FP8 cast is:
```
P_exp = (S - row_max) * scale_log2 + max_offset
```
When rescale_threshold=4.0, the softmax's update_row_max skips the O-accumulator rescale if the row_max change is within threshold:

```
if acc_scale_ >= -self.rescale_threshold:  # i.e., row_max increased by < 4.0
    row_max_new = row_max_old  # keep stale row_max
    acc_scale = 1.0            # skip rescale
```
This means the actual row_max can exceed the stored row_max by up to 4.0. The exponent becomes:
```
P_max_exp = threshold + max_offset = 4.0 + 8.0 = 12.0
P_max = 2^12 = 4096
```
But FP8 e4m3 maximum is 448 (2^8.81). Values above 448 saturate/overflow, corrupting the softmax normalization.

## Fix
Set `rescale_threshold = 0.0` for FP8

result after fix
<img width="1800" height="750" alt="Image" src="https://github.com/user-attachments/assets/a078ffe6-aa0e-4d6c-824a-8f54a29754bb" />

## Reproduction

```
"""
gt: SDPA fp32
baseline: fa4 bf16
target: fa4 fp8
"""

from typing import Optional
import torch
import torch.nn.functional as F

from flash_attn.cute.interface import _flash_attn_fwd

BATCH_SIZE = 1

NUM_Q_HEADS = 6
NUM_KV_HEADS = 1
HEAD_DIM = 128
SCALING = 1.0 / (HEAD_DIM**0.5)
PAGE_SIZE = 128

MAX_SEQLEN = 1024


FP32_DTYPE = torch.float32
FP8_DTYPE = torch.float8_e4m3fn
BF16_DTYPE = torch.bfloat16
DEVICE = "cuda:0"

def reference_attention_varlen(
    q_flat: torch.Tensor,
    k_flat: torch.Tensor,
    v_flat: torch.Tensor,
    cu_seqlens_q: list[int],
    cu_seqlens_k: list[int],
    scaling: float,
    causal: bool = True,
) -> torch.Tensor:
    """
    Variable-length reference attention using PyTorch SDPA in float32.

    q_flat: [total_q_tokens, num_q_heads, head_dim]
    k_flat: [total_k_tokens, num_kv_heads, head_dim]
    v_flat: [total_k_tokens, num_kv_heads, head_dim]

    Returns: [total_q_tokens, num_q_heads, head_dim] in bf16
    """
    num_q_heads = q_flat.shape[1]
    num_kv_heads = k_flat.shape[1]
    gqa_ratio = num_q_heads // num_kv_heads
    batch_size = len(cu_seqlens_q) - 1

    outputs = []
    for i in range(batch_size):
        q_start, q_end = cu_seqlens_q[i], cu_seqlens_q[i + 1]
        k_start, k_end = cu_seqlens_k[i], cu_seqlens_k[i + 1]

        qi = q_flat[q_start:q_end]
        ki = k_flat[k_start:k_end]
        vi = v_flat[k_start:k_end]

        if gqa_ratio > 1:
            ki = ki.repeat_interleave(gqa_ratio, dim=1)
            vi = vi.repeat_interleave(gqa_ratio, dim=1)

        # [1, num_heads, seq_len, head_dim]
        qi = qi.transpose(0, 1).unsqueeze(0)
        ki = ki.transpose(0, 1).unsqueeze(0)
        vi = vi.transpose(0, 1).unsqueeze(0)

        q_len = qi.shape[2]
        k_len = ki.shape[2]
        if causal and q_len != k_len:
            # Build bottom-right aligned causal mask explicitly to avoid
            # PyTorch version-dependent is_causal behavior when Q_len != K_len.
            offset = k_len - q_len
            row = torch.arange(q_len, device=qi.device).unsqueeze(1)
            col = torch.arange(k_len, device=qi.device).unsqueeze(0)
            mask = col <= row + offset
            out = F.scaled_dot_product_attention(qi, ki, vi, attn_mask=mask, scale=scaling)
        else:
            out = F.scaled_dot_product_attention(qi, ki, vi, scale=scaling, is_causal=causal)
        outputs.append(out.squeeze(0).transpose(0, 1))

    return torch.cat(outputs, dim=0)


def run_fa4(
    q: torch.Tensor,
    k_cache: torch.Tensor,
    v_cache: torch.Tensor,
    page_table: torch.Tensor,
    kv_seqlens: torch.Tensor,
    cu_seqlens_q: torch.Tensor,
    causal: bool,
    softmax_scale: float,
    q_descale: Optional[torch.Tensor] = None,
    k_descale: Optional[torch.Tensor] = None,
    v_descale: Optional[torch.Tensor] = None,
):

    result = _flash_attn_fwd(
        q=q,
        k=k_cache,
        v=v_cache,
        cu_seqlens_q=cu_seqlens_q,
        seqused_k=kv_seqlens,
        page_table=page_table,
        causal=causal,
        softmax_scale=softmax_scale,
        q_descale=q_descale,
        k_descale=k_descale,
        v_descale=v_descale,
    )

    if isinstance(result, tuple):
        return result[0]
    return result


def build_paged_kv_cache(
    k_flat: torch.Tensor,
    v_flat: torch.Tensor,
    cu_seqlens: list[int],
):
    bs = len(cu_seqlens) - 1
    seq_lens = [cu_seqlens[i + 1] - cu_seqlens[i] for i in range(bs)]
    max_seq_len = max(seq_lens)
    max_pages = (max_seq_len + PAGE_SIZE - 1) // PAGE_SIZE
    total_pages = sum((sl + PAGE_SIZE - 1) // PAGE_SIZE for sl in seq_lens)
    
    k_cache = torch.zeros(total_pages + 1, PAGE_SIZE, NUM_KV_HEADS, HEAD_DIM, dtype=k_flat.dtype, device=k_flat.device)
    v_cache = torch.zeros(total_pages + 1, PAGE_SIZE, NUM_KV_HEADS, HEAD_DIM, dtype=v_flat.dtype, device=v_flat.device)
    page_table = torch.zeros(bs, max_pages, dtype=torch.int32, device=k_flat.device)
    cache_seqlens = torch.tensor(seq_lens, dtype=torch.int32, device=k_flat.device)

    page_idx = 1
    for i in range(bs):
        s, e = cu_seqlens[i], cu_seqlens[i + 1]
        sl = e - s
        n_pages = (sl + PAGE_SIZE - 1) // PAGE_SIZE
        for p in range(n_pages):
            tok_start = s + p * PAGE_SIZE
            tok_end = min(tok_start + PAGE_SIZE, e)
            n = tok_end - tok_start
            k_cache[page_idx, :n] = k_flat[tok_start:tok_end]
            v_cache[page_idx, :n] = v_flat[tok_start:tok_end]
            page_table[i, p] = page_idx
            page_idx += 1

    return k_cache, v_cache, page_table, cache_seqlens

def precision_metrics(output: torch.Tensor, reference: torch.Tensor) -> dict:
    out_f = output.float().flatten()
    ref_f = reference.float().flatten()
    diff = (out_f - ref_f).abs()
    cos_sim = F.cosine_similarity(out_f.unsqueeze(0), ref_f.unsqueeze(0)).item()
    return {
        "max_diff": diff.max().item(),
        "mean_diff": diff.mean().item(),
        "cos_sim": cos_sim,
        "has_nan": bool(torch.isnan(output).any()),
    }

def fmt_metrics(m: dict) -> str:
    nan_flag = " [NaN!]" if m["has_nan"] else ""
    return f"max_diff={m['max_diff']:.6f}  mean_diff={m['mean_diff']:.6f}  cos_sim={m['cos_sim']:.8f}{nan_flag}"

def decode(q: torch.Tensor, k: torch.Tensor, v: torch.Tensor, cu_seqlens_q: torch.Tensor, cu_seqlens_k: torch.Tensor, dtype):
    k_cache, v_cache, page_table, kv_seqlens = build_paged_kv_cache(k, v, cu_seqlens_k.tolist())
    
    q = q.to(dtype)
    k_cache = k_cache.to(dtype)
    v_cache = v_cache.to(dtype)
    if dtype == FP8_DTYPE:
        ones = torch.ones(BATCH_SIZE, NUM_KV_HEADS, dtype=torch.float32, device=q.device)
        result = run_fa4(q, k_cache, v_cache, page_table, kv_seqlens, cu_seqlens_q, True, SCALING, ones, ones, ones)
    else:
        result = run_fa4(q, k_cache, v_cache, page_table, kv_seqlens, cu_seqlens_q, True, SCALING)
        
    return result

def cu_seqlens(seq_lens: list[int]) -> torch.Tensor:
    cu = [0]
    for s in seq_lens:
        cu.append(cu[-1] + s)
    return torch.tensor(cu, dtype=torch.int32, device=DEVICE)

def compare(kv_seqlen: int):
    total_kv_tokens = BATCH_SIZE * (kv_seqlen + 1)
    q = torch.randn(BATCH_SIZE, NUM_Q_HEADS, HEAD_DIM, dtype=FP32_DTYPE, device=DEVICE)
    k = torch.randn(total_kv_tokens, NUM_KV_HEADS, HEAD_DIM, dtype=FP32_DTYPE, device=DEVICE)
    v = torch.randn(total_kv_tokens, NUM_KV_HEADS, HEAD_DIM, dtype=FP32_DTYPE, device=DEVICE)

    cu_seqlens_q = cu_seqlens([1] * BATCH_SIZE)
    cu_seqlens_kv = cu_seqlens([kv_seqlen + 1] * BATCH_SIZE)

    ground_truth = reference_attention_varlen(q, k, v, cu_seqlens_q.tolist(), cu_seqlens_kv.tolist(), SCALING, True)
    result_bf16 = decode(q, k, v, cu_seqlens_q, cu_seqlens_kv, BF16_DTYPE).to(FP32_DTYPE)
    result_fp8 = decode(q, k, v, cu_seqlens_q, cu_seqlens_kv, FP8_DTYPE).to(FP32_DTYPE)
    m_fp8_bf16 = precision_metrics(result_fp8, result_bf16)
    print(f"FA4 FP8 vs BF16 {kv_seqlen=}: {fmt_metrics(m_fp8_bf16)}")

    m_fp8_gt = precision_metrics(result_fp8, ground_truth)
    m_bf16_gt = precision_metrics(result_bf16, ground_truth)

    return m_fp8_bf16, m_fp8_gt, m_bf16_gt

def bench():
    kv_seqlens = []
    cos_fp8_bf16 = []
    cos_fp8_gt = []
    cos_bf16_gt = []
    for i in range(1, MAX_SEQLEN):
        m_fp8_bf16, m_fp8_gt, m_bf16_gt = compare(i)
        kv_seqlens.append(i)
        cos_fp8_bf16.append(m_fp8_bf16['cos_sim'])
        cos_fp8_gt.append(m_fp8_gt['cos_sim'])
        cos_bf16_gt.append(m_bf16_gt['cos_sim'])
    return kv_seqlens, cos_fp8_bf16, cos_fp8_gt, cos_bf16_gt


def plot(kv_seqlens: list[int], cos_fp8_bf16: list[float], cos_fp8_gt: list[float], cos_bf16_gt: list[float]):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(12, 5))
    plt.plot(kv_seqlens, cos_fp8_bf16, linewidth=0.8, label="FA4 FP8 vs FA4 BF16")
    plt.plot(kv_seqlens, cos_fp8_gt, linewidth=0.8, label="FA4 FP8 vs SDPA FP32")
    plt.plot(kv_seqlens, cos_bf16_gt, linewidth=0.8, label="FA4 BF16 vs SDPA FP32")
    plt.xlabel("KV Sequence Length")
    plt.ylabel("Cosine Similarity")
    plt.title("FA4 Precision: Cosine Similarity vs KV Sequence Length")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("tests/fa4_fp8_cos_sim.png", dpi=150)
    plt.close()
    print("Plot saved to tests/fa4_fp8_cos_sim.png")


def main():
    kv_seqlens, cos_fp8_bf16, cos_fp8_gt, cos_bf16_gt = bench()
    plot(kv_seqlens, cos_fp8_bf16, cos_fp8_gt, cos_bf16_gt)

if __name__ == '__main__':
    main()
```

## Related

- PR #2109 (b65ae6b) — FP8 e4m3/e5m2 support by @dcw02 

cc @dcw02 

## 评论 (3)

### MatthewBonanni · 2026-07-22

Should be fixed by https://github.com/Dao-AILab/flash-attention/pull/2717, right? cc @Johnsonms 

### Johnsonms · 2026-07-23

Hi @MatthewBonanni , I will check it by end of this week. Thanks

### Johnsonms · 2026-07-25

Hi @drisspg Could you please help this? I am on leave
