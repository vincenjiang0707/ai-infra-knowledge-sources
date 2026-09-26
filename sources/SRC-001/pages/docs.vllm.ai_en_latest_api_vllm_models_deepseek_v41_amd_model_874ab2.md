source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v41/amd/model/
lastmod: 2026-09-24

class DeepseekV4Model(nn.Module, EagleModelMixin):
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
config = vllm_config.model_config.hf_config
quant_config = vllm_config.quant_config
self.config = config
self.quant_config = quant_config
self.parallel_config = vllm_config.parallel_config
self.use_mega_moe = False
self.use_sequence_parallel = _use_sequence_parallel(vllm_config)
if self.use_mega_moe and not vllm_config.parallel_config.enable_expert_parallel:
raise NotImplementedError(
"DeepSeek V4 MegaMoE currently requires expert parallel. "
"Enable it with --enable-expert-parallel, or pick a different "
"moe backend."
)
self.vocab_size = config.vocab_size
self.hc_eps = config.hc_eps
self.hc_mult = config.hc_mult
self.hc_dim = self.hc_mult * config.hidden_size
self.rms_norm_eps = config.rms_norm_eps
# Three aux streams: one per non-default input GEMM in
# DeepseekV4Attention._run_parallel_input_projections
# (compressor kv_score, indexer.weights_proj). fused_wqa_wkv stays on
# the default stream.
aux_stream_list = [torch.cuda.Stream() for _ in range(3)]
# Reserved topk indices buffer for all Indexer layers to reuse.
self.topk_indices_buffer = torch.empty(
vllm_config.scheduler_config.max_num_batched_tokens,
config.index_topk,
dtype=torch.int32,
)
# Two-level candidate filtering: the indexer at
# candidate_source_layer_id publishes the top candidate blocks of
# compressed positions here; later ratio-1 indexers (24/28/32/36)
# mask their scores with it.
candidate_source_layer = getattr(config, "candidate_source_layer_id", -1)
candidate_topk_blocks = getattr(config, "candidate_topk_blocks", 0)
if candidate_source_layer >= 0 and candidate_topk_blocks > 0:
self.candidate_block_buffer = torch.empty(
vllm_config.scheduler_config.max_num_batched_tokens,
candidate_topk_blocks,
dtype=torch.int32,
)
else:
self.candidate_block_buffer = None
if get_pp_group().is_first_rank:
self.embed_tokens = VocabParallelEmbedding(
config.vocab_size,
config.hidden_size,
quant_config=quant_config,
prefix=f"{prefix}.embed_tokens",
)
else:
self.embed_tokens = PPMissingLayer()
self.engram_layout = EngramLayout.from_config(config)
self.start_layer, self.end_layer, self.layers = make_layers(
config.num_hidden_layers,
lambda prefix: DeepseekV4DecoderLayer(
vllm_config,
prefix=prefix,
topk_indices_buffer=self.topk_indices_buffer,
aux_stream_list=aux_stream_list,
candidate_block_buffer=self.candidate_block_buffer,
engram_layout=self.engram_layout,
),
prefix=f"{prefix}.layers",
)
# The n-gram hash needs a slot-keyed rolling store of compressed ids
# (chunked prefill / decode lookback); key it off the first local
# layer's sliding-window KV cache. Only PP ranks owning an engram
# layer need it.
self.engram_hash: NgramHashState | None = None
self.engram_swa_prefix: str | None = None
if self.engram_layout is not None:
local_engram = any(
isinstance(layer, DeepseekV4DecoderLayer) and layer.engram is not None
for layer in islice(self.layers, self.start_layer, self.end_layer)
)
if local_engram:
first_layer = next(
iter(islice(self.layers, self.start_layer, self.end_layer))
)
swa_cache_module = first_layer.attn.swa_cache_layer
self.engram_hash = NgramHashState(
vllm_config, self.engram_layout, swa_cache_module
)
self.engram_swa_prefix = swa_cache_module.prefix
if get_pp_group().is_last_rank:
self.norm = RMSNorm(config.hidden_size, self.rms_norm_eps)
else:
self.norm = PPMissingLayer()
self.mhc_post = MHCPostOp()
spec_config = vllm_config.speculative_config
needs_mtp_hidden_states = spec_config is not None and (
spec_config.use_eagle() or spec_config.uses_draft_model()
)
if get_pp_group().is_last_rank and needs_mtp_hidden_states:
self._mtp_hidden_buffer = torch.empty(
vllm_config.scheduler_config.max_num_batched_tokens,
self.hc_dim,
dtype=vllm_config.model_config.dtype,
)
else:
self._mtp_hidden_buffer = None
def embed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
return self.embed_tokens(input_ids)
def make_empty_intermediate_tensors(
self,
batch_size: int,
dtype: torch.dtype,
device: torch.device,
) -> IntermediateTensors:
# PP intermediate tensors carry the multi-stream hidden_states
# of shape (num_tokens, hc_mult, hidden_size) — V4 expands the
# token embedding to hc_mult streams before the first decoder
# layer and keeps that shape until the final hc collapse — plus the
# (num_tokens, hc_mult) pre-mix the next rank's first layer needs
# for its attention collapse.
return IntermediateTensors(
{
"hidden_states": torch.zeros(
(batch_size, self.hc_mult, self.config.hidden_size),
dtype=dtype,
device=device,
),
"pre_mix": torch.zeros(
(batch_size, self.hc_mult),
dtype=torch.float32,
device=device,
),
}
)
def forward(
self,
input_ids: torch.Tensor,
positions: torch.Tensor,
intermediate_tensors: IntermediateTensors | None,
inputs_embeds: torch.Tensor | None = None,
lookback_token_ids: torch.Tensor | None = None,
) -> torch.Tensor | IntermediateTensors:
if get_pp_group().is_first_rank:
if inputs_embeds is not None:
hidden_states = inputs_embeds
else:
hidden_states = self.embed_input_ids(input_ids)
else:
assert intermediate_tensors is not None
hidden_states = intermediate_tensors["hidden_states"]
if self.use_mega_moe:
input_ids = input_ids.to(torch.int64)
# Engram n-gram hashes for the whole (flattened) batch, computed once
# on the full token stream — before any sequence-parallel sharding —
# and consumed by the engram layers (1 and 14) below. Skipped on
# profile runs (KV cache unbound -> no slot space to key the rolling
# compressed-id cache into).
engram_hashes: torch.Tensor | None = None
engram_mask: torch.Tensor | None = None
if (
self.engram_hash is not None
and input_ids is not None
and is_forward_context_available()
):
attn_metadata = get_forward_context().attn_metadata
if isinstance(attn_metadata, list):
attn_metadata = attn_metadata[dbo_current_ubatch_id()]
if isinstance(attn_metadata, dict) and self.engram_hash.ensure_cache():
assert self.engram_swa_prefix is not None
swa_metadata = typing.cast(
"DeepseekSparseSWAMetadata", attn_metadata[self.engram_swa_prefix]
)
# Image-span tokens are dead: they break n-grams (hash op
# takes True=dead) and their gate is zeroed (Engram.forward
# takes True=keep).
image_mask = image_sentinel_mask(input_ids)
engram_mask = ~image_mask
if lookback_token_ids is None:
if not self.engram_hash.use_slot_cache:
raise NotImplementedError(
"engram needs `lookback_token_ids` from the model "
"runner (the DBO/ubatch wrapper drops model kwargs)"
)
num_reqs = swa_metadata.num_decodes + swa_metadata.num_prefills
lookback_token_ids = input_ids.new_full(
(num_reqs, self.engram_hash.lookback_depth), -1
)
engram_hashes = self.engram_hash(
input_ids,
positions,
swa_metadata.query_start_loc,
image_mask,
lookback_token_ids,
image_sentinel_mask(lookback_token_ids),
swa_metadata.slot_mapping,
swa_metadata.block_table,
)
# Gather all Engram rows before entering the decoder layers.
for layer in islice(self.layers, self.start_layer, self.end_layer):
engram = getattr(layer, "engram", None)
if engram is not None:
engram.prepare_embeddings(
engram_hashes[:, engram.layer_hash_index]
)
full_num_tokens = positions.shape[0]
if self.use_sequence_parallel:
if envs.VLLM_MOE_SKIP_PADDING and is_forward_context_available():
forward_context = get_forward_context()
forward_context.is_padding = sp_padding_mask(
forward_context.is_padding, hidden_states
)
hidden_states = sp_shard(hidden_states)
input_ids = sp_shard(input_ids)
residual, post_mix, res_mix = None, None, None
pre_mix: torch.Tensor | None = None
if not get_pp_group().is_first_rank:
assert intermediate_tensors is not None
pre_mix = intermediate_tensors["pre_mix"]
aux_hidden_states: list[torch.Tensor] = []
final_aux_recon: torch.Tensor | None = None # avoid duplicate mhc_post call
for idx, layer in enumerate(
islice(self.layers, self.start_layer, self.end_layer),
start=self.start_layer,
):
hidden_states, residual, post_mix, res_mix, pre_mix = layer(
hidden_states,
positions,
input_ids,
pre_mix,
post_mix,
res_mix,
residual,
engram_hashes,
engram_mask,
)
if idx + 1 in self.aux_hidden_state_layers:
# Reconstruct the aux hidden state for draft models
aux_recon = self.mhc_post(hidden_states, residual, post_mix, res_mix)
aux_hidden_state = aux_recon.mean(dim=1)
if self.use_sequence_parallel:
aux_hidden_state = sp_all_gather(aux_hidden_state)[:full_num_tokens]
aux_hidden_states.append(aux_hidden_state)
final_aux_recon = aux_recon
if layer is not None:
# Reuse if the last layer was captured as an aux hidden state
if self.end_layer in self.aux_hidden_state_layers:
hidden_states = final_aux_recon
else:
hidden_states = self.mhc_post(
hidden_states, residual, post_mix, res_mix
)
if not get_pp_group().is_last_rank:
return IntermediateTensors(
{"hidden_states": hidden_states, "pre_mix": pre_mix}
)
if self.use_sequence_parallel:
hidden_states = sp_all_gather(hidden_states)[:full_num_tokens]
pre_mix = sp_all_gather(pre_mix)[:full_num_tokens]
if self._mtp_hidden_buffer is not None:
num_tokens = hidden_states.shape[0]
self._mtp_hidden_buffer[:num_tokens].copy_(hidden_states.flatten(1))
# Collapse the hc copies with the pre-mix from the last layer's FFN
# mixes — the mix the reference applies via
# ``last_layer.hc_pre(h, pre_mix)`` (v4.1 has no learned hc_head).
assert pre_mix is not None
hidden_states = torch.ops.vllm.hc_collapse_triton(hidden_states, pre_mix)
hidden_states = self.norm(hidden_states)
if len(aux_hidden_states) > 0:
return hidden_states, aux_hidden_states
return hidden_states
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
stacked_params_mapping = [
# (param_name, shard_name, shard_id)
("gate_up_proj", "w1", 0),
("gate_up_proj", "w3", 1),
("attn.fused_wqa_wkv", "attn.wq_a", 0),
("attn.fused_wqa_wkv", "attn.wkv", 1),
("compressor.fused_wkv_wgate", "compressor.wkv", 0),
("compressor.fused_wkv_wgate", "compressor.wgate", 1),
]
params_dict = dict(self.named_parameters())
loaded_params: set[str] = set()
def _resolve_param_name(name: str) -> str:
"""Resolve scale naming across ROCm FP8 and MXFP8 methods."""
if name.endswith("_inv"):
direct_name = name.removesuffix("_inv")
if direct_name in params_dict:
return direct_name
inv_name = f"{name}_inv"
if name not in params_dict and inv_name in params_dict:
return inv_name
return name
# TP for attention
tp_size = get_tensor_model_parallel_world_size()
tp_rank = get_tensor_model_parallel_rank()
n_head = self.config.num_attention_heads
n_local_head = n_head // tp_size
head_rank_start = n_local_head * tp_rank
head_rank_end = n_local_head * (tp_rank + 1)
# Pre-compute expert mapping ONCE.
expert_mapping = self.get_expert_mapping()
# Block-FP8 shared experts: pad the intermediate up to the TP-uniform
# block count so the standard loaders below slice it evenly (trailing
# ranks land on the zero pad). SP / unquantized ones need no padding.
pad_shared_expert = (
getattr(self.quant_config, "weight_block_size", None) is not None
and not self.use_sequence_parallel
)
for name, loaded_weight in weights:
if name.startswith(("vision.", "aligner.", "image_")):
# Vision weights are loaded by the outer multimodal wrapper.
logger.warning_once("Skipping non-text weight: %s", name)
continue
if pad_shared_expert and ".shared_experts." in name:
loaded_weight = self._pad_shared_expert_weight(
self.quant_config, name, loaded_weight
)
for param_name, weight_name, shard_id in stacked_params_mapping:
# Skip non-stacked layers and experts (experts handled below).
if ".experts." in name:
continue
if weight_name not in name:
continue
name = name.replace(weight_name, param_name)
if is_pp_missing_parameter(name, self):
break
if name not in params_dict:
head, _, leaf = name.rpartition(".")
suffixed = f"{head}.base_layer.{leaf}"
if suffixed in params_dict:
name = suffixed
name = _resolve_param_name(name)
param = params_dict[name]
weight_loader = param.weight_loader
weight_loader(param, loaded_weight, shard_id)
loaded_params.add(name)
break
else:
if ".experts." in name:
# E8M0 scales are stored as float8_e8m0fnu in
# checkpoints but the MoE param is uint8. copy_()
# would do a numeric conversion (e.g. 2^-7 → 0),
# destroying the raw exponent bytes.
if (
"weight_scale" in name
and loaded_weight.dtype == torch.float8_e8m0fnu
):
loaded_weight = loaded_weight.view(torch.uint8)
for mapping in expert_mapping:
param_name, weight_name, expert_id, expert_shard_id = mapping
if weight_name not in name:
continue
name_mapped = name.replace(weight_name, param_name)
if is_pp_missing_parameter(name_mapped, self):
continue
name_mapped = _resolve_param_name(name_mapped)
param = params_dict[name_mapped]
# We should ask the weight loader to return success or not
# here since otherwise we may skip experts with other
# available replicas.
weight_loader = typing.cast(
Callable[..., bool], param.weight_loader
)
success = weight_loader(
param,
loaded_weight,
name_mapped,
shard_id=expert_shard_id,
expert_id=expert_id,
return_success=True,
)
if success:
name = name_mapped
break
loaded_params.add(name_mapped)
continue
elif "attn_sink" in name:
if is_pp_missing_parameter(name, self):
continue
narrow_weight = loaded_weight[head_rank_start:head_rank_end]
n = narrow_weight.shape[0]
params_dict[name][:n].copy_(narrow_weight)
loaded_params.add(name)
continue
else:
if is_pp_missing_parameter(name, self):
continue
# Non-LoRA params on a LoRA-wrapped module live at
# ``<head>.base_layer.<leaf>``; the checkpoint is plain.
if name not in params_dict:
head, _, leaf = name.rpartition(".")
suffixed = f"{head}.base_layer.{leaf}"
if suffixed in params_dict:
name = suffixed
name = _resolve_param_name(name)
param = params_dict[name]
weight_loader = getattr(
param, "weight_loader", default_weight_loader
)
weight_loader(param, loaded_weight)
loaded_params.add(name)
continue
return loaded_params
@staticmethod
def _pad_shared_expert_weight(
quant_config: QuantizationConfig | None,
name: str,
loaded_weight: torch.Tensor,
) -> torch.Tensor:
"""Zero-pad a block-FP8 shared-expert weight/scale on its intermediate
axis so the standard TP loaders split it into even, block-aligned shards
(trailing ranks get the zero pad). gate (w1)/up (w3) [I, H] pad dim 0;
down (w2 -> down_proj) [H, I] pads dim 1.
"""
block_size = getattr(quant_config, "weight_block_size", None)
assert block_size is not None
# Round the intermediate axis up to a whole number of TP shards. The axis
# is in elements for weights (step = block) and in blocks for scales.
step = (
1 if name.endswith(("weight_scale_inv", "weight_scale")) else block_size[0]
)
dim = 1 if ".down_proj." in name else 0
mult = get_tensor_model_parallel_world_size() * step
pad = cdiv(loaded_weight.shape[dim], mult) * mult - loaded_weight.shape[dim]
if pad == 0:
return loaded_weight
pad_shape = list(loaded_weight.shape)
pad_shape[dim] = pad
return torch.cat([loaded_weight, loaded_weight.new_zeros(pad_shape)], dim=dim)
def get_expert_mapping(self) -> list[tuple[str, str, int, str]]:
# Params for weights, fp8 weight scales, fp8 activation scales
# (param_name, weight_name, expert_id, shard_id)
return fused_moe_make_expert_params_mapping(
self,
ckpt_gate_proj_name="w1",
ckpt_down_proj_name="w2",
ckpt_up_proj_name="w3",
num_experts=self.config.n_routed_experts,
)
def finalize_mega_moe_weights(self) -> None:
return
def finalize_mhc_broadcast_weights(self) -> None:
if not get_pp_group().is_first_rank or self.start_layer >= self.end_layer:
return
layer = self.layers[self.start_layer]
if isinstance(layer, DeepseekV4DecoderLayer):
broadcast = (
layer.hc_attn_fn.detach()
.view(-1, layer.hc_mult, layer.hidden_size)
.sum(dim=1)
)
if layer.hc_attn_fn_broadcast is None:
layer.hc_attn_fn_broadcast = broadcast
else:
layer.hc_attn_fn_broadcast.copy_(broadcast)