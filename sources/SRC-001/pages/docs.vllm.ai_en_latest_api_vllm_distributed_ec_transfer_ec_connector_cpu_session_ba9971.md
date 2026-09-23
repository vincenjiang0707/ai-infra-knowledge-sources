source: https://docs.vllm.ai/en/latest/api/vllm/distributed/ec_transfer/ec_connector/cpu/session/
lastmod: 2026-09-23

#

`vllm.distributed.ec_transfer.ec_connector.cpu.session`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session)

Session objects for the ECCPUConnector.

Layer hierarchy: connector → session → transport (connection)

Two long-lived sessions:

ProducerSession — owns ZmqServerTransport. The connector calls poll_step() once per engine step, which drains the transport without blocking and feeds the raw bytes to poll(). poll() decodes XferReqs, grants or NACKs them, pins source blocks, sends XferAck replies, drains NIXL completion notifications, and sweeps expired xfers.

ConsumerSession — owns one ZmqClientConnection and the NIXL agent registration for that peer. The connector calls poll(messages, now) once per engine step with the raw bytes collected for this peer. poll() decodes XferAcks, dispatches them to ConsumerXfer objects, and advances all active xfer state machines.

Internal data classes:

ProducerXfer — one pinned read grant, keyed by session_id. ConsumerXfer — state machine for one NIXL READ, keyed by mm_hash.

Classes:

-
–[ConsumerSession](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ConsumerSession)Long-lived per-producer session on the consumer side.

-
–[ConsumerSessionResults](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ConsumerSessionResults)Results from ConsumerSession.take_results().

-
–[ConsumerXfer](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ConsumerXfer)State machine for one NIXL READ on the consumer side.

-
–[ProducerSession](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ProducerSession)Long-lived producer session. Owns ZmqServerTransport.

-
–[ProducerXfer](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ProducerXfer)One pinned read grant on the producer side.

-
–[XferState](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.XferState)Lifecycle states of a single ConsumerXfer.


##

`ConsumerSession`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ConsumerSession)

Long-lived per-producer session on the consumer side.

Owns the ZMQ DEALER connection and the NIXL agent registration for one producer peer. The connector calls poll(messages, now) once per engine step with the raw bytes collected from this peer's DEALER socket.

poll() decodes XferAcks, dispatches them to the right ConsumerXfer, advances all active xfer state machines, and drains quarantined xfers. Results accumulate in internal sets; call take_results() to collect them.

Methods:

-
–[close](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ConsumerSession.close)Release all transfer handles, deregister NIXL peer, close connection.

-
–[on_peer_down](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ConsumerSession.on_peer_down)WAITING_ACK xfers → cancel (retry allowed); READING xfers → quarantine.

-
–[poll](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ConsumerSession.poll)Decode inbound XferAcks, dispatch to xfers, and advance all state machines.

-
–[start_xfer](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ConsumerSession.start_xfer)Create a ConsumerXfer and send the XferReq over the connection.

-
–[take_results](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ConsumerSession.take_results)Return and clear all accumulated results since the last call.


## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/session.py`


|
|

###

`_ensure_registered(metadata, mem_descriptor)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ConsumerSession._ensure_registered)

Register or re-register the peer in DataTransport. Returns agent_name.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/session.py`


###

`close()`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ConsumerSession.close)

Release all transfer handles, deregister NIXL peer, close connection.

Connection teardown is routed through the transport so the pooled connection is dropped in lock-step with the session — a session and its DEALER connection have a 1:1 lifecycle, so a later connect() to the same peer builds a fresh socket instead of handing back this dead one.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/session.py`


###

`on_peer_down()`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ConsumerSession.on_peer_down)

WAITING_ACK xfers → cancel (retry allowed); READING xfers → quarantine.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/session.py`


###

`poll(messages, now)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ConsumerSession.poll)

Decode inbound XferAcks, dispatch to xfers, and advance all state machines.

messages: raw bytes from ZmqClientTransport.poll() for this peer. Results accumulate until take_results() is called.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/session.py`


###

`start_xfer(mm_hash, block_indices, deadline)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ConsumerSession.start_xfer)

Create a ConsumerXfer and send the XferReq over the connection.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/session.py`


###

`take_results()`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ConsumerSession.take_results)

Return and clear all accumulated results since the last call.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/session.py`


##

`ConsumerSessionResults`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ConsumerSessionResults)

Results from ConsumerSession.take_results().

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/session.py`


##

`ConsumerXfer`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ConsumerXfer)

State machine for one NIXL READ on the consumer side.

transfer_handle is the in-flight NIXL handle returned by post_read() — used for check_xfer_state() / release_xfer_handle(). The dlist handle for the remote peer lives inside DataTransport, not here.

Methods:

-
–[cancel](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ConsumerXfer.cancel)Cancel a WAITING_ACK xfer (peer down). No tombstone — caller allows retry.

-
–[handle_ack](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ConsumerXfer.handle_ack)Issue the NIXL READ on an OK XferAck. Returns False on any NACK.

-
–[release](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ConsumerXfer.release)Force-release the transfer handle. Shutdown only.


## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/session.py`


|
|

###

`cancel()`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ConsumerXfer.cancel)

Cancel a WAITING_ACK xfer (peer down). No tombstone — caller allows retry.

###

`handle_ack(ack, agent_name)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ConsumerXfer.handle_ack)

Issue the NIXL READ on an OK XferAck. Returns False on any NACK.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/session.py`


###

`release()`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ConsumerXfer.release)

Force-release the transfer handle. Shutdown only.

##

`ProducerSession`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ProducerSession)

Long-lived producer session. Owns ZmqServerTransport.

poll_step() runs once per engine step: drains the transport without blocking, decodes XferReqs, grants or NACKs each one, drains NIXL completion notifications, and sweeps expired xfers.

Methods:

-
–[poll](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ProducerSession.poll)Decode and process inbound XferReqs, drain NIXL notifs, sweep timeouts.

-
–[poll_step](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ProducerSession.poll_step)Drain the transport without blocking and process what arrived.


## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/session.py`


|
|

###

`poll(messages)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ProducerSession.poll)

Decode and process inbound XferReqs, drain NIXL notifs, sweep timeouts.

messages: (identity, payload) pairs from ZmqServerTransport.poll().

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/session.py`


###

`poll_step()`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ProducerSession.poll_step)

##

`ProducerXfer`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.ProducerXfer)

One pinned read grant on the producer side.

Pure data — lifecycle operations (pin/unpin) are performed by ProducerSession. Keyed by (consumer_session_id, mm_hash) in ProducerSession._active_xfers.

## Source code in `vllm/distributed/ec_transfer/ec_connector/cpu/session.py`


##

`XferState`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.cpu.session.XferState)

Bases: [Enum](https://docs.python.org/3/library/enum.html#enum.Enum)

Lifecycle states of a single ConsumerXfer.