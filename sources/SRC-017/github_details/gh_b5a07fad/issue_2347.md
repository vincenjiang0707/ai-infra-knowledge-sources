# [Issue #2347] [Issue]: NCCL Checkpoint - allocInitParams() reads past the end of a caller-supplied ncclConfig_t (with version skew)

source: https://github.com/NVIDIA/nccl/issues/2347
state: closed | updated: 2026-08-31T14:14:22Z
labels: 

## 正文

### How is this issue impacting you?

Application crash

### Share Your Debug Logs

### Version

- NCCL Checkpoint Shim version: NCCL v2.30.7-1, [contrib/nccl_checkpoint/shim.cc](https://github.com/NVIDIA/nccl/blob/7b83616df3ae082a1f32bb74c27458bfe8153a13/contrib/nccl_checkpoint/shim.cc)
- vllm built with NCCL version 2.27.5

### Description

allocInitParams() copies a caller-supplied ncclConfig_t with a whole-struct assignment and then stamps the current size/magic/version onto the result.

ncclConfig_t is size-prefixed so that a caller compiled against an older nccl.h may pass a shorter struct; parseCommConfig() honours that by reading size. The shim does not. Two consequences:

1. **Out-of-bounds read.** *configPtr copies sizeof(ncclConfig_t) bytes from an object the caller allocated smaller. This is a read past the end of a live object, reachable from any application built against a pre-2.30 header.
2. **The garbage is then validated.** Because size is rewritten to the current release's value, parseCommConfig() validates fields that the caller never initialized.

### Reproduction
Any PyTorch- or vLLM-based application; both ship against nvidia-nccl-cu12 2.27.5, which predates the six config fields added in 2.30 (nChannelsPerNetPeer, nvlinkCentricSched, graphUsageMode, numRmaCtx, maxP2pPeers, graphStreamOrdering). Take a checkpoint and restore:

```
init.cc:2371 (parseCommConfig) NCCL WARN Invalid config nChannelsPerNetPeer attribute value 0
NCCL Checkpoint: shim_checkpoint.cc:140 (restoreCommViaInit) -> 4

ncclCheckpointRestore() returns ncclInvalidArgument on every rank. Observed on 8 × L4, TP=8, vLLM, NCCL v2.30.7-1.
```

### Proposed Fix
Initialize from NCCL_CONFIG_INITIALIZER and memcpy only min(configPtr->size, sizeof(ncclConfig_t)) bytes over it, so fields the caller does not own retain their NCCL_CONFIG_UNDEF_INT sentinel and parseCommConfig() skips them. Read netName/commName from the local copy rather than configPtr to avoid the same overread on that path.

### Your platform details

- 8 x L4 GPU, testing multi GPU, single host checkpoint / restore. 


## 评论 (4)

### lrbison · 2026-08-18

Good find.  Thank you.  Do you have a PR already?

### nicolexin · 2026-08-18

Just uploaded a PR, PTAL :)

### lrbison · 2026-08-24

Thanks for the PR.  I'm testing it internally along with a few other small fixes.

### lrbison · 2026-08-31

Took your commit as https://github.com/NVIDIA/nccl/commit/8c764e4667b0236d7625ddce45ce4bf29fc1ae6f

Thank you!
