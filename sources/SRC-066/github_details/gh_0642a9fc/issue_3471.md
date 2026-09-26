# [Issue #3471] [BUG] [CuTeDSL] cute.right_inverse refuses layouts with dynamic sizes

source: https://github.com/NVIDIA/cutlass/issues/3471
state: open | updated: 2026-09-04T12:51:57Z
labels: bug, ? - Needs Triage, CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

**Describe the bug**
Invoking cute.right_inverse with a dynamic layout raises an exception that states that the function outright refuses to deal with dynamic layouts. I don't see a fundamental issue with that, and with the specific arguments I used there should be a well-defined result.

**Steps/Code to reproduce bug**
```py
import torch
import cutlass.cute as cute
from cutlass.cute.runtime import from_dlpack


@cute.jit
def repro(tensor: cute.Tensor):
    layout = cute.make_layout(
        (16, tensor.shape[1]),
        stride=(1, 16),
    )
    expected = cute.make_layout(16 * tensor.shape[1], stride=1)

    print("layout:          ", layout)
    print("expected inverse:", expected)
    print("actual inverse:  ", cute.right_inverse(layout))

tensor = from_dlpack(torch.empty((4096, 8192), device="cuda"))
tensor = tensor.mark_compact_shape_dynamic(mode=1)
repro(tensor)
```

**Environment details (please complete the following information):**
CuTeDSL version 4.7.0


## 评论 (2)

### ccecka · 2026-08-17

This does appear to be a bug in CuTeDSL.

It functions in PyCuTe
```
>>> from pycute import *
>>> import sympy
>>> N = sympy.symbols("N", positive=True, integer=True)
>>> right_inverse(Layout((16,N), (1,16)))
Layout((16, N), (1, 16))
```

### kzos · 2026-09-04

@ccecka I opened #3582 for this. It supports the dynamic-shape/static-integer-stride case and includes compiler plus cutegen coverage. For the reproducer it returns PyCuTe’s equivalent uncoalesced `(16,N):(1,16)`; canonical `16*N:1` remains under #3469. The pinned CPU suites pass (236 CuTe IR tests and 220 cutegen tests).
