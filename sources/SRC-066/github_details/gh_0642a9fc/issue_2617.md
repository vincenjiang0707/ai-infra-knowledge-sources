# [Issue #2617] [QST][DSL] How to pass a cpu list to kernel and visit element use dynamic index?

source: https://github.com/NVIDIA/cutlass/issues/2617
state: closed | updated: 2026-09-26T16:23:25Z
labels: question, ? - Needs Triage, inactive-30d, inactive-90d

## 正文

**What is your question?**
Hi! I'm really excited to discover CuteDSL as such a powerful kernel writing tool. I'm new to Cute DSL and currently facing an issue while implementing `Group GEMM`.

**My problem is:** 
the stride list for the m-dimension in `Group GEMM` currently resides in CPU memory. Is there a way to pass this list to the GPU during kernel launch by copying it to `.param` space, rather than using `torch.to("cuda")`? This would be crucial for achieving high-performance `Group GEMM` execution.

I think we can use `List[cutlass.Int32]` or `Tuple[cutlass.Int32, ...]` to pass the list to kernel，but I can't visit element that use dynamic index，such as:

```python
@cute.kernel
def kernel(seqs: List[Int32]):
    tidx, _, _ = cute.arch.thread_idx()
    cute.printf("tidx = {}, val = {}", tidx, seqs[tidx])
```

A way to implement this feature using C++:

```cpp
template<int N>
struct IntList {
    int list[N];
};

__global__ void square(int* array, const __grid_constant__ IntList<10> l) {
    // use list
}
```

so should we support a fixed-length list container similar to C++'s `std::array`?

Thanks for your help!

## 评论 (22)

### sfc-gh-lpaille · 2025-09-08

maybe passing a ctypes array would work ?

### zfan2356 · 2025-09-09

> maybe passing a ctypes array would work ?

There are two ways to pass parameters to a CUDA kernel: by pointer or by "value set". When passing a pointer, it must point to GPU memory—otherwise, it will result in an "illegal memory access" error.

Currently, we have an array residing in CPU memory. If we want to pass it via pointer, we'd need to move it to GPU using `torch.to()`, which incurs significant data transfer overhead.

### fengxie · 2025-09-10

> > maybe passing a ctypes array would work ?
> 
> There are two ways to pass parameters to a CUDA kernel: by pointer or by "value set". When passing a pointer, it must point to GPU memory—otherwise, it will result in an "illegal memory access" error.
> 
> Currently, we have an array residing in CPU memory. If we want to pass it via pointer, we'd need to move it to GPU using `torch.to()`, which incurs significant data transfer overhead.

If you just want to pass a small vector/array to GPU, you can directly pass `TensorSSA` to kernel. It's similar to pass an `std::array` as value. Does this example work for you?

https://gist.github.com/fengxie/7b48fc4a0984b6deb7d1aa4072ec35fb

If you want to pass a large vector/array to GPU, using global memory is better for performance.

### fengxie · 2025-09-10

> > > maybe passing a ctypes array would work ?
> > 
> > 
> > There are two ways to pass parameters to a CUDA kernel: by pointer or by "value set". When passing a pointer, it must point to GPU memory—otherwise, it will result in an "illegal memory access" error.
> > Currently, we have an array residing in CPU memory. If we want to pass it via pointer, we'd need to move it to GPU using `torch.to()`, which incurs significant data transfer overhead.
> 
> If you just want to pass a small vector/array to GPU, you can directly pass `TensorSSA` to kernel. It's similar to pass an `std::array` as value. Does this example work for you?
> 
> https://gist.github.com/fengxie/7b48fc4a0984b6deb7d1aa4072ec35fb
> 
> If you want to pass a large vector/array to GPU, using global memory is better for performance.

There is a known bug with current release version to work with dynamic index like thread index. This bug will be fixed in next release coming soon.

It's worth to note that non-uniform access with different indices per thread can be inefficient.

### zfan2356 · 2025-09-10

