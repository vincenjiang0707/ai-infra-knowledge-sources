source: https://docs.vllm.ai/en/latest/api/vllm/ir/op/
lastmod: 2026-09-24

#

`vllm.ir.op`

[¶](https://docs.vllm.ai#vllm.ir.op)

Classes:

-
–[IrOp](https://docs.vllm.ai#vllm.ir.op.IrOp) -
–[IrOpImpl](https://docs.vllm.ai#vllm.ir.op.IrOpImpl) -
–[IrOpInplace](https://docs.vllm.ai#vllm.ir.op.IrOpInplace)IR op with inplace support via maybe_inplace.


Functions:

-
–[enable_torch_wrap](https://docs.vllm.ai#vllm.ir.op.enable_torch_wrap)Context manager to enable/disable torch custom op wrapping for vLLM IR ops.

-
–[register_op](https://docs.vllm.ai#vllm.ir.op.register_op)Register a new vLLM IR op.

-
–[set_default_torch_wrap](https://docs.vllm.ai#vllm.ir.op.set_default_torch_wrap)Permanently set the torch wrap flag.


Attributes:

-
–[RESERVED_PROVIDERS](https://docs.vllm.ai#vllm.ir.op.RESERVED_PROVIDERS)Providers that are reserved and cannot be used for custom implementations.


##

`RESERVED_PROVIDERS = ['native', 'unfused']`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.ir.op.RESERVED_PROVIDERS)

Providers that are reserved and cannot be used for custom implementations.

##

`_ENABLE_TORCH_WRAP = True`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.ir.op._ENABLE_TORCH_WRAP)

Global override flag to control torch op layer wrapping.

##

`IrOp`

[¶](https://docs.vllm.ai#vllm.ir.op.IrOp)

Methods:

-
–[__repr__](https://docs.vllm.ai#vllm.ir.op.IrOp.__repr__)Return unambiguous string representation.

-
–[__str__](https://docs.vllm.ai#vllm.ir.op.IrOp.__str__)Return human-readable string representation using docstring.

-
–[apply_arg_defaults](https://docs.vllm.ai#vllm.ir.op.IrOp.apply_arg_defaults)Return args with default values applied.

-
–[dispatch](https://docs.vllm.ai#vllm.ir.op.IrOp.dispatch)Dispatch to the appropriate implementation based on current priority

-
–[get_priority](https://docs.vllm.ai#vllm.ir.op.IrOp.get_priority)Get the current dispatch priority for implementations for this op.

-
–[register_fake](https://docs.vllm.ai#vllm.ir.op.IrOp.register_fake)Register a fake impl for the torch custom op. If this method is not called,

-
–[register_impl](https://docs.vllm.ai#vllm.ir.op.IrOp.register_impl)Register an implementation for this custom op.

-
–[set_default](https://docs.vllm.ai#vllm.ir.op.IrOp.set_default)Permanently set the dispatch priority for this op. Use this for

-
–[set_priority](https://docs.vllm.ai#vllm.ir.op.IrOp.set_priority)Context manager setting the dispatch priority for this op's impls.


## Source code in `vllm/ir/op.py`


|
|

###

`__repr__()`

[¶](https://docs.vllm.ai#vllm.ir.op.IrOp.__repr__)

###

`__str__()`

[¶](https://docs.vllm.ai#vllm.ir.op.IrOp.__str__)

Return human-readable string representation using docstring.

###

`_fake_call(*args, **kwargs)`

[¶](https://docs.vllm.ai#vllm.ir.op.IrOp._fake_call)

Call to the fake implementation of the op. We use indirection because we want users to be able to register fake later but also want it to fall back to native directly by default, instead of going through the dispatching mechanism.

## Source code in `vllm/ir/op.py`


###

`_inner_call(*args, **kwargs)`

[¶](https://docs.vllm.ai#vllm.ir.op.IrOp._inner_call)

Eager call to torch op lands here. When torch wrapping is disabled, **call** routes straight here instead of going through torch op dispatching.

## Source code in `vllm/ir/op.py`


###

`apply_arg_defaults(args)`

[¶](https://docs.vllm.ai#vllm.ir.op.IrOp.apply_arg_defaults)

Return args with default values applied. Defaults are taken from the native implementation signature.

SHOULD NOT BE USED IN THE DISPATCH PATH (SLOW). Only for Inductor lowering.

## Source code in `vllm/ir/op.py`


###

`dispatch(*args, **kwargs)`

[¶](https://docs.vllm.ai#vllm.ir.op.IrOp.dispatch)

Dispatch to the appropriate implementation based on current priority and argument support checks. Returns the selected IrOpImpl.

THIS FUNCTION IS ON THE HOT PATH (OP DISPATCH), MUST BE FAST.

## Source code in `vllm/ir/op.py`


###

`get_priority()`

[¶](https://docs.vllm.ai#vllm.ir.op.IrOp.get_priority)

###

`register_fake(fn)`

[¶](https://docs.vllm.ai#vllm.ir.op.IrOp.register_fake)

Register a fake impl for the torch custom op. If this method is not called, the native implementation is used directly for the fake implementation.

###

`register_impl(provider, *, supported=True, supports_args=None, inplace=False)`

[¶](https://docs.vllm.ai#vllm.ir.op.IrOp.register_impl)

Register an implementation for this custom op.

Parameters:

-

(`provider`

[¶](https://docs.vllm.ai#vllm.ir.op.IrOp.register_impl(provider))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The name of the provider, must be unique.

-

(`supported`

[¶](https://docs.vllm.ai#vllm.ir.op.IrOp.register_impl(supported))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –Static support check, use this to check platform support.

-

(`supports_args`

[¶](https://docs.vllm.ai#vllm.ir.op.IrOp.register_impl(supports_args))

, default:[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[...,[bool](https://docs.python.org/3/builtins/functions.html#bool)] | None`None`

) –Dynamic arg support check, used for types and shapes.

-

(`inplace`

[¶](https://docs.vllm.ai#vllm.ir.op.IrOp.register_impl(inplace))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Does this op reuse activation input memory for outputs


Returns:

The decorated function must have the same semantics and signature as the native implementation.

The provider name must be unique and not one of the RESERVED_PROVIDERS. The supported and supports_args parameters should not be used to implement custom enablement logic based on global state (e.g. environment variables). Instead, supported param should only be used to check for platform support (e.g. whether a specific hardware or library is available). supports_args should be used to check whether the provided arguments are compatible with the implementation. For custom enablement logic, set op impl priority.

Example:

@my_op.register_impl("my_provider", supported=torch.cuda.is_available())
def my_provider_impl(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor: ...


## Source code in `vllm/ir/op.py`


###

`set_default(priority)`

[¶](https://docs.vllm.ai#vllm.ir.op.IrOp.set_default)

Permanently set the dispatch priority for this op. Use this for process-lifetime setup (e.g., worker startup). For scoped overrides, use `set_priority`

instead.

## Source code in `vllm/ir/op.py`


###

`set_priority(priority)`

[¶](https://docs.vllm.ai#vllm.ir.op.IrOp.set_priority)

Context manager setting the dispatch priority for this op's impls.

## Source code in `vllm/ir/op.py`


##

`IrOpImpl`

[¶](https://docs.vllm.ai#vllm.ir.op.IrOpImpl)

Methods:

-
–[func_impl_fn](https://docs.vllm.ai#vllm.ir.op.IrOpImpl.func_impl_fn)Copy any inputs in activations if this is an inplace impl,

-
–[uuid](https://docs.vllm.ai#vllm.ir.op.IrOpImpl.uuid)Compile-time hash to uniquely determine whether the implementation has


Attributes:

-
([supports_all_args](https://docs.vllm.ai#vllm.ir.op.IrOpImpl.supports_all_args)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Check if this implementation supports all args unconditionally.


## Source code in `vllm/ir/op.py`


|
|

###

`supports_all_args`

`property`

[¶](https://docs.vllm.ai#vllm.ir.op.IrOpImpl.supports_all_args)

Check if this implementation supports all args unconditionally.

###

`func_impl_fn(*args, **kwargs)`

[¶](https://docs.vllm.ai#vllm.ir.op.IrOpImpl.func_impl_fn)

Copy any inputs in activations if this is an inplace impl, to ensure functional semantics.

## Source code in `vllm/ir/op.py`


###

`uuid()`

[¶](https://docs.vllm.ai#vllm.ir.op.IrOpImpl.uuid)

Compile-time hash to uniquely determine whether the implementation has changed. Used by vllm-compile hash mechanism and torch.compile lowering pass uuid to control the vLLM compile cache and AOTAutograd/Inductor caches respectively.

Source file contents do not change so we cache uuid. TODO(luka): Cache the file hash as multiple impls are likely in the same file.

## Source code in `vllm/ir/op.py`


##

`IrOpInplace`

[¶](https://docs.vllm.ai#vllm.ir.op.IrOpInplace)

Bases: [IrOp](https://docs.vllm.ai#vllm.ir.op.IrOp)

IR op with inplace support via maybe_inplace.

## Source code in `vllm/ir/op.py`


##

`_torch_ops_subtree(lib)`

[¶](https://docs.vllm.ai#vllm.ir.op._torch_ops_subtree)

`torch.ops`

subtree for `lib.ns`

; fall back if doc mocks replace `ns`

.

##

`_validate_name(name, entity_type)`

[¶](https://docs.vllm.ai#vllm.ir.op._validate_name)

Validate that a name matches the required pattern `[a-z_][a-z_0-9]*`

.

## Source code in `vllm/ir/op.py`


##

`enable_torch_wrap(enable=True)`

[¶](https://docs.vllm.ai#vllm.ir.op.enable_torch_wrap)

Context manager to enable/disable torch custom op wrapping for vLLM IR ops. When torch wrapping is disabled, the torch custom op layer is skipped and IR ops dispatch directly to the implementation. Helpful for avoiding torch dispatch overhead in eager mode and avoiding the need for lowering for platforms not using Inductor.

## Source code in `vllm/ir/op.py`


##

`register_op(f=None, *, name=None, activations=None, allow_inplace=False)`

[¶](https://docs.vllm.ai#vllm.ir.op.register_op)

Register a new vLLM IR op.

Parameters:

-

(`f`

[¶](https://docs.vllm.ai#vllm.ir.op.register_op(f))

, default:[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)| None`None`

) –the native implementation of the op

-

(`name`

[¶](https://docs.vllm.ai#vllm.ir.op.register_op(name))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –the name of the op, defaults to the function name

-

(`activations`

[¶](https://docs.vllm.ai#vllm.ir.op.register_op(activations))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None`None`

) –list of activation params, defaults to params starting with 'x'

-

(`allow_inplace`

[¶](https://docs.vllm.ai#vllm.ir.op.register_op(allow_inplace))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –add a maybe_inplace overload that allows inplace impls


Returns:

Example usage:

```bash
@vllm.ir.register_op
def my_add(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
return x + y
@vllm.ir.register_op(name="custom_mul")
def multiply(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
return x * y
```