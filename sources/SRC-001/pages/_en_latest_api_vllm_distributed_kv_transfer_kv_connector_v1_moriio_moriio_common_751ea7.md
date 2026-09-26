source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common/
lastmod: 2026-09-24

#

`vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common)

Classes:

-
–[HandshakeError](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.HandshakeError)Exception raised when handshake fails.

-
–[LayerTransferPlan](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.LayerTransferPlan)Plan for transferring a single layer.

-
–[MoRIIOConnectorMetadata](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.MoRIIOConnectorMetadata) -
–[MoRIIOConstants](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.MoRIIOConstants)Constants for MoRIIO connector.

-
–[MoRIIOError](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.MoRIIOError)Base exception for MoRIIO operations.

-
–[RemoteAllocInfo](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.RemoteAllocInfo)Information about remote block allocation.

-
–[ReqMeta](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.ReqMeta)Metadata for a single request.

-
–[RoleManager](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.RoleManager)Manages role state across the connector.

-
–[TransferBatchState](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.TransferBatchState)Verdict for a group of transfer statuses that belong to one request.

-
–[TransferError](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.TransferError)Exception raised when transfer fails.


Functions:

-
–[fold_local_rank](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.fold_local_rank)Fold a global DP rank into its pod-local rank [0, dp_size_local).

-
–[get_peer_zmq_from_request_id](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.get_peer_zmq_from_request_id)Extract the

*peer's*zmq_address from the vLLM router request_id. -
–[get_role](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.get_role)Get the global role.

-
–[parse_moriio_zmq_address](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.parse_moriio_zmq_address)Parse the MoRI-IO zmq address into its components.

-
–[pod_index](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.pod_index)Pod index (0-based) a global DP rank lives on for Wide-EP multi-pod.

-
–[resolve_host_ip](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.resolve_host_ip)The IP this MoRIIO process advertises for KV transfer.

-
–[set_role](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.set_role)Set the global role.

-
–[zmq_ctx](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.zmq_ctx)Context manager for a ZMQ socket.


##

`HandshakeError`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.HandshakeError)

Bases: [MoRIIOError](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.MoRIIOError)

Exception raised when handshake fails.

##

`LayerTransferPlan`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.LayerTransferPlan)

Plan for transferring a single layer.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`


##

`MoRIIOConnectorMetadata`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.MoRIIOConnectorMetadata)

Bases: [KVConnectorMetadata](https://docs.vllm.ai/base/#vllm.distributed.kv_transfer.kv_connector.v1.base.KVConnectorMetadata)

Methods:

-
–[add_new_req](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.MoRIIOConnectorMetadata.add_new_req)Ingest a peer's

`kv_transfer_params`

into a typed`ReqMeta`

.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`


|
|

###

`add_new_req(request_id, local_block_ids, kv_transfer_params, write_mode=False)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.MoRIIOConnectorMetadata.add_new_req)

Ingest a peer's `kv_transfer_params`

into a typed `ReqMeta`

.

This is the single place peer info enters the connector. The `kv_transfer_params`

contract (as produced by the llm-d sidecar / vLLM router, or echoed by the prefill leg's `request_finished`

):

Required (always): * `transfer_id`

-- stable id shared by both legs. * `remote_engine_id`

-- peer engine id for the handshake table. * `remote_block_ids`

-- peer block ids (may be [] in WRITE mode, where decode allocates its own blocks).

## Peer address -- ONE of the following two must resolve

- embedded in
`request_id`

(vLLM-router PD id form), OR - explicit
`remote_host`

+`remote_handshake_port`

+`remote_notify_port`

(llm-d sidecar / returnable path). If neither resolves we raise -- there is no safe default host/port.

Optional (defaulted): * `tp_size`

(default 1) -- peer TP size. * `remote_dp_size`

(default 1) -- peer GLOBAL DP size. * `remote_dp_size_local`

