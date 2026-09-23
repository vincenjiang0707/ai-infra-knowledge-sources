source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/nvidia/ops/recoverssm/
lastmod: 2026-09-23

@dataclass
class KDARecoverSSMCommitContext:
conv_states: tuple[torch.Tensor, ...]
conv_state_base_addrs: torch.Tensor
conv_state_block_strides: torch.Tensor
conv_state_dim_strides: torch.Tensor
conv_state_token_strides: torch.Tensor
conv_history_len: int
checkpoints: tuple[torch.Tensor, ...]
state_base_addrs: torch.Tensor
state_block_strides: torch.Tensor
correction_caches: tuple[torch.Tensor, ...]
correction_cache_base_addrs: torch.Tensor
correction_cache_block_strides: torch.Tensor
kg_caches: tuple[torch.Tensor, ...]
kg_cache_base_addrs: torch.Tensor
kg_cache_block_strides: torch.Tensor
commit_lens: torch.Tensor
final_state_indices: torch.Tensor
boundary_state_indices: torch.Tensor
boundary_recovery_lens: torch.Tensor
A_log: torch.Tensor
dt_bias: torch.Tensor
lower_bound: float | None
spec_query_len: int
@classmethod
def create(
cls,
layers: Sequence[Any],
*,
spec_query_len: int,
max_num_reqs: int,
) -> "KDARecoverSSMCommitContext":
if not layers:
raise ValueError("KDA RecoverSSM commit requires at least one layer")
if any(len(layer.kv_cache) != 4 for layer in layers):
raise ValueError(
"KDA RecoverSSM pages must contain conv, state, correction, "
"and key/gate"
)
conv_states = [layer.kv_cache[0] for layer in layers]
if not is_conv_state_dim_first():
conv_states = [state.transpose(-1, -2) for state in conv_states]
checkpoints = [layer.kv_cache[1] for layer in layers]
correction_caches = [layer.kv_cache[2] for layer in layers]
kg_caches = [layer.kv_cache[3] for layer in layers]
A_log = [layer.A_log for layer in layers]
dt_bias = [
layer.dt_bias.view(layer.local_num_heads, layer.head_dim)
for layer in layers
]
lower_bounds = {layer.gate_lower_bound for layer in layers}
if len(lower_bounds) != 1:
raise ValueError("KDA RecoverSSM layers need matching gate bounds")
state_ref = checkpoints[0]
if state_ref.ndim != 4:
raise ValueError("KDA RecoverSSM checkpoint must be four-dimensional")
num_blocks, num_heads, value_dim, key_dim = state_ref.shape
for state in checkpoints:
if (
state.shape != state_ref.shape
or state.dtype != state_ref.dtype
or state.device != state_ref.device
or state.stride()[1:] != state_ref.stride()[1:]
):
raise ValueError(
"KDA RecoverSSM layers need matching checkpoint layout"
)
expected_correction_shape = (
num_blocks,
num_heads,
spec_query_len,
value_dim,
)
correction_ref = correction_caches[0]
for correction_cache in correction_caches:
if (
correction_cache.shape != expected_correction_shape
or correction_cache.dtype != torch.float32
or correction_cache.device != state_ref.device
or correction_cache.stride()[1:] != correction_ref.stride()[1:]
):
raise ValueError(
"KDA RecoverSSM correction buffers need float32 shape "
f"{expected_correction_shape}"
)
expected_kg_shape = (num_blocks, num_heads, spec_query_len, 2 * key_dim)
kg_ref = kg_caches[0]
for kg_cache in kg_caches:
if (
kg_cache.shape != expected_kg_shape
or kg_cache.dtype != kg_ref.dtype
or kg_cache.device != state_ref.device
or kg_cache.stride()[1:] != kg_ref.stride()[1:]
):
raise ValueError(
f"KDA RecoverSSM key/gate buffers need shape {expected_kg_shape}"
)
if any(param.shape != (num_heads,) for param in A_log):
raise ValueError("KDA RecoverSSM A_log shape is incompatible")
if any(param.shape != (num_heads, key_dim) for param in dt_bias):
raise ValueError("KDA RecoverSSM dt_bias shape is incompatible")
conv_ref = conv_states[0]
if conv_ref.ndim != 3:
raise ValueError("KDA RecoverSSM conv state must be three-dimensional")
conv_dim, conv_state_len = conv_ref.shape[1:]
conv_history_len = conv_state_len - spec_query_len + 1
if conv_history_len <= 0:
raise ValueError("KDA RecoverSSM conv state is shorter than its window")
for conv_state in conv_states:
if (
conv_state.shape != conv_ref.shape
or conv_state.dtype != conv_ref.dtype
or conv_state.device != state_ref.device
or conv_state.shape[0] != num_blocks
):
raise ValueError("KDA RecoverSSM layers need matching conv state")
device = state_ref.device
def _base_addrs(tensors: Sequence[torch.Tensor]) -> torch.Tensor:
return torch.tensor(
[tensor.data_ptr() for tensor in tensors],
dtype=torch.int64,
device=device,
)
def _block_strides(tensors: Sequence[torch.Tensor]) -> torch.Tensor:
return torch.tensor(
[tensor.stride(0) for tensor in tensors],
dtype=torch.int64,
device=device,
)
return cls(
conv_states=tuple(conv_states),
conv_state_base_addrs=_base_addrs(conv_states),
conv_state_block_strides=_block_strides(conv_states),
conv_state_dim_strides=torch.tensor(
[state.stride(1) for state in conv_states],
dtype=torch.int64,
device=device,
),
conv_state_token_strides=torch.tensor(
[state.stride(2) for state in conv_states],
dtype=torch.int64,
device=device,
),
conv_history_len=conv_history_len,
checkpoints=tuple(checkpoints),
state_base_addrs=_base_addrs(checkpoints),
state_block_strides=_block_strides(checkpoints),
correction_caches=tuple(correction_caches),
correction_cache_base_addrs=_base_addrs(correction_caches),
correction_cache_block_strides=_block_strides(correction_caches),
kg_caches=tuple(kg_caches),
kg_cache_base_addrs=_base_addrs(kg_caches),
kg_cache_block_strides=_block_strides(kg_caches),
commit_lens=torch.empty(max_num_reqs, dtype=torch.int32, device=device),
final_state_indices=torch.empty(
max_num_reqs, dtype=torch.int32, device=device
),
boundary_state_indices=torch.empty(
max_num_reqs, dtype=torch.int32, device=device
),
boundary_recovery_lens=torch.empty(
max_num_reqs, dtype=torch.int32, device=device
),
A_log=torch.stack(tuple(A_log)).contiguous(),
dt_bias=torch.stack(tuple(dt_bias)).contiguous(),
lower_bound=lower_bounds.pop(),
spec_query_len=spec_query_len,
)
def commit(
self,
num_accepted_tokens: torch.Tensor,
state_indices: torch.Tensor,
query_start_loc: torch.Tensor,
request_indices: torch.Tensor | None = None,
block_table: torch.Tensor | None = None,
num_computed_tokens: torch.Tensor | None = None,
mamba_block_size: int | None = None,
) -> None:
"""Fold accepted KDA and convolution inputs into every layer."""
batch = state_indices.shape[0]
if batch == 0:
return
if batch > self.commit_lens.shape[0]:
raise ValueError("KDA RecoverSSM commit batch exceeds its plan capacity")
if query_start_loc.shape[0] != batch + 1:
raise ValueError("KDA RecoverSSM commit metadata is incompatible")
if request_indices is not None and request_indices.shape[0] < batch:
raise ValueError("KDA RecoverSSM request mapping is too short")
align_args = (block_table, num_computed_tokens, mamba_block_size)
if any(arg is not None for arg in align_args) and any(
arg is None for arg in align_args
):
raise ValueError("KDA RecoverSSM align metadata is incomplete")
if mamba_block_size is not None and mamba_block_size < self.spec_query_len:
raise ValueError(
"KDA RecoverSSM align block size must cover one speculative window"
)
if block_table is not None and block_table.ndim != 2:
raise ValueError("KDA RecoverSSM block table must be two-dimensional")
device = self.checkpoints[0].device
if (
any(
tensor.device != device
for tensor in (
num_accepted_tokens,
state_indices,
query_start_loc,
)
)
or (request_indices is not None and request_indices.device != device)
or (block_table is not None and block_table.device != device)
or (
num_computed_tokens is not None and num_computed_tokens.device != device
)
):
raise ValueError("KDA RecoverSSM commit inputs must be on the same device")
block_table_stride = (0, 0) if block_table is None else block_table.stride()
num_computed_stride = (
0 if num_computed_tokens is None else num_computed_tokens.stride(0)
)
num_layers = len(self.checkpoints)
conv_ref = self.conv_states[0]
conv_dim = conv_ref.shape[1]
block_history = triton.next_power_of_2(self.conv_history_len)
_prepare_commit_plan_kernel[(batch,)](
num_accepted_tokens,
request_indices,
state_indices,
query_start_loc,
block_table,
num_computed_tokens,
self.commit_lens,
self.final_state_indices,
self.boundary_state_indices,
self.boundary_recovery_lens,
NULL_BLOCK_ID,
mamba_block_size or 1,
block_table.shape[1] if block_table is not None else 1,
num_accepted_tokens.stride(0),
request_indices.stride(0) if request_indices is not None else 0,
state_indices.stride(0),
query_start_loc.stride(0),
block_table_stride[0],
block_table_stride[1],
num_computed_stride,
SPEC_QUERY_LEN=self.spec_query_len,
num_warps=1,
)
_compact_conv_state_kernel[(triton.cdiv(conv_dim, 256), batch, num_layers)](
conv_ref,
self.conv_state_base_addrs,
self.conv_state_block_strides,
self.conv_state_dim_strides,
self.conv_state_token_strides,
state_indices,
self.commit_lens,
self.final_state_indices,
self.boundary_state_indices,
self.boundary_recovery_lens,
NULL_BLOCK_ID,
conv_dim,
self.conv_history_len,
state_indices.stride(0),
BLOCK_D=256,
BLOCK_HISTORY=block_history,
ALIGN_MODE=block_table is not None,
num_warps=4,
)
state_ref = self.checkpoints[0]
_, num_heads, value_dim, key_dim = state_ref.shape
block_k = triton.next_power_of_2(key_dim)
block_v = min(triton.next_power_of_2(value_dim), 32)
grid = (
triton.cdiv(value_dim, block_v),
batch,
num_layers * num_heads,
)
_commit_kda_state_kernel[grid](
state_ref,
self.state_base_addrs,
self.state_block_strides,
self.correction_caches[0],
self.correction_cache_base_addrs,
self.correction_cache_block_strides,
self.kg_caches[0],
self.kg_cache_base_addrs,
self.kg_cache_block_strides,
self.A_log,
self.dt_bias,
state_indices,
self.commit_lens,
self.final_state_indices,
self.boundary_state_indices,
self.boundary_recovery_lens,
self.lower_bound or 0.0,
NULL_BLOCK_ID,
state_ref.stride(1),
state_ref.stride(2),
state_ref.stride(3),
self.correction_caches[0].stride(1),
self.correction_caches[0].stride(2),
self.correction_caches[0].stride(3),
self.kg_caches[0].stride(1),
self.kg_caches[0].stride(2),
self.kg_caches[0].stride(3),
self.A_log.stride(0),
self.A_log.stride(1),
self.dt_bias.stride(0),
self.dt_bias.stride(1),
self.dt_bias.stride(2),
state_indices.stride(0),
K=key_dim,
V=value_dim,
BK=block_k,
BV=block_v,
NUM_HEADS=num_heads,
USE_LOWER_BOUND=self.lower_bound is not None,
ALIGN_MODE=block_table is not None,
num_warps=4,
num_stages=2,
)