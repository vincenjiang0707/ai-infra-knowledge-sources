# [Issue #4242] [RFC]: Generalize adaptive scatter transfer for Engram, Reshard, and Structured Object

source: https://github.com/kvcache-ai/Mooncake/issues/4242
state: open | updated: 2026-09-20T11:44:10Z
labels: RFC

## 正文

## Changes proposed

This RFC proposes a common adaptive scatter-transfer path for three Mooncake
workloads:

1. Engram selected-row reads;
2. heterogeneous Reshard transfers;
3. Structured Object PUT/GET.

The common layer should decide between direct RDMA and owner-side gather, use
pre-registered staging memory when gathering is profitable, and overlap packing
with bulk RDMA under bounded resource limits. The policy belongs in Transfer
Engine and Store transfer primitives rather than in separate Engram, Reshard,
or Structured Object implementations.

PR #4117 is the first implementation step. It adds an adaptive gather path for
many-small scatter READs while retaining the existing direct path and fallback.
This RFC documents the workload model, current bottlenecks, performance goals,
and the parts of the Structured Object design that should become reusable
infrastructure.

## Motivation

Classic Transfer Engine is efficient when a request contains a small number of
large registered-memory ranges. It is less efficient when one logical operation
contains tens of thousands of small fragments. Posting one RDMA operation per
fragment exposes WQE, doorbell, CQ, queue-depth, and completion costs instead of
the link bandwidth.

Gathering small source fragments into registered staging memory replaces many
small RDMA operations with a few bulk operations, but it introduces different
costs:

- requester-side range normalization, validation, coalescing, and plan encoding;
- command transport and owner-side plan decoding;
- random-row CPU copies into staging memory;
- staging-buffer allocation and lifetime management;
- pack/transfer pipeline fill and drain;
- per-fragment completion publication in upper layers.

The optimization therefore cannot be a fixed fragment-size threshold or a
larger global RDMA queue. It must compare the complete direct and gather costs
for the actual fragment geometry and available hardware resources.

## Metric definition

Two bandwidth numbers must be reported separately:

- **RDMA window throughput:** bytes divided by the time from the first bulk RDMA
  post to final data completion. This measures whether the network is saturated.
- **End-to-end useful throughput:** logical payload bytes divided by the complete
  `transferScatter()` or Store API latency. This includes planning, command
  handling, packing, transfer, and completion publication.

On two A10 + ERDMA peers, the current measurements are:

| Workload | p50 | End-to-end useful throughput |
| --- | ---: | ---: |
| 98,304 x 264 B random rows | 5.920 ms | 35.07 Gbit/s |
| 131,072 x 264 B random rows | 8.004 ms | 34.59 Gbit/s |
| 32,768 x 264 B + 64 x 512 KiB | 4.817 ms | 70.09 Gbit/s |
| 64 x 512 KiB direct control | 3.384 ms | 79.32 Gbit/s |

The owner-side bulk RDMA window for the 98,304 x 264 B workload is about
2.47 ms, or approximately 84 Gbit/s. The RNIC is therefore already close to
line rate after data has been packed. The 35 Gbit/s end-to-end result is not an
RDMA bandwidth regression; it is the cost of the complete many-small-fragment
pipeline.

## Current bottlenecks

Profiling the 98,304 x 264 B workload gives the following approximate costs:

- requester planning: 1.25-1.60 ms;
- command connection setup: 0.15-0.24 ms per shard;
- owner decode and validation: 0.16-0.33 ms per 24,576-span shard;
- random-row packing: 1.3-1.6 ms per 6.49 MiB shard;
- RDMA completion tail across four shards: 0.9-3.1 ms;
- last owner shard completion: about 4.5 ms after owner execution begins.

Additional experiments show that this is not solved by increasing parallelism:

- 8, 12, and 16 request shards reached 31.42, 28.82, and 27.36 Gbit/s;
- a single command with pipeline depth 8 reached at most 35.65 Gbit/s;
- smaller chunks and software prefetch did not improve the end-to-end result.

