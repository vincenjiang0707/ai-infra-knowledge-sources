# [Issue #2025] Triton FP4 dequantization has a truncated constant, disagreeing with CUDA/CPU by 7 ULP

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/2025
state: closed | updated: 2026-07-29T18:08:02Z
labels: Intel

## 正文

### System Info

Affects the Triton backend (`bitsandbytes/backends/triton/`), which is registered for XPU (Intel GPU) and used as the fallback when no native library is available. Reproducible by inspection; no specific hardware needed.

Verified on `main` at `1f4007e`. Also present at `f2233a6`.

### Reproduction

The bug is a single mistyped literal:

```python
# bitsandbytes/backends/triton/kernels_4bit.py:222, in dequantize_fp4_tree
tl.where(first_bit, 0.00520833, 0.0),  # 1001, 1000
```

That constant is the magnitude of the smallest nonzero FP4 level — 4-bit codes `0b0001` and `0b1001`. The intended value is `1/192` (`0.0625 / 12`: the FP4 subnormal `0.0625`, normalized by the format's absmax of 12). The literal has one significant digit too few, so it rounds to a different float32 than every other FP4 table in the repository.

| source                                                      | literal           | float32 value         | float32 bits |
| ----------------------------------------------------------- | ----------------- | --------------------- | ------------ |
| `backends/triton/kernels_4bit.py:222` `dequantize_fp4_tree` | `0.00520833`      | 0.005208330228924751  | `0x3BAAAAA4` |
| `csrc/kernels.cu:17` `fp4_dequantization_lut`               | `0.005208333333f` | 0.0052083334885537624 | `0x3BAAAAAB` |
| `csrc/gemm_4bit_common.cuh:39,47` `FP4_LUT_F32`             | `0.005208333333f` | 0.0052083334885537624 | `0x3BAAAAAB` |
| `csrc/cpu_ops.cpp:272,280-281` `fp4_lut` / AVX-512 LUT      | `0.005208333333f` | 0.0052083334885537624 | `0x3BAAAAAB` |
| `functional.py` `get_4bit_type("fp4")`                      | `0.0625 / 12`     | 0.0052083334885537624 | `0x3BAAAAAB` |
| exact                                                       | `1/192`           | 0.005208333333…       | `0x3BAAAAAB` |

Five places agree; only the Triton tree disagrees. The gap is 7 ULP in float32 — relative error 6.3e-7, about 5x float32 epsilon.

To confirm the two literals really are different floats (not a display artifact):

```python
import struct
for lit in (0.00520833, 0.005208333333, 0.0625 / 12):
    print(hex(struct.unpack("<I", struct.pack("<f", lit))[0]))
# 0x3baaaaa4
# 0x3baaaaab
# 0x3baaaaab
```

### Expected behavior

Dequantizing the same FP4 code should give the same value on every backend. Codes 1 and 9 should dequantize to `absmax * (1/192)` (rounded to float32), matching the CUDA kernel, the CPU kernel, the 4-bit GEMM LUT, and the Python code table.


## 评论 (1)

### matthewdouglas · 2026-07-29

Thanks for the report.

This LUT value does have the 7 ULP gap but considering that the output is then typically rounded to fp16/bf16, that difference is going to be absorbed.

I'm going to give this a low priority because the impact isn't significant, especially since it's just in the fallback path on XPU. With that said, it's worth fixing for consistency across the implementations. We already have a PR for this so I'll check that out.




