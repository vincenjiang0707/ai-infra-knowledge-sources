source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/attention/attention/
lastmod: 2026-09-23

class Attention(nn.Module, AttentionLayerBase):
"""Attention layer.
This class takes query, key, and value tensors as input. The input tensors
can either contain prompt tokens or generation tokens.
The class does the following:
1. Store the input key and value tensors in the KV cache.
2. Perform (multi-head/multi-query/grouped-query) attention.
3. Return the output tensor.
"""
def __init__(
self,
num_heads: int,
head_size: int,
scale: float,
num_kv_heads: int | None = None,
alibi_slopes: list[float] | None = None,
use_alibi_sqrt: bool | None = None,
cache_config: CacheConfig | None = None,
quant_config: QuantizationConfig | None = None,
logits_soft_cap: float | None = None,
per_layer_sliding_window: int | None = None,
prefix: str = "",
attn_type: str = AttentionType.DECODER,
kv_sharing_target_layer_name: str | None = None,
mm_prefix_clamp_sliding_window: bool = False,
attn_backend: type[AttentionBackend] | None = None,
head_size_v: int | None = None,
**extra_impl_args,
) -> None:
"""The KV cache is stored inside this class and is accessed via
`self.kv_cache`.
"""
super().__init__()
sliding_window: int | None
if per_layer_sliding_window is not None:
# per-layer sliding window
sliding_window = per_layer_sliding_window
elif cache_config is not None:
# model-level sliding window
sliding_window = cache_config.sliding_window
else:
sliding_window = None
vllm_config = get_current_vllm_config()
if cache_config is not None:
kv_cache_dtype = cache_config.cache_dtype
else:
kv_cache_dtype = "auto"
# llm-compressor models declare an FP8 KV-cache scheme in their
# checkpoint config. Honor it only when the user did not explicitly
# pick a kv_cache_dtype; an explicit choice (e.g. bfloat16) must win.
# The "auto" case is normally resolved upstream in
# resolve_kv_cache_dtype_string, but we re-apply here defensively in
# case anything bypassed that path.
kv_cache_scheme = getattr(quant_config, "kv_cache_scheme", None)
if kv_cache_scheme is not None and kv_cache_dtype == "auto":
kv_cache_dtype = "fp8"
if cache_config is not None:
cache_config.cache_dtype = "fp8"
# Check if per-head quant scales are required based on kv_cache_scheme
use_per_head_quant_scales = (
kv_cache_scheme is not None
and kv_cache_scheme.get("strategy") == "attn_head"
)
# Skip quantization for specified layers
if cache_config is not None and cache_config.kv_cache_dtype_skip_layers:
from vllm.model_executor.models.utils import extract_layer_index
skip = False
# Check attention type
if (
sliding_window is not None
and "sliding_window" in cache_config.kv_cache_dtype_skip_layers
):
skip = True
# Check layer index
layer_idx = extract_layer_index(prefix)
if str(layer_idx) in cache_config.kv_cache_dtype_skip_layers:
skip = True
if skip:
kv_cache_dtype = "auto"
logger.debug(
"Layer %s: kv_cache_dtype=%s, sliding_window=%s",
prefix,
kv_cache_dtype,
sliding_window,
)
self.kv_cache_torch_dtype = kv_cache_dtype_str_to_dtype(
kv_cache_dtype, vllm_config.model_config
)
self.kv_cache_dtype = kv_cache_dtype
if num_kv_heads is None:
num_kv_heads = num_heads
assert num_heads % num_kv_heads == 0, (
f"num_heads ({num_heads}) is not divisible by num_kv_heads ({num_kv_heads})"
)
self.quant_config = quant_config
self.layer_name = prefix
self.num_heads = num_heads
self.head_size = head_size
self.head_size_v = self.head_size if head_size_v is None else head_size_v
self.num_kv_heads = num_kv_heads
self.sliding_window = sliding_window
self.has_sink = extra_impl_args.get("sinks") is not None
# NOTE: model_config may be None during certain tests
model_config = vllm_config.model_config
self.use_mm_prefix = model_config is not None and model_config.is_mm_prefix_lm
# During model initialization, the default dtype is set as the model
# weight and activation dtype.
dtype = torch.get_default_dtype()
if attn_backend is None:
self.attn_backend = get_attn_backend(
head_size,
dtype,
kv_cache_dtype,
use_mla=False,
has_sink=self.has_sink,
use_mm_prefix=self.use_mm_prefix,
use_per_head_quant_scales=use_per_head_quant_scales,
attn_type=attn_type,
has_sliding_window=sliding_window is not None,
)
else:
self.attn_backend = attn_backend
backend_supports_alibi_sqrt = self.attn_backend.supports_alibi_sqrt()
use_alibi_sqrt = use_alibi_sqrt if use_alibi_sqrt else False
if use_alibi_sqrt and not backend_supports_alibi_sqrt:
raise ValueError(
f"use_alibi_sqrt is not supported by backend "
f"{self.attn_backend.get_name()}."
)
self.use_alibi_sqrt = bool(use_alibi_sqrt)
if backend_supports_alibi_sqrt:
extra_impl_args["use_alibi_sqrt"] = self.use_alibi_sqrt
# prefix caching + batch invariance is currently not supported for
# FLASHINFER and TRITON_MLA.
if (
cache_config is not None
and cache_config.enable_prefix_caching
and envs.VLLM_BATCH_INVARIANT
and (
self.attn_backend.get_name() == "FLASHINFER"
or self.attn_backend.get_name() == "TRITON_MLA"
)
):
logger.warning_once(
"Disabling prefix caching for FLASHINFER/TRITON_MLA "
"with batch invariance, as it is not yet supported.",
)
cache_config.enable_prefix_caching = False
if extra_impl_args.get("chunk_lookback", -1) > -1:
assert self.attn_backend.get_name() == "TRITON_ATTN", (
f"Chunked attention with lookback requires the Triton backend, "
f"but got {self.attn_backend.get_name()}."
)
if self.attn_backend.get_name() == "FLEX_ATTENTION":
block_m = vllm_config.attention_config.flex_attn_block_m
block_n = vllm_config.attention_config.flex_attn_block_n
if envs.VLLM_BATCH_INVARIANT and cache_config is not None:
if block_m is not None and block_m > cache_config.block_size:
raise ValueError(
f"flex_attn_block_m ({block_m}) must be "
f"<= cache block size ({cache_config.block_size}) for "
f"batch invariance"
)
if block_n is not None and block_n > cache_config.block_size:
raise ValueError(
f"flex_attn_block_n ({block_n}) must be "
f"<= cache block size ({cache_config.block_size}) for "
f"batch invariance"
)
if block_m is not None:
extra_impl_args.setdefault("block_m", block_m)
if block_n is not None:
extra_impl_args.setdefault("block_n", block_n)
impl_cls = self.attn_backend.get_impl_cls()
self.impl = impl_cls( # type: ignore[assignment] # impl_cls always returns an AttentionImpl subclass
num_heads,
head_size,
scale,
num_kv_heads,
alibi_slopes,
sliding_window,
kv_cache_dtype,
logits_soft_cap,
attn_type,
kv_sharing_target_layer_name,
**extra_impl_args,
)
self.backend = AttentionBackendEnum[self.attn_backend.get_name()]
self.dtype = dtype
# For cuda-alike (CUDA and ROCM) and cpu platforms, we control how
# torch.compile works by registering the attention as one giant
# opaque custom op. For other platforms, we directly call them
# and let torch.compile handle them.
self.use_direct_call = not current_platform.opaque_attention_op()
compilation_config = vllm_config.compilation_config
if prefix in compilation_config.static_forward_context:
raise ValueError(f"Duplicate layer name: {prefix}")
compilation_config.static_forward_context[prefix] = self
self.attn_type = attn_type
if kv_sharing_target_layer_name is not None:
validate_kv_sharing_target(
prefix,
kv_sharing_target_layer_name,
compilation_config.static_forward_context,
)
self.kv_sharing_target_layer_name = kv_sharing_target_layer_name
# Gemma4: clamp mm_prefix bidirectional ranges by the sliding window
# (read by the Triton backend impl). Default False for all other models.
self.mm_prefix_clamp_sliding_window = mm_prefix_clamp_sliding_window
# use a placeholder kv cache tensor during init, which will be replaced
# by bind_kv_cache
# this variable will not be accessed if use_direct_call is True
self.kv_cache = torch.tensor([])
# Initialize KV cache quantization attributes
_init_kv_cache_quant(self, quant_config, prefix)
# for attn backends supporting query quantization
self.query_quant = None
if (
self.impl.supports_quant_query_input
and (
self.kv_cache_dtype.startswith("fp8")
or self.kv_cache_dtype.startswith("nvfp4")
)
and not self.kv_cache_dtype.endswith("per_token_head")
):
is_per_head = (
hasattr(self, "q_scale") and self.q_scale.numel() == self.num_kv_heads
)
block_size = self.head_size * self.num_heads // self.num_kv_heads
self.query_quant = QuantFP8(
static=True,
group_shape=GroupShape(-1, block_size)
if is_per_head
else GroupShape.PER_TENSOR,
)
def forward(
self,
query: torch.Tensor,
key: torch.Tensor,
value: torch.Tensor,
# For some alternate attention backends like MLA the attention output
# shape does not match the query shape, so we optionally let the model
# definition specify the output tensor shape.
output_shape: torch.Size | None = None,
output_dtype: torch.dtype | None = None,
) -> torch.Tensor:
"""The KV cache is stored inside this class and is accessed via
`self.kv_cache`.
Attention metadata (`attn_metadata`) is set using a context manager in
the model runner's `execute_model` method. It is accessed via forward
context using
`vllm.forward_context.get_forward_context().attn_metadata`.
"""
if output_dtype is None:
output_dtype = query.dtype
if self.query_quant is not None:
# quantizing with a simple torch operation enables
# torch.compile to fuse this into previous ops
# which reduces overheads during decoding.
# Otherwise queries are quantized using custom ops
# which causes decoding overheads
assert self.kv_cache_dtype in {"fp8", "fp8_e4m3"} or (
self.kv_cache_dtype.startswith("nvfp4")
)
# check if query quantization is supported
if self.impl.supports_quant_query_input:
query, _ = self.query_quant(query, self._q_scale)
if output_shape is None:
# Handle both 2D [num_tokens, hidden] and
# 3D [num_tokens, heads, head_dim] query
num_tokens = query.shape[0]
output_shape = torch.Size((num_tokens, self.num_heads * self.head_size_v))
output = torch.empty(output_shape, dtype=output_dtype, device=query.device)
hidden_size = output_shape[-1]
# Reshape the query, key, and value tensors.
# NOTE(woosuk): We do this outside the custom op to minimize the
# CPU overheads from the non-CUDA-graph regions.
query = query.view(-1, self.num_heads, self.head_size)
output = output.view(-1, self.num_heads, self.head_size_v)
if key is not None:
key = key.view(-1, self.num_kv_heads, self.head_size)
if value is not None:
value = value.view(-1, self.num_kv_heads, self.head_size_v)
kv_cache_dummy_dep = None
if self.use_direct_call:
# Skip this if sharing KV cache with an earlier attention layer.
if (
not self.attn_backend.forward_includes_kv_cache_update
and self.kv_sharing_target_layer_name is None
and key is not None
and value is not None
):
kv_cache_dummy_dep = unified_kv_cache_update(
key, value, self.layer_name
)
unified_attention_with_output(
query,
key,
value,
output,
self.layer_name,
kv_cache_dummy_dep=kv_cache_dummy_dep,
)
else:
# Skip this if sharing KV cache with an earlier attention layer.
encoded = _encode_layer_name(self.layer_name)
if (
not self.attn_backend.forward_includes_kv_cache_update
and self.kv_sharing_target_layer_name is None
and key is not None
and value is not None
):
kv_cache_dummy_dep = torch.ops.vllm.unified_kv_cache_update(
key, value, encoded
)
torch.ops.vllm.unified_attention_with_output(
query,
key,
value,
output,
encoded,
kv_cache_dummy_dep=kv_cache_dummy_dep,
)
return output.view(-1, hidden_size)
def extra_repr(self) -> str:
s = f"head_size={self.impl.head_size}" # type: ignore
s += f", num_heads={self.impl.num_heads}" # type: ignore
s += f", num_kv_heads={self.impl.num_kv_heads}" # type: ignore
s += f", scale={self.impl.scale}" # type: ignore
s += f", backend={self.impl.__class__.__name__}"
return s
def process_weights_after_loading(self, act_dtype: torch.dtype):
self.impl.process_weights_after_loading(act_dtype)
# If we should not load quant weights, we initialize the scales to 1.0
# as the default value. See [Note: Register q/k/v/prob scales in state dict]
# for more details.
quant_method = (
resolve_quant_method(self.quant_config, self, prefix=self.layer_name)
if self.quant_config
else None
)
if not should_load_quant_weights(quant_method):
set_default_quant_scales(self, register_buffer=False)
def get_attn_backend(self) -> type[AttentionBackend]:
return self.attn_backend
def get_kv_cache_spec(self, vllm_config: VllmConfig) -> KVCacheSpec | None:
# Block size may get updated after model loading, refresh it
block_size = vllm_config.cache_config.block_size
# Encoder-only attention is prefill-only and keeps no autoregressive KV
# cache. In hybrid models (e.g. Qwen3.5 / ColQwen3.5: GatedDeltaNet
# linear_attention interleaved with full_attention) the runner iterates
# every attention module to build the KV-cache spec, so an ENCODER_ONLY
# full_attention layer reaches here; it contributes no KV cache group.
if self.attn_type in (AttentionType.ENCODER_ONLY, AttentionType.ENCODER):
return None
# Should not be called for enc-dec attention.
assert self.attn_type == AttentionType.DECODER
quant_mode = get_kv_quant_mode(self.kv_cache_dtype)
if self.sliding_window is not None:
assert not self.attn_backend.is_mla(), (
"MLA is not supported for sliding window"
)
# SW chooses its own block_size, decoupled from the user's
# ``--block-size`` (which only constrains primary attention).
# When this SW layer is a padded spec (skip-quant: its page is
# padded up to ``skip_page_size_padded``), pick the largest kernel
# block that still fits the shared page so we waste fewer padding
# bytes per block. Otherwise (page_size_padded is None) take the
# primary block size when the backend can run it unsplit: if this
# page does not divide the primary page, ``unify`` then pads it
# (padded pages cannot be split) instead of scaling a small block
# to a size coprime with the primary one, which inflates the
# scheduler LCM (e.g. a 1024 B/token SWA draft next to a 1152
# B/token MLA target: 1728 vs 1536 gives LCM 13824). Backends that
# cannot run the primary block start from their smallest block and
# ``unify`` scales it up by an integer ratio.
shared_page = vllm_config.cache_config.skip_page_size_padded
# The backend owns its packing
sw_per_token = self.attn_backend.customize_spec(
SlidingWindowSpec(
block_size=1,
num_kv_heads=self.num_kv_heads,
head_size=self.head_size,
head_size_v=self.head_size_v,
dtype=self.kv_cache_torch_dtype,
kv_quant_mode=quant_mode,
sliding_window=self.sliding_window,
)
).real_page_size_bytes
page_budget = shared_page or sw_per_token * block_size
sw_block_size = _largest_kernel_block_within(
self.attn_backend, sw_per_token, page_budget, block_size
)
return SlidingWindowSpec(
block_size=sw_block_size,
num_kv_heads=self.num_kv_heads,
head_size=self.head_size,
head_size_v=self.head_size_v,
dtype=self.kv_cache_torch_dtype,
kv_quant_mode=quant_mode,
sliding_window=self.sliding_window,
page_size_padded=shared_page,
)
else:
return FullAttentionSpec(
block_size=block_size,
num_kv_heads=self.num_kv_heads,
head_size=self.head_size,
head_size_v=self.head_size_v,
dtype=self.kv_cache_torch_dtype,
kv_quant_mode=quant_mode,
)