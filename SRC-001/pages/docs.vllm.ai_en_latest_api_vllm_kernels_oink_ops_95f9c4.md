source: https://docs.vllm.ai/en/latest/api/vllm/kernels/oink_ops/
lastmod: 2026-09-23

#

`vllm.kernels.oink_ops`

[¶](https://docs.vllm.ai#vllm.kernels.oink_ops)

This file registers Oink implementations for vLLM IR ops.

vLLM does not depend on the external Oink repository/package. When an external plugin registers torch.library.custom_op entrypoints under the `oink::`

namespace (e.g. via vLLM's general_plugins mechanism), these ops will be marked as supported. To dispatch to those ops, set kernel_config.ir_op_priority.`VLLM_USE_OINK_OPS=1`

will add this to priority by default.

Functions:

-
–[has_oink_op](https://docs.vllm.ai#vllm.kernels.oink_ops.has_oink_op)Check if a specific oink op is registered.


Attributes:

-
–[oink_add_rms_supported](https://docs.vllm.ai#vllm.kernels.oink_ops.oink_add_rms_supported)Oink fused_add_rms_norm has the same constraints as rms_norm,

-
–[oink_rms_supported](https://docs.vllm.ai#vllm.kernels.oink_ops.oink_rms_supported)Oink rms only supports 2d-like inputs with contiguous weight


##

`oink_add_rms_supported = lambda x, x_residual, weight, epsilon, variance_size=None: variance_size is None and weight is not None and x.dim() >= 2 and x.dtype == weight.dtype and weight.is_contiguous() and _can_view_as_2d(x) and _is_oink_stride_compatible_2d(x.view(-1, x.shape[-1])) and x.dtype == x_residual.dtype and x.shape == x_residual.shape and _can_view_as_2d(x_residual) and _is_oink_stride_compatible_2d(x_residual.view(-1, x_residual.shape[-1]))`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.kernels.oink_ops.oink_add_rms_supported)

Oink fused_add_rms_norm has the same constraints as rms_norm, and residual must be 2d-like with compatible strides.

##

`oink_rms_supported = lambda x, weight, epsilon, variance_size=None: variance_size is None and weight is not None and x.dim() >= 2 and x.dtype == weight.dtype and weight.is_contiguous() and _can_view_as_2d(x) and _is_oink_stride_compatible_2d(x.view(-1, x.shape[-1]))`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.kernels.oink_ops.oink_rms_supported)

Oink rms only supports 2d-like inputs with contiguous weight and no variance_size override.

##

`_can_view_as_2d(x)`

[¶](https://docs.vllm.ai#vllm.kernels.oink_ops._can_view_as_2d)

Return True if x.view(-1, x.shape[-1]) is viewable (no copy).

## Source code in `vllm/kernels/oink_ops.py`


##

`_is_oink_stride_compatible_2d(x_2d)`

[¶](https://docs.vllm.ai#vllm.kernels.oink_ops._is_oink_stride_compatible_2d)

Return True if x_2d meets Oink's pointer-path stride constraints.