> > > maybe passing a ctypes array would work ?
> > 
> > 
> > There are two ways to pass parameters to a CUDA kernel: by pointer or by "value set". When passing a pointer, it must point to GPU memory—otherwise, it will result in an "illegal memory access" error.
> > Currently, we have an array residing in CPU memory. If we want to pass it via pointer, we'd need to move it to GPU using `torch.to()`, which incurs significant data transfer overhead.
> 
> If you just want to pass a small vector/array to GPU, you can directly pass `TensorSSA` to kernel. It's similar to pass an `std::array` as value. Does this example work for you?
> 
> https://gist.github.com/fengxie/7b48fc4a0984b6deb7d1aa4072ec35fb
> 
> If you want to pass a large vector/array to GPU, using global memory is better for performance.

Thanks for your help! However, this approach doesn't solve my problem. I have a `List[int]` array residing in CPU memory, and I want to pass this array directly to a `@cute.jit` function, which will then forward it to a `@cute.kernel` function. The CUDA driver should automatically handle moving this `List[int]` data from CPU to the GPU's `.param` memory space during kernel launch. so maybe I can't use `cute.Tensor` for pack my array.

Cute DSL can pass a `List[int]` parameter to `cute.jit` or `cute.kernel` function, however, it does not support using **runtime indices** to access elements by index within the list.

### zfan2356 · 2025-09-10

> > > > maybe passing a ctypes array would work ?
> > > 
> > > 
> > > There are two ways to pass parameters to a CUDA kernel: by pointer or by "value set". When passing a pointer, it must point to GPU memory—otherwise, it will result in an "illegal memory access" error.
> > > Currently, we have an array residing in CPU memory. If we want to pass it via pointer, we'd need to move it to GPU using `torch.to()`, which incurs significant data transfer overhead.
> > 
> > 
> > If you just want to pass a small vector/array to GPU, you can directly pass `TensorSSA` to kernel. It's similar to pass an `std::array` as value. Does this example work for you?
> > https://gist.github.com/fengxie/7b48fc4a0984b6deb7d1aa4072ec35fb
> > If you want to pass a large vector/array to GPU, using global memory is better for performance.
> 
> There is a known bug with current release version to work with dynamic index like thread index. This bug will be fixed in next release coming soon.
> 
> It's worth to note that non-uniform access with different indices per thread can be inefficient.

Fantastic! If we could support dynamic indexing for the `List[int]` class in `cute.jit` and `cute.kernel` function, this issue might be resolved.

### fengxie · 2025-09-10

> > > > maybe passing a ctypes array would work ?
> > > 
> > > 
> > > There are two ways to pass parameters to a CUDA kernel: by pointer or by "value set". When passing a pointer, it must point to GPU memory—otherwise, it will result in an "illegal memory access" error.
> > > Currently, we have an array residing in CPU memory. If we want to pass it via pointer, we'd need to move it to GPU using `torch.to()`, which incurs significant data transfer overhead.
> > 
> > 
> > If you just want to pass a small vector/array to GPU, you can directly pass `TensorSSA` to kernel. It's similar to pass an `std::array` as value. Does this example work for you?
> > https://gist.github.com/fengxie/7b48fc4a0984b6deb7d1aa4072ec35fb
> > If you want to pass a large vector/array to GPU, using global memory is better for performance.
> 
> Thanks for your help! However, this approach doesn't solve my problem. I have a `List[int]` array residing in CPU memory, and I want to pass this array directly to a `@cute.jit` function, which will then forward it to a `@cute.kernel` function. The CUDA driver should automatically handle moving this `List[int]` data from CPU to the GPU's `.param` memory space during kernel launch. so maybe I can't use `cute.Tensor` for pack my array.
> 
> Cute DSL can pass a `List[int]` parameter to `cute.jit` or `cute.kernel` function, however, it does not support using **runtime indices** to access elements by index within the list.

