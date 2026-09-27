# [Issue #4337] [RFC][Store] Offline timestamped master RPC trace replay

source: https://github.com/kvcache-ai/Mooncake/issues/4337
state: open | updated: 2026-09-26T17:14:58Z
labels: 

## 正文

## Problem

Running a serving simulator and a Mooncake master together on a CPU-only host makes their CPU and memory contention part of the measurement. A saved sequence of master calls lets us stop the producer, repeat the same offered workload against a dedicated master, and inspect metadata pressure and background eviction separately from model execution and KV payload transfers.

The proposed addition accepts an external timestamped RPC-intent trace. It does not require or vendor SGLang, a model, a simulator fork, or generated workloads in Mooncake.

## Related work and scope

- The Store Master Benchmark item in #1035 motivates reproducible master evaluation.
- Open PR #3147 generates configurable, stateful synthetic traffic at runtime, including Poisson arrivals and committed-key pools. This proposal addresses a different input contract: replaying an already-produced sequence with its timestamps, physical keys, batch boundaries and completion dependencies. It also adds a launcher that measures a dedicated master. Both approaches can be useful; this is not a replacement for that PR.
- Open PR #3665 provides an in-process master for local tests/evaluation. This proposal uses the existing MasterClient RPC path and a separate master process, with independent CPU affinity and process measurements.

## Proposed design

1. A versioned JSONL contract describes logical clients, keys, object/slice sizes, relative microsecond timestamps, and dependencies. Version 2 separates setup, workload and teardown, with a completion barrier between phases. Storage clients mount capacity independently of request-only clients.
2. A C++ executable uses the existing MasterClient APIs for registration, mount/unmount, Exist, replica lookup, PutStart/End/Revoke and Remove. A bounded worker pool dispatches due events once dependencies complete. It preserves scheduled timestamps under overload so queueing remains visible. End/Revoke only finalize keys for which the corresponding Start succeeded.
3. Heartbeats run in a separate bounded pool. Failed heartbeats invalidate the run; the benchmark does not silently remount a failed client. The launcher owns process startup and cleanup.
4. A standard-library Python launcher validates the trace, starts a loopback-only master, applies disjoint CPU affinity, and samples process CPU/RSS and existing Prometheus metrics. Outputs distinguish planned, sent and completed calls, per-key statuses, client-call latency, dispatch lag and lifecycle phases. The manifest records commands, settings and input/binary hashes.
5. Capacity-pressure experiments retain mounted capacity and grow the producer's working set. The real master's background eviction chooses victims. An optional assertion requires eviction during workload; incomplete-write timeout/discard/release activity is reported separately. Explicit timeout overrides support controlled experiments.

Fake segment addresses represent logical capacity only: no KV payload is allocated or transferred. Use a fresh, dedicated master. The trace is fully parsed before timed replay; memory use grows with trace size. Summary generation avoids copying the full event trace for each phase.

## Boundaries and alternatives

This is fixed-intent replay, not a closed-loop serving simulator. Actual misses and errors can differ from the producer's state; RPC latency does not feed back into future request generation. Logical GPU counts are provenance, not throughput calibration. Shared memory bandwidth and host contention remain possible even with disjoint CPU affinity.

The initial contract excludes HA recovery, topology changes during workload, transfers, placement/pinning policies and disk replicas. Producers must not silently discard such semantics. A small handwritten example and deterministic test fixtures are included; generated traces and framework adapters remain external.

A Python-only driver would need suitable direct master bindings; the existing C++ MasterClient provides the required metadata APIs without bringing a serving framework or payload path into the benchmark. The runtime synthetic workload in #3147 remains a complementary approach when no recorded trace is available.

## Validation and review

The implementation branch is [benchmark/master-rpc-trace-replay](https://github.com/CHiSwsz/Mooncake/tree/benchmark/master-rpc-trace-replay). It contains benchmark code, documentation and tests only; production master code and RPC schemas are unchanged.

Validation covers parser rejection, dependency scheduling, overload lag, phase barriers, partial writes, multiple slices per object, real-master lifecycle and heartbeat handling, workload-only metrics, and background eviction on an external fixed-capacity trace.

Feedback is welcome on the trace contract, overlap with other benchmark tooling, and whether this should remain a separate target or later share common launcher/reporting infrastructure.

AI assistance: Codex assisted with implementation, tests, documentation and this RFC. Human line-by-line review is pending and will remain explicit in the draft PR.


## 评论 (1)

### github-actions[bot] · 2026-09-26

Thanks for opening this issue, @CHiSwsz!

| Field | Value |
|-------|-------|
| **Issue** | #4337 |
| **GitHub user ID** | `94686251` |
| **Reporter** | @CHiSwsz |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.
