source: https://docs.vllm.ai/en/latest/api/vllm/ir/
lastmod: 2026-09-24

#

`vllm.ir`

[¶](https://docs.vllm.ai#vllm.ir)

Modules:

Functions:

-
–[enable_torch_wrap](https://docs.vllm.ai#vllm.ir.enable_torch_wrap)Context manager to enable/disable torch custom op wrapping for vLLM IR ops.

-
–[register_op](https://docs.vllm.ai#vllm.ir.register_op)Register a new vLLM IR op.

-
–[set_default_torch_wrap](https://docs.vllm.ai#vllm.ir.set_default_torch_wrap)Permanently set the torch wrap flag.


##

`enable_torch_wrap(enable=True)`

[¶](https://docs.vllm.ai#vllm.ir.enable_torch_wrap)

Context manager to enable/disable torch custom op wrapping for vLLM IR ops. When torch wrapping is disabled, the torch custom op layer is skipped and IR ops dispatch directly to the implementation. Helpful for avoiding torch dispatch overhead in eager mode and avoiding the need for lowering for platforms not using Inductor.

## Source code in `vllm/ir/op.py`


##

`register_op(f=None, *, name=None, activations=None, allow_inplace=False)`

[¶](https://docs.vllm.ai#vllm.ir.register_op)

Register a new vLLM IR op.

Parameters:

-

(`f`

[¶](https://docs.vllm.ai#vllm.ir.register_op(f))

, default:[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)| None`None`

) –the native implementation of the op

-

(`name`

[¶](https://docs.vllm.ai#vllm.ir.register_op(name))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –the name of the op, defaults to the function name

-

(`activations`

[¶](https://docs.vllm.ai#vllm.ir.register_op(activations))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None`None`

) –list of activation params, defaults to params starting with 'x'

-

(`allow_inplace`

[¶](https://docs.vllm.ai#vllm.ir.register_op(allow_inplace))

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