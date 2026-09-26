# [Issue #4099] [Bug]: RedisStoragePlugin set()/remove() report REDIS_REPLY_ERROR as success

source: https://github.com/kvcache-ai/Mooncake/issues/4099
state: closed | updated: 2026-09-15T03:38:40Z
labels: 

## 正文

### Environment

- Affects all versions where `RedisStoragePlugin` is built (`-DUSE_REDIS=ON`)
- Present as of commit d451255c on `main`

### Description

`RedisStoragePlugin::set()` and `RedisStoragePlugin::remove()` in
`mooncake-transfer-engine/src/transfer_metadata_plugin.cpp` treat any non-null reply as
success. They never inspect `reply->type`, so a `REDIS_REPLY_ERROR` — an error reply the
server deliberately sent — is reported to the caller as a completed write:

```cpp
redisReply *resp = execLocked("SET", key, ...);
if (!resp) return false;
freeReplyObject(resp);
return true;              // true even for -READONLY, -NOAUTH, -OOM, -MISCONF
```

The consequence is a silent write loss. `registerSegmentDesc()` and
`unregisterSegmentDesc()` see success, log nothing, and continue, while Redis holds no
new value. Remote peers then resolve a stale descriptor or none at all, and there is no
signal anywhere that the publish did not happen.

The most likely trigger is a **failover**. When a managed Redis promotes a replica, or a
load balancer briefly routes to one, the connection is healthy and the command is
rejected with `-READONLY`:

```
-READONLY You can't write against a read only replica.
```

`redisCommand()` returns a valid reply object in that case, so nothing in the current
code path notices. Other realistic cases are `-OOM` under `maxmemory`, `-MISCONF` when
RDB persistence is failing, and `-NOAUTH` if a reconnect lands on a server that requires
credentials the client does not have.

`get()` is affected differently but not silently: an error reply has a non-null `str`, so
it is passed to the JSON parser and surfaces as a misleading
`RedisStoragePlugin: JSON parse error` rather than as a backend error.

### Expected Behavior

A `REDIS_REPLY_ERROR` should be reported as failure, with the server's error string in
the log so `-READONLY` is distinguishable from a connection problem. `set()` and
`remove()` should return false, and `getWithStatus()` should map it to `kUnavailable`
rather than letting it reach the JSON parser.

Retrying is deliberately not the answer: the server answered, so the command was
received and rejected. Only the reporting is wrong.

### Steps to Reproduce

Point a node at a Redis replica, or set `maxmemory` low enough to force `-OOM`, and
register a segment:

    redis-cli -p <port> replicaof <host> <port>   # make it a replica
    # then trigger a segment registration on the node

`registerSegmentDesc()` returns success and logs nothing, but the key is absent from
Redis.

### Additional Context

Raised as a follow-up from the review of #4042, which fixed the connection-recovery half
of #4003 and left this reporting gap untouched to keep that diff focused. #4042 makes the
failover case slightly more reachable, since a reconnect can now land on a different
server than the original connection did.

I am happy to take this one.


## 评论 (2)

### github-actions[bot] · 2026-09-14

Thanks for opening this issue, @zuozhubinge!

| Field | Value |
|-------|-------|
| **Issue** | #4099 |
| **GitHub user ID** | `13146499` |
| **Reporter** | @zuozhubinge |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### he-yufeng · 2026-09-14

Fix up at #4107. Verified the report against current main and reproduced the silent-write path end to end: with a fake Redis answering -READONLY to every command, the stock class reports set()/remove() as success, and with the patch both fail loudly with the server's error string in the log. The healthy path (writes succeed, nil GET still maps to kNotFound) is unchanged.

One adjustment to the expected-behavior sketch: getWithStatus() on an error reply does land on kUnavailable today, but only by falling out of the JSON parser with a misleading log line. The PR makes that path explicit.

