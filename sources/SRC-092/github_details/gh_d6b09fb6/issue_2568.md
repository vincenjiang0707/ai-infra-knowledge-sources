# [Issue #2568] [RFC]: Traffic class hint API for TransferEngine — bridging upper-layer semantics (KV / EP / CTRL) to lower-layer SL/TC

source: https://github.com/kvcache-ai/Mooncake/issues/2568
state: open | updated: 2026-09-25T03:14:21Z
labels: stale

## 正文

## Summary

Extend the `SelectionContext` introduced in #2079 with a `traffic_class` field, allowing callers to express *application semantics* (KV-cache transfer vs. EP all-to-all vs. control-plane RPC) so the engine can map them to the *link-layer resources* (SL / TC / QP pool) already exposed by #1187, #2525, and #2526.

This RFC does **not** introduce a new abstraction — it adds one orthogonal dimension to an existing struct.

## Motivation

Three independent pieces of work over the last six weeks have converged on "different traffic types should use different NIC resources", but the convergence is happening *only at the link layer*:

| Project | Knob | Layer |
|---|---|---|
| NCCL v2.30.7 | `NCCL_GIN_IB_TC` (separate TC for GIN control vs. data) | env var |
| Mooncake #1187 | `MC_IB_TC` (global RDMA traffic class) | env var |
| Mooncake #2525 | `MC_IB_SL` (global RDMA service level) | env var |
| Mooncake #2526 | SL/TC applied to the notification QP | code |

All four expose **link-layer knobs with global scope** — one value per process, applied to every transfer regardless of its purpose. There is currently no way for a caller to say:

> "This `submitTransfer` carries a KV write on the TTFT critical path; that one is an EP dispatch background flow; the third is a heartbeat."

The link layer is therefore forced into one of three suboptimal modes:

1. Static one-size-fits-all (today): all flows share the same SL/TC, contention is unmanaged.
2. Per-process pinning via env vars: requires running multiple `TransferEngine` instances to differentiate flows, wasting resources.
3. Caller-provided raw SL/TC: leaks link-layer details into vLLM / SGLang / DeepEP, violating layering.

The orthogonal SGLang RFC sgl-project/sglang#28631 plumbs **priority** (`CRITICAL` / `BACKGROUND` / `IDLE`) through the Python data path. As that RFC explicitly notes, priority decides *when* a transfer is sent (queue order); it does **not** decide *which NIC channel* it uses. The traffic-class dimension proposed here covers the latter and is independently meaningful.

## Proposed change

