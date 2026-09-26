source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/conformer_encoder/
lastmod: 2026-09-24

class ConformerEncoder(nn.Module):
"""Conformer encoder used by FireRedASR2."""
def __init__(
self,
idim: int,
n_layers_enc: int,
n_head: int,
d_model: int,
kernel_size: int = 33,
pe_maxlen: int = 5000,
):
super().__init__()
self.odim = d_model
self.input_preprocessor = Conv2dSubsampling(idim, d_model)
self.positional_encoding = RelPositionalEncoding(d_model, max_len=pe_maxlen)
self.layer_stack = nn.ModuleList()
for _ in range(n_layers_enc):
block = RelPosEmbConformerBlock(d_model, n_head, kernel_size)
self.layer_stack.append(block)
def forward(
self,
padded_input: torch.Tensor,
input_lengths: torch.Tensor,
pad: bool = True,
):
if pad:
padded_input = F.pad(
padded_input,
(0, 0, 0, self.input_preprocessor.context - 1),
"constant",
0.0,
)
src_mask = self.padding_position_is_0(padded_input, input_lengths)
embed_output, input_lengths, src_mask = self.input_preprocessor(
padded_input, src_mask
)
enc_output = embed_output
pos_emb = self.positional_encoding(embed_output)
for enc_layer in self.layer_stack:
enc_output = enc_layer(
enc_output, pos_emb, slf_attn_mask=src_mask, pad_mask=src_mask
)
return enc_output, input_lengths, src_mask
def padding_position_is_0(
self, padded_input: torch.Tensor, input_lengths: torch.Tensor
) -> torch.Tensor:
N, T = padded_input.size()[:2]
# Use broadcasting instead of a Python loop for efficiency.
positions = torch.arange(T, device=padded_input.device).unsqueeze(0)
mask = (positions < input_lengths.unsqueeze(1)).to(torch.uint8)
return mask.unsqueeze(1)