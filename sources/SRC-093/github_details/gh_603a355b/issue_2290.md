# [Issue #2290] [RFC]: Control-plane orchestration of vLLM sleep mode and kvcached for warm standby and multi-model GPU pooling

source: https://github.com/vllm-project/aibrix/issues/2290
state: open | updated: 2026-09-24T21:27:35Z
labels: kind/enhancement, area/autoscaling, area/acceleration

## 正文

### Summary

AIBrix scales replicas as 0-or-N and only *observes* engine memory state; it never drives it. Two engine-side mechanisms now make GPU memory reclaimable at runtime — vLLM **sleep mode** (park a whole idle model's weights+KV) and **kvcached** (elastically shrink/grow a model's KV so several models share one GPU) — but both are mechanism-only, with no control plane. This RFC proposes AIBrix own the *policy*: a control-plane-driven "warm/asleep" tier between one replica and zero, plus KV-budget arbitration across co-resident models. The result: multi-minute cold starts become second-scale wakes, and one GPU can densely host many long-tail models.

### Motivation

Scaling is binary today. To reclaim a GPU we either keep a replica running (burning HBM while idle) or delete the pod and pay a multi-minute cold start (weight load + CUDA graph capture) when traffic returns. Neither fits bursty or long-tail traffic.

The engine now exposes the levers, but not the policy:

| | vLLM sleep mode | kvcached (github.com/ovg-project/kvcached) |
|---|---|---|
| Scope | whole model (weights + KV) | KV cache only (weights allocated outside it) |
| Granularity | all-or-nothing, single process | page-level elastic, cross-process co-residency |
| Target | a fully **idle** model | several **active** models sharing a GPU |
| Mechanism | CUDA VMM; `/sleep` `/wake_up`; level 1 weights→CPU, level 2 discard | CUDA VMM; per-process `cudaMemGetInfo` headroom + `/dev/shm` budget via `kvctl` |
| Control | manual API only; `VLLM_SERVER_DEV_MODE`-gated; no autoscaling | decentralized by design; no scheduler/admission/cross-node; `controller/` is a demo |

They are complementary: kvcached handles elastic KV among active co-resident models; sleep parks idle models' weights. Both are VMM actuators that enforce/observe — neither *decides*. The missing piece is a control plane that decides **which** model sleeps/wakes and **when**, **how much** KV budget each co-resident model gets, **admission** when a GPU is oversubscribed, and **routing/readiness** as models move between awake / warm / asleep. AIBrix already scrapes `vllm:engine_sleep_state` but never acts on it, and has no notion of co-resident KV budget — so it is the natural owner.

### Proposed Change

(Sketch only; full design — CRD, state machine, budget algorithm, agent protocol — to follow in a complete doc.)

1. A **warm/asleep lifecycle state** between `minReplicas` and zero: low traffic → `POST /sleep?level=1&mode=wait` (graceful drain); traffic returns → `/wake_up` (seconds). Pod/IP/endpoint persist.
2. A **KV-budget arbiter** across co-resident models, driving `kvctl` limits by policy (per-model min/max/share, priority) with cost-asymmetric reclaim — shrink KV first (cheap), sleep weights only when protected floors don't fit (expensive).
3. A **decide/execute split**: a Go controller (placement, admission, sleep/wake & budget policy, status) over a pod-side agent (kvcached engine, `kvctl`, sleep).
4. **Required couplings:** invalidate the prefix index on sleep (KV is wiped — see the sleep/prefix-index bug), exclude asleep pods from routing/readiness, and document the `VLLM_SERVER_DEV_MODE` requirement.

### Alternatives Considered

- **HPA scale-to-zero** (`minReplicas=0`): already supported, but pays the full cold start and has no warm tier.
- **Leave it to kvcached's decentralized scheme:** works on a single node but has no admission/priority/cross-node policy and no sleep orchestration — precisely the demo `controller/` AIBrix would replace.
- **Token-level time-sharing** (swap at request granularity): higher utilization ceiling but far more complex/intrusive; this RFC targets model-granularity pooling.


## 评论 (9)

### jiangxiaobin96 · 2026-06-18

