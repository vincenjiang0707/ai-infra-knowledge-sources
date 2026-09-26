source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/config/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.fused_moe.config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config)

Classes:

-
–[FusedMoEConfig](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEConfig) -
–[FusedMoEParallelConfig](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEParallelConfig) -
–[FusedMoEQuantConfig](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEQuantConfig)The FusedMoEQuantConfig contains all the quantization parameters for

-
–[FusedMoEQuantDesc](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEQuantDesc)A quantization descriptor for fused MoE ops. This class can describe


Functions:

-
–[biased_moe_quant_config](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.biased_moe_quant_config)Construct a quant config for unquantized activations with biases.

-
–[fp8_w8a16_moe_quant_config](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.fp8_w8a16_moe_quant_config)Construct a quant config for 16-bit float activations and fp8 weights.

-
–[fp8_w8a8_moe_quant_config](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.fp8_w8a8_moe_quant_config)Construct a quant config for fp8 activations and fp8 weights.

-
–[gptq_marlin_moe_quant_config](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.gptq_marlin_moe_quant_config)Construct a quant config for gptq marlin quantization.

-
–[int4_w4a16_moe_quant_config](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.int4_w4a16_moe_quant_config)Construct a quant config for 16-bit float activations and int4 weights.

-
–[int4_w4afp8_moe_quant_config](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.int4_w4afp8_moe_quant_config)Construct a quant config for fp8 activations and int4 weights.

-
–[int8_w8a16_moe_quant_config](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.int8_w8a16_moe_quant_config)Construct a quant config for 16-bit float activations and int8 weights.

-
–[int8_w8a8_moe_quant_config](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.int8_w8a8_moe_quant_config)Construct a quant config for int8 activations and int8 weights.

-
–[mxfp4_moe_quant_config](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.mxfp4_moe_quant_config)Construct a quant config for MXFP4 x MXFP4 MoE.

-
–[mxfp4_mxfp8_moe_quant_config](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.mxfp4_mxfp8_moe_quant_config)Construct a quant config for mxfp4 activations and mxfp4 weights.

-
–[mxfp4_w4a16_moe_quant_config](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.mxfp4_w4a16_moe_quant_config)Construct a quant config for unquantized activations and mxfp4 weights.

-
–[mxfp4_w4a8_moe_quant_config](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.mxfp4_w4a8_moe_quant_config)Construct a quant config for fp8 activations and mxfp4 weights.

-
–[nvfp4_moe_quant_config](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.nvfp4_moe_quant_config)Construct a quant config for mxfp4 activations and nvp4 weights.

-
–[nvfp4_w4a16_moe_quant_config](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.nvfp4_w4a16_moe_quant_config)Construct a quant config for 16-but activations and nvp4 weights.

-
–[ocp_mx_moe_quant_config](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.ocp_mx_moe_quant_config)Construct a quant config for mxfp4 activations and mxfp4 weights.


##

`FusedMoEConfig`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEConfig)

Methods:

-
–[should_defer_moe_finalize](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEConfig.should_defer_moe_finalize)Return whether this invocation may defer the top-k reduction.


Attributes:

-
([use_deferred_moe_finalize](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEConfig.use_deferred_moe_finalize)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether experts may return an unfinalized output on this deployment.

-
([w13_num_shards](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEConfig.w13_num_shards)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of shards fused into w13: gate and up for gated, up only.


## Source code in `vllm/model_executor/layers/fused_moe/config.py`


|
|

###

`use_deferred_moe_finalize`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEConfig.use_deferred_moe_finalize)

Whether experts may return an unfinalized output on this deployment.

Evaluated on read rather than in `__post_init__`

because `defer_moe_finalize`

is set after construction, like `skip_final_all_reduce`

.

###

`w13_num_shards`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEConfig.w13_num_shards)

Number of shards fused into w13: gate and up for gated, up only.

###

