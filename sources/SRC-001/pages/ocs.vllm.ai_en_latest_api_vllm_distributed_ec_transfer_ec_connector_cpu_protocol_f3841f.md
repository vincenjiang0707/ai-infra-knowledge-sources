source: https://docs.vllm.ai/en/latest/api/vllm/distributed/ec_transfer/ec_connector/cpu/protocol/
lastmod: 2026-09-23

#

`vllm.distributed.ec_transfer.ec_connector.cpu.protocol`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.protocol)

Scheduler-side wire types for the ECCPUConnector.

Two peer-to-peer message types exchanged between consumer and producer over ZMQ (XferReq, XferAck) plus a peer-compatibility fingerprint (compute_ec_compatibility_hash) sent on every XferReq so a producer refuses to serve a mismatched peer.

Classes:

-
–[XferAck](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.protocol.XferAck)Producer → Consumer: response to an XferReq.

-
–[XferReq](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.protocol.XferReq)Consumer → Producer: I want to READ mm_hash; pin it and tell me where.

-
–[XferStatus](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.protocol.XferStatus)Outcome the producer reports for an XferReq.


Functions:

-
–[compute_ec_compatibility_hash](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.protocol.compute_ec_compatibility_hash)Peer-compatibility fingerprint over the four factors that determine


##

`XferAck`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.protocol.XferAck)

Bases: `Struct`


Producer → Consumer: response to an XferReq.

On status == OK: producer has pinned source blocks and returns their indices plus fresh NIXL metadata for the consumer to register and READ. On any NACK_*: optional fields are empty; consumer falls back to local encode.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/protocol.py`


##

`XferReq`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.protocol.XferReq)

Bases: `Struct`


Consumer → Producer: I want to READ mm_hash; pin it and tell me where.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/protocol.py`


##

`XferStatus`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.protocol.XferStatus)

Bases: [IntEnum](https://docs.python.org/3/library/enum.html#enum.IntEnum)

Outcome the producer reports for an XferReq.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/protocol.py`


##

`compute_ec_compatibility_hash(vllm_version, model, dtype, block_size_bytes)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.protocol.compute_ec_compatibility_hash)

Peer-compatibility fingerprint over the four factors that determine byte-layout compatibility. Producer NACKs any XferReq whose hash differs.