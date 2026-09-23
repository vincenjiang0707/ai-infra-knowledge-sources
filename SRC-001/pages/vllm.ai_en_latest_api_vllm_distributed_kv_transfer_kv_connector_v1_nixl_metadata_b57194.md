source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/nixl/metadata/
lastmod: 2026-09-23

#

`vllm.distributed.kv_transfer.kv_connector.v1.nixl.metadata`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.nixl.metadata)

Metadata dataclasses and helpers for the NIXL connector.

Classes:

-
–[HeartbeatInfo](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.nixl.metadata.HeartbeatInfo)Heartbeat data for a single remote engine, sent from D worker to P.

-
–[NixlHandshakePayload](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.nixl.metadata.NixlHandshakePayload)Wrapper for NIXL handshake sent over the wire.


Functions:

-
–[compute_nixl_compatibility_hash](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.nixl.metadata.compute_nixl_compatibility_hash)Compute compatibility hash for NIXL KV transfer.


##

`HeartbeatInfo`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.nixl.metadata.HeartbeatInfo)

Heartbeat data for a single remote engine, sent from D worker to P.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/nixl/metadata.py`


##

`NixlHandshakePayload`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.nixl.metadata.NixlHandshakePayload)

Bases: [KVConnectorHandshakeMetadata](https://docs.vllm.ai/base/#vllm.distributed.kv_transfer.kv_connector.v1.base.KVConnectorHandshakeMetadata)

Wrapper for NIXL handshake sent over the wire.

Enables two-phase decoding for graceful compatibility checking: 1. Decode NixlHandshakePayload to get compatibility_hash 2. Compute local hash and compare 3. Only if hashes match, decode agent_metadata_bytes

This prevents decoder errors when NixlAgentMetadata schema is incompatible, allowing graceful failure with clear error message.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/nixl/metadata.py`


##

`_get_speculative_compatibility_factors(vllm_config)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.nixl.metadata._get_speculative_compatibility_factors)

Return NIXL compatibility factors for hidden-state-based speculators.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/nixl/metadata.py`


##

`compute_nixl_compatibility_hash(vllm_config, attn_backend_name, transfer_mode='pull')`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.nixl.metadata.compute_nixl_compatibility_hash)

Compute compatibility hash for NIXL KV transfer.

Hash only the factors that affect whether two NIXL instances can successfully transfer KV cache data.

Factors included: - vLLM version and NIXL connector version - Model architecture (name, dtype, KV heads, layers) - KV cache format (dtype, sliding window) - Attention backend - EAGLE/MTP configuration that affects transferred state - Transfer mode (push vs pull)

The transfer mode is included because the push (WRITE) and pull (READ) connectors use incompatible transfer protocols; a push connector and a pull connector must never complete a handshake with each other.

Note: Factors like tensor_parallel_size, block_size, and kv_cache_layout are validated at runtime in _validate_remote_agent_handshake and are not included in this hash to support heterogeneous deployments.

Note - the set of factors are likely to evolve significantly over time to be more or less permissive.

Returns:

-

–[str](https://docs.python.org/3/builtins/stdtypes.html#str)SHA-256 hex digest