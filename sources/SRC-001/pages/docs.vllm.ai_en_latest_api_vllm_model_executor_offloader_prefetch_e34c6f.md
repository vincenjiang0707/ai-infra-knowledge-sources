source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/offloader/prefetch/
lastmod: 2026-09-23

#

`vllm.model_executor.offloader.prefetch`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch)

Prefetch-based CPU offloading with async prefetching.

Uses static buffers and event-based stream forking for torch.compile + CUDA graph compatibility. Events allow the copy stream to join CUDA graph captures, ensuring H2D copies are properly captured.

Classes:

-
–[ParamInfo](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.ParamInfo)Metadata about an offloaded parameter.

-
–[PrefetchOffloader](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.PrefetchOffloader)Prefetching-based offloader with group-based layer selection.

-
–[StaticBufferPool](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.StaticBufferPool)Pre-allocated GPU buffer pool for offloaded parameters.


##

`ParamInfo`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.ParamInfo)

Metadata about an offloaded parameter.

Attributes:

-
([key](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.ParamInfo.key)

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int), ...],[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int), ...],[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)]Unique key for buffer pool grouping.

-
([num_bytes](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.ParamInfo.num_bytes)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Size in bytes.


## Source code in `vllm/model_executor/offloader/prefetch.py`


###

`key`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.ParamInfo.key)

Unique key for buffer pool grouping.

Includes parameter name to prevent different parameters with the same shape from sharing buffers within the same layer. Parameters with the same name across different layers will share buffers (via slots).

Includes stride because parameters with same shape but different strides need separate buffers to preserve memory layout.

###

`num_bytes`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.ParamInfo.num_bytes)

Size in bytes.

##

`PrefetchOffloader`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.PrefetchOffloader)

Bases: [BaseOffloader](https://docs.vllm.ai/base/#vllm.model_executor.offloader.base.BaseOffloader)

Prefetching-based offloader with group-based layer selection.

Groups layers and uses async H2D prefetch to hide transfer latency. Uses static buffers and stream synchronization for torch.compile and CUDA graph compatibility.

Parameters:

-

(`group_size`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.PrefetchOffloader(group_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Group every N layers together.

-

(`num_in_group`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.PrefetchOffloader(num_in_group))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Offload this many layers per group (last N of each group).

-

(`prefetch_step`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.PrefetchOffloader(prefetch_step))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of layers to prefetch ahead.

-

(`mode`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.PrefetchOffloader(mode))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'cpu'`

) –Offload mode ("cpu" is currently supported).


Methods:

-
–[join_after_forward](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.PrefetchOffloader.join_after_forward)Join copy_stream after model forward completes.

-
–[post_init](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.PrefetchOffloader.post_init)Allocate static buffer pool and start initial prefetches.

-
–[sync_prev_onload](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.PrefetchOffloader.sync_prev_onload)Sync previous onload operations.

-
–[wrap_modules](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.PrefetchOffloader.wrap_modules)Wrap modules with prefetch offloading logic.


## Source code in `vllm/model_executor/offloader/prefetch.py`


|
|

###

`_hook_module_forward(index, module)`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.PrefetchOffloader._hook_module_forward)

Hook module's forward with torch.compile-compatible sync.

## Source code in `vllm/model_executor/offloader/prefetch.py`


###

`_start_prefetch(layer_idx)`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.PrefetchOffloader._start_prefetch)

Called by custom op - start async copy to static buffer.

###

`_wait_for_layer(layer_idx)`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.PrefetchOffloader._wait_for_layer)

Called by custom op - wait for copy to complete.

Synchronization strategy: - During CUDA graph capture: use event-based wait (graph-compatible) - Outside capture (warmup/eager): use wait_stream (more robust)

During capture, we skip wait for pre-capture prefetches because: 1. sync_before_graph_capture() ensures pre-capture work is complete 2. We can't wait on pre-capture events during capture (isolation error)

## Source code in `vllm/model_executor/offloader/prefetch.py`


###

`join_after_forward()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.PrefetchOffloader.join_after_forward)

Join copy_stream after model forward completes.

Call this after the model forward pass but before CUDA graph capture ends. This ensures copy_stream is rejoined for any prefetches started during the forward pass.

We join ALL layers that have _prefetch_in_capture=True, meaning their prefetch was started during capture but not yet waited on (joined). This handles both full and piecewise cudagraph modes correctly: - Full mode: joins layers 0..prefetch_step-1 (prefetched by last layers) - Piecewise mode: joins only layers prefetched by THIS subgraph's layers

## Source code in `vllm/model_executor/offloader/prefetch.py`


###

`post_init()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.PrefetchOffloader.post_init)

Allocate static buffer pool and start initial prefetches.

Note: Parameters have already been offloaded to CPU during wrap_modules() (in _CpuParamOffloader.**init**), so GPU memory is available for the static buffer pool.

## Source code in `vllm/model_executor/offloader/prefetch.py`


###

`sync_prev_onload()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.PrefetchOffloader.sync_prev_onload)

Sync previous onload operations.

Ensures any H2D copies in flight on copy_stream complete before the compute stream continues. Call this before CUDA graph capture/replay or when synchronization is needed.

## Source code in `vllm/model_executor/offloader/prefetch.py`


###

`wrap_modules(modules_generator, prefix='')`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.PrefetchOffloader.wrap_modules)

