source: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/fusion/mla_attn_quant_fusion/
lastmod: 2026-09-23

class MLAAttnFp8GroupQuantPattern(
VllmPatternReplacement[..., tuple[torch.Tensor, torch.Tensor]]
):
"""Fusion for MLA Attention+Fp8GroupQuant (per-group dynamic FP8).
Matches the pattern: MLA attention -> per_token_group_fp8_quant, and
replaces it with MLA attention(output_block_scale=group_scale_buffer).
Used by models with block FP8 quantization (e.g. DeepSeek V3).
"""
def __init__(
self,
layer: MLAAttention,
dtype: torch.dtype,
quant_key: QuantKey,
has_col_major_scales: bool,
is_e8m0: bool,
is_tma_aligned: bool,
) -> None:
self._layer_name = layer.layer_name
self._num_heads = layer.num_heads
self._v_head_dim = layer.v_head_dim
self._kv_lora_rank = layer.kv_lora_rank
self._qk_rope_head_dim = layer.qk_rope_head_dim
self._qk_head_dim = layer.qk_nope_head_dim + layer.qk_rope_head_dim
self._output_dim = layer.num_heads * layer.v_head_dim
self._dtype = dtype
self._layer = layer
self._group_size = quant_key.scale.group_shape[1]
self._has_col_major_scales = has_col_major_scales
self._is_e8m0 = is_e8m0
self._is_tma_aligned = is_tma_aligned
self._quant_matcher = MatcherQuantFP8(
quant_key,
has_col_major_scales=has_col_major_scales,
is_e8m0=is_e8m0,
is_tma_aligned=is_tma_aligned,
)
@property
def pattern(
self,
) -> Callable[..., tuple[torch.Tensor, torch.Tensor]]:
_ln = _encode_layer_name(self._layer_name)
if _USE_LAYERNAME:
def _pattern_with_ln( # type: ignore[misc]
q,
kv_c_normed,
k_pe,
output_attn,
kv_cache_dummy_dep,
scale,
layer_name,
):
at1 = auto_functionalized(
MLA_ATTN_OP,
q=q,
kv_c_normed=kv_c_normed,
k_pe=k_pe,
output=output_attn,
layer_name=layer_name,
output_scale=None,
output_block_scale=None,
kv_cache_dummy_dep=kv_cache_dummy_dep,
)
attn_out = at1[1]
result = torch.empty(
attn_out.shape, device=attn_out.device, dtype=FP8_DTYPE
)
finfo = torch.finfo(FP8_DTYPE)
_, result, scale = auto_functionalized(
self._quant_matcher.QUANT_OP,
input=attn_out,
output_q=result,
output_s=scale,
group_size=self._group_size,
eps=1e-10,
fp8_min=finfo.min,
fp8_max=finfo.max,
scale_ue8m0=self._is_e8m0,
dummy_is_scale_transposed=self._has_col_major_scales,
dummy_is_tma_aligned=self._is_tma_aligned,
)
return result, scale
return _pattern_with_ln
def _pattern(
q: torch.Tensor,
kv_c_normed: torch.Tensor,
k_pe: torch.Tensor,
output_attn: torch.Tensor,
kv_cache_dummy_dep: torch.Tensor,
scale: torch.Tensor,
) -> tuple[torch.Tensor, torch.Tensor]:
at1 = auto_functionalized(
MLA_ATTN_OP,
q=q,
kv_c_normed=kv_c_normed,
k_pe=k_pe,
output=output_attn,
layer_name=_ln,
output_scale=None,
output_block_scale=None,
kv_cache_dummy_dep=kv_cache_dummy_dep,
)
attn_out = at1[1]
result = torch.empty(
attn_out.shape, device=attn_out.device, dtype=FP8_DTYPE
)
finfo = torch.finfo(FP8_DTYPE)
_, result, scale = auto_functionalized(
self._quant_matcher.QUANT_OP,
input=attn_out,
output_q=result,
output_s=scale,
group_size=self._group_size,
eps=1e-10,
fp8_min=finfo.min,
fp8_max=finfo.max,
scale_ue8m0=self._is_e8m0,
dummy_is_scale_transposed=self._has_col_major_scales,
dummy_is_tma_aligned=self._is_tma_aligned,
)
return result, scale
return _pattern
@property
def replacement(
self,
) -> Callable[..., tuple[torch.Tensor, torch.Tensor]]:
_ln = _encode_layer_name(self._layer_name)
if _USE_LAYERNAME:
def _replacement_with_ln( # type: ignore[misc]
q,
kv_c_normed,
k_pe,
output_attn,
kv_cache_dummy_dep,
scale,
layer_name,
):
output_attn = torch.empty(
[q.shape[0], self._output_dim],
dtype=FP8_DTYPE,
device=q.device,
)
at1 = auto_functionalized(
MLA_ATTN_OP,
q=q,
kv_c_normed=kv_c_normed,
k_pe=k_pe,
output=output_attn,
layer_name=layer_name,
output_scale=None,
output_block_scale=scale,
kv_cache_dummy_dep=kv_cache_dummy_dep,
quant_group_size=self._group_size,
quant_scale_ue8m0=self._is_e8m0,
quant_col_major=self._has_col_major_scales,
quant_tma_aligned=self._is_tma_aligned,
)
return at1[1], at1[2]
return _replacement_with_ln
def _replacement(q, kv_c_normed, k_pe, output_attn, kv_cache_dummy_dep, scale):
output_attn = torch.empty(
[q.shape[0], self._output_dim],
dtype=FP8_DTYPE,
device=q.device,
)
at1 = auto_functionalized(
MLA_ATTN_OP,
q=q,
kv_c_normed=kv_c_normed,
k_pe=k_pe,
output=output_attn,
layer_name=_ln,
output_scale=None,
output_block_scale=scale,
kv_cache_dummy_dep=kv_cache_dummy_dep,
quant_group_size=self._group_size,
quant_scale_ue8m0=self._is_e8m0,
quant_col_major=self._has_col_major_scales,
quant_tma_aligned=self._is_tma_aligned,
)
return at1[1], at1[2]
return _replacement
def get_inputs(self) -> list[torch.Tensor]:
inputs: list = [
self.empty(5, self._num_heads, self._qk_head_dim, dtype=self._dtype),
self.empty(5, self._kv_lora_rank, dtype=self._dtype),
self.empty(5, 1, self._qk_rope_head_dim, dtype=self._dtype),
self.empty(5, self._output_dim, dtype=self._dtype),
self.empty(0, dtype=self._dtype),
self._quant_matcher.empty_f32(1, 1),
]
if _USE_LAYERNAME:
inputs.append(_encode_layer_name(self._layer_name))
return inputs