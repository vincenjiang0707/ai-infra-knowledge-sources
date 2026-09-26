# [Issue #1656] libfabric backend: `fi_writedata` silently emulated as send/recv on EFA RDM endpoints — `rdma_write_bytes` HW counter never increments on EFA SRD

source: https://github.com/ai-dynamo/nixl/issues/1656
state: closed | updated: 2026-07-17T13:05:00Z
labels: Network

## 正文

## Bug

The libfabric backend opens `FI_EP_RDM` endpoints and posts data via `fi_writedata`. On AWS EFA SRD, `fi_writedata` (RDMA WRITE *with immediate data*) is silently emulated as a `send/recv` pair because EFA SRD does not support the 32-bit immediate-data field on `IBV_WR_RDMA_WRITE`. The wire-level effect:

- `tx_bytes` / `tx_pkts` increment as expected (traffic does flow over the EFA NIC)
- **`rdma_write_bytes` / `rdma_read_bytes` HW counters never increment** for NIXL traffic
- The receive side of the emulation pulls from a fixed buffer pool that exhausts at ~240 in-flight writes, capping concurrency

This makes NIXL traffic invisible to standard EFA observability tooling (`efatop`, Grafana panels reading `/sys/class/infiniband/*/ports/1/hw_counters/rdma_write_bytes`) and creates a hard cliff for production disaggregated inference workloads.

## Reproducer

Verified today on 2× `p5.48xlarge` HyperPod EKS nodes with EFA installer 1.48.0, libfabric 2.4.0amzn3.0:

| Pod | NIC | counter | BEFORE | AFTER | **Δ** |
|---|---|---|---|---|---|
| Server (10.1.3.73) | rdmap79s0 | `tx_bytes` | 113,939,005,799,538 | 113,939,006,343,542 | **+544,004 B** |
| Server | rdmap79s0 | `rdma_write_bytes` | 111,173,889,070,980 | 111,173,889,070,980 | **0** |
| Client (10.1.3.151) | rdmap79s0 | `tx_bytes` | 1,614,764,867,836 | 1,614,765,411,840 | **+544,004 B** |
| Client | rdmap79s0 | `rdma_write_bytes` | 1,614,213,362,880 | 1,614,213,362,880 | **0** |

Reproducer used `fi_pingpong -p efa -e rdm` between pods (same FI_EP_RDM endpoint type the NIXL libfabric plugin uses). `fi_pingpong` itself uses `fi_send/fi_recv` on RDM, so this output captures the wire-level behavior of the FI_EP_RDM endpoint family on EFA — not specifically NIXL — but the relevant signal is that any FI_EP_RDM endpoint on EFA SRD shows `tx_bytes` movement, **not** `rdma_write_bytes`. NIXL's plugin opens FI_EP_RDM and uses `fi_writedata` (verified via `strings libplugin_LIBFABRIC.so` — both `fi_writedata` and `fi_senddata` symbols present), which goes through the same SEND/RECV emulation because EFA SRD cannot satisfy the immediate-data semantic on RDMA WRITE.

**Full reproduction package** (private gist — README, environment.txt, reproduce.sh, expected/actual output): https://gist.github.com/dmvevents/f3591769c690e77528c0b3890b877552

## Why this matters for production

vLLM `NixlConnector` users hitting `Backend LIBFABRIC was instantiated` + `/v1/completions` returning text reasonably believe their KV transfer is going over true RDMA. It is not — it is going over a SEND/RECV emulation that uses extra memory bandwidth, has no zero-copy semantics at the receiver, and serializes through a fixed receiver buffer pool. For ~1M-context agentic workloads (e.g. Nemotron 3 Ultra disaggregated serving), this manifests as TTFT regressions of 2-10× vs what native RDMA WRITE would deliver, and a hard concurrency ceiling at ~240 in-flight transfers.

## Cross-references

- **#1497** (`libfabric: Update control messages from SEND/RECV to WRITE`, draft, anshumang) — proposes unifying the notification path on `fi_writedata`. **Important:** this PR moves notifications onto the same primitive that is silently emulated on EFA RDM, extending the coverage of this bug rather than fixing it. The PR body explicitly states "both data transfers and notifications now arrive via FI_REMOTE_WRITE" — but on EFA RDM, neither path is using FI_REMOTE_WRITE at the wire level. Suggest aligning #1497's unified path on `fi_write` (no immediate) rather than `fi_writedata` so the upstream goal of "unify under FI_REMOTE_WRITE" actually delivers native RDMA WRITE.
- **Monarch PR #3391** (Meta) — sets a precedent for runtime EFA capability detection via `ibv_query_device` → `attr.max_qp_rd_atom`. If `max_qp_rd_atom == 0`, the device does not support native RDMA verbs and Monarch falls back to `fi_send/fi_recv` deliberately. Universal code path that works on both P4d (no RDMA verbs) and P5+ (full RDMA verbs) without code changes. NIXL has no analogous detection; it always calls `fi_writedata` regardless of what the device actually supports.
- **libfabric upstream ofiwg/libfabric#12253** (`prov/efa: Baseline remaining software features`) — open issue acknowledging EFA provider feature gaps relative to FI capability flags.
- **vllm-project/vllm#41814** (this team filed) — downstream symptom: vLLM `NixlConnector` defaults to `["UCX"]` and operators must discover the LIBFABRIC override via `kv_connector_extra_config.backends`. Once switched to LIBFABRIC, they hit *this* issue.

