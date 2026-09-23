source: https://docs.vllm.ai/en/latest/api/vllm/compilation/caching/
lastmod: 2026-09-23

#

`vllm.compilation.caching`

[¶](https://docs.vllm.ai#vllm.compilation.caching)

Classes:

-
–[StandaloneCompiledArtifacts](https://docs.vllm.ai#vllm.compilation.caching.StandaloneCompiledArtifacts)Storage for standalone compiled artifacts with content-based deduplication.

-
–[VllmSerializableFunction](https://docs.vllm.ai#vllm.compilation.caching.VllmSerializableFunction)A wrapper around a compiled function by vllm. It will forward the tensor


Functions:

-
–[reconstruct_serializable_fn_from_mega_artifact](https://docs.vllm.ai#vllm.compilation.caching.reconstruct_serializable_fn_from_mega_artifact)Construct a VllmSerializableFunction from cached inductor artifacts.


##

`StandaloneCompiledArtifacts`

[¶](https://docs.vllm.ai#vllm.compilation.caching.StandaloneCompiledArtifacts)

Storage for standalone compiled artifacts with content-based deduplication.

Deduplication works via a two-level indirection: 1. `submodule_bytes`

maps "{submod_name}_{shape}" -> SHA256 hash 2. `submodule_bytes_store`

maps SHA256 hash -> actual bytes

When inserting, we compute the SHA256 hash of the bytes. If the hash already exists in `submodule_bytes_store`

, we reuse the existing entry rather than storing duplicate bytes. This is common because submodules often compile to identical artifacts (e.g., identical transformer layers split on attn)

## Source code in `vllm/compilation/caching.py`


|
|

##

`VllmSerializableFunction`

[¶](https://docs.vllm.ai#vllm.compilation.caching.VllmSerializableFunction)

Bases: `SerializableCallable`


A wrapper around a compiled function by vllm. It will forward the tensor inputs to the compiled function and return the result. It also implements a serialization interface to support PyTorch's precompile with custom backend, so that we can save and load the compiled function on disk. There's no need to wrap around the compiled function if we don't want to serialize them in particular cases. Right now serialization for the custom backend is done via serializing the Dynamo fx graph plus example inputs.

Methods:

-
–[finalize_loading](https://docs.vllm.ai#vllm.compilation.caching.VllmSerializableFunction.finalize_loading)Eagerly initialize the compiled backend and perform all loading.


Attributes:

## Source code in `vllm/compilation/caching.py`


|
|

###

`co_name`

`property`

[¶](https://docs.vllm.ai#vllm.compilation.caching.VllmSerializableFunction.co_name)

Used for depyf debugging.

###

`finalize_loading(vllm_config)`

[¶](https://docs.vllm.ai#vllm.compilation.caching.VllmSerializableFunction.finalize_loading)

Eagerly initialize the compiled backend and perform all loading.

Must be called after _verify_source_unchanged has populated compilation_config.traced_files, which is needed for cache dir computation.

## Source code in `vllm/compilation/caching.py`


##

`reconstruct_serializable_fn_from_mega_artifact(state, standalone_compile_artifacts, vllm_config, sym_shape_indices_map, returns_tuple_map, fake_mode)`

[¶](https://docs.vllm.ai#vllm.compilation.caching.reconstruct_serializable_fn_from_mega_artifact)

Construct a VllmSerializableFunction from cached inductor artifacts.

This function reconstructs a callable model from pre-compiled inductor artifacts without re-running the compilation. It: 1. Loads all cached artifacts 2. Builds compiled callables for each submodule/shape 3. Creates PiecewiseBackend instances that dispatch to cached artifacts 4. Wraps with cudagraph if needed 5. Returns the final VllmSerializableFunction

Note: This function shares similar logic with PiecewiseCompileInterpreter in backends.py. Both create PiecewiseBackend instances and wrap them with cudagraph. The key difference is: - this function: PiecewiseBackend receives pre-compiled runnables (compiled_runnables is set, graph is None) - PiecewiseCompileInterpreter: PiecewiseBackend receives the FX graph to compile (graph is set, compiled_runnables is None)

If modifying the backend creation/wrapping logic, consider updating both.

Parameters:

-

(`fake_mode`

[¶](https://docs.vllm.ai#vllm.compilation.caching.reconstruct_serializable_fn_from_mega_artifact(fake_mode))`FakeTensorMode`

) –FakeTensorMode used to unpickle the cached graph.

-

(`state`

[¶](https://docs.vllm.ai#vllm.compilation.caching.reconstruct_serializable_fn_from_mega_artifact(state))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)]Deserialized state dict containing graph_module, example_inputs, prefix, sym_tensor_indices, is_encoder, etc.

-

(`standalone_compile_artifacts`

[¶](https://docs.vllm.ai#vllm.compilation.caching.reconstruct_serializable_fn_from_mega_artifact(standalone_compile_artifacts))

) –[StandaloneCompiledArtifacts](https://docs.vllm.ai#vllm.compilation.caching.StandaloneCompiledArtifacts)The StandaloneCompiledArtifacts containing pre-compiled artifacts for each submodule/shape combination.

-

(`vllm_config`

[¶](https://docs.vllm.ai#vllm.compilation.caching.reconstruct_serializable_fn_from_mega_artifact(vllm_config))

) –[VllmConfig](https://docs.vllm.ai/config/#vllm.config.VllmConfig)The vLLM configuration.

-

(`sym_shape_indices_map`

[¶](https://docs.vllm.ai#vllm.compilation.caching.reconstruct_serializable_fn_from_mega_artifact(sym_shape_indices_map))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]Mapping from submod_name to sym_shape_indices.

-

(`returns_tuple_map`

[¶](https://docs.vllm.ai#vllm.compilation.caching.reconstruct_serializable_fn_from_mega_artifact(returns_tuple_map))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[bool](https://docs.python.org/3/builtins/functions.html#bool)]Mapping from submod_name to returns_tuple.


Returns:

-

–[VllmSerializableFunction](https://docs.vllm.ai#vllm.compilation.caching.VllmSerializableFunction)A VllmSerializableFunction that can be called directly.


## Source code in `vllm/compilation/caching.py`


|
|