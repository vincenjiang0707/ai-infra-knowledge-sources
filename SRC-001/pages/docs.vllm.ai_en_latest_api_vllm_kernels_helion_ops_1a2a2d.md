source: https://docs.vllm.ai/en/latest/api/vllm/kernels/helion/ops/
lastmod: 2026-09-23

#

`vllm.kernels.helion.ops`

[¶](https://docs.vllm.ai#vllm.kernels.helion.ops)

Helion kernel implementation.

Importing this package does NOT register any kernels. Runtime code imports the specific op module it needs, e.g.::

```
from vllm.kernels.helion.ops import scaled_mm # noqa: F401
```


which triggers that op's `@register_kernel`

as an import side effect.

Tools that need the full registry (e.g. scripts/autotune_helion_kernels.py) call `import_all_ops()`

to force every op module to register.

Modules:

-
–[dynamic_per_token_scaled_fp8_quant](https://docs.vllm.ai/dynamic_per_token_scaled_fp8_quant/#vllm.kernels.helion.ops.dynamic_per_token_scaled_fp8_quant) -
–[fused_qk_norm_rope](https://docs.vllm.ai/fused_qk_norm_rope/#vllm.kernels.helion.ops.fused_qk_norm_rope) -
–[per_token_group_fp8_quant](https://docs.vllm.ai/per_token_group_fp8_quant/#vllm.kernels.helion.ops.per_token_group_fp8_quant) -
–[rms_norm_dynamic_per_token_quant](https://docs.vllm.ai/rms_norm_dynamic_per_token_quant/#vllm.kernels.helion.ops.rms_norm_dynamic_per_token_quant) -
–[rms_norm_per_block_quant](https://docs.vllm.ai/rms_norm_per_block_quant/#vllm.kernels.helion.ops.rms_norm_per_block_quant) -
–[silu_and_mul_per_block_quant](https://docs.vllm.ai/silu_and_mul_per_block_quant/#vllm.kernels.helion.ops.silu_and_mul_per_block_quant) -
–[silu_mul_fp8](https://docs.vllm.ai/silu_mul_fp8/#vllm.kernels.helion.ops.silu_mul_fp8)

Functions:

-
–[import_all_kernels](https://docs.vllm.ai#vllm.kernels.helion.ops.import_all_kernels)Import every kernel submodule so all

`@register_kernel`

decorators run.

##

`import_all_kernels()`

[¶](https://docs.vllm.ai#vllm.kernels.helion.ops.import_all_kernels)

Import every kernel submodule so all `@register_kernel`

decorators run.

Returns: