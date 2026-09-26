# [Issue #2327] [Question]:  Why NCCL_ALGO_NVLS only support NCCL_PROTO_SIMPLE, no NCCL_PROTO_LL/NCCL_PROTO_LL128?

source: https://github.com/NVIDIA/nccl/issues/2327
state: open | updated: 2026-08-17T13:18:38Z
labels: question

## 正文

### Question

In [this issue](https://github.com/NVIDIA/nccl/issues/1506), you mentioned that LL/LL128 relies on the flags being part of the data. When SHARP technologies are used, the flags would be reduced along with the rest of the data, which would break the protocol. I would like to know why this violates the protocol.
I have a question:  Even though SHARP’s reduction operation sums up the LL flags as part of the aggregation process, could the corresponding flag validation logic be adapted to check against this aggregated summed value instead?
For example, consider an allreduce operation across a communicator consisting of 8 ranks running under the LL protocol. Each rank initializes its local flag to 1. After SHARP aggregates these flags via summation across all 8 ranks, the aggregated flag value becomes 8. Would it be valid to modify the completion check to verify whether the aggregated flag equals 8 instead of 1 in this scenario?

## 评论 (4)

### sjeaugey · 2026-08-07

Yes indeed, there could be cases where we could use it in the context of LL* protocols.

However, flags are encoded as 32 or 64 bits, so while it could be ~easy to implement it on 32 bits integer for LL and 64 bits integer for LL128, for other datatypes, it would not work. We cannot change the format from int to float between every operation and the flags are shared for all datatypes.

On top of that, LL/LL128 help a lot with pipelining intra-node, but with NVLS, there is a single step intra-node, so we're not gaining much. The only gain would be on the networking side, and for that, a better approach would probably be to be able to decouple the protocol at different steps, combine NVLS/Simple intra-node with Tree or Ring/LL* inter-node.

### carpediem0309 · 2026-08-17

Thank you for your answer, but I still have a question. Why can't the flag be the same data type as the data? For example, the LL format could become `float data1, float flag1, float data2, float flag2`. In the NVLS+LL receive flow, I would expect the received flag to already be the reduced result across all ranks. Using the example from my first question: if each rank's flag is initialized to a `float` value of 1, then I would expect the flag after the NVLS reduce-sum operation to become a `float` value of 8. Is there any problem with this?

### sjeaugey · 2026-08-17

What if NCCL is called alternatively with different datatypes (e.g. float32 and float16)?

Since we reuse the same buffer for all datatypes, we need a constant type.

### carpediem0309 · 2026-08-17

If the data type is fp16, the LL data format could become `fp16 data1, fp16 data2, fp16 flag1, fp16 flag2, fp16 data3, fp16 data4, fp16 flag3, fp16 flag4`, in which case we would need to check that flag1, flag2, flag3, and flag4 all equal the expected values. What I'm trying to say is: if the LL struct changes according to the data type of the data, would this make SHARP+LL work?
