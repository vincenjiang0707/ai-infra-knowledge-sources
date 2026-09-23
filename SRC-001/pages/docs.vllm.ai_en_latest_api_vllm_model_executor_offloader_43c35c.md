source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/offloader/
lastmod: 2026-09-23

#

`vllm.model_executor.offloader`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader)

Model parameter offloading infrastructure.

Modules:

-
–[base](https://docs.vllm.ai/base/#vllm.model_executor.offloader.base)Base classes for model parameter offloading.

-
–[prefetch](https://docs.vllm.ai/prefetch/#vllm.model_executor.offloader.prefetch)Prefetch-based CPU offloading with async prefetching.

-
–[prefetch_ops](https://docs.vllm.ai/prefetch_ops/#vllm.model_executor.offloader.prefetch_ops)Custom ops for prefetch offloader torch.compile + CUDA graph compatibility.

-
–[uva](https://docs.vllm.ai/uva/#vllm.model_executor.offloader.uva)UVA-based CPU offloading using Unified Virtual Addressing.


Classes:

-
–[BaseOffloader](https://docs.vllm.ai#vllm.model_executor.offloader.BaseOffloader)Base class for model parameter offloading strategies.

-
–[NoopOffloader](https://docs.vllm.ai#vllm.model_executor.offloader.NoopOffloader)No-op offloader that returns modules as-is without any offloading.

-
–[PrefetchOffloader](https://docs.vllm.ai#vllm.model_executor.offloader.PrefetchOffloader)Prefetching-based offloader with group-based layer selection.

-
–[UVAOffloader](https://docs.vllm.ai#vllm.model_executor.offloader.UVAOffloader)Offloader using Unified Virtual Addressing (UVA) for zero-copy access.


Functions:

-
–[create_offloader](https://docs.vllm.ai#vllm.model_executor.offloader.create_offloader)Create an offloader based on the offload configuration.

-
–[get_offloader](https://docs.vllm.ai#vllm.model_executor.offloader.get_offloader)Get the global offloader instance.

-
–[set_offloader](https://docs.vllm.ai#vllm.model_executor.offloader.set_offloader)Set or reset the global offloader instance.

-
–[should_pin_memory](https://docs.vllm.ai#vllm.model_executor.offloader.should_pin_memory)Check if pinned memory should be used for weight offloading.


##

`BaseOffloader`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.BaseOffloader)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for model parameter offloading strategies.

Offloaders control how model parameters are stored and loaded during inference. Different strategies trade memory for compute/transfer time.

Methods:

-
–[join_after_forward](https://docs.vllm.ai#vllm.model_executor.offloader.BaseOffloader.join_after_forward)Join streams after forward. Override in subclasses.

-
–[post_init](https://docs.vllm.ai#vllm.model_executor.offloader.BaseOffloader.post_init)Called after model construction completes.

-
–[sync_prev_onload](https://docs.vllm.ai#vllm.model_executor.offloader.BaseOffloader.sync_prev_onload)Sync previous onload operations. Override in subclasses.

-
–[wrap_modules](https://docs.vllm.ai#vllm.model_executor.offloader.BaseOffloader.wrap_modules)Wrap modules with offloading logic.


Attributes:

-
([supports_tower_offload](https://docs.vllm.ai#vllm.model_executor.offloader.BaseOffloader.supports_tower_offload)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether

`wrap_modules`

also accepts modules routed by

## Source code in `vllm/model_executor/offloader/base.py`


###

`supports_tower_offload = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.BaseOffloader.supports_tower_offload)

Whether `wrap_modules`

also accepts modules routed by `SupportsMultiModal._mark_tower_model`

, outside the `make_layers`

call.

Offloaders whose `wrap_modules`

may only be called on the decoder layer stack (e.g. `PrefetchOffloader`

, which schedules prefetches over a circular layer stack) must keep this `False`

.

###

`_start_prefetch(layer_idx)`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.BaseOffloader._start_prefetch)

###

`_wait_for_layer(layer_idx)`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.BaseOffloader._wait_for_layer)

###

`join_after_forward()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.BaseOffloader.join_after_forward)

###

`post_init()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.BaseOffloader.post_init)

Called after model construction completes.

Offloaders can use this to: - Finalize parameter storage - Start initial prefetching - Allocate shared resources

###

`sync_prev_onload()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.BaseOffloader.sync_prev_onload)

###

`wrap_modules(modules_generator, prefix='')`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.BaseOffloader.wrap_modules)

Wrap modules with offloading logic.

Parameters:

-

(`modules_generator`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.BaseOffloader.wrap_modules(modules_generator))

) –[Generator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator)[[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module), None, None]Generator yielding modules to potentially offload.

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.BaseOffloader.wrap_modules(prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –Name prefix prepended to parameter names before matching them against the offloading parameter set. Used when the modules are not the full model, so that name segments stay fully qualified (e.g.

`visual`

for a tower module).

Returns:

## Source code in `vllm/model_executor/offloader/base.py`


##

`NoopOffloader`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.NoopOffloader)

Bases: [BaseOffloader](https://docs.vllm.ai/base/#vllm.model_executor.offloader.base.BaseOffloader)

No-op offloader that returns modules as-is without any offloading.

Methods:

-
–[wrap_modules](https://docs.vllm.ai#vllm.model_executor.offloader.NoopOffloader.wrap_modules)Return modules unchanged.


## Source code in `vllm/model_executor/offloader/base.py`


###

`wrap_modules(modules_generator, prefix='')`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.NoopOffloader.wrap_modules)

##

`PrefetchOffloader`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.PrefetchOffloader)

Bases: [BaseOffloader](https://docs.vllm.ai/base/#vllm.model_executor.offloader.base.BaseOffloader)

Prefetching-based offloader with group-based layer selection.

Groups layers and uses async H2D prefetch to hide transfer latency. Uses static buffers and stream synchronization for torch.compile and CUDA graph compatibility.

Parameters:

-

(`group_size`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.PrefetchOffloader(group_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Group every N layers together.

-

(`num_in_group`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.PrefetchOffloader(num_in_group))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Offload this many layers per group (last N of each group).

-

(`prefetch_step`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.PrefetchOffloader(prefetch_step))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of layers to prefetch ahead.

-

(`mode`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.PrefetchOffloader(mode))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'cpu'`

) –Offload mode ("cpu" is currently supported).


Methods:

-
–[join_after_forward](https://docs.vllm.ai#vllm.model_executor.offloader.PrefetchOffloader.join_after_forward)Join copy_stream after model forward completes.

-
–[post_init](https://docs.vllm.ai#vllm.model_executor.offloader.PrefetchOffloader.post_init)Allocate static buffer pool and start initial prefetches.

-
–[sync_prev_onload](https://docs.vllm.ai#vllm.model_executor.offloader.PrefetchOffloader.sync_prev_onload)Sync previous onload operations.

-
–[wrap_modules](https://docs.vllm.ai#vllm.model_executor.offloader.PrefetchOffloader.wrap_modules)Wrap modules with prefetch offloading logic.


## Source code in `vllm/model_executor/offloader/prefetch.py`


|
|

###

`_hook_module_forward(index, module)`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.PrefetchOffloader._hook_module_forward)

Hook module's forward with torch.compile-compatible sync.

## Source code in `vllm/model_executor/offloader/prefetch.py`


###

`_start_prefetch(layer_idx)`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.PrefetchOffloader._start_prefetch)

Called by custom op - start async copy to static buffer.

###

`_wait_for_layer(layer_idx)`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.PrefetchOffloader._wait_for_layer)

Called by custom op - wait for copy to complete.

Synchronization strategy: - During CUDA graph capture: use event-based wait (graph-compatible) - Outside capture (warmup/eager): use wait_stream (more robust)

During capture, we skip wait for pre-capture prefetches because: 1. sync_before_graph_capture() ensures pre-capture work is complete 2. We can't wait on pre-capture events during capture (isolation error)

## Source code in `vllm/model_executor/offloader/prefetch.py`


###

`join_after_forward()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.PrefetchOffloader.join_after_forward)

Join copy_stream after model forward completes.

Call this after the model forward pass but before CUDA graph capture ends. This ensures copy_stream is rejoined for any prefetches started during the forward pass.

We join ALL layers that have _prefetch_in_capture=True, meaning their prefetch was started during capture but not yet waited on (joined). This handles both full and piecewise cudagraph modes correctly: - Full mode: joins layers 0..prefetch_step-1 (prefetched by last layers) - Piecewise mode: joins only layers prefetched by THIS subgraph's layers

## Source code in `vllm/model_executor/offloader/prefetch.py`


###

`post_init()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.PrefetchOffloader.post_init)

Allocate static buffer pool and start initial prefetches.

Note: Parameters have already been offloaded to CPU during wrap_modules() (in _CpuParamOffloader.**init**), so GPU memory is available for the static buffer pool.

## Source code in `vllm/model_executor/offloader/prefetch.py`


###

`sync_prev_onload()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.PrefetchOffloader.sync_prev_onload)

Sync previous onload operations.

Ensures any H2D copies in flight on copy_stream complete before the compute stream continues. Call this before CUDA graph capture/replay or when synchronization is needed.

## Source code in `vllm/model_executor/offloader/prefetch.py`


###

`wrap_modules(modules_generator, prefix='')`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.PrefetchOffloader.wrap_modules)

Wrap modules with prefetch offloading logic.

## Source code in `vllm/model_executor/offloader/prefetch.py`


##

`UVAOffloader`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.UVAOffloader)

Bases: [BaseOffloader](https://docs.vllm.ai/base/#vllm.model_executor.offloader.base.BaseOffloader)

Offloader using Unified Virtual Addressing (UVA) for zero-copy access.

This offloader moves parameters to pinned CPU memory and creates CUDA views using UVA. The GPU can then directly access the CPU memory without explicit transfers, at the cost of PCIe bandwidth (slower than GPU memory).

When UVA is disabled via env var, falls back to a functional_call-based approach that moves parameters on-demand.

Parameters:

-

(`cpu_offload_max_bytes`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.UVAOffloader(cpu_offload_max_bytes))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum bytes to offload to CPU.

-

(`cpu_offload_params`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.UVAOffloader(cpu_offload_params))

, default:[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None`None`

) –Set of parameter name segments to selectively offload. If empty, all parameters are eligible up to the byte limit.


Methods:

-
–[wrap_modules](https://docs.vllm.ai#vllm.model_executor.offloader.UVAOffloader.wrap_modules)Wrap modules with UVA offloading.


## Source code in `vllm/model_executor/offloader/uva.py`


|
|

###

`_maybe_offload_to_cpu(module, prefix='')`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.UVAOffloader._maybe_offload_to_cpu)

Offload module parameters to CPU using UVA if budget allows.

## Source code in `vllm/model_executor/offloader/uva.py`


|
|

###

`wrap_modules(modules_generator, prefix='')`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.UVAOffloader.wrap_modules)

Wrap modules with UVA offloading.

## Source code in `vllm/model_executor/offloader/uva.py`


##

`create_offloader(offload_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.create_offloader)

Create an offloader based on the offload configuration.

Uses the explicit `offload_backend`

selector. When set to `"auto"`

, selects prefetch if `offload_group_size > 0`

, UVA if `cpu_offload_gb > 0`

, otherwise noop.

## Source code in `vllm/model_executor/offloader/base.py`


##

`get_offloader()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.get_offloader)

##

`set_offloader(instance)`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.set_offloader)

Set or reset the global offloader instance.

## Source code in `vllm/model_executor/offloader/base.py`


##

`should_pin_memory()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.should_pin_memory)

Check if pinned memory should be used for weight offloading.

Combines the platform capability check with the user override env var. On unified-memory systems (e.g. GH200) pinned memory eats into GPU memory, so users can disable it via VLLM_WEIGHT_OFFLOADING_DISABLE_PIN_MEMORY.