# [Issue #2348] [Issue]: NCCL Checkpoint - getHostHash() is cached across checkpoint/restore; restored communicators use a stale host identity

source: https://github.com/NVIDIA/nccl/issues/2348
state: open | updated: 2026-08-23T20:31:38Z
labels: 

## 正文

### How is this issue impacting you?

Data corruption

### Description
getHostHash() ([src/misc/utils.cc:155](https://github.com/NVIDIA/nccl/blob/7b83616df3ae082a1f32bb74c27458bfe8153a13/src/misc/utils.cc#L155)) memoizes via std::call_once into a file-static. getHostHashOnce() hashes gethostname() + /proc/sys/kernel/random/boot_id. Both run at first NCCL init, before any checkpoint.

When a process image is checkpointed and restored — on a different physical host — the once_flag comes back already set. The hash is never recomputed. Communicators rebuilt by ncclCheckpointRestore() consume the stale value at init.cc:717. Nothing in contrib/nccl_checkpoint/ references hostHash, NCCL_HOSTID or boot_id.

Since the shim's contract is that it rebuilds communicators from scratch, and host identity is exactly the state that cannot survive relocation, we read this as a restore-path defect.

### Observation
8 × L4, TP=8, vLLM. A second-generation restore onto a different node emits its restore-time NCCL logs stamped with the original pod's name, 16 times, and its own zero times.

### Impact
- **Single-pod restore is benign**: all ranks share the same stale hash and are in fact co-located. 
- **Multi-pod is not**: Two pods restored from a common snapshot hold a byte-identical cached hash copied from one memory image, so NCCL would classify ranks on different physical machines as node-local and select SHM/P2P for them. This blocks prefill/decode disaggregation and pipeline parallelism on top of snapshots.

### Suggested fix
Reset the once_flag and recompute the host hash inside ncclCheckpointRestore(), before any communicator is rebuilt.

### NCCL Version

NCCL v2.30.7-1


## 评论 (3)

### lrbison · 2026-08-18

Thank you for the report.

Do I understand correctly that the communicators that were part of the checkpoint and are restored are still functional, but if you try to create a new multi-host communicator after restore and both pods were restored from the same image, then NCCL incorrectly believes SHM is a valid transport when it isn't.

### nicolexin · 2026-08-19

Thanks for the reply! 

And you are right to question this (I haven't really tested multi-host checkpoint/restore) - the collision needs two processes restored from the same snapshot. Since we snapshot per pod, a multi-pod communicator has each member snapshotted separately, and each restores with its own distinct frozen hash - they would still classify each other as being on remote nodes correctly.

The only way to get a shared stale value is one snapshot restored into N pods, but those are independent replicas anyway. They should never form a communicator with each other.

That's actually left is just the value is not accurate after restoration, I will leave this up to you to evaluate whether we need a fix or not. Since I don't have a real use cases here, feel free to close it!


### lrbison · 2026-08-19

I see.  I do still think there is an issue here, even if it doesn't affect the checkpoint operation, it can affect any new communicators created between the (identical) pods after checkpoint restore.   Leaving this issue as open for now, with the understanding that it should be closed in subsequent checkpoint feature updates.
