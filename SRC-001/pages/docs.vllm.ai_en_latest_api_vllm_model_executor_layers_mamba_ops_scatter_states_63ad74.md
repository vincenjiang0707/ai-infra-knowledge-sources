source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/mamba/ops/scatter_states/
lastmod: 2026-09-23

Scatter `src`

rows into `state`

at `indices`

(in place).

Equivalent to `state[indices] = src`

but non-atomic and bandwidth-bound, since mamba cache slots are unique per sequence. `gather_initial_states`

is the read-side counterpart.

## Source code in `vllm/model_executor/layers/mamba/ops/scatter_states.py`


| @triton_kernel_dispatcher_with_warmup(
kernel=_scatter_states_kernel,
warmup_inputs=_scatter_states_warmup_inputs,
)
def scatter_states(
state: torch.Tensor,
src: torch.Tensor,
indices: torch.Tensor,
) -> DispatchSpec:
"""Scatter ``src`` rows into ``state`` at ``indices`` (in place).
Equivalent to ``state[indices] = src`` but non-atomic and bandwidth-bound,
since mamba cache slots are unique per sequence. ``gather_initial_states``
is the read-side counterpart.
"""
assert state.ndim >= 2
assert state.is_cuda
assert src.ndim == state.ndim
assert indices.ndim == 1
assert indices.device == state.device
assert src.shape[1:] == state.shape[1:]
assert src.shape[0] == indices.shape[0]
assert indices.dtype in (torch.int32, torch.int64)
row_size = state[0].numel()
assert state[0].is_contiguous()
assert src[0].is_contiguous()
block_size = min(triton.next_power_of_2(row_size), 1024)
grid = (triton.cdiv(row_size, block_size), indices.numel())
return grid, dict(
stride_state_batch=state.stride(0),
stride_src_batch=src.stride(0),
stride_indices=indices.stride(0),
row_size=row_size,
BLOCK_SIZE=block_size,
num_warps=8,
launch_pdl=current_platform.is_arch_support_pdl(),
)
|