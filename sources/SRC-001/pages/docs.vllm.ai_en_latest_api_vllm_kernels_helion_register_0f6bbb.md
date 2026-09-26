source: https://docs.vllm.ai/en/latest/api/vllm/kernels/helion/register/
lastmod: 2026-09-24

#

`vllm.kernels.helion.register`

[¶](https://docs.vllm.ai#vllm.kernels.helion.register)

vLLM Helion kernel registration with pre-tuned config selection.

This module leverages Helion's internal config selection infrastructure to use pre-tuned configs instead of runtime autotuning.

### How Helion Normally Works[¶](https://docs.vllm.ai#vllm.kernels.helion.register--how-helion-normally-works)

For each kernel invocation, Helion: 1. Computes a cache key from input arguments 2. Looks up the key in its internal compilation cache 3. On cache miss, runs autotuning to find the best config 4. Compiles and caches the kernel with that config

### How We Override It[¶](https://docs.vllm.ai#vllm.kernels.helion.register--how-we-override-it)

We override two Helion hooks to use pre-tuned configs:

-
**key**: We provide a key function (derived from config_picker) that computes cache keys matching our pre-tuned config keys. This ensures Helion's internal cache uses keys that correspond to configs we've prepared. -
**autotuner_fn**: We provide PresetConfigSearch which, instead of autotuning, simply returns the pre-tuned config for the computed key. On cache miss, Helion calls our autotuner which returns the author-prepared config.

Both hooks use the same config_picker logic to ensure the cache key computed by key matches the config returned by the autotuner.

### Key Classes[¶](https://docs.vllm.ai#vllm.kernels.helion.register--key-classes)

- HelionKernelWrapper: Wraps raw kernel + config_picker, creates configured kernels
- ConfiguredHelionKernel: Platform-specific kernel with pre-tuned configs
- PresetConfigSearch: Custom autotuner that returns pre-tuned configs

Classes:

-
–[ConfiguredHelionKernel](https://docs.vllm.ai#vllm.kernels.helion.register.ConfiguredHelionKernel)A configured Helion kernel bound to a specific platform.

-
–[HelionKernelWrapper](https://docs.vllm.ai#vllm.kernels.helion.register.HelionKernelWrapper)Wrapper for Helion kernels with pre-tuned config selection and HOP support.

-
–[PresetConfigSearch](https://docs.vllm.ai#vllm.kernels.helion.register.PresetConfigSearch)Custom autotuner that uses a preset config selector instead of autotuning.


Functions:

-
–[register_kernel](https://docs.vllm.ai#vllm.kernels.helion.register.register_kernel)Register a Helion kernel with pre-tuned config selection.


##

`ConfiguredHelionKernel`

[¶](https://docs.vllm.ai#vllm.kernels.helion.register.ConfiguredHelionKernel)

A configured Helion kernel bound to a specific platform.

## Source code in `vllm/kernels/helion/register.py`


|
|

###

`_create_key_computer()`

[¶](https://docs.vllm.ai#vllm.kernels.helion.register.ConfiguredHelionKernel._create_key_computer)

Create a key computer function derived from the config picker.

The returned function receives kernel arguments unpacked (*args) to match Helion's key signature (called as self._key_fn(*args)).

## Source code in `vllm/kernels/helion/register.py`


##

`HelionKernelWrapper`

[¶](https://docs.vllm.ai#vllm.kernels.helion.register.HelionKernelWrapper)

Wrapper for Helion kernels with pre-tuned config selection and HOP support.

Methods:

-
–[run_autotune](https://docs.vllm.ai#vllm.kernels.helion.register.HelionKernelWrapper.run_autotune)Run autotuning for a single input configuration.


## Source code in `vllm/kernels/helion/register.py`


|
|

###

`run_autotune(inputs, autotune_effort='quick')`

[¶](https://docs.vllm.ai#vllm.kernels.helion.register.HelionKernelWrapper.run_autotune)

Run autotuning for a single input configuration.

## Source code in `vllm/kernels/helion/register.py`


##

`PresetConfigSearch`

[¶](https://docs.vllm.ai#vllm.kernels.helion.register.PresetConfigSearch)

Bases: `BaseAutotuner`


Custom autotuner that uses a preset config selector instead of autotuning.

## Source code in `vllm/kernels/helion/register.py`


##

`_register_vllm_helion_dynamo_variable()`

[¶](https://docs.vllm.ai#vllm.kernels.helion.register._register_vllm_helion_dynamo_variable)

Register HelionKernelWrapper with Dynamo's VariableBuilder.

When Dynamo encounters a HelionKernelWrapper during tracing, this extracts the underlying Helion Kernel and delegates to Helion's own registered Kernel handler, which handles HOP emission, side table registration, and inductor lowering setup.

## Source code in `vllm/kernels/helion/register.py`


##

`register_kernel(op_name=None, *, config_picker, fake_impl=None, mutates_args=None, helion_settings=None, input_generator=None)`

[¶](https://docs.vllm.ai#vllm.kernels.helion.register.register_kernel)

Register a Helion kernel with pre-tuned config selection.

Parameters:

-

(`op_name`

[¶](https://docs.vllm.ai#vllm.kernels.helion.register.register_kernel(op_name))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –Name to register the op under. Defaults to the function name.

-

(`fake_impl`

[¶](https://docs.vllm.ai#vllm.kernels.helion.register.register_kernel(fake_impl))

, default:[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)| None`None`

) –Optional meta/fake implementation for tracing.

-

(`mutates_args`

[¶](https://docs.vllm.ai#vllm.kernels.helion.register.register_kernel(mutates_args))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None`None`

) –Names of arguments the kernel mutates in place.

-

(`helion_settings`

[¶](https://docs.vllm.ai#vllm.kernels.helion.register.register_kernel(helion_settings))`Settings | None`

, default:`None`

) –Optional Helion settings override.

-

(`config_picker`

[¶](https://docs.vllm.ai#vllm.kernels.helion.register.register_kernel(config_picker))`ConfigPicker`

) –Required. Receives

`(args, config_keys)`

where each config key is a`dict[str, Any]`

mapping parameter names to values. Return the best-matching dict, or`None`

to fall back to the default config.Example::

`def pick_config(args, config_keys): x = args[0] best = min(config_keys, key=lambda k: abs(k["size"] - x.shape[0])) return best`

-

(`input_generator`

[¶](https://docs.vllm.ai#vllm.kernels.helion.register.register_kernel(input_generator))

, default:[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[],[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[CaseKey](https://docs.vllm.ai/case_key/#vllm.kernels.helion.case_key.CaseKey),[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Any](https://docs.python.org/3/library/typing.html#typing.Any), ...]]] | None`None`

) –Optional. Returns

`dict[str, tuple]`

where each key is a serialized config key and each value is a tuple of arguments to pass to the kernel.Example::

`def generate_inputs(): return { "4096": (torch.randn(4096, device="cuda"), 0.5), "8192": (torch.randn(8192, device="cuda"), 0.5), }`


## Source code in `vllm/kernels/helion/register.py`


|
|