Extend `SelectionContext` (mooncake-transfer-engine/tent/include/tent/runtime/transport_selector.h, introduced in #2079) with one optional field:

```cpp
enum class TrafficClass : uint8_t {
    DEFAULT          = 0,   // unspecified — preserve current behavior
    KV_PUT           = 1,   // P→D KV write, latency-critical
    KV_GET           = 2,   // D pull from prefix cache
    KV_LOOKUP_META   = 3,   // small control RPC for KV metadata
    EP_DISPATCH      = 4,   // MoE expert-parallel forward all-to-all
    EP_COMBINE       = 5,   // MoE expert-parallel backward all-to-all
    CTRL             = 6,   // heartbeat, handshake, restart detection
    USER_DEFINED_BASE = 128 // reserved for downstream extension
};

struct SelectionContext {
    SegmentType segment_type;
    bool same_machine;
    MemoryType local_memory_type;
    MemoryType remote_memory_type;
    const std::vector<TransportType>* buffer_transports;
    size_t transfer_size;
    int priority_level;
    std::optional<std::string> policy_name;

    // NEW: caller's semantic intent for this transfer
    TrafficClass traffic_class = TrafficClass::DEFAULT;
};
```

`SelectionPolicy` gains an optional `traffic_class_filter` (mirroring how `priority` is already filtered today), and `TransportSelector` consults it during rule matching. **No new top-level concepts** — the dispatch path, JSON config schema, and rule-evaluation logic all stay as #2079 left them.

A default mapping table (overridable via `MC_TRAFFIC_CLASS_SL_MAP` env var, mirroring `NCCL_GIN_IB_TC`):

| TrafficClass     | Default SL | Default TC | Default QP pool         |
|------------------|------------|------------|-------------------------|
| `DEFAULT`        | 0          | 0          | data QP (current)       |
| `KV_PUT`         | TBD        | TBD        | data QP                 |
| `KV_GET`         | TBD        | TBD        | data QP                 |
| `KV_LOOKUP_META` | TBD        | TBD        | data QP                 |
| `EP_DISPATCH`    | TBD        | TBD        | data QP                 |
| `EP_COMBINE`     | TBD        | TBD        | data QP                 |
| `CTRL`           | TBD        | TBD        | data QP                 |

All SL/TC values are deployment-specific (depend on switch VL-to-SL mapping and PFC configuration) and intentionally left as TBD here. The table goes through `SelectionPolicy` JSON like any other rule, so operators override per fabric. The only hard semantic is `DEFAULT = 0/0` (preserves current behavior).

## Five questions the RFC must answer

**Q1. Enum boundary — first-class vs. user-defined?**
First-class: the seven values above (covering current Mooncake / vLLM / SGLang / DeepEP traffic). Extension: `USER_DEFINED_BASE = 128` reserves the upper half of `uint8_t` for downstream projects (e.g., training frameworks adding `GRAD_ALLREDUCE`) without forcing them through this RFC.

**Q2. Who injects the hint?**
Both — caller-explicit *and* transport-inferred default. Existing call sites continue to work (default = `DEFAULT` = current behavior). New call sites in vLLM `MooncakeStoreConnector`, SGLang `disaggregation/mooncake/conn.py`, and DeepEP V2 elastic buffer (#2503) opt in by passing the hint at `submitTransfer`. Transport may infer a default when caller leaves it `DEFAULT` (e.g., notification-QP path defaults to `CTRL`).

**Q3. How is `TrafficClass` mapped to `(SL, TC, QP_pool)`?**
Built-in default table (above) + per-deployment override via JSON `SelectionPolicy` (already supported by #2079) + env var `MC_TRAFFIC_CLASS_SL_MAP` for quick experiments (mirroring `NCCL_GIN_IB_TC` ergonomics). No new mechanism.

**Q4. Relationship with #2525 / #2526 dual-QP?**
#2526 makes the notification QP's SL/TC configurable (previously hard-coded to 0). Once #2526 lands, a natural follow-up question is: *who decides which transfers go through the notification QP vs. the data QP?* Today that decision is implicit (only handshake/notify messages use the notification QP). This RFC makes it explicit: `TrafficClass` becomes the decision input. For example, a deployment *could* configure `CTRL` to route through the notification QP — but the default mapping keeps all traffic on the data QP to preserve current behavior. The RFC does not mandate notification-QP routing; it only provides the signal that *enables* it as a policy choice.

**Q5. Telemetry?**
Per-NIC × per-class counters: `mooncake_te_traffic_class_in_flight_bytes{nic, class}`, `_completed_count`, `_error_count`. Reuses existing Mooncake metrics naming convention; existing dashboards consume the new dimension by adding one label.

## Anticipated concerns

**"Why not let callers pass SL/TC directly?"**
SL/TC are link-layer resources whose allocation is a fabric / operator concern. Applications should express *intent* (KV vs. EP vs. CTRL); the transport layer + operator config decide the *implementation*. This is the same split as DiffServ DSCP at the IP layer (apps tag class, routers map to queues) and `NCCL_GIN_IB_TC` (NCCL maps GIN to its own TC; apps don't configure TC bits directly).

**"Why not reuse `priority_level`?"**
`priority_level` (in #2079 / #2048) is a **scheduling-layer** concept — it determines dequeue order within a single queue. `TrafficClass` is a **link-layer** concept — it determines *which* queue (SL/VL → NIC TX queue → DSCP → switch egress) the transfer takes. The two are orthogonal (a `(priority=HIGH, class=KV_PUT)` and a `(priority=LOW, class=KV_PUT)` should share the same SL/TC but dequeue in different order). This is the same orthogonality articulated in @catyans/@alogfans's discussion on #2489 (CC vs. QoS).

## Scope (and explicit non-goals)

In scope:
- Extend `SelectionContext` + `SelectionPolicy` with `traffic_class`.
- Default mapping table + env-var override.
- Notification-QP routing via `CTRL` / `KV_LOOKUP_META`.
- Per-class telemetry counters.
- Backward compatibility: `DEFAULT` preserves current behavior bit-for-bit.

Out of scope (explicit, to keep the RFC tractable):
- vLLM / SGLang / DeepEP integration (separate follow-up PRs once this lands).
- Cross-process traffic-class quota (would extend the shared-memory plan from #2048).
- NIXL pass-through (companion RFC in `ai-dynamo/nixl` once at least two backends adopt this shape).
- Notification-QP SL/TC configuration — handled by #2526; this RFC only provides the classification signal, not the QP-level plumbing.

## Open questions

1. Should `USER_DEFINED_BASE` be `128` or higher, leaving more room for future first-class values?
2. Should the default mapping table live in `Config` or be hard-coded with env-var override only?
3. Should `KV_LOOKUP_META` default to notification QP, or stay on data QP for symmetry with `KV_PUT`?
4. Telemetry naming — `mooncake_te_traffic_class_*` vs. a more concise `mc_te_tc_*`?

## References

- Mooncake #1187 — `MC_IB_TC` env var
- Mooncake #2048 — TENT QoS (priority + slot rotation)
- Mooncake #2079 — `TransportSelector` / `SelectionContext` (this RFC extends)
- Mooncake #2489 — CC plugin (orthogonal to this — CC = rate, this = classification)
- Mooncake #2525 — `MC_IB_SL` env var
- Mooncake #2526 — Notification-QP SL/TC plumbing
- sgl-project/sglang#28631 — orthogonal priority RFC (this RFC's companion at the SGLang layer)
- NCCL v2.30.7 release notes — `NCCL_GIN_IB_TC` precedent

## Acknowledgements

Cc: @alogfans @stmatengss @staryxchen @lvshufan — most active on the QoS / TENT / RDMA-config line (#2048, #2079, #2489, #2293).


## 评论 (7)

### github-actions[bot] · 2026-06-23

Thanks for opening this issue, @catyans!

| Field | Value |
|-------|-------|
| **Issue** | #2568 |
| **GitHub user ID** | `18214026` |
| **Reporter** | @catyans |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### alogfans · 2026-06-24

An important issue is that, if we expect to configure different traffic_classes for different tasks within the same transfer engine, we need to allocate multiple QPs, each assign different parameters during their handshakes. The control path may be changed significantly.

### staryxchen · 2026-06-24

Thanks for your proposal! But I have some concerns about extending `SelectionContext` with a `TrafficClass` enum.

**1. Layering inversion.** Every existing field in `SelectionContext` is an engine-observable fact (segment type, memory type, size, priority). `KV_PUT` / `EP_DISPATCH` / `CTRL` are *application* semantics — adding them asks `TransferEngine` to own a vocabulary of upper-layer scenarios and their mapping to link-layer resources. The DSCP analogy in the RFC actually argues against this: DSCP is opaque bits, not an enum routers interpret.

**2. Closed enum is a release bottleneck.** Every new traffic shape (training gradient sync, parameter prefetch, …) comes back through this RFC. The `USER_DEFINED_BASE = 128` escape hatch implicitly admits this — if extension is expected, the closed-enum shape was wrong.

**3. @alogfans's point is the load-bearing one.** SL/TC are baked into QP attributes at handshake; real per-class differentiation needs per-class QP pools. A `traffic_class` field is just a label — it doesn't move that complexity. With every class defaulting to "data QP", the field lands as a no-op.

---

**Alternative — use what's already there.**

`SelectionContext` already has `policy_name` (transport_selector.h:83), and `matchesPolicy` already short-circuits on an exact match (transport_selector.cpp:251). That's the correct hook: the caller passes an opaque channel name, the engine never interprets it.

- `SelectionContext`: **no change.** Callers set `policy_name = "kv-critical"` / `"ctrl"`.
- `SelectionPolicy`: extend with link-layer attributes:
  ```json
  {
    "name": "kv-critical",
    "segment_type": "memory",
    "service_level": 3,
    "traffic_class": 96,
    "qp_pool": "kv"
  }
  ```

Zero churn in `SelectionContext`, no business vocabulary in the engine, consistent with #2079, and `qp_pool` becomes an explicit field instead of an enum-implied assumption. Telemetry labels by `policy_name`.

### catyans · 2026-06-25

Thank you @staryxchen — this is a much better shape than what I proposed, and all three points are correct. Let me address each and adjust the RFC accordingly.

**On (1) layering inversion** — you're right, and the DSCP analogy does cut against me. `KV_PUT`/`EP_DISPATCH`/`CTRL` are application vocabulary; the engine shouldn't own them. An opaque identifier the engine never interprets is the correct hook.

**On (2) closed enum** — agreed. `USER_DEFINED_BASE = 128` was a tell that the closed-enum shape was wrong. A config-driven approach where a new traffic shape is just a new JSON entry (no code change, no RFC round-trip) is strictly better.

**On (3) — the load-bearing point** — this is the one that matters most, and I think it's right: SL/TC are baked into QP attributes at handshake, so a label alone is a no-op. Real per-class differentiation needs **per-class QP pools**, and that's the actual complexity. `qp_pool` as an explicit field surfaces it instead of hiding it behind an enum-implied "data QP" default.

**Revised direction — adopting your proposal.** I'll drop the `TrafficClass` enum and the `SelectionContext` change entirely, and instead:

- `SelectionContext`: **no change**. Callers set `policy_name` (e.g. `"kv-critical"` / `"ctrl"`), which `matchesPolicy` already short-circuits on (transport_selector.cpp:251).
- `SelectionPolicy`: extend with link-layer attributes — `service_level`, `traffic_class`, `qp_pool` — parsed from the same JSON as the existing fields (`name`/`segment_type`/`devices`/`transports`, transport_selector.h:90), and carried out via `SelectionResult`.

I'd suggest splitting this into two independent units so the no-op concern is addressed head-on rather than deferred:

1. **Policy-level SL/TC (small, mergeable now).** Add `service_level`/`traffic_class` to `SelectionPolicy` + `SelectionResult`, and apply the resolved SL/TC at QP setup. This makes the link-layer knobs from #2525/#2526 *per-policy configurable* instead of process-global — useful on its own, but I'll be explicit that without per-class QP pools, policies sharing a QP still collapse to one SL.

2. **Per-class QP pools (the real work).** A follow-up RFC for pool creation/lifecycle/routing keyed by `qp_pool`, so different policies actually land on QPs with different SL/TC. This is where the genuine differentiation lives, and I'd rather design it explicitly than imply it.

Does this two-step split work for you? If so I'll rewrite the RFC around `policy_name` + `SelectionPolicy` and open the step-1 PR first. Thanks again for redirecting this — the opaque-name + explicit-qp_pool framing is clearly the right one.


### staryxchen · 2026-06-25

> Thank you [@staryxchen](https://github.com/staryxchen) — this is a much better shape than what I proposed, and all three points are correct. Let me address each and adjust the RFC accordingly.
> 
> **On (1) layering inversion** — you're right, and the DSCP analogy does cut against me. `KV_PUT`/`EP_DISPATCH`/`CTRL` are application vocabulary; the engine shouldn't own them. An opaque identifier the engine never interprets is the correct hook.
> 
> **On (2) closed enum** — agreed. `USER_DEFINED_BASE = 128` was a tell that the closed-enum shape was wrong. A config-driven approach where a new traffic shape is just a new JSON entry (no code change, no RFC round-trip) is strictly better.
> 
> **On (3) — the load-bearing point** — this is the one that matters most, and I think it's right: SL/TC are baked into QP attributes at handshake, so a label alone is a no-op. Real per-class differentiation needs **per-class QP pools**, and that's the actual complexity. `qp_pool` as an explicit field surfaces it instead of hiding it behind an enum-implied "data QP" default.
> 
> **Revised direction — adopting your proposal.** I'll drop the `TrafficClass` enum and the `SelectionContext` change entirely, and instead:
> 
> * `SelectionContext`: **no change**. Callers set `policy_name` (e.g. `"kv-critical"` / `"ctrl"`), which `matchesPolicy` already short-circuits on (transport_selector.cpp:251).
> * `SelectionPolicy`: extend with link-layer attributes — `service_level`, `traffic_class`, `qp_pool` — parsed from the same JSON as the existing fields (`name`/`segment_type`/`devices`/`transports`, transport_selector.h:90), and carried out via `SelectionResult`.
> 
> I'd suggest splitting this into two independent units so the no-op concern is addressed head-on rather than deferred:
> 
> 1. **Policy-level SL/TC (small, mergeable now).** Add `service_level`/`traffic_class` to `SelectionPolicy` + `SelectionResult`, and apply the resolved SL/TC at QP setup. This makes the link-layer knobs from [[TransferEngine] Make InfiniBand Service Level configurable via MC_IB_SL #2525](https://github.com/kvcache-ai/Mooncake/pull/2525)/[[TransferEngine] Apply configured SL/TC to the TENT notification QP #2526](https://github.com/kvcache-ai/Mooncake/pull/2526) _per-policy configurable_ instead of process-global — useful on its own, but I'll be explicit that without per-class QP pools, policies sharing a QP still collapse to one SL.
> 2. **Per-class QP pools (the real work).** A follow-up RFC for pool creation/lifecycle/routing keyed by `qp_pool`, so different policies actually land on QPs with different SL/TC. This is where the genuine differentiation lives, and I'd rather design it explicitly than imply it.
> 
> Does this two-step split work for you? If so I'll rewrite the RFC around `policy_name` + `SelectionPolicy` and open the step-1 PR first. Thanks again for redirecting this — the opaque-name + explicit-qp_pool framing is clearly the right one.

@catyans The two-step split is good for me. Only one reminder: When naming fields in the JSON schema, make sure to reserve space for Step 2 (either the “qp_pool” placeholder field or a versioned schema); otherwise, you’ll have to modify the schema again when Step 2 rolls around to ensure compatibility with older configurations.

### catyans · 2026-06-26

Thanks @staryxchen — good call on schema forward-compat. I'll reserve `qp_pool` in the `SelectionPolicy` schema from step 1 (parsed and stored, defaulting to the current "data QP" behavior when unset), so step 2 only adds pool creation/routing semantics without a schema change or breaking existing configs. Will open the step-1 PR (`service_level`/`traffic_class`/`qp_pool` on `SelectionPolicy` + `SelectionResult`, applied at QP setup) along these lines.


### github-actions[bot] · 2026-09-25

This issue has had no activity for 90 days and will be closed in 7 days if there is no further activity. Please comment or react if it should stay open.
