source: https://docs.vllm.ai/en/latest/api/vllm/kernels/aiter_ops/
lastmod: 2026-09-23

#

`vllm.kernels.aiter_ops`

[¶](https://docs.vllm.ai#vllm.kernels.aiter_ops)

Functions:

-
–[flatten_to_2d_is_free](https://docs.vllm.ai#vllm.kernels.aiter_ops.flatten_to_2d_is_free)Whether

`x.reshape(-1, x.shape[-1])`

is a view with unit-stride rows.

Attributes:

-
–[AITER_SUPPORTED](https://docs.vllm.ai#vllm.kernels.aiter_ops.AITER_SUPPORTED)Most kernels in this file are supported if AITER is installed.

-
–[aiter_lib](https://docs.vllm.ai#vllm.kernels.aiter_ops.aiter_lib)This library holds torch custom ops for wrapped AITER ops.

-
–[direct_register_aiter_op](https://docs.vllm.ai#vllm.kernels.aiter_ops.direct_register_aiter_op)Syntactic sugar for registering AITER custom ops.

-
–[rms_add_no_var_16bit_only](https://docs.vllm.ai#vllm.kernels.aiter_ops.rms_add_no_var_16bit_only)AITER fused_add_rms_norm only supports 16-bit activations and no var_size override.

-
–[rms_no_var_16bit_only](https://docs.vllm.ai#vllm.kernels.aiter_ops.rms_no_var_16bit_only)AITER rms_norm only supports float16 and bfloat16 acts, no var_size override,


##

`AITER_SUPPORTED = is_aiter_found()`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.kernels.aiter_ops.AITER_SUPPORTED)

Most kernels in this file are supported if AITER is installed.

##

`aiter_lib = Library('vllm_aiter', 'FRAGMENT')`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.kernels.aiter_ops.aiter_lib)

This library holds torch custom ops for wrapped AITER ops. Many AITER ops want to remain invisible to torch.compile even after lowering. They are thus wrapped into torch custom ops inside the IR op implementations.

##

`direct_register_aiter_op = functools.partial(direct_register_custom_op, target_lib=aiter_lib)`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.kernels.aiter_ops.direct_register_aiter_op)

Syntactic sugar for registering AITER custom ops.

##

`rms_add_no_var_16bit_only = lambda x, x_residual, weight, epsilon, variance_size=None: variance_size is None and x.dtype in (torch.float16, torch.bfloat16) and (weight is None or weight.dtype == x.dtype) and flatten_to_2d_is_free(x) and flatten_to_2d_is_free(x_residual)`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.kernels.aiter_ops.rms_add_no_var_16bit_only)

AITER fused_add_rms_norm only supports 16-bit activations and no var_size override. Requires weight dtype to match x dtype, and flattening both the activation and the residual to 2D to be free.

##

`rms_no_var_16bit_only = lambda x, weight, epsilon, variance_size=None: variance_size is None and x.dtype in (torch.float16, torch.bfloat16) and (weight is None or weight.dtype == x.dtype) and flatten_to_2d_is_free(x)`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.kernels.aiter_ops.rms_no_var_16bit_only)

AITER rms_norm only supports float16 and bfloat16 acts, no var_size override, requires weight dtype to match x dtype, and requires flattening the activation to 2D to be free.

##

`flatten_to_2d_is_free(x)`

[¶](https://docs.vllm.ai#vllm.kernels.aiter_ops.flatten_to_2d_is_free)

Whether `x.reshape(-1, x.shape[-1])`

is a view with unit-stride rows.

The AITER norm kernels only take dense 2D inputs, so the wrappers below flatten the leading dims with `Tensor.reshape`

, which silently falls back to `contiguous()`

when the flattened shape is not expressible with the existing strides, adding a whole-tensor device copy that costs more than the kernel saves. A strided last dim flattens without a copy but not into a dense buffer, so it is rejected too.