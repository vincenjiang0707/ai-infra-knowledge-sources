source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/falcon_h1/
lastmod: 2026-09-24

#

`vllm.model_executor.models.falcon_h1`

[¶](https://docs.vllm.ai#vllm.model_executor.models.falcon_h1)

Inference-only FalconH1 model.

Classes:

-
–[FalconH1ForCausalLM](https://docs.vllm.ai#vllm.model_executor.models.falcon_h1.FalconH1ForCausalLM) -
–[FalconH1ParallelHybrid](https://docs.vllm.ai#vllm.model_executor.models.falcon_h1.FalconH1ParallelHybrid)A hybrid decoder layer for FalconH1 where the input is processed

-
–[FalconH1SSMDecoderLayer](https://docs.vllm.ai#vllm.model_executor.models.falcon_h1.FalconH1SSMDecoderLayer)

##

`FalconH1ForCausalLM`

[¶](https://docs.vllm.ai#vllm.model_executor.models.falcon_h1.FalconH1ForCausalLM)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [HasInnerState](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.HasInnerState)

, [SupportsLoRA](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsLoRA)

, [SupportsPP](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)

, [IsHybrid](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.IsHybrid)[SupportsMambaPrefixCaching](https://docs.vllm.ai/interfaces/#vllm.model_executor.models.interfaces.SupportsMambaPrefixCaching)

Methods:

-
–[get_mamba_state_shape_from_config](https://docs.vllm.ai#vllm.model_executor.models.falcon_h1.FalconH1ForCausalLM.get_mamba_state_shape_from_config)Calculate shapes for Mamba's convolutional and state caches.


## Source code in `vllm/model_executor/models/falcon_h1.py`


|
|

###

`get_mamba_state_shape_from_config(vllm_config)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.falcon_h1.FalconH1ForCausalLM.get_mamba_state_shape_from_config)

Calculate shapes for Mamba's convolutional and state caches.

Parameters:

-

(`vllm_config`

[¶](https://docs.vllm.ai#vllm.model_executor.models.falcon_h1.FalconH1ForCausalLM.get_mamba_state_shape_from_config(vllm_config))

) –[VllmConfig](https://docs.vllm.ai/config/#vllm.config.VllmConfig)vLLM config


Returns:

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)]Tuple containing:

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)]- conv_state_shape: Shape for convolutional state cache

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)],[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)]]- temporal_state_shape: Shape for state space model cache


## Source code in `vllm/model_executor/models/falcon_h1.py`


##

`FalconH1ParallelHybrid`

[¶](https://docs.vllm.ai#vllm.model_executor.models.falcon_h1.FalconH1ParallelHybrid)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

A hybrid decoder layer for FalconH1 where the input is processed in parallel through both the self-attention branch and the SSM (Mamba) branch. Their outputs are then summed to produce the final hidden state.

## This layer uses

- FalconH1AttentionDecoderLayer for the multi-head self-attention branch.
- FalconH1SSMDecoderLayer for the state-space (Mamba) branch.

## Source code in `vllm/model_executor/models/falcon_h1.py`


|
|

##

`FalconH1SSMDecoderLayer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.falcon_h1.FalconH1SSMDecoderLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

## Source code in `vllm/model_executor/models/falcon_h1.py`


|
|

###

`_init_mup_vector()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.falcon_h1.FalconH1SSMDecoderLayer._init_mup_vector)

Non learnable per-block scaling vector composed of element-wise multipliersapplied to each separate contiguous block of the output of the linear projection (in_proj) before further processing (gating, convolution, SSM):

```
- Z block: [0 : d_ssm] → zxbcdt_multipliers[0]
- X block: [d_ssm : 2 * d_ssm] → zxbcdt_multipliers[1]
- B block: [2 * d_ssm : 2 * d_ssm + G * S] → zxbcdt_multipliers[2]
- C block: [2 * d_ssm + G * S : 2 * d_ssm + 2 * G * S]
→ zxbcdt_multipliers[3]
- dt block: [2 * d_ssm + 2 * G * S : end] → zxbcdt_multipliers[4]
```


## where

- d_ssm: Dimension of state-space model latent
- G: Number of groups (n_groups)
- S: SSM state size per group
- All indices are divided by tp_size to support tensor parallelism