(default = `remote_dp_size`

) -- per-pod DP size for Wide-EP multi-pod port/host folding; 0/absent means single-pod. * `remote_hosts`

(default [remote_host]) -- per-pod IP list indexed by `pod_idx = rank // dp_local`

.

Routing keys consumed elsewhere (NOT here): `remote_dp_rank`

/ `remote_dp_rank_override`

gate the decode->prefill notify target in MoRIIOConnectorScheduler; they are router-authoritative and never self-derived (see that class's request routing contract).

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`


|
|

##

`MoRIIOConstants`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.MoRIIOConstants)

Constants for MoRIIO connector.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`


##

`MoRIIOError`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.MoRIIOError)

##

`RemoteAllocInfo`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.RemoteAllocInfo)

Information about remote block allocation.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`


##

`ReqMeta`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.ReqMeta)

Metadata for a single request.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`


##

`RoleManager`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.RoleManager)

Manages role state across the connector.

Methods:

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`


###

`get_role()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.RoleManager.get_role)

##

`TransferBatchState`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.TransferBatchState)

Bases: [Enum](https://docs.python.org/3/library/enum.html#enum.Enum)

Verdict for a group of transfer statuses that belong to one request.

A request's KV transfer is spread over one status per layer (two for a KDA layer), so a single status never decides the request: PENDING means at least one is still in flight and none has failed, FAILED means at least one failed, DONE means all succeeded.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`


##

`TransferError`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.TransferError)

Bases: [MoRIIOError](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.MoRIIOError)

Exception raised when transfer fails.

##

`fold_local_rank(global_dp_rank, dp_size_local)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.fold_local_rank)

Fold a global DP rank into its pod-local rank [0, dp_size_local).

`dp_size_local == 0`

is the external-DP sentinel (local size unknown): return the rank unchanged, since a global DP rank is always < the global DP size so no folding is needed and the modulo is skipped (never divides by zero).

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`


##

`get_peer_zmq_from_request_id(request_id, is_producer)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.get_peer_zmq_from_request_id)

Extract the *peer's* zmq_address from the vLLM router request_id.

The producer (prefill) needs the decode's address; the consumer (decode) needs the prefill's address.

Returns `None`

when the request_id does not encode peer info. The llm-d routing sidecar (`llm-d-inference-scheduler`

) does not embed addresses in `request_id`

; instead it passes `remote_host`

, `remote_handshake_port`

and `remote_notify_port`

explicitly in `kv_transfer_params`

. Callers must handle the `None`

return by falling back to those fields. See `add_new_req`

for the canonical fallback path.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`


##

`get_role()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.get_role)

##

`parse_moriio_zmq_address(zmq_address)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.parse_moriio_zmq_address)

Parse the MoRI-IO zmq address into its components.

Parses `"host:IP,handshake:PORT,notify:PORT"`

into (host, handshake_port, notify_port).

Each key-value pair is split on the *first* colon so that IPv6 addresses (e.g. `host:::1`

) are handled correctly. Raises `ValueError`

if any of `host`

, `handshake`

, or `notify`

keys are absent or if the port values are non-numeric.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`


##

`pod_index(global_dp_rank, dp_size_local)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.pod_index)

Pod index (0-based) a global DP rank lives on for Wide-EP multi-pod.

`dp_size_local == 0`

(external-DP sentinel) collapses to a single pod.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`


##

`resolve_host_ip(extra_config)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.resolve_host_ip)

The IP this MoRIIO process advertises for KV transfer.

Honors an explicit `host_ip`

in `kv_connector_extra_config`

before falling back to `get_ip()`

. An external router/orchestrator can set it to the node's routable address; this is required under frameworks (e.g. Ray) where `get_ip()`

resolves to an unroutable public IP and `VLLM_HOST_IP`

cannot be propagated to the worker processes that bind the transfer engine.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_common.py`


##

`set_role(role)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.set_role)

##

`zmq_ctx(socket_type, addr)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.zmq_ctx)

Context manager for a ZMQ socket.