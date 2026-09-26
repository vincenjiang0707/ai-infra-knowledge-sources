# [Issue #410] [RFC] Chunk-ready symmetric-buffer protocol for streaming MegaMoE inputs

source: https://github.com/deepseek-ai/DeepGEMM/issues/410
state: open | updated: 2026-08-24T03:41:53Z
labels: 

## 正文

## Summary

I would like to discuss an opt-in, chunk-ready producer/consumer protocol for MegaMoE's symmetric input buffer.

Today the caller fills the full `x`, `x_sf`, `topk_idx`, and `topk_weights` ranges before calling `fp8_fp4_mega_moe`. The mega-kernel overlaps dispatch, expert compute, and combine internally, but this whole-batch handoff prevents the router/TopK/input-layout producers from overlapping with dispatch of earlier token chunks.

The proposed direction is a fixed-capacity ring of token chunks. Producers publish routing and activation-layout readiness with generation counters; MegaMoE consumes ready chunks and publishes safe reuse. This is an RFC rather than a performance claim: the protocol, progress guarantees, and incremental expert scheduling need agreement before implementation.

## Motivation

The current public flow is effectively:

```text
Router/TopK + input layout (all tokens)
                    |
                    v
MegaMoE dispatch -> L1 -> activation -> L2 -> combine
```

The desired overlap is within one MoE layer, across token chunks:

```text
produce chunk n+1     produce chunk n
        |                    |
        +--------------------+--> dispatch/compute/combine chunk n-1
```

`chunk` here means a token micro-batch within the same MoE invocation, not a transformer layer. This proposal does not try to pipeline across layer dependencies.

The current SM100 dispatch path also performs whole-invocation expert counting, a grid sync, and a cross-rank barrier before pulling token data. Therefore this cannot be implemented correctly by adding one `ready` flag around the existing kernel. It requires an explicit chunk-aware counting/scheduling contract.

## Proposed protocol

This is a non-binding sketch intended to make the correctness questions concrete.

### Fixed-capacity ring

Allocate the front-end staging area statically with:

- `num_slots`
- `tokens_per_slot`
- payload views for `x`, `x_sf`, `topk_idx`, and `topk_weights`
- per-source-rank, per-slot metadata
- a logical token base and valid-token count for the final partial chunk

All allocation and shapes remain fixed so the path can be captured and replayed by CUDA Graphs. There should be no allocation or shape-dependent host work during replay.

### Independent readiness generations

Routing and activation layout can finish in either order, so a single ordered enum is awkward. For source rank `r`, slot `s`, and expected generation `g`, use independent monotonic generations:

```text
route_ready_gen[r][s]  == g  // topk_idx/topk_weights are published
layout_ready_gen[r][s] == g  // x/x_sf are published
consumed_gen[r][s]     == g  // the slot can be reused
```

The consumer may read a slot only after both ready generations match `g`. The producer may reuse it for `g + ring_size` only after the required consumer acknowledgements are complete.

An `(epoch, sequence)` value, or a sufficiently wide monotonic sequence, should prevent ABA across ring wrap and CUDA Graph replay.

### Memory ordering

For each ready generation:

1. Producer writes the slot payload.
2. Producer publishes the generation with system-scope release semantics.
3. A remote consumer observes the generation with system-scope acquire semantics before reading the payload.

Slot reuse needs the reverse handoff: consumers finish all reads, publish completion with release semantics, and the owner observes completion with acquire semantics before overwriting the slot.

For the first implementation, reuse could conservatively wait until the chunk's combine is complete. If the kernel can prove that no slot-resident payload or metadata is referenced after all remote pulls, an earlier `input_consumed` acknowledgement could be a later optimization.

Because a source chunk may feed several destination ranks, `consumed_gen` probably needs either per-rank acknowledgements or a collective/bitmask completion rule. The exact primitive should reuse DeepGEMM's existing NVLink barrier and acquire/release conventions where possible.

### Chunk-aware dispatch scheduling

The dispatch side needs to replace the whole-invocation count/sync barrier with one of these (or another maintainer-preferred design):

1. Chunk-local expert pools, optionally padding the last partial expert block in each chunk.
2. Incremental per-expert reservations across chunks, plus an end-of-stream seal for partial blocks.

The second option may preserve packing efficiency, but it needs a precise rule for when an expert block is complete and may be consumed by L1. In both cases, source metadata must include the logical token index so combine writes back to the original output position.

