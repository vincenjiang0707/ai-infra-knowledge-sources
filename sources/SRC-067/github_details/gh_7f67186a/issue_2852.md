# [Issue #2852] FA4 SM103 backward preprocess predicate shape mismatch for padded head dimensions

source: https://github.com/Dao-AILab/flash-attention/issues/2852
state: open | updated: 2026-09-04T01:33:17Z
labels: 

## 正文

### Summary

On B300/SM103, FA4 beta27's backward preprocess reuses a predicate covering all per-thread row modes after slicing the O/dO source and destination tensors to a single row. CuTe rejects the resulting copy because the predicate has shape `(1,(2,3))` while the data expects `(1,(3))`.

The same `flash_bwd_preprocess.py` code is present in beta29 and current `main` (`4fd8d758c1fb7d93ef2e9a316ba4db1ab7fc05fe` as fetched on 2026-09-03).

### Environment

- NVIDIA B300 / SM103
- CUDA 13.2 base image
- PyTorch 2.10.0a0+3a035ad5.nv25.12
- Python 3.13
- `flash-attn-4==4.0.0b27`
- `nvidia-cutlass-dsl==4.6.2`
- BF16, varlen causal attention
- `CUTE_DSL_SHOW_STACKTRACE=1`

### Sanitized reproducer

```python
import torch
from flash_attn.cute import flash_attn_varlen_func

torch.manual_seed(42)
q = torch.randn(256, 16, 80, device="cuda", dtype=torch.bfloat16, requires_grad=True)
k = torch.randn(256, 4, 80, device="cuda", dtype=torch.bfloat16, requires_grad=True)
v = torch.randn(256, 4, 80, device="cuda", dtype=torch.bfloat16, requires_grad=True)
cu = torch.tensor([0, 256], device="cuda", dtype=torch.int32)
result = flash_attn_varlen_func(
    q,
    k,
    v,
    cu_seqlens_q=cu,
    cu_seqlens_k=cu,
    max_seqlen_q=256,
    max_seqlen_k=256,
    causal=True,
)
out = result[0] if isinstance(result, tuple) else result
out.float().square().mean().backward()
```

Backward-preprocess compile key:

```text
dtype=BFloat16, head_dim=80, head_dim_v=80, m_block_size=128,
has_cuseqlens_q=True, has_seqused_q=False, has_dlse=False,
has_dq_accum=True, has_scale_p=False, use_padded_offsets=True,
nheads_major=False, pack_gqa=False, qhead_per_kvhead=1,
nheads_kv=1, has_cu_total_m_blocks=False
```

Compiler diagnostic:

```text
error: unknown: 'cute.copy' op expects pred to have compatible shape with: (1,(3)) but got actual predShape: (1,(2,3))
note: unknown: see current operation: "cute.copy"(...) :
  (!cute_nvgpu.atom.universal_copy<bf16, 128 b>,
   !cute.memref<bf16, gmem, align<16>, "((8,1),(3)):((1,0),(32))">,
   !cute.memref<bf16, rmem, align<16>, "((8,1),(3)):((1,0),(8))">,
   !cute.memref<i8, rmem, align<32>, "(1,(2,3)):(3,(0,1))">) -> ()
```

### Source mapping and proposed correction

`flash_attn/cute/flash_bwd_preprocess.py` constructs `tOpO` from unsliced `tOcO`, then captures it in a `partial`. Inside the `m` loop it slices both data tensors with `[None, m, None]` but does not slice the predicate.

Slicing the predicate over the same row mode makes the preprocess compile and run:

```diff
-copy = partial(copy_utils.copy, pred=tOpO)
 ...
-copy(tOgO[None, m, None], tOrO[None, m, None])
-copy(tOgdO[None, m, None], tOrdO[None, m, None])
+row_predicate = tOpO[None, m, None] if const_expr(tOpO is not None) else None
+copy_utils.copy(tOgO[None, m, None], tOrO[None, m, None], pred=row_predicate)
+copy_utils.copy(tOgdO[None, m, None], tOrdO[None, m, None], pred=row_predicate)
```

This report is limited to the backward-preprocess predicate mismatch; the reproducer may encounter other constraints later in the general SM100 backward kernel once preprocess is repaired.


## 评论 (1)

### MarkIsDoingIt · 2026-09-04

Correction from the instrumented real workload: the production failure is not an 80-wide LM head. The actual failing `_bwd_preprocess` specialization on B300 is:

```text
dtype=BFloat16, head_dim=72, head_dim_v=72, m_block_size=128,
has_cuseqlens_q=True, has_seqused_q=False, has_dlse=False,
has_dq_accum=True, has_scale_p=False, use_padded_offsets=True,
nheads_major=False, pack_gqa=False, qhead_per_kvhead=1,
nheads_kv=1, has_cu_total_m_blocks=False
```

The same run first compiled the language-model specialization at `head_dim=head_dim_v=256`, then failed on a deliberately executed 16-token dummy vision-tower forward used by VeRL for text-only Qwen3.5 batches. The 72-wide tensor at the Transformers FA4 boundary was `q=k=v=(1,16,16,72)`; at the varlen API it was `(16,16,72)`. The checkpoint LM path was separately measured as Q `(1,16,S,256)`, K/V `(1,4,S,256)`, matching the `hd256` kernel names.

Thus the 80-wide reproducer in the original report is synthetic and demonstrates the same non-32-aligned predicate defect, but 80 was never observed in the model. The real trigger is Qwen3.5 vision `head_dim=72`, padded internally to 96. The source mapping and proposed same-row predicate slice remain unchanged.
