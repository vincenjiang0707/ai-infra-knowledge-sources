source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/mamba/ops/gather_initial_states/
lastmod: 2026-09-23

def gather_initial_states(
state: torch.Tensor,
indices: torch.Tensor,
has_initial_state: torch.Tensor,
) -> torch.Tensor:
"""Gather dense state rows, replacing uninitialized rows with zeros."""
assert state.ndim >= 2
assert state.is_cuda or state.is_xpu
assert indices.ndim == 1 and has_initial_state.ndim == 1
assert indices.shape == has_initial_state.shape
assert indices.device == state.device
assert has_initial_state.device == state.device
assert indices.dtype in (torch.int32, torch.int64)
assert has_initial_state.dtype == torch.bool
row_size = state[0].numel()
# Mamba pages may pad stride(0), but each state row remains dense.
assert state[0].is_contiguous()
output = torch.empty(
(indices.numel(), *state.shape[1:]),
dtype=state.dtype,
device=state.device,
)
block_size = min(triton.next_power_of_2(row_size), 1024)
grid = (triton.cdiv(row_size, block_size), indices.numel())
_gather_initial_states_kernel[grid](
state,
indices,
has_initial_state,
output,
state.stride(0),
indices.stride(0),
has_initial_state.stride(0),
row_size=row_size,
BLOCK_SIZE=block_size,
num_warps=8,
launch_pdl=current_platform.is_arch_support_pdl(),
)
return output