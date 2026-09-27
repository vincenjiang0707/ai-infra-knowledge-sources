source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v41/nvidia/ops/cute_dsl/all_reduce_mhc/
lastmod: 2026-09-27

```python
class AllReduceMHC:
"""Lamport TP all-reduce fused with mHC post, collapse and RMSNorm.
``__call__`` reduces ``x`` across the TP group, writes the post-mixed hc
streams and the normalized collapse, and leaves the next mixes to the
caller. ``finalize`` does the same for an unfinalized MoE output, folding
the top-k reduction and the shared-expert add into the publish. Each
instance owns a Lamport mailbox; construction is collective over the TP
group.
"""
def __init__(
self,
*,
hidden_size: int,
hc_mult: int,
max_num_tokens: int,
top_k: int,
device: torch.device,
) -> None:
group = get_tp_group().device_group
self.hidden_size = hidden = hidden_size
self.hc_mult = hc = hc_mult
self.capacity = capacity = max_num_tokens
self.top_k = top_k
tp = dist.get_world_size(group)
rank = dist.get_rank(group)
device = torch.device(device)
# FlashInfer's LL_ALL_REDUCE_GB300_TP{4,8}_H5120 and
# LL_FINALIZE_..._H5120_K* presets: a cluster of 5 x 128 threads covers
# a 640-fragment token in one fully used trip, and the finalize stages
# all top_k rows at once.
with torch.accelerator.device_index(device.index):
self._publish = cute.compile(
_SharedOnlyPublishDeviceKernel(
hidden=hidden,
tp=tp,
rank=rank,
capacity_m=capacity,
elements_per_thread=VEC_BF16,
threads=128,
release_before_store=False,
enable_pdl=True,
),
make_fake_dynamic_compact_tensor(
BFloat16, alignment=16, divisibility=hidden
),
make_fake_compact_tensor(Int32, (2,), assumed_align=4),
Int64(0),
Int32(capacity),
current_cu_stream(),
)
self._finalize_publish = cute.compile(
_QuadFinalizePublishDeviceKernel(
hidden=hidden,
top_k=top_k,
tp=tp,
rank=rank,
capacity_m=capacity,
threads=128,
# DSV4.1's router folds the scale into the weights.
routed_scaling_factor=1.0,
include_shared_expert=True,
load_shared_expert_before_pdl=False,
enable_pdl=True,
prefetch_group=top_k,
fp32_weights=True,
),
make_fake_dynamic_compact_tensor(
BFloat16, alignment=16, divisibility=hidden
),
make_fake_dynamic_compact_tensor(
Float32, alignment=4, divisibility=top_k
),
make_fake_dynamic_compact_tensor(
Int32, alignment=4, divisibility=top_k
),
make_fake_dynamic_compact_tensor(
BFloat16, alignment=16, divisibility=hidden
),
make_fake_compact_tensor(Int32, (2,), assumed_align=4),
Int64(0),
Int32(capacity),
current_cu_stream(),
)
self._collective = cute.compile(
_LamportMHCDeviceKernel(
hidden=hidden,
hc=hc,
tp=tp,
capacity_m=capacity,
cluster_size=5,
rank_lanes=1,
threads=128,
enable_pdl=True,
),
make_fake_compact_tensor(
BFloat16,
(LAMPORT_GENERATIONS * tp * capacity * hidden,),
assumed_align=16,
),
make_fake_dynamic_compact_tensor(
BFloat16, alignment=16, divisibility=hc * hidden
),
make_fake_dynamic_compact_tensor(Float32, alignment=4, divisibility=hc),
make_fake_dynamic_compact_tensor(
Float32, alignment=4, divisibility=hc * hc
),
make_fake_dynamic_compact_tensor(Float32, alignment=4, divisibility=hc),
make_fake_compact_tensor(BFloat16, (hidden,), assumed_align=16),
make_fake_dynamic_compact_tensor(
BFloat16, alignment=16, divisibility=hc * hidden
),
make_fake_dynamic_compact_tensor(
BFloat16, alignment=16, divisibility=hidden
),
make_fake_compact_tensor(Int32, (2,), assumed_align=4),
Float32(0.0),
Int32(capacity),
current_cu_stream(),
)
self._mailbox = symm_mem.empty(
(LAMPORT_GENERATIONS, tp, capacity, hidden),
dtype=torch.bfloat16,
device=device,
)
self._mailbox_handle = symm_mem.rendezvous(self._mailbox, group)
multicast = int(self._mailbox_handle.multicast_ptr or 0)
if not multicast or multicast % 16:
raise RuntimeError("NVLink multicast mapping is unavailable")
self._multicast = multicast
# Every slot starts as the Lamport sentinel, BF16 negative zero.
self._mailbox.view(torch.int16).fill_(-32768)
self._stage_state = torch.zeros(2, dtype=torch.int32, device=device)
torch.accelerator.synchronize()
dist.barrier(group=group)
def __call__(
self,
x: torch.Tensor,
residual: torch.Tensor,
post: torch.Tensor,
comb: torch.Tensor,
pre: torch.Tensor,
norm_weight: torch.Tensor,
norm_eps: float,
) -> tuple[torch.Tensor, torch.Tensor]:
"""Return (post-mixed residual streams, normalized layer input).
Args:
x: [M, hidden] BF16 TP-partial sublayer output.
residual: [M, hc, hidden] BF16 residual streams.
post: [M, hc(, 1)] FP32 post-mix.
comb: [M, hc, hc] FP32 residual mix, indexed [source, target].
pre: [M, hc] FP32 carried pre-mix for the collapse.
norm_weight: [hidden] BF16 RMSNorm weight.
norm_eps: RMSNorm epsilon.
"""
m = x.shape[0]
self._check(m, residual, post, comb, pre)
if x.shape != (m, self.hidden_size):
raise ValueError("unexpected x shape")
self._publish(
to_cute_dynamic(x.flatten(), 16, divisibility=self.hidden_size),
to_cute(self._stage_state, 4),
Int64(self._multicast),
Int32(m),
current_cu_stream(),
)
return self._collect(residual, post, comb, pre, norm_weight, norm_eps, m)
def finalize(
self,
gemm2_permuted: torch.Tensor,
expert_weights: torch.Tensor,
expanded_idx_to_permuted_idx: torch.Tensor,
shared_output: torch.Tensor,
residual: torch.Tensor,
post: torch.Tensor,
comb: torch.Tensor,
pre: torch.Tensor,
norm_weight: torch.Tensor,
norm_eps: float,
) -> tuple[torch.Tensor, torch.Tensor]:
"""``__call__`` for a MoE output left unfinalized.
Args:
gemm2_permuted: [rows, hidden] BF16 unweighted GEMM2 output in the
MoE's permuted order.
expert_weights: [M, top_k] FP32 routing weights, already scaled.
expanded_idx_to_permuted_idx: [M, top_k] int32 row of each route,
-1 for an expert this rank does not hold.
shared_output: [M, hidden] BF16 TP-partial shared-expert output.
residual: [M, hc, hidden] BF16 residual streams.
post: [M, hc(, 1)] FP32 post-mix.
comb: [M, hc, hc] FP32 residual mix, indexed [source, target].
pre: [M, hc] FP32 carried pre-mix for the collapse.
norm_weight: [hidden] BF16 RMSNorm weight.
norm_eps: RMSNorm epsilon.
"""
m = shared_output.shape[0]
hidden, top_k = self.hidden_size, self.top_k
self._check(m, residual, post, comb, pre)
if gemm2_permuted.dim() != 2 or gemm2_permuted.shape[1] != hidden:
raise ValueError("gemm2_permuted must be [rows, hidden]")
if shared_output.shape != (m, hidden):
raise ValueError("unexpected shared_output shape")
if expert_weights.dtype != torch.float32 or expert_weights.numel() != m * top_k:
raise ValueError("expert_weights must be FP32 [M, top_k]")
if (
expanded_idx_to_permuted_idx.dtype != torch.int32
or expanded_idx_to_permuted_idx.numel() != m * top_k
):
raise ValueError("expanded_idx_to_permuted_idx must be int32 [M, top_k]")
self._finalize_publish(
to_cute_dynamic(gemm2_permuted.flatten(), 16, divisibility=hidden),
to_cute_dynamic(expert_weights.flatten(), 4, divisibility=top_k),
to_cute_dynamic(
expanded_idx_to_permuted_idx.flatten(), 4, divisibility=top_k
),
to_cute_dynamic(shared_output.flatten(), 16, divisibility=hidden),
to_cute(self._stage_state, 4),
Int64(self._multicast),
Int32(m),
current_cu_stream(),
)
return self._collect(residual, post, comb, pre, norm_weight, norm_eps, m)
def _check(
self,
m: int,
residual: torch.Tensor,
post: torch.Tensor,
comb: torch.Tensor,
pre: torch.Tensor,
) -> None:
hc = self.hc_mult
if not 1 <= m <= self.capacity:
raise ValueError(f"M={m} is outside [1, {self.capacity}]")
if residual.shape != (m, hc, self.hidden_size):
raise ValueError("unexpected residual shape")
if (
post.numel() != m * hc
or pre.numel() != m * hc
or comb.numel() != m * hc * hc
):
raise ValueError("unexpected mix shapes")
def _collect(
self,
residual: torch.Tensor,
post: torch.Tensor,
comb: torch.Tensor,
pre: torch.Tensor,
norm_weight: torch.Tensor,
norm_eps: float,
m: int,
) -> tuple[torch.Tensor, torch.Tensor]:
hidden, hc = self.hidden_size, self.hc_mult
residual_output = torch.empty_like(residual)
layer_input = torch.empty(
(m, hidden), dtype=torch.bfloat16, device=residual.device
)
self._collective(
to_cute(self._mailbox.flatten(), 16),
to_cute_dynamic(residual.flatten(), 16, divisibility=hc * hidden),
to_cute_dynamic(post.flatten(), 4, divisibility=hc),
to_cute_dynamic(comb.flatten(), 4, divisibility=hc * hc),
to_cute_dynamic(pre.flatten(), 4, divisibility=hc),
to_cute(norm_weight, 16),
to_cute_dynamic(residual_output.flatten(), 16, divisibility=hc * hidden),
to_cute_dynamic(layer_input.flatten(), 16, divisibility=hidden),
to_cute(self._stage_state, 4),
Float32(norm_eps),
Int32(m),
current_cu_stream(),
)
return residual_output, layer_input
```