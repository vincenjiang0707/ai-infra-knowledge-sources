source: https://docs.vllm.ai/en/latest/api/vllm/lora/ops/triton_ops/utils/
lastmod: 2026-09-23

#

`vllm.lora.ops.triton_ops.utils`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.utils)

Functions:

-
–[supports_pdl](https://docs.vllm.ai#vllm.lora.ops.triton_ops.utils.supports_pdl)Refer to: https://github.com/triton-lang/triton/blob/v3.5.0/python/tutorials/11-programmatic-dependent-launch.py.


##

`_get_lora_a_ptr(lora_a_weights, device)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.utils._get_lora_a_ptr)

`_LORA_A_PTR_DICT`

collects the required information during `profile_run`

, After this, it remains constant and subsequent usage is through LUT. Refer to: https://github.com/triton-lang/triton/blob/release/3.1.x/python/tutorials/08-grouped-gemm.py

## Source code in `vllm/lora/ops/triton_ops/utils.py`


##

`_get_lora_b_ptr(lora_weights, offset_start, device)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.utils._get_lora_b_ptr)

`_LORA_B_PTR_DICT`

collects the required information during `profile_run`

, After this, it remains constant and subsequent usage is through LUT. Refer to: https://github.com/triton-lang/triton/blob/release/3.1.x/python/tutorials/08-grouped-gemm.py

## Source code in `vllm/lora/ops/triton_ops/utils.py`


|
|

##

`_normalize_lora_config_keys(config)`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.utils._normalize_lora_config_keys)

Normalize Triton config dict keys to uppercase BLOCK_SIZE_* format.

## Source code in `vllm/lora/ops/triton_ops/utils.py`


##

`supports_pdl(device=None)`

`cached`

[¶](https://docs.vllm.ai#vllm.lora.ops.triton_ops.utils.supports_pdl)

Refer to: https://github.com/triton-lang/triton/blob/v3.5.0/python/tutorials/11-programmatic-dependent-launch.py.