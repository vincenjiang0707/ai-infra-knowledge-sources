source: https://docs.vllm.ai/en/latest/api/vllm/compilation/decorators/
lastmod: 2026-09-24

#

`vllm.compilation.decorators`

[¶](https://docs.vllm.ai#vllm.compilation.decorators)

Functions:

-
–[ignore_torch_compile](https://docs.vllm.ai#vllm.compilation.decorators.ignore_torch_compile)A decorator to ignore support_torch_compile decorator

-
–[maybe_use_cudagraph_partition_wrapper](https://docs.vllm.ai#vllm.compilation.decorators.maybe_use_cudagraph_partition_wrapper)Context manager to set/unset customized cudagraph partition wrappers.

-
–[should_torch_compile_mm_encoder](https://docs.vllm.ai#vllm.compilation.decorators.should_torch_compile_mm_encoder)Callable to be passed to

`@support_torch_compile`

's`enable_if`

argument. -
–[support_torch_compile](https://docs.vllm.ai#vllm.compilation.decorators.support_torch_compile)A decorator to add support for compiling the forward method of a class.


Attributes:

-
([DynamicArgDims](https://docs.vllm.ai#vllm.compilation.decorators.DynamicArgDims)

) –[TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias)Argument name -> the dynamic dimension(s) of that argument.


##

`DynamicArgDims = dict[str, int | list[int] | dict[int, str]]`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.compilation.decorators.DynamicArgDims)

Argument name -> the dynamic dimension(s) of that argument.

##

`_should_ignore_torch_compile(cls)`

[¶](https://docs.vllm.ai#vllm.compilation.decorators._should_ignore_torch_compile)

##

`_support_torch_compile(cls, dynamic_arg_dims, mark_unbacked_dims=None, enable_if=None, is_encoder=False)`

[¶](https://docs.vllm.ai#vllm.compilation.decorators._support_torch_compile)

Internal implementation of support_torch_compile decorator.

## Source code in `vllm/compilation/decorators.py`


|
|

##

`_try_load_aot_compiled_fn(model, aot_compilation_path)`

[¶](https://docs.vllm.ai#vllm.compilation.decorators._try_load_aot_compiled_fn)

Try to load an AOT-compiled function from disk.

Returns the loaded callable on success, or None on failure. Re-raises on failure when `VLLM_FORCE_AOT_LOAD`

is set.

## Source code in `vllm/compilation/decorators.py`


##

`ignore_torch_compile(cls)`

[¶](https://docs.vllm.ai#vllm.compilation.decorators.ignore_torch_compile)

A decorator to ignore support_torch_compile decorator on the class. This is useful when a parent class has a support_torch_compile decorator, but we don't want to compile the class `cls`

that inherits the parent class. This only ignores compiling the forward of the class the decorator is applied to.

If the parent has ignore_torch_compile but the child has support_torch_compile, the child will still be compiled.

If the class has one or more submodules that have support_torch_compile decorator applied, compile will not be ignored for those submodules.

## Source code in `vllm/compilation/decorators.py`


##

`maybe_use_cudagraph_partition_wrapper(vllm_config)`

[¶](https://docs.vllm.ai#vllm.compilation.decorators.maybe_use_cudagraph_partition_wrapper)

Context manager to set/unset customized cudagraph partition wrappers.

If we're using Inductor-based graph partitioning, we currently have the whole `fx.Graph`

before Inductor lowering and the piecewise splitting happens after all graph passes and fusions. Here, we add a custom hook for Inductor to wrap each partition with our static graph wrapper class to maintain more control over static graph capture and replay.

## Source code in `vllm/compilation/decorators.py`


##

`should_torch_compile_mm_encoder(vllm_config)`

[¶](https://docs.vllm.ai#vllm.compilation.decorators.should_torch_compile_mm_encoder)

Callable to be passed to `@support_torch_compile`

's `enable_if`

argument.

##

`support_torch_compile(cls=None, *, dynamic_arg_dims=None, mark_unbacked_dims=None, enable_if=None, is_encoder=False)`

[¶](https://docs.vllm.ai#vllm.compilation.decorators.support_torch_compile)

support_torch_compile(
*, enable_if: Callable[[VllmConfig], bool] | None = None
) -> Callable[[type[_T]], type[_T]]


support_torch_compile(
*, dynamic_arg_dims: DynamicArgDims | None
) -> Callable[[type[_T]], type[_T]]


support_torch_compile(
*, mark_unbacked_dims: dict[str, int | list[int]] | None
) -> Callable[[type[_T]], type[_T]]


A decorator to add support for compiling the forward method of a class.

Usage 1: use directly as a decorator without arguments:

@support_torch_compile
class MyModel(nn.Module):
def forward(self, x: torch.Tensor, y: Optional[torch.Tensor]): ...


Usage 2: use as a decorator with arguments:

@support_torch_compile(dynamic_arg_dims={"x": 0, "y": 0})
class MyModel(nn.Module):
def forward(self, x: torch.Tensor, y: Optional[torch.Tensor]): ...


`dynamic_arg_dims`

is a dictionary that maps argument names to the dynamic dimensions of the argument. The value can be: - int: a single dimension index (e.g., 0) - list[int]: multiple dimension indices (e.g., [0, 1]) - dict[int, str]: dimension to shape_id mapping for shape relations (e.g., {0: "b"}). Dimensions with the same shape_id share the same unbacked symbol.

if `dynamic_arg_dims`

is `None`

, it is inferred from the type annotation of the `forward`

method, based on the following default rules:

- if the argument is annotated as
`torch.Tensor`

or`Optional[torch.Tensor]`

, the first dimension will be marked as dynamic. - if the argument is annotated as
`IntermediateTensors`

, the first dimension of all the tensors in the intermediate tensors will be marked as dynamic.

During runtime, when we actually mark dimensions of tensors, it depends on the value of arguments:

- if it is a single integer (can be negative), the corresponding dimension of the argument will be marked as dynamic.
- if it is
`None`

, ignored. - if it is
`IntermediateTensors`

, all the tensors in the intermediate tensors will be marked as dynamic. - otherwise, it will raise an error.

NOTE: if an argument is `None`

, it should always be passed as `None`

during the lifetime of the model, otherwise, it cannot be captured as a single computation graph.

`enable_if`

is a function that takes a `VllmConfig`

object as input and returns a boolean value indicating whether to compile the model or not. This is useful if you want to compile the model only when certain conditions are met.

`mark_unbacked_dims`

is a dictionary that maps argument names with a dynamic dim to be decorated with `mark_unbacked`

. This is useful if we would like to enforce that dynamo does not specialize on 0/1 values in the case of dummy input such as for vision model compilation

`is_encoder`

marks this module as a portion of an multimodal encoder. When True, the compile range upper bound is set to MAX_INT32 instead of max_num_batched_tokens, since encoder input shapes are unpredictable. This is typically used for vision encoder sub-modules in multimodal models.

`shape_invariants`

is a function that gets compiled right before forward. The function should have the torch._check calls that are needed to set the relationships between different input sizes. For example: torch._check(input_ids.size()[0] == inputs_embeds.size()[0]) This enforces constraints on the symbolic shapes without hardcoding specific values. It is needed for some models to avoid data dependent errors and maximize perf when unbacked shapes are used.

## Source code in `vllm/compilation/decorators.py`


|
|