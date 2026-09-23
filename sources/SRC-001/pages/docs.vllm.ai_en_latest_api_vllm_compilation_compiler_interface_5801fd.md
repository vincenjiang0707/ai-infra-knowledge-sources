source: https://docs.vllm.ai/en/latest/api/vllm/compilation/compiler_interface/
lastmod: 2026-09-23

#

`vllm.compilation.compiler_interface`

[¶](https://docs.vllm.ai#vllm.compilation.compiler_interface)

Classes:

-
–[AlwaysHitShapeEnv](https://docs.vllm.ai#vllm.compilation.compiler_interface.AlwaysHitShapeEnv)Why do we need this class:

-
–[CompilerInterface](https://docs.vllm.ai#vllm.compilation.compiler_interface.CompilerInterface)The interface for a compiler that can be used by vLLM.

-
–[InductorAdaptor](https://docs.vllm.ai#vllm.compilation.compiler_interface.InductorAdaptor)The adaptor for the Inductor compiler, version 2.5, 2.6, 2.7.

-
–[InductorStandaloneAdaptor](https://docs.vllm.ai#vllm.compilation.compiler_interface.InductorStandaloneAdaptor)The adaptor for the Inductor compiler.


Functions:

-
–[trigger_inductor_lazy_init](https://docs.vllm.ai#vllm.compilation.compiler_interface.trigger_inductor_lazy_init)Eagerly trigger inductor's once-per-process lazy inits (SFDP pattern


##

`AlwaysHitShapeEnv`

[¶](https://docs.vllm.ai#vllm.compilation.compiler_interface.AlwaysHitShapeEnv)

Why do we need this class:

For normal `torch.compile`

usage, every compilation will have one Dynamo bytecode compilation and one Inductor compilation. The Inductor compilation happens under the context of the Dynamo bytecode compilation, and that context is used to determine the dynamic shape information, etc.

For our use case, we only run Dynamo bytecode compilation once, and run Inductor compilation multiple times with different shapes plus a general shape. The compilation for specific shapes happens outside of the context of the Dynamo bytecode compilation. At that time, we don't have shape environment to provide to Inductor, and it will fail the Inductor code cache lookup.

By providing a dummy shape environment that always hits, we can make the Inductor code cache lookup always hit, and we can compile the graph for different shapes as needed.

The following dummy methods are obtained by trial-and-error until it works.

## Source code in `vllm/compilation/compiler_interface.py`


##

`CompilerInterface`

[¶](https://docs.vllm.ai#vllm.compilation.compiler_interface.CompilerInterface)

The interface for a compiler that can be used by vLLM.

Methods:

-
–[compile](https://docs.vllm.ai#vllm.compilation.compiler_interface.CompilerInterface.compile)Compile the graph with the given example inputs and compiler config,

-
–[compute_hash](https://docs.vllm.ai#vllm.compilation.compiler_interface.CompilerInterface.compute_hash)Gather all the relevant information from the vLLM config,

-
–[initialize_cache](https://docs.vllm.ai#vllm.compilation.compiler_interface.CompilerInterface.initialize_cache)When the vLLM process uses

`cache_dir`

as the cache directory, -
–[load](https://docs.vllm.ai#vllm.compilation.compiler_interface.CompilerInterface.load)Load the compiled function from the handle.


## Source code in `vllm/compilation/compiler_interface.py`


###

`compile(graph, example_inputs, compiler_config, compile_range, key=None)`

[¶](https://docs.vllm.ai#vllm.compilation.compiler_interface.CompilerInterface.compile)

Compile the graph with the given example inputs and compiler config, with a range. The `compile_range`

specifies the range of the inputs, it could be concrete size (if compile_sizes is provided), e.g. [4, 4] or a range [5, 8]. Right now we only support one variable in ranges for all inputs, which is the batchsize (number of tokens) during inference.

Dynamo will make sure `graph(*example_inputs)`

is valid.

The function should return a compiled callable function, as well as a handle that can be used to directly load the compiled function.

The handle should be a plain Python object, preferably a string or a file path for readability.

If the compiler doesn't support caching, it should return None for the handle. If the compiler fails to compile the graph, it should return None for the compiled function as well.

`key`

is required for StandaloneInductorAdapter, it specifies where to save the compiled artifact. The compiled artifact gets saved to `cache_dir/key`

.

## Source code in `vllm/compilation/compiler_interface.py`


###

`compute_hash(vllm_config)`

[¶](https://docs.vllm.ai#vllm.compilation.compiler_interface.CompilerInterface.compute_hash)

Gather all the relevant information from the vLLM config, to compute a hash so that we can cache the compiled model.

See [ VllmConfig.compute_hash](https://docs.vllm.ai/config/#vllm.config.VllmConfig.compute_hash) to check what information is already considered by default. This function should only consider the information that is specific to the compiler.

## Source code in `vllm/compilation/compiler_interface.py`


###

`initialize_cache(cache_dir, disable_cache=False, prefix='')`

[¶](https://docs.vllm.ai#vllm.compilation.compiler_interface.CompilerInterface.initialize_cache)

When the vLLM process uses `cache_dir`

as the cache directory, the compiler should initialize itself with the cache directory, e.g. by re-directing its own cache directory to a sub-directory.

prefix can be used in combination with cache_dir to figure out the base cache directory, e.g. there're multiple parts of model being compiled, but we want to share the same cache directory for all of them.

e.g. cache_dir = "/path/to/dir/backbone", prefix = "backbone" cache_dir = "/path/to/dir/eagle_head", prefix = "eagle_head"

## Source code in `vllm/compilation/compiler_interface.py`


###

`load(handle, graph, example_inputs, graph_index, compile_range)`

[¶](https://docs.vllm.ai#vllm.compilation.compiler_interface.CompilerInterface.load)

Load the compiled function from the handle. Raises an error if the handle is invalid.

The handle is the second return value of the `compile`

function.

## Source code in `vllm/compilation/compiler_interface.py`


##

`InductorAdaptor`

[¶](https://docs.vllm.ai#vllm.compilation.compiler_interface.InductorAdaptor)

Bases: [CompilerInterface](https://docs.vllm.ai#vllm.compilation.compiler_interface.CompilerInterface)

The adaptor for the Inductor compiler, version 2.5, 2.6, 2.7.

Methods:

-
–[metrics_context](https://docs.vllm.ai#vllm.compilation.compiler_interface.InductorAdaptor.metrics_context)This method returns the Dynamo metrics context (if it exists,


## Source code in `vllm/compilation/compiler_interface.py`


|
|

###

`metrics_context()`

[¶](https://docs.vllm.ai#vllm.compilation.compiler_interface.InductorAdaptor.metrics_context)

This method returns the Dynamo metrics context (if it exists, otherwise a null context). It is used by various compile components. Present in torch>=2.6, it's used inside FxGraphCache in torch==2.6 (but not after). It might also be used in various other torch.compile internal functions.

Because it is re-entrant, we always set it (even if entering via Dynamo and the context was already entered). We might want to revisit if it should be set at a different mode of compilation.

This is likely a bug in PyTorch: public APIs should not rely on manually setting up internal contexts. But we also rely on non-public APIs which might not provide these guarantees.

## Source code in `vllm/compilation/compiler_interface.py`


##

`InductorStandaloneAdaptor`

[¶](https://docs.vllm.ai#vllm.compilation.compiler_interface.InductorStandaloneAdaptor)

Bases: [CompilerInterface](https://docs.vllm.ai#vllm.compilation.compiler_interface.CompilerInterface)

The adaptor for the Inductor compiler. Requires PyTorch 2.8+. This is not on by default yet, but we plan to turn it on by default for PyTorch 2.8.

Use VLLM_USE_STANDALONE_COMPILE to toggle this on or off.

## Source code in `vllm/compilation/compiler_interface.py`


|
|

##

`_get_vllm_functorch_config()`

[¶](https://docs.vllm.ai#vllm.compilation.compiler_interface._get_vllm_functorch_config)

Return the functorch config overrides that vLLM applies at compile time.

Used by both set_functorch_config() and get_inductor_factors() to ensure the compile-time config and cache key are always consistent.

## Source code in `vllm/compilation/compiler_interface.py`


##

`_patch_standalone_compile_atomic_save()`

[¶](https://docs.vllm.ai#vllm.compilation.compiler_interface._patch_standalone_compile_atomic_save)

Backport of pytorch/pytorch#162432 for torch < 2.10.0.

Patches CompiledArtifact.save() to use write_atomic for binary format, preventing corrupt cache files when multiple processes compile concurrently.

## Source code in `vllm/compilation/compiler_interface.py`


##

`trigger_inductor_lazy_init(device=None)`

[¶](https://docs.vllm.ai#vllm.compilation.compiler_interface.trigger_inductor_lazy_init)

Eagerly trigger inductor's once-per-process lazy inits (SFDP pattern matcher, pad_mm, misc patterns).

These normally fire on the first torch.compile invocation and include CUDA syncs. If warmup hits the on-disk compile cache, no compile actually runs so these never fire during warmup, and they'd blow up on the first real-request cache miss once the sync-check gate is on.

Private torch API; best-effort. Newer torch versions take an `input_device`

argument and cache per-device, so pass the current CUDA device to ensure the cache key matches later compile calls.