# [Issue #5044] [Bug] HIP RMSNorm corrupts row-boundary elements for odd hidden sizes

source: https://github.com/ROCm/aiter/issues/5044
state: open | updated: 2026-09-05T05:37:55Z
labels: 

## 正文

### Problem Description

`aiter.rms_norm` produces incorrect results for odd FP16 hidden sizes on MI308X.

An adjacent aligned shape (`hidden_size=768`) passes, while
`hidden_size=769` corrupts column 0 of several following rows.

The failing path loads `module_rmsnorm_quant`, suggesting an unhandled
vectorized tail in the HIP RMSNorm fast path. The OPUS RMSNorm path and the
previous AITER implementation produce correct results for the same shape.





### Operating System

Linux

### CPU

Intel Xeon Platinum 8575C

### GPU

AMD MI308X

### ROCm Version

ROCm7.2.0

### ROCm Component

_No response_

### Steps to Reproduce

## Minimal Reproduction

```python
import importlib.metadata

import aiter
import torch
import torch.nn.functional as F


def run_case(hidden_size: int) -> None:
    torch.manual_seed(0)
    x = torch.randn(7, hidden_size, device="cuda", dtype=torch.float16)
    weight = torch.randn(hidden_size, device="cuda", dtype=torch.float16)

    expected = F.rms_norm(x, (hidden_size,), weight, eps=1e-6)
    actual = aiter.rms_norm(x, weight, 1e-6)
    torch.cuda.synchronize()

    close = torch.isclose(actual, expected, rtol=5e-2, atol=5e-2)
    mismatch = torch.nonzero(~close, as_tuple=False)
    max_abs_diff = (actual - expected).abs().max().item()

    print(
        f"hidden_size={hidden_size}: "
        f"mismatches={mismatch.tolist()}, max_abs_diff={max_abs_diff:.6f}"
    )
    torch.testing.assert_close(actual, expected, rtol=5e-2, atol=5e-2)


if __name__ == "__main__":
    print(f"AITER: {importlib.metadata.version('aiter')}")
    print(f"PyTorch: {torch.__version__}, ROCm: {torch.version.hip}")

    run_case(768)  # Aligned control: passes
    run_case(769)  # Odd hidden size: fails
```

## Observed Result

```text
AITER: 0.1.21.dev80+g987203ba5.d20260825
PyTorch: 2.9.1+git7e1940d, ROCm: 7.2.26015-fc0010cf6a

hidden_size=768: mismatches=[], max_abs_diff=0.000977
hidden_size=769: mismatches=[[1, 0], [3, 0], [5, 0]], max_abs_diff=0.511719

AssertionError: Tensor-likes are not close!
Mismatched elements: 3 / 5383
Greatest absolute difference: 0.51171875
```

## Expected Result

Both aligned and odd hidden sizes should match the PyTorch RMSNorm reference.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

<details>
<summary>rocminfo --support output</summary>

```
Paste output here
```

</details>


### Additional Information

_No response_

## 评论 (1)

### rk9595 · 2026-09-05

I traced this in the source and I think the mechanism is a buffer-bound rounding, not a vectorized-tail bug in the fast path itself.

`add_rmsnorm_quant_kernel` (`csrc/kernels/rmsnorm_quant_kernels.cu`) bounds its gmem descriptors at `n` rounded **up** to a 4-byte multiple:

```cpp
static constexpr int32_t ooba_i = 4 / sizeof(DTYPE_I);   // 2 for fp16/bf16
const int oob_i = (n + ooba_i - 1) / ooba_i * ooba_i;    // n=769 -> 770
auto buffer_i      = opus::make_gmem<DTYPE_I>(input_ptr, oob_i * sizeof(DTYPE_I));
auto weight_buffer = opus::make_gmem<DTYPE_I>(weight,    oob_i * sizeof(DTYPE_I));
const int oob_o = is_fp4 ? (n + 1) / 2 : (n + ooba_o - 1) / ooba_o * ooba_o;
```

For `n = 769` fp16 that window is 770 elements, so column 769 — which is column 0 of the *next* row, since the rows are contiguous — is inside the bound for both the loads and the stores. Two consequences:

1. The next row's first element is squared into the sum of squares, biasing the variance of every row.
2. Every block also *writes* a normalized value into the next row's column 0 (scaled by `weight[769]`, itself one element past the weight tensor). The block that legitimately owns that row writes the correct value too, and whichever store lands last wins. That race is why the corruption appears on rows 1, 3, 5 rather than on all of them, and why an aligned `hidden_size=768` is clean.

This looks like the same class as #4467, which fixed exactly this rounding for the packed FP4 output but left the 2-byte and 1-byte cases. By the same reading it should also affect `rmsnorm_quant` / `add_rmsnorm_quant` with fp8 or int8 output whenever `n % 4 != 0` (there `ooba_o` is 4, so up to 3 bytes of the next row are clobbered), and `residual_out` in the fused-add path. The existing tests never sweep an unaligned `n` — `test_rmsnorm2d.py` uses `[4096, 8192, 16384, 32768, 65536]` and `test_rmsnorm2dFusedAddQuant.py` `[1024, 2048, 3584, 4096, 8192]` — which is presumably why it has survived in tree.

I'd like to take this. The fix I have in mind is to bound the descriptors at the exact row byte length and mask the register tail after each load, so correctness doesn't depend on whether the hardware range check drops a partial dword or just the out-of-range bytes; I'll probe that on the device first and add a scalar tail path for the last element only if it turns out to be needed. Plus guard-row regression tests for unaligned `n` across the plain, fused-add, and fp8/int8 quant entry points, following the guard pattern #4467 introduced.

I'll verify on gfx942 (both the repro above and a before/after perf check on the aligned shapes, since this touches the hot path). Let me know if you'd rather handle it internally or if you'd prefer a different shape for the fix.

