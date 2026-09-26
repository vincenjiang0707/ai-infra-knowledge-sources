# [Issue #2747] [QST] [CuTeDSL] Kernel Launch Failure due to requesting too much SMEM

source: https://github.com/NVIDIA/cutlass/issues/2747
state: closed | updated: 2026-09-05T17:12:28Z
labels: question, ? - Needs Triage, inactive-30d, inactive-90d

## 正文

**What is your question?**

I've observed that when we use automatic SMEM calculation and request too much SMEM, the kernel launch may fail without triggering an error. Is there a way to guard against this? The CUDA Check function is available [here](https://github.com/NVIDIA/cutlass/blob/8afb19d9047afc26816a046059afe66763e68aa5/python/CuTeDSL/cutlass/base_dsl/runtime/cuda.py#L283), but I'm unsure what result should be passed in here.

```python
import cutlass.cute as cute
import cutlass
import torch
# Initialize CUDA context
torch.rand(1, device="cuda")

@cute.kernel
def kernel():
    """
    Example kernel that allocates shared memory.
    The total allocation will be automatically calculated when smem=None.
    """
    allocator = cutlass.utils.SmemAllocator()
    raw_buffer = allocator.allocate(512000000, byte_alignment=64)
    return


# Compile the example
@cute.jit
def launch_kernel():
    k = kernel()
    k.launch(
        grid=(1, 1, 1),
        block=(1, 1, 1),
    )
    print(f"Kernel recorded internal smem usage: {k.smem_usage()}")

fn = cute.compile(launch_kernel)
fn()
```

## 评论 (2)

### github-actions[bot] · 2025-12-04

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-03-04

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.
