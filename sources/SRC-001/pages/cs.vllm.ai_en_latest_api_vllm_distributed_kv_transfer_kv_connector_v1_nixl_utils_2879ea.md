source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/nixl/utils/
lastmod: 2026-09-24

#

`vllm.distributed.kv_transfer.kv_connector.v1.nixl.utils`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.nixl.utils)

Shared constants, lazy imports and helpers for the NIXL connector.

Functions:

-
–[get_base_request_id](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.nixl.utils.get_base_request_id)Strip the per-request

`-<8 hex>`

randomization suffix, if present. -
–[zmq_ctx](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.nixl.utils.zmq_ctx)Context manager for a ZMQ socket.


##

`get_base_request_id(request_id)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.nixl.utils.get_base_request_id)

Strip the per-request `-<8 hex>`

randomization suffix, if present.

##

`zmq_ctx(socket_type, addr)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.nixl.utils.zmq_ctx)

Context manager for a ZMQ socket.