More shards reduce initial packing time but add command handling, decoding,
staging contention, and RDMA scheduling overhead. Smaller chunks improve overlap
only until per-chunk submission and completion costs dominate. The current four
shards are near the best point for this machine, but the remaining requester and
CPU-gather costs are still too large.

Store integrations may add another upper-layer cost: lease refresh and
per-fragment result materialization. That cost must be profiled separately from
the Transfer Engine data window and should use batch completion wherever the API
contract permits it.

## Workload scenarios

### 1. Engram

Engram reads many fixed-size embedding rows from one or a few large tables into
a contiguous output buffer. Source rows are usually random, destinations are
ordered, and individual fragments are small (264 B in the current DeepSeek
integration). The path is latency-sensitive because it contributes directly to
TTFT and may execute for multiple layers.

Relevant characteristics:

- very high fragment count;
- fixed or nearly fixed fragment size;
- random source addresses and contiguous destination addresses;
- READ-heavy operation;
- registered CPU or GPU destination owned by the framework;
- repeated calls where connection and allocation setup must be amortized.

Engram should submit one logical layer read. It should not implement its own
gather policy, staging allocator, or shard scheduler.

### 2. Reshard

Reshard has a wider geometry. A plan may contain a few large contiguous regions,
many small intersections, or both in the same operation. Source and destination
layouts can differ because of TP, PP, DP, EP, head placement, or page layout.

Relevant characteristics:

- few-large, many-small, and mixed workloads are all valid;
- both source and destination can be fragmented;
- READ and WRITE directions are relevant;
- large ranges should remain direct;
- small ranges may be gathered only when their destination order permits it;
- logical coverage, ordering, and completion semantics must be preserved.

Reshard therefore needs a hybrid plan, not one global mode. The planner should
partition a logical operation into direct ranges and gatherable runs, execute
both under one completion object, and never materialize the complete tensor only
to reshape it.

### 3. Structured Object

Structured Object stores metadata plus named tensor, ndarray, bytes, or ragged
members. Its PUT path may receive multiple source buffers that form one logical
payload. Its GET path may selectively materialize members or byte ranges into a
caller-provided destination.

Relevant characteristics:

- PUT commonly concatenates multiple logical buffers;
- GET may read full chunks, selected members, or multiple ranges;
- object manifests and codecs remain an upper-layer concern;
- chunking provides natural pipeline boundaries;
- caller-provided and BufferPool-backed destinations can avoid an extra copy.

Structured Object already implements useful mechanisms in PRs #3023, #3024,
and #3112. This RFC does not move manifests, codecs, or Python object semantics
into Transfer Engine. It generalizes the transport ideas underneath them.

## Structured Object ideas generalized by this RFC

The following Structured Object ideas apply directly to Engram and Reshard:

1. **Preserve scatter input until the staging boundary.** Multi-buffer PUT avoids
   building one large Python `bytes` object. Engram row IDs and Reshard logical
   intersections should likewise remain compact descriptors until the owner
   copies them into staging memory.

2. **Use pre-registered BufferPool leases.** Structured Object stages grouped
   PUTs in reusable registered pool memory before calling `batch_put_from`.
   PR #4117 extends the same ownership model to owner-side scatter READ gather:
   acquire a bounded lease, pack into it, submit bulk RDMA, and release it after
   completion.

3. **Chunk work and overlap copy with transfer.** Structured Object splits large
   payloads into bounded chunks and permits multiple chunks in flight. The
   generic scatter path uses the same pipeline shape for random rows and Reshard
   fragments, with chunk size and depth selected from a cost model rather than
   Structured Object's rollout-specific defaults.

4. **Write/read directly from registered buffers.** Structured Object uses
   `batch_put_from`, `batch_get_into`, `get_into_ranges`, caller destinations,
   and pool-backed arrays to avoid intermediate Python-owned payloads. Engram
   and Reshard should end in their final registered CPU/GPU destination whenever
   the transport and layout permit it.

