source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/nixl/tp_mapping/
lastmod: 2026-09-24

Build the complete local-to-remote TP mapping.

Computes source ranks, head slot assignments, and the rank offset factor in a single pass.

DCP support is scoped to MLA only, with a side is either fully replicated or fully sharded. DCP-branch reuses the same rank set used at handshake selection.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/nixl/tp_mapping.py`


| def compute_tp_mapping(
transfer_topology: TransferTopology,
remote_tp_size: int,
group_spec_types: tuple[type[KVCacheSpec], ...],
remote_dcp_size: int = 1,
) -> TPMapping:
"""Build the complete local-to-remote TP mapping.
Computes source ranks, head slot assignments, and the rank offset
factor in a single pass.
DCP support is scoped to MLA only, with a side is either fully replicated or fully
sharded. DCP-branch reuses the same rank set used at handshake selection.
"""
tp_rank = transfer_topology.tp_rank
tp_size = transfer_topology.tp_size
total_num_kv_heads = transfer_topology.total_num_kv_heads
# --- Attention source ranks ---
if transfer_topology.is_mla or tp_size >= remote_tp_size:
if transfer_topology.is_mla and remote_dcp_size > 1:
attn_ranks = transfer_topology.dcp_source_ranks(
remote_tp_size, remote_dcp_size
)
else:
# D (local TP) > P (remote TP): multiple local ranks read different chunks
# from *one* remote rank, corresponding to different kv heads.
# For MLA, we only need one remote since cache is duplicated. When
# P TP=k*TP k, this will spread mla ranks to read from remote k*tp_rank.
attn_ranks = [tp_rank * remote_tp_size // tp_size]
else:
# P (remote TP) > D (local TP): one local rank
# reads from multiple remote ranks.
# GQA dedup: when K < remote_tp_size, several remote ranks
# hold the same KV head. np.unique keeps only the first
# rank per unique head so we don't issue redundant reads.
abs_tp = remote_tp_size // tp_size
start = tp_rank * abs_tp
heads = np.arange(start, start + abs_tp) * total_num_kv_heads // remote_tp_size
_, unique_idx = np.unique(heads, return_index=True)
attn_ranks = (start + np.sort(unique_idx)).tolist()
# --- SSM source ranks ---
has_ssm = any(_is_ssm_spec(t) for t in group_spec_types)
if has_ssm:
if tp_size < remote_tp_size:
abs_tp = remote_tp_size // tp_size
ssm_ranks = list(range(tp_rank * abs_tp, (tp_rank + 1) * abs_tp))
else:
ssm_ranks = list(attn_ranks)
else:
ssm_ranks = []
all_ranks = sorted(set(attn_ranks) | set(ssm_ranks))
# --- Per-group ordered source ranks ---
source_ranks_per_group = tuple(
tuple(ssm_ranks) if _is_ssm_spec(t) else tuple(attn_ranks)
for t in group_spec_types
)
# --- Attention head slots ---
head_to_slot: dict[int, int] = {}
for i, r in enumerate(attn_ranks):
head_to_slot[r * total_num_kv_heads // remote_tp_size] = i
rank_to_attention_slot = {
r: head_to_slot.get(r * total_num_kv_heads // remote_tp_size, 0)
for r in all_ranks
}
# --- Rank offset factor ---
if transfer_topology.is_mla or tp_size <= remote_tp_size:
# We don't index into remote for reading, no offset needed.
rank_offset_factor = 0
elif tp_size > total_num_kv_heads:
local_head = tp_rank * total_num_kv_heads // tp_size
p_start = attn_ranks[0] * total_num_kv_heads // remote_tp_size
rank_offset_factor = local_head - p_start
else:
# D TP > P TP: we index into remote to read different heads depending on rank.
rank_offset_factor = tp_rank % (tp_size // remote_tp_size)
local_consumers = transfer_topology.dcp_consumer_count(
remote_tp_size, remote_dcp_size
)
return TPMapping(
source_ranks_per_group=source_ranks_per_group,
all_source_ranks=tuple(all_ranks),
rank_to_attention_slot=rank_to_attention_slot,
rank_offset_factor=rank_offset_factor,
local_consumers=local_consumers,
)
|