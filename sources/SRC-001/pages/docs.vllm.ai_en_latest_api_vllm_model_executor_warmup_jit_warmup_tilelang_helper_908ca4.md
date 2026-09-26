source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/warmup/jit_warmup_tilelang_helper/
lastmod: 2026-09-24

#

`vllm.model_executor.warmup.jit_warmup_tilelang_helper`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_tilelang_helper)

Compile-only helpers for TileLang JIT warmup.

Classes:

-
–[TileLangWarmupTensor](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_tilelang_helper.TileLangWarmupTensor)Minimal tensor-like object accepted by TileLang compile().

-
–[VllmTileLangJitKernel](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_tilelang_helper.VllmTileLangJitKernel)TileLang owner whose runtime launch specification is reused for warmup.


Functions:

-
–[compile_tilelang](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_tilelang_helper.compile_tilelang)Compile one TileLang specialization and populate its call cache.

-
–[kernel_launcher](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_tilelang_helper.kernel_launcher)Launch TileLang from declarative kernel and runtime argument tuples.


##

`TileLangWarmupTensor`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_tilelang_helper.TileLangWarmupTensor)

Minimal tensor-like object accepted by TileLang compile().

TileLang builds its cache key and TIR from tensor dtype, shape and stride. This object deliberately has no storage, so compile-only warmup does not allocate GPU memory and does not launch the kernel.

## Source code in `vllm/model_executor/warmup/jit_warmup_tilelang_helper.py`


##

`VllmTileLangJitKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_tilelang_helper.VllmTileLangJitKernel)

Bases:

, [VllmJitKernel](https://docs.vllm.ai/jit_warmup/#vllm.model_executor.warmup.jit_warmup.VllmJitKernel)[CompileKeyT][Generic](https://docs.python.org/3/library/typing.html#typing.Generic)[CompileKeyT]

TileLang owner whose runtime launch specification is reused for warmup.

Methods:

-
–[warmup_inputs](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_tilelang_helper.VllmTileLangJitKernel.warmup_inputs)Return runtime-shaped inputs that reproduce one compile key.


## Source code in `vllm/model_executor/warmup/jit_warmup_tilelang_helper.py`


###

`warmup_inputs(compile_key)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_tilelang_helper.VllmTileLangJitKernel.warmup_inputs)

Return runtime-shaped inputs that reproduce one compile key.

##

`compile_tilelang(jit_impl, *args, **kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_tilelang_helper.compile_tilelang)

Compile one TileLang specialization and populate its call cache.

TileLang's `compile()`

materializes the kernel without launching it. We also store the compiled kernel in `_kernel_cache`

using the same parsed key as `__call__`

so runtime does not report a cache miss for an already materialized specialization.

## Source code in `vllm/model_executor/warmup/jit_warmup_tilelang_helper.py`


##

`kernel_launcher(call_fn)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.jit_warmup_tilelang_helper.kernel_launcher)

Launch TileLang from declarative kernel and runtime argument tuples.