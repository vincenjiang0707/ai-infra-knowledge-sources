source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/deepencoder2/
lastmod: 2026-09-23

@PluggableLayer.register("qwen2_decoder")
class CustomQwen2Decoder(PluggableLayer):
"""Qwen2 visual encoder
non-causal attention + causal attention
token_type_ids ：0=non-causal, 1=causal
"""
# --8<-- [end:qwen2_decoder]
def __init__(
self,
decoder_layer: int = 24,
max_position_embeddings: int = 131072,
hidden_dimension: int = 896,
num_attention_heads: int = 14,
num_key_value_heads: int = 2,
intermediate_size: int = 4864,
vocab_size: int = 151936,
attn_implementation: str = "sdpa",
rms_norm_eps: float = 1e-06,
rope_theta: float = 1000000.0,
attention_dropout: float = 0.0,
hidden_act: str = "silu",
initializer_range: float = 0.02,
):
super().__init__()
# load
Qwen2Config = transformers.Qwen2Config
# config
config = Qwen2Config(
hidden_size=hidden_dimension,
num_hidden_layers=decoder_layer,
num_attention_heads=num_attention_heads,
num_key_value_heads=num_key_value_heads,
intermediate_size=intermediate_size,
max_position_embeddings=max_position_embeddings,
vocab_size=vocab_size,
rms_norm_eps=rms_norm_eps,
rope_theta=rope_theta,
attention_dropout=attention_dropout,
hidden_act=hidden_act,
initializer_range=initializer_range,
_attn_implementation=attn_implementation, # ⭐
)
#
self.model = self._create_custom_model(config)
del self.model.embed_tokens
def _create_custom_model(self, config):
"""Qwen2Model."""
class CustomQwen2ModelInner(Qwen2Model):
def forward(
self,
input_ids=None,
attention_mask=None,
position_ids=None,
past_key_values=None,
inputs_embeds=None,
token_type_ids=None, # ⭐
use_cache=None,
output_attentions=None,
output_hidden_states=None,
return_dict=None,
cache_position=None,
):
causal_mask_mapping = {
"full_attention": self._update_causal_mask(
attention_mask,
inputs_embeds,
cache_position,
past_key_values,
output_attentions,
)
}
outputs = super().forward(
input_ids=input_ids,
attention_mask=causal_mask_mapping,
position_ids=position_ids,
past_key_values=past_key_values,
inputs_embeds=inputs_embeds,
use_cache=use_cache,
output_attentions=output_attentions,
output_hidden_states=output_hidden_states,
return_dict=return_dict,
cache_position=cache_position,
)
return outputs
def _update_causal_mask(
self,
attention_mask,
input_tensor,
cache_position,
past_key_values,
output_attentions,
):
dtype, device = input_tensor.dtype, input_tensor.device
min_dtype = torch.finfo(dtype).min
batch_size, sequence_length = (
input_tensor.shape[0],
input_tensor.shape[1],
)
# attention mask
causal_mask = self._create_custom_4d_mask(
sequence_length=sequence_length,
dtype=dtype,
device=device,
batch_size=batch_size,
)
# padding mask
if attention_mask is not None and attention_mask.dim() == 2:
padding_mask = attention_mask[:, None, None, :].to(dtype=dtype)
padding_mask = (1.0 - padding_mask) * min_dtype
causal_mask = causal_mask + padding_mask
return causal_mask
@classmethod
@lru_cache(maxsize=8)
def compute_mask_base(cls, sequence_length, dtype, device):
# token_type_ids is the fixed pattern [0]*n_query + [1]*n_query,
# identical across the batch, so the mask depends only on
# sequence_length: img tokens (first half) attend to
# everything, txt tokens (second half) attend causally among
# themselves. lru_cache keeps one batch-invariant [1, 1, S, S]
# mask per (S, dtype, device).
min_dtype = torch.finfo(dtype).min
n_query = sequence_length // 2
img = torch.arange(sequence_length, device=device) < n_query
txt = ~img
causal = torch.tril(
torch.ones(
sequence_length,
sequence_length,
dtype=torch.bool,
device=device,
)
)
allow = img[None, :] | (txt[:, None] & txt[None, :] & causal)
return torch.where(
allow,
torch.zeros((), dtype=dtype, device=device),
torch.full((), min_dtype, dtype=dtype, device=device),
)[None, None]
def _create_custom_4d_mask(
self,
sequence_length,
dtype,
device,
batch_size,
):
base = self.compute_mask_base(sequence_length, dtype, device)
return base.expand(batch_size, -1, -1, -1)
return CustomQwen2ModelInner(config)
def forward(
self,
inputs_embeds: torch.Tensor,
token_type_ids: torch.Tensor,
attention_mask: torch.Tensor = None,
**kwargs,
):
"""Args:
inputs_embeds: [batch_size, seq_len, hidden_dim]
token_type_ids: [batch_size, seq_len], 0=non-causal, 1=causal
attention_mask: [batch_size, seq_len], optional
"""
return self.model(
inputs_embeds=inputs_embeds,
token_type_ids=token_type_ids,
attention_mask=attention_mask,
**kwargs,
)