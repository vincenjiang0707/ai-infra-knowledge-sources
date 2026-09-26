# [Issue #2351] [Question]: What is the actual boundary on CUDA graph capture with NCCL checkpoint shim?

source: https://github.com/NVIDIA/nccl/issues/2351
state: closed | updated: 2026-08-19T13:42:58Z
labels: question

## 正文

### Question

The [NCCL Checkpoint Shim](https://github.com/NVIDIA/nccl/tree/master/contrib/nccl_checkpoint) lists "CUDA graph capture is not supported" under Limitations. The reasoning is sound: a captured graph bakes kernel arguments in as literal addresses, and the shim destroys and rebuilds each communicator rather than suspending it in place.

However, I was testing with vllm `--enforce-eager removed` and it did not fail:
- CUDA graphs are captured
- ncclCheckpointRestore() success on all 8 ranks
- vllm restored and comes back live, no graph related errors
- Prompt response is coherent
- Comparison with `--enforce-eager added`, prompt response from both restored pods are byte-identical

Environment: NCCL 2.30.7-1, CUDA driver 580.126.20, 8× L4 (PCIe, no NVLink), TP=8, vLLM 0.19.1

**Our hypothesis**: address-reuse determinism. The restored process re-creates NCCL's buffers through the same allocation sequence, so they land at the same addresses and the frozen kernel arguments stay valid. That is a property of this configuration, not a guarantee.

**Questions**: 
- Is that the mechanism, and under what conditions does it stop holding? The limitation is stated with no conditions and no reason given — so it may be wider than the real constraint. One passing configuration cannot tell us whether we are inside the envelope or merely lucky.
-  What would a violation of this limitation look like? We don't know if we would get a crash, a hang, or quietly wrong tokens so we cannot write a check that would catch one.


## 评论 (1)

### lrbison · 2026-08-18

I believe your hypothesis of why this happens is correct, but I have not attempted to enumerate the various reasons where this assumption could break.  My primary worry would be the use of any communicators in non-blocking mode that would cause separate threads to race towards memory re-allocation in restore.

I've been asked if this is something to leverage, but I don't encourage it.  I expect attempting to replay invalid graph capture would most likely cause a hang or invalid memory access (IMA).
