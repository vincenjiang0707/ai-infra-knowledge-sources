source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/
lastmod: 2026-09-24

class CollectiveKernel:
"""Own and launch the routed AllReduce/RMSNorm plus shared ReduceScatter."""
def __init__(
self,
*,
group: dist.ProcessGroup,
rank: int,
tp_size: int,
latent_dim: int,
hidden_dim: int,
max_m: int,
max_token_ctas: int,
rms_eps: float,
fp32_internal: bool,
top_k: int = 0,
) -> None:
validate_shape(
tp_size=tp_size,
latent_dim=latent_dim,
hidden_dim=hidden_dim,
)
self.rank = rank
self.tp_size = tp_size
self.latent_dim = latent_dim
self.hidden_dim = hidden_dim
self.shard_dim = hidden_dim // tp_size
self.max_m = max_m
self.max_token_ctas = max_token_ctas
self.rms_eps = float(rms_eps)
self.fp32_internal = fp32_internal
self.top_k = top_k
device = torch.device("cuda", torch.accelerator.current_device_index())
self._dummy_expert_weights = torch.empty(
(max_m, max(top_k, 1)), dtype=torch.bfloat16, device=device
)
self._dummy_expanded_idx = torch.empty(
(max_m, max(top_k, 1)), dtype=torch.int32, device=device
)
self._seven_cta_max_m = (
min(max_m, _SEVEN_CTA_MAX_M)
if (tp_size, latent_dim, hidden_dim) == (8, 3584, 7168)
and top_k == 16
and self._dummy_expert_weights.dtype == torch.bfloat16
and torch.cuda.get_device_capability(device)[0] == 10
else 0
)
bytes_per_routed_buffer = max_m * tp_size * latent_dim * 2
routed_bytes = NUM_LAMPORT_BUFFERS * bytes_per_routed_buffer
self._routed_workspace = symm_mem.empty(
routed_bytes // 4,
dtype=torch.float32,
device=device,
)
self._routed_symm_mem = symm_mem.rendezvous(self._routed_workspace, group)
self._routed_workspace.fill_(-0.0)
actual_bytes_per_buffer = (
self._routed_symm_mem.buffer_size // NUM_LAMPORT_BUFFERS // 16 * 16
)
if actual_bytes_per_buffer < bytes_per_routed_buffer:
raise RuntimeError("routed symmetric workspace is too small")
self._routed_flags = torch.tensor(
[0, 2, actual_bytes_per_buffer, 0, 0, 0, 0, 0, 0],
dtype=torch.uint32,
device=device,
)
routed_multicast_ptr = self._routed_symm_mem.multicast_ptr
if routed_multicast_ptr is None or routed_multicast_ptr == 0:
raise RuntimeError("routed NVLS multicast mapping is unavailable")
self._routed_multicast_ptr = int(routed_multicast_ptr)
self._latent_output = torch.empty(
(max_m, latent_dim), dtype=torch.bfloat16, device=device
)
self._shared_output = torch.empty(
(max_m, hidden_dim), dtype=torch.bfloat16, device=device
)
shard_start = rank * self.shard_dim
shard_end = shard_start + self.shard_dim
self._shared_shard = self._shared_output[:, shard_start:shard_end]
self._shared_workspace = symm_mem.empty(
(NUM_LAMPORT_BUFFERS, max_m, tp_size, self.shard_dim),
dtype=torch.bfloat16,
device=device,
)
self._shared_symm_mem = symm_mem.rendezvous(self._shared_workspace, group)
self._shared_workspace.view(torch.int32).fill_(-0x80000000)
self._shared_flags = torch.zeros(12, dtype=torch.int32, device=device)
self._shared_flags[1] = 1
self._shared_flags[2] = max_m * tp_size * self.shard_dim * 2
peer_ptrs = [
self._shared_symm_mem.get_buffer(
peer,
self._shared_workspace.shape,
torch.bfloat16,
).data_ptr()
for peer in range(tp_size)
]
if any(pointer == 0 for pointer in peer_ptrs):
raise RuntimeError("shared LSA peer mapping is unavailable")
self._shared_peer_ptrs = torch.tensor(
peer_ptrs, dtype=torch.int64, device=device
)
torch.accelerator.synchronize(device)
dist.barrier(group=group, device_ids=[device.index])
if self._seven_cta_max_m:
specializations = (
(1, 1),
(self._seven_cta_max_m, self._seven_cta_max_m),
)
for owner in range(tp_size):
if rank == owner:
for compile_max_m, compile_token_ctas in specializations:
if (compile_max_m, compile_token_ctas) == (
max_m,
max_token_ctas,
):
continue
compile_kernel(
rank=rank,
tp_size=tp_size,
latent_dim=latent_dim,
hidden_dim=hidden_dim,
max_m=compile_max_m,
max_token_ctas=compile_token_ctas,
latent_output=self._latent_output,
routed_workspace=self._routed_workspace,
routed_flags=self._routed_flags,
routed_multicast_ptr=self._routed_multicast_ptr,
shared_output=self._shared_output,
shared_workspace=self._shared_workspace,
shared_flags=self._shared_flags,
shared_peer_ptrs=self._shared_peer_ptrs,
rms_eps=self.rms_eps,
fp32_internal=fp32_internal,
top_k=top_k,
)
dist.barrier(group=group, device_ids=[device.index])
for owner in range(tp_size):
if rank == owner:
compile_kernel(
rank=rank,
tp_size=tp_size,
latent_dim=latent_dim,
hidden_dim=hidden_dim,
max_m=max_m,
max_token_ctas=max_token_ctas,
latent_output=self._latent_output,
routed_workspace=self._routed_workspace,
routed_flags=self._routed_flags,
routed_multicast_ptr=self._routed_multicast_ptr,
shared_output=self._shared_output,
shared_workspace=self._shared_workspace,
shared_flags=self._shared_flags,
shared_peer_ptrs=self._shared_peer_ptrs,
rms_eps=self.rms_eps,
fp32_internal=fp32_internal,
top_k=top_k,
)
dist.barrier(group=group, device_ids=[device.index])
def __call__(
self,
latent_source: torch.Tensor | UnfinalizedMoEOutput,
shared_source: torch.Tensor,
gamma: torch.Tensor,
) -> tuple[torch.Tensor, torch.Tensor]:
if shared_source.ndim != 2:
raise ValueError("shared_source must be rank-2")
expected: list[tuple[torch.Tensor, tuple[int, ...], str, torch.dtype]]
if isinstance(latent_source, UnfinalizedMoEOutput):
if self.top_k <= 0:
raise ValueError("collective was not configured for top-k finalize")
gemm2_permuted = latent_source.gemm2_permuted
expert_weights = latent_source.expert_weights
expanded_idx = latent_source.expanded_idx_to_permuted_idx
m = expanded_idx.shape[0]
expected = [
(
gemm2_permuted,
(gemm2_permuted.shape[0], self.latent_dim),
"gemm2_permuted",
torch.bfloat16,
),
(
expert_weights,
(m, self.top_k),
"expert_weights",
torch.bfloat16,
),
(
expanded_idx,
(m, self.top_k),
"expanded_idx_to_permuted_idx",
torch.int32,
),
]
else:
if self.top_k > 0:
raise ValueError("top-k collective requires an unfinalized output")
if latent_source.ndim != 2:
raise ValueError("latent_source must be rank-2")
m = latent_source.shape[0]
gemm2_permuted = latent_source
expert_weights = self._dummy_expert_weights
expanded_idx = self._dummy_expanded_idx
expected = [
(
latent_source,
(m, self.latent_dim),
"latent_source",
torch.bfloat16,
),
]
device = self._routed_workspace.device
expected.extend(
[
(
shared_source,
(m, self.hidden_dim),
"shared_source",
torch.bfloat16,
),
(gamma, (self.latent_dim,), "gamma", torch.bfloat16),
]
)
for tensor, shape, name, dtype in expected:
if (
tensor.shape != shape
or tensor.dtype != dtype
or tensor.device != device
or not tensor.is_contiguous()
):
raise ValueError(
f"{name} must be contiguous CUDA {dtype} {list(shape)}"
)
if not 1 <= m <= self.max_m:
raise ValueError(f"runtime M={m} must be in [1, {self.max_m}]")
launch_max_m = self.max_m
launch_token_ctas = self.max_token_ctas
if self._seven_cta_max_m and m <= self._seven_cta_max_m:
if m == 1:
launch_max_m = 1
launch_token_ctas = 1
else:
launch_max_m = self._seven_cta_max_m
launch_token_ctas = self._seven_cta_max_m
with torch.accelerator.device_index(device.index):
launch(
gemm2_permuted,
gamma,
self._latent_output,
self._routed_workspace,
self._routed_flags,
self._routed_multicast_ptr,
shared_source,
self._shared_output,
self._shared_workspace,
self._shared_flags,
self._shared_peer_ptrs,
self.rms_eps,
rank=self.rank,
tp_size=self.tp_size,
latent_dim=self.latent_dim,
hidden_dim=self.hidden_dim,
max_m=launch_max_m,
max_token_ctas=launch_token_ctas,
fp32_internal=self.fp32_internal,
top_k=self.top_k,
expert_weights=expert_weights,
expanded_idx_to_permuted_idx=expanded_idx,
)
return (
self._latent_output[:m],
self._shared_shard,
)
@property
def latent_output(self) -> torch.Tensor:
return self._latent_output
@property
def shared_output(self) -> torch.Tensor:
return self._shared_output