# [Issue #2773] [FEA] Support indexing `List[cute.Tensor]` with `thread_idx` inside kernel

source: https://github.com/NVIDIA/cutlass/issues/2773
state: closed | updated: 2026-09-20T16:49:33Z
labels: feature request, ? - Needs Triage, inactive-30d, inactive-90d, CuTe DSL

## 正文

### Which component requires the feature?

CuTe DSL

### Feature Request

Hi! Recently I have been using `CuTe DSL` to implement a fused kernel, which involves NVLink-Domain communication by accessing peer memory mapped by `torch symmetric memory`. I need to pass a list of `cute.Tensor`s into the kernel and use `thread_idx` to index into the list. However, it seems that `cute.arch.thread_idx()` cannot be used as an integer to index a list, so the following error popped out:
```
cutlass.base_dsl.common.DSLRuntimeError: DSLRuntimeError: '<class 'cutlass.base_dsl._mlir_helpers.arith.ArithValue'>' object cannot be interpreted as an integer
```

Now I implement my kernel in the following way:
``` Python
@cute.kernel
def a2a(
    mS: cute.Tensor,
    peer_bufs: List[cute.Tensor],  # List of peer mem tensors
    rank: cutlass.Constexpr[int],
):
    tidx, _, _ = cute.arch.thread_idx()

    # Cannot use tidx to index List[cute.Tensor]
    # peer_bufs[tidx][rank] = mS[tidx]

    if tidx == 0:
        peer_bufs[0][rank] = mS[tidx]
    if tidx == 1:
        peer_bufs[1][rank] = mS[tidx]
    if tidx == 2:
        peer_bufs[2][rank] = mS[tidx]
    if tidx == 3:
        peer_bufs[3][rank] = mS[tidx]
    if tidx == 4:
        peer_bufs[4][rank] = mS[tidx]
    if tidx == 5:
        peer_bufs[5][rank] = mS[tidx]
    if tidx == 6:
        peer_bufs[6][rank] = mS[tidx]
    if tidx == 7:
        peer_bufs[7][rank] = mS[tidx]
```

It seems really inelegant and verbose. Most importantly, list with different lengths is not supported since I cannot dynamically adjust my kernel at runtime, but theoretically as long as the length of list passed into kernel is the same as the one passed into `cute.compile`, it should be feasible. However, for example, with the above kernel, when I passed `List[cute.Tensor]` with only 4 `cute.Tensor`s in it, the following error popped out:

```
[rank3]:     peer_bufs[4][rank] = mS[tidx]
[rank3]: IndexError: list index out of range
```

I hope to know whether this usage is not feasible at all, or it is an incoming feature. Or there might be another way in `CuTe DSL` to maneuver this situation. Thanks!!!!

## 评论 (8)

### fengxie · 2025-11-17

This is known limitation of CuTe DSL unfortunately as List is compile time structure. We can not index it at runtime.

You can pass list of tensors as tensor of pointers.

```python
import cutlass
import cutlass.cute as cute
from cutlass.cute.runtime import from_dlpack


@cute.jit
def test_ptr_array(ptr_array: cute.Tensor, index: cutlass.Int32):
    intptr = ptr_array[index]
    ptr = cute.make_ptr(cutlass.Float32, intptr, cute.AddressSpace.generic)
    tensor = cute.make_tensor(ptr, cute.make_ordered_layout((4, 2), order=(1, 0)))
    cute.print_tensor(tensor)


if __name__ == "__main__":
    import torch

    tensors = [torch.randn(4, 2, dtype=torch.float32) for _ in range(10)]
    ptr_array = torch.tensor([tensor.data_ptr() for tensor in tensors])
    test_ptr_array(from_dlpack(ptr_array), 3)
    print(tensors[3])
```

### Gin-Sin · 2025-11-17

