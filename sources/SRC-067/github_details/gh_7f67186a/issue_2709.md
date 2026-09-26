# [Issue #2709] [Question] Split-KV paged attention block_table out-of-bounds risk in compute_attn_1rowblock_splitkv

source: https://github.com/Dao-AILab/flash-attention/issues/2709
state: closed | updated: 2026-07-16T17:40:07Z
labels: 

## 正文

### Question
In `compute_attn_1rowblock_splitkv`, the kernel accesses `block_table[block_table_idx_cur]` and `block_table[block_table_idx_next]` when advancing gK/gV pointer.

I want to confirm two points:
1. Is there any in-kernel runtime check to prevent `n_block * kBlockN >= binfo.actual_seqlen_k` before block_table lookup?
2. The iteration range is bounded by `n_block_min / n_block_max` calculated on host side. Does the code rely purely on loop bounds to guarantee all `n_block * kBlockN < actual_seqlen_k`, without inline bounds checking inside loop?

Additional concern:
Even if token position `n_block * kBlockN < actual_seqlen_k`, there is NO check whether `block_table_idx_cur` exceeds the allocated length of block_table buffer, which may cause out-of-bound global memory access if host does not allocate enough entries for block_table.

Relevant code snippet location:
`compute_attn_1rowblock_splitkv`, block_table branch inside the `if (n_block > n_block_min)` block.

Environment:
Commit: main branch
GPU: Hopper

## 评论 (2)

### Johnsonms · 2026-07-15

Thanks for your raising and detail, Will check it today

### Johnsonms · 2026-07-16

Thanks for the detailed report. I went through both the kernel and the host wrapper. Short answer: the behavior is correct and intentional — the block_table lookup is safe **by contract**, not by an in-kernel bounds check. 
**Q1 — Is there an in-kernel runtime check for `n_block * kBlockN >= actual_seqlen_k` before the block_table lookup?**

No per-iteration check. Safety is structural, established where the bounds are computed (`csrc/flash_attn/src/flash_fwd_kernel.h:532`):

```cpp
int n_block_max = std::min(cute::ceil_div(binfo.actual_seqlen_k, kBlockN),
                           (n_split_idx + 1) * n_blocks_per_split);
```

`ceil_div(actual_seqlen_k, kBlockN)` is the smallest block count covering `actual_seqlen_k`, so the largest index the loop touches is `n_block_max - 1`, giving `(n_block_max - 1) * kBlockN < actual_seqlen_k`. The loop only decrements, so **every** `n_block * kBlockN < actual_seqlen_k` holds by construction. The partial last block is handled by the `Is_even_MN` masking on the K/V *reads*, not by a guard on the block_table index.

**Q2 — Does correctness rely purely on the host-computed `n_block_min` / `n_block_max`, with no inline bounds check in the loop?**

Yes. There is no in-loop bounds check on `block_table_idx_cur` / `block_table_idx_next`. Correctness rests entirely on `n_block_min` / `n_block_max`, which are derived from `actual_seqlen_k`.

**On the "no check that `block_table_idx` is within the allocated buffer" concern:**

Correct, and this is by design (a caller contract). The host wrapper sizes the table and defines the KV coverage from it (`csrc/flash_attn/flash_api.cpp`):

- `block_table` shape is enforced as `[batch_size, max_num_blocks_per_seq]` (`CHECK_SHAPE`, line 620 / 1299).
- In the kvcache path, `seqlen_k = max_num_blocks_per_seq * page_block_size` (line 1268).

So as long as `actual_seqlen_k <= max_num_blocks_per_seq * page_block_size`:

```
max index accessed = (n_block_max - 1) * kBlockN / page_block_size
                   <  actual_seqlen_k / page_block_size
                   <= max_num_blocks_per_seq      -> in bounds
```

Alignment is fine too: `page_block_size % 256 == 0` and `kBlockN` is in {64, 128, 256} <= page_block_size, so a block start never straddles a page boundary mid-lookup.

**The one real gap:** the kernel does *not* validate `cache_seqlens[b]` against `max_num_blocks_per_seq * page_block_size`. If a caller passes a per-sequence `cache_seqlens` (or `seqused_k`) larger than what the block_table actually covers, `actual_seqlen_k` exceeds the table and you get exactly the OOB global read you describe. This is a **caller-contract violation**, not a kernel logic bug — but it is currently silent (no `TORCH_CHECK` guards it). If we want defense-in-depth, the cheap fix is a host-side `TORCH_CHECK` in `mha_fwd_kvcache` asserting `max(cache_seqlens) <= max_num_blocks_per_seq * page_block_size`, rather than an in-kernel per-iteration check (which would cost registers/branches on the hot path).
