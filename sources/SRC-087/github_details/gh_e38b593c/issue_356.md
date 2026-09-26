# [Issue #356] [RFC]: Add Multi-node Training Suppor

source: https://github.com/vllm-project/speculators/issues/356
state: closed | updated: 2026-08-14T17:41:39Z
labels: stale, RFC

## 正文

### Motivation.

# RFC: Multi-node Training Support for Speculators

## Introduction

This RFC proposes the addition of multi-node training support . The changes aim to enable efficient distributed training across multiple nodes, allowing the project to scale to larger models and datasets.

## Motivation

As the Speculators project continues to evolve, there is a growing need to support training on multi-node clusters. Single-node training with multiple GPUs has limitations in terms of memory and computational capacity, especially for larger models. Multi-node training enables:

- Scaling to larger model sizes beyond the memory capacity of a single node
- Faster training times by distributing the workload across multiple nodes
- Access to more computational resources for experiments and production deployments


### Proposed Change.

### Multi-node Training Parameters

Add new parameters to `scripts/gen_and_train.py` to support multi-node training:

| Parameter       | Description                  | Default Value         |
|-----------------|------------------------------|-----------------------|
| `nproc_per_node`| Number of processes per node | `torch.accelerator.device_count()` |
| `nnodes`        | Total number of nodes        | 1                     |
| `node_rank`     | Rank of the current node     | 0                     |
| `master_addr`   | IP address of the master node| None                  |
| `master_port`   | Port of the master node      | 12345                 |

### Rank Parameter Correction

- Correct the usage of `local_rank` to `rank` in `scripts/train.py` for the `setup_dataloader` function
- Update `MultipackDistributedBatchSamplerV2` calls to use global rank instead of local rank for proper data sharding
- Fix documentation in `src/speculators/train/distributed_batch_sampler.py` to clarify the use of global rank

### Command Execution Optimization

- Enhance `build_torchrun_command` to handle unset parameters gracefully
- Implement logic to automatically select the appropriate command format based on the number of nodes:
  - Single-node training: `torchrun --standalone --nproc_per_node={device_count}`
  - Multi-node training: Full torchrun command with all distributed parameters

### Documentation Updates

- Add detailed documentation for multi-node training parameters in `scripts/README.md`
- Include multi-node training startup examples
- Add documentation for scheduler-related parameters

## Testing

### Single-node Training

```bash
torchrun --standalone --nproc_per_node=4 scripts/train.py
```

### Multi-node Training

```bash
# Node 0
torchrun --nnodes=2 --nproc_per_node=4 --node_rank=0 --master_addr=192.168.1.100 --master_port=12345 scripts/train.py

# Node 1
torchrun --nnodes=2 --nproc_per_node=4 --node_rank=1 --master_addr=192.168.1.100 --master_port=12345 scripts/train.py
```

## Related Work


- [x]  add multi-node support for training:  https://github.com/vllm-project/speculators/pull/299
- [ ] add multi-node device-mesh for fully shard execution

## 评论 (5)

### fynnsu · 2026-03-23

Yes, I think this would be good to add and the changes seem relatively minimal.
It would probably also be good to set a device `mesh` (see [fully_shard docs](https://docs.pytorch.org/docs/stable/distributed.fsdp.fully_shard.html#pytorch-fsdp2-fully-shard)) so that we either do hybrid sharding (fully shard within node, replicate across nodes) or even no sharding (fully replicate on every rank) since drafters are small. 

I would also like to your thoughts on if local_rank0 on non-zero nodes is treated specially for anything? I think it's probably safe to only have node0 local_rank0 (i.e. rank0 overall) do logging and checkpointing and have every other rank only do training, but just want to confirm. Is there anything we need to be running on every node?



### Liccol · 2026-03-25

> Yes, I think this would be good to add and the changes seem relatively minimal. It would probably also be good to set a device `mesh` (see [fully_shard docs](https://docs.pytorch.org/docs/stable/distributed.fsdp.fully_shard.html#pytorch-fsdp2-fully-shard)) so that we either do hybrid sharding (fully shard within node, replicate across nodes) or even no sharding (fully replicate on every rank) since drafters are small.
> 
> I would also like to your thoughts on if local_rank0 on non-zero nodes is treated specially for anything? I think it's probably safe to only have node0 local_rank0 (i.e. rank0 overall) do logging and checkpointing and have every other rank only do training, but just want to confirm. Is there anything we need to be running on every node?

Yes, good idea! I've added the fully shard related work to the related work section. Maybe we can merge PR #299 first, and submit a new PR after verifying the fully shard modifications.
As for local_rank0, logging should be handled on node0+local_rank0 to avoid misleading. Nothing else needs to be specifically handled on node0 local_rank0 as I can see.

### ianliuy · 2026-04-15

## Analysis: `local_rank` vs global `rank` bug in multi-node training

### What's broken?

In multi-node distributed training, data sharding is incorrect: processes on different nodes with the same `local_rank` receive **identical data shards**, causing data duplication and wasted compute. Additionally, tqdm progress bars appear on multiple nodes instead of just one.

### Who is affected?

Anyone running multi-node training (i.e. `nnodes > 1`). Single-node training is unaffected because `local_rank == rank` when there's only one node.

### When does it trigger?

Always, when `nnodes > 1`. For example, in a 2-node × 4-GPU setup:
- Node 0, GPU 0: `local_rank=0, rank=0` → gets shard 0
- Node 1, GPU 0: `local_rank=0, rank=4` → **also gets shard 0** (should get shard 4)

### Where is the bug?

1. **`scripts/train.py`**: `setup_dataloader()` accepts `local_rank` (line 58) and passes it as `rank=local_rank` to `MultipackDistributedBatchSamplerV2` (line 79). Call sites (lines 298, 306) pass `local_rank` instead of global `rank`.

2. **`src/speculators/train/trainer.py`**: `train_epoch()` and `val_epoch()` guard tqdm with `self.local_rank == 0` (lines 234, 277), showing progress bars on every node's GPU 0.

### Why does it happen?

The training infrastructure was originally built for single-node in PR #143, where `local_rank == rank`. The `local_rank` variable was used throughout without distinguishing it from global rank. When multi-node support is needed, this assumption breaks.

### How to fix?

- Change `setup_dataloader()` to accept and pass global `rank` instead of `local_rank`
- Add `self.rank` to the Trainer and use it for tqdm guards
- Update distributed setup logging to include global rank

This is a rebased version of the fix from #299 by @Liccol, which has been stale with merge conflicts. All review feedback from @fynnsu on that PR has been incorporated.

### Testing

Will be filled after implementation.

---

I'm working on a fix.


### github-actions[bot] · 2026-07-14

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!

### github-actions[bot] · 2026-08-14

This issue has been automatically closed due to inactivity. Please feel free to reopen if you feel it is still relevant. Thank you!
