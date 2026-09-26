# [Issue #2067] quantize_4bit fails with "invalid configuration argument" (ops.cu:54) for tensors of exactly >= 2^31 elements

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/2067
state: open | updated: 2026-09-03T18:18:20Z
labels: 

## 正文


**Versions:** bitsandbytes 0.49.1, torch 2.11.0+cu128, CUDA 12.8, NVIDIA H200 (141 GB).

**Repro (isolated, one process per size, fp32 flattened input, compress_statistics=True — mirroring axolotl 0.18's `_simulate_nf4_roundtrip` call):**
```
n = 2**31 - 65536   -> OK
n = 2**31           -> Error invalid configuration argument at line 54 in file /src/csrc/ops.cu
n = 2**31 + 65536   -> same failure
```
A clean int32 boundary in `quantize_4bit`'s kernel-launch arithmetic.

**Real-world trigger:** axolotl 0.18's merge CLI enables NF4 round-trip simulation for every 4-bit config; any model carrying a >= 2^31-element tensor (e.g. google/gemma-4-E4B-it's embedding) cannot merge. Smaller-vocab models (Mistral-7B, Qwen3.5-4B) pass, which hides the boundary.

**Expected:** chunked launch or int64 indexing above 2^31 elements, or a clear size-limit error.


## 评论 (1)

### matthewdouglas · 2026-09-03

This looks like #1785. For what it's worth, in this particular use case, it's probably not the best idea to quantize the embedding in NF4.
