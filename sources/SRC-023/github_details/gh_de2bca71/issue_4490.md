# [Issue #4490] mla_gluon: page table has no >2GB addressing fallback, and global_load fallbacks are unmasked

source: https://github.com/ROCm/aiter/issues/4490
state: open | updated: 2026-09-23T14:08:44Z
labels: 

## 正文

Two addressing-guard asymmetries in `aiter/ops/triton/gluon/mla_gluon.py`, found while
root-causing an unrelated fault (fixed in #4488). **Neither has a reproducer** — both are
latent on the configuration I have (Kimi-K3, 8x MI355X gfx950, TP8, bf16 KV) — so I am
reporting rather than patching. Line numbers are against `main` at the time of writing.

### 1. The page table has no >2 GB fallback, while the KV cache does

`within_2gb` is computed from `kv_c` alone:

```python
max_kv_bytes = kv_c.shape[0] * kv_c.stride(0) * kv_c.element_size()
within_2gb = max_kv_bytes <= 0x80000000
```

`WITHIN_2GB` then selects `buffer_load_to_shared` (32-bit offsets) vs
`global_load_to_shared` (64-bit) for the KV and PE loads. But `Req_to_tokens` — the page
table — is loaded with `buffer_load_to_shared` **unconditionally**, with no equivalent guard,
even though it can be large: in my configuration `flat_kv_indices` reaches 754,974,720 int32
= **3.02 GB**, and scales with `max_num_seqs * max_model_len`.

It is silent for me because the offsets actually used stay small (`batch_page_start <= 1728`),
so the large allocation is never indexed far into. It looks reachable once page-table offsets
grow.

### 2. The `global_load_to_shared` fallbacks pass no mask

Every `buffer_load_to_shared` call passes `mask=offs_n_* < split_kv_end`. All eight
`global_load_to_shared` fallbacks pass no mask at all. Since `within_2gb` is false for any KV
cache above 2 GB, the unmasked path is the one that runs in practice for large-cache
deployments.

One site carries a comment asserting the loop body is in-bounds by `num_iter` arithmetic,
which may well be true there; the prologue and epilogue sites handle potentially-partial
blocks.

I clamped the page index at all eight sites during the #4488 investigation and the fault I
was chasing persisted, so **this is not that bug** — it is an observation about the guard
asymmetry, and the masked/unmasked split may be deliberate for performance. Flagging it in
case it is not.


## 评论 (1)

### stefankoncarevic · 2026-09-23

## Reproducer for point 2 (unmasked `global_load_to_shared`)

The issue notes that neither finding has a reproducer. Here is one for the second
finding. It faults in about five seconds, needs only `aiter` and `torch`, and does not
involve vLLM.

```python
import sys
import torch
from aiter.ops.triton.gluon.mla_gluon import mla_gluon

BATCH, NHEAD, KV_LORA, QK_ROPE = 256, 8, 512, 64
KV_ROWS = int(sys.argv[1])          # cache rows
SEQ = int(sys.argv[2])              # KV entries per request

dev = "cuda"
q_nope = torch.randn(BATCH, NHEAD, KV_LORA, dtype=torch.bfloat16, device=dev)
q_pe = torch.randn(BATCH, NHEAD, QK_ROPE, dtype=torch.bfloat16, device=dev)
kv_c = torch.randn(KV_ROWS, KV_LORA + QK_ROPE, dtype=torch.bfloat16, device=dev)
o = torch.empty(BATCH, NHEAD, KV_LORA, dtype=torch.bfloat16, device=dev)

page_table = torch.arange(BATCH * SEQ, dtype=torch.int32, device=dev) % KV_ROWS
seq_info = torch.arange(0, (BATCH + 1) * SEQ, SEQ, dtype=torch.int32, device=dev)

mla_gluon(
    q_nope=q_nope, q_pe=q_pe, kv_c=kv_c, o=o,
    page_table=page_table, seq_info=seq_info,
    sm_scale=(KV_LORA + QK_ROPE) ** -0.5,
    k_pe=None, kv_pe_offset=KV_LORA,
    use_2d_view=False, kv_scale=1.0, min_kv_seq_len=1,
)
torch.cuda.synchronize()
print("no fault")
```

Run each case in its own process; the fault aborts the interpreter.

```bash
AMD_SERIALIZE_KERNEL=3 python repro.py 1864000 1   # 2.00 GiB -> no fault
AMD_SERIALIZE_KERNEL=3 python repro.py 1870000 1   # 2.01 GiB -> Memory access fault
```

## What measured

The switch is exactly the kernel's own `within_2gb` bound. Below it the masked
`buffer_load_to_shared` path runs and is clean; above it the unmasked
`global_load_to_shared` path runs and faults.

| KV cache | branch | result |
|---|---|---|
| 1,800,000 rows, 1.93 GiB | `buffer_load` | passes |
| 1,864,000 rows, 2.00 GiB | `buffer_load` | passes |
| 1,870,000 rows, 2.01 GiB | `global_load` | **memory access fault** |
| 3,500,000 rows, 3.75 GiB | `global_load` | **memory access fault** |

It is not limited to partial trailing tiles. With a 3.75 GiB cache it faults at every
per-request KV length we tried — 1, 64, 128, 129 and 256 — so both full and partial
`BLOCK_N` tiles are affected. The in-tree comment claiming the loop body is in-bounds by
`num_iter` arithmetic does not hold at these shapes.

Below 2 GiB the same shapes are clean, which rules out the shapes themselves. Small caches
appear to pass only because the stray address still lands in mapped memory.

## Environment

- AMD Instinct MI355X, `gfx950`
- `amd-aiter` 0.1.22.post1, which already contains #4474 (the int64 stride widening)

So #4474 fixed the stride overflow but not the missing bounds mask, and the two are
independent. Worth noting that #4488, which would have added regression coverage for the
>2 GB path, was closed without merging, so nothing currently guards this branch. On
today's `main` there are 8 `global_load_to_shared` call sites and none of them pass a
mask.

## Impact

This is not latent. Any decode with fewer than 16 heads per rank on gfx950 selects
`mla_gluon`, and any serving configuration with more than 2 GiB of KV cache per layer then
takes the unmasked path. We hit it with DeepSeek-Coder-V2-Lite at TP2 (8 heads per rank),
where it aborts the worker process during warm-up. The masked/unmasked split therefore
does not look deliberate — the unmasked path is not usable.
