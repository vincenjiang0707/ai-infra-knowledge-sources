source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/gemma3n/
lastmod: 2026-09-23

@support_torch_compile(
enable_if=lambda vllm_config: vllm_config.cache_config.kv_sharing_fast_prefill
)
class Gemma3nSelfDecoder(nn.Module):
"""Includes altup embedding and self decoder layers."""
def __init__(
self,
*,
vllm_config: VllmConfig,
prefix: str = "",
decoder_layers: list[Gemma3nDecoderLayer],
layer_idx_start: int,
):
super().__init__()
self.decoder_layers = decoder_layers
self.layer_idx_start = layer_idx_start
config = vllm_config.model_config.hf_config
self.config = config
quant_config = vllm_config.quant_config
self.embed_tokens = VocabParallelEmbedding(
config.vocab_size,
config.hidden_size,
quant_config=quant_config,
prefix=f"{prefix}.embed_tokens",
)
self.register_buffer(
"embed_scale",
torch.tensor(
config.hidden_size**0.5,
dtype=self.embed_tokens.weight.dtype,
),
persistent=False,
)
# Additional per-layer embeddings (PLE)
self.embed_tokens_per_layer = VocabParallelEmbedding(
config.vocab_size_per_layer_input,
config.num_hidden_layers * config.hidden_size_per_layer_input,
quant_config=quant_config,
prefix=f"{prefix}.per_layer_embed_tokens",
)
self.register_buffer(
"embed_scale_per_layer",
torch.tensor(
config.hidden_size_per_layer_input**0.5,
dtype=self.embed_tokens.weight.dtype,
),
persistent=False,
)
self.per_layer_model_projection = ColumnParallelLinear(
config.hidden_size,
config.num_hidden_layers * config.hidden_size_per_layer_input,
bias=False,
gather_output=True,
return_bias=False,
quant_config=quant_config,
prefix=f"{prefix}.per_layer_model_projection",
)
self.per_layer_projection_norm = RMSNorm(
hidden_size=config.hidden_size_per_layer_input,
eps=config.rms_norm_eps,
)
self.register_buffer(
"per_layer_input_scale",
torch.rsqrt(torch.tensor(2.0)).to(self.embed_tokens.weight.dtype),
persistent=False,
)
self.register_buffer(
"per_layer_projection_scale",
torch.tensor(
config.hidden_size**0.5,
dtype=self.embed_tokens.weight.dtype,
),
persistent=False,
)
self.altup_projections = nn.ModuleList(
[
ColumnParallelLinear(
config.hidden_size,
config.hidden_size,
bias=False,
gather_output=True,
return_bias=False,
quant_config=quant_config,
prefix=f"{prefix}.altup_projections.{idx - 1}",
)
for idx in range(1, self.config.altup_num_inputs)
]
)
def get_per_layer_input_embeddings(self, input_ids: torch.Tensor) -> torch.Tensor:
# Deal with the fact that vocab_size_per_layer_input < vocab_size
# which causes us to have some out of vocab tokens by setting
# those token ids to 0. This matches the HF implementation.
per_layer_inputs_mask = torch.logical_and(
input_ids >= 0, input_ids < self.config.vocab_size_per_layer_input
)
per_layer_inputs_tokens = torch.where(
per_layer_inputs_mask, input_ids, torch.zeros_like(input_ids)
)
return (
self.embed_tokens_per_layer(per_layer_inputs_tokens)
* self.embed_scale_per_layer
)
def get_per_layer_inputs(
self,
hidden_states_0: torch.Tensor,
per_layer_inputs: torch.Tensor | None,
) -> torch.Tensor:
per_layer_projection = self.per_layer_model_projection(hidden_states_0)
per_layer_projection = per_layer_projection.reshape(
*hidden_states_0.shape[:-1],
self.config.num_hidden_layers,
self.config.hidden_size_per_layer_input,
)
per_layer_projection = self.per_layer_projection_norm(per_layer_projection)
if per_layer_inputs is not None:
# Profiling run does not compute per_layer_inputs
per_layer_inputs = per_layer_projection + per_layer_inputs
per_layer_inputs *= self.per_layer_input_scale
else:
per_layer_inputs = per_layer_projection
return per_layer_inputs
def embed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
return self.embed_tokens(input_ids) * self.embed_scale
def altup_embed(self, hidden_states_0: torch.Tensor) -> torch.Tensor:
# Altup embed.
hidden_states = [hidden_states_0] * self.config.altup_num_inputs
target_magnitude = torch.mean(hidden_states_0**2, dim=-1, keepdim=True) ** 0.5
for i in range(1, self.config.altup_num_inputs):
hidden_states[i] = self.altup_projections[i - 1](hidden_states[i])
new_magnitude = (
torch.mean(hidden_states[i] ** 2, dim=-1, keepdim=True) ** 0.5
)
hidden_states[i] *= target_magnitude / torch.maximum(new_magnitude, EPS)
hidden_states = torch.stack(hidden_states, dim=-1)
return hidden_states
def forward(
self,
input_ids: torch.Tensor | None,
positions: torch.Tensor,
inputs_embeds: torch.Tensor | None = None,
per_layer_inputs: torch.Tensor | None = None,
**kwargs,
) -> tuple[torch.Tensor, torch.Tensor]:
if inputs_embeds is not None:
hidden_states_0 = inputs_embeds
else:
hidden_states_0 = self.embed_input_ids(input_ids)
adjusted_per_layer_inputs = self.get_per_layer_inputs(
hidden_states_0, per_layer_inputs
)
hidden_states = self.altup_embed(hidden_states_0)
# [altnum_inputs, num_tokens, hidden_size]
hidden_states = hidden_states.permute(2, 0, 1)
for idx, layer in enumerate(self.decoder_layers):
layer_idx = idx + self.layer_idx_start
# [altup_num_inputs, num_tokens, hidden_size]
hidden_states = layer(
positions=positions,
hidden_states=hidden_states,
per_layer_input=adjusted_per_layer_inputs[:, layer_idx, :],
**kwargs,
)
# [num_tokens, hidden_size, altnum_inputs]
hidden_states = hidden_states.permute(1, 2, 0)
return hidden_states, adjusted_per_layer_inputs