source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/mamba/ops/selective_state_update_replayssm_output_only/
lastmod: 2026-09-23

def selective_state_update_replayssm_output_only(
state: torch.Tensor,
x: torch.Tensor,
dt: torch.Tensor,
A: torch.Tensor,
B: torch.Tensor,
C: torch.Tensor,
D: torch.Tensor | None = None,
dt_bias: torch.Tensor | None = None,
z: torch.Tensor | None = None,
dt_softplus: bool = False,
x_cache: torch.Tensor | None = None,
dt_cache: torch.Tensor | None = None,
B_cache: torch.Tensor | None = None,
bc_pre: torch.Tensor | None = None,
write_pos: torch.Tensor | None = None,
is_flush: torch.Tensor | None = None,
max_cache_len: int = 16,
state_batch_indices: torch.Tensor | None = None,
null_block_id: int = NULL_BLOCK_ID,
out: torch.Tensor | None = None,
enable_stochastic_rounding: bool = False,
cache_philox_rounds: int = 0,
) -> torch.Tensor:
"""Cached-bc SSM update for vLLM's autoregressive Mamba2 decode path."""
has_heads = state.dim() > 3
if state.dim() == 3:
state = state.unsqueeze(1)
if x.dim() == 2:
x = x.unsqueeze(1)
if dt.dim() == 2:
dt = dt.unsqueeze(1)
if A.dim() == 2:
A = A.unsqueeze(0)
if B.dim() == 2:
B = B.unsqueeze(1)
if C.dim() == 2:
C = C.unsqueeze(1)
if D is not None and D.dim() == 1:
D = D.unsqueeze(0)
if z is not None and z.dim() == 2:
z = z.unsqueeze(1)
if dt_bias is not None and dt_bias.dim() == 1:
dt_bias = dt_bias.unsqueeze(0)
if out is not None and out.dim() == 2:
out = out.unsqueeze(1)
if state_batch_indices is not None and state_batch_indices.dim() == 1:
state_batch_indices = state_batch_indices.unsqueeze(1)
_, nheads, dim, dstate = state.shape
batch = x.shape[0]
assert x.shape == (batch, nheads, dim)
assert dt.shape == x.shape
assert A.shape == (nheads, dim, dstate)
ngroups = B.shape[1]
assert nheads % ngroups == 0, "nheads must be divisible by ngroups"
assert B.shape == (batch, ngroups, dstate)
assert C.shape == B.shape
if D is not None:
assert D.shape == (nheads, dim)
if z is not None:
assert z.shape == x.shape
if dt_bias is not None:
assert dt_bias.shape == (nheads, dim)
assert out is not None and out.shape == x.shape
assert A.stride(-1) == 0 and A.stride(-2) == 0, (
"Cached kernel requires TIE_HDIM (A scalar per head)"
)
assert dt.stride(-1) == 0, "Cached kernel requires TIE_HDIM (dt scalar per head)"
if dt_bias is not None:
assert dt_bias.stride(-1) == 0, (
"Cached kernel requires TIE_HDIM (dt_bias scalar per head)"
)
assert x_cache is not None
assert dt_cache is not None
assert B_cache is not None
assert x_cache.shape[1:] == (nheads, max_cache_len, dim)
assert dt_cache.shape[1:] == (nheads, max_cache_len)
assert B_cache.shape[1:] == (ngroups, max_cache_len, dstate)
assert write_pos is not None and write_pos.shape[0] >= batch
assert write_pos.dtype == torch.int32
assert is_flush is not None and is_flush.shape[0] >= batch
assert is_flush.dtype in (torch.bool, torch.int8)
assert bc_pre is not None
assert bc_pre.shape[0] >= batch and bc_pre.shape[1] >= ngroups
assert bc_pre.shape[2] == max_cache_len
assert bc_pre.dtype == torch.float32
if state_batch_indices is not None:
assert state_batch_indices.shape[0] >= batch
assert state_batch_indices.shape[1] >= 1
block_size_k_cache = max(1, triton.next_power_of_2(max_cache_len))
block_size_k_dot = max(16, block_size_k_cache)
block_size_m, num_warps, nf_tile, fl_tile, num_stages = get_replayssm_config(
"mamba2_output_only", dstate=dstate, L=max_cache_len
)
bs_dstate = triton.next_power_of_2(dstate)
nf_dstate_tile = max(16, min(nf_tile, bs_dstate))
nf_nds = triton.cdiv(bs_dstate, nf_dstate_tile)
fl_dstate_tile = max(16, min(fl_tile, bs_dstate))
fl_nds = triton.cdiv(bs_dstate, fl_dstate_tile)
# AMD Triton does not support tf32x3, so use its backend default. CUDA
# retains tf32x3 to preserve fp32 parity with the elementwise baseline.
dot_input_precision = None if current_platform.is_rocm() else "tf32x3"
grid = lambda META: (triton.cdiv(dim, META["BLOCK_SIZE_M"]), batch, nheads)
z_strides = (z.stride(0), z.stride(1), z.stride(2)) if z is not None else (0, 0, 0)
state_indices_strides = (
(state_batch_indices.stride(0), state_batch_indices.stride(1))
if state_batch_indices is not None
else (0, 0)
)
rand_seed = (
torch.randint(0, 2**32, (1,), device=state.device)
if enable_stochastic_rounding
else None
)
with torch.accelerator.device_index(x.device.index):
# Both kernels always launch: the precompute kernel self-skips flush
# rows per row (the branch can't be hoisted out under CUDA graphs), so
# it is a no-op when every row is flushing.
_replayssm_output_only_precompute_kernel[(batch, ngroups)](
B,
C,
B_cache,
write_pos,
is_flush,
bc_pre,
state_batch_indices,
null_block_id,
batch,
ngroups,
dstate,
B.stride(0),
B.stride(1),
B.stride(2),
C.stride(0),
C.stride(1),
C.stride(2),
B_cache.stride(0),
B_cache.stride(1),
B_cache.stride(2),
B_cache.stride(3),
bc_pre.stride(0),
bc_pre.stride(1),
bc_pre.stride(2),
state_indices_strides[0],
state_indices_strides[1],
max_cache_len,
block_size_k_cache,
num_warps=2,
)
_replayssm_output_only_kernel[grid](
state,
rand_seed,
x,
dt,
dt_bias,
A,
B,
C,
D,
z,
out,
x_cache,
dt_cache,
B_cache,
bc_pre,
write_pos,
is_flush,
state_batch_indices,
null_block_id,
batch,
nheads,
dim,
dstate,
nheads // ngroups,
state.stride(0),
state.stride(1),
state.stride(2),
state.stride(3),
x.stride(0),
x.stride(1),
x.stride(2),
dt.stride(0),
dt.stride(1),
dt_bias.stride(0) if dt_bias is not None else 0,
A.stride(0),
B.stride(0),
B.stride(1),
B.stride(2),
C.stride(0),
C.stride(1),
C.stride(2),
D.stride(0) if D is not None else 0,
D.stride(1) if D is not None else 0,
z_strides[0],
z_strides[1],
z_strides[2],
out.stride(0),
out.stride(1),
out.stride(2),
x_cache.stride(0),
x_cache.stride(1),
x_cache.stride(3),
x_cache.stride(2),
dt_cache.stride(0),
dt_cache.stride(1),
dt_cache.stride(2),
B_cache.stride(0),
B_cache.stride(1),
B_cache.stride(2),
B_cache.stride(3),
bc_pre.stride(0),
bc_pre.stride(1),
bc_pre.stride(2),
state_indices_strides[0],
state_indices_strides[1],
dt_softplus,
max_cache_len,
block_size_m,
block_size_k_cache,
block_size_k_dot,
nf_dstate_tile,
nf_nds,
fl_dstate_tile,
fl_nds,
dot_input_precision,
enable_stochastic_rounding,
cache_philox_rounds,
num_warps=num_warps,
num_stages=num_stages,
)
if not has_heads:
out = out.squeeze(1)
return out