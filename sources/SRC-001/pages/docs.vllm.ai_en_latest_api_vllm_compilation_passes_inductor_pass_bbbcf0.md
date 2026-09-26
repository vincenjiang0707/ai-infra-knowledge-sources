source: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/inductor_pass/
lastmod: 2026-09-24

#

`vllm.compilation.passes.inductor_pass`

[¶](https://docs.vllm.ai#vllm.compilation.passes.inductor_pass)

Classes:

-
–[CallableInductorPass](https://docs.vllm.ai#vllm.compilation.passes.inductor_pass.CallableInductorPass)This class is a wrapper for a callable that automatically provides an

-
–[InductorPass](https://docs.vllm.ai#vllm.compilation.passes.inductor_pass.InductorPass)A custom graph pass that uses a hash of its source as the UUID.


Functions:

-
–[enable_fake_mode](https://docs.vllm.ai#vllm.compilation.passes.inductor_pass.enable_fake_mode)Applies a FakeTensorMode context. This is useful when you don't want to

-
–[get_pass_context](https://docs.vllm.ai#vllm.compilation.passes.inductor_pass.get_pass_context)Get the current pass context.

-
–[pass_context](https://docs.vllm.ai#vllm.compilation.passes.inductor_pass.pass_context)A context manager that stores the current pass context,


##

`CallableInductorPass`

[¶](https://docs.vllm.ai#vllm.compilation.passes.inductor_pass.CallableInductorPass)

Bases: [InductorPass](https://docs.vllm.ai#vllm.compilation.passes.inductor_pass.InductorPass)

This class is a wrapper for a callable that automatically provides an implementation of the UUID.

## Source code in `vllm/compilation/passes/inductor_pass.py`


##

`InductorPass`

[¶](https://docs.vllm.ai#vllm.compilation.passes.inductor_pass.InductorPass)

Bases: `CustomGraphPass`


A custom graph pass that uses a hash of its source as the UUID. This is defined as a convenience and should work in most cases.

Methods:

-
–[hash_dict](https://docs.vllm.ai#vllm.compilation.passes.inductor_pass.InductorPass.hash_dict)Utility method to hash a dictionary, can alternatively be used for uuid.

-
–[hash_source](https://docs.vllm.ai#vllm.compilation.passes.inductor_pass.InductorPass.hash_source)Utility method to hash the sources of functions or objects.

-
–[uuid](https://docs.vllm.ai#vllm.compilation.passes.inductor_pass.InductorPass.uuid)Provide a unique identifier for the pass, used in Inductor code cache.


## Source code in `vllm/compilation/passes/inductor_pass.py`


###

`hash_dict(dict_)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.compilation.passes.inductor_pass.InductorPass.hash_dict)

Utility method to hash a dictionary, can alternatively be used for uuid.

Returns:

-

–[str](https://docs.python.org/3/builtins/stdtypes.html#str)A sha256 hash of the json rep of the dictionary.


## Source code in `vllm/compilation/passes/inductor_pass.py`


###

`hash_source(*srcs)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.compilation.passes.inductor_pass.InductorPass.hash_source)

Utility method to hash the sources of functions or objects.

Parameters:

-

(`srcs`

[¶](https://docs.vllm.ai#vllm.compilation.passes.inductor_pass.InductorPass.hash_source(srcs))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)|[Any](https://docs.python.org/3/library/typing.html#typing.Any)`()`

) –strings or objects to add to the hash. Objects and functions have their source inspected. Results are cached by resolved types to avoid repeated inspect.getsource() calls.


## Source code in `vllm/compilation/passes/inductor_pass.py`


###

`uuid()`

[¶](https://docs.vllm.ai#vllm.compilation.passes.inductor_pass.InductorPass.uuid)

Provide a unique identifier for the pass, used in Inductor code cache. This should depend on the pass implementation, so that changes to the pass result in recompilation. By default, the object source is hashed.

## Source code in `vllm/compilation/passes/inductor_pass.py`


##

`enable_fake_mode(fn)`

[¶](https://docs.vllm.ai#vllm.compilation.passes.inductor_pass.enable_fake_mode)

Applies a FakeTensorMode context. This is useful when you don't want to create or run things with real tensors.

## Source code in `vllm/compilation/passes/inductor_pass.py`


##

`get_pass_context()`

[¶](https://docs.vllm.ai#vllm.compilation.passes.inductor_pass.get_pass_context)

##

`pass_context(compile_range)`

[¶](https://docs.vllm.ai#vllm.compilation.passes.inductor_pass.pass_context)

A context manager that stores the current pass context, usually it is a list of sizes to specialize.