`should_defer_moe_finalize(num_tokens)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEConfig.should_defer_moe_finalize)

Return whether this invocation may defer the top-k reduction.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


##

`FusedMoEParallelConfig`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEParallelConfig)

Methods:

-
–[make](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEParallelConfig.make)Determine MoE parallel configuration. Based on the input

`tp_size_`

, -
–[make_no_parallel](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEParallelConfig.make_no_parallel)For usage in CI/CD and testing.


## Source code in `vllm/model_executor/layers/fused_moe/config.py`


|
|

###

`make(tp_size_, pcp_size_, dp_size_, sp_size_, vllm_parallel_config)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEParallelConfig.make)

Determine MoE parallel configuration. Based on the input `tp_size_`

, `dp_size_`

and vllm's parallel config, determine what level's of parallelism to use in the fused moe layer.

Parameters:

-

(`tp_size_`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEParallelConfig.make(tp_size_))

) –[int](https://docs.python.org/3/builtins/functions.html#int)`tp_size`

passed into the FusedMoEFactory constructor. -

(`pcp_size_`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEParallelConfig.make(pcp_size_))

) –[int](https://docs.python.org/3/builtins/functions.html#int)`pcp_size`

passed into the FusedMoEFactory constructor. -

(`dp_size_`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEParallelConfig.make(dp_size_))

) –[int](https://docs.python.org/3/builtins/functions.html#int)`dp_size`

passed into the FusedMoEFactory constructor. -

(`sp_size_`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEParallelConfig.make(sp_size_))

) –[int](https://docs.python.org/3/builtins/functions.html#int)`sp_size`

passed into the FusedMoEFactory constructor. -

(`vllm_parallel_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEParallelConfig.make(vllm_parallel_config))

) –[ParallelConfig](https://docs.vllm.ai/config/#vllm.config.ParallelConfig)vLLM's parallel config object which contains the

`enable_expert_parallel`

flag.

Examples:

When there is no parallelism requested, i.e. `tp_size_`

= `pcp_size_`

= `dp_size_`

= 1, we simply return the sizes unaltered and the ranks set to 0.

Expert Parallelism is considered only when either `dp_size_`

, `pcp_size_`

or `tp_size_`

is non trivial.

Note that PCP serves the same function as DP here.

When TP = 2, DP(PCP) = 1 and EP = False, the configuration on different devices:

- device 0 : TP = {2, 0} DP = {1, 0} EP = {1, 0} // legend : {size, rank}
- device 1 : TP = {2, 1} DP = {1, 0} EP = {1, 0}
- Comment : Tensors are sharded across 2 devices.

When TP = 1, DP(PCP) = 2 and EP = False, the configuration on different devices:

- device 0 : TP = {2, 0} DP = {2, 0} EP = {1, 0}
- device 1 : TP = {2, 1} DP = {2, 1} EP = {1, 0}
- Comment: There are 2 engine instances and the tensors are sharded across 2 decvices.

When TP = 2, DP(PCP) = 2 and EP = False, the configuration on different devices:

- device 0: TP = {4, 0} DP = {2, 0} EP = {1, 0}
- device 1: TP = {4, 1} DP = {2, 0} EP = {1, 0}
- device 2: TP = {4, 2} DP = {2, 1} EP = {1, 0}
- device 3: TP = {4, 3} DP = {2, 1} EP = {1, 0}
- Comment: There are 2 engine instances and the tensors are sharded across 4 devices.

When, TP = 2, DP(PCP) = 1 and EP = True, the configuration on different devices:

- device 0: TP = {1, 0} DP = {1, 0} EP = {2, 0}
- device 1: TP = {1, 0} DP = {1, 0} EP = {2, 1}
- Comment: The experts are split between the 2 devices.

When, TP = 1, DP(PCP) = 2 and EP = True, the configuration on different devices:

- device 0: TP = {1, 0} DP = {2, 0} EP = {2, 0}
- device 1: TP = {1, 0} DP = {2, 1} EP = {2, 1}
- Comment: There are 2 engine instances and the experts are split between the 2 devices.

When TP = 2, DP(PCP) = 2 and EP = True, the configuration on different devices:

- device 0: TP = {1, 0} DP = {2, 0} EP = {4, 0}
- device 1: TP = {1, 0} DP = {2, 0} EP = {4, 1}
- device 2: TP = {1, 0} DP = {2, 1} EP = {4, 2}
- device 3: TP = {1, 0} DP = {2, 1} EP = {4, 3}
- Comment: There are 2 engine instances and the experts are split between the 4 devices.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


|
|

###

`make_no_parallel()`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEParallelConfig.make_no_parallel)

For usage in CI/CD and testing.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


##

`FusedMoEQuantConfig`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEQuantConfig)

The FusedMoEQuantConfig contains all the quantization parameters for a single FusedMoEMethodBase operation. It consists of four FusedMoEQuantDescs, one for each activation and set of weights.

Each FusedMoEMethodBase must implement a get_fused_moe_quant_config method to construct a FusedMoEQuantConfig for use with that class.

FusedMoEQuant configs are only used for modular kernels, fused_experts (from fused_moe.py), cutlass_moe_fp[48], rocm_aiter_fused_experts and triton_kernel_moe_forward. Other MoE methods can ignore the FusedMoEQuantConfig (for now) and hardcode it to None.

There are currently some restrictions on what can be expressed: - Most MoE ops only support similar quantization strategies for each parameter, e.g. both weights must have the same GroupShape and both activations must share the same GroupShape. One exception to this is the cutlass moe which allows per channel quantization on the outputs. Note: this restrictions are not always rigorously checked. - Not all fused MoE functions support all the parameters, e.g. zero points, global scales, alphas and biases are not universally supported. - Fully general GroupShapes are not allowed. Activations only support per token, per tensor or K-blocked. - Weights are not required to have a GroupShape since they have already been quantized.

Other notes: - PrecisionConfigs are specific to GPT OSS Triton. - As a follow up it would probably make sense to subclass FusedMoEQuantDesc or FusedMoEQuantConfig for particular FusedMoEMethodBase subclasses so that only the required quantization parameters are used/stored.

Methods:

-
–[batched_scale_shape](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEQuantConfig.batched_scale_shape)Construct the proper activation batched scale shape for this

-
–[config_name](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEQuantConfig.config_name)Return a string used to construct the filename that contains the

-
–[make](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEQuantConfig.make)General builder function for a FusedMoEQuantConfig.

-
–[scale_shape](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEQuantConfig.scale_shape)Construct the proper activation scale shape for this


## Source code in `vllm/model_executor/layers/fused_moe/config.py`


|
|

###

`batched_scale_shape(num_experts, max_tokens, hidden_dim)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEQuantConfig.batched_scale_shape)

Construct the proper activation batched scale shape for this config, e.g. (num experts, *scale_shape).

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


###

`config_name(dtype)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEQuantConfig.config_name)

Return a string used to construct the filename that contains the tuning info for a particular quantization scheme. See try_get_optimal_moe_config in fused_moe.py.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


###

`make(quant_dtype=None, per_act_token_quant=False, per_out_ch_quant=False, block_shape=None, w1_scale=None, w2_scale=None, a1_scale=None, a2_scale=None, g1_alphas=None, g2_alphas=None, a1_gscale=None, a2_gscale=None, w1_bias=None, w2_bias=None, w1_zp=None, w2_zp=None, weight_dtype=None, is_scale_swizzled=True, gemm1_alpha=None, gemm1_beta=None, gemm1_clamp_limit=None)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEQuantConfig.make)

