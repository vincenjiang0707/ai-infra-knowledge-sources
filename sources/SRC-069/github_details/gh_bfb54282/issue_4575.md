# [Issue #4575] [Feature] Fuse LSE correction into DCP A2A

source: https://github.com/flashinfer-ai/flashinfer/issues/4575
state: closed | updated: 2026-09-21T18:34:37Z
labels: priority: must have (P0), op: comm

## 正文

## Motivation

SGLang uses FlashInfer's MNNVL DCP A2A operator to exchange partial attention outputs and LSE values across context-parallel ranks. The current API returns the peer-stacked tensors, after which SGLang launches a separate kernel to apply the LSE correction:

```python
recv_o, recv_stats = decode_cp_a2a_alltoall(
    partial_o,
    softmax_stats,
    workspace,
    cp_rank,
    cp_size,
)
output = lse_reduce(recv_o, recv_stats[..., 0])
```

Could FlashInfer provide a fused A2A + LSE-reduction operation that directly returns the corrected attention output?

## Proposed Interface

```python
output = decode_cp_a2a_lse_reduce(
    partial_o,            # [..., cp_size, head_dim], fp16/bf16
    partial_lse,          # [..., cp_size], fp32
    workspace,
    cp_rank,
    cp_size,
    is_lse_base_on_e=False,
    enable_pdl=None,
)
```

## Expected behavior

- Perform the same MNNVL exchange as `decode_cp_a2a_alltoall`.
- Apply the exact LSE-weighted reduction over contributions from all CP ranks.
- Return `output` with shape `[..., head_dim]`, with the CP dimension removed.
- Support both base-2 LSE, used by FlashInfer MLA, and natural-log LSE.
- Remain compatible with CUDA graph capture and replay.
- Ideally avoid materializing peer-stacked receive tensors and launching a separate correction kernel.

For inputs shaped as follows:

```text
partial_o:   [batch, local_heads, cp_size, head_dim]
partial_lse: [batch, local_heads, cp_size]
```

the result should have shape:

```text
output:      [batch, local_heads, head_dim]
```

## Reference validation

The fused result should match the current A2A followed by an explicit LSE reduction:

```python
softmax_stats = torch.zeros(
    *partial_lse.shape, 2, dtype=torch.float32, device=partial_lse.device
)
softmax_stats[..., 0] = partial_lse

recv_o, recv_stats = decode_cp_a2a_alltoall(
    partial_o,
    softmax_stats,
    workspace,
    cp_rank,
    cp_size,
)

recv_lse = recv_stats[..., 0]
lse_max = recv_lse.max(dim=-1, keepdim=True).values
weights = (
    torch.exp(recv_lse - lse_max)
    if is_lse_base_on_e
    else torch.exp2(recv_lse - lse_max)
)
expected = (
    (recv_o.float() * weights.unsqueeze(-1)).sum(dim=-2)
    / weights.sum(dim=-1, keepdim=True)
).to(partial_o.dtype)

actual = decode_cp_a2a_lse_reduce(
    partial_o,
    partial_lse,
    workspace,
    cp_rank,
    cp_size,
    is_lse_base_on_e=is_lse_base_on_e,
)

torch.testing.assert_close(actual, expected, rtol=1e-2, atol=1e-3)
```


## 评论 (5)

### kwen2501 · 2026-08-19

@aleozlx we have a prototype, can you please sign me up for this issue? Thank you!

### aleozlx · 2026-08-19

@kmrao-nv i'm guessing this should get a P0 label?

### aleozlx · 2026-08-19

@kwen2501 lmk if you have a rough time line . thanks for help!

### kwen2501 · 2026-08-29

@aleozlx I am converting my PoC to be closer to the API surface asked here. 
ETA: Sept 1. Thanks for the patience!

### kwen2501 · 2026-09-06

Implemented in #4929: `decode_cp_a2a_lse_reduce` now provides the NCCL-LSA fused decode context-parallel A2A plus LSE-weighted reduction op, with eager and CUDA Graph support.

Four-rank BF16 benchmark (max-rank median):

| Shape | Fused eager | Fused + graph* | Legacy A2A + merge | Speedup |
|---|---:|---:|---:|---:|
| batch 1, heads 2, dim 64 | 12.14 µs | 10.15 µs | 178.91 µs | 14.7× |
| batch 1, heads 8, dim 128 | 15.04 µs | 13.24 µs | 179.22 µs | 11.9× |
| batch 4, heads 8, dim 128 | 18.04 µs | 16.40 µs | 178.73 µs | 9.9× |
| batch 16, heads 8, dim 128 | 18.96 µs | 17.02 µs | 180.88 µs | 9.5× |

*Groups 50 operations into one graph; values are per-operation averages.

