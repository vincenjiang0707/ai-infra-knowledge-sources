source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/amd/model/
lastmod: 2026-09-24

class DeepseekV4DecoderLayer(nn.Module):
def __init__(
self,
vllm_config,
prefix,
topk_indices_buffer: torch.Tensor | None = None,
aux_stream_list: list[torch.cuda.Stream] | None = None,
fuse_heterogeneous_shared_expert: bool = False,
):
super().__init__()
# Lazy import to avoid top-level tilelang dependency.
# Registers both torch.ops.vllm.mhc_pre and mhc_post
import vllm.model_executor.layers.mhc # noqa: F401
config = vllm_config.model_config.hf_config
self.hidden_size = config.hidden_size
self.rms_norm_eps = config.rms_norm_eps
self.attn = DeepseekV4ROCMAiterMLAAttention(
vllm_config,
prefix=f"{prefix}.attn",
topk_indices_buffer=topk_indices_buffer,
aux_stream_list=aux_stream_list,
)
self.ffn = DeepseekV4MoE(
vllm_config,
prefix=f"{prefix}.ffn",
fuse_heterogeneous_shared_expert=fuse_heterogeneous_shared_expert,
)
self.attn_norm = RMSNorm(self.hidden_size, self.rms_norm_eps)
self.ffn_norm = RMSNorm(self.hidden_size, self.rms_norm_eps)
self.hc_mult = config.hc_mult
self.hc_sinkhorn_iters = config.hc_sinkhorn_iters
self.hc_eps = config.hc_eps
self.hc_post_alpha = 2.0
mix_hc = (2 + self.hc_mult) * self.hc_mult
hc_dim = self.hc_mult * self.hidden_size
self.hc_attn_fn = nn.Parameter(
torch.empty(
(mix_hc, hc_dim),
dtype=torch.float32,
),
requires_grad=False,
)
self.hc_ffn_fn = nn.Parameter(
torch.empty(
(mix_hc, hc_dim),
dtype=torch.float32,
),
requires_grad=False,
)
self.hc_attn_base = nn.Parameter(
torch.empty(
mix_hc,
dtype=torch.float32,
),
requires_grad=False,
)
self.hc_ffn_base = nn.Parameter(
torch.empty(
mix_hc,
dtype=torch.float32,
),
requires_grad=False,
)
self.hc_attn_scale = nn.Parameter(
torch.empty(
3,
dtype=torch.float32,
),
requires_grad=False,
)
self.hc_ffn_scale = nn.Parameter(
torch.empty(
3,
dtype=torch.float32,
),
requires_grad=False,
)
self.mhc_pre = MHCPreOp()
self.mhc_post = MHCPostOp()
self.mhc_fused_post_pre = MHCFusedPostPreOp()
# AITER mhc kernels (pre/post/fused) require hc_mult == 4.
use_aiter_mhc = (
HAS_AITER_MHC and self.hidden_size % 256 == 0 and self.hc_mult == 4
)
# Prefer AITER fused post+pre when eligible; otherwise TileLang.
self.use_fused_mhc = use_aiter_mhc or HAS_TILELANG_MHC
# Fold attn/ffn RMSNorm into MHC only when the active backend's
# fused-rmsnorm path supports this hidden size.
if use_aiter_mhc:
self.fuse_mhc_rmsnorm = self.hidden_size in _AITER_MHC_FUSED_RMSNORM_SIZES
else:
self.fuse_mhc_rmsnorm = HAS_TILELANG_MHC and self.use_fused_mhc
def hc_pre(
self,
x: torch.Tensor,
hc_fn: torch.Tensor,
hc_scale: torch.Tensor,
hc_base: torch.Tensor,
norm_weight: torch.Tensor | None = None,
norm_eps: float = 0.0,
):
"""Reduce HC residual streams to the next sub-layer input.
When ``norm_weight`` is set, RMSNorm is fused into the pre kernel.
"""
post_mix, res_mix, layer_input = self.mhc_pre(
residual=x,
fn=hc_fn,
hc_scale=hc_scale,
hc_base=hc_base,
rms_eps=self.rms_norm_eps,
hc_pre_eps=self.hc_eps,
hc_sinkhorn_eps=self.hc_eps,
hc_post_mult_value=self.hc_post_alpha,
sinkhorn_repeat=self.hc_sinkhorn_iters,
norm_weight=norm_weight,
norm_eps=norm_eps,
)
return layer_input, post_mix, res_mix
def hc_post(
self,
x: torch.Tensor,
residual: torch.Tensor,
post: torch.Tensor,
comb: torch.Tensor,
):
return self.mhc_post(x, residual, post, comb)
def _forward_fused_post_pre(
self,
x: torch.Tensor,
positions: torch.Tensor,
input_ids: torch.Tensor | None,
post_mix: torch.Tensor | None = None,
res_mix: torch.Tensor | None = None,
residual: torch.Tensor | None = None,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
attn_norm_weight = self.attn_norm.weight if self.fuse_mhc_rmsnorm else None
attn_norm_eps = (
self.attn_norm.variance_epsilon if self.fuse_mhc_rmsnorm else 0.0
)
if residual is None:
# Run standalone hc_pre on first layer
residual = x
x, post_mix, res_mix = self.hc_pre(
x,
self.hc_attn_fn,
self.hc_attn_scale,
self.hc_attn_base,
norm_weight=attn_norm_weight,
norm_eps=attn_norm_eps,
)
else:
residual, post_mix, res_mix, x = self.mhc_fused_post_pre(
x,
residual,
post_mix,
res_mix,
self.hc_attn_fn,
self.hc_attn_scale,
self.hc_attn_base,
self.rms_norm_eps,
self.hc_eps,
self.hc_eps,
self.hc_post_alpha,
self.hc_sinkhorn_iters,
norm_weight=attn_norm_weight,
norm_eps=attn_norm_eps,
)
if not self.fuse_mhc_rmsnorm:
x = self.attn_norm(x)
x = self.attn(positions, x, None)
ffn_norm_weight = self.ffn_norm.weight if self.fuse_mhc_rmsnorm else None
ffn_norm_eps = self.ffn_norm.variance_epsilon if self.fuse_mhc_rmsnorm else 0.0
residual, post_mix, res_mix, x = self.mhc_fused_post_pre(
x,
residual,
post_mix,
res_mix,
self.hc_ffn_fn,
self.hc_ffn_scale,
self.hc_ffn_base,
self.rms_norm_eps,
self.hc_eps,
self.hc_eps,
self.hc_post_alpha,
self.hc_sinkhorn_iters,
norm_weight=ffn_norm_weight,
norm_eps=ffn_norm_eps,
)
if not self.fuse_mhc_rmsnorm:
x = self.ffn_norm(x)
x = self.ffn(x, input_ids)
return x, residual, post_mix, res_mix
def _forward_unfused_post_pre(
self,
x: torch.Tensor,
positions: torch.Tensor,
input_ids: torch.Tensor | None,
post_mix: torch.Tensor | None = None,
res_mix: torch.Tensor | None = None,
residual: torch.Tensor | None = None,
) -> tuple[
torch.Tensor, torch.Tensor | None, torch.Tensor | None, torch.Tensor | None
]:
residual = x
x, post, comb = self.hc_pre(
x, self.hc_attn_fn, self.hc_attn_scale, self.hc_attn_base
)
x = self.attn_norm(x)
x = self.attn(positions, x, None)
x = self.hc_post(x, residual, post, comb)
residual = x
x, post, comb = self.hc_pre(
x, self.hc_ffn_fn, self.hc_ffn_scale, self.hc_ffn_base
)
x = self.ffn_norm(x)
x = self.ffn(x, input_ids)
x = self.hc_post(x, residual, post, comb)
return x, None, None, None
def forward(
self,
x: torch.Tensor,
positions: torch.Tensor,
input_ids: torch.Tensor | None,
post_mix: torch.Tensor | None = None,
res_mix: torch.Tensor | None = None,
residual: torch.Tensor | None = None,
) -> tuple[
torch.Tensor, torch.Tensor | None, torch.Tensor | None, torch.Tensor | None
]:
if not self.use_fused_mhc:
return self._forward_unfused_post_pre(
x, positions, input_ids, post_mix, res_mix, residual
)
return self._forward_fused_post_pre(
x, positions, input_ids, post_mix, res_mix, residual
)