General builder function for a FusedMoEQuantConfig. - quant_dtype: Optional quantization type. None if activations are unquantized or quantized prior to calling. Note: "nvfp4", "mxfp4", "mxfp6_e3m2", "mxfp6_e2m3" are the only valid string values for quant_dtype. - per_act_token_quant: Activations have per token quantization. - per_out_ch_quant: Outputs have per channel quantization. (only for cutlass). - block_shape: Optional block size for block-wise quantization. Incompatible with per_act_token and per_out_ch quant. - w1_scale: Optional scale to be used for w1. - w2_scale: Optional scale to be used for w2. - a1_scale: Optional scale to be used for a1. - a2_scale: Optional scale to be used for a2. - g1_alphas: Optional global quantization scales for w1 (for nvfp4). Optional per-channel scales for w1 (for W4A8 FP8). Optional dq scale i.e. w_scale * a_scale (for W8A8 fp8). - g2_alphas: Optional global quantization scales for w2 (for nvfp4). Optional per-channel scales for w2 (for W4A8 FP8). Optional dq scale i.e. w_scale * a_scale (for W8A8 fp8). - a1_gscale: Optional global quantization scales for a1 (1.0 /a2_scale). - a2_gscale: Optional global quantization scales for a2 (1.0 /a2_scale).

