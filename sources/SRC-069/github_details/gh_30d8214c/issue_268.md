# [Issue #268] m_grouped_fp8_gemm_nt_masked get incorrect result when m < 64 in H20

source: https://github.com/deepseek-ai/DeepGEMM/issues/268
state: closed | updated: 2026-01-04T02:22:57Z
labels: 

## 正文

### Environment
```
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.54.14              Driver Version: 550.54.14      CUDA Version: 12.6     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA H20                     On  |   00000000:08:00.0 Off |                    0 |
| N/A   31C    P0             72W /  500W |       3MiB /  97871MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+

```
### Question
When max_m < 64 (ie: 8,16,32), below tests assert error, but it's ok when max_m > 64.
Since readme not mention this, so I just wonder it's bug or feature?
Using below script can reproduce it. 
Hoping for reply, thanks.
### Script
``` python
import enum
import torch
import deep_gemm

from deep_gemm.testing import calc_diff

from deep_gemm.utils import (
    ceil_div,
    per_token_cast_to_fp8, per_block_cast_to_fp8,
)


class KernelType(enum.Enum):
    # For SM100 GEMMs
    Kernel1D1D = 0
    Kernel1D2D = 1
    KernelNoSF = 2

    def is_1d1d(self):
        return self.value == 0

    def is_1d2d(self):
        return self.value == 1

    def is_nosf(self):
        return self.value == 2


def generate_m_grouped_masked(num_groups: int, max_m: int, expected_m_per_group: int, n: int, k: int,
                              use_ue8m0: bool = False, use_bf16: bool = False):
    a = torch.randn((num_groups, max_m, k), device='cuda', dtype=torch.bfloat16)
    b = torch.randn((num_groups, n, k), device='cuda', dtype=torch.bfloat16)
    d = torch.empty((num_groups, max_m, n), device='cuda', dtype=torch.bfloat16)
    ref_d = torch.einsum('gmk,gnk->gmn', a, b)

    masked_m = torch.empty((num_groups, ), device='cuda', dtype=torch.int)
    for j in range(num_groups):
        masked_m[j] = int(expected_m_per_group)
    assert masked_m.amax().item() <= max_m

    if use_bf16:
        return a, b, masked_m, d, ref_d

    a_fp8 = (torch.empty_like(a, dtype=torch.float8_e4m3fn), torch.empty((num_groups, max_m, ceil_div(k, 128)), device='cuda', dtype=torch.float))
    b_fp8 = (torch.empty_like(b, dtype=torch.float8_e4m3fn), torch.empty((num_groups, ceil_div(n, 128), ceil_div(k, 128)), device='cuda', dtype=torch.float))
    for i in range(num_groups):
        a_fp8[0][i], a_fp8[1][i] = per_token_cast_to_fp8(a[i], use_ue8m0=use_ue8m0)
        b_fp8[0][i], b_fp8[1][i] = per_block_cast_to_fp8(b[i], use_ue8m0=use_ue8m0)

    return a_fp8, b_fp8, masked_m, d, ref_d

if __name__ == "__main__":
    max_m = 32
    kernel_type = KernelType.Kernel1D2D
    num_groups = 64
    n = 1536 
    k = 2048
    expected_m_per_group = max_m // 2
    use_ue8m0 = False
    kernel_opt = f'1D1D' if kernel_type.is_1d1d() else '1D2D'
    disable_ue8m0_cast = not use_ue8m0
    a, b, masked_m, d, ref_d = generate_m_grouped_masked(num_groups, max_m, expected_m_per_group, n, k, use_ue8m0=use_ue8m0)
    for i in range(10):        
        deep_gemm.m_grouped_fp8_gemm_nt_masked(a, b, d, masked_m, expected_m_per_group, disable_ue8m0_cast=disable_ue8m0_cast)
        for j in range(num_groups):
            diff = calc_diff(d[j, :masked_m[j].item()], ref_d[j, :masked_m[j].item()])
            assert diff < 0.001, f'{max_m=}, {n=}, {k=}, {j=}, masked_m={masked_m[j]}, {kernel_opt}, {num_groups=}, {diff:.5f}'
```
### Result
```
Warning: please use at least NVCC 12.9 for the best DeepGEMM performance
Traceback (most recent call last):
  File "/data2/baowending.bwd/DeepGEMM/tests/test_unstable.py", line 26, in <module>
    assert diff < 0.001, f'{max_m=}, {n=}, {k=}, {j=}, masked_m={masked_m[j]}, {kernel_opt}, {num_groups=}, {diff:.5f}'
AssertionError: max_m=32, n=1536, k=2048, j=1, masked_m=16, 1D2D, num_groups=64, 0.22588
```

## 评论 (3)

### yurekami · 2026-01-01

Thanks for the detailed bug report with a reproducer!

I investigated the code and found a potential root cause. In `sm90_m_grouped_fp8_gemm_masked_1d2d()`:

```cpp
const auto& config = get_best_config<SM90ArchSpec>(
    GemmType::MGroupedMasked, KernelType::Kernel1D2D,
    expected_m, n, k, ...  // Uses expected_m for config selection
);
```

The config is selected based on `expected_m` (16 in your test), while TMA descriptors use `m` (max_m = 32):

```cpp
const auto& tensor_map_a = make_tma_a_desc(major_a, a, m, k, ...);  // Uses max_m
```

In `get_block_m_candidates()`, for Kernel1D2D with `m <= 16`:
```cpp
if (m <= 16) candidates.push_back(16);
if (m <= 32) candidates.push_back(32);
```

When `expected_m = 16`, `block_m = 16` becomes a candidate, but the actual tensor has `max_m = 32` rows. This mismatch between config selection (expected_m) and actual data dimensions (max_m) when max_m < 64 may cause alignment/boundary issues in the kernel.

**Potential fixes:**
1. Pass `max_m` instead of `expected_m` to `get_best_config` for masked GEMM
2. Add a constraint that `block_m <= max_m` (not just `expected_m`)
3. Document the limitation that `max_m >= 64` is required for masked GEMM

The 22.6% error suggests incorrect indexing or boundary handling when the block size exceeds or misaligns with the actual data dimensions.

I don't have a full fix yet as this requires deeper kernel-level investigation, but wanted to share these findings.

### alibaba-miji · 2026-01-04

Thanks for reply and explain! We temporary limit max_m >= 64 to avoid this problem, hoping to get it fixed in repo

### alibaba-miji · 2026-01-04

By the way, the problem still exists when `expected_m == max_m == 16 / 32`, so I think the real problem may still related to max_m
