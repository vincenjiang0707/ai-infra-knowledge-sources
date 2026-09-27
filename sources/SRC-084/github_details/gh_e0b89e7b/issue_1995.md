# [Issue #1995] quantize_blockwise / dequantize_blockwise produce incorrect results for non-contiguous CPU inputs (CPU follow-up to #1690)

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1995
state: closed | updated: 2026-07-09T19:58:00Z
labels: x64 CPU, aarch64

## 正文

**Follow-up to #1690 / #1342 — the CPU backend was not covered by the fix.**

Those issues were closed by #1859, which added `A = A.contiguous()` to the **CUDA** kernels only. The **CPU backend still exhibits the silent-corruption bug** exactly as described in #1690: `quantize_blockwise` / `dequantize_blockwise` return wrong results for non-contiguous inputs instead of either handling them or raising. The MPS backend is unaffected (it copies via `reshape`).

### System Info

```
bitsandbytes: 0.50.0.dev0 (current main)
torch:        2.12.1
python:       3.12.13
platform:     macOS-26.0-arm64 (Apple Silicon) — CPU backend
```

The affected code is the platform-independent CPU backend, so this is expected to reproduce on any CPU host (Linux/Windows), not just macOS.

### Reproduction

```python
import torch
import bitsandbytes.functional as F

# A non-contiguous tensor produced by a strided slice
A_full = torch.randn(64, 128)
A_noncontig = A_full[::2, :]          # non-contiguous view
A_contig = A_noncontig.contiguous()   # identical values, contiguous layout
assert not A_noncontig.is_contiguous()

qn, sn = F.quantize_blockwise(A_noncontig, blocksize=64)
qc, sc = F.quantize_blockwise(A_contig,   blocksize=64)

print("quantized codes identical:", torch.equal(qn, qc))                 # False
print("absmax identical:         ", torch.equal(sn.absmax, sc.absmax))   # False
print("max |code difference|:    ", (qn.int() - qc.int()).abs().max().item())  # 248
```

Output:

```
quantized codes identical: False
absmax identical:          False
max |code difference|:     248
```

Both calls quantize mathematically identical data, yet produce completely different results — the non-contiguous call reads the underlying buffer in physical order rather than logical order, and no error is raised.

Verified across `fp16` / `bf16` / `fp32` × blocksize `64` / `128` / `256`, for both `quantize_blockwise` and `dequantize_blockwise` (18/18 combinations fail). This is the same bug class as #1342 / #1690, now isolated to the CPU backend.

### Expected behavior

Quantizing/dequantizing a non-contiguous tensor on CPU should give identical results to its `.contiguous()` equivalent — matching the CUDA backend's behavior after #1859.

---

I'd be happy to open a PR for the CPU fix. One question on the preferred approach, since #1690 raised both: should the CPU kernels **auto-convert** with `A = A.contiguous()` (matching the CUDA fix in #1859), or **raise** on non-contiguous input? I'll follow whichever you prefer, and include regression tests (extending `TestNonContiguousInputs` to CPU).


## 评论 (1)

### matthewdouglas · 2026-07-09

Hi,

I think it would be reasonable to do what we're doing on the CUDA backend and use `A.contiguous()` here. Thanks!