5. **Batch one logical operation.** Structured Object groups physical chunks
   behind one logical object operation. Scatter transfer should similarly use
   compact plans and batch completion instead of one control round trip and one
   result publication per fragment.

6. **Keep bounded fallback behavior.** Structured Object falls back to ordinary
   Store PUT/GET when BufferPool or fast-path APIs are unavailable. Generic
   scatter must keep direct transfer as the correctness fallback when capability
   negotiation, staging allocation, validation, or active gather fails.

7. **Separate policy from data semantics.** Structured Object retains member and
   manifest semantics above its payload transport. Engram retains table/row
   semantics, and Reshard retains logical placement semantics. Transfer Engine
   should receive only registered ranges, ownership, and completion contracts.

The following parts stay Structured Object-specific and are not generalized:
manifest publication, codecs, cleanup keys, grouped object placement, Python
ownership wrappers, and fixed 64 MiB rollout defaults.

## Proposed common design

### Normalized scatter plan

Callers lower their domain-specific operation into registered source and
destination ranges. A single O(N) normalization pass should:

- validate bounds and registration;
- coalesce adjacent source/destination ranges;
- identify contiguous destination runs;
- classify direct and gather candidates;
- encode compact relative offsets without building duplicate shard vectors;
- attach batch completion spans instead of per-fragment success callbacks.

### Adaptive direct, gather, and hybrid modes

For total bytes `S`, fragment count `N`, coalesced span count `M`, link bandwidth
`B_net`, measured packing bandwidth `B_mem`, small-copy rate `R_copy`, RDMA post
rate `R_post`, queue depth `Q`, RTT `L`, chunk size `C`, and pipeline width `P`:

```text
T_direct = L + max(S / B_net,
                   N / R_post,
                   ceil(N / Q) * L)

K = ceil(S / C)

T_pack = S / (P * B_mem) + M / (P * R_copy)

T_bulk = L + max(S / B_net,
                 K / R_post,
                 ceil(K / Q) * L)

T_gather = T_plan + T_control + T_decode
           + C / B_mem
           + max(T_pack, T_bulk)
           + C / B_net
```

The `C / B_mem` and `C / B_net` terms model pipeline fill and drain. Candidate
chunk sizes should satisfy both bandwidth-delay-product and fixed-cost
amortization constraints:

```text
C_min = max(B_net * L, B_net * T_chunk_fixed / epsilon)
C_max = min(staging_budget / P, S)
```

The planner evaluates bounded `(mode, C, P)` candidates and selects gather only
when it beats direct by a safety margin. A mixed request applies this decision
per compatible run, so a few large ranges remain direct while many small ranges
can share a gather pipeline.

`B_net`, `Q`, and transport limits come from active contexts and configuration.
`B_mem`, `R_copy`, control latency, and fixed chunk cost should come from a small
startup calibration or conservative moving measurements. The policy must not
contain NIC model names, token counts, or topology-specific constants.

### Effective packing/transfer overlap

PR #4117 introduces bounded staging and pipeline depth, but profiling shows that
the current one-wave four-shard layout still pays most of the first large-chunk
packing cost before the link becomes busy. The follow-up should:

- begin the first RDMA operation after the minimum profitable chunk is packed;
- keep packing and RDMA completion on independent bounded workers;
- reuse command connections or multiplex subplans when control setup is material;
- avoid serial owner decode before all packing workers can start;
- reuse normalized/encoded storage within one operation;
- expose queueing, packing, post, and completion timestamps for profiling.

## Performance goals

The primary goals are relative so they remain meaningful across RDMA NICs:

1. The bulk RDMA window should reach at least 90% of the same-buffer direct
   control throughput.
2. For bandwidth-sized many-small workloads (`S >= 16 MiB`), complete API useful
   throughput should reach at least 70% of the direct control throughput. On the
   current reference peers this means at least 55 Gbit/s and no more than 3.8 ms
   p50 for 98,304 x 264 B.
3. For latency-sized Engram reads, remote-minus-local p50 should be bounded by
   two network RTTs plus 20% of the local gather time.
