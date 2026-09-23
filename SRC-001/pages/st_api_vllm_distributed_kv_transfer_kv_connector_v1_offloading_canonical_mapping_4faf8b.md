source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/offloading/canonical_mapping/
lastmod: 2026-09-23

#

`vllm.distributed.kv_transfer.kv_connector.v1.offloading.canonical_mapping`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.canonical_mapping)

Derivation of canonical page mappings for KV offloading.

The only place in the offloading stack that reasons about parallelism (TP/DCP/PCP); everything downstream consumes byte mappings. The canonical page of a layer is the full offloaded block without parallelism: all KV heads, all block_size * dcp * pcp tokens, in the worker's page encoding. Uncertifiable layers get an opaque fallback mapping (fail closed).

Classes:

-
–[ByteRegion](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.canonical_mapping.ByteRegion)A byte region within a page that repeats once per token.


Functions:

-
–[canonical_format_id](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.canonical_mapping.canonical_format_id)Identity of the canonical byte format, for namespacing persisted KV.

-
–[derive_canonical_mappings](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.canonical_mapping.derive_canonical_mappings)Per-layer canonical page mappings for this worker.


##

`ByteRegion`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.canonical_mapping.ByteRegion)

A byte region within a page that repeats once per token.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/canonical_mapping.py`


##

`_RankContext`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.canonical_mapping._RankContext)

Sharding parameters of one worker rank within the offload group.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/canonical_mapping.py`


##

`_attention_byte_regions(kv_cache, spec, num_blocks, head_shard, num_head_shards, cp_size)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.canonical_mapping._attention_byte_regions)

Byte regions of an attention page, given this rank's head shard. None when the physical layout is not recognized (fail closed).

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/canonical_mapping.py`


##

`_coalesce_runs(runs)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.canonical_mapping._coalesce_runs)

Collapse contiguous fragments within and across runs to minimize the number of copy ops (e.g. a single-rank mapping becomes one whole-page run).

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/canonical_mapping.py`


##

`_interleave_cp_tokens(regions, num_tokens, ctx)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.canonical_mapping._interleave_cp_tokens)

Place each region's num_tokens rows at their canonical token positions, one run per chunk of interleaved tokens.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/canonical_mapping.py`


##

`_layer_mapping(spec, kv_cache, num_blocks, ctx)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.canonical_mapping._layer_mapping)

Certified mapping for one layer at one rank, or None (fail closed).

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/canonical_mapping.py`


##

`_local_to_canonical_token(local_idx, ctx)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.canonical_mapping._local_to_canonical_token)

Canonical position of one of this rank's local token indices.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/canonical_mapping.py`


##

`_opaque_fallback_mapping(page_size_bytes, num_ranks, rank)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.canonical_mapping._opaque_fallback_mapping)

Fallback: place the worker's page whole at a worker-exclusive offset.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/canonical_mapping.py`


##

`_packed_kv_regions(kv_cache, spec, head_shard, num_head_shards, cp_size)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.canonical_mapping._packed_kv_regions)

K and V adjacent per (token, head), in NHD or HND stride order.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/canonical_mapping.py`


##

`_split_kv_regions(kv_cache, spec, head_shard, num_head_shards, cp_size)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.canonical_mapping._split_kv_regions)

K and V in separate page halves, in NHD or HND stride order.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/canonical_mapping.py`


##

`_verify_tiling(layer_name, per_rank)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.canonical_mapping._verify_tiling)

Whichever ranks a block elects as writers must tile the canonical page exactly once, and each rank's runs must cover exactly its local page.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/canonical_mapping.py`


##

`canonical_format_id(kv_cache_layout)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.canonical_mapping.canonical_format_id)

Identity of the canonical byte format, for namespacing persisted KV. Canonical pages keep the worker's KV layout family, so the id couples the format version with that family; consumers must match it exactly. The family keeps its historical NHD/HND spelling so ids stay stable for KV persisted before the layout enum existed.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/canonical_mapping.py`


##

`derive_canonical_mappings(vllm_config, kv_cache_config, kv_caches)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.canonical_mapping.derive_canonical_mappings)

Per-layer canonical page mappings for this worker.

Empty when the worker group is not exactly the TP x PCP grid; layers absent from the result have no canonical representation.