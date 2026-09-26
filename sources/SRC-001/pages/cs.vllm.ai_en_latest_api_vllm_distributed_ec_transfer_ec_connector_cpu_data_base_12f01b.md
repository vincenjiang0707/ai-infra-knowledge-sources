source: https://docs.vllm.ai/en/latest/api/vllm/distributed/ec_transfer/ec_connector/cpu/data/base/
lastmod: 2026-09-24

#

`vllm.distributed.ec_transfer.ec_connector.cpu.data.base`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.data.base)

Abstract base class for the EC data-plane transport (NIXL/UCX).

Classes:

-
–[DataTransport](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.data.base.DataTransport)Interface wrapping the NIXL data-plane for EC block transfers.


##

`DataTransport`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.data.base.DataTransport)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Interface wrapping the NIXL data-plane for EC block transfers.

## Peer lifecycle

add_remote_peer() — register a peer and store its dlist handle internally remove_remote_peer() — deregister and release the stored handle post_read() — issue a READ using the stored handle for agent_name

The dlist handle (prepped xfer descriptor list) is an implementation detail of the transport and is never exposed to callers.

Methods:

-
–[add_remote_peer](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.data.base.DataTransport.add_remote_peer)Register a remote peer, prep its READ-source dlist, and return agent_name.

-
–[check_xfer_state](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.data.base.DataTransport.check_xfer_state)Return the NIXL state string: 'DONE', 'PROC', or an error string.

-
–[deregister](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.data.base.DataTransport.deregister)Deregister all memory and tear down the NIXL agent.

-
–[get_agent_metadata](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.data.base.DataTransport.get_agent_metadata)Return this agent's serialized NIXL metadata blob.

-
–[get_mem_descriptor](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.data.base.DataTransport.get_mem_descriptor)Return the msgpack-encoded block descriptor list for this agent.

-
–[get_new_notifs](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.data.base.DataTransport.get_new_notifs)Drain NIXL completion notifications addressed to this agent.

-
–[post_read](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.data.base.DataTransport.post_read)Issue a consumer-initiated READ using the stored dlist for agent_name.

-
–[release_xfer_handle](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.data.base.DataTransport.release_xfer_handle)Release a transfer handle returned by post_read.

-
–[remove_remote_peer](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.data.base.DataTransport.remove_remote_peer)Deregister a previously registered remote peer and release its handle.


## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/data/base.py`


###

`add_remote_peer(metadata, mem_descriptor)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.data.base.DataTransport.add_remote_peer)

Register a remote peer, prep its READ-source dlist, and return agent_name.

The dlist handle is stored internally and used by post_read().

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/data/base.py`


###

`check_xfer_state(handle)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.data.base.DataTransport.check_xfer_state)

###

`deregister()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.data.base.DataTransport.deregister)

###

`get_agent_metadata()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.data.base.DataTransport.get_agent_metadata)

###

`get_mem_descriptor()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.data.base.DataTransport.get_mem_descriptor)

###

`get_new_notifs()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.data.base.DataTransport.get_new_notifs)

###

`post_read(local_indices, agent_name, remote_indices, notif_msg)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.data.base.DataTransport.post_read)

Issue a consumer-initiated READ using the stored dlist for agent_name.

Returns a transfer handle for use with check_xfer_state / release_xfer_handle.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/data/base.py`


###

`release_xfer_handle(handle)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.data.base.DataTransport.release_xfer_handle)

###

`remove_remote_peer(agent_name)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.data.base.DataTransport.remove_remote_peer)

Deregister a previously registered remote peer and release its handle.