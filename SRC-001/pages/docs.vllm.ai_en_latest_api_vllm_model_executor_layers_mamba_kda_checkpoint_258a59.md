source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/mamba/kda_checkpoint/
lastmod: 2026-09-23

@dataclass(frozen=True)
class FlashKDAPrefillCheckpointExporter(MambaPrefillCheckpointExporter):
"""Store FlashKDA recurrent and convolution checkpoint states."""
state_len: int | None = None
def export(
self,
checkpoint: MambaPrefillCheckpointMetadata,
*,
raw_qkv: torch.Tensor,
conv_state: torch.Tensor,
recurrent_checkpoint: torch.Tensor,
recurrent_state: torch.Tensor,
cu_seqlens: torch.Tensor,
) -> None:
state_len = (
self.state_len if self.state_len is not None else conv_state.shape[-1]
)
width = raw_qkv.shape[-1]
recurrent_row_size = recurrent_checkpoint[0].numel()
block_size = 256
store_cache_checkpoints_kernel[
(
checkpoint.checkpoint_offsets.numel(),
triton.cdiv(max(width * state_len, recurrent_row_size), block_size),
)
](
raw_qkv,
conv_state,
recurrent_checkpoint,
recurrent_state,
cu_seqlens,
checkpoint.checkpoint_offsets,
checkpoint.state_indices,
raw_qkv.stride(0),
raw_qkv.stride(1),
conv_state.stride(0),
conv_state.stride(1),
conv_state.stride(2),
recurrent_checkpoint.stride(0),
recurrent_state.stride(0),
checkpoint.checkpoint_offsets.stride(0),
state_len,
width,
recurrent_row_size,
NULL_BLOCK_ID,
block_size,
)