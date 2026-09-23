source: https://docs.vllm.ai/en/latest/api/vllm/kernels/helion/
lastmod: 2026-09-23

#

`vllm.kernels.helion`

[¶](https://docs.vllm.ai#vllm.kernels.helion)

Helion integration for vLLM.

Modules:

-
–[case_key](https://docs.vllm.ai/case_key/#vllm.kernels.helion.case_key)Structured key for identifying kernel config/autotune/benchmark cases.

-
–[config_manager](https://docs.vllm.ai/config_manager/#vllm.kernels.helion.config_manager)Configuration management for Helion kernels.

-
–[ops](https://docs.vllm.ai/ops/#vllm.kernels.helion.ops)Helion kernel implementation.

-
–[register](https://docs.vllm.ai/register/#vllm.kernels.helion.register)vLLM Helion kernel registration with pre-tuned config selection.

-
–[utils](https://docs.vllm.ai/utils/#vllm.kernels.helion.utils)Utility functions for Helion kernel management.


Classes:

-
–[CaseKey](https://docs.vllm.ai#vllm.kernels.helion.CaseKey)Immutable, hashable dict for identifying kernel cases.

-
–[ConfigManager](https://docs.vllm.ai#vllm.kernels.helion.ConfigManager)File-level configuration management for Helion kernels (global singleton).

-
–[ConfigSet](https://docs.vllm.ai#vllm.kernels.helion.ConfigSet)In-memory collection of Helion configs with lookup/query capabilities.

-
–[ConfiguredHelionKernel](https://docs.vllm.ai#vllm.kernels.helion.ConfiguredHelionKernel)A configured Helion kernel bound to a specific platform.

-
–[HelionKernelWrapper](https://docs.vllm.ai#vllm.kernels.helion.HelionKernelWrapper)Wrapper for Helion kernels with pre-tuned config selection and HOP support.


Functions:

-
–[canonicalize_gpu_name](https://docs.vllm.ai#vllm.kernels.helion.canonicalize_gpu_name)Canonicalize GPU name for use as a platform identifier.

-
–[register_kernel](https://docs.vllm.ai#vllm.kernels.helion.register_kernel)Register a Helion kernel with pre-tuned config selection.


##

`CaseKey`

[¶](https://docs.vllm.ai#vllm.kernels.helion.CaseKey)

Immutable, hashable dict for identifying kernel cases.

Used as the key for config lookup, autotuning, benchmarking, and input generation. Behaves like a read-only dict and can be used as a dict key or in sets.

The canonical string form (`__str__`

) is stable JSON with sorted keys. Use `CaseKey.default()`

for the default/fallback key. The regular constructor requires at least one key-value pair::

```
CaseKey({"intermediate": 2048, "numtokens": 256})
CaseKey.default() # default/fallback
```


Methods:

-
–[default](https://docs.vllm.ai#vllm.kernels.helion.CaseKey.default)Create a default case key (empty).

-
–[is_default](https://docs.vllm.ai#vllm.kernels.helion.CaseKey.is_default)Return True if this is the default case key (empty).


## Source code in `vllm/kernels/helion/case_key.py`


###

`default()`

`classmethod`

[¶](https://docs.vllm.ai#vllm.kernels.helion.CaseKey.default)

##

`ConfigManager`

[¶](https://docs.vllm.ai#vllm.kernels.helion.ConfigManager)

File-level configuration management for Helion kernels (global singleton).

Methods:

-
–[reset_instance](https://docs.vllm.ai#vllm.kernels.helion.ConfigManager.reset_instance)For testing purposes only.

-
–[save_configs](https://docs.vllm.ai#vllm.kernels.helion.ConfigManager.save_configs)Save configs for a kernel/platform, merging with existing.


## Source code in `vllm/kernels/helion/config_manager.py`


|
|

###

`reset_instance()`

`classmethod`

[¶](https://docs.vllm.ai#vllm.kernels.helion.ConfigManager.reset_instance)

###

`save_configs(kernel_name, platform, configs)`

[¶](https://docs.vllm.ai#vllm.kernels.helion.ConfigManager.save_configs)

Save configs for a kernel/platform, merging with existing.

## Source code in `vllm/kernels/helion/config_manager.py`


##

`ConfigSet`

[¶](https://docs.vllm.ai#vllm.kernels.helion.ConfigSet)

In-memory collection of Helion configs with lookup/query capabilities.

Configs are stored keyed by `CaseKey`

. The default config uses `CaseKey.default()`

as its key.

Methods:

-
–[to_config_entries](https://docs.vllm.ai#vllm.kernels.helion.ConfigSet.to_config_entries)Serialize to config entries format for JSON output.

-
–[to_dict](https://docs.vllm.ai#vllm.kernels.helion.ConfigSet.to_dict)Return configs as a nested dict (platform -> key -> config).


## Source code in `vllm/kernels/helion/config_manager.py`


|
|

###

`to_config_entries()`

[¶](https://docs.vllm.ai#vllm.kernels.helion.ConfigSet.to_config_entries)

Serialize to config entries format for JSON output.

## Source code in `vllm/kernels/helion/config_manager.py`


###

`to_dict()`

[¶](https://docs.vllm.ai#vllm.kernels.helion.ConfigSet.to_dict)

Return configs as a nested dict (platform -> key -> config).

## Source code in `vllm/kernels/helion/config_manager.py`


##

`ConfiguredHelionKernel`

[¶](https://docs.vllm.ai#vllm.kernels.helion.ConfiguredHelionKernel)

A configured Helion kernel bound to a specific platform.

## Source code in `vllm/kernels/helion/register.py`


|
|

###

`_create_key_computer()`

[¶](https://docs.vllm.ai#vllm.kernels.helion.ConfiguredHelionKernel._create_key_computer)

Create a key computer function derived from the config picker.

The returned function receives kernel arguments unpacked (*args) to match Helion's key signature (called as self._key_fn(*args)).

## Source code in `vllm/kernels/helion/register.py`


##

`HelionKernelWrapper`

[¶](https://docs.vllm.ai#vllm.kernels.helion.HelionKernelWrapper)

Wrapper for Helion kernels with pre-tuned config selection and HOP support.

Methods:

-
–[run_autotune](https://docs.vllm.ai#vllm.kernels.helion.HelionKernelWrapper.run_autotune)Run autotuning for a single input configuration.


## Source code in `vllm/kernels/helion/register.py`


|
|

###

`run_autotune(inputs, autotune_effort='quick')`

[¶](https://docs.vllm.ai#vllm.kernels.helion.HelionKernelWrapper.run_autotune)

Run autotuning for a single input configuration.

## Source code in `vllm/kernels/helion/register.py`


##

`canonicalize_gpu_name(name)`

[¶](https://docs.vllm.ai#vllm.kernels.helion.canonicalize_gpu_name)

Canonicalize GPU name for use as a platform identifier.

Converts to lowercase, replaces separators with underscores, and maps known variant names to their canonical form via _GPU_NAME_ALIASES. e.g., "NVIDIA H100 80GB HBM3" -> "nvidia_h100" "NVIDIA A100-SXM4-80GB" -> "nvidia_a100" "AMD Instinct MI300X" -> "amd_instinct_mi300x"

## Source code in `vllm/kernels/helion/utils.py`


##

`register_kernel(op_name=None, *, config_picker, fake_impl=None, mutates_args=None, helion_settings=None, input_generator=None)`

[¶](https://docs.vllm.ai#vllm.kernels.helion.register_kernel)

Register a Helion kernel with pre-tuned config selection.

Parameters:

-

(`op_name`

[¶](https://docs.vllm.ai#vllm.kernels.helion.register_kernel(op_name))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –Name to register the op under. Defaults to the function name.

-

(`fake_impl`

[¶](https://docs.vllm.ai#vllm.kernels.helion.register_kernel(fake_impl))

, default:[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)| None`None`

) –Optional meta/fake implementation for tracing.

-

(`mutates_args`

[¶](https://docs.vllm.ai#vllm.kernels.helion.register_kernel(mutates_args))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None`None`

) –Names of arguments the kernel mutates in place.

-

(`helion_settings`

[¶](https://docs.vllm.ai#vllm.kernels.helion.register_kernel(helion_settings))`Settings | None`

, default:`None`

) –Optional Helion settings override.

-

(`config_picker`

[¶](https://docs.vllm.ai#vllm.kernels.helion.register_kernel(config_picker))`ConfigPicker`

) –Required. Receives

`(args, config_keys)`

where each config key is a`dict[str, Any]`

mapping parameter names to values. Return the best-matching dict, or`None`

to fall back to the default config.Example::

`def pick_config(args, config_keys): x = args[0] best = min(config_keys, key=lambda k: abs(k["size"] - x.shape[0])) return best`

-

(`input_generator`

[¶](https://docs.vllm.ai#vllm.kernels.helion.register_kernel(input_generator))

, default:[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[],[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[CaseKey](https://docs.vllm.ai/case_key/#vllm.kernels.helion.case_key.CaseKey),[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Any](https://docs.python.org/3/library/typing.html#typing.Any), ...]]] | None`None`

) –Optional. Returns

`dict[str, tuple]`

where each key is a serialized config key and each value is a tuple of arguments to pass to the kernel.Example::

`def generate_inputs(): return { "4096": (torch.randn(4096, device="cuda"), 0.5), "8192": (torch.randn(8192, device="cuda"), 0.5), }`


## Source code in `vllm/kernels/helion/register.py`


|
|