Ah, i see. How about this? https://gist.github.com/fengxie/57d57429a0300fa2b9507c669f4a659c 

We should be able to put list of integer values into vector/array then pass to kernel.

Dynamic indexing vector has a known bug which should be fixed soon. Comment out print part should be able to run on today's release versionl

### fengxie · 2025-09-10

> Fantastic! If we could support dynamic indexing for the List[int] class in cute.jit and cute.kernel function, this issue might be resolved.

Probably not dynamic indexing for `List[int]` or any other Python object as we don't natively support them at runtime. But it could be converted into `vector` then index it like the example shows.

### zfan2356 · 2025-09-10

> Ah, i see. How about this? https://gist.github.com/fengxie/57d57429a0300fa2b9507c669f4a659c
> 
> We should be able to put list of integer values into vector/array then pass to kernel.
> 
> Dynamic indexing vector has a known bug which should be fixed soon. Comment out print part should be able to run on today's release versionl

Sure! This approach might be well-suited to my use case. Thank you very much!

### zfan2356 · 2025-09-17

> Ah, i see. How about this? https://gist.github.com/fengxie/57d57429a0300fa2b9507c669f4a659c
> 
> We should be able to put list of integer values into vector/array then pass to kernel.
> 
> Dynamic indexing vector has a known bug which should be fixed soon. Comment out print part should be able to run on today's release versionl

@fengxie Hello! I'm excited to find that CuteDSL has released version 4.2.0, and I've successfully resolved the previous issue.

But I do have another question regarding passing List containers to kernels. When I pass a List, does CuteDSL process the entire list at compile time? Or, if I want to pass different lists to the same kernel, will I need to recompile it each time?

In the documentation, I found the statement: "Example: Lists can contain dynamic values but their structure cannot be modified during kernel execution." Does this mean that **only the list length** is fixed at compile time, while the values within the list can be dynamic? If so, can I pass different lists of the same length to the kernel without triggering a recompilation? 

aka, can I only add the list length to compile key to avoid recompile when pass a same length list but have different value？

Thank you for your clarification!


### fengxie · 2025-09-17

> In the documentation, I found the statement: "Example: Lists can contain dynamic values but their structure cannot be modified during kernel execution." Does this mean that only the list length is fixed at compile time, while the values within the list can be dynamic? If so, can I pass different lists of the same length to the kernel without triggering a recompilation?

You can pass different lists with different values without trigger recompile as long as following are not changed
* corresponding type of values 
* Length of list

E.g. changing Int32 -> Int64 will trigger re-compile. Or if you pass list of tensors, type changes like static shape, leading dim can also trigger re-compiler.

If no type change, then recompile is not needed.

> aka, can I only add the list length to compile key to avoid recompile when pass a same length list but have different value？

If no type change, then it should be enough. If you expect type change, then you can put factors impact type, e.g. leading dimension or element type of tensor. 

### zfan2356 · 2025-09-19

> Sure! This approach might be well-suited to my use case. Thank you very much!

@fengxie I'm very sorry to bother you again, but I've encountered an issue when trying to access a random index of `cute.TensorSSA` within the cute.kernel function. Below is the error message I received:
```
cutlass.base_dsl.common.DSLRuntimeError: DSLRuntimeError: 🧊🧊🧊 ICE IR Verification Failed 🧊🧊🧊
  Caused exception: Verification failed:
error: "epilog_gmem_copy_and_partition"("/test.py":1705:0): operand #1 does not dominate this use
 note: "epilog_gmem_copy_and_partition"("/test.py":1705:0): see current operation: %527 = "cute.crd2idx"(%526, %2565) : (!cute.coord<"?">, !cute.layout<"(11):(1)">) -> !cute.int_tuple<"?">
 note: "while_after_block_8"("/test.py":807:0): operand defined here (op is neither in a parent nor in a child region)
```
The error occurs at the following line, where `cu_seqlens_m` is a `cute.TensorSSA` variable and `mA_mkl` is a cute.Tensor variable, and `cu_seqlens_m` is `Optional[cute.TensorSSA | cute.Tensor]` type
```
 mA_mk = cute.domain_offset((cu_seqlens_m[batch_idx], 0), mA_mkl)
```
Due to the complexity of the code, I haven't been able to reproduce the issue with a minimal example. Could you please provide any insights into what might be causing this error? I'll try to create a simplified version of the problem if needed.