- w1_bias: Optional biases for w1 (GPT OSS Triton).
- w2_bias: Optional biases for w1 (GPT OSS Triton).
- w1_zp: Optional w1 zero points for int4/int8 quantization.
- w2_zp: Optional w2 zero points for int4/int8 quantization.
- is_scale_swizzled: Whether the activation scale-factor layout is swizzled. Pass through to the underlying quantization kernel for dtypes that distinguish layouts (nvfp4, mxfp8). Defaults to True.
- gemm1_alpha: Optional MXFP4 TRTLLM SwiGLU alpha parameter.
- gemm1_beta: Optional MXFP4 TRTLLM SwiGLU beta parameter.
- gemm1_clamp_limit: Optional MXFP4 TRTLLM SwiGLU clamp limit.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


|
|

###

`scale_shape(max_tokens, hidden_dim)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEQuantConfig.scale_shape)

Construct the proper activation scale shape for this config.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


##

`FusedMoEQuantDesc`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.FusedMoEQuantDesc)

A quantization descriptor for fused MoE ops. This class can describe either activations or weights.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


##

`_get_config_dtype_str(dtype, use_fp8_w8a8=False, use_fp8_w8a16=False, use_int8_w8a16=False, use_int4_w4a16=False, ocp_mx_scheme=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config._get_config_dtype_str)

Return a string used to construct the filename that contains the tuning info for a particular quantization scheme. See try_get_optimal_moe_config in fused_moe.py.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


##

`_quant_flags_to_group_shape(quant_dtype, per_act_token_quant, per_out_ch_quant, block_shape)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config._quant_flags_to_group_shape)

Convert MoE quantization flags into more generic GroupShapes.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


##

`biased_moe_quant_config(w1_bias, w2_bias, gemm1_alpha=None, gemm1_beta=None, gemm1_clamp_limit=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.biased_moe_quant_config)

Construct a quant config for unquantized activations with biases.

gemm1_alpha/gemm1_beta/gemm1_clamp_limit carry the SwiGLU gate params through to the fused activation kernel (e.g. swigluoai_uninterleave).

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


##

`fp8_w8a16_moe_quant_config(w1_scale, w2_scale, w1_bias=None, w2_bias=None, block_shape=None, gemm1_alpha=None, gemm1_beta=None, gemm1_clamp_limit=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.fp8_w8a16_moe_quant_config)

Construct a quant config for 16-bit float activations and fp8 weights.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


##

`fp8_w8a8_moe_quant_config(w1_scale, w2_scale, a1_scale=None, a2_scale=None, w1_bias=None, w2_bias=None, per_act_token_quant=False, per_out_ch_quant=False, block_shape=None, a1_gscale=None, a2_gscale=None, g1_alphas=None, g2_alphas=None, gemm1_alpha=None, gemm1_beta=None, gemm1_clamp_limit=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.fp8_w8a8_moe_quant_config)

Construct a quant config for fp8 activations and fp8 weights.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


##

