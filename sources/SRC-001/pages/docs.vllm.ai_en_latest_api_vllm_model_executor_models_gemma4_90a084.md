source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/gemma4/
lastmod: 2026-09-24

@support_torch_compile(
enable_if=lambda vllm_config: not vllm_config.cache_config.kv_sharing_fast_prefill
)
class Gemma4Model(nn.Module, EagleModelMixin, SupportsQuant):
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
config = _get_text_config(vllm_config.model_config.hf_config)
cache_config = vllm_config.cache_config
quant_config = vllm_config.quant_config
self.config = config
self.quant_config = quant_config
self.hf_to_vllm_mapper = _gemma4_layer_weights_mapper(config)
# PLE config values (default to 0 if not present — disables PLE)
self.hidden_size_per_layer_input = getattr(
config, "hidden_size_per_layer_input", 0
)
self.vocab_size_per_layer_input = getattr(
config, "vocab_size_per_layer_input", config.vocab_size
)
self.embed_tokens = VocabParallelEmbedding(
config.vocab_size,
config.hidden_size,
quant_config=quant_config,
prefix=f"{prefix}.embed_tokens",
)
# Per-Layer Embedding (PLE) components
self.embed_tokens_per_layer: VocabParallelEmbedding | None
self.per_layer_model_projection: ColumnParallelLinear | None
self.per_layer_projection_norm: RMSNorm | None
if (
self.hidden_size_per_layer_input is not None
and self.hidden_size_per_layer_input > 0
):
total_ple_dim = self.hidden_size_per_layer_input * config.num_hidden_layers
self.embed_tokens_per_layer = VocabParallelEmbedding(
self.vocab_size_per_layer_input,
total_ple_dim,
quant_config=quant_config,
prefix=f"{prefix}.embed_tokens_per_layer",
)
# Scaled embedding factor (from config, not hardcoded)
# Register as buffer so it moves to GPU with the model
# and interacts correctly with torch.compile AOT caching.
self.register_buffer(
"embed_scale_per_layer",
torch.tensor(self.hidden_size_per_layer_input**0.5),
persistent=False,
)
# Projection: hidden_size → total_ple_dim
# ColumnParallelLinear with gather_output=True
self.per_layer_model_projection = ColumnParallelLinear(
config.hidden_size,
total_ple_dim,
bias=False,
gather_output=True,
return_bias=False,
quant_config=quant_config,
prefix=f"{prefix}.per_layer_model_projection",
)
# PLE projection norm: output = norm(x) * weight
self.per_layer_projection_norm = RMSNorm(
self.hidden_size_per_layer_input,
eps=config.rms_norm_eps,
)
# Scale factor for combining projection + per_layer_inputs
# Register as buffer so it moves to GPU with the model
# and interacts correctly with torch.compile AOT caching.
self.register_buffer(
"per_layer_input_scale",
torch.rsqrt(torch.tensor(2.0)),
persistent=False,
)
# Scaled projection: multiply output by hidden_size**-0.5.
# Register as buffer for GPU placement and torch.compile.
self.register_buffer(
"per_layer_projection_scale",
torch.tensor(config.hidden_size**-0.5),
persistent=False,
)
else:
self.embed_tokens_per_layer = None
self.embed_scale_per_layer = None
self.per_layer_model_projection = None
self.per_layer_projection_norm = None
self.per_layer_input_scale = None
self.per_layer_projection_scale = None
self.start_layer, self.end_layer, self.layers = make_layers(
config.num_hidden_layers,
lambda prefix: Gemma4DecoderLayer(
config,
cache_config=cache_config,
quant_config=quant_config,
prefix=prefix,
),
prefix=f"{prefix}.layers",
)
# Final norm: output = norm(x) * weight
self.norm = RMSNorm(config.hidden_size, eps=config.rms_norm_eps)
# Embedding scale = sqrt(hidden_size), cast to model dtype to avoid
# mixed-precision drift from bf16 * fp32 across deep stacks.
self.register_buffer(
"normalizer",
torch.tensor(
config.hidden_size**0.5,
dtype=vllm_config.model_config.dtype,
),
persistent=False,
)
# --- You Only Cache Once (YOCO) split for fast prefill ---
first_kv_shared_layer_idx = config.num_hidden_layers - getattr(
config, "num_kv_shared_layers", 0
)
from vllm.compilation.backends import set_model_tag
# Layers 0..(K-1) are self-decoder layers in YOCO
with set_model_tag("self_decoder"):
self.self_decoder = Gemma4SelfDecoderLayers(
vllm_config=vllm_config,
prefix=f"{prefix}.self_decoder",
decoder_layers=self.layers[:first_kv_shared_layer_idx],
layer_idx_start=0,
embed_tokens=self.embed_tokens,
normalizer=self.normalizer,
embed_tokens_per_layer=getattr(self, "embed_tokens_per_layer", None),
embed_scale_per_layer=getattr(self, "embed_scale_per_layer", None),
per_layer_model_projection=getattr(
self, "per_layer_model_projection", None
),
per_layer_projection_norm=getattr(
self, "per_layer_projection_norm", None
),
per_layer_input_scale=getattr(self, "per_layer_input_scale", None),
per_layer_projection_scale=getattr(
self, "per_layer_projection_scale", None
),
)
# Layers K..(N-1) are cross-decoder layers in YOCO
with set_model_tag("cross_decoder"):
self.cross_decoder = Gemma4CrossDecoderLayers(
vllm_config=vllm_config,
prefix=f"{prefix}.cross_decoder",
decoder_layers=self.layers[first_kv_shared_layer_idx:],
layer_idx_start=first_kv_shared_layer_idx,
)
self.fast_prefill_enabled = cache_config.kv_sharing_fast_prefill
if self.fast_prefill_enabled:
# Allocate static buffers for CUDAGraph
max_num_tokens = vllm_config.scheduler_config.max_num_batched_tokens
device = next(self.parameters()).device
self.positions = torch.zeros(
max_num_tokens, dtype=torch.int64, device=device
)
self.hidden_states = torch.zeros(
(max_num_tokens, config.hidden_size),
dtype=vllm_config.model_config.dtype,
device=device,
)
if (
self.hidden_size_per_layer_input
and self.hidden_size_per_layer_input > 0
):
self.per_layer_inputs = torch.zeros(
(
max_num_tokens,
config.num_hidden_layers,
self.hidden_size_per_layer_input,
),
dtype=vllm_config.model_config.dtype,
device=device,
)
else:
self.per_layer_inputs = None
# Custom factory that includes per_layer_inputs for PLE-enabled PP.
# per_layer_inputs has shape (batch, num_layers, per_layer_dim),
# which differs from the standard (batch, hidden_size) shape,
# so we can't use the default factory.
ple_dim = self.hidden_size_per_layer_input
num_layers = config.num_hidden_layers
hidden_size = config.hidden_size
def _make_empty_intermediate_tensors(
batch_size: int,
dtype: torch.dtype,
device: torch.device,
) -> IntermediateTensors:
tensors: dict[str, torch.Tensor] = {
"hidden_states": torch.zeros(
(batch_size, hidden_size),
dtype=dtype,
device=device,
),
}
if ple_dim and ple_dim > 0:
tensors["per_layer_inputs"] = torch.zeros(
(batch_size, num_layers, ple_dim),
dtype=dtype,
device=device,
)
return IntermediateTensors(tensors)
self.make_empty_intermediate_tensors = _make_empty_intermediate_tensors
def embed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
return self.self_decoder.embed_input_ids(input_ids)
def get_per_layer_inputs(self, input_ids: torch.Tensor) -> torch.Tensor | None:
"""Get per-layer embeddings from embed_tokens_per_layer.
Returns:
Per-layer embeddings (num_tokens, num_layers,
hidden_size_per_layer_input)
"""
return self.self_decoder.get_per_layer_inputs(input_ids)
def project_per_layer_inputs(
self,
inputs_embeds: torch.Tensor,
per_layer_inputs: torch.Tensor | None,
) -> torch.Tensor | None:
"""Project inputs_embeds and combine with per_layer_inputs.
Steps:
1. Project inputs_embeds: hidden_size → total_ple_dim
2. Scale by hidden_size^{-0.5}
3. Reshape to (num_tokens, num_layers, per_layer_dim)
4. Normalize with per_layer_projection_norm
5. Combine: (projection + per_layer_inputs) * 1/sqrt(2)
"""
return self.self_decoder.project_per_layer_inputs(
inputs_embeds, per_layer_inputs
)
def fast_prefill_forward(
self,
input_ids: torch.Tensor | None,
positions: torch.Tensor,
inputs_embeds: torch.Tensor | None = None,
per_layer_inputs: torch.Tensor | None = None,
**kwargs,
) -> torch.Tensor:
logits_indices_padded, num_logits_indices = None, None
attn_metadata = get_forward_context().attn_metadata
if attn_metadata is not None:
assert isinstance(attn_metadata, dict)
layer_attn_metadata = attn_metadata[
self.layers[-1].self_attn.attn.layer_name
]
if isinstance(layer_attn_metadata, KVSharingFastPrefillMetadata):
logits_indices_padded = layer_attn_metadata.logits_indices_padded
num_logits_indices = layer_attn_metadata.num_logits_indices
batch_size = positions.size(0)
self.positions[:batch_size].copy_(positions)
self_decoder_hidden_states, per_layer_inputs = self.self_decoder(
input_ids=input_ids,
positions=self.positions[:batch_size],
inputs_embeds=inputs_embeds,
per_layer_inputs=per_layer_inputs,
**kwargs,
)
if logits_indices_padded is None:
logits_indices_padded = torch.arange(
batch_size,
dtype=positions.dtype,
device=positions.device,
)
# NOTE: Keep .clone() until fix in
# https://github.com/vllm-project/vllm/pull/22282
hidden_states = self_decoder_hidden_states.clone()
num_padded = logits_indices_padded.size(0)
self.positions[:num_padded].copy_(positions[logits_indices_padded])
self.hidden_states[:num_padded].copy_(
self_decoder_hidden_states[logits_indices_padded]
)
if self.per_layer_inputs is not None and per_layer_inputs is not None:
self.per_layer_inputs[:num_padded].copy_(
per_layer_inputs[logits_indices_padded]
)
# Update batch_descriptor so the cross-decoder's piecewise
# CUDAGraphWrapper dispatches to the correct (reduced) batch size.
forward_context = get_forward_context()
orig_batch_desc = forward_context.batch_descriptor
if orig_batch_desc is not None:
forward_context.batch_descriptor = replace(
orig_batch_desc, num_tokens=num_padded
)
cross_per_layer = (
self.per_layer_inputs[:num_padded]
if self.per_layer_inputs is not None
else None
)
cross_hidden_states = self.cross_decoder(
self.positions[:num_padded],
self.hidden_states[:num_padded],
cross_per_layer,
**kwargs,
)
# Restore the original batch_descriptor
forward_context.batch_descriptor = orig_batch_desc
if num_logits_indices is not None:
assert num_logits_indices > 0
hidden_states[logits_indices_padded[:num_logits_indices]] = (
cross_hidden_states[:num_logits_indices]
)
else:
hidden_states = cross_hidden_states
return hidden_states
def forward(
self,
input_ids: torch.Tensor | None,
positions: torch.Tensor,
intermediate_tensors: IntermediateTensors | None,
inputs_embeds: torch.Tensor | None = None,
per_layer_inputs: torch.Tensor | None = None,
**kwargs,
) -> torch.Tensor | IntermediateTensors | tuple[torch.Tensor, list[torch.Tensor]]:
if self.fast_prefill_enabled:
hidden_states = self.fast_prefill_forward(
input_ids,
positions,
inputs_embeds,
per_layer_inputs,
**kwargs,
)
hidden_states = self.norm(hidden_states)
return hidden_states
# Normal (non-fast-prefill) path with PP support
if get_pp_group().is_first_rank:
if inputs_embeds is not None:
hidden_states = inputs_embeds
# When called from the multimodal wrapper, raw PLE
# embeddings are pre-computed and passed explicitly.
# Project them through per_layer_model_projection.
per_layer_inputs = self.project_per_layer_inputs(
hidden_states, per_layer_inputs
)
else:
hidden_states = self.embed_input_ids(input_ids)
# Compute per-layer inputs for PLE
per_layer_embeds = self.get_per_layer_inputs(input_ids)
per_layer_inputs = self.project_per_layer_inputs(
hidden_states, per_layer_embeds
)
else:
assert intermediate_tensors is not None
hidden_states = intermediate_tensors["hidden_states"]
if per_layer_inputs is not None:
per_layer_inputs = intermediate_tensors["per_layer_inputs"]
residual = None
aux_hidden_states = self._maybe_add_hidden_state([], 0, hidden_states, residual)
for layer_idx, layer in enumerate(
islice(self.layers, self.start_layer, self.end_layer)
):
# Extract the per-layer embedding for this specific layer
if per_layer_inputs is not None:
actual_layer_idx = self.start_layer + layer_idx
layer_per_input = per_layer_inputs[
:, actual_layer_idx, :
] # (num_tokens, per_layer_dim)
else:
layer_per_input = None
hidden_states, residual = layer(
positions,
hidden_states,
residual,
per_layer_input=layer_per_input,
**kwargs,
)
self._maybe_add_hidden_state(
aux_hidden_states, layer_idx + 1, hidden_states, residual
)
if not get_pp_group().is_last_rank:
tensors: dict[str, torch.Tensor] = {
"hidden_states": hidden_states,
}
if per_layer_inputs is not None:
tensors["per_layer_inputs"] = per_layer_inputs
return IntermediateTensors(tensors)
# Gemma4 incorporates residual into hidden_states directly
# Apply norm without residual fusion when possible.
if residual is None:
hidden_states = self.norm(hidden_states)
else:
hidden_states, _ = self.norm(hidden_states, residual)
if len(aux_hidden_states) > 0:
return hidden_states, aux_hidden_states
return hidden_states
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
loader = AutoWeightsLoader(self)
return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)