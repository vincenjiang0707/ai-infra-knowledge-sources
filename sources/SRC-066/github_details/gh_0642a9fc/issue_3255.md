# [Issue #3255] [BUG] Segmentation fault occurred when indexing the tensor.

source: https://github.com/NVIDIA/cutlass/issues/3255
state: open | updated: 2026-09-17T11:13:30Z
labels: bug, ? - Needs Triage, inactive-30d, inactive-90d, CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

**Describe the bug**
When executing the following code, a segmentation fault occurs. However, if we make the layout static (i.e., do not call `mark_layout_dynamic`), the issue does not appear.

**Steps/Code to reproduce bug**
```
import torch
import cutlass
import cutlass.cute as cute
import cutlass.utils.hopper_helpers as sm90_utils
import cutlass.utils as utils
from cutlass.cute.runtime import from_dlpack

@cute.jit
def layout_demo(tensor: cute.Tensor, m: cutlass.Int32, n: cutlass.Int32):
    swizzle_mode = sm90_utils.get_smem_layout_atom(
      utils.LayoutEnum.ROW_MAJOR,
      cutlass.Float16,
      64
    )
    print("CuTeDSL DEBUG swizzle_mode", swizzle_mode)
    shared_memory_layout_atom = sm90_utils.make_smem_layout_atom(
      swizzle_mode,
      cutlass.Float16
    )
    print("CuTeDSL DEBUG shared_memory_layout_atom", shared_memory_layout_atom)

    shared_memory_layout = cute.tile_to_shape(shared_memory_layout_atom, (128, 64), order=(0, 1))
    print("CuTeDSL DEBUG shared_memory_layout", shared_memory_layout)

    swizzled_matrix_layout = cute.tile_to_shape(shared_memory_layout, tensor.shape, order=(0, 1))
    print("CuTeDSL DEBUG swizzled_matrix_layout", swizzled_matrix_layout)

    swizzled_matrix_tensor = cute.make_tensor(tensor.iterator, swizzled_matrix_layout)
    print("CuTeDSL DEBUG swizzled_matrix_tensor", swizzled_matrix_tensor)

    target_tile = swizzled_matrix_tensor[((None, m), (None, n))]
    print("CuTeDSL DEBUG target_tile", target_tile)

if __name__ == '__main__':
    matrix = torch.randn((4096, 4096), dtype=torch.float16, device="cuda")
    cute_matrix = from_dlpack(matrix, assumed_align=16).mark_layout_dynamic()
    layout_demo(cute_matrix, 13, 27)
```

**Expected behavior**
```
CuTeDSL DEBUG swizzle_mode SmemLayoutAtomKind.K_SW128
CuTeDSL DEBUG shared_memory_layout_atom S<3,4,3> o 0 o (8,64):(64,1)
CuTeDSL DEBUG shared_memory_layout S<3,4,3> o 0 o ((8,16),(64,1)):((64,512),(1,0))
CuTeDSL DEBUG swizzled_matrix_layout S<3,4,3> o 0 o (((8,16),?),((64,1),?)):(((64,512),8192),((1,0),?{div=8192}))
CuTeDSL DEBUG swizzled_matrix_tensor tensor<ptr<f16, gmem, align<16>> o S<3,4,3> o 0 o (((8,16),?),((64,1),?)):(((64,512),8192),((1,0),?{div=8192}))>
error: expects no error(`x`) in layout, but got "x:x o 0 o x:x"
Segmentation fault (core dumped)
```

**Environment details (please complete the following information):**
 - nvidia-cutlass-dsl 4.5.1
 - nvidia-cutlass-dsl-libs-base 4.5.1
 - nvidia-cutlass-dsl-libs-cu13 4.5.1

**Additional context**
None.


## 评论 (2)

### github-actions[bot] · 2026-06-19

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-09-17

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.