`gptq_marlin_moe_quant_config(w1_scale, w2_scale, weight_bits, group_size, w1_zp=None, w2_zp=None, w1_bias=None, w2_bias=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.gptq_marlin_moe_quant_config)

Construct a quant config for gptq marlin quantization.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


##

`int4_w4a16_moe_quant_config(w1_scale, w2_scale, w1_zp=None, w2_zp=None, w1_bias=None, w2_bias=None, block_shape=None, a1_gscale=None, a2_gscale=None, gemm1_clamp_limit=None, gemm1_alpha=None, gemm1_beta=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.int4_w4a16_moe_quant_config)

Construct a quant config for 16-bit float activations and int4 weights.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


##

`int4_w4afp8_moe_quant_config(w1_scale, w2_scale, g1_alphas, g2_alphas, per_act_token_quant=False, per_out_ch_quant=False, block_shape=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.int4_w4afp8_moe_quant_config)

Construct a quant config for fp8 activations and int4 weights.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


##

`int8_w8a16_moe_quant_config(w1_scale, w2_scale, w1_zp=None, w2_zp=None, w1_bias=None, w2_bias=None, block_shape=None, a1_gscale=None, a2_gscale=None, gemm1_clamp_limit=None, gemm1_alpha=None, gemm1_beta=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.int8_w8a16_moe_quant_config)

Construct a quant config for 16-bit float activations and int8 weights.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


##

`int8_w8a8_moe_quant_config(w1_scale, w2_scale, a1_scale, a2_scale, w1_bias=None, w2_bias=None, per_act_token_quant=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.int8_w8a8_moe_quant_config)

Construct a quant config for int8 activations and int8 weights.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


##

`mxfp4_moe_quant_config(w1_scale, w2_scale)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.mxfp4_moe_quant_config)

Construct a quant config for MXFP4 x MXFP4 MoE. MXFP4 uses block scaling only (E8M0 scales, 32-element groups), with no separate alphas / global activation scales in this config.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


##

`mxfp4_mxfp8_moe_quant_config(w1_scale, w2_scale, a1_scale=None, a2_scale=None, w1_bias=None, w2_bias=None, block_shape=None, gemm1_alpha=None, gemm1_beta=None, gemm1_clamp_limit=None, mx_alignment=0, is_scale_swizzled=True)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.mxfp4_mxfp8_moe_quant_config)

Construct a quant config for mxfp4 activations and mxfp4 weights.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


##

`mxfp4_w4a16_moe_quant_config(w1_scale, w2_scale, w1_bias=None, w2_bias=None, gemm1_alpha=None, gemm1_beta=None, gemm1_clamp_limit=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.mxfp4_w4a16_moe_quant_config)

Construct a quant config for unquantized activations and mxfp4 weights.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


##

`mxfp4_w4a8_moe_quant_config(w1_scale, w2_scale, a1_scale=None, a2_scale=None, w1_bias=None, w2_bias=None, block_shape=None, gemm1_clamp_limit=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.mxfp4_w4a8_moe_quant_config)

Construct a quant config for fp8 activations and mxfp4 weights.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


##

`nvfp4_moe_quant_config(g1_alphas, g2_alphas, a1_gscale, a2_gscale, w1_scale, w2_scale, w1_bias=None, w2_bias=None, is_scale_swizzled=True, gemm1_alpha=None, gemm1_beta=None, gemm1_clamp_limit=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.nvfp4_moe_quant_config)

Construct a quant config for mxfp4 activations and nvp4 weights.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


##

`nvfp4_w4a16_moe_quant_config(g1_alphas, g2_alphas, w1_scale, w2_scale, gemm1_alpha=None, gemm1_beta=None, gemm1_clamp_limit=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.nvfp4_w4a16_moe_quant_config)

Construct a quant config for 16-but activations and nvp4 weights.

## Source code in `vllm/model_executor/layers/fused_moe/config.py`


##

`ocp_mx_moe_quant_config(quant_dtype, w1_scale, w2_scale, weight_dtype=None, a1_scale=None, a2_scale=None, w1_bias=None, w2_bias=None, block_shape=None, gemm1_alpha=None, gemm1_beta=None, gemm1_clamp_limit=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.config.ocp_mx_moe_quant_config)

Construct a quant config for mxfp4 activations and mxfp4 weights.