We can follow [Aegaeon](https://ennanzhai.github.io/pub/sosp25-aegaeon.pdf) grouping the same model request and use some algorithms to determine when to switch model by sleep mode to guarantee TTFT.

### newhans · 2026-07-01

A few things I'm not clear on after reading this:

**Who provides GPU co-location?** AIBrix uses `nvidia.com/gpu` today (whole-GPU). This RFC assumes pods are already co-resident, but that requires fractional GPU scheduling (HAMi, Volcano, time-slicing, or custom). Is AIBrix going to own that layer, or is it an external dep? If external, does the control plane need to know *which* sharing mechanism is in use to calculate headroom correctly?

**Wake-up under memory pressure.** When a sleeping model wakes, its neighbors may have expanded into the freed space. What happens if they can't shrink fast enough (in-flight requests holding pages)? What if multiple models wake at once? The RFC says "cost-asymmetric reclaim" but doesn't say what happens when reclaim fails — does the wake get rejected, or does a neighbor get killed? Feels like this needs an explicit overcommit policy.

**Host memory as the second bottleneck.** Level 1 sleep offloads weights to host RAM. With multiple models sleeping on the same node (say 8 GPUs × 2-3 models each), offloaded weights alone can eat hundreds of GB. The control plane needs to account for node-level memory headroom when deciding sleep levels — otherwise you trade GPU OOM for host OOM (or the Linux OOM-killer starts evicting pods). Is the sleep-level decision (L1 vs L2) going to be node-aware?

Also — #2287 (prefix index not invalidated on sleep) is a good example of why the control plane needs to own the full sleep lifecycle.

### Jeffwan · 2026-07-05

@newhans Great questions — let me address them one by one.

> Who provides GPU co-location?

I don't think we need a GPU resource claim for this abstraction. The goal here isn't to deliver yet another GPU-sharing solution — the isolation should be transparent to the GPU. In other words, only the GPU worker claims the GPU; the rest of the model registration stays resource-agnostic.

> Wake-up under memory pressure.

This is a good point. Technically, we can surface the response status from vLLM: if a model can't be woken up on its original pod, it can be re-registered on a different one. This is analogous to VPA's in-place update failure falling back to the out-of-place path.

> Host memory as the second bottleneck.

Absolutely. Both DRAM and HBM need to be monitored and accounted for by the controller when making placement decisions, this ultimately becomes a multi-dimensional resource management problem.

That said, I'd personally defer this to a second phase. Building a full resource-management layer on top of Kubernetes adds significant complexity, and that complexity is exactly the gap between a prototype and production-ready usage.


You clearly have a lot of context in this space. :D I'd love to keep this conversation going. Happy to hear your thoughts on the phasing

### Jeffwan · 2026-07-05

@jiangxiaobin96 we can build the interface abstraction for that strategy, technically, I personally feel aegaeon's granularity is too fine-grain which limits its landing. We'd like to build a more generic multiplexing system which is engine agnostic or just reply on few engine features.

### newhans · 2026-07-13

Thanks @Jeffwan. I agree that full joint HBM/DRAM resource management should probably be a second-phase goal.
My main concern is that Phase 1 should still define an explicit safety boundary. For example, it could start with same-node warm standby, serialize wake-ups on each physical GPU, check available HBM/DRAM before sleep or wake, and fall back to re-registration when reclaim or wake fails.
I also agree that AIBrix does not need to implement another GPU-sharing layer. That could be provided by HAMi, Volcano, DRA, or another external mechanism. However, AIBrix would still need a small provider-neutral contract to reserve capacity before wake-up and reconcile resources after sleep.
I’ve recently been exploring CUDA checkpoint and CRIU as well. They may provide a cheaper out-of-place fallback than a full cold start. I’ll do some experiments and can share the findings separately.

### rishabhsinha17 · 2026-08-25

Two kvcached-side changes landed last week, after this RFC was written, that affect what the arbiter and pod agent can target:

1. Per-instance memory limits are now an API rather than raw kvctl shm writes: ovg-project/kvcached#414 (merged) adds revisioned instance-level limits with acknowledgement and deferred-state reporting. The semantics matter for the arbiter: lowering a limit never revokes active pages, it only blocks further physical growth until usage drains, so shrink is asynchronous by contract. That bears on @newhans's wake-under-pressure question: the revision/ack handshake is how a controller detects non-convergence and escalates to sleeping a neighbor; a hard cap was discussed and deferred pending CPU offload integration. Relatedly, ovg-project/kvcached#448 (merged) fixed co-resident vLLM startup profiling (ovg-project/kvcached#193), previously the main multi-model bring-up failure.
2. Lifecycle readiness and failure propagation is an accepted kvcached workstream: item (5) of ovg-project/kvcached#375, a poll-only phase model (INITIALIZING, READY, DEGRADED, FAILED) plus typed failure records on the ovg-project/kvcached#385 snapshot contract, scope approved by maintainers. That is the surface a pod agent should poll for the routing/readiness coupling in point 4 rather than scraping shm. I own that item; implementation starts once capability discovery lands.

I contribute to kvcached (five merged PRs, including the alloc rollback ovg-project/kvcached#430 and vLLM compat ovg-project/kvcached#439) and ran the vLLM rows of the multi-model support matrix in ovg-project/kvcached#425, so I can take #2419 and the kvcached-facing half of the agent protocol.

One scoping question: is the pod-side agent intended to live in aibrix and consume kvcached's public surface (snapshots, limit API) alongside vLLM's sleep endpoints, or do you want parts of it upstreamed into kvcached? The boundary agreed in ovg-project/kvcached#375 puts mechanism hooks upstream and policy in integration projects, so I can route the kvcached-side pieces wherever that split lands.


### Jeffwan · 2026-08-25

@rishabhsinha17 thanks for bringing the latest changes. 
1. I personally feel a sidecar is needed since that's the bridge of the control plane and provides enough flexibilties to integrate with solutions like AIBrix. While, if the kvcached's public api is generic enough, that could be considered as well. One thing I am not super clear is the management scope of the agent. Ideally, I hope it to be a host agent but now seems pod level or GPU level is more appropriate.
2. feel free to take some pieces if you like to contribute. some PRs has been landed in aibrix but overall status is still in early stage

### rishabhsinha17 · 2026-08-25

@Jeffwan on the management scope: kvcached's own state model points at host-level as the natural agent boundary. The contended resource is the physical page pool, which is shared per GPU across engine processes on the same host (shm-backed, one allocator per device), so an arbiter needs the host-level view of it. Enforcement is already per-instance through the #414 limit API (revisioned, ack'd, never revokes active pages), and lifecycle/readiness is per-engine, which the #375 item 5 work surfaces per instance. A single host daemon can expose both: per-GPU pool state plus per-instance readiness and limit acks. Pod-level behavior then falls out of the per-instance API rather than needing a sidecar per pod, which matches your host-agent preference.

On pieces: I will start with the kvcached-facing surface. Happy to take #2419 plus the agent's kvcached client once you settle where the daemon lives.


### Zeyu-ZEYU · 2026-09-23

A status update on the ModelClaim GPU-memory work, and what comes next.

**In review: #2647**, which resolves #2744. A claim declares what one instance costs on a GPU. Placement keeps an account per card, and admits a model only where the card has room. When a model lands, the card is divided between the engines on it, and each engine stays routable only while it is held to its limit.

**Next, one PR each.** Each gets its own issue when it starts.

1. Online KV budgeting (#2795). Divide a card again whenever its engines change, and every 10 seconds as load changes. A sleeping engine keeps only its floor.
2. A claim that cannot be placed (#2806). Back off rather than retry every 10 seconds, start over when room may have appeared, and say when no card could ever hold the model.
3. Faster readiness (#2807). Check an activating instance every second or two, rather than every 10 seconds.
4. A claim that is not placed yet (#2808). The gateway answers 503 with `Retry-After` and the reason, rather than 400 "model does not exist".

**Later**, opened one at a time:

- Start an engine with its limit already in force (#2770).
- Check a declaration against what the engine actually used, once `hbm_peak_bytes` reports something other than 0.
- Show a card's account on status.
- Metrics for KV divisions, under #2455.
- Remove the `reclaim` policy of the pool annotation.
- Make room for a new model by squeezing busy neighbours, or by putting idle ones to sleep.
- Wake a sleeping model through the controller.
- Report used and preallocated KV separately from the runtime.
- Correct the gateway's KV-pressure signal under kvcached limits, which divides by `num_gpu_blocks`.
- Account for and divide each card of a multi-GPU pod, rather than sizing the pod by its smallest card.
- Offload KV to host memory, starting with experiments under #2419.
- Per-model priority, and a minimum and maximum KV.
- Best-fit placement, and refusing non-positive figures at apply time with CEL, if maintainers want them.

