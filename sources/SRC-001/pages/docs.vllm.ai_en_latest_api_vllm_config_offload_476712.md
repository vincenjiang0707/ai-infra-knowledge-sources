source: https://docs.vllm.ai/en/latest/api/vllm/config/offload/
lastmod: 2026-09-24

#

`vllm.config.offload`

[¶](https://docs.vllm.ai#vllm.config.offload)

Configuration for model weight offloading.

Classes:

-
–[OffloadConfig](https://docs.vllm.ai#vllm.config.offload.OffloadConfig)Configuration for model weight offloading to reduce GPU memory usage.

-
–[PrefetchOffloadConfig](https://docs.vllm.ai#vllm.config.offload.PrefetchOffloadConfig)Configuration for prefetch-based CPU offloading.

-
–[UVAOffloadConfig](https://docs.vllm.ai#vllm.config.offload.UVAOffloadConfig)Configuration for UVA (Unified Virtual Addressing) CPU offloading.


##

`OffloadConfig`

[¶](https://docs.vllm.ai#vllm.config.offload.OffloadConfig)

Configuration for model weight offloading to reduce GPU memory usage.

Methods:

-
–[compute_hash](https://docs.vllm.ai#vllm.config.offload.OffloadConfig.compute_hash)Provide a hash that uniquely identifies all the offload configs.

-
–[validate_offload_config](https://docs.vllm.ai#vllm.config.offload.OffloadConfig.validate_offload_config)Validate offload configuration constraints.


Attributes:

-
([offload_backend](https://docs.vllm.ai#vllm.config.offload.OffloadConfig.offload_backend)`OffloadBackend`

) –The backend for weight offloading. Options:

-
([prefetch](https://docs.vllm.ai#vllm.config.offload.OffloadConfig.prefetch)

) –[PrefetchOffloadConfig](https://docs.vllm.ai#vllm.config.offload.PrefetchOffloadConfig)Parameters for prefetch offloading backend.

-
([uva](https://docs.vllm.ai#vllm.config.offload.OffloadConfig.uva)

) –[UVAOffloadConfig](https://docs.vllm.ai#vllm.config.offload.UVAOffloadConfig)Parameters for UVA offloading backend.


## Source code in `vllm/config/offload.py`


###

`offload_backend = 'auto'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.offload.OffloadConfig.offload_backend)

The backend for weight offloading. Options: - "auto": Selects based on which sub-config has non-default values (prefetch if offload_group_size > 0, uva if cpu_offload_gb > 0). - "uva": UVA (Unified Virtual Addressing) zero-copy offloading. - "prefetch": Async prefetch with group-based layer offloading.

###

`prefetch = Field(default_factory=PrefetchOffloadConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.offload.OffloadConfig.prefetch)

Parameters for prefetch offloading backend.

###

`uva = Field(default_factory=UVAOffloadConfig)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.offload.OffloadConfig.uva)

Parameters for UVA offloading backend.

###

`compute_hash()`

[¶](https://docs.vllm.ai#vllm.config.offload.OffloadConfig.compute_hash)

Provide a hash that uniquely identifies all the offload configs.

All fields are included because PrefetchOffloader patches module forwards and inserts custom ops (wait_prefetch, start_prefetch) into the computation graph. Changing any offload setting can alter which layers are hooked and how prefetch indices are computed, so the compilation cache must distinguish them.

## Source code in `vllm/config/offload.py`


###

`validate_offload_config()`

[¶](https://docs.vllm.ai#vllm.config.offload.OffloadConfig.validate_offload_config)

Validate offload configuration constraints.

## Source code in `vllm/config/offload.py`


##

`PrefetchOffloadConfig`

[¶](https://docs.vllm.ai#vllm.config.offload.PrefetchOffloadConfig)

Configuration for prefetch-based CPU offloading.

Groups layers and uses async H2D prefetch to hide transfer latency.

Attributes:

-
([offload_group_size](https://docs.vllm.ai#vllm.config.offload.PrefetchOffloadConfig.offload_group_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Group every N layers together. Offload last

`offload_num_in_group`

-
([offload_num_in_group](https://docs.vllm.ai#vllm.config.offload.PrefetchOffloadConfig.offload_num_in_group)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of layers to offload per group.

-
([offload_params](https://docs.vllm.ai#vllm.config.offload.PrefetchOffloadConfig.offload_params)

) –[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The set of parameter name segments to target for prefetch offloading.

-
([offload_prefetch_step](https://docs.vllm.ai#vllm.config.offload.PrefetchOffloadConfig.offload_prefetch_step)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of layers to prefetch ahead.


## Source code in `vllm/config/offload.py`


###

`offload_group_size = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.offload.PrefetchOffloadConfig.offload_group_size)

Group every N layers together. Offload last `offload_num_in_group`

layers of each group. Default is 0 (disabled). Example: group_size=8, num_in_group=2 offloads layers 6,7,14,15,22,23,... Unlike cpu_offload_gb, this uses explicit async prefetching to hide transfer latency.

###

`offload_num_in_group = Field(default=1, ge=1)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.offload.PrefetchOffloadConfig.offload_num_in_group)

Number of layers to offload per group. Must be <= offload_group_size. Default is 1.

###

`offload_params = Field(default_factory=set)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.offload.PrefetchOffloadConfig.offload_params)

The set of parameter name segments to target for prefetch offloading. Unmatched parameters are not offloaded. If this set is empty, ALL parameters of each offloaded layer are offloaded. Uses segment matching: "w13_weight" matches "mlp.experts.w13_weight" but not "mlp.experts.w13_weight_scale".

###

`offload_prefetch_step = Field(default=1, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.offload.PrefetchOffloadConfig.offload_prefetch_step)

Number of layers to prefetch ahead. Higher values hide more latency but use more GPU memory. Default is 1.

##

`UVAOffloadConfig`

[¶](https://docs.vllm.ai#vllm.config.offload.UVAOffloadConfig)

Configuration for UVA (Unified Virtual Addressing) CPU offloading.

Uses zero-copy access from CPU-pinned memory. Simple but requires fast CPU-GPU interconnect.

Attributes:

-
([cpu_offload_gb](https://docs.vllm.ai#vllm.config.offload.UVAOffloadConfig.cpu_offload_gb)

) –[float](https://docs.python.org/3/builtins/functions.html#float)The space in GiB to offload to CPU, per GPU. Default is 0, which means

-
([cpu_offload_params](https://docs.vllm.ai#vllm.config.offload.UVAOffloadConfig.cpu_offload_params)

) –[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The set of parameter name segments to target for CPU offloading.


## Source code in `vllm/config/offload.py`


###

`cpu_offload_gb = Field(default=0, ge=0)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.offload.UVAOffloadConfig.cpu_offload_gb)

The space in GiB to offload to CPU, per GPU. Default is 0, which means no offloading. Intuitively, this argument can be seen as a virtual way to increase the GPU memory size. For example, if you have one 24 GB GPU and set this to 10, virtually you can think of it as a 34 GB GPU. Then you can load a 13B model with BF16 weight, which requires at least 26GB GPU memory. Note that this requires fast CPU-GPU interconnect, as part of the model is loaded from CPU memory to GPU memory on the fly in each model forward pass. This uses UVA (Unified Virtual Addressing) for zero-copy access.

###

`cpu_offload_params = Field(default_factory=set)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.config.offload.UVAOffloadConfig.cpu_offload_params)

The set of parameter name segments to target for CPU offloading. Unmatched parameters are not offloaded. If this set is empty, parameters are offloaded non-selectively until the memory limit defined by `cpu_offload_gb`

is reached. Examples: - For parameter name "mlp.experts.w2_weight": - "experts" or "experts.w2_weight" will match. - "expert" or "w2" will NOT match (must be exact segments). This allows distinguishing parameters like "w2_weight" and "w2_weight_scale".