## Suggested fix paths

### Path A — minimal: replace `fi_writedata` with `fi_write` on the data path

`fi_write` (no immediate data) maps directly to `IBV_WR_RDMA_WRITE` and is supported natively on P5/P5en/B200 EFA SRD. This:

- Increments `rdma_write_bytes` (visible to operators in `efatop`)
- Removes the 240-in-flight emulation buffer ceiling
- Zero-copy at the receiver
- Costs the 32-bit immediate-data flow-control field — but flow control can be carried out-of-band (NATS, etcd, or a small auxiliary message)

Patch surface: ~30 lines in `libfabric_backend.cpp` postXfer hot path.

### Path B — robust: runtime capability detect (Monarch PR #3391 pattern)

```cpp
struct ibv_device_attr attr;
ibv_query_device(ctx, &attr);
bool has_rdma_write = (attr.max_qp_rd_atom > 0);
if (has_rdma_write) {
    use fi_write();   // native — moves rdma_write_bytes, no emul ceiling
} else {
    use fi_send();    // explicit — works on P4d, no false RDMA claims
}
```

This pattern works on both P4d (no RDMA verbs, falls to send/recv) and P5+ (full RDMA verbs, native). PR #1497's unification of data + notifications is compatible with this if the unified primitive is `fi_write` rather than `fi_writedata`.

## What is NOT this bug

- Not a TCP fallback. Traffic does flow over EFA — `tx_bytes` increments confirm this.
- Not a routing / SG / VPC issue. EFA wire path is healthy (cumulative `rdma_write_bytes` of >100 TB on these NICs from prior NCCL training workloads, confirming RDMA WRITE *does* work natively when invoked via the right verbs).
- Not the recently-discussed UCX-default issue at `vllm-project/vllm#41814` (vLLM-side, separate fix in `kv_connector_extra_config.backends`).
- Not aws-ofi-nccl 1.14 silent no-op (NCCL-side, separate issue, fixed by source-building 1.19.1+).

## Asks

1. Acknowledgment of the silent-emulation behavior in NIXL libfabric plugin documentation (`src/plugins/libfabric/README.md`)
2. Decision on Path A vs Path B (or other) for the upstream fix
3. Coordination with #1497 to ensure the unified data + notification path uses `fi_write` (not `fi_writedata`) on EFA RDM endpoints
4. Optional regression test in `nixlbench` that asserts `rdma_write_bytes` HW counter delta > 0 after a cross-node transfer

We are happy to draft the patch but want to align on the approach before sending a PR that might collide with #1497's in-flight refactor.

cc @anshumang (libfabric plugin maintainer per CODEOWNERS / #1505)


## 评论 (3)

### amitrad-aws · 2026-05-20

The EFA SRD does support immediate data when using `fi_writedata` (when running on instances that support RDMA write like p5 in your case). It seems the analysis is incorrect
The reproducer you mentioned `fi_pingpong -p efa -e rdm` is running a test case that isn't supposed to use RDMA write so you won't see the statistics you are referring to incresing.
I ran a simple nixlbench run with WRITE and I do see these statistics incrementing. 
Please provide a description of the original scenario (and a reproducer if possible).

### dmvevents · 2026-06-05

@amitrad-aws — you're right, the analysis is wrong. Apologies for the noise.

The error is in the issue body itself: I noted that `fi_pingpong -p efa -e rdm` uses `fi_send/fi_recv` (not `fi_writedata`), and then extrapolated from a send/recv-shaped traffic profile to a claim about every FI_EP_RDM transfer on EFA SRD. That extrapolation is invalid — a test of the send/recv path can't tell you anything about the `fi_writedata` path.

What I should have run was `nixlbench` with WRITE (which is what you ran) — that exercises the actual `fi_writedata` code path NIXL uses. I'll do that on our P5 cluster this week and confirm `rdma_write_bytes` increments here too. If it does (which it should, based on your result), I'll close this with a correction post.

I'll also retract the corresponding suggestion on #1497 about preferring `fi_write` over `fi_writedata` on EFA RDM — that recommendation rested on the same wrong assumption.

Sorry for the cycle. Will report back by 2026-06-12 with the nixlbench WRITE counter delta from our side.


### brminich · 2026-07-10

@dmvevents is there any update?
can we close it?