> This is known limitation of CuTe DSL unfortunately as List is compile time structure. We can not index it at runtime.
> 
> You can pass list of tensors as tensor of pointers.
> 
> import cutlass
> import cutlass.cute as cute
> from cutlass.cute.runtime import from_dlpack
> 
> 
> @cute.jit
> def test_ptr_array(ptr_array: cute.Tensor, index: cutlass.Int32):
>     intptr = ptr_array[index]
>     ptr = cute.make_ptr(cutlass.Float32, intptr, cute.AddressSpace.generic)
>     tensor = cute.make_tensor(ptr, cute.make_ordered_layout((4, 2), order=(1, 0)))
>     cute.print_tensor(tensor)
> 
> 
> if __name__ == "__main__":
>     import torch
> 
>     tensors = [torch.randn(4, 2, dtype=torch.float32) for _ in range(10)]
>     ptr_array = torch.tensor([tensor.data_ptr() for tensor in tensors])
>     test_ptr_array(from_dlpack(ptr_array), 3)
>     print(tensors[3])

What should I do if I want to access the tensor of tensor pointers inside the kernel instead of a JIT function? Can I still `make_ptr` within a kernel? If yes, is there any  overhead to do so?

### fengxie · 2025-11-18

> > This is known limitation of CuTe DSL unfortunately as List is compile time structure. We can not index it at runtime.
> > You can pass list of tensors as tensor of pointers.
> > import cutlass
> > import cutlass.cute as cute
> > from cutlass.cute.runtime import from_dlpack
> > @cute.jit
> > def test_ptr_array(ptr_array: cute.Tensor, index: cutlass.Int32):
> > intptr = ptr_array[index]
> > ptr = cute.make_ptr(cutlass.Float32, intptr, cute.AddressSpace.generic)
> > tensor = cute.make_tensor(ptr, cute.make_ordered_layout((4, 2), order=(1, 0)))
> > cute.print_tensor(tensor)
> > if **name** == "**main**":
> > import torch
> > ```
> > tensors = [torch.randn(4, 2, dtype=torch.float32) for _ in range(10)]
> > ptr_array = torch.tensor([tensor.data_ptr() for tensor in tensors])
> > test_ptr_array(from_dlpack(ptr_array), 3)
> > print(tensors[3])
> > ```
> 
> What should I do if I want to access the tensor of tensor pointers inside the kernel instead of a JIT function? Can I still `make_ptr` within a kernel? If yes, is there any overhead to do so?

It should be the same from `cute.kernel`. As `make_ptr`, `make_tensor` don't do actual computation, there should be almost no overhead.

### Gin-Sin · 2025-11-20

> > > This is known limitation of CuTe DSL unfortunately as List is compile time structure. We can not index it at runtime.
> > > You can pass list of tensors as tensor of pointers.
> > > import cutlass
> > > import cutlass.cute as cute
> > > from cutlass.cute.runtime import from_dlpack
> > > @cute.jit
> > > def test_ptr_array(ptr_array: cute.Tensor, index: cutlass.Int32):
> > > intptr = ptr_array[index]
> > > ptr = cute.make_ptr(cutlass.Float32, intptr, cute.AddressSpace.generic)
> > > tensor = cute.make_tensor(ptr, cute.make_ordered_layout((4, 2), order=(1, 0)))
> > > cute.print_tensor(tensor)
> > > if **name** == "**main**":
> > > import torch
> > > ```
> > > tensors = [torch.randn(4, 2, dtype=torch.float32) for _ in range(10)]
> > > ptr_array = torch.tensor([tensor.data_ptr() for tensor in tensors])
> > > test_ptr_array(from_dlpack(ptr_array), 3)
> > > print(tensors[3])
> > > ```
> > 
> > 
> > What should I do if I want to access the tensor of tensor pointers inside the kernel instead of a JIT function? Can I still `make_ptr` within a kernel? If yes, is there any overhead to do so?
> 
> It should be the same from `cute.kernel`. As `make_ptr`, `make_tensor` don't do actual computation, there should be almost no overhead.

It seems the index you passed into `cute.jit` function is determined in compile-time. However, I need to use `thread_idx` or other values in run-time to index the tensor of pointers and call `make_ptr` in order to call `cute.make_tensor`, so the pointer I need to use won't be determined in compile-time. Can it work under this situation?

