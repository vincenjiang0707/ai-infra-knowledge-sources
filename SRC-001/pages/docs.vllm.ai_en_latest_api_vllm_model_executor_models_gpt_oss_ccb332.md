source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/gpt_oss/
lastmod: 2026-09-23

@support_torch_compile
class GptOssModel(nn.Module, EagleModelMixin):
# Override to swap in an alternative TransformerBlock subclass.
block_cls: type[nn.Module] = TransformerBlock
def __init__(
self,
*,
vllm_config: VllmConfig,
prefix: str = "",
):
super().__init__()
self.config = vllm_config.model_config.hf_config
self.quant_config = vllm_config.quant_config
self.parallel_config = vllm_config.parallel_config
self.embedding = VocabParallelEmbedding(
self.config.vocab_size,
self.config.hidden_size,
)
self.start_layer, self.end_layer, self.layers = make_layers(
self.config.num_hidden_layers,
lambda prefix: self.block_cls(
vllm_config,
prefix=prefix,
quant_config=self.quant_config,
),
prefix=f"{prefix}.layers",
)
self.norm = RMSNorm(self.config.hidden_size, eps=1e-5)
self.make_empty_intermediate_tensors = make_empty_intermediate_tensors_factory(
["hidden_states", "residual"], self.config.hidden_size
)
def embed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
return self.embedding(input_ids)
def forward(
self,
input_ids: torch.Tensor | None,
positions: torch.Tensor,
intermediate_tensors: IntermediateTensors | None = None,
inputs_embeds: torch.Tensor | None = None,
) -> torch.Tensor:
if get_pp_group().is_first_rank:
if inputs_embeds is not None:
x = inputs_embeds
else:
x = self.embed_input_ids(input_ids)
residual = None
else:
assert intermediate_tensors is not None
x = intermediate_tensors["hidden_states"]
residual = intermediate_tensors["residual"]
aux_hidden_states = self._maybe_add_hidden_state(
[], self.start_layer, x, residual
)
for i in range(self.start_layer, self.end_layer):
layer = self.layers[i]
x, residual = layer(x, positions, residual)
self._maybe_add_hidden_state(aux_hidden_states, i + 1, x, residual)
if not get_pp_group().is_last_rank:
return IntermediateTensors({"hidden_states": x, "residual": residual})
x, _ = self.norm(x, residual)
if len(aux_hidden_states) > 0:
return x, aux_hidden_states
return x
def get_expert_mapping(self) -> list[tuple[str, str, int, str]]:
# Params for weights, weight scales, activation scales
# (param_name, weight_name, expert_id, shard_id)
# NOTE: this is only used for quark.
return fused_moe_make_expert_params_mapping(
self,
ckpt_gate_proj_name="w1",
ckpt_down_proj_name="w2",
ckpt_up_proj_name="w3",
num_experts=self.config.num_local_experts,
num_redundant_experts=0,
)
def _load_weights_mxfp4(
self,
ep_rank_end: int,
ep_rank_start: int,
heads_per_rank: int,
head_start: int,
weights: Iterable[tuple[str, torch.Tensor]],
stacked_params_mapping: list[tuple[str, str, str]],
) -> set[str]:
params_dict = dict(self.named_parameters())
loaded_params: set[str] = set()
use_ep = self.parallel_config.enable_expert_parallel
num_experts = self.config.num_local_experts
# In MoE, we need to flatten the tensor parallel size across the data
# parallel size when EP is disabled.
tp_size, tp_rank = FusedMoEParallelConfig.flatten_tp_across_dp_and_pcp(
tp_size=get_tensor_model_parallel_world_size(),
dp_size=get_dp_group().world_size,
dp_rank=get_dp_group().rank_in_group,
pcp_size=get_pcp_group().world_size,
pcp_rank=get_pcp_group().rank_in_group,
)
intermediate_size = self.config.intermediate_size
intermediate_size_block = intermediate_size // OCP_MX_BLOCK_SIZE
per_rank_intermediate_size_block = cdiv(intermediate_size_block, tp_size)
per_rank_intermediate_size = (
per_rank_intermediate_size_block * OCP_MX_BLOCK_SIZE
)
# Calculate common slicing bounds for current rank
tp_rank_start = tp_rank * per_rank_intermediate_size
tp_rank_end = min((tp_rank + 1) * per_rank_intermediate_size, intermediate_size)
# Use centralized weight remapping for MoE expert parameters
for name, weight in remap_moe_expert_weights(weights, params_dict):
# Skip layers on other devices.
if is_pp_missing_parameter(name, self):
continue
if self._try_load_streamed_expert(name, weight, params_dict, loaded_params):
continue
if ".w13_weight_scale" in name:
# Handle MLP gate and up projection weights scale
if use_ep:
narrow_weight = weight[ep_rank_start:ep_rank_end, ...]
else:
narrow_weight = weight[:, 2 * tp_rank_start : 2 * tp_rank_end, ...]
param = params_dict[name]
weight_loader = _get_weight_loader(param)
weight_loader(
param,
narrow_weight,
weight_name=name,
shard_id=None,
expert_id=None,
)
loaded_params.add(name)
continue
elif ".w2_weight_scale" in name:
# Handle MLP down projection weights
if use_ep:
narrow_weight = weight[ep_rank_start:ep_rank_end, ...]
else:
narrow_weight = weight[
...,
tp_rank_start // OCP_MX_BLOCK_SIZE : tp_rank_end
// OCP_MX_BLOCK_SIZE,
]
param = params_dict[name]
weight_loader = _get_weight_loader(param)
weight_loader(
param,
narrow_weight,
weight_name=name,
shard_id=None,
expert_id=None,
)
loaded_params.add(name)
continue
elif ".w13_weight" in name:
# Handle MLP gate and up projection weights
# flat weight from (E, 2 * N, block_size, entry_per_block)
# to (E, 2 * N, -1), shouldn't trigger copy for contiguous
weight = weight.view(
num_experts, 2 * intermediate_size, -1
).contiguous()
# Extract gate and up projection parts
# since the weight is shuffled, we can slice directly
if use_ep:
narrow_weight = weight[ep_rank_start:ep_rank_end, ...]
else:
narrow_weight = weight[:, 2 * tp_rank_start : 2 * tp_rank_end, ...]
param = params_dict[name]
weight_loader = _get_weight_loader(param)
weight_loader(
param,
narrow_weight,
weight_name=name,
shard_id=None,
expert_id=None,
)
loaded_params.add(name)
continue
elif ".w2_weight" in name:
# Handle MLP down projection weights
# same flatten here, but since 2 mx4 value are packed in 1
# uint8, divide by 2
weight = weight.view(
num_experts, -1, intermediate_size // 2
).contiguous()
if use_ep:
narrow_weight = weight[ep_rank_start:ep_rank_end, ...]
else:
narrow_weight = weight[..., tp_rank_start // 2 : tp_rank_end // 2]
param = params_dict[name]
weight_loader = _get_weight_loader(param)
weight_loader(
param,
narrow_weight,
weight_name=name,
shard_id=None,
expert_id=None,
)
loaded_params.add(name)
continue
elif ".w13_bias" in name:
# Handle MLP gate and up projection biases
# Extract gate and up projection bias parts
if use_ep:
narrow_weight = weight[ep_rank_start:ep_rank_end, ...]
else:
narrow_weight = weight[:, 2 * tp_rank_start : 2 * tp_rank_end]
param = params_dict[name]
weight_loader = _get_weight_loader(param)
weight_loader(
param,
narrow_weight,
weight_name=name,
shard_id=None,
expert_id=None,
)
loaded_params.add(name)
continue
elif ".w2_bias" in name:
# Handle MLP down projection bias
param = params_dict[name]
weight_loader = _get_weight_loader(param)
if use_ep:
weight = weight[ep_rank_start:ep_rank_end, ...]
else:
# (only load on rank 0 to avoid duplication)
if tp_rank != 0:
weight.zero_()
weight_loader(
param, weight, weight_name=name, shard_id=None, expert_id=None
)
loaded_params.add(name)
continue
elif "sinks" in name:
# Handle attention sinks (distributed across ranks)
param = params_dict[name]
narrow_weight = weight.narrow(0, head_start, heads_per_rank)
param.data.copy_(narrow_weight)
loaded_params.add(name)
continue
for param_name, weight_name, shard_id in stacked_params_mapping:
if weight_name not in name:
continue
name = name.replace(weight_name, param_name)
param = params_dict[name]
weight_loader = _get_weight_loader(param)
if weight_loader == default_weight_loader:
weight_loader(param, weight)
else:
weight_loader(param, weight, shard_id)
break
else:
# Handle all other weights with potential renaming
if name not in params_dict:
continue
param = params_dict[name]
weight_loader = _get_weight_loader(param)
weight_loader(param, weight)
loaded_params.add(name)
return loaded_params
def _load_weights_quark(
self,
ep_rank_end: int,
ep_rank_start: int,
heads_per_rank: int,
head_start: int,
weights: Iterable[tuple[str, torch.Tensor]],
stacked_params_mapping: list[tuple[str, str, str]],
) -> set[str]:
params_dict = dict(self.named_parameters())
loaded_params: set[str] = set()
use_ep = self.parallel_config.enable_expert_parallel
num_experts = self.config.num_local_experts
if use_ep:
tp_rank = get_tensor_model_parallel_rank()
tp_size = get_tensor_model_parallel_world_size()
else:
tp_size, tp_rank = FusedMoEParallelConfig.flatten_tp_across_dp_and_pcp(
tp_size=get_tensor_model_parallel_world_size(),
dp_size=get_dp_group().world_size,
dp_rank=get_dp_group().rank_in_group,
pcp_size=get_pcp_group().world_size,
pcp_rank=get_pcp_group().rank_in_group,
)
def _is_mxfp4(weight_dtype: str | None) -> bool:
"""Return True for any MXFP4 weight-dtype variant.
Covers "gpt_oss_mxfp4" (GptOssMxfp4MoEMethod) and "mxfp4"
(QuarkMoEMethod with fp4 weights) and any future variants.
"""
return weight_dtype is not None and "mxfp4" in weight_dtype
def _get_moe_weight_dtype(layer_id: int = 0) -> str | None:
"""Helper function to get MoE quantization weight dtype.
Args:
layer_id: Layer index to check (default 0, as all layers should
have the same quantization method)
Returns:
Weight dtype string (e.g., "mxfp4", "fp8") or None if not available
"""
if hasattr(self.layers[layer_id].mlp.experts._quant_method, "weight_dtype"):
return self.layers[layer_id].mlp.experts._quant_method.weight_dtype
return None
intermediate_size = self.config.intermediate_size
moe_weight_dtype = _get_moe_weight_dtype(layer_id=0)
if _is_mxfp4(moe_weight_dtype):
# MXFP4 requires OCP_MX_BLOCK_SIZE alignment
intermediate_size_block = intermediate_size // OCP_MX_BLOCK_SIZE
per_rank_intermediate_size_block = cdiv(intermediate_size_block, tp_size)
per_rank_intermediate_size = (
per_rank_intermediate_size_block * OCP_MX_BLOCK_SIZE
)
else:
# FP8 and other formats don't need alignment
per_rank_intermediate_size = cdiv(intermediate_size, tp_size)
tp_rank_start = tp_rank * per_rank_intermediate_size
tp_rank_end = min((tp_rank + 1) * per_rank_intermediate_size, intermediate_size)
expert_params_mapping = self.get_expert_mapping()
# Streamed per-expert reload is intentionally unsupported for Quark.
for name, loaded_weight in weights:
if is_pp_missing_parameter(name, self):
continue
layer_id, expert_id, fused_name = None, None, None
moe_quant_method = None
if "experts" in name:
parts = name.split(".")
ids = [s for s in parts if s.isdigit()]
# for amd-quark format that each expert is separated
# need to extract the parameter name with experts fused.
# example model: amd/gpt-oss-20b-MoE-Quant-W-MXFP4-A-FP8-KV-FP8
if len(ids) == 2:
layer_id, expert_id = int(ids[0]), int(ids[-1])
parts.pop(len(parts) - 1 - parts[::-1].index(str(expert_id)))
fused_name = ".".join(parts)
# for openai mxfp4 format that all experts are combined
# no need to extract the parameter name with experts fused.
# models: openai/gpt-oss-20b, openai/gpt-oss-120b
elif len(ids) == 1:
layer_id, expert_id = int(ids[0]), None
fused_name = name
else:
raise NameError(
f"Layer {name} contains more than 2 numeric indices. This is "
"an unexpected condition. Please open an issue if encountered."
)
# The MoE refactor (#41184) moved expert params under
# `mlp.experts.routed_experts.*`; remap the legacy checkpoint
# name so keys like w2_bias resolve against params_dict.
fused_name = fused_name.replace(
".mlp.experts.", ".mlp.experts.routed_experts."
)
moe_quant_method = _get_moe_weight_dtype(layer_id=layer_id)
if (
all(key in name for key in ["input_scale", "mlp.experts"])
and expert_id is not None
):
assert loaded_weight.numel() == 1
assert fused_name is not None
expert_data = params_dict[fused_name].data[expert_id]
expert_data.copy_(loaded_weight)
loaded_params.add(fused_name)
continue
# Unified handler for mxfp4 weights and scales
elif _is_mxfp4(moe_quant_method) and any(
name.endswith(suffix)
for suffix in [
".w13_weight_scale",
".w2_weight_scale",
".w13_weight",
".w2_weight",
]
):
is_w13 = ".w13_" in name
is_scale = "_scale" in name
# Reshape weight for mxfp4 if needed (not for scales)
if not is_scale and expert_id is None:
if is_w13:
if loaded_weight.dim() < 3:
raise ValueError(
f"Expected w13_weight to have at least 3 "
f"dimensions, got shape "
f"{loaded_weight.shape}"
)
if loaded_weight.shape[0] != num_experts:
raise ValueError(
f"Expected w13_weight first dimension to be "
f"{num_experts}, got "
f"{loaded_weight.shape[0]}"
)
loaded_weight = loaded_weight.view(
num_experts, 2 * intermediate_size, -1
).contiguous()
else:
if loaded_weight.dim() < 3:
raise ValueError(
f"Expected w2_weight to have at least 3 "
f"dimensions, got shape "
f"{loaded_weight.shape}"
)
if loaded_weight.shape[0] != num_experts:
raise ValueError(
f"Expected w2_weight first dimension to be "
f"{num_experts}, got "
f"{loaded_weight.shape[0]}"
)
loaded_weight = loaded_weight.view(
num_experts, -1, intermediate_size // 2
).contiguous()
if use_ep:
sliced_weight = loaded_weight[ep_rank_start:ep_rank_end, ...]
else:
if is_w13:
if expert_id is None:
sliced_weight = loaded_weight[
:, 2 * tp_rank_start : 2 * tp_rank_end, ...
]
else:
sliced_weight = loaded_weight[
2 * tp_rank_start : 2 * tp_rank_end, ...
]
else:
if is_scale:
sliced_weight = loaded_weight[
...,
tp_rank_start // OCP_MX_BLOCK_SIZE : tp_rank_end
// OCP_MX_BLOCK_SIZE,
]
else:
sliced_weight = loaded_weight[
..., tp_rank_start // 2 : tp_rank_end // 2
]
# NOTE(rob): because gpt-oss ckpt has "unique" structure with
# fused gate_up_proj fused on disk, we cannot use the existing
# weight loaders without added complexity, so just do the
# direct load here.
assert fused_name is not None
param = params_dict[fused_name]
expert_data = param.data[expert_id]
dim1 = sliced_weight.shape[0]
dim2 = sliced_weight.shape[1]
expert_data.data[:dim1, :dim2].copy_(sliced_weight)
loaded_params.add(fused_name)
continue
elif name.endswith(".w13_weight") and moe_quant_method == "fp8":
if use_ep:
narrow_weight = loaded_weight[ep_rank_start:ep_rank_end, ...]
else:
if expert_id is None:
narrow_weight = loaded_weight[
:, 2 * tp_rank_start : 2 * tp_rank_end, :
]
else:
narrow_weight = loaded_weight[
2 * tp_rank_start : 2 * tp_rank_end, :
]
assert fused_name is not None
param = params_dict[fused_name]
if expert_id is None:
param.data.copy_(narrow_weight)
else:
param.data[expert_id].copy_(narrow_weight)
loaded_params.add(fused_name)
continue
elif name.endswith(".w13_weight_scale") and moe_quant_method == "fp8":
assert fused_name is not None
param = params_dict[fused_name]
# Check if this is per-channel or per-tensor scale
if loaded_weight.numel() > 1 and loaded_weight.dim() == 1:
if use_ep:
narrow_weight = loaded_weight[ep_rank_start:ep_rank_end, ...]
else:
narrow_weight = loaded_weight[
2 * tp_rank_start : 2 * tp_rank_end
]
else:
narrow_weight = loaded_weight
if expert_id is None:
param.data.copy_(narrow_weight)
else:
param.data[expert_id].copy_(narrow_weight)
loaded_params.add(fused_name)
continue
elif name.endswith(".w13_input_scale") and moe_quant_method == "fp8":
assert fused_name is not None
param = params_dict[fused_name]
if expert_id is None:
param.data.copy_(loaded_weight)
else:
param.data[expert_id].copy_(loaded_weight)
loaded_params.add(fused_name)
continue
elif name.endswith(".w2_weight") and moe_quant_method == "fp8":
if use_ep:
narrow_weight = loaded_weight[ep_rank_start:ep_rank_end, ...]
else:
if expert_id is None:
narrow_weight = loaded_weight[..., tp_rank_start:tp_rank_end]
else:
narrow_weight = loaded_weight[..., tp_rank_start:tp_rank_end]
assert fused_name is not None
param = params_dict[fused_name]
if expert_id is None:
param.data.copy_(narrow_weight)
else:
param.data[expert_id].copy_(narrow_weight)
loaded_params.add(fused_name)
continue
elif name.endswith(".w2_weight_scale") and moe_quant_method == "fp8":
assert fused_name is not None
param = params_dict[fused_name]
if use_ep:
narrow_weight = loaded_weight[ep_rank_start:ep_rank_end, ...]
else:
narrow_weight = loaded_weight
if expert_id is None:
param.data.copy_(narrow_weight)
else:
param.data[expert_id].copy_(narrow_weight)
loaded_params.add(fused_name)
continue
# Unified handler for bias loading (w13_bias and w2_bias)
elif name.endswith(".w13_bias") or name.endswith(".w2_bias"):
is_w13_bias = name.endswith(".w13_bias")
if use_ep:
sliced_weight = loaded_weight[ep_rank_start:ep_rank_end, ...]
else:
if is_w13_bias:
if expert_id is None:
sliced_weight = loaded_weight[
:, 2 * tp_rank_start : 2 * tp_rank_end
]
else:
sliced_weight = loaded_weight[
2 * tp_rank_start : 2 * tp_rank_end
]
else:
sliced_weight = loaded_weight
if tp_rank != 0:
sliced_weight = sliced_weight.zero_()
# NOTE(rob): because gpt-oss ckpt has "unique" structure with
# fused gate_up_proj fused on disk, we cannot use the existing
# weight loaders without added complexity, so just do the
# direct load here.
assert fused_name is not None
param = params_dict[fused_name]
expert_data = param.data[expert_id]
dim1 = sliced_weight.shape[0]
expert_data.data[:dim1].copy_(sliced_weight)
loaded_params.add(fused_name)
continue
elif "sinks" in name:
# Handle attention sinks (distributed across ranks)
param = params_dict[name]
narrow_weight = loaded_weight.narrow(0, head_start, heads_per_rank)
param.data.copy_(narrow_weight)
loaded_params.add(name)
continue
for param_name, weight_name, shard_id in stacked_params_mapping:
# Skip non-stacked layers and experts (experts handled below).
if weight_name not in name:
continue
# We have mlp.experts[0].gate_proj in the checkpoint.
# Since we handle the experts below in expert_params_mapping,
# we need to skip here BEFORE we update the name, otherwise
# name will be updated to mlp.experts[0].gate_up_proj, which
# will then be updated below in expert_params_mapping
# for mlp.experts[0].gate_gate_up_proj, which breaks load.
if ("mlp.experts." in name) and name not in params_dict:
continue
name = name.replace(weight_name, param_name)
if name.endswith("scale"):
# Remapping the name of FP8 kv-scale.
remapped_name = maybe_remap_kv_scale_name(name, params_dict)
if remapped_name is None:
continue
name = remapped_name
param = params_dict[name]
weight_loader = param.weight_loader
weight_loader(param, loaded_weight, shard_id)
loaded_params.add(name)
break
else:
for mapping in expert_params_mapping:
# Anyway, this is an expert weight and should not be
# attempted to load as other weights later
param_name, weight_name, mapping_expert_id, shard_id = mapping
weight_name = (
weight_name[:-1] if weight_name.endswith(".") else weight_name
)
if weight_name not in name:
continue
assert fused_name is not None
param = params_dict[fused_name]
# We should ask the weight loader to return success or not
# here since otherwise we may skip experts with other
# available replicas.
weight_loader = typing.cast(
Callable[..., bool], param.weight_loader
)
# Use checkpoint's expert_id for quark format (when expert_id
# is extracted from weight name), otherwise use mapping's expert_id
actual_expert_id = (
expert_id if expert_id is not None else mapping_expert_id
)
success = weight_loader(
param,
loaded_weight,
fused_name,
shard_id=shard_id,
expert_id=actual_expert_id,
return_success=True,
)
if success:
name = fused_name
loaded_params.add(name)
break
else:
if name not in params_dict:
continue
param = params_dict[name]
weight_loader = _get_weight_loader(param)
weight_loader(param, loaded_weight)
loaded_params.add(name)
return loaded_params
def _load_weights_other(
self,
ep_rank_end: int,
ep_rank_start: int,
heads_per_rank: int,
head_start: int,
weights: Iterable[tuple[str, torch.Tensor]],
stacked_params_mapping: list[tuple[str, str, str]],
) -> set[str]:
params_dict = dict(self.named_parameters())
loaded_params: set[str] = set()
use_ep = self.parallel_config.enable_expert_parallel
# In MoE, we need to flatten the tensor parallel size across the data
# parallel size when EP is disabled.
tp_size, tp_rank = FusedMoEParallelConfig.flatten_tp_across_dp_and_pcp(
tp_size=get_tensor_model_parallel_world_size(),
dp_size=get_dp_group().world_size,
dp_rank=get_dp_group().rank_in_group,
pcp_size=get_pcp_group().world_size,
pcp_rank=get_pcp_group().rank_in_group,
)
intermediate_size = self.config.intermediate_size
per_rank_intermediate_size = cdiv(intermediate_size, tp_size)
# Calculate common slicing bounds for current rank
tp_rank_start = tp_rank * per_rank_intermediate_size
tp_rank_end = min((tp_rank + 1) * per_rank_intermediate_size, intermediate_size)
# Use centralized weight remapping for MoE expert parameters.
# The MoERunner refactor moved expert params under
# `mlp.experts.routed_experts.*`; this remaps checkpoint names so
# MoE weight/bias keys resolve against params_dict.
for name, weight in remap_moe_expert_weights(weights, params_dict):
# Skip layers on other devices.
if is_pp_missing_parameter(name, self):
continue
if self._try_load_streamed_expert(name, weight, params_dict, loaded_params):
continue
if ".w13_weight" in name:
# Handle MLP gate and up projection weights
# Extract gate and up projection parts
if use_ep:
narrow_weight = weight[ep_rank_start:ep_rank_end, ...]
else:
narrow_weight = weight[:, :, 2 * tp_rank_start : 2 * tp_rank_end]
narrow_weight = narrow_weight.permute(0, 2, 1).contiguous()
param = params_dict[name]
param.copy_(narrow_weight)
loaded_params.add(name)
continue
elif ".w2_weight" in name:
# Handle MLP down projection weights
if use_ep:
narrow_weight = weight[ep_rank_start:ep_rank_end, ...]
else:
narrow_weight = weight[:, tp_rank_start:tp_rank_end, :]
narrow_weight = narrow_weight.permute(0, 2, 1).contiguous()
param = params_dict[name]
param.copy_(narrow_weight)
loaded_params.add(name)
continue
elif ".w13_bias" in name:
# Handle MLP gate and up projection biases
# Extract gate and up projection bias parts
if use_ep:
narrow_weight = weight[ep_rank_start:ep_rank_end, ...]
else:
narrow_weight = weight[:, 2 * tp_rank_start : 2 * tp_rank_end]
param = params_dict[name]
param.copy_(narrow_weight)
loaded_params.add(name)
continue
elif ".w2_bias" in name:
# Handle MLP down projection bias
if use_ep:
weight = weight[ep_rank_start:ep_rank_end, ...]
else:
# (only load on rank 0 to avoid duplication)
if tp_rank != 0:
weight.zero_()
param = params_dict[name]
param.copy_(weight)
loaded_params.add(name)
continue
elif "sinks" in name:
# Handle attention sinks (distributed across ranks)
param = params_dict[name]
narrow_weight = weight.narrow(0, head_start, heads_per_rank)
param.data.copy_(narrow_weight)
loaded_params.add(name)
continue
for param_name, weight_name, shard_id in stacked_params_mapping:
if weight_name not in name:
continue
name = name.replace(weight_name, param_name)
param = params_dict[name]
weight_loader = _get_weight_loader(param)
if weight_loader == default_weight_loader:
weight_loader(param, weight)
else:
weight_loader(param, weight, shard_id)
break
else:
# Handle all other weights with potential renaming
if name not in params_dict:
continue
param = params_dict[name]
weight_loader = _get_weight_loader(param)
weight_loader(param, weight)
loaded_params.add(name)
return loaded_params
@staticmethod
def _get_streamed_expert_info(
name: str,
params_dict: dict[str, torch.nn.Parameter],
) -> tuple[int, str, str] | None:
"""Parse ``...experts.<expert_id>.<fused_param>`` checkpoint keys."""
if ".mlp.experts." not in name:
return None
suffix = name.rsplit(".", 1)[-1]
shard_id = _GPT_OSS_STREAMED_EXPERT_SUFFIX_TO_SHARD.get(suffix)
if shard_id is None:
return None
prefix, expert_suffix = name.split(".mlp.experts.", maxsplit=1)
expert_id_str, separator, param_suffix = expert_suffix.partition(".")
if not separator or not expert_id_str.isdigit():
return None
expert_id = int(expert_id_str)
for base_layer_prefix in ("", "base_layer."):
fused_name = (
f"{prefix}.mlp.experts.{base_layer_prefix}routed_experts.{param_suffix}"
)
if fused_name in params_dict:
return expert_id, fused_name, shard_id
return None
@classmethod
def _try_load_streamed_expert(
cls,
name: str,
loaded_weight: torch.Tensor,
params_dict: dict[str, torch.nn.Parameter],
loaded_params: set[str],
) -> bool:
expert_info = cls._get_streamed_expert_info(name, params_dict)
if expert_info is None:
return False
expert_id, fused_name, shard_id = expert_info
param = params_dict[fused_name]
weight_loader = typing.cast(Callable[..., bool], param.weight_loader)
success = weight_loader(
param,
loaded_weight,
weight_name=fused_name,
shard_id=shard_id,
expert_id=expert_id,
return_success=True,
)
if success:
loaded_params.add(fused_name)
return True
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
stacked_params_mapping = [
# (param_name, shard_name, shard_id)
(".qkv_proj", ".q_proj", "q"),
(".qkv_proj", ".k_proj", "k"),
(".qkv_proj", ".v_proj", "v"),
]
tp_rank = get_tensor_model_parallel_rank()
tp_size = get_tensor_model_parallel_world_size()
# Attention heads per rank
heads_per_rank = self.config.num_attention_heads // tp_size
head_start = tp_rank * heads_per_rank
ep_size = get_ep_group().world_size
ep_rank = get_ep_group().rank_in_group
num_experts = self.config.num_local_experts
experts_per_rank = num_experts // ep_size
ep_rank_start = ep_rank * experts_per_rank
ep_rank_end = (ep_rank + 1) * experts_per_rank
quant_method = (
self.config.quantization_config["quant_method"]
if hasattr(self.config, "quantization_config")
else None
)
# Normalize the checkpoint's quant_method to the internal name.
# Note: there are three places where "mxfp4" -> "gpt_oss_mxfp4"
# normalization occurs, each serving a different data path:
# 1. GptOssMxfp4Config.override_quantization_method() — sets
# ModelConfig.quantization (used to select the QuantizationConfig
# class at model init time), reading from model_arch_config which
# is a snapshot taken before verify_and_update_model_config runs.
# 2. GptOssForCausalLMConfig.verify_and_update_model_config() —
# patches hf_config.quantization_config in-place (a separate copy
# of the dict from model_arch_config) for later hf_config lookups.
# 3. Here — reads directly from self.config (the raw HF config) which
# may still carry the original "mxfp4" string from the checkpoint.
if quant_method == "mxfp4":
quant_method = "gpt_oss_mxfp4"
if quant_method == "gpt_oss_mxfp4":
return self._load_weights_mxfp4(
ep_rank_end,
ep_rank_start,
heads_per_rank,
head_start,
weights,
stacked_params_mapping,
)
elif quant_method == "quark":
return self._load_weights_quark(
ep_rank_end,
ep_rank_start,
heads_per_rank,
head_start,
weights,
stacked_params_mapping,
)
else:
return self._load_weights_other(
ep_rank_end,
ep_rank_start,
heads_per_rank,
head_start,
weights,
stacked_params_mapping,
)