4. Few-large direct workloads must remain within 5% of the existing direct path.
5. For mixed Reshard workloads, the adaptive plan should be within 10% of the
   better forced-direct or forced-gather result without caller tuning.
6. p95 should remain within 1.2x p50 under an isolated link and CPU allocation.
7. Staging use must remain bounded by `P * C`; pool exhaustion must fall back
   without partial success or leaked leases.

These goals deliberately distinguish link saturation from full API latency.
Reaching 80-84 Gbit/s inside the RDMA window does not by itself satisfy the
Engram TTFT goal.

## Integration boundaries

- **Engram:** `lookup_into` lowers selected rows into one Store ranged read and
  supplies the final registered destination.
- **Reshard:** logical planners remain in `mooncake-reshard`; the executor lowers
  resolved edges into one generic scatter operation.
- **Structured Object:** existing payload and manifest APIs remain unchanged.
  Rewiring a PUT or GET path to the generic scatter executor requires an A/B
  benchmark against the current BufferPool and ranged-read implementation.
- **Store:** owns object metadata, leases, replica selection, and BufferPool
  provisioning. Transfer Engine owns only transfer planning and execution.
- **Transfer Engine:** owns direct/gather/hybrid selection, compact commands,
  staging lifecycle, transfer completion, and transport fallback.

## Validation matrix

Validation must include cross-machine RDMA and local controls:

| Dimension | Cases |
| --- | --- |
| Fragment size | 64, 128, 264, 512 B; 1, 4, 32, 512 KiB |
| Fragment count | 1K, 4K, 32K, 98,304, 131,072 |
| Geometry | random source, contiguous source, contiguous destination, fragmented destination |
| Mix | all small, few large, small + large |
| Direction | READ and WRITE where supported |
| Destination | registered CPU, pinned CPU, registered GPU |
| Resources | 1/2/4/8 staging slots, pool pressure, concurrent callers |
| Network | at least two RDMA implementations when available |

Every result should report payload, p50/p95, full API goodput, RDMA-window
goodput, requester planning, command/decode, packing, and completion time.

## Phasing

1. **Baseline:** land #4117 with adaptive READ gather, BufferPool staging,
   compact commands, direct fallback, and focused tests.
2. **Planner/control:** remove duplicate range/shard materialization, reuse
   command state where safe, and add low-overhead stage metrics.
3. **Pipeline:** make chunk packing and RDMA overlap effective under random-row
   workloads; calibrate the portable cost model.
4. **Reshard:** lower few-large, many-small, and mixed plans into the common API
   and validate both correctness and the mixed-workload performance target.
5. **Structured Object:** A/B its PUT and GET paths against the common executor;
   migrate only paths that preserve or improve current performance.
6. **Framework validation:** measure Engram local and cross-machine CPU/GPU
   destinations in vLLM/SGLang and report TTFT impact.

## Non-goals

- Changing global QP, CQ, READ-credit, `remote_accessible`, or pinned-memory
  defaults solely for these workloads.
- Encoding model, table, tensor, placement, or object-manifest semantics inside
  Transfer Engine.
- Replacing Reshard logical planners or Structured Object codecs.
- Claiming full API line rate from an RDMA-window-only measurement.

## Related work

- #4117: adaptive RDMA scatter reads
- #4083: current EngramStore ownership and lookup interface
- #3692: manifest-driven heterogeneous KV cache Reshard
- #3953: COO sparse updates as Structured Objects
- #3023: BufferPool-backed Structured Object reads
- #3024: multi-buffer Structured Object PUT
- #3112: native fast-copy PUT hot path

### Before submitting a new issue...

- [x] Make sure you already searched for relevant issues and read the documentation.


## 评论 (1)

### github-actions[bot] · 2026-09-20

Thanks for opening this issue, @zxpdemonio!

| Field | Value |
|-------|-------|
| **Issue** | #4242 |
| **GitHub user ID** | `16206312` |
| **Reporter** | @zxpdemonio |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.
