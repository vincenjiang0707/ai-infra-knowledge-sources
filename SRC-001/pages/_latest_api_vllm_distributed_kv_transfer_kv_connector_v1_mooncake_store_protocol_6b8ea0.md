source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/protocol/
lastmod: 2026-09-23

#

`vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.protocol`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.protocol)

Wire-format constants for the LookupKey ZMQ admin channel.

This is the single source of truth shared by `LookupKeyClient`

and `LookupKeyServer`

on the scheduler<->worker rank-0 admin channel.

Wire format (REQ/REP over IPC):

```
Request: [msg_type: bytes] [payload_frames...]
msg_type == LOOKUP_MSG:
frame 1: num_tokens (u32 big-endian, 4 bytes); the worker derives
the aligned lookup length
frame 2: hash_len (u16 big-endian, 2 bytes) — byte length of each
fixed-size block hash (0 when there are no hashes)
frame 3: raw block hashes concatenated back-to-back (each hash_len
bytes); the server splits on hash_len
Response: hit_length (u32 big-endian, first 4 bytes), followed by zero
or more 8-byte tail-key boundaries. Each entry is group_id
(u32), then boundary_tokens (u32).
msg_type == RESET_MSG:
(no payload frames)
Response: [RESP_OK] or [RESP_ERR]
```


The first frame of every request is a named bytes tag (not a numeric sentinel that aliases the data field) so the protocol stays self-describing and extensible: adding new admin commands requires only a new tag and a new dispatch branch.

Mirrors the named-tag convention used by the NIXL connector (see `vllm/distributed/kv_transfer/kv_connector/v1/nixl/metadata.py`

).