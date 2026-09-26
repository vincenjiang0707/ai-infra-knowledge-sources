source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/offloader/base/
lastmod: 2026-09-24

#

`vllm.model_executor.offloader.base`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.base)

Base classes for model parameter offloading.

Classes:

-
–[BaseOffloader](https://docs.vllm.ai#vllm.model_executor.offloader.base.BaseOffloader)Base class for model parameter offloading strategies.

-
–[NoopOffloader](https://docs.vllm.ai#vllm.model_executor.offloader.base.NoopOffloader)No-op offloader that returns modules as-is without any offloading.


Functions:

-
–[create_offloader](https://docs.vllm.ai#vllm.model_executor.offloader.base.create_offloader)Create an offloader based on the offload configuration.

-
–[get_offloader](https://docs.vllm.ai#vllm.model_executor.offloader.base.get_offloader)Get the global offloader instance.

-
–[set_offloader](https://docs.vllm.ai#vllm.model_executor.offloader.base.set_offloader)Set or reset the global offloader instance.

-
–[should_pin_memory](https://docs.vllm.ai#vllm.model_executor.offloader.base.should_pin_memory)Check if pinned memory should be used for weight offloading.


##

`BaseOffloader`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.base.BaseOffloader)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for model parameter offloading strategies.

Offloaders control how model parameters are stored and loaded during inference. Different strategies trade memory for compute/transfer time.

Methods:

-
–[join_after_forward](https://docs.vllm.ai#vllm.model_executor.offloader.base.BaseOffloader.join_after_forward)Join streams after forward. Override in subclasses.

-
–[post_init](https://docs.vllm.ai#vllm.model_executor.offloader.base.BaseOffloader.post_init)Called after model construction completes.

-
–[sync_prev_onload](https://docs.vllm.ai#vllm.model_executor.offloader.base.BaseOffloader.sync_prev_onload)Sync previous onload operations. Override in subclasses.

-
–[wrap_modules](https://docs.vllm.ai#vllm.model_executor.offloader.base.BaseOffloader.wrap_modules)Wrap modules with offloading logic.


Attributes:

-
([supports_tower_offload](https://docs.vllm.ai#vllm.model_executor.offloader.base.BaseOffloader.supports_tower_offload)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether

`wrap_modules`

also accepts modules routed by

## Source code in `vllm/model_executor/offloader/base.py`


###

`supports_tower_offload = False`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.base.BaseOffloader.supports_tower_offload)

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

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.base.BaseOffloader._start_prefetch)

###

`_wait_for_layer(layer_idx)`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.base.BaseOffloader._wait_for_layer)

###

`join_after_forward()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.base.BaseOffloader.join_after_forward)

###

`post_init()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.base.BaseOffloader.post_init)

Called after model construction completes.

Offloaders can use this to: - Finalize parameter storage - Start initial prefetching - Allocate shared resources

###

`sync_prev_onload()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.base.BaseOffloader.sync_prev_onload)

###

`wrap_modules(modules_generator, prefix='')`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.base.BaseOffloader.wrap_modules)

Wrap modules with offloading logic.

Parameters:

-

(`modules_generator`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.base.BaseOffloader.wrap_modules(modules_generator))

) –[Generator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator)[[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module), None, None]Generator yielding modules to potentially offload.

-

(`prefix`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.base.BaseOffloader.wrap_modules(prefix))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`''`

) –Name prefix prepended to parameter names before matching them against the offloading parameter set. Used when the modules are not the full model, so that name segments stay fully qualified (e.g.

`visual`

for a tower module).

Returns:

## Source code in `vllm/model_executor/offloader/base.py`


##

`NoopOffloader`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.base.NoopOffloader)

Bases: [BaseOffloader](https://docs.vllm.ai#vllm.model_executor.offloader.base.BaseOffloader)

No-op offloader that returns modules as-is without any offloading.

Methods:

-
–[wrap_modules](https://docs.vllm.ai#vllm.model_executor.offloader.base.NoopOffloader.wrap_modules)Return modules unchanged.


## Source code in `vllm/model_executor/offloader/base.py`


###

`wrap_modules(modules_generator, prefix='')`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.base.NoopOffloader.wrap_modules)

##

`create_offloader(offload_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.base.create_offloader)

Create an offloader based on the offload configuration.

Uses the explicit `offload_backend`

selector. When set to `"auto"`

, selects prefetch if `offload_group_size > 0`

, UVA if `cpu_offload_gb > 0`

, otherwise noop.

## Source code in `vllm/model_executor/offloader/base.py`


##

`get_offloader()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.base.get_offloader)

##

`set_offloader(instance)`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.base.set_offloader)

Set or reset the global offloader instance.

## Source code in `vllm/model_executor/offloader/base.py`


##

`should_pin_memory()`

[¶](https://docs.vllm.ai#vllm.model_executor.offloader.base.should_pin_memory)

Check if pinned memory should be used for weight offloading.

Combines the platform capability check with the user override env var. On unified-memory systems (e.g. GH200) pinned memory eats into GPU memory, so users can disable it via VLLM_WEIGHT_OFFLOADING_DISABLE_PIN_MEMORY.