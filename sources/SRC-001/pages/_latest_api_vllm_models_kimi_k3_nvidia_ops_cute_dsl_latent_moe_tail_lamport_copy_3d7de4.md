source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/lamport_copy/
lastmod: 2026-09-24

class LamportCopy:
"""Consume the local physical copy of an NVLS-multicast mailbox."""
def __init__(self, hidden_dim: int, ctas: int, threads: int):
self.hidden_dim = hidden_dim
self.ctas = ctas
self.threads = threads
@cute.jit
def __call__(
self,
symmetric_mailbox: cute.Tensor,
local_output: cute.Tensor,
m: cutlass.Int32,
stream: cuda.CUstream,
):
fragments = m * cutlass.Int32(self.hidden_dim // VEC_BF16)
grid_ctas = cutlass.min(
cutlass.Int32(self.ctas),
cute.ceil_div(fragments, self.threads),
)
self.kernel(symmetric_mailbox, local_output, m).launch(
grid=(grid_ctas, 1, 1),
block=(self.threads, 1, 1),
stream=stream,
use_pdl=True,
)
@cute.kernel
def kernel(
self,
symmetric_mailbox: cute.Tensor,
local_output: cute.Tensor,
m: cutlass.Int32,
):
# The Lamport marker carries producer readiness, so polling can begin
# before the producer grid reaches ordinary completion.
cute.arch.griddepcontrol_launch_dependents()
tidx, _, _ = cute.arch.thread_idx()
block, _, _ = cute.arch.block_idx()
grid_x, _, _ = cute.arch.grid_dim()
thread = cutlass.Int64(block * self.threads + tidx)
stride = cutlass.Int64(grid_x * self.threads)
fragments = cutlass.Int64(m) * cutlass.Int64(self.hidden_dim // VEC_BF16)
fragment = thread
while fragment < fragments:
element = fragment * VEC_BF16
source = cute.make_ptr(
cutlass.BFloat16,
(symmetric_mailbox.iterator + element).llvm_ptr,
cute.AddressSpace.gmem,
assumed_align=16,
)
packed = load_global_u32x4(source, volatile=True)
while fragment_is_dirty(packed):
packed = load_global_u32x4(source, volatile=True)
destination = cutlass.Int64((local_output.iterator + element).toint())
store_global_u32x4(destination, packed, volatile=False)
store_lamport_sentinel_128(source)
fragment = fragment + stride