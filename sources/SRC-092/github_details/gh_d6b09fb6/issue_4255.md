# [Issue #4255] [RFC]: [Store] Add LastHitOnly lease selection to BatchProbeKey

source: https://github.com/kvcache-ai/Mooncake/issues/4255
state: open | updated: 2026-09-21T11:36:08Z
labels: RFC

## 正文

## Changes proposed

K3 cache lookups can renew leases for several KDA checkpoints even though only one checkpoint is eventually loaded. This RFC proposes adding selective lease acquisition to `BatchProbeKey` so callers can protect the last complete checkpoint they can actually reuse.

After discussing this with @Aionw, we agreed to propose adding a policy struct directly as an argument to the existing `BatchProbeKey` request. The initial implementation would support two modes:

- `None`: check existence without granting or extending leases.
- `LastHitOnly`: select the last complete candidate and grant read leases to all of its keys.

The immediate use case is K3. We propose implementing only these two modes for now, with `LongestPrefix` and `LongestPrefixLastOnly` left for future work when a concrete use case requires them.

This follows the discussion in [#3801](https://github.com/kvcache-ai/Mooncake/pull/3801) and builds on the probe API introduced by [RFC #3769](https://github.com/kvcache-ai/Mooncake/issues/3769).

## Motivation

`BatchExistKey` grants a read lease on every readable hit. During prefix-cache lookup, however, the engine may query many candidate KDA checkpoints and load only one. Renewing all of them keeps unused state protected from eviction.

For K3, the reuse requirements are different for KV and KDA:

- KV must cover the prefix needed to resume computation.
- KDA needs a complete checkpoint at the chosen resume boundary. Earlier KDA checkpoints do not have to exist consecutively.

The intended lookup flow is therefore:

1. Query and lease KV with `batch_is_exist`, determining the usable KV boundary.
2. Restrict KDA candidates to valid resume positions within that boundary.
3. Select and lease only the last complete KDA checkpoint, then load the required KV and KDA data.

Some excess leasing on the KV side is acceptable for this initial change. The goal is to avoid retaining unused KDA checkpoints.

**A hit must represent a complete candidate**, which can contain several physical keys. For example, with KV available through position 384:

| KDA checkpoint | Rank 0 | Rank 1 | Complete |
| --- | --- | --- | --- |
| 128 | Present | Present | Yes |
| 256 | Missing | Present | No |
| 384 | Present | Missing | No |

The correct result is checkpoint 128, with both of its keys leased. Selecting the last individual key, or selecting the last hit independently on each rank, would not protect the checkpoint that can actually be restored.

## Proposed API

Keep the flat key list and add a policy specifying how many keys form one candidate:

```cpp
enum class ProbeLeaseMode : uint8_t {
    None = 0,
    LastHitOnly = 1,
};

struct GrantLeasePolicy {
    ProbeLeaseMode lease_mode{ProbeLeaseMode::None};
    uint64_t candidate_size{1};
};

std::vector<tl::expected<bool, ErrorCode>> BatchProbeKey(
    const GrantLeasePolicy& policy,
    const std::vector<std::string>& keys,
    const std::string& tenant_id = "default");
```

Names above are proposed names. `candidate_size` is the number of physical keys in each candidate. With `n = candidate_size`, candidate `i` contains the keys in `[i * n, (i + 1) * n)`:

```text
keys = [KDA128.r0, KDA128.r1, KDA256.r0, KDA256.r1]
candidate_size = 2

candidate 0 = [KDA128.r0, KDA128.r1]
candidate 1 = [KDA256.r0, KDA256.r1]
```

For the targeted K3 layouts, each checkpoint requires the same number of keys once the participating components, cache groups, and ranks are fixed. A single `candidate_size` therefore describes the grouping while preserving the existing flat input. The size may differ between requests; variable candidate sizes within one request are outside this proposal's scope.

The caller orders candidates by increasing resume position and places every key required for a candidate contiguously. Missing members must not be omitted, and deduplication across candidates must not change the grouping. Store does not need to understand K3, token positions, tensor layouts, or rank names. These candidate groups exist only for the request; they do not require persistent group registration.

### Policy semantics

For `None`, `candidate_size` is unused and the operation retains the existing probe behavior: no read lease is granted or extended.

For `LastHitOnly`:

1. A candidate is complete only if every member has a readable replica under the existing existence-check rules.
2. Choose the last complete candidate in input order. Gaps between candidates are allowed.
3. Grant read leases to every member of that candidate using the existing default lease TTL.
4. Do not explicitly renew keys outside the selected candidate. If no candidate is complete, grant no leases.

For a nonempty `LastHitOnly` request, `candidate_size` must be positive and divide `keys.size()` exactly. The default value of 1 treats each key as one candidate; K3 callers must provide the full checkpoint's actual key count. Invalid sizes or unknown modes return parameter errors without leasing objects. Empty requests return empty results. Duplicate key positions remain valid; a selected physical object only needs to be leased once.

Under this proposal, `BatchProbeKey` becomes an existence probe with optional, explicit lease selection. `None` remains the default mode in the policy struct. Documentation must make clear that the batch API is lease-free only with `None`; single-key `ProbeKey` remains lease-free.

### Return values

Keep the existing per-key result-vector type, length, and input order. `None` retains its existence-result semantics. For a successful `LastHitOnly` call, return a **selected-only mask**: every position in the selected candidate is `true` after all of its keys have been leased; all other positions are `false`, even if those keys exist.

For the example above:

- `[true, true, false, false]`: candidate 0 was selected and leased; candidate 1 was incomplete when checked.
- `[false, false, true, true]`: candidate 1 was selected and leased, regardless of whether candidate 0 also exists.
- `[false, false, false, false]`: no complete candidate was selected.

Here, `false` means **not selected**, not necessarily missing. The caller divides the mask into groups of `candidate_size` entries and accepts at most one all-`true` group; partially true groups or multiple true groups are invalid. An all-`false` mask means no complete candidate was selected. Errors remain errors and must not be treated as ordinary misses to publish a successful lookup. No additional selected-index field is needed.

### Compatibility and scope

For this iteration, we assume the participating components can be updated together. We propose changing the existing RPC signature directly, without adding a versioned RPC or mixed-version fallback. This is a wire-format change; the default mode does not make it compatible with the previous signature.

`ExistKey`, `BatchExistKey`, and single-key `ProbeKey` retain their existing behavior. The initial scope covers the Store client layers and Python binding, without adding new C, Go, or Rust probe APIs.

## Implementation

The existing lookup path can be reused for an initial scan without leases. `LastHitOnly` then examines complete candidates in reverse order, with a separate result mask initialized to `false`:

1. Acquire the snapshot guard and the selected candidate's metadata shard locks in the established order, acquiring distinct shards in ascending order.
2. Recheck every member while those locks are held.
3. If any member is no longer readable, leave that candidate's mask entries `false`, release the locks, and try an earlier candidate.
4. If all members are readable, grant their leases and mark only that candidate's positions `true` before releasing the locks, then return the mask.

No member should be leased until the entire candidate passes validation. This prevents a candidate that became incomplete between the scan and selection from receiving partial leases during this operation. Unselected candidates keep all-`false` mask entries, regardless of their existence.

Only the candidate being validated needs its relevant shards locked together. A single RPC is not, by itself, sufficient to prevent eviction between checking different shards. The implementation must also avoid reentering helpers that acquire a shard lock already held by the caller.

The mask identifies the protected candidate, not a snapshot of all keys' existence at one instant. A candidate initially observed as incomplete may be discovered on a later request if a concurrent write completes it. Initial lookup errors must be returned without acquiring leases.

The policy must be passed through `WrappedMasterService`, `MasterClient`, `Client`, `RealClient`, `DummyClient`, and the Python binding. Both the Master RPC registration and the production DummyClient-to-RealClient RPC path need coverage.

## Inference engine integration

The observations below are based on vLLM [`601e1c7`](https://github.com/vllm-project/vllm/tree/601e1c7c51a10d6fd884d39f079f38bb942e436f) and SGLang [`5c69e32`](https://github.com/sgl-project/sglang/tree/5c69e32abe013fa1b913022682a3104c79105f37). The Store policy supplies selection and leasing; the engines still own KV/KDA pairing and the final resume boundary.

### vLLM

The native `MooncakeStoreConnector` currently queries KV and KDA together in one `batch_is_exist` call, then uses its coordinator to determine the reusable boundary. Its Mamba path requires `align` mode. Lookup already expands the required rank namespaces and checks their completeness. See [the lookup implementation](https://github.com/vllm-project/vllm/blob/601e1c7c51a10d6fd884d39f079f38bb942e436f/vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py#L2170).

The target integration is:

1. Separate KV and KDA lookup in the connector. Query and lease KV first.
2. Reuse the coordinator's matching rules to construct valid KDA candidate boundaries. Account for final-token recomputation, Eagle, alignment, and partial-hash/tail-key mapping before selective leasing.
3. Group all required KDA cache-group and rank keys for each candidate, then call `BatchProbeKey(LastHitOnly)`. Reorder the current group → hash → namespace list into checkpoint → group → namespace order. For the fixed set of participating KDA groups, `candidate_size` is the sum of their required namespace counts; adding a size argument to the unchanged list would not be sufficient.
4. Publish the selected boundary only after confirming that it is the boundary the load path will use. Preserve the existing `MooncakeLookupResult` and scheduler interface.

These changes can remain within the connector implementation, primarily `store/worker.py` and `coordinator.py`, for its currently supported K3 configurations. They do not require K3 model or core scheduler changes.

Both paths typically use two Store lookup RPCs, compared with the current single mixed query. The expected benefit is less unnecessary KDA retention, not a guaranteed reduction in lookup latency.

### SGLang

SGLang's K3 HiCache path already queries KV and KDA separately. However, its KDA query currently expands the full input hash chain and only applies the KV boundary when interpreting results. A local K3 checkpoint contains both temporal and convolution-state objects. See [`batch_exists_v2`](https://github.com/sgl-project/sglang/blob/5c69e32abe013fa1b913022682a3104c79105f37/python/sglang/srt/mem_cache/storage/mooncake_store/mooncake_store.py#L857).

For a single rank and stage, the integration is straightforward:

1. Keep the existing KV existence query and lease acquisition.
2. Trim KDA candidates to the usable KV boundary before expanding their physical keys.
3. Reuse the existing page → component key order and set `candidate_size` from the key builder's `key_multiplier` (currently 2 for a local K3 checkpoint). Apply `LastHitOnly` and use the same selected boundary for loading.

Distributed lookup also needs a common complete boundary across all required ranks and stages. Taking the minimum of local maxima is insufficient for sparse checkpoints: `{128, 384}` and `{128, 256}` have a common maximum of 128, not 256. The reviewed [controller path](https://github.com/sgl-project/sglang/blob/5c69e32abe013fa1b913022682a3104c79105f37/python/sglang/srt/mem_cache/hybrid_cache/hybrid_cache_controller.py#L1036) currently passes on the maximum length, so this coordination must be addressed during integration.

The work belongs in the Mooncake storage backend and HiCache controller, including ordinary prefetch and PP ticket coordination. The final trailing key must refer to the protected checkpoint. Shared helpers such as `_batch_exist` must not be changed globally because they also serve write-side deduplication. Other required side pools must constrain the candidates before final selection.

## Validation

The implementation should cover:

- `None` preserving lease deadlines, including objects with shared leases.
- Sparse candidates, missing components or rank shards, duplicate keys, empty requests, zero candidate sizes, non-divisible key counts, invalid policies, and tenant isolation. Cover size 1 and different sizes across requests as well.
- Every selected member receiving a lease, with independent leases of unselected objects unchanged. Verify selected-only masks even when multiple candidates are complete, and an all-`false` mask when none is selected.
- Eviction between the initial scan and candidate validation, including fallback to an earlier candidate and consistency between returned results and leased keys.
- Concurrent selection and eviction across shards, plus both direct and DummyClient RPC paths and Python bindings.
- vLLM's final-boundary constraints and SGLang's component completeness and TP/PP coordination, including loading exactly the protected checkpoint.

Performance evaluation should measure lookup RPC count and latency, lock hold time, KDA objects/bytes whose leases are renewed, and cache behavior under pressure. This RFC does not claim an end-to-end performance improvement before those measurements.

## Future work

`LongestPrefix` and `LongestPrefixLastOnly`, suggested by @staryxchen in the earlier discussion #3801 , can be considered when another workload needs consecutive-prefix selection. They are not required to address the current K3 use case and are outside this implementation's scope. We do not propose adding their enum values, configuration, or a general policy framework in advance.


### Before submitting a new issue...

- [ ] Make sure you already searched for relevant issues and read the [documentation](https://kvcache-ai.github.io/Mooncake/)

## 评论 (1)

### github-actions[bot] · 2026-09-21

Thanks for opening this issue, @yokinoshitayoki!

| Field | Value |
|-------|-------|
| **Issue** | #4255 |
| **GitHub user ID** | `113957881` |
| **Reporter** | @yokinoshitayoki |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.
