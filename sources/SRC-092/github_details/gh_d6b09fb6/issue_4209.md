# [Issue #4209] [Bug][TE] TCP transport: first transfer after an idle gap fails with queue-full rejections; PD decode hangs until timeout

source: https://github.com/kvcache-ai/Mooncake/issues/4209
state: open | updated: 2026-09-18T03:16:14Z
labels: 

## 正文


## environment

- mooncake-transfer-engine **0.3.13.post1** (PyPI wheel); also reproduced on the **0.3.14rc1** release wheel
- vLLM 0.29.0 (built-in `MooncakeConnector`), 1 node, disaggregated prefill/decode (1P1D) on one host
- 2× NVIDIA H20 96GB (one GPU per instance), TCP transport (`mooncake_protocol: "tcp"`, `MC_FORCE_TCP=1`; RDMA path not usable on this host)
- Qwen/Qwen3-8B

## 🐛 Describe the bug

With the TCP transport, the **first KV transfer between two engine instances succeeds, but a transfer submitted after a short idle gap (~5 s) fails**: on the producer, every slice of the batch is rejected by the TCP lane queue (`TCP lane queue-full rejection count: 1 → 2 → 4 → ... → 512+` within milliseconds), `batch_transfer_sync_write` returns -1, and the error is relayed to the consumer (`pulling kv_caches for [...] failed: Mooncake transfer engine returned -1`).

The consumer request then stays in `WAITING_FOR_REMOTE_KVS` (`Deferred: 1`) and the client hangs until its own timeout. A request sent **~90 s later succeeds**, so deployments observe either 60-90 s TTFT spikes after every idle period or outright request failures, depending on client timeout.

## How to reproduce

1. Start P and D with the built-in vLLM `MooncakeConnector` over TCP (single host; any router that fires the prefill and decode requests concurrently works, e.g. `examples/disaggregated/mooncake_connector/mooncake_connector_proxy.py`):

```bash
# prefill (GPU 0)
vllm serve Qwen/Qwen3-8B --port 8111 --tensor-parallel-size 1 \
  --max-model-len 8192 --max-num-seqs 4 --max-num-batched-tokens 2048 \
  --gpu-memory-utilization 0.60 --no-enable-prefix-caching \
  --kv-transfer-config '{"kv_connector":"MooncakeConnector","kv_role":"kv_producer","kv_connector_extra_config":{"mooncake_protocol":"tcp"}}'
# decode (GPU 1)
vllm serve Qwen/Qwen3-8B --port 8112 --tensor-parallel-size 1 ... \
  --kv-transfer-config '{"kv_connector":"MooncakeConnector","kv_role":"kv_consumer","kv_connector_extra_config":{"mooncake_protocol":"tcp"}}'
```

2. Send a completion request through the router → **succeeds** (P logs `Sending to ... done, took 0.18 s`).
3. Wait ~5 s. Send it again → **hangs until client timeout**. P side:

```
W tcp_transport_lane_impl.h:1330] TCP lane queue-full rejection count: 1
W tcp_transport_lane_impl.h:1330] TCP lane queue-full rejection count: 2
... doubling up to 512+ within one millisecond ...
E mooncake_connector.py:1877] pulling kv_caches for ['cmpl-...'] failed: Mooncake transfer engine returned -1
```

4. Send it again ~90 s after step 3 → **succeeds again**.

Consistently reproduced on two machines (H20 and A100), multiple runs. Also reproduced with `MC_TCP_ADMISSION_TIMEOUT_MS=60000` (failure shape changes: the batch is not hard-rejected but still never transfers).

## Analysis

After a transfer completes and the peer connection group goes idle, the group is **retired** — all lanes are closed and `group->state` is set to `CLOSED` (`tcp_transport_lane_impl.h`, retirement block). A submission that arrives shortly after finds the group via `state->groups.find(key)`, sees `group->state != GroupState::OPEN`, and is **hard-rejected with `SHUTDOWN`** (`enqueuePooledTransfer`) instead of re-creating the group and its connections. The retired group is not removed from `state->groups` in the retirement path, so submissions keep failing until something re-creates the group — which matches the observed ~90 s self-heal.

Evidence summary:

- First transfer after engine start always succeeds; the failure only appears after an idle gap
- During the hang the four lane connections are `ESTABLISHED` with empty kernel queues → the stall is in TE user space (lane queue / admission), not the kernel
- Failure depends on the admission timeout (default 1 s fails immediately; 60 s still hangs) but recovery time (~90 s) is unchanged — consistent with a stale `CLOSED` group rather than a transient queue backlog

Suggested fix: in `enqueuePooledTransfer`, drop a non-`OPEN` group and re-create it (or remove retired groups from `state->groups` atomically when retiring) instead of rejecting the work.

## Workaround

Retry the request after ~90 s (self-healed), or keep the peer continuously busy (impractical). No configuration knob we found avoids it.


## 评论 (1)

### github-actions[bot] · 2026-09-18

Thanks for opening this issue, @CAICAIIs!

| Field | Value |
|-------|-------|
| **Issue** | #4209 |
| **GitHub user ID** | `39020005` |
| **Reporter** | @CAICAIIs |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.