### fengxie · 2025-11-20

> > > > This is known limitation of CuTe DSL unfortunately as List is compile time structure. We can not index it at runtime.
> > > > You can pass list of tensors as tensor of pointers.
> > > > import cutlass
> > > > import cutlass.cute as cute
> > > > from cutlass.cute.runtime import from_dlpack
> > > > @cute.jit
> > > > def test_ptr_array(ptr_array: cute.Tensor, index: cutlass.Int32):
> > > > intptr = ptr_array[index]
> > > > ptr = cute.make_ptr(cutlass.Float32, intptr, cute.AddressSpace.generic)
> > > > tensor = cute.make_tensor(ptr, cute.make_ordered_layout((4, 2), order=(1, 0)))
> > > > cute.print_tensor(tensor)
> > > > if **name** == "**main**":
> > > > import torch
> > > > ```
> > > > tensors = [torch.randn(4, 2, dtype=torch.float32) for _ in range(10)]
> > > > ptr_array = torch.tensor([tensor.data_ptr() for tensor in tensors])
> > > > test_ptr_array(from_dlpack(ptr_array), 3)
> > > > print(tensors[3])
> > > > ```
> > > 
> > > 
> > > What should I do if I want to access the tensor of tensor pointers inside the kernel instead of a JIT function? Can I still `make_ptr` within a kernel? If yes, is there any overhead to do so?
> > 
> > 
> > It should be the same from `cute.kernel`. As `make_ptr`, `make_tensor` don't do actual computation, there should be almost no overhead.
> 
> It seems the index you passed into `cute.jit` function is determined in compile-time. However, I need to use `thread_idx` or other values in run-time to index the tensor of pointers and call `make_ptr` in order to call `cute.make_tensor`, so the pointer I need to use won't be determined in compile-time. Can it work under this situation?

It should work for dynamic index as well. Let me know if you hit issues.

### Gin-Sin · 2025-11-20

> > > > > This is known limitation of CuTe DSL unfortunately as List is compile time structure. We can not index it at runtime.
> > > > > You can pass list of tensors as tensor of pointers.
> > > > > import cutlass
> > > > > import cutlass.cute as cute
> > > > > from cutlass.cute.runtime import from_dlpack
> > > > > @cute.jit
> > > > > def test_ptr_array(ptr_array: cute.Tensor, index: cutlass.Int32):
> > > > > intptr = ptr_array[index]
> > > > > ptr = cute.make_ptr(cutlass.Float32, intptr, cute.AddressSpace.generic)
> > > > > tensor = cute.make_tensor(ptr, cute.make_ordered_layout((4, 2), order=(1, 0)))
> > > > > cute.print_tensor(tensor)
> > > > > if **name** == "**main**":
> > > > > import torch
> > > > > ```
> > > > > tensors = [torch.randn(4, 2, dtype=torch.float32) for _ in range(10)]
> > > > > ptr_array = torch.tensor([tensor.data_ptr() for tensor in tensors])
> > > > > test_ptr_array(from_dlpack(ptr_array), 3)
> > > > > print(tensors[3])
> > > > > ```
> > > > 
> > > > 
> > > > What should I do if I want to access the tensor of tensor pointers inside the kernel instead of a JIT function? Can I still `make_ptr` within a kernel? If yes, is there any overhead to do so?
> > > 
> > > 
> > > It should be the same from `cute.kernel`. As `make_ptr`, `make_tensor` don't do actual computation, there should be almost no overhead.
> > 
> > 
> > It seems the index you passed into `cute.jit` function is determined in compile-time. However, I need to use `thread_idx` or other values in run-time to index the tensor of pointers and call `make_ptr` in order to call `cute.make_tensor`, so the pointer I need to use won't be determined in compile-time. Can it work under this situation?
> 
> It should work for dynamic index as well. Let me know if you hit issues.

Sure, thanks!

### github-actions[bot] · 2025-12-20

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-03-20

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.
