source: https://docs.vllm.ai/en/latest/api/vllm/compilation/codegen/
lastmod: 2026-09-24

#

`vllm.compilation.codegen`

[¶](https://docs.vllm.ai#vllm.compilation.codegen)

Code generation for split_gm stitching graph execution.

Generates a plain Python function that replaces the FX GraphModule's interpreter-based execution of the stitching graph, eliminating nn.Module.**call** overhead and **getattr** dispatch.

Functions:

-
–[compile_execution_fn](https://docs.vllm.ai#vllm.compilation.codegen.compile_execution_fn)Compile execution code and bind submodule callables.

-
–[generate_execution_code](https://docs.vllm.ai#vllm.compilation.codegen.generate_execution_code)Generate Python source code from a split_gm's stitching graph.


##

`_node_ref(arg, consts, const_index)`

[¶](https://docs.vllm.ai#vllm.compilation.codegen._node_ref)

Convert an FX node argument to a source code reference.

## Source code in `vllm/compilation/codegen.py`


##

`compile_execution_fn(code, submod_callables, submod_names, consts=None)`

[¶](https://docs.vllm.ai#vllm.compilation.codegen.compile_execution_fn)

Compile execution code and bind submodule callables.

Parameters:

-

(`code`

[¶](https://docs.vllm.ai#vllm.compilation.codegen.compile_execution_fn(code))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Python source from generate_execution_code().

-

(`submod_callables`

[¶](https://docs.vllm.ai#vllm.compilation.codegen.compile_execution_fn(submod_callables))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[...,[Any](https://docs.python.org/3/library/typing.html#typing.Any)]]Mapping of submodule names to their callables.

-

(`submod_names`

[¶](https://docs.vllm.ai#vllm.compilation.codegen.compile_execution_fn(submod_names))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Ordered list of submodule names matching the indices used in the generated code.

-

(`consts`

[¶](https://docs.vllm.ai#vllm.compilation.codegen.compile_execution_fn(consts))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None`None`

) –List of non-primitive constant objects referenced by the generated code via

**vllm_consts**. None for legacy cached code that predates this feature.

Returns:

## Source code in `vllm/compilation/codegen.py`


##

`generate_execution_code(split_gm)`

[¶](https://docs.vllm.ai#vllm.compilation.codegen.generate_execution_code)

Generate Python source code from a split_gm's stitching graph.

Walks split_gm.graph.nodes and produces a function that calls submodules via a **vllm_submods** list, avoiding FX GraphModule overhead and dict lookup cost.

Non-primitive constant arguments (e.g. torch.device, DTensor placement types) are collected into a constants list and referenced by index in the generated code, avoiding reliance on repr() being eval-able.

If a submodule is a plain torch.fx.GraphModule, it is inlined directly in the generated code and we do not need to serialize it in the artifact.

Parameters:

-

(`split_gm`

[¶](https://docs.vllm.ai#vllm.compilation.codegen.generate_execution_code(split_gm))

) –[GraphModule](https://pytorch.org/docs/stable/fx.html#torch.fx.GraphModule)The split graph module produced by split_graph().


Returns:

-

–[str](https://docs.python.org/3/builtins/stdtypes.html#str)A tuple of (code, submod_names, consts) where code is the Python

-

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]source, submod_names is the ordered list of submodule target names

-

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Any](https://docs.python.org/3/library/typing.html#typing.Any)]corresponding to list indices used in the generated code, and

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)],[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Any](https://docs.python.org/3/library/typing.html#typing.Any)]]consts is a list of non-primitive constant objects referenced

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)],[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Any](https://docs.python.org/3/library/typing.html#typing.Any)]]by the generated code via

**vllm_consts**. These objects are -

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)],[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Any](https://docs.python.org/3/library/typing.html#typing.Any)]]kept alive for the lifetime of the compiled function.