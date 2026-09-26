source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/warmup/jit_warmup_triton_helper/
lastmod: 2026-09-24

#

`vllm.model_executor.warmup.jit_warmup_triton_helper`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_triton_helper)

Classes:

-
–[TritonCompileKey](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_triton_helper.TritonCompileKey)Triton-derived compile key with one non-comparing replay input.

-
–[TritonJitKey](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_triton_helper.TritonJitKey)Process-local identity of one Triton JIT specialization.

-
–[TritonKernelDispatcher](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_triton_helper.TritonKernelDispatcher)Callable Triton launcher with compile-time warmup support.

-
–[TritonWarmupTensor](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_triton_helper.TritonWarmupTensor)Compile-only tensor metadata used by Triton warmup.

-
–[VllmTritonJitKernel](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_triton_helper.VllmTritonJitKernel)Triton owner whose runtime launch specification is reused for warmup.


Functions:

-
–[triton_kernel_dispatcher_with_warmup](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_triton_helper.triton_kernel_dispatcher_with_warmup)Decorate a dispatch function or a native Triton kernel for warmup.

-
–[triton_scalar_specialization_rep](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_triton_helper.triton_scalar_specialization_rep)Return an integer with the same default Triton JIT specialization.

-
–[triton_warmup_inputs](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_triton_helper.triton_warmup_inputs)Build launcher inputs from Triton's native positional argument order.


##

`TritonCompileKey`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_triton_helper.TritonCompileKey)

Triton-derived compile key with one non-comparing replay input.

## Source code in `vllm/model_executor/warmup/jit_warmup_triton_helper.py`


##

`TritonJitKey`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_triton_helper.TritonJitKey)

Process-local identity of one Triton JIT specialization.

## Source code in `vllm/model_executor/warmup/jit_warmup_triton_helper.py`


##

`TritonKernelDispatcher`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_triton_helper.TritonKernelDispatcher)

Bases: [Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)[P]

Callable Triton launcher with compile-time warmup support.

## Source code in `vllm/model_executor/warmup/jit_warmup_triton_helper.py`


##

`TritonWarmupTensor`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_triton_helper.TritonWarmupTensor)

Compile-only tensor metadata used by Triton warmup.

`strides=None`

represents compact row-major storage. Pass explicit strides whenever the runtime tensor can be padded, transposed, or otherwise strided.

## Source code in `vllm/model_executor/warmup/jit_warmup_triton_helper.py`


##

`VllmTritonJitKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_triton_helper.VllmTritonJitKernel)

Bases:

, [VllmJitKernel](https://docs.vllm.ai/jit_warmup/#vllm.model_executor.warmup.jit_warmup.VllmJitKernel)[CompileKeyT][Generic](https://docs.python.org/3/library/typing.html#typing.Generic)[CompileKeyT]

Triton owner whose runtime launch specification is reused for warmup.

Methods:

-
–[warmup_inputs](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_triton_helper.VllmTritonJitKernel.warmup_inputs)Return runtime-shaped inputs that reproduce one compile key.


## Source code in `vllm/model_executor/warmup/jit_warmup_triton_helper.py`


|
|

###

`warmup_inputs(compile_key)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_triton_helper.VllmTritonJitKernel.warmup_inputs)

Return runtime-shaped inputs that reproduce one compile key.

##

`_triton_key_deriver(kernel)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_triton_helper._triton_key_deriver)

Prepare Triton's key derivation once for one kernel and device.

## Source code in `vllm/model_executor/warmup/jit_warmup_triton_helper.py`


|
|

##

`triton_kernel_dispatcher_with_warmup(*, warmup_inputs, kernel=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_triton_helper.triton_kernel_dispatcher_with_warmup)

Decorate a dispatch function or a native Triton kernel for warmup.

## Source code in `vllm/model_executor/warmup/jit_warmup_triton_helper.py`


##

`triton_scalar_specialization_rep(value)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_triton_helper.triton_scalar_specialization_rep)

Return an integer with the same default Triton JIT specialization.

For an ordinary integer argument, Triton's cache key contains its inferred type (`i32`

, `i64`

, or `u64`

) and one of three value classes:

`1`

is specialized as the exact constant`1`

.- Multiples of 16 receive a
`tt.divisibility = 16`

attribute. - All other values have no value specialization.

Warmup only needs one concrete value for each cache-key class. This helper returns `1`

for the exact-one class and otherwise returns a divisible or generic representative while preserving the inferred integer type.

This applies only to non-`constexpr`

integer arguments using Triton's default specialization. Do not use it for arguments listed in `do_not_specialize`

or `do_not_specialize_on_alignment`

.

## Source code in `vllm/model_executor/warmup/jit_warmup_triton_helper.py`


##

`triton_warmup_inputs(kernel, *args, grid, pointer_dtypes=None, **kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_triton_helper.triton_warmup_inputs)

Build launcher inputs from Triton's native positional argument order.