source: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/fusion/qk_norm_rope_kvcache_fusion/
lastmod: 2026-09-24

class QkNormRopeKvCachePattern:
"""Match the unfused sequence:
q, k, v = split(qkv, ...)
q = rms_norm(q.view(heads), q_weight).view(flat)
k = rms_norm(k.view(heads), k_weight).view(flat)
q, k = rotary_embedding(positions, q, k, cos_sin_cache, is_neox)
q = q.view(num_heads, head_dim)
k = k.view(num_kv_heads, head_dim)
v = v.view(num_kv_heads, head_dim)
dummy = unified_kv_cache_update(k, v, layer_name)
Replace with:
q_out = empty(...)
k_out = empty(...)
dummy = fused_qk_norm_rope_and_unified_kv_cache_update(
q_out, k_out, qkv, positions, q_weight, k_weight,
eps, cos_sin_cache, is_neox, layer_name)
v = split(qkv, ...)[2].view(num_kv_heads, head_dim)
"""
FUSED_OP = torch.ops.vllm.fused_qk_norm_rope_and_unified_kv_cache_update.default
def __init__(
self,
layer: Attention,
eps: float,
is_neox: bool,
quant_query: bool,
) -> None:
self.layer_name = layer.layer_name
self.num_heads = layer.num_heads
self.num_kv_heads = layer.num_kv_heads
self.head_size = layer.head_size
self.head_size_v = layer.head_size_v
self.eps = eps
self.is_neox = is_neox
self.quant_query = quant_query
self.encoded_layer_name = _encode_layer_name(self.layer_name)
self.query_quant_group_shape = (
layer.query_quant.group_shape
if layer.query_quant is not None
else GroupShape.PER_TENSOR
)
self.q_size = self.num_heads * self.head_size
self.k_size = self.num_kv_heads * self.head_size
self.v_size = self.num_kv_heads * self.head_size_v
self.rope_matcher: MatcherRotaryEmbedding | MatcherMRotaryEmbedding = (
MatcherRotaryEmbedding(
is_neox=is_neox,
head_size=self.head_size,
num_heads=self.num_heads,
num_kv_heads=self.num_kv_heads,
)
)
def get_inputs(self) -> list:
T = 5
L = 4096
qkv = empty_bf16(T, self.q_size + self.k_size + self.v_size)
positions = empty_i64(T)
q_weight = empty_bf16(1, self.head_size)
k_weight = empty_bf16(1, self.head_size)
cos_sin_cache = empty_bf16(L, self.head_size)
inputs = [qkv, positions, q_weight, k_weight, cos_sin_cache]
if self.quant_query:
q_scale = empty_fp32(1)
inputs += [q_scale]
if _USE_LAYERNAME:
inputs.append(self.encoded_layer_name)
return inputs
def _get_layer_name(self, layer_name: LayerNameType | None) -> LayerNameType:
return self.encoded_layer_name if layer_name is None else layer_name
def pattern_non_fp8_quant_query(
self,
qkv: torch.Tensor,
positions: torch.Tensor,
q_weight: torch.Tensor,
k_weight: torch.Tensor,
cos_sin_cache: torch.Tensor,
layer_name: LayerNameType | None = None,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
q, k, v = qkv.split([self.q_size, self.k_size, self.v_size], dim=-1)
q_by_head = q.view(-1, self.q_size // self.head_size, self.head_size)
q_normed = vllm.ir.ops.rms_norm(q_by_head, q_weight, self.eps)
q_flat = q_normed.view(-1, self.q_size)
k_by_head = k.view(-1, self.k_size // self.head_size, self.head_size)
k_normed = vllm.ir.ops.rms_norm(k_by_head, k_weight, self.eps)
k_flat = k_normed.view(-1, self.k_size)
q_rope, k_rope = self.rope_matcher(positions, q_flat, k_flat, cos_sin_cache)
q_rope = q_rope.view(-1, self.num_heads, self.head_size)
k_rope = k_rope.view(-1, self.num_kv_heads, self.head_size)
v = v.view(-1, self.num_kv_heads, self.head_size_v)
dummy = torch.ops.vllm.unified_kv_cache_update(
k_rope, v, self._get_layer_name(layer_name)
)
return dummy, q_rope, k_rope, v
def replacement_non_fp8_quant_query(
self,
qkv: torch.Tensor,
positions: torch.Tensor,
q_weight: torch.Tensor,
k_weight: torch.Tensor,
cos_sin_cache: torch.Tensor,
layer_name: LayerNameType | None = None,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
q_out = torch.empty(
qkv.shape[0],
self.num_heads,
self.head_size,
device=qkv.device,
dtype=qkv.dtype,
)
k_out = torch.empty(
qkv.shape[0],
self.num_kv_heads,
self.head_size,
device=qkv.device,
dtype=qkv.dtype,
)
_, _, v = qkv.split([self.q_size, self.k_size, self.v_size], dim=-1)
v = v.view(qkv.shape[0], self.num_kv_heads, self.head_size_v)
results = auto_functionalized(
self.FUSED_OP,
q_out=q_out,
k_out=k_out,
qkv=qkv,
positions=positions,
q_weight=q_weight,
k_weight=k_weight,
rms_norm_eps=self.eps,
cos_sin_cache=cos_sin_cache,
is_neox=self.is_neox,
layer_name=self._get_layer_name(layer_name),
)
return results[0], results[1], results[2], v
def _quantize_query(
self,
query: torch.Tensor,
q_scale: torch.Tensor,
) -> tuple[torch.Tensor, torch.Tensor | None]:
if self.query_quant_group_shape.is_per_tensor():
q_out = torch.empty_like(query, dtype=current_platform.fp8_dtype())
q_quant = auto_functionalized(
torch.ops.vllm.rocm_aiter_per_tensor_quant.default,
out=q_out,
x=query,
scale=q_scale,
is_dynamic=False,
)
# The AITER op's schema marks scale mutable, so preserve its
# functionalized write-back as an output of the matched region.
return q_quant[1], q_quant[2]
# QuantFP8.forward_hip falls back to the generic static op for the
# historical per-head shape (-1, block_size). This also covers the
# degenerate one-local-KV-head case where a scalar scale is represented
# as (-1, q_size), rather than changing Attention's classification.
q_out = torch.empty(
query.shape,
device=query.device,
dtype=current_platform.fp8_dtype(),
)
q_quant = auto_functionalized(
torch.ops._C.static_scaled_fp8_quant.default,
result=q_out,
input=query,
scale=q_scale,
group_shape=[
self.query_quant_group_shape.row,
self.query_quant_group_shape.col,
],
)
return q_quant[1], None
def pattern_fp8_quant_query(
self,
qkv: torch.Tensor,
positions: torch.Tensor,
q_weight: torch.Tensor,
k_weight: torch.Tensor,
cos_sin_cache: torch.Tensor,
q_scale: torch.Tensor,
layer_name: LayerNameType | None = None,
) -> tuple[torch.Tensor, ...]:
q, k, v = qkv.split([self.q_size, self.k_size, self.v_size], dim=-1)
q_by_head = q.view(-1, self.q_size // self.head_size, self.head_size)
q_normed = vllm.ir.ops.rms_norm(q_by_head, q_weight, self.eps)
q_flat = q_normed.view(-1, self.q_size)
k_by_head = k.view(-1, self.k_size // self.head_size, self.head_size)
k_normed = vllm.ir.ops.rms_norm(k_by_head, k_weight, self.eps)
k_flat = k_normed.view(-1, self.k_size)
q_rope, k_rope = self.rope_matcher(positions, q_flat, k_flat, cos_sin_cache)
q_rope_fp8, q_scale_out = self._quantize_query(q_rope, q_scale)
k_rope = k_rope.view(-1, self.num_kv_heads, self.head_size)
v = v.view(-1, self.num_kv_heads, self.head_size_v)
dummy = torch.ops.vllm.unified_kv_cache_update(
k_rope, v, self._get_layer_name(layer_name)
)
if q_scale_out is None:
return dummy, q_rope_fp8, k_rope, v
return dummy, q_rope_fp8, k_rope, v, q_scale_out
def replacement_fp8_quant_query(
self,
qkv: torch.Tensor,
positions: torch.Tensor,
q_weight: torch.Tensor,
k_weight: torch.Tensor,
cos_sin_cache: torch.Tensor,
q_scale: torch.Tensor,
layer_name: LayerNameType | None = None,
) -> tuple[torch.Tensor, ...]:
q_out = torch.empty(
qkv.shape[0],
self.num_heads,
self.head_size,
device=qkv.device,
dtype=qkv.dtype,
)
k_out = torch.empty(
qkv.shape[0],
self.num_kv_heads,
self.head_size,
device=qkv.device,
dtype=qkv.dtype,
)
_, _, v = qkv.split([self.q_size, self.k_size, self.v_size], dim=-1)
v = v.view(qkv.shape[0], self.num_kv_heads, self.head_size_v)
results = auto_functionalized(
self.FUSED_OP,
q_out=q_out,
k_out=k_out,
qkv=qkv,
positions=positions,
q_weight=q_weight,
k_weight=k_weight,
rms_norm_eps=self.eps,
cos_sin_cache=cos_sin_cache,
is_neox=self.is_neox,
layer_name=self._get_layer_name(layer_name),
)
# Re-apply the same quant form on the kernel's bf16 q_out; the fused
# operation does not quantize Q.
q_fp8_flat = results[1].view(-1, self.q_size)
q_fp8, q_scale_out = self._quantize_query(q_fp8_flat, q_scale)
if q_scale_out is None:
return results[0], q_fp8, results[2], v
return results[0], q_fp8, results[2], v, q_scale_out
@staticmethod
def wrap_trace_fn(
trace_fn: Callable[P, fx.GraphModule],
*process_fx_fns: Callable[[fx.GraphModule], None],
) -> Callable[P, fx.GraphModule]:
def wrapped(*args: P.args, **kwargs: P.kwargs) -> fx.GraphModule:
gm = trace_fn(*args, **kwargs)
for process_fx in process_fx_fns:
process_fx(gm)
return gm
return wrapped
@staticmethod
def fx_view_to_reshape(gm: torch.fx.GraphModule) -> None:
from torch._inductor.fx_passes.post_grad import view_to_reshape
view_to_reshape(gm)
def _extra_check(self, match: pm.Match) -> bool:
return True
def _register(self, pattern, replacement, pm_pass) -> None:
trace_fn = QkNormRopeKvCachePattern.wrap_trace_fn(
pm.fwd_only,
QkNormRopeKvCachePattern.fx_view_to_reshape,
)
# Pre-build the search pattern with `ignore_types=(int, torch.SymInt)`
# and pass it via `search_fn_pattern=` so torch skips both of its
# internal `fx_to_pattern` calls and treats dynamic-shape SymInts as
# wildcards.
inputs = self.get_inputs()
argnames = [*inspect.signature(pattern).parameters.keys()]
search_gm = trace_fn(pattern, inputs)
search_fn_pattern = pm.fx_to_pattern(
search_gm,
ignore_types=(int, torch.SymInt),
argnames=argnames,
)
pm.register_replacement(
pattern,
replacement,
inputs,
trace_fn,
pm_pass,
extra_check=self._extra_check,
search_fn_pattern=search_fn_pattern,
)
def register(self, pm_pass: PatternMatcherPass) -> None:
# make_fx counts `self` in bound-method code params; wrap as plain fns.
if self.quant_query:
if _USE_LAYERNAME:
def pattern_q_with_layer(
qkv,
positions,
q_weight,
k_weight,
cos_sin_cache,
q_scale,
layer_name,
):
return self.pattern_fp8_quant_query(
qkv,
positions,
q_weight,
k_weight,
cos_sin_cache,
q_scale,
layer_name,
)
def replacement_q_with_layer(
qkv,
positions,
q_weight,
k_weight,
cos_sin_cache,
q_scale,
layer_name,
):
return self.replacement_fp8_quant_query(
qkv,
positions,
q_weight,
k_weight,
cos_sin_cache,
q_scale,
layer_name,
)
self._register(pattern_q_with_layer, replacement_q_with_layer, pm_pass)
else:
def pattern_q_without_layer(
qkv, positions, q_weight, k_weight, cos_sin_cache, q_scale
):
return self.pattern_fp8_quant_query(
qkv, positions, q_weight, k_weight, cos_sin_cache, q_scale
)
def replacement_q_without_layer(
qkv, positions, q_weight, k_weight, cos_sin_cache, q_scale
):
return self.replacement_fp8_quant_query(
qkv, positions, q_weight, k_weight, cos_sin_cache, q_scale
)
self._register(
pattern_q_without_layer, replacement_q_without_layer, pm_pass
)
else:
if _USE_LAYERNAME:
def pattern_noq_with_layer(
qkv,
positions,
q_weight,
k_weight,
cos_sin_cache,
layer_name,
):
return self.pattern_non_fp8_quant_query(
qkv,
positions,
q_weight,
k_weight,
cos_sin_cache,
layer_name,
)
def replacement_noq_with_layer(
qkv,
positions,
q_weight,
k_weight,
cos_sin_cache,
layer_name,
):
return self.replacement_non_fp8_quant_query(
qkv,
positions,
q_weight,
k_weight,
cos_sin_cache,
layer_name,
)
self._register(
pattern_noq_with_layer, replacement_noq_with_layer, pm_pass
)
else:
def pattern_noq_without_layer(
qkv, positions, q_weight, k_weight, cos_sin_cache
):
return self.pattern_non_fp8_quant_query(
qkv, positions, q_weight, k_weight, cos_sin_cache
)
def replacement_noq_without_layer(
qkv, positions, q_weight, k_weight, cos_sin_cache
):
return self.replacement_non_fp8_quant_query(
qkv, positions, q_weight, k_weight, cos_sin_cache
)
self._register(
pattern_noq_without_layer,
replacement_noq_without_layer,
pm_pass,
)