# [Issue #2302] [Question/RFE] Cross-context ordering before a single GIN signal

source: https://github.com/NVIDIA/nccl/issues/2302
state: closed | updated: 2026-07-28T16:02:32Z
labels: question

## 正文

### Question

# [Question/RFE] Cross-context ordering before a single GIN signal

## Summary

Is there an NCCL GIN operation equivalent to `nvshmem_fence()` for establishing ordering across multiple GIN contexts before sending a single signal to one peer?

My use case has multiple GPU CTAs issuing puts to the same target peer. I would like to distribute those puts across multiple GIN contexts for better parallelism, and then send one ready signal after all puts have been issued.

With NVSHMEM, the publication pattern is:

```cpp
// Multiple CTAs issue puts to the same target PE.

// Application-level rendezvous:
// all CTAs have issued their puts.

if (is_last_cta) {
    nvshmem_fence();
    nvshmem_signal_op(
        remote_ready,
        1,
        NVSHMEM_SIGNAL_SET,
        target_pe
    );
}
```

My understanding is that `nvshmem_fence()` orders all earlier operations to the target PE before the subsequent signal, without requiring full remote completion.

## GIN version of the use case

The GIN kernel is conceptually similar to this:

```cpp
int context_index = blockIdx.x % num_contexts;
ncclGin gin{dev_comm, context_index};

gin.put(
    team,
    target_peer,
    dst_window,
    dst_offset,
    src_window,
    src_offset,
    bytes
);

// Application-level rendezvous:
// all producer CTAs have issued their puts.

if (is_last_cta) {
    ncclGin signal_gin{dev_comm, signal_context};

    signal_gin.signal(
        team,
        target_peer,
        ncclGin_StrongSignalInc{ready_signal}
    );
}
```

However, according to the documented semantics, a strong signal only orders preceding puts to the same peer on the same GIN context.

Therefore, if data is distributed across several contexts, a signal on one context does not appear to order puts submitted through the other contexts.

For example:

```text
Context 0:
    put A ----------------------> complete
                    strong signal -----> ready visible

Context 1:
    put B --------------------------------------> complete

Target:
                    observes ready
                    may read B too early
```

There is no ordering violation within either context. The missing relationship is between the signal on context 0 and the put on context 1.

## Current workaround

My safest workaround is to send all puts and the signal for a given target peer through one GIN context.

This preserves the required same-context ordering, but it also means that approximately 32 producer CTAs may contend on one context and, depending on the backend, possibly one QP per peer.

A per-context fan-in protocol is another possible solution, where every used context sends its own strong signal and the target waits for all contributions. However, that changes the synchronization protocol and adds additional signal state and traffic.

## Questions

1. Is there an existing one-sided GIN primitive that orders puts across multiple contexts before one subsequent signal to the same peer?

   Conceptually, I need:

   ```text
   puts on contexts 0..N to peer P
       happen-before
   one signal to peer P
   ```

   I only need delivery ordering. I do not need a full quiet operation or remote completion before the signal is submitted.

2. Can `ncclGinAllContexts()` be used for this purpose outside a GIN barrier?

   I found all-context fencing support associated with GIN barriers, but a collective barrier does not fit this one-sided producer-to-consumer notification pattern.

3. Does a strong signal cover all preceding puts submitted on the same context by different CTAs, provided that the application establishes a correct device-level rendezvous before submitting the signal?

4. Is using one strong signal per context and performing fan-in at the target the intended solution for this pattern?

5. If no cross-context fence currently exists, would NCCL consider exposing an operation similar to:

   ```cpp
   gin.fence(target_peer, all_contexts);
   signal_gin.signal(team, target_peer, strong_signal);
   ```

   The desired scope is:

   - one source rank;
   - one target peer;
   - all or a selected set of GIN contexts;
   - ordering only;
   - no participation from the target peer.

6. If using a single context is the recommended solution, is one GIN context guaranteed to provide one ordering domain per peer across all GIN backends? Are there performance recommendations for approximately 32 producer CTAs sharing that context?

## Environment

- NCCL version: 2.30.7
- CUDA version: 13.0
- GPU: H800

## 评论 (3)

### xiaofanl-nvidia · 2026-07-25

++ @kgioioso to take a look. 

### kgioioso · 2026-07-25

Hi @Enigmatisms,

For the most part, GIN contexts are designed to be independent. (Barriers are one exception).

> Is there an existing one-sided GIN primitive that orders puts across multiple contexts before one subsequent signal to the same peer?

No, there is not. We are a bit limited by what is offered by the underlying transport. There are no ordering guarantees across queue pairs. For most GIN backends, each context has one queue pair per peer. Hence, there is no ordering across contexts.

The only way to achieve the semantics you want would be to add an nvshmem-style flush that ensures all operations along all contexts are complete & visible on the other side. But this is very expensive and, as you noted, a stronger guarantee that what your use case needs.

> Does a strong signal cover all preceding puts submitted on the same context by different CTAs, provided that the application establishes a correct device-level rendezvous before submitting the signal?

Yes, per-peer. (As long as you use NCCL_GIN_RESOURCE_SHARING_GPU, which is the default)

> Is using one strong signal per context and performing fan-in at the target the intended solution for this pattern?

My guess is that this would be the best for your use case. But, you may want to do an experiment to compare (1) sharing one context across CTAs and (2) using one context (and one signal) per CTA.

To be honest, most of the use cases I have seen have independent ctas. Each sender-receiver CTA pair can use one context, and there is no need for syncing across CTAs at the sender or the receiver. If you have a use case where this isn't possible, I'd love to learn more. Do you have 32 producer CTAs and 1 consumer CTA?

> If no cross-context fence currently exists, would NCCL consider exposing an operation?

We are always open to adding things provided (1) the use case is semi-repeatable and (2) the performance is reasonable. However, like I said, this is very expensive, we haven't seen a huge need, and most of the time there is a more efficient alternative. 

Happy to hear to more if you feel strongly that this would be useful.

> Is one GIN context guaranteed to provide one ordering domain per peer across all GIN backends? 

In GIN, one context is one ordering domain per peer. All backends must implement these semantics.

### Enigmatisms · 2026-07-28

Thanks for the detailed explanation — it clarified the intended GIN ordering model very well.

Yes, my use case is indeed multiple producer CTAs feeding a single consumer and a single ready point. For now, I plan to keep all puts and the final strong signal for a given peer within one shared GIN context/order domain. I am not planning to implement the multi-context signal fan-out and target-side fan-in scheme—where each producer or context sends its own signal contribution—at this stage, since it would add protocol complexity and correctness risk.

I do not have any further questions. Thanks again for the clear and helpful guidance!
