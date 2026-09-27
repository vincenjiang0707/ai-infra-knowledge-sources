# [Issue #4670] [MP] [Bug] Worker heartbeat stalls in degraded mode ~2 min after server restart (no connect timeout on the MQ client socket)

source: https://github.com/LMCache/LMCache/issues/4670
state: open | updated: 2026-09-17T17:32:53Z
labels: 

## 正文

**Summary**
MP worker heartbeat can stay in degraded mode ~2 minutes after a restarted cache server is already healthy, because the MQ client's ZMQ DEALER sets no connect timeout — a reconnect attempt whose SYN is silently dropped rides the OS TCP connect timeout (~127s on Linux), and KV re-registration (which only fires on the unhealthy→healthy heartbeat edge) is delayed by the same amount.

**Details**
Environment: MP mode on Kubernetes — vLLM with `LMCacheMPConnector`, cache server in a separate pod behind a ClusterIP Service (:5555), default `heartbeat_interval=10`.

When the server pod restarts, the pod flaps NotReady → Ready and Kubernetes removes/restores the Service endpoint. A zmq auto-reconnect attempt that races that window can have its SYN silently dropped (a conntrack entry is created with no DNAT; TCP SYN retransmits follow the same stale entry even after the endpoint is restored). Because `MessageQueueClient` sets no `zmq.CONNECT_TIMEOUT`, that single connect attempt inherits the OS default (~127s on Linux) and monopolizes the socket for the full window — stalling every pending request on it, including heartbeat PINGs — before zmq gives up, opens a fresh socket (new source port → new conntrack entry), and immediately succeeds.

We captured this live from `/proc/net/tcp` at failure time: one socket to the Service IP:5555 stuck in `SYN_SENT` while the same pod's second MQ client socket was simultaneously `ESTABLISHED` (a per-connection race, not node-wide networking). Re-registration then landed ~132s after server restore — the kernel connect timeout almost to the second. Reproduced identically on v0.5.2, v0.5.3, and v0.5.4 dev nightlies (~14% of our fault-tolerance e2e runs).

A second, compounding problem: the `HeartbeatThread` logs only health *edges* ("entering degraded mode" / "healthy again"), never individual ping failures — so the entire stall window is invisible in logs and very hard to diagnose from the field.

**Steps / Reproduction (if applicable)**
1. Deploy MP mode on Kubernetes: vLLM (`LMCacheMPConnector`) + cache server pod behind a ClusterIP Service.
2. Send a couple of requests so KV chunks are stored (the worker heartbeat starts on the first store).
3. Hold the server down for longer than one ping cycle — e.g. a Chaos Mesh `pod-failure` for 30s (the k8s analog of `run-restart-recovery.sh`) — then let it restore.
4. Watch the vLLM log and the server's registration state. Intermittently (~1 in 7 runs), no heartbeat line appears after "entering degraded mode" and re-registration takes ~130s instead of ~10s; `/proc/net/tcp` in the vLLM pod shows a socket to the Service IP:5555 in `SYN_SENT` (state `02`) during the stall.

**Expected Outcome / Goal**
After the server is back, the heartbeat recovers (and re-registers KV caches) within ~1–2 ping cycles; prolonged ping failures are visible in the log.

**Actual Outcome (if applicable)**
Recovery intermittently takes ~130s (bounded by the kernel TCP connect timeout, so worse on hosts with higher `tcp_syn_retries`), during which the worker serves in degraded mode with external hit rate 0 — and the log shows nothing between "entering degraded mode" and the eventual recovery.

**Additional Context**
Verified the mechanism with a pyzmq socket-monitor harness against a blackholed endpoint (SYN dropped, no RST): a stock DEALER emits one `connect_delayed` event and then wedges in `SYN_SENT` for the whole observation window; with `zmq.CONNECT_TIMEOUT=5s` + `zmq.RECONNECT_IVL_MAX=1s` it cycles `closed`/`retried` every ~5s and recovers within one attempt cycle once the server is back. PR with that fix (configurable as `lmcache.mp.connect_timeout`) plus throttled ping-failure logging incoming.

## 评论 (1)

### daitran-tensormesh · 2026-09-17

Scope update for anyone following this issue: per review on #4671, the PR now contains only the bounded connect (`zmq.CONNECT_TIMEOUT` + `zmq.RECONNECT_IVL_MAX` on the MQ client, `lmcache.mp.connect_timeout`, test, docs). The "second, compounding problem" above (the heartbeat logs only health edges, so a stall window is invisible) is **not** addressed by that PR: the `_failed_pings` counter and throttled per-ping logging were dropped as redundant. With the connect bounded, a stall is limited to a single missed ping, which makes the observability gap far less important. If maintainers still want ping-failure visibility, I am happy to open that as a separate, small follow-up rather than widen #4671.

