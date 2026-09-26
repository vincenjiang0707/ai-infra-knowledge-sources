# [Issue #4174] [Bug][TENT] First RPC to a peer after it goes away fails: the pool cannot tell an idle connection is dead

source: https://github.com/kvcache-ai/Mooncake/issues/4174
state: open | updated: 2026-09-17T13:29:35Z
labels: 

## 正文

**Summary**

A pooled RPC connection whose peer is gone fails the first call after that, with
`io_error: End of file`. The pool flushes on that failure and the next attempt
succeeds, so the retry is left to each caller — and not every caller retries.
Reproduced with a real peer process restarted at the same address, so a peer
restart, or an idle connection dropped by the network, costs the first RPC to
that address in production too.

It surfaced as a flake in `tent_hp_tcp_transport_test`:
`WriteAndSlicedRead/HighPerformanceTcpLaneDistributionTest.InterleavedPeersUseEveryConfiguredLane/1`
fails at `client.submitTransferTasks(batch, {request}).ok()`
(`hp_tcp_transport_test.cpp:893`).

**Reproduction**

*Production-shaped.* A two-mode binary: `server <port>` runs a `ControlService`
peer in its own process on a fixed port; `client <port>` fetches a descriptor,
waits, then fetches twice more, keeping its connection pool across the restart.
The driver starts the peer, runs the client, `kill -9`s the peer, starts a new
peer on the same port, and lets the client continue. Upstream code, no patch:

```
BEFORE_RESTART      ok=1 msg=OK
FIRST_AFTER_RESTART ok=0 msg=RpcServiceError: Failed to call RPC function. server: 127.0.0.1:40123, func_id: 1, message: End of file
SECOND_AFTER_RESTART ok=1 msg=OK
```

*Test-shaped and quicker.* The same failure appears when a segment server's
ephemeral port is reused inside one process:

```bash
cmake -G Ninja -B build-tent -DUSE_TENT=ON -DUSE_HTTP=ON -DBUILD_UNIT_TESTS=ON \
  -DBUILD_EXAMPLES=ON -DENABLE_DEBUG_SYMBOLS=OFF -DUSE_CUDA=OFF -DUSE_UB=ON \
  -DCMAKE_BUILD_TYPE=Debug
cmake --build build-tent --target tent_hp_tcp_transport_test -j128
cd build-tent/mooncake-transfer-engine/tent/tests
./tent_hp_tcp_transport_test \
  --gtest_filter='*InterleavedPeersUseEveryConfiguredLane/1' --gtest_repeat=300
```

A fresh process passes (0 failures in 100 runs) because its pool is empty;
repeating inside one process fails 142 of 300 iterations.

**Root cause**

The pool is keyed by `server_addr` (`tent/include/tent/rpc/rpc.h:119`) and lives
on a `CoroRpcAgent`, which for `ControlClient` is process-wide, so an entry
outlives its peer. Client-side trace of the production-shaped run:

```
CALL      server=127.0.0.1:40123 fid=1 from_pool=0 closed_at_acquire=0
CALL      server=127.0.0.1:40123 fid=1 from_pool=1 closed_at_acquire=0
CALL_FAIL server=127.0.0.1:40123 from_pool=1 closed_at_acquire=0 errc=1 msg=End of file
CALL      server=127.0.0.1:40123 fid=1 from_pool=0 closed_at_acquire=0
```

Every failure uses a pooled connection (33 of 33 over 200 repeated runs), and
`coro_rpc_client::has_closed()` was false each time, so the pool cannot tell that
an idle connection's peer is gone.

**Impact**

`rpc_reconnect_test.cpp` pins the contract
(`StalePoolIsFlushedSoTheNextCallSucceeds`, `AFailedCallIsNotRetried`), which puts
the retry on each caller:

| call site | retries today |
| --- | --- |
| `TcpTransport` send/recv (`tcp_transport.cpp:284,288`) | yes, `max_retry_count` loop |
| `RdmaEndPoint` bootstrap (`endpoint.cpp:514`) | yes |
| notifications (`transfer_engine_impl.cpp:2543`) | yes, retried every pass |
| `PeerSegmentRegistry::getSegmentDesc` (`segment_registry.cpp:73`) | no |
| `ub_transport.cpp:478`, `proxy_manager.cpp:286,301,312` | to confirm |

A retry inside the RPC layer is not available: `End of file` does not say whether
the peer ran the handler, which is why `AFailedCallIsNotRetried` uses a
side-effecting handler.

**Open questions**

- Is "every caller retries once" the contract? If yes, the call sites above
  without a retry are bugs. One retry in the descriptor fetch makes the
  production-shaped run report `FIRST_AFTER_RESTART ok=1`, and turns 142/300 into
  0/300.
- Should the failure be distinguishable? A peer that answered with an error and a
  peer that dropped the connection both arrive as `RpcServiceError`, so a caller
  cannot retry only the safe case.
- Is revalidating on acquire viable? `has_closed()` cannot detect it (0/33) and
  `coro_rpc_client` exposes no socket, so it would need a keepalive on idle
  connections or an upstream hook.
- Should a pool entry be dropped when its address is rebound by a different
  server, so a new peer cannot inherit a stale connection?


## 评论 (3)

### github-actions[bot] · 2026-09-17

Thanks for opening this issue, @CAICAIIs!

| Field | Value |
|-------|-------|
| **Issue** | #4174 |
| **GitHub user ID** | `39020005` |
| **Reporter** | @CAICAIIs |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### CAICAIIs · 2026-09-17

**Plan**

I'd rather fix this by moving the retry down a layer than by adding one to every
caller. Three PRs:

- PR1: give "the peer never answered" its own status code. Today it lands in
  `RpcServiceError` together with "the peer answered with an error", and the layer
  already computes the difference (`peerAnswered()`), it just throws it away. No
  behavior change. PR2 needs it.

- PR2: take the connection pool out of `CoroRpcAgent`. The pool sits in a class that
  is also the server, so server instances carry a client pool they never use. Move
  the pool, the generation flush and the "only a successful call goes back to the
  pool" rule into the client-side layer for one address, and decide per RPC whether
  a repeat is safe, next to the wire format: reads and bootstrap yes, `notify`,
  `delegate`, `sendData`, `unpin` no. Then the retry exists once and no caller needs
  to know about it. The 15 `ControlClient` methods and their ~30 call sites stay as
  they are, and the retry I added in `PeerSegmentRegistry` goes away.

- PR3: split `CoroRpcAgent` into server and client. It does both today
  (`registerFunction`/`start`/`process` and `call`/`callAsync`). Cheaper once PR2
  has removed the pool. Five tests construct it directly.

Don't break in PR2: pools are per thread (the client agent is `thread_local`), the
flush drops the whole pool but only for the generation the caller drew from, and
the async paths stay fire-and-forget with no retry. `rpc_reconnect_test` covers
these.

If CI has to be green before PR2, the one-attempt retry in the descriptor fetch can
go in first; PR2 deletes it.

### KashmirAwana · 2026-09-17

Looks like the connection pool isn't detecting when a peer goes away, leading to the first RPC call failing after a peer restart. I'd check how the pool determines connection health.

