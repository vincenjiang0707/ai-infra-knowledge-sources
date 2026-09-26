source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/mhc/
lastmod: 2026-09-24

@CustomOp.register("mhc_fused_post_pre")
class MHCFusedPostPreOp(CustomOp):
"""Fused MHC post block followed by the next MHC pre block.
Equivalent to applying MHCPostOp and then MHCPreOp to the updated
residual streams, returning residual_cur, post_mix_cur, comb_mix_cur,
and layer_input_cur.
"""
# --8<-- [end:mhc_fused_post_pre]
@classmethod
def enabled(cls) -> bool:
return True
def forward_cuda(
self,
x: torch.Tensor,
residual: torch.Tensor,
post_layer_mix: torch.Tensor,
comb_res_mix: torch.Tensor,
fn: torch.Tensor,
hc_scale: torch.Tensor,
hc_base: torch.Tensor,
rms_eps: float,
hc_pre_eps: float,
hc_sinkhorn_eps: float,
hc_post_mult_value: float,
sinkhorn_repeat: int,
n_splits: int = 1,
tile_n: int = 1,
norm_weight: torch.Tensor | None = None,
norm_eps: float = 0.0,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
return torch.ops.vllm.mhc_fused_post_pre_tilelang(
x,
residual,
post_layer_mix,
comb_res_mix,
fn,
hc_scale,
hc_base,
rms_eps,
hc_pre_eps,
hc_sinkhorn_eps,
hc_post_mult_value,
sinkhorn_repeat,
n_splits,
tile_n,
norm_weight,
norm_eps,
)
def forward_hip(
self,
x: torch.Tensor,
residual: torch.Tensor,
post_layer_mix: torch.Tensor,
comb_res_mix: torch.Tensor,
fn: torch.Tensor,
hc_scale: torch.Tensor,
hc_base: torch.Tensor,
rms_eps: float,
hc_pre_eps: float,
hc_sinkhorn_eps: float,
hc_post_mult_value: float,
sinkhorn_repeat: int,
n_splits: int = 1,
tile_n: int = 1,
norm_weight: torch.Tensor | None = None,
norm_eps: float = 0.0,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
if HAS_AITER_MHC_FUSED and _aiter_mhc_supported(
residual,
norm_weight,
supports_norm=HAS_AITER_MHC_FUSED_NORM,
):
return torch.ops.vllm.mhc_fused_post_pre_aiter(
x,
residual,
post_layer_mix,
comb_res_mix,
fn,
hc_scale,
hc_base,
rms_eps,
hc_pre_eps,
hc_sinkhorn_eps,
hc_post_mult_value,
sinkhorn_repeat,
n_splits,
tile_n,
norm_weight,
norm_eps,
)
if HAS_TILELANG_MHC:
return torch.ops.vllm.mhc_fused_post_pre_tilelang(
x,
residual,
post_layer_mix,
comb_res_mix,
fn,
hc_scale,
hc_base,
rms_eps,
hc_pre_eps,
hc_sinkhorn_eps,
hc_post_mult_value,
sinkhorn_repeat,
n_splits,
tile_n,
norm_weight,
norm_eps,
)
residual_cur, post_mix_cur, comb_mix_cur, layer_input_cur = self.forward_native(
x,
residual,
post_layer_mix,
comb_res_mix,
fn,
hc_scale,
hc_base,
rms_eps,
hc_pre_eps,
hc_sinkhorn_eps,
hc_post_mult_value,
sinkhorn_repeat,
n_splits,
tile_n,
norm_weight,
norm_eps,
)
return (
residual_cur,
post_mix_cur,
comb_mix_cur,
_apply_mhc_norm(layer_input_cur, norm_weight, norm_eps),
)
def forward_native(
self,
x: torch.Tensor,
residual: torch.Tensor,
post_layer_mix: torch.Tensor,
comb_res_mix: torch.Tensor,
fn: torch.Tensor,
hc_scale: torch.Tensor,
hc_base: torch.Tensor,
rms_eps: float,
hc_pre_eps: float,
hc_sinkhorn_eps: float,
hc_post_mult_value: float,
sinkhorn_repeat: int,
n_splits: int = 1,
tile_n: int = 1,
norm_weight: torch.Tensor | None = None,
norm_eps: float = 0.0,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
# Decompose into post + pre (no fused kernel available).
residual_cur = mhc_kernels.mhc_post_torch(
x, residual, post_layer_mix, comb_res_mix
)
post_mix_cur, comb_mix_cur, layer_input_cur = mhc_kernels.mhc_pre_torch(
residual_cur,
fn,
hc_scale,
hc_base,
rms_eps,
hc_pre_eps,
hc_sinkhorn_eps,
hc_post_mult_value,
sinkhorn_repeat,
)
return residual_cur, post_mix_cur, comb_mix_cur, layer_input_cur
def forward_xpu(
self,
x: torch.Tensor,
residual: torch.Tensor,
post_layer_mix: torch.Tensor,
comb_res_mix: torch.Tensor,
fn: torch.Tensor,
hc_scale: torch.Tensor,
hc_base: torch.Tensor,
rms_eps: float,
hc_pre_eps: float,
hc_sinkhorn_eps: float,
hc_post_mult_value: float,
sinkhorn_repeat: int,
n_splits: int = 1,
tile_n: int = 1,
norm_weight: torch.Tensor | None = None,
norm_eps: float = 0.0,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
return torch.ops._xpu_C.mhc_fused_post_pre(
x,
residual,
post_layer_mix,
comb_res_mix,
fn,
hc_scale,
hc_base,
rms_eps,
hc_pre_eps,
hc_sinkhorn_eps,
hc_post_mult_value,
sinkhorn_repeat,
)
def forward_cpu(
self,
x: torch.Tensor,
residual: torch.Tensor,
post_layer_mix: torch.Tensor,
comb_res_mix: torch.Tensor,
fn: torch.Tensor,
hc_scale: torch.Tensor,
hc_base: torch.Tensor,
rms_eps: float,
hc_pre_eps: float,
hc_sinkhorn_eps: float,
hc_post_mult_value: float,
sinkhorn_repeat: int,
n_splits: int = 1,
tile_n: int = 1,
norm_weight: torch.Tensor | None = None,
norm_eps: float = 0.0,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
# Decompose into post + pre (no fused kernel available).
residual_cur = mhc_kernels.mhc_post_cpu(
x, residual, post_layer_mix, comb_res_mix
)
post_mix_cur, comb_mix_cur, layer_input_cur = mhc_kernels.mhc_pre_cpu(
residual_cur,
fn,
hc_scale,
hc_base,
rms_eps,
hc_pre_eps,
hc_sinkhorn_eps,
hc_post_mult_value,
sinkhorn_repeat,
)
return residual_cur, post_mix_cur, comb_mix_cur, layer_input_cur