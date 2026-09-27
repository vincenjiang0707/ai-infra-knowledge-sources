# [Issue #5030] [RFC] Shared Device-DAX KV pooling for LMCache MP servers

source: https://github.com/LMCache/LMCache/issues/5030
state: open | updated: 2026-09-17T08:31:21Z
labels: 

## 正文

**Label**

`new feature`

**Is your feature request related to a problem? Please describe.**

LMCache MP servers currently allocate Device-DAX L1 storage independently.
Mapping one physical region from multiple MP servers requires a common extent allocator and object-lifetime authority: otherwise allocations can overlap and readers cannot establish that a producer has finished writing an object.

Upstream the experimental `memory_coordinator` component so independent MP servers can pool KV capacity and reuse committed objects in an operator-provisioned shared DAX region. 
The serving target is **MP mode only**.

**Describe the solution you'd like**

```text
serving engines
      |
 existing MP connectors
      |
 MP servers <---- optional fleet connection ----> MP Coordinator
      |                                                membership/views/controls
      +---- reservation metadata RPCs ----> Memory Coordinator
      |                                     durable allocation/reservations
      +---- GPU transfers + visibility ---> shared DAX region
```

| Component | Responsibility in this architecture |
| --- | --- |
| **MP Coordinator** (`lmcache/v1/mp_coordinator/`) | Existing fleet membership and health, cache directory and usage views, and quota/L2 eviction and cache-control dispatch for supported backends. It does not grant DAX extents or own shared-object reservations. |
| **Memory Coordinator** (`lmcache/v1/memory_coordinator/`) | Standalone durable authority for shared-region identity, aligned allocation, object generations, write ownership and read reservations. |
| **MP cache servers** | Validate grants, map each host's device, register GPU access, complete transfers and apply publish/acquire visibility barriers. |
| **Deployment operator** | Establish that all mappings refer to the same physical payload incarnation and perform coordinated offline resets. |

**Relationship with the existing MP Coordinator**

The two coordinators have separate responsibilities. 
MP servers contact the Memory Coordinator directly for shared-object reserve/commit/release operations; the MP Coordinator is not an allocation hop. Its eventually consistent cache directory provides placement hints, which cannot replace a Memory Coordinator reservation or authorize access to a shared extent.

The initial shared mode can retain MP Coordinator registration and heartbeats through the existing HTTP-server registration path, with cache-event reporting disabled. The prototype explicitly rejects `--coordinator-event-reporting` in shared mode, so MP Coordinator membership must not be presented as working shared-DAX directory, usage or fleet-policy integration.
Existing event contracts identify shared placements by tier/backend and reporter incarnation, rather than the DAX region identity and durable region epoch needed by this allocation authority.

A later MP Coordinator integration should build on its existing shared-placement and shared-capacity accounting support. It must define region identity and reporting ownership, distinguish a coordinator process restart from a payload reset, reconcile directory/usage views without counting the pool once per MP server, and make fleet controls respect the Memory Coordinator's object lifecycle. Tests must cover multiple reporting servers, stale/replayed events and same-payload restarts before shared-DAX event reporting is enabled. This follow-up remains outside the initial sharing milestone and does not transfer allocation authority to the MP Coordinator.

The coordinator's allocation state machine is an internal service component.
There is no embedded `MemoryPool` serving mode, pool created independently by each MP server, or fallback to a fresh local authority after RPC failure. This series adds no legacy `LMCacheEngine` or in-process storage-backend integration.
Internal test doubles remain useful for unit tests; separate processes are required to qualify the serving path.

The first sharing milestone has one region, one immutable layout profile, one active durable authority and static aligned allocation:

```text
write: reserve extent -> D2H completion -> publish visibility -> commit VALID
read:  reserve VALID object -> acquire visibility -> H2D completion -> release
close: stop admission -> wait handlers -> flush completions -> drain -> unmap
```

Only metadata crosses coordinator RPCs: canonical object keys, shapes/dtypes, offsets, lengths, generations, epochs and opaque reservation tokens. Keys retain model, rank, object-group and cache-salt identity. Write batches are capacity-atomic, a duplicate key has one winning writer, and unfinished objects are invisible to readers. KV bytes and process-local pointers stay in the data path.

Durable state and exclusive writer ownership are mandatory before service or MP activation. Mutations persist before acknowledgement; corrupt or missing initialized state fails startup. A normal restart restores the epoch and
reservations only for the same physical payload incarnation. Stale identities and ambiguous mutation replies fence the client, without automatic mutation retries. Replacing or clearing the region requires an offline reset after all
clients are quiesced. A state-directory lock protects that directory; the operator must also ensure one authority state directory per physical region.

Allocation is monotonic. Aborted writes consume their extents, committed objects are immutable and reservation tokens do not expire. Exhaustion is an explicit result. Deletion, eviction, extent reuse, elastic capacity assignment,
HA, Kubernetes resources and fleet reporting are outside this initial sharing milestone.

The implementation will submitted as different PRs

| PRs | MP sharing prerequisite |
| --- | --- |
| 1–2 | Safe MP transfer-context lifetime and an opt-in MQ handler drain |
| 3–6 | Region/wire contracts and service-owned durable reservation state |
| 7–10 | Authenticated service, launch configuration and validated MP HTTP client |
| 11–14 | DAX mapping/visibility, write/read backend lifecycle and MP constraints |
| 15–17 | L1/storage delegation, lookup activation and complete MP shutdown ordering |
| 18–19 | Separate-process file-backed qualification and verified shared-hardware GPU qualification |

PR 1 now fixes MP transfer-context lifetime so unregister, worker reaping and
module close cannot release GPU IPC mappings while handlers or transfers still
use them. 

Initial shared mode supports pure Device-DAX, TP=1, one read lock, `lmcache_driven` transfers and noop eviction. It rejects L2/P2P/GDS, hybrid DRAM, lazy/SHM allocation, experimental transfer modules and MP Coordinator event reporting. Shared-L1 errors become misses or failed stores so engines can recompute; status reports shared L1 unhealthy and usage unknown. Broader combinations need their own validation.

**Describe alternatives you've considered**

- Separate private DAX pools retain independent ownership but cannot reuse a shared object allocation across MP servers.
- A remote L2 backend provides sharing with different allocation and data-transfer semantics.
- Hosting allocation authority in the MP Coordinator would require changes to its persistence, writer exclusion and availability contracts. The standalone service preserves the experimental component's existing responsibility.



## 评论 (1)

### jooho-XCENA · 2026-09-17

It is encouraging to see this RFC converge on a separation we had been exploring in Maru: shared-pool authority alongside fleet coordination. We [outlined this rationale in July](https://github.com/LMCache/LMCache/pull/4052#issuecomment-4934280592), because fabric-attached CXL requires shared membership and cross-host read protection beyond each MP server’s local state. The direction here reinforces that architectural motivation.

We are currently testing Maru on a CXL fabric configured through a physical switch, with multiple hosts accessing the shared pool. This is the deployment model behind our design, and an active validation effort.

That pool may also serve applications beyond LMCache. Maru’s [separation of a Resource Manager from per-application metadata services](https://github.com/xcena-dev/maru/blob/main/docs/source/design_doc/architecture_overview.md#key-design-properties) provides a basis for managing capacity across application groups while keeping application-specific object semantics separate. If shared L1 needs a memory coordinator, could it operate over regions allocated by a common resource manager such as Maru’s, with LMCache retaining its cache policy and object-lifecycle responsibilities?

The docs already describe cross-host sharing. A small topology diagram and a clear boundary between the fixed shared region, pool resource management, and external fabric provisioning would help us align the two approaches.
