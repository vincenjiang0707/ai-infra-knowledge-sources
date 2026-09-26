# [Issue #313] [Question] Is there a simpler implementation for the UTCCP transposer?

source: https://github.com/deepseek-ai/DeepGEMM/issues/313
state: closed | updated: 2026-04-27T05:45:42Z
labels: 

## 正文

# [Question] Is there a simpler implementation for the UTCCP transposer?

Hi, I was reading the UTCCP transposer warp logic in `utccp_required_smem_warp_transpose` and noticed that it uses a very clever XOR-based coordinate remapping to avoid shared-memory bank conflicts during the transpose.

From what I understand, the underlying problem here is essentially a shared-memory transpose of `uint32[4][32] -> uint32[32][4]`. The current implementation seems to solve the bank-conflict issue by permuting the per-lane scalar load/store order.

For this specific `4x32 -> 32x4` case, I was wondering whether a simpler approach could also work: keep the loads scalar, then perform a single vector store per lane.

For example, something like:

```cpp
uint32_t values[4];

#pragma unroll
for (int i = 0; i < 4; ++i) {
    values[i] = ld_shared(smem_ptr + i * 32 + lane_idx);
}

__syncwarp();

// each lane writes one contiguous 16B row in the transposed 32x4 layout
st_shared(smem_ptr + lane_idx * 4, values[0], values[1], values[2], values[3]);
```

My understanding is that:

- the scalar loads from `smem_ptr + i * 32 + lane_idx` are already conflict-free
- the main conflict comes from the scalar stores in the transposed layout
- using one 16B vector store per lane might also avoid bank conflicts, while making the transpose logic a bit simpler

Does the current XOR-based transpose have advantages over a scalar-load + vector-store approach that I may be missing?

## 评论 (0)