### fengxie · 2025-09-19

@anakinxc do you have some insight?

### fengxie · 2025-09-19

May I take a look at definition of this function?

> The error occurs at the following line, where cu_seqlens_m is a cute.TensorSSA variable and mA_mkl is a cute.Tensor variable, and cu_seqlens_m is Optional[cute.TensorSSA | cute.Tensor] type

### zfan2356 · 2025-09-19

> May I take a look at definition of this function?
> 
> > The error occurs at the following line, where cu_seqlens_m is a cute.TensorSSA variable and mA_mkl is a cute.Tensor variable, and cu_seqlens_m is Optional[cute.TensorSSA | cute.Tensor] type

Of course! 

```
    @cute.kernel
    def kernel(
        self,
        tma_atom_a: Optional[cute.CopyAtom],
        mA_mkl: cute.Tensor,
        tma_atom_b: cute.CopyAtom,
        mB_nkl: cute.Tensor,
        tma_atom_d: Optional[cute.CopyAtom],
        mD_mnl: Optional[cute.Tensor],
        tma_atom_c: Optional[cute.CopyAtom],
        mC_mnl: Optional[cute.Tensor],
        epilogue_params: ParamsBase,
        mAIdx: Optional[cute.Tensor],
        cu_seqlens_m: Optional[cute.Tensor | cute.TensorSSA],
        cu_seqlens_k: Optional[cute.Tensor | cute.TensorSSA],
        tensormaps: Optional[cute.Tensor],
        tiled_mma: cute.TiledMma,
        cluster_layout_mnk: cute.Layout,
        a_smem_layout: cute.ComposedLayout,
        b_smem_layout: cute.ComposedLayout,
        epi_smem_layout: cute.ComposedLayout,
        epi_c_smem_layout: cute.ComposedLayout,
        tile_sched_params: ParamsBase,
        TileSchedulerCls: cutlass.Constexpr[Callable],
    ):
```
Or if you known about https://github.com/Dao-AILab/quack, I just add `cute.TensorSSA` support to pass a cpu intlist to `dense_gemm_sm90` kernel

### fengxie · 2025-09-19

I suspect we don't handle `Optional[cute.Tensor | cute.TensorSSA]` correctly. How about just remove this type annotation? @brandon-yujie-sun for visibility ;)

### zfan2356 · 2025-09-20

> I suspect we don't handle `Optional[cute.Tensor | cute.TensorSSA]` correctly. How about just remove this type annotation? [@brandon-yujie-sun](https://github.com/brandon-yujie-sun) for visibility ;)

Hmm, it doesn't seem to be working. I've written a small example, and it appears that using `Optional[cute.Tensor | cute.TensorSSA]` might work successfully. I'll try to create a minimal reproducible example to better demonstrate the issue. Thanks for your help!

### fengxie · 2025-09-20

> > I suspect we don't handle `Optional[cute.Tensor | cute.TensorSSA]` correctly. How about just remove this type annotation? [@brandon-yujie-sun](https://github.com/brandon-yujie-sun) for visibility ;)
> 
> Hmm, it doesn't seem to be working. I've written a small example, and it appears that using `Optional[cute.Tensor | cute.TensorSSA]` might work successfully. I'll try to create a minimal reproducible example to better demonstrate the issue. Thanks for your help!

Thanks a lot for trying and reporting.

### github-actions[bot] · 2025-10-20

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### fengxie · 2025-10-20

@zfan2356 is this still an issue with `4.2.1` ?

### github-actions[bot] · 2025-11-19

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-02-17

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.