Wrap modules with prefetch offloading logic.

## Source code in `vllm/model_executor/offloader/prefetch.py`


##

`StaticBufferPool`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.StaticBufferPool)

Pre-allocated GPU buffer pool for offloaded parameters.

Allocates slot_capacity copies of each unique parameter (name, shape, stride, dtype), allowing for double/triple buffering during prefetch.

Buffer slots are reused circularly: layer N uses slot (N % slot_capacity).

The key includes parameter name to prevent different parameters within the same layer from sharing buffers. Parameters with the same name across different layers share buffers via the slot mechanism.

Methods:

-
–[get_buffer](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.StaticBufferPool.get_buffer)Get a static buffer for the given name/shape/stride/dtype/slot.


## Source code in `vllm/model_executor/offloader/prefetch.py`


###

`get_buffer(name, shape, stride, dtype, slot_idx)`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch.StaticBufferPool.get_buffer)

Get a static buffer for the given name/shape/stride/dtype/slot.

## Source code in `vllm/model_executor/offloader/prefetch.py`


##

`_BaseParamOffloader`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._BaseParamOffloader)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for parameter offloading strategies.

Methods:

-
–[assign_static_buffer](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._BaseParamOffloader.assign_static_buffer)Point parameter data to GPU static buffer.

-
–[create](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._BaseParamOffloader.create)Factory method to create appropriate offloader for mode.

-
–[post_init](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._BaseParamOffloader.post_init)Initialize offloading (move parameter to storage).

-
–[sync_cpu_storage](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._BaseParamOffloader.sync_cpu_storage)Sync CPU storage with current param.data.


## Source code in `vllm/model_executor/offloader/prefetch.py`


###

`_param`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._BaseParamOffloader._param)

Get the parameter being offloaded.

Supports dotted names (e.g. 'self_attn.qkv_proj.weight') by traversing the module hierarchy.

###

`assign_static_buffer(gpu_buffer)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._BaseParamOffloader.assign_static_buffer)

###

`create(mode, **kwargs)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._BaseParamOffloader.create)

Factory method to create appropriate offloader for mode.

## Source code in `vllm/model_executor/offloader/prefetch.py`


###

`post_init()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._BaseParamOffloader.post_init)

###

`sync_cpu_storage()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._BaseParamOffloader.sync_cpu_storage)

Sync CPU storage with current param.data.

Called after process_weights_after_loading to update _cpu_storage with the final processed weights.

##

`_CpuParamOffloader`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._CpuParamOffloader)

Bases: [_BaseParamOffloader](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._BaseParamOffloader)

Offload parameter to pinned CPU memory.

Uses GPU static buffers as the actual parameter, with CPU storage kept separately. This ensures torch.compile sees GPU tensors at trace time.

The offloading happens in two phases: 1. **init**() - copies GPU data to CPU, frees GPU memory immediately 2. assign_static_buffer() - points param.data to GPU static buffer

Methods:

-
–[assign_static_buffer](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._CpuParamOffloader.assign_static_buffer)Point parameter data to GPU static buffer.

-
–[post_init](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._CpuParamOffloader.post_init)No-op: offloading done in offload_to_cpu/assign_static_buffer.

-
–[sync_cpu_storage](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._CpuParamOffloader.sync_cpu_storage)Sync CPU storage with current param.data.


## Source code in `vllm/model_executor/offloader/prefetch.py`


|
|

###

`_offload_to_cpu_internal()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._CpuParamOffloader._offload_to_cpu_internal)

Copy parameter data to pinned CPU storage and free GPU memory.

This replaces param.data with CPU storage, allowing weight loading to continue writing to CPU memory. GPU memory is freed when the original GPU tensor is garbage collected.

## Source code in `vllm/model_executor/offloader/prefetch.py`


###

`_update_cpu_storage_from_param()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._CpuParamOffloader._update_cpu_storage_from_param)

Update _cpu_storage from current param.data, ensuring pinned memory.

After process_weights_after_loading, device_loading_context creates non-pinned CPU tensors via `p.data = p.data.to("cpu")`

. Using non-pinned memory with `copy_(src, non_blocking=True)`

causes CUDA to perform a stream synchronization before the copy, breaking the event-based fork synchronization and potentially allowing the copy to overwrite the GPU buffer while the compute stream still reads it.

This method ensures _cpu_storage always uses pinned memory when available, re-pinning if necessary.

## Source code in `vllm/model_executor/offloader/prefetch.py`


###

`assign_static_buffer(gpu_buffer)`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._CpuParamOffloader.assign_static_buffer)

Point parameter data to GPU static buffer.

This is called after weight loading AND process_weights_after_loading complete. At this point: - param.data may have been replaced by device_loading_context (which creates new CPU tensors after quantization processing) - We need to update _cpu_storage to point to current param.data so that prefetch copies the processed weights, not stale data - Then point param.data to the GPU buffer for torch.compile

## Source code in `vllm/model_executor/offloader/prefetch.py`


###

`post_init()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._CpuParamOffloader.post_init)

###

`sync_cpu_storage()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._CpuParamOffloader.sync_cpu_storage)

Sync CPU storage with current param.data.

Called after process_weights_after_loading to update _cpu_storage with the final processed weights. This is critical because: 1. process_weights_after_loading may transform weights (quantization) 2. device_loading_context creates NEW CPU tensors when moving back 3. Our old _cpu_storage would have pre-processed or stale data

If the parameter no longer exists on the module (e.g. transient KV-cache scale parameters such as k_scale/v_scale that are created by BaseKVCacheMethod.create_weights() and then deleted by process_weights_after_loading() after copying their values into permanent _k_scale buffers), the offloader marks itself as deleted and skips the sync. The caller (_ModuleOffloader.sync_cpu_storage) is responsible for removing these stale entries.

## Source code in `vllm/model_executor/offloader/prefetch.py`


##

`_ModuleOffloader`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._ModuleOffloader)

Manages offloading for a single module.

Uses static buffers from a shared pool instead of dynamic allocation.

Methods:

-
–[assign_buffer_slot](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._ModuleOffloader.assign_buffer_slot)Assign this module to a buffer slot in the pool.

-
–[get_param_infos](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._ModuleOffloader.get_param_infos)Get parameter metadata for buffer pool allocation.

-
–[post_init](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._ModuleOffloader.post_init)Collect total offloaded bytes (offloading already done in

**init**). -
–[start_onload_to_static](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._ModuleOffloader.start_onload_to_static)Start async copy from CPU storage to GPU buffer.

-
–[sync_cpu_storage](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._ModuleOffloader.sync_cpu_storage)Sync CPU storage with current param.data.


## Source code in `vllm/model_executor/offloader/prefetch.py`


|
|

###

`assign_buffer_slot(pool, slot_idx)`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._ModuleOffloader.assign_buffer_slot)

Assign this module to a buffer slot in the pool.

Also assigns static GPU buffers to each parameter offloader, which moves the parameter data to point to the GPU buffer.

## Source code in `vllm/model_executor/offloader/prefetch.py`


###

`get_param_infos()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._ModuleOffloader.get_param_infos)

Get parameter metadata for buffer pool allocation.

Note: sync_cpu_storage() must be called before this method to ensure _cpu_storage reflects the final processed weights (after quantization).

## Source code in `vllm/model_executor/offloader/prefetch.py`


###

`post_init()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._ModuleOffloader.post_init)

Collect total offloaded bytes (offloading already done in **init**).

## Source code in `vllm/model_executor/offloader/prefetch.py`


###

`start_onload_to_static()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._ModuleOffloader.start_onload_to_static)

Start async copy from CPU storage to GPU buffer.

Uses event-based forking to join copy_stream to CUDA graph capture. This ensures H2D copies are properly captured when recording a graph.

IMPORTANT: We must wait for the compute stream before copying, because the previous layer's forward may still be using the buffer (GPU ops are async). Without this sync, we could overwrite the buffer while it's being read.

## Source code in `vllm/model_executor/offloader/prefetch.py`


###

`sync_cpu_storage()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._ModuleOffloader.sync_cpu_storage)

Sync CPU storage with current param.data.

Called after process_weights_after_loading to ensure _cpu_storage contains the final processed weights, not stale pre-loading data.

Parameters whose underlying nn.Parameter was deleted by process_weights_after_loading (e.g. transient KV-cache scale params) are pruned from self._param_offloaders so they do not participate in buffer-pool allocation or prefetching.

## Source code in `vllm/model_executor/offloader/prefetch.py`


##

`_get_next_prefetch_index(index, prefetch_step, module_count)`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.prefetch._get_next_prefetch_index)

Return a refill target that preserves static-buffer slot ownership.