source: https://docs.vllm.ai/en/latest/design/custom_op/
lastmod: 2026-09-24

# CustomOp[¶](https://docs.vllm.ai#customop)

[ CustomOp](https://docs.vllm.ai/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp) is an abstract class used for dispatching the forward method of various operations to the appropriate backend. It also offers a mechanism for both vLLM and OOT (Out-Of-Tree) plugins to register their custom operations.

This document will introduce how CustomOp works in vLLM and how to implement a new [ CustomOp](https://docs.vllm.ai/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp).

## How CustomOp Works in vLLM[¶](https://docs.vllm.ai#how-customop-works-in-vllm)

[ CustomOp](https://docs.vllm.ai/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp) manages two dictionaries of all custom ops (i.e., op classes, indexed by registered name) in its class, for vLLM and OOT plugins respectively.

We can use `@CustomOp.register("op_name")`

to register an op class to the [ CustomOp](https://docs.vllm.ai/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp) system. After this, the

`op_name`

and its class will be added into the `op_registry`

dictionary. In addition, We can also register an OOT op by `@CustomOp.register_oot("op_name")`

. We will introduce this mechanism in detail later.When a [ CustomOp](https://docs.vllm.ai/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp) is called (i.e., call its

`forward()`

method), if it is enabled (i.e., with `--compilation_config.custom_ops '["+op_name"]'`

), it will automatically dispatch the forward method to the appropriate backend according to `current_platform`

. Otherwise (i.e., it is disabled), it will only call the `forward_native()`

method to use PyTorch-native implementation of this forward method.**CPU platform:**dispatch to`forward_cpu()`

.**CUDA platform:**dispatch to`forward_cuda()`

.**ROCm platform:**dispatch to`forward_hip()`

. If`forward_hip()`

is not implemented, it will use`forward_cuda()`

as a fallback.**XPU platform:**dispatch to`forward_xpu()`

.**TPU platform:**dispatch to`forward_tpu()`

.**OOT platform:**dispatch to`forward_oot()`

. This will only be called on OOT platforms.**Default:**dispatch to`forward_native()`

as a final fallback for all platforms.

Note

Note that the dispatching logic might not be absolute because of class inheritance. Derived class might override the behavior.

Furthermore, vLLM decides whether to enable or disable a [ CustomOp](https://docs.vllm.ai/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp) based on

`compilation_config.custom_ops`

. To be specific, if a [is not registered in](https://docs.vllm.ai/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp)

`CustomOp`

`compilation_config.custom_ops`

(i.e., uses the default config), it will be enabled if `compilation_config.custom_ops`

contains `all`

, or will be disabled if it contains `none`

.Note

Note that `all`

and `none`

cannot coexist in `compilation_config.custom_ops`

.

By default, if `compilation_config.backend == "inductor"`

and `compilation_config.mode != CompilationMode.NONE`

, a `none`

will be appended into `compilation_config.custom_ops`

, otherwise a `all`

will be appended. In other words, this means [ CustomOp](https://docs.vllm.ai/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp) will be disabled in some platforms (i.e., those use

`inductor`

as default backend for `torch.compile`

) when running with torch compile mode. In this case, Inductor generates (fused) Triton kernels for those disabled custom ops.Note

For multi-modal models, vLLM has enforced the enabling of some custom ops to use device-specific deep-optimized kernels for better performance in ViT part, such as [ MMEncoderAttention](https://docs.vllm.ai/api/vllm/model_executor/layers/attention/mm_encoder_attention/#vllm.model_executor.layers.attention.mm_encoder_attention.MMEncoderAttention) and

`ApplyRotaryEmb`

. We can also pass a `enforce_enable=True`

param to the `__init__()`

method of the [to enforce enable itself at object-level.](https://docs.vllm.ai/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp)

`CustomOp`

Note that this `enforce_enable`

mechanism will be removed after we add a separate `compilation_config`

for multi-modal part.

## How to Customise Your Configuration for CustomOp[¶](https://docs.vllm.ai#how-to-customise-your-configuration-for-customop)

vLLM also offers fine-grained control over which custom ops to enable or disable for users, by manually passing a `--compilation_config.custom_ops '["..."]'`

when launching a server.

For example:

- Use
`--compilation_config.custom_ops '["all"]'`

to enable all custom ops. - Use
`--compilation_config.custom_ops '["none"]'`

to disable all custom ops. - Use
`--compilation_config.custom_ops '["all,-op1"]'`

to enable all custom ops except op1 (i.e., prefixed with a`-`

means "disable"). - Use
`--compilation_config.custom_ops '["none,+op1,+op2"]'`

to only enable op1 and op2 (i.e., prefixed with a`+`

means "enable").

## Types of Supported CustomOp in vLLM[¶](https://docs.vllm.ai#types-of-supported-customop-in-vllm)

**1. Attention:**

@PluggableLayer.register("multi_head_latent_attention")
class MultiHeadLatentAttentionWrapper(PluggableLayer):
"""Pluggable MLA layer which allows OOT backends to add
custom implementations of the outer MLA layer (including rope & o_proj).
Note that currently oot platforms can still use CustomOp.register_oot to
replace MLA layer entirely, although we use PluggableLayer to register
this layer now.
This class takes positions and hidden_states as input.
The input tensors can either contain prefill tokens or decode tokens.
The class does the following:
1. MLA Preprocess.
2. Perform multi-head attention to prefill tokens and
multi-query attention to decode tokens separately.
3. Return the output tensor.
"""


**2. Activation:**

@CustomOp.register("silu_and_mul")
class SiluAndMul(CustomOp):
"""An activation function for SwiGLU.
The function computes x -> silu(x[:d]) * x[d:] where d = x.shape[-1] // 2.
Shapes:
x: (num_tokens, 2 * d) or (batch_size, seq_len, 2 * d)
return: (num_tokens, d) or (batch_size, seq_len, d)
"""
@CustomOp.register("mul_and_silu")
class MulAndSilu(CustomOp):
"""An activation function for SwiGLU.
The function computes x -> x[:d] * silu(x[d:]) where d = x.shape[-1] // 2.
Shapes:
x: (num_tokens, 2 * d) or (batch_size, seq_len, 2 * d)
return: (num_tokens, d) or (batch_size, seq_len, d)
"""
@CustomOp.register("gelu_new")
class NewGELU(CustomOp):
@CustomOp.register("gelu_fast")
class FastGELU(CustomOp):
@CustomOp.register("quick_gelu")
class QuickGELU(CustomOp):
# https://github.com/huggingface/transformers/blob/main/src/transformers/activations.py#L90
@CustomOp.register("gelu_and_mul")
class GeluAndMul(CustomOp):
"""An activation function for GeGLU.
The function computes x -> GELU(x[:d]) * x[d:] where d = x.shape[-1] // 2.
Shapes:
x: (batch_size, seq_len, 2 * d) or (num_tokens, 2 * d)
return: (batch_size, seq_len, d) or (num_tokens, d)
"""
@CustomOp.register("gelu_and_mul_sparse")
class GeluAndMulSparse(CustomOp):
"""An activation function for GeluAndMulSparse.
This activation function is used in Gemma3n. It computes:
up_proj = self.up_proj(x)
gate_proj = self.gate_proj(x)
gate_proj = self._gaussian_topk(gate_proj) # sparsity
activations = self.act_fn(gate_proj) # gelu
down_proj = self.down_proj(activations * up_proj)
Shapes:
x: (num_tokens, 2 * d) or (batch_size, seq_len, 2 * d)
return: (num_tokens, d) or (batch_size, seq_len, d)
"""
@CustomOp.register("relu2")
class ReLUSquaredActivation(CustomOp):
"""Applies the relu^2 activation introduced in https://arxiv.org/abs/2109.08668v2."""
@CustomOp.register("xielu")
class XIELU(CustomOp):
"""Applies the xIELU activation function introduced in https://arxiv.org/abs/2411.13010
If the user has installed the nickjbrowning/XIELU, we import xIELU CUDA
Otherwise, we emit a single warning and use xIELU Python
"""
@CustomOp.register("swigluoai_and_mul")
class SwigluOAIAndMul(CustomOp):
# https://github.com/huggingface/transformers/blob/v4.55.0/src/transformers/models/gpt_oss/modeling_gpt_oss.py#L106-L110
@CustomOp.register("fatrelu_and_mul")
class FatreluAndMul(CustomOp):
"""An activation function for FATReLU.
The function computes x -> FATReLU(x[:d]) * x[d:] where
d = x.shape[-1] // 2.
This is used in openbmb/MiniCPM-S-1B-sft.
Shapes:
x: (num_tokens, 2 * d) or (batch_size, seq_len, 2 * d)
return: (num_tokens, d) or (batch_size, seq_len, d)
"""


**3. MM-Conv:**

@CustomOp.register("conv2d")
class Conv2dLayer(ConvLayerBase):
"""Conv layer with Conv2d."""
@CustomOp.register("conv3d")
class Conv3dLayer(ConvLayerBase):
"""Conv layer with Conv3d."""


**4. Embedding:**

@PluggableLayer.register("vocab_parallel_embedding")
class VocabParallelEmbedding(PluggableLayer):
"""Embedding parallelized in the vocabulary dimension.
Adapted from torch.nn.Embedding, note that we pad the vocabulary size to
make sure it is divisible by the number of model parallel GPUs.
In order to support various loading methods, we ensure that LoRA-added
embeddings are always at the end of TP-sharded tensors. In other words,
we shard base embeddings and LoRA embeddings separately (both padded),
and place them in the same tensor.
In this example, we will have the original vocab size = 1010,
added vocab size = 16 and padding to 64. Therefore, the total
vocab size with padding will be 1088 (because we first pad 1010 to
1024, add 16, and then pad to 1088).
Therefore, the tensor format looks like the following:
TP1, rank 0 (no sharding):
|< --------BASE-------- >|< -BASE PADDING-- >|< -----LORA------ >|< -LORA PADDING-- >|
corresponding token_id: | 0 | 1 | ... | 1009 | -1 | ... | -1 | 1010 | ... | 1025 | -1 | ... | -1 |
index: | 0 | 1 | ... | 1009 | 1010 | ... | 1023 | 1024 | ... | 1039 | 1040 | ... | 1087 |
TP2, rank 0:
|< --------------------BASE--------------------- >|< -----LORA------ >|< -LORA PADDING- >|
corresponding token_id: | 0 | 1 | 2 | ... | 497 | 498 | ... | 511 | 1010 | ... | 1025 | -1 | ... | -1 |
index: | 0 | 1 | 2 | ... | 497 | 498 | ... | 511 | 512 | ... | 527 | 528 | ... | 543 |
TP2, rank 1:
|< -----------BASE----------- >|< -BASE PADDING- >|< -----------LORA PADDING----------- >|
corresponding token_id: | 512 | 513 | 514 | ... | 1009 | -1 | ... | -1 | -1 | ... | -1 | -1 | ... | -1 |
index: | 0 | 1 | 2 | ... | 497 | 498 | ... | 511 | 512 | ... | 527 | 528 | ... | 543 |
Args:
num_embeddings: vocabulary size.
embedding_dim: size of hidden state.
params_dtype: type of the parameters.
org_num_embeddings: original vocabulary size (without LoRA).
padding_size: padding size for the vocabulary.
quant_config: quant config for the layer
prefix: full name of the layer in the state dict
disable_tp: If true, tensor parallelism will be disabled for this layer.
quant_method: Preselected quantization method for model-specific layers.
parallel_group: Process group used to shard and reduce the embedding.
""" # noqa: E501
@PluggableLayer.register("parallel_lm_head")
class ParallelLMHead(VocabParallelEmbedding):
"""Parallelized LM head.
Output logits weight matrices used in the Sampler. The weight and bias
tensors are padded to make sure they are divisible by the number of
model parallel GPUs.
Args:
num_embeddings: vocabulary size.
embedding_dim: size of hidden state.
bias: whether to use bias.
params_dtype: type of the parameters.
org_num_embeddings: original vocabulary size (without LoRA).
padding_size: padding size for the vocabulary.
disable_tp: If true, tensor parallelism will be disabled for this layer.
"""


**5. Linear:**

@PluggableLayer.register("row_parallel_linear")
class RowParallelLinear(LinearBase):
"""Linear layer with row parallelism.
The linear layer is defined as Y = XA + b. A is parallelized along
its first dimension and X along its second dimension as:
- -
| A_1 |
| . |
A = | . | X = [X_1, ..., X_p]
| . |
| A_p |
- -
Arguments:
input_size: first dimension of matrix A.
output_size: second dimension of matrix A.
bias: If true, add bias. Note that bias is not parallelized.
input_is_parallel: If true, we assume that the input is already
split across the GPUs and we do not split
again.
skip_bias_add: This was added to enable performance optimization where
bias can be fused with other element-wise operations.
We skip adding bias but instead return it.
params_dtype: Data type for the parameters.
reduce_results: If true, call all-reduce on output and make Y available
to all GPUs, otherwise, every GPU will have its output
which is Y = X_iA_i
quant_config: Quantization configure.
prefix: The name of the layer in the state dict, including all parents
(e.g. model.layers.0.down_proj)
return_bias: If true, return bias together with outputs in forward pass.
disable_tp: If true, weights matrix won't be sharded through tp rank.
"""
@PluggableLayer.register("column_parallel_linear")
class ColumnParallelLinear(LinearBase):
"""Linear layer with column parallelism.
The linear layer is defined as Y = XA + b. A is parallelized along
its second dimension as A = [A_1, ..., A_p].
Args:
input_size: first dimension of matrix A.
output_size: second dimension of matrix A.
bias: If true, add bias.
gather_output: If true, call all-gather on output and make Y available
to all GPUs, otherwise, every GPU will have its output
which is Y_i = XA_i
skip_bias_add: This was added to enable performance optimizations where
bias can be fused with other element-wise operations. we
skip adding bias but instead return it.
params_dtype: Data type for the parameters.
quant_config: Quantization configure.
prefix: The name of the layer in the state dict, including all parents
(e.g. model.layers.0.qkv_proj)
return_bias: If true, return bias together with outputs in forward pass.
disable_tp: If true, weights matrix won't be sharded through tp rank.
tp_rank: Override the tensor-parallel rank used for sharding. Defaults to
the global TP rank. Used to shard at a coarser granularity than one
shard per rank (see ``DCPGroupColumnParallelLinear``).
tp_size: Override the tensor-parallel world size used for sharding.
Defaults to the global TP world size.
"""
@PluggableLayer.register("replicated_linear")
class ReplicatedLinear(LinearBase):
"""Replicated linear layer.
Args:
input_size: input dimension of the linear layer.
output_size: output dimension of the linear layer.
bias: If true, add bias.
skip_bias_add: If true, skip adding bias but instead return it.
params_dtype: Data type for the parameters.
quant_config: Quantization configure.
prefix: The name of the layer in the state dict, including all parents
(e.g. model.layers.0.qkv_proj)
return_bias: If true, return bias together with outputs in forward pass.
disable_tp: Take no effect for replicated linear layers.
"""


**6. Logits Processor:**

@PluggableLayer.register("logits_processor")
class LogitsProcessor(PluggableLayer):
"""Process logits and apply logits processors from sampling metadata.
This layer does the following:
1. Gather logits from model hidden_states.
2. Scale logits if needed.
3. Apply logits processors (if any).
"""


**7. Mamba:**

@PluggableLayer.register("mamba_mixer")
class MambaMixer(MambaBase, PluggableLayer):
"""Compute ∆, A, B, C, and D the state space parameters and compute
the `contextualized_states`. A, D are input independent
(see Mamba paper [1] Section 3.5.2 "Interpretation of A"
for why A isn't selective) ∆, B, C are input-dependent
(this is a key difference between Mamba and the linear time
invariant S4, and is why Mamba is called
**selective** state spaces)
"""
@PluggableLayer.register("mamba_mixer2")
class MambaMixer2(MambaBase, PluggableLayer):
"""Compute ∆, A, B, C, and D the state space parameters and compute
the `contextualized_states`. A, D are input independent
(see Mamba paper [1] Section 3.5.2 "Interpretation of A"
for why A isn't selective) ∆, B, C are input-dependent
(this is a key difference between Mamba and the linear time
invariant S4, and is why Mamba is called
**selective** state spaces)
"""
@CustomOp.register("mixer2_gated_rms_norm")
class Mixer2RMSNormGated(CustomOp):
@PluggableLayer.register("short_conv")
class ShortConv(MambaBase, PluggableLayer):


**8. MoE:**

@CustomOp.register("modular_fused_moe")
class FusedMoEModularMethod(FusedMoEMethodBase, CustomOp):
@CustomOp.register("unquantized_fused_moe")
class UnquantizedFusedMoEMethod(FusedMoEMethodBase, CustomOp):
"""MoE method without quantization."""
@PluggableLayer.register("transformers_fused_moe")
class TransformersMoERunner(MoERunner):
"""Custom MoERunner for the Transformers modeling backend."""
@CustomOp.register("grouped_topk")
class GroupedTopk(CustomOp):
"""GroupedTopk used by the Deepseek-V2 and Deepseek-V3 model."""


**9. Norm:**

@CustomOp.register("rms_norm")
class RMSNorm(CustomOp):
"""Root mean square normalization.
Computes x -> w * x / sqrt(E[x^2] + eps) where w is the learned weight.
Refer to https://arxiv.org/abs/1910.07467
"""
@CustomOp.register("rms_norm_gated")
class RMSNormGated(CustomOp):
"""RMS Normalization with optional gating.
This is a native PyTorch implementation that supports:
- Standard RMS normalization
- Group RMS normalization
- Optional gating with SiLU activation
"""
@CustomOp.register("gemma_rms_norm")
class GemmaRMSNorm(CustomOp):
"""RMS normalization for Gemma.
Two differences from the above RMSNorm:
1. x * (1 + w) instead of x * w.
2. (x * w).to(orig_dtype) instead of x.to(orig_dtype) * w.
"""


**10. Quantization:**

@CustomOp.register("quant_fp8")
class QuantFP8(CustomOp):
"""Quantize input tensor to FP8 (per-tensor, per-token, per-channel, or per-group).
This CustomOp supports both static and dynamic quantization.
"""


**11. Rope:**

@CustomOp.register("rotary_embedding")
class RotaryEmbeddingBase(CustomOp):
"""Original rotary positional embedding."""
@CustomOp.register("dual_chunk_rotary_embedding")
class DualChunkRotaryEmbedding(CustomOp):
"""Rotary positional embedding for Dual Chunk Attention."""
@CustomOp.register("apply_rotary_emb")
class ApplyRotaryEmb(CustomOp):


**12. Encoder:**

@PluggableLayer.register("qwen2_decoder")
class CustomQwen2Decoder(PluggableLayer):
"""Qwen2 visual encoder
non-causal attention + causal attention
token_type_ids ：0=non-causal, 1=causal
"""
@CustomOp.register("mm_encoder_attn")
class MMEncoderAttention(CustomOp):
"""Multi-headed attention without any cache, used for multimodal encoder."""
@PluggableLayer.register("rel_pos_attention")
class RelPosAttention(PluggableLayer):
"""Multi-head Attention block with relative position embeddings."""


## Guidelines for Implementing a New CustomOp[¶](https://docs.vllm.ai#guidelines-for-implementing-a-new-customop)

### Implement a New CustomOp in vLLM[¶](https://docs.vllm.ai#implement-a-new-customop-in-vllm)

This part is a tutorial of how to implement a New [ CustomOp](https://docs.vllm.ai/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp) in vLLM.

Steps:

- Implement a new op class, which extends from
base class.`CustomOp`

- Add the
`@CustomOp.register("op_name")`

decorator on this op class to register it intosystem.`CustomOp`

- Implement different
`forward_xxx()`

method according to your needs.

Taking [ MMEncoderAttention](https://docs.vllm.ai/api/vllm/model_executor/layers/attention/mm_encoder_attention/#vllm.model_executor.layers.attention.mm_encoder_attention.MMEncoderAttention) as an example:

## Code

@CustomOp.register("mm_encoder_attn")
class MMEncoderAttention(CustomOp):
def __init__(
self,
num_heads: int,
head_size: int,
scale: float | None = None,
num_kv_heads: int | None = None,
prefix: str = "",
multimodal_config: MultiModalConfig | None = None,
) -> None:
super().__init__()
# Init...
def forward_native(
self,
query: torch.Tensor,
key: torch.Tensor,
value: torch.Tensor,
cu_seqlens: torch.Tensor | None = None,
max_seqlen: torch.Tensor | None = None, # Only used for Flash Attention
) -> torch.Tensor:
# Call TORCH_SDPA implementation...
def forward_cuda(
self,
query: torch.Tensor,
key: torch.Tensor,
value: torch.Tensor,
cu_seqlens: torch.Tensor | None = None,
max_seqlen: torch.Tensor | None = None, # Only used for Flash Attention
) -> torch.Tensor:
# Call FA or TORCH_SDPA implementation...
def forward_cpu(
self,
query: torch.Tensor,
key: torch.Tensor,
value: torch.Tensor,
cu_seqlens: torch.Tensor | None = None,
max_seqlen: torch.Tensor | None = None, # Only used for Flash Attention
) -> torch.Tensor:
# Call TORCH_SDPA implementation...
def forward_xpu(
self,
query: torch.Tensor,
key: torch.Tensor,
value: torch.Tensor,
cu_seqlens: torch.Tensor | None = None,
max_seqlen: torch.Tensor | None = None, # Only used for Flash Attention
) -> torch.Tensor:
# Call FA implementation...
def forward_tpu(
self,
query: torch.Tensor,
key: torch.Tensor,
value: torch.Tensor,
cu_seqlens: torch.Tensor | None = None,
max_seqlen: torch.Tensor | None = None, # Only used for Flash Attention
) -> torch.Tensor:
# Call PALLAS implementation...


### Register a New CustomOp in OOT Device Plugins[¶](https://docs.vllm.ai#register-a-new-customop-in-oot-device-plugins)

Currently, thanks to [vLLM's hardware-plugin mechanism](https://docs.vllm.ai/plugin_system/), there are various OOT device plugins emerging out to enable vLLM seamlessly runs on different hardwares. You can also find more details about this mechanism at [Introducing vLLM Hardware Plugin, Best Practice from Ascend NPU](https://blog.vllm.ai/2025/05/12/hardware-plugin.html).

**Official device plugins:**[vllm-ascend](https://github.com/vllm-project/vllm-ascend)(for Huawei Ascend NPU),[vllm-spyre](https://github.com/vllm-project/vllm-spyre)(for Spyre),[vllm-gaudi](https://github.com/vllm-project/vllm-gaudi)(for Intel Gaudi),[vllm-neuron](https://github.com/vllm-project/vllm-neuron)(for AWS Neuron),[vllm-meta](https://github.com/vllm-project/vllm-metal)(for Apple Silicon), etc.**Non-official device plugins:**[vllm-metax](https://github.com/MetaX-MACA/vLLM-metax)(for MetaX GPU),[vllm-kunlun](https://github.com/baidu/vLLM-Kunlun)(for Baidu Kunlun XPU),[vllm-musa](https://github.com/MooreThreads/vllm-musa)(for Moore Threads GPU), etc.

In this case, [ CustomOp](https://docs.vllm.ai/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp) can enable these hardware manufacturers to seamlessly replace vLLM's operations with their deep-optimized kernels for specific devices at runtime, by just registering an OOT

[and implementing the](https://docs.vllm.ai/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp)

`CustomOp`

`forward_oot()`

method.Now, this part will show you how to register an OOT [ CustomOp](https://docs.vllm.ai/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp) for a device plugin.

Taking [ MMEncoderAttention](https://docs.vllm.ai/api/vllm/model_executor/layers/attention/mm_encoder_attention/#vllm.model_executor.layers.attention.mm_encoder_attention.MMEncoderAttention) as an example:

- Implement a
`CustomMMEncoderAttention`

class which extends fromand implement its`MMEncoderAttention`

`forward_oot()`

method. - Register your
`CustomMMEncoderAttention`

into vLLM to replace.`MMEncoderAttention`


## Code

from vllm.model_executor.layers.attention import MMEncoderAttention
from vllm.model_executor.custom_op import CustomOp
@CustomOp.register_oot("MMEncoderAttention")
class CustomMMEncoderAttention(MMEncoderAttention):
def __init__(...):
super().__init__(...)
def forward_oot(...):
# Call optimized device-specific kernels.
...


In this case, a new item `{"MMEncoderAttention": CustomMMEncoderAttention}`

will be added into `op_registry_oot`

. When initializing a [ MMEncoderAttention](https://docs.vllm.ai/api/vllm/model_executor/layers/attention/mm_encoder_attention/#vllm.model_executor.layers.attention.mm_encoder_attention.MMEncoderAttention) op object, if the class name (i.e.,

[) is contained in the keys of](https://docs.vllm.ai/api/vllm/model_executor/layers/attention/mm_encoder_attention/#vllm.model_executor.layers.attention.mm_encoder_attention.MMEncoderAttention)

`MMEncoderAttention`

`op_registry_oot`

, vLLM will replace it with our registered class (i.e., `CustomMMEncoderAttention`

) and instantiate it.After that, when this [ MMEncoderAttention](https://docs.vllm.ai/api/vllm/model_executor/layers/attention/mm_encoder_attention/#vllm.model_executor.layers.attention.mm_encoder_attention.MMEncoderAttention) op is called, your

`forward_oot()`

will be called if it is enabled. Thus, you will get expected performance on your hardwares without directly modify vLLM.In addition, you can also register all your [ CustomOp](https://docs.vllm.ai/api/vllm/model_executor/custom_op/#vllm.model_executor.custom_op.CustomOp) at one place for better management.