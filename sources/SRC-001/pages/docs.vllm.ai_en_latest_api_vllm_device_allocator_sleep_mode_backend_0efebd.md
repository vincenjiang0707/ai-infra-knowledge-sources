source: https://docs.vllm.ai/en/latest/api/vllm/device_allocator/sleep_mode_backend/
lastmod: 2026-09-24

#

`vllm.device_allocator.sleep_mode_backend`

[¶](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend)

Pluggable sleep-mode backends (RFC #34303).

vLLM's sleep/wake-up today is hard-wired to `CuMemAllocator`

: the GPU worker calls `allocator.sleep(...)`

/ `allocator.wake_up(...)`

directly. RFC #34303 proposes additional mechanisms for freeing and restoring GPU state - CUDA process checkpoint, CRIU, durable snapshot/restore - that share the *dispatch* (`/sleep`

endpoint -> engine -> executor -> worker) but differ in *mechanism* and in which resources they preserve (NCCL communicators, compiled kernels, CUDA graphs, survival across process restart).

This module introduces a thin backend abstraction so those mechanisms can be selected by name without changing the public API. The default `cumem`

backend wraps today's `CuMemAllocator`

path 1:1, so existing users see no behavior change. The factory mirrors `KVConnectorFactory`

and lets third-party backends register through a `vllm.general_plugins`

entry point at import time.

Classes:

-
–[CuMemBackend](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.CuMemBackend)Default backend.

-
–[SleepModeBackend](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackend)Interface for a mechanism that frees and restores GPU state.

-
–[SleepModeBackendFactory](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackendFactory)Registry and resolver for sleep-mode backends.


##

`CuMemBackend`

[¶](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.CuMemBackend)

Bases: [SleepModeBackend](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackend)

Default backend.

Wraps the platform sleep-mode allocator exactly as the GPU worker did before this abstraction existed, so behavior is identical to vLLM's current sleep/wake-up. `get_mem_allocator_instance()`

resolves to `CuMemAllocator`

on CUDA and `XpuMemAllocator`

on XPU; suspend offloads per-allocation between GPU and host, with NCCL buffers left untouched (they are allocated outside the allocator pool).

## Source code in `vllm/device_allocator/sleep_mode_backend.py`


##

`SleepModeBackend`

[¶](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackend)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Interface for a mechanism that frees and restores GPU state.

A backend owns the *mechanism* of suspend/resume. The dispatch path (`/sleep`

endpoint -> engine -> executor -> worker) is shared across all backends and lives outside this class.

Capability flags are `@classmethod`

so callers (executor, `/health`

, AUTO selection) can introspect a backend without instantiating it, matching the capability-flag convention used by attention backends.

Methods:

-
–[discard](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackend.discard)Discard selected tagged allocations without preserving contents.

-
–[is_supported](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackend.is_supported)Whether this backend can run on the current platform/driver.

-
–[preserves_communicators](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackend.preserves_communicators)If False, collective communicators (e.g. NCCL) are destroyed by

-
–[preserves_compiled_artifacts](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackend.preserves_compiled_artifacts)If True, torch.compile / JIT kernels survive suspend/resume and need

-
–[preserves_graphs_with_communicators](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackend.preserves_graphs_with_communicators)If True, CUDA graphs containing collective communicators (e.g. NCCL)

-
–[resume](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackend.resume)Restore previously-suspended GPU state.

-
–[state](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackend.state)Current lifecycle state. Lets

`/health`

distinguish a healthy-idle -
–[supports_durable_storage](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackend.supports_durable_storage)If True, suspended state can be persisted beyond the process

-
–[suspend](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackend.suspend)Free GPU state.


## Source code in `vllm/device_allocator/sleep_mode_backend.py`


###

`discard(tags)`

[¶](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackend.discard)

Discard selected tagged allocations without preserving contents.

## Source code in `vllm/device_allocator/sleep_mode_backend.py`


###

`is_supported()`

`classmethod`

[¶](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackend.is_supported)

###

`preserves_communicators()`

`classmethod`

[¶](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackend.preserves_communicators)

If False, collective communicators (e.g. NCCL) are destroyed by `suspend`

and the executor must re-initialize them on `resume`

.

###

`preserves_compiled_artifacts()`

`classmethod`

[¶](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackend.preserves_compiled_artifacts)

If True, torch.compile / JIT kernels survive suspend/resume and need not be recompiled on resume.

###

`preserves_graphs_with_communicators()`

`classmethod`

[¶](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackend.preserves_graphs_with_communicators)

If True, CUDA graphs containing collective communicators (e.g. NCCL) stay valid after resume. False when communicators are rebuilt (embedded comm handles go stale).

## Source code in `vllm/device_allocator/sleep_mode_backend.py`


###

`resume(tags=None)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackend.resume)

Restore previously-suspended GPU state.

`tags`

optionally limits which tagged allocations are restored (e.g. `["weights"]`

or `["kv_cache"]`

).

## Source code in `vllm/device_allocator/sleep_mode_backend.py`


###

`state()`

[¶](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackend.state)

Current lifecycle state. Lets `/health`

distinguish a healthy-idle (suspended) engine from a healthy-serving one (see RFC #34303).

###

`supports_durable_storage()`

`classmethod`

[¶](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackend.supports_durable_storage)

If True, suspended state can be persisted beyond the process lifetime (disk or object storage) and restored in a new process.

###

`suspend(level=1)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackend.suspend)

Free GPU state.

`level`

follows existing sleep-mode semantics: level 1 offloads weights to host RAM (restorable in-process); level 2 discards weights (reloaded from the model source on resume).

## Source code in `vllm/device_allocator/sleep_mode_backend.py`


##

`SleepModeBackendFactory`

[¶](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackendFactory)

Registry and resolver for sleep-mode backends.

Mirrors `KVConnectorFactory`

: lazy module/class registration and a built-in registry populated at import time. Third-party backends register the same way from a `vllm.general_plugins`

entry point.

Methods:

-
–[create_backend](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackendFactory.create_backend)Instantiate the backend selected by

`model_config`

. -
–[get_backend_class](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackendFactory.get_backend_class)Resolve a registered backend class by name.

-
–[register_backend](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackendFactory.register_backend)Register a backend with a lazy-loading module and class name.


## Source code in `vllm/device_allocator/sleep_mode_backend.py`


###

`create_backend(model_config)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackendFactory.create_backend)

Instantiate the backend selected by `model_config`

.

## Source code in `vllm/device_allocator/sleep_mode_backend.py`


###

`get_backend_class(name)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackendFactory.get_backend_class)

Resolve a registered backend class by name.

## Source code in `vllm/device_allocator/sleep_mode_backend.py`


###

`register_backend(name, module_path, class_name)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.device_allocator.sleep_mode_backend.SleepModeBackendFactory.register_backend)

Register a backend with a lazy-loading module and class name.