source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v41/nvidia/model_state/
lastmod: 2026-09-24

class DeepseekV41ModelState(DefaultModelState):
"""DefaultModelState plus the engram lookback window and SWA bounded replay.
The engram n-gram hash needs the ids of the ``depth`` tokens preceding
each request's chunk start (see ``common/engram.py``). The runner keeps
the full token history on device, so the window is gathered there every
step: exact for prompt and generated tokens alike, whatever instance
produced their KV.
SWA bounded replay (``CacheConfig.swa_bounded_replay``) keeps the
sliding-window KV out of prefix caching and rebuilds it after a prefix hit
by recomputing the hit's last window; the scheduler tells each request the
position from which it holds window KV (``NewRequestData.replay_start``).
``prepare_attn`` gathers those per batch, pads the replayed tokens' slots
in the prefix-cacheable groups so the cached KV stays as is, and hands the
starts to the sliding-window metadata builders, whose kernels read no
window KV below them.
"""
def __init__(
self,
vllm_config: VllmConfig,
model: nn.Module,
encoder_cache: EncoderCache | None,
device: torch.device,
):
super().__init__(vllm_config, model, encoder_cache, device)
depth = model.token_lookback_depth
self.lookback_token_ids: torch.Tensor | None = None
if depth > 0:
# Persistent so a captured graph can read it on replay.
self.lookback_token_ids = torch.full(
(self.max_num_reqs, depth), -1, dtype=torch.int32, device=device
)
# Per request state index; batches gather from it (see prepare_attn).
self._replay_start_np = np.zeros(self.max_num_reqs, dtype=np.int32)
self._replay_start = torch.zeros(
self.max_num_reqs, dtype=torch.int32, device=device
)
self._replay_start_staging = UvaBufferPool(self.max_num_reqs, torch.int32)
# The replay window and the indices of the prefix-cacheable groups, from
# the KV cache config on first use; None until then.
self._replay: tuple[int, torch.Tensor] | None = None
def add_request(self, req_index: int, new_req_data: NewRequestData) -> None:
super().add_request(req_index, new_req_data)
self._replay_start_np[req_index] = new_req_data.replay_start
def prepare_inputs(
self, input_batch: InputBatch, req_states: RequestState
) -> dict[str, torch.Tensor | None]:
model_inputs = super().prepare_inputs(input_batch, req_states)
window = self.lookback_token_ids
if window is None:
return model_inputs
all_token_ids = req_states.all_token_ids.gpu
depth = window.shape[1]
_gather_lookback_kernel[(window.shape[0],)](
window,
input_batch.idx_mapping,
req_states.num_computed_tokens.gpu,
all_token_ids,
all_token_ids.stride(0),
input_batch.idx_mapping.shape[0],
DEPTH=depth,
BLOCK_DEPTH=triton.next_power_of_2(depth),
)
model_inputs["lookback_token_ids"] = window
return model_inputs
def prepare_dummy_inputs(self, num_reqs: int, num_tokens: int) -> dict[str, Any]:
model_inputs = super().prepare_dummy_inputs(num_reqs, num_tokens)
if self.lookback_token_ids is not None:
# The captured graph reads this buffer; replays refill it in place.
self.lookback_token_ids.fill_(-1)
model_inputs["lookback_token_ids"] = self.lookback_token_ids
return model_inputs
def prepare_attn(
self,
input_batch: InputBatch,
cudagraph_mode: CUDAGraphMode,
block_tables: tuple[torch.Tensor, ...],
slot_mappings: torch.Tensor,
attn_groups: list[list[AttentionGroup]],
kv_cache_config: KVCacheConfig,
for_capture: bool = False,
ubatch_idx: int = 0,
model_specific_attn_metadata: ModelSpecificAttnMetadata | None = None,
) -> dict[str, Any]:
if self._replay is None:
specs = [group.kv_cache_spec for group in kv_cache_config.kv_cache_groups]
self._replay = (
max(spec.prefix_replay_tokens for spec in specs),
torch.tensor(
[i for i, spec in enumerate(specs) if spec.prefix_cacheable],
dtype=torch.int32,
device=self.device,
),
)
window, cacheable_groups = self._replay
if window:
num_reqs = input_batch.num_reqs
# Decode rows sit above the hit, so only prefills carry a replay
# start; dummy batches (captures, profiling) carry none.
replay_start_np = np.where(
input_batch.is_prefilling_np[:num_reqs],
self._replay_start_np[input_batch.idx_mapping_np[:num_reqs]],
0,
).astype(np.int32)
replay_start = self._replay_start_staging.copy_to_gpu(
replay_start_np, out=self._replay_start[:num_reqs]
)
if replay_start_np.any():
# The replayed tokens rebuild window KV only: their slots in the
# prefix-cacheable groups are padded so the cached KV stays as is.
_pad_replayed_slots_kernel[(num_reqs,)](
slot_mappings,
slot_mappings.stride(0),
cacheable_groups,
input_batch.query_start_loc,
input_batch.positions,
replay_start,
window,
PAD_SLOT_ID,
NUM_GROUPS=cacheable_groups.numel(),
BLOCK=1024,
)
assert model_specific_attn_metadata is None
model_specific_attn_metadata = ReplayAttnMetadata(replay_start)
return super().prepare_attn(
input_batch,
cudagraph_mode,
block_tables,
slot_mappings,
attn_groups,
kv_cache_config,
for_capture=for_capture,
ubatch_idx=ubatch_idx,
model_specific_attn_metadata=model_specific_attn_metadata,
)