source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/nvidia/model/
lastmod: 2026-09-23

class KimiLinearModel(nn.Module, EagleModelMixin, SupportsQuant):
packed_modules_mapping = {
"gate_up_proj": ["gate_proj", "up_proj"],
"in_proj_qkvgfab": ["q_proj", "k_proj", "v_proj", "b_proj", "f_a_proj"],
"conv1d": ["q_conv1d", "k_conv1d", "v_conv1d"],
"fused_qkv_a_proj": ["q_a_proj", "kv_a_proj_with_mqa"],
"fused_qkv_a_g_proj": ["q_a_proj", "kv_a_proj_with_mqa", "g_proj"],
}
supports_aux_hidden_states_over_pp = True
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
config = vllm_config.model_config.hf_text_config
self.config = config
self.attn_res_block_size: int | None = config.attn_res_block_size
self.use_attn_res = self.attn_res_block_size is not None
parallel_config = vllm_config.parallel_config
use_mega_moe = vllm_config.kernel_config.moe_backend == "deep_gemm_mega_moe"
self.use_sequence_parallel = (
parallel_config.pipeline_parallel_size == 1
and parallel_config.enable_expert_parallel
and parallel_config.tensor_parallel_size > 1
and (use_mega_moe or parallel_config.data_parallel_size > 1)
)
self.vocab_size = config.vocab_size
# GEMM-RS/AR uses NCCL symmetric-memory multicast, which requires all
# TP ranks to belong to one NVLink domain.
self.run_gemm_rs_ar = maybe_init_gemm_rs_ar(
vllm_config, self.use_sequence_parallel
)
if get_pp_group().is_first_rank or spec_decode_needs_target_embed(vllm_config):
self.embed_tokens = VocabParallelEmbedding(
config.vocab_size,
config.hidden_size,
prefix=f"{prefix}.embed_tokens",
)
else:
self.embed_tokens = PPMissingLayer()
# Aux stream for overlapping the MLA g_proj output-gate GEMM with the
# attention front-end (DeepseekV4 convention: created at the model
# level and threaded into each attention layer).
aux_stream = torch.cuda.Stream()
def get_layer(prefix: str):
return KimiDecoderLayer(
config,
vllm_config,
prefix,
aux_stream=aux_stream,
run_gemm_rs_ar=self.run_gemm_rs_ar,
)
self.start_layer, self.end_layer, self.layers = make_layers(
config.num_hidden_layers,
get_layer,
prefix=f"{prefix}.layers",
)
self.num_attn_res_blocks = (
cdiv(self.end_layer, self.attn_res_block_size)
if self.attn_res_block_size is not None
else 0
)
if get_pp_group().is_last_rank:
self.norm = RMSNorm(config.hidden_size, eps=config.rms_norm_eps)
if self.use_attn_res:
self.output_attn_res_norm = RMSNorm(
config.hidden_size, eps=config.rms_norm_eps
)
self.output_attn_res_proj = ReplicatedLinear(
config.hidden_size,
1,
bias=False,
quant_config=None,
prefix=f"{prefix}.output_attn_res_proj",
)
else:
self.norm = PPMissingLayer()
if self.use_attn_res:
self.output_attn_res_norm = PPMissingLayer()
self.output_attn_res_proj = PPMissingLayer()
world_size = get_tensor_model_parallel_world_size()
assert config.num_attention_heads % world_size == 0, (
"num_attention_heads must be divisible by world_size"
)
def make_empty_intermediate_tensors(
self,
batch_size: int,
dtype: torch.dtype,
device: torch.device,
) -> IntermediateTensors:
residual_shape: tuple[int, ...] = (batch_size, self.config.hidden_size)
if self.use_attn_res:
assert self.attn_res_block_size is not None
residual_shape = (
batch_size,
cdiv(self.start_layer, self.attn_res_block_size),
self.config.hidden_size,
)
return IntermediateTensors(
{
"hidden_states": torch.zeros(
(batch_size, self.config.hidden_size), dtype=dtype, device=device
),
"residual": torch.zeros(residual_shape, dtype=dtype, device=device),
}
)
def _set_aux_hidden_state_layers(self, layers: tuple[int, ...]) -> None:
super()._set_aux_hidden_state_layers(layers)
if self.use_attn_res and self._aux_attn_res_stream:
pp = get_pp_group()
if not pp.is_last_rank and self.end_layer in self.aux_hidden_state_layers:
raise ValueError(
f"Auxiliary layer {self.end_layer} cannot end a non-final PP "
"stage when VLLM_KIMI_K3_AUX_ATTN_RES_STREAM=1"
)
if self.use_attn_res:
logger.info_once(
"Kimi-K3 aux hidden capture: layers=%s mode=%s "
"(VLLM_KIMI_K3_AUX_ATTN_RES_STREAM=%d)",
self.aux_hidden_state_layers,
"attn_res_stream" if self._aux_attn_res_stream else "prefix_only",
int(self._aux_attn_res_stream),
)
@property
def _aux_attn_res_stream(self) -> bool:
return envs.VLLM_KIMI_K3_AUX_ATTN_RES_STREAM
def _capture_aux_hidden_stream(
self,
layer_idx: int,
prefix_sum: torch.Tensor,
pending_mlp_out: torch.Tensor | None,
block_residual: torch.Tensor,
) -> torch.Tensor:
"""Return the AttnRes stream after ``layer_idx``."""
prefix = prefix_sum if pending_mlp_out is None else prefix_sum + pending_mlp_out
if not (self._aux_attn_res_stream and self.use_attn_res):
return prefix
if layer_idx + 1 < self.end_layer:
consumer = self.layers[layer_idx + 1]
score_norm = consumer.self_attention_res_norm
score_proj = consumer.self_attention_res_proj
num_blocks = consumer.prev_valid_blocks
elif get_pp_group().is_last_rank:
score_norm = self.output_attn_res_norm
score_proj = self.output_attn_res_proj
num_blocks = self.num_attn_res_blocks
else:
raise RuntimeError("Auxiliary AttnRes capture crossed a PP boundary")
return attn_res(
prefix,
None,
block_residual,
score_norm.weight,
score_proj.weight.squeeze(0),
None,
num_blocks=num_blocks,
block_write_idx=-1,
eps=score_norm.variance_epsilon,
output_norm_eps=0.0,
)
def embed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
return self.embed_tokens(input_ids)
def forward(
self,
input_ids: torch.Tensor | None,
positions: torch.Tensor,
intermediate_tensors: IntermediateTensors | None,
inputs_embeds: torch.Tensor | None = None,
**kwargs,
) -> torch.Tensor | IntermediateTensors | tuple[torch.Tensor, list[torch.Tensor]]:
if get_pp_group().is_first_rank:
if inputs_embeds is not None:
hidden_states = inputs_embeds
else:
hidden_states = self.embed_input_ids(input_ids)
residual = None
else:
assert intermediate_tensors is not None
hidden_states = intermediate_tensors["hidden_states"]
residual = intermediate_tensors["residual"]
assert hidden_states is not None
full_num_tokens = positions.shape[0]
if self.use_sequence_parallel:
if envs.VLLM_MOE_SKIP_PADDING and is_forward_context_available():
forward_context = get_forward_context()
forward_context.is_padding = sp_padding_mask(
forward_context.is_padding, hidden_states
)
hidden_states = sp_shard(hidden_states)
assert residual is None, "Currently, SP is not supported with PP"
remote_aux = self.collect_remote_aux_hidden_states(intermediate_tensors)
# sharded aux hidden states when sp is enabled
aux_hidden_states: list[torch.Tensor] = []
if (
get_pp_group().is_first_rank
and self.start_layer in self.aux_hidden_state_layers
):
if self.use_attn_res or residual is None:
aux_hidden_states.append(hidden_states)
else:
aux_hidden_states.append(hidden_states + residual)
prefix_sum = None
if self.use_attn_res:
block_residual = hidden_states.new_empty(
hidden_states.size(0),
self.num_attn_res_blocks,
hidden_states.size(1),
)
if residual is not None:
block_residual[:, : residual.size(1), :].copy_(residual)
prefix_sum = hidden_states
hidden_states = None
residual = block_residual
for layer_idx, layer in enumerate(
self.layers[self.start_layer : self.end_layer],
start=self.start_layer,
):
hidden_states, prefix_sum, residual = layer(
positions=positions,
hidden_states=hidden_states,
prefix_sum=prefix_sum,
residual=residual,
)
if (layer_idx + 1) in self.aux_hidden_state_layers:
if self.use_attn_res:
assert prefix_sum is not None
assert residual is not None
aux_hidden_state = self._capture_aux_hidden_stream(
layer_idx, prefix_sum, hidden_states, residual
)
else:
assert residual is not None
aux_hidden_state = hidden_states + residual
aux_hidden_states.append(aux_hidden_state)
assert hidden_states is not None
assert residual is not None
if not get_pp_group().is_last_rank:
assert not self.use_sequence_parallel, (
"Currently, SP is not supported with PP"
)
if prefix_sum is not None:
hidden_states = hidden_states + prefix_sum
return IntermediateTensors(
{
"hidden_states": hidden_states,
"residual": residual,
**self.pack_local_aux_hidden_states(aux_hidden_states),
}
)
if self.use_attn_res:
assert prefix_sum is not None
hidden_states = attn_res(
prefix_sum,
hidden_states,
residual,
self.output_attn_res_norm.weight,
self.output_attn_res_proj.weight.squeeze(0),
None,
num_blocks=self.num_attn_res_blocks,
block_write_idx=-1,
eps=self.output_attn_res_norm.variance_epsilon,
output_norm_eps=0.0,
)
else:
hidden_states = hidden_states + residual
if self.use_sequence_parallel:
if aux_hidden_states:
hidden_size = hidden_states.shape[-1]
packed_hidden_states = torch.cat(
[hidden_states, *aux_hidden_states], dim=-1
)
packed_hidden_states = sp_all_gather(packed_hidden_states)
packed_hidden_states = packed_hidden_states[:full_num_tokens]
hidden_states, *aux_hidden_states = packed_hidden_states.split(
hidden_size, dim=-1
)
else:
hidden_states = sp_all_gather(hidden_states)
hidden_states = hidden_states[:full_num_tokens]
# NOTE: the final norm is applied in compute_logits instead of here, so
# the MTP draft model receives the pre-norm hidden states.
aux_hidden_states = remote_aux + aux_hidden_states
if aux_hidden_states:
return hidden_states, aux_hidden_states
return hidden_states
def load_weights(
self,
weights: Iterable[
tuple[str, torch.Tensor] | tuple[str, torch.Tensor, dict[str, Any]]
],
) -> set[str]:
kda_config = self.config.linear_attn_config
use_full_rank_gate = bool(
kda_config and kda_config.get("use_full_rank_gate", False)
)
beta_shard_id = 5 if use_full_rank_gate else 3
stacked_params_mapping = [
# (param_name, shard_name, shard_id)
(".in_proj_qkvgfab", ".q_proj", 0),
(".in_proj_qkvgfab", ".k_proj", 1),
(".in_proj_qkvgfab", ".v_proj", 2),
(".in_proj_qkvgfab", ".b_proj", beta_shard_id),
(".in_proj_qkvgfab", ".f_a_proj", 4),
(".conv1d", ".q_conv1d", 0),
(".conv1d", ".k_conv1d", 1),
(".conv1d", ".v_conv1d", 2),
(".gate_up_proj", ".gate_proj", 0),
(".gate_up_proj", ".up_proj", 1),
]
if use_full_rank_gate:
stacked_params_mapping.append((".in_proj_qkvgfab", ".g_proj", 3))
if getattr(self.config, "q_lora_rank", None) is not None:
if self.config.mla_use_output_gate:
stacked_params_mapping += [
(".fused_qkv_a_g_proj", ".q_a_proj", 0),
(".fused_qkv_a_g_proj", ".kv_a_proj_with_mqa", 1),
(".fused_qkv_a_g_proj", ".g_proj", 2),
]
else:
stacked_params_mapping += [
(".fused_qkv_a_proj", ".q_a_proj", 0),
(".fused_qkv_a_proj", ".kv_a_proj_with_mqa", 1),
]
use_mega_moe = any(
module.use_mega_moe
for module in self.modules()
if isinstance(module, KimiMoE)
)
if self.config.is_moe and use_mega_moe:
expert_params_mapping = make_kimi_k3_mega_moe_expert_params_mapping(
self.config.num_experts
)
elif self.config.is_moe:
# Params for weights, fp8 weight scales, fp8 activation scales
# (param_name, weight_name, expert_id, shard_id)
expert_params_mapping = fused_moe_make_expert_params_mapping(
self,
ckpt_gate_proj_name="w1",
ckpt_down_proj_name="w2",
ckpt_up_proj_name="w3",
num_experts=self.config.num_experts,
)
else:
expert_params_mapping = []
params_dict = dict(self.named_parameters())
# Under the MXFP4 quant interface the routed experts register unpacked
# params (``w13_weight``), while the compressed-tensors checkpoint names
# them ``.weight_packed``. Rebind so the expert mapping resolves; scales
# already share the ``.weight_scale`` suffix.
experts_unpacked = not use_mega_moe and not any(
n.endswith("w13_weight_packed") for n in params_dict
)
loaded_params: set[str] = set()
for args in weights:
name, loaded_weight = args[0], args[1]
kwargs: dict[str, Any] = args[2] if len(args) > 2 else {}
if "rotary_emb.inv_freq" in name:
continue
if experts_unpacked and name.endswith(".weight_packed"):
name = name.replace(".weight_packed", ".weight")
spec_layer = get_spec_layer_idx_from_weight_name(self.config, name)
if spec_layer is not None:
continue # skip spec decode layers for main model
if "rotary_emb.cos_cached" in name or "rotary_emb.sin_cached" in name:
# Models trained using ColossalAI may include these tensors in
# the checkpoint. Skip them.
continue
for param_name, weight_name, shard_id in stacked_params_mapping:
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
name_mapped = name.replace(weight_name, param_name)
# Packed projections are only present on compatible layers.
if name_mapped not in params_dict:
continue
name = name_mapped
# Skip loading extra bias for GPTQ models.
if name.endswith(".bias") and name not in params_dict:
continue
if is_pp_missing_parameter(name, self):
continue
param = params_dict[name]
weight_loader = param.weight_loader
weight_loader(param, loaded_weight, shard_id)
break
else:
for (
expert_param_name,
expert_weight_name,
expert_id,
expert_shard_id,
) in expert_params_mapping:
if expert_weight_name not in name:
continue
name = name.replace(expert_weight_name, expert_param_name)
if is_pp_missing_parameter(name, self):
continue
param = params_dict[name]
weight_loader = param.weight_loader
weight_loader(
param,
loaded_weight,
name,
expert_id=expert_id,
shard_id=expert_shard_id,
)
break
else:
# Skip loading extra bias for GPTQ models.
if (
name.endswith(".bias")
and name not in params_dict
and not self.config.is_linear_attn
): # noqa: E501
continue
# Remapping the name of FP8 kv-scale.
remapped_name = maybe_remap_kv_scale_name(name, params_dict)
if remapped_name is None:
continue
name = remapped_name
if is_pp_missing_parameter(name, self):
continue
param = params_dict[name]
weight_loader = getattr(
param, "weight_loader", default_weight_loader
)
weight_loader(param, loaded_weight, **kwargs)
loaded_params.add(name)
return loaded_params
def finalize_mega_moe_weights(self) -> None:
for module in self.modules():
if isinstance(module, KimiMoE) and module.use_mega_moe:
module.experts.finalize_weights()