source: https://docs.vllm.ai/en/latest/api/vllm/env_override/
lastmod: 2026-09-24

#

`vllm.env_override`

[¶](https://docs.vllm.ai#vllm.env_override)

Functions:

-
–[get_graph_partition_signature_patched](https://docs.vllm.ai#vllm.env_override.get_graph_partition_signature_patched)Gets signature for each graph partition, including input nodes, output nodes, and

-
–[should_partition_patched](https://docs.vllm.ai#vllm.env_override.should_partition_patched)Return True if we should partition the inductor graph on this node.


##

`_VllmFallbackAllowList`

[¶](https://docs.vllm.ai#vllm.env_override._VllmFallbackAllowList)

Membership proxy that auto-allows vllm::*/vllm_aiter::* base_names.

## Source code in `vllm/env_override.py`


##

`_apply_constrain_to_fx_strides_patch()`

[¶](https://docs.vllm.ai#vllm.env_override._apply_constrain_to_fx_strides_patch)

Patch lowering.constrain_to_fx_strides globally. Safe to call multiple times; only the first call does anything. Only applies for torch >= 2.11 and < 2.12.

## Source code in `vllm/env_override.py`


##

`_apply_cpp_indirect_assert_patch()`

[¶](https://docs.vllm.ai#vllm.env_override._apply_cpp_indirect_assert_patch)

Replace CppVecKernel.indirect_assert with a fixed copy that uses `VecMask<...>::from(scalar)`

for scalar masks.

Idempotent: marks the class with `_vllm_indirect_assert_patched`

after the first apply.

## Source code in `vllm/env_override.py`


##

`_apply_fxgraphcache_pickle_patch(pickler_cls, bypass_cls)`

[¶](https://docs.vllm.ai#vllm.env_override._apply_fxgraphcache_pickle_patch)

Wrap pickler_cls.dumps to convert ValueError into bypass_cls.

Idempotent: sets `_vllm_fxgraph_dumps_patched`

on the class after the first apply to prevent re-application. The wrapper function is also marked with `_vllm_patched`

as an additional safeguard.

## Source code in `vllm/env_override.py`


##

`_apply_inductor_pattern_matcher_patch()`

[¶](https://docs.vllm.ai#vllm.env_override._apply_inductor_pattern_matcher_patch)

Allow custom ops and functionalization wrappers with unsupported dtypes.

## Source code in `vllm/env_override.py`


##

`_get_torch_cuda_version()`

[¶](https://docs.vllm.ai#vllm.env_override._get_torch_cuda_version)

##

`_get_torch_root()`

[¶](https://docs.vllm.ai#vllm.env_override._get_torch_root)

Locate the installed torch package without importing it.

## Source code in `vllm/env_override.py`


##

`_get_torch_version_attr(attr)`

[¶](https://docs.vllm.ai#vllm.env_override._get_torch_version_attr)

Read an attribute of torch.version without importing torch.

PyTorch version must not be determined by importing directly because it will trigger the CUDA initialization, losing the chance to set the LD_LIBRARY_PATH beforehand.

## Source code in `vllm/env_override.py`


##

`_maybe_promote_torch_symbols_for_rocm()`

[¶](https://docs.vllm.ai#vllm.env_override._maybe_promote_torch_symbols_for_rocm)

Put libtorch_cpu.so in the global symbol scope on ROCm, for GPU profiling.

Must run before 'import torch'. libkineto advertises itself to rocprofiler-sdk by exporting rocprofiler_configure from libtorch_cpu.so, and rocprofiler-sdk looks for that symbol exactly once, from a lazy initializer that runs *during* 'import torch'. CPython loads extension modules RTLD_LOCAL, so unless something has already placed the symbol in the global scope the lookup misses and no client is ever registered.

The failure is silent and total: no queue interception, so roctracer yields no GPU records, while torch.profiler still writes a complete CPU-only trace and reports success.

Best effort. If the library cannot be loaded early we leave the process exactly as it would have been, losing only GPU tracing.

## Source code in `vllm/env_override.py`


##

`_maybe_set_cuda_compatibility_path()`

[¶](https://docs.vllm.ai#vllm.env_override._maybe_set_cuda_compatibility_path)

Set LD_LIBRARY_PATH for CUDA forward compatibility if enabled.

Must run before 'import torch' since torch loads CUDA shared libraries at import time and the dynamic linker only consults LD_LIBRARY_PATH when a library is first loaded.

CUDA forward compatibility is only supported on select professional and datacenter NVIDIA GPUs. Consumer GPUs (GeForce, RTX) do not support it and will get Error 803 if compat libs are loaded.

## Source code in `vllm/env_override.py`


##

`_patch_cpp_indirect_assert_if_needed()`

[¶](https://docs.vllm.ai#vllm.env_override._patch_cpp_indirect_assert_if_needed)

Apply cpp codegen indirect_assert backport when on torch 2.11.x.

Defers application until torch._inductor.codegen.cpp is naturally imported by Inductor. Importing it eagerly during vllm.**init** pulls in torch._inductor.scheduler, whose top-level `import torch._inductor.async_compile`

can fail with `ModuleNotFoundError: import of torch._inductor.async_compile halted; None in sys.modules`

depending on the import order on the runner (observed in vLLM CPU CI).

## Source code in `vllm/env_override.py`


##

`_patch_fxgraphcache_pickle_if_needed()`

[¶](https://docs.vllm.ai#vllm.env_override._patch_fxgraphcache_pickle_if_needed)

Apply FxGraphCachePickler.dumps ValueError backport when on torch 2.10.x.

## Source code in `vllm/env_override.py`


##

`_patch_get_raw_stream_if_needed()`

[¶](https://docs.vllm.ai#vllm.env_override._patch_get_raw_stream_if_needed)

Workaround for TorchInductor autotune get_raw_stream() bug.

## Source code in `vllm/env_override.py`


##

`_patch_inductor_fallback_allow_list()`

[¶](https://docs.vllm.ai#vllm.env_override._patch_inductor_fallback_allow_list)

Wrap torch._inductor.lowering.FALLBACK_ALLOW_LIST so any custom op in the `vllm::`

or `vllm_aiter::`

namespaces is treated as a member.

Idempotent: a sentinel attribute on the proxy prevents re-wrapping.

## Source code in `vllm/env_override.py`


##

`_patch_inductor_pattern_matcher()`

[¶](https://docs.vllm.ai#vllm.env_override._patch_inductor_pattern_matcher)

Apply the backport when Inductor imports its pattern matcher.

## Source code in `vllm/env_override.py`


##

`_safe_builtins_dict(builtins_dict)`

[¶](https://docs.vllm.ai#vllm.env_override._safe_builtins_dict)

Filter a builtins dict to only picklable entries for serialization.

## Source code in `vllm/env_override.py`


##

`_update_scheduler_patched(self)`

[¶](https://docs.vllm.ai#vllm.env_override._update_scheduler_patched)

(Re)initializes the scheduler member. When initializing the scheduler, no CUBIN files should be generated (to avoid biasing any benchmarks and pessimizing fusion decisions).

## Source code in `vllm/env_override.py`


##

`get_graph_partition_signature_patched(self, partitions, skip_cudagraphs)`

[¶](https://docs.vllm.ai#vllm.env_override.get_graph_partition_signature_patched)

Gets signature for each graph partition, including input nodes, output nodes, and whether deallocating an input within graph partition.

## Source code in `vllm/env_override.py`


|
|

##

`should_partition_patched(self, node, should_log=False)`

[¶](https://docs.vllm.ai#vllm.env_override.should_partition_patched)

Return True if we should partition the inductor graph on this node.

## Source code in `vllm/env_override.py`


|
|