Consumers can initially wait for all source ranks' routing/layout readiness for generation `g`. Processing source ranks independently could be a later optimization; it should not be required by the first protocol.

## Progress and deadlock requirements

A persistent consumer must not occupy all SM resources while spinning on data that can only be produced by kernels that have not run yet. A streamed path therefore needs an explicit progress mechanism, for example:

- launch ordering/PDL that guarantees producer progress before consumer waits,
- an SM reservation or green-context split, or
- another scheduling rule that maintainers consider safe.

Correctness must not depend on overlap actually occurring. Serialized execution should remain valid, and a slow or empty source rank must not deadlock other ranks.

## API direction

I suggest keeping the current batch-ready API unchanged and adding an opt-in streamed mode. Conceptually:

```python
buffer = get_symm_buffer_for_mega_moe(
    ...,
    front_num_slots=S,
    front_tokens_per_slot=C,
)

# Producer kernels write a slot and publish route/layout generations.
# One MegaMoE invocation consumes the known number of logical chunks.
fp8_fp4_mega_moe(..., buffer, streaming=True, stream_epoch=epoch)
```

The actual publish operations should be device-side; the Python sketch only shows allocation and invocation. A device-visible descriptor could carry slot strides, metadata pointers, expected generation, total tokens, and the number of valid chunks.

The existing full-batch path should remain the default and a correctness fallback.

## Suggested implementation slices

1. Define/allocate the fixed ring metadata and document the release/acquire protocol; add single-rank protocol tests without changing the default kernel.
2. Add a correctness-first streamed dispatch path with chunk-local scheduling and the current output layout.
3. Add multi-rank acknowledgements, uneven/zero-token cases, and NVLink ordering stress tests.
4. Integrate a producer (router/TopK/layout) and tune chunk size, slot count, and progress policy on SM100/NVSwitch systems.

These should be separate PRs rather than one large change.

## Validation plan

- Compare streamed and current batch-ready outputs across token counts, TopK values, expert distributions, and partial chunks.
- Cover one rank and multi-rank runs, uneven tokens per rank, zero-token chunks, repeated ring wrap, and repeated CUDA Graph replay.
- Stress delayed producers/consumers to expose missing ordering or premature reuse.
- Profile on B200/NVSwitch to verify that router/TopK/layout work actually overlaps with dispatch and that spinning does not reduce throughput.
- Treat performance as successful only when end-to-end MoE latency improves; kernel-only timing is insufficient.

I do not have a B200/NVSwitch performance result for this protocol yet; this RFC is meant to agree on the interface and correctness model first.

## Non-goals

- Fusing the router or TopK implementation into DeepGEMM.
- Changing expert placement/EPLB semantics.
- Replacing the current batch-ready API.
- Claiming cross-layer pipeline overlap.
- Requiring the split-kernel implementation.

## Related work

- #357 splits MegaMoE's internal K1/K2/combine pipeline while keeping the external full-batch input contract. This RFC is about the producer-to-dispatch handoff and could be independent of either fused or split internals.
- #389 fixes a shared-memory async-proxy reuse hazard inside combine. It is a different scope, but it reinforces the need to specify ordering before any ring slot is reused.
- #338 and #370 discuss adjacent activation/layout interoperability concerns; the proposed protocol should not hard-code one producer implementation.

## Questions for maintainers

1. Should this protocol live in `SymmBuffer`, or should the caller own the ring metadata and pass a descriptor to MegaMoE?
2. Are independent `route_ready_gen` and `layout_ready_gen` counters a reasonable contract, or would one combined publish point be preferable?
3. For incremental dispatch, do you prefer chunk-local padded expert blocks or cross-chunk reservations with an end-of-stream seal?
4. What progress mechanism is acceptable for a consumer launched before all chunks are ready: PDL, reserved SMs/green contexts, or another approach?
5. Would a single-rank, correctness-only protocol/allocation PR be a useful first slice before B200 multi-rank optimization?

If the direction is acceptable, I can start with the protocol/allocation slice and keep the existing path untouched.


## 评论 (1)

### 200lz · 2026-08-24

I’m interested in working on the correctness side of the first slice. Rather than changing the MegaMoE dispatch path initially, I’d like to prototype/test the ring generation state machine, including repeated wraparound, independent route/layout publication order, delayed consumers, and CUDA Graph replay. This could either become part of the protocol/allocation PR or a separate test-focused PR. I’ll keep the existing batch-ready path untouched.
