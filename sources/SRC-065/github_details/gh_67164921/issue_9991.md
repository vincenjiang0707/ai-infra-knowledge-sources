# [Issue #9991] tl.store(i1, i32) implicitly casts int32 as int8 lead unexpected behavior

source: https://github.com/triton-lang/triton/issues/9991
state: closed | updated: 2026-09-18T23:05:19Z
labels: bug

## 正文

### Describe the bug

+ Description: There is a discrepancy between the Triton documentation and the actual compiler behavior regarding the data type precision for triton.languange.sum.

According to the [official documentation](https://triton-lang.org/main/python-api/generated/triton.language.sum.html#triton.language.sum), this operation is supposed to handle/process data as int32. However, upon testing the runtime behavior, it appears the compiler is actually lowering the bool as `tl.int8` as shown in https://github.com/triton-lang/triton/blob/main/python/triton/language/semantic.py#L1029.

+ Expected Behavior: The summation of bool type in triton is equivalent as `torch.sum(x, dtype=torch.bool)`

+ Actual Behavior: The summation of boolean Tensor with 256 `True` return `False`

```python
import triton
import triton.language as tl
import time
import numpy as np

import torch
import numpy as np

@triton.jit
def triton_sum_2D_dim0_dim1(in_ptr0, out_ptr0, L: tl.constexpr, M: tl.constexpr):
    lblk_idx = tl.arange(0, L)
    mblk_idx = tl.arange(0, M)
    idx = mblk_idx[None, :] + lblk_idx[:, None] * M
    x = tl.load(in_ptr0 + idx)
    ret = tl.sum(x, 1)
    ret = tl.sum(ret, 0)
    tl.store(out_ptr0, ret)

shape = [128, 2]
x0 = torch.ones(shape).to(torch.bool).cuda()
ans_int8 = torch.sum(x0.to(torch.int8), (0, 1), dtype=torch.int8).to(torch.bool)
ans_bool = torch.sum(x0, (0, 1), dtype=torch.bool)
ans = torch.sum(x0, (0, 1))
output_shape = shape[2:]
output = torch.zeros(output_shape, dtype=torch.bool).cuda()

triton_sum_2D_dim0_dim1[(1,)](x0, output, *shape, debug=True)
print(f'torch sum int8, bool, not specified: {ans_int8}, {ans_bool}, {ans}')
print(f'triton : {output}')
# torch sum int8, bool, not specified: False, True, 256
# triton : False
```

### Environment details

+ NVIDIA-SMI 575.57.08              Driver Version: 575.57.08      CUDA Version: 12.9
+ Tesla V100-PCIE-16GB
+ triton Version: 3.4.0
+ torch Version: 2.10.0+cu129

## 评论 (3)

### chfeng-cs · 2026-04-12

Hi @greatofdream , are you planning to submit a fix for this? 
Happy to take it on if you're not.

### greatofdream · 2026-04-13

> Hi [@greatofdream](https://github.com/greatofdream) , are you planning to submit a fix for this? Happy to take it on if you're not.

@chfeng-cs I have not submitted a fix yet because I am not entirely sure if using int8  for the boolean summation was intentional. If int8 is used on purpose, the documentation should be updated. Otherwise, appreciate you taking it on.

### greatofdream · 2026-04-13

I checked the TTIR generated from above triton kernel and found the summation is processed with int32 dtype. The reason of above bug comes from wrong cast from i32 to i8 in **`tl.store`** when the output dtype is bool .
```ttir
    %x_27 = tt.load %x_26 : tensor<128x2x!tt.ptr<i8>> loc(#loc20)
    %x_28 = arith.cmpi ne, %x_27, %x : tensor<128x2xi8> loc(#loc20)
    %input = arith.extui %x_28 : tensor<128x2xi1> to tensor<128x2xi32> loc(#loc30)
    %ret = "tt.reduce"(%input) <{axis = 1 : i32}> ({
    ^bb0(%ret_30: i32 loc(callsite(#loc1 at #loc28)), %ret_31: i32 loc(callsite(#loc1 at #loc28))):
      %ret_32 = arith.extui %ret_30 : i32 to i64 loc(#loc35)
      %ret_33 = arith.extui %ret_31 : i32 to i64 loc(#loc35)
      %ret_34 = arith.addi %ret_32, %ret_33 : i64 loc(#loc35)
      %ret_35 = arith.cmpi sle, %ret_34, %c4294967295_i64 : i64 loc(#loc35)
      %ret_36 = arith.cmpi sge, %ret_34, %c0_i64 : i64 loc(#loc35)
      %ret_37 = arith.andi %ret_35, %ret_36 : i1 loc(#loc35)
      tt.assert %ret_37, "int32 overflow detected for operation add" : i1 loc(#loc35)
      %ret_38 = arith.addi %ret_30, %ret_31 : i32 loc(#loc35)
      tt.reduce.return %ret_38 : i32 loc(#loc31)
    }) : (tensor<128x2xi32>) -> tensor<128xi32> loc(#loc31)
    %ret_29 = "tt.reduce"(%ret) <{axis = 0 : i32}> ({
    ^bb0(%ret_30: i32 loc(callsite(#loc1 at #loc29)), %ret_31: i32 loc(callsite(#loc1 at #loc29))):
      %ret_32 = arith.extui %ret_30 : i32 to i64 loc(#loc36)
      %ret_33 = arith.extui %ret_31 : i32 to i64 loc(#loc36)
      %ret_34 = arith.addi %ret_32, %ret_33 : i64 loc(#loc36)
      %ret_35 = arith.cmpi sle, %ret_34, %c4294967295_i64 : i64 loc(#loc36)
      %ret_36 = arith.cmpi sge, %ret_34, %c0_i64 : i64 loc(#loc36)
      %ret_37 = arith.andi %ret_35, %ret_36 : i1 loc(#loc36)
      tt.assert %ret_37, "int32 overflow detected for operation add" : i1 loc(#loc36)
      %ret_38 = arith.addi %ret_30, %ret_31 : i32 loc(#loc36)
      tt.reduce.return %ret_38 : i32 loc(#loc33)
    }) : (tensor<128xi32>) -> i32 loc(#loc33)
    %0 = tt.bitcast %out_ptr0 : !tt.ptr<i1> -> !tt.ptr<i8> loc(#loc15)
    %1 = arith.trunci %ret_29 : i32 to i8 loc(#loc15)
    tt.store %0, %1 : !tt.ptr<i8> loc(#loc15)
    tt.return